#!/usr/bin/env python3
"""Seed Higher Mathematics 2nd Paper Ch05 (Binomial Expansion).

Curated from Udvash HSC Question Bank 2026 printed pp. 127–131 (PDF 133–137).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
OCR is noisy (~5 pages); reconstructs board-style items from solutions/column
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
    "higher_mathematics p2 ch05; curated bilingual"
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
# hm2_27_ch05_t01 — Binomial theorem / দ্বিপদী উপপাদ্য
# =============================================================================
T01 = [
    q(
        "The expansion of (x + y)^n has how many terms (n ∈ ℕ)?",
        "(x + y)^n এর বিস্তৃতিতে পদসংখ্যা কত (n ∈ ℕ)?",
        ["n", "n − 1", "n + 1", "2n"],
        ["n", "n − 1", "n + 1", "2n"],
        "C", "easy", "factual",
        "By the binomial theorem, (x + y)^n has n + 1 terms.",
        "দ্বিপদী উপপাদ্যানুসারে (x + y)^n এর পদসংখ্যা n + 1।",
    ),
    q(
        "In the expansion of (x + y)^n, the general term T_{r+1} is:",
        "(x + y)^n এর বিস্তৃতিতে সাধারণ পদ T_{r+1} কোনটি?",
        ["ⁿC_r x^{n−r} y^r", "ⁿC_r x^r y^{n−r}", "ⁿC_{r+1} x^{n−r} y^r", "ⁿC_r x^{n−r} y^{r+1}"],
        ["ⁿC_r x^{n−r} y^r", "ⁿC_r x^r y^{n−r}", "ⁿC_{r+1} x^{n−r} y^r", "ⁿC_r x^{n−r} y^{r+1}"],
        "A", "easy", "factual",
        "T_{r+1} = ⁿC_r x^{n−r} y^r for r = 0, 1, …, n.",
        "T_{r+1} = ⁿC_r x^{n−r} y^r; এখানে r = 0, 1, …, n।",
    ),
    q(
        "The binomial coefficient ⁿC_r equals:",
        "দ্বিপদী সহগ ⁿC_r এর মান কোনটি?",
        ["n! / (r!(n − r)!)", "n! / r!", "n! / (n − r)!", "(n − r)! / r!"],
        ["n! / (r!(n − r)!)", "n! / r!", "n! / (n − r)!", "(n − r)! / r!"],
        "A", "easy", "factual",
        "By definition ⁿC_r = n! / (r!(n − r)!) for 0 ≤ r ≤ n.",
        "সংজ্ঞা অনুসারে ⁿC_r = n! / (r!(n − r)!)।",
    ),
    q(
        "Which identity is always true?",
        "নিচের কোনটি সর্বদা সত্য?",
        ["ⁿC_r = ⁿC_{n−r}", "ⁿC_r = ⁿC_{r+1}", "ⁿC_r = ^{n+1}C_r", "ⁿC_r = ⁿC_{n+r}"],
        ["ⁿC_r = ⁿC_{n−r}", "ⁿC_r = ⁿC_{r+1}", "ⁿC_r = ^{n+1}C_r", "ⁿC_r = ⁿC_{n+r}"],
        "A", "easy", "conceptual",
        "Binomial coefficients are symmetric: ⁿC_r = ⁿC_{n−r}.",
        "দ্বিপদী সহগ প্রতিসম: ⁿC_r = ⁿC_{n−r}।",
    ),
    q(
        "Pascal’s identity states that:",
        "Pascal এর অভেদ কোনটি?",
        ["ⁿC_r + ⁿC_{r−1} = ^{n+1}C_r", "ⁿC_r + ⁿC_r = ^{n+1}C_r", "ⁿC_r − ⁿC_{r−1} = ^{n+1}C_r", "ⁿC_r · ⁿC_{r−1} = ^{n+1}C_r"],
        ["ⁿC_r + ⁿC_{r−1} = ^{n+1}C_r", "ⁿC_r + ⁿC_r = ^{n+1}C_r", "ⁿC_r − ⁿC_{r−1} = ^{n+1}C_r", "ⁿC_r · ⁿC_{r−1} = ^{n+1}C_r"],
        "A", "medium", "conceptual",
        "Pascal: ⁿC_r + ⁿC_{r−1} = ^{n+1}C_r.",
        "Pascal: ⁿC_r + ⁿC_{r−1} = ^{n+1}C_r।",
    ),
    q(
        "Expanding (x − y)^n, the first term is:",
        "(x − y)^n বিস্তৃতিতে প্রথম পদ কোনটি?",
        ["x^n", "y^n", "(−y)^n", "n x^{n−1} y"],
        ["x^n", "y^n", "(−y)^n", "n x^{n−1} y"],
        "A", "easy", "factual",
        "T_1 corresponds to r = 0: ⁿC_0 x^n (−y)^0 = x^n.",
        "r = 0 হলে প্রথম পদ = x^n।",
    ),
    q(
        "In (x − y)^n, the third term is:",
        "(x − y)^n এর বিস্তৃতিতে তৃতীয় পদ কোনটি?",
        ["ⁿC_2 x^{n−2} y^2", "−ⁿC_2 x^{n−2} y^2", "ⁿC_3 x^{n−3} y^3", "−ⁿC_1 x^{n−1} y"],
        ["ⁿC_2 x^{n−2} y^2", "−ⁿC_2 x^{n−2} y^2", "ⁿC_3 x^{n−3} y^3", "−ⁿC_1 x^{n−1} y"],
        "A", "medium", "numerical",
        "T_3 = ⁿC_2 x^{n−2} (−y)^2 = ⁿC_2 x^{n−2} y^2.",
        "T_3 = ⁿC_2 x^{n−2} (−y)^2 = ⁿC_2 x^{n−2} y^2।",
    ),
    q(
        "For (x − y)^n with n odd, which statements are true? (i) first term = x^n (ii) third term = ⁿC_2 x^{n−2} y^2 (iii) there are two middle terms",
        "(x − y)^n এ n বিজোড় হলে— (i) প্রথম পদ = x^n (ii) তৃতীয় পদ = ⁿC_2 x^{n−2} y^2 (iii) মধ্যপদ দুটি — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "All three hold: first term x^n, T_3 is positive, and odd n gives two middle terms.",
        "তিনটিই সত্য: প্রথম পদ x^n, T_3 ধনাত্মক, এবং বিজোড় n এ মধ্যপদ দুটি।",
    ),
    q(
        "The coefficient of x^3 in (1 + x)^5 is:",
        "(1 + x)^5 এর বিস্তৃতিতে x^3 এর সহগ কত?",
        ["5", "10", "15", "20"],
        ["5", "10", "15", "20"],
        "B", "easy", "numerical",
        "Coeff = ⁵C_3 = 10.",
        "সহগ = ⁵C_3 = 10।",
    ),
    q(
        "The coefficient of x^3 in (1 − 2x)^5 is:",
        "(1 − 2x)^5 এর বিস্তৃতিতে x^3 এর সহগ কত?",
        ["−80", "−10", "10", "80"],
        ["−80", "−10", "10", "80"],
        "A", "medium", "numerical",
        "⁵C_3 (−2)^3 = 10 × (−8) = −80.",
        "⁵C_3 (−2)^3 = 10 × (−8) = −80।",
    ),
    q(
        "If the coefficient of x^4 in (2a + x)^5 is 40, then a equals:",
        "(2a + x)^5 এর বিস্তৃতিতে x^4 এর সহগ 40 হলে a এর মান কত?",
        ["1", "√2", "2", "4"],
        ["1", "√2", "2", "4"],
        "D", "medium", "numerical",
        "⁵C_4 (2a) = 5 · 2a = 10a = 40 ⇒ a = 4.",
        "10a = 40 ⇒ a = 4।",
    ),
    q(
        "The fourth term in the expansion of (3 − x^2)^7 is:",
        "(3 − x^2)^7 এর বিস্তৃতিতে ৪র্থ পদ কোনটি?",
        ["−2835 x^6", "−35 x^6", "35 x^6", "2835 x^6"],
        ["−2835 x^6", "−35 x^6", "35 x^6", "2835 x^6"],
        "A", "hard", "numerical",
        "T_4 = ⁷C_3 3^4 (−x^2)^3 = 35 · 81 · (−x^6) = −2835 x^6.",
        "T_4 = ⁷C_3 3^4 (−x^2)^3 = −2835 x^6।",
    ),
    q(
        "In (x + 5)^13, which statements are true? (i) number of terms = 14 (ii) third term = 1950 x^{11} (iii) the 8th term is a middle term",
        "(x + 5)^13 এর বিস্তৃতিতে— (i) পদসংখ্যা = 14 (ii) ৩য় পদ = 1950 x^{11} (iii) ৮ম পদ একটি মধ্যপদ — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "Terms = 14; T_3 = ¹³C_2 x^{11} 5^2 = 1950 x^{11}; n odd ⇒ middle are 7th and 8th.",
        "পদ 14; T_3 = 1950 x^{11}; বিজোড় n এ মধ্যপদ ৭ম ও ৮ম।",
    ),
    q(
        "The sum of binomial coefficients in (1 + x)^n is:",
        "(1 + x)^n এর দ্বিপদী সহগসমূহের সমষ্টি কত?",
        ["n", "2^n", "n!", "n 2^{n−1}"],
        ["n", "2^n", "n!", "n 2^{n−1}"],
        "B", "easy", "conceptual",
        "Putting x = 1: (1 + 1)^n = 2^n = Σ ⁿC_r.",
        "x = 1 বসালে (1 + 1)^n = 2^n = Σ ⁿC_r।",
    ),
    q(
        "The value of ⁿC_0 + ⁿC_1 + … + ⁿC_n equals:",
        "ⁿC_0 + ⁿC_1 + … + ⁿC_n এর মান কত?",
        ["2^{n−1}", "2^n", "2^{n+1}", "n 2^n"],
        ["2^{n−1}", "2^n", "2^{n+1}", "n 2^n"],
        "B", "easy", "factual",
        "Same as the sum of coefficients of (1 + x)^n at x = 1, which is 2^n.",
        "(1 + x)^n এ x = 1 বসালে সমষ্টি 2^n।",
    ),
    q(
        "If ⁿC_2 = ⁿC_3, then n equals:",
        "ⁿC_2 = ⁿC_3 হলে n এর মান কত?",
        ["3", "4", "5", "6"],
        ["3", "4", "5", "6"],
        "C", "medium", "numerical",
        "ⁿC_2 = ⁿC_3 ⇒ n = 2 + 3 = 5.",
        "ⁿC_2 = ⁿC_3 ⇒ n = 5।",
    ),
    q(
        "In (x + 1/x)^5, the power of x in T_{r+1} is 5 − 2r. For the term containing x^1, r equals:",
        "(x + 1/x)^5 এ T_{r+1} এর x এর সূচক 5 − 2r। x^1 যুক্ত পদের জন্য r কত?",
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        "B", "medium", "numerical",
        "5 − 2r = 1 ⇒ 2r = 4 ⇒ r = 2.",
        "5 − 2r = 1 ⇒ r = 2।",
    ),
    q(
        "(a − b)^7 expanded has fifth term equal to:",
        "(a − b)^7 এর বিস্তৃতিতে ৫ম পদ কোনটি?",
        ["−35 a^3 b^4", "35 a^3 b^4", "−21 a^2 b^5", "21 a^4 b^3"],
        ["−35 a^3 b^4", "35 a^3 b^4", "−21 a^2 b^5", "21 a^4 b^3"],
        "B", "medium", "numerical",
        "T_5 = ⁷C_4 a^3 (−b)^4 = 35 a^3 b^4.",
        "T_5 = ⁷C_4 a^3 (−b)^4 = 35 a^3 b^4।",
    ),
    q(
        "For every n ≥ 0, the value of ⁿC_0 is:",
        "প্রতিটি n ≥ 0 এর জন্য ⁿC_0 এর মান কত?",
        ["0", "1", "n", "n!"],
        ["0", "1", "n", "n!"],
        "B", "easy", "factual",
        "ⁿC_0 = 1 for every n ≥ 0.",
        "প্রতিটি n ≥ 0 এর জন্য ⁿC_0 = 1।",
    ),
    q(
        "Which expansion matches the binomial theorem for positive integer n?",
        "ধনাত্মক পূর্ণসংখ্যা n এর জন্য দ্বিপদী উপপাদ্য কোনটি?",
        [
            "(a + b)^n = Σ_{r=0}^n ⁿC_r a^{n−r} b^r",
            "(a + b)^n = Σ_{r=1}^n ⁿC_r a^{n−r} b^r",
            "(a + b)^n = Σ ⁿC_r a^r b^r",
            "(a + b)^n = a^n + b^n only",
        ],
        [
            "(a + b)^n = Σ_{r=0}^n ⁿC_r a^{n−r} b^r",
            "(a + b)^n = Σ_{r=1}^n ⁿC_r a^{n−r} b^r",
            "(a + b)^n = Σ ⁿC_r a^r b^r",
            "(a + b)^n = a^n + b^n কেবল",
        ],
        "A", "easy", "factual",
        "Standard binomial theorem: (a + b)^n = Σ_{r=0}^n ⁿC_r a^{n−r} b^r.",
        "দ্বিপদী উপপাদ্য: (a + b)^n = Σ_{r=0}^n ⁿC_r a^{n−r} b^r।",
    ),
]


# =============================================================================
# hm2_27_ch05_t02 — General and middle terms / সাধারণ ও মধ্যপদ
# =============================================================================
T02 = [
    q(
        "If n is even, the middle term in (x + y)^n is the:",
        "n জোড় হলে (x + y)^n এর মধ্যপদ কততম?",
        ["(n/2)th term", "(n/2 + 1)th term", "(n + 1)th term", "(n − 1)th term"],
        ["(n/2) তম পদ", "(n/2 + 1) তম পদ", "(n + 1) তম পদ", "(n − 1) তম পদ"],
        "B", "easy", "factual",
        "For even n there is one middle term: the (n/2 + 1)th term.",
        "জোড় n এ এক মধ্যপদ: (n/2 + 1) তম পদ।",
    ),
    q(
        "If n is odd, the two middle terms of (x + y)^n are:",
        "n বিজোড় হলে (x + y)^n এর দুই মধ্যপদ কোনটি?",
        [
            "((n + 1)/2)th and ((n + 3)/2)th",
            "(n/2)th and (n/2 + 1)th",
            "nth and (n + 1)th",
            "1st and last",
        ],
        [
            "((n + 1)/2) তম ও ((n + 3)/2) তম",
            "(n/2) তম ও (n/2 + 1) তম",
            "n তম ও (n + 1) তম",
            "১ম ও শেষ",
        ],
        "A", "easy", "factual",
        "Odd n ⇒ middle terms ((n + 1)/2)th and ((n + 3)/2)th.",
        "বিজোড় n ⇒ মধ্যপদ ((n + 1)/2) ও ((n + 3)/2) তম।",
    ),
    q(
        "In the expansion of (√x + 1/√x)^6, the middle term is the:",
        "(√x + 1/√x)^6 এর বিস্তৃতিতে মধ্যপদ কততম?",
        ["3rd", "4th", "5th", "6th"],
        ["৩য়", "৪র্থ", "৫ম", "৬ষ্ঠ"],
        "B", "medium", "numerical",
        "n = 6 even ⇒ one middle term = (6/2 + 1) = 4th term.",
        "n = 6 জোড় ⇒ মধ্যপদ = ৪র্থ পদ।",
    ),
    q(
        "In (2 + x)^17, the two middle terms are:",
        "(2 + x)^17 এর বিস্তৃতিতে মধ্যপদ দুটি কোনটি?",
        ["7th and 8th", "8th and 9th", "9th and 10th", "10th and 11th"],
        ["৭ম ও ৮ম", "৮ম ও ৯ম", "৯ম ও ১০ম", "১০ম ও ১১ম"],
        "C", "medium", "numerical",
        "n = 17 odd ⇒ 9th and 10th terms.",
        "n = 17 বিজোড় ⇒ ৯ম ও ১০ম পদ।",
    ),
    q(
        "For (a + bx)^{2n}, the middle term is the:",
        "(a + bx)^{2n} এর সম্প্রসারণে মধ্যপদ কততম?",
        ["(n − 1)th", "(n + 1)th", "(2n)th", "(2n + 1)th"],
        ["(n − 1) তম", "(n + 1) তম", "2n তম", "(2n + 1) তম"],
        "B", "easy", "factual",
        "Exponent 2n is even ⇒ middle = (2n/2 + 1) = (n + 1)th term.",
        "ঘাত 2n জোড় ⇒ মধ্যপদ = (n + 1) তম।",
    ),
    q(
        "Stimulus: (1 − 2x)^11. The middle term(s) of the expansion are:",
        "উদ্দীপক: (1 − 2x)^11। বিস্তৃতিতে মধ্যপদ কোনটি?",
        ["5th only", "6th only", "5th and 6th", "6th and 7th"],
        ["শুধু ৫ম", "শুধু ৬ষ্ঠ", "৫ম ও ৬ষ্ঠ", "৬ষ্ঠ ও ৭ম"],
        "D", "medium", "numerical",
        "n = 11 odd ⇒ middle = 6th and 7th terms.",
        "n = 11 বিজোড় ⇒ মধ্যপদ ৬ষ্ঠ ও ৭ম।",
    ),
    q(
        "Stimulus: (1 − 2x)^11. The coefficient of the 6th term is:",
        "উদ্দীপক: (1 − 2x)^11। ৬ষ্ঠ পদের সহগ কত?",
        ["−14784", "−462", "462", "14784"],
        ["−14784", "−462", "462", "14784"],
        "A", "hard", "numerical",
        "T_6 = ¹¹C_5 (−2)^5 = 462 · (−32) = −14784.",
        "T_6 = ¹¹C_5 (−2)^5 = −14784।",
    ),
    q(
        "The middle term of (x − 1/x)^8 equals:",
        "(x − 1/x)^8 এর মধ্যপদের মান কত?",
        ["−70", "−56", "56", "70"],
        ["−70", "−56", "56", "70"],
        "D", "medium", "numerical",
        "n = 8 even ⇒ T_5 = ⁸C_4 x^4 (−1/x)^4 = 70.",
        "মধ্যপদ T_5 = ⁸C_4 = 70।",
    ),
    q(
        "In (2x + 1/x)^10, which term is independent of x?",
        "(2x + 1/x)^10 এর বিস্তৃতিতে কত তম পদটি x বর্জিত?",
        ["5th", "6th", "10th", "11th"],
        ["৫ম", "৬ষ্ঠ", "১০ম", "১১ম"],
        "B", "medium", "numerical",
        "T_{r+1}: power 10 − 2r = 0 ⇒ r = 5 ⇒ 6th term.",
        "10 − 2r = 0 ⇒ r = 5 ⇒ ৬ষ্ঠ পদ।",
    ),
    q(
        "In (x − 1/x^2)^9, the term independent of x has value:",
        "(x − 1/x^2)^9 এর বিস্তৃতিতে x বর্জিত পদের মান কত?",
        ["−84", "−36", "36", "84"],
        ["−84", "−36", "36", "84"],
        "A", "hard", "numerical",
        "9 − 3r = 0 ⇒ r = 3; value = ⁹C_3 (−1)^3 = −84.",
        "9 − 3r = 0 ⇒ r = 3; মান = −84।",
    ),
    q(
        "The general term of (x + y)^{20} that contains x^{11} is T_{r+1} with r equal to:",
        "(x + y)^{20} এ x^{11} যুক্ত পদের জন্য r এর মান কত (T_{r+1})?",
        ["8", "9", "10", "11"],
        ["8", "9", "10", "11"],
        "B", "medium", "numerical",
        "20 − r = 11 ⇒ r = 9 ⇒ T_{10}.",
        "20 − r = 11 ⇒ r = 9।",
    ),
    q(
        "In (x + y)^{20}, the exponent of x in the 11th term is:",
        "(x + y)^{20} এর বিস্তৃতিতে ১১তম পদে x এর সূচক কত?",
        ["12", "11", "10", "9"],
        ["12", "11", "10", "9"],
        "C", "easy", "numerical",
        "T_11 has r = 10: x^{20−10} = x^{10}.",
        "T_11 এ r = 10 ⇒ x^{10}।",
    ),
    q(
        "For (x + y)^{15}, how many middle terms are there?",
        "(x + y)^{15} এর বিস্তৃতিতে মধ্যপদ কয়টি?",
        ["1", "2", "3", "0"],
        ["1", "2", "3", "0"],
        "B", "easy", "factual",
        "n = 15 odd ⇒ two middle terms.",
        "n = 15 বিজোড় ⇒ মধ্যপদ দুটি।",
    ),
    q(
        "In (x^2 − 2/x)^6, which term is independent of x?",
        "(x^2 − 2/x)^6 এর বিস্তৃতিতে x বর্জিত পদ কততম?",
        ["3rd", "4th", "5th", "6th"],
        ["৩য়", "৪র্থ", "৫ম", "৬ষ্ঠ"],
        "C", "hard", "numerical",
        "Power 12 − 3r = 0 ⇒ r = 4 ⇒ 5th term.",
        "12 − 3r = 0 ⇒ r = 4 ⇒ ৫ম পদ।",
    ),
    q(
        "The term independent of x in (√x − 1/(2√x))^{10} occurs when r equals:",
        "(√x − 1/(2√x))^{10} এ x বর্জিত পদের জন্য r এর মান কত?",
        ["3", "4", "5", "6"],
        ["3", "4", "5", "6"],
        "C", "hard", "numerical",
        "Power of x: (10 − 2r)/2 = 0 ⇒ r = 5.",
        "(10 − 2r)/2 = 0 ⇒ r = 5।",
    ),
    q(
        "In (x + y)^{2n} with n ∈ ℕ, the middle term is:",
        "n ∈ ℕ হলে (x + y)^{2n} এর মধ্যপদ কোনটি?",
        ["(n − 1)th", "nth", "(n + 1)th", "(2n)th"],
        ["(n − 1) তম", "n তম", "(n + 1) তম", "2n তম"],
        "C", "easy", "factual",
        "Even exponent 2n ⇒ single middle term (n + 1)th.",
        "জোড় ঘাত 2n ⇒ মধ্যপদ (n + 1) তম।",
    ),
    q(
        "Which is the general (r + 1)th term of (2x − 3y)^n?",
        "(2x − 3y)^n এর সাধারণ (r + 1) তম পদ কোনটি?",
        [
            "ⁿC_r (2x)^{n−r} (−3y)^r",
            "ⁿC_r (2x)^r (−3y)^{n−r}",
            "ⁿC_r (2x)^{n−r} (3y)^r",
            "ⁿC_r 2^{n−r} x (−3)^r",
        ],
        [
            "ⁿC_r (2x)^{n−r} (−3y)^r",
            "ⁿC_r (2x)^r (−3y)^{n−r}",
            "ⁿC_r (2x)^{n−r} (3y)^r",
            "ⁿC_r 2^{n−r} x (−3)^r",
        ],
        "A", "medium", "conceptual",
        "T_{r+1} = ⁿC_r (2x)^{n−r} (−3y)^r.",
        "T_{r+1} = ⁿC_r (2x)^{n−r} (−3y)^r।",
    ),
    q(
        "For (x + y)^{18}, the middle term number is:",
        "(x + y)^{18} এর মধ্যপদ কততম?",
        ["9th", "10th", "11th", "18th"],
        ["৯ম", "১০ম", "১১ম", "১৮ম"],
        "B", "easy", "numerical",
        "n = 18 even ⇒ middle = 18/2 + 1 = 10th term.",
        "মধ্যপদ = ১০ম পদ।",
    ),
    q(
        "In (x + y)^{19}, the two middle terms are the:",
        "(x + y)^{19} এর দুই মধ্যপদ কোনটি?",
        ["9th and 10th", "10th and 11th", "11th and 12th", "19th and 20th"],
        ["৯ম ও ১০ম", "১০ম ও ১১ম", "১১ম ও ১২ম", "১৯ম ও ২০ম"],
        "B", "easy", "numerical",
        "((19 + 1)/2) = 10th and ((19 + 3)/2) = 11th.",
        "মধ্যপদ ১০ম ও ১১ম।",
    ),
    q(
        "In (x − 1/x)^{12}, the term independent of x has value:",
        "(x − 1/x)^{12} এর বিস্তৃতিতে x বর্জিত পদের মান কত?",
        ["−924", "924", "792", "990"],
        ["−924", "924", "792", "990"],
        "B", "hard", "numerical",
        "12 − 2r = 0 ⇒ r = 6; value = ¹²C_6 (−1)^6 = 924.",
        "r = 6 ⇒ মান = ¹²C_6 = 924।",
    ),
]


# =============================================================================
# hm2_27_ch05_t03 — Applications of binomial expansion / দ্বিপদী বিস্তৃতির প্রয়োগ
# =============================================================================
T03 = [
    q(
        "In (x + 1)^{30}, if the coefficient of the rth term equals that of the (r + 6)th term, then r equals:",
        "(x + 1)^{30} এর বিস্তৃতিতে r তম পদের সহগ (r + 6) তম পদের সহগের সমান হলে r এর মান কত?",
        ["12", "13", "27", "28"],
        ["12", "13", "27", "28"],
        "B", "hard", "numerical",
        "³⁰C_{r−1} = ³⁰C_{r+5} ⇒ (r − 1) + (r + 5) = 30 ⇒ 2r + 4 = 30 ⇒ r = 13.",
        "2r + 4 = 30 ⇒ r = 13।",
    ),
    q(
        "If the 4th and 5th terms in (1 + x)^8 are equal, then x equals:",
        "(1 + x)^8 এর বিস্তৃতিতে ৪র্থ ও ৫ম পদ সমান হলে x এর মান কত?",
        ["3/5", "4/5", "5/4", "5/3"],
        ["3/5", "4/5", "5/4", "5/3"],
        "B", "medium", "numerical",
        "⁸C_3 x^3 = ⁸C_4 x^4 ⇒ x = ⁸C_3/⁸C_4 = 56/70 = 4/5.",
        "x = ⁸C_3/⁸C_4 = 4/5।",
    ),
    q(
        "The expansion of (1 + 2x)^{−2} is valid when:",
        "(1 + 2x)^{−2} এর বিস্তৃতি কখন বৈধ?",
        ["|x| > 1/2", "|x| < 1/2", "|x| ≤ 1/2", "|x| ≥ 1/2"],
        ["|x| > 1/2", "|x| < 1/2", "|x| ≤ 1/2", "|x| ≥ 1/2"],
        "B", "medium", "conceptual",
        "Need |2x| < 1 ⇒ |x| < 1/2.",
        "|2x| < 1 ⇒ |x| < 1/2।",
    ),
    q(
        "In (1 + 2x)^{−2}, the coefficient of x^n is:",
        "(1 + 2x)^{−2} এর বিস্তৃতিতে x^n এর সহগ কোনটি?",
        ["(−2)^n n", "(−2)^n (n + 1)", "(−1)^n (n + 1)", "(−1)^n n"],
        ["(−2)^n n", "(−2)^n (n + 1)", "(−1)^n (n + 1)", "(−1)^n n"],
        "B", "hard", "numerical",
        "(1 + u)^{−2} has coeff (−1)^n (n + 1) for u^n; with u = 2x get (−2)^n (n + 1).",
        "সহগ = (−2)^n (n + 1)।",
    ),
    q(
        "The sum of the coefficients of the first three terms of −x(1 + x)^{−1} is:",
        "−x(1 + x)^{−1} এর বিস্তৃতিতে প্রথম তিনটি পদের সহগের সমষ্টি কত?",
        ["−3", "−1", "1", "3"],
        ["−3", "−1", "1", "3"],
        "B", "hard", "numerical",
        "−x(1 − x + x^2 − …) = −x + x^2 − x^3 + …; coeffs −1 + 1 − 1 = −1.",
        "সহগসমূহ −1, 1, −1; সমষ্টি −1।",
    ),
    q(
        "If (1 − x)^{−3} = 1 + 3x + 6x^2 + 10x^3 + 15x^4 + …, the coefficient of the 5th term is:",
        "(1 − x)^{−3} = 1 + 3x + 6x^2 + 10x^3 + 15x^4 + … হলে ৫ম পদের সহগ কত?",
        ["−15", "−10", "10", "15"],
        ["−15", "−10", "10", "15"],
        "D", "medium", "numerical",
        "5th term is 15x^4, so coefficient 15.",
        "৫ম পদ 15x^4; সহগ 15।",
    ),
    q(
        "If 1 − 3x + 6x^2 − 10x^3 + 15x^4 − … equals (1 + x)^n, then n is:",
        "1 − 3x + 6x^2 − 10x^3 + 15x^4 − … = (1 + x)^n হলে n এর মান কত?",
        ["−2", "−3", "2", "3"],
        ["−2", "−3", "2", "3"],
        "B", "medium", "conceptual",
        "The series matches (1 + x)^{−3}.",
        "ধারাটি (1 + x)^{−3} এর সাথে মিলে; n = −3।",
    ),
    q(
        "The binomial expansion of (1 + x)^α (α not a non-negative integer) converges absolutely when:",
        "(1 + x)^α (α অঋণাত্মক পূর্ণসংখ্যা নয়) এর বিস্তৃতি পরমভাবে অভিসারী হবে যখন:",
        ["−1 ≤ x ≤ 1", "−1 < x < 1", "x > 1", "x < −1"],
        ["−1 ≤ x ≤ 1", "−1 < x < 1", "x > 1", "x < −1"],
        "B", "medium", "conceptual",
        "Absolute convergence requires −1 < x < 1.",
        "পরম অভিসরণের জন্য −1 < x < 1 প্রয়োজন।",
    ),
    q(
        "If the coefficients of x^3 and x^4 in (a + x)^5 are equal, then a equals:",
        "(a + x)^5 এ x^3 ও x^4 এর সহগ সমান হলে a এর মান কত?",
        ["1/2", "1", "3/2", "2"],
        ["1/2", "1", "3/2", "2"],
        "A", "medium", "numerical",
        "⁵C_3 a^2 = ⁵C_4 a ⇒ 10a^2 = 5a ⇒ a = 1/2 (a ≠ 0).",
        "10a^2 = 5a ⇒ a = 1/2।",
    ),
    q(
        "If in (b + 2x)^5 the coefficient of x^3 is 320, then b equals:",
        "(b + 2x)^5 এর বিস্তৃতিতে x^3 এর সহগ 320 হলে b এর মান কত?",
        ["±4", "±2", "4", "−2"],
        ["±4", "±2", "4", "−2"],
        "B", "hard", "numerical",
        "⁵C_3 b^2 2^3 = 10 · b^2 · 8 = 80b^2 = 320 ⇒ b^2 = 4 ⇒ b = ±2.",
        "80b^2 = 320 ⇒ b = ±2।",
    ),
    q(
        "The coefficient of x^{16} in (x^2 + 2x)^{10} is:",
        "(x^2 + 2x)^{10} এর বিস্তৃতিতে x^{16} এর সহগ কত?",
        ["3360", "3630", "6360", "6330"],
        ["3360", "3630", "6360", "6330"],
        "A", "hard", "numerical",
        "Power 20 − r = 16 ⇒ r = 4; coeff = ¹⁰C_4 (2)^4 = 210 · 16 = 3360.",
        "r = 4 হলে সহগ = ¹⁰C_4 · 2^4 = 3360।",
    ),
    q(
        "The coefficient of x^r in (1 − x)^{−1} is:",
        "(1 − x)^{−1} এর বিস্তৃতিতে x^r এর সহগ কত?",
        ["(−1)^r", "1", "r + 1", "(−1)^r (r + 1)"],
        ["(−1)^r", "1", "r + 1", "(−1)^r (r + 1)"],
        "B", "easy", "factual",
        "(1 − x)^{−1} = Σ x^r, so every coefficient is 1.",
        "(1 − x)^{−1} = Σ x^r; সহগ সর্বদা 1।",
    ),
    q(
        "If y = x − x^2 + x^3 − … (|x| < 1), then (1 − y)^{−1} equals:",
        "y = x − x^2 + x^3 − … (|x| < 1) হলে (1 − y)^{−1} কত?",
        ["1 − x", "1 + x", "(1 + x)^{−1}", "(1 − x)^{−1}"],
        ["1 − x", "1 + x", "(1 + x)^{−1}", "(1 − x)^{−1}"],
        "B", "hard", "application",
        "y = x/(1 + x) ⇒ 1 − y = 1/(1 + x) ⇒ (1 − y)^{−1} = 1 + x.",
        "y = x/(1 + x) ⇒ (1 − y)^{−1} = 1 + x।",
    ),
    q(
        "The coefficient of the 4th term in (1 − y)^5 is:",
        "(1 − y)^5 এর বিস্তৃতির ৪র্থ পদের সহগ কত?",
        ["10", "−10", "5", "−5"],
        ["10", "−10", "5", "−5"],
        "B", "easy", "numerical",
        "T_4 coefficient = (−1)^3 ⁵C_3 = −10.",
        "সহগ = (−1)^3 ⁵C_3 = −10।",
    ),
    q(
        "How many terms are in the expansion of (1 − x^2)^n when n ∈ ℕ?",
        "n ∈ ℕ হলে (1 − x^2)^n এর বিস্তৃতিতে পদ কয়টি?",
        ["2(n + 1)", "2n + 1", "2n", "n + 1"],
        ["2(n + 1)", "2n + 1", "2n", "n + 1"],
        "D", "easy", "conceptual",
        "(1 − x^2)^n is a binomial of degree n, so it has n + 1 terms.",
        "(1 − x^2)^n এ পদসংখ্যা n + 1।",
    ),
    q(
        "In (3x^2 − 2/x)^5, the coefficient of x is:",
        "(3x^2 − 2/x)^5 এর বিস্তৃতিতে x এর সহগ কোনটি?",
        ["−720", "−90", "90", "720"],
        ["−720", "−90", "90", "720"],
        "A", "hard", "numerical",
        "10 − 3r = 1 ⇒ r = 3; coeff = ⁵C_3 3^2 (−2)^3 = 10 · 9 · (−8) = −720.",
        "r = 3 হলে সহগ = −720।",
    ),
    q(
        "If the coefficients of the 6th and 7th terms of (2 + x)^{11} are equal, then x equals:",
        "(2 + x)^{11} এ ৬ষ্ঠ ও ৭ম পদের সহগ সমান হলে x এর মান কত?",
        ["1", "2", "1/2", "4"],
        ["1", "2", "1/2", "4"],
        "B", "hard", "numerical",
        "¹¹C_5 2^6 x^5 = ¹¹C_6 2^5 x^6 ⇒ x = 2 · ¹¹C_5/¹¹C_6 = 2.",
        "x = 2 · ¹¹C_5/¹¹C_6 = 2।",
    ),
    q(
        "Approximating (1.01)^{10} by the first three terms of the binomial expansion gives approximately:",
        "দ্বিপদী বিস্তৃতির প্রথম তিন পদ দিয়ে (1.01)^{10} এর আনুমানিক মান কোনটি?",
        ["1.100", "1.1045", "1.105", "1.01"],
        ["1.100", "1.1045", "1.105", "1.01"],
        "B", "medium", "application",
        "(1 + 0.01)^{10} ≈ 1 + 10(0.01) + 45(0.01)^2 = 1.1045.",
        "≈ 1 + 0.1 + 0.0045 = 1.1045।",
    ),
    q(
        "Using (1 − x)^{−1} ≈ 1 + x + x^2 for small x, an approximation of 1/0.98 is closest to:",
        "ক্ষুদ্র x এর জন্য (1 − x)^{−1} ≈ 1 + x + x^2 ব্যবহার করে 1/0.98 এর নিকটতম মান কোনটি?",
        ["1.02", "1.0204", "0.98", "1.04"],
        ["1.02", "1.0204", "0.98", "1.04"],
        "B", "medium", "application",
        "1/0.98 = (1 − 0.02)^{−1} ≈ 1 + 0.02 + 0.0004 = 1.0204.",
        "≈ 1 + 0.02 + 0.0004 = 1.0204।",
    ),
    q(
        "In (y + 1)^{2n}, the coefficient of y^{n+1} is:",
        "(y + 1)^{2n} এর বিস্তারে y^{n+1} এর সহগ কোনটি?",
        ["^{2n}C_{n−1}", "^{2n}C_n", "^{2n}C_{n+1}", "^{2n}C_{2n}"],
        ["^{2n}C_{n−1}", "^{2n}C_n", "^{2n}C_{n+1}", "^{2n}C_{2n}"],
        "C", "medium", "numerical",
        "(y + 1)^{2n} = Σ ^{2n}C_k y^k, so the coefficient of y^{n+1} is ^{2n}C_{n+1}.",
        "সহগ = ^{2n}C_{n+1}।",
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
    counts["hm2_27_ch05_t01"] = write_topic("hm2_27_ch05_t01", T01)["count"]
    counts["hm2_27_ch05_t02"] = write_topic("hm2_27_ch05_t02", T02)["count"]
    counts["hm2_27_ch05_t03"] = write_topic("hm2_27_ch05_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm2_27_ch05",
        "title_en": "Binomial Expansion",
        "title_bn": "দ্বিপদী বিস্তৃতি",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(127, 132)],
        "topics": {
            "hm2_27_ch05_t01": {
                "title_en": "Binomial theorem",
                "title_bn": "দ্বিপদী উপপাদ্য",
                "udvash_types": [
                    "binomial theorem statement and term count",
                    "binomial coefficients and Pascal identity",
                    "expansion of (x±y)^n and coefficient extraction",
                    "sum of coefficients and symmetry ⁿC_r = ⁿC_{n−r}",
                ],
                "count": 20,
            },
            "hm2_27_ch05_t02": {
                "title_en": "General and middle terms",
                "title_bn": "সাধারণ ও মধ্যপদ",
                "udvash_types": [
                    "general term T_{r+1}",
                    "middle term(s) for even/odd n",
                    "term independent of x",
                    "stimulus-linked middle term and coefficient",
                ],
                "count": 20,
            },
            "hm2_27_ch05_t03": {
                "title_en": "Applications of binomial expansion",
                "title_bn": "দ্বিপদী বিস্তৃতির প্রয়োগ",
                "udvash_types": [
                    "equal consecutive terms and finding x or a",
                    "infinite binomial series and validity |x|<1",
                    "negative-index expansions and coefficient formulas",
                    "numerical approximation via truncated expansion",
                ],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "garbled_stems": "Noisy OCR reconstructed from answer-key algebra and standard board forms",
            "figure_graphs": "No figure-dependent items in ch05 MCQ block",
            "stimulus_pairs": "Linked stimulus blocks curated as clear standalone stems",
            "ambiguous_option_glyphs": "Broken Bangla/option glyphs replaced with closed-form HSC standards",
        },
        "low_confidence": [
            "OCR on pp. 127–131 noisy; column text and solution lines used to reconstruct stems.",
            "Inline math stored as plain text (ⁿC_r, fractions, exponents) for JSONL.",
            "Some printed multi-select glyph keys incomplete; properties rewritten clearly.",
            "A few infinite-series option glyphs standardized to closed algebraic forms.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm2_ch05.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
        "math2_progress": {
            "topics_complete": "15/30",
            "note": "Ch05 continues higher_mathematics 2nd paper after Ch01–Ch04 (240Q)",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch05_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
