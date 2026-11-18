import { getTranslations } from "next-intl/server";
import { Link } from "@/i18n/navigation";
import { LanguageToggle } from "@/components/language-toggle";
import { BrandLockup } from "@/components/brand-lockup";
import { CreateExamLink } from "@/components/create-exam-link";
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
  const brand = locale === "bn" ? t("brandBn") : t("brand");

  return (
    <div className="min-h-screen">
      <header className="border-b border-[var(--line)] bg-[var(--paper)]/85 backdrop-blur-md">
        <div className="mx-auto flex max-w-5xl items-center justify-between gap-2 px-3 py-3 sm:gap-4 sm:px-4 sm:py-3.5">
          <BrandLockup
            locale={locale}
            brand={brand}
            tagline={t("tagline")}
            size="sm"
            className="min-w-0"
          />
          <div className="flex shrink-0 items-center gap-1.5 sm:gap-3">
            <LanguageToggle />
            {showTutorNav ? (
              <>
                <Link
                  href="/tutor/exams"
                  className="hidden text-sm font-medium text-[var(--ink)] underline-offset-4 hover:underline sm:inline"
                >
                  {t("nav.exams")}
                </Link>
                <CreateExamLink
                  plain
                  className="pressable hidden rounded-md px-1.5 py-1 text-sm font-medium text-[var(--lagoon)] underline-offset-4 hover:underline sm:inline"
                >
                  {t("nav.newExam")}
                </CreateExamLink>
                <form action={logoutAction} className="shrink-0">
                  <input type="hidden" name="locale" value={locale} />
                  <input type="hidden" name="next" value={`/${locale}/login`} />
                  <Button
                    type="submit"
                    variant="ghost"
                    className="min-h-10 whitespace-nowrap px-2.5 sm:px-4"
                  >
                    {t("nav.logout")}
                  </Button>
                </form>
              </>
            ) : null}
          </div>
        </div>
      </header>
      <main className="mx-auto max-w-5xl px-4 py-8 sm:py-10">{children}</main>
    </div>
  );
}
