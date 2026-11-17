import { getDb } from "@/db";

export type Subject = { id: string; name_en: string; name_bn: string };
export type Paper = {
  id: string;
  subject_id: string;
  number: number;
  name_en: string;
  name_bn: string;
};
export type Chapter = {
  id: string;
  paper_id: string;
  chapter_number: number;
  title_en: string;
  title_bn: string;
};
export type Topic = {
  id: string;
  chapter_id: string;
  topic_order: number;
  title_en: string;
  title_bn: string;
};

export function listSubjects(): Subject[] {
  return getDb().prepare("SELECT id, name_en, name_bn FROM subjects ORDER BY name_en").all() as Subject[];
}

export function listPapers(subjectId: string): Paper[] {
  return getDb()
    .prepare(
      `SELECT id, subject_id, number, name_en, name_bn
       FROM papers WHERE subject_id = ? ORDER BY number`,
    )
    .all(subjectId) as Paper[];
}

export function listChapters(paperId: string): Chapter[] {
  return getDb()
    .prepare(
      `SELECT id, paper_id, chapter_number, title_en, title_bn
       FROM chapters WHERE paper_id = ? ORDER BY chapter_number`,
    )
    .all(paperId) as Chapter[];
}

export function listTopics(chapterId: string): Topic[] {
  return getDb()
    .prepare(
      `SELECT id, chapter_id, topic_order, title_en, title_bn
       FROM topics WHERE chapter_id = ? ORDER BY topic_order`,
    )
    .all(chapterId) as Topic[];
}

export function localizedName(
  locale: string,
  en: string,
  bn: string,
): string {
  return locale === "bn" ? bn : en;
}
