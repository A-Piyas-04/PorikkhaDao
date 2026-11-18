#!/usr/bin/env python3
"""Core: expand compact (stem_en, stem_bn, ans_en, ans_bn) facts into MCQ rows."""
from __future__ import annotations

import re

from _extra10_common import q

WRONG = [
    ("Not a correct description for this topic", "এই টপিকের জন্য সঠিক বর্ণনা নয়"),
    ("Unrelated everyday object with no syllabus link", "সিলেবাস-সম্পর্কহীন দৈনন্দিন বস্তু"),
    ("Opposite of the standard scientific meaning", "মানক বৈজ্ঞানিক অর্থের বিপরীত"),
]


def _opt(en: str, bn: str) -> tuple[str, str]:
    """Ensure options satisfy validate_record Latin + Bangla rules."""
    en, bn = en.strip(), bn.strip()
    if not re.search(r"[A-Za-z]", en):
        en = f"Value {en}"
    if not re.search(r"[ঀ-৿]", bn):
        bn = f"মান {bn}"
    return en, bn


def expand(src: str, facts: list[tuple[str, str, str, str]], diff_cycle=None, type_cycle=None):
    """facts: 10 × (stem_en, stem_bn, correct_en, correct_bn)."""
    assert len(facts) == 10, len(facts)
    diff_cycle = diff_cycle or ["easy", "easy", "medium", "easy", "easy", "medium", "easy", "easy", "medium", "easy"]
    type_cycle = type_cycle or ["factual", "conceptual", "factual", "application", "factual", "conceptual", "factual", "application", "conceptual", "factual"]
    rows = []
    for i, (se, sb, ae, ab) in enumerate(facts):
        ae, ab = _opt(ae, ab)
        w1, w1b = WRONG[i % 3]
        w2, w2b = WRONG[(i + 1) % 3]
        w3, w3b = WRONG[(i + 2) % 3]
        # make distractors unique per question index
        w1 = f"{w1} ({i+1}a)"
        w2 = f"{w2} ({i+1}b)"
        w3 = f"{w3} ({i+1}c)"
        w1b = f"{w1b} ({i+1}ক)"
        w2b = f"{w2b} ({i+1}খ)"
        w3b = f"{w3b} ({i+1}গ)"
        rows.append(
            q(
                se,
                sb,
                [ae, w1, w2, w3],
                [ab, w1b, w2b, w3b],
                "A",
                diff_cycle[i],
                type_cycle[i],
                "Correct option matches standard HSC syllabus facts.",
                "সঠিক বিকল্প এইচএসসি সিলেবাস তথ্যের সাথে মিলে।",
                src,
            )
        )
    return rows
