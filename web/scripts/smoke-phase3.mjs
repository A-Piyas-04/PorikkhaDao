import Database from "better-sqlite3";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dbPath = path.join(__dirname, "..", "..", "content", "db", "porikkhadao.sqlite");
const db = new Database(dbPath);

const exam = db
  .prepare(
    `SELECT e.*, u.email AS owner_email
     FROM exams e
     JOIN users u ON u.id = e.owner_user_id
     WHERE e.status = 'published'
     ORDER BY e.created_at DESC LIMIT 1`,
  )
  .get();

if (!exam) {
  console.error("FAIL: no published exam");
  process.exit(1);
}

const attempts = db
  .prepare(
    `SELECT a.status, a.score, a.answered_count, a.correct_count, u.email, u.display_name
     FROM attempts a
     JOIN users u ON u.id = a.student_user_id
     WHERE a.exam_id = ?
     ORDER BY a.started_at DESC`,
  )
  .all(exam.id);

const totalQ = db
  .prepare(`SELECT COUNT(*) AS c FROM exam_questions WHERE exam_id = ?`)
  .get(exam.id).c;

const ownerOk = db
  .prepare(`SELECT id FROM exams WHERE id = ? AND owner_user_id = ?`)
  .get(exam.id, exam.owner_user_id);

const stranger = db
  .prepare(`SELECT id FROM exams WHERE id = ? AND owner_user_id = ?`)
  .get(exam.id, "not-an-owner");

console.log(
  JSON.stringify(
    {
      ok: true,
      examId: exam.id,
      title: exam.title,
      totalQuestions: totalQ,
      attemptCount: attempts.length,
      attempts: attempts.map((a) => ({
        name: a.display_name,
        email: a.email,
        status: a.status,
        score: a.score,
        answered: a.answered_count,
      })),
      ownerScoped: Boolean(ownerOk) && !stranger,
      resultsPath: `/en/tutor/exams/${exam.id}/results`,
    },
    null,
    2,
  ),
);
