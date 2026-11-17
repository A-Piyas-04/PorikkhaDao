import { getTranslations, setRequestLocale } from "next-intl/server";
import { AppShell } from "@/components/app-shell";
import { getExamQuestionCount, getPublishedExamByToken } from "@/lib/exams";

export const dynamic = "force-dynamic";

export default async function PublicExamStubPage({
  params,
}: {
  params: Promise<{ locale: string; token: string }>;
}) {
  const { locale, token } = await params;
  setRequestLocale(locale);
  const t = await getTranslations("public");
  const exam = getPublishedExamByToken(token);

  return (
    <AppShell locale={locale}>
      {!exam ? (
        <p className="rounded-lg border border-red-200 bg-red-50 px-4 py-6 text-red-800">
          {t("notFound")}
        </p>
      ) : (
        <section className="max-w-xl space-y-4 rounded-xl border border-[var(--line)] bg-white/85 p-6">
          <h1 className="font-display text-3xl text-[var(--ink)]">{exam.title}</h1>
          <p className="text-[var(--muted)]">
            {t("duration", { minutes: exam.duration_minutes })}
          </p>
          <p className="text-[var(--muted)]">
            {t("questions", { count: getExamQuestionCount(exam.id) })}
          </p>
          <p className="rounded-md bg-[var(--mist)] px-3 py-2 text-sm text-[var(--ink)]">
            {t("phase2")}
          </p>
        </section>
      )}
    </AppShell>
  );
}
