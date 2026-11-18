#!/usr/bin/env python3
"""PorikkhaDao question-bank pipeline CLI.

Subcommands (run from repo root):

  python tools/question_bank/pipeline/bank.py status
      Coverage: authored vs. target per topic/paper, duplicates, invalid rows.

  python tools/question_bank/pipeline/bank.py validate
      Structural + bilingual + global de-dup check over all topic JSONL.
      Non-zero exit if anything is invalid or duplicated.

  python tools/question_bank/pipeline/bank.py export
      Rebuild content/bank/import/<subject>_<paper>_chNN.csv (app import
      template), content/bank/bank.json (consolidated), and manifest.json.
      Only validated, de-duplicated questions are exported.

  python tools/question_bank/pipeline/bank.py import [--db PATH] [--limit-per-topic N]
      Seed all in-scope syllabi and load validated questions into the app
      SQLite bank with verified=1 so they are live in the app.

The topic JSONL files under content/bank/topics/ are the source of truth and
the resumable checkpoint; every command here is safe to re-run.
"""
from __future__ import annotations

import argparse
import csv
import json
import sqlite3
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import core  # noqa: E402


def _gather(limit_per_topic: int | None = None):
    """Return (rows_by_topic, errors, dup_count).

    rows_by_topic[topic_id] = list of valid, de-duplicated authored records.
    errors = list of (topic_id, line_no, reason).
    """
    seen: set[str] = set()
    rows_by_topic: dict[str, list[dict]] = {}
    errors: list[tuple[str, int, str]] = []
    dups = 0
    for _, _, topic in core.iter_topics():
        tid = topic["id"]
        kept: list[dict] = []
        for i, q in enumerate(core.read_jsonl(core.topic_path(tid)), 1):
            err = core.validate_record(q)
            if err:
                errors.append((tid, i, err))
                continue
            k = core.stem_key(q["stem_en"])
            if k in seen:
                dups += 1
                continue
            seen.add(k)
            kept.append(q)
            if limit_per_topic and len(kept) >= limit_per_topic:
                break
        rows_by_topic[tid] = kept
    return rows_by_topic, errors, dups


def cmd_status(args: argparse.Namespace) -> int:
    rows_by_topic, errors, dups = _gather()
    target = args.target
    per_paper: dict[str, Counter] = {}
    topic_meta = {t["id"]: (d, t) for d, _, t in core.iter_topics()}
    for tid, rows in rows_by_topic.items():
        data = topic_meta[tid][0]
        key = f"{data['subject']['id']} p{data['paper']['number']}"
        per_paper.setdefault(key, Counter())
        per_paper[key]["authored"] += len(rows)
        per_paper[key]["topics"] += 1
        per_paper[key]["complete"] += 1 if len(rows) >= target else 0
    total = sum(len(r) for r in rows_by_topic.values())
    print(f"{'paper':22} {'topics':>6} {'complete':>9} {'authored':>9}  (target {target}/topic)")
    for key in sorted(per_paper):
        c = per_paper[key]
        print(f"{key:22} {c['topics']:>6} {c['complete']:>9} {c['authored']:>9}")
    print("-" * 52)
    print(f"{'TOTAL':22} {len(rows_by_topic):>6} "
          f"{sum(1 for r in rows_by_topic.values() if len(r) >= target):>9} {total:>9}")
    print(f"\ninvalid rows: {len(errors)}   duplicates skipped: {dups}")
    if errors[:10]:
        print("first invalid rows:")
        for tid, ln, reason in errors[:10]:
            print(f"  {tid} line {ln}: {reason}")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    _, errors, dups = _gather()
    if errors:
        for tid, ln, reason in errors:
            print(f"INVALID {tid} line {ln}: {reason}", file=sys.stderr)
    print(f"invalid: {len(errors)}   duplicates: {dups}")
    return 1 if errors else 0


def cmd_export(args: argparse.Namespace) -> int:
    rows_by_topic, errors, dups = _gather(args.limit_per_topic)
    if errors and not args.allow_invalid:
        print(f"Refusing to export: {len(errors)} invalid rows. "
              f"Run `validate` or pass --allow-invalid.", file=sys.stderr)
        return 1
    core.IMPORT_DIR.mkdir(parents=True, exist_ok=True)
    consolidated: list[dict] = []
    manifest_topics: dict[str, int] = {}
    for data in core.load_syllabi():
        subject, paper = data["subject"]["id"], data["paper"]["number"]
        for chapter in data["chapters"]:
            csv_rows = []
            for topic in chapter["topics"]:
                tid = topic["id"]
                for q in rows_by_topic.get(tid, []):
                    verified = q.get("verified", True)
                    if isinstance(verified, str):
                        verified = verified.strip().lower() in {"1", "true", "yes"}
                    csv_rows.append(core.to_csv_row(q, tid, verified=bool(verified)))
                    consolidated.append({"topic_id": tid, "chapter_id": chapter["id"],
                                         "subject": subject, "paper": paper, **q})
                manifest_topics[tid] = len(rows_by_topic.get(tid, []))
            name = f"{subject}_{paper}_ch{chapter['number']:02d}.csv"
            with (core.IMPORT_DIR / name).open("w", encoding="utf-8", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=core.CSV_HEADERS)
                w.writeheader()
                w.writerows(csv_rows)
    (core.BANK / "bank.json").write_text(
        json.dumps(consolidated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    target = args.target
    manifest = {
        "target_per_topic": target,
        "total_topics": len(manifest_topics),
        "authored_questions": sum(manifest_topics.values()),
        "complete_topics": sum(n >= target for n in manifest_topics.values()),
        "missing_questions": sum(max(0, target - n) for n in manifest_topics.values()),
        "verified_for_app": sum(manifest_topics.values()),
        "invalid_skipped": len(errors),
        "duplicates_skipped": dups,
        "topic_counts": manifest_topics,
    }
    (core.BANK / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Exported {manifest['authored_questions']} questions across "
          f"{len(manifest_topics)} topics -> {core.IMPORT_DIR}")
    print(f"  bank.json + manifest.json written to {core.BANK}")
    return 0


def _seed_syllabi(conn: sqlite3.Connection) -> None:
    """Add in-scope syllabus hierarchy. Non-destructive: INSERT OR IGNORE keeps
    any existing rows (e.g. dev exams wired to old pilot data) intact, and the
    2027 IDs are a distinct namespace so new rows insert cleanly."""
    for data in core.load_syllabi():
        subj, paper = data["subject"], data["paper"]
        paper_id = f"{subj['id']}_p{paper['number']}"
        conn.execute("INSERT OR IGNORE INTO subjects (id, name_en, name_bn) VALUES (?,?,?)",
                     (subj["id"], subj["name_en"], subj["name_bn"]))
        conn.execute("INSERT OR IGNORE INTO papers (id, subject_id, number, name_en, name_bn) "
                     "VALUES (?,?,?,?,?)",
                     (paper_id, subj["id"], paper["number"], paper["name_en"], paper["name_bn"]))
        for ch in data["chapters"]:
            conn.execute("INSERT OR IGNORE INTO chapters "
                         "(id, paper_id, chapter_number, title_en, title_bn, curriculum_version) "
                         "VALUES (?,?,?,?,?,?)",
                         (ch["id"], paper_id, ch["number"], ch["title_en"], ch["title_bn"],
                          data["curriculum_version"]))
            for t in ch["topics"]:
                conn.execute("INSERT OR IGNORE INTO topics "
                             "(id, chapter_id, topic_order, title_en, title_bn) VALUES (?,?,?,?,?)",
                             (t["id"], ch["id"], t["order"], t["title_en"], t["title_bn"]))


def cmd_import(args: argparse.Namespace) -> int:
    rows_by_topic, errors, dups = _gather(args.limit_per_topic)
    if errors and not args.allow_invalid:
        print(f"Refusing to import: {len(errors)} invalid rows. "
              f"Run `validate` first.", file=sys.stderr)
        return 1
    db_path = Path(args.db) if args.db else core.APP_DB
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(core.APP_SCHEMA.read_text(encoding="utf-8"))
    if args.reset_content:
        # Destructive: wipe the question-bank tables AND the dev exam wiring that
        # references them, for a pristine launch DB. Leaves users untouched.
        for stmt in ("DELETE FROM answers", "DELETE FROM attempts",
                     "DELETE FROM exam_questions", "DELETE FROM exams",
                     "DELETE FROM question_topics", "DELETE FROM questions",
                     "DELETE FROM topics", "DELETE FROM chapters",
                     "DELETE FROM papers", "DELETE FROM subjects"):
            conn.execute(stmt)
        print("reset-content: cleared bank + dev exam/attempt tables")
    _seed_syllabi(conn)
    topic_meta = {t["id"]: d for d, _, t in core.iter_topics()}
    inserted = skipped = 0
    for tid, rows in rows_by_topic.items():
        cv = topic_meta[tid]["curriculum_version"]
        for q in rows:
            # JSONL keeps verified:false until human review; import marks them
            # live for the app unless --keep-unverified is set.
            src_verified = q.get("verified", True)
            if isinstance(src_verified, str):
                src_verified = src_verified.strip().lower() in {"1", "true", "yes"}
            verified = bool(src_verified) if args.keep_unverified else True
            row = core.to_csv_row(q, tid, verified=verified)
            h = core.stem_key(q["stem_en"])
            existing = conn.execute("SELECT id FROM questions WHERE stem_hash=?", (h,)).fetchone()
            if existing:
                qid = existing["id"]
                skipped += 1
                if verified:
                    conn.execute("UPDATE questions SET verified=1 WHERE id=?", (qid,))
            else:
                cur = conn.execute(
                    "INSERT INTO questions (stem, option_a, option_b, option_c, option_d, "
                    "correct, difficulty, qtype, source, explanation, verified, stem_hash, "
                    "curriculum_version) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (row["stem"], row["option_a"], row["option_b"], row["option_c"], row["option_d"],
                     row["correct"], row["difficulty"], row["type"], row["source"],
                     row["explanation"], 1 if verified else 0, h, cv))
                qid = cur.lastrowid
                inserted += 1
            conn.execute("INSERT OR IGNORE INTO question_topics (question_id, topic_id) VALUES (?,?)",
                         (qid, tid))
    conn.commit()
    live = conn.execute("SELECT COUNT(*) FROM questions WHERE verified=1").fetchone()[0]
    total_q = conn.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    conn.close()
    print(f"Imported into {db_path}")
    print(f"  inserted={inserted}  already-present={skipped}  invalid-skipped={len(errors)}  dups={dups}")
    print(f"  questions in DB: {total_q}  verified=1 (live in app): {live}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("status", "validate", "export", "import"):
        sp = sub.add_parser(name)
        sp.add_argument("--target", type=int, default=20, help="target questions per topic")
        if name in ("export", "import"):
            sp.add_argument("--limit-per-topic", type=int, default=None,
                            help="cap questions used per topic")
            sp.add_argument("--allow-invalid", action="store_true")
        if name == "import":
            sp.add_argument("--db", default=None, help="SQLite path (default: app bank)")
            sp.add_argument("--reset-content", action="store_true",
                            help="DESTRUCTIVE: wipe bank + dev exam data for a clean launch DB")
            sp.add_argument("--keep-unverified", action="store_true",
                            help="Preserve JSONL verified flags (default: mark all imported as verified=1 for the app)")
    args = p.parse_args()
    return {"status": cmd_status, "validate": cmd_validate,
            "export": cmd_export, "import": cmd_import}[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
