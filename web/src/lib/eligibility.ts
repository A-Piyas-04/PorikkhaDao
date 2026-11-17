import { getDb } from "@/db";

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
export function findEligibleQuestionIds(filters: EligibilityFilters): number[] {
  const includeTopics = filters.topicIds.filter(Boolean);
  if (includeTopics.length === 0) return [];

  const db = getDb();
  const placeholders = includeTopics.map(() => "?").join(",");
  const params: unknown[] = [...includeTopics, ...includeTopics];

  let difficultyClause = "";
  if (filters.difficulty) {
    difficultyClause = "AND q.difficulty = ?";
    params.push(filters.difficulty);
  }

  let typeClause = "";
  if (filters.qtype) {
    typeClause = "AND q.qtype = ?";
    params.push(filters.qtype);
  }

  const sql = `
    SELECT q.id
    FROM questions q
    WHERE q.verified = 1
      AND EXISTS (SELECT 1 FROM question_topics qt0 WHERE qt0.question_id = q.id)
      AND NOT EXISTS (
        SELECT 1 FROM question_topics qt
        WHERE qt.question_id = q.id
          AND qt.topic_id NOT IN (${placeholders})
      )
      AND (
        SELECT COUNT(*) FROM question_topics qt3 WHERE qt3.question_id = q.id
      ) = (
        SELECT COUNT(*) FROM question_topics qt4
        WHERE qt4.question_id = q.id AND qt4.topic_id IN (${placeholders})
      )
      ${difficultyClause}
      ${typeClause}
  `;

  const rows = db.prepare(sql).all(...params) as { id: number }[];
  return rows.map((r) => r.id);
}

export function countEligible(filters: EligibilityFilters): number {
  return findEligibleQuestionIds(filters).length;
}

export function pickRandomEligible(
  filters: EligibilityFilters,
  count: number,
): number[] {
  const ids = findEligibleQuestionIds(filters);
  if (count > ids.length) {
    throw new Error(`NOT_ENOUGH:${ids.length}`);
  }

  const db = getDb();
  const placeholders = ids.map(() => "?").join(",");
  const rows = db
    .prepare(
      `SELECT id FROM questions
       WHERE id IN (${placeholders})
       ORDER BY RANDOM()
       LIMIT ?`,
    )
    .all(...ids, count) as { id: number }[];

  return rows.map((r) => r.id);
}

export function getQuestionsByIds(ids: number[]): QuestionRow[] {
  if (ids.length === 0) return [];
  const db = getDb();
  const placeholders = ids.map(() => "?").join(",");
  const rows = db
    .prepare(
      `SELECT id, stem, option_a, option_b, option_c, option_d, correct, difficulty, qtype
       FROM questions WHERE id IN (${placeholders})`,
    )
    .all(...ids) as QuestionRow[];

  const byId = new Map(rows.map((r) => [r.id, r]));
  return ids.map((id) => byId.get(id)!).filter(Boolean);
}
