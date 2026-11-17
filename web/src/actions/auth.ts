"use server";

import { redirect } from "next/navigation";
import {
  createSession,
  destroySession,
  verifyTutorCredentials,
} from "@/lib/auth";

export type AuthState = { error?: string };

export async function loginAction(
  _prev: AuthState,
  formData: FormData,
): Promise<AuthState> {
  const email = String(formData.get("email") ?? "").trim();
  const password = String(formData.get("password") ?? "");
  const locale = String(formData.get("locale") ?? "en");

  if (!email || !password) {
    return { error: "missing" };
  }

  const user = verifyTutorCredentials(email, password);
  if (!user) {
    return { error: "invalid" };
  }

  await createSession(user);
  redirect(`/${locale}/tutor/exams`);
}

export async function logoutAction(formData: FormData) {
  const locale = String(formData.get("locale") ?? "en");
  await destroySession();
  redirect(`/${locale}/login`);
}
