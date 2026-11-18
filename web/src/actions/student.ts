"use server";

import { redirect } from "next/navigation";
import { createSession, getSession, identifyStudent } from "@/lib/auth";
import {
  buildAttemptPayload,
  finalizeExpiredIfNeeded,
  getAttemptForStudent,
  requirePublishedExam,
  saveAnswer,
  startOrResumeAttempt,
  submitAttempt,
  type AttemptPayload,
} from "@/lib/attempts";

export type IdentifyState = { error?: string };

function isRedirect(err: unknown) {
  return (
    typeof err === "object" &&
    err &&
    "digest" in err &&
    String((err as { digest?: string }).digest).startsWith("NEXT_REDIRECT")
  );
}

export async function identifyStudentAction(
  _prev: IdentifyState,
  formData: FormData,
): Promise<IdentifyState> {
  const locale = String(formData.get("locale") ?? "en");
  const token = String(formData.get("token") ?? "");
  const name = String(formData.get("name") ?? "");
  const email = String(formData.get("email") ?? "");

  try {
    await requirePublishedExam(token);
    const user = await identifyStudent(name, email);
    await createSession(user);
    redirect(`/${locale}/e/${token}`);
  } catch (err) {
    if (isRedirect(err)) throw err;
    const message = err instanceof Error ? err.message : "";
    if (message === "MISSING_IDENTITY") return { error: "missing" };
    if (message === "EMAIL_IS_TUTOR") return { error: "tutor_email" };
    if (message === "EXAM_NOT_FOUND") return { error: "not_found" };
    throw err;
  }
}

export async function startAttemptAction(formData: FormData) {
  const locale = String(formData.get("locale") ?? "en");
  const token = String(formData.get("token") ?? "");
  const session = await getSession();
  if (!session || session.role !== "student") {
    redirect(`/${locale}/e/${token}`);
  }

  try {
    const exam = await requirePublishedExam(token);
    const attempt = await startOrResumeAttempt(exam, session.id);
    if (attempt.status !== "in_progress") {
      redirect(`/${locale}/e/${token}/done`);
    }
    redirect(`/${locale}/e/${token}/attempt`);
  } catch (err) {
    if (isRedirect(err)) throw err;
    const message = err instanceof Error ? err.message : "";
    if (message === "ALREADY_FINALIZED") {
      redirect(`/${locale}/e/${token}/done`);
    }
    throw err;
  }
}

export async function saveAnswerAction(input: {
  attemptId: string;
  questionId: number;
  option: "A" | "B" | "C" | "D";
}): Promise<{ ok: boolean; error?: string; status?: string }> {
  const session = await getSession();
  if (!session || session.role !== "student") {
    return { ok: false, error: "auth" };
  }

  try {
    const attempt = await saveAnswer(
      input.attemptId,
      session.id,
      input.questionId,
      input.option,
    );
    return { ok: true, status: attempt.status };
  } catch (err) {
    const message = err instanceof Error ? err.message : "";
    if (message === "FINALIZED") {
      return { ok: false, error: "finalized", status: "finalized" };
    }
    return { ok: false, error: message || "save_failed" };
  }
}

export async function submitAttemptAction(formData: FormData) {
  const locale = String(formData.get("locale") ?? "en");
  const token = String(formData.get("token") ?? "");
  const attemptId = String(formData.get("attemptId") ?? "");
  const session = await getSession();
  if (!session || session.role !== "student") {
    redirect(`/${locale}/e/${token}`);
  }

  try {
    await submitAttempt(attemptId, session.id);
  } catch {
    // still navigate to done
  }
  redirect(`/${locale}/e/${token}/done`);
}

export async function loadAttemptPayloadAction(
  token: string,
): Promise<AttemptPayload | { error: string }> {
  const session = await getSession();
  if (!session || session.role !== "student") {
    return { error: "auth" };
  }
  try {
    const exam = await requirePublishedExam(token);
    const found = await getAttemptForStudent(exam.id, session.id);
    if (!found) return { error: "no_attempt" };
    const current = await finalizeExpiredIfNeeded(found);
    if (current.status !== "in_progress") {
      return { error: "finalized" };
    }
    return buildAttemptPayload(current, exam);
  } catch {
    return { error: "not_found" };
  }
}
