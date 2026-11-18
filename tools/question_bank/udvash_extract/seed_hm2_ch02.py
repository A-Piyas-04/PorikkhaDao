#!/usr/bin/env python3
"""Seed Higher Mathematics 2nd Paper Ch02 (Linear Programming).

Curated from Udvash HSC Question Bank 2026 printed pp. 40–43 (PDF 46–49).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
OCR is noisy (~4 pages); reconstructs board-style items from solutions/column
text and supplements with accurate HSC-level authored MCQs. Figure-only
LP graph items rewritten as text-describable questions.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
from core import validate_record  # noqa: E402

TOPICS = ROOT / "content" / "bank" / "topics"
PARSED = ROOT / "content" / "bank" / "udvash_raw" / "higher_mathematics_2" / "parsed"
SOURCE = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "higher_mathematics p2 ch02; curated bilingual"
)


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    if not re.search(r"[A-Za-z]", en):
        en = f"value {en}"
    if not re.search(r"[ঀ-৿]", bn):
        if en.startswith("value ") or re.search(r"[A-Za-z]{3,}", en):
            bn = "মান " + bn.removeprefix("মান ").strip()
    return en, bn


def q(
    stem_en: str,
    stem_bn: str,
    opts_en: list[str],
    opts_bn: list[str],
    correct: str,
    difficulty: str,
    qtype: str,
    exp_en: str,
    exp_bn: str,
) -> dict:
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
        "source": SOURCE,
    }


# =============================================================================
# hm2_27_ch02_t01 — Linear constraints and feasible region / রৈখিক শর্ত ও সম্ভাব্য অঞ্চল
# =============================================================================
T01 = [
    q(
        "A student wants to spend at most 300 taka on notebooks (x) and pens (y). Each notebook costs 25 taka and each pen 10 taka. He buys more than 9 notebooks and at least 3 pens. Which constraints are correct?",
        "কোনো ছাত্র সর্বোচ্চ ৩০০ টাকা ব্যয় করে খাতা (x) ও কলম (y) কিনতে চায়। প্রতিটি খাতার দাম ২৫ টাকা ও কলমের দাম ১০ টাকা। সে ৯টির বেশি খাতা ও কমপক্ষে ৩টি কলম ক্রয় করবে। কোন শর্তগুলো সঠিক?",
        [
            "25x + 10y ≤ 300, x > 9, y ≥ 3",
            "25x + 10y ≥ 300, x > 9, y ≥ 3",
            "25x + 10y ≤ 300, x < 9, y < 3",
            "25x + 10y ≥ 300, x < 9, y < 3",
        ],
        [
            "25x + 10y ≤ 300, x > 9, y ≥ 3",
            "25x + 10y ≥ 300, x > 9, y ≥ 3",
            "25x + 10y ≤ 300, x < 9, y < 3",
            "25x + 10y ≥ 300, x < 9, y < 3",
        ],
        "A", "medium", "application",
        "Budget: 25x + 10y ≤ 300. More than 9 notebooks: x > 9. At least 3 pens: y ≥ 3.",
        "বাজেট ২৫x + ১০y ≤ ৩০০; x > ৯ এবং y ≥ ৩।",
    ),
    q(
        "In forming a linear programming problem, which statements are true? (i) Resources must be finite (ii) Decision variables must exist (iii) Decision variables cannot be positive",
        "যোগাশ্রয়ী প্রোগ্রাম সমস্যা গঠনে— (i) সসীম সম্পদ থাকতে হবে (ii) সিদ্ধান্ত চলক থাকতে হবে (iii) সিদ্ধান্ত চলক ধনাত্মক হতে পারে না — কোনটি সঠিক?",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii", "i, ii ও iii"],
        "A", "easy", "conceptual",
        "LP needs finite resources and decision variables; variables are non-negative (not “cannot be positive”). So (iii) is false.",
        "সসীম সম্পদ ও সিদ্ধান্ত চলক প্রয়োজন; চলক অঋণাত্মক হয়—তাই (iii) ভুল।",
    ),
    q(
        "Under the constraints 5x + 2y ≤ 30, x ≥ 2, y ≤ 5 and x, y ≥ 0, which point is a corner of the feasible region?",
        "5x + 2y ≤ 30, x ≥ 2, y ≤ 5 এবং x, y ≥ 0 শর্তে সম্ভাব্য অঞ্চলের কোন বিন্দুটি প্রান্তিক বিন্দু?",
        ["(2, 5)", "(1, 5)", "(7, 0)", "(0, 5)"],
        ["(2, 5)", "(1, 5)", "(7, 0)", "(0, 5)"],
        "A", "medium", "numerical",
        "Feasible corners include (2, 5), (2, 0), (6, 0), (4, 5). (2, 5) satisfies all constraints.",
        "প্রান্তিক বিন্দুসমূহ (2,5), (2,0), (6,0), (4,5); (2,5) সব শর্ত সিদ্ধ করে।",
    ),
    q(
        "Which of the following expresses a linear inequality suitable for linear programming?",
        "নিচের কোনটি যোগাশ্রয়ী প্রোগ্রামের জন্য উপযুক্ত রৈখিক অসমতা প্রকাশ করে?",
        ["2x + 3y = 6", "2x + y ≥ 6", "x² = 6", "x² + y² > 16"],
        ["2x + 3y = 6", "2x + y ≥ 6", "x² = 6", "x² + y² > 16"],
        "B", "easy", "factual",
        "LP constraints are linear inequalities (degree 1). Equations or quadratic relations are not linear inequalities.",
        "যোগাশ্রয়ী অসমতা একঘাত; সমীকরণ বা দ্বিঘাত সম্পর্ক নয়।",
    ),
    q(
        "For a linear programming problem in two variables, which non-negativity restriction is always assumed?",
        "দ্বিচলক যোগাশ্রয়ী প্রোগ্রামে কোন অঋণাত্মকতা শর্ত সর্বদা ধরা হয়?",
        ["x ≥ 0, y ≥ 0", "x > 0, y < 0", "x ≤ 0, y ≤ 0", "x > 0, y = 0"],
        ["x ≥ 0, y ≥ 0", "x > 0, y < 0", "x ≤ 0, y ≤ 0", "x > 0, y = 0"],
        "A", "easy", "factual",
        "Decision variables in standard LP are non-negative: x ≥ 0, y ≥ 0.",
        "সিদ্ধান্ত চলক অঋণাত্মক: x ≥ 0, y ≥ 0।",
    ),
    q(
        "Linear programming requires which of the following? (i) Quadratic equations (ii) Non-negative variables (iii) Linear inequalities",
        "যোগাশ্রয়ী প্রোগ্রামে প্রয়োজন হয়— (i) দ্বিঘাত সমীকরণ (ii) অঋণাত্মক চলক (iii) একঘাত বিশিষ্ট অসমতা — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "C", "easy", "conceptual",
        "LP uses non-negative variables and linear inequalities; quadratic equations are not required.",
        "অঋণাত্মক চলক ও রৈখিক অসমতা দরকার; দ্বিঘাত সমীকরণ নয়।",
    ),
    q(
        "Under x + y ≤ 8, x + 2y ≤ 10, x ≥ 0, y ≥ 0, the feasible region is a closed polygon in the first quadrant. Which listed set is its set of corner points?",
        "x + y ≤ 8, x + 2y ≤ 10, x ≥ 0, y ≥ 0 শর্তে সম্ভাব্য অঞ্চলের প্রান্তিক বিন্দুগুলো কোনটি?",
        [
            "(0, 0), (8, 0), (6, 2), (0, 5)",
            "(0, 0), (10, 0), (0, 8)",
            "(0, 0), (8, 0), (0, 8)",
            "(2, 4), (8, 0), (0, 5)",
        ],
        [
            "(0, 0), (8, 0), (6, 2), (0, 5)",
            "(0, 0), (10, 0), (0, 8)",
            "(0, 0), (8, 0), (0, 8)",
            "(2, 4), (8, 0), (0, 5)",
        ],
        "A", "medium", "numerical",
        "Axes intercepts: (8,0) and (0,5). Intersection of x+y=8 and x+2y=10 gives (6,2). With (0,0) these are the corners.",
        "ছেদবিন্দু (6,2); অক্ষ ছেদ (8,0) ও (0,5); সাথে (0,0)।",
    ),
    q(
        "The shaded feasible region is the triangle with vertices (0, 0), (5, 0) and (0, 6). Which constraints describe it?",
        "ছায়াঙ্কিত সম্ভাব্য অঞ্চলের শীর্ষবিন্দু (0, 0), (5, 0) ও (0, 6)। কোন শর্তাবলি এটি নির্দেশ করে?",
        [
            "6x + 5y ≤ 30; x ≥ 0, y ≥ 0",
            "6x + 5y ≥ 30; x ≥ 0, y ≥ 0",
            "6x + 5y ≤ 30; x ≤ 0, y ≤ 0",
            "6x − 5y ≤ 30; x ≥ 0, y ≥ 0",
        ],
        [
            "6x + 5y ≤ 30; x ≥ 0, y ≥ 0",
            "6x + 5y ≥ 30; x ≥ 0, y ≥ 0",
            "6x + 5y ≤ 30; x ≤ 0, y ≤ 0",
            "6x − 5y ≤ 30; x ≥ 0, y ≥ 0",
        ],
        "A", "medium", "conceptual",
        "Line through (5,0) and (0,6) is 6x + 5y = 30. The triangle toward the origin is 6x + 5y ≤ 30 with x, y ≥ 0.",
        "(5,0) ও (0,6) দিয়ে 6x + 5y = 30; মূলবিন্দুর দিকে ≤ এবং x, y ≥ 0।",
    ),
    q(
        "Under the constraints x + y ≤ 6, x ≥ 0, y ≥ 0, the shape of the feasible region is:",
        "x + y ≤ 6, x ≥ 0, y ≥ 0 শর্তাধীনে সমাধান অঞ্চলের আকৃতি কী?",
        ["rectangular", "square", "triangular", "trapezoidal"],
        ["আয়তাকার", "বর্গাকার", "ত্রিভুজাকার", "ট্রাপিজিয়াম আকার"],
        "C", "easy", "conceptual",
        "The region is the right triangle with vertices (0,0), (6,0), (0,6).",
        "শীর্ষ (0,0), (6,0), (0,6) — ত্রিভুজাকার অঞ্চল।",
    ),
    q(
        "Which statement about a bounded feasible region in two-variable LP is correct?",
        "দ্বিচলক যোগাশ্রয়ী প্রোগ্রামে আবদ্ধ সম্ভাব্য অঞ্চল সম্পর্কে কোনটি সঠিক?",
        [
            "It is a closed convex polygon in the plane",
            "It must be an unbounded half-plane only",
            "It always excludes all axis intercepts",
            "It can never contain the origin",
        ],
        [
            "এটি সমতলে একটি বদ্ধ উত্তল বহুভুজ",
            "এটি শুধুমাত্র অনাবদ্ধ অর্ধতল হতে হবে",
            "এতে অক্ষ ছেদবিন্দু কখনো থাকে না",
            "এতে মূলবিন্দু কখনো থাকতে পারে না",
        ],
        "A", "easy", "conceptual",
        "A bounded feasible set from linear inequalities is a closed convex polygon (possibly a segment or point).",
        "রৈখিক অসমতার আবদ্ধ সম্ভাব্য সেট বদ্ধ উত্তল বহুভুজ।",
    ),
    q(
        "For 3x + 2y ≥ 6, 2x + 5y ≥ 10, x ≥ 0, y ≥ 0, the feasible region is:",
        "3x + 2y ≥ 6, 2x + 5y ≥ 10, x ≥ 0, y ≥ 0 শর্তে সম্ভাব্য অঞ্চল কেমন?",
        [
            "unbounded in the first quadrant away from the origin",
            "the triangle joining (0,0), (2,0) and (0,3)",
            "empty",
            "only the single point (0, 0)",
        ],
        [
            "প্রথম চতুর্ভাগে মূলবিন্দু থেকে দূরে অনাবদ্ধ",
            "(0,0), (2,0) ও (0,3) যোগ করা ত্রিভুজ",
            "শূন্য সেট",
            "শুধুমাত্র বিন্দু (0, 0)",
        ],
        "A", "medium", "conceptual",
        "Both inequalities cut off the origin; the feasible set lies away from (0,0) and is unbounded.",
        "উভয় অসমতা মূলবিন্দু বাদ দেয়; সম্ভাব্য অঞ্চল অনাবদ্ধ।",
    ),
    q(
        "The line AC joins A(1, 0) and C(1, 1). Which inequality describes the half-plane to the right of AC (including the line) in a typical LP graph with vertices A(1,0), B(2,0), C(1,1), D(0,2)?",
        "AC রেখা A(1, 0) ও C(1, 1) যোগ করে। AC-এর ডানদিকের (রেখাসহ) অর্ধতল কোন অসমতায় প্রকাশিত?",
        ["x ≥ 1", "x ≤ 1", "y ≥ 2", "y = 1"],
        ["x ≥ 1", "x ≤ 1", "y ≥ 2", "y = 1"],
        "A", "medium", "conceptual",
        "AC is the vertical line x = 1; the half-plane to its right is x ≥ 1.",
        "AC হলো x = 1; ডানদিকের অর্ধতল x ≥ 1।",
    ),
    q(
        "Under x + y ≤ 5, x − y ≤ 3, x ≥ 0, y ≥ 0, which triple correctly lists three corner points of the feasible region?",
        "x + y ≤ 5, x − y ≤ 3, x ≥ 0, y ≥ 0 শর্তে সম্ভাব্য অঞ্চলের তিনটি প্রান্তিক বিন্দু কোনটি?",
        [
            "(0, 0), (3, 0), (4, 1)",
            "(0, 5), (5, 0), (0, 3)",
            "(3, 0), (0, 5), (4, 1)",
            "(4, 1), (0, 3), (0, 5)",
        ],
        [
            "(0, 0), (3, 0), (4, 1)",
            "(0, 5), (5, 0), (0, 3)",
            "(3, 0), (0, 5), (4, 1)",
            "(4, 1), (0, 3), (0, 5)",
        ],
        "C", "hard", "numerical",
        "Corners: (0,0), (3,0) on x−y=3, intersection of x+y=5 and x−y=3 → (4,1), and (0,5).",
        "ছেদ (4,1); প্রান্তিক: (0,0), (3,0), (4,1), (0,5)। তালিকায় (3,0), (0,5), (4,1)।",
    ),
    q(
        "In forming an LP problem, which are correct? (i) Decision variables must exist (ii) Resources must be infinite (iii) Constraints may appear as equations",
        "যোগাশ্রয়ী প্রোগ্রাম সমস্যা গঠনে— (i) সিদ্ধান্ত চলক অবশ্যই থাকতে হবে (ii) অসীম সম্পদ থাকতে হবে (iii) সীমাবদ্ধতা সমীকরণ আকারেও থাকতে পারে — কোনটি সঠিক?",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii", "i, ii ও iii"],
        "C", "easy", "conceptual",
        "Resources must be finite, not infinite. Decision variables are required; equality constraints are allowed.",
        "সম্পদ সসীম হতে হবে; সিদ্ধান্ত চলক ও সমীকরণ-সীমাবদ্ধতা গ্রহণযোগ্য।",
    ),
    q(
        "Which of the following is NOT a linear constraint?",
        "নিচের কোনটি রৈখিক শর্ত নয়?",
        ["x + 2y ≤ 10", "3x − y ≥ 4", "xy ≤ 6", "x ≥ 0"],
        ["x + 2y ≤ 10", "3x − y ≥ 4", "xy ≤ 6", "x ≥ 0"],
        "C", "easy", "factual",
        "The product xy is nonlinear; the others are linear (degree 1) constraints.",
        "xy গুণফল অরৈখিক; বাকিগুলো রৈখিক।",
    ),
    q(
        "A feasible region is formed by x ≥ 0, y ≥ 0, x ≤ 4 and y ≤ 3. The region is:",
        "x ≥ 0, y ≥ 0, x ≤ 4 ও y ≤ 3 দ্বারা গঠিত সম্ভাব্য অঞ্চল কোনটি?",
        [
            "a rectangle with corners (0,0), (4,0), (4,3), (0,3)",
            "a triangle with corners (0,0), (4,0), (0,3)",
            "an unbounded strip",
            "empty",
        ],
        [
            "শীর্ষ (0,0), (4,0), (4,3), (0,3) বিশিষ্ট আয়তক্ষেত্র",
            "শীর্ষ (0,0), (4,0), (0,3) বিশিষ্ট ত্রিভুজ",
            "অনাবদ্ধ স্ট্রিপ",
            "শূন্য সেট",
        ],
        "A", "easy", "conceptual",
        "Four linear bounds produce the closed rectangle [0,4] × [0,3].",
        "চারটি রৈখিক সীমা আয়তক্ষেত্র [0,4] × [0,3] গঠন করে।",
    ),
    q(
        "Under x + y ≤ 9, 3x + 4y ≤ 30, x ≥ 0, y ≥ 0, which statement is true?",
        "x + y ≤ 9, 3x + 4y ≤ 30, x ≥ 0, y ≥ 0 শর্তাধীনে কোনটি সত্য?",
        [
            "One corner point is (6, 3)",
            "Corner points are only (0, 0) and (9, 0)",
            "The point (10, 0) is feasible",
            "The feasible region is unbounded",
        ],
        [
            "একটি প্রান্তিক বিন্দু (6, 3)",
            "প্রান্তিক বিন্দু শুধু (0, 0) ও (9, 0)",
            "(10, 0) সম্ভাব্য",
            "সম্ভাব্য অঞ্চল অনাবদ্ধ",
        ],
        "A", "medium", "numerical",
        "Solving x+y=9 and 3x+4y=30 yields (6,3), a corner of the bounded feasible polygon.",
        "x+y=9 ও 3x+4y=30 সমাধানে (6,3) — একটি প্রান্তিক বিন্দু।",
    ),
    q(
        "If the only constraints are x ≥ 2, y ≥ 0 and x + y ≤ 5, is (1, 1) in the feasible region?",
        "শুধুমাত্র শর্ত x ≥ 2, y ≥ 0 ও x + y ≤ 5 হলে (1, 1) সম্ভাব্য অঞ্চলে আছে কি?",
        ["Yes", "No, because x ≥ 2 fails", "No, because y ≥ 0 fails", "No, because x + y ≤ 5 fails"],
        ["হ্যাঁ", "না, কারণ x ≥ 2 সিদ্ধ নয়", "না, কারণ y ≥ 0 সিদ্ধ নয়", "না, কারণ x + y ≤ 5 সিদ্ধ নয়"],
        "B", "easy", "numerical",
        "(1,1) has x = 1 < 2, so it violates x ≥ 2.",
        "x = 1 < 2 বলে x ≥ 2 লঙ্ঘিত।",
    ),
    q(
        "The intersection of the half-planes 2x + y ≤ 8 and 2x + 3y ≤ 12 in the first quadrant is:",
        "প্রথম চতুর্ভাগে 2x + y ≤ 8 ও 2x + 3y ≤ 12 অর্ধতলদ্বয়ের ছেদ কী?",
        [
            "a bounded polygonal feasible region including (0,0)",
            "only the ray along the positive x-axis",
            "empty",
            "the entire first quadrant",
        ],
        [
            "(0,0)সহ একটি আবদ্ধ বহুভুজাকার সম্ভাব্য অঞ্চল",
            "শুধু ধনাত্মক x-অক্ষ বরাবর রশ্মি",
            "শূন্য সেট",
            "সম্পূর্ণ প্রথম চতুর্ভাগ",
        ],
        "A", "medium", "conceptual",
        "With x ≥ 0, y ≥ 0 the two inequalities cut a closed polygon containing the origin.",
        "x, y ≥ 0সহ দুই অসমতা মূলবিন্দুসহ আবদ্ধ বহুভুজ কাটে।",
    ),
    q(
        "Which description matches an unbounded feasible region?",
        "অনাবদ্ধ সম্ভাব্য অঞ্চলের সঠিক বর্ণনা কোনটি?",
        [
            "Constraints point away from the origin so the region extends to infinity",
            "The region is always a single point",
            "All corner points lie on a circle",
            "No linear inequality can ever be unbounded",
        ],
        [
            "শর্তগুলো মূলবিন্দু থেকে দূরে থাকায় অঞ্চল অসীমে বিস্তৃত",
            "অঞ্চল সর্বদা একটিমাত্র বিন্দু",
            "সব প্রান্তিক বিন্দু বৃত্তের উপর",
            "কোনো রৈখিক অসমতা অনাবদ্ধ হতে পারে না",
        ],
        "A", "medium", "conceptual",
        "≥ type resource constraints often leave an unbounded “away from origin” feasible set.",
        "≥ ধরনের শর্তে সম্ভাব্য অঞ্চল প্রায়ই অনাবদ্ধ হয়।",
    ),
]


# =============================================================================
# hm2_27_ch02_t02 — Objective functions / উদ্দেশ্য ফাংশন
# =============================================================================
T02 = [
    q(
        "Which of the following is an objective function in linear programming?",
        "নিচের কোনটি যোগাশ্রয়ী প্রোগ্রামের অভীষ্ট (উদ্দেশ্য) ফাংশন?",
        ["z = 40x + 50y", "x ≥ 0", "y ≥ 0", "x + y ≥ 0"],
        ["z = 40x + 50y", "x ≥ 0", "y ≥ 0", "x + y ≥ 0"],
        "A", "easy", "factual",
        "The objective is a linear function of decision variables to be optimized; the others are constraints.",
        "উদ্দেশ্য ফাংশন চলকের রৈখিক ফাংশন; বাকিগুলো শর্ত।",
    ),
    q(
        "The purpose of a linear programming model includes: (i) finding desired production levels (ii) listing constraints only without an objective (iii) maximizing profit",
        "যোগাশ্রয়ী প্রোগ্রামের উদ্দেশ্য— (i) উৎপাদনের কাঙ্ক্ষিত মান নির্ণয় (ii) শুধু প্রতিবন্ধকতা লিপিবদ্ধ করা (উদ্দেশ্য ছাড়া) (iii) সর্বোচ্চ মুনাফা অর্জন — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "B", "easy", "conceptual",
        "LP aims to optimize (e.g. maximize profit) subject to constraints; an objective is essential, so (ii) alone is incomplete.",
        "উদ্দেশ্যসহ সর্বোত্তমকরণই লক্ষ্য; শুধু শর্ত লিখা যথেষ্ট নয়।",
    ),
    q(
        "Variables used in linear programming are always:",
        "যোগাশ্রয়ী প্রোগ্রামে ব্যবহৃত চলক সর্বদা কেমন?",
        ["positive only", "negative only", "non-negative", "both positive and negative freely"],
        ["শুধু ধনাত্মক", "শুধু ঋণাত্মক", "অঋণাত্মক", "ধনাত্মক ও ঋণাত্মক উভয়ই মুক্তভাবে"],
        "C", "easy", "factual",
        "Standard LP decision variables satisfy x, y ≥ 0 (non-negative).",
        "সিদ্ধান্ত চলক অঋণাত্মক: x, y ≥ 0।",
    ),
    q(
        "Regarding the objective function z in terms of decision variables x, y: (i) z is a function of x and y (ii) z is only of maximization type (iii) usually x, y ≥ 0",
        "উদ্দেশ্য অপেক্ষক z ও সিদ্ধান্ত চলক x, y সম্পর্কে— (i) z হলো x ও y এর ফাংশন (ii) z শুধুমাত্র সর্বোচ্চকরণ ধরনের হয় (iii) সাধারণত x, y ≥ 0 — কোনটি সঠিক?",
        ["i only", "ii only", "iii only", "i and iii only"],
        ["শুধু i", "শুধু ii", "শুধু iii", "শুধু i ও iii"],
        "D", "easy", "conceptual",
        "z = f(x,y) may be maximized or minimized; non-negativity is standard. So (i) and (iii).",
        "z সর্বোচ্চ বা সর্বনিম্ন হতে পারে; (i) ও (iii) সত্য।",
    ),
    q(
        "How many main steps are usually listed in solving a two-variable linear programming problem graphically at HSC level?",
        "HSC স্তরে দ্বিচলক যোগাশ্রয়ী প্রোগ্রাম লেখচিত্রে সমাধানের সাধারণত কয়টি প্রধান ধাপ বলা হয়?",
        ["4", "3", "2", "1"],
        ["৪টি", "৩টি", "২টি", "১টি"],
        "A", "easy", "factual",
        "Typical steps: formulate, graph constraints, find corner points, evaluate the objective — often summarized as four steps.",
        "গঠন, লেখ, প্রান্তিক বিন্দু, উদ্দেশ্য মূল্যায়ন — সাধারণত চার ধাপ।",
    ),
    q(
        "If the objective is z = 3x + 4y, evaluating at the corner (5, 2) gives:",
        "উদ্দেশ্য z = 3x + 4y হলে প্রান্তিক বিন্দু (5, 2)-এ মান কত?",
        ["15", "20", "23", "30"],
        ["15", "20", "23", "30"],
        "C", "easy", "numerical",
        "z(5, 2) = 3·5 + 4·2 = 15 + 8 = 23.",
        "z(5, 2) = 15 + 8 = 23।",
    ),
    q(
        "An objective function in two-variable LP must be:",
        "দ্বিচলক যোগাশ্রয়ী প্রোগ্রামে উদ্দেশ্য ফাংশন কেমন হতে হবে?",
        [
            "linear in x and y",
            "quadratic in x and y",
            "any nonlinear smooth function",
            "independent of both x and y",
        ],
        [
            "x ও y-এ রৈখিক",
            "x ও y-এ দ্বিঘাত",
            "যেকোনো অরৈখিক মসৃণ ফাংশন",
            "x ও y উভয়ের উপর নির্ভরশীল নয়",
        ],
        "A", "easy", "factual",
        "By definition the LP objective is a linear function of the decision variables.",
        "যোগাশ্রয়ী প্রোগ্রামে উদ্দেশ্য ফাংশন রৈখিক।",
    ),
    q(
        "Under 2x + 3y ≤ 6, x ≥ 0, y ≥ 0, the maximum of z = x + 2y equals:",
        "2x + 3y ≤ 6, x ≥ 0, y ≥ 0 শর্তে z = x + 2y এর সর্বোচ্চ মান কত?",
        ["3", "4", "6", "7"],
        ["3", "4", "6", "7"],
        "B", "medium", "numerical",
        "Corners: (0,0)→0, (3,0)→3, (0,2)→4. Maximum is 4 at (0,2).",
        "প্রান্তিক: (0,0), (3,0), (0,2); সর্বোচ্চ 4।",
    ),
    q(
        "Under x + y ≤ 2, x + 4y ≤ 4, x ≥ 0, y ≥ 0, the minimum of z = 3x + 6y equals:",
        "x + y ≤ 2, x + 4y ≤ 4, x ≥ 0, y ≥ 0 শর্তে z = 3x + 6y এর সর্বনিম্ন মান কত?",
        ["0", "8", "10", "12"],
        ["0", "8", "10", "12"],
        "A", "medium", "numerical",
        "All coefficients of z are non-negative and (0,0) is feasible, so the minimum is 0.",
        "z-এর সহগ ধনাত্মক এবং (0,0) সম্ভাব্য; সর্বনিম্ন 0।",
    ),
    q(
        "If z = 25 − x is to be maximized over a feasible set whose x-coordinates of corners are among {0, 5, 8, 15}, the maximum of z occurs where x is:",
        "z = 25 − x সর্বোচ্চকরণে সম্ভাব্য প্রান্তিক বিন্দুগুলোর x ∈ {0, 5, 8, 15} হলে সর্বোচ্চ মান কোন x-এ?",
        ["largest x", "smallest x", "x = 8 only", "any x equally"],
        ["বৃহত্তম x", "ক্ষুদ্রতম x", "শুধু x = 8", "যেকোনো x সমান"],
        "B", "medium", "conceptual",
        "z = 25 − x decreases as x increases, so the maximum is at the smallest feasible x.",
        "x বাড়লে z কমবে; ক্ষুদ্রতম x-এ সর্বোচ্চ z।",
    ),
    q(
        "For the objective z = 2x − y, which change increases z?",
        "উদ্দেশ্য z = 2x − y হলে কোন পরিবর্তনে z বাড়ে?",
        [
            "increasing x and decreasing y",
            "decreasing x and increasing y",
            "decreasing both x and y equally in a way that keeps 2x − y fixed",
            "setting x = 0 and maximizing y only",
        ],
        [
            "x বাড়ানো ও y কমানো",
            "x কমানো ও y বাড়ানো",
            "x ও y এমনভাবে কমানো যে 2x − y অপরিবর্তিত",
            "x = 0 রেখে শুধু y সর্বোচ্চ করা",
        ],
        "A", "medium", "conceptual",
        "Coefficient of x is +2 and of y is −1, so larger x and smaller y raise z.",
        "x-এর সহগ +2, y-এর −1; তাই x বাড়লে ও y কমলে z বাড়ে।",
    ),
    q(
        "Under 2x + y ≤ 8, 2x + 3y ≤ 12, x ≥ 0, y ≥ 0, the maximum of z = 4x + 3y is:",
        "2x + y ≤ 8, 2x + 3y ≤ 12, x ≥ 0, y ≥ 0 শর্তে z = 4x + 3y এর সর্বোচ্চ মান কত?",
        ["12", "16", "17", "18"],
        ["12", "16", "17", "18"],
        "D", "medium", "numerical",
        "Corners: (0,0)→0, (4,0)→16, (3,2)→18, (0,4)→12. Maximum 18 at (3,2).",
        "(3,2)-এ z = 18 সর্বোচ্চ।",
    ),
    q(
        "If profit per unit of product A is 40 and of B is 50, and x, y are units produced, the profit objective is:",
        "A পণ্যের একক মুনাফা ৪০ ও B-এর ৫০ এবং x, y উৎপাদন সংখ্যা হলে মুনাফার উদ্দেশ্য ফাংশন কোনটি?",
        ["z = 40x + 50y", "z = 40 + 50", "z = 40x − 50y", "z = x/40 + y/50"],
        ["z = 40x + 50y", "z = 40 + 50", "z = 40x − 50y", "z = x/40 + y/50"],
        "A", "easy", "application",
        "Total profit is 40 per unit of A times x plus 50 per unit of B times y.",
        "মোট মুনাফা = ৪০x + ৫০y।",
    ),
    q(
        "Which statement about optimizing a linear objective over a nonempty bounded polygonal feasible region is true?",
        "অশূন্য আবদ্ধ বহুভুজাকার সম্ভাব্য অঞ্চলে রৈখিক উদ্দেশ্য সর্বোত্তমকরণে কোনটি সত্য?",
        [
            "An optimum occurs at a corner point",
            "An optimum never occurs at a corner",
            "The objective must be zero at every corner",
            "Only maximization is possible, never minimization",
        ],
        [
            "সর্বোত্তম মান কোনো প্রান্তিক বিন্দুতে ঘটে",
            "সর্বোত্তম মান কখনো প্রান্তিক বিন্দুতে ঘটে না",
            "প্রতিটি প্রান্তিক বিন্দুতে উদ্দেশ্য শূন্য",
            "শুধু সর্বোচ্চকরণ সম্ভব, সর্বনিম্নকরণ নয়",
        ],
        "A", "medium", "conceptual",
        "The fundamental theorem of LP (2D graphical case): extrema of a linear objective occur at vertices.",
        "রৈখিক উদ্দেশ্যের চরম মান প্রান্তিক বিন্দুতে পাওয়া যায়।",
    ),
    q(
        "Under z = x + y with feasible corners (2, 5), (2, 0), (6, 0), (4, 5), the maximum of z is:",
        "z = x + y এবং প্রান্তিক বিন্দু (2, 5), (2, 0), (6, 0), (4, 5) হলে z এর সর্বোচ্চ মান কত?",
        ["6", "7", "9", "12"],
        ["6", "7", "9", "12"],
        "C", "medium", "numerical",
        "Values: 7, 2, 6, 9. Maximum is 9 at (4, 5).",
        "(4,5)-এ z = 9 সর্বোচ্চ।",
    ),
    q(
        "A cost objective z = 5x + 3y is to be minimized. Compared with maximization of the same z, the optimal corner:",
        "ব্যয় উদ্দেশ্য z = 5x + 3y সর্বনিম্নকরণে, একই z সর্বোচ্চকরণের তুলনায় সর্বোত্তম প্রান্তিক বিন্দু:",
        [
            "may differ; min and max need not share the same vertex",
            "must always be the same vertex",
            "must be the centroid of the region",
            "cannot exist if the region is bounded",
        ],
        [
            "ভিন্ন হতে পারে; সর্বনিম্ন ও সর্বোচ্চ একই শীর্ষে নাও হতে পারে",
            "সর্বদা একই শীর্ষে হবে",
            "অঞ্চলের কেন্দ্রবিন্দুতেই হবে",
            "অঞ্চল আবদ্ধ হলে অস্তিত্ব থাকে না",
        ],
        "A", "medium", "conceptual",
        "Max and min of a nonconstant linear function on a polygon occur at (generally) different vertices.",
        "সর্বোচ্চ ও সর্বনিম্ন সাধারণত ভিন্ন প্রান্তিক বিন্দুতে।",
    ),
    q(
        "If z = 2x + 7y subject to x + y ≤ 9, x + 2y ≤ 12, x ≥ 0, y ≥ 0, then max z equals:",
        "z = 2x + 7y এবং x + y ≤ 9, x + 2y ≤ 12, x ≥ 0, y ≥ 0 হলে max z কত?",
        ["0", "18", "33", "42"],
        ["0", "18", "33", "42"],
        "D", "medium", "numerical",
        "Corners (0,0), (9,0), (6,3), (0,6): z values 0, 18, 33, 42. Maximum 42 at (0,6).",
        "(0,6)-এ z = 42 সর্বোচ্চ।",
    ),
    q(
        "Which is an example of a minimization objective in a business LP?",
        "ব্যবসায়িক যোগাশ্রয়ী প্রোগ্রামে সর্বনিম্নকরণ উদ্দেশ্যের উদাহরণ কোনটি?",
        [
            "minimize total production cost z = 20x + 15y",
            "maximize revenue z = 20x + 15y",
            "require x + y ≤ 100 only, with no z",
            "set z = x² + y²",
        ],
        [
            "মোট উৎপাদন ব্যয় z = 20x + 15y ন্যূনতমকরণ",
            "আয় z = 20x + 15y সর্বোচ্চকরণ",
            "শুধু x + y ≤ 100, কোনো z নেই",
            "z = x² + y² নির্ধারণ",
        ],
        "A", "easy", "application",
        "Cost minimization is a classic LP objective; revenue max is maximization; quadratic z is not LP.",
        "ব্যয় ন্যূনতমকরণ ক্লাসিক LP উদ্দেশ্য।",
    ),
    q(
        "Evaluating z = x − y at A(1, 0), B(2, 0), C(1, 1) gives the minimum value:",
        "A(1, 0), B(2, 0), C(1, 1) বিন্দুতে z = x − y মূল্যায়নে সর্বনিম্ন মান কত?",
        ["−2", "0", "1", "2"],
        ["−2", "0", "1", "2"],
        "B", "medium", "numerical",
        "z(A)=1, z(B)=2, z(C)=0. The minimum among these is 0.",
        "মান 1, 2, 0; সর্বনিম্ন 0।",
    ),
    q(
        "Under constraints whose feasible corners include (0, 0) and (5, 0), for z = 7x + 3y the value at (5, 0) is:",
        "সম্ভাব্য প্রান্তিক বিন্দুতে (0, 0) ও (5, 0) থাকলে z = 7x + 3y এর (5, 0)-এ মান কত?",
        ["0", "15", "35", "38"],
        ["0", "15", "35", "38"],
        "C", "easy", "numerical",
        "z(5, 0) = 7·5 + 3·0 = 35.",
        "z(5, 0) = 35।",
    ),
]


# =============================================================================
# hm2_27_ch02_t03 — Graphical optimization / লেখচিত্রের সাহায্যে সর্বোত্তম মান
# =============================================================================
T03 = [
    q(
        "Under 2x + y ≤ 8, 2x + 3y ≤ 12, x ≥ 0, y ≥ 0, maximize z = 4x + 3y. The optimal value is:",
        "2x + y ≤ 8, 2x + 3y ≤ 12, x ≥ 0, y ≥ 0 শর্তে z = 4x + 3y সর্বোচ্চকরণে সর্বোত্তম মান কত?",
        ["12", "16", "17", "18"],
        ["12", "16", "17", "18"],
        "D", "medium", "numerical",
        "Evaluate at corners (0,0), (4,0), (3,2), (0,4): maximum 18 at (3,2).",
        "(3,2)-এ সর্বোচ্চ মান 18।",
    ),
    q(
        "A graph shows feasible corners (0, 0), (5, 0), (2, 3), (0, 4). For z = 7x + 3y the maximum is:",
        "সম্ভাব্য প্রান্তিক বিন্দু (0, 0), (5, 0), (2, 3), (0, 4)। z = 7x + 3y এর সর্বোচ্চ মান কত?",
        ["12", "15", "23", "35"],
        ["12", "15", "23", "35"],
        "D", "medium", "numerical",
        "z: 0, 35, 23, 12. Maximum 35 at (5,0).",
        "(5,0)-এ z = 35 সর্বোচ্চ।",
    ),
    q(
        "Under 5x + 2y ≤ 30, x ≥ 2, 0 ≤ y ≤ 5, maximize z = x + y. Optimal z equals:",
        "5x + 2y ≤ 30, x ≥ 2, 0 ≤ y ≤ 5 শর্তে z = x + y সর্বোচ্চকরণে মান কত?",
        ["6", "7", "9", "12"],
        ["6", "7", "9", "12"],
        "C", "medium", "numerical",
        "Corners (2,0), (6,0), (4,5), (2,5): z = 2, 6, 9, 7. Maximum 9.",
        "(4,5)-এ z = 9 সর্বোচ্চ।",
    ),
    q(
        "Under x + y ≤ 9, x + 2y ≤ 12, x ≥ 0, y ≥ 0, maximize z = 2x + 7y. The maximum is:",
        "x + y ≤ 9, x + 2y ≤ 12, x ≥ 0, y ≥ 0 শর্তে z = 2x + 7y এর সর্বোচ্চ মান কত?",
        ["0", "18", "33", "42"],
        ["0", "18", "33", "42"],
        "D", "medium", "numerical",
        "Corners (0,0), (9,0), (6,3), (0,6) give z = 0, 18, 33, 42.",
        "(0,6)-এ সর্বোচ্চ 42।",
    ),
    q(
        "Feasible region has corners A(1,0), B(2,0), C(1,1). Minimize z = x − y. The minimum is:",
        "সম্ভাব্য অঞ্চলের শীর্ষ A(1,0), B(2,0), C(1,1)। z = x − y এর সর্বনিম্ন মান কত?",
        ["−2", "0", "1", "2"],
        ["−2", "0", "1", "2"],
        "B", "medium", "numerical",
        "z values 1, 2, 0; minimum is 0 at C(1,1).",
        "C(1,1)-এ সর্বনিম্ন 0।",
    ),
    q(
        "Under 2x + 3y ≤ 6, x ≥ 0, y ≥ 0, the maximum of z = x + 2y is attained at:",
        "2x + 3y ≤ 6, x ≥ 0, y ≥ 0 শর্তে z = x + 2y এর সর্বোচ্চ মান কোন বিন্দুতে?",
        ["(0, 0)", "(3, 0)", "(0, 2)", "(1, 1)"],
        ["(0, 0)", "(3, 0)", "(0, 2)", "(1, 1)"],
        "C", "medium", "numerical",
        "Among corners, z(0,2) = 4 is largest (z(3,0)=3, z(0,0)=0).",
        "(0,2)-এ z = 4 সর্বোচ্চ।",
    ),
    q(
        "Under x + y ≤ 6, y ≥ 0, x ≥ 0, maximize z = 2x − y. The maximum value is:",
        "x + y ≤ 6, x ≥ 0, y ≥ 0 শর্তে z = 2x − y এর সর্বোচ্চ মান কত?",
        ["6", "8", "10", "12"],
        ["6", "8", "10", "12"],
        "D", "medium", "numerical",
        "Corners (0,0)→0, (6,0)→12, (0,6)→−6. Maximum 12 at (6,0).",
        "(6,0)-এ z = 12 সর্বোচ্চ।",
    ),
    q(
        "A triangular feasible region has vertices (0,0), (5,0), (0,6). If z = 25 − x, then max z equals:",
        "ত্রিভুজাকার সম্ভাব্য অঞ্চলের শীর্ষ (0,0), (5,0), (0,6)। z = 25 − x হলে max z কত?",
        ["20", "25", "25 − 5 = 20 only among x>0", "30"],
        ["20", "25", "শুধু x>0 হলে 20", "30"],
        "B", "medium", "numerical",
        "Smallest feasible x among corners is 0 at (0,0) and (0,6); z = 25.",
        "ক্ষুদ্রতম x = 0; z = 25।",
    ),
    q(
        "Under x + y ≤ 5, x + 2y ≥ 8, x ≥ 0, y ≥ 0, which statements hold? (i) Corner points include (2,3), (0,4), (0,5) (ii) Minimum of 2x − y equals −5 (iii) Maximum of 2x − y equals 1",
        "x + y ≤ 5, x + 2y ≥ 8, x ≥ 0, y ≥ 0 শর্তাধীনে— (i) প্রান্তিক বিন্দু (2,3), (0,4), (0,5) (ii) 2x − y এর সর্বনিম্ন = −5 (iii) 2x − y এর সর্বোচ্চ = 1 — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "hard", "numerical",
        "Corners: (0,4), (0,5), (2,3). For w=2x−y: values −4, −5, 1. So min −5, max 1; all three statements hold.",
        "প্রান্তিক সঠিক; 2x−y এর মান −4, −5, 1 — সর্বনিম্ন −5, সর্বোচ্চ 1।",
    ),
    q(
        "To solve a 2-variable LP graphically, after drawing the feasible region one should:",
        "লেখচিত্রে দ্বিচলক LP সমাধানে সম্ভাব্য অঞ্চল আঁকার পর কী করতে হয়?",
        [
            "evaluate the objective at each corner point",
            "only shade the second quadrant",
            "discard all axis intercepts",
            "replace inequalities by x² + y² = 1",
        ],
        [
            "প্রতিটি প্রান্তিক বিন্দুতে উদ্দেশ্য ফাংশন মূল্যায়ন করা",
            "শুধু দ্বিতীয় চতুর্ভাগ ছায়াঙ্কিত করা",
            "সব অক্ষ ছেদবিন্দু বাদ দেওয়া",
            "অসমতাকে x² + y² = 1 দিয়ে প্রতিস্থাপন",
        ],
        "A", "easy", "conceptual",
        "Graphical method: compare objective values at the vertices of the feasible polygon.",
        "প্রান্তিক বিন্দুতে উদ্দেশ্য তুলনা করে সর্বোত্তম মান পাওয়া যায়।",
    ),
    q(
        "Under 3x + 4y ≥ 12, 4x + 3y ≥ 12, x ≥ 0, y ≥ 0, for z = 4x + 3y the minimum occurs near the intersection of the two lines. That intersection is:",
        "3x + 4y ≥ 12, 4x + 3y ≥ 12, x ≥ 0, y ≥ 0 এবং z = 4x + 3y সর্বনিম্নকরণে দুই রেখার ছেদবিন্দু কোনটি?",
        ["(0, 4)", "(12/7, 12/7)", "(3, 0)", "(0, 0)"],
        ["(0, 4)", "(12/7, 12/7)", "(3, 0)", "(0, 0)"],
        "B", "hard", "numerical",
        "Solve 3x+4y=12 and 4x+3y=12: multiply first by 3 and second by 4 → 9x+12y=36, 16x+12y=48 → 7x=12 → x=12/7, y=12/7.",
        "সমাধানে x = y = 12/7।",
    ),
    q(
        "If a feasible region is unbounded and z = x + y (coefficients positive), then:",
        "সম্ভাব্য অঞ্চল অনাবদ্ধ এবং z = x + y (সহগ ধনাত্মক) হলে:",
        [
            "a finite maximum may fail to exist, while a minimum can occur at a corner",
            "both max and min always exist and are equal",
            "z is constant everywhere",
            "the origin is always optimal for the maximum",
        ],
        [
            "সসীম সর্বোচ্চ নাও থাকতে পারে; সর্বনিম্ন কোনো প্রান্তিকে থাকতে পারে",
            "সর্বোচ্চ ও সর্বনিম্ন সর্বদা আছে ও সমান",
            "সর্বত্র z ধ্রুবক",
            "সর্বোচ্চের জন্য মূলবিন্দুই সর্বদা সর্বোত্তম",
        ],
        "A", "hard", "conceptual",
        "With positive coefficients, z → ∞ along an unbounded ray, so max may be infinite; min still at a vertex if the region is closed.",
        "ধনাত্মক সহগে অনাবদ্ধ দিকে z → ∞; সর্বনিম্ন প্রান্তিকে থাকতে পারে।",
    ),
    q(
        "Corners of a feasible set are (0,0), (4,0), (0,3). Maximize z = 2x + 5y. Optimal point and value:",
        "সম্ভাব্য শীর্ষ (0,0), (4,0), (0,3)। z = 2x + 5y সর্বোচ্চকরণে সর্বোত্তম বিন্দু ও মান:",
        ["(4, 0), z = 8", "(0, 3), z = 15", "(0, 0), z = 0", "(2, 1.5), z = 11.5"],
        ["(4, 0), z = 8", "(0, 3), z = 15", "(0, 0), z = 0", "(2, 1.5), z = 11.5"],
        "B", "medium", "numerical",
        "z(4,0)=8, z(0,3)=15, z(0,0)=0. Optimum at (0,3) with 15.",
        "(0,3)-এ z = 15 সর্বোত্তম।",
    ),
    q(
        "Under x ≥ 0, y ≥ 0, x + 4y ≤ 4, x + y ≤ 2, maximize z = 3x + 6y. The maximum is:",
        "x ≥ 0, y ≥ 0, x + 4y ≤ 4, x + y ≤ 2 শর্তে z = 3x + 6y এর সর্বোচ্চ মান কত?",
        ["0", "6", "8", "12"],
        ["0", "6", "8", "12"],
        "C", "hard", "numerical",
        "Corners (0,0), (2,0), (4/3, 2/3), (0,1): z = 0, 6, 8, 6. Maximum 8 at (4/3, 2/3).",
        "ছেদবিন্দু (4/3, 2/3)-এ z = 8 সর্বোচ্চ।",
    ),
    q(
        "Graphical optimization fails to apply directly when:",
        "লেখচিত্রের সাহায্যে সর্বোত্তমকরণ সরাসরি প্রযোজ্য নয় যখন:",
        [
            "there are more than two decision variables",
            "there are exactly two variables and linear constraints",
            "the objective is linear in two variables",
            "the feasible region is a polygon in the plane",
        ],
        [
            "সিদ্ধান্ত চলক দুইয়ের বেশি",
            "ঠিক দুই চলক ও রৈখিক শর্ত আছে",
            "উদ্দেশ্য দুই চলকে রৈখিক",
            "সম্ভাব্য অঞ্চল সমতলে বহুভুজ",
        ],
        "A", "easy", "conceptual",
        "The plane graph method is for two variables; higher dimensions need other algorithms.",
        "লেখচিত্র পদ্ধতি দ্বিচলকের জন্য; বেশি চলকে অন্য পদ্ধতি লাগে।",
    ),
    q(
        "At the feasible corners (0,0), (8,0), (6,2), (0,5), the objective z = 3x + 2y has maximum:",
        "প্রান্তিক বিন্দু (0,0), (8,0), (6,2), (0,5)-এ z = 3x + 2y এর সর্বোচ্চ মান কত?",
        ["10", "24", "22", "16"],
        ["10", "24", "22", "16"],
        "B", "medium", "numerical",
        "z: 0, 24, 22, 10. Maximum 24 at (8,0).",
        "(8,0)-এ z = 24 সর্বোচ্চ।",
    ),
    q(
        "A factory produces x units of A and y of B with constraints x + y ≤ 40, 2x + y ≤ 60, x,y ≥ 0. Profit z = 30x + 20y. Maximum profit is:",
        "কারখানা A-এর x ও B-এর y একক উৎপাদন করে; শর্ত x + y ≤ 40, 2x + y ≤ 60, x,y ≥ 0। মুনাফা z = 30x + 20y। সর্বোচ্চ মুনাফা কত?",
        ["800", "900", "1000", "1200"],
        ["800", "900", "1000", "1200"],
        "C", "hard", "application",
        "Corners (0,0), (30,0), (20,20), (0,40): z = 0, 900, 1000, 800. Maximum 1000 at (20,20).",
        "প্রান্তিক মান 0, 900, 1000, 800; সর্বোচ্চ 1000।",
    ),
    q(
        "If every corner of a bounded feasible region gives the same value of a linear objective z, then:",
        "আবদ্ধ সম্ভাব্য অঞ্চলের প্রতিটি প্রান্তিক বিন্দুতে রৈখিক z একই মান দিলে:",
        [
            "z is constant on the whole feasible region",
            "the problem has no feasible point",
            "z must be nonlinear",
            "only one corner is optimal and others are infeasible",
        ],
        [
            "সম্পূর্ণ সম্ভাব্য অঞ্চলে z ধ্রুবক",
            "কোনো সম্ভাব্য বিন্দু নেই",
            "z অবশ্যই অরৈখিক",
            "শুধু এক প্রান্তিক সর্বোত্তম ও বাকি অসম্ভাব্য",
        ],
        "A", "hard", "conceptual",
        "A linear function with equal values at all vertices of a polygon is constant on the convex hull.",
        "সব শীর্ষে সমান মান হলে উত্তল অঞ্চলে z ধ্রুবক।",
    ),
    q(
        "Under x + 2y ≤ 10, x ≤ 6, x ≥ 0, y ≥ 0, minimize z = x + 3y. The minimum is:",
        "x + 2y ≤ 10, x ≤ 6, x ≥ 0, y ≥ 0 শর্তে z = x + 3y এর সর্বনিম্ন মান কত?",
        ["0", "6", "10", "15"],
        ["0", "6", "10", "15"],
        "A", "easy", "numerical",
        "(0,0) is feasible and z ≥ 0 on the first quadrant for these coefficients, so min z = 0.",
        "(0,0) সম্ভাব্য এবং z ≥ 0; সর্বনিম্ন 0।",
    ),
    q(
        "Feasible corners are (2,5), (2,0), (6,0), (4,5). For z = 5x + 2y, the maximum value is:",
        "প্রান্তিক বিন্দু (2,5), (2,0), (6,0), (4,5)। z = 5x + 2y এর সর্বোচ্চ মান কত?",
        ["20", "30", "32", "40"],
        ["20", "30", "32", "40"],
        "B", "medium", "numerical",
        "z: 20, 10, 30, 30. Maximum 30 (attained at (6,0) and also check (4,5)=30).",
        "(6,0) ও (4,5) উভয়ে z = 30 সর্বোচ্চ।",
    ),
]


def write_topic(topic_id: str, rows: list[dict]) -> dict:
    if len(rows) != 20:
        raise SystemExit(f"{topic_id}: expected 20 rows, got {len(rows)}")
    clean = []
    for i, r in enumerate(rows, 1):
        err = validate_record(r)
        if err:
            raise SystemExit(f"{topic_id}#{i}: {err}\n{json.dumps(r, ensure_ascii=False)[:400]}")
        clean.append(r)
    stems = [r["stem_en"] for r in clean]
    if len(set(map(str.casefold, stems))) != 20:
        raise SystemExit(f"{topic_id}: duplicate stems")
    path = TOPICS / f"{topic_id}.jsonl"
    path.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in clean) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {path.name}: {len(clean)}")
    return {"path": str(path.relative_to(ROOT)).replace("\\", "/"), "count": len(clean)}


def main() -> None:
    assert len(T01) == 20 and len(T02) == 20 and len(T03) == 20
    counts = {}
    counts["hm2_27_ch02_t01"] = write_topic("hm2_27_ch02_t01", T01)["count"]
    counts["hm2_27_ch02_t02"] = write_topic("hm2_27_ch02_t02", T02)["count"]
    counts["hm2_27_ch02_t03"] = write_topic("hm2_27_ch02_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm2_27_ch02",
        "title_en": "Linear Programming",
        "title_bn": "যোগাশ্রয়ী প্রোগ্রাম",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(40, 44)],
        "topics": {
            "hm2_27_ch02_t01": {
                "title_en": "Linear constraints and feasible region",
                "title_bn": "রৈখিক শর্ত ও সম্ভাব্য অঞ্চল",
                "udvash_types": [
                    "LP formulation constraints from word problems",
                    "feasibility / corner points",
                    "bounded vs unbounded regions",
                    "linear vs nonlinear inequalities",
                ],
                "count": 20,
            },
            "hm2_27_ch02_t02": {
                "title_en": "Objective functions",
                "title_bn": "উদ্দেশ্য ফাংশন",
                "udvash_types": [
                    "identify objective vs constraints",
                    "non-negativity of variables",
                    "max/min interpretation",
                    "evaluate z at given points",
                ],
                "count": 20,
            },
            "hm2_27_ch02_t03": {
                "title_en": "Graphical optimization",
                "title_bn": "লেখচিত্রের সাহায্যে সর্বোত্তম মান",
                "udvash_types": [
                    "corner-point method",
                    "max/min from listed vertices",
                    "text rewrite of figure-only graphs",
                    "application word LPs",
                ],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "figure_only_graphs": "Printed LP shaded-region / multi-panel figures rewritten as text stems with explicit corners or inequalities",
            "garbled_stems": "Noisy OCR reconstructed from answer-key algebra and standard board forms",
            "stimulus_pairs": "Linked stimulus blocks curated as standalone clear stems",
            "ambiguous_option_glyphs": "Broken Bangla/option glyphs replaced with closed-form HSC standards",
        },
        "low_confidence": [
            "OCR on pp. 40–43 noisy; column text and solution lines used to reconstruct stems.",
            "Inline math stored as plain text (≤, ≥, ∈) for JSONL.",
            "Some printed figure keys incomplete; text-equivalent corner lists retained.",
            "Figure-linked stimulus items rewritten without relying on diagram OCR.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm2_ch02.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
        "math2_progress": {
            "topics_complete": "6/30",
            "note": "Ch02 continues higher_mathematics 2nd paper after Ch01 (60Q)",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch02_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
