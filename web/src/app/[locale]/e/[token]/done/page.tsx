import { getTranslations, setRequestLocale } from "next-intl/server";
import { AppShell } from "@/components/app-shell";
import { getSession } from "@/lib/auth";
import {
  finalizeExpiredIfNeeded,
  getAttemptForStudent,
} from "@/lib/attempts";
import { getPublishedExamByToken } from "@/lib/exams";
import { Link } from "@/i18n/navigation";

export const dynamic = "force-dynamic";

export default async function DonePage({
  params,
}: {
  params: Promise<{ locale: string; token: string }>;
}) {
  const { locale, token } = await params;
  setRequestLocale(locale);
  const t = await getTranslations("done");
  const exam = getPublishedExamByToken(token);
  const session = await getSession();

  const found =
    exam && session?.role === "student"
      ? getAttemptForStudent(exam.id, session.id)
      : null;
  const attempt = found ? finalizeExpiredIfNeeded(found) : null;
  const titleKey =
    attempt?.status === "expired" ? "expiredTitle" : "submittedTitle";

  return (
    <AppShell locale={locale}>
      <section className="mx-auto max-w-md space-y-4 rounded-2xl border border-[var(--line)] bg-white/90 p-6 shadow-sm">
        {!exam || !attempt ? (
          <p className="text-[var(--muted)]">{t("noAttempt")}</p>
        ) : (
          <>
            <h1 className="font-display text-3xl text-[var(--ink)]">{t(titleKey)}</h1>
            <p className="text-[var(--muted)]">{exam.title}</p>
            <p className="text-[var(--ink)]">{t("body")}</p>
            <p className="text-sm text-[var(--muted)]">
              {t("status", { status: attempt.status })}
            </p>
          </>
        )}
        <Link
          href={`/e/${token}`}
          className="inline-flex min-h-11 items-center text-sm font-semibold text-[var(--lagoon)]"
        >
          ← Back
        </Link>
      </section>
    </AppShell>
  );
}
