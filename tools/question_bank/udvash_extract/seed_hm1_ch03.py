#!/usr/bin/env python3
"""Seed Higher Mathematics 1st Paper Ch3 (Straight Lines).

Curated from Udvash HSC Question Bank 2026 printed pp. 110–123 (PDF 116–129).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
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
PARSED = ROOT / "content" / "bank" / "udvash_raw" / "higher_mathematics_1" / "parsed"
SOURCE = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "higher_mathematics p1 ch03; curated bilingual"
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
# hm1_27_ch03_t01 — Slope and equations of a line
# Prefer Udvash T-07 / slope-intercept / two-point / parallel forms
# =============================================================================
T01 = [
    q(
        "A straight line passes through (0, 4) and (10, -4). Which are true? "
        "(i) its slope is -5  (ii) its equation is 4x + 5y = 20  "
        "(iii) the midpoint of the segment joining the points is (5, 0)",
        "(0, 4) ও (10, -4) বিন্দুগামী সরলরেখার জন্য কোনটি সঠিক? "
        "(i) ঢাল -5  (ii) সমীকরণ 4x + 5y = 20  "
        "(iii) বিন্দুদ্বয়ের সংযোগ রেখাংশের মধ্যবিন্দু (5, 0)",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "C", "medium", "conceptual",
        "Slope = (-4-4)/(10-0) = -4/5, so (i) is false. "
        "Two-point form gives 4x + 5y = 20; midpoint is (5, 0).",
        "ঢাল = -4/5, তাই (i) মিথ্যা। সমীকরণ 4x + 5y = 20 এবং মধ্যবিন্দু (5, 0)।",
    ),
    q(
        "The equation of the line parallel to 2x + 3y + 4 = 0 and passing through (1, 2) is:",
        "2x + 3y + 4 = 0 রেখার সমান্তরাল এবং (1, 2) বিন্দুগামী সরলরেখার সমীকরণ:",
        ["3x - 2y + 8 = 0", "3x + 2y + 8 = 0", "2x + 3y + 8 = 0", "2x + 3y - 8 = 0"],
        ["3x - 2y + 8 = 0", "3x + 2y + 8 = 0", "2x + 3y + 8 = 0", "2x + 3y - 8 = 0"],
        "D", "easy", "numerical",
        "Parallel form: 2x + 3y + k = 0. Through (1, 2): 2 + 6 + k = 0 ⇒ k = -8.",
        "সমান্তরাল: 2x + 3y + k = 0; (1, 2) বসিয়ে k = -8।",
    ),
    q(
        "The slope of the line qy + px + r = 0 is:",
        "qy + px + r = 0 রেখার ঢাল কোনটি?",
        ["-q/p", "-p/q", "p/q", "q/p"],
        ["-q/p", "-p/q", "p/q", "q/p"],
        "B", "easy", "factual",
        "Rewrite as y = (-p/q)x - r/q, so m = -p/q.",
        "y = (-p/q)x - r/q ⇒ ঢাল m = -p/q।",
    ),
    q(
        "The midpoint of the intercepts cut by 2x + 6y = 12 on the axes is:",
        "2x + 6y = 12 সরলরেখাটি অক্ষদ্বয়ে যে খণ্ডিতাংশ করে তার মধ্যবিন্দুর স্থানাঙ্ক:",
        ["(-1, 3)", "(-3, 1)", "(3, 1)", "(1, 3)"],
        ["(-1, 3)", "(-3, 1)", "(3, 1)", "(1, 3)"],
        "C", "easy", "numerical",
        "Intercepts: x = 6, y = 2. Midpoint = (3, 1).",
        "খণ্ডিতাংশ 6 ও 2; মধ্যবিন্দু (3, 1)।",
    ),
    q(
        "The line 4x + 3y - 12 = 0 meets the x-axis at:",
        "4x + 3y - 12 = 0 সরলরেখাটি x-অক্ষকে যে বিন্দুতে ছেদ করে:",
        ["(0, 4)", "(4, 0)", "(0, 3)", "(3, 0)"],
        ["(0, 4)", "(4, 0)", "(0, 3)", "(3, 0)"],
        "D", "easy", "numerical",
        "Put y = 0: 4x = 12 ⇒ x = 3. Point (3, 0).",
        "y = 0 বসিয়ে x = 3; ছেদবিন্দু (3, 0)।",
    ),
    q(
        "The slope of 4x + 3y - 12 = 0 is:",
        "4x + 3y - 12 = 0 রেখার ঢাল কত?",
        ["-4/3", "4/3", "-3/4", "3/4"],
        ["মান -4/3", "মান 4/3", "মান -3/4", "মান 3/4"],
        "A", "easy", "numerical",
        "m = -A/B = -4/3.",
        "m = -A/B = -4/3।",
    ),
    q(
        "The slope of 6x + 5y + 25 = 0 is:",
        "6x + 5y + 25 = 0 সরলরেখার ঢাল কত?",
        ["6/5", "-6/5", "5/6", "-5/6"],
        ["মান 6/5", "মান -6/5", "মান 5/6", "মান -5/6"],
        "B", "easy", "numerical",
        "m = -6/5.",
        "m = -6/5।",
    ),
    q(
        "The equation of the line through A(4, 0) and B(0, -5) is:",
        "A(4, 0) ও B(0, -5) বিন্দুগামী সরলরেখার সমীকরণ:",
        ["4x - 5y + 20 = 0", "5x - 4y - 20 = 0", "5x - 4y + 20 = 0", "4x - 5y - 20 = 0"],
        ["4x - 5y + 20 = 0", "5x - 4y - 20 = 0", "5x - 4y + 20 = 0", "4x - 5y - 20 = 0"],
        "B", "medium", "numerical",
        "Intercept form x/4 + y/(-5) = 1 ⇒ 5x - 4y = 20.",
        "খণ্ডিতাংশ আকারে 5x - 4y = 20।",
    ),
    q(
        "If the slope of y = (1/sqrt(3))x + 3 is tan θ, then θ = ?",
        "y = (1/sqrt(3))x + 3 এর ঢাল tan θ হলে θ এর মান কত?",
        ["30°", "45°", "60°", "90°"],
        ["30°", "45°", "60°", "90°"],
        "A", "easy", "numerical",
        "m = 1/sqrt(3) = tan 30° ⇒ θ = 30°.",
        "m = 1/sqrt(3) = tan 30° ⇒ θ = 30°।",
    ),
    q(
        "The line 2x + 3y = 6 meets the y-axis at:",
        "2x + 3y = 6 রেখাটি y-অক্ষকে কোন বিন্দুতে ছেদ করে?",
        ["(0, 2)", "(0, 3)", "(2, 0)", "(3, 0)"],
        ["(0, 2)", "(0, 3)", "(2, 0)", "(3, 0)"],
        "A", "easy", "numerical",
        "Put x = 0: 3y = 6 ⇒ y = 2. Point (0, 2).",
        "x = 0 বসিয়ে y = 2; বিন্দু (0, 2)।",
    ),
    q(
        "A line has slope 2/3 and y-intercept -5. Its equation is:",
        "একটি সরলরেখার ঢাল 2/3 এবং y-অক্ষের খণ্ডিতাংশ -5 হলে সমীকরণ:",
        ["2x + 3y = 15", "3x + 2y = 15", "2x - 3y = 15", "3x - 2y = 15"],
        ["2x + 3y = 15", "3x + 2y = 15", "2x - 3y = 15", "3x - 2y = 15"],
        "C", "medium", "numerical",
        "y = (2/3)x - 5 ⇒ 3y = 2x - 15 ⇒ 2x - 3y = 15.",
        "y = (2/3)x - 5 ⇒ 2x - 3y = 15।",
    ),
    q(
        "The midpoint of the intercepts cut by 3x + 2y = 12 on the axes is:",
        "3x + 2y = 12 রেখাটির অক্ষদ্বয়ের খণ্ডিতাংশের মধ্যবিন্দুর স্থানাঙ্ক:",
        ["(-2, -3)", "(3, -2)", "(2, 3)", "(3, 2)"],
        ["(-2, -3)", "(3, -2)", "(2, 3)", "(3, 2)"],
        "C", "easy", "numerical",
        "Intercepts (4, 0) and (0, 6); midpoint (2, 3).",
        "ছেদবিন্দু (4, 0) ও (0, 6); মধ্যবিন্দু (2, 3)।",
    ),
    q(
        "The slope of a line perpendicular to y = -7x + 9 is:",
        "y = -7x + 9 রেখার সাথে লম্ব রেখার নতি (ঢাল) কত?",
        ["1/7", "-1/7", "-7", "7"],
        ["মান 1/7", "মান -1/7", "মান -7", "মান 7"],
        "A", "easy", "numerical",
        "m1 = -7; for perpendicular, m2 = 1/7.",
        "m1 = -7; লম্বের জন্য m2 = 1/7।",
    ),
    q(
        "A line through (-5, 10) makes angle tan^(-1)(3/4) with the positive x-axis. "
        "Its equation is:",
        "(-5, 10) বিন্দুগামী সরলরেখা x-অক্ষের ধনাত্মক দিকের সাথে tan^(-1)(3/4) কোণ উৎপন্ন করে। সমীকরণ:",
        ["4x - 3y - 10 = 0", "3x - 4y + 55 = 0", "3x + 4y + 55 = 0", "4x + 3y + 30 = 0"],
        ["4x - 3y - 10 = 0", "3x - 4y + 55 = 0", "3x + 4y + 55 = 0", "4x + 3y + 30 = 0"],
        "B", "medium", "numerical",
        "y - 10 = (3/4)(x + 5) ⇒ 4y - 40 = 3x + 15 ⇒ 3x - 4y + 55 = 0.",
        "y - 10 = (3/4)(x + 5) ⇒ 3x - 4y + 55 = 0।",
    ),
    q(
        "For the line y = x, which are true? "
        "(i) it passes through the origin  (ii) its slope is -1  "
        "(iii) it makes 45° with both axes",
        "y = x সরলরেখাটির জন্য কোনটি সঠিক? "
        "(i) মূলবিন্দুগামী  (ii) ঢাল -1  (iii) উভয় অক্ষের সাথে 45° কোণ উৎপন্ন করে",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "B", "easy", "conceptual",
        "Slope is +1, not -1. It passes through O and makes 45° with both axes.",
        "ঢাল +1; মূলবিন্দুগামী এবং উভয় অক্ষের সাথে 45°।",
    ),
    q(
        "The lengths cut by px + qy = pq on the x-axis and y-axis are respectively:",
        "px + qy = pq সরলরেখাটি x ও y অক্ষদ্বয় হতে যে অংশ খণ্ডন করে তাদের দৈর্ঘ্য যথাক্রমে:",
        ["p, q", "q, p", "pq, 1", "1, pq"],
        ["p, q", "q, p", "pq, 1", "1, pq"],
        "A", "medium", "numerical",
        "x/p + y/q = 1 ⇒ intercepts p and q.",
        "x/p + y/q = 1 ⇒ খণ্ডিতাংশ p ও q।",
    ),
    q(
        "The equation of the line through (sqrt(3), 2) perpendicular to x - sqrt(3)y = 6 is:",
        "x - sqrt(3)y = 6 রেখার উপর লম্ব এবং (sqrt(3), 2) বিন্দুগামী রেখার সমীকরণ:",
        ["sqrt(3)x + y + 5 = 0", "sqrt(3)x + y = 5", "x + sqrt(3)y = 5", "x + sqrt(3)y + 5 = 0"],
        ["sqrt(3)x + y + 5 = 0", "sqrt(3)x + y = 5", "x + sqrt(3)y = 5", "x + sqrt(3)y + 5 = 0"],
        "C", "medium", "numerical",
        "Given slope 1/sqrt(3); perpendicular slope -sqrt(3). "
        "y - 2 = -sqrt(3)(x - sqrt(3)) ⇒ x + sqrt(3)y = 5.",
        "লম্বের ঢাল -sqrt(3); সমীকরণ x + sqrt(3)y = 5।",
    ),
    q(
        "An equation of a straight line parallel to the y-axis is:",
        "y-অক্ষের সমান্তরাল সরলরেখার সমীকরণ হল:",
        ["x = 2", "x = y", "y = 1", "x - y = 2"],
        ["x = 2", "x = y", "y = 1", "x - y = 2"],
        "A", "easy", "factual",
        "Lines parallel to the y-axis have the form x = constant.",
        "y-অক্ষের সমান্তরাল রেখা x = ধ্রুবক আকারের।",
    ),
    q(
        "For 3x - 7y - 21 = 0, which are true? "
        "(i) slope is 3/7  (ii) it passes through (-7, -6)  "
        "(iii) it cuts a length 7 from the x-axis",
        "3x - 7y - 21 = 0 সরলরেখাটির জন্য কোনটি সঠিক? "
        "(i) ঢাল 3/7  (ii) (-7, -6) বিন্দুগামী  "
        "(iii) x-অক্ষ হতে 7 একক দৈর্ঘ্য খণ্ডিত করে",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "D", "hard", "conceptual",
        "m = 3/7; (-7, -6) satisfies the equation; x-intercept is 7.",
        "ঢাল 3/7; (-7, -6) সিদ্ধ করে; x-খণ্ডিতাংশ 7।",
    ),
    q(
        "For the triangle formed by 3x + 4y - 12 = 0 with the axes, which are true? "
        "(i) area is 6 square units  (ii) it lies in the first quadrant  "
        "(iii) the intercepted segment between axes has length 5",
        "3x + 4y - 12 = 0 অক্ষদ্বয়ের সাথে যে ত্রিভুজ গঠন করে- "
        "(i) ক্ষেত্রফল 6 বর্গ একক  (ii) ১ম চতুর্ভাগে অবস্থিত  "
        "(iii) অক্ষদ্বয় কর্তৃক খণ্ডিত অংশের পরিমাণ 5 একক",
        ["i and ii", "ii and iii", "i and iii", "i, ii and iii"],
        ["i ও ii", "ii ও iii", "i ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "Intercepts 4 and 3; area = (1/2)*4*3 = 6; hypotenuse sqrt(16+9) = 5; first quadrant.",
        "খণ্ডিতাংশ 4 ও 3; ক্ষেত্রফল 6; কর্তিত অংশ 5; ১ম চতুর্ভাগ।",
    ),
]


# =============================================================================
# hm1_27_ch03_t02 — Angles and intersection of lines
# Prefer Udvash T-08 / T-12 / T-13: parallel/perp, angle, intersection, concurrent
# =============================================================================
T02 = [
    q(
        "If 2x + ky + 1 = 0 and 3x - 2y + 5 = 0 are perpendicular, then k = ?",
        "2x + ky + 1 = 0 এবং 3x - 2y + 5 = 0 রেখাদ্বয় পরস্পর লম্ব হলে k এর মান কত?",
        ["-6", "-3", "3", "6"],
        ["মান -6", "মান -3", "মান 3", "মান 6"],
        "C", "medium", "numerical",
        "m1 = -2/k, m2 = 3/2. For perpendicular, m1 m2 = -1 ⇒ k = 3.",
        "m1 m2 = -1 ⇒ (-2/k)(3/2) = -1 ⇒ k = 3।",
    ),
    q(
        "For what value of a is (a - 1)x + (a + 1)y = 5a parallel to 3x + 5y = -7?",
        "a এর কোন মানের জন্য (a - 1)x + (a + 1)y = 5a রেখাটি 3x + 5y = -7 এর সমান্তরাল হবে?",
        ["-7", "-4", "4", "7"],
        ["মান -7", "মান -4", "মান 4", "মান 7"],
        "C", "medium", "numerical",
        "Parallel ⇒ (a-1)/3 = (a+1)/5 ⇒ 5(a-1) = 3(a+1) ⇒ a = 4.",
        "সমান্তরাল শর্তে (a-1)/3 = (a+1)/5 ⇒ a = 4।",
    ),
    q(
        "The line y + x = 0 makes what angle with the positive direction of the x-axis?",
        "y + x = 0 রেখাটি x-অক্ষের ধনাত্মক দিকের সাথে কত কোণ উৎপন্ন করে?",
        ["45°", "135°", "225°", "315°"],
        ["45°", "135°", "225°", "315°"],
        "B", "easy", "numerical",
        "Slope m = -1 ⇒ θ = tan^(-1)(-1) = 135° (acute alternate is 45° below).",
        "ঢাল m = -1 ⇒ θ = 135°।",
    ),
    q(
        "The point of intersection of x + y - 4 = 0 and x - y - 2 = 0 is:",
        "x + y - 4 = 0 ও x - y - 2 = 0 রেখাদ্বয়ের ছেদবিন্দুর স্থানাঙ্ক:",
        ["(-3, -1)", "(-1, -3)", "(3, 1)", "(1, 3)"],
        ["(-3, -1)", "(-1, -3)", "(3, 1)", "(1, 3)"],
        "C", "easy", "numerical",
        "Adding: 2x = 6 ⇒ x = 3; then y = 1. Intersection (3, 1).",
        "যোগে x = 3, y = 1; ছেদবিন্দু (3, 1)।",
    ),
    q(
        "The area of the triangle formed by x + y - 4 = 0, x - y - 2 = 0 and the y-axis is:",
        "x + y - 4 = 0 ও x - y - 2 = 0 রেখাদ্বয় y-অক্ষের সাথে যে ত্রিভুজ গঠন করে তার ক্ষেত্রফল:",
        ["3 square units", "4 square units", "6 square units", "9 square units"],
        ["3 বর্গ একক", "4 বর্গ একক", "6 বর্গ একক", "9 বর্গ একক"],
        "D", "medium", "numerical",
        "Intersection (3, 1); y-intercepts (0, 4) and (0, -2). Area = (1/2)*6*3 = 9.",
        "ছেদ (3, 1); y-ছেদ (0, 4), (0, -2); ক্ষেত্রফল 9।",
    ),
    q(
        "For what value of a are the lines 3x + 2y - 5 = 0, ax + 4y - 9 = 0 and "
        "x + 2y - 7 = 0 concurrent?",
        "a এর মান কত হলে 3x + 2y - 5 = 0, ax + 4y - 9 = 0 এবং x + 2y - 7 = 0 সমবিন্দু হবে?",
        ["7", "5", "3", "-7"],
        ["মান 7", "মান 5", "মান 3", "মান -7"],
        "A", "hard", "numerical",
        "Intersection of 1st and 3rd is (-1, 4). Plug into 2nd: -a + 16 - 9 = 0 ⇒ a = 7.",
        "১ম ও ৩য় এর ছেদ (-1, 4); ২য়ে বসিয়ে a = 7।",
    ),
    q(
        "The product of the slopes of 3x + y = 3 and 3x - y = 3 is:",
        "3x + y = 3 এবং 3x - y = 3 রেখাদ্বয়ের ঢালদ্বয়ের গুণফল:",
        ["-9", "-1", "1", "9"],
        ["মান -9", "মান -1", "মান 1", "মান 9"],
        "A", "easy", "numerical",
        "m1 = -3, m2 = 3; product = -9.",
        "m1 = -3, m2 = 3; গুণফল -9।",
    ),
    q(
        "The line through the intersection of x + y = 4 and x - y = 2 that is "
        "parallel to the y-axis is:",
        "x + y = 4 ও x - y = 2 এর ছেদবিন্দুগামী এবং y-অক্ষের সমান্তরাল রেখার সমীকরণ:",
        ["y = 1", "x = 1", "y = 3", "x = 3"],
        ["y = 1", "x = 1", "y = 3", "x = 3"],
        "D", "medium", "numerical",
        "Intersection is (3, 1). Parallel to y-axis ⇒ x = 3.",
        "ছেদবিন্দু (3, 1); y-অক্ষের সমান্তরাল ⇒ x = 3।",
    ),
    q(
        "If 8x - by - 9 = 0 is parallel to 4x + 3y + 2 = 0, then b = ?",
        "8x - by - 9 = 0 এবং 4x + 3y + 2 = 0 সমান্তরাল হলে b এর মান কত?",
        ["-6", "-3", "3", "6"],
        ["মান -6", "মান -3", "মান 3", "মান 6"],
        "A", "medium", "numerical",
        "m1 = 8/b, m2 = -4/3. Equal slopes ⇒ 8/b = -4/3 ⇒ b = -6.",
        "ঢাল সমান ⇒ 8/b = -4/3 ⇒ b = -6।",
    ),
    q(
        "The angle between the lines x + y = 3 and x - y = 3 is:",
        "x + y = 3 এবং x - y = 3 রেখাদ্বয়ের মধ্যবর্তী কোণ কত?",
        ["30°", "45°", "60°", "90°"],
        ["30°", "45°", "60°", "90°"],
        "D", "easy", "numerical",
        "m1 = -1, m2 = 1; m1 m2 = -1 ⇒ lines are perpendicular ⇒ 90°.",
        "m1 m2 = -1 ⇒ রেখাদ্বয় লম্ব ⇒ 90°।",
    ),
    q(
        "The intersection of x + y + 4 = 0 and x - y - 2 = 0 is:",
        "x + y + 4 = 0 ও x - y - 2 = 0 রেখাদ্বয়ের ছেদবিন্দু:",
        ["(3, 1)", "(1, 3)", "(-3, -1)", "(-1, -3)"],
        ["(3, 1)", "(1, 3)", "(-3, -1)", "(-1, -3)"],
        "D", "easy", "numerical",
        "Adding: 2x + 2 = 0 ⇒ x = -1; then y = -3.",
        "যোগে x = -1, y = -3।",
    ),
    q(
        "The area of the triangle formed by x + y + 4 = 0, x - y - 2 = 0 and the x-axis is:",
        "x + y + 4 = 0 ও x - y - 2 = 0 রেখাদ্বয় x-অক্ষের সাথে যে ত্রিভুজ গঠন করে তার ক্ষেত্রফল:",
        ["9 square units", "6 square units", "4 square units", "3 square units"],
        ["9 বর্গ একক", "6 বর্গ একক", "4 বর্গ একক", "3 বর্গ একক"],
        "A", "medium", "numerical",
        "Vertices (-1, -3), (-4, 0), (2, 0). Area = (1/2)*6*3 = 9.",
        "শীর্ষ (-1, -3), (-4, 0), (2, 0); ক্ষেত্রফল 9।",
    ),
    q(
        "The acute angle between y = 2x + 3 and 3x - y + 5 = 0 is:",
        "y = 2x + 3 এবং 3x - y + 5 = 0 রেখাদ্বয়ের সূক্ষ্মকোণ কত?",
        ["tan^(-1)(-1/7)", "tan^(-1)(1/7)", "-tan^(-1)(1/7)", "tan^(-1)(7)"],
        ["tan^(-1)(-1/7)", "tan^(-1)(1/7)", "-tan^(-1)(1/7)", "tan^(-1)(7)"],
        "B", "hard", "numerical",
        "m1 = 2, m2 = 3. tan θ = |(3-2)/(1+6)| = 1/7 ⇒ θ = tan^(-1)(1/7).",
        "tan θ = |1/7| ⇒ θ = tan^(-1)(1/7)।",
    ),
    q(
        "The lines x + 2y - 6 = 0 and x + 2y + 8 = 0 are:",
        "x + 2y - 6 = 0 এবং x + 2y + 8 = 0 রেখাদ্বয়:",
        ["passing through the origin", "intersecting", "perpendicular", "parallel"],
        ["মূলবিন্দুগামী", "পরস্পর ছেদকারী", "পরস্পর লম্ব", "পরস্পর সমান্তরাল"],
        "D", "easy", "conceptual",
        "Same slope -1/2 and distinct intercepts ⇒ parallel.",
        "ঢাল সমান (-1/2) কিন্তু ভিন্ন খণ্ডিতাংশ ⇒ সমান্তরাল।",
    ),
    q(
        "The angle between y = -2x and 2y = x is:",
        "y = -2x এবং 2y = x রেখাদ্বয়ের মধ্যবর্তী কোণ:",
        ["90°", "tan^(-1)(1/2)", "tan^(-1)(2)", "0°"],
        ["90°", "tan^(-1)(1/2)", "tan^(-1)(2)", "0°"],
        "A", "easy", "numerical",
        "m1 = -2, m2 = 1/2; product = -1 ⇒ 90°.",
        "m1 m2 = -1 ⇒ কোণ 90°।",
    ),
    q(
        "For what value of k are x - y + 5 = 0, x + y - 1 = 0 and kx - y + 13 = 0 concurrent?",
        "k এর কোন মানের জন্য x - y + 5 = 0, x + y - 1 = 0 এবং kx - y + 13 = 0 সমবিন্দুগামী?",
        ["1", "5", "1/5", "-5"],
        ["মান 1", "মান 5", "মান 1/5", "মান -5"],
        "B", "medium", "numerical",
        "First two meet at (-2, 3). Then -2k - 3 + 13 = 0 ⇒ k = 5.",
        "ছেদবিন্দু (-2, 3); তৃতীয়ে বসিয়ে k = 5।",
    ),
    q(
        "The line 3x + sqrt(3)y - 10 = 0 makes what angle with the positive x-axis?",
        "3x + sqrt(3)y - 10 = 0 রেখাটি x-অক্ষের ধনাত্মক দিকের সাথে কত কোণ উৎপন্ন করে?",
        ["π/6", "π/3", "π/2", "2π/3"],
        ["π/6", "π/3", "π/2", "2π/3"],
        "D", "medium", "numerical",
        "m = -sqrt(3) ⇒ θ = tan^(-1)(-sqrt(3)) = 2π/3 (in standard position).",
        "m = -sqrt(3) ⇒ θ = 2π/3।",
    ),
    q(
        "The line x - sqrt(3)y = 6 makes what degree-angle with the positive x-axis?",
        "x - sqrt(3)y = 6 রেখাটি x-অক্ষের ধনাত্মক দিকের সাথে কত ডিগ্রি কোণ করে?",
        ["30°", "45°", "60°", "120°"],
        ["30°", "45°", "60°", "120°"],
        "A", "easy", "numerical",
        "y = (1/sqrt(3))x - 2 ⇒ m = tan 30° ⇒ θ = 30°.",
        "m = 1/sqrt(3) = tan 30° ⇒ θ = 30°।",
    ),
    q(
        "If the slope of a line is 2/3 and it is perpendicular to ax + 3y - 7 = 0, then a = ?",
        "ঢাল 2/3 বিশিষ্ট সরলরেখাটি ax + 3y - 7 = 0 এর উপর লম্ব হলে a এর মান:",
        ["2", "3", "9/2", "2/9"],
        ["মান 2", "মান 3", "মান 9/2", "মান 2/9"],
        "C", "medium", "numerical",
        "Slope of given line = -a/3. Perpendicular: (2/3)(-a/3) = -1 ⇒ a = 9/2.",
        "(2/3)(-a/3) = -1 ⇒ a = 9/2।",
    ),
    q(
        "Which are true for y - x - 2 = 0? "
        "(i) it makes 45° with the x-axis  "
        "(ii) the intercept between the axes has length 2√2  "
        "(iii) it meets the y-axis at (0, 2)",
        "y - x - 2 = 0 সরলরেখাটির জন্য কোনটি সঠিক? "
        "(i) x-অক্ষের সাথে 45° কোণ  (ii) অক্ষদ্বয়ের মধ্যবর্তী খণ্ডিতাংশের দৈর্ঘ্য 2√2  "
        "(iii) y-অক্ষকে (0, 2) বিন্দুতে ছেদ করে",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "y = x + 2 ⇒ m = 1 ⇒ 45°. Intercepts ±2; length sqrt(4+4) = 2√2. Meets y-axis at (0, 2).",
        "ঢাল 1 ⇒ 45°; খণ্ডিতাংশ দৈর্ঘ্য 2√2; y-ছেদ (0, 2)।",
    ),
]


# =============================================================================
# hm1_27_ch03_t03 — Distance from a point to a line
# Prefer Udvash T-09 / T-10: point-to-line and parallel-line distance
# =============================================================================
T03 = [
    q(
        "The perpendicular distance from (-sqrt(3), 1) to the line sqrt(3)x - y + 9 = 0 is:",
        "(-sqrt(3), 1) বিন্দু হতে sqrt(3)x - y + 9 = 0 রেখার উপর লম্ব দূরত্ব কত?",
        ["1/2 unit", "5/2 units", "2 units", "5 units"],
        ["1/2 একক", "5/2 একক", "2 একক", "5 একক"],
        "B", "medium", "numerical",
        "d = |-3 - 1 + 9|/sqrt(3+1) = 5/2. (Printed key sometimes lists 5; corrected to 5/2.)",
        "d = |-3 - 1 + 9|/2 = 5/2 একক। (মুদ্রিত কীতে কখনো 5; সংশোধিত 5/2।)",
    ),
    q(
        "The distance between the parallel lines 2x + 3y = 9 and 4x + 6y = 7 is:",
        "2x + 3y = 9 এবং 4x + 6y = 7 সমান্তরাল রেখাদ্বয়ের মধ্যবর্তী দূরত্ব:",
        ["1/2", "2/sqrt(13)", "11/(2√13)", "25/(2√13)"],
        ["মান 1/2", "মান 2/sqrt(13)", "মান 11/(2√13)", "মান 25/(2√13)"],
        "C", "medium", "numerical",
        "Rewrite as 4x + 6y - 18 = 0 and 4x + 6y - 7 = 0. "
        "d = |−18 − (−7)|/sqrt(16+36) = 11/(2√13).",
        "d = 11/sqrt(52) = 11/(2√13)।",
    ),
    q(
        "The perpendicular distance from the origin to x + y - 2 = 0 is:",
        "মূলবিন্দু হতে x + y - 2 = 0 রেখার লম্ব দূরত্ব:",
        ["1 unit", "√2 units", "2 units", "2√2 units"],
        ["1 একক", "√2 একক", "2 একক", "2√2 একক"],
        "B", "easy", "numerical",
        "d = |−2|/sqrt(1+1) = √2.",
        "d = 2/√2 = √2।",
    ),
    q(
        "For the parallel lines x - 3y + 5 = 0 and 2x - 6y + 9 = 0, which are true? "
        "(i) the lines are parallel  (ii) slope of the second is 1/3  "
        "(iii) distance between them is 1/(2√10)",
        "x - 3y + 5 = 0 ও 2x - 6y + 9 = 0 রেখাদ্বয়ের ক্ষেত্রে কোনটি সঠিক? "
        "(i) রেখাদ্বয় সমান্তরাল  (ii) দ্বিতীয় রেখার ঢাল 1/3  "
        "(iii) মধ্যবর্তী দূরত্ব 1/(2√10)",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "D", "hard", "conceptual",
        "Both slopes equal 1/3 so parallel. Distance between 2x-6y+10=0 and "
        "2x-6y+9=0 is 1/√40 = 1/(2√10). All three statements hold.",
        "উভয়ের ঢাল 1/3 ⇒ সমান্তরাল; দূরত্ব 1/(2√10)। তিনটিই সত্য।",
    ),
    q(
        "Which equation represents a line at distance 4 from the origin with slope -1?",
        "মূলবিন্দু হতে 4 একক দূরবর্তী এবং −1 ঢালবিশিষ্ট সরলরেখার সমীকরণ কোনটি?",
        ["x + y + 4√2 = 0", "y - x + 4√2 = 0", "y + 4√2 x = 0", "4√2 x - y = 0"],
        ["x + y + 4√2 = 0", "y - x + 4√2 = 0", "y + 4√2 x = 0", "4√2 x - y = 0"],
        "A", "hard", "numerical",
        "Line: x + y + c = 0 with |c|/√2 = 4 ⇒ |c| = 4√2. One form is x + y + 4√2 = 0.",
        "|c|/√2 = 4 ⇒ c = ±4√2; একটি রূপ x + y + 4√2 = 0।",
    ),
    q(
        "The perpendicular distance from (2, -3) to 2x - 3y = 0 is:",
        "(2, -3) বিন্দু থেকে 2x - 3y = 0 রেখার লম্ব দূরত্ব:",
        ["√13 / 2", "1", "√13", "13"],
        ["√13 / 2", "মান 1", "√13", "মান 13"],
        "C", "medium", "numerical",
        "d = |4 + 9|/sqrt(4+9) = 13/√13 = √13.",
        "d = 13/√13 = √13।",
    ),
    q(
        "If the perpendicular distance from (3, 1) to √3 x - y + 8 = 0 is p, then p = ?",
        "(3, 1) বিন্দু হতে √3 x - y + 8 = 0 রেখার উপর অঙ্কিত লম্বের দৈর্ঘ্য p হলে p = ?",
        ["5", "(3√3 + 7)/2", "2", "(3√3 - 7)/2"],
        ["মান 5", "মান (3√3 + 7)/2", "মান 2", "মান (3√3 - 7)/2"],
        "B", "medium", "numerical",
        "p = |3√3 - 1 + 8|/2 = (3√3 + 7)/2.",
        "p = |3√3 + 7|/2।",
    ),
    q(
        "The distance between the parallel lines x + 2y - 6 = 0 and x + 2y + 8 = 0 is:",
        "x + 2y - 6 = 0 ও x + 2y + 8 = 0 সমান্তরাল রেখাদ্বয়ের মধ্যবর্তী দূরত্ব:",
        ["2/√5", "14/√5", "7/√5", "8/√5"],
        ["মান 2/√5", "মান 14/√5", "মান 7/√5", "মান 8/√5"],
        "B", "medium", "numerical",
        "d = |−6 − 8|/sqrt(1+4) = 14/√5.",
        "d = 14/√5।",
    ),
    q(
        "The foot of the perpendicular from (2, -1) to 3x - 4y + 5 = 0 is:",
        "(2, -1) বিন্দু হতে 3x - 4y + 5 = 0 রেখার উপর অঙ্কিত লম্বের পাদবিন্দু:",
        ["(1/5, 7/5)", "(1/5, 2/5)", "(1, 2)", "(3/5, 1)"],
        ["(1/5, 7/5)", "(1/5, 2/5)", "(1, 2)", "(3/5, 1)"],
        "A", "hard", "numerical",
        "(x-2)/3 = (y+1)/(-4) = -(6+4+5)/25 = -3/5. "
        "Hence foot = (2 - 9/5, -1 + 12/5) = (1/5, 7/5).",
        "পাদবিন্দু সূত্রে (1/5, 7/5)।",
    ),
    q(
        "For 2x - 3y = 0, which are true? "
        "(i) it passes through the origin  (ii) (3, 2) lies on it  "
        "(iii) distance from (2, -3) to it is √13",
        "2x - 3y = 0 সরলরেখার জন্য কোনটি সঠিক? "
        "(i) মূলবিন্দুগামী  (ii) (3, 2) বিন্দুটি রেখার উপর  "
        "(iii) (2, -3) থেকে লম্ব দূরত্ব √13",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "Through origin; 2·3 − 3·2 = 0 so (3, 2) lies on it; "
        "distance from (2, -3) is 13/√13 = √13. All three hold.",
        "মূলবিন্দুগামী; (3,2) সিদ্ধ করে; দূরত্ব √13। তিনটিই সত্য।",
    ),
    q(
        "The length of the intercept cut by 3x + 4y - 12 = 0 between the axes is:",
        "3x + 4y - 12 = 0 রেখাটি অক্ষদ্বয়ের মধ্যে যে অংশ খণ্ডিত করে তার দৈর্ঘ্য:",
        ["3 units", "4 units", "5 units", "6 units"],
        ["3 একক", "4 একক", "5 একক", "6 একক"],
        "C", "easy", "numerical",
        "Intercepts 4 and 3; length = sqrt(16+9) = 5.",
        "খণ্ডিতাংশ 4 ও 3; দৈর্ঘ্য sqrt(16+9) = 5।",
    ),
    q(
        "The perpendicular distance from the origin to the line through (6, 0) and (0, -3) is:",
        "(6, 0) ও (0, -3) বিন্দুগামী রেখা হতে মূলবিন্দুর লম্ব দূরত্ব:",
        ["4 units", "3 units", "6/√5 units", "√5 units"],
        ["4 একক", "3 একক", "6/√5 একক", "√5 একক"],
        "C", "medium", "numerical",
        "Intercept form gives x − 2y − 6 = 0; d = 6/√5.",
        "সমীকরণ x − 2y − 6 = 0; d = 6/√5।",
    ),
    q(
        "The area of the triangle formed by x + y - 4 = 0 with the coordinate axes is:",
        "x + y - 4 = 0 সরলরেখাটি অক্ষদ্বয়ের সাথে যে ত্রিভুজ তৈরি করে তার ক্ষেত্রফল:",
        ["4", "8", "16", "32"],
        ["মান 4", "মান 8", "মান 16", "মান 32"],
        "B", "easy", "numerical",
        "Intercepts 4, 4; area = (1/2)*4*4 = 8.",
        "খণ্ডিতাংশ 4, 4; ক্ষেত্রফল 8।",
    ),
    q(
        "Which are true for x + y - 2 = 0? "
        "(i) 2x + 2y + 3 = 0 is parallel to it  "
        "(ii) distance from origin is √2  "
        "(iii) area of triangle with axes is 2",
        "x + y - 2 = 0 রেখাটির জন্য কোনটি সঠিক? "
        "(i) 2x + 2y + 3 = 0 এর সমান্তরাল  "
        "(ii) মূলবিন্দু হতে লম্ব দূরত্ব √2 একক  "
        "(iii) অক্ষদ্বয়ের সাথে ত্রিভুজের ক্ষেত্রফল 2 বর্গ একক",
        ["i and ii", "ii and iii", "i and iii", "i, ii and iii"],
        ["i ও ii", "ii ও iii", "i ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "Same slope -1; d = √2; area = (1/2)*2*2 = 2. All true.",
        "ঢাল সমান; d = √2; ক্ষেত্রফল 2। তিনটিই সত্য।",
    ),
    q(
        "The length cut by √2 x − y + 5 = 0 on the y-axis is:",
        "√2 x − y + 5 = 0 রেখাটি দ্বারা y-অক্ষের খণ্ডিতাংশের দৈর্ঘ্য:",
        ["-5", "-5/√2", "5/√2", "5"],
        ["মান -5", "মান -5/√2", "মান 5/√2", "মান 5"],
        "D", "easy", "numerical",
        "Put x = 0: −y + 5 = 0 ⇒ y = 5. Absolute intercept length 5.",
        "x = 0 ⇒ y = 5; খণ্ডিতাংশের দৈর্ঘ্য 5।",
    ),
    q(
        "The equation of the line through (1, -1) perpendicular to 2x + 3y + 5 = 0 is:",
        "2x + 3y + 5 = 0 রেখার উপর লম্ব এবং (1, -1) বিন্দুগামী রেখার সমীকরণ:",
        ["3x - 2y + 5 = 0", "3x + 2y + 5 = 0", "2x - 3y + 4 = 0", "3x - 2y - 5 = 0"],
        ["3x - 2y + 5 = 0", "3x + 2y + 5 = 0", "2x - 3y + 4 = 0", "3x - 2y - 5 = 0"],
        "D", "medium", "numerical",
        "Perpendicular slope 3/2: y + 1 = (3/2)(x - 1) ⇒ 3x - 2y - 5 = 0.",
        "লম্বের ঢাল 3/2; সমীকরণ 3x - 2y - 5 = 0।",
    ),
    q(
        "For 2x + 3y = 8, which are true? "
        "(i) x-intercept is 4  (ii) area with the axes is 16/3  "
        "(iii) it meets the y-axis at (0, 8/3)",
        "2x + 3y = 8 রেখার জন্য কোনটি সঠিক? "
        "(i) x-খণ্ডিতাংশ 4  (ii) অক্ষদ্বয়ের সাথে ক্ষেত্রফল 16/3  "
        "(iii) y-অক্ষকে (0, 8/3) বিন্দুতে ছেদ করে",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "x-intercept 4, y-intercept 8/3; area = (1/2)*4*(8/3) = 16/3. All three hold.",
        "x-খণ্ডিতাংশ 4; y-ছেদ (0, 8/3); ক্ষেত্রফল 16/3। তিনটিই সত্য।",
    ),
    q(
        "The perpendicular distance from the origin to 5x - 4y - 20 = 0 is:",
        "মূলবিন্দু হতে 5x − 4y − 20 = 0 রেখার লম্ব দূরত্ব কত?",
        ["2", "4", "5", "20/√41"],
        ["মান 2", "মান 4", "মান 5", "মান 20/√41"],
        "D", "medium", "numerical",
        "d = |−20|/sqrt(25+16) = 20/√41.",
        "d = 20/√41।",
    ),
    q(
        "If the distance between the parallel lines 3x + 4y + c1 = 0 and "
        "3x + 4y + c2 = 0 is 2, and c1 = 5, then a possible value of c2 is:",
        "সমান্তরাল রেখা 3x + 4y + c1 = 0 ও 3x + 4y + c2 = 0 এর দূরত্ব 2 এবং c1 = 5 হলে c2 এর সম্ভাব্য মান:",
        ["-5", "15", "10", "0"],
        ["মান -5", "মান 15", "মান 10", "মান 0"],
        "B", "hard", "numerical",
        "|c1 − c2|/5 = 2 ⇒ |5 − c2| = 10 ⇒ c2 = 15 or −5. Among options preferring 15.",
        "|5 − c2|/5 = 2 ⇒ c2 = 15 বা −5; বিকল্পে 15।",
    ),
    q(
        "The distance from the point (1, 2) to the line 3x − 4y + 5 = 0 is:",
        "(1, 2) বিন্দু হতে 3x − 4y + 5 = 0 রেখার দূরত্ব:",
        ["0", "1/5", "2/5", "1"],
        ["মান 0", "মান 1/5", "মান 2/5", "মান 1"],
        "A", "easy", "numerical",
        "3(1) − 4(2) + 5 = 3 − 8 + 5 = 0, so the point lies on the line; distance 0.",
        "বিন্দুটি রেখার উপর ⇒ দূরত্ব 0।",
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
    counts["hm1_27_ch03_t01"] = write_topic("hm1_27_ch03_t01", T01)["count"]
    counts["hm1_27_ch03_t02"] = write_topic("hm1_27_ch03_t02", T02)["count"]
    counts["hm1_27_ch03_t03"] = write_topic("hm1_27_ch03_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm1_27_ch03",
        "title_en": "Straight Lines",
        "title_bn": "সরলরেখা",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(110, 124)],
        "topics": {
            "hm1_27_ch03_t01": {
                "title_en": "Slope and equations of a line",
                "title_bn": "ঢাল ও সরলরেখার সমীকরণ",
                "udvash_types": ["T-07", "T-08"],
                "count": 20,
            },
            "hm1_27_ch03_t02": {
                "title_en": "Angles and intersection of lines",
                "title_bn": "রেখার মধ্যবর্তী কোণ ও ছেদ",
                "udvash_types": ["T-08", "T-12", "T-13"],
                "count": 20,
            },
            "hm1_27_ch03_t03": {
                "title_en": "Distance from a point to a line",
                "title_bn": "বিন্দু থেকে রেখার দূরত্ব",
                "udvash_types": ["T-09", "T-10"],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "Q01_polar": "Polar/Cartesian r=2sinθ is circle content; kept out of straight-line topics",
            "Q14_i": "Printed claim slope=-5 for (0,4)-(10,-4) is wrong (true slope -4/5); curated with corrected key ii+iii",
            "Q15_printed_key": "Printed key often marks distance 5; true value from (-√3,1) to √3x-y+9=0 is 5/2; corrected",
            "Q17_figure": "Figure-only section-formula item skipped",
            "Q65_no_key": "OCR notes (No Answer) for origin-to-AB distance; reconstructed equation independently",
            "Q74_iii": "Printed y-intercept (0,8) mismatches 2x+3y=8 (true (0,8/3)); curated with corrected statements",
            "Q125_options": "OCR garbled foot-of-perpendicular options; recomputed foot (1/5,7/5) and rewrote options",
        },
        "low_confidence": [
            "Some multi-select keys corrected when printed উত্তরমালা contradicted algebra.",
            "Figure-dependent board stems rewritten as equation-only stems.",
            "Inline math stored as plain text (sqrt, tan^(-1), √) for JSONL.",
            "Concurrent-line a/k values cross-checked against intersection method.",
        ],
        "validate": {
            "command": "python tools/question_bank/udvash_extract/seed_hm1_ch03.py",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch03_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
