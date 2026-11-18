"use client";

import { useEffect, useMemo, useState, useActionState } from "react";
import { useTranslations } from "next-intl";
import { createExamAction, getEligibleCountAction, type CreateExamState } from "@/actions/exams";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { FilterCheckItem, FilterSection } from "@/components/filter-section";

type Option = { id: string; label: string };

function uniquePreserve(ids: string[]): string[] {
  const seen = new Set<string>();
  const out: string[] = [];
  for (const id of ids) {
    if (seen.has(id)) continue;
    seen.add(id);
    out.push(id);
  }
  return out;
}

function toggleOrdered(prev: string[], id: string): string[] {
  if (prev.includes(id)) return prev.filter((x) => x !== id);
  return [...prev, id];
}

export function CreateExamForm({
  locale,
  subjects,
  papersBySubject,
  chaptersByPaper,
  topicsByChapter,
}: {
  locale: string;
  subjects: Option[];
  papersBySubject: Record<string, Option[]>;
  chaptersByPaper: Record<string, Option[]>;
  topicsByChapter: Record<string, Option[]>;
}) {
  const t = useTranslations("create");
  const [state, formAction, pending] = useActionState<CreateExamState, FormData>(
    createExamAction,
    {},
  );

  const initialSubject = subjects[0]?.id ?? "";
  const initialPapers = papersBySubject[initialSubject] ?? [];
  const initialPaperIds = initialPapers.map((p) => p.id);
  const initialChapters = initialPaperIds.flatMap(
    (pid) => chaptersByPaper[pid] ?? [],
  );
  const initialChapterIds = initialChapters.map((c) => c.id);
  const initialTopicIds = initialChapterIds.flatMap(
    (cid) => (topicsByChapter[cid] ?? []).map((x) => x.id),
  );

  const [selectedSubjects, setSelectedSubjects] = useState<string[]>(
    initialSubject ? [initialSubject] : [],
  );
  const [selectedPapers, setSelectedPapers] = useState<string[]>(initialPaperIds);
  const [selectedChapters, setSelectedChapters] =
    useState<string[]>(initialChapterIds);
  const [selectedTopics, setSelectedTopics] = useState<string[]>(initialTopicIds);
  const [difficulty, setDifficulty] = useState("");
  const [qtype, setQtype] = useState("");
  const [eligible, setEligible] = useState<number | null>(null);

  const [openSubjects, setOpenSubjects] = useState(true);
  const [openPapers, setOpenPapers] = useState(true);
  const [openChapters, setOpenChapters] = useState(false);
  const [openTopics, setOpenTopics] = useState(false);
  const [openChapterGroups, setOpenChapterGroups] = useState<Record<string, boolean>>(
    {},
  );
  const [openTopicGroups, setOpenTopicGroups] = useState<Record<string, boolean>>({});

  const paperSubjectMap = useMemo(() => {
    const map = new Map<string, string>();
    for (const [subjectId, papers] of Object.entries(papersBySubject)) {
      for (const paper of papers) map.set(paper.id, subjectId);
    }
    return map;
  }, [papersBySubject]);

  const chapterPaperMap = useMemo(() => {
    const map = new Map<string, string>();
    for (const [paperId, chapters] of Object.entries(chaptersByPaper)) {
      for (const chapter of chapters) map.set(chapter.id, paperId);
    }
    return map;
  }, [chaptersByPaper]);

  const visiblePapers = useMemo(() => {
    return selectedSubjects.flatMap((sid) =>
      (papersBySubject[sid] ?? []).map((p) => ({
        ...p,
        subjectId: sid,
        subjectLabel: subjects.find((s) => s.id === sid)?.label ?? sid,
      })),
    );
  }, [selectedSubjects, papersBySubject, subjects]);

  const visibleChapters = useMemo(() => {
    return selectedPapers.flatMap((pid) =>
      (chaptersByPaper[pid] ?? []).map((c) => ({
        ...c,
        paperId: pid,
        paperLabel:
          visiblePapers.find((p) => p.id === pid)?.label ??
          Object.values(papersBySubject)
            .flat()
            .find((p) => p.id === pid)?.label ??
          pid,
      })),
    );
  }, [selectedPapers, chaptersByPaper, visiblePapers, papersBySubject]);

  const visibleTopicIds = useMemo(() => {
    return selectedChapters.flatMap((cid) =>
      (topicsByChapter[cid] ?? []).map((topic) => topic.id),
    );
  }, [selectedChapters, topicsByChapter]);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      if (selectedTopics.length === 0) {
        setEligible(0);
        return;
      }
      const count = await getEligibleCountAction({
        topicIds: selectedTopics,
        difficulty,
        qtype,
      });
      if (!cancelled) setEligible(count);
    })();
    return () => {
      cancelled = true;
    };
  }, [selectedTopics, difficulty, qtype]);

  const errorMessage = useMemo(() => {
    if (!state.error) return null;
    if (state.error === "title") return t("errorTitle");
    if (state.error === "topics") return t("errorTopics");
    if (state.error === "count") return t("errorCount");
    if (state.error === "duration") return t("errorDuration");
    if (state.error === "auth") return t("errorAuth");
    if (state.error === "not_enough") {
      return t("errorNotEnough", { count: state.eligibleCount ?? eligible ?? 0 });
    }
    return state.error;
  }, [state, t, eligible]);

  function papersForSubject(subjectId: string): string[] {
    return (papersBySubject[subjectId] ?? []).map((p) => p.id);
  }

  function chaptersForPapers(paperIds: string[]): string[] {
    return paperIds.flatMap((pid) => (chaptersByPaper[pid] ?? []).map((c) => c.id));
  }

  function topicsForChapters(chapterIds: string[]): string[] {
    return chapterIds.flatMap((cid) =>
      (topicsByChapter[cid] ?? []).map((topic) => topic.id),
    );
  }

  function toggleSubject(subjectId: string) {
    const turningOn = !selectedSubjects.includes(subjectId);
    const nextSubjects = toggleOrdered(selectedSubjects, subjectId);
    setSelectedSubjects(nextSubjects);

    if (turningOn) {
      const newPapers = papersForSubject(subjectId);
      const nextPapers = uniquePreserve([...selectedPapers, ...newPapers]);
      const newChapters = chaptersForPapers(newPapers);
      const nextChapters = uniquePreserve([...selectedChapters, ...newChapters]);
      const newTopics = topicsForChapters(newChapters);
      setSelectedPapers(nextPapers);
      setSelectedChapters(nextChapters);
      setSelectedTopics(uniquePreserve([...selectedTopics, ...newTopics]));
      return;
    }

    const removePapers = new Set(papersForSubject(subjectId));
    const nextPapers = selectedPapers.filter((id) => !removePapers.has(id));
    const removeChapters = new Set(chaptersForPapers([...removePapers]));
    const nextChapters = selectedChapters.filter((id) => !removeChapters.has(id));
    const removeTopics = new Set(topicsForChapters([...removeChapters]));
    setSelectedPapers(nextPapers);
    setSelectedChapters(nextChapters);
    setSelectedTopics(selectedTopics.filter((id) => !removeTopics.has(id)));
  }

  function togglePaper(paperId: string) {
    const turningOn = !selectedPapers.includes(paperId);
    const subjectId = paperSubjectMap.get(paperId);
    if (!subjectId) return;

    if (turningOn && !selectedSubjects.includes(subjectId)) {
      setSelectedSubjects((prev) => [...prev, subjectId]);
    }

    const nextPapers = toggleOrdered(selectedPapers, paperId);
    setSelectedPapers(nextPapers);

    if (turningOn) {
      const newChapters = chaptersForPapers([paperId]);
      const nextChapters = uniquePreserve([...selectedChapters, ...newChapters]);
      const newTopics = topicsForChapters(newChapters);
      setSelectedChapters(nextChapters);
      setSelectedTopics(uniquePreserve([...selectedTopics, ...newTopics]));
      return;
    }

    const removeChapters = new Set(chaptersForPapers([paperId]));
    const nextChapters = selectedChapters.filter((id) => !removeChapters.has(id));
    const removeTopics = new Set(topicsForChapters([...removeChapters]));
    setSelectedChapters(nextChapters);
    setSelectedTopics(selectedTopics.filter((id) => !removeTopics.has(id)));

    const stillHasPaper = nextPapers.some(
      (pid) => paperSubjectMap.get(pid) === subjectId,
    );
    if (!stillHasPaper) {
      setSelectedSubjects((prev) => prev.filter((id) => id !== subjectId));
    }
  }

  function toggleChapter(chapterId: string) {
    const turningOn = !selectedChapters.includes(chapterId);
    const paperId = chapterPaperMap.get(chapterId);
    if (!paperId) return;
    const subjectId = paperSubjectMap.get(paperId);
    if (!subjectId) return;

    if (turningOn) {
      if (!selectedSubjects.includes(subjectId)) {
        setSelectedSubjects((prev) => [...prev, subjectId]);
      }
      if (!selectedPapers.includes(paperId)) {
        setSelectedPapers((prev) => [...prev, paperId]);
      }
    }

    const nextChapters = toggleOrdered(selectedChapters, chapterId);
    setSelectedChapters(nextChapters);

    if (turningOn) {
      const newTopics = topicsForChapters([chapterId]);
      setSelectedTopics(uniquePreserve([...selectedTopics, ...newTopics]));
      return;
    }

    const removeTopics = new Set(topicsForChapters([chapterId]));
    setSelectedTopics(selectedTopics.filter((id) => !removeTopics.has(id)));
  }

  function toggleTopic(topicId: string) {
    setSelectedTopics((prev) =>
      prev.includes(topicId) ? prev.filter((x) => x !== topicId) : [...prev, topicId],
    );
  }

  function selectAllSubjects() {
    const allIds = subjects.map((s) => s.id);
    setSelectedSubjects(allIds);
    const allPapers = allIds.flatMap((sid) => papersForSubject(sid));
    setSelectedPapers(uniquePreserve(allPapers));
    const allChapters = chaptersForPapers(allPapers);
    setSelectedChapters(uniquePreserve(allChapters));
    setSelectedTopics(uniquePreserve(topicsForChapters(allChapters)));
  }

  function deselectAllSubjects() {
    setSelectedSubjects([]);
    setSelectedPapers([]);
    setSelectedChapters([]);
    setSelectedTopics([]);
  }

  function selectAllPapers() {
    const ids = visiblePapers.map((p) => p.id);
    const nextPapers = uniquePreserve([...selectedPapers, ...ids]);
    setSelectedPapers(nextPapers);
    const chapters = chaptersForPapers(ids);
    setSelectedChapters(uniquePreserve([...selectedChapters, ...chapters]));
    setSelectedTopics(
      uniquePreserve([...selectedTopics, ...topicsForChapters(chapters)]),
    );
  }

  function deselectAllPapers() {
    const removePapers = new Set(visiblePapers.map((p) => p.id));
    const nextPapers = selectedPapers.filter((id) => !removePapers.has(id));
    const removeChapters = new Set(chaptersForPapers([...removePapers]));
    const nextChapters = selectedChapters.filter((id) => !removeChapters.has(id));
    const removeTopics = new Set(topicsForChapters([...removeChapters]));
    setSelectedPapers(nextPapers);
    setSelectedChapters(nextChapters);
    setSelectedTopics(selectedTopics.filter((id) => !removeTopics.has(id)));
    setSelectedSubjects((prev) =>
      prev.filter((sid) =>
        nextPapers.some((pid) => paperSubjectMap.get(pid) === sid),
      ),
    );
  }

  function selectAllChaptersForPaper(paperId: string) {
    const chapterIds = chaptersForPapers([paperId]);
    setSelectedChapters(uniquePreserve([...selectedChapters, ...chapterIds]));
    setSelectedTopics(
      uniquePreserve([...selectedTopics, ...topicsForChapters(chapterIds)]),
    );
    if (!selectedPapers.includes(paperId)) {
      setSelectedPapers((prev) => [...prev, paperId]);
    }
  }

  function deselectAllChaptersForPaper(paperId: string) {
    const removeChapters = new Set(chaptersForPapers([paperId]));
    const nextChapters = selectedChapters.filter((id) => !removeChapters.has(id));
    const removeTopics = new Set(topicsForChapters([...removeChapters]));
    setSelectedChapters(nextChapters);
    setSelectedTopics(selectedTopics.filter((id) => !removeTopics.has(id)));
  }

  function selectAllVisibleChapters() {
    const ids = visibleChapters.map((c) => c.id);
    setSelectedChapters(uniquePreserve([...selectedChapters, ...ids]));
    setSelectedTopics(
      uniquePreserve([...selectedTopics, ...topicsForChapters(ids)]),
    );
  }

  function deselectAllVisibleChapters() {
    const removeChapters = new Set(visibleChapters.map((c) => c.id));
    const nextChapters = selectedChapters.filter((id) => !removeChapters.has(id));
    const removeTopics = new Set(topicsForChapters([...removeChapters]));
    setSelectedChapters(nextChapters);
    setSelectedTopics(selectedTopics.filter((id) => !removeTopics.has(id)));
  }

  function selectAllTopicsForChapter(chapterId: string) {
    const topicIds = topicsForChapters([chapterId]);
    setSelectedTopics(uniquePreserve([...selectedTopics, ...topicIds]));
  }

  function deselectAllTopicsForChapter(chapterId: string) {
    const removeTopics = new Set(topicsForChapters([chapterId]));
    setSelectedTopics(selectedTopics.filter((id) => !removeTopics.has(id)));
  }

  function selectAllVisibleTopics() {
    setSelectedTopics(uniquePreserve([...selectedTopics, ...visibleTopicIds]));
  }

  function deselectAllVisibleTopics() {
    const remove = new Set(visibleTopicIds);
    setSelectedTopics(selectedTopics.filter((id) => !remove.has(id)));
  }

  const selectedVisibleChapters = visibleChapters.filter((c) =>
    selectedChapters.includes(c.id),
  ).length;
  const selectedVisibleTopics = visibleTopicIds.filter((id) =>
    selectedTopics.includes(id),
  ).length;
  const selectedVisiblePapers = visiblePapers.filter((p) =>
    selectedPapers.includes(p.id),
  ).length;

  return (
    <form action={formAction} className="space-y-6">
      <input type="hidden" name="locale" value={locale} />
      {selectedSubjects.map((id) => (
        <input key={`subject-${id}`} type="hidden" name="subjectIds" value={id} />
      ))}
      {selectedPapers.map((id) => (
        <input key={`paper-${id}`} type="hidden" name="paperIds" value={id} />
      ))}
      {selectedChapters.map((id) => (
        <input key={`chapter-${id}`} type="hidden" name="chapterIds" value={id} />
      ))}

      <div>
        <Label htmlFor="title">{t("examTitle")}</Label>
        <Input id="title" name="title" required defaultValue="HSC practice exam" />
      </div>

      <p className="rounded-md border border-dashed border-[var(--lagoon)]/40 bg-[var(--mist)] px-3 py-2 text-sm text-[var(--muted)]">
        {t("scopeHint")}
      </p>

      <div className="space-y-3">
        <FilterSection
          title={t("subjects")}
          summary={t("selectedCount", {
            selected: selectedSubjects.length,
            total: subjects.length,
          })}
          open={openSubjects}
          onOpenChange={setOpenSubjects}
          selectAllLabel={t("selectAll")}
          deselectAllLabel={t("deselectAll")}
          onSelectAll={selectAllSubjects}
          onDeselectAll={deselectAllSubjects}
          canSelectAll={selectedSubjects.length < subjects.length}
          canDeselectAll={selectedSubjects.length > 0}
        >
          <div className="grid gap-2 sm:grid-cols-2">
            {subjects.map((subject) => (
              <FilterCheckItem
                key={subject.id}
                checked={selectedSubjects.includes(subject.id)}
                onChange={() => toggleSubject(subject.id)}
                label={subject.label}
              />
            ))}
          </div>
        </FilterSection>

        <FilterSection
          title={t("papers")}
          summary={
            visiblePapers.length === 0
              ? t("selectSubjectFirst")
              : t("selectedCount", {
                  selected: selectedVisiblePapers,
                  total: visiblePapers.length,
                })
          }
          open={openPapers}
          onOpenChange={setOpenPapers}
          selectAllLabel={t("selectAll")}
          deselectAllLabel={t("deselectAll")}
          onSelectAll={visiblePapers.length ? selectAllPapers : undefined}
          onDeselectAll={visiblePapers.length ? deselectAllPapers : undefined}
          canSelectAll={selectedVisiblePapers < visiblePapers.length}
          canDeselectAll={selectedVisiblePapers > 0}
          empty={
            visiblePapers.length === 0 ? (
              <p className="text-sm text-[var(--muted)]">{t("selectSubjectFirst")}</p>
            ) : undefined
          }
        >
          <div className="grid gap-2 sm:grid-cols-2">
            {visiblePapers.map((paper) => (
              <FilterCheckItem
                key={paper.id}
                checked={selectedPapers.includes(paper.id)}
                onChange={() => togglePaper(paper.id)}
                label={
                  selectedSubjects.length > 1
                    ? `${paper.subjectLabel} — ${paper.label}`
                    : paper.label
                }
              />
            ))}
          </div>
        </FilterSection>

        <FilterSection
          title={t("chapters")}
          summary={
            visibleChapters.length === 0
              ? t("selectPaperFirst")
              : t("selectedCount", {
                  selected: selectedVisibleChapters,
                  total: visibleChapters.length,
                })
          }
          open={openChapters}
          onOpenChange={setOpenChapters}
          selectAllLabel={t("selectAll")}
          deselectAllLabel={t("deselectAll")}
          onSelectAll={visibleChapters.length ? selectAllVisibleChapters : undefined}
          onDeselectAll={
            visibleChapters.length ? deselectAllVisibleChapters : undefined
          }
          canSelectAll={selectedVisibleChapters < visibleChapters.length}
          canDeselectAll={selectedVisibleChapters > 0}
          empty={
            visibleChapters.length === 0 ? (
              <p className="text-sm text-[var(--muted)]">{t("selectPaperFirst")}</p>
            ) : undefined
          }
        >
          <div className="space-y-2">
            {selectedPapers.map((paperId) => {
              const chapters = chaptersByPaper[paperId] ?? [];
              if (chapters.length === 0) return null;
              const paperMeta = visiblePapers.find((p) => p.id === paperId);
              const paperLabel =
                selectedSubjects.length > 1 && paperMeta
                  ? `${paperMeta.subjectLabel} — ${paperMeta.label}`
                  : (paperMeta?.label ?? paperId);
              const selectedInGroup = chapters.filter((c) =>
                selectedChapters.includes(c.id),
              ).length;
              const groupOpen = openChapterGroups[paperId] ?? false;
              return (
                <FilterSection
                  key={paperId}
                  nested
                  title={paperLabel}
                  summary={t("selectedCount", {
                    selected: selectedInGroup,
                    total: chapters.length,
                  })}
                  open={groupOpen}
                  onOpenChange={(next) =>
                    setOpenChapterGroups((prev) => ({ ...prev, [paperId]: next }))
                  }
                  selectAllLabel={t("selectAll")}
                  deselectAllLabel={t("deselectAll")}
                  onSelectAll={() => selectAllChaptersForPaper(paperId)}
                  onDeselectAll={() => deselectAllChaptersForPaper(paperId)}
                  canSelectAll={selectedInGroup < chapters.length}
                  canDeselectAll={selectedInGroup > 0}
                >
                  <div className="grid gap-2 sm:grid-cols-2">
                    {chapters.map((chapter) => (
                      <FilterCheckItem
                        key={chapter.id}
                        checked={selectedChapters.includes(chapter.id)}
                        onChange={() => toggleChapter(chapter.id)}
                        label={chapter.label}
                      />
                    ))}
                  </div>
                </FilterSection>
              );
            })}
          </div>
        </FilterSection>

        <FilterSection
          title={t("topics")}
          hint={t("topicsHint")}
          summary={
            visibleTopicIds.length === 0
              ? t("selectChapterFirst")
              : t("selectedCount", {
                  selected: selectedVisibleTopics,
                  total: visibleTopicIds.length,
                })
          }
          open={openTopics}
          onOpenChange={setOpenTopics}
          selectAllLabel={t("selectAll")}
          deselectAllLabel={t("deselectAll")}
          onSelectAll={visibleTopicIds.length ? selectAllVisibleTopics : undefined}
          onDeselectAll={
            visibleTopicIds.length ? deselectAllVisibleTopics : undefined
          }
          canSelectAll={selectedVisibleTopics < visibleTopicIds.length}
          canDeselectAll={selectedVisibleTopics > 0}
          empty={
            visibleTopicIds.length === 0 ? (
              <p className="text-sm text-[var(--muted)]">{t("selectChapterFirst")}</p>
            ) : undefined
          }
        >
          <div className="space-y-2">
            {selectedChapters.map((chapterId) => {
              const topics = topicsByChapter[chapterId] ?? [];
              if (topics.length === 0) return null;
              const chapterLabel =
                visibleChapters.find((c) => c.id === chapterId)?.label ?? chapterId;
              const selectedInGroup = topics.filter((topic) =>
                selectedTopics.includes(topic.id),
              ).length;
              const groupOpen = openTopicGroups[chapterId] ?? false;
              return (
                <FilterSection
                  key={chapterId}
                  nested
                  title={chapterLabel}
                  summary={t("selectedCount", {
                    selected: selectedInGroup,
                    total: topics.length,
                  })}
                  open={groupOpen}
                  onOpenChange={(next) =>
                    setOpenTopicGroups((prev) => ({ ...prev, [chapterId]: next }))
                  }
                  selectAllLabel={t("selectAll")}
                  deselectAllLabel={t("deselectAll")}
                  onSelectAll={() => selectAllTopicsForChapter(chapterId)}
                  onDeselectAll={() => deselectAllTopicsForChapter(chapterId)}
                  canSelectAll={selectedInGroup < topics.length}
                  canDeselectAll={selectedInGroup > 0}
                >
                  <div className="grid gap-2 sm:grid-cols-2">
                    {topics.map((topic) => (
                      <FilterCheckItem
                        key={topic.id}
                        name="topicIds"
                        value={topic.id}
                        checked={selectedTopics.includes(topic.id)}
                        onChange={() => toggleTopic(topic.id)}
                        label={topic.label}
                      />
                    ))}
                  </div>
                </FilterSection>
              );
            })}
          </div>
        </FilterSection>
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <div>
          <Label htmlFor="count">{t("count")}</Label>
          <Input id="count" name="count" type="number" min={1} defaultValue={50} required />
        </div>
        <div>
          <Label htmlFor="duration">{t("duration")}</Label>
          <Input id="duration" name="duration" type="number" min={1} defaultValue={30} required />
        </div>
        <div>
          <Label htmlFor="difficulty">{t("difficulty")}</Label>
          <select
            id="difficulty"
            name="difficulty"
            className="w-full rounded-md border border-[var(--line)] bg-white px-3 py-2 text-sm"
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value)}
          >
            <option value="">{t("any")}</option>
            <option value="easy">easy</option>
            <option value="medium">medium</option>
            <option value="hard">hard</option>
          </select>
        </div>
        <div>
          <Label htmlFor="qtype">{t("type")}</Label>
          <select
            id="qtype"
            name="qtype"
            className="w-full rounded-md border border-[var(--line)] bg-white px-3 py-2 text-sm"
            value={qtype}
            onChange={(e) => setQtype(e.target.value)}
          >
            <option value="">{t("any")}</option>
            <option value="factual">factual</option>
            <option value="conceptual">conceptual</option>
            <option value="numerical">numerical</option>
            <option value="application">application</option>
          </select>
        </div>
      </div>

      <div className="rounded-md border border-dashed border-[var(--lagoon)] bg-[var(--mist)] px-4 py-3">
        <p className="text-sm text-[var(--muted)]">{t("eligible")}</p>
        <p className="font-display text-3xl text-[var(--ink)]">
          {eligible === null ? "…" : eligible}
        </p>
      </div>

      {errorMessage ? (
        <p className="rounded-md border border-red-200 bg-red-50 px-3 py-2 text-sm text-red-800">
          {errorMessage}
        </p>
      ) : null}

      <Button type="submit" disabled={pending || (eligible !== null && eligible < 1)}>
        {t("generate")}
      </Button>
    </form>
  );
}
