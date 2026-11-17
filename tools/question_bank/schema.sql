-- PorikkhaDao Phase 0 local question bank (SQLite)
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS subjects (
  id TEXT PRIMARY KEY,
  name_en TEXT NOT NULL,
  name_bn TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS papers (
  id TEXT PRIMARY KEY,
  subject_id TEXT NOT NULL REFERENCES subjects(id),
  number INTEGER NOT NULL CHECK (number IN (1, 2)),
  name_en TEXT NOT NULL,
  name_bn TEXT NOT NULL,
  UNIQUE (subject_id, number)
);

CREATE TABLE IF NOT EXISTS chapters (
  id TEXT PRIMARY KEY,
  paper_id TEXT NOT NULL REFERENCES papers(id),
  chapter_number INTEGER NOT NULL,
  title_en TEXT NOT NULL,
  title_bn TEXT NOT NULL,
  curriculum_version TEXT NOT NULL,
  UNIQUE (paper_id, chapter_number)
);

CREATE TABLE IF NOT EXISTS topics (
  id TEXT PRIMARY KEY,
  chapter_id TEXT NOT NULL REFERENCES chapters(id),
  topic_order INTEGER NOT NULL,
  title_en TEXT NOT NULL,
  title_bn TEXT NOT NULL,
  UNIQUE (chapter_id, topic_order)
);

CREATE TABLE IF NOT EXISTS questions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  stem TEXT NOT NULL,
  option_a TEXT NOT NULL,
  option_b TEXT NOT NULL,
  option_c TEXT NOT NULL,
  option_d TEXT NOT NULL,
  correct TEXT NOT NULL CHECK (correct IN ('A', 'B', 'C', 'D')),
  difficulty TEXT CHECK (difficulty IS NULL OR difficulty IN ('easy', 'medium', 'hard')),
  qtype TEXT CHECK (qtype IS NULL OR qtype IN ('factual', 'conceptual', 'numerical', 'application')),
  source TEXT,
  explanation TEXT,
  verified INTEGER NOT NULL DEFAULT 0 CHECK (verified IN (0, 1)),
  stem_hash TEXT NOT NULL UNIQUE,
  curriculum_version TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS question_topics (
  question_id INTEGER NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
  topic_id TEXT NOT NULL REFERENCES topics(id),
  PRIMARY KEY (question_id, topic_id)
);

CREATE INDEX IF NOT EXISTS idx_questions_verified ON questions(verified);
CREATE INDEX IF NOT EXISTS idx_questions_difficulty ON questions(difficulty);
CREATE INDEX IF NOT EXISTS idx_questions_qtype ON questions(qtype);
CREATE INDEX IF NOT EXISTS idx_question_topics_topic ON question_topics(topic_id);
CREATE INDEX IF NOT EXISTS idx_topics_chapter ON topics(chapter_id);
