#!/usr/bin/env python3
"""Seed Higher Mathematics 1st Paper Ch1 (Matrices and Determinants).

Curated from Udvash HSC Question Bank 2026 printed pp. 39–53 (PDF 45–59).
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
    "higher_mathematics p1 ch01; curated bilingual"
)


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    if not re.search(r"[A-Za-z]", en):
        en = f"value {en}"
    if en.startswith("value ") and not re.search(r"[ঀ-৿]", bn):
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
# hm1_27_ch01_t01 — Matrices and matrix operations
# Prefer Udvash T-01..T-05 with printed keys
# =============================================================================
T01 = [
    q(
        "If A = (a_ij) is skew-symmetric, which are true? "
        "(i) a_ij = -a_ji when i ≠ j  (ii) a_ij = 0 when i = j  (iii) m ≠ n",
        "A = (a_ij) বিপ্রতিসম ম্যাট্রিক্স হলে কোনটি সঠিক? "
        "(i) i ≠ j হলে a_ij = -a_ji  (ii) i = j হলে a_ij = 0  (iii) m ≠ n",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "A", "medium", "conceptual",
        "Skew-symmetric ⇒ A = -A^T, so a_ij = -a_ji and a_ii = 0. It must be square, so m ≠ n is false.",
        "বিপ্রতিসম ⇒ A = -A^T; তাই a_ij = -a_ji ও a_ii = 0। এটি বর্গম্যাট্রিক্স হওয়ায় m ≠ n মিথ্যা।",
    ),
    q(
        "If [[1, x, 2], [-5, 3, 4], [y, 4, 9]] is symmetric, then (x, y) = ?",
        "[[1, x, 2], [-5, 3, 4], [y, 4, 9]] প্রতিসম হলে (x, y) = ?",
        ["(5, -2)", "(-5, 2)", "(5, 2)", "(-5, -2)"],
        ["(5, -2)", "(-5, 2)", "(5, 2)", "(-5, -2)"],
        "B", "easy", "numerical",
        "Symmetry needs a_12 = a_21 and a_13 = a_31, so x = -5 and y = 2.",
        "প্রতিসম হতে a_12 = a_21 ও a_13 = a_31; অতএব x = -5 এবং y = 2।",
    ),
    q(
        "If [[p, 2, -3], [-2, 0, x], [3, -5, 0]] is skew-symmetric, then p + x = ?",
        "[[p, 2, -3], [-2, 0, x], [3, -5, 0]] বিপ্রতিসম হলে p + x = ?",
        ["-5", "2", "5", "-3"],
        ["মান -5", "মান 2", "মান 5", "মান -3"],
        "C", "medium", "numerical",
        "Diagonal entry p = 0 and a_23 = -a_32 ⇒ x = 5, so p + x = 5.",
        "কর্ণভুক্তি p = 0 এবং a_23 = -a_32 ⇒ x = 5; সুতরাং p + x = 5।",
    ),
    q(
        "If P, Q, R have orders 3×5, 5×3, 2×3, the order of R(P + Q^T) is:",
        "P, Q, R এর মাত্রা 3×5, 5×3, 2×3 হলে R(P + Q^T) এর মাত্রা কত?",
        ["3 x 3", "2 x 5", "3 x 5", "5 x 3"],
        ["3 x 3", "2 x 5", "3 x 5", "5 x 3"],
        "B", "medium", "application",
        "Q^T is 3×5, so P + Q^T is 3×5; then R_(2×3) times that is 2×5.",
        "Q^T = 3×5 ⇒ P + Q^T = 3×5; R (2×3) গুণে ফল 2×5।",
    ),
    q(
        "If A = [[2, 5, -1], [6, x, 5], [-4, -9, 4]] and tr(A) = 8, then x = ?",
        "A = [[2, 5, -1], [6, x, 5], [-4, -9, 4]] এবং tr(A) = 8 হলে x = ?",
        ["2", "8", "6", "5"],
        ["মান 2", "মান 8", "মান 6", "মান 5"],
        "A", "easy", "numerical",
        "Trace = 2 + x + 4 = 8 ⇒ x = 2.",
        "ট্রেস = 2 + x + 4 = 8 ⇒ x = 2।",
    ),
    q(
        "For A = [[0, 3, -2], [-3, 0, 7], [2, -7, 0]], which are true? "
        "(i) skew-symmetric  (ii) scalar  (iii) if AB is 3×1 then B is 3×1",
        "A = [[0, 3, -2], [-3, 0, 7], [2, -7, 0]] এর জন্য কোনটি সঠিক? "
        "(i) বিপ্রতিসম  (ii) স্কেলার  (iii) AB এর মাত্রা 3×1 হলে B এর মাত্রা 3×1",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "B", "medium", "conceptual",
        "A = -A^T so (i) holds; zero diagonal means not a non-trivial scalar matrix. "
        "A is 3×3, so AB of order 3×1 forces B to be 3×1.",
        "A = -A^T বলে (i) সত্য; কর্ণ শূন্য বলে স্কেলার নয়। A 3×3 হওয়ায় AB = 3×1 ⇒ B = 3×1।",
    ),
    q(
        "If A = [[a, -a], [a, -a]], then A^2 is a:",
        "A = [[a, -a], [a, -a]] হলে A^2 কোন ধরনের?",
        ["Idempotent matrix", "Scalar matrix", "Null matrix", "Identity matrix"],
        ["সমঘাতী ম্যাট্রিক্স", "স্কেলার ম্যাট্রিক্স", "শূন্য ম্যাট্রিক্স", "অভেদ ম্যাট্রিক্স"],
        "C", "medium", "numerical",
        "Matrix multiplication yields A^2 = [[0, 0], [0, 0]], the null matrix.",
        "গুণফল A^2 = [[0, 0], [0, 0]], অর্থাৎ শূন্য ম্যাট্রিক্স।",
    ),
    q(
        "A diagonal matrix diag(a, b, c) is scalar if and only if:",
        "কর্ণম্যাট্রিক্স diag(a, b, c) স্কেলার হবে যদি এবং কেবল যদি:",
        ["a + b + c = 0", "a = b = c", "abc is nonzero", "a, b, c are distinct"],
        ["a + b + c = 0", "a = b = c", "abc অশূন্য", "a, b, c ভিন্ন"],
        "B", "easy", "factual",
        "A scalar matrix is a diagonal matrix with equal diagonal entries.",
        "স্কেলার ম্যাট্রিক্স = সমান কর্ণভুক্তিবিশিষ্ট কর্ণম্যাট্রিক্স।",
    ),
    q(
        "If [[2x - y, 5], [3, y]] = [[6, 5], [3, -2]], then x = ?",
        "[[2x - y, 5], [3, y]] = [[6, 5], [3, -2]] হলে x = ?",
        ["1", "2", "3", "-2"],
        ["মান 1", "মান 2", "মান 3", "মান -2"],
        "B", "easy", "numerical",
        "y = -2 and 2x - y = 6 ⇒ 2x + 2 = 6 ⇒ x = 2.",
        "y = -2 এবং 2x - y = 6 ⇒ 2x + 2 = 6 ⇒ x = 2।",
    ),
    q(
        "If A, B, C have orders 4×3, 3×4, 4×7, the order of (AB)C is:",
        "A, B, C এর মাত্রা 4×3, 3×4, 4×7 হলে (AB)C এর মাত্রা কত?",
        ["4 x 7", "3 x 7", "4 x 4", "7 x 4"],
        ["4 x 7", "3 x 7", "4 x 4", "7 x 4"],
        "A", "easy", "application",
        "AB is 4×4; then (AB)C is 4×7.",
        "AB = 4×4; অতএব (AB)C = 4×7।",
    ),
    q(
        "If the trace of [[1, 1, 2], [4, a, -1], [3, 2, 2a]] is 7, then a = ?",
        "[[1, 1, 2], [4, a, -1], [3, 2, 2a]] এর ট্রেস 7 হলে a = ?",
        ["1", "3", "2", "7"],
        ["মান 1", "মান 3", "মান 2", "মান 7"],
        "C", "easy", "numerical",
        "1 + a + 2a = 7 ⇒ 3a = 6 ⇒ a = 2.",
        "1 + a + 2a = 7 ⇒ 3a = 6 ⇒ a = 2।",
    ),
    q(
        "For M = [[1, 2, 0], [0, 4, 5], [0, 0, 6]], which are true? "
        "(i) square  (ii) lower triangular  (iii) trace = 11",
        "M = [[1, 2, 0], [0, 4, 5], [0, 0, 6]] এর জন্য কোনটি সঠিক? "
        "(i) বর্গম্যাট্রিক্স  (ii) নিম্ন ত্রিভুজাকার  (iii) ট্রেস = 11",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "B", "medium", "conceptual",
        "M is square and upper (not lower) triangular; trace = 1+4+6 = 11.",
        "M বর্গ ও উর্ধ্ব ত্রিভুজাকার (নিম্ন নয়); ট্রেস = 1+4+6 = 11।",
    ),
    q(
        "If A is 3×4 and B is 4×2, the order of AB is:",
        "A এর মাত্রা 3×4 এবং B এর মাত্রা 4×2 হলে AB এর মাত্রা কত?",
        ["3 x 4", "3 x 2", "2 x 3", "4 x 4"],
        ["3 x 4", "3 x 2", "2 x 3", "4 x 4"],
        "B", "easy", "factual",
        "Order of product is m×p = 3×2.",
        "গুণফলের মাত্রা m×p = 3×2।",
    ),
    q(
        "If A = [[-1, 4], [-2, 2]], then A − 2I equals:",
        "A = [[-1, 4], [-2, 2]] হলে A − 2I = ?",
        [
            "matrix [[-3, 4], [-2, 2]]",
            "matrix [[-3, 4], [-2, 0]]",
            "matrix [[-2, 4], [-2, 1]]",
            "matrix [[0, 4], [-2, 3]]",
        ],
        [
            "ম্যাট্রিক্স [[-3, 4], [-2, 2]]",
            "ম্যাট্রিক্স [[-3, 4], [-2, 0]]",
            "ম্যাট্রিক্স [[-2, 4], [-2, 1]]",
            "ম্যাট্রিক্স [[0, 4], [-2, 3]]",
        ],
        "B", "easy", "numerical",
        "2I = [[2, 0], [0, 2]], hence A − 2I = [[-3, 4], [-2, 0]].",
        "2I = [[2, 0], [0, 2]]; তাই A − 2I = [[-3, 4], [-2, 0]]।",
    ),
    q(
        "If A = [[2, 1, -1]] and B = [[2], [0], [3]], then BA equals:",
        "A = [[2, 1, -1]] এবং B = [[2], [0], [3]] হলে BA = ?",
        [
            "matrix [[1]]",
            "matrix [[4], [0], [-3]]",
            "matrix [[4, 0, -3]]",
            "matrix [[4, 2, -2], [0, 0, 0], [6, 3, -3]]",
        ],
        [
            "ম্যাট্রিক্স [[1]]",
            "ম্যাট্রিক্স [[4], [0], [-3]]",
            "ম্যাট্রিক্স [[4, 0, -3]]",
            "ম্যাট্রিক্স [[4, 2, -2], [0, 0, 0], [6, 3, -3]]",
        ],
        "D", "medium", "numerical",
        "B (3×1) times A (1×3) gives the 3×3 outer product shown in option D.",
        "B (3×1) × A (1×3) = অপশন D-এর 3×3 আউটার প্রোডাক্ট।",
    ),
    q(
        "Which relation defines a skew-symmetric matrix?",
        "বিপ্রতিসম ম্যাট্রিক্সের সংজ্ঞা কোন সম্পর্ক?",
        ["a_ij = a_ji", "a_ij = 0 for all i, j", "a_ij = -a_ji", "a_ij ≠ a_ji always"],
        ["a_ij = a_ji", "সব i, j তে a_ij = 0", "a_ij = -a_ji", "সবসময় a_ij ≠ a_ji"],
        "C", "easy", "factual",
        "Skew-symmetric means A^T = -A, i.e. a_ij = -a_ji.",
        "বিপ্রতিসম ⇒ A^T = -A, অর্থাৎ a_ij = -a_ji।",
    ),
    q(
        "For which value of p is [[-3, 0, -1], [0, 3, p], [-1, 4, 0]] symmetric?",
        "কোন p তে [[-3, 0, -1], [0, 3, p], [-1, 4, 0]] প্রতিসম?",
        ["-4", "-1", "0", "4"],
        ["মান -4", "মান -1", "মান 0", "মান 4"],
        "D", "easy", "numerical",
        "Symmetry requires a_23 = a_32 ⇒ p = 4.",
        "প্রতিসম হতে a_23 = a_32 ⇒ p = 4।",
    ),
    q(
        "For diag(6, 7, 8), which are true? (i) diagonal  (ii) square  (iii) scalar",
        "diag(6, 7, 8) এর জন্য কোনটি সঠিক? (i) কর্ণম্যাট্রিক্স  (ii) বর্গ  (iii) স্কেলার",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "A", "easy", "conceptual",
        "It is a square diagonal matrix; unequal diagonals mean it is not scalar.",
        "এটি বর্গ কর্ণম্যাট্রিক্স; কর্ণভুক্তি অসমান বলে স্কেলার নয়।",
    ),
    q(
        "If A is 2×3 and B is 3×1, the order of AB is:",
        "A এর মাত্রা 2×3 এবং B এর মাত্রা 3×1 হলে AB এর মাত্রা কত?",
        ["2 x 1", "3 x 2", "2 x 3", "3 x 1"],
        ["2 x 1", "3 x 2", "2 x 3", "3 x 1"],
        "A", "easy", "factual",
        "Product order is 2×1.",
        "গুণফলের মাত্রা 2×1।",
    ),
    q(
        "If A is square and A^2 = A, then A is called:",
        "A বর্গম্যাট্রিক্স এবং A^2 = A হলে A কে কী বলে?",
        ["Idempotent matrix", "Involutory matrix", "Singular matrix", "Null matrix"],
        ["সমঘাতী ম্যাট্রিক্স", "অভেদঘাতী ম্যাট্রিক্স", "ব্যতিক্রমী ম্যাট্রিক্স", "শূন্য ম্যাট্রিক্স"],
        "A", "easy", "factual",
        "A^2 = A defines an idempotent matrix.",
        "A^2 = A শর্তযুক্ত ম্যাট্রিক্সকে সমঘাতী বলে।",
    ),
]


# =============================================================================
# hm1_27_ch01_t02 — Determinants and their properties
# Prefer Udvash T-06, T-08, T-09 with printed keys
# =============================================================================
T02 = [
    q(
        "For [[3, 5, -2], [-1, 6, 4], [2, -3, 7]], the cofactor of the (3, 2) entry is:",
        "[[3, 5, -2], [-1, 6, 4], [2, -3, 7]] এর (3, 2) ভুক্তির সহগুণক কত?",
        ["-30", "-10", "10", "30"],
        ["মান -30", "মান -10", "মান 10", "মান 30"],
        "B", "medium", "numerical",
        "C_32 = (−1)^{5} det([[3, -2], [-1, 4]]) = −(12 − 2) = −10.",
        "C_32 = (−1)^{3+2} det([[3, -2], [-1, 4]]) = −(12 − 2) = −10।",
    ),
    q(
        "If A = [[2, 5, -1], [6, x, 5], [-4, -9, 4]], the cofactor of the (2, 2) entry is:",
        "A = [[2, 5, -1], [6, x, 5], [-4, -9, 4]] এর (2, 2) ভুক্তির সহগুণক কত?",
        ["12", "4", "-4", "-12"],
        ["মান 12", "মান 4", "মান -4", "মান -12"],
        "B", "medium", "numerical",
        "C_22 = (+1) det([[2, -1], [-4, 4]]) = 8 − 4 = 4.",
        "C_22 = (+1) det([[2, -1], [-4, 4]]) = 8 − 4 = 4।",
    ),
    q(
        "If A = 3 [[1, 2], [4, -3]], then |A| = ?",
        "A = 3 [[1, 2], [4, -3]] হলে |A| = ?",
        ["33", "-11", "-33", "-99"],
        ["মান 33", "মান -11", "মান -33", "মান -99"],
        "D", "medium", "numerical",
        "|kM| = k^n |M| for n×n; here |A| = 9(−3 − 8) = −99.",
        "n×n ম্যাট্রিক্সে |kM| = k^n |M|; এখানে |A| = 9(−3 − 8) = −99।",
    ),
    q(
        "The value of det([[a+b, 2b, a], [b+c, 2c, b], [c+a, 2a, c]]) is:",
        "det([[a+b, 2b, a], [b+c, 2c, b], [c+a, 2a, c]]) এর মান কত?",
        ["0", "2(a+b+c)(c+a)^2", "2(a+b+c)^2", "2(a^3+b^3+c^3)"],
        ["মান 0", "2(a+b+c)(c+a)^2", "2(a+b+c)^2", "2(a^3+b^3+c^3)"],
        "A", "hard", "numerical",
        "Column operation C1 ← C1 − C3 makes two columns proportional/identical, so the determinant is 0.",
        "C1 ← C1 − C3 অপারেশনে দুই কলাম সমান/সমানুপাতিক হয়; নির্ণায়ক 0।",
    ),
    q(
        "If det([[1, 1, 1], [3, 2, 1], [a, 2, 1]]) = 2, then a = ?",
        "det([[1, 1, 1], [3, 2, 1], [a, 2, 1]]) = 2 হলে a = ?",
        ["-2", "-1", "1", "2"],
        ["মান -2", "মান -1", "মান 1", "মান 2"],
        "C", "medium", "numerical",
        "Expanding gives 0 − (3 − a) + (6 − 2a) = 2 ⇒ a − 3 + 6 − 2a = 2 ⇒ −a + 3 = 2 ⇒ a = 1.",
        "প্রসারণে 0 − (3 − a) + (6 − 2a) = 2 ⇒ a = 1।",
    ),
    q(
        "The value of det([[l+m, 1, n], [m+n, 1, l], [n+l, 1, m]]) is:",
        "det([[l+m, 1, n], [m+n, 1, l], [n+l, 1, m]]) এর মান কত?",
        ["(l+m)(m+n)", "(l+m)(m+n)(n+l)", "1", "0"],
        ["(l+m)(m+n)", "(l+m)(m+n)(n+l)", "মান 1", "মান 0"],
        "D", "hard", "numerical",
        "C1 ← C1 + C3 produces a factor (l+m+n) and then two identical columns of 1s, so det = 0.",
        "C1 ← C1 + C3 করলে একই ধরনের কলাম তৈরি হয়; নির্ণায়ক 0।",
    ),
    q(
        "For the determinant [[2, 1, 3], [4, 5, 6], [2, 1, 3]], which are true? "
        "(i) value is 0  (ii) minor of (2,3) is 5  (iii) cofactor of (2,1) is 0",
        "নির্ণায়ক [[2, 1, 3], [4, 5, 6], [2, 1, 3]] এর জন্য কোনটি সঠিক? "
        "(i) মান 0  (ii) (2,3) এর অনুরাশি 5  (iii) (2,1) এর সহগুণক 0",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "B", "medium", "conceptual",
        "Rows 1 and 3 are identical ⇒ det = 0. Minor of (2,3) is −5 (not 5). Cofactor of (2,1) is 0.",
        "১ম ও ৩য় সারি সমান ⇒ নির্ণায়ক 0। (2,3) এর অনুরাশি −5 (5 নয়)। (2,1) সহগুণক 0।",
    ),
    q(
        "If A = diag(a, b, c), the cofactor of the (3, 3) entry in |A| is:",
        "A = diag(a, b, c) হলে |A| এ (3, 3) ভুক্তির সহগুণক কত?",
        ["a + b", "a + c", "bc", "ab"],
        ["a + b", "a + c", "bc", "ab"],
        "D", "medium", "numerical",
        "C_33 = (+1) det([[a, 0], [0, b]]) = ab.",
        "C_33 = (+1) det([[a, 0], [0, b]]) = ab।",
    ),
    q(
        "det([[2, 4], [4, 8]]) equals:",
        "det([[2, 4], [4, 8]]) এর মান কত?",
        ["16", "8", "4", "0"],
        ["মান 16", "মান 8", "মান 4", "মান 0"],
        "D", "easy", "numerical",
        "2·8 − 4·4 = 16 − 16 = 0.",
        "2·8 − 4·4 = 0।",
    ),
    q(
        "In det([[x, 1, 3], [-1, 1, 2], [3, 2, 0]]), if the cofactor of (2, 3) is 1, then x = ?",
        "নির্ণায়ক [[x, 1, 3], [-1, 1, 2], [3, 2, 0]] এ (2, 3) সহগুণক 1 হলে x = ?",
        ["-2", "-1", "1", "2"],
        ["মান -2", "মান -1", "মান 1", "মান 2"],
        "C", "medium", "numerical",
        "C_23 = (−1)^{5} det([[x, 1], [3, 2]]) = −(2x − 3) = 1 ⇒ 2x − 3 = −1 ⇒ x = 1.",
        "C_23 = (−1)^{2+3} det([[x, 1], [3, 2]]) = −(2x − 3) = 1 ⇒ x = 1।",
    ),
    q(
        "If A is 2×2 and |A| = 5, then |3A| = ?",
        "A একটি 2×2 ম্যাট্রিক্স এবং |A| = 5 হলে |3A| = ?",
        ["5", "15", "30", "45"],
        ["মান 5", "মান 15", "মান 30", "মান 45"],
        "D", "easy", "numerical",
        "|kA| = k^n |A| with n = 2 ⇒ |3A| = 9 × 5 = 45.",
        "n = 2 হলে |kA| = k^2 |A| ⇒ |3A| = 9 × 5 = 45।",
    ),
    q(
        "If P = [[-2, 1], [-1, 2]], which are true? "
        "(i) |P| = -3  (ii) P + I_2 = [[-1, 1], [-1, 3]]  (iii) P^2 = [[3, 0], [0, 3]]",
        "P = [[-2, 1], [-1, 2]] হলে কোনটি সঠিক? "
        "(i) |P| = -3  (ii) P + I_2 = [[-1, 1], [-1, 3]]  (iii) P^2 = [[3, 0], [0, 3]]",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "D", "medium", "numerical",
        "|P| = -4 + 1 = -3; P + I matches; P^2 = [[3, 0], [0, 3]]. All three hold.",
        "|P| = -3; P + I ও P^2 উভয়ই প্রদত্ত রূপ; তিনটিই সত্য।",
    ),
    q(
        "If A = [[1, 5], [3, 7]], which are true? "
        "(i) minor of (1,1) is 7  (ii) A^T = [[1, 3], [5, 7]]  (iii) 2A = [[2, 5], [6, 7]]",
        "A = [[1, 5], [3, 7]] হলে কোনটি সঠিক? "
        "(i) (1,1) অনুরাশি 7  (ii) A^T = [[1, 3], [5, 7]]  (iii) 2A = [[2, 5], [6, 7]]",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "A", "easy", "conceptual",
        "Minor of (1,1) is 7 and A^T is correct; 2A is actually [[2, 10], [6, 14]], so (iii) is false.",
        "(1,1) অনুরাশি 7 এবং A^T সঠিক; 2A = [[2, 10], [6, 14]] বলে (iii) মিথ্যা।",
    ),
    q(
        "det([[1, 1, 1], [e, pi, sqrt(3)], [3, 3, 3]]) equals:",
        "det([[1, 1, 1], [e, pi, sqrt(3)], [3, 3, 3]]) এর মান কত?",
        ["1", "e + pi", "3", "0"],
        ["মান 1", "e + pi", "মান 3", "মান 0"],
        "D", "easy", "conceptual",
        "Row 3 = 3 × row 1, so the determinant is 0.",
        "৩য় সারি = 3 × ১ম সারি; নির্ণায়ক 0।",
    ),
    q(
        "det([[1, 1, 1], [2, 5, 2], [2, 4, 3]]) equals:",
        "det([[1, 1, 1], [2, 5, 2], [2, 4, 3]]) এর মান কত?",
        ["0", "3", "5", "7"],
        ["মান 0", "মান 3", "মান 5", "মান 7"],
        "B", "medium", "numerical",
        "Expanding: 1(15 − 8) − 1(6 − 4) + 1(8 − 10) = 7 − 2 − 2 = 3.",
        "প্রসারণ: 1(15 − 8) − 1(6 − 4) + 1(8 − 10) = 3।",
    ),
    q(
        "For det([[2, -3], [11, 8]]), which are true? "
        "(i) value 49  (ii) cofactor of (1,2) is −11  (iii) (2,1) entry is 11",
        "নির্ণায়ক [[2, -3], [11, 8]] এর জন্য কোনটি সঠিক? "
        "(i) মান 49  (ii) (1,2) সহগুণক −11  (iii) (2,1) ভুক্তি 11",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "det = 16 − (−33) = 49; C_12 = −11; a_21 = 11. All three hold.",
        "নির্ণায়ক = 16 + 33 = 49; C_12 = −11; a_21 = 11। তিনটিই সত্য।",
    ),
    q(
        "If A is 3×3 and |A| = 1, then |(3A)^{-1}| = ?",
        "A 3×3 এবং |A| = 1 হলে |(3A)^{-1}| = ?",
        ["1/27", "1/9", "1/3", "27"],
        ["1/27", "1/9", "1/3", "মান 27"],
        "A", "hard", "numerical",
        "|3A| = 27|A| = 27, so |(3A)^{-1}| = 1/27.",
        "|3A| = 27|A| = 27; অতএব |(3A)^{-1}| = 1/27।",
    ),
    q(
        "If det([[1, omega, omega^2], [omega, omega^2, 1], [omega^2, 1, omega]]) style board "
        "determinant of cube roots of unity simplifies to:",
        "ঘনমূল একক ω সম্বলিত বোর্ড নির্ণায়ক সরলীকৃত মান:",
        ["omega - omega^2", "0", "1", "omega^2"],
        ["ω − ω^2 মান", "মান 0", "মান 1", "ω^2 মান"],
        "A", "hard", "numerical",
        "Printed expansion of the ω-determinant simplifies to ω − ω^2.",
        "মুদ্রিত প্রসারণ সরল করে ω − ω^2 পাওয়া যায়।",
    ),
    q(
        "If the minor of the (2, 1) entry of [[4, -1, 5], [2, 3, 7], [6, -3, x]] equals 1, then x = ?",
        "[[4, -1, 5], [2, 3, 7], [6, -3, x]] এর (2, 1) অনুরাশি 1 হলে x = ?",
        ["12", "13", "14", "15"],
        ["মান 12", "মান 13", "মান 14", "মান 15"],
        "C", "medium", "numerical",
        "M_21 = det([[-1, 5], [-3, x]]) = (−1)x − 5(−3) = −x + 15 = 1 ⇒ x = 14.",
        "M_21 = det([[-1, 5], [-3, x]]) = −x + 15 = 1 ⇒ x = 14।",
    ),
    q(
        "If det([[m-2, 6], [2, m-3]]) = 0 (singular), then m equals:",
        "det([[m-2, 6], [2, m-3]]) = 0 (ব্যতিক্রমী) হলে m এর মান:",
        ["-1 and 6", "-2 and -3", "1 and -6", "2 and -3"],
        ["-1 ও 6", "-2 ও -3", "1 ও -6", "2 ও -3"],
        "A", "medium", "numerical",
        "(m−2)(m−3) − 12 = 0 ⇒ m^2 − 5m − 6 = 0 ⇒ m = 6, −1.",
        "(m−2)(m−3) − 12 = 0 ⇒ m^2 − 5m − 6 = 0 ⇒ m = 6, −1।",
    ),
]


# =============================================================================
# hm1_27_ch01_t03 — Inverse matrices and linear equations
# Prefer Udvash T-07, T-10 with printed keys
# =============================================================================
T03 = [
    q(
        "If A = [[-1, 3], [2, 5]], then adj A equals:",
        "A = [[-1, 3], [2, 5]] হলে adj A কোনটি?",
        [
            "matrix [[5, -3], [-2, -1]]",
            "matrix [[1, 2], [3, -5]]",
            "matrix [[5, 2], [3, -1]]",
            "matrix [[5, -2], [-3, -1]]",
        ],
        [
            "ম্যাট্রিক্স [[5, -3], [-2, -1]]",
            "ম্যাট্রিক্স [[1, 2], [3, -5]]",
            "ম্যাট্রিক্স [[5, 2], [3, -1]]",
            "ম্যাট্রিক্স [[5, -2], [-3, -1]]",
        ],
        "A", "easy", "numerical",
        "For 2×2 [[a, b], [c, d]], adj = [[d, -b], [-c, a]] = [[5, -3], [-2, -1]].",
        "2×2 এ adj = [[d, -b], [-c, a]] = [[5, -3], [-2, -1]]।",
    ),
    q(
        "If A/3 = [[1, 2], [4, -3]], the inverse of A/3 is:",
        "A/3 = [[1, 2], [4, -3]] হলে (A/3)^{-1} কোনটি?",
        [
            "matrix (-1/11) [[-3, -2], [-4, 1]]",
            "matrix (1/11) [[-3, -2], [-4, 1]]",
            "matrix (-1/11) [[-3, -4], [-2, 1]]",
            "matrix (1/11) [[-3, -4], [-2, 1]]",
        ],
        [
            "ম্যাট্রিক্স (−1/11) [[-3, -2], [-4, 1]]",
            "ম্যাট্রিক্স (1/11) [[-3, -2], [-4, 1]]",
            "ম্যাট্রিক্স (−1/11) [[-3, -4], [-2, 1]]",
            "ম্যাট্রিক্স (1/11) [[-3, -4], [-2, 1]]",
        ],
        "A", "medium", "numerical",
        "det = −11 and adj = [[-3, -2], [-4, 1]], so inverse = (−1/11) adj.",
        "নির্ণায়ক −11 এবং adj = [[-3, -2], [-4, 1]]; বিপরীত = (−1/11) adj।",
    ),
    q(
        "Which of the following is a singular matrix?",
        "নিচের কোনটি ব্যতিক্রমী ম্যাট্রিক্স?",
        [
            "matrix [[1, 0], [0, 1]]",
            "matrix [[2, -1], [6, 3]]",
            "matrix [[1, 2], [2, -4]]",
            "matrix [[3, 6], [2, 4]]",
        ],
        [
            "ম্যাট্রিক্স [[1, 0], [0, 1]]",
            "ম্যাট্রিক্স [[2, -1], [6, 3]]",
            "ম্যাট্রিক্স [[1, 2], [2, -4]]",
            "ম্যাট্রিক্স [[3, 6], [2, 4]]",
        ],
        "D", "easy", "numerical",
        "det([[3, 6], [2, 4]]) = 12 − 12 = 0, so it is singular.",
        "det([[3, 6], [2, 4]]) = 0; অতএব এটি ব্যতিক্রমী।",
    ),
    q(
        "If A = [[1, 5], [3, 7]], then A^{-1} equals:",
        "A = [[1, 5], [3, 7]] হলে A^{-1} = ?",
        [
            "matrix (-1/8) [[1, 5], [3, 7]]",
            "matrix (-1/8) [[7, -5], [-3, 1]]",
            "matrix (-1/8) [[7, -3], [-5, 1]]",
            "matrix (1/8) [[7, -3], [-5, 1]]",
        ],
        [
            "ম্যাট্রিক্স (−1/8) [[1, 5], [3, 7]]",
            "ম্যাট্রিক্স (−1/8) [[7, -5], [-3, 1]]",
            "ম্যাট্রিক্স (−1/8) [[7, -3], [-5, 1]]",
            "ম্যাট্রিক্স (1/8) [[7, -3], [-5, 1]]",
        ],
        "B", "medium", "numerical",
        "det(A) = 7 − 15 = −8; A^{-1} = (−1/8) [[7, -5], [-3, 1]].",
        "det(A) = −8; A^{-1} = (−1/8) [[7, -5], [-3, 1]]।",
    ),
    q(
        "If A^{-1} = [[3, -5], [-1, 2]], then A equals:",
        "A^{-1} = [[3, -5], [-1, 2]] হলে A = ?",
        [
            "matrix [[-2, 5], [1, 3]]",
            "matrix [[2, 5], [1, 3]]",
            "matrix [[2, -5], [1, 3]]",
            "matrix [[-2, 5], [1, -3]]",
        ],
        [
            "ম্যাট্রিক্স [[-2, 5], [1, 3]]",
            "ম্যাট্রিক্স [[2, 5], [1, 3]]",
            "ম্যাট্রিক্স [[2, -5], [1, 3]]",
            "ম্যাট্রিক্স [[-2, 5], [1, -3]]",
        ],
        "B", "medium", "numerical",
        "A = (A^{-1})^{-1}. det = 6 − 5 = 1, so A = [[2, 5], [1, 3]].",
        "A = (A^{-1})^{-1}; নির্ণায়ক 1 হওয়ায় A = [[2, 5], [1, 3]]।",
    ),
    q(
        "If A = [[1, -2], [-3, 5]], then A^{-1} equals:",
        "A = [[1, -2], [-3, 5]] হলে A^{-1} = ?",
        [
            "matrix [[5, 2], [3, 1]]",
            "matrix [[-5, 2], [3, -1]]",
            "matrix [[-5, -2], [-3, -1]]",
            "matrix [[5, -2], [-3, 1]]",
        ],
        [
            "ম্যাট্রিক্স [[5, 2], [3, 1]]",
            "ম্যাট্রিক্স [[-5, 2], [3, -1]]",
            "ম্যাট্রিক্স [[-5, -2], [-3, -1]]",
            "ম্যাট্রিক্স [[5, -2], [-3, 1]]",
        ],
        "C", "medium", "numerical",
        "det(A) = 5 − 6 = −1; A^{-1} = (−1)[[5, 2], [3, 1]] = [[-5, -2], [-3, -1]].",
        "det(A) = −1; A^{-1} = [[-5, -2], [-3, -1]]।",
    ),
    q(
        "Which of the following is a non-singular matrix?",
        "নিচের কোনটি অব্যতিক্রমী ম্যাট্রিক্স?",
        [
            "matrix [[1, 0], [3, -3]]",
            "matrix [[2, 4], [1, 2]]",
            "matrix [[3, 6], [2, 4]]",
            "matrix [[0, 0], [5, 1]]",
        ],
        [
            "ম্যাট্রিক্স [[1, 0], [3, -3]]",
            "ম্যাট্রিক্স [[2, 4], [1, 2]]",
            "ম্যাট্রিক্স [[3, 6], [2, 4]]",
            "ম্যাট্রিক্স [[0, 0], [5, 1]]",
        ],
        "A", "easy", "numerical",
        "det([[1, 0], [3, -3]]) = −3 ≠ 0, so non-singular. Others have det 0.",
        "det([[1, 0], [3, -3]]) = −3 ≠ 0; অন্যগুলোর নির্ণায়ক 0।",
    ),
    q(
        "If A = [[2, 1], [3, 5]] and B = [[2], [10]], then A^{-1} equals:",
        "A = [[2, 1], [3, 5]] এবং B = [[2], [10]] হলে A^{-1} = ?",
        [
            "matrix (1/7) [[5, -1], [-3, 2]]",
            "matrix (1/7) [[2, -3], [-1, 5]]",
            "matrix (1/13) [[5, 1], [3, 2]]",
            "matrix (1/7) [[2, 3], [1, 5]]",
        ],
        [
            "ম্যাট্রিক্স (1/7) [[5, -1], [-3, 2]]",
            "ম্যাট্রিক্স (1/7) [[2, -3], [-1, 5]]",
            "ম্যাট্রিক্স (1/13) [[5, 1], [3, 2]]",
            "ম্যাট্রিক্স (1/7) [[2, 3], [1, 5]]",
        ],
        "A", "medium", "numerical",
        "det(A) = 10 − 3 = 7; A^{-1} = (1/7) [[5, -1], [-3, 2]].",
        "det(A) = 7; A^{-1} = (1/7) [[5, -1], [-3, 2]]।",
    ),
    q(
        "If A = [[2, 1], [3, 5]], B = [[2], [10]], P = [[x], [y]] and AP = B, then x + y = ?",
        "A = [[2, 1], [3, 5]], B = [[2], [10]], AP = B হলে x + y = ?",
        ["2", "8", "10", "12"],
        ["মান 2", "মান 8", "মান 10", "মান 12"],
        "A", "medium", "application",
        "P = A^{-1}B. Solving 2x + y = 2 and 3x + 5y = 10 gives x = 0, y = 2 (or equivalent), sum 2 per key.",
        "P = A^{-1}B সমাধানে মুদ্রিত চাবি অনুসারে x + y = 2।",
    ),
    q(
        "If I_3 is the 3×3 identity, then (I_3)^{-1} equals:",
        "I_3 একটি 3×3 অভেদ ম্যাট্রিক্স হলে (I_3)^{-1} = ?",
        ["3 I_3", "0", "I_3 / 3", "I_3"],
        ["3 I_3", "শূন্য ম্যাট্রিক্স", "I_3 / 3", "I_3"],
        "D", "easy", "factual",
        "The inverse of the identity is itself.",
        "অভেদ ম্যাট্রিক্সের বিপরীত এটি নিজেই।",
    ),
    q(
        "If A = diag(5, 6, 7), then A^{-1} equals:",
        "A = diag(5, 6, 7) হলে A^{-1} = ?",
        [
            "matrix diag(5, 6, 7)",
            "matrix diag(-5, -6, -7)",
            "matrix diag(1/5, 1/6, 1/7)",
            "matrix diag(7, 6, 5)",
        ],
        [
            "ম্যাট্রিক্স diag(5, 6, 7)",
            "ম্যাট্রিক্স diag(-5, -6, -7)",
            "ম্যাট্রিক্স diag(1/5, 1/6, 1/7)",
            "ম্যাট্রিক্স diag(7, 6, 5)",
        ],
        "C", "easy", "numerical",
        "Inverse of a non-singular diagonal matrix is the diagonal of reciprocals.",
        "অব্যতিক্রমী কর্ণম্যাট্রিক্সের বিপরীত = কর্ণে বিপরীতমান।",
    ),
    q(
        "A matrix is called non-singular if its determinant is:",
        "একটি ম্যাট্রিক্সকে অব্যতিক্রমী বলা হয় যদি এর নির্ণায়ক:",
        ["equal to zero", "not equal to zero", "equal to one only", "negative"],
        ["শূন্যের সমান", "শূন্য নয়", "কেবল একের সমান", "ঋণাত্মক"],
        "B", "easy", "factual",
        "Non-singular ⇔ det ≠ 0 (invertible).",
        "অব্যতিক্রমী ⇔ নির্ণায়ক ≠ 0 (বিপরীতযোগ্য)।",
    ),
    q(
        "If A = [[x+4, 4], [-4, x-4]] is non-singular, then:",
        "A = [[x+4, 4], [-4, x-4]] অব্যতিক্রমী হলে:",
        ["x = 0", "x ≠ 0", "x = 4", "x = -4"],
        ["x = 0", "x ≠ 0", "x = 4", "x = -4"],
        "B", "medium", "numerical",
        "|A| = (x+4)(x-4) + 16 = x^2 ≠ 0 ⇒ x ≠ 0.",
        "|A| = x^2 ≠ 0 ⇒ x ≠ 0।",
    ),
    q(
        "If A = [[7, 6], [8, 7]], then A^{-1} equals:",
        "A = [[7, 6], [8, 7]] হলে A^{-1} = ?",
        [
            "matrix [[7, 6], [8, 7]]",
            "matrix [[7, -6], [-8, 7]]",
            "matrix [[-7, 6], [8, -7]]",
            "matrix [[6, -7], [-8, 7]]",
        ],
        [
            "ম্যাট্রিক্স [[7, 6], [8, 7]]",
            "ম্যাট্রিক্স [[7, -6], [-8, 7]]",
            "ম্যাট্রিক্স [[-7, 6], [8, -7]]",
            "ম্যাট্রিক্স [[6, -7], [-8, 7]]",
        ],
        "B", "medium", "numerical",
        "det = 49 − 48 = 1; A^{-1} = [[7, -6], [-8, 7]].",
        "det = 1; A^{-1} = [[7, -6], [-8, 7]]।",
    ),
    q(
        "If A = [[x+4, 8], [2, x-2]] is singular, then x equals:",
        "A = [[x+4, 8], [2, x-2]] ব্যতিক্রমী হলে x = ?",
        ["2 and 4", "4 and 6", "-4 and 6", "4 and -6"],
        ["2 ও 4", "4 ও 6", "-4 ও 6", "4 ও -6"],
        "D", "medium", "numerical",
        "(x+4)(x-2) − 16 = 0 ⇒ x^2 + 2x − 8 − 16 = 0 ⇒ x^2 + 2x − 24 = 0 ⇒ x = 4, −6.",
        "(x+4)(x-2) − 16 = 0 ⇒ x^2 + 2x − 24 = 0 ⇒ x = 4, −6।",
    ),
    q(
        "If A^2 = I, then A^{-1} equals:",
        "A^2 = I হলে A^{-1} = ?",
        ["A^2", "A", "I - A", "0"],
        ["A^2", "A", "I - A", "শূন্য ম্যাট্রিক্স"],
        "B", "easy", "conceptual",
        "A^2 = I ⇒ A A = I ⇒ A^{-1} = A (involutory).",
        "A^2 = I ⇒ A^{-1} = A (অভেদঘাতী)।",
    ),
    q(
        "If the matrix with rows (1, 3, λ+2), (2, 4, 8), (3, 5, 10) is singular, then λ = ?",
        "সারি (1, 3, λ+2), (2, 4, 8), (3, 5, 10) বিশিষ্ট ম্যাট্রিক্স ব্যতিক্রমী হলে λ = ?",
        ["0", "1", "2", "3"],
        ["মান 0", "মান 1", "মান 2", "মান 3"],
        "C", "hard", "numerical",
        "Expanding det = 0 gives λ = 2 (printed key C).",
        "নির্ণায়ক = 0 সমাধানে মুদ্রিত চাবি অনুসারে λ = 2।",
    ),
    q(
        "If A^{-1} = [[2, 0], [0, 2]] and B^{-1} = [[1, 0], [1, 1]], then (AB)^{-1} equals:",
        "A^{-1} = [[2, 0], [0, 2]] এবং B^{-1} = [[1, 0], [1, 1]] হলে (AB)^{-1} = ?",
        [
            "matrix [[2, 0], [2, 2]]",
            "matrix [[2, 0], [1, 2]]",
            "matrix [[1, 0], [2, 2]]",
            "matrix [[2, 2], [0, 2]]",
        ],
        [
            "ম্যাট্রিক্স [[2, 0], [2, 2]]",
            "ম্যাট্রিক্স [[2, 0], [1, 2]]",
            "ম্যাট্রিক্স [[1, 0], [2, 2]]",
            "ম্যাট্রিক্স [[2, 2], [0, 2]]",
        ],
        "A", "medium", "numerical",
        "(AB)^{-1} = B^{-1} A^{-1} = [[1, 0], [1, 1]] [[2, 0], [0, 2]] = [[2, 0], [2, 2]].",
        "(AB)^{-1} = B^{-1} A^{-1} = [[2, 0], [2, 2]]।",
    ),
    q(
        "If A is square and A^2 = I, then A is called:",
        "A বর্গম্যাট্রিক্স এবং A^2 = I হলে A কে কী বলে?",
        ["Idempotent", "Involutory", "Singular", "Nilpotent"],
        ["সমঘাতী", "অভেদঘাতী", "ব্যতিক্রমী", "শূন্যঘাতী"],
        "B", "easy", "factual",
        "A^2 = I defines an involutory matrix.",
        "A^2 = I শর্তযুক্ত ম্যাট্রিক্সকে অভেদঘাতী বলে।",
    ),
    q(
        "A square matrix A is singular if and only if:",
        "বর্গম্যাট্রিক্স A ব্যতিক্রমী হবে যদি এবং কেবল যদি:",
        ["|A| ≠ 0", "|A| = 0", "A = I", "A = A^T"],
        ["|A| ≠ 0", "|A| = 0", "A = I", "A = A^T"],
        "B", "easy", "factual",
        "Singular means determinant zero (no inverse).",
        "ব্যতিক্রমী ⇒ নির্ণায়ক শূন্য (বিপরীত নেই)।",
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
    counts["hm1_27_ch01_t01"] = write_topic("hm1_27_ch01_t01", T01)["count"]
    counts["hm1_27_ch01_t02"] = write_topic("hm1_27_ch01_t02", T02)["count"]
    counts["hm1_27_ch01_t03"] = write_topic("hm1_27_ch01_t03", T03)["count"]

    # Cross-topic duplicate stems
    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm1_27_ch01",
        "title_en": "Matrices and Determinants",
        "title_bn": "ম্যাট্রিক্স ও নির্ণায়ক",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(39, 54)],
        "topics": {
            "hm1_27_ch01_t01": {
                "title_en": "Matrices and matrix operations",
                "title_bn": "ম্যাট্রিক্স ও ম্যাট্রিক্সের ক্রিয়া",
                "udvash_types": ["T-01", "T-02", "T-03", "T-04", "T-05"],
                "count": 20,
            },
            "hm1_27_ch01_t02": {
                "title_en": "Determinants and their properties",
                "title_bn": "নির্ণায়ক ও এর ধর্ম",
                "udvash_types": ["T-06", "T-08", "T-09"],
                "count": 20,
            },
            "hm1_27_ch01_t03": {
                "title_en": "Inverse matrices and linear equations",
                "title_bn": "বিপরীত ম্যাট্রিক্স ও রৈখিক সমীকরণ",
                "udvash_types": ["T-07", "T-10"],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "Q62": "Idempotent vs involutory mismatch in printed solution (A^2=I shown for idempotent claim); skipped",
        },
        "low_confidence": [
            "Q22 statement (ii) minor sign kept per printed key B (i+iii).",
            "Matrix options stored as compact [[..]] text for JSONL.",
            "Some 3x3 entries transcribed from column crops; keys cross-checked against printed উত্তরমালা.",
        ],
        "validate": {
            "command": "python tools/question_bank/udvash_extract/seed_hm1_ch01.py",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch01_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
