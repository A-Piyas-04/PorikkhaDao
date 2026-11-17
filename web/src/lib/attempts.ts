import { getDb } from "@/db";
import { getExamQuestions, getPublishedExamByToken, type ExamRecord } from "@/lib/exams";
import { addMinutesIso, isPastDeadline, nowUtcIso } from "@/lib/time";

export type AttemptRecord = {
  id: string;
  exam_id: string;
  student_user_id: string;
  started_at: string;
  deadline_at: string;
  finalized_at: string | null;
  status: "in_progress" | "submitted" | "expired";
  score: number | null;
  answered_count: number;
  correct_count: number;
};

export type StudentQuestion = {
  id: number;
  order: number;
  stem: string;
  options: { A: string; B: string; C: string; D: string };
};

export type AttemptPayload = {
  attempt: AttemptRecord;
  exam: ExamRecord;
  questions: StudentQuestion[];
  answers: Record<number, "A" | "B" | "C" | "D">;
  serverNow: string;
};

function scoreAttempt(attemptId: string, examId: string): {
  answered: number;
  correct: number;
  score: number;
} {
  const db = getDb();
  const questions = getExamQuestions(examId);
  const answerRows = db
    .prepare(`SELECT question_id, selected_option FROM answers WHERE attempt_id = ?`)
    .all(attemptId) as { question_id: number; selected_option: string | null }[];
  const byQ = new Map(answerRows.map((r) => [r.question_id, r.selected_option]));

  let answered = 0;
  let correct = 0;
  for (const q of questions) {
    const selected = byQ.get(q.id);
    if (selected) {
      answered += 1;
      if (selected === q.correct) correct += 1;
    }
  }
  return { answered, correct, score: correct };
}

export function getAttemptById(attemptId: string): AttemptRecord | null {
  const row = getDb()
    .prepare(`SELECT * FROM attempts WHERE id = ?`)
    .get(attemptId) as AttemptRecord | undefined;
  return row ?? null;
}

export function getAttemptForStudent(
  examId: string,
  studentId: string,
): AttemptRecord | null {
  const row = getDb()
    .prepare(`SELECT * FROM attempts WHERE exam_id = ? AND student_user_id = ?`)
    .get(examId, studentId) as AttemptRecord | undefined;
  return row ?? null;
}

export function finalizeAttempt(
  attempt: AttemptRecord,
  status: "submitted" | "expired",
): AttemptRecord {
  if (attempt.status !== "in_progress") return attempt;

  const { answered, correct, score } = scoreAttempt(attempt.id, attempt.exam_id);
  const finalizedAt = nowUtcIso();
  getDb()
    .prepare(
      `UPDATE attempts
       SET status = ?, finalized_at = ?, score = ?, answered_count = ?, correct_count = ?
       WHERE id = ? AND status = 'in_progress'`,
    )
    .run(status, finalizedAt, score, answered, correct, attempt.id);

  return getAttemptById(attempt.id)!;
}

/** Finalize if still in progress and past deadline. */
export function finalizeExpiredIfNeeded(attempt: AttemptRecord): AttemptRecord {
  if (attempt.status !== "in_progress") return attempt;
  if (!isPastDeadline(attempt.deadline_at)) return attempt;
  return finalizeAttempt(attempt, "expired");
}

export function finalizeAllExpired(): number {
  const now = nowUtcIso();
  const rows = getDb()
    .prepare(
      `SELECT * FROM attempts
       WHERE status = 'in_progress' AND deadline_at <= ?`,
    )
    .all(now) as AttemptRecord[];

  for (const row of rows) {
    finalizeAttempt(row, "expired");
  }
  return rows.length;
}

export function startOrResumeAttempt(
  exam: ExamRecord,
  studentId: string,
): AttemptRecord {
  const existing = getAttemptForStudent(exam.id, studentId);
  if (existing) {
    const current = finalizeExpiredIfNeeded(existing);
    if (current.status !== "in_progress") {
      throw new Error("ALREADY_FINALIZED");
    }
    return current;
  }

  const startedAt = nowUtcIso();
  const deadlineAt = addMinutesIso(startedAt, exam.duration_minutes);
  const id = crypto.randomUUID();
  getDb()
    .prepare(
      `INSERT INTO attempts (
         id, exam_id, student_user_id, started_at, deadline_at, status
       ) VALUES (?, ?, ?, ?, ?, 'in_progress')`,
    )
    .run(id, exam.id, studentId, startedAt, deadlineAt);

  return getAttemptById(id)!;
}

export function saveAnswer(
  attemptId: string,
  studentId: string,
  questionId: number,
  option: "A" | "B" | "C" | "D",
): AttemptRecord {
  const attempt = getAttemptById(attemptId);
  if (!attempt || attempt.student_user_id !== studentId) {
    throw new Error("NOT_FOUND");
  }

  let current = finalizeExpiredIfNeeded(attempt);
  if (current.status !== "in_progress") {
    throw new Error("FINALIZED");
  }

  const belongs = getDb()
    .prepare(
      `SELECT 1 AS ok FROM exam_questions WHERE exam_id = ? AND question_id = ?`,
    )
    .get(current.exam_id, questionId) as { ok: number } | undefined;
  if (!belongs) throw new Error("BAD_QUESTION");

  getDb()
    .prepare(
      `INSERT INTO answers (attempt_id, question_id, selected_option, updated_at)
       VALUES (?, ?, ?, ?)
       ON CONFLICT(attempt_id, question_id) DO UPDATE SET
         selected_option = excluded.selected_option,
         updated_at = excluded.updated_at`,
    )
    .run(current.id, questionId, option, nowUtcIso());

  return current;
}

export function submitAttempt(attemptId: string, studentId: string): AttemptRecord {
  const attempt = getAttemptById(attemptId);
  if (!attempt || attempt.student_user_id !== studentId) {
    throw new Error("NOT_FOUND");
  }

  let current = finalizeExpiredIfNeeded(attempt);
  if (current.status === "expired") return current;
  if (current.status === "submitted") return current;
  return finalizeAttempt(current, "submitted");
}

export function studentQuestionsForExam(examId: string): StudentQuestion[] {
  return getExamQuestions(examId).map((q, index) => ({
    id: q.id,
    order: index + 1,
    stem: q.stem,
    options: {
      A: q.option_a,
      B: q.option_b,
      C: q.option_c,
      D: q.option_d,
    },
  }));
}

export function getAnswerMap(attemptId: string): Record<number, "A" | "B" | "C" | "D"> {
  const rows = getDb()
    .prepare(
      `SELECT question_id, selected_option FROM answers
       WHERE attempt_id = ? AND selected_option IS NOT NULL`,
    )
    .all(attemptId) as { question_id: number; selected_option: "A" | "B" | "C" | "D" }[];

  const map: Record<number, "A" | "B" | "C" | "D"> = {};
  for (const row of rows) map[row.question_id] = row.selected_option;
  return map;
}

export function buildAttemptPayload(
  attempt: AttemptRecord,
  exam: ExamRecord,
): AttemptPayload {
  const current = finalizeExpiredIfNeeded(attempt);
  return {
    attempt: current,
    exam,
    questions: studentQuestionsForExam(exam.id),
    answers: getAnswerMap(current.id),
    serverNow: nowUtcIso(),
  };
}

export function requirePublishedExam(token: string): ExamRecord {
  const exam = getPublishedExamByToken(token);
  if (!exam) throw new Error("EXAM_NOT_FOUND");
  return exam;
}
