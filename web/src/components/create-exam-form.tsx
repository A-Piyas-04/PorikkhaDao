"use client";

import { useEffect, useMemo, useState, useActionState } from "react";
import { useTranslations } from "next-intl";
import { createExamAction, getEligibleCountAction, type CreateExamState } from "@/actions/exams";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

type Option = { id: string; label: string };

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

  const [subjectId, setSubjectId] = useState(subjects[0]?.id ?? "");
  const papers = papersBySubject[subjectId] ?? [];
  const [paperId, setPaperId] = useState(papers[0]?.id ?? "");
  const chapters = chaptersByPaper[paperId] ?? [];
  const [chapterId, setChapterId] = useState(chapters[0]?.id ?? "");
  const topics = topicsByChapter[chapterId] ?? [];
  const [selectedTopics, setSelectedTopics] = useState<string[]>(
    () => topics.map((x) => x.id),
  );
  const [difficulty, setDifficulty] = useState("");
  const [qtype, setQtype] = useState("");
  const [eligible, setEligible] = useState<number | null>(null);

  useEffect(() => {
    const nextPapers = papersBySubject[subjectId] ?? [];
    setPaperId(nextPapers[0]?.id ?? "");
  }, [subjectId, papersBySubject]);

  useEffect(() => {
    const nextChapters = chaptersByPaper[paperId] ?? [];
    setChapterId(nextChapters[0]?.id ?? "");
  }, [paperId, chaptersByPaper]);

  useEffect(() => {
    const nextTopics = topicsByChapter[chapterId] ?? [];
    setSelectedTopics(nextTopics.map((x) => x.id));
  }, [chapterId, topicsByChapter]);

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

  function toggleTopic(id: string) {
    setSelectedTopics((prev) =>
      prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id],
    );
  }

  return (
    <form action={formAction} className="space-y-6">
      <input type="hidden" name="locale" value={locale} />

      <div>
        <Label htmlFor="title">{t("examTitle")}</Label>
        <Input id="title" name="title" required defaultValue="Physics 2nd Paper practice" />
      </div>

      <div className="grid gap-4 md:grid-cols-3">
        <div>
          <Label htmlFor="subject">{t("subject")}</Label>
          <select
            id="subject"
            className="w-full rounded-md border border-[var(--line)] bg-white px-3 py-2 text-sm"
            value={subjectId}
            onChange={(e) => setSubjectId(e.target.value)}
          >
            {subjects.map((s) => (
              <option key={s.id} value={s.id}>
                {s.label}
              </option>
            ))}
          </select>
        </div>
        <div>
          <Label htmlFor="paper">{t("paper")}</Label>
          <select
            id="paper"
            className="w-full rounded-md border border-[var(--line)] bg-white px-3 py-2 text-sm"
            value={paperId}
            onChange={(e) => setPaperId(e.target.value)}
          >
            {papers.map((p) => (
              <option key={p.id} value={p.id}>
                {p.label}
              </option>
            ))}
          </select>
        </div>
        <div>
          <Label htmlFor="chapter">{t("chapter")}</Label>
          <select
            id="chapter"
            className="w-full rounded-md border border-[var(--line)] bg-white px-3 py-2 text-sm"
            value={chapterId}
            onChange={(e) => setChapterId(e.target.value)}
          >
            {chapters.map((c) => (
              <option key={c.id} value={c.id}>
                {c.label}
              </option>
            ))}
          </select>
        </div>
      </div>

      <fieldset>
        <legend className="mb-1 text-sm font-medium">{t("topics")}</legend>
        <p className="mb-3 text-sm text-[var(--muted)]">{t("topicsHint")}</p>
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
