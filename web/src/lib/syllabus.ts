import { ensureDb, sql } from "@/db";

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

export async function listSubjects(): Promise<Subject[]> {
  await ensureDb();
  const rows = await sql()`
    SELECT id, name_en, name_bn FROM subjects ORDER BY name_en
  `;
  return rows as unknown as Subject[];
}

export async function listPapers(subjectId: string): Promise<Paper[]> {
  await ensureDb();
  const rows = await sql()`
    SELECT id, subject_id, number, name_en, name_bn
    FROM papers WHERE subject_id = ${subjectId} ORDER BY number
  `;
  return rows as unknown as Paper[];
}

export async function listChapters(paperId: string): Promise<Chapter[]> {
  await ensureDb();
  const rows = await sql()`
    SELECT id, paper_id, chapter_number, title_en, title_bn
    FROM chapters WHERE paper_id = ${paperId} ORDER BY chapter_number
  `;
  return rows as unknown as Chapter[];
}

export async function listTopics(chapterId: string): Promise<Topic[]> {
  await ensureDb();
  const rows = await sql()`
    SELECT id, chapter_id, topic_order, title_en, title_bn
    FROM topics WHERE chapter_id = ${chapterId} ORDER BY topic_order
  `;
  return rows as unknown as Topic[];
}

export function localizedName(
  locale: string,
  en: string,
  bn: string,
): string {
  return locale === "bn" ? bn : en;
}
