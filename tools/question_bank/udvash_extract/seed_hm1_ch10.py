#!/usr/bin/env python3
"""Seed Higher Mathematics 1st Paper Ch10 (Integration).

Curated from Udvash HSC Question Bank 2026 printed pp. 329–343 (PDF 335–349).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
OCR is heavily noisy (~15 pages); reconstructs board-style items from solutions/
column text and supplements with accurate HSC-level authored MCQs. Figure-only
items rewritten as text-describable questions.
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
    "higher_mathematics p1 ch10; curated bilingual"
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
# hm1_27_ch10_t01 — Indefinite integrals / অনির্দিষ্ট যোগজ
# =============================================================================
T01 = [
    q(
        "If ∫ dx/(2 − 5x) = f(x) + C, then f(x) equals:",
        "যদি ∫ dx/(2 − 5x) = f(x) + C হয়, তবে f(x) এর মান কোনটি?",
        ["(1/5) ln|2 − 5x|", "−(1/5) ln|2 − 5x|", "3 ln|2 − 5x|", "−3 ln|2 − 5x|"],
        ["(1/5) ln|2 − 5x|", "−(1/5) ln|2 − 5x|", "3 ln|2 − 5x|", "−3 ln|2 − 5x|"],
        "B", "easy", "numerical",
        "∫ dx/(2 − 5x) = (−1/5) ln|2 − 5x| + C.",
        "∫ dx/(2 − 5x) = (−1/5) ln|2 − 5x| + C।",
    ),
    q(
        "∫ dx/√(x² − a²) equals:",
        "∫ dx/√(x² − a²) এর মান কত?",
        ["ln|x − a| + C", "(1/a) ln|(x − a)/(x + a)| + C", "ln|x + √(x² − a²)| + C", "sin⁻¹(x/a) + C"],
        ["ln|x − a| + C", "(1/a) ln|(x − a)/(x + a)| + C", "ln|x + √(x² − a²)| + C", "sin⁻¹(x/a) + C"],
        "C", "medium", "factual",
        "Standard form: ∫ dx/√(x² − a²) = ln|x + √(x² − a²)| + C.",
        "প্রামাণিক সূত্র: ∫ dx/√(x² − a²) = ln|x + √(x² − a²)| + C।",
    ),
    q(
        "If f(x) = sin x and g(x) = cos x, then ∫ eˣ {f(x) + g(x)} dx equals:",
        "f(x) = sin x এবং g(x) = cos x হলে ∫ eˣ {f(x) + g(x)} dx এর মান কত?",
        ["eˣ sin x + C", "eˣ cos x + C", "eˣ (cos x + sin x) + C", "eˣ (cos x − sin x) + C"],
        ["eˣ sin x + C", "eˣ cos x + C", "eˣ (cos x + sin x) + C", "eˣ (cos x − sin x) + C"],
        "A", "medium", "numerical",
        "∫ eˣ {f + f'} dx = eˣ f + C with f = sin x, f' = cos x ⇒ eˣ sin x + C.",
        "∫ eˣ {f + f'} dx = eˣ f + C; f = sin x ⇒ eˣ sin x + C।",
    ),
    q(
        "∫ cos(bx) dx equals (b ≠ 0):",
        "∫ cos(bx) dx এর মান কত? (b ≠ 0)",
        ["−(1/b) sin(bx) + C", "(1/b) sin(bx) + C", "−b sin(bx) + C", "b sin(bx) + C"],
        ["−(1/b) sin(bx) + C", "(1/b) sin(bx) + C", "−b sin(bx) + C", "b sin(bx) + C"],
        "B", "easy", "factual",
        "∫ cos(bx) dx = (1/b) sin(bx) + C.",
        "∫ cos(bx) dx = (1/b) sin(bx) + C।",
    ),
    q(
        "∫ tan x dx equals which of the following?",
        "∫ tan x dx এর মান নিচের কোনটি?",
        ["−ln|cos x| + C only", "ln|sec x| + C only", "both −ln|cos x| + C and ln|sec x| + C", "ln|cot x| + C"],
        ["শুধু −ln|cos x| + C", "শুধু ln|sec x| + C", "−ln|cos x| + C এবং ln|sec x| + C উভয়ই", "ln|cot x| + C"],
        "C", "easy", "conceptual",
        "∫ tan x dx = ∫ sin x/cos x dx = −ln|cos x| + C = ln|sec x| + C.",
        "∫ tan x dx = −ln|cos x| + C = ln|sec x| + C।",
    ),
    q(
        "∫ cot x dx equals:",
        "∫ cot x dx এর মান কোনটি?",
        ["ln|cos x| + C", "ln|sec x| + C", "ln|tan x| + C", "ln|sin x| + C"],
        ["ln|cos x| + C", "ln|sec x| + C", "ln|tan x| + C", "ln|sin x| + C"],
        "D", "easy", "factual",
        "∫ cot x dx = ∫ cos x/sin x dx = ln|sin x| + C.",
        "∫ cot x dx = ln|sin x| + C।",
    ),
    q(
        "∫ 5ˣ dx equals:",
        "∫ 5ˣ dx এর মান কত?",
        ["5ˣ ln 5 + C", "5ˣ / ln 5 + C", "5ˣ / 5 + C", "ln(5ˣ) + C"],
        ["5ˣ ln 5 + C", "5ˣ / ln 5 + C", "5ˣ / 5 + C", "ln(5ˣ) + C"],
        "B", "easy", "factual",
        "∫ aˣ dx = aˣ / ln a + C with a = 5.",
        "∫ aˣ dx = aˣ / ln a + C; a = 5।",
    ),
    q(
        "If ∫ Pˣ dx = F(x) + C, then F(x) equals:",
        "যদি ∫ Pˣ dx = F(x) + C হয়, তবে F(x) এর মান কোনটি?",
        ["Pˣ log_e P", "Pˣ / log_e P", "Pˣ /(x + 1)", "x Pˣ"],
        ["Pˣ log_e P", "Pˣ / log_e P", "Pˣ /(x + 1)", "x Pˣ"],
        "B", "easy", "factual",
        "∫ Pˣ dx = Pˣ / ln P + C = Pˣ / log_e P + C.",
        "∫ Pˣ dx = Pˣ / ln P + C।",
    ),
    q(
        "If ∫ cosec²(5 − 8x) dx = a cot(5 − 8x) + C, then a equals:",
        "যদি ∫ cosec²(5 − 8x) dx = a cot(5 − 8x) + C হয়, তবে a এর মান কোনটি?",
        ["−8", "−1/8", "1/8", "8"],
        ["−8", "−1/8", "1/8", "8"],
        "C", "medium", "numerical",
        "u = 5 − 8x ⇒ ∫ csc² u (−du/8) = (1/8) cot u ⇒ a = 1/8.",
        "u = 5 − 8x নিলে a = 1/8 পাওয়া যায়।",
    ),
    q(
        "∫ dx/√(5 − x²) equals:",
        "∫ dx/√(5 − x²) এর মান কত?",
        ["sin⁻¹(x/√5) + C", "(1/√5) sin⁻¹(x/√5) + C", "tan⁻¹(x/√5) + C", "√(5 − x²) + C"],
        ["sin⁻¹(x/√5) + C", "(1/√5) sin⁻¹(x/√5) + C", "tan⁻¹(x/√5) + C", "√(5 − x²) + C"],
        "A", "medium", "numerical",
        "∫ dx/√(a² − x²) = sin⁻¹(x/a) with a = √5.",
        "a = √5 নিয়ে ∫ dx/√(a² − x²) = sin⁻¹(x/a)।",
    ),
    q(
        "∫ e^{ax} dx equals (a ≠ 0):",
        "∫ e^{ax} dx এর মান কত? (a ≠ 0)",
        ["−a e^{ax} + C", "−(1/a) e^{ax} + C", "a e^{ax} + C", "(1/a) e^{ax} + C"],
        ["−a e^{ax} + C", "−(1/a) e^{ax} + C", "a e^{ax} + C", "(1/a) e^{ax} + C"],
        "D", "easy", "factual",
        "∫ e^{ax} dx = (1/a) e^{ax} + C.",
        "∫ e^{ax} dx = (1/a) e^{ax} + C।",
    ),
    q(
        "∫ sec² x dx equals:",
        "∫ sec² x dx এর মান কত?",
        ["tan x + C", "−tan x + C", "sec x tan x + C", "cot x + C"],
        ["tan x + C", "−tan x + C", "sec x tan x + C", "cot x + C"],
        "A", "easy", "factual",
        "Derivative of tan x is sec² x, so the integral is tan x + C.",
        "tan x এর অন্তরজ sec² x; সুতরাং যোগজ tan x + C।",
    ),
    q(
        "∫ dx/(1 + x²) equals:",
        "∫ dx/(1 + x²) এর মান কত?",
        ["ln|1 + x²| + C", "tan⁻¹ x + C", "sin⁻¹ x + C", "1/(2x) + C"],
        ["ln|1 + x²| + C", "tan⁻¹ x + C", "sin⁻¹ x + C", "1/(2x) + C"],
        "B", "easy", "factual",
        "Standard form: ∫ dx/(1 + x²) = tan⁻¹ x + C.",
        "প্রামাণিক সূত্র: ∫ dx/(1 + x²) = tan⁻¹ x + C।",
    ),
    q(
        "∫ (1/x) dx equals (x ≠ 0):",
        "∫ (1/x) dx এর মান কত? (x ≠ 0)",
        ["x + C", "1/x² + C", "ln|x| + C", "eˣ + C"],
        ["x + C", "1/x² + C", "ln|x| + C", "eˣ + C"],
        "C", "easy", "factual",
        "∫ x⁻¹ dx = ln|x| + C.",
        "∫ x⁻¹ dx = ln|x| + C।",
    ),
    q(
        "∫ xⁿ dx equals (n ≠ −1):",
        "∫ xⁿ dx এর মান কত? (n ≠ −1)",
        ["n xⁿ⁻¹ + C", "xⁿ⁺¹/(n + 1) + C", "xⁿ⁺¹/n + C", "n xⁿ⁺¹ + C"],
        ["n xⁿ⁻¹ + C", "xⁿ⁺¹/(n + 1) + C", "xⁿ⁺¹/n + C", "n xⁿ⁺¹ + C"],
        "B", "easy", "factual",
        "Power rule of integration: ∫ xⁿ dx = xⁿ⁺¹/(n + 1) + C.",
        "ঘাত সূত্র: ∫ xⁿ dx = xⁿ⁺¹/(n + 1) + C।",
    ),
    q(
        "∫ [(1 − sin x)/(1 + sin x)] dx equals:",
        "∫ [(1 − sin x)/(1 + sin x)] dx এর মান কত?",
        ["(tan x − sec x) + C", "(sec x − tan x) + C", "(tan x + sec x) + C", "−(tan x + sec x) + C"],
        ["(tan x − sec x) + C", "(sec x − tan x) + C", "(tan x + sec x) + C", "−(tan x + sec x) + C"],
        "A", "hard", "numerical",
        "Multiply by (1 − sin x): integrand → sec² x − sec x tan x ⇒ tan x − sec x + C.",
        "সরলীকরণে sec² x − sec x tan x পাওয়া যায় ⇒ tan x − sec x + C।",
    ),
    q(
        "∫ cos²(3x) dx equals:",
        "∫ cos²(3x) dx এর মান কত?",
        ["(1/6)(x + sin 6x) + C", "(1/2)(x − sin 6x) + C", "(1/12)(6x + sin 6x) + C", "(1/4)(6x − sin 6x) + C"],
        ["(1/6)(x + sin 6x) + C", "(1/2)(x − sin 6x) + C", "(1/12)(6x + sin 6x) + C", "(1/4)(6x − sin 6x) + C"],
        "C", "medium", "numerical",
        "cos² 3x = (1 + cos 6x)/2 ⇒ ∫ = x/2 + (sin 6x)/12 = (6x + sin 6x)/12 + C.",
        "cos² 3x = (1 + cos 6x)/2 ব্যবহার করে মান (6x + sin 6x)/12 + C।",
    ),
    q(
        "∫ eˣ {sin 3x + 3 cos 3x} dx equals:",
        "∫ eˣ {sin 3x + 3 cos 3x} dx এর মান কত?",
        ["3 eˣ sin 3x + C", "eˣ sin 3x + C", "3 eˣ cos 3x + C", "eˣ cos 3x + C"],
        ["3 eˣ sin 3x + C", "eˣ sin 3x + C", "3 eˣ cos 3x + C", "eˣ cos 3x + C"],
        "B", "medium", "numerical",
        "With f = sin 3x, f' = 3 cos 3x: ∫ eˣ(f + f') dx = eˣ sin 3x + C.",
        "f = sin 3x, f' = 3 cos 3x ⇒ eˣ sin 3x + C।",
    ),
    q(
        "∫ dx/√(a² − x²) equals:",
        "∫ dx/√(a² − x²) এর মান কত?",
        ["ln|x + √(a² − x²)| + C", "sin⁻¹(x/a) + C", "tan⁻¹(x/a) + C", "sec⁻¹(x/a) + C"],
        ["ln|x + √(a² − x²)| + C", "sin⁻¹(x/a) + C", "tan⁻¹(x/a) + C", "sec⁻¹(x/a) + C"],
        "B", "easy", "factual",
        "Standard form: ∫ dx/√(a² − x²) = sin⁻¹(x/a) + C.",
        "প্রামাণিক সূত্র: ∫ dx/√(a² − x²) = sin⁻¹(x/a) + C।",
    ),
    q(
        "∫ √(a² − x²) dx equals:",
        "∫ √(a² − x²) dx এর মান কত?",
        [
            "(x/2)√(a² − x²) + (a²/2) sin⁻¹(x/a) + C",
            "(x/2)√(a² − x²) − (a²/2) sin⁻¹(x/a) + C",
            "√(a² − x²) + C",
            "(a²/2) cos⁻¹(x/a) + C",
        ],
        [
            "(x/2)√(a² − x²) + (a²/2) sin⁻¹(x/a) + C",
            "(x/2)√(a² − x²) − (a²/2) sin⁻¹(x/a) + C",
            "√(a² − x²) + C",
            "(a²/2) cos⁻¹(x/a) + C",
        ],
        "A", "hard", "factual",
        "Standard form for ∫ √(a² − x²) dx uses trig substitution / circle identity.",
        "প্রামাণিক সূত্র: (x/2)√(a² − x²) + (a²/2) sin⁻¹(x/a) + C।",
    ),
]


# =============================================================================
# hm1_27_ch10_t02 — Methods of integration / যোগজীকরণের পদ্ধতি
# =============================================================================
T02 = [
    q(
        "∫ sin² x cos x dx equals:",
        "∫ sin² x cos x dx এর মান কত?",
        ["(1/3) sin³ x + C", "(1/2) sin² x + C", "−(1/3) cos³ x + C", "sin³ x cos x + C"],
        ["(1/3) sin³ x + C", "(1/2) sin² x + C", "−(1/3) cos³ x + C", "sin³ x cos x + C"],
        "A", "easy", "numerical",
        "Let z = sin x ⇒ dz = cos x dx ⇒ ∫ z² dz = z³/3 + C.",
        "z = sin x ধরে ∫ z² dz = z³/3 + C।",
    ),
    q(
        "∫ x sec² x dx equals:",
        "∫ x sec² x dx এর মান কত?",
        ["x tan x + ln|sin x| + C", "x tan x − ln|sin x| + C", "x tan x + ln|cos x| + C", "x tan x − ln|cos x| + C"],
        ["x tan x + ln|sin x| + C", "x tan x − ln|sin x| + C", "x tan x + ln|cos x| + C", "x tan x − ln|cos x| + C"],
        "C", "hard", "numerical",
        "By parts: u = x, dv = sec² x dx ⇒ x tan x − ∫ tan x dx = x tan x + ln|cos x| + C.",
        "অংশযোগ: x tan x − ∫ tan x dx = x tan x + ln|cos x| + C।",
    ),
    q(
        "If ∫ x dx/√(1 − x²) = f(x) + C, then f(x) equals:",
        "যদি ∫ x dx/√(1 − x²) = f(x) + C হয়, তবে f(x) = কত?",
        ["sin⁻¹ x", "cos⁻¹ x", "ln √(1 − x²)", "−√(1 − x²)"],
        ["sin⁻¹ x", "cos⁻¹ x", "ln √(1 − x²)", "−√(1 − x²)"],
        "D", "medium", "numerical",
        "u = 1 − x² ⇒ du = −2x dx ⇒ ∫ = −√(1 − x²) + C.",
        "u = 1 − x² ধরে f(x) = −√(1 − x²)।",
    ),
    q(
        "∫ eˣ (ln x + 1/x) dx equals:",
        "∫ eˣ (ln x + 1/x) dx এর মান কত?",
        ["eˣ ln x + C", "eˣ / x + C", "ln x + C", "eˣ + ln x + C"],
        ["eˣ ln x + C", "eˣ / x + C", "ln x + C", "eˣ + ln x + C"],
        "A", "medium", "numerical",
        "∫ eˣ {f + f'} dx = eˣ f + C with f = ln x.",
        "f = ln x নিয়ে eˣ ln x + C।",
    ),
    q(
        "∫ (cos x)/√(sin x) dx equals:",
        "∫ (cos x)/√(sin x) dx এর মান কত?",
        ["sec x + C", "√(tan x) + C", "2 √(sin x) + C", "√(sin x) + C"],
        ["sec x + C", "√(tan x) + C", "2 √(sin x) + C", "√(sin x) + C"],
        "C", "easy", "numerical",
        "z = sin x ⇒ dz = cos x dx ⇒ ∫ z^{−1/2} dz = 2√z + C = 2√(sin x) + C.",
        "z = sin x ধরে 2√(sin x) + C।",
    ),
    q(
        "∫ tan² x sec² x dx equals:",
        "∫ tan² x sec² x dx এর মান কত?",
        ["(1/3) tan³ x + C", "(1/2) tan² x + C", "tan x + C", "sec³ x + C"],
        ["(1/3) tan³ x + C", "(1/2) tan² x + C", "tan x + C", "sec³ x + C"],
        "A", "easy", "numerical",
        "z = tan x ⇒ dz = sec² x dx ⇒ ∫ z² dz = z³/3 + C.",
        "z = tan x ধরে ∫ z² dz = z³/3 + C।",
    ),
    q(
        "∫ x eˣ dx equals:",
        "∫ x eˣ dx এর মান কত?",
        ["eˣ + C", "x eˣ + C", "eˣ (x − 1) + C", "eˣ (x + 1) + C"],
        ["eˣ + C", "x eˣ + C", "eˣ (x − 1) + C", "eˣ (x + 1) + C"],
        "C", "medium", "numerical",
        "Integration by parts: u = x, dv = eˣ dx ⇒ x eˣ − ∫ eˣ dx = eˣ(x − 1) + C.",
        "অংশযোগে eˣ(x − 1) + C।",
    ),
    q(
        "∫ sin(10 − x/5) dx equals:",
        "∫ sin(10 − x/5) dx এর মান কত?",
        ["5 cos(10 − x/5) + C", "−5 cos(10 − x/5) + C", "−(1/5) cos(10 − x/5) + C", "(1/5) cos(10 − x/5) + C"],
        ["5 cos(10 − x/5) + C", "−5 cos(10 − x/5) + C", "−(1/5) cos(10 − x/5) + C", "(1/5) cos(10 − x/5) + C"],
        "A", "medium", "numerical",
        "y = 10 − x/5 ⇒ dx = −5 dy ⇒ ∫ sin y (−5 dy) = 5 cos y + C.",
        "y = 10 − x/5 ধরে 5 cos(10 − x/5) + C।",
    ),
    q(
        "∫ (sec² x)/√(tan x) dx equals:",
        "∫ (sec² x)/√(tan x) dx এর মান কত?",
        ["√(tan x) + C", "2 √(tan x) + C", "(1/2) √(tan x) + C", "tan x + C"],
        ["√(tan x) + C", "2 √(tan x) + C", "(1/2) √(tan x) + C", "tan x + C"],
        "B", "easy", "numerical",
        "z = tan x ⇒ ∫ z^{−1/2} dz = 2√z + C = 2√(tan x) + C.",
        "z = tan x ধরে 2√(tan x) + C।",
    ),
    q(
        "∫ cos x · e^{sin x} dx equals:",
        "∫ cos x · e^{sin x} dx এর মান কত?",
        ["e^{cos x} + C", "e^{sin x} + C", "sin x · e^{sin x} + C", "−e^{sin x} + C"],
        ["e^{cos x} + C", "e^{sin x} + C", "sin x · e^{sin x} + C", "−e^{sin x} + C"],
        "B", "easy", "numerical",
        "z = sin x ⇒ dz = cos x dx ⇒ ∫ e^z dz = e^{sin x} + C.",
        "z = sin x ধরে e^{sin x} + C।",
    ),
    q(
        "∫ (1 + tan² x)/(1 − tan x) dx equals:",
        "∫ (1 + tan² x)/(1 − tan x) dx এর মান কত?",
        ["−ln|1 − tan x| + C", "ln|1 − tan x| + C", "1 − tan x + C", "tan x + C"],
        ["−ln|1 − tan x| + C", "ln|1 − tan x| + C", "1 − tan x + C", "tan x + C"],
        "A", "hard", "numerical",
        "1 + tan² x = sec² x; u = 1 − tan x ⇒ du = −sec² x dx ⇒ −ln|u| + C.",
        "u = 1 − tan x ⇒ −ln|1 − tan x| + C।",
    ),
    q(
        "∫ xⁿ ln x dx is found primarily by which method?",
        "∫ xⁿ ln x dx মূলত কোন পদ্ধতিতে নির্ণয় করা যায়?",
        ["partial fractions only", "integration by parts", "direct formula without parts", "only trig substitution"],
        ["শুধু আংশিক ভগ্নাংশ", "অংশযোগ (by parts)", "অংশযোগ ছাড়াই সরাসরি সূত্র", "শুধু ত্রিকোণমিতিক প্রতিস্থাপন"],
        "B", "easy", "conceptual",
        "Take u = ln x, dv = xⁿ dx (n ≠ −1) and integrate by parts.",
        "u = ln x, dv = xⁿ dx নিয়ে অংশযোগ করা হয়।",
    ),
    q(
        "To evaluate ∫ dx/(x² − a²), the preferred algebraic method is:",
        "∫ dx/(x² − a²) নির্ণয়ে পছন্দনীয় বীজগাণিতিক পদ্ধতি কোনটি?",
        ["integration by parts", "partial fractions / standard log form", "only double-angle identities", "reduction to tan⁻¹ only"],
        ["অংশযোগ", "আংশিক ভগ্নাংশ / প্রামাণিক লগ সূত্র", "শুধু দ্বিগুণ কোণ সূত্র", "শুধু tan⁻¹ এ রূপান্তর"],
        "B", "medium", "conceptual",
        "∫ dx/(x² − a²) = (1/(2a)) ln|(x − a)/(x + a)| + C via partial fractions.",
        "আংশিক ভগ্নাংশে (1/(2a)) ln|(x − a)/(x + a)| + C।",
    ),
    q(
        "∫ (2x + 3)/(x² + 3x + 2) dx equals:",
        "∫ (2x + 3)/(x² + 3x + 2) dx এর মান কত?",
        ["ln|x² + 3x + 2| + C", "2 ln|x² + 3x + 2| + C", "tan⁻¹(x + 3/2) + C", "(2x + 3)²/2 + C"],
        ["ln|x² + 3x + 2| + C", "2 ln|x² + 3x + 2| + C", "tan⁻¹(x + 3/2) + C", "(2x + 3)²/2 + C"],
        "A", "medium", "numerical",
        "d/dx(x² + 3x + 2) = 2x + 3 ⇒ integral = ln|x² + 3x + 2| + C.",
        "হরের অন্তরজ = লব ⇒ ln|x² + 3x + 2| + C।",
    ),
    q(
        "∫ sin⁶ θ cos θ dθ equals:",
        "∫ sin⁶ θ cos θ dθ এর মান কত?",
        ["(1/7) sin⁷ θ + C", "(1/6) sin⁶ θ + C", "−(1/7) cos⁷ θ + C", "sin⁷ θ cos θ + C"],
        ["(1/7) sin⁷ θ + C", "(1/6) sin⁶ θ + C", "−(1/7) cos⁷ θ + C", "sin⁷ θ cos θ + C"],
        "A", "easy", "numerical",
        "z = sin θ ⇒ ∫ z⁶ dz = z⁷/7 + C.",
        "z = sin θ ধরে z⁷/7 + C।",
    ),
    q(
        "∫ (tan⁻¹ x)/(1 + x²) dx equals:",
        "∫ (tan⁻¹ x)/(1 + x²) dx এর মান কত?",
        ["tan⁻¹ x + C", "(1/2)(tan⁻¹ x)² + C", "ln|1 + x²| + C", "x tan⁻¹ x + C"],
        ["tan⁻¹ x + C", "(1/2)(tan⁻¹ x)² + C", "ln|1 + x²| + C", "x tan⁻¹ x + C"],
        "B", "medium", "numerical",
        "z = tan⁻¹ x ⇒ dz = dx/(1 + x²) ⇒ ∫ z dz = z²/2 + C.",
        "z = tan⁻¹ x ধরে (1/2)(tan⁻¹ x)² + C।",
    ),
    q(
        "∫ (ln x)/x dx equals:",
        "∫ (ln x)/x dx এর মান কত?",
        ["ln|ln x| + C", "(1/2)(ln x)² + C", "1/x + C", "x ln x + C"],
        ["ln|ln x| + C", "(1/2)(ln x)² + C", "1/x + C", "x ln x + C"],
        "B", "easy", "numerical",
        "z = ln x ⇒ dz = dx/x ⇒ ∫ z dz = z²/2 + C.",
        "z = ln x ধরে (1/2)(ln x)² + C।",
    ),
    q(
        "∫ x^{−3/2} dx equals:",
        "∫ x^{−3/2} dx এর মান কত?",
        ["−2 x^{−1/2} + C", "2 √x + C", "−√x + C", "ln|√x| + C"],
        ["−2 x^{−1/2} + C", "2 √x + C", "−√x + C", "ln|√x| + C"],
        "A", "medium", "numerical",
        "∫ x^{−3/2} dx = x^{−1/2}/(−1/2) = −2/√x + C.",
        "∫ x^{−3/2} dx = −2/√x + C।",
    ),
    q(
        "∫ ln(2x) dx equals:",
        "∫ ln(2x) dx এর মান কত?",
        ["x ln|2x| + C", "x(ln|2x| − 1) + C", "2x ln|2x| + C", "(ln|2x|)/x + C"],
        ["x ln|2x| + C", "x(ln|2x| − 1) + C", "2x ln|2x| + C", "(ln|2x|)/x + C"],
        "B", "medium", "numerical",
        "By parts: ∫ ln(2x) dx = x ln|2x| − ∫ x·(1/x) dx = x(ln|2x| − 1) + C.",
        "অংশযোগে x(ln|2x| − 1) + C।",
    ),
    q(
        "∫ cot x csc x dx equals:",
        "∫ cot x csc x dx এর মান কত?",
        ["csc x + C", "−csc x + C", "sec x + C", "−sec x + C"],
        ["csc x + C", "−csc x + C", "sec x + C", "−sec x + C"],
        "B", "easy", "numerical",
        "d/dx(csc x) = −csc x cot x ⇒ ∫ cot x csc x dx = −csc x + C.",
        "csc x এর অন্তরজ −csc x cot x ⇒ যোগজ −csc x + C।",
    ),
]


# =============================================================================
# hm1_27_ch10_t03 — Definite integrals and applications / নির্দিষ্ট যোগজ ও প্রয়োগ
# =============================================================================
T03 = [
    q(
        "The area bounded by y = 2x − x² and the x-axis equals:",
        "y = 2x − x² বক্ররেখা এবং x-অক্ষ দ্বারা সীমাবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত?",
        ["0 square units", "2/3 square units", "4/3 square units", "2 square units"],
        ["0 বর্গ একক", "2/3 বর্গ একক", "4/3 বর্গ একক", "2 বর্গ একক"],
        "C", "medium", "application",
        "Roots x = 0, 2: ∫_0² (2x − x²) dx = [x² − x³/3]_0² = 4 − 8/3 = 4/3.",
        "ছেদবিন্দু 0, 2; ∫_0² (2x − x²) dx = 4/3।",
    ),
    q(
        "The area bounded by y = −√(4 − x²) and y = 0 equals:",
        "y = −√(4 − x²) এবং y = 0 দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল কোনটি?",
        ["4π", "2π", "π", "π/2"],
        ["4π", "2π", "π", "π/2"],
        "B", "medium", "application",
        "Lower semicircle of radius 2: area = (1/2)π·2² = 2π.",
        "ব্যাসার্ধ 2 এর নিম্ন অর্ধবৃত্ত; ক্ষেত্রফল 2π।",
    ),
    q(
        "∫_2^4 ln x dx equals:",
        "∫_2^4 ln x dx এর মান কত?",
        ["6 ln 2 − 2", "2 − 6 ln 2", "2 + 6 ln 2", "4 ln 2 − 2"],
        ["6 ln 2 − 2", "2 − 6 ln 2", "2 + 6 ln 2", "4 ln 2 − 2"],
        "A", "medium", "numerical",
        "[x ln x − x]_2^4 = (4 ln 4 − 4) − (2 ln 2 − 2) = 6 ln 2 − 2.",
        "[x ln x − x]_2^4 = 6 ln 2 − 2।",
    ),
    q(
        "∫_0^{π/2} cos x dx equals:",
        "∫_0^{π/2} cos x dx এর মান কত?",
        ["0", "1", "−1", "2"],
        ["0", "1", "−1", "2"],
        "B", "easy", "numerical",
        "[sin x]_0^{π/2} = 1 − 0 = 1.",
        "[sin x]_0^{π/2} = 1।",
    ),
    q(
        "∫_0^{π/4} sec θ dθ equals:",
        "∫_0^{π/4} sec θ dθ এর মান কোনটি?",
        ["ln 2", "(1/2) ln(√2 + 1)", "ln(√2 + 1)", "ln(√2 − 1)"],
        ["ln 2", "(1/2) ln(√2 + 1)", "ln(√2 + 1)", "ln(√2 − 1)"],
        "C", "medium", "numerical",
        "[ln|sec θ + tan θ|]_0^{π/4} = ln(√2 + 1) − ln 1 = ln(√2 + 1).",
        "[ln|sec θ + tan θ|]_0^{π/4} = ln(√2 + 1)।",
    ),
    q(
        "The area enclosed by the ellipse 5x² + 20y² = 100 equals:",
        "5x² + 20y² = 100 উপবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত বর্গ একক?",
        ["10", "100", "10π", "100π"],
        ["10", "100", "10π", "100π"],
        "C", "medium", "application",
        "x²/20 + y²/5 = 1 ⇒ a = √20, b = √5 ⇒ area = πab = 10π.",
        "x²/20 + y²/5 = 1 ⇒ ক্ষেত্রফল πab = 10π।",
    ),
    q(
        "∫_0^1 dx/(1 + x) equals:",
        "∫_0^1 dx/(1 + x) এর মান কত?",
        ["1 − ln 2", "ln 2", "ln 2 − 1", "−ln 2"],
        ["1 − ln 2", "ln 2", "ln 2 − 1", "−ln 2"],
        "B", "easy", "numerical",
        "[ln|1 + x|]_0^1 = ln 2 − ln 1 = ln 2.",
        "[ln|1 + x|]_0^1 = ln 2।",
    ),
    q(
        "The area bounded by y = 5x, the y-axis and the line x = 4 equals:",
        "y = 5x, y-অক্ষ এবং x = 4 সরলরেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত বর্গ একক?",
        ["10", "20", "40", "80"],
        ["10", "20", "40", "80"],
        "C", "easy", "application",
        "∫_0^4 5x dx = (5/2)x²|_0^4 = 40.",
        "∫_0^4 5x dx = 40।",
    ),
    q(
        "∫_1^e (1/x) dx equals:",
        "∫_1^e (1/x) dx এর মান কত?",
        ["0", "1", "e", "e − 1"],
        ["0", "1", "e", "e − 1"],
        "B", "easy", "numerical",
        "[ln|x|]_1^e = 1 − 0 = 1.",
        "[ln|x|]_1^e = 1।",
    ),
    q(
        "The area enclosed by the circle x² + y² = 1 equals:",
        "x² + y² = 1 বৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত?",
        ["1/2", "1", "π", "π/2"],
        ["1/2", "1", "π", "π/2"],
        "C", "easy", "application",
        "Unit circle area = π(1)² = π.",
        "একক বৃত্তের ক্ষেত্রফল π।",
    ),
    q(
        "If ∫_2^5 f(x) dx = 4, then ∫_4^7 f(x − 2) dx equals:",
        "যদি ∫_2^5 f(x) dx = 4 হয়, তবে ∫_4^7 f(x − 2) dx = কত?",
        ["0", "4", "3", "2"],
        ["0", "4", "3", "2"],
        "B", "medium", "conceptual",
        "Substitute z = x − 2: limits 2→5 map to 4→7 ⇒ same integral value 4.",
        "z = x − 2 প্রতিস্থাপনে সীমা অপরিবর্তিত; মান 4।",
    ),
    q(
        "The area bounded by the parabola x = 4 − y² and the y-axis equals:",
        "x = 4 − y² পরাবৃত্ত এবং y-অক্ষ দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত?",
        ["4/3 square units", "8/3 square units", "16/3 square units", "32/3 square units"],
        ["4/3 বর্গ একক", "8/3 বর্গ একক", "16/3 বর্গ একক", "32/3 বর্গ একক"],
        "D", "hard", "application",
        "y from −2 to 2: 2∫_0^2 (4 − y²) dy = 2[4y − y³/3]_0^2 = 32/3.",
        "∫_{-2}^2 (4 − y²) dy = 32/3।",
    ),
    q(
        "∫_0^{π/2} √(1 + cos x) dx equals:",
        "∫_0^{π/2} √(1 + cos x) dx এর মান কত?",
        ["−1", "1", "√2", "2√2"],
        ["−1", "1", "√2", "2√2"],
        "D", "hard", "numerical",
        "1 + cos x = 2 cos²(x/2) ⇒ ∫_0^{π/2} √2 cos(x/2) dx = 2√2 [sin(x/2)]_0^{π/2} = 2√2.",
        "√(1 + cos x) = √2 |cos(x/2)| ⇒ মান 2√2।",
    ),
    q(
        "∫_0^1 4/(1 + x²) dx equals:",
        "∫_0^1 4/(1 + x²) dx এর মান কত?",
        ["4 ln 2", "π", "π/2", "1"],
        ["4 ln 2", "π", "π/2", "1"],
        "B", "medium", "numerical",
        "4[tan⁻¹ x]_0^1 = 4(π/4 − 0) = π.",
        "4[tan⁻¹ x]_0^1 = π।",
    ),
    q(
        "∫_0^1 [(1 − x)/(1 + x)] dx equals:",
        "∫_0^1 [(1 − x)/(1 + x)] dx এর মান কোনটি?",
        ["2 ln 2 + 1", "2 ln 2 − 1", "ln 2 + 1", "ln 2 − 2"],
        ["2 ln 2 + 1", "2 ln 2 − 1", "ln 2 + 1", "ln 2 − 2"],
        "B", "hard", "numerical",
        "(1 − x)/(1 + x) = −1 + 2/(1 + x) ⇒ [−x + 2 ln|1 + x|]_0^1 = 2 ln 2 − 1.",
        "সরলীকরণে 2 ln 2 − 1।",
    ),
    q(
        "∫_0^{π/4} cos²(2x) dx equals:",
        "∫_0^{π/4} cos²(2x) dx এর মান কত?",
        ["π/8", "π/4", "π/16", "1/2"],
        ["π/8", "π/4", "π/16", "1/2"],
        "A", "medium", "numerical",
        "cos² 2x = (1 + cos 4x)/2 ⇒ (1/2)[x + (sin 4x)/4]_0^{π/4} = π/8.",
        "(1 + cos 4x)/2 ব্যবহার করে মান π/8।",
    ),
    q(
        "∫_0^1 e^{√x}/√x dx equals:",
        "∫_0^1 e^{√x}/√x dx এর মান কোনটি?",
        ["2(e − 1)", "2(1 − e)", "e − 1", "1 − 1/e"],
        ["2(e − 1)", "2(1 − e)", "e − 1", "1 − 1/e"],
        "A", "hard", "numerical",
        "z = √x ⇒ dx/√x = 2 dz ⇒ ∫_0^1 2 e^z dz = 2(e − 1).",
        "z = √x ধরে 2(e − 1)।",
    ),
    q(
        "∫_0^{π/4} √(1 + sin 2x) dx equals:",
        "∫_0^{π/4} √(1 + sin 2x) dx এর মান কত?",
        ["−2", "0", "1", "√2"],
        ["−2", "0", "1", "√2"],
        "C", "hard", "numerical",
        "√(1 + sin 2x) = |sin x + cos x|; on [0, π/4] = sin x + cos x ⇒ [sin x − cos x]_0^{π/4} = 1.",
        "[sin x − cos x]_0^{π/4} = 1।",
    ),
    q(
        "The shaded area between y = x and y = x² from their intersection points equals:",
        "y = x এবং y = x² এর ছেদবিন্দুদ্বয়ের মধ্যে ছায়াঙ্কিত ক্ষেত্রের ক্ষেত্রফল কত বর্গ একক?",
        ["1/6", "1/3", "1/2", "1"],
        ["1/6", "1/3", "1/2", "1"],
        "A", "medium", "application",
        "Intersect at 0, 1: ∫_0^1 (x − x²) dx = [x²/2 − x³/3]_0^1 = 1/6.",
        "∫_0^1 (x − x²) dx = 1/6।",
    ),
    q(
        "∫_0^3 (1 + x²) dx equals:",
        "∫_0^3 (1 + x²) dx এর মান কত?",
        ["6", "9", "10", "12"],
        ["6", "9", "10", "12"],
        "D", "easy", "numerical",
        "[x + x³/3]_0^3 = 3 + 9 = 12.",
        "[x + x³/3]_0^3 = 12।",
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
    counts["hm1_27_ch10_t01"] = write_topic("hm1_27_ch10_t01", T01)["count"]
    counts["hm1_27_ch10_t02"] = write_topic("hm1_27_ch10_t02", T02)["count"]
    counts["hm1_27_ch10_t03"] = write_topic("hm1_27_ch10_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm1_27_ch10",
        "title_en": "Integration",
        "title_bn": "যোগজীকরণ",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(329, 344)],
        "topics": {
            "hm1_27_ch10_t01": {
                "title_en": "Indefinite integrals",
                "title_bn": "অনির্দিষ্ট যোগজ",
                "udvash_types": [
                    "standard indefinite forms",
                    "trig/exp/log integrals",
                    "e^x(f+f') formula",
                    "inverse trig forms",
                ],
                "count": 20,
            },
            "hm1_27_ch10_t02": {
                "title_en": "Methods of integration",
                "title_bn": "যোগজীকরণের পদ্ধতি",
                "udvash_types": [
                    "substitution",
                    "integration by parts",
                    "partial fractions",
                    "trig identities",
                ],
                "count": 20,
            },
            "hm1_27_ch10_t03": {
                "title_en": "Definite integrals and applications",
                "title_bn": "নির্দিষ্ট যোগজ ও প্রয়োগ",
                "udvash_types": [
                    "definite evaluation",
                    "area under curves",
                    "ellipse/circle/parabola area",
                    "definite-integral properties",
                ],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "figure_only_sketches": "Printed shaded-region diagrams rewritten as text-describable area MCQs",
            "garbled_integral_stems": "Many ∫ stems OCR-unreadable; reconstructed from solution lines and standard board forms",
            "stimulus_pairs": "Linked stimulus blocks curated as standalone clear stems",
            "noisy_option_glyphs": "Broken fraction/option glyphs replaced with closed-form HSC standards",
        },
        "low_confidence": [
            "OCR on pp. 329–343 heavily noisy; column PNGs/answer keys used to reconstruct stems.",
            "Inline math stored as plain text (sqrt, ^, pi, ln/e, ^{ }) for JSONL.",
            "Some printed definite limits inconsistent in OCR; closed-form board standards retained.",
            "Area-of-region figure items rewritten without relying on diagram OCR.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm1_ch10.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
        "math1_completion": {
            "topics_complete": "30/30",
            "note": "Ch10 finishes higher_mathematics 1st paper question bank curation",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch10_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
