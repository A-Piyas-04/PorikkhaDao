import Database from "better-sqlite3";
import bcrypt from "bcryptjs";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { randomBytes, randomUUID } from "node:crypto";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dbPath = path.join(__dirname, "..", "..", "content", "db", "porikkhadao.sqlite");
const schemaPath = path.join(__dirname, "..", "src", "db", "schema-phase1.sql");

const db = new Database(dbPath);
db.pragma("foreign_keys = ON");
db.exec(fs.readFileSync(schemaPath, "utf8"));

const email = "tutor@porikkhadao.local";
let tutor = db.prepare("SELECT id FROM users WHERE email = ?").get(email);
if (!tutor) {
  const id = randomUUID();
  db.prepare(
    `INSERT INTO users (id, email, display_name, role, password_hash)
     VALUES (?, ?, ?, 'tutor', ?)`,
  ).run(id, email, "Demo Tutor", bcrypt.hashSync("porikkha123", 10));
  tutor = { id };
}

const topics = [
  "phy2_ch01_t01",
  "phy2_ch01_t02",
  "phy2_ch01_t03",
  "phy2_ch01_t04",
  "phy2_ch01_t05",
  "phy2_ch01_t06",
];
const ph = topics.map(() => "?").join(",");
const eligible = db
  .prepare(
    `
  SELECT q.id
  FROM questions q
  WHERE q.verified = 1
    AND EXISTS (SELECT 1 FROM question_topics qt0 WHERE qt0.question_id = q.id)
    AND NOT EXISTS (
      SELECT 1 FROM question_topics qt
      WHERE qt.question_id = q.id AND qt.topic_id NOT IN (${ph})
    )
    AND (
      SELECT COUNT(*) FROM question_topics qt3 WHERE qt3.question_id = q.id
    ) = (
      SELECT COUNT(*) FROM question_topics qt4
      WHERE qt4.question_id = q.id AND qt4.topic_id IN (${ph})
    )
`,
  )
  .all(...topics, ...topics);

if (eligible.length < 50) {
  console.error(`FAIL: eligible=${eligible.length}, need >= 50`);
  process.exit(1);
}

const picked = db
  .prepare(
    `SELECT id FROM questions WHERE id IN (${eligible.map(() => "?").join(",")})
     ORDER BY RANDOM() LIMIT 50`,
  )
  .all(...eligible.map((r) => r.id));

const examId = randomUUID();
const token = randomBytes(24).toString("hex");
const settings = JSON.stringify({
  topicIds: topics,
  difficulty: "",
  qtype: "",
  requestedCount: 50,
});

const tx = db.transaction(() => {
  db.prepare(
    `INSERT INTO exams (id, owner_user_id, title, duration_minutes, status, share_token, settings_json, published_at)
     VALUES (?, ?, ?, 30, 'published', ?, ?, datetime('now'))`,
  ).run(examId, tutor.id, "Smoke Physics 6-topic exam", token, settings);
  const insert = db.prepare(
    `INSERT INTO exam_questions (exam_id, question_id, sort_order) VALUES (?, ?, ?)`,
  );
  picked.forEach((row, i) => insert.run(examId, row.id, i + 1));
});
tx();

const qCount = db
  .prepare(`SELECT COUNT(*) AS c FROM exam_questions WHERE exam_id = ?`)
  .get(examId).c;

console.log(
  JSON.stringify(
    {
      ok: true,
      eligible: eligible.length,
      examId,
      questions: qCount,
      sharePath: `/en/e/${token}`,
    },
    null,
    2,
  ),
);
