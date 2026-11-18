#!/usr/bin/env python3
"""Copy the local SQLite bank into Supabase/Postgres.

Usage (from repo root):
  python -m pip install "psycopg[binary]"
  set DATABASE_URL=postgresql://...   # Session/direct URI preferred for bulk load
  python tools/question_bank/migrate_sqlite_to_postgres.py

Optional:
  --sqlite path\\to\\porikkhadao.sqlite
  --schema-only   apply web/src/db/schema-postgres.sql only
  --skip-schema   assume tables already exist
  --clear         truncate app tables before copy (bank + app data)
"""

from __future__ import annotations

import argparse
import os
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SQLITE = ROOT / "content" / "db" / "porikkhadao.sqlite"
SCHEMA_SQL = ROOT / "web" / "src" / "db" / "schema-postgres.sql"

TABLE_ORDER = [
    "subjects",
    "papers",
    "chapters",
    "topics",
    "questions",
    "question_topics",
    "users",
    "exams",
    "exam_questions",
    "attempts",
    "answers",
]

CLEAR_ORDER = list(reversed(TABLE_ORDER))


def require_psycopg():
    try:
        import psycopg  # noqa: F401
        from psycopg.rows import dict_row  # noqa: F401
    except ImportError:
        print('Install driver first: python -m pip install "psycopg[binary]"', file=sys.stderr)
        sys.exit(1)


def validate_url(url: str) -> None:
    if "[YOUR-PASSWORD]" in url or "[YOUR-DATABASE-PASSWORD]" in url:
        print(
            "DATABASE_URL still has the password placeholder.\n"
            "Replace [YOUR-DATABASE-PASSWORD] with your real DB password (no brackets).",
            file=sys.stderr,
        )
        sys.exit(1)
    # Common mistake: leaving square brackets around the password from the docs.
    # e.g. ...:[PorikkhaDao]@host  → password sent is literally "[PorikkhaDao]"
    if "]@" in url or "%5D@" in url or "]:@" in url:
        print(
            "DATABASE_URL still has [brackets] around the password.\n"
            "Supabase docs show [YOUR-DATABASE-PASSWORD] as a PLACEHOLDER.\n"
            "Remove the brackets — send only the password characters.\n\n"
            "Wrong: ...postgres.xxx:[PorikkhaDao]@aws-0-....pooler.supabase.com:5432/postgres\n"
            "Right: ...postgres.xxx:PorikkhaDao@aws-0-....pooler.supabase.com:5432/postgres\n",
            file=sys.stderr,
        )
        sys.exit(1)


def connect_pg(url: str):
    import psycopg
    from psycopg import OperationalError

    try:
        return psycopg.connect(url)
    except OperationalError as exc:
        msg = str(exc)
        print(f"Could not connect to Postgres:\n  {msg}\n", file=sys.stderr)
        if "db." in url and "supabase.co" in url and "pooler.supabase.com" not in url:
            print(
                "You used a Direct connection (db.*.supabase.co). On many Windows\n"
                "networks that host is IPv6-only and fails with getaddrinfo.\n\n"
                "Fix:\n"
                "  1. Supabase → Connect → choose Session pooler (port 5432)\n"
                "  2. Type: URI → Copy\n"
                "  3. Replace [YOUR-DATABASE-PASSWORD] with the password only\n"
                "     (no square brackets around it)\n"
                "  4. Re-run with that URI as DATABASE_URL\n",
                file=sys.stderr,
            )
        elif "password" in msg.lower() or "authentication" in msg.lower():
            print(
                "Auth failed. Check the DB password (project creation password),\n"
                "and remove any [brackets] around it in the URI.\n",
                file=sys.stderr,
            )
        raise SystemExit(1) from exc


def apply_schema(pg) -> None:
    sql = SCHEMA_SQL.read_text(encoding="utf-8")
    with pg.cursor() as cur:
        cur.execute(sql)
    pg.commit()
    print(f"Applied schema from {SCHEMA_SQL}")


def clear_tables(pg) -> None:
    with pg.cursor() as cur:
        for table in CLEAR_ORDER:
            cur.execute(f'TRUNCATE TABLE "{table}" RESTART IDENTITY CASCADE')
    pg.commit()
    print("Cleared existing rows")


def sqlite_columns(sqlite_conn: sqlite3.Connection, table: str) -> list[str]:
    rows = sqlite_conn.execute(f"PRAGMA table_info({table})").fetchall()
    return [r[1] for r in rows]


def copy_table(sqlite_conn: sqlite3.Connection, pg, table: str) -> int:
    cols = sqlite_columns(sqlite_conn, table)
    if not cols:
        print(f"  skip {table} (missing in SQLite)")
        return 0

    rows = sqlite_conn.execute(
        f"SELECT {', '.join(cols)} FROM {table}"
    ).fetchall()
    if not rows:
        print(f"  {table}: 0 rows")
        return 0

    placeholders = ", ".join(["%s"] * len(cols))
    col_list = ", ".join(f'"{c}"' for c in cols)
    insert_sql = f'INSERT INTO "{table}" ({col_list}) VALUES ({placeholders})'

    with pg.cursor() as cur:
        cur.executemany(insert_sql, rows)
    pg.commit()
    print(f"  {table}: {len(rows)} rows")
    return len(rows)


def reset_question_identity(pg) -> None:
    with pg.cursor() as cur:
        cur.execute(
            """
            SELECT setval(
              pg_get_serial_sequence('questions', 'id'),
              COALESCE((SELECT MAX(id) FROM questions), 1),
              true
            )
            """
        )
    pg.commit()


def main() -> int:
    require_psycopg()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sqlite", type=Path, default=DEFAULT_SQLITE)
    parser.add_argument("--schema-only", action="store_true")
    parser.add_argument("--skip-schema", action="store_true")
    parser.add_argument("--clear", action="store_true")
    args = parser.parse_args()

    url = os.environ.get("DATABASE_URL")
    if not url:
        print("DATABASE_URL is required", file=sys.stderr)
        return 1

    validate_url(url)

    if not args.sqlite.exists():
        print(f"SQLite file not found: {args.sqlite}", file=sys.stderr)
        return 1

    # Prefer session connection for bulk load on Windows (not transaction pooler).
    if "pooler.supabase.com" in url and ":6543" in url:
        print(
            "Warning: transaction pooler (port 6543) can be flaky for bulk load.\n"
            "Prefer Session pooler (port 5432) from Supabase → Connect.",
            file=sys.stderr,
        )

    sqlite_conn = sqlite3.connect(str(args.sqlite))
    pg = connect_pg(url)

    try:
        if not args.skip_schema:
            apply_schema(pg)
        if args.schema_only:
            return 0
        if args.clear:
            clear_tables(pg)

        print(f"Copying from {args.sqlite}")
        total = 0
        for table in TABLE_ORDER:
            total += copy_table(sqlite_conn, pg, table)
        reset_question_identity(pg)
        print(f"Done. Copied {total} rows total.")
        return 0
    finally:
        sqlite_conn.close()
        pg.close()


if __name__ == "__main__":
    raise SystemExit(main())
