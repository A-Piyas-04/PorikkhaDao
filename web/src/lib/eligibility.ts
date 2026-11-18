import { ensureDb, sql } from "@/db";

export type EligibilityFilters = {
  topicIds: string[];
  difficulty?: "easy" | "medium" | "hard" | "";
  qtype?: "factual" | "conceptual" | "numerical" | "application" | "";
};

export type QuestionRow = {
  id: number;
  stem: string;
  option_a: string;
  option_b: string;
  option_c: string;
  option_d: string;
  correct: "A" | "B" | "C" | "D";
  difficulty: string | null;
  qtype: string | null;
};

/** Strict filter: every topic tag on a question must be in includeTopics. */
export async function findEligibleQuestionIds(
  filters: EligibilityFilters,
): Promise<number[]> {
  const includeTopics = filters.topicIds.filter(Boolean);
  if (includeTopics.length === 0) return [];

  await ensureDb();
  const db = sql();

  const difficulty = filters.difficulty || null;
  const qtype = filters.qtype || null;

  const rows = await db`
    SELECT q.id
    FROM questions q
    WHERE q.verified = 1
      AND EXISTS (SELECT 1 FROM question_topics qt0 WHERE qt0.question_id = q.id)
      AND NOT EXISTS (
        SELECT 1 FROM question_topics qt
        WHERE qt.question_id = q.id
          AND qt.topic_id NOT IN ${db(includeTopics)}
      )
      AND (
        SELECT COUNT(*) FROM question_topics qt3 WHERE qt3.question_id = q.id
      ) = (
        SELECT COUNT(*) FROM question_topics qt4
        WHERE qt4.question_id = q.id AND qt4.topic_id IN ${db(includeTopics)}
      )
      AND (${difficulty}::text IS NULL OR q.difficulty = ${difficulty})
      AND (${qtype}::text IS NULL OR q.qtype = ${qtype})
  `;

  return (rows as unknown as { id: number }[]).map((r) => r.id);
}

export async function countEligible(filters: EligibilityFilters): Promise<number> {
  return (await findEligibleQuestionIds(filters)).length;
}

export async function pickRandomEligible(
  filters: EligibilityFilters,
  count: number,
): Promise<number[]> {
  const ids = await findEligibleQuestionIds(filters);
  if (count > ids.length) {
    throw new Error(`NOT_ENOUGH:${ids.length}`);
  }

  await ensureDb();
  const db = sql();
  const rows = await db`
    SELECT id FROM questions
    WHERE id IN ${db(ids)}
    ORDER BY RANDOM()
    LIMIT ${count}
  `;

  return (rows as unknown as { id: number }[]).map((r) => r.id);
}

export async function getQuestionsByIds(ids: number[]): Promise<QuestionRow[]> {
  if (ids.length === 0) return [];
  await ensureDb();
  const db = sql();
  const rows = await db`
    SELECT id, stem, option_a, option_b, option_c, option_d, correct, difficulty, qtype
    FROM questions WHERE id IN ${db(ids)}
  `;

  const byId = new Map(
    (rows as unknown as QuestionRow[]).map((r) => [r.id, r]),
  );
  return ids.map((id) => byId.get(id)!).filter(Boolean);
}
