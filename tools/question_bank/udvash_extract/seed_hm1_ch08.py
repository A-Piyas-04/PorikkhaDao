#!/usr/bin/env python3
"""Seed Higher Mathematics 1st Paper Ch8 (Functions and Graphs).

Curated from Udvash HSC Question Bank 2026 printed pp. 250–254 (PDF 256–260).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
OCR is heavily noisy (~5 pages); reconstructs board-style items and supplements
with accurate HSC-level authored MCQs. Figure-only graph items rewritten as
text-describable questions.
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
    "higher_mathematics p1 ch08; curated bilingual"
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
# hm1_27_ch08_t01 — Domain, range and types of functions
# =============================================================================
T01 = [
    q(
        "The range of f(x) = sin x is:",
        "f(x) = sin x এর রেঞ্জ কোনটি?",
        ["(-1, 1)", "[-2, 2]", "[-1, 1]", "(-2, 2)"],
        ["(-1, 1)", "[-2, 2]", "[-1, 1]", "(-2, 2)"],
        "C", "easy", "factual",
        "sin x attains every value in [-1, 1] and never goes outside that closed interval.",
        "sin x এর মান সর্বদা [-1, 1] বদ্ধ ব্যবধিতে থাকে এবং প্রতিটি মান অর্জন করে।",
    ),
    q(
        "The domain of y = sqrt((x − 1)(x − 2)) is:",
        "y = √((x − 1)(x − 2)) ফাংশনটির ডোমেন কত?",
        ["x < 1", "x > 2", "1 < x < 2", "R − (1, 2)"],
        ["x < 1", "x > 2", "1 < x < 2", "R − (1, 2)"],
        "D", "medium", "numerical",
        "(x − 1)(x − 2) ≥ 0 ⇒ x ≤ 1 or x ≥ 2 ⇒ domain = R − (1, 2).",
        "(x − 1)(x − 2) ≥ 0 ⇒ x ≤ 1 বা x ≥ 2 ⇒ ডোমেন = R − (1, 2)।",
    ),
    q(
        "The domain of f(x) = sqrt(4 − x^2) is:",
        "f(x) = √(4 − x²) এর ডোমেন কত?",
        ["[0, 2]", "(0, 2)", "[-2, 2]", "(-2, 2)"],
        ["[0, 2]", "(0, 2)", "[-2, 2]", "(-2, 2)"],
        "C", "easy", "numerical",
        "4 − x^2 ≥ 0 ⇒ x^2 ≤ 4 ⇒ −2 ≤ x ≤ 2; endpoints give f = 0.",
        "4 − x² ≥ 0 ⇒ x² ≤ 4 ⇒ −2 ≤ x ≤ 2; প্রান্তবিন্দুতে f = 0।",
    ),
    q(
        "The range of g(x) = sqrt(225 − x^2) is:",
        "g(x) = √(225 − x²) এর রেঞ্জ কোনটি?",
        ["(0, 15)", "(0, 9)", "[0, 15]", "[0, 9]"],
        ["(0, 15)", "(0, 9)", "[0, 15]", "[0, 9]"],
        "C", "medium", "numerical",
        "Domain −15 ≤ x ≤ 15; at x = 0, g = 15; at x = ±15, g = 0 ⇒ range [0, 15].",
        "ডোমেন −15 ≤ x ≤ 15; x = 0 এ g = 15; x = ±15 এ g = 0 ⇒ রেঞ্জ [0, 15]।",
    ),
    q(
        "The range of the cosine function is:",
        "কোসাইন ফাংশনের রেঞ্জ কোনটি?",
        ["{-1, 1}", "(-1, 1]", "(-1, 1)", "[-1, 1]"],
        ["{-1, 1}", "(-1, 1]", "(-1, 1)", "[-1, 1]"],
        "D", "easy", "factual",
        "cos x takes every real value in the closed interval [-1, 1].",
        "cos x এর মান সর্বদা বদ্ধ ব্যবধি [-1, 1] এ থাকে।",
    ),
    q(
        "Which statements are true? (i) Every function is a relation "
        "(ii) Not every relation is a function (iii) g(x) = 2x + 1 is one-one",
        "কোনগুলো সঠিক? (i) সকল ফাংশনই সম্পর্ক "
        "(ii) সকল সম্পর্ক ফাংশন নয় (iii) g(x) = 2x + 1 একটি এক-এক ফাংশন",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "easy", "conceptual",
        "Functions are special relations; many relations fail the unique-image rule; "
        "g(x1)=g(x2) ⇒ 2x1+1=2x2+1 ⇒ x1=x2, so g is one-one.",
        "ফাংশন বিশেষ সম্পর্ক; সব সম্পর্ক ফাংশন নয়; g এক-এক কারণ g(x1)=g(x2) ⇒ x1=x2।",
    ),
    q(
        "The domain of f(x) = sqrt(x − 2) is:",
        "f(x) = √(x − 2) ফাংশনের ডোমেন কত?",
        ["(-2, ∞)", "(2, ∞)", "[2, ∞)", "(-∞, 2]"],
        ["(-2, ∞)", "(2, ∞)", "[2, ∞)", "(-∞, 2]"],
        "C", "easy", "numerical",
        "x − 2 ≥ 0 ⇒ x ≥ 2 ⇒ domain [2, ∞).",
        "x − 2 ≥ 0 ⇒ x ≥ 2 ⇒ ডোমেন [2, ∞)।",
    ),
    q(
        "If f(x) = sqrt(8 − x), the domain is:",
        "f(x) = √(8 − x) হলে ডোমেন কোনটি?",
        ["(-∞, 8]", "(-∞, 8)", "[8, ∞)", "(8, ∞)"],
        ["(-∞, 8]", "(-∞, 8)", "[8, ∞)", "(8, ∞)"],
        "A", "easy", "numerical",
        "8 − x ≥ 0 ⇒ x ≤ 8 ⇒ domain (−∞, 8].",
        "8 − x ≥ 0 ⇒ x ≤ 8 ⇒ ডোমেন (−∞, 8]।",
    ),
    q(
        "A function is called onto (surjective) when:",
        "একটি ফাংশনকে অনটু বা সার্বিক বলা হয় যখন:",
        ["domain equals range", "domain equals codomain", "codomain equals range", "domain is empty"],
        ["ডোমেন = রেঞ্জ", "ডোমেন = কোডোমেন", "কোডোমেন = রেঞ্জ", "ডোমেন শূন্য"],
        "C", "medium", "conceptual",
        "Onto means every element of the codomain is an image, i.e. range = codomain.",
        "সার্বিক মানে কোডোমেনের প্রতিটি উপাদানই প্রতিবিম্ব; অর্থাৎ রেঞ্জ = কোডোমেন।",
    ),
    q(
        "The domain of f(x) = 1/(x − 4) is:",
        "f(x) = 1/(x − 4) এর ডোমেন কোনটি?",
        ["R − {4}", "R − {-4}", "R − {0}", "{4}"],
        ["R − {4}", "R − {-4}", "R − {0}", "{4}"],
        "A", "easy", "numerical",
        "Denominator zero when x = 4, so domain is all reals except 4.",
        "x = 4 এ হর শূন্য; ডোমেন R − {4}।",
    ),
    q(
        "Which function is both one-one and onto from R to R?",
        "নিচের কোন ফাংশনটি R থেকে R এ এক-এক ও সার্বিক?",
        ["f(x) = 2x^2", "f(x) = |2x|", "f(x) = cos x", "f(x) = 2x + 1"],
        ["f(x) = 2x^2", "f(x) = |2x|", "f(x) = cos x", "f(x) = 2x + 1"],
        "D", "medium", "conceptual",
        "Only the non-constant linear map 2x+1 is bijective on R; the others fail injectivity or surjectivity.",
        "শুধু রৈখিক ফাংশন 2x+1 R-এ দ্বিএকক; বাকিগুলো এক-এক বা সার্বিক নয়।",
    ),
    q(
        "f(x) = x^2 is an even function because:",
        "f(x) = x² জোড় ফাংশন কারণ:",
        ["f(-x) = -f(x)", "f(-x) = f(x)", "f(x) = 0", "f(x) = x"],
        ["f(-x) = -f(x)", "f(-x) = f(x)", "f(x) = 0", "f(x) = x"],
        "B", "easy", "conceptual",
        "f(-x) = (-x)^2 = x^2 = f(x), the defining property of an even function.",
        "f(-x) = (−x)² = x² = f(x); এটিই জোড় ফাংশনের শর্ত।",
    ),
    q(
        "f(x) = sin x is an odd function because:",
        "f(x) = sin x বিজোড় ফাংশন কারণ:",
        ["f(-x) = f(x)", "f(-x) = -f(x)", "f(x) = 1", "domain is empty"],
        ["f(-x) = f(x)", "f(-x) = -f(x)", "f(x) = 1", "ডোমেন শূন্য"],
        "B", "easy", "conceptual",
        "sin(-x) = -sin x, so f is odd and its graph has 180° rotational symmetry about the origin.",
        "sin(−x) = −sin x; বিজোড় ফাংশনের লেখ মূলবিন্দু সাপেক্ষে ১৮০° প্রতিসম।",
    ),
    q(
        "The range of f(x) = x^2 + 1, x ∈ R, is:",
        "f(x) = x² + 1, x ∈ R এর রেঞ্জ:",
        ["R", "[0, ∞)", "[1, ∞)", "(-∞, 1]"],
        ["R", "[0, ∞)", "[1, ∞)", "(-∞, 1]"],
        "C", "easy", "numerical",
        "x^2 ≥ 0 ⇒ x^2 + 1 ≥ 1; every y ≥ 1 is attained, so range [1, ∞).",
        "x² ≥ 0 ⇒ x² + 1 ≥ 1; y ≥ 1 সব মান অর্জিত ⇒ রেঞ্জ [1, ∞)।",
    ),
    q(
        "The domain of f(x) = ln(x − 1) is:",
        "f(x) = ln(x − 1) এর ডোমেন:",
        ["x > 1", "x ≥ 1", "x < 1", "x ≠ 1"],
        ["x > 1", "x ≥ 1", "x < 1", "x ≠ 1"],
        "A", "easy", "numerical",
        "Natural log requires a positive argument: x − 1 > 0 ⇒ x > 1.",
        "লগারিদমের আর্গুমেন্ট ধনাত্মক: x − 1 > 0 ⇒ x > 1।",
    ),
    q(
        "For real values, the domain of f(x) = 1/sqrt(x^2 − 9) is:",
        "বাস্তব মানের জন্য f(x) = 1/√(x² − 9) এর ডোমেন:",
        ["(-∞, -3] ∪ [3, ∞)", "(-∞, -3) ∪ (3, ∞)", "[-3, 3]", "(-3, 3)"],
        ["(-∞, -3] ∪ [3, ∞)", "(-∞, -3) ∪ (3, ∞)", "[-3, 3]", "(-3, 3)"],
        "B", "hard", "numerical",
        "Need x^2 − 9 > 0 (strict, since sqrt is in a denominator) ⇒ |x| > 3.",
        "হরে বর্গমূল থাকায় x² − 9 > 0 ⇒ |x| > 3।",
    ),
    q(
        "A constant function f(x) = c (c fixed) has range:",
        "ধ্রুবক ফাংশন f(x) = c (c ধ্রুব) এর রেঞ্জ:",
        ["R", "{c}", "[0, c]", "empty set"],
        ["R", "{c}", "[0, c]", "শূন্য সেট"],
        "B", "easy", "conceptual",
        "Every input maps to the single value c, so the range is the singleton {c}.",
        "প্রতিটি ইনপুটের আউটপুট c; রেঞ্জ একক সেট {c}।",
    ),
    q(
        "By the vertical-line test, a curve in the xy-plane is a function of x if:",
        "উলম্ব রেখা পরীক্ষা অনুসারে, xy-তলে একটি রেখাচিত্র x এর ফাংশন যদি:",
        [
            "every horizontal line meets it at most once",
            "every vertical line meets it at most once",
            "it is closed",
            "it is a circle",
        ],
        [
            "প্রতিটি অনুভূমিক রেখা সর্বোচ্চ একবার ছেদ করে",
            "প্রতিটি উলম্ব রেখা সর্বোচ্চ একবার ছেদ করে",
            "এটি বদ্ধ",
            "এটি বৃত্ত",
        ],
        "B", "easy", "conceptual",
        "Unique y for each x means no vertical line can cut the graph more than once.",
        "প্রতিটি x এর জন্য অনন্য y ⇒ কোনো উলম্ব রেখা একবারের বেশি ছেদ করতে পারে না।",
    ),
    q(
        "If f : {1, 2, 3} → {a, b, c} with f(1)=a, f(2)=b, f(3)=a, then f is:",
        "f : {1, 2, 3} → {a, b, c} এবং f(1)=a, f(2)=b, f(3)=a হলে f:",
        ["one-one but not onto", "onto but not one-one", "neither one-one nor onto", "bijective"],
        ["এক-এক কিন্তু সার্বিক নয়", "সার্বিক কিন্তু এক-এক নয়", "এক-একও নয় সার্বিকও নয়", "দ্বিএকক"],
        "C", "medium", "conceptual",
        "f(1)=f(3) so not one-one; c is unused so not onto.",
        "f(1)=f(3) ⇒ এক-এক নয়; c প্রতিবিম্ব নয় ⇒ সার্বিকও নয়।",
    ),
    q(
        "The domain of f(x) = (2x − 3)/(x^2 − 5x + 6) is:",
        "f(x) = (2x − 3)/(x² − 5x + 6) এর ডোমেন:",
        ["R − {2, 3}", "R − {2}", "R − {3}", "R"],
        ["R − {2, 3}", "R − {2}", "R − {3}", "R"],
        "A", "medium", "numerical",
        "x^2 − 5x + 6 = (x − 2)(x − 3); exclude zeros of the denominator: R − {2, 3}.",
        "x² − 5x + 6 = (x − 2)(x − 3); হর শূন্যের স্থান বাদ: R − {2, 3}।",
    ),
]


# =============================================================================
# hm1_27_ch08_t02 — Composition and inverse functions
# =============================================================================
T02 = [
    q(
        "If f(x) = x + 3, then f(f(−3)) equals:",
        "f(x) = x + 3 হলে f(f(−3)) এর মান কত?",
        ["-3", "0", "3", "9"],
        ["-3", "0", "3", "9"],
        "C", "easy", "numerical",
        "f(−3) = 0; f(f(−3)) = f(0) = 3.",
        "f(−3) = 0; f(f(−3)) = f(0) = 3।",
    ),
    q(
        "If y = x + 3 defines f, then f^{−1}(−9) equals:",
        "y = x + 3 হলে f⁻¹(−9) এর মান কত?",
        ["12", "6", "-6", "-12"],
        ["12", "6", "-6", "-12"],
        "D", "easy", "numerical",
        "Inverse is x − 3, so f^{−1}(−9) = −9 − 3 = −12.",
        "বিপরীত f⁻¹(x) = x − 3; f⁻¹(−9) = −12।",
    ),
    q(
        "If f(x) = x^2 (x ∈ R), then the preimage f^{−1}(169) is:",
        "f(x) = x² (x ∈ R) হলে f⁻¹(169) = ?",
        ["{13}", "{-13, 13}", "(-13, 13)", "[-13, 13]"],
        ["{13}", "{-13, 13}", "(-13, 13)", "[-13, 13]"],
        "B", "medium", "numerical",
        "x^2 = 169 ⇒ x = ±13, so the preimage set is {-13, 13}.",
        "x² = 169 ⇒ x = ±13; পূর্বপ্রতিবিম্ব সেট {-13, 13}।",
    ),
    q(
        "If g(x) = ln(cos x), then e^{2g(x)} equals:",
        "g(x) = ln(cos x) হলে e^{2g(x)} এর মান:",
        ["1 + cos 2x", "1 − cos 2x", "(1/2)(1 + cos 2x)", "(1/2)(1 − cos 2x)"],
        ["1 + cos 2x", "1 − cos 2x", "(1/2)(1 + cos 2x)", "(1/2)(1 − cos 2x)"],
        "C", "hard", "numerical",
        "e^{2 ln(cos x)} = cos^2 x = (1 + cos 2x)/2.",
        "e^{2 ln(cos x)} = cos² x = (1 + cos 2x)/2।",
    ),
    q(
        "If f(x) = 2 ln(cos x) and g(x) = x^2 − 3, then (g ∘ f)(x) equals:",
        "f(x) = 2 ln(cos x) এবং g(x) = x² − 3 হলে (g ∘ f)(x) = ?",
        ["8 ln(cos x) − 3", "4 (ln(cos x))^2 − 3", "2 ln(cos x) − 3", "ln(cos x) − 3"],
        ["8 ln(cos x) − 3", "4 (ln(cos x))^2 − 3", "2 ln(cos x) − 3", "ln(cos x) − 3"],
        "B", "hard", "numerical",
        "g(f(x)) = (2 ln(cos x))^2 − 3 = 4 (ln(cos x))^2 − 3.",
        "g(f(x)) = (2 ln(cos x))² − 3 = 4 (ln(cos x))² − 3।",
    ),
    q(
        "If f(x) = 3x − 2 and g(x) = 2x + 5, then (g ∘ f)(−2) equals:",
        "f(x) = 3x − 2 এবং g(x) = 2x + 5 হলে (g ∘ f)(−2) = ?",
        ["-11", "1", "13", "25"],
        ["-11", "1", "13", "25"],
        "A", "medium", "numerical",
        "f(−2) = −8; g(−8) = −16 + 5 = −11.",
        "f(−2) = −8; g(−8) = −16 + 5 = −11।",
    ),
    q(
        "If f(x) = 3x − 2, then f^{−1}(x) equals:",
        "f(x) = 3x − 2 হলে f⁻¹(x) = ?",
        ["3x + 2", "(x + 2)/3", "3x − 2", "(x − 2)/3"],
        ["3x + 2", "(x + 2)/3", "3x − 2", "(x − 2)/3"],
        "B", "easy", "numerical",
        "y = 3x − 2 ⇒ x = (y + 2)/3 ⇒ f^{−1}(x) = (x + 2)/3.",
        "y = 3x − 2 ⇒ x = (y + 2)/3 ⇒ f⁻¹(x) = (x + 2)/3।",
    ),
    q(
        "If f(x) = ln x, then f(25) equals:",
        "f(x) = ln x হলে f(25) এর মান কত?",
        ["ln 5", "5 ln 2", "ln 25 / 2", "2 ln 5"],
        ["ln 5", "5 ln 2", "ln 25 / 2", "2 ln 5"],
        "D", "easy", "numerical",
        "ln 25 = ln(5^2) = 2 ln 5.",
        "ln 25 = ln(5²) = 2 ln 5।",
    ),
    q(
        "If f(x) = x^2 + 3 with x ≥ 0, then f^{−1}(11) equals:",
        "f(x) = x² + 3, x ≥ 0 হলে f⁻¹(11) এর মান:",
        ["2", "2 sqrt(2)", "3", "2 sqrt(3)"],
        ["2", "2 sqrt(2)", "3", "2 sqrt(3)"],
        "B", "medium", "numerical",
        "x^2 + 3 = 11 ⇒ x = sqrt(8) = 2√2 (non-negative branch).",
        "x² + 3 = 11 ⇒ x = √8 = 2√2 (অঋণাত্মক শাখা)।",
    ),
    q(
        "If f(x) = 2 e^{2x}, then f(ln(2x)) equals:",
        "f(x) = 2e^{2x} হলে f(ln(2x)) এর মান:",
        ["4x", "4x^2", "8x", "8x^2"],
        ["4x", "4x^2", "8x", "8x^2"],
        "D", "hard", "numerical",
        "f(ln(2x)) = 2 e^{2 ln(2x)} = 2 (2x)^2 = 8x^2.",
        "f(ln(2x)) = 2 e^{2 ln(2x)} = 2(2x)² = 8x²।",
    ),
    q(
        "A real function admits an inverse on its domain/codomain setup only if it is:",
        "একটি বাস্তব ফাংশনের বিপরীত থাকে কেবল যদি এটি:",
        ["even", "periodic", "one-one and onto", "continuous only"],
        ["জোড়", "পর্যাবৃত্ত", "এক-এক ও সার্বিক", "শুধু অবিচ্ছিন্ন"],
        "C", "easy", "conceptual",
        "Invertibility (with a two-sided inverse) requires a bijection: one-one and onto.",
        "দ্বিপাক্ষিক বিপরীতের জন্য ফাংশন দ্বিএকক (এক-এক ও সার্বিক) হতে হয়।",
    ),
    q(
        "If f(x) = 2x + 1, then f^{−1}(x) equals:",
        "f(x) = 2x + 1 হলে f⁻¹(x) = ?",
        ["(x + 1)/2", "(x − 1)/2", "2x − 1", "1 − 2x"],
        ["(x + 1)/2", "(x − 1)/2", "2x − 1", "1 − 2x"],
        "B", "easy", "numerical",
        "y = 2x + 1 ⇒ x = (y − 1)/2 ⇒ f^{−1}(x) = (x − 1)/2.",
        "y = 2x + 1 ⇒ x = (y − 1)/2 ⇒ f⁻¹(x) = (x − 1)/2।",
    ),
    q(
        "If f(x) = e^x, then f^{−1}(x) equals:",
        "f(x) = e^x হলে f⁻¹(x) = ?",
        ["e^{−x}", "ln x", "1/x", "x^e"],
        ["e^{−x}", "ln x", "1/x", "x^e"],
        "B", "easy", "factual",
        "The inverse of the exponential is the natural logarithm (x > 0).",
        "সূচকীয় ফাংশনের বিপরীত প্রাকৃতিক লগারিদম (x > 0)।",
    ),
    q(
        "If f^{−1}(x) = x^3, then f(x) equals:",
        "f⁻¹(x) = x³ হলে f(x) = ?",
        ["x^{1/3}", "x^3", "3x", "1/x^3"],
        ["x^{1/3}", "x^3", "3x", "1/x^3"],
        "A", "medium", "numerical",
        "If the inverse cubes, the original function is the real cube root: f(x) = x^{1/3}.",
        "বিপরীত ঘন করলে মূল ফাংশন ঘনমূল: f(x) = x^{1/3}।",
    ),
    q(
        "If f(x) = sqrt(x) and g(x) = x + 1 (x ≥ 0), then (f ∘ g)(3) equals:",
        "f(x) = √x এবং g(x) = x + 1 (x ≥ 0) হলে (f ∘ g)(3) = ?",
        ["2", "sqrt(3)", "4", "sqrt(2)"],
        ["2", "sqrt(3)", "4", "sqrt(2)"],
        "A", "easy", "numerical",
        "(f ∘ g)(3) = f(g(3)) = f(4) = 2.",
        "(f ∘ g)(3) = f(g(3)) = f(4) = 2।",
    ),
    q(
        "In general, for composable f and g:",
        "সাধারণত সংযোজ্য f ও g এর জন্য:",
        ["f ∘ g = g ∘ f always", "f ∘ g may differ from g ∘ f", "composition is undefined", "inverses are equal"],
        ["সর্বদা f ∘ g = g ∘ f", "f ∘ g ও g ∘ f ভিন্ন হতে পারে", "সংযোজন অসংজ্ঞাত", "বিপরীত সমান"],
        "B", "easy", "conceptual",
        "Function composition is associative but not commutative in general.",
        "ফাংশন সংযোজন সাধারণত বিনিময়যোগ্য নয়; f∘g ≠ g∘f হতে পারে।",
    ),
    q(
        "If f(x) = (2x + 3)/(x − 1) (x ≠ 1), then f^{−1}(x) equals:",
        "f(x) = (2x + 3)/(x − 1), x ≠ 1 হলে f⁻¹(x) = ?",
        ["(x + 3)/(x − 2)", "(x − 3)/(x − 2)", "(x + 3)/(2 − x)", "(x − 3)/(2 − x)"],
        ["(x + 3)/(x − 2)", "(x − 3)/(x − 2)", "(x + 3)/(2 − x)", "(x − 3)/(2 − x)"],
        "A", "hard", "numerical",
        "y(x − 1) = 2x + 3 ⇒ xy − y = 2x + 3 ⇒ xy − 2x = y + 3 ⇒ x(y − 2) = y + 3 "
        "⇒ x = (y + 3)/(y − 2). Swap variables.",
        "y(x − 1) = 2x + 3 ⇒ x = (y + 3)/(y − 2) ⇒ f⁻¹(x) = (x + 3)/(x − 2)।",
    ),
    q(
        "Define f(x) = 3x + 1 for x ≤ 1 and f(x) = 2x − 3 for x > 5. Then f(0) equals:",
        "f(x) = 3x + 1 যখন x ≤ 1 এবং f(x) = 2x − 3 যখন x > 5। f(0) = ?",
        ["-3", "-1", "0", "1"],
        ["-3", "-1", "0", "1"],
        "D", "medium", "numerical",
        "0 ≤ 1, so use the first piece: f(0) = 1.",
        "0 ≤ 1, তাই প্রথম খণ্ড: f(0) = 3·0 + 1 = 1।",
    ),
    q(
        "If f(x) = 3x + 1 for all x ≤ 1, then (f ∘ f)(−1) equals:",
        "সকল x ≤ 1 এর জন্য f(x) = 3x + 1 হলে (f ∘ f)(−1) = ?",
        ["-7", "-5", "1", "3"],
        ["-7", "-5", "1", "3"],
        "B", "hard", "numerical",
        "f(−1) = −2; f(−2) = 3(−2)+1 = −5.",
        "f(−1) = −2; f(−2) = −6 + 1 = −5।",
    ),
    q(
        "If (f ∘ g)(x) = x for all x in the domain of g, then:",
        "(f ∘ g)(x) = x সর্বত্র সত্য হলে:",
        ["f is the zero map", "g is a left inverse of f", "f is a left inverse of g", "g = f"],
        ["f শূন্য ম্যাপ", "g হলো f এর বাম বিপরীত", "f হলো g এর বাম বিপরীত", "g = f"],
        "C", "medium", "conceptual",
        "f(g(x)) = x means f undoes g from the left: f is a left inverse of g.",
        "f(g(x)) = x ⇒ f হলো g এর বাম বিপরীত।",
    ),
]


# =============================================================================
# hm1_27_ch08_t03 — Graphs and transformations
# =============================================================================
T03 = [
    q(
        "A parabola opens upward, has vertex on the y-axis at (0, −3), and is congruent to y = x^2. Its equation is:",
        "একটি প্যারাবোলা উপরের দিকে খোলা, শীর্ষ y-অক্ষে (0, −3), এবং y = x² এর সমরূপ। সমীকরণ:",
        ["y = x^2", "y = x^2 − 3", "y = −2x^2", "x = y^2"],
        ["y = x^2", "y = x^2 − 3", "y = −2x^2", "x = y^2"],
        "B", "easy", "conceptual",
        "Vertical shift of y = x^2 down by 3 units gives y = x^2 − 3.",
        "y = x² কে ৩ একক নিচে সরালে y = x² − 3।",
    ),
    q(
        "For f(x) = sin x, which are true? (i) domain = R (ii) range = [-1, 1] "
        "(iii) graph is symmetric about the y-axis",
        "f(x) = sin x এর জন্য কোনগুলো সঠিক? (i) ডোমেন = R (ii) রেঞ্জ = [-1, 1] "
        "(iii) লেখচিত্র y-অক্ষের সাপেক্ষে প্রতিসম",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii", "i, ii ও iii"],
        "A", "medium", "conceptual",
        "sin is odd, so the graph has origin symmetry, not y-axis symmetry. (i) and (ii) hold.",
        "sin বিজোড় ⇒ y-অক্ষ প্রতিসম নয়; (i) ও (ii) সঠিক।",
    ),
    q(
        "For f(x) = 3 cos x, which are true? (i) range = [-3, 3] (ii) period = 2π "
        "(iii) graph is symmetric about the y-axis",
        "f(x) = 3 cos x এর জন্য কোনগুলো সঠিক? (i) রেঞ্জ = [-3, 3] (ii) পর্যায়কাল = 2π "
        "(iii) লেখচিত্র y-অক্ষের সাপেক্ষে প্রতিসম",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "Amplitude 3 ⇒ range [-3, 3]; period of cos is 2π; cos is even ⇒ y-axis symmetry.",
        "বিস্তার ৩ ⇒ রেঞ্জ [-3, 3]; পর্যায় 2π; cos জোড় ⇒ y-অক্ষ প্রতিসম।",
    ),
    q(
        "For f(x) = cos 3x, which are true? (i) period = 2π/3 (ii) range = [-3, 3] "
        "(iii) graph is symmetric about the y-axis",
        "f(x) = cos 3x এর জন্য কোনগুলো সঠিক? (i) পর্যায়কাল = 2π/3 (ii) রেঞ্জ = [-3, 3] "
        "(iii) লেখচিত্র y-অক্ষের সাপেক্ষে প্রতিসম",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "B", "medium", "conceptual",
        "Period = 2π/3; range remains [-1, 1], not [-3, 3]; cos 3x is even.",
        "পর্যায় 2π/3; রেঞ্জ [-1, 1] ([-3, 3] নয়); cos 3x জোড়।",
    ),
    q(
        "The graph of y = −|2x| lies entirely in which half-plane?",
        "y = −|2x| এর লেখচিত্র কোন অর্ধতলে থাকে?",
        ["above the x-axis only", "on or below the x-axis", "right of the y-axis only", "inside the unit circle"],
        ["শুধু x-অক্ষের উপরে", "x-অক্ষের উপর বা নিচে", "শুধু y-অক্ষের ডানে", "একক বৃত্তের ভিতরে"],
        "B", "easy", "conceptual",
        "|2x| ≥ 0 ⇒ −|2x| ≤ 0, so the graph never goes above the x-axis.",
        "|2x| ≥ 0 ⇒ −|2x| ≤ 0; লেখ কখনো x-অক্ষের উপরে যায় না।",
    ),
    q(
        "The graph of x + y = 0 is the line that:",
        "x + y = 0 এর লেখচিত্র সেই সরলরেখা যা:",
        ["has slope 1 through origin", "has slope −1 through origin", "is horizontal", "is vertical"],
        ["মূলবিন্দু দিয়ে ঢাল 1", "মূলবিন্দু দিয়ে ঢাল −1", "অনুভূমিক", "উলম্ব"],
        "B", "easy", "factual",
        "y = −x is the line through the origin with slope −1.",
        "y = −x মূলবিন্দুগামী ঢাল −1 এর রেখা।",
    ),
    q(
        "Compared with y = f(x), the graph of y = f(x) + k (k > 0) is shifted:",
        "y = f(x) এর তুলনায় y = f(x) + k (k > 0) এর লেখ:",
        ["k units left", "k units right", "k units up", "k units down"],
        ["k একক বামে", "k একক ডানে", "k একক উপরে", "k একক নিচে"],
        "C", "easy", "conceptual",
        "Adding a positive constant raises every y-value by k (vertical translation up).",
        "ধনাত্মক ধ্রুবক যোগ করলে প্রতিটি y-মান k বাড়ে (উলম্ব স্থানান্তর উপরে)।",
    ),
    q(
        "Compared with y = f(x), the graph of y = f(x − h) (h > 0) is shifted:",
        "y = f(x) এর তুলনায় y = f(x − h) (h > 0) এর লেখ:",
        ["h units left", "h units right", "h units up", "h units down"],
        ["h একক বামে", "h একক ডানে", "h একক উপরে", "h একক নিচে"],
        "B", "easy", "conceptual",
        "Replacing x by x − h moves the graph h units to the right.",
        "x এর স্থলে x − h বসালে লেখ h একক ডানে সরে।",
    ),
    q(
        "The graph of y = −f(x) is obtained from y = f(x) by:",
        "y = −f(x) পাওয়া যায় y = f(x) থেকে:",
        ["reflection in the y-axis", "reflection in the x-axis", "rotation by 90 deg", "horizontal stretch"],
        ["y-অক্ষে প্রতিফলন", "x-অক্ষে প্রতিফলন", "৯০° ঘূর্ণন", "অনুভূমিক প্রসারণ"],
        "B", "easy", "conceptual",
        "Negating outputs reflects the graph across the x-axis.",
        "আউটপুটের চিহ্ন পরিবর্তন x-অক্ষ সাপেক্ষে প্রতিফলন।",
    ),
    q(
        "The graph of y = f(−x) is obtained from y = f(x) by:",
        "y = f(−x) পাওয়া যায় y = f(x) থেকে:",
        ["reflection in the y-axis", "reflection in the x-axis", "shift up by 1", "vertical shrink"],
        ["y-অক্ষে প্রতিফলন", "x-অক্ষে প্রতিফলন", "১ একক উপরে সরণ", "উলম্ব সংকোচন"],
        "A", "easy", "conceptual",
        "Replacing x by −x reflects the graph across the y-axis.",
        "x এর স্থলে −x বসালে y-অক্ষ সাপেক্ষে প্রতিফলন।",
    ),
    q(
        "The fundamental period of y = sin(2x) is:",
        "y = sin(2x) এর মৌলিক পর্যায়কাল:",
        ["2π", "π", "π/2", "4π"],
        ["2π", "π", "π/2", "4π"],
        "B", "easy", "numerical",
        "Period of sin(bx) is 2π/|b|; here b = 2 ⇒ period π.",
        "sin(bx) এর পর্যায় 2π/|b|; b = 2 ⇒ পর্যায় π।",
    ),
    q(
        "The vertex of the parabola y = (x − 2)^2 + 3 is:",
        "প্যারাবোলা y = (x − 2)² + 3 এর শীর্ষবিন্দু:",
        ["(2, 3)", "(-2, 3)", "(2, -3)", "(3, 2)"],
        ["(2, 3)", "(-2, 3)", "(2, -3)", "(3, 2)"],
        "A", "easy", "numerical",
        "Vertex form y = (x − h)^2 + k has vertex (h, k) = (2, 3).",
        "y = (x − h)² + k আকারে শীর্ষ (h, k) = (2, 3)।",
    ),
    q(
        "The graph of y = |x| is best described as:",
        "y = |x| এর লেখচিত্রের সঠিক বর্ণনা:",
        ["a V opening upward, vertex at origin, even", "a V opening downward", "a circle", "a straight line of slope 1 only"],
        ["উপরের দিকে খোলা V, শীর্ষ মূলবিন্দুতে, জোড়", "নিচের দিকে খোলা V", "একটি বৃত্ত", "শুধু ঢাল 1 এর সরলরেখা"],
        "A", "easy", "conceptual",
        "|x| is even; for x ≥ 0 it is y = x and for x < 0 it is y = −x, forming an upward V.",
        "|x| জোড়; x≥0 এ y=x, x<0 এ y=−x — উপরের দিকে খোলা V।",
    ),
    q(
        "The graph of y = 1/x (x ≠ 0) has asymptotes:",
        "y = 1/x (x ≠ 0) এর অসীমরেখা:",
        ["only y = 0", "only x = 0", "both x = 0 and y = 0", "x = 1 and y = 1"],
        ["শুধু y = 0", "শুধু x = 0", "x = 0 ও y = 0 উভয়ই", "x = 1 ও y = 1"],
        "C", "medium", "factual",
        "Vertical asymptote x = 0 and horizontal asymptote y = 0.",
        "উলম্ব অসীমরেখা x = 0 এবং অনুভূমিক অসীমরেখা y = 0।",
    ),
    q(
        "The vertex of y = (x + 3)^2 is:",
        "y = (x + 3)² এর শীর্ষবিন্দু:",
        ["(3, 0)", "(-3, 0)", "(0, 3)", "(0, -3)"],
        ["(3, 0)", "(-3, 0)", "(0, 3)", "(0, -3)"],
        "B", "easy", "numerical",
        "y = (x + 3)^2 = (x − (−3))^2 has vertex (−3, 0).",
        "y = (x + 3)² = (x − (−3))² এর শীর্ষ (−3, 0)।",
    ),
    q(
        "An even function’s graph is always symmetric about:",
        "জোড় ফাংশনের লেখচিত্র সর্বদা প্রতিসম:",
        ["the origin", "the x-axis", "the y-axis", "the line y = x"],
        ["মূলবিন্দু সাপেক্ষে", "x-অক্ষ সাপেক্ষে", "y-অক্ষ সাপেক্ষে", "y = x রেখা সাপেক্ষে"],
        "C", "easy", "factual",
        "f(−x) = f(x) means mirror symmetry across the y-axis.",
        "f(−x) = f(x) ⇒ y-অক্ষ সাপেক্ষে দর্পণ প্রতিসমতা।",
    ),
    q(
        "An odd function’s graph is always symmetric under:",
        "বিজোড় ফাংশনের লেখচিত্র সর্বদা প্রতিসম:",
        ["reflection in the y-axis", "180 deg rotation about the origin", "reflection in y = x", "horizontal translation"],
        ["y-অক্ষে প্রতিফলন", "মূলবিন্দুতে ১৮০° ঘূর্ণন", "y = x এ প্রতিফলন", "অনুভূমিক সরণ"],
        "B", "easy", "factual",
        "f(−x) = −f(x) is equivalent to 180° rotational symmetry about the origin.",
        "f(−x) = −f(x) ⇒ মূলবিন্দুতে ১৮০° ঘূর্ণন প্রতিসমতা।",
    ),
    q(
        "Starting from y = sqrt(x), the graph of y = sqrt(x − 1) + 2 is obtained by shifting:",
        "y = √x থেকে y = √(x − 1) + 2 পাওয়া যায় সরিয়ে:",
        ["1 right and 2 up", "1 left and 2 up", "1 right and 2 down", "1 left and 2 down"],
        ["১ ডানে ও ২ উপরে", "১ বামে ও ২ উপরে", "১ ডানে ও ২ নিচে", "১ বামে ও ২ নিচে"],
        "A", "medium", "application",
        "x → x − 1 shifts right by 1; then +2 shifts up by 2.",
        "x → x − 1 ⇒ ১ ডানে; +2 ⇒ ২ উপরে।",
    ),
    q(
        "Compared with y = f(x), the graph of y = 2f(x) is:",
        "y = f(x) এর তুলনায় y = 2f(x) এর লেখ:",
        ["vertically stretched by factor 2", "horizontally stretched by factor 2", "shifted up by 2", "reflected in x-axis"],
        ["উলম্বভাবে ২ গুণ প্রসারিত", "অনুভূমিকভাবে ২ গুণ প্রসারিত", "২ একক উপরে সরা", "x-অক্ষে প্রতিফলিত"],
        "A", "easy", "conceptual",
        "Multiplying outputs by 2 doubles distances from the x-axis (vertical stretch).",
        "আউটপুট ২ দিয়ে গুণ করলে x-অক্ষ থেকে দূরত্ব দ্বিগুণ (উলম্ব প্রসারণ)।",
    ),
    q(
        "The graph of y = sqrt(x) is defined only for:",
        "y = √x এর লেখচিত্র কেবল সংজ্ঞায়িত:",
        ["x < 0", "x ≤ 0", "x ≥ 0", "all real x"],
        ["x < 0", "x ≤ 0", "x ≥ 0", "সকল বাস্তব x"],
        "C", "easy", "factual",
        "Real square root requires a non-negative radicand; domain [0, ∞).",
        "বাস্তব বর্গমূলের জন্য অঋণাত্মক রাডিক্যান্ড; ডোমেন [0, ∞)।",
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
    counts["hm1_27_ch08_t01"] = write_topic("hm1_27_ch08_t01", T01)["count"]
    counts["hm1_27_ch08_t02"] = write_topic("hm1_27_ch08_t02", T02)["count"]
    counts["hm1_27_ch08_t03"] = write_topic("hm1_27_ch08_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm1_27_ch08",
        "title_en": "Functions and Graphs",
        "title_bn": "ফাংশন ও ফাংশনের লেখচিত্র",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(250, 255)],
        "topics": {
            "hm1_27_ch08_t01": {
                "title_en": "Domain, range and types of functions",
                "title_bn": "ডোমেন, রেঞ্জ ও ফাংশনের প্রকার",
                "udvash_types": ["T-01", "T-02", "T-04", "domain", "range", "one-one", "onto", "even/odd"],
                "count": 20,
            },
            "hm1_27_ch08_t02": {
                "title_en": "Composition and inverse functions",
                "title_bn": "সংযোজিত ও বিপরীত ফাংশন",
                "udvash_types": ["T-03", "T-05", "composition", "inverse", "piecewise eval"],
                "count": 20,
            },
            "hm1_27_ch08_t03": {
                "title_en": "Graphs and transformations",
                "title_bn": "লেখচিত্র ও রূপান্তর",
                "udvash_types": ["T-06", "sketches", "shifts", "reflections", "period", "symmetry"],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "figure_only_sketches": "Printed sketch/option-figure items (parabola sketches, which-graph-is-function, y=-|2x| panels) rewritten as text-describable MCQs",
            "Q01_piecewise_garbled": "Opening piecewise f(0.5)-style stem OCR-unreadable; replaced with clear authored domain/eval items",
            "Q14_figure_functions": "Vertical-line-test figure options unreadable; curated as conceptual vertical-line-test stem",
            "stimulus_pairs": "Linked stimulus blocks kept as standalone clear stems where OCR lost shared definitions",
        },
        "low_confidence": [
            "OCR on pp. 250–254 heavily noisy; column PNGs/answer keys used to reconstruct stems.",
            "Short chapter (~5 printed pages); authored supplements fill to exactly 20/topic.",
            "Inline math stored as plain text (sqrt, ^, pi, ln/e) for JSONL.",
            "Some printed keys cite calculator/figure; retained only when closed form matches.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm1_ch08.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch08_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
