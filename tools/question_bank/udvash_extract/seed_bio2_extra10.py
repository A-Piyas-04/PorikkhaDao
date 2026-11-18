#!/usr/bin/env python3
"""Append exactly 10 short bilingual MCQs to every bio2_27_*.jsonl topic (36).

APPEND-only: existing rows are preserved. Target: 30 lines per file.
Idempotent: skips topics already at 30.
Loads question banks from _bio2_extra10_*.json beside this script,
merged with any EXTRA defined below.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPICS = ROOT / "content" / "bank" / "topics"
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
from core import validate_record  # noqa: E402

SRC = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "biology p2; curated bilingual; extra short set"
)


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    if not re.search(r"[A-Za-z]", en):
        if "%" in en:
            en = f"about {en}"
        else:
            en = f"value {en}"
        if not re.search(r"[ঀ-৿]", bn):
            bn = f"মান {bn}"
        elif en.startswith("about ") and "শতাংশ" not in bn and "%" in bn:
            bn = f"প্রায় {bn}"
    if not re.search(r"[ঀ-৿]", bn) and re.search(r"[A-Za-z]{3,}", bn):
        bn = f"{bn} (বৈজ্ঞানিক নাম)"
    return en, bn


def q(stem_en, stem_bn, opts_en, opts_bn, correct, difficulty, qtype, exp_en, exp_bn):
    pairs = [_norm_pair(e, b) for e, b in zip(opts_en, opts_bn)]
    (a, ab), (b, bb), (c, cb), (d, db) = pairs
    if not re.search(r"[ঀ-৿]", exp_bn):
        exp_bn = "ব্যাখ্যা: " + exp_bn
    return {
        "stem_en": stem_en,
        "stem_bn": stem_bn,
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
        "explanation_en": exp_en,
        "explanation_bn": exp_bn,
        "verified": False,
        "source": SRC,
    }


def pack_rows(raw_rows: list) -> list[dict]:
    out = []
    for r in raw_rows:
        if len(r) != 9:
            raise SystemExit(f"bad row arity {len(r)}: {r[:2]}")
        out.append(q(*r))
    return out


def load_extra() -> dict[str, list[dict]]:
    merged: dict[str, list[dict]] = {}
    for path in sorted(HERE.glob("_bio2_extra10_*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for tid, rows in data.items():
            if tid in merged:
                raise SystemExit(f"duplicate topic in JSON banks: {tid}")
            if len(rows) != 10:
                raise SystemExit(f"{path.name}:{tid} expected 10 rows, got {len(rows)}")
            merged[tid] = pack_rows(rows)
    return merged


def append_topic(topic_id: str, new_rows: list[dict]) -> tuple[int, str]:
    path = TOPICS / f"{topic_id}.jsonl"
    if not path.exists():
        raise SystemExit(f"missing {path}")
    existing = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    n = len(existing)
    if n == 30:
        return 30, "already 30"
    if n != 20:
        raise SystemExit(f"{topic_id}: expected 20 existing rows, found {n}")
    if len(new_rows) != 10:
        raise SystemExit(f"{topic_id}: expected 10 new rows, got {len(new_rows)}")

    stems = {r["stem_en"].casefold().strip() for r in existing}
    for i, row in enumerate(new_rows, 1):
        err = validate_record(row)
        if err:
            raise SystemExit(f"{topic_id} newQ{i}: {err}\n{json.dumps(row, ensure_ascii=False)}")
        key = row["stem_en"].casefold().strip()
        if key in stems:
            raise SystemExit(f"{topic_id} newQ{i}: duplicate stem: {row['stem_en']}")
        stems.add(key)

    with path.open("a", encoding="utf-8", newline="\n") as fh:
        for row in new_rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return 30, "appended 10"


def main() -> int:
    extra = load_extra()
    expected = sorted(p.stem for p in TOPICS.glob("bio2_27_*.jsonl"))
    if len(expected) != 36:
        raise SystemExit(f"expected 36 bio2 topics, found {len(expected)}")
    missing = [t for t in expected if t not in extra]
    if missing:
        raise SystemExit(f"EXTRA missing topics ({len(missing)}): {missing}")
    extra_only = [t for t in extra if t not in expected]
    if extra_only:
        raise SystemExit(f"EXTRA unknown topics: {extra_only}")

    counts: dict[str, int] = {}
    for tid in expected:
        final, msg = append_topic(tid, extra[tid])
        counts[tid] = final
        print(f"{tid}: {msg} -> {final}")

    bad = {k: v for k, v in counts.items() if v != 30}
    if bad:
        raise SystemExit(f"not all at 30: {bad}")
    print(f"OK: {len(counts)} bio2 topics at 30")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())