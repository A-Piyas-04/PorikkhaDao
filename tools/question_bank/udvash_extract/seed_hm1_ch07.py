#!/usr/bin/env python3
"""Seed Higher Mathematics 1st Paper Ch7 (Trigonometric Ratios of Associated Angles).

Curated from Udvash HSC Question Bank 2026 printed pp. 229–240 (PDF 235–246).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
OCR is heavily noisy; reconstructs board-style items and supplements with accurate HSC-level authored MCQs.
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
    "higher_mathematics p1 ch07; curated bilingual"
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
# hm1_27_ch07_t01 — Sum and difference formulas
# =============================================================================
T01 = [
    q(
        "cosec(270 deg - theta) equals:",
        "cosec(270° − θ) এর মান:",
        ["-sin theta", "sin theta", "cosec theta", "-sec theta"],
        ["-sin θ", "sin θ", "cosec θ", "-sec θ"],
        "D", "easy", "conceptual",
        "cosec(270° − θ) = cosec(3×90° − θ) = −sec θ.",
        "cosec(270° − θ) = cosec(3×90° − θ) = −sec θ।",
    ),
    q(
        "If tan theta = 1/2, then cos 2theta equals:",
        "tan θ = 1/2 হলে cos 2θ এর মান:",
        ["3/5", "-3/5", "4/5", "5/3"],
        ["3/5", "-3/5", "4/5", "5/3"],
        "A", "medium", "numerical",
        "cos 2θ = (1 − tan²θ)/(1 + tan²θ) = (1 − 1/4)/(1 + 1/4) = (3/4)/(5/4) = 3/5.",
        "cos 2θ = (1 − tan²θ)/(1 + tan²θ) = (1 − 1/4)/(1 + 1/4) = 3/5।",
    ),
    q(
        "(1 − tan 25 deg)/(1 + tan 25 deg) equals:",
        "(1 − tan 25°)/(1 + tan 25°) এর মান:",
        ["tan 25 deg", "cot 20 deg", "cot 70 deg", "tan 50 deg"],
        ["tan 25°", "cot 20°", "cot 70°", "tan 50°"],
        "C", "medium", "numerical",
        "(tan 45° − tan 25°)/(1 + tan 45° tan 25°) = tan(45° − 25°) = tan 20° = cot 70°.",
        "(tan 45° − tan 25°)/(1 + tan 45° tan 25°) = tan 20° = cot 70°।",
    ),
    q(
        "cot 15 deg equals:",
        "cot 15° এর মান:",
        ["2 + sqrt(3)", "2 − sqrt(3)", "sqrt(3)", "1/sqrt(3)"],
        ["2 + √3", "2 − √3", "√3", "1/√3"],
        "A", "medium", "numerical",
        "cot 15° = cot(45° − 30°) = (cot 45° cot 30° + 1)/(cot 30° − cot 45°) = (√3 + 1)/(√3 − 1) = 2 + √3.",
        "cot 15° = cot(45° − 30°) = (√3 + 1)/(√3 − 1) = 2 + √3।",
    ),
    q(
        "tan 75 deg − tan 30 deg − tan 75 deg · tan 30 deg equals:",
        "tan 75° − tan 30° − tan 75° · tan 30° এর মান:",
        ["-1", "1", "sqrt(3)", "0"],
        ["-1", "1", "√3", "0"],
        "B", "medium", "numerical",
        "tan(75° − 30°) = tan 45° = 1 ⇒ (tan 75° − tan 30°)/(1 + tan 75° tan 30°) = 1 "
        "⇒ tan 75° − tan 30° − tan 75° tan 30° = 1.",
        "tan(75° − 30°) = 1 ⇒ tan 75° − tan 30° = 1 + tan 75° tan 30° ⇒ পার্থক্য − গুণফল = 1।",
    ),
    q(
        "If A + B = 90 deg, then which is true?",
        "A + B = 90° হলে কোনটি সঠিক?",
        ["tan A = tan B", "tan A = −tan B", "tan A tan B = −1", "tan A tan B = 1"],
        ["tan A = tan B", "tan A = −tan B", "tan A tan B = −1", "tan A tan B = 1"],
        "D", "easy", "conceptual",
        "tan(A + B) is undefined ⇒ 1 − tan A tan B = 0 ⇒ tan A tan B = 1.",
        "tan(A + B) অসংজ্ঞাত ⇒ 1 − tan A tan B = 0 ⇒ tan A tan B = 1।",
    ),
    q(
        "sin(A − 30 deg) + sin(150 deg + A) equals:",
        "sin(A − 30°) + sin(150° + A) এর মান:",
        ["sqrt(3) cos A", "0", "cos A", "sin A"],
        ["√3 cos A", "0", "cos A", "sin A"],
        "B", "medium", "numerical",
        "sin(150° + A) = sin(180° + (A − 30°)) = −sin(A − 30°); sum is 0.",
        "sin(150° + A) = −sin(A − 30°); যোগফল 0।",
    ),
    q(
        "[sin(45 deg + A) + sin(45 deg − A)] / [cos(45 deg − A) − cos(45 deg + A)] equals:",
        "[sin(45° + A) + sin(45° − A)] / [cos(45° − A) − cos(45° + A)] এর মান:",
        ["cot A", "-1", "1", "tan A"],
        ["cot A", "-1", "1", "tan A"],
        "A", "hard", "numerical",
        "Numerator = 2 sin 45° cos A; denominator = 2 sin 45° sin A ⇒ ratio = cot A.",
        "লব = 2 sin 45° cos A; হর = 2 sin 45° sin A ⇒ cot A।",
    ),
    q(
        "cosec(−330 deg) equals:",
        "cosec(−330°) এর মান:",
        ["-2", "-1", "1", "2"],
        ["-2", "-1", "1", "2"],
        "D", "medium", "numerical",
        "cosec(−330°) = −cosec 330° = −cosec(360° − 30°) = −(−cosec 30°) = 2.",
        "cosec(−330°) = −cosec 330° = cosec 30° = 2।",
    ),
    q(
        "Which identity is correct?",
        "কোন অভেদটি সঠিক?",
        ["sin(−θ) = sin θ", "tan(−θ) = tan θ", "sec(−θ) = sec θ", "cosec(−θ) = cosec θ"],
        ["sin(−θ) = sin θ", "tan(−θ) = tan θ", "sec(−θ) = sec θ", "cosec(−θ) = cosec θ"],
        "C", "easy", "conceptual",
        "sec is even: sec(−θ) = 1/cos(−θ) = 1/cos θ = sec θ.",
        "sec যুগ্ম ফাংশন: sec(−θ) = sec θ।",
    ),
    q(
        "tan(−480 deg) equals:",
        "tan(−480°) এর মান:",
        ["sqrt(3)", "1/sqrt(3)", "-1/sqrt(3)", "-sqrt(3)"],
        ["√3", "1/√3", "-1/√3", "-√3"],
        "A", "hard", "numerical",
        "tan(−480°) = −tan 480° = −tan(5×90° + 30°) = −(−cot 30°) = √3.",
        "tan(−480°) = −tan 480° = cot 30° = √3।",
    ),
    q(
        "If sin 25 deg + cos 25 deg = sin 65 deg + cos x deg, then x equals:",
        "sin 25° + cos 25° = sin 65° + cos x° হলে x এর মান:",
        ["25", "50", "65", "70"],
        ["25", "50", "65", "70"],
        "C", "easy", "numerical",
        "sin 65° = cos 25° ⇒ cos 25° = cos x° ⇒ x = 65.",
        "sin 65° = cos 25° ⇒ cos x° = cos 25° ⇒ x = 65।",
    ),
    q(
        "sin(A + B) expands to:",
        "sin(A + B) এর সম্প্রসারণ:",
        ["sin A cos B − cos A sin B", "sin A cos B + cos A sin B",
         "cos A cos B − sin A sin B", "cos A cos B + sin A sin B"],
        ["sin A cos B − cos A sin B", "sin A cos B + cos A sin B",
         "cos A cos B − sin A sin B", "cos A cos B + sin A sin B"],
        "B", "easy", "factual",
        "Standard sum formula: sin(A + B) = sin A cos B + cos A sin B.",
        "যোগ সূত্র: sin(A + B) = sin A cos B + cos A sin B।",
    ),
    q(
        "cos(A − B) expands to:",
        "cos(A − B) এর সম্প্রসারণ:",
        ["cos A cos B + sin A sin B", "cos A cos B − sin A sin B",
         "sin A cos B − cos A sin B", "sin A cos B + cos A sin B"],
        ["cos A cos B + sin A sin B", "cos A cos B − sin A sin B",
         "sin A cos B − cos A sin B", "sin A cos B + cos A sin B"],
        "A", "easy", "factual",
        "Standard difference formula: cos(A − B) = cos A cos B + sin A sin B.",
        "বিয়োগ সূত্র: cos(A − B) = cos A cos B + sin A sin B।",
    ),
    q(
        "tan(A + B) equals:",
        "tan(A + B) এর মান:",
        ["(tan A + tan B)/(1 − tan A tan B)", "(tan A − tan B)/(1 + tan A tan B)",
         "(tan A + tan B)/(1 + tan A tan B)", "(tan A − tan B)/(1 − tan A tan B)"],
        ["(tan A + tan B)/(1 − tan A tan B)", "(tan A − tan B)/(1 + tan A tan B)",
         "(tan A + tan B)/(1 + tan A tan B)", "(tan A − tan B)/(1 − tan A tan B)"],
        "A", "easy", "factual",
        "Standard formula: tan(A + B) = (tan A + tan B)/(1 − tan A tan B).",
        "যোগ সূত্র: tan(A + B) = (tan A + tan B)/(1 − tan A tan B)।",
    ),
    q(
        "If alpha + beta + gamma = pi/2, then cosec(beta + gamma) equals:",
        "α + β + γ = π/2 হলে cosec(β + γ) এর মান:",
        ["-sec alpha", "sec alpha", "-cosec alpha", "cosec alpha"],
        ["-sec α", "sec α", "-cosec α", "cosec α"],
        "B", "hard", "conceptual",
        "beta + gamma = pi/2 − alpha ⇒ cosec(beta + gamma) = sec alpha.",
        "β + γ = π/2 − α ⇒ cosec(β + γ) = sec α।",
    ),
    q(
        "sin 75 deg equals:",
        "sin 75° এর মান:",
        ["(sqrt(6) + sqrt(2))/4", "(sqrt(6) − sqrt(2))/4", "(sqrt(3) + 1)/2", "1/2"],
        ["(√6 + √2)/4", "(√6 − √2)/4", "(√3 + 1)/2", "1/2"],
        "A", "medium", "numerical",
        "sin 75° = sin(45° + 30°) = (√2/2)(√3/2) + (√2/2)(1/2) = (√6 + √2)/4.",
        "sin 75° = sin(45° + 30°) = (√6 + √2)/4।",
    ),
    q(
        "cos 15 deg equals:",
        "cos 15° এর মান:",
        ["(sqrt(6) + sqrt(2))/4", "(sqrt(6) − sqrt(2))/4", "(sqrt(3) − 1)/2", "sqrt(3)/2"],
        ["(√6 + √2)/4", "(√6 − √2)/4", "(√3 − 1)/2", "√3/2"],
        "A", "medium", "numerical",
        "cos 15° = cos(45° − 30°) = (√2/2)(√3/2) + (√2/2)(1/2) = (√6 + √2)/4.",
        "cos 15° = cos(45° − 30°) = (√6 + √2)/4।",
    ),
    q(
        "tan 15 deg equals:",
        "tan 15° এর মান:",
        ["2 − sqrt(3)", "2 + sqrt(3)", "sqrt(3) − 1", "sqrt(3)"],
        ["2 − √3", "2 + √3", "√3 − 1", "√3"],
        "A", "medium", "numerical",
        "tan 15° = tan(45° − 30°) = (1 − 1/√3)/(1 + 1/√3) = 2 − √3.",
        "tan 15° = tan(45° − 30°) = 2 − √3।",
    ),
    q(
        "(1 + tan 50 deg)(1 − tan 5 deg) equals approximately:",
        "(1 + tan 50°)(1 − tan 5°) এর মান প্রায়:",
        ["-2", "-1", "1", "2"],
        ["-2", "-1", "1", "2"],
        "D", "hard", "numerical",
        "Direct evaluation: tan 50° ≈ 1.1918, tan 5° ≈ 0.0875 ⇒ product ≈ 2.",
        "tan 50° ≈ 1.1918, tan 5° ≈ 0.0875 ⇒ গুণফল ≈ 2।",
    ),
]


# =============================================================================
# hm1_27_ch07_t02 — Multiple and half angles
# =============================================================================
T02 = [
    q(
        "3 cos 20 deg − 4 cos^3 20 deg equals:",
        "3 cos 20° − 4 cos³ 20° এর মান:",
        ["-1/2", "1/2", "sqrt(3)/2", "-sqrt(3)/2"],
        ["-1/2", "1/2", "√3/2", "-√3/2"],
        "A", "medium", "numerical",
        "4 cos³ θ − 3 cos θ = cos 3θ ⇒ 3 cos 20° − 4 cos³ 20° = −cos 60° = −1/2.",
        "3 cos 20° − 4 cos³ 20° = −cos 60° = −1/2।",
    ),
    q(
        "If sin 5 deg = p, then sin 10 deg equals:",
        "sin 5° = p হলে sin 10° এর মান:",
        ["2p sqrt(1 − p^2)", "2 sqrt(1 − p^2)", "2p sqrt(p^2 − 1)", "2p"],
        ["2p√(1 − p²)", "2√(1 − p²)", "2p√(p² − 1)", "2p"],
        "A", "medium", "numerical",
        "sin 10° = 2 sin 5° cos 5° = 2p √(1 − p²).",
        "sin 10° = 2 sin 5° cos 5° = 2p √(1 − p²)।",
    ),
    q(
        "Which statements about cos 2A are true? "
        "(i) cos 2A = 1 − 2 sin^2 A  (ii) cos 2A = 2 cos^2 A − 1  "
        "(iii) cos 2A = (1 − tan^2 A)/(1 + tan^2 A)",
        "cos 2A সম্পর্কে কোনগুলো সঠিক? "
        "(i) cos 2A = 1 − 2 sin² A  (ii) cos 2A = 2 cos² A − 1  "
        "(iii) cos 2A = (1 − tan² A)/(1 + tan² A)",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "easy", "conceptual",
        "All three are standard double-angle forms of cos 2A.",
        "তিনটিই cos 2A এর আদর্শ দ্বিগুণ সূত্র।",
    ),
    q(
        "If tan theta = sqrt(3), which are true? "
        "(i) sin 2theta = sqrt(3)/2  (ii) cos 2theta = −1/2  (iii) tan 2theta = −sqrt(3)",
        "tan θ = √3 হলে কোনগুলো সঠিক? "
        "(i) sin 2θ = √3/2  (ii) cos 2θ = −1/2  (iii) tan 2θ = −√3",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "medium", "numerical",
        "θ = 60° ⇒ 2θ = 120° ⇒ sin = √3/2, cos = −1/2, tan = −√3.",
        "θ = 60° ⇒ 2θ = 120° ⇒ sin = √3/2, cos = −1/2, tan = −√3।",
    ),
    q(
        "2 sin^2 75 deg equals:",
        "2 sin² 75° এর মান:",
        ["1 − sqrt(3)/2", "(2 + sqrt(3))/2", "(2 − sqrt(3))/2", "1 + sqrt(3)/2"],
        ["1 − √3/2", "(2 + √3)/2", "(2 − √3)/2", "1 + √3/2"],
        "A", "medium", "numerical",
        "2 sin² 75° = 1 − cos 150° = 1 − (−√3/2) wait: cos 150° = −√3/2 ⇒ 1 − (−√3/2) = 1 + √3/2. "
        "Using 2 sin² x = 1 − cos 2x: 1 − cos 150° = 1 − (−√3/2) = 1 + √3/2. "
        "Also 2 sin² 15° = 1 − cos 30° = 1 − √3/2. Stem is 75° ⇒ answer 1 + √3/2.",
        "2 sin² 75° = 1 − cos 150° = 1 + √3/2।",
    ),
    q(
        "2 tan(45 deg + x) / [1 + tan^2 (45 deg + x)] equals:",
        "2 tan(45° + x) / [1 + tan²(45° + x)] এর মান:",
        ["cos 2x", "sin 2x", "cot 2x", "tan 2x"],
        ["cos 2x", "sin 2x", "cot 2x", "tan 2x"],
        "A", "hard", "numerical",
        "2 tan φ/(1 + tan² φ) = sin 2φ with φ = 45° + x ⇒ sin(90° + 2x) = cos 2x.",
        "φ = 45° + x ⇒ sin(90° + 2x) = cos 2x।",
    ),
    q(
        "If cos 2A = 1/2, then sin A equals:",
        "cos 2A = 1/2 হলে sin A এর মান:",
        ["±1/2", "±1/sqrt(2)", "±sqrt(3)/2", "±sqrt(1/4)"],
        ["±1/2", "±1/√2", "±√3/2", "±1/2"],
        "A", "medium", "numerical",
        "sin² A = (1 − cos 2A)/2 = (1 − 1/2)/2 = 1/4 ⇒ sin A = ±1/2.",
        "sin² A = (1 − cos 2A)/2 = 1/4 ⇒ sin A = ±1/2।",
    ),
    q(
        "tan 40 deg equals:",
        "tan 40° এর মান:",
        ["2 tan 20 deg / (1 + tan^2 20 deg)", "2 tan 20 deg / (1 − tan^2 20 deg)",
         "2 tan theta / (1 − tan^2 theta)", "(1 − tan^2 20 deg) / (2 tan 20 deg)"],
        ["2 tan 20° / (1 + tan² 20°)", "2 tan 20° / (1 − tan² 20°)",
         "2 tan θ / (1 − tan² θ)", "(1 − tan² 20°) / (2 tan 20°)"],
        "B", "easy", "conceptual",
        "tan 2α = 2 tan α/(1 − tan² α) with α = 20° ⇒ tan 40°.",
        "tan 2α = 2 tan α/(1 − tan² α); α = 20° ⇒ tan 40°।",
    ),
    q(
        "If tan A = 1/sqrt(3), then sin 3A equals:",
        "tan A = 1/√3 হলে sin 3A এর মান:",
        ["0", "1", "1/2", "sqrt(3)/2"],
        ["0", "1", "1/2", "√3/2"],
        "B", "medium", "numerical",
        "A = 30° ⇒ 3A = 90° ⇒ sin 3A = 1.",
        "A = 30° ⇒ 3A = 90° ⇒ sin 3A = 1।",
    ),
    q(
        "sin 2A equals:",
        "sin 2A এর মান:",
        ["2 sin A cos A", "cos^2 A − sin^2 A", "2 tan A / (1 − tan^2 A)", "1 − 2 sin^2 A"],
        ["2 sin A cos A", "cos² A − sin² A", "2 tan A / (1 − tan² A)", "1 − 2 sin² A"],
        "A", "easy", "factual",
        "Standard double-angle: sin 2A = 2 sin A cos A.",
        "দ্বিগুণ সূত্র: sin 2A = 2 sin A cos A।",
    ),
    q(
        "Which are correct? "
        "(i) tan 2A = 2 tan A / (1 − tan^2 A)  "
        "(ii) sin 2A = 2 tan A / (1 + tan^2 A)  "
        "(iii) cos 2A = (1 − tan^2 A)/(1 + tan^2 A)",
        "কোনগুলো সঠিক? "
        "(i) tan 2A = 2 tan A / (1 − tan² A)  "
        "(ii) sin 2A = 2 tan A / (1 + tan² A)  "
        "(iii) cos 2A = (1 − tan² A)/(1 + tan² A)",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "easy", "conceptual",
        "All three are standard tan-half / double-angle identities.",
        "তিনটিই আদর্শ দ্বিগুণ/tan সূত্র।",
    ),
    q(
        "If 2 tan^2 (x/2) − 1 = 0, then cos x equals:",
        "2 tan²(x/2) − 1 = 0 হলে cos x এর মান:",
        ["0", "1/3", "1/2", "2/3"],
        ["0", "1/3", "1/2", "2/3"],
        "B", "hard", "numerical",
        "tan(x/2) = 1/√2 ⇒ cos x = (1 − tan²(x/2))/(1 + tan²(x/2)) = (1 − 1/2)/(1 + 1/2) = (1/2)/(3/2) = 1/3.",
        "tan(x/2) = 1/√2 ⇒ cos x = (1 − 1/2)/(1 + 1/2) = 1/3।",
    ),
    q(
        "2 sin^2 15 deg equals:",
        "2 sin² 15° এর মান:",
        ["1 − sqrt(3)/2", "1 + sqrt(3)/2", "(2 − sqrt(3))/2", "sqrt(3)/2"],
        ["1 − √3/2", "1 + √3/2", "(2 − √3)/2", "√3/2"],
        "A", "medium", "numerical",
        "2 sin² 15° = 1 − cos 30° = 1 − √3/2.",
        "2 sin² 15° = 1 − cos 30° = 1 − √3/2।",
    ),
    q(
        "If cos theta = 3/5 and 0 < theta < pi/2, then sin 2theta equals:",
        "cos θ = 3/5 এবং 0 < θ < π/2 হলে sin 2θ এর মান:",
        ["6/25", "24/25", "7/25", "12/25"],
        ["6/25", "24/25", "7/25", "12/25"],
        "B", "medium", "numerical",
        "sin θ = 4/5 ⇒ sin 2θ = 2·(4/5)·(3/5) = 24/25.",
        "sin θ = 4/5 ⇒ sin 2θ = 24/25।",
    ),
    q(
        "cos 3theta in terms of cos theta is:",
        "cos θ এর সাপেক্ষে cos 3θ:",
        ["4 cos^3 theta − 3 cos theta", "3 cos theta − 4 cos^3 theta",
         "3 sin theta − 4 sin^3 theta", "4 sin^3 theta − 3 sin theta"],
        ["4 cos³ θ − 3 cos θ", "3 cos θ − 4 cos³ θ",
         "3 sin θ − 4 sin³ θ", "4 sin³ θ − 3 sin θ"],
        "A", "easy", "factual",
        "Standard triple-angle: cos 3θ = 4 cos³ θ − 3 cos θ.",
        "ত্রিগুণ সূত্র: cos 3θ = 4 cos³ θ − 3 cos θ।",
    ),
    q(
        "sin 3theta equals:",
        "sin 3θ এর মান:",
        ["3 sin theta − 4 sin^3 theta", "4 sin^3 theta − 3 sin theta",
         "4 cos^3 theta − 3 cos theta", "3 cos theta − 4 cos^3 theta"],
        ["3 sin θ − 4 sin³ θ", "4 sin³ θ − 3 sin θ",
         "4 cos³ θ − 3 cos θ", "3 cos θ − 4 cos³ θ"],
        "A", "easy", "factual",
        "Standard triple-angle: sin 3θ = 3 sin θ − 4 sin³ θ.",
        "ত্রিগুণ সূত্র: sin 3θ = 3 sin θ − 4 sin³ θ।",
    ),
    q(
        "If sin theta = 3/5, then sin 3theta equals:",
        "sin θ = 3/5 হলে sin 3θ এর মান:",
        ["-117/125", "117/125", "27/125", "-27/125"],
        ["-117/125", "117/125", "27/125", "-27/125"],
        "B", "hard", "numerical",
        "sin 3θ = 3·(3/5) − 4·(27/125) = 9/5 − 108/125 = 225/125 − 108/125 = 117/125.",
        "sin 3θ = 3·(3/5) − 4·(27/125) = 117/125।",
    ),
    q(
        "[1 − tan^2 (pi/4 + x)] / [1 + tan^2 (pi/4 + x)] equals:",
        "[1 − tan²(π/4 + x)] / [1 + tan²(π/4 + x)] এর মান:",
        ["sin 2x", "−cos 2x", "−sin 2x", "cos 2x"],
        ["sin 2x", "−cos 2x", "−sin 2x", "cos 2x"],
        "C", "hard", "numerical",
        "Expression = cos(2(π/4 + x)) = cos(π/2 + 2x) = −sin 2x.",
        "মান = cos(π/2 + 2x) = −sin 2x।",
    ),
    q(
        "If f(x) = cos 2x − sin 2x = 0, a principal solution for x is:",
        "f(x) = cos 2x − sin 2x = 0 হলে x এর একটি প্রধান সমাধান:",
        ["pi", "pi/8", "pi/4", "pi/2"],
        ["মান pi", "মান pi/8", "মান pi/4", "মান pi/2"],
        "B", "medium", "numerical",
        "cos 2x = sin 2x ⇒ tan 2x = 1 ⇒ 2x = π/4 ⇒ x = π/8.",
        "tan 2x = 1 ⇒ 2x = π/4 ⇒ x = π/8।",
    ),
    q(
        "tan theta + 2 cot 2theta equals:",
        "tan θ + 2 cot 2θ এর মান:",
        ["cot theta", "tan theta", "2 cot theta", "2 tan theta"],
        ["cot θ", "tan θ", "2 cot θ", "2 tan θ"],
        "A", "hard", "numerical",
        "2 cot 2θ = (1 − tan² θ)/tan θ ⇒ tan θ + 2 cot 2θ = tan θ + (1 − tan² θ)/tan θ = 1/tan θ = cot θ.",
        "tan θ + 2 cot 2θ = cot θ।",
    ),
]


# Fix T02 Q5 options/key — 2 sin^2 75° = 1 + √3/2
T02[4] = q(
    "2 sin^2 75 deg equals:",
    "2 sin² 75° এর মান:",
    ["1 − sqrt(3)/2", "1 + sqrt(3)/2", "(2 − sqrt(3))/2", "sqrt(3)/2"],
    ["1 − √3/2", "1 + √3/2", "(2 − √3)/2", "√3/2"],
    "B", "medium", "numerical",
    "2 sin² 75° = 1 − cos 150° = 1 − (−√3/2) = 1 + √3/2.",
    "2 sin² 75° = 1 − cos 150° = 1 + √3/2।",
)

# Fix T02 Q7 duplicate option D same as A — change D
T02[6] = q(
    "If cos 2A = 1/2, then sin A equals:",
    "cos 2A = 1/2 হলে sin A এর মান:",
    ["±1/2", "±1/sqrt(2)", "±sqrt(3)/2", "±sqrt(3)/4"],
    ["±1/2", "±1/√2", "±√3/2", "±√3/4"],
    "A", "medium", "numerical",
    "sin² A = (1 − cos 2A)/2 = 1/4 ⇒ sin A = ±1/2.",
    "sin² A = (1 − cos 2A)/2 = 1/4 ⇒ sin A = ±1/2।",
)


# =============================================================================
# hm1_27_ch07_t03 — Transformation of trigonometric expressions
# =============================================================================
T03 = [
    q(
        "The identity cos^2 A − cos^2 B equals:",
        "অভেদ cos² A − cos² B সমান:",
        ["sin(A + B) sin(B − A)", "sin(A − B)", "cos(A − B)", "cos(A + B)"],
        ["sin(A + B) sin(B − A)", "sin(A − B)", "cos(A − B)", "cos(A + B)"],
        "A", "medium", "conceptual",
        "Standard: cos² A − cos² B = sin(A + B) sin(B − A).",
        "আদর্শ অভেদ: cos² A − cos² B = sin(A + B) sin(B − A)।",
    ),
    q(
        "If A + B = pi/4, then cos^2 A − cos^2 B equals:",
        "A + B = π/4 হলে cos² A − cos² B এর মান:",
        ["(sqrt(2)/2) cos(A − B)", "(sqrt(2)/2) sin(B − A)", "cos(A − B)", "sin(B − A)"],
        ["(√2/2) cos(A − B)", "(√2/2) sin(B − A)", "cos(A − B)", "sin(B − A)"],
        "B", "hard", "numerical",
        "cos² A − cos² B = sin(A+B) sin(B−A) = sin(π/4) sin(B−A) = (√2/2) sin(B−A).",
        "মান = sin(π/4) sin(B − A) = (√2/2) sin(B − A)।",
    ),
    q(
        "cos^2 3 deg + cos^2 6 deg + ... + cos^2 87 deg equals:",
        "cos² 3° + cos² 6° + … + cos² 87° এর মান:",
        ["14", "14.5", "28", "28.5"],
        ["14", "14.5", "28", "28.5"],
        "B", "hard", "numerical",
        "29 terms; pair cos² k + cos²(90−k)=1 for 14 pairs, plus cos² 45° = 1/2 ⇒ 14.5.",
        "১৪ জোড়া যোগফল ১ এবং cos² 45° = 1/2 ⇒ মোট 14.5।",
    ),
    q(
        "sin 65 deg + cos 65 deg equals:",
        "sin 65° + cos 65° এর মান:",
        ["2 cos 40 deg", "2 sin 20 deg", "2 sin 40 deg", "sqrt(2) cos 20 deg"],
        ["2 cos 40°", "2 sin 20°", "2 sin 40°", "√2 cos 20°"],
        "D", "medium", "numerical",
        "sin 65° + cos 65° = sin 65° + sin 25° = 2 sin 45° cos 20° = √2 cos 20°.",
        "sin 65° + cos 65° = 2 sin 45° cos 20° = √2 cos 20°।",
    ),
    q(
        "sin^4 theta − cos^4 theta equals:",
        "sin⁴ θ − cos⁴ θ এর মান:",
        ["1 + 2 sin^2 theta", "1 + 2 cos^2 theta", "2 sin^2 theta − 1", "2 cos^2 theta − 1"],
        ["1 + 2 sin² θ", "1 + 2 cos² θ", "2 sin² θ − 1", "2 cos² θ − 1"],
        "C", "medium", "conceptual",
        "sin⁴ − cos⁴ = (sin² − cos²)(sin² + cos²) = sin² − cos² = 2 sin² − 1.",
        "sin⁴ − cos⁴ = sin² − cos² = 2 sin² θ − 1।",
    ),
    q(
        "Which are true for multiple-angle transforms? "
        "(i) cos 4A = (1 − tan^2 2A)/(1 + tan^2 2A)  "
        "(ii) sin 6A = 2 sin 3A cos 3A  "
        "(iii) tan 8A = 2 tan 4A / (1 − tan^2 4A)",
        "গুণিতক রূপান্তরে কোনগুলো সঠিক? "
        "(i) cos 4A = (1 − tan² 2A)/(1 + tan² 2A)  "
        "(ii) sin 6A = 2 sin 3A cos 3A  "
        "(iii) tan 8A = 2 tan 4A / (1 − tan² 4A)",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "easy", "conceptual",
        "Each is a direct double-angle rewrite of the next multiple.",
        "প্রতিটি পরবর্তী গুণিতকের দ্বিগুণ সূত্রের সরাসরি রূপ।",
    ),
    q(
        "sin A cos B can be rewritten as:",
        "sin A cos B কে লেখা যায়:",
        ["[sin(A+B) + sin(A−B)]/2", "[sin(A+B) − sin(A−B)]/2",
         "[cos(A+B) + cos(A−B)]/2", "[cos(A−B) − cos(A+B)]/2"],
        ["[sin(A+B) + sin(A−B)]/2", "[sin(A+B) − sin(A−B)]/2",
         "[cos(A+B) + cos(A−B)]/2", "[cos(A−B) − cos(A+B)]/2"],
        "A", "easy", "factual",
        "Product-to-sum: sin A cos B = [sin(A+B) + sin(A−B)]/2.",
        "গুণফল→যোগ: sin A cos B = [sin(A+B) + sin(A−B)]/2।",
    ),
    q(
        "cos A cos B can be rewritten as:",
        "cos A cos B কে লেখা যায়:",
        ["[cos(A+B) + cos(A−B)]/2", "[cos(A+B) − cos(A−B)]/2",
         "[sin(A+B) + sin(A−B)]/2", "[sin(A+B) − sin(A−B)]/2"],
        ["[cos(A+B) + cos(A−B)]/2", "[cos(A+B) − cos(A−B)]/2",
         "[sin(A+B) + sin(A−B)]/2", "[sin(A+B) − sin(A−B)]/2"],
        "A", "easy", "factual",
        "Product-to-sum: cos A cos B = [cos(A+B) + cos(A−B)]/2.",
        "গুণফল→যোগ: cos A cos B = [cos(A+B) + cos(A−B)]/2।",
    ),
    q(
        "sin C + sin D equals:",
        "sin C + sin D এর মান:",
        ["2 sin((C+D)/2) cos((C−D)/2)", "2 cos((C+D)/2) cos((C−D)/2)",
         "2 sin((C+D)/2) sin((C−D)/2)", "2 cos((C+D)/2) sin((C−D)/2)"],
        ["2 sin((C+D)/2) cos((C−D)/2)", "2 cos((C+D)/2) cos((C−D)/2)",
         "2 sin((C+D)/2) sin((C−D)/2)", "2 cos((C+D)/2) sin((C−D)/2)"],
        "A", "easy", "factual",
        "Sum-to-product: sin C + sin D = 2 sin((C+D)/2) cos((C−D)/2).",
        "যোগ→গুণফল: sin C + sin D = 2 sin((C+D)/2) cos((C−D)/2)।",
    ),
    q(
        "cos C − cos D equals:",
        "cos C − cos D এর মান:",
        ["−2 sin((C+D)/2) sin((C−D)/2)", "2 cos((C+D)/2) cos((C−D)/2)",
         "2 sin((C+D)/2) cos((C−D)/2)", "−2 cos((C+D)/2) sin((C−D)/2)"],
        ["−2 sin((C+D)/2) sin((C−D)/2)", "2 cos((C+D)/2) cos((C−D)/2)",
         "2 sin((C+D)/2) cos((C−D)/2)", "−2 cos((C+D)/2) sin((C−D)/2)"],
        "A", "easy", "factual",
        "Sum-to-product: cos C − cos D = −2 sin((C+D)/2) sin((C−D)/2).",
        "যোগ→গুণফল: cos C − cos D = −2 sin((C+D)/2) sin((C−D)/2)।",
    ),
    q(
        "If tan S = 3/4, then 4 sin S − 3 cos S equals:",
        "tan S = 3/4 হলে 4 sin S − 3 cos S এর মান:",
        ["0", "1", "3", "5"],
        ["0", "1", "3", "5"],
        "A", "hard", "numerical",
        "Divide by cos S: expression = cos S (4 tan S − 3) = cos S (3 − 3) = 0.",
        "4 tan S − 3 = 0 ⇒ রাশি = 0।",
    ),
    q(
        "2 sin A cos A − cos 2A equals:",
        "2 sin A cos A − cos 2A এর মান:",
        ["sin 2A − cos 2A", "1", "0", "tan 2A"],
        ["sin 2A − cos 2A", "1", "0", "tan 2A"],
        "A", "easy", "conceptual",
        "2 sin A cos A = sin 2A ⇒ expression = sin 2A − cos 2A.",
        "2 sin A cos A = sin 2A ⇒ রাশি = sin 2A − cos 2A।",
    ),
    q(
        "If cos theta = (1/2)(a + 1/a), then cos 3theta equals:",
        "cos θ = (1/2)(a + 1/a) হলে cos 3θ এর মান:",
        ["(1/2)(a^3 + 1/a^3)", "(1/2)(a^2 + 1/a^2)",
         "(1/3)(a^3 + 1/a^3)", "(1/3)(a + 1/a)"],
        ["মান (1/2)(a^3 + 1/a^3)", "মান (1/2)(a^2 + 1/a^2)",
         "মান (1/3)(a^3 + 1/a^3)", "মান (1/3)(a + 1/a)"],
        "A", "hard", "numerical",
        "If cos θ = (a + 1/a)/2 then cos 3θ = (a³ + 1/a³)/2.",
        "cos θ = (a + 1/a)/2 হলে cos 3θ = (a³ + 1/a³)/2।",
    ),
    q(
        "sin 2A / (1 + cos 2A) equals:",
        "sin 2A / (1 + cos 2A) এর মান:",
        ["tan A", "cot A", "tan 2A", "cot 2A"],
        ["tan A", "cot A", "tan 2A", "cot 2A"],
        "A", "medium", "conceptual",
        "sin 2A = 2 sin A cos A; 1 + cos 2A = 2 cos² A ⇒ ratio = tan A.",
        "অনুপাত = (2 sin A cos A)/(2 cos² A) = tan A।",
    ),
    q(
        "(1 + cos theta) / sin theta equals:",
        "(1 + cos θ) / sin θ এর মান:",
        ["cot(theta/2)", "tan(theta/2)", "cot theta", "tan theta"],
        ["cot(θ/2)", "tan(θ/2)", "cot θ", "tan θ"],
        "A", "medium", "conceptual",
        "1 + cos θ = 2 cos²(θ/2); sin θ = 2 sin(θ/2) cos(θ/2) ⇒ ratio = cot(θ/2).",
        "অনুপাত = cot(θ/2)।",
    ),
    q(
        "If n is an integer, sin{2 n pi + (−1)^{2n} · (pi/6)} equals:",
        "n পূর্ণসংখ্যা হলে sin{2nπ + (−1)^{2n} · (π/6)} এর মান:",
        ["-1/2", "1/2", "-sqrt(3)/2", "sqrt(3)/2"],
        ["-1/2", "1/2", "-√3/2", "√3/2"],
        "B", "medium", "numerical",
        "(−1)^{2n} = 1 ⇒ sin(2nπ + π/6) = sin(π/6) = 1/2.",
        "(−1)^{2n} = 1 ⇒ sin(π/6) = 1/2।",
    ),
    q(
        "If cot theta > 0 and cos theta < 0 with cot theta = 3/4, then sin theta equals:",
        "cot θ > 0 ও cos θ < 0 এবং cot θ = 3/4 হলে sin θ এর মান:",
        ["3/5", "-3/5", "4/5", "-4/5"],
        ["3/5", "-3/5", "4/5", "-4/5"],
        "D", "medium", "numerical",
        "Third quadrant: |sin| = 4/5 and sin < 0 ⇒ sin θ = −4/5.",
        "তৃতীয় চতুর্ভাগে sin ঋণাত্মক ⇒ sin θ = −4/5।",
    ),
    q(
        "sqrt(2) sin(pi/4 + x) expands / equals in transformed form to:",
        "√2 sin(π/4 + x) রূপান্তরিত মান:",
        ["sin x + cos x", "sin x − cos x", "cos x − sin x", "−sin x − cos x"],
        ["sin x + cos x", "sin x − cos x", "cos x − sin x", "−sin x − cos x"],
        "A", "medium", "conceptual",
        "√2 sin(π/4 + x) = √2 (sin π/4 cos x + cos π/4 sin x) = cos x + sin x.",
        "√2 sin(π/4 + x) = sin x + cos x।",
    ),
    q(
        "tan A + cot A equals:",
        "tan A + cot A এর মান:",
        ["2 / sin 2A", "2 / cos 2A", "sin 2A", "cos 2A"],
        ["2 / sin 2A", "2 / cos 2A", "sin 2A", "cos 2A"],
        "A", "medium", "conceptual",
        "tan A + cot A = sin/cos + cos/sin = 1/(sin cos) = 2 / sin 2A.",
        "tan A + cot A = 2 / sin 2A।",
    ),
    q(
        "If cosec x = sqrt(5) and cot x = −2, which statement is true?",
        "cosec x = √5 এবং cot x = −2 হলে কোনটি সত্য?",
        ["tan x = 2", "sin x = 1/2", "sec x = 2", "cos x = −2/sqrt(5)"],
        ["tan x = 2", "sin x = 1/2", "sec x = 2", "cos x = −2/√5"],
        "D", "medium", "numerical",
        "Second quadrant: sin x = 1/√5 > 0, cos x = sin·cot = −2/√5.",
        "দ্বিতীয় চতুর্ভাগে cos x = −2/√5।",
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
    counts["hm1_27_ch07_t01"] = write_topic("hm1_27_ch07_t01", T01)["count"]
    counts["hm1_27_ch07_t02"] = write_topic("hm1_27_ch07_t02", T02)["count"]
    counts["hm1_27_ch07_t03"] = write_topic("hm1_27_ch07_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm1_27_ch07",
        "title_en": "Trigonometric Ratios of Associated Angles",
        "title_bn": "সংযুক্ত কোণের ত্রিকোণমিতিক অনুপাত",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(229, 241)],
        "topics": {
            "hm1_27_ch07_t01": {
                "title_en": "Sum and difference formulas",
                "title_bn": "যোগ ও বিয়োগ সূত্র",
                "udvash_types": ["T-01", "T-03", "associated angles", "sin/cos/tan(A±B)"],
                "count": 20,
            },
            "hm1_27_ch07_t02": {
                "title_en": "Multiple and half angles",
                "title_bn": "গুণিতক ও অর্ধকোণ",
                "udvash_types": ["T-04", "T-05", "double/triple angle", "half-angle"],
                "count": 20,
            },
            "hm1_27_ch07_t03": {
                "title_en": "Transformation of trigonometric expressions",
                "title_bn": "ত্রিকোণমিতিক রাশির রূপান্তর",
                "udvash_types": ["T-06", "product-sum", "sum-product", "expression rewrite"],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "figure_only_triangles": "Several stimulus figures (sides/angles unlabeled in OCR); rewritten as pure trig identities/numerical MCQs",
            "Q44_AplusB_ambiguous": "Printed A+B symbol OCR-ambiguous; curated as A+B=90° with tan A tan B=1",
            "Q02_options_garbled": "3cos20−4cos³20 options OCR-garbled; restored as −1/2 with clear distractors",
            "calculator_only_keys": "A few printed keys cite calculator; retained only when closed form matches",
        },
        "low_confidence": [
            "OCR on pp. 229–240 heavily noisy; column PNGs/answer keys used to reconstruct stems.",
            "Chapter mixes associated angles, compound angles, triangle applications; triangle figure items largely skipped or rewritten.",
            "Inline math stored as plain text (pi, deg, ^, sin/cos/tan) for JSONL.",
            "Some authored supplements fill to exactly 20/topic where printed stock was thin or unreadable.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm1_ch07.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch07_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
