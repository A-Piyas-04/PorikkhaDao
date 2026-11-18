import postgres from "postgres";

declare global {
  // eslint-disable-next-line no-var
  var __porikkhadaoSql: ReturnType<typeof postgres> | undefined;
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

/** Ensures DB client is ready. Tutor accounts are created via Google OAuth. */
export async function ensureDb() {
  return sql();
}

/** @deprecated Use ensureDb() / sql(). */
export async function getDb() {
  return ensureDb();
}
