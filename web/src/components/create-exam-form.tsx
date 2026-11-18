"use client";

import { useEffect, useMemo, useState, useActionState } from "react";
import { useTranslations } from "next-intl";
import { createExamAction, getEligibleCountAction, type CreateExamState } from "@/actions/exams";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

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

  const visibleTopics = useMemo(() => {
    return selectedChapters.flatMap((cid) =>
      (topicsByChapter[cid] ?? []).map((topic) => ({
        ...topic,
        chapterId: cid,
        chapterLabel:
          visibleChapters.find((c) => c.id === cid)?.label ??
          Object.values(chaptersByPaper)
            .flat()
            .find((c) => c.id === cid)?.label ??
          cid,
      })),
    );
  }, [selectedChapters, topicsByChapter, visibleChapters, chaptersByPaper]);

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

    // Drop subject if no papers left for it
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

  function selectAllChaptersForPaper(paperId: string) {
    const chapterIds = chaptersForPapers([paperId]);
    const nextChapters = uniquePreserve([...selectedChapters, ...chapterIds]);
    setSelectedChapters(nextChapters);
    setSelectedTopics(
      uniquePreserve([...selectedTopics, ...topicsForChapters(chapterIds)]),
    );
    if (!selectedPapers.includes(paperId)) {
      setSelectedPapers((prev) => [...prev, paperId]);
    }
  }

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

      <fieldset>
        <legend className="mb-2 text-sm font-medium">{t("subjects")}</legend>
        <div className="grid gap-2 sm:grid-cols-2">
          {subjects.map((subject) => (
            <label
              key={subject.id}
              className="flex items-start gap-2 rounded-md border border-[var(--line)] bg-white px-3 py-2 text-sm"
            >
              <input
                type="checkbox"
                checked={selectedSubjects.includes(subject.id)}
                onChange={() => toggleSubject(subject.id)}
                className="mt-0.5"
              />
              <span>{subject.label}</span>
            </label>
          ))}
        </div>
      </fieldset>

      <fieldset>
        <legend className="mb-2 text-sm font-medium">{t("papers")}</legend>
        {visiblePapers.length === 0 ? (
          <p className="text-sm text-[var(--muted)]">{t("selectSubjectFirst")}</p>
        ) : (
          <div className="grid gap-2 sm:grid-cols-2">
            {visiblePapers.map((paper) => (
              <label
                key={paper.id}
                className="flex items-start gap-2 rounded-md border border-[var(--line)] bg-white px-3 py-2 text-sm"
              >
                <input
                  type="checkbox"
                  checked={selectedPapers.includes(paper.id)}
                  onChange={() => togglePaper(paper.id)}
                  className="mt-0.5"
                />
                <span>
                  {selectedSubjects.length > 1
                    ? `${paper.subjectLabel} — ${paper.label}`
                    : paper.label}
                </span>
              </label>
            ))}
          </div>
        )}
      </fieldset>

      <fieldset>
        <legend className="mb-2 text-sm font-medium">{t("chapters")}</legend>
        {visibleChapters.length === 0 ? (
          <p className="text-sm text-[var(--muted)]">{t("selectPaperFirst")}</p>
        ) : (
          <div className="space-y-4">
            {selectedPapers.map((paperId) => {
              const chapters = chaptersByPaper[paperId] ?? [];
              if (chapters.length === 0) return null;
              const paperLabel =
                visiblePapers.find((p) => p.id === paperId)?.label ?? paperId;
              const allSelected = chapters.every((c) =>
                selectedChapters.includes(c.id),
              );
              return (
                <div key={paperId}>
                  <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
                    <p className="text-xs font-semibold uppercase tracking-wide text-[var(--muted)]">
                      {paperLabel}
                    </p>
                    {!allSelected ? (
                      <button
                        type="button"
                        className="text-xs font-semibold text-[var(--lagoon)]"
                        onClick={() => selectAllChaptersForPaper(paperId)}
                      >
                        {t("selectAllChapters")}
                      </button>
                    ) : null}
                  </div>
                  <div className="grid gap-2 sm:grid-cols-2">
                    {chapters.map((chapter) => (
                      <label
                        key={chapter.id}
                        className="flex items-start gap-2 rounded-md border border-[var(--line)] bg-white px-3 py-2 text-sm"
                      >
                        <input
                          type="checkbox"
                          checked={selectedChapters.includes(chapter.id)}
                          onChange={() => toggleChapter(chapter.id)}
                          className="mt-0.5"
                        />
                        <span>{chapter.label}</span>
                      </label>
                    ))}
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </fieldset>

      <fieldset>
        <legend className="mb-1 text-sm font-medium">{t("topics")}</legend>
        <p className="mb-3 text-sm text-[var(--muted)]">{t("topicsHint")}</p>
        {visibleTopics.length === 0 ? (
          <p className="text-sm text-[var(--muted)]">{t("selectChapterFirst")}</p>
        ) : (
          <div className="space-y-4">
            {selectedChapters.map((chapterId) => {
              const topics = topicsByChapter[chapterId] ?? [];
              if (topics.length === 0) return null;
              const chapterLabel =
                visibleChapters.find((c) => c.id === chapterId)?.label ?? chapterId;
              return (
                <div key={chapterId}>
                  <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-[var(--muted)]">
                    {chapterLabel}
                  </p>
                  <div className="grid gap-2 sm:grid-cols-2">
                    {topics.map((topic) => (
                      <label
                        key={topic.id}
                        className="flex items-start gap-2 rounded-md border border-[var(--line)] bg-white px-3 py-2 text-sm"
                      >
                        <input
                          type="checkbox"
                          name="topicIds"
                          value={topic.id}
                          checked={selectedTopics.includes(topic.id)}
                          onChange={() => toggleTopic(topic.id)}
                          className="mt-0.5"
                        />
                        <span>{topic.label}</span>
                      </label>
                    ))}
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </fieldset>

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
