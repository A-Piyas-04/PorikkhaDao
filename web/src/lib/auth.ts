import { cookies } from "next/headers";
import { SignJWT, jwtVerify } from "jose";
import bcrypt from "bcryptjs";
import { ensureDb, sql } from "@/db";

const COOKIE = "porikkhadao_session";

export type SessionUser = {
  id: string;
  email: string;
  displayName: string;
  role: "tutor" | "student";
};

function secretKey() {
  const secret = process.env.SESSION_SECRET;
  if (!secret) {
    throw new Error("SESSION_SECRET is not set");
  }
  return new TextEncoder().encode(secret);
}

export async function createSession(user: SessionUser) {
  const token = await new SignJWT({
    email: user.email,
    displayName: user.displayName,
    role: user.role,
  })
    .setProtectedHeader({ alg: "HS256" })
    .setSubject(user.id)
    .setIssuedAt()
    .setExpirationTime("7d")
    .sign(secretKey());

  const jar = await cookies();
  jar.set(COOKIE, token, {
    httpOnly: true,
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
    path: "/",
    maxAge: 60 * 60 * 24 * 7,
  });
}

export async function destroySession() {
  const jar = await cookies();
  jar.delete(COOKIE);
}

export async function getSession(): Promise<SessionUser | null> {
  const jar = await cookies();
  const token = jar.get(COOKIE)?.value;
  if (!token) return null;

  try {
    const { payload } = await jwtVerify(token, secretKey());
    if (!payload.sub || typeof payload.email !== "string") return null;
    return {
      id: payload.sub,
      email: payload.email,
      displayName: String(payload.displayName ?? ""),
      role: payload.role === "student" ? "student" : "tutor",
    };
  } catch {
    return null;
  }
}

export async function requireTutor(locale = "en"): Promise<SessionUser> {
  const session = await getSession();
  if (!session || session.role !== "tutor") {
    const { redirect } = await import("next/navigation");
    redirect(`/${locale}/login`);
  }
  return session as SessionUser;
}

export async function verifyTutorCredentials(
  email: string,
  password: string,
): Promise<SessionUser | null> {
  await ensureDb();
  const rows = await sql()`
    SELECT id, email, display_name, role, password_hash
    FROM users WHERE email = ${email} AND role = 'tutor'
  `;
  const row = rows[0] as
    | {
        id: string;
        email: string;
        display_name: string;
        role: "tutor";
        password_hash: string;
      }
    | undefined;

  if (!row) return null;
  if (!row.password_hash || !bcrypt.compareSync(password, row.password_hash)) {
    return null;
  }

  return {
    id: row.id,
    email: row.email,
    displayName: row.display_name,
    role: "tutor",
  };
}

/** Passwordless student identify: upsert by email, refresh display name. */
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

  const existingRows = await sql()`
    SELECT id, email, display_name, role FROM users WHERE email = ${normalizedEmail}
  `;
  const existing = existingRows[0] as
    | { id: string; email: string; display_name: string; role: string }
    | undefined;

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
