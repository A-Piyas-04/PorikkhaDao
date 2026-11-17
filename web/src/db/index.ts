import fs from "node:fs";
import path from "node:path";
import Database from "better-sqlite3";
import bcrypt from "bcryptjs";
import { getDbPath } from "./path";

declare global {
  // eslint-disable-next-line no-var
  var __porikkhadaoDb: Database.Database | undefined;
}

function migrate(db: Database.Database) {
  const schemaPath = path.join(process.cwd(), "src", "db", "schema-phase1.sql");
  const sql = fs.readFileSync(schemaPath, "utf8");
  db.exec(sql);
}

function seedTutor(db: Database.Database) {
  const email = process.env.TUTOR_EMAIL ?? "tutor@porikkhadao.local";
  const password = process.env.TUTOR_PASSWORD ?? "porikkha123";
  const name = process.env.TUTOR_NAME ?? "Demo Tutor";
  const existing = db.prepare("SELECT id FROM users WHERE email = ?").get(email);
  if (existing) return;

  const hash = bcrypt.hashSync(password, 10);
  db.prepare(
    `INSERT INTO users (id, email, display_name, role, password_hash)
     VALUES (?, ?, ?, 'tutor', ?)`,
  ).run(crypto.randomUUID(), email, name, hash);
}

export function getDb() {
  if (globalThis.__porikkhadaoDb) {
    return globalThis.__porikkhadaoDb;
  }

  const dbPath = getDbPath();
  if (!fs.existsSync(dbPath)) {
    throw new Error(
      `SQLite bank not found at ${dbPath}. Run Phase 0 tools first (init-db, seed-syllabus, import).`,
    );
  }

  const db = new Database(dbPath);
  db.pragma("foreign_keys = ON");
  migrate(db);
  seedTutor(db);
  globalThis.__porikkhadaoDb = db;
  return db;
}
