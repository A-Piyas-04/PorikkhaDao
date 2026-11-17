import { getTranslations } from "next-intl/server";
import { Link } from "@/i18n/navigation";
import { LanguageToggle } from "@/components/language-toggle";
import { logoutAction } from "@/actions/auth";
import { Button } from "@/components/ui/button";

export async function AppShell({
  locale,
  children,
  showTutorNav = false,
}: {
  locale: string;
  children: React.ReactNode;
  showTutorNav?: boolean;
}) {
  const t = await getTranslations();

  return (
    <div className="min-h-screen">
      <header className="border-b border-[var(--line)] bg-[var(--paper)]/90 backdrop-blur">
        <div className="mx-auto flex max-w-5xl items-center justify-between gap-4 px-4 py-4">
          <div>
            <Link href="/" className="font-display text-2xl tracking-tight text-[var(--ink)]">
              {locale === "bn" ? t("brandBn") : t("brand")}
            </Link>
            <p className="text-sm text-[var(--muted)]">{t("tagline")}</p>
          </div>
          <div className="flex items-center gap-3">
            <LanguageToggle />
            {showTutorNav ? (
              <>
                <Link
                  href="/tutor/exams"
                  className="hidden text-sm font-medium text-[var(--ink)] sm:inline"
                >
                  {t("nav.exams")}
                </Link>
                <Link
                  href="/tutor/exams/new"
                  className="hidden text-sm font-medium text-[var(--lagoon)] sm:inline"
                >
                  {t("nav.newExam")}
                </Link>
                <form action={logoutAction}>
                  <input type="hidden" name="locale" value={locale} />
                  <Button type="submit" variant="ghost">
                    {t("nav.logout")}
                  </Button>
                </form>
              </>
            ) : null}
          </div>
        </div>
      </header>
      <main className="mx-auto max-w-5xl px-4 py-8">{children}</main>
    </div>
  );
}
