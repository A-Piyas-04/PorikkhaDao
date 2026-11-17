PRAGMA foreign_keys = ON;

-- Students are passwordless until Google OAuth (after Phase 3).
-- They store password_hash as empty string '' (avoids risky users-table rebuild).

CREATE TABLE IF NOT EXISTS attempts (
  id TEXT PRIMARY KEY,
  exam_id TEXT NOT NULL REFERENCES exams(id) ON DELETE CASCADE,
  student_user_id TEXT NOT NULL REFERENCES users(id),
  started_at TEXT NOT NULL,
  deadline_at TEXT NOT NULL,
  finalized_at TEXT,
  status TEXT NOT NULL CHECK (status IN ('in_progress', 'submitted', 'expired')) DEFAULT 'in_progress',
  score INTEGER,
  answered_count INTEGER NOT NULL DEFAULT 0,
  correct_count INTEGER NOT NULL DEFAULT 0,
  UNIQUE (exam_id, student_user_id)
);

CREATE TABLE IF NOT EXISTS answers (
  attempt_id TEXT NOT NULL REFERENCES attempts(id) ON DELETE CASCADE,
  question_id INTEGER NOT NULL REFERENCES questions(id),
  selected_option TEXT CHECK (selected_option IS NULL OR selected_option IN ('A', 'B', 'C', 'D')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY (attempt_id, question_id)
);

CREATE INDEX IF NOT EXISTS idx_attempts_exam ON attempts(exam_id);
CREATE INDEX IF NOT EXISTS idx_attempts_student ON attempts(student_user_id);
CREATE INDEX IF NOT EXISTS idx_attempts_status_deadline ON attempts(status, deadline_at);
CREATE INDEX IF NOT EXISTS idx_answers_attempt ON answers(attempt_id);
