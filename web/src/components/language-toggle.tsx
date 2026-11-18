"use client";

import { useLocale, useTranslations } from "next-intl";
import { usePathname, useRouter } from "@/i18n/navigation";

export function LanguageToggle() {
  const t = useTranslations();
  const locale = useLocale();
  const router = useRouter();
  const pathname = usePathname();

  return (
    <div className="inline-flex shrink-0 rounded-md border border-[var(--line)] bg-white p-0.5 text-xs sm:text-sm">
      <button
        type="button"
        className={`pressable rounded px-1.5 py-1 touch-manipulation sm:px-2.5 ${locale === "en" ? "bg-[var(--ink)] text-white" : "text-[var(--muted)]"}`}
        onClick={() => router.replace(pathname, { locale: "en" })}
        aria-pressed={locale === "en"}
      >
        {t("english")}
      </button>
      <button
        type="button"
        className={`pressable rounded px-1.5 py-1 touch-manipulation sm:px-2.5 ${locale === "bn" ? "bg-[var(--ink)] text-white" : "text-[var(--muted)]"}`}
        onClick={() => router.replace(pathname, { locale: "bn" })}
        aria-pressed={locale === "bn"}
      >
        {t("bangla")}
      </button>
    </div>
  );
}
