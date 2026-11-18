import { ensureDb, sql } from "@/db";
import {
  finalizeAllExpired,
  finalizeExpiredIfNeeded,
  type AttemptRecord,
} from "@/lib/attempts";
import {
  getExamForOwner,
  getExamQuestionCount,
  type ExamRecord,
} from "@/lib/exams";

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

function mapAttemptBase(row: Record<string, unknown>): AttemptRecord {
  const toIso = (value: unknown) =>
    value instanceof Date ? value.toISOString() : String(value);

  return {
    id: String(row.id),
    exam_id: String(row.exam_id),
    student_user_id: String(row.student_user_id),
    started_at: toIso(row.started_at),
    deadline_at: toIso(row.deadline_at),
    finalized_at: row.finalized_at == null ? null : toIso(row.finalized_at),
    status: row.status as AttemptRecord["status"],
    score: row.score == null ? null : Number(row.score),
    answered_count: Number(row.answered_count ?? 0),
    correct_count: Number(row.correct_count ?? 0),
  };
}

/**
 * Owner-scoped results. Returns null if exam missing or not owned by tutor.
 * Finalizes overdue in-progress attempts before reading.
 */
export async function getExamResultsForOwner(
  examId: string,
  ownerUserId: string,
): Promise<ExamResultsPayload | null> {
  const exam = await getExamForOwner(examId, ownerUserId);
  if (!exam) return null;

  await finalizeAllExpired();

  const totalQuestions = await getExamQuestionCount(examId);
  await ensureDb();
  const rows = await sql()`
    SELECT a.*, u.display_name, u.email
    FROM attempts a
    JOIN users u ON u.id = a.student_user_id
    WHERE a.exam_id = ${examId}
    ORDER BY a.started_at DESC
  `;

  const attempts: AttemptResultRow[] = [];
  for (const row of rows as Record<string, unknown>[]) {
    const current = await finalizeExpiredIfNeeded(mapAttemptBase(row));

    let liveAnswered = current.answered_count;
    if (current.status === "in_progress") {
      const countRows = await sql()`
        SELECT COUNT(*)::int AS c FROM answers
        WHERE attempt_id = ${current.id} AND selected_option IS NOT NULL
      `;
      liveAnswered = Number((countRows[0] as { c: number }).c ?? 0);
    }

    attempts.push({
      attemptId: current.id,
      studentName: String(row.display_name),
      studentEmail: String(row.email),
      status: current.status,
      startedAt: current.started_at,
      deadlineAt: current.deadline_at,
      finalizedAt: current.finalized_at,
      answeredCount: liveAnswered,
      correctCount: current.correct_count,
      score: current.score,
      totalQuestions,
    });
  }

  return { exam, totalQuestions, attempts };
}
