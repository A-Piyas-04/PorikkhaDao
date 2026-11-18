import { getTranslations, setRequestLocale } from "next-intl/server";
import { notFound } from "next/navigation";
import { Link } from "@/i18n/navigation";
import { requireTutor } from "@/lib/auth";
import { getExamForOwner, getExamQuestions, parseSettings } from "@/lib/exams";
import { isSectionStart } from "@/lib/exam-sections";
import { publishExamAction } from "@/actions/exams";
import { Button, buttonClassName } from "@/components/ui/button";
import { CopyLinkButton } from "@/components/copy-link-button";

export const dynamic = "force-dynamic";

export default async function ExamPreviewPage({
  params,
  searchParams,
}: {
  params: Promise<{ locale: string; id: string }>;
  searchParams: Promise<{ published?: string }>;
}) {
  const { locale, id } = await params;
  const sp = await searchParams;
  setRequestLocale(locale);
  const tutor = await requireTutor(locale);
  const exam = await getExamForOwner(id, tutor.id);
  if (!exam) notFound();

  const t = await getTranslations("preview");
  const questions = await getExamQuestions(exam.id, locale);
  const settings = parseSettings(exam.settings_json);
  const shareUrl =
    exam.status === "published" && exam.share_token
      ? `${process.env.NEXT_PUBLIC_APP_URL ?? "http://localhost:3000"}/${locale}/e/${exam.share_token}`
      : null;

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <h1 className="font-display text-4xl text-[var(--ink)]">{exam.title}</h1>
          <p className="mt-1 text-[var(--muted)]">
            {exam.duration_minutes} min · {questions.length} MCQ · {exam.status}
          </p>
        </div>
        <div className="flex flex-wrap gap-2">
          <Link href="/tutor/exams" className={buttonClassName("ghost")}>
            {t("back")}
          </Link>
          {exam.status !== "published" ? (
            <form action={publishExamAction}>
              <input type="hidden" name="examId" value={exam.id} />
              <input type="hidden" name="locale" value={locale} />
              <Button type="submit">{t("publish")}</Button>
            </form>
          ) : (
            <span className="rounded-md bg-[var(--mist)] px-3 py-2 text-sm font-semibold text-[var(--lagoon)]">
              {t("published")}
            </span>
          )}
          <Link
            href={`/tutor/exams/${exam.id}/results`}
            className={buttonClassName("secondary")}
          >
            {t("results")}
          </Link>
          {shareUrl ? (
            <CopyLinkButton
              url={shareUrl}
              label={t("copyLink")}
              copiedLabel={t("copied")}
            />
          ) : null}
        </div>
      </div>

      {sp.published === "1" || shareUrl ? (
        <p className="rounded-md border border-[var(--lagoon)]/30 bg-[var(--mist)] px-4 py-3 text-sm text-[var(--ink)]">
          {t("shareHint")}
          {shareUrl ? (
            <>
              <br />
              <code className="break-all text-xs">{shareUrl}</code>
            </>
          ) : null}
        </p>
      ) : null}

      <ol className="space-y-4">
        {questions.map((q, index) => {
          const order = index + 1;
          const section = isSectionStart(settings.sections, order);
          const sectionLabel = section
            ? locale === "bn"
              ? section.labelBn
              : section.labelEn
            : null;
          return (
            <li key={q.id} className="list-none">
              {sectionLabel ? (
                <h2 className="mb-3 mt-2 font-display text-xl text-[var(--lagoon)]">
                  {t("section")}: {sectionLabel}
                </h2>
              ) : null}
              <div className="rounded-lg border border-[var(--line)] bg-white/85 px-4 py-4">
                <p className="font-medium text-[var(--ink)]">
                  {order}. {q.stem}
                </p>
                <ul className="mt-3 grid gap-1 text-sm text-[var(--muted)] sm:grid-cols-2">
                  <li>A. {q.option_a}</li>
                  <li>B. {q.option_b}</li>
                  <li>C. {q.option_c}</li>
                  <li>D. {q.option_d}</li>
                </ul>
                <p className="mt-2 text-xs font-semibold text-[var(--lagoon)]">
                  {t("answerKey")}: {q.correct}
                </p>
              </div>
            </li>
          );
        })}
      </ol>
    </div>
  );
}
