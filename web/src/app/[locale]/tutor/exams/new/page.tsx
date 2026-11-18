import { getTranslations, setRequestLocale } from "next-intl/server";
import { requireTutor } from "@/lib/auth";
import {
  listChapters,
  listPapers,
  listSubjects,
  listTopics,
  localizedName,
} from "@/lib/syllabus";
import { CreateExamForm } from "@/components/create-exam-form";

export const dynamic = "force-dynamic";

export default async function NewExamPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  setRequestLocale(locale);
  await requireTutor(locale);
  const t = await getTranslations("create");

  const subjectRows = await listSubjects();
  const subjects = subjectRows.map((s) => ({
    id: s.id,
    label: localizedName(locale, s.name_en, s.name_bn),
  }));

  const papersBySubject: Record<string, { id: string; label: string }[]> = {};
  const chaptersByPaper: Record<string, { id: string; label: string }[]> = {};
  const topicsByChapter: Record<string, { id: string; label: string }[]> = {};

  for (const subject of subjectRows) {
    const papers = await listPapers(subject.id);
    papersBySubject[subject.id] = papers.map((p) => ({
      id: p.id,
      label: localizedName(locale, p.name_en, p.name_bn),
    }));
    for (const paper of papers) {
      const chapters = await listChapters(paper.id);
      chaptersByPaper[paper.id] = chapters.map((c) => ({
        id: c.id,
        label: `${c.chapter_number}. ${localizedName(locale, c.title_en, c.title_bn)}`,
      }));
      for (const chapter of chapters) {
        topicsByChapter[chapter.id] = (await listTopics(chapter.id)).map(
          (topic) => ({
            id: topic.id,
            label: localizedName(locale, topic.title_en, topic.title_bn),
          }),
        );
      }
    }
  }

  return (
    <div className="space-y-6">
      <h1 className="font-display text-4xl text-[var(--ink)]">{t("title")}</h1>
      <div className="rounded-xl border border-[var(--line)] bg-white/80 p-6 shadow-sm">
        <CreateExamForm
          locale={locale}
          subjects={subjects}
          papersBySubject={papersBySubject}
          chaptersByPaper={chaptersByPaper}
          topicsByChapter={topicsByChapter}
        />
      </div>
    </div>
  );
}
