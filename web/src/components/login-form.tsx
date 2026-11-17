"use client";

import { useActionState } from "react";
import { useTranslations } from "next-intl";
import { loginAction, type AuthState } from "@/actions/auth";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export function LoginForm({ locale }: { locale: string }) {
  const t = useTranslations("login");
  const [state, action, pending] = useActionState<AuthState, FormData>(loginAction, {});

  return (
    <form
      action={action}
      className="mx-auto max-w-md space-y-4 rounded-xl border border-[var(--line)] bg-white/80 p-6 shadow-sm"
    >
      <input type="hidden" name="locale" value={locale} />
      <h1 className="font-display text-3xl text-[var(--ink)]">{t("title")}</h1>
      <div>
        <Label htmlFor="email">{t("email")}</Label>
        <Input
          id="email"
          name="email"
          type="email"
          autoComplete="username"
          defaultValue="tutor@porikkhadao.local"
          required
        />
      </div>
      <div>
        <Label htmlFor="password">{t("password")}</Label>
        <Input
          id="password"
          name="password"
          type="password"
          autoComplete="current-password"
          defaultValue="porikkha123"
          required
        />
      </div>
      {state.error ? (
        <p className="text-sm text-red-700">
          {state.error === "missing" ? t("errorMissing") : t("errorInvalid")}
        </p>
      ) : null}
      <Button type="submit" disabled={pending} className="w-full">
        {t("submit")}
      </Button>
      <p className="text-xs text-[var(--muted)]">{t("hint")}</p>
    </form>
  );
}
