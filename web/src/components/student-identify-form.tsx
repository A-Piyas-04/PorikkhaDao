"use client";

import { useActionState } from "react";
import { useTranslations } from "next-intl";
import { identifyStudentAction, type IdentifyState } from "@/actions/student";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export function StudentIdentifyForm({
  locale,
  token,
}: {
  locale: string;
  token: string;
}) {
  const t = useTranslations("public");
  const [state, action, pending] = useActionState<IdentifyState, FormData>(
    identifyStudentAction,
    {},
  );

  return (
    <form action={action} className="space-y-4">
      <input type="hidden" name="locale" value={locale} />
      <input type="hidden" name="token" value={token} />
      <h2 className="text-lg font-semibold text-[var(--ink)]">{t("identifyTitle")}</h2>
      <div>
        <Label htmlFor="name">{t("name")}</Label>
        <Input
          id="name"
          name="name"
          autoComplete="name"
          required
          className="min-h-11 text-base"
        />
      </div>
      <div>
        <Label htmlFor="email">{t("email")}</Label>
        <Input
          id="email"
          name="email"
          type="email"
          autoComplete="email"
          inputMode="email"
          required
          className="min-h-11 text-base"
        />
      </div>
      {state.error ? (
        <p className="text-sm text-red-700">
          {state.error === "tutor_email" ? t("errorTutorEmail") : t("errorMissing")}
        </p>
      ) : null}
      <Button type="submit" disabled={pending} className="min-h-11 w-full touch-manipulation">
        {t("continue")}
      </Button>
    </form>
  );
}
