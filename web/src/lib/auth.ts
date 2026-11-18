import { ensureDb, sql } from "@/db";
import { createClient } from "@/lib/supabase/server";
import { appOrigin } from "@/lib/supabase/env";

export type SessionUser = {
  id: string;
  email: string;
  displayName: string;
  role: "tutor" | "student";
};

export type AuthIntent = "tutor" | "student";

function tutorEmailSet(): Set<string> {
  const raw = process.env.TUTOR_EMAILS || process.env.TUTOR_EMAIL || "";
  return new Set(
    raw
      .split(",")
      .map((value) => value.trim().toLowerCase())
      .filter(Boolean),
  );
}

export function isTutorEmail(email: string): boolean {
  return tutorEmailSet().has(email.trim().toLowerCase());
}

type AuthProfile = {
  id: string;
  email: string;
  displayName: string;
};

function profileFromAuthUser(user: {
  id: string;
  email?: string | null;
  user_metadata?: Record<string, unknown>;
}): AuthProfile {
  const email = (user.email ?? "").trim().toLowerCase();
  if (!email) throw new Error("MISSING_EMAIL");

  const meta = user.user_metadata ?? {};
  const displayName = String(
    meta.full_name ?? meta.name ?? meta.user_name ?? email.split("@")[0],
  );

  return { id: user.id, email, displayName };
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

/** Upsert app `users` row after Google sign-in. */
export async function syncAppUser(
  authUser: {
    id: string;
    email?: string | null;
    user_metadata?: Record<string, unknown>;
  },
  intent: AuthIntent,
): Promise<SessionUser> {
  const profile = profileFromAuthUser(authUser);
  const allowlisted = isTutorEmail(profile.email);
  const existing = await findAppUserByEmail(profile.email);

  if (existing) {
    const role: "tutor" | "student" = allowlisted ? "tutor" : existing.role;

    if (intent === "tutor" && role !== "tutor") {
      throw new Error("NOT_TUTOR");
    }
    if (intent === "student" && role === "tutor") {
      throw new Error("EMAIL_IS_TUTOR");
    }

    await sql()`
      UPDATE users
      SET display_name = ${profile.displayName},
          role = ${role}
      WHERE id = ${existing.id}
    `;

    return {
      id: existing.id,
      email: existing.email,
      displayName: profile.displayName,
      role,
    };
  }

  const role: "tutor" | "student" = allowlisted ? "tutor" : "student";
  if (intent === "tutor" && role !== "tutor") {
    throw new Error("NOT_TUTOR");
  }
  if (intent === "student" && role === "tutor") {
    throw new Error("EMAIL_IS_TUTOR");
  }

  await sql()`
    INSERT INTO users (id, email, display_name, role, password_hash)
    VALUES (${profile.id}, ${profile.email}, ${profile.displayName}, ${role}, '')
  `;

  return {
    id: profile.id,
    email: profile.email,
    displayName: profile.displayName,
    role,
  };
}

export async function getSession(): Promise<SessionUser | null> {
  const supabase = await createClient();
  const { data, error } = await supabase.auth.getUser();
  if (error || !data.user?.email) return null;

  const email = data.user.email.trim().toLowerCase();
  const existing = await findAppUserByEmail(email);
  if (!existing) return null;

  const allowlisted = isTutorEmail(email);
  const role: "tutor" | "student" = allowlisted ? "tutor" : existing.role;
  const displayName =
    String(
      data.user.user_metadata?.full_name ??
        data.user.user_metadata?.name ??
        existing.display_name,
    ) || existing.display_name;

  return {
    id: existing.id,
    email: existing.email,
    displayName,
    role,
  };
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
  const supabase = await createClient();
  await supabase.auth.signOut();
}

export async function startGoogleOAuth(input: {
  intent: AuthIntent;
  next: string;
}) {
  const next = input.next.startsWith("/") ? input.next : "/";
  const redirectTo = `${appOrigin()}/auth/callback?next=${encodeURIComponent(next)}&intent=${input.intent}`;

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
