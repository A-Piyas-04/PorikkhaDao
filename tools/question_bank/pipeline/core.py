#!/usr/bin/env python3
"""Shared core for the PorikkhaDao question-bank pipeline.

Single source of truth for: in-scope papers, syllabus loading, the authored
question record schema, structural + bilingual validation, de-duplication,
and conversion to the app import-CSV / app-DB row shapes.

Authoring model: questions are written as one JSON object per line into
`content/bank/topics/<topic_id>.jsonl`. This file is the durable, resumable
checkpoint. Everything downstream (CSV, consolidated JSON, SQLite import)
is derived from it, so re-running export/import is always safe.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTENT = ROOT / "content"
SYLLABUS_DIR = CONTENT / "syllabus"
BANK = CONTENT / "bank"
TOPICS_DIR = BANK / "topics"
IMPORT_DIR = BANK / "import"
APP_DB = CONTENT / "db" / "porikkhadao.sqlite"
APP_SCHEMA = Path(__file__).resolve().parents[1] / "schema.sql"

# Five subjects, both papers where they exist; ICT is a single paper. No English.
PAPERS: list[tuple[str, int]] = [
    ("ict", 1),
    ("physics", 1), ("physics", 2),
    ("chemistry", 1), ("chemistry", 2),
    ("biology", 1), ("biology", 2),
    ("higher_mathematics", 1), ("higher_mathematics", 2),
]

# App import template header (content/templates/questions_import.csv).
CSV_HEADERS = ["stem", "option_a", "option_b", "option_c", "option_d",
               "correct", "topic_ids", "difficulty", "type", "source",
               "verified", "explanation"]

# Authored record fields (bilingual, split per language).
FIELDS = ["stem_en", "stem_bn",
          *[f"option_{a}_{lang}" for a in "abcd" for lang in ("en", "bn")],
          "correct", "difficulty", "type", "explanation_en", "explanation_bn"]

DIFFICULTIES = {"easy", "medium", "hard"}
QTYPES = {"factual", "conceptual", "numerical", "application"}
SOURCE_LABEL = "original; AI-authored; structural+bilingual validated"
UDVASH_SOURCE_PREFIX = "Udvash HSC Question Bank 2026; licensed redistribution"


def syllabus_file(subject: str, paper: int) -> Path:
    if subject == "ict":
        return SYLLABUS_DIR / "ict_2027.json"
    label = "1st" if paper == 1 else "2nd"
    return SYLLABUS_DIR / f"{subject}_{label}_paper_2027.json"


def load_syllabi() -> list[dict]:
    out = []
    for subject, paper in PAPERS:
        path = syllabus_file(subject, paper)
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["subject"]["id"] == subject and data["paper"]["number"] == paper, path
        out.append(data)
    return out


def iter_topics():
    """Yield (data, chapter, topic) for every in-scope topic."""
    for data in load_syllabi():
        for chapter in data["chapters"]:
            for topic in chapter["topics"]:
                yield data, chapter, topic


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.casefold()).strip()


def stem_key(stem_en: str) -> str:
    return hashlib.sha256(norm(stem_en).encode("utf-8")).hexdigest()


def has_bangla(text: str) -> bool:
    return bool(re.search(r"[ঀ-৿]", text))


def has_latin(text: str) -> bool:
    return bool(re.search(r"[A-Za-z]", text))


def validate_record(q: dict) -> str | None:
    """Return an error string, or None if the record is structurally sound."""
    if not isinstance(q, dict):
        return "not an object"
    for k in FIELDS:
        if not isinstance(q.get(k), str) or not q[k].strip():
            return f"missing/empty field: {k}"
    if q["correct"] not in {"A", "B", "C", "D"}:
        return "bad answer key"
    if q["difficulty"] not in DIFFICULTIES:
        return "bad difficulty"
    if q["type"] not in QTYPES:
        return "bad type"
    # Bangla present where it must be.
    for k in ("stem_bn", "explanation_bn"):
        if not has_bangla(q[k]):
            return f"missing Bangla in {k}"
    # English present in stem + options.
    for k in ("stem_en", *[f"option_{a}_en" for a in "abcd"]):
        if not has_latin(q[k]):
            return f"missing English in {k}"
    # Bangla option translations, unless the option is a pure symbol/number.
    for a in "abcd":
        en, bn = q[f"option_{a}_en"].strip(), q[f"option_{a}_bn"].strip()
        if not has_bangla(bn) and (en != bn or re.search(r"[A-Za-z]{3,}", en)):
            return f"missing Bangla translation of option {a}"
    # Distinct options within each language.
    for lang in ("en", "bn"):
        opts = [norm(q[f"option_{a}_{lang}"]) for a in "abcd"]
        if len(set(opts)) != 4:
            return f"duplicate {lang} options"
    return None


def to_csv_row(q: dict, topic_id: str, verified: bool = True) -> dict:
    """Authored record -> app import CSV row (bilingual fields joined by newline)."""
    source = q.get("source") or SOURCE_LABEL
    return {
        "stem": q["stem_en"] + "\n" + q["stem_bn"],
        **{f"option_{a}": q[f"option_{a}_en"] + "\n" + q[f"option_{a}_bn"] for a in "abcd"},
        "correct": q["correct"],
        "topic_ids": topic_id,
        "difficulty": q["difficulty"],
        "type": q["type"],
        "source": source,
        "verified": "true" if verified else "false",
        "explanation": q["explanation_en"] + "\n" + q["explanation_bn"],
    }


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def topic_path(topic_id: str) -> Path:
    return TOPICS_DIR / f"{topic_id}.jsonl"
