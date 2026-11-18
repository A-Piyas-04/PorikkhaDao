import { randomBytes } from "node:crypto";
import { ensureDb, sql } from "@/db";
import {
  countEligible,
  getQuestionsByIds,
  pickRandomEligible,
  type EligibilityFilters,
  type QuestionRow,
} from "@/lib/eligibility";
import { localizeQuestion } from "@/lib/bilingual-text";
import {
  pickSectionedQuestions,
  type ExamScope,
  type ExamSection,
} from "@/lib/exam-sections";

export type { ExamScope, ExamSection };

export type ExamSettings = EligibilityFilters & {
  requestedCount: number;
  scope?: ExamScope;
  sections?: ExamSection[];
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

function mapExam(row: Record<string, unknown>): ExamRecord {
  return {
    id: String(row.id),
    owner_user_id: String(row.owner_user_id),
    title: String(row.title),
    duration_minutes: Number(row.duration_minutes),
    status: row.status as ExamRecord["status"],
    share_token: row.share_token == null ? null : String(row.share_token),
    settings_json: String(row.settings_json),
    created_at: row.created_at instanceof Date
      ? row.created_at.toISOString()
      : String(row.created_at),
    published_at:
      row.published_at == null
        ? null
        : row.published_at instanceof Date
          ? row.published_at.toISOString()
          : String(row.published_at),
  };
}

export function parseSettings(json: string): ExamSettings {
  return JSON.parse(json) as ExamSettings;
}

export async function listExamsForTutor(ownerId: string): Promise<ExamRecord[]> {
  await ensureDb();
  const rows = await sql()`
    SELECT * FROM exams WHERE owner_user_id = ${ownerId} ORDER BY created_at DESC
  `;
  return (rows as Record<string, unknown>[]).map(mapExam);
}

export async function getExamForOwner(
  examId: string,
  ownerId: string,
): Promise<ExamRecord | null> {
  await ensureDb();
  const rows = await sql()`
    SELECT * FROM exams WHERE id = ${examId} AND owner_user_id = ${ownerId}
  `;
  const row = rows[0] as Record<string, unknown> | undefined;
  return row ? mapExam(row) : null;
}

export async function getPublishedExamByToken(
  token: string,
): Promise<ExamRecord | null> {
  await ensureDb();
  const rows = await sql()`
    SELECT * FROM exams WHERE share_token = ${token} AND status = 'published'
  `;
  const row = rows[0] as Record<string, unknown> | undefined;
  return row ? mapExam(row) : null;
}

export async function getExamQuestionCount(examId: string): Promise<number> {
  await ensureDb();
  const rows = await sql()`
    SELECT COUNT(*)::int AS c FROM exam_questions WHERE exam_id = ${examId}
  `;
  return Number((rows[0] as { c: number }).c);
}

export async function getExamQuestions(
  examId: string,
  locale?: string,
): Promise<QuestionRow[]> {
  await ensureDb();
  const idRows = await sql()`
    SELECT question_id AS id FROM exam_questions
    WHERE exam_id = ${examId} ORDER BY sort_order
  `;
  const ids = (idRows as unknown as { id: number }[]).map((r) => r.id);
  const rows = await getQuestionsByIds(ids);
  if (!locale) return rows;
  return rows.map((row) => localizeQuestion(row, locale));
}

export async function createExamDraft(input: {
  ownerId: string;
  title: string;
  durationMinutes: number;
  settings: ExamSettings;
}): Promise<{ examId: string; eligibleCount: number }> {
  const eligibleCount = await countEligible(input.settings);
  if (input.settings.requestedCount > eligibleCount) {
    throw new Error(`NOT_ENOUGH:${eligibleCount}`);
  }
  if (input.settings.requestedCount < 1) {
    throw new Error("INVALID_COUNT");
  }
  if (input.settings.topicIds.length < 1) {
    throw new Error("NO_TOPICS");
  }

  let questionIds: number[];
  let sections: ExamSection[] = [];

  if (input.settings.scope) {
    const picked = await pickSectionedQuestions(
      input.settings,
      input.settings.requestedCount,
      input.settings.scope,
    );
    questionIds = picked.questionIds;
    sections = picked.sections;
  } else {
    questionIds = await pickRandomEligible(
      input.settings,
      input.settings.requestedCount,
    );
  }

  const settings: ExamSettings = {
    ...input.settings,
    sections,
  };

  const examId = crypto.randomUUID();
  const settingsJson = JSON.stringify(settings);
  const db = sql();

  await db.begin(async (tx) => {
    await tx`
      INSERT INTO exams (id, owner_user_id, title, duration_minutes, status, share_token, settings_json)
      VALUES (
        ${examId},
        ${input.ownerId},
        ${input.title.trim()},
        ${input.durationMinutes},
        'draft',
        NULL,
        ${settingsJson}
      )
    `;
    for (let index = 0; index < questionIds.length; index += 1) {
      await tx`
        INSERT INTO exam_questions (exam_id, question_id, sort_order)
        VALUES (${examId}, ${questionIds[index]}, ${index + 1})
      `;
    }
  });

  return { examId, eligibleCount };
}

export async function publishExam(
  examId: string,
  ownerId: string,
): Promise<ExamRecord> {
  const exam = await getExamForOwner(examId, ownerId);
  if (!exam) throw new Error("NOT_FOUND");
  if ((await getExamQuestionCount(examId)) < 1) throw new Error("EMPTY_EXAM");

  const token = exam.share_token ?? randomBytes(24).toString("hex");
  await ensureDb();
  await sql()`
    UPDATE exams
    SET status = 'published', share_token = ${token}, published_at = NOW()
    WHERE id = ${examId} AND owner_user_id = ${ownerId}
  `;

  return (await getExamForOwner(examId, ownerId))!;
}
