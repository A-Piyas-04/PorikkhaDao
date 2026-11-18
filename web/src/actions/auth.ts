"use server";

import { redirect } from "next/navigation";
import { destroySession, startGoogleOAuth } from "@/lib/auth";

export type AuthState = { error?: string };

export async function signInWithGoogleAction(formData: FormData) {
  const locale = String(formData.get("locale") ?? "en");
  const intentRaw = String(formData.get("intent") ?? "tutor");
  const intent = intentRaw === "student" ? "student" : "tutor";
  const nextRaw = String(formData.get("next") ?? "");
  const next =
    nextRaw.startsWith("/")
      ? nextRaw
      : intent === "tutor"
        ? `/${locale}/tutor/exams`
        : `/${locale}`;

  await startGoogleOAuth({ intent, next });
}

export async function logoutAction(formData: FormData) {
  const locale = String(formData.get("locale") ?? "en");
  const next = String(formData.get("next") ?? `/${locale}/login`);
  await destroySession();
  redirect(next.startsWith("/") ? next : `/${locale}/login`);
}
