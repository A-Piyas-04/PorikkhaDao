import { getDb } from "@/db";
import {
  finalizeAllExpired,
  finalizeExpiredIfNeeded,
  type AttemptRecord,
} from "@/lib/attempts";
import { getExamForOwner, getExamQuestionCount, type ExamRecord } from "@/lib/exams";

export type AttemptResultRow = {
  attemptId: string;
  studentName: string;
  studentEmail: string;
  status: AttemptRecord["status"];
  startedAt: string;
  deadlineAt: string;
  finalizedAt: string | null;
  answeredCount: number;
  correctCount: number;
  score: number | null;
  totalQuestions: number;
};

export type ExamResultsPayload = {
  exam: ExamRecord;
  totalQuestions: number;
  attempts: AttemptResultRow[];
};

/**
 * Owner-scoped results. Returns null if exam missing or not owned by tutor.
 * Finalizes overdue in-progress attempts before reading.
 */
export function getExamResultsForOwner(
  examId: string,
  ownerUserId: string,
): ExamResultsPayload | null {
  const exam = getExamForOwner(examId, ownerUserId);
  if (!exam) return null;

  finalizeAllExpired();

  const totalQuestions = getExamQuestionCount(examId);
  const rows = getDb()
    .prepare(
      `SELECT a.*, u.display_name, u.email
       FROM attempts a
       JOIN users u ON u.id = a.student_user_id
       WHERE a.exam_id = ?
       ORDER BY a.started_at DESC`,
    )
    .all(examId) as (AttemptRecord & {
    display_name: string;
    email: string;
  })[];

  const countAnswered = getDb().prepare(
    `SELECT COUNT(*) AS c FROM answers
     WHERE attempt_id = ? AND selected_option IS NOT NULL`,
  );

  const attempts: AttemptResultRow[] = rows.map((row) => {
    const current = finalizeExpiredIfNeeded({
      id: row.id,
      exam_id: row.exam_id,
      student_user_id: row.student_user_id,
      started_at: row.started_at,
      deadline_at: row.deadline_at,
      finalized_at: row.finalized_at,
      status: row.status,
      score: row.score,
      answered_count: row.answered_count,
      correct_count: row.correct_count,
    });

    const liveAnswered =
      current.status === "in_progress"
        ? ((countAnswered.get(current.id) as { c: number }).c ?? 0)
        : current.answered_count;

    return {
      attemptId: current.id,
      studentName: row.display_name,
      studentEmail: row.email,
      status: current.status,
      startedAt: current.started_at,
      deadlineAt: current.deadline_at,
      finalizedAt: current.finalized_at,
      answeredCount: liveAnswered,
      correctCount: current.correct_count,
      score: current.score,
      totalQuestions,
    };
  });

  return { exam, totalQuestions, attempts };
}
