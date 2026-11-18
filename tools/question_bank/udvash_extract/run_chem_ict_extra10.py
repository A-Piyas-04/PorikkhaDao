#!/usr/bin/env python3
"""Append exactly 10 NEW short bilingual MCQs to each chem1/chem2/ict topic JSONL (20→30).

APPEND only. Does not touch physics/bio/math. verified:false.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TOPICS = ROOT / "content" / "bank" / "topics"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
from _extra10_common import q, append_extra10  # noqa: E402

# Import banks from sibling modules (built below as BANK dicts)
from extra10_chem1_bank import BANK as CHEM1  # noqa: E402
from extra10_chem2_bank import BANK as CHEM2  # noqa: E402
from extra10_ict_bank import BANK as ICT  # noqa: E402


def main() -> int:
    all_banks = {**CHEM1, **CHEM2, **ICT}
    expected = (
        [f"chem1_27_ch{c:02d}_t{t:02d}" for c, n in [(1, 3), (2, 5), (3, 5), (4, 4), (5, 4)] for t in range(1, n + 1)]
        + [f"chem2_27_ch{c:02d}_t{t:02d}" for c, n in [(1, 4), (2, 6), (3, 4), (4, 4), (5, 4)] for t in range(1, n + 1)]
        + [f"ict27_ch{c:02d}_t{t:02d}" for c, n in [(1, 7), (2, 7), (3, 6), (4, 5), (5, 7), (6, 5)] for t in range(1, n + 1)]
    )
    missing = [tid for tid in expected if tid not in all_banks]
    extra = [tid for tid in all_banks if tid not in expected]
    if missing or extra:
        raise SystemExit(f"bank mismatch missing={missing[:5]}... extra={extra[:5]}")
    if len(all_banks) != 80:
        raise SystemExit(f"expected 80 topics, got {len(all_banks)}")

    # Skip topics already at 30 (idempotent)
    to_run = {}
    for tid, rows in all_banks.items():
        path = TOPICS / f"{tid}.jsonl"
        n = sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
        if n == 30:
            print(f"Skip {tid} (already 30)")
            continue
        if n != 20:
            raise SystemExit(f"{tid}: expected 20 lines before append, got {n}")
        to_run[tid] = rows

    if not to_run:
        print("All 80 topics already at 30.")
        return 0

    counts = append_extra10(to_run, expected_existing=20)
    # verify
    prefixes = {"chem1_27": 0, "chem2_27": 0, "ict27": 0}
    bad = []
    for tid in expected:
        n = sum(1 for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines() if line.strip())
        if n != 30:
            bad.append((tid, n))
        if tid.startswith("chem1_27"):
            prefixes["chem1_27"] += 1 if n == 30 else 0
        elif tid.startswith("chem2_27"):
            prefixes["chem2_27"] += 1 if n == 30 else 0
        elif tid.startswith("ict27"):
            prefixes["ict27"] += 1 if n == 30 else 0
    if bad:
        raise SystemExit(f"not all at 30: {bad[:10]}")
    print(json.dumps({"appended_topics": len(counts), "at_30": prefixes}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
