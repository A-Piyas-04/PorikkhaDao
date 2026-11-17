import { randomBytes } from "node:crypto";
import { getDb } from "@/db";
import {
  countEligible,
  getQuestionsByIds,
  pickRandomEligible,
  type EligibilityFilters,
  type QuestionRow,
} from "@/lib/eligibility";

export type ExamSettings = EligibilityFilters & {
  requestedCount: number;
};

export type ExamRecord = {
  id: string;
  owner_user_id: string;
  title: string;
  duration_minutes: number;
  status: "draft" | "published";
  share_token: string | null;
  settings_json: string;
  created_at: string;
  published_at: string | null;
};

export function parseSettings(json: string): ExamSettings {
  return JSON.parse(json) as ExamSettings;
}

export function listExamsForTutor(ownerId: string): ExamRecord[] {
  return getDb()
    .prepare(
      `SELECT * FROM exams WHERE owner_user_id = ? ORDER BY created_at DESC`,
    )
    .all(ownerId) as ExamRecord[];
}

export function getExamForOwner(examId: string, ownerId: string): ExamRecord | null {
  const row = getDb()
    .prepare(`SELECT * FROM exams WHERE id = ? AND owner_user_id = ?`)
    .get(examId, ownerId) as ExamRecord | undefined;
  return row ?? null;
}

export function getPublishedExamByToken(token: string): ExamRecord | null {
  const row = getDb()
    .prepare(`SELECT * FROM exams WHERE share_token = ? AND status = 'published'`)
    .get(token) as ExamRecord | undefined;
  return row ?? null;
}

export function getExamQuestionCount(examId: string): number {
  const row = getDb()
    .prepare(`SELECT COUNT(*) AS c FROM exam_questions WHERE exam_id = ?`)
    .get(examId) as { c: number };
  return row.c;
}

export function getExamQuestions(examId: string): QuestionRow[] {
  const ids = (
    getDb()
      .prepare(
        `SELECT question_id AS id FROM exam_questions
         WHERE exam_id = ? ORDER BY sort_order`,
      )
      .all(examId) as { id: number }[]
  ).map((r) => r.id);
  return getQuestionsByIds(ids);
}

export function createExamDraft(input: {
  ownerId: string;
  title: string;
  durationMinutes: number;
  settings: ExamSettings;
}): { examId: string; eligibleCount: number } {
  const eligibleCount = countEligible(input.settings);
  if (input.settings.requestedCount > eligibleCount) {
    throw new Error(`NOT_ENOUGH:${eligibleCount}`);
  }
  if (input.settings.requestedCount < 1) {
    throw new Error("INVALID_COUNT");
  }
  if (input.settings.topicIds.length < 1) {
    throw new Error("NO_TOPICS");
  }

  const questionIds = pickRandomEligible(
    input.settings,
    input.settings.requestedCount,
  );

  const examId = crypto.randomUUID();
  const db = getDb();
  const insertExam = db.prepare(
    `INSERT INTO exams (id, owner_user_id, title, duration_minutes, status, share_token, settings_json)
     VALUES (?, ?, ?, ?, 'draft', NULL, ?)`,
  );
  const insertEq = db.prepare(
    `INSERT INTO exam_questions (exam_id, question_id, sort_order) VALUES (?, ?, ?)`,
  );

  const tx = db.transaction(() => {
    insertExam.run(
      examId,
      input.ownerId,
      input.title.trim(),
      input.durationMinutes,
      JSON.stringify(input.settings),
    );
    questionIds.forEach((qid, index) => {
      insertEq.run(examId, qid, index + 1);
    });
  });
  tx();

  return { examId, eligibleCount };
}

export function publishExam(examId: string, ownerId: string): ExamRecord {
  const exam = getExamForOwner(examId, ownerId);
  if (!exam) throw new Error("NOT_FOUND");
  if (getExamQuestionCount(examId) < 1) throw new Error("EMPTY_EXAM");

  const token = exam.share_token ?? randomBytes(24).toString("hex");
  getDb()
    .prepare(
      `UPDATE exams
       SET status = 'published', share_token = ?, published_at = datetime('now')
       WHERE id = ? AND owner_user_id = ?`,
    )
    .run(token, examId, ownerId);

  return getExamForOwner(examId, ownerId)!;
}
