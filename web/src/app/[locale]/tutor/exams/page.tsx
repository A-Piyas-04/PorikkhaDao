import { getTranslations, setRequestLocale } from "next-intl/server";
import { Link } from "@/i18n/navigation";
import { requireTutor } from "@/lib/auth";
import { getExamQuestionCount, listExamsForTutor } from "@/lib/exams";
import { buttonClassName } from "@/components/ui/button";
import { CopyLinkButton } from "@/components/copy-link-button";

export const dynamic = "force-dynamic";

export default async function ExamsPage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  setRequestLocale(locale);
  const tutor = await requireTutor(locale);
  const t = await getTranslations("exams");
  const tp = await getTranslations("preview");
  const exams = await listExamsForTutor(tutor.id);
  const questionCounts = await Promise.all(
    exams.map((exam) => getExamQuestionCount(exam.id)),
  );

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-end justify-between gap-3">
        <h1 className="font-display text-4xl text-[var(--ink)]">{t("title")}</h1>
        <Link
          href="/tutor/exams/new"
          className={buttonClassName("primary", "relative z-10 min-h-11")}
        >
          {t("create")}
        </Link>
      </div>

      {exams.length === 0 ? (
        <p className="rounded-lg border border-dashed border-[var(--line)] bg-white/70 px-4 py-8 text-[var(--muted)]">
          {t("empty")}
        </p>
      ) : (
        <ul className="space-y-3">
          {exams.map((exam, index) => {
            const qCount = questionCounts[index];
            const shareUrl =
              exam.status === "published" && exam.share_token
                ? `${process.env.NEXT_PUBLIC_APP_URL ?? "http://localhost:3000"}/${locale}/e/${exam.share_token}`
                : null;
            return (
              <li
                key={exam.id}
                className="flex flex-col gap-3 rounded-lg border border-[var(--line)] bg-white/80 px-4 py-4 sm:flex-row sm:items-center sm:justify-between"
              >
                <div>
                  <p className="font-semibold text-[var(--ink)]">{exam.title}</p>
                  <p className="text-sm text-[var(--muted)]">
                    {exam.status === "published" ? t("statusPublished") : t("statusDraft")}
                    {" · "}
                    {t("duration", { minutes: exam.duration_minutes })}
                    {" · "}
                    {t("questions", { count: qCount })}
                  </p>
                </div>
                <div className="flex flex-wrap gap-2">
                  <Link
                    href={`/tutor/exams/${exam.id}`}
                    className={buttonClassName("secondary")}
                  >
                    {t("open")}
                  </Link>
                  <Link
                    href={`/tutor/exams/${exam.id}/results`}
                    className={buttonClassName("ghost")}
                  >
                    {t("results")}
                  </Link>
                  {shareUrl ? (
                    <CopyLinkButton
                      url={shareUrl}
                      label={t("share")}
                      copiedLabel={tp("copied")}
                    />
                  ) : null}
                </div>
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}
