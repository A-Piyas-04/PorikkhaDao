import { ensureDb, sql } from "@/db";
import {
  getExamQuestions,
  getPublishedExamByToken,
  parseSettings,
  type ExamRecord,
} from "@/lib/exams";
import { sectionLabelForOrder } from "@/lib/exam-sections";
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
  sectionLabel?: string | null;
};

export type AttemptPayload = {
  attempt: AttemptRecord;
  exam: ExamRecord;
  questions: StudentQuestion[];
  answers: Record<number, "A" | "B" | "C" | "D">;
  serverNow: string;
};

function mapAttempt(row: Record<string, unknown>): AttemptRecord {
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

async function scoreAttempt(
  attemptId: string,
  examId: string,
): Promise<{ answered: number; correct: number; score: number }> {
  const questions = await getExamQuestions(examId);
  const answerRows = await sql()`
    SELECT question_id, selected_option FROM answers WHERE attempt_id = ${attemptId}
  `;
  const byQ = new Map(
    (
      answerRows as unknown as {
        question_id: number;
        selected_option: string | null;
      }[]
    ).map((r) => [r.question_id, r.selected_option]),
  );

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

export async function getAttemptById(
  attemptId: string,
): Promise<AttemptRecord | null> {
  await ensureDb();
  const rows = await sql()`SELECT * FROM attempts WHERE id = ${attemptId}`;
  const row = rows[0] as Record<string, unknown> | undefined;
  return row ? mapAttempt(row) : null;
}

export async function getAttemptForStudent(
  examId: string,
  studentId: string,
): Promise<AttemptRecord | null> {
  await ensureDb();
  const rows = await sql()`
    SELECT * FROM attempts WHERE exam_id = ${examId} AND student_user_id = ${studentId}
  `;
  const row = rows[0] as Record<string, unknown> | undefined;
  return row ? mapAttempt(row) : null;
}

export async function finalizeAttempt(
  attempt: AttemptRecord,
  status: "submitted" | "expired",
): Promise<AttemptRecord> {
  if (attempt.status !== "in_progress") return attempt;

  const { answered, correct, score } = await scoreAttempt(
    attempt.id,
    attempt.exam_id,
  );
  const finalizedAt = nowUtcIso();
  await ensureDb();
  await sql()`
    UPDATE attempts
    SET status = ${status},
        finalized_at = ${finalizedAt},
        score = ${score},
        answered_count = ${answered},
        correct_count = ${correct}
    WHERE id = ${attempt.id} AND status = 'in_progress'
  `;

  return (await getAttemptById(attempt.id))!;
}

/** Finalize if still in progress and past deadline. */
export async function finalizeExpiredIfNeeded(
  attempt: AttemptRecord,
): Promise<AttemptRecord> {
  if (attempt.status !== "in_progress") return attempt;
  if (!isPastDeadline(attempt.deadline_at)) return attempt;
  return finalizeAttempt(attempt, "expired");
}

export async function finalizeAllExpired(): Promise<number> {
  const now = nowUtcIso();
  await ensureDb();
  const rows = await sql()`
    SELECT * FROM attempts
    WHERE status = 'in_progress' AND deadline_at <= ${now}
  `;

  for (const row of rows as Record<string, unknown>[]) {
    await finalizeAttempt(mapAttempt(row), "expired");
  }
  return rows.length;
}

export async function startOrResumeAttempt(
  exam: ExamRecord,
  studentId: string,
): Promise<AttemptRecord> {
  const existing = await getAttemptForStudent(exam.id, studentId);
  if (existing) {
    const current = await finalizeExpiredIfNeeded(existing);
    if (current.status !== "in_progress") {
      throw new Error("ALREADY_FINALIZED");
    }
    return current;
  }

  const startedAt = nowUtcIso();
  const deadlineAt = addMinutesIso(startedAt, exam.duration_minutes);
  const id = crypto.randomUUID();
  await ensureDb();
  await sql()`
    INSERT INTO attempts (
      id, exam_id, student_user_id, started_at, deadline_at, status
    ) VALUES (
      ${id}, ${exam.id}, ${studentId}, ${startedAt}, ${deadlineAt}, 'in_progress'
    )
  `;

  return (await getAttemptById(id))!;
}

export async function saveAnswer(
  attemptId: string,
  studentId: string,
  questionId: number,
  option: "A" | "B" | "C" | "D",
): Promise<AttemptRecord> {
  const attempt = await getAttemptById(attemptId);
  if (!attempt || attempt.student_user_id !== studentId) {
    throw new Error("NOT_FOUND");
  }

  const current = await finalizeExpiredIfNeeded(attempt);
  if (current.status !== "in_progress") {
    throw new Error("FINALIZED");
  }

  await ensureDb();
  const belongs = await sql()`
    SELECT 1 AS ok FROM exam_questions
    WHERE exam_id = ${current.exam_id} AND question_id = ${questionId}
  `;
  if (belongs.length === 0) throw new Error("BAD_QUESTION");

  const updatedAt = nowUtcIso();
  await sql()`
    INSERT INTO answers (attempt_id, question_id, selected_option, updated_at)
    VALUES (${current.id}, ${questionId}, ${option}, ${updatedAt})
    ON CONFLICT (attempt_id, question_id) DO UPDATE SET
      selected_option = EXCLUDED.selected_option,
      updated_at = EXCLUDED.updated_at
  `;

  return current;
}

export async function submitAttempt(
  attemptId: string,
  studentId: string,
): Promise<AttemptRecord> {
  const attempt = await getAttemptById(attemptId);
  if (!attempt || attempt.student_user_id !== studentId) {
    throw new Error("NOT_FOUND");
  }

  const current = await finalizeExpiredIfNeeded(attempt);
  if (current.status === "expired") return current;
  if (current.status === "submitted") return current;
  return finalizeAttempt(current, "submitted");
}

export async function studentQuestionsForExam(
  examId: string,
  locale = "en",
  settingsJson?: string,
): Promise<StudentQuestion[]> {
  const questions = await getExamQuestions(examId);
  const sections = settingsJson
    ? parseSettings(settingsJson).sections
    : undefined;
  return questions.map((q, index) => {
    const order = index + 1;
    return {
      id: q.id,
      order,
      stem: q.stem,
      options: {
        A: q.option_a,
        B: q.option_b,
        C: q.option_c,
        D: q.option_d,
      },
      sectionLabel: sectionLabelForOrder(sections, order, locale),
    };
  });
}

export async function getAnswerMap(
  attemptId: string,
): Promise<Record<number, "A" | "B" | "C" | "D">> {
  await ensureDb();
  const rows = await sql()`
    SELECT question_id, selected_option FROM answers
    WHERE attempt_id = ${attemptId} AND selected_option IS NOT NULL
  `;

  const map: Record<number, "A" | "B" | "C" | "D"> = {};
  for (const row of rows as unknown as {
    question_id: number;
    selected_option: "A" | "B" | "C" | "D";
  }[]) {
    map[row.question_id] = row.selected_option;
  }
  return map;
}

export async function buildAttemptPayload(
  attempt: AttemptRecord,
  exam: ExamRecord,
  locale = "en",
): Promise<AttemptPayload> {
  const current = await finalizeExpiredIfNeeded(attempt);
  return {
    attempt: current,
    exam,
    questions: await studentQuestionsForExam(
      exam.id,
      locale,
      exam.settings_json,
    ),
    answers: await getAnswerMap(current.id),
    serverNow: nowUtcIso(),
  };
}

export async function requirePublishedExam(token: string): Promise<ExamRecord> {
  const exam = await getPublishedExamByToken(token);
  if (!exam) throw new Error("EXAM_NOT_FOUND");
  return exam;
}
