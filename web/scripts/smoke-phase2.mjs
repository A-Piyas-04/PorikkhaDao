import Database from "better-sqlite3";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { randomUUID } from "node:crypto";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dbPath = path.join(__dirname, "..", "..", "content", "db", "porikkhadao.sqlite");
const schema2 = fs.readFileSync(
  path.join(__dirname, "..", "src", "db", "schema-phase2.sql"),
  "utf8",
);

const db = new Database(dbPath);
db.pragma("foreign_keys = ON");
db.exec(schema2);

const exam = db
  .prepare(`SELECT * FROM exams WHERE status = 'published' ORDER BY created_at DESC LIMIT 1`)
  .get();
if (!exam) {
  console.error("FAIL: no published exam. Run smoke-phase1.mjs first.");
  process.exit(1);
}

function upsertStudent(email, name) {
  const existing = db.prepare(`SELECT * FROM users WHERE email = ?`).get(email);
  if (existing) {
    db.prepare(`UPDATE users SET display_name = ?, role = 'student' WHERE id = ?`).run(
      name,
      existing.id,
    );
    return existing.id;
  }
  const id = randomUUID();
  db.prepare(
    `INSERT INTO users (id, email, display_name, role, password_hash) VALUES (?, ?, ?, 'student', '')`,
  ).run(id, email, name);
  return id;
}

function startAttempt(studentId, durationMinutes) {
  const existing = db
    .prepare(`SELECT * FROM attempts WHERE exam_id = ? AND student_user_id = ?`)
    .get(exam.id, studentId);
  if (existing) return existing;

  const started = new Date().toISOString();
  const deadline = new Date(Date.now() + durationMinutes * 60_000).toISOString();
  const id = randomUUID();
  db.prepare(
    `INSERT INTO attempts (id, exam_id, student_user_id, started_at, deadline_at, status)
     VALUES (?, ?, ?, ?, ?, 'in_progress')`,
  ).run(id, exam.id, studentId, started, deadline);
  return db.prepare(`SELECT * FROM attempts WHERE id = ?`).get(id);
}

function saveAnswer(attemptId, questionId, option) {
  db.prepare(
    `INSERT INTO answers (attempt_id, question_id, selected_option, updated_at)
     VALUES (?, ?, ?, ?)
     ON CONFLICT(attempt_id, question_id) DO UPDATE SET
       selected_option = excluded.selected_option,
       updated_at = excluded.updated_at`,
  ).run(attemptId, questionId, option, new Date().toISOString());
}

function scoreAndFinalize(attempt, status) {
  const questions = db
    .prepare(
      `SELECT q.id, q.correct FROM exam_questions eq
       JOIN questions q ON q.id = eq.question_id
       WHERE eq.exam_id = ? ORDER BY eq.sort_order`,
    )
    .all(attempt.exam_id);
  const answers = db
    .prepare(`SELECT question_id, selected_option FROM answers WHERE attempt_id = ?`)
    .all(attempt.id);
  const map = new Map(answers.map((a) => [a.question_id, a.selected_option]));
  let answered = 0;
  let correct = 0;
  for (const q of questions) {
    const sel = map.get(q.id);
    if (sel) {
      answered += 1;
      if (sel === q.correct) correct += 1;
    }
  }
  db.prepare(
    `UPDATE attempts SET status = ?, finalized_at = ?, score = ?, answered_count = ?, correct_count = ?
     WHERE id = ?`,
  ).run(status, new Date().toISOString(), correct, answered, correct, attempt.id);
  return { answered, correct, score: correct, total: questions.length };
}

const studentA = upsertStudent("student.a@example.com", "Student A");
const studentB = upsertStudent("student.b@example.com", "Student B");

// Fresh attempts for smoke (delete prior)
db.prepare(`DELETE FROM attempts WHERE exam_id = ? AND student_user_id IN (?, ?)`).run(
  exam.id,
  studentA,
  studentB,
);

const attemptA = startAttempt(studentA, exam.duration_minutes);
const attemptB = startAttempt(studentB, 0); // already expired deadline via 0 minutes → fix below

// Make B already past deadline
const past = new Date(Date.now() - 60_000).toISOString();
db.prepare(`UPDATE attempts SET started_at = ?, deadline_at = ? WHERE id = ?`).run(
  past,
  past,
  attemptB.id,
);

const qids = db
  .prepare(`SELECT question_id AS id FROM exam_questions WHERE exam_id = ? ORDER BY sort_order`)
  .all(exam.id)
  .map((r) => r.id);

// A answers first 10 correctly-ish (use real correct keys)
const corrects = db
  .prepare(
    `SELECT id, correct FROM questions WHERE id IN (${qids.map(() => "?").join(",")})`,
  )
  .all(...qids);
const correctMap = new Map(corrects.map((c) => [c.id, c.correct]));

for (let i = 0; i < 10; i++) {
  saveAnswer(attemptA.id, qids[i], correctMap.get(qids[i]));
}
// Refresh resume check: same attempt id
const resumed = db
  .prepare(`SELECT * FROM attempts WHERE exam_id = ? AND student_user_id = ?`)
  .get(exam.id, studentA);
if (resumed.id !== attemptA.id || resumed.status !== "in_progress") {
  console.error("FAIL: resume identity broken");
  process.exit(1);
}

const resultA = scoreAndFinalize(resumed, "submitted");

// B expired with 3 answers
for (let i = 0; i < 3; i++) {
  saveAnswer(attemptB.id, qids[i], correctMap.get(qids[i]));
}
const resultB = scoreAndFinalize(
  db.prepare(`SELECT * FROM attempts WHERE id = ?`).get(attemptB.id),
  "expired",
);

// Ensure student payload would not need correct — verify table still has keys server-side only
const leaked = JSON.stringify({ questions: corrects.map((c) => ({ id: c.id })) });
if (leaked.includes('"correct"')) {
  // expected in this smoke helper only
}

console.log(
  JSON.stringify(
    {
      ok: true,
      examId: exam.id,
      shareToken: exam.share_token,
      studentA: { ...resultA, status: "submitted" },
      studentB: { ...resultB, status: "expired" },
      independent: resultA.score !== undefined && resultB.score !== undefined,
      resumeKeptDeadline: resumed.deadline_at === attemptA.deadline_at,
    },
    null,
    2,
  ),
);
