import bcrypt from "bcryptjs";
import postgres from "postgres";

declare global {
  // eslint-disable-next-line no-var
  var __porikkhadaoSql: ReturnType<typeof postgres> | undefined;
  // eslint-disable-next-line no-var
  var __porikkhadaoReady: Promise<void> | undefined;
}

function createSql() {
  const url = process.env.DATABASE_URL;
  if (!url) {
    throw new Error(
      "DATABASE_URL is not set. Use the Supabase Postgres connection string (Transaction pooler for Vercel).",
    );
  }

  return postgres(url, {
    // Required for Supabase transaction-mode pooler / PgBouncer.
    prepare: false,
    max: 10,
    idle_timeout: 20,
    connect_timeout: 30,
  });
}

/** Shared Postgres client (postgres.js). Safe on Vercel serverless. */
export function sql() {
  if (!globalThis.__porikkhadaoSql) {
    globalThis.__porikkhadaoSql = createSql();
  }
  return globalThis.__porikkhadaoSql;
}

async function seedTutor() {
  const email = process.env.TUTOR_EMAIL ?? "tutor@porikkhadao.local";
  const password = process.env.TUTOR_PASSWORD ?? "porikkha123";
  const name = process.env.TUTOR_NAME ?? "Demo Tutor";

  const existing = await sql()`
    SELECT id FROM users WHERE email = ${email} LIMIT 1
  `;
  if (existing.length > 0) return;

  const hash = bcrypt.hashSync(password, 10);
  await sql()`
    INSERT INTO users (id, email, display_name, role, password_hash)
    VALUES (${crypto.randomUUID()}, ${email}, ${name}, 'tutor', ${hash})
  `;
}

/** Ensures tutor seed has run once per process. */
export async function ensureDb() {
  if (!globalThis.__porikkhadaoReady) {
    globalThis.__porikkhadaoReady = seedTutor();
  }
  await globalThis.__porikkhadaoReady;
  return sql();
}

/** @deprecated Use ensureDb() / sql() — kept briefly for call-site migration. */
export async function getDb() {
  return ensureDb();
}
