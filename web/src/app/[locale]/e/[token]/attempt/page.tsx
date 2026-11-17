import { setRequestLocale } from "next-intl/server";
import { redirect } from "next/navigation";
import { ExamAttemptClient } from "@/components/exam-attempt-client";
import { getSession } from "@/lib/auth";
import {
  buildAttemptPayload,
  finalizeExpiredIfNeeded,
  getAttemptForStudent,
  requirePublishedExam,
} from "@/lib/attempts";

export const dynamic = "force-dynamic";

export default async function AttemptPage({
  params,
}: {
  params: Promise<{ locale: string; token: string }>;
}) {
  const { locale, token } = await params;
  setRequestLocale(locale);

  const session = await getSession();
  if (!session || session.role !== "student") {
    redirect(`/${locale}/e/${token}`);
  }

  let exam;
  try {
    exam = requirePublishedExam(token);
  } catch {
    redirect(`/${locale}/e/${token}`);
  }

  const attempt = getAttemptForStudent(exam.id, session.id);
  if (!attempt) {
    redirect(`/${locale}/e/${token}`);
  }

  const current = finalizeExpiredIfNeeded(attempt);
  if (current.status !== "in_progress") {
    redirect(`/${locale}/e/${token}/done`);
  }

  const payload = buildAttemptPayload(current, exam);

  return (
    <ExamAttemptClient locale={locale} token={token} initial={payload} />
  );
}
