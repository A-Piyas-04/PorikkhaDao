import { getTranslations, setRequestLocale } from "next-intl/server";
import { AppShell } from "@/components/app-shell";
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

  return (
    <AppShell locale={locale}>
      <section className="max-w-2xl py-10">
        <p className="font-display text-5xl leading-tight text-[var(--ink)]">
          {locale === "bn" ? t("brandBn") : t("brand")}
        </p>
        <p className="mt-4 text-lg text-[var(--muted)]">{t("tagline")}</p>
        <div className="mt-8">
          <Link href="/login">
            <Button type="button">{t("home.cta")}</Button>
          </Link>
        </div>
      </section>
    </AppShell>
  );
}
