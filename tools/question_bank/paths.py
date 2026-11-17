"""Shared filesystem paths for PorikkhaDao question-bank tools."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "content"
SYLLABUS_PATH = CONTENT / "syllabus" / "physics_2nd_paper.json"
TEMPLATE_PATH = CONTENT / "templates" / "questions_import.csv"
PILOT_CSV_PATH = CONTENT / "pilot" / "physics_2nd_ch1_ch2.csv"
DB_DIR = CONTENT / "db"
DB_PATH = DB_DIR / "porikkhadao.sqlite"
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"

CSV_HEADERS = [
    "stem",
    "option_a",
    "option_b",
    "option_c",
    "option_d",
    "correct",
    "topic_ids",
    "difficulty",
    "type",
    "source",
    "verified",
    "explanation",
]
