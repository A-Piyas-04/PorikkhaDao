import { cookies } from "next/headers";
import { SignJWT, jwtVerify } from "jose";
import { ensureDb, sql } from "@/db";
import { createClient } from "@/lib/supabase/server";
import { appOrigin } from "@/lib/supabase/env";

const STUDENT_COOKIE = "porikkhadao_student";

export type SessionUser = {
  id: string;
  email: string;
  displayName: string;
  role: "tutor" | "student";
};

function studentSecretKey() {
  const secret =
    process.env.SESSION_SECRET ||
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY ||
    "dev-student-session-secret";
  return new TextEncoder().encode(secret);
}

async function findAppUserByEmail(email: string) {
  await ensureDb();
  const rows = await sql()`
    SELECT id, email, display_name, role
    FROM users WHERE email = ${email}
    LIMIT 1
  `;
  return rows[0] as
    | {
        id: string;
        email: string;
        display_name: string;
        role: "tutor" | "student";
      }
    | undefined;
}

/** Any Google account that signs in via tutor login becomes a tutor. */
export async function syncTutorFromGoogle(authUser: {
  id: string;
  email?: string | null;
  user_metadata?: Record<string, unknown>;
}): Promise<SessionUser> {
  const email = (authUser.email ?? "").trim().toLowerCase();
  if (!email) throw new Error("MISSING_EMAIL");

  const meta = authUser.user_metadata ?? {};
  const displayName = String(
    meta.full_name ?? meta.name ?? meta.user_name ?? email.split("@")[0],
  );

  const existing = await findAppUserByEmail(email);
  if (existing) {
    await sql()`
      UPDATE users
      SET display_name = ${displayName},
          role = 'tutor'
      WHERE id = ${existing.id}
    `;
    return {
      id: existing.id,
      email: existing.email,
      displayName,
      role: "tutor",
    };
  }

  await sql()`
    INSERT INTO users (id, email, display_name, role, password_hash)
    VALUES (${authUser.id}, ${email}, ${displayName}, 'tutor', '')
  `;

  return {
    id: authUser.id,
    email,
    displayName,
    role: "tutor",
  };
}

/** Passwordless student on exam link: name + email, no Google. */
export async function identifyStudent(
  name: string,
  email: string,
): Promise<SessionUser> {
  await ensureDb();
  const normalizedEmail = email.trim().toLowerCase();
  const displayName = name.trim();
  if (!normalizedEmail || !displayName) {
    throw new Error("MISSING_IDENTITY");
  }

  const existing = await findAppUserByEmail(normalizedEmail);
  if (existing) {
    if (existing.role === "tutor") {
      throw new Error("EMAIL_IS_TUTOR");
    }
    await sql()`
      UPDATE users SET display_name = ${displayName} WHERE id = ${existing.id}
    `;
    return {
      id: existing.id,
      email: existing.email,
      displayName,
      role: "student",
    };
  }

  const id = crypto.randomUUID();
  await sql()`
    INSERT INTO users (id, email, display_name, role, password_hash)
    VALUES (${id}, ${normalizedEmail}, ${displayName}, 'student', '')
  `;

  return {
    id,
    email: normalizedEmail,
    displayName,
    role: "student",
  };
}

export async function createStudentSession(user: SessionUser) {
  const token = await new SignJWT({
    email: user.email,
    displayName: user.displayName,
    role: "student",
  })
    .setProtectedHeader({ alg: "HS256" })
    .setSubject(user.id)
    .setIssuedAt()
    .setExpirationTime("12h")
    .sign(studentSecretKey());

  const jar = await cookies();
  jar.set(STUDENT_COOKIE, token, {
    httpOnly: true,
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
    path: "/",
    maxAge: 60 * 60 * 12,
  });
}

async function getStudentCookieSession(): Promise<SessionUser | null> {
  const jar = await cookies();
  const token = jar.get(STUDENT_COOKIE)?.value;
  if (!token) return null;

  try {
    const { payload } = await jwtVerify(token, studentSecretKey());
    if (!payload.sub || typeof payload.email !== "string") return null;
    if (payload.role !== "student") return null;
    return {
      id: payload.sub,
      email: payload.email,
      displayName: String(payload.displayName ?? ""),
      role: "student",
    };
  } catch {
    return null;
  }
}

async function getTutorSession(): Promise<SessionUser | null> {
  const supabase = await createClient();
  const { data, error } = await supabase.auth.getUser();
  if (error || !data.user?.email) return null;

  const email = data.user.email.trim().toLowerCase();
  const existing = await findAppUserByEmail(email);
  if (!existing || existing.role !== "tutor") return null;

  const displayName = String(
    data.user.user_metadata?.full_name ??
      data.user.user_metadata?.name ??
      existing.display_name,
  );

  return {
    id: existing.id,
    email: existing.email,
    displayName,
    role: "tutor",
  };
}

export async function getSession(): Promise<SessionUser | null> {
  const tutor = await getTutorSession();
  if (tutor) return tutor;
  return getStudentCookieSession();
}

export async function requireTutor(locale = "en"): Promise<SessionUser> {
  const session = await getSession();
  if (!session || session.role !== "tutor") {
    const { redirect } = await import("next/navigation");
    redirect(`/${locale}/login`);
  }
  return session as SessionUser;
}

export async function requireStudent(
  locale = "en",
  returnTo?: string,
): Promise<SessionUser> {
  const session = await getSession();
  if (!session || session.role !== "student") {
    const { redirect } = await import("next/navigation");
    redirect(returnTo ?? `/${locale}`);
  }
  return session as SessionUser;
}

export async function destroySession() {
  const jar = await cookies();
  jar.delete(STUDENT_COOKIE);
  try {
    const supabase = await createClient();
    await supabase.auth.signOut();
  } catch {
    // Supabase may be unconfigured in some local edge cases
  }
}

export async function startGoogleTutorOAuth(next: string) {
  const safeNext = next.startsWith("/") ? next : "/";
  const redirectTo = `${appOrigin()}/auth/callback?next=${encodeURIComponent(safeNext)}`;

  const supabase = await createClient();
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: "google",
    options: {
      redirectTo,
      queryParams: {
        access_type: "offline",
        prompt: "select_account",
      },
    },
  });

  if (error || !data.url) {
    throw new Error(error?.message || "OAUTH_START_FAILED");
  }

  const { redirect } = await import("next/navigation");
  redirect(data.url);
}
