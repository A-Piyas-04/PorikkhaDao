import { getTranslations, setRequestLocale } from "next-intl/server";
import { AppShell } from "@/components/app-shell";
import { BrandMark } from "@/components/brand-mark";
import { Link } from "@/i18n/navigation";
import { Button } from "@/components/ui/button";

export default async function HomePage({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations();
  const brand = locale === "bn" ? t("brandBn") : t("brand");

  return (
    <AppShell locale={locale}>
      <section className="relative overflow-hidden rounded-2xl border border-[var(--line)] bg-[var(--paper)]/70 px-6 py-12 sm:px-10 sm:py-16">
        <div
          aria-hidden
          className="pointer-events-none absolute inset-0 opacity-[0.35]"
          style={{
            backgroundImage:
              "repeating-linear-gradient(0deg, transparent, transparent 27px, rgba(201,214,222,0.55) 28px)",
            maskImage:
              "linear-gradient(90deg, transparent 0%, black 12%, black 88%, transparent 100%)",
          }}
        />
        <div className="relative max-w-xl">
          <BrandMark className="h-16 w-16 sm:h-20 sm:w-20" title={brand} />
          <h1 className="mt-6 font-display text-5xl leading-[1.05] tracking-tight text-[var(--ink)] sm:text-6xl">
            {brand}
          </h1>
          <p className="mt-4 max-w-md text-lg leading-relaxed text-[var(--muted)]">
            {t("tagline")}
          </p>
          <div className="mt-8 flex flex-wrap items-center gap-3">
            <Link href="/login">
              <Button type="button" className="min-h-11 px-5">
                {t("home.cta")}
              </Button>
            </Link>
            <p className="text-sm text-[var(--muted)]">{t("home.sub")}</p>
          </div>
        </div>
      </section>
    </AppShell>
  );
}
