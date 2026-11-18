#!/usr/bin/env python3
"""Append 10 NEW bilingual MCQs to each ict27_*.jsonl (20 → 30). APPEND only."""
from __future__ import annotations

from _extra10_common import append_extra10
from extra10_ict_bank import BANK


def main() -> int:
    counts = append_extra10(BANK, expected_existing=20)
    print(f"ict topics at 30: {len(counts)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
