import { getTranslations, setRequestLocale } from "next-intl/server";
import { AppShell } from "@/components/app-shell";
import { StudentIdentifyForm } from "@/components/student-identify-form";
import { Button } from "@/components/ui/button";
import { getSession, destroySession } from "@/lib/auth";
import {
  finalizeExpiredIfNeeded,
  getAttemptForStudent,
} from "@/lib/attempts";
import { getExamQuestionCount, getPublishedExamByToken } from "@/lib/exams";
import { startAttemptAction } from "@/actions/student";
import { redirect } from "next/navigation";

export const dynamic = "force-dynamic";

async function switchIdentityAction(formData: FormData) {
  "use server";
  const locale = String(formData.get("locale") ?? "en");
  const token = String(formData.get("token") ?? "");
  await destroySession();
  redirect(`/${locale}/e/${token}`);
}

export default async function ExamLandingPage({
  params,
}: {
  params: Promise<{ locale: string; token: string }>;
}) {
  const { locale, token } = await params;
  setRequestLocale(locale);
  const t = await getTranslations("public");
  const exam = getPublishedExamByToken(token);
  const session = await getSession();

  if (!exam) {
    return (
      <AppShell locale={locale}>
        <p className="rounded-lg border border-red-200 bg-red-50 px-4 py-6 text-red-800">
          {t("notFound")}
        </p>
      </AppShell>
    );
  }

  const qCount = getExamQuestionCount(exam.id);
  const studentSession = session?.role === "student" ? session : null;
  const attempt = studentSession
    ? getAttemptForStudent(exam.id, studentSession.id)
    : null;
  const current = attempt ? finalizeExpiredIfNeeded(attempt) : null;

  return (
    <AppShell locale={locale}>
      <section className="mx-auto max-w-lg space-y-6">
        <div className="rounded-2xl border border-[var(--line)] bg-white/90 p-5 shadow-sm sm:p-6">
          <p className="text-sm font-medium text-[var(--lagoon)]">{t("title")}</p>
          <h1 className="mt-1 font-display text-3xl leading-tight text-[var(--ink)] sm:text-4xl">
            {exam.title}
          </h1>
          <dl className="mt-4 grid grid-cols-2 gap-3 text-sm">
            <div className="rounded-lg bg-[var(--mist)] px-3 py-3">
              <dt className="text-[var(--muted)]">Time</dt>
              <dd className="text-lg font-semibold text-[var(--ink)]">
                {t("duration", { minutes: exam.duration_minutes })}
              </dd>
            </div>
            <div className="rounded-lg bg-[var(--mist)] px-3 py-3">
              <dt className="text-[var(--muted)]">MCQ</dt>
              <dd className="text-lg font-semibold text-[var(--ink)]">
                {t("questions", { count: qCount })}
              </dd>
            </div>
          </dl>
        </div>

        <div className="rounded-2xl border border-[var(--line)] bg-white/90 p-5 shadow-sm sm:p-6">
          {!studentSession ? (
            <StudentIdentifyForm locale={locale} token={token} />
          ) : (
            <div className="space-y-4">
              <p className="text-sm text-[var(--muted)]">
                {t("signedInAs", { name: studentSession.displayName })}
              </p>
              <p className="text-sm text-[var(--ink)]">{t("readyHint")}</p>

              {current && current.status !== "in_progress" ? (
                <>
                  <p className="rounded-md bg-[var(--mist)] px-3 py-2 text-sm">
                    {t("alreadyDone")}
                  </p>
                  <form action={startAttemptAction}>
                    <input type="hidden" name="locale" value={locale} />
                    <input type="hidden" name="token" value={token} />
                    <Button type="submit" className="min-h-12 w-full touch-manipulation">
                      {t("viewResult")}
                    </Button>
                  </form>
                </>
              ) : (
                <form action={startAttemptAction}>
                  <input type="hidden" name="locale" value={locale} />
                  <input type="hidden" name="token" value={token} />
                  <Button type="submit" className="min-h-12 w-full touch-manipulation">
                    {current ? t("resume") : t("start")}
                  </Button>
                </form>
              )}

              <form action={switchIdentityAction}>
                <input type="hidden" name="locale" value={locale} />
                <input type="hidden" name="token" value={token} />
                <button
                  type="submit"
                  className="w-full min-h-11 text-sm text-[var(--muted)] underline-offset-2 hover:underline touch-manipulation"
                >
                  {t("changeIdentity")}
                </button>
              </form>
            </div>
          )}
        </div>
      </section>
    </AppShell>
  );
}
