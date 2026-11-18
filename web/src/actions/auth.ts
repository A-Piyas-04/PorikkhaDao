"use server";

import { redirect } from "next/navigation";
import { destroySession, startGoogleTutorOAuth } from "@/lib/auth";

export async function signInWithGoogleAction(formData: FormData) {
  const locale = String(formData.get("locale") ?? "en");
  const nextRaw = String(formData.get("next") ?? "");
  const next = nextRaw.startsWith("/")
    ? nextRaw
    : `/${locale}/tutor/exams`;

  await startGoogleTutorOAuth(next);
}

export async function logoutAction(formData: FormData) {
  const locale = String(formData.get("locale") ?? "en");
  const next = String(formData.get("next") ?? `/${locale}/login`);
  await destroySession();
  redirect(next.startsWith("/") ? next : `/${locale}/login`);
}
