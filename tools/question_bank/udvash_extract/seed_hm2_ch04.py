#!/usr/bin/env python3
"""Seed Higher Mathematics 2nd Paper Ch04 (Polynomials and Polynomial Equations).

Curated from Udvash HSC Question Bank 2026 printed pp. 100–112 (PDF 106–118).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
OCR is noisy (~13 pages); reconstructs board-style items from solutions/column
text and supplements with accurate HSC-level authored MCQs.
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
    "higher_mathematics p2 ch04; curated bilingual"
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
# hm2_27_ch04_t01 — Polynomial operations and factorization
# =============================================================================
T01 = [
    q(
        "Which of the following is a polynomial?",
        "নিচের কোনটি বহুপদী?",
        ["x³ − 2√x + 1", "√x + 4x − 1", "x² + 2x⁻¹ − 5", "2x² + 3x − 5"],
        ["x³ − 2√x + 1", "√x + 4x − 1", "x² + 2x⁻¹ − 5", "2x² + 3x − 5"],
        "D", "easy", "factual",
        "A polynomial may contain only non-negative integer powers of the variable; 2x² + 3x − 5 qualifies.",
        "বহুপদীতে চলকের শুধু অঋণাত্মক পূর্ণসংখ্যা ঘাত থাকতে পারে; 2x² + 3x − 5 একটি বহুপদী।",
    ),
    q(
        "Which of the following is not a polynomial expression?",
        "নিচের কোনটি বহুপদী রাশি নয়?",
        ["ax² + 2hxy + by²", "2x² + 3xy + y²", "x² + y² + 2gx + 2fy + c", "2√x + 4√y + 5"],
        ["ax² + 2hxy + by²", "2x² + 3xy + y²", "x² + y² + 2gx + 2fy + c", "2√x + 4√y + 5"],
        "D", "easy", "factual",
        "Square roots of variables are not non-negative integer powers, so 2√x + 4√y + 5 is not a polynomial.",
        "চলকের বর্গমূল অঋণাত্মক পূর্ণসংখ্যা ঘাত নয়; তাই 2√x + 4√y + 5 বহুপদী নয়।",
    ),
    q(
        "The condition that ax² + bx + c = 0 is a quadratic equation is:",
        "ax² + bx + c = 0 দ্বিঘাত সমীকরণ হওয়ার শর্ত কোনটি?",
        ["a = 0", "a ≠ 0", "b = 0", "b ≠ 0"],
        ["a = 0", "a ≠ 0", "b = 0", "b ≠ 0"],
        "B", "easy", "factual",
        "A quadratic equation requires the coefficient of x² to be non-zero, so a ≠ 0.",
        "দ্বিঘাত সমীকরণে x² এর সহগ শূন্য নয় হতে হয়; তাই a ≠ 0।",
    ),
    q(
        "If f(x) = x³ − 3x² − 2x, which statements are true? (i) f(x) = 0 has three roots counting multiplicity (ii) one root of f(x) = 0 is 0 (iii) x − 1 is a factor of f(x)",
        "f(x) = x³ − 3x² − 2x হলে— (i) f(x) = 0 এর মূল তিনটি (ii) একটি মূল 0 (iii) x − 1, f(x) এর উৎপাদক — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "A", "medium", "conceptual",
        "f(x) = x(x² − 3x − 2); one root is 0. f(1) = −4 ≠ 0, so x − 1 is not a factor.",
        "f(x) = x(x² − 3x − 2); একটি মূল 0। f(1) ≠ 0 বলে x − 1 উৎপাদক নয়।",
    ),
    q(
        "The degree of the product of a cubic polynomial and a quadratic polynomial is:",
        "একটি ত্রিঘাত বহুপদী ও একটি দ্বিঘাত বহুপদীর গুণফলের ঘাত কত?",
        ["2", "3", "5", "6"],
        ["2", "3", "5", "6"],
        "C", "easy", "factual",
        "deg(fg) = deg(f) + deg(g) = 3 + 2 = 5 for non-zero polynomials.",
        "অশূন্য বহুপদীর জন্য deg(fg) = 3 + 2 = 5।",
    ),
    q(
        "Factorization of x² − 5x + 6 is:",
        "x² − 5x + 6 এর উৎপাদকে বিশ্লেষণ কোনটি?",
        ["(x − 1)(x − 6)", "(x − 2)(x − 3)", "(x + 2)(x + 3)", "(x − 2)(x + 3)"],
        ["(x − 1)(x − 6)", "(x − 2)(x − 3)", "(x + 2)(x + 3)", "(x − 2)(x + 3)"],
        "B", "easy", "numerical",
        "x² − 5x + 6 = (x − 2)(x − 3).",
        "x² − 5x + 6 = (x − 2)(x − 3)।",
    ),
    q(
        "x³ − 1 factorizes as:",
        "x³ − 1 এর উৎপাদক বিশ্লেষণ কোনটি?",
        ["(x − 1)(x² + x + 1)", "(x + 1)(x² − x + 1)", "(x − 1)(x² − x + 1)", "(x − 1)³"],
        ["(x − 1)(x² + x + 1)", "(x + 1)(x² − x + 1)", "(x − 1)(x² − x + 1)", "(x − 1)³"],
        "A", "easy", "factual",
        "Difference of cubes: x³ − 1 = (x − 1)(x² + x + 1).",
        "ঘনমূলের ব্যবধান: x³ − 1 = (x − 1)(x² + x + 1)।",
    ),
    q(
        "Expanding (x + 2)(x − 2) gives:",
        "(x + 2)(x − 2) বিস্তার করলে কী পাওয়া যায়?",
        ["x² − 4", "x² + 4", "x² − 2x − 4", "x² + 4x − 4"],
        ["x² − 4", "x² + 4", "x² − 2x − 4", "x² + 4x − 4"],
        "A", "easy", "numerical",
        "Difference of squares: (x + 2)(x − 2) = x² − 4.",
        "বর্গের ব্যবধান: (x + 2)(x − 2) = x² − 4।",
    ),
    q(
        "The factorization of x² + 2x + 1 is:",
        "x² + 2x + 1 এর উৎপাদক কোনটি?",
        ["(x + 1)²", "(x − 1)²", "(x + 1)(x − 1)", "(x + 2)(x − 1)"],
        ["(x + 1)²", "(x − 1)²", "(x + 1)(x − 1)", "(x + 2)(x − 1)"],
        "A", "easy", "numerical",
        "x² + 2x + 1 = (x + 1)².",
        "x² + 2x + 1 = (x + 1)²।",
    ),
    q(
        "If p(x) = 2x³ − 5x + 1 and q(x) = x² + 3, then the degree of p(x) + q(x) is:",
        "p(x) = 2x³ − 5x + 1 এবং q(x) = x² + 3 হলে p(x) + q(x) এর ঘাত কত?",
        ["1", "2", "3", "5"],
        ["1", "2", "3", "5"],
        "C", "easy", "numerical",
        "The leading term of the sum is 2x³, so the degree is 3.",
        "যোগফলের প্রধান পদ 2x³; ঘাত 3।",
    ),
    q(
        "The leading coefficient of 7 − 3x + 5x⁴ − x² is:",
        "7 − 3x + 5x⁴ − x² এর প্রধান সহগ কত?",
        ["7", "−3", "5", "−1"],
        ["7", "−3", "5", "−1"],
        "C", "easy", "factual",
        "The highest-degree term is 5x⁴, so the leading coefficient is 5.",
        "সর্বোচ্চ ঘাতের পদ 5x⁴; প্রধান সহগ 5।",
    ),
    q(
        "Using a³ + b³ = (a + b)(a² − ab + b²), the factorization of 8x³ + 27 is:",
        "a³ + b³ সূত্র ব্যবহার করে 8x³ + 27 এর উৎপাদক কোনটি?",
        ["(2x + 3)(4x² − 6x + 9)", "(2x − 3)(4x² + 6x + 9)", "(2x + 3)(4x² + 6x + 9)", "(2x + 3)²(2x − 3)"],
        ["(2x + 3)(4x² − 6x + 9)", "(2x − 3)(4x² + 6x + 9)", "(2x + 3)(4x² + 6x + 9)", "(2x + 3)²(2x − 3)"],
        "A", "medium", "numerical",
        "8x³ + 27 = (2x)³ + 3³ = (2x + 3)(4x² − 6x + 9).",
        "8x³ + 27 = (2x + 3)(4x² − 6x + 9)।",
    ),
    q(
        "A non-zero constant polynomial has degree:",
        "একটি অশূন্য ধ্রুবক বহুপদীর ঘাত কত?",
        ["0", "1", "undefined", "infinity"],
        ["0", "1", "অসংজ্ঞাত", "অসীম"],
        "A", "easy", "factual",
        "By definition a non-zero constant polynomial has degree 0.",
        "সংজ্ঞা অনুসারে অশূন্য ধ্রুবক বহুপদীর ঘাত 0।",
    ),
    q(
        "Expanding (x + 1)³ gives:",
        "(x + 1)³ বিস্তার করলে কী পাওয়া যায়?",
        ["x³ + 1", "x³ + 3x + 1", "x³ + 3x² + 3x + 1", "x³ + 3x² + 1"],
        ["x³ + 1", "x³ + 3x + 1", "x³ + 3x² + 3x + 1", "x³ + 3x² + 1"],
        "C", "easy", "numerical",
        "(x + 1)³ = x³ + 3x² + 3x + 1.",
        "(x + 1)³ = x³ + 3x² + 3x + 1।",
    ),
    q(
        "If f(x) = x² − 4 and g(x) = x − 2, then f(x)/g(x) simplifies (for x ≠ 2) to:",
        "f(x) = x² − 4 এবং g(x) = x − 2 হলে (x ≠ 2 এর জন্য) f(x)/g(x) সরলীকৃত রূপ কোনটি?",
        ["x + 2", "x − 2", "x² − 2", "x + 4"],
        ["x + 2", "x − 2", "x² − 2", "x + 4"],
        "A", "easy", "numerical",
        "x² − 4 = (x − 2)(x + 2), so the quotient is x + 2.",
        "x² − 4 = (x − 2)(x + 2); ভাগফল x + 2।",
    ),
    q(
        "The number of terms in the polynomial 3x⁴ − 2x² + x − 7 is:",
        "3x⁴ − 2x² + x − 7 বহুপদীতে কয়টি পদ আছে?",
        ["3", "4", "5", "7"],
        ["3", "4", "5", "7"],
        "B", "easy", "factual",
        "The four terms are 3x⁴, −2x², x and −7.",
        "পদগুলো: 3x⁴, −2x², x ও −7 — মোট 4টি।",
    ),
    q(
        "If one factor of x² − 7x + 12 is (x − 3), the other factor is:",
        "x² − 7x + 12 এর একটি উৎপাদক (x − 3) হলে অপর উৎপাদক কোনটি?",
        ["x − 4", "x + 4", "x − 3", "x − 12"],
        ["x − 4", "x + 4", "x − 3", "x − 12"],
        "A", "easy", "numerical",
        "x² − 7x + 12 = (x − 3)(x − 4).",
        "x² − 7x + 12 = (x − 3)(x − 4)।",
    ),
    q(
        "The homogeneous polynomial among the following is:",
        "নিচের কোনটি সমমাত্রিক বহুপদী?",
        ["x² + 2xy + y²", "x² + 2x + 1", "x³ + x² + x", "xy + x + y"],
        ["x² + 2xy + y²", "x² + 2x + 1", "x³ + x² + x", "xy + x + y"],
        "A", "medium", "conceptual",
        "Every term of x² + 2xy + y² has total degree 2.",
        "x² + 2xy + y² এর প্রতিটি পদের মোট ঘাত 2; তাই সমমাত্রিক।",
    ),
    q(
        "If p(x) = x² + 3x + 2 and q(x) = x + 1, then p(x) − (x + 2)q(x) equals:",
        "p(x) = x² + 3x + 2 এবং q(x) = x + 1 হলে p(x) − (x + 2)q(x) এর মান কত?",
        ["0", "1", "x", "x + 2"],
        ["0", "1", "x", "x + 2"],
        "A", "medium", "numerical",
        "(x + 2)(x + 1) = x² + 3x + 2 = p(x), so the difference is 0.",
        "(x + 2)(x + 1) = p(x); পার্থক্য 0।",
    ),
    q(
        "Factorization of x³ + 6x² + 11x + 6 is:",
        "x³ + 6x² + 11x + 6 এর উৎপাদক বিশ্লেষণ কোনটি?",
        ["(x + 1)(x + 2)(x + 3)", "(x − 1)(x − 2)(x − 3)", "(x + 1)(x + 2)(x − 3)", "(x + 1)²(x + 4)"],
        ["(x + 1)(x + 2)(x + 3)", "(x − 1)(x − 2)(x − 3)", "(x + 1)(x + 2)(x − 3)", "(x + 1)²(x + 4)"],
        "A", "medium", "numerical",
        "Possible rational roots −1, −2, −3 all work: (x + 1)(x + 2)(x + 3).",
        "মূল −1, −2, −3; উৎপাদক (x + 1)(x + 2)(x + 3)।",
    ),
]


# =============================================================================
# hm2_27_ch04_t02 — Remainder and factor theorems
# =============================================================================
T02 = [
    q(
        "By the remainder theorem, the remainder when a polynomial f(x) is divided by (x − a) is:",
        "ভাগশেষ উপপাদ্য অনুসারে, বহুপদী f(x) কে (x − a) দ্বারা ভাগ করলে ভাগশেষ কত?",
        ["f(0)", "f(a)", "f(−a)", "f′(a)"],
        ["f(0)", "f(a)", "f(−a)", "f′(a)"],
        "B", "easy", "factual",
        "The remainder theorem states that the remainder is f(a).",
        "ভাগশেষ উপপাদ্য অনুসারে ভাগশেষ f(a)।",
    ),
    q(
        "When 4x³ + 2x² + 3x − 6 is divided by (x − 1), the remainder is:",
        "4x³ + 2x² + 3x − 6 কে (x − 1) দ্বারা ভাগ করলে ভাগশেষ কত?",
        ["0", "1", "3", "−11"],
        ["0", "1", "3", "−11"],
        "C", "medium", "numerical",
        "f(1) = 4 + 2 + 3 − 6 = 3.",
        "f(1) = 4 + 2 + 3 − 6 = 3।",
    ),
    q(
        "By the factor theorem, (x − a) is a factor of f(x) if and only if:",
        "উৎপাদক উপপাদ্য অনুসারে, (x − a) বহুপদী f(x) এর উৎপাদক হবে যদি এবং কেবল যদি—",
        ["f(a) = 0", "f(a) ≠ 0", "f(0) = a", "f′(a) = 0"],
        ["f(a) = 0", "f(a) ≠ 0", "f(0) = a", "f′(a) = 0"],
        "A", "easy", "factual",
        "Factor theorem: (x − a) divides f(x) if and only if f(a) = 0.",
        "উৎপাদক উপপাদ্য: (x − a) | f(x) ⇔ f(a) = 0।",
    ),
    q(
        "The value of k for which (x + 3) is a factor of x² + 7x + 3 + k is:",
        "k এর মান কত হলে x² + 7x + 3 + k এর একটি উৎপাদক x + 3 হবে?",
        ["−33", "−9", "9", "33"],
        ["−33", "−9", "9", "33"],
        "C", "medium", "numerical",
        "f(−3) = 0 ⇒ 9 − 21 + 3 + k = 0 ⇒ k = 9.",
        "f(−3) = 0 ⇒ 9 − 21 + 3 + k = 0 ⇒ k = 9।",
    ),
    q(
        "If one root of x² − 3x + 2 + k = 0 is 3, then k equals:",
        "x² − 3x + 2 + k = 0 সমীকরণের একটি মূল 3 হলে k এর মান কত?",
        ["−3", "−2", "1", "2"],
        ["−3", "−2", "1", "2"],
        "B", "easy", "numerical",
        "Substitute x = 3: 9 − 9 + 2 + k = 0 ⇒ k = −2.",
        "x = 3 বসিয়ে: 9 − 9 + 2 + k = 0 ⇒ k = −2।",
    ),
    q(
        "If (x − 3) is a factor of x² + 2x + ℓ, then ℓ equals:",
        "x² + 2x + ℓ এর একটি উৎপাদক x − 3 হলে ℓ এর মান কত?",
        ["−15", "−3", "3", "15"],
        ["−15", "−3", "3", "15"],
        "A", "medium", "numerical",
        "f(3) = 0 ⇒ 9 + 6 + ℓ = 0 ⇒ ℓ = −15.",
        "f(3) = 0 ⇒ 9 + 6 + ℓ = 0 ⇒ ℓ = −15।",
    ),
    q(
        "If −4 is a root of x² + 9x + P = 0, then P equals:",
        "x² + 9x + P = 0 সমীকরণের একটি মূল −4 হলে P এর মান কত?",
        ["−52", "−20", "20", "52"],
        ["−52", "−20", "20", "52"],
        "C", "easy", "numerical",
        "(−4)² + 9(−4) + P = 0 ⇒ P = 20.",
        "(−4)² + 9(−4) + P = 0 ⇒ P = 20।",
    ),
    q(
        "The remainder when x³ − 2x + 5 is divided by (x − 2) is:",
        "x³ − 2x + 5 কে (x − 2) দ্বারা ভাগ করলে ভাগশেষ কত?",
        ["5", "7", "9", "13"],
        ["5", "7", "9", "13"],
        "C", "easy", "numerical",
        "f(2) = 8 − 4 + 5 = 9.",
        "f(2) = 8 − 4 + 5 = 9।",
    ),
    q(
        "If f(x) = x³ − 6x² + 11x − 6, then which of the following is a factor of f(x)?",
        "f(x) = x³ − 6x² + 11x − 6 হলে নিচের কোনটি f(x) এর উৎপাদক?",
        ["x − 4", "x − 1", "x + 1", "x + 2"],
        ["x − 4", "x − 1", "x + 1", "x + 2"],
        "B", "medium", "numerical",
        "f(1) = 1 − 6 + 11 − 6 = 0, so (x − 1) is a factor.",
        "f(1) = 0; তাই (x − 1) একটি উৎপাদক।",
    ),
    q(
        "When x³ + 1 is divided by (x + 1), the remainder is:",
        "x³ + 1 কে (x + 1) দ্বারা ভাগ করলে ভাগশেষ কত?",
        ["−2", "−1", "0", "2"],
        ["−2", "−1", "0", "2"],
        "C", "easy", "numerical",
        "f(−1) = −1 + 1 = 0.",
        "f(−1) = 0; ভাগশেষ 0।",
    ),
    q(
        "If px² + qx + r = 0 has a root equal to zero, then:",
        "px² + qx + r = 0 সমীকরণের একটি মূল শূন্য হলে কোনটি সত্য?",
        ["p = 0", "q = 0", "r = 0", "p = q"],
        ["p = 0", "q = 0", "r = 0", "p = q"],
        "C", "easy", "conceptual",
        "Substituting x = 0 gives r = 0.",
        "x = 0 বসিয়ে r = 0 পাওয়া যায়।",
    ),
    q(
        "If one root of x³ − 5x² + 11x − 7 = 0 is 2 + i√3, then its real root is:",
        "x³ − 5x² + 11x − 7 = 0 সমীকরণের একটি মূল 2 + i√3 হলে এর বাস্তব মূল কত?",
        ["−15", "−9", "−1", "1"],
        ["−15", "−9", "−1", "1"],
        "D", "hard", "numerical",
        "Conjugate 2 − i√3 is also a root; sum of roots = 5 ⇒ real root = 1.",
        "অনুবন্ধী মূলসহ সমষ্টি 5; বাস্তব মূল = 1।",
    ),
    q(
        "The remainder when f(x) = 2x³ − x² + 3x − 5 is divided by (x + 2) is:",
        "f(x) = 2x³ − x² + 3x − 5 কে (x + 2) দ্বারা ভাগ করলে ভাগশেষ কত?",
        ["−31", "−19", "−7", "5"],
        ["−31", "−19", "−7", "5"],
        "A", "medium", "numerical",
        "f(−2) = −16 − 4 − 6 − 5 = −31.",
        "f(−2) = −16 − 4 − 6 − 5 = −31।",
    ),
    q(
        "If (x − 2) is a factor of x³ − kx² + 2x − 4, then k equals:",
        "x³ − kx² + 2x − 4 এর উৎপাদক (x − 2) হলে k এর মান কত?",
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        "B", "medium", "numerical",
        "f(2) = 8 − 4k + 4 − 4 = 0 ⇒ k = 2.",
        "f(2) = 0 ⇒ k = 2।",
    ),
    q(
        "If −4 is a root of x² − 7x + p = 0, then p equals:",
        "x² − 7x + p = 0 সমীকরণের একটি মূল −4 হলে p এর মান কত?",
        ["−66", "−44", "44", "60"],
        ["−66", "−44", "44", "60"],
        "B", "medium", "numerical",
        "16 + 28 + p = 0 ⇒ p = −44.",
        "16 + 28 + p = 0 ⇒ p = −44।",
    ),
    q(
        "If x³ + 5x² − 49x − 245 = 0 has two roots whose sum is zero, the third root is:",
        "x³ + 5x² − 49x − 245 = 0 সমীকরণের দুইটি মূলের যোগফল শূন্য হলে তৃতীয় মূল কত?",
        ["5", "3", "2", "−5"],
        ["5", "3", "2", "−5"],
        "D", "hard", "numerical",
        "Sum of roots = −5; if α + (−α) + β = −5 then β = −5.",
        "মূলত্রয়ের সমষ্টি −5; α + (−α) + β = −5 ⇒ β = −5।",
    ),
    q(
        "If f(a) = f(b) = 0 with a ≠ b, then which statement is true?",
        "a ≠ b এবং f(a) = f(b) = 0 হলে কোনটি সত্য?",
        ["(x − a)(x − b) divides f(x)", "only (x − a) divides f(x)", "f has no linear factors", "remainder on dividing by (x − a) is b"],
        ["(x − a)(x − b) দ্বারা f(x) নিঃশেষে বিভাজ্য", "শুধু (x − a) দ্বারা বিভাজ্য", "f এর কোনো রৈখিক উৎপাদক নেই", "(x − a) দ্বারা ভাগশেষ b"],
        "A", "medium", "conceptual",
        "By the factor theorem both (x − a) and (x − b) are factors, so their product divides f(x).",
        "উৎপাদক উপপাদ্যে (x − a) ও (x − b) উভয়ই উৎপাদক।",
    ),
    q(
        "The remainder when xⁿ − 1 (n a positive integer) is divided by (x − 1) is:",
        "ধনাত্মক পূর্ণসংখ্যা n এর জন্য xⁿ − 1 কে (x − 1) দ্বারা ভাগ করলে ভাগশেষ কত?",
        ["0", "1", "n", "−1"],
        ["0", "1", "n", "−1"],
        "A", "easy", "numerical",
        "f(1) = 1ⁿ − 1 = 0.",
        "f(1) = 0; ভাগশেষ 0।",
    ),
    q(
        "If one root of x³ − 3x² − 16x + 48 = 0 is opposite in sign to another and their sum is zero, the third root is:",
        "x³ − 3x² − 16x + 48 = 0 সমীকরণের দুইটি মূলের যোগফল শূন্য হলে তৃতীয় মূল কোনটি?",
        ["−4", "−3", "3", "4"],
        ["−4", "−3", "3", "4"],
        "C", "hard", "numerical",
        "Sum of roots = 3; if α + (−α) + γ = 3 then γ = 3.",
        "মূলত্রয়ের সমষ্টি 3; α − α + γ = 3 ⇒ γ = 3।",
    ),
    q(
        "If f(x) = x³ − 3x + 10, then the sum of roots of f(x) = 0 equals:",
        "f(x) = x³ − 3x + 10 = 0 এর মূলগুলোর সমষ্টি কত?",
        ["7", "3", "0", "−3"],
        ["7", "3", "0", "−3"],
        "C", "easy", "numerical",
        "For x³ + 0·x² − 3x + 10 = 0, sum of roots = 0.",
        "x² এর সহগ 0; মূলগুলোর সমষ্টি 0।",
    ),
]


# =============================================================================
# hm2_27_ch04_t03 — Roots of polynomial equations
# =============================================================================
T03 = [
    q(
        "If one root of 4x² − 5x + c = 0 is 1, then the other root is:",
        "4x² − 5x + c = 0 সমীকরণের একটি মূল 1 হলে অপর মূলটি কত?",
        ["5/4", "−5/4", "1/4", "−1/4"],
        ["5/4", "−5/4", "1/4", "−1/4"],
        "C", "medium", "numerical",
        "Sum of roots = 5/4; other root = 5/4 − 1 = 1/4.",
        "মূলদ্বয়ের সমষ্টি 5/4; অপর মূল = 1/4।",
    ),
    q(
        "If the roots of 3x² + 2x + 1 = 0 are α and β, then 1/α + 1/β equals:",
        "3x² + 2x + 1 = 0 সমীকরণের মূলদ্বয় α ও β হলে 1/α + 1/β এর মান কত?",
        ["2", "−2", "1", "−3"],
        ["2", "−2", "1", "−3"],
        "B", "medium", "numerical",
        "1/α + 1/β = (α + β)/(αβ) = (−2/3)/(1/3) = −2.",
        "(α + β)/(αβ) = (−2/3)/(1/3) = −2।",
    ),
    q(
        "If one root of x² + ax + b = 0 is 1 + i, then (a, b) equals:",
        "x² + ax + b = 0 সমীকরণের একটি মূল 1 + i হলে a ও b এর মান কত?",
        ["a = −2, b = 2", "a = 2, b = −2", "a = −1, b = 1", "a = 1, b = −1"],
        ["a = −2, b = 2", "a = 2, b = −2", "a = −1, b = 1", "a = 1, b = −1"],
        "A", "medium", "numerical",
        "Other root is 1 − i; a = −(sum) = −2 and b = product = 2.",
        "অপর মূল 1 − i; a = −2, b = 2।",
    ),
    q(
        "For which values of k are the roots of 4x² − 2x + k = 0 complex?",
        "k এর মান কত হলে 4x² − 2x + k = 0 সমীকরণের মূলদ্বয় জটিল হবে?",
        ["k > 1/4", "k ≥ 1/4", "k < 1/4", "k ≤ 1/4"],
        ["k > 1/4", "k ≥ 1/4", "k < 1/4", "k ≤ 1/4"],
        "A", "medium", "numerical",
        "D < 0 ⇒ 4 − 16k < 0 ⇒ k > 1/4.",
        "D < 0 ⇒ 4 − 16k < 0 ⇒ k > 1/4।",
    ),
    q(
        "If α and β are roots of x² − 4x + 1 = 0, then (α + β)² equals:",
        "x² − 4x + 1 = 0 সমীকরণের মূলদ্বয় α, β হলে (α + β)² এর মান কত?",
        ["−16", "−4", "4", "16"],
        ["−16", "−4", "4", "16"],
        "D", "easy", "numerical",
        "α + β = 4, so (α + β)² = 16.",
        "α + β = 4; (α + β)² = 16।",
    ),
    q(
        "If p = 0 in 4x² + px − 1 = 0, the roots are: (i) real and rational (ii) irrational (iii) equal in magnitude but opposite in sign",
        "4x² + px − 1 = 0 এ p = 0 হলে মূলদ্বয়— (i) বাস্তব ও মূলদ (ii) অমূলদ (iii) সমান মানের কিন্তু বিপরীত চিহ্নবিশিষ্ট — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "B", "medium", "conceptual",
        "4x² − 1 = 0 ⇒ x = ±1/2; roots are real, rational, and opposite in sign.",
        "4x² − 1 = 0 ⇒ x = ±1/2; বাস্তব, মূলদ ও বিপরীত চিহ্ন।",
    ),
    q(
        "The discriminant of x² − 4x + k² = 0 when k = 0 is:",
        "k = 0 হলে x² − 4x + k² = 0 সমীকরণের নিশ্চায়ক কত?",
        ["−16", "−4", "4", "16"],
        ["−16", "−4", "4", "16"],
        "D", "easy", "numerical",
        "D = 16 − 4·1·0 = 16.",
        "D = 16 − 0 = 16।",
    ),
    q(
        "If k = 2 in x² − 4x + k² = 0, then α − β equals:",
        "k = 2 হলে x² − 4x + k² = 0 এর মূলদ্বয়ের বিয়োগফল α − β কত?",
        ["0", "2", "4", "16"],
        ["0", "2", "4", "16"],
        "A", "medium", "numerical",
        "Equation becomes (x − 2)² = 0; equal roots ⇒ α − β = 0.",
        "(x − 2)² = 0; সমমূল ⇒ α − β = 0।",
    ),
    q(
        "A quadratic equation having a root −1 + i√3 is:",
        "একটি মূল −1 + i√3 হলে দ্বিঘাত সমীকরণ কোনটি?",
        ["x² + 4x + 4 = 0", "x² − 2x − 4 = 0", "x² − 2x + 4 = 0", "x² + 2x + 4 = 0"],
        ["x² + 4x + 4 = 0", "x² − 2x − 4 = 0", "x² − 2x + 4 = 0", "x² + 2x + 4 = 0"],
        "D", "medium", "numerical",
        "Other root −1 − i√3; sum = −2, product = 4 ⇒ x² + 2x + 4 = 0.",
        "অপর মূল −1 − i√3; সমীকরণ x² + 2x + 4 = 0।",
    ),
    q(
        "If α and β are roots of x² + x − 1 = 0, then α² + β² equals:",
        "x² + x − 1 = 0 সমীকরণের মূলদ্বয় α ও β হলে α² + β² এর মান কত?",
        ["3", "1", "0", "−1"],
        ["3", "1", "0", "−1"],
        "A", "medium", "numerical",
        "α² + β² = (α + β)² − 2αβ = (−1)² − 2(−1) = 3.",
        "(α + β)² − 2αβ = 1 + 2 = 3।",
    ),
    q(
        "The nature of the roots of 2x² + 3x − 2 = 0 is:",
        "2x² + 3x − 2 = 0 এর মূলগুলোর প্রকৃতি কীরূপ?",
        ["real, equal, rational", "real, unequal, rational", "real, equal, irrational", "complex, unequal, irrational"],
        ["বাস্তব, সমান, মূলদ", "বাস্তব, অসমান, মূলদ", "বাস্তব, সমান, অমূলদ", "জটিল, অসমান, অমূলদ"],
        "B", "medium", "conceptual",
        "D = 9 + 16 = 25, a perfect square; roots real, unequal and rational.",
        "D = 25 পূর্ণবর্গ; মূলদ্বয় বাস্তব, অসমান ও মূলদ।",
    ),
    q(
        "For x² − px + p + 3 = 0 to have real and unequal roots, p must satisfy:",
        "x² − px + p + 3 = 0 এর মূলদ্বয় বাস্তব ও অসমান হলে p এর মান কোনটি?",
        ["p = −2 or 6", "p ≥ −2", "−2 < p < 6", "p < −2 or p > 6"],
        ["p = −2 বা 6", "p ≥ −2", "−2 < p < 6", "p < −2 অথবা p > 6"],
        "D", "hard", "numerical",
        "D = p² − 4p − 12 > 0 ⇒ (p − 6)(p + 2) > 0 ⇒ p < −2 or p > 6.",
        "D > 0 ⇒ p < −2 অথবা p > 6।",
    ),
    q(
        "The equation whose roots are each 2 less than the roots of x² − 5x − 1 = 0 is:",
        "x² − 5x − 1 = 0 এর মূলদ্বয় হতে 2 কম মূলবিশিষ্ট সমীকরণ কোনটি?",
        ["x² + x + 7 = 0", "x² − x + 7 = 0", "x² + x − 7 = 0", "x² − x − 7 = 0"],
        ["x² + x + 7 = 0", "x² − x + 7 = 0", "x² + x − 7 = 0", "x² − x − 7 = 0"],
        "D", "hard", "application",
        "Replace x by (x + 2): (x + 2)² − 5(x + 2) − 1 = 0 ⇒ x² − x − 7 = 0.",
        "x এর স্থলে (x + 2) বসিয়ে x² − x − 7 = 0।",
    ),
    q(
        "If α, β, γ are roots of x³ + 7x + 2 = 0, which statements are true? (i) α + β + γ = 0 (ii) αβ + βγ + γα = 7 (iii) αβγ = −2",
        "x³ + 7x + 2 = 0 এর মূলত্রয় α, β, γ হলে— (i) α + β + γ = 0 (ii) αβ + βγ + γα = 7 (iii) αβγ = −2 — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "For x³ + 0·x² + 7x + 2 = 0: sum = 0, sum of products = 7, product = −2.",
        "সমষ্টি 0, দুই দুই করে গুণফলের সমষ্টি 7, গুণফল −2।",
    ),
    q(
        "If the roots of (k − 2)x² + 2kx − 1 = 0 are complex, then k lies in:",
        "(k − 2)x² + 2kx − 1 = 0 এর মূলগুলো জটিল হলে k এর মান—",
        ["−2 < k < 1", "−2 ≤ k ≤ 1", "k < −2 or k > 1", "k ≤ −2 or k ≥ 1"],
        ["−2 < k < 1", "−2 ≤ k ≤ 1", "k < −2 অথবা k > 1", "k ≤ −2 অথবা k ≥ 1"],
        "A", "hard", "numerical",
        "D < 0 ⇒ 4k² + 4(k − 2) < 0 ⇒ (k + 2)(k − 1) < 0 ⇒ −2 < k < 1.",
        "D < 0 ⇒ −2 < k < 1।",
    ),
    q(
        "If α and β are roots of x² − 5x + 9 = 0, the equation with roots α + β and αβ is:",
        "x² − 5x + 9 = 0 এর মূলদ্বয় α, β হলে α + β ও αβ মূলবিশিষ্ট সমীকরণ কোনটি?",
        ["x² − 14x + 45 = 0", "x² + 14x + 45 = 0", "x² − 4x + 45 = 0", "x² + 4x − 45 = 0"],
        ["x² − 14x + 45 = 0", "x² + 14x + 45 = 0", "x² − 4x + 45 = 0", "x² + 4x − 45 = 0"],
        "A", "hard", "application",
        "α + β = 5, αβ = 9; new sum = 14, new product = 45 ⇒ x² − 14x + 45 = 0.",
        "নতুন সমষ্টি 14, গুণফল 45; সমীকরণ x² − 14x + 45 = 0।",
    ),
    q(
        "If α and β are roots of x² + 4x + 5 = 0, the equation with roots α + 2 and β + 2 is:",
        "x² + 4x + 5 = 0 এর মূলদ্বয় α, β হলে α + 2 ও β + 2 মূলবিশিষ্ট সমীকরণ কোনটি?",
        ["x² − 1 = 0", "x² − 8x + 1 = 0", "x² + 1 = 0", "x² + 8x + 1 = 0"],
        ["x² − 1 = 0", "x² − 8x + 1 = 0", "x² + 1 = 0", "x² + 8x + 1 = 0"],
        "C", "hard", "application",
        "New sum = α + β + 4 = 0; new product = αβ + 2(α + β) + 4 = 1 ⇒ x² + 1 = 0.",
        "নতুন সমষ্টি 0, গুণফল 1; সমীকরণ x² + 1 = 0।",
    ),
    q(
        "If consecutive integer roots of x² − 7x + c = 0 are required, then c equals:",
        "x² − 7x + c = 0 এর মূলদ্বয় পরপর পূর্ণসংখ্যা হলে c এর মান কত?",
        ["3", "4", "7", "12"],
        ["3", "4", "7", "12"],
        "D", "medium", "numerical",
        "Roots 3 and 4: sum 7, product 12 ⇒ c = 12.",
        "মূল 3 ও 4; গুণফল c = 12।",
    ),
    q(
        "For 3x² + 2x + 1 = 0: (i) roots real and equal (ii) sum of roots = −2/3 (iii) product of roots = 1/3",
        "3x² + 2x + 1 = 0 এর ক্ষেত্রে— (i) মূলদ্বয় বাস্তব ও সমান (ii) মূলদ্বয়ের যোগফল −2/3 (iii) মূলদ্বয়ের গুণফল 1/3 — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "C", "medium", "conceptual",
        "D = 4 − 12 = −8 < 0 so roots are complex; (ii) and (iii) hold.",
        "D < 0 বলে (i) মিথ্যা; (ii) ও (iii) সত্য।",
    ),
    q(
        "If α, β, γ are roots of x³ − 3x² − 25x + 75 = 0 and one root is the negative of another, the roots are:",
        "x³ − 3x² − 25x + 75 = 0 এর একটি মূল অপরটির বিপরীত চিহ্নবিশিষ্ট হলে মূলত্রয় কোনটি?",
        ["3, 5, −6", "6, −3, 3", "3, 5, −5", "5, 2, −7"],
        ["3, 5, −6", "6, −3, 3", "3, 5, −5", "5, 2, −7"],
        "C", "hard", "application",
        "Sum = 3 and α = −β ⇒ γ = 3; product (−β)·β·3 = −75 ⇒ β² = 25 ⇒ roots 3, 5, −5.",
        "সমষ্টি 3 ও α = −β ⇒ γ = 3; মূলত্রয় 3, 5, −5।",
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
    counts["hm2_27_ch04_t01"] = write_topic("hm2_27_ch04_t01", T01)["count"]
    counts["hm2_27_ch04_t02"] = write_topic("hm2_27_ch04_t02", T02)["count"]
    counts["hm2_27_ch04_t03"] = write_topic("hm2_27_ch04_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm2_27_ch04",
        "title_en": "Polynomials and Polynomial Equations",
        "title_bn": "বহুপদী ও বহুপদী সমীকরণ",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(100, 113)],
        "topics": {
            "hm2_27_ch04_t01": {
                "title_en": "Polynomial operations and factorization",
                "title_bn": "বহুপদীর ক্রিয়া ও উৎপাদক",
                "udvash_types": [
                    "definition and degree of polynomials",
                    "addition, multiplication and division of polynomials",
                    "factorization identities and linear factors",
                    "homogeneous and constant polynomials",
                ],
                "count": 20,
            },
            "hm2_27_ch04_t02": {
                "title_en": "Remainder and factor theorems",
                "title_bn": "ভাগশেষ ও উৎপাদক উপপাদ্য",
                "udvash_types": [
                    "remainder theorem f(a)",
                    "factor theorem and finding k",
                    "evaluating remainders by substitution",
                    "root-zero and reciprocal-root constructions",
                ],
                "count": 20,
            },
            "hm2_27_ch04_t03": {
                "title_en": "Roots of polynomial equations",
                "title_bn": "বহুপদী সমীকরণের মূল",
                "udvash_types": [
                    "sum and product of roots",
                    "discriminant and nature of roots",
                    "forming equations from transformed roots",
                    "cubic Vieta relations and complex conjugate roots",
                ],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "garbled_stems": "Noisy OCR reconstructed from answer-key algebra and standard board forms",
            "figure_graphs": "Discriminant graph-choice items skipped; nature-of-roots kept as text",
            "stimulus_pairs": "Linked stimulus blocks curated as standalone clear stems",
            "ambiguous_option_glyphs": "Broken Bangla/option glyphs replaced with closed-form HSC standards",
        },
        "low_confidence": [
            "OCR on pp. 100–112 noisy; column text and solution lines used to reconstruct stems.",
            "Inline math stored as plain text (√, i, Σ, fractions) for JSONL.",
            "Some printed multi-select glyph keys incomplete; properties rewritten clearly.",
            "A few cubic/root-list options standardized to closed algebraic forms.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm2_ch04.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
        "math2_progress": {
            "topics_complete": "12/30",
            "note": "Ch04 continues higher_mathematics 2nd paper after Ch01–Ch03 (180Q)",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch04_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
