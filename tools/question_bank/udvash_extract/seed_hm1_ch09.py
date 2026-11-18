#!/usr/bin/env python3
"""Seed Higher Mathematics 1st Paper Ch9 (Differentiation).

Curated from Udvash HSC Question Bank 2026 printed pp. 287–299 (PDF 293–305).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
OCR is heavily noisy (~13 pages); reconstructs board-style items from solutions/
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
    "higher_mathematics p1 ch09; curated bilingual"
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
# hm1_27_ch09_t01 — Limits and continuity / সীমা ও অবিচ্ছিন্নতা
# =============================================================================
T01 = [
    q(
        "lim (x→0) (sin x)/x equals:",
        "lim (x→0) (sin x)/x এর মান কত?",
        ["0", "1", "∞", "does not exist"],
        ["0", "1", "∞", "অস্তিত্ব নেই"],
        "B", "easy", "factual",
        "Standard limit: lim (x→0) (sin x)/x = 1.",
        "প্রামাণিক সীমা: lim (x→0) (sin x)/x = 1।",
    ),
    q(
        "lim (x→0) (1 − cos x)/x^2 equals:",
        "lim (x→0) (1 − cos x)/x² এর মান কত?",
        ["0", "1", "1/2", "2"],
        ["0", "1", "1/2", "2"],
        "C", "medium", "numerical",
        "Use 1 − cos x = 2 sin²(x/2): lim = lim 2 sin²(x/2)/x² = lim (1/2)[sin(x/2)/(x/2)]² = 1/2.",
        "1 − cos x = 2 sin²(x/2) ব্যবহার করে সীমা 1/2 পাওয়া যায়।",
    ),
    q(
        "lim (x→0) (tan^{-1} 2x)/(3x) equals:",
        "lim (x→0) (tan⁻¹ 2x)/(3x) এর মান কত?",
        ["0", "2/3", "3/2", "1"],
        ["0", "2/3", "3/2", "1"],
        "B", "medium", "numerical",
        "lim (tan^{-1} u)/u = 1 with u = 2x ⇒ lim (tan^{-1} 2x)/(2x) · (2/3) = 2/3.",
        "u = 2x নিয়ে lim (tan⁻¹ u)/u = 1 ⇒ মান 2/3।",
    ),
    q(
        "lim (x→0) (sin 2x)/(x cos 3x) equals:",
        "lim (x→0) (sin 2x)/(x cos 3x) এর মান কত?",
        ["0", "1", "2", "3"],
        ["0", "1", "2", "3"],
        "C", "medium", "numerical",
        "Rewrite as 2 · (sin 2x)/(2x) · 1/cos 3x → 2 · 1 · 1 = 2 as x → 0.",
        "2 · (sin 2x)/(2x) · 1/cos 3x → 2 · 1 · 1 = 2।",
    ),
    q(
        "lim (x→0) (e^x − 1)/x equals:",
        "lim (x→0) (eˣ − 1)/x এর মান কত?",
        ["0", "1", "e", "∞"],
        ["0", "1", "e", "∞"],
        "B", "easy", "factual",
        "Standard exponential limit: lim (x→0) (e^x − 1)/x = 1.",
        "প্রামাণিক সীমা: lim (x→0) (eˣ − 1)/x = 1।",
    ),
    q(
        "lim (x→0) (1 + 2x)^{1/(2x)} equals:",
        "lim (x→0) (1 + 2x)^{1/(2x)} এর মান কত?",
        ["0", "1", "e", "e^2"],
        ["0", "1", "e", "e^2"],
        "C", "medium", "numerical",
        "lim (1 + u)^{1/u} = e with u = 2x → e.",
        "u = 2x নিয়ে lim (1 + u)^{1/u} = e।",
    ),
    q(
        "lim (x→0) (sin x)/sin(2x) equals:",
        "lim (x→0) (sin x)/sin(2x) এর মান কত?",
        ["0", "1/2", "1", "2"],
        ["0", "1/2", "1", "2"],
        "B", "easy", "numerical",
        "(sin x)/sin(2x) = (sin x)/x · x/(2x) · 2x/sin(2x) · 1/1 → 1 · (1/2) · 1 = 1/2.",
        "প্রামাণিক sin-সীমা ব্যবহার করে মান 1/2।",
    ),
    q(
        "lim (x→0) [2 ln(1 + x) − ln(1 − x)] equals:",
        "lim (x→0) [2 ln(1 + x) − ln(1 − x)] এর মান কত?",
        ["0", "1", "2", "∞"],
        ["0", "1", "2", "∞"],
        "A", "medium", "numerical",
        "Expression → 2 ln 1 − ln 1 = 0 − 0 = 0 (or rewrite as ln[(1+x)²/(1−x)] → ln 1 = 0).",
        "ln[(1+x)²/(1−x)] → ln 1 = 0।",
    ),
    q(
        "lim (x→∞) x / √(x² + 3x + 4) equals:",
        "lim (x→∞) x / √(x² + 3x + 4) এর মান কত?",
        ["−1", "0", "1", "∞"],
        ["−1", "0", "1", "∞"],
        "C", "medium", "numerical",
        "Divide by |x|: for x → +∞, get 1/√(1 + 3/x + 4/x²) → 1.",
        "x → +∞ এ |x| দিয়ে ভাগ করলে 1/√(1 + 3/x + 4/x²) → 1।",
    ),
    q(
        "lim (x→0) (a^x − 1)/x equals (a > 0, a ≠ 1):",
        "lim (x→0) (aˣ − 1)/x এর মান কত (a > 0, a ≠ 1)?",
        ["a", "1/a", "ln a", "a ln a"],
        ["a", "1/a", "ln a", "a ln a"],
        "C", "medium", "factual",
        "Standard limit: lim (x→0) (a^x − 1)/x = ln a.",
        "প্রামাণিক সীমা: lim (x→0) (aˣ − 1)/x = ln a।",
    ),
    q(
        "lim (x→0) (tan^{-1} x)/x equals:",
        "lim (x→0) (tan⁻¹ x)/x এর মান কত?",
        ["0", "1", "π/4", "∞"],
        ["0", "1", "π/4", "∞"],
        "B", "easy", "factual",
        "Standard inverse-tangent limit: lim (x→0) (tan^{-1} x)/x = 1.",
        "প্রামাণিক সীমা: lim (x→0) (tan⁻¹ x)/x = 1।",
    ),
    q(
        "A function f is continuous at x = b if and only if:",
        "x = b বিন্দুতে f অবিচ্ছিন্ন হবে যদি এবং কেবল যদি:",
        [
            "f(b) is undefined",
            "lim (x→b) f(x) does not exist",
            "lim (x→b) f(x) = f(b)",
            "f'(b) = 0",
        ],
        [
            "f(b) অসংজ্ঞাত",
            "lim (x→b) f(x) এর অস্তিত্ব নেই",
            "lim (x→b) f(x) = f(b)",
            "f'(b) = 0",
        ],
        "C", "easy", "conceptual",
        "Continuity at b requires the limit exists and equals the function value f(b).",
        "b-তে অবিচ্ছিন্নতার শর্ত: সীমার অস্তিত্ব এবং lim f(x) = f(b)।",
    ),
    q(
        "lim (x→3) (x³ − 27)/(x − 3) equals:",
        "lim (x→3) (x³ − 27)/(x − 3) এর মান কত?",
        ["0", "9", "27", "81"],
        ["0", "9", "27", "81"],
        "C", "easy", "numerical",
        "Factor: (x − 3)(x² + 3x + 9)/(x − 3) → 9 + 9 + 9 = 27.",
        "(x − 3)(x² + 3x + 9)/(x − 3) → 9 + 9 + 9 = 27।",
    ),
    q(
        "lim (x→0) (√(1 + x) − 1)/x equals:",
        "lim (x→0) (√(1 + x) − 1)/x এর মান কত?",
        ["0", "1/2", "1", "2"],
        ["0", "1/2", "1", "2"],
        "B", "medium", "numerical",
        "Rationalize: multiply by √(1+x)+1 → 1/(√(1+x)+1) → 1/2.",
        "√(1+x)+1 দিয়ে গুণ করে 1/(√(1+x)+1) → 1/2।",
    ),
    q(
        "lim (x→0) sin(mx)/sin(nx) equals (n ≠ 0):",
        "lim (x→0) sin(mx)/sin(nx) এর মান কত (n ≠ 0)?",
        ["0", "m/n", "n/m", "mn"],
        ["0", "m/n", "n/m", "mn"],
        "B", "medium", "numerical",
        "(sin mx)/(mx) · m/n · (nx)/sin(nx) → 1 · (m/n) · 1 = m/n.",
        "প্রামাণিক sin-সীমায় মান m/n।",
    ),
    q(
        "lim (x→0) (e^{ax} − 1)/x equals:",
        "lim (x→0) (e^{ax} − 1)/x এর মান কত?",
        ["0", "1", "a", "e^a"],
        ["0", "1", "a", "e^a"],
        "C", "easy", "numerical",
        "Write a · (e^{ax} − 1)/(ax) → a · 1 = a.",
        "a · (e^{ax} − 1)/(ax) → a · 1 = a।",
    ),
    q(
        "If lim (x→a) f(x) = L and lim (x→a) g(x) = M, then lim (x→a) [f(x) − g(x)] equals:",
        "lim (x→a) f(x) = L এবং lim (x→a) g(x) = M হলে lim (x→a) [f(x) − g(x)] = ?",
        ["L + M", "L − M", "LM", "L/M"],
        ["L + M", "L − M", "LM", "L/M"],
        "B", "easy", "conceptual",
        "Limit of a difference equals the difference of the limits when both exist.",
        "উভয় সীমা বিদ্যমান হলে পার্থক্যের সীমা = সীমার পার্থক্য।",
    ),
    q(
        "lim (x→0) (tan 3x)/x equals:",
        "lim (x→0) (tan 3x)/x এর মান কত?",
        ["0", "1", "3", "1/3"],
        ["0", "1", "3", "1/3"],
        "C", "easy", "numerical",
        "3 · (tan 3x)/(3x) → 3 · 1 = 3.",
        "3 · (tan 3x)/(3x) → 3 · 1 = 3।",
    ),
    q(
        "Which limit is infinite (tends to ∞)?",
        "কোনটি অসীম সীমা (∞-এর দিকে যায়)?",
        [
            "lim (x→0) (sin x)/x",
            "lim (x→0) (1 − cos x)/x²",
            "lim (x→0) 1/x²",
            "lim (x→0) (e^x − 1)/x",
        ],
        [
            "lim (x→0) (sin x)/x",
            "lim (x→0) (1 − cos x)/x²",
            "lim (x→0) 1/x²",
            "lim (x→0) (eˣ − 1)/x",
        ],
        "C", "easy", "conceptual",
        "As x → 0, 1/x² → +∞, while the other three limits are finite.",
        "x → 0 এ 1/x² → +∞; অন্য তিনটি সসীম সীমা।",
    ),
    q(
        "lim (x→0) [ln(1 − 3x)]/(3x) equals:",
        "lim (x→0) [ln(1 − 3x)]/(3x) এর মান কত?",
        ["−1", "0", "1", "3"],
        ["−1", "0", "1", "3"],
        "A", "hard", "numerical",
        "Let u = −3x: lim ln(1+u)/u · (−1) = 1 · (−1) = −1 "
        "[equivalently lim ln(1−3x)/(−3x) · (−1) = −1].",
        "u = −3x নিয়ে lim ln(1+u)/u = 1 ⇒ মান −1।",
    ),
]


# =============================================================================
# hm1_27_ch09_t02 — Rules of differentiation / অন্তরীকরণের সূত্র
# =============================================================================
T02 = [
    q(
        "d/dx (sin x) equals:",
        "d/dx (sin x) এর মান কোনটি?",
        ["−cos x", "cos x", "−sin x", "sec x"],
        ["−cos x", "cos x", "−sin x", "sec x"],
        "B", "easy", "factual",
        "Derivative of sine is cosine.",
        "sine-এর অন্তরজ cosine।",
    ),
    q(
        "d/dx (ln x) equals (x > 0):",
        "d/dx (ln x) এর মান কত (x > 0)?",
        ["x", "1/x", "ln x", "e^x"],
        ["x", "1/x", "ln x", "e^x"],
        "B", "easy", "factual",
        "d/dx (ln x) = 1/x for x > 0.",
        "x > 0 এর জন্য d/dx (ln x) = 1/x।",
    ),
    q(
        "d/dx (x e^x) equals:",
        "d/dx (x eˣ) এর মান কত?",
        ["e^x", "(1 + x) e^x", "x e^x", "(1 − x) e^x"],
        ["e^x", "(1 + x) e^x", "x e^x", "(1 − x) e^x"],
        "B", "easy", "numerical",
        "Product rule: 1 · e^x + x · e^x = (1 + x) e^x.",
        "গুণের সূত্র: eˣ + x eˣ = (1 + x) eˣ।",
    ),
    q(
        "d/dx (a^x) equals (a > 0):",
        "d/dx (aˣ) এর মান কত (a > 0)?",
        ["a^x", "a^x ln a", "x a^{x−1}", "ln a"],
        ["a^x", "a^x ln a", "x a^{x−1}", "ln a"],
        "B", "easy", "factual",
        "d/dx (a^x) = a^x ln a.",
        "d/dx (aˣ) = aˣ ln a।",
    ),
    q(
        "If y = sin 2x, then the n-th derivative y_n equals:",
        "y = sin 2x হলে n-তম অন্তরজ y_n = ?",
        [
            "2^n sin(nπ/2 − 2x)",
            "2^n sin(nπ/2 + 2x)",
            "sin(nπ/2 + 2x)",
            "2 sin(nπ/2 + 2x)",
        ],
        [
            "2^n sin(nπ/2 − 2x)",
            "2^n sin(nπ/2 + 2x)",
            "sin(nπ/2 + 2x)",
            "2 sin(nπ/2 + 2x)",
        ],
        "B", "medium", "factual",
        "For y = sin(Ax + B), y_n = A^n sin(nπ/2 + Ax + B); here A = 2, B = 0.",
        "y = sin(Ax+B) হলে y_n = Aⁿ sin(nπ/2 + Ax + B); এখানে A = 2।",
    ),
    q(
        "If y = cos 3x, then y_n equals:",
        "y = cos 3x হলে y_n = ?",
        [
            "3^n cos 3x",
            "3^n sin 3x",
            "3^n cos(nπ/2 + 3x)",
            "3^n sin(nπ/2 + 3x)",
        ],
        [
            "3^n cos 3x",
            "3^n sin 3x",
            "3^n cos(nπ/2 + 3x)",
            "3^n sin(nπ/2 + 3x)",
        ],
        "C", "medium", "factual",
        "For y = cos(Ax + B), y_n = A^n cos(nπ/2 + Ax + B); A = 3, B = 0.",
        "y = cos(Ax+B) হলে y_n = Aⁿ cos(nπ/2 + Ax + B)।",
    ),
    q(
        "d/dx (2^x) equals:",
        "d/dx (2ˣ) এর মান কত?",
        ["2^x", "x 2^{x−1}", "2^x ln 2", "ln 2"],
        ["2^x", "x 2^{x−1}", "2^x ln 2", "ln 2"],
        "C", "easy", "factual",
        "d/dx (a^x) = a^x ln a with a = 2 ⇒ 2^x ln 2.",
        "a = 2 নিয়ে 2ˣ ln 2।",
    ),
    q(
        "d/dx (log₁₀ x) equals (x > 0):",
        "d/dx (log₁₀ x) এর মান কত (x > 0)?",
        ["1/x", "(log₁₀ e)/x", "x log₁₀ e", "ln 10"],
        ["1/x", "(log₁₀ e)/x", "x log₁₀ e", "ln 10"],
        "B", "medium", "factual",
        "log₁₀ x = ln x / ln 10 ⇒ derivative (1/x)/ln 10 = (log₁₀ e)/x.",
        "log₁₀ x = ln x / ln 10 ⇒ অন্তরজ (log₁₀ e)/x।",
    ),
    q(
        "d/dx (e^{sin² x}) equals:",
        "d/dx (e^{sin² x}) এর মান কোনটি?",
        [
            "e^{sin² x} sin 2x",
            "2 e^{sin² x} sin x",
            "−e^{sin² x} sin 2x",
            "e^{sin² x}",
        ],
        [
            "e^{sin² x} sin 2x",
            "2 e^{sin² x} sin x",
            "−e^{sin² x} sin 2x",
            "e^{sin² x}",
        ],
        "A", "medium", "numerical",
        "Chain rule: e^{sin² x} · 2 sin x cos x = e^{sin² x} sin 2x.",
        "শৃঙ্খল সূত্র: e^{sin² x} · 2 sin x cos x = e^{sin² x} sin 2x।",
    ),
    q(
        "If y = 1/x, then y_3 equals:",
        "y = 1/x হলে y₃ = ?",
        ["−6/x⁴", "6/x⁴", "−2/x³", "2/x³"],
        ["−6/x⁴", "6/x⁴", "−2/x³", "2/x³"],
        "A", "medium", "numerical",
        "y = x^{−1}; y_n = (−1)^n n! x^{−n−1}; n = 3 ⇒ (−1)^3 3! / x⁴ = −6/x⁴.",
        "y_n = (−1)ⁿ n! x^{−n−1}; n = 3 ⇒ −6/x⁴।",
    ),
    q(
        "If x = a cos θ, y = a sin θ, then dy/dx equals:",
        "x = a cos θ, y = a sin θ হলে dy/dx = ?",
        ["−x/y", "x/y", "−y/x", "y/x"],
        ["−x/y", "x/y", "−y/x", "y/x"],
        "A", "medium", "numerical",
        "dx/dθ = −a sin θ, dy/dθ = a cos θ ⇒ dy/dx = −cot θ = −x/y.",
        "dy/dx = (a cos θ)/(−a sin θ) = −cot θ = −x/y।",
    ),
    q(
        "d/dx (sin √x) equals:",
        "d/dx (sin √x) এর মান কত?",
        [
            "−cos √x",
            "(cos √x)/(2√x)",
            "cos √x",
            "(cos √x)/√x",
        ],
        [
            "−cos √x",
            "(cos √x)/(2√x)",
            "cos √x",
            "(cos √x)/√x",
        ],
        "B", "medium", "numerical",
        "Chain: cos √x · (1/(2√x)).",
        "শৃঙ্খল সূত্র: cos √x · 1/(2√x)।",
    ),
    q(
        "d/dx (e^{−2x} cos x) equals:",
        "d/dx (e^{−2x} cos x) এর মান কোনটি?",
        [
            "−e^{−2x}(sin x + 2 cos x)",
            "−e^{−2x}(sin x − 2 cos x)",
            "e^{−2x}(sin x + 2 cos x)",
            "e^{−2x}(sin x − 2 cos x)",
        ],
        [
            "−e^{−2x}(sin x + 2 cos x)",
            "−e^{−2x}(sin x − 2 cos x)",
            "e^{−2x}(sin x + 2 cos x)",
            "e^{−2x}(sin x − 2 cos x)",
        ],
        "A", "hard", "numerical",
        "Product rule: e^{−2x}(−sin x) + (−2e^{−2x}) cos x = −e^{−2x}(sin x + 2 cos x).",
        "গুণের সূত্রে −e^{−2x}(sin x + 2 cos x)।",
    ),
    q(
        "If y = cos(ax + b), then y_n equals:",
        "y = cos(ax + b) হলে y_n = ?",
        [
            "(−1)^n a^n sin(nπ/2 + ax + b)",
            "a^n sin(nπ/2 + ax + b)",
            "cos(nπ/2 + ax + b)",
            "a^n cos(nπ/2 + ax + b)",
        ],
        [
            "(−1)^n a^n sin(nπ/2 + ax + b)",
            "a^n sin(nπ/2 + ax + b)",
            "cos(nπ/2 + ax + b)",
            "a^n cos(nπ/2 + ax + b)",
        ],
        "D", "medium", "factual",
        "Standard formula: y_n = a^n cos(nπ/2 + ax + b).",
        "সূত্র: y_n = aⁿ cos(nπ/2 + ax + b)।",
    ),
    q(
        "If xy + 2 = 0, then dy/dx equals:",
        "xy + 2 = 0 হলে dy/dx = ?",
        ["−y/x", "y/x", "−x/y", "x/y"],
        ["−y/x", "y/x", "−x/y", "x/y"],
        "A", "medium", "numerical",
        "Differentiate: x y' + y = 0 ⇒ y' = −y/x (or from y = −2/x, y' = 2/x² = −y/x).",
        "অন্তরীকরণে x y' + y = 0 ⇒ y' = −y/x।",
    ),
    q(
        "d/dx (tan^{-1}(e^x)) equals:",
        "d/dx (tan⁻¹(eˣ)) এর মান কত?",
        [
            "e^x / (1 + e^{2x})",
            "1/(1 + e^{2x})",
            "e^x / (1 + e^x)",
            "1/(1 + e^x)",
        ],
        [
            "e^x / (1 + e^{2x})",
            "1/(1 + e^{2x})",
            "e^x / (1 + e^x)",
            "1/(1 + e^x)",
        ],
        "A", "medium", "numerical",
        "d/dx tan^{-1} u = u'/(1+u²) with u = e^x ⇒ e^x/(1+e^{2x}).",
        "u = eˣ নিয়ে eˣ/(1 + e^{2x})।",
    ),
    q(
        "If y = √(sec 2x), then dy/dx equals:",
        "y = √(sec 2x) হলে dy/dx = ?",
        ["y tan 2x", "2 tan 2x", "y cot 2x", "sec 2x tan 2x"],
        ["y tan 2x", "2 tan 2x", "y cot 2x", "sec 2x tan 2x"],
        "A", "hard", "numerical",
        "y = (sec 2x)^{1/2}; y' = (1/2)(sec 2x)^{−1/2} · sec 2x tan 2x · 2 = y tan 2x.",
        "শৃঙ্খল সূত্রে y' = y tan 2x।",
    ),
    q(
        "d/dx [sin²(x²)] equals:",
        "d/dx [sin²(x²)] এর মান কত?",
        [
            "2 sin(x²)",
            "2x sin(x²)",
            "2x sin(2x²)",
            "2x² sin(2x²)",
        ],
        [
            "2 sin(x²)",
            "2x sin(x²)",
            "2x sin(2x²)",
            "2x² sin(2x²)",
        ],
        "C", "hard", "numerical",
        "2 sin(x²) cos(x²) · 2x = 2x sin(2x²).",
        "2 sin(x²) cos(x²) · 2x = 2x sin(2x²)।",
    ),
    q(
        "If y = sec x, then y₂ + y equals:",
        "y = sec x হলে y₂ + y এর মান কোনটি?",
        ["0", "1", "2y³", "2y²"],
        ["0", "1", "2y³", "2y²"],
        "C", "hard", "numerical",
        "y₁ = sec x tan x; y₂ = sec³ x + sec x tan² x = 2 sec³ x − sec x; "
        "y₂ + y = 2 sec³ x = 2y³.",
        "y₂ + y = 2 sec³ x = 2y³।",
    ),
    q(
        "d/dx (x^x) for x > 0 equals:",
        "x > 0 এর জন্য d/dx (xˣ) = ?",
        [
            "x^x",
            "x^x ln x",
            "x^x (1 + ln x)",
            "x^{x−1}",
        ],
        [
            "x^x",
            "x^x ln x",
            "x^x (1 + ln x)",
            "x^{x−1}",
        ],
        "C", "medium", "numerical",
        "Write x^x = e^{x ln x}; derivative e^{x ln x}(ln x + 1) = x^x (1 + ln x).",
        "xˣ = e^{x ln x} ⇒ অন্তরজ xˣ (1 + ln x)।",
    ),
]


# =============================================================================
# hm1_27_ch09_t03 — Applications of derivatives / অন্তরজের প্রয়োগ
# =============================================================================
T03 = [
    q(
        "For the curve y = x² − 2x − 5, the equation of the tangent at (4, 3) is:",
        "y = x² − 2x − 5 বক্ররেখার (4, 3) বিন্দুতে স্পর্শকের সমীকরণ কোনটি?",
        [
            "6x − y + 21 = 0",
            "6x − y − 21 = 0",
            "x − 6y + 21 = 0",
            "x − 6y − 21 = 0",
        ],
        [
            "6x − y + 21 = 0",
            "6x − y − 21 = 0",
            "x − 6y + 21 = 0",
            "x − 6y − 21 = 0",
        ],
        "B", "medium", "application",
        "y' = 2x − 2; at x = 4, slope = 6. Tangent: y − 3 = 6(x − 4) ⇒ 6x − y − 21 = 0.",
        "y' = 2x − 2; x = 4 এ ঢাল 6 ⇒ 6x − y − 21 = 0।",
    ),
    q(
        "At (0, 1) on y = e^x, which statements are true? "
        "(i) tangent: x − y + 1 = 0 (ii) normal: x + y − 1 = 0 (iii) slope of tangent = 1",
        "(0, 1) বিন্দুতে y = eˣ বক্ররেখার জন্য কোনগুলো সঠিক? "
        "(i) স্পর্শক: x − y + 1 = 0 (ii) অভিলম্ব: x + y − 1 = 0 (iii) স্পর্শকের ঢাল = 1",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "medium", "application",
        "y' = e^x; at 0, slope = 1. Tangent y − 1 = 1(x − 0) ⇒ x − y + 1 = 0; "
        "normal slope −1 ⇒ x + y − 1 = 0. All three hold.",
        "ঢাল 1; স্পর্শক ও অভিলম্ব উভয়ই সঠিক; তিনটিই সত্য।",
    ),
    q(
        "For the circle x² + y² = 20, the tangent at (2, 4) is:",
        "x² + y² = 20 বৃত্তের (2, 4) বিন্দুতে স্পর্শকের সমীকরণ কোনটি?",
        [
            "x + 2y + 10 = 0",
            "x + 2y = 10",
            "2x + y − 10 = 0",
            "2x − y − 10 = 0",
        ],
        [
            "x + 2y + 10 = 0",
            "x + 2y = 10",
            "2x + y − 10 = 0",
            "2x − y − 10 = 0",
        ],
        "B", "medium", "application",
        "2x + 2y y' = 0 ⇒ y' = −x/y = −1/2 at (2,4). "
        "Tangent: y − 4 = (−1/2)(x − 2) ⇒ x + 2y = 10.",
        "ঢাল −1/2; স্পর্শক x + 2y = 10।",
    ),
    q(
        "f(x) = x(2a − x). Its maximum value is:",
        "f(x) = x(2a − x) এর সর্বোচ্চ মান কোনটি?",
        ["a", "2a", "a²", "2a²"],
        ["a", "2a", "a²", "2a²"],
        "C", "medium", "application",
        "f' = 2a − 2x = 0 ⇒ x = a; f'' < 0; f(a) = a(2a − a) = a².",
        "x = a এ সর্বোচ্চ; f(a) = a²।",
    ),
    q(
        "A function f is increasing at x = a if:",
        "x = a বিন্দুতে f ক্রমবর্ধমান হবে যদি:",
        ["f'(a) = 0", "f'(a) < 0", "f'(a) ≠ 0", "f'(a) > 0"],
        ["f'(a) = 0", "f'(a) < 0", "f'(a) ≠ 0", "f'(a) > 0"],
        "D", "easy", "conceptual",
        "Locally increasing when the derivative is positive.",
        "অন্তরজ ধনাত্মক হলে ফাংশন ক্রমবর্ধমান।",
    ),
    q(
        "f(x) = x² − 2x is decreasing when:",
        "f(x) = x² − 2x ক্রমহ্রাসমান হবে যখন:",
        ["x > 1", "x < 1", "x > 2", "x < 2"],
        ["x > 1", "x < 1", "x > 2", "x < 2"],
        "B", "easy", "application",
        "f' = 2x − 2 < 0 ⇒ x < 1.",
        "f' = 2x − 2 < 0 ⇒ x < 1।",
    ),
    q(
        "For y = Ax(1 − x), the slope at (1, 1) equals:",
        "y = Ax(1 − x) বক্ররেখার (1, 1) বিন্দুতে ঢাল = ?",
        ["2A", "4A", "−A", "−2A"],
        ["2A", "4A", "−A", "−2A"],
        "C", "medium", "application",
        "y = Ax − Ax²; y' = A − 2Ax; at x = 1, slope = A − 2A = −A.",
        "y' = A − 2Ax; x = 1 এ ঢাল −A।",
    ),
    q(
        "If the tangent to y = Ax(1 − x) at the origin makes 60° with the positive x-axis, then A =",
        "y = Ax(1 − x) এর মূলবিন্দুতে স্পর্শক ধনাত্মক x-অক্ষের সাথে 60° কোণ করলে A = ?",
        ["√3", "1/√3", "1/2", "−√3"],
        ["√3", "1/√3", "1/2", "−√3"],
        "A", "medium", "application",
        "At origin, slope = A = tan 60° = √3.",
        "মূলবিন্দুতে ঢাল A = tan 60° = √3।",
    ),
    q(
        "For y = x² − x + 1, the slope of the normal at (2, 3) is:",
        "y = x² − x + 1 বক্ররেখার (2, 3) বিন্দুতে অভিলম্বের ঢাল কত?",
        ["−3", "−1/3", "1/3", "3"],
        ["−3", "−1/3", "1/3", "3"],
        "B", "medium", "application",
        "y' = 2x − 1; at x = 2, tangent slope = 3; normal slope = −1/3.",
        "স্পর্শকের ঢাল 3; অভিলম্বের ঢাল −1/3।",
    ),
    q(
        "f(x) = 3x² − 2x + 1. Which are true? "
        "(i) increasing at x = 1 (ii) minimum at x = 1/3 (iii) tangent slope at origin is −2",
        "f(x) = 3x² − 2x + 1 এর জন্য কোনগুলো সঠিক? "
        "(i) x = 1 এ ক্রমবর্ধমান (ii) x = 1/3 এ সর্বনিম্ন (iii) মূলবিন্দুতে স্পর্শকের ঢাল −2",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "hard", "application",
        "f' = 6x − 2; f'(1) = 4 > 0; critical at x = 1/3 with f'' = 6 > 0 (min); f'(0) = −2.",
        "f'(1) > 0; x = 1/3 এ min; f'(0) = −2; তিনটিই সত্য।",
    ),
    q(
        "If s = 5t³ − 9t² + 3t + 2, the velocity at t = 4 is:",
        "s = 5t³ − 9t² + 3t + 2 হলে t = 4 এ বেগ কত?",
        ["71", "171", "243", "343"],
        ["71", "171", "243", "343"],
        "B", "medium", "application",
        "v = ds/dt = 15t² − 18t + 3; at t = 4: 15·16 − 72 + 3 = 240 − 72 + 3 = 171.",
        "v = 15t² − 18t + 3; t = 4 এ v = 171।",
    ),
    q(
        "If the tangent to y = cx² at x = 1 makes a 30° angle with the positive x-axis, then c =",
        "y = cx² বক্ররেখার x = 1 বিন্দুতে স্পর্শক ধনাত্মক x-অক্ষের সাথে 30° কোণ করলে c = ?",
        ["√3", "1/(2√3)", "1/2", "√3 / 2"],
        ["√3", "1/(2√3)", "1/2", "√3 / 2"],
        "B", "hard", "application",
        "y' = 2cx; at x = 1, slope = 2c = tan 30° = 1/√3 ⇒ c = 1/(2√3).",
        "2c = tan 30° = 1/√3 ⇒ c = 1/(2√3)।",
    ),
    q(
        "For the circle x² + y² = 9, the normal at (2, √5) is:",
        "x² + y² = 9 বৃত্তের (2, √5) বিন্দুতে অভিলম্বের সমীকরণ কোনটি?",
        [
            "2x + √5 y = 0",
            "√5 x + 2y = 0",
            "2x − √5 y = 0",
            "√5 x − 2y = 0",
        ],
        [
            "2x + √5 y = 0",
            "√5 x + 2y = 0",
            "2x − √5 y = 0",
            "√5 x − 2y = 0",
        ],
        "D", "hard", "application",
        "Normal to a circle through center (0,0) and (2, √5) has equation √5 x − 2y = 0 "
        "(line: y = (√5/2)x ⇒ √5 x − 2y = 0).",
        "কেন্দ্র ও বিন্দুগামী রেখা: √5 x − 2y = 0।",
    ),
    q(
        "If the tangent to the curve 3x² + y − 7 = 0 is parallel to the x-axis, the point is:",
        "3x² + y − 7 = 0 বক্ররেখার স্পর্শক x-অক্ষের সমান্তরাল হলে বিন্দুটি:",
        ["(0, 7)", "(0, −7)", "(6, 0)", "(−6, 0)"],
        ["(0, 7)", "(0, −7)", "(6, 0)", "(−6, 0)"],
        "A", "medium", "application",
        "y = 7 − 3x²; y' = −6x = 0 ⇒ x = 0, y = 7 ⇒ (0, 7).",
        "y' = −6x = 0 ⇒ x = 0, y = 7।",
    ),
    q(
        "For y = 3x(x − 2), the slope of the tangent at (2, 0) is:",
        "y = 3x(x − 2) বক্ররেখার (2, 0) বিন্দুতে স্পর্শকের ঢাল কত?",
        ["−12", "−6", "6", "12"],
        ["−12", "−6", "6", "12"],
        "C", "easy", "application",
        "y = 3x² − 6x; y' = 6x − 6; at x = 2, slope = 12 − 6 = 6.",
        "y' = 6x − 6; x = 2 এ ঢাল 6।",
    ),
    q(
        "For y = 3x(x − 2), the tangent at the origin is:",
        "y = 3x(x − 2) এর মূলবিন্দুতে স্পর্শকের সমীকরণ কোনটি?",
        ["y + 6x = 0", "y − 6x = 0", "x + 6y = 0", "x − 6y = 0"],
        ["y + 6x = 0", "y − 6x = 0", "x + 6y = 0", "x − 6y = 0"],
        "A", "easy", "application",
        "At (0,0), slope = −6; tangent y = −6x ⇒ y + 6x = 0.",
        "মূলবিন্দুতে ঢাল −6 ⇒ y + 6x = 0।",
    ),
    q(
        "f(x) = x + 1/x (x > 0) has a minimum at x =",
        "f(x) = x + 1/x (x > 0) এর ক্ষুদ্রতম মান কোন x-এ?",
        ["0", "1", "−1", "2"],
        ["0", "1", "−1", "2"],
        "B", "medium", "application",
        "f' = 1 − 1/x² = 0 ⇒ x = ±1; for x > 0 take x = 1; f''(1) = 2/x³ > 0 ⇒ minimum.",
        "f' = 0 ⇒ x = 1 (x > 0); f'' > 0 ⇒ সর্বনিম্ন।",
    ),
    q(
        "If y = x ln x, the abscissa where the tangent is parallel to the x-axis is:",
        "y = x ln x বক্ররেখার যে বিন্দুতে স্পর্শক x-অক্ষের সমান্তরাল, তার ভুজ:",
        ["e", "−e", "1/e", "−1/e"],
        ["e", "−e", "1/e", "−1/e"],
        "C", "medium", "application",
        "y' = ln x + 1 = 0 ⇒ ln x = −1 ⇒ x = 1/e.",
        "y' = ln x + 1 = 0 ⇒ x = 1/e।",
    ),
    q(
        "Differentiation of a function geometrically represents the:",
        "কোনো ফাংশনের অন্তরীকরণ জ্যামিতিকভাবে কী নির্দেশ করে?",
        ["slope (of the tangent)", "area", "a straight line only", "volume"],
        ["ঢাল (স্পর্শকের)", "ক্ষেত্রফল", "শুধু সরলরেখা", "আয়তন"],
        "A", "easy", "conceptual",
        "f'(x) is the slope of the tangent to y = f(x) at x.",
        "f'(x) হলো y = f(x) এর স্পর্শকের ঢাল।",
    ),
    q(
        "For y = ax(1 − x), the slope at the origin equals:",
        "y = ax(1 − x) বক্ররেখার মূলবিন্দুতে ঢাল কত?",
        ["−a", "a", "a − 2ax", "a + 2ax"],
        ["−a", "a", "a − 2ax", "a + 2ax"],
        "B", "easy", "application",
        "y' = a − 2ax; at x = 0, slope = a.",
        "y' = a − 2ax; x = 0 এ ঢাল a।",
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
    counts["hm1_27_ch09_t01"] = write_topic("hm1_27_ch09_t01", T01)["count"]
    counts["hm1_27_ch09_t02"] = write_topic("hm1_27_ch09_t02", T02)["count"]
    counts["hm1_27_ch09_t03"] = write_topic("hm1_27_ch09_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm1_27_ch09",
        "title_en": "Differentiation",
        "title_bn": "অন্তরীকরণ",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(287, 300)],
        "topics": {
            "hm1_27_ch09_t01": {
                "title_en": "Limits and continuity",
                "title_bn": "সীমা ও অবিচ্ছিন্নতা",
                "udvash_types": [
                    "standard limits",
                    "trig/exp/log limits",
                    "continuity definition",
                    "infinite limits",
                ],
                "count": 20,
            },
            "hm1_27_ch09_t02": {
                "title_en": "Rules of differentiation",
                "title_bn": "অন্তরীকরণের সূত্র",
                "udvash_types": [
                    "basic derivatives",
                    "product/chain",
                    "nth derivatives",
                    "parametric/implicit",
                    "inverse trig/exp",
                ],
                "count": 20,
            },
            "hm1_27_ch09_t03": {
                "title_en": "Applications of derivatives",
                "title_bn": "অন্তরজের প্রয়োগ",
                "udvash_types": [
                    "tangent/normal",
                    "increasing/decreasing",
                    "max/min",
                    "velocity",
                    "angle with axes",
                ],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "figure_only_sketches": "Printed graph/option-figure items (e.g. exponential sketch panels) rewritten as text-describable MCQs",
            "garbled_limit_stems": "Many lim stems OCR-unreadable; reconstructed from solution lines and standard board forms",
            "stimulus_pairs": "Linked stimulus blocks (shared curve definitions) curated as standalone clear stems",
            "mixed_integration_intrusions": "Occasional integration options in printed keys skipped; chapter kept to differentiation",
        },
        "low_confidence": [
            "OCR on pp. 287–299 heavily noisy; column PNGs/answer keys used to reconstruct stems.",
            "Inline math stored as plain text (sqrt, ^, pi, ln/e, ^{ }) for JSONL.",
            "Some printed angle/point labels inconsistent in OCR; closed-form board standards retained.",
            "Parametric and nth-derivative formulas verified against standard HSC identities.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm1_ch09.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch09_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
