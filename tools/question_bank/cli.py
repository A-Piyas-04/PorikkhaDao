#!/usr/bin/env python3
"""PorikkhaDao Phase 0 question-bank CLI (SQLite + CSV)."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
import sys
from pathlib import Path
from typing import Iterable

from paths import (
    CSV_HEADERS,
    DB_DIR,
    DB_PATH,
    SCHEMA_PATH,
    SYLLABUS_PATH,
    TEMPLATE_PATH,
)


def normalize_stem(stem: str) -> str:
    text = stem.strip().lower()
    text = re.sub(r"\s+", " ", text)
    return text


def stem_hash(stem: str) -> str:
    return hashlib.sha256(normalize_stem(stem).encode("utf-8")).hexdigest()


def connect(db_path: Path = DB_PATH) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def cmd_init(_args: argparse.Namespace) -> int:
    schema = SCHEMA_PATH.read_text(encoding="utf-8")
    with connect() as conn:
        conn.executescript(schema)
    print(f"Initialized schema at {DB_PATH}")
    return 0


def load_syllabus(path: Path = SYLLABUS_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def cmd_seed_syllabus(_args: argparse.Namespace) -> int:
    data = load_syllabus()
    curriculum = data["curriculum_version"]
    subject = data["subject"]
    paper = data["paper"]
    paper_id = f"{subject['id']}_p{paper['number']}"

    with connect() as conn:
        conn.execute(
            "INSERT OR REPLACE INTO subjects (id, name_en, name_bn) VALUES (?, ?, ?)",
            (subject["id"], subject["name_en"], subject["name_bn"]),
        )
        conn.execute(
            """
            INSERT OR REPLACE INTO papers (id, subject_id, number, name_en, name_bn)
            VALUES (?, ?, ?, ?, ?)
            """,
            (paper_id, subject["id"], paper["number"], paper["name_en"], paper["name_bn"]),
        )
        for chapter in data["chapters"]:
            conn.execute(
                """
                INSERT OR REPLACE INTO chapters
                (id, paper_id, chapter_number, title_en, title_bn, curriculum_version)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    chapter["id"],
                    paper_id,
                    chapter["number"],
                    chapter["title_en"],
                    chapter["title_bn"],
                    curriculum,
                ),
            )
            for topic in chapter["topics"]:
                conn.execute(
                    """
                    INSERT OR REPLACE INTO topics
                    (id, chapter_id, topic_order, title_en, title_bn)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        topic["id"],
                        chapter["id"],
                        topic["order"],
                        topic["title_en"],
                        topic["title_bn"],
                    ),
                )
        conn.commit()

    topic_count = sum(len(ch["topics"]) for ch in data["chapters"])
    print(
        f"Seeded syllabus: subject={subject['id']}, paper={paper['number']}, "
        f"chapters={len(data['chapters'])}, topics={topic_count}"
    )
    return 0


def parse_verified(value: str) -> int | None:
    raw = (value or "").strip().lower()
    if raw in {"1", "true", "yes", "y"}:
        return 1
    if raw in {"0", "false", "no", "n", ""}:
        return 0
    return None


def known_topic_ids(conn: sqlite3.Connection) -> set[str]:
    rows = conn.execute("SELECT id FROM topics").fetchall()
    return {row["id"] for row in rows}


def validate_row(
    row: dict[str, str],
    line_no: int,
    known_topics: set[str],
    seen_hashes: set[str],
) -> list[str]:
    errors: list[str] = []
    stem = (row.get("stem") or "").strip()
    if not stem:
        errors.append(f"L{line_no}: missing stem")

    for key in ("option_a", "option_b", "option_c", "option_d"):
        if not (row.get(key) or "").strip():
            errors.append(f"L{line_no}: missing {key}")

    correct = (row.get("correct") or "").strip().upper()
    if correct not in {"A", "B", "C", "D"}:
        errors.append(f"L{line_no}: correct must be A/B/C/D")

    topic_raw = (row.get("topic_ids") or "").strip()
    if not topic_raw:
        errors.append(f"L{line_no}: missing topic_ids")
        topic_ids: list[str] = []
    else:
        topic_ids = [t.strip() for t in topic_raw.replace(",", ";").split(";") if t.strip()]
        if not topic_ids:
            errors.append(f"L{line_no}: empty topic_ids")
        for tid in topic_ids:
            if tid not in known_topics:
                errors.append(f"L{line_no}: unknown topic_id '{tid}'")

    difficulty = (row.get("difficulty") or "").strip().lower()
    if difficulty and difficulty not in {"easy", "medium", "hard"}:
        errors.append(f"L{line_no}: invalid difficulty '{difficulty}'")

    qtype = (row.get("type") or "").strip().lower()
    if qtype and qtype not in {"factual", "conceptual", "numerical", "application"}:
        errors.append(f"L{line_no}: invalid type '{qtype}'")

    verified = parse_verified(row.get("verified") or "")
    if verified is None:
        errors.append(f"L{line_no}: verified must be true/false or 1/0")

    if stem:
        h = stem_hash(stem)
        if h in seen_hashes:
            errors.append(f"L{line_no}: duplicate stem (normalized)")
        else:
            seen_hashes.add(h)

    return errors


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise SystemExit(f"CSV has no header: {path}")
        missing = [h for h in CSV_HEADERS if h not in reader.fieldnames]
        if missing:
            raise SystemExit(f"CSV missing columns {missing}: {path}")
        return [dict(row) for row in reader]


def cmd_validate(args: argparse.Namespace) -> int:
    csv_path = Path(args.csv)
    with connect() as conn:
        topics = known_topic_ids(conn)
        if not topics:
            print("No topics in DB. Run: python cli.py seed-syllabus", file=sys.stderr)
            return 1
        rows = read_csv_rows(csv_path)
        seen: set[str] = set()
        all_errors: list[str] = []
        for i, row in enumerate(rows, start=2):
            all_errors.extend(validate_row(row, i, topics, seen))

    if all_errors:
        print(f"VALIDATION FAILED ({len(all_errors)} issues) for {csv_path}")
        for err in all_errors[:50]:
            print(f"  - {err}")
        if len(all_errors) > 50:
            print(f"  ... and {len(all_errors) - 50} more")
        return 1

    print(f"VALIDATION OK: {len(rows)} rows in {csv_path}")
    return 0


def cmd_import(args: argparse.Namespace) -> int:
    csv_path = Path(args.csv)
    if cmd_validate(args) != 0:
        return 1

    curriculum = load_syllabus()["curriculum_version"]
    rows = read_csv_rows(csv_path)
    inserted = 0
    skipped = 0

    with connect() as conn:
        for row in rows:
            verified = parse_verified(row.get("verified") or "") or 0
            if args.verified_only and verified != 1:
                skipped += 1
                continue

            h = stem_hash(row["stem"])
            existing = conn.execute(
                "SELECT id FROM questions WHERE stem_hash = ?", (h,)
            ).fetchone()
            if existing:
                skipped += 1
                continue

            difficulty = (row.get("difficulty") or "").strip().lower() or None
            qtype = (row.get("type") or "").strip().lower() or None
            cur = conn.execute(
                """
                INSERT INTO questions (
                  stem, option_a, option_b, option_c, option_d, correct,
                  difficulty, qtype, source, explanation, verified, stem_hash, curriculum_version
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    row["stem"].strip(),
                    row["option_a"].strip(),
                    row["option_b"].strip(),
                    row["option_c"].strip(),
                    row["option_d"].strip(),
                    row["correct"].strip().upper(),
                    difficulty,
                    qtype,
                    (row.get("source") or "").strip() or None,
                    (row.get("explanation") or "").strip() or None,
                    verified,
                    h,
                    curriculum,
                ),
            )
            qid = cur.lastrowid
            topic_ids = [
                t.strip()
                for t in (row.get("topic_ids") or "").replace(",", ";").split(";")
                if t.strip()
            ]
            for tid in topic_ids:
                conn.execute(
                    "INSERT OR IGNORE INTO question_topics (question_id, topic_id) VALUES (?, ?)",
                    (qid, tid),
                )
            inserted += 1
        conn.commit()

    print(f"IMPORT DONE: inserted={inserted}, skipped={skipped}, file={csv_path}")
    return 0


def parse_topic_list(raw: str | None) -> list[str]:
    if not raw:
        return []
    return [t.strip() for t in raw.replace(",", ";").split(";") if t.strip()]


def eligible_question_ids(
    conn: sqlite3.Connection,
    include_topics: list[str],
    *,
    verified_only: bool = True,
) -> list[int]:
    """Strict filter: all of a question's topic tags must be in include_topics."""
    if not include_topics:
        return []

    placeholders = ",".join("?" for _ in include_topics)
    verified_clause = "AND q.verified = 1" if verified_only else ""
    sql = f"""
        SELECT q.id
        FROM questions q
        WHERE 1=1 {verified_clause}
          AND NOT EXISTS (
            SELECT 1
            FROM question_topics qt
            WHERE qt.question_id = q.id
              AND qt.topic_id NOT IN ({placeholders})
          )
          AND EXISTS (
            SELECT 1 FROM question_topics qt2 WHERE qt2.question_id = q.id
          )
          AND (
            SELECT COUNT(*) FROM question_topics qt3 WHERE qt3.question_id = q.id
          ) = (
            SELECT COUNT(*) FROM question_topics qt4
            WHERE qt4.question_id = q.id AND qt4.topic_id IN ({placeholders})
          )
    """
    params = list(include_topics) + list(include_topics)
    rows = conn.execute(sql, params).fetchall()
    return [int(r["id"]) for r in rows]


def cmd_count(args: argparse.Namespace) -> int:
    include = parse_topic_list(args.topics)
    if not include:
        print("Provide --topics id1;id2;...", file=sys.stderr)
        return 1

    with connect() as conn:
        missing = [t for t in include if t not in known_topic_ids(conn)]
        if missing:
            print(f"Unknown topics: {missing}", file=sys.stderr)
            return 1
        ids = eligible_question_ids(conn, include, verified_only=not args.include_unverified)
        print(f"eligible_count={len(ids)}")
        print("include_topics=" + ";".join(include))
        if args.show_ids:
            print("question_ids=" + ",".join(str(i) for i in ids))
    return 0


def cmd_stats(_args: argparse.Namespace) -> int:
    with connect() as conn:
        subjects = conn.execute("SELECT COUNT(*) AS c FROM subjects").fetchone()["c"]
        papers = conn.execute("SELECT COUNT(*) AS c FROM papers").fetchone()["c"]
        chapters = conn.execute("SELECT COUNT(*) AS c FROM chapters").fetchone()["c"]
        topics = conn.execute("SELECT COUNT(*) AS c FROM topics").fetchone()["c"]
        total_q = conn.execute("SELECT COUNT(*) AS c FROM questions").fetchone()["c"]
        verified_q = conn.execute(
            "SELECT COUNT(*) AS c FROM questions WHERE verified = 1"
        ).fetchone()["c"]
        print(
            f"subjects={subjects} papers={papers} chapters={chapters} topics={topics} "
            f"questions={total_q} verified={verified_q}"
        )
        rows = conn.execute(
            """
            SELECT t.id, t.title_en, COUNT(qt.question_id) AS qcount
            FROM topics t
            LEFT JOIN question_topics qt ON qt.topic_id = t.id
            LEFT JOIN questions q ON q.id = qt.question_id AND q.verified = 1
            GROUP BY t.id
            ORDER BY t.id
            """
        ).fetchall()
        print("verified_questions_per_topic:")
        for row in rows:
            # recount verified only
            count = conn.execute(
                """
                SELECT COUNT(DISTINCT q.id) AS c
                FROM questions q
                JOIN question_topics qt ON qt.question_id = q.id
                WHERE qt.topic_id = ? AND q.verified = 1
                """,
                (row["id"],),
            ).fetchone()["c"]
            print(f"  {row['id']}: {count}  ({row['title_en']})")
    return 0


def cmd_write_template(_args: argparse.Namespace) -> int:
    TEMPLATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with TEMPLATE_PATH.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_HEADERS)
        writer.writeheader()
    print(f"Wrote template {TEMPLATE_PATH}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="PorikkhaDao question-bank tools")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init-db", help="Create SQLite schema")
    p_init.set_defaults(func=cmd_init)

    p_seed = sub.add_parser("seed-syllabus", help="Load Physics 2nd Paper syllabus JSON")
    p_seed.set_defaults(func=cmd_seed_syllabus)

    p_tpl = sub.add_parser("write-template", help="Write empty CSV import template")
    p_tpl.set_defaults(func=cmd_write_template)

    p_val = sub.add_parser("validate", help="Validate a questions CSV")
    p_val.add_argument("--csv", required=True)
    p_val.set_defaults(func=cmd_validate)

    p_imp = sub.add_parser("import", help="Validate and import a questions CSV")
    p_imp.add_argument("--csv", required=True)
    p_imp.add_argument(
        "--verified-only",
        action="store_true",
        help="Skip rows with verified=false",
    )
    p_imp.set_defaults(func=cmd_import)

    p_count = sub.add_parser("count", help="Eligible verified question count for topics")
    p_count.add_argument("--topics", required=True, help="Semicolon-separated topic IDs")
    p_count.add_argument("--include-unverified", action="store_true")
    p_count.add_argument("--show-ids", action="store_true")
    p_count.set_defaults(func=cmd_count)

    p_stats = sub.add_parser("stats", help="Bank summary")
    p_stats.set_defaults(func=cmd_stats)

    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    DB_DIR.mkdir(parents=True, exist_ok=True)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
