import { getTranslations, setRequestLocale } from "next-intl/server";
import { notFound } from "next/navigation";
import { Link } from "@/i18n/navigation";
import { requireTutor } from "@/lib/auth";
import { getExamResultsForOwner } from "@/lib/results";
import { formatDhaka } from "@/lib/time";
import { Button } from "@/components/ui/button";
import { CopyLinkButton } from "@/components/copy-link-button";

export const dynamic = "force-dynamic";

function statusLabel(
  status: string,
  t: (key: string) => string,
): string {
  if (status === "submitted") return t("statusSubmitted");
  if (status === "expired") return t("statusExpired");
  return t("statusInProgress");
}

function statusClass(status: string): string {
  if (status === "submitted") return "bg-[var(--lagoon)]/15 text-[var(--lagoon)]";
  if (status === "expired") return "bg-amber-100 text-amber-900";
  return "bg-[var(--mist)] text-[var(--muted)]";
}

export default async function ExamResultsPage({
  params,
}: {
  params: Promise<{ locale: string; id: string }>;
}) {
  const { locale, id } = await params;
  setRequestLocale(locale);
  const tutor = await requireTutor(locale);
  const t = await getTranslations("results");
  const tp = await getTranslations("preview");

  const payload = await getExamResultsForOwner(id, tutor.id);
  if (!payload) notFound();

  const { exam, totalQuestions, attempts } = payload;
  const shareUrl =
    exam.status === "published" && exam.share_token
      ? `${process.env.NEXT_PUBLIC_APP_URL ?? "http://localhost:3000"}/${locale}/e/${exam.share_token}`
      : null;

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <p className="text-sm font-medium text-[var(--lagoon)]">{t("title")}</p>
          <h1 className="font-display text-3xl text-[var(--ink)] sm:text-4xl">
            {exam.title}
          </h1>
          <p className="mt-1 text-sm text-[var(--muted)]">
            {t("summary", { count: attempts.length, total: totalQuestions })}
          </p>
          <p className="mt-1 text-xs text-[var(--muted)]">{t("timezoneNote")}</p>
        </div>
        <div className="flex flex-wrap gap-2">
          <Link href={`/tutor/exams/${exam.id}`}>
            <Button type="button" variant="ghost">
              {t("back")}
            </Button>
          </Link>
          {shareUrl ? (
            <CopyLinkButton
              url={shareUrl}
              label={tp("copyLink")}
              copiedLabel={tp("copied")}
            />
          ) : null}
        </div>
      </div>

      {exam.status !== "published" ? (
        <p className="rounded-lg border border-dashed border-[var(--line)] bg-white/80 px-4 py-6 text-[var(--muted)]">
          {t("draftHint")}
        </p>
      ) : attempts.length === 0 ? (
        <p className="rounded-lg border border-dashed border-[var(--line)] bg-white/80 px-4 py-6 text-[var(--muted)]">
          {t("empty")}
        </p>
      ) : (
        <>
          {/* Mobile cards */}
          <ul className="space-y-3 md:hidden">
            {attempts.map((row) => (
              <li
                key={row.attemptId}
                className="rounded-xl border border-[var(--line)] bg-white/90 p-4 shadow-sm"
              >
                <div className="flex items-start justify-between gap-2">
                  <div>
                    <p className="font-semibold text-[var(--ink)]">{row.studentName}</p>
                    <p className="break-all text-sm text-[var(--muted)]">{row.studentEmail}</p>
                  </div>
                  <span
                    className={`shrink-0 rounded-full px-2.5 py-1 text-xs font-semibold ${statusClass(row.status)}`}
                  >
                    {statusLabel(row.status, t)}
                  </span>
                </div>
                <dl className="mt-3 grid grid-cols-2 gap-2 text-sm">
                  <div>
                    <dt className="text-[var(--muted)]">{t("answered")}</dt>
                    <dd className="font-medium text-[var(--ink)]">
                      {t("ofTotal", {
                        answered: row.answeredCount,
                        total: row.totalQuestions,
                      })}
                    </dd>
                  </div>
                  <div>
                    <dt className="text-[var(--muted)]">{t("score")}</dt>
                    <dd className="font-medium text-[var(--ink)]">
                      {row.score === null
                        ? "—"
                        : `${row.score} / ${row.totalQuestions}`}
                    </dd>
                  </div>
                  <div>
                    <dt className="text-[var(--muted)]">{t("started")}</dt>
                    <dd className="text-[var(--ink)]">
                      {formatDhaka(row.startedAt, locale)}
                    </dd>
                  </div>
                  <div>
                    <dt className="text-[var(--muted)]">{t("deadline")}</dt>
                    <dd className="text-[var(--ink)]">
                      {formatDhaka(row.deadlineAt, locale)}
                    </dd>
                  </div>
                  <div className="col-span-2">
                    <dt className="text-[var(--muted)]">{t("finalized")}</dt>
                    <dd className="text-[var(--ink)]">
                      {formatDhaka(row.finalizedAt, locale)}
                    </dd>
                  </div>
                </dl>
              </li>
            ))}
          </ul>

          {/* Desktop table */}
          <div className="hidden overflow-x-auto rounded-xl border border-[var(--line)] bg-white/90 md:block">
            <table className="w-full min-w-[720px] text-left text-sm">
              <thead className="border-b border-[var(--line)] bg-[var(--mist)]/80 text-[var(--muted)]">
                <tr>
                  <th className="px-4 py-3 font-medium">{t("student")}</th>
                  <th className="px-4 py-3 font-medium">{t("status")}</th>
                  <th className="px-4 py-3 font-medium">{t("answered")}</th>
                  <th className="px-4 py-3 font-medium">{t("score")}</th>
                  <th className="px-4 py-3 font-medium">{t("started")}</th>
                  <th className="px-4 py-3 font-medium">{t("deadline")}</th>
                  <th className="px-4 py-3 font-medium">{t("finalized")}</th>
                </tr>
              </thead>
              <tbody>
                {attempts.map((row) => (
                  <tr key={row.attemptId} className="border-b border-[var(--line)] last:border-0">
                    <td className="px-4 py-3">
                      <p className="font-medium text-[var(--ink)]">{row.studentName}</p>
                      <p className="text-[var(--muted)]">{row.studentEmail}</p>
                    </td>
                    <td className="px-4 py-3">
                      <span
                        className={`inline-flex rounded-full px-2.5 py-1 text-xs font-semibold ${statusClass(row.status)}`}
                      >
                        {statusLabel(row.status, t)}
                      </span>
                    </td>
                    <td className="px-4 py-3 tabular-nums text-[var(--ink)]">
                      {t("ofTotal", {
                        answered: row.answeredCount,
                        total: row.totalQuestions,
                      })}
                    </td>
                    <td className="px-4 py-3 tabular-nums font-semibold text-[var(--ink)]">
                      {row.score === null
                        ? "—"
                        : `${row.score} / ${row.totalQuestions}`}
                    </td>
                    <td className="px-4 py-3 text-[var(--muted)]">
                      {formatDhaka(row.startedAt, locale)}
                    </td>
                    <td className="px-4 py-3 text-[var(--muted)]">
                      {formatDhaka(row.deadlineAt, locale)}
                    </td>
                    <td className="px-4 py-3 text-[var(--muted)]">
                      {formatDhaka(row.finalizedAt, locale)}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}
    </div>
  );
}
