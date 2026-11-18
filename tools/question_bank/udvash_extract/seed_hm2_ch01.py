#!/usr/bin/env python3
"""Seed Higher Mathematics 2nd Paper Ch01 (Real Numbers and Inequalities).

Curated from Udvash HSC Question Bank 2026 printed pp. 24–28 (PDF 30–34).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
OCR is noisy (~5 pages); reconstructs board-style items from solutions/column
text and supplements with accurate HSC-level authored MCQs. Figure-only
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
PARSED = ROOT / "content" / "bank" / "udvash_raw" / "higher_mathematics_2" / "parsed"
SOURCE = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "higher_mathematics p2 ch01; curated bilingual"
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
# hm2_27_ch01_t01 — Real numbers and intervals / বাস্তব সংখ্যা ও ব্যবধান
# =============================================================================
T01 = [
    q(
        "If S = {x : x ∈ Z and 8 < x² < 27}, then the greatest lower bound of S is:",
        "S = {x : x ∈ Z এবং 8 < x² < 27} হলে, S এর গরিষ্ঠ নিম্নসীমা কোনটি?",
        ["−5", "−3", "3", "5"],
        ["−5", "−3", "3", "5"],
        "A", "medium", "numerical",
        "√8 < |x| < √27 ⇒ about 2.8 < |x| < 5.2. Integers: ±3, ±4, ±5. Greatest lower bound of S is −5.",
        "√8 < |x| < √27 ⇒ পূর্ণসংখ্যা ±3, ±4, ±5। গরিষ্ঠ নিম্নসীমা −5।",
    ),
    q(
        "A lower bound of the set {1/5, 1/2, 0.2, …} is:",
        "{1/5, 1/2, 0.2, …} সেটের একটি নিম্নসীমা কোনটি?",
        ["−1", "0", "2", "1"],
        ["−1", "0", "2", "1"],
        "B", "easy", "conceptual",
        "All listed terms are positive; 0 is a lower bound (and the greatest lower bound of the sequence tending to 0).",
        "সব পদ ধনাত্মক; 0 একটি নিম্নসীমা।",
    ),
    q(
        "Which of the following is correct?",
        "নিচের কোনটি সঠিক?",
        ["Z ⊂ N", "N ⊂ R", "Q ∩ N = R", "Q ∪ Z = N"],
        ["Z ⊂ N", "N ⊂ R", "Q ∩ N = R", "Q ∪ Z = N"],
        "B", "easy", "factual",
        "Natural numbers are a subset of the reals: N ⊂ R. Z is not a subset of N.",
        "স্বাভাবিক সংখ্যা বাস্তব সংখ্যার উপসেট: N ⊂ R।",
    ),
    q(
        "For the set of real numbers, which laws hold?",
        "বাস্তব সংখ্যার সেটের ক্ষেত্রে কোন বিধিগুলো মানে?",
        [
            "commutative and associative only",
            "commutative and distributive only",
            "associative and distributive only",
            "commutative, associative and distributive",
        ],
        [
            "শুধু বিনিময় ও সংযোজন বিধি",
            "শুধু বিনিময় ও বণ্টন বিধি",
            "শুধু সংযোজন ও বণ্টন বিধি",
            "বিনিময়, সংযোজন ও বণ্টন বিধি",
        ],
        "D", "easy", "factual",
        "R is a field: addition and multiplication are commutative and associative, and multiplication distributes over addition.",
        "R একটি ক্ষেত্র; বিনিময়, সংযোজন ও বণ্টন বিধি সব মানে।",
    ),
    q(
        "If S = {x ∈ R : x − x² + 6 > 0}, then sup S equals:",
        "S = {x ∈ R : x − x² + 6 > 0} হলে, sup S এর মান কত?",
        ["−2", "−3", "2", "3"],
        ["−2", "−3", "2", "3"],
        "D", "medium", "numerical",
        "x − x² + 6 > 0 ⇒ x² − x − 6 < 0 ⇒ (x − 3)(x + 2) < 0 ⇒ −2 < x < 3. Hence sup S = 3.",
        "(x − 3)(x + 2) < 0 ⇒ −2 < x < 3; সুতরাং sup S = 3।",
    ),
    q(
        "If S = {x ∈ N : 5 < x² + 1 < 82}, then the supremum of S is:",
        "S = {x ∈ N : 5 < x² + 1 < 82} হলে, S এর সুপ্রিমাম কত?",
        ["2", "4", "8", "81"],
        ["2", "4", "8", "81"],
        "C", "medium", "numerical",
        "4 < x² < 81 and x ∈ N ⇒ x = 3, 4, 5, 6, 7, 8. Hence sup S = 8.",
        "4 < x² < 81 এবং x ∈ N ⇒ x = 3,…,8; সুতরাং sup S = 8।",
    ),
    q(
        "Which of the following is an example of the associative law for real numbers?",
        "বাস্তব সংখ্যার সংযোজন বিধির উদাহরণ কোনটি?",
        ["2 + 3 = 3 + 2", "(2 + 3) + 4 = 2 + (3 + 4)", "2 + 0 = 2", "2(3 + 4) = 2·3 + 2·4"],
        ["2 + 3 = 3 + 2", "(2 + 3) + 4 = 2 + (3 + 4)", "2 + 0 = 2", "2(3 + 4) = 2·3 + 2·4"],
        "B", "easy", "factual",
        "(a + b) + c = a + (b + c) is associativity; (2 + 3) + 4 = 2 + (3 + 4).",
        "(a + b) + c = a + (b + c) সংযোজন বিধি।",
    ),
    q(
        "Which inclusion chain of number sets is correct?",
        "সংখ্যা সেটের কোন অন্তর্ভুক্তি শৃঙ্খলটি সঠিক?",
        [
            "N ⊂ W ⊂ Z ⊂ Q ⊂ C ⊂ R",
            "N ⊂ Q ⊂ Z ⊂ C ⊂ R",
            "N ⊂ W ⊂ Z ⊂ Q ⊂ R ⊂ C",
            "N ⊂ Q ⊂ Z ⊂ R ⊂ C",
        ],
        [
            "N ⊂ W ⊂ Z ⊂ Q ⊂ C ⊂ R",
            "N ⊂ Q ⊂ Z ⊂ C ⊂ R",
            "N ⊂ W ⊂ Z ⊂ Q ⊂ R ⊂ C",
            "N ⊂ Q ⊂ Z ⊂ R ⊂ C",
        ],
        "C", "easy", "factual",
        "Standard chain: N ⊂ W ⊂ Z ⊂ Q ⊂ R ⊂ C.",
        "প্রামাণিক শৃঙ্খল: N ⊂ W ⊂ Z ⊂ Q ⊂ R ⊂ C।",
    ),
    q(
        "Among the following, which set relation is correct?",
        "নিচের কোন সেট সম্পর্কটি সঠিক?",
        ["Z ⊂ N", "R ⊂ Q", "Q ⊂ Z", "Q ⊂ R"],
        ["Z ⊂ N", "R ⊂ Q", "Q ⊂ Z", "Q ⊂ R"],
        "D", "easy", "factual",
        "Every rational is real: Q ⊂ R. The other listed inclusions are false.",
        "প্রত্যেক মূলদ সংখ্যা বাস্তব: Q ⊂ R। অন্যগুলো মিথ্যা।",
    ),
    q(
        "Consider: (i) N = {1, 2, 3, 4, …} (ii) Z = {…, −2, −1, 0, 1, 2, …} (iii) Q = {π, 1, e, √2}. Which is correct?",
        "(i) N = {1, 2, 3, 4, …} (ii) Z = {…, −2, −1, 0, 1, 2, …} (iii) Q = {π, 1, e, √2} — কোনটি সঠিক?",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii", "i, ii ও iii"],
        "A", "easy", "conceptual",
        "Q is the set of rationals; π, e, √2 are irrational, so (iii) is false.",
        "Q মূলদ সংখ্যার সেট; π, e, √2 অমূলদ — (iii) মিথ্যা।",
    ),
    q(
        "The set N of natural numbers is closed under:",
        "স্বাভাবিক সংখ্যার সেট N কোন ক্ষেত্রে আবদ্ধ?",
        [
            "addition and subtraction only",
            "subtraction and multiplication only",
            "addition and multiplication only",
            "addition, subtraction and multiplication",
        ],
        [
            "শুধু যোগ ও বিয়োগ",
            "শুধু বিয়োগ ও গুণ",
            "শুধু যোগ ও গুণ",
            "যোগ, বিয়োগ ও গুণ",
        ],
        "C", "easy", "conceptual",
        "N is closed under + and × but not under − (e.g. 2 − 5 ∉ N).",
        "N যোগ ও গুণে আবদ্ধ, বিয়োগে নয়।",
    ),
    q(
        "The inequality form of the interval [1, 3) is:",
        "[1, 3) ব্যবধির অসমতারূপ কোনটি?",
        ["1 < x < 3", "1 ≤ x ≤ 3", "1 ≤ x < 3", "1 < x ≤ 3"],
        ["1 < x < 3", "1 ≤ x ≤ 3", "1 ≤ x < 3", "1 < x ≤ 3"],
        "C", "easy", "factual",
        "[1, 3) means 1 ≤ x < 3.",
        "[1, 3) অর্থ 1 ≤ x < 3।",
    ),
    q(
        "Which of the following is a rational number?",
        "নিচের কোনটি মূলদ সংখ্যা?",
        ["√2", "π", "1/5", "e"],
        ["√2", "π", "1/5", "e"],
        "C", "easy", "factual",
        "1/5 = 0.2 is rational; √2, π, e are irrational.",
        "1/5 মূলদ; √2, π, e অমূলদ।",
    ),
    q(
        "The inequality form of [5, 7) ∪ (7, 10] is:",
        "[5, 7) ∪ (7, 10] ব্যবধির অসমতারূপ কোনটি?",
        [
            "{x ∈ R : 5 ≤ x ≤ 10}",
            "{x ∈ R : 5 < x < 10}",
            "{x ∈ R : 5 ≤ x ≤ 10, x ≠ 7}",
            "{x ∈ R : 5 < x ≤ 10, x ≠ 7}",
        ],
        [
            "{x ∈ R : 5 ≤ x ≤ 10}",
            "{x ∈ R : 5 < x < 10}",
            "{x ∈ R : 5 ≤ x ≤ 10, x ≠ 7}",
            "{x ∈ R : 5 < x ≤ 10, x ≠ 7}",
        ],
        "C", "medium", "conceptual",
        "[5, 7) ∪ (7, 10] = [5, 10] excluding 7.",
        "[5, 7) ∪ (7, 10] = [5, 10] থেকে 7 বাদ।",
    ),
    q(
        "√2 is:",
        "√2 হলো —",
        ["rational only", "irrational only", "real and rational", "real and irrational"],
        ["শুধু মূলদ", "শুধু অমূলদ", "বাস্তব ও মূলদ", "বাস্তব ও অমূলদ"],
        "D", "easy", "factual",
        "√2 is an irrational real number.",
        "√2 একটি অমূলদ বাস্তব সংখ্যা।",
    ),
    q(
        "Let A = {x : x ∈ R, x ∈ [−3, 7]} and B = {2, 3, 8}. Then sup(A ∪ B) equals:",
        "A = {x : x ∈ R, x ∈ [−3, 7]} এবং B = {2, 3, 8} হলে, sup(A ∪ B) কত?",
        ["7", "8", "10", "15"],
        ["7", "8", "10", "15"],
        "B", "medium", "numerical",
        "A ∪ B reaches up to 8 (from B), which is larger than 7. So sup(A ∪ B) = 8.",
        "A ∪ B এর বৃহত্তম উপাদানসীমা 8; সুপ্রিমাম 8।",
    ),
    q(
        "The law (b + c)·a = b·a + c·a is called the:",
        "(b + c)·a = b·a + c·a বিধিটির নাম কী?",
        ["closure law", "associative law", "distributive law", "commutative law"],
        ["আবদ্ধ বিধি", "সংযোজন বিধি", "বণ্টন বিধি", "বিনিময় বিধি"],
        "C", "easy", "factual",
        "This is the distributive law of multiplication over addition.",
        "এটি গুণের উপর যোগের বণ্টন বিধি।",
    ),
    q(
        "If a, b ∈ R, which statement about intervals is true for the open interval (a, b)?",
        "a, b ∈ R হলে, উন্মুক্ত ব্যবধি (a, b) সম্পর্কে কোনটি সত্য?",
        [
            "it includes both a and b",
            "it includes a but not b",
            "it includes neither a nor b",
            "it includes b but not a",
        ],
        [
            "a ও b উভয়ই অন্তর্ভুক্ত",
            "শুধু a অন্তর্ভুক্ত",
            "a ও b কোনোটিই অন্তর্ভুক্ত নয়",
            "শুধু b অন্তর্ভুক্ত",
        ],
        "C", "easy", "conceptual",
        "(a, b) = {x ∈ R : a < x < b}; endpoints excluded.",
        "(a, b) তে প্রান্তবিন্দু a, b অন্তর্ভুক্ত নয়।",
    ),
    q(
        "inf{x ∈ R : x > 2} equals:",
        "inf{x ∈ R : x > 2} এর মান কত?",
        ["0", "1", "2", "3"],
        ["0", "1", "2", "3"],
        "C", "medium", "conceptual",
        "The open ray (2, ∞) has greatest lower bound 2, though 2 is not in the set.",
        "(2, ∞) এর গরিষ্ঠ নিম্নসীমা 2।",
    ),
    q(
        "Which of the following is an irrational number?",
        "নিচের কোনটি অমূলদ সংখ্যা?",
        ["0.25", "22/7", "√9", "√3"],
        ["0.25", "22/7", "√9", "√3"],
        "D", "easy", "factual",
        "√3 is irrational; 0.25 and 22/7 are rational; √9 = 3 is rational.",
        "√3 অমূলদ; অন্যগুলো মূলদ।",
    ),
]


# =============================================================================
# hm2_27_ch01_t02 — Absolute value / পরম মান
# =============================================================================
T02 = [
    q(
        "The solution of |2x − 9| > 7 is:",
        "|2x − 9| > 7 অসমতাটির সমাধান কোনটি?",
        ["(−∞, 1)", "(8, ∞)", "(−∞, 1) ∪ (8, ∞)", "(−∞, 1) ∩ (8, ∞)"],
        ["(−∞, 1)", "(8, ∞)", "(−∞, 1) ∪ (8, ∞)", "(−∞, 1) ∩ (8, ∞)"],
        "C", "medium", "numerical",
        "2x − 9 > 7 or 2x − 9 < −7 ⇒ x > 8 or x < 1 ⇒ (−∞, 1) ∪ (8, ∞).",
        "x > 8 অথবা x < 1 ⇒ (−∞, 1) ∪ (8, ∞)।",
    ),
    q(
        "For real x: (i) |x| = x if x ≥ 0 (ii) |x| = −x if x ≤ 0 (iii) |x + y| = |x| + |y|. Which is correct?",
        "বাস্তব সংখ্যার ক্ষেত্রে: (i) x ≥ 0 হলে |x| = x (ii) x ≤ 0 হলে |x| = −x (iii) |x + y| = |x| + |y| — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "A", "easy", "conceptual",
        "(iii) is false in general; |x + y| ≤ |x| + |y|.",
        "(iii) সাধারণত মিথ্যা; |x + y| ≤ |x| + |y|।",
    ),
    q(
        "Express −1 < x < 4 using absolute value:",
        "−1 < x < 4 কে পরম মানের সাহায্যে প্রকাশ করলে:",
        ["|x − 1| < 4", "|x + 4| < 1", "|x − 3/2| < 5/2", "|x + 1| < 4"],
        ["|x − 1| < 4", "|x + 4| < 1", "|x − 3/2| < 5/2", "|x + 1| < 4"],
        "C", "medium", "numerical",
        "Midpoint 3/2, half-length 5/2: |x − 3/2| < 5/2.",
        "মধ্যবিন্দু 3/2, অর্ধদৈর্ঘ্য 5/2: |x − 3/2| < 5/2।",
    ),
    q(
        "The solution set of |2x + 1| < 3 is:",
        "|2x + 1| < 3 অসমতার সমাধান সেট কোনটি?",
        ["−2 < x < 1", "−2 ≤ x ≤ 1", "−1 < x < 2", "−1 ≤ x ≤ 2"],
        ["−2 < x < 1", "−2 ≤ x ≤ 1", "−1 < x < 2", "−1 ≤ x ≤ 2"],
        "A", "easy", "numerical",
        "−3 < 2x + 1 < 3 ⇒ −4 < 2x < 2 ⇒ −2 < x < 1.",
        "−3 < 2x + 1 < 3 ⇒ −2 < x < 1।",
    ),
    q(
        "The solution of |x| ≥ 3 is:",
        "|x| ≥ 3 অসমতার সমাধান কোনটি?",
        ["(−∞, −3] ∪ [3, ∞)", "(−∞, 3]", "[−3, 3]", "[3, ∞)"],
        ["(−∞, −3] ∪ [3, ∞)", "(−∞, 3]", "[−3, 3]", "[3, ∞)"],
        "A", "easy", "numerical",
        "|x| ≥ 3 ⇒ x ≤ −3 or x ≥ 3.",
        "|x| ≥ 3 ⇒ x ≤ −3 অথবা x ≥ 3।",
    ),
    q(
        "Express −7 < x + 3 < 5 using absolute value:",
        "−7 < x + 3 < 5 কে পরম মানের সাহায্যে প্রকাশ কর:",
        ["|x + 2| < 4", "|x + 4| < 6", "|x + 3| < 6", "|x + 1| < 3"],
        ["|x + 2| < 4", "|x + 4| < 6", "|x + 3| < 6", "|x + 1| < 3"],
        "B", "medium", "numerical",
        "Subtract −1: −6 < x + 4 < 6 ⇒ |x + 4| < 6.",
        "−6 < x + 4 < 6 ⇒ |x + 4| < 6।",
    ),
    q(
        "The solution set of |x − 1| < 1 is:",
        "|x − 1| < 1 অসমতার সমাধান সেট কোনটি?",
        ["[−1, 1]", "[0, 2]", "(0, 2)", "(−1, 1]"],
        ["[−1, 1]", "[0, 2]", "(0, 2)", "(−1, 1]"],
        "C", "easy", "numerical",
        "−1 < x − 1 < 1 ⇒ 0 < x < 2 ⇒ (0, 2).",
        "0 < x < 2 ⇒ (0, 2)।",
    ),
    q(
        "For real p, q: (i) |p + q| ≤ |p| + |q| (ii) |pq| = |p| |q| (iii) |p − q| ≤ ||p| − |q||. Which is correct?",
        "বাস্তব p, q এর ক্ষেত্রে: (i) |p + q| ≤ |p| + |q| (ii) |pq| = |p| |q| (iii) |p − q| ≤ ||p| − |q|| — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "A", "medium", "conceptual",
        "(iii) is false; the reverse triangle inequality is |p − q| ≥ ||p| − |q||.",
        "(iii) মিথ্যা; সঠিক হলো |p − q| ≥ ||p| − |q||।",
    ),
    q(
        "If |2x − 7| < 3, then:",
        "|2x − 7| < 3 হলে নিচের কোনটি সঠিক?",
        ["−7 < x < −3", "−5 < x < −3", "2 < x < 5", "3 < x < 7"],
        ["−7 < x < −3", "−5 < x < −3", "2 < x < 5", "3 < x < 7"],
        "C", "easy", "numerical",
        "−3 < 2x − 7 < 3 ⇒ 4 < 2x < 10 ⇒ 2 < x < 5. (Board sometimes writes ≤; for strict < the open interval holds.)",
        "4 < 2x < 10 ⇒ 2 < x < 5।",
    ),
    q(
        "Which is correct for |2x − 1|?",
        "|2x − 1| এর ক্ষেত্রে কোনটি সঠিক?",
        [
            "1 − 2x when x ≥ 1/2",
            "2x − 1 when x ≥ 1/2",
            "1 + 2x when x > 1/2",
            "2x + 1 when x ≤ 1/2",
        ],
        [
            "x ≥ 1/2 হলে 1 − 2x",
            "x ≥ 1/2 হলে 2x − 1",
            "x > 1/2 হলে 1 + 2x",
            "x ≤ 1/2 হলে 2x + 1",
        ],
        "B", "easy", "factual",
        "|2x − 1| = 2x − 1 when 2x − 1 ≥ 0 i.e. x ≥ 1/2.",
        "x ≥ 1/2 হলে |2x − 1| = 2x − 1।",
    ),
    q(
        "The solution of |x − 3| ≤ 1 is:",
        "|x − 3| ≤ 1 অসমতার সমাধান কোনটি?",
        ["−4 ≤ x ≤ 4", "−4 < x < 4", "2 ≤ x ≤ 4", "2 < x < 4"],
        ["−4 ≤ x ≤ 4", "−4 < x < 4", "2 ≤ x ≤ 4", "2 < x < 4"],
        "C", "easy", "numerical",
        "−1 ≤ x − 3 ≤ 1 ⇒ 2 ≤ x ≤ 4.",
        "2 ≤ x ≤ 4।",
    ),
    q(
        "If a = 3, b = −7 and c = −9, then ||a − b| − c| equals:",
        "a = 3, b = −7 এবং c = −9 হলে ||a − b| − c| এর মান কত?",
        ["1", "5", "13", "19"],
        ["1", "5", "13", "19"],
        "D", "medium", "numerical",
        "||3 − (−7)| − (−9)| = ||10| + 9| = |19| = 19.",
        "||10| + 9| = 19।",
    ),
    q(
        "If a and b are real, which is always true?",
        "a ও b বাস্তব হলে, নিচের কোনটি সর্বদা সঠিক?",
        ["|a − b| ≥ |a| + |b|", "|a + b| ≤ |a| + |b|", "|a + b| = |a| + |b|", "|a − b| = |a| + |b|"],
        ["|a − b| ≥ |a| + |b|", "|a + b| ≤ |a| + |b|", "|a + b| = |a| + |b|", "|a − b| = |a| + |b|"],
        "B", "easy", "factual",
        "Triangle inequality: |a + b| ≤ |a| + |b| always.",
        "ত্রিভুজ অসমতা: |a + b| ≤ |a| + |b|।",
    ),
    q(
        "If |x − 3| = 8, then the values of x are:",
        "|x − 3| = 8 হলে x এর মান কোনগুলো?",
        ["11 and 5", "11 and −5", "−11 and −5", "−11 and 5"],
        ["11 ও 5", "11 ও −5", "−11 ও −5", "−11 ও 5"],
        "B", "easy", "numerical",
        "x − 3 = 8 or x − 3 = −8 ⇒ x = 11 or x = −5.",
        "x = 11 অথবা x = −5।",
    ),
    q(
        "The solution of 0 < |x − 3| < 4 is:",
        "0 < |x − 3| < 4 অসমতাটির সমাধান কোনটি?",
        [
            "{x : x < 7}",
            "{x : −1 < x ≤ 7}",
            "{x : −1 < x < 3}",
            "{x : −1 < x < 3} ∪ {x : 3 < x < 7}",
        ],
        [
            "{x : x < 7}",
            "{x : −1 < x ≤ 7}",
            "{x : −1 < x < 3}",
            "{x : −1 < x < 3} ∪ {x : 3 < x < 7}",
        ],
        "D", "medium", "numerical",
        "|x − 3| < 4 and x ≠ 3 ⇒ −1 < x < 7, x ≠ 3.",
        "−1 < x < 7 এবং x ≠ 3।",
    ),
    q(
        "||2 − 6| − |1 − 9|| equals:",
        "||2 − 6| − |1 − 9|| এর মান কত?",
        ["3", "4", "12", "18"],
        ["3", "4", "12", "18"],
        "B", "easy", "numerical",
        "||−4| − |−8|| = |4 − 8| = 4.",
        "|4 − 8| = 4।",
    ),
    q(
        "For a, b ∈ R: (i) |ab| = |a| |b| (ii) |a + b| = |a| + |b| (iii) |a|² = a². Which is correct?",
        "a, b ∈ R হলে: (i) |ab| = |a| |b| (ii) |a + b| = |a| + |b| (iii) |a|² = a² — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "B", "medium", "conceptual",
        "(ii) holds only when ab ≥ 0; not always. (i) and (iii) are always true.",
        "(ii) সর্বদা সত্য নয়; (i) ও (iii) সর্বদা সত্য।",
    ),
    q(
        "If |x| = |y| for x, y ∈ R, then:",
        "x, y ∈ R এবং |x| = |y| হলে, নিচের কোনটি সঠিক?",
        ["x = y only", "x = −y only", "x = y or x = −y", "xy = 0"],
        ["শুধু x = y", "শুধু x = −y", "x = y অথবা x = −y", "xy = 0"],
        "C", "easy", "conceptual",
        "|x| = |y| ⇔ x = y or x = −y.",
        "|x| = |y| ⇔ x = y অথবা x = −y।",
    ),
    q(
        "Express the set {x ∈ R : x ∈ [−3, 7]} using absolute value:",
        "{x ∈ R : x ∈ [−3, 7]} কে পরম মান চিহ্নে প্রকাশ করলে:",
        ["|x| ≤ 5", "|x| < 5", "|x − 2| ≤ 5", "|x − 2| < 5"],
        ["|x| ≤ 5", "|x| < 5", "|x − 2| ≤ 5", "|x − 2| < 5"],
        "C", "medium", "numerical",
        "Midpoint 2, half-length 5: |x − 2| ≤ 5.",
        "মধ্যবিন্দু 2, অর্ধদৈর্ঘ্য 5: |x − 2| ≤ 5।",
    ),
    q(
        "If |5 − 2x| < 4, then:",
        "|5 − 2x| < 4 অসমতাটির সমাধান কোনটি?",
        ["−1 < x < 9", "1/2 < x < 9/2", "x ≤ 1/2 or x ≥ 9/2", "1 < x < 9"],
        ["−1 < x < 9", "1/2 < x < 9/2", "x ≤ 1/2 অথবা x ≥ 9/2", "1 < x < 9"],
        "B", "medium", "numerical",
        "−4 < 5 − 2x < 4 ⇒ −9 < −2x < −1 ⇒ 1/2 < x < 9/2.",
        "1/2 < x < 9/2।",
    ),
]


# =============================================================================
# hm2_27_ch01_t03 — Solving inequalities / অসমতার সমাধান
# =============================================================================
T03 = [
    q(
        "For ax − b > 0: (i) solution is [b/a, ∞) when a ≥ 0 (ii) (−∞, b/a) when a < 0 (iii) no solution when a = 0. Which is correct?",
        "ax − b > 0 এর সমাধান: (i) a ≥ 0 হলে [b/a, ∞) (ii) a < 0 হলে (−∞, b/a) (iii) a = 0 হলে কোনো সমাধান নেই — কোনটি সঠিক?",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii", "i, ii ও iii"],
        "B", "hard", "conceptual",
        "(i) is wrong: need a > 0 and the open ray (b/a, ∞), not a ≥ 0 with a closed ray. (ii) and (iii) match the standard cases.",
        "(i) ভুল (a > 0 ও উন্মুক্ত রশ্মি দরকার)। সঠিক ii ও iii।",
    ),
    q(
        "If x < −1, which is correct?",
        "x < −1 হলে নিচের কোনটি সঠিক?",
        ["3x > −3", "3x > 3", "3x < 3", "−3x > 3"],
        ["3x > −3", "3x > 3", "3x < 3", "−3x > 3"],
        "D", "easy", "numerical",
        "x < −1 ⇒ multiply by −3 (reverse): −3x > 3.",
        "x < −1 ⇒ −3x > 3 (অসমতা উল্টে)।",
    ),
    q(
        "The solution of x² + 2x − 3 < 0 is:",
        "x² + 2x − 3 < 0 অসমতাটির সমাধান কোনটি?",
        ["1 < x < 3", "x < −3 or x > 1", "−1 < x < 3", "−3 < x < 1"],
        ["1 < x < 3", "x < −3 অথবা x > 1", "−1 < x < 3", "−3 < x < 1"],
        "D", "medium", "numerical",
        "(x + 3)(x − 1) < 0 ⇒ −3 < x < 1.",
        "(x + 3)(x − 1) < 0 ⇒ −3 < x < 1।",
    ),
    q(
        "The solution of |2x − 7| > 5 is:",
        "|2x − 7| > 5 অসমতাটির বাস্তব সমাধান কোনটি?",
        ["x < 1", "x > 6", "x > 6 or x < 1", "x > 6 and x < 1"],
        ["x < 1", "x > 6", "x > 6 অথবা x < 1", "x > 6 এবং x < 1"],
        "C", "medium", "numerical",
        "2x − 7 > 5 or 2x − 7 < −5 ⇒ x > 6 or x < 1.",
        "x > 6 অথবা x < 1।",
    ),
    q(
        "Which inequality is true at the point (1, 1)?",
        "(1, 1) বিন্দুতে কোন অসমতাটি সত্য?",
        ["x + y > 0", "x > 1", "x + y > 3", "y = 2x"],
        ["x + y > 0", "x > 1", "x + y > 3", "y = 2x"],
        "A", "easy", "application",
        "At (1, 1): 1 + 1 = 2 > 0 true; x > 1 false; x + y > 3 false; y = 2x is equality not this inequality list winner.",
        "(1, 1) এ x + y = 2 > 0 সত্য।",
    ),
    q(
        "An integer solution of −3 ≤ 2x < 8 is:",
        "−3 ≤ 2x < 8 এর সমাধানে পূর্ণসংখ্যা কোনটি?",
        ["3", "4", "5", "6"],
        ["3", "4", "5", "6"],
        "A", "easy", "numerical",
        "−3/2 ≤ x < 4. Among options, only 3 lies in [−1.5, 4).",
        "−1.5 ≤ x < 4; অপশনগুলোর মধ্যে শুধু 3 সমাধানে আছে।",
    ),
    q(
        "The solution of (x − 4)(x − 5) > 0 is:",
        "(x − 4)(x − 5) > 0 এর সমাধান কোনটি?",
        ["x ≤ 4 and x ≥ 5", "x < 4 or x > 5", "x ≤ 4 or x ≥ 5", "x > 4 or x ≤ 5"],
        ["x ≤ 4 এবং x ≥ 5", "x < 4 অথবা x > 5", "x ≤ 4 অথবা x ≥ 5", "x > 4 অথবা x ≤ 5"],
        "B", "medium", "numerical",
        "Product positive outside the roots: x < 4 or x > 5.",
        "মূলদ্বয়ের বাইরে: x < 4 অথবা x > 5।",
    ),
    q(
        "The solution of (2x − 5)² < 0 is:",
        "(2x − 5)² < 0 এর সমাধান কোনটি?",
        ["x = 2.5", "x ≠ 2.5", "x > 2.5", "no real solution"],
        ["x = 2.5", "x ≠ 2.5", "x > 2.5", "কোনো বাস্তব সমাধান নেই"],
        "D", "medium", "conceptual",
        "A square is never negative; (2x − 5)² < 0 has empty solution set.",
        "বর্গ কখনো ঋণাত্মক নয়; সমাধান সেট শূন্য।",
    ),
    q(
        "For −2 ≤ x ≤ 3: (i) there are 6 integers in the interval (ii) supremum is 3 (iii) |2x − 1| ≤ 5. Which is correct?",
        "−2 ≤ x ≤ 3 এর ক্ষেত্রে: (i) 6টি পূর্ণসংখ্যা আছে (ii) উর্ধ্বসীমা/সুপ্রিমাম 3 (iii) |2x − 1| ≤ 5 — কোনটি সঠিক?",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii", "i, ii ও iii"],
        "D", "hard", "conceptual",
        "Integers −2…3 are six; sup = 3; |2x − 1| ≤ 5 holds on [−2, 3].",
        "তিনটি বিবৃতিই সত্য।",
    ),
    q(
        "If |2x − 1| < 2, the solution is:",
        "|2x − 1| < 2 হলে সমাধান কোনটি?",
        ["(−3/2, 1/2)", "(−1/2, 3/2)", "(−2, 2)", "(0, 1)"],
        ["(−3/2, 1/2)", "(−1/2, 3/2)", "(−2, 2)", "(0, 1)"],
        "B", "medium", "numerical",
        "−2 < 2x − 1 < 2 ⇒ −1 < 2x < 3 ⇒ −1/2 < x < 3/2.",
        "−1/2 < x < 3/2।",
    ),
    q(
        "The solution of x² − 5x + 6 < 0 is:",
        "x² − 5x + 6 < 0 এর সমাধান কোনটি?",
        ["x < 2", "2 ≤ x ≤ 3", "2 < x < 3", "x > 3 or x < 2"],
        ["x < 2", "2 ≤ x ≤ 3", "2 < x < 3", "x > 3 অথবা x < 2"],
        "C", "medium", "numerical",
        "(x − 2)(x − 3) < 0 ⇒ 2 < x < 3.",
        "(x − 2)(x − 3) < 0 ⇒ 2 < x < 3।",
    ),
    q(
        "The solution of (x + 2)(x + 3) > 0 is:",
        "(x + 2)(x + 3) > 0 অসমতাটির সমাধান কোনটি?",
        ["x < −3", "x > −2", "−3 < x < −2", "x < −3 or x > −2"],
        ["x < −3", "x > −2", "−3 < x < −2", "x < −3 অথবা x > −2"],
        "D", "medium", "numerical",
        "Product positive for x < −3 or x > −2.",
        "x < −3 অথবা x > −2।",
    ),
    q(
        "If −2 ≤ x ≤ 0, which is correct?",
        "−2 ≤ x ≤ 0 হলে কোনটি সঠিক?",
        [
            "|x| ≤ 2 and 0 ≤ x + 2 ≤ 2 only",
            "x ∈ [−2, 2] only",
            "0 ≤ x + 2 ≤ 2 and x ∈ [−2, 0]",
            "|x| < 2 only",
        ],
        [
            "শুধু |x| ≤ 2 এবং 0 ≤ x + 2 ≤ 2",
            "শুধু x ∈ [−2, 2]",
            "0 ≤ x + 2 ≤ 2 এবং x ∈ [−2, 0]",
            "শুধু |x| < 2",
        ],
        "C", "medium", "conceptual",
        "−2 ≤ x ≤ 0 ⇔ 0 ≤ x + 2 ≤ 2 and x ∈ [−2, 0]. Note |x| ≤ 2 is weaker (includes [0, 2]).",
        "−2 ≤ x ≤ 0 ⇔ 0 ≤ x + 2 ≤ 2।",
    ),
    q(
        "Solve 3 − 2x ≤ 1:",
        "3 − 2x ≤ 1 অসমতাটির সমাধান কোনটি?",
        ["x ≤ 1", "x ≥ 1", "x < 1", "x > 1"],
        ["x ≤ 1", "x ≥ 1", "x < 1", "x > 1"],
        "B", "easy", "numerical",
        "−2x ≤ −2 ⇒ x ≥ 1 (inequality reverses).",
        "−2x ≤ −2 ⇒ x ≥ 1।",
    ),
    q(
        "The solution set of 2x − 3 > 0 and x − 1 < 0 is:",
        "2x − 3 > 0 এবং x − 1 < 0 এর সমাধান সেট:",
        ["x > 3/2", "x < 1", "3/2 < x < 1", "empty set"],
        ["x > 3/2", "x < 1", "3/2 < x < 1", "শূন্য সেট"],
        "D", "hard", "numerical",
        "x > 3/2 and x < 1 cannot hold together; intersection empty.",
        "x > 3/2 ও x < 1 একসাথে অসম্ভব; ছেদ শূন্য।",
    ),
    q(
        "Solve −1 ≤ (2x − 1)/3 < 3:",
        "−1 ≤ (2x − 1)/3 < 3 এর সমাধান কোনটি?",
        ["−1 ≤ x < 5", "−1 ≤ x ≤ 5", "1 ≤ x < 5", "−2 ≤ x < 5"],
        ["−1 ≤ x < 5", "−1 ≤ x ≤ 5", "1 ≤ x < 5", "−2 ≤ x < 5"],
        "A", "medium", "numerical",
        "−3 ≤ 2x − 1 < 9 ⇒ −2 ≤ 2x < 10 ⇒ −1 ≤ x < 5.",
        "−1 ≤ x < 5।",
    ),
    q(
        "If x² ≤ 4, then:",
        "x² ≤ 4 হলে:",
        ["x ≤ 2", "x ≥ −2", "−2 ≤ x ≤ 2", "x < −2 or x > 2"],
        ["x ≤ 2", "x ≥ −2", "−2 ≤ x ≤ 2", "x < −2 অথবা x > 2"],
        "C", "easy", "numerical",
        "x² ≤ 4 ⇔ |x| ≤ 2 ⇔ −2 ≤ x ≤ 2.",
        "x² ≤ 4 ⇔ −2 ≤ x ≤ 2।",
    ),
    q(
        "The solution of (x − 1)/(x + 2) > 0 is:",
        "(x − 1)/(x + 2) > 0 এর সমাধান কোনটি?",
        ["x < −2 or x > 1", "−2 < x < 1", "x ≤ −2 or x ≥ 1", "x > −2"],
        ["x < −2 অথবা x > 1", "−2 < x < 1", "x ≤ −2 অথবা x ≥ 1", "x > −2"],
        "A", "hard", "numerical",
        "Critical points −2, 1; positive on (−∞, −2) ∪ (1, ∞).",
        "(−∞, −2) ∪ (1, ∞)।",
    ),
    q(
        "Solve |x + 1| ≥ 2:",
        "|x + 1| ≥ 2 এর সমাধান কোনটি?",
        ["−3 ≤ x ≤ 1", "x ≤ −3 or x ≥ 1", "x ≤ −1 or x ≥ 2", "−1 ≤ x ≤ 1"],
        ["−3 ≤ x ≤ 1", "x ≤ −3 অথবা x ≥ 1", "x ≤ −1 অথবা x ≥ 2", "−1 ≤ x ≤ 1"],
        "B", "medium", "numerical",
        "x + 1 ≤ −2 or x + 1 ≥ 2 ⇒ x ≤ −3 or x ≥ 1.",
        "x ≤ −3 অথবা x ≥ 1।",
    ),
    q(
        "If 1 < |2x − 3| ≤ 7, a correct description of the solution is:",
        "1 < |2x − 3| ≤ 7 হলে সমাধান সেটের সঠিক বর্ণনা কোনটি?",
        [
            "{x ∈ R : |x| < 4}",
            "{x ∈ R : 1 < x < 5, x ≠ 3/2}",
            "{x ∈ R : x ≤ −2 or x ≥ 5}",
            "{x ∈ R : −2 ≤ x < 1 or 2 < x ≤ 5}",
        ],
        [
            "{x ∈ R : |x| < 4}",
            "{x ∈ R : 1 < x < 5, x ≠ 3/2}",
            "{x ∈ R : x ≤ −2 or x ≥ 5}",
            "{x ∈ R : −2 ≤ x < 1 or 2 < x ≤ 5}",
        ],
        "D", "hard", "numerical",
        "|2x − 3| ≤ 7 ⇒ −2 ≤ x ≤ 5; |2x − 3| > 1 ⇒ x < 1 or x > 2. Intersection: [−2, 1) ∪ (2, 5].",
        "−2 ≤ x < 1 অথবা 2 < x ≤ 5।",
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
    counts["hm2_27_ch01_t01"] = write_topic("hm2_27_ch01_t01", T01)["count"]
    counts["hm2_27_ch01_t02"] = write_topic("hm2_27_ch01_t02", T02)["count"]
    counts["hm2_27_ch01_t03"] = write_topic("hm2_27_ch01_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm2_27_ch01",
        "title_en": "Real Numbers and Inequalities",
        "title_bn": "বাস্তব সংখ্যা ও অসমতা",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(24, 29)],
        "topics": {
            "hm2_27_ch01_t01": {
                "title_en": "Real numbers and intervals",
                "title_bn": "বাস্তব সংখ্যা ও ব্যবধান",
                "udvash_types": [
                    "number-set relations N/W/Z/Q/R/C",
                    "inf/sup and bounds",
                    "interval notation",
                    "field axioms / laws",
                ],
                "count": 20,
            },
            "hm2_27_ch01_t02": {
                "title_en": "Absolute value",
                "title_bn": "পরম মান",
                "udvash_types": [
                    "definition and properties",
                    "equations |ax+b|=c",
                    "inequalities |ax+b|<c / >c",
                    "express intervals as |x-a|<k",
                ],
                "count": 20,
            },
            "hm2_27_ch01_t03": {
                "title_en": "Solving inequalities",
                "title_bn": "অসমতার সমাধান",
                "udvash_types": [
                    "linear inequalities",
                    "quadratic / product sign charts",
                    "combined absolute inequalities",
                    "integer / point-check items",
                ],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "figure_only_graphs": "Printed inequality graph sketches rewritten as text stems (point-check / algebraic form)",
            "garbled_stems": "Noisy OCR reconstructed from answer-key algebra and standard board forms",
            "stimulus_pairs": "Linked stimulus blocks curated as standalone clear stems",
            "ambiguous_option_glyphs": "Broken Bangla/option glyphs replaced with closed-form HSC standards",
        },
        "low_confidence": [
            "OCR on pp. 24–28 noisy; column text and solution lines used to reconstruct stems.",
            "Inline math stored as plain text (| |, √, ∈, ∪, ≤) for JSONL.",
            "Some printed answer keys inconsistent with strict vs non-strict inequality; closed-form board standards retained.",
            "Figure-linked stimulus items rewritten without relying on diagram OCR.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm2_ch01.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
        "math2_start": {
            "topics_complete": "3/30",
            "note": "Ch01 begins higher_mathematics 2nd paper question bank curation",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch01_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
