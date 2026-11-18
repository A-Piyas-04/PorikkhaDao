"use client";

import { useTranslations } from "next-intl";
import { signInWithGoogleAction } from "@/actions/auth";
import { Button } from "@/components/ui/button";

export function StudentIdentifyForm({
  locale,
  token,
}: {
  locale: string;
  token: string;
}) {
  const t = useTranslations("public");

  return (
    <div className="space-y-4">
      <div>
        <h2 className="font-display text-2xl text-[var(--ink)]">{t("identifyTitle")}</h2>
        <p className="mt-1 text-sm text-[var(--muted)]">{t("identifyHint")}</p>
      </div>
      <form action={signInWithGoogleAction} className="border-t border-[var(--line)] pt-4">
        <input type="hidden" name="locale" value={locale} />
        <input type="hidden" name="intent" value="student" />
        <input type="hidden" name="next" value={`/${locale}/e/${token}`} />
        <Button type="submit" className="min-h-11 w-full touch-manipulation">
          {t("google")}
        </Button>
      </form>
    </div>
  );
}
