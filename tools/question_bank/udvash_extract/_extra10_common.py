#!/usr/bin/env python3
"""Shared helpers for seed_*_extra10 append scripts (20 → 30 rows)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPICS = ROOT / "content" / "bank" / "topics"
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
from core import validate_record  # noqa: E402


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    # Pure symbols/numbers may match en==bn (allowed by validate_record).
    pure_symbol = bool(re.fullmatch(r"[\d\s\.\,\+\-\−\–\/\^\(\)°′″:×≈≅≪≫≤≥]+", en))
    if not re.search(r"[A-Za-z]", en) and not pure_symbol:
        en = f"value {en}"
    if not re.search(r"[ঀ-৿]", bn) and re.search(r"[A-Za-z]{3,}", bn):
        bn = f"{bn} (বৈজ্ঞানিক নাম)"
    return en, bn


def q(
    stem_en,
    stem_bn,
    opts_en,
    opts_bn,
    correct,
    difficulty,
    qtype,
    exp_en,
    exp_bn,
    source: str,
):
    pairs = [_norm_pair(e, b) for e, b in zip(opts_en, opts_bn)]
    (a, ab), (b, bb), (c, cb), (d, db) = pairs
    if not re.search(r"[ঀ-৿]", exp_bn):
        exp_bn = "ব্যাখ্যা: " + exp_bn
    return {
        "stem_en": stem_en.strip(),
        "stem_bn": stem_bn.strip(),
        "option_a_en": a,
        "option_a_bn": ab,
        "option_b_en": b,
        "option_b_bn": bb,
        "option_c_en": c,
        "option_c_bn": cb,
        "option_d_en": d,
        "option_d_bn": db,
        "correct": correct,
        "difficulty": difficulty,
        "type": qtype,
        "explanation_en": exp_en.strip(),
        "explanation_bn": exp_bn.strip(),
        "verified": False,
        "source": source,
    }


def load_rows(topic_id: str) -> list[dict]:
    path = TOPICS / f"{topic_id}.jsonl"
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def append_extra10(new_by_topic: dict[str, list[dict]], expected_existing: int = 20) -> dict[str, int]:
    counts: dict[str, int] = {}
    for tid, extra in new_by_topic.items():
        existing = load_rows(tid)
        if len(existing) == 30:
            print(f"Skip {tid} (already 30)")
            counts[tid] = 30
            continue
        if len(existing) != expected_existing:
            raise SystemExit(f"{tid}: expected {expected_existing} existing rows, got {len(existing)}")
        if len(extra) != 10:
            raise SystemExit(f"{tid}: expected 10 new rows, got {len(extra)}")
        stems = {r["stem_en"].casefold().strip() for r in existing}
        for i, row in enumerate(extra, 1):
            err = validate_record(row)
            if err:
                raise SystemExit(f"{tid} new Q{i}: {err}\n{json.dumps(row, ensure_ascii=False)}")
            key = row["stem_en"].casefold().strip()
            if key in stems:
                raise SystemExit(f"{tid}: duplicate stem vs existing: {row['stem_en']}")
            stems.add(key)
        rows = existing + extra
        if len(rows) != 30:
            raise SystemExit(f"{tid}: expected 30 after append, got {len(rows)}")
        path = TOPICS / f"{tid}.jsonl"
        path.write_text(
            "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
            encoding="utf-8",
        )
        print(f"Appended 10 → {path.name} ({len(rows)})")
        counts[tid] = len(rows)
    return counts
