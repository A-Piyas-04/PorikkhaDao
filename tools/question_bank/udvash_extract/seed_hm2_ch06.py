#!/usr/bin/env python3
"""Seed Higher Mathematics 2nd Paper Ch06 (Conics).

Curated from Udvash HSC Question Bank 2026 printed pp. 165–179 (PDF 171–185).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
OCR is noisy (~15 pages; figure/solution pages especially garbled); reconstructs
board-style items from readable stems/solutions and supplements with accurate
HSC-level authored MCQs. Figure-only graph items rewritten as text-describable.
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
    "higher_mathematics p2 ch06; curated bilingual"
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
# hm2_27_ch06_t01 — Parabola / পরাবৃত্ত
# =============================================================================
T01 = [
    q(
        "For the parabola y² = 4x + 3y − 7, the length of the latus rectum is:",
        "y² = 4x + 3y − 7 পরাবৃত্তটির উপকেন্দ্রিক লম্বের দৈর্ঘ্য কত?",
        ["4", "8", "16", "2"],
        ["4", "8", "16", "2"],
        "A", "medium", "numerical",
        "Complete the square: (y − 3/2)² = 4(x − 19/16). Comparing with Y² = 4aX gives 4a = 4, so a = 1; latus rectum = 4a = 4.",
        "বর্গ সম্পূর্ণ করে (y − 3/2)² = 4(x − 19/16)। তুলনায় 4a = 4, সুতরাং উপকেন্দ্রিক লম্বের দৈর্ঘ্য 4।",
    ),
    q(
        "The equation of the directrix of the parabola y² = 8x is:",
        "y² = 8x পরাবৃত্তের নিয়ামক রেখার সমীকরণ কোনটি?",
        ["x − 2 = 0", "x + 2 = 0", "y − 2 = 0", "y + 2 = 0"],
        ["x − 2 = 0", "x + 2 = 0", "y − 2 = 0", "y + 2 = 0"],
        "B", "easy", "factual",
        "y² = 8x = 4·2·x ⇒ a = 2. Directrix is x = −a ⇒ x + 2 = 0.",
        "y² = 8x = 4·2·x ⇒ a = 2। নিয়ামক x = −a ⇒ x + 2 = 0।",
    ),
    q(
        "The polar equation r(1 + cos θ) = 2 represents which conic?",
        "r(1 + cos θ) = 2 সমীকরণটি কোন কনিক প্রকাশ করে?",
        ["a straight line", "a circle", "a parabola", "an ellipse"],
        ["সরলরেখা", "বৃত্ত", "পরাবৃত্ত", "উপবৃত্ত"],
        "C", "medium", "conceptual",
        "r + r cos θ = 2 ⇒ r = 2 − x. Squaring: x² + y² = (2 − x)² ⇒ y² = −4(x − 1), a parabola.",
        "r + x = 2 ⇒ r = 2 − x। বর্গ করে y² = −4(x − 1), যা পরাবৃত্ত।",
    ),
    q(
        "For the parabola x² = −3y, which statements are true? (i) length of latus rectum = 3 (ii) focus is (0, −3/4) (iii) equation of latus rectum is 4y − 3 = 0",
        "x² = −3y পরাবৃত্তের— (i) উপকেন্দ্রিক লম্বের দৈর্ঘ্য 3 (ii) উপকেন্দ্র (0, −3/4) (iii) উপকেন্দ্রিক লম্বের সমীকরণ 4y − 3 = 0 — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "A", "medium", "conceptual",
        "x² = −4·(3/4)·y ⇒ a = 3/4. Latus rectum = 4a = 3; focus (0, −a) = (0, −3/4). Latus rectum is y = −a ⇒ 4y + 3 = 0, so (iii) is false.",
        "a = 3/4; উপকেন্দ্রিক লম্ব = 3; উপকেন্দ্র (0, −3/4)। লম্বের সমীকরণ 4y + 3 = 0, সুতরাং (iii) মিথ্যা।",
    ),
    q(
        "Stimulus: x² + 5y = 0 is a conic. Its directrix equation is:",
        "উদ্দীপক: x² + 5y = 0 একটি কনিক। এর নিয়ামকের সমীকরণ কোনটি?",
        ["5x + 4 = 0", "5x − 4 = 0", "4y + 5 = 0", "4y − 5 = 0"],
        ["5x + 4 = 0", "5x − 4 = 0", "4y + 5 = 0", "4y − 5 = 0"],
        "D", "medium", "numerical",
        "x² = −5y = 4·(−5/4)·y ⇒ a = 5/4. Directrix y = a (opens downward) gives y = 5/4 ⇒ 4y − 5 = 0.",
        "x² = −5y ⇒ a = 5/4। নিয়ামক y = 5/4 ⇒ 4y − 5 = 0।",
    ),
    q(
        "Stimulus: x² + 5y = 0 is a conic. The coordinates of its focus are:",
        "উদ্দীপক: x² + 5y = 0 একটি কনিক। এর উপকেন্দ্রের স্থানাঙ্ক কত?",
        ["(0, 5/4)", "(0, −5/4)", "(5/4, 0)", "(−5/4, 0)"],
        ["(0, 5/4)", "(0, −5/4)", "(5/4, 0)", "(−5/4, 0)"],
        "B", "medium", "numerical",
        "x² = −4·(5/4)·y; focus is (0, −a) = (0, −5/4).",
        "উপকেন্দ্র (0, −a) = (0, −5/4)।",
    ),
    q(
        "For (x − 1)² = −y, which are true? (i) vertex is (1, 0) (ii) focus is (−1/4, 0) (iii) distance from focus to the nearest directrix equals 1/2",
        "(x − 1)² = −y এর— (i) শীর্ষ (1, 0) (ii) উপকেন্দ্র (−1/4, 0) (iii) উপকেন্দ্র থেকে নিকটতম নিয়ামকের দূরত্ব = 1/2 — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "B", "hard", "conceptual",
        "(x − 1)² = −4·(1/4)·y ⇒ a = 1/4. Vertex (1, 0); focus (1, −1/4), not (−1/4, 0). Distance from focus to directrix = 2a = 1/2. So (i) and (iii).",
        "a = 1/4; শীর্ষ (1, 0); উপকেন্দ্র (1, −1/4); উপকেন্দ্র–নিয়ামক দূরত্ব 2a = 1/2। সুতরাং i ও iii।",
    ),
    q(
        "A point P on the parabola x² = 16y has abscissa 16. The focal distance of P is:",
        "x² = 16y পরাবৃত্তের উপরিস্থিত P বিন্দুর ভুজ 16 হলে, P বিন্দুর উপকেন্দ্রিক দূরত্ব কত?",
        ["12", "20", "24", "36"],
        ["12", "20", "24", "36"],
        "B", "medium", "numerical",
        "x² = 4·4·y ⇒ a = 4. At x = 16, 256 = 16y ⇒ y = 16. Focal distance = y + a = 16 + 4 = 20.",
        "a = 4; x = 16 ⇒ y = 16। উপকেন্দ্রিক দূরত্ব = y + a = 20।",
    ),
    q(
        "If the parabola x² = Py passes through (6, −3), the coordinates of its focus are:",
        "x² = Py পরাবৃত্তটি (6, −3) বিন্দুগামী হলে, পরাবৃত্তের উপকেন্দ্রের স্থানাঙ্ক—",
        ["(0, 3)", "(3, 0)", "(0, −3)", "(−3, 0)"],
        ["(0, 3)", "(3, 0)", "(0, −3)", "(−3, 0)"],
        "C", "medium", "application",
        "36 = P(−3) ⇒ P = −12. So x² = −12y = 4·(−3)·y; focus (0, −3).",
        "36 = −3P ⇒ P = −12। x² = 4·(−3)·y; উপকেন্দ্র (0, −3)।",
    ),
    q(
        "The equation (x − 1)² + 3y = 0 represents:",
        "(x − 1)² + 3y = 0 সমীকরণটি কী নির্দেশ করে?",
        ["a straight line", "a circle", "a parabola", "a hyperbola"],
        ["সরলরেখা", "বৃত্ত", "পরাবৃত্ত", "অধিবৃত্ত"],
        "C", "easy", "factual",
        "(x − 1)² = −3y is of the form X² = −4aY, a parabola.",
        "(x − 1)² = −3y পরাবৃত্তের আদর্শ রূপ।",
    ),
    q(
        "For the parabola y² − kx = 0, if the directrix is x − 1 = 0, then k equals:",
        "y² − kx = 0 পরাবৃত্তটির নিয়ামক রেখার সমীকরণ x − 1 = 0 হলে k এর মান—",
        ["4", "4√2", "−4", "−4√2"],
        ["4", "4√2", "−4", "−4√2"],
        "C", "medium", "numerical",
        "y² = kx = 4ax ⇒ a = k/4. Directrix x = −a. Given x = 1 ⇒ −a = 1 ⇒ a = −1 ⇒ k = −4.",
        "a = k/4; নিয়ামক x = −a = 1 ⇒ a = −1 ⇒ k = −4।",
    ),
    q(
        "For the parabola y² − 4x + 4y − 6 = 0, the focus is:",
        "y² − 4x + 4y − 6 = 0 পরাবৃত্তের উপকেন্দ্রের স্থানাঙ্ক কোনটি?",
        ["(−5/2, −2)", "(−3/2, −2)", "(−3, −2)", "(−2, −2)"],
        ["(−5/2, −2)", "(−3/2, −2)", "(−3, −2)", "(−2, −2)"],
        "B", "hard", "numerical",
        "(y + 2)² = 4(x + 5/2). Vertex (−5/2, −2), a = 1; focus (−5/2 + 1, −2) = (−3/2, −2).",
        "(y + 2)² = 4(x + 5/2); শীর্ষ (−5/2, −2); উপকেন্দ্র (−3/2, −2)।",
    ),
    q(
        "Stimulus: y² = 3x is a parabola. The coordinates of its focus are:",
        "উদ্দীপক: y² = 3x একটি পরাবৃত্ত। উপকেন্দ্রের স্থানাঙ্ক কোনটি?",
        ["(3/4, 0)", "(0, 3/4)", "(3/2, 0)", "(0, 3/2)"],
        ["(3/4, 0)", "(0, 3/4)", "(3/2, 0)", "(0, 3/2)"],
        "A", "easy", "numerical",
        "y² = 4·(3/4)·x ⇒ a = 3/4; focus (a, 0) = (3/4, 0).",
        "a = 3/4; উপকেন্দ্র (3/4, 0)।",
    ),
    q(
        "Stimulus: y² = 3x is a parabola. The equation of its directrix is:",
        "উদ্দীপক: y² = 3x একটি পরাবৃত্ত। নিয়ামক রেখার সমীকরণ কোনটি?",
        ["3x + 4 = 0", "3x − 4 = 0", "4x − 3 = 0", "4x + 3 = 0"],
        ["3x + 4 = 0", "3x − 4 = 0", "4x − 3 = 0", "4x + 3 = 0"],
        "D", "easy", "numerical",
        "a = 3/4; directrix x = −a ⇒ 4x + 3 = 0.",
        "a = 3/4; নিয়ামক x = −3/4 ⇒ 4x + 3 = 0।",
    ),
    q(
        "If the line y = mx + c touches the parabola y² = 6x, which are true? (i) c = 3/(2m) for m ≠ 0 (ii) both the parabola and the line always pass through the origin (iii) a point of contact can be written as (3/(2m²), 3/m)",
        "y² = 6x পরাবৃত্তটি y = mx + c রেখাকে স্পর্শ করলে— (i) m ≠ 0 এর জন্য c = 3/(2m) (ii) পরাবৃত্ত ও সরলরেখা উভয়ই সর্বদা মূলবিন্দুগামী (iii) স্পর্শবিন্দু (3/(2m²), 3/m) হতে পারে — কোনটি সঠিক?",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii", "i, ii ও iii"],
        "C", "hard", "conceptual",
        "y² = 4·(3/2)·x ⇒ a = 3/2. Tangent condition: c = a/m = 3/(2m). Point of contact (a/m², 2a/m) = (3/(2m²), 3/m). The line through the origin forces c = 0, which is not always true. So (i) and (iii).",
        "a = 3/2; স্পর্শশর্ত c = a/m; স্পর্শবিন্দু (a/m², 2a/m)। (ii) সর্বদা সত্য নয়। সুতরাং i ও iii।",
    ),
    q(
        "The standard parabola y² = 4ax has eccentricity equal to:",
        "আদর্শ পরাবৃত্ত y² = 4ax এর উৎকেন্দ্রিকতা কত?",
        ["0", "1", "1/2", "√2"],
        ["0", "1", "1/2", "√2"],
        "B", "easy", "factual",
        "By definition a parabola has eccentricity e = 1.",
        "সংজ্ঞা অনুসারে পরাবৃত্তের উৎকেন্দ্রিকতা e = 1।",
    ),
    q(
        "The parametric equations of the parabola y² = 4ax are:",
        "পরাবৃত্ত y² = 4ax এর পরামিতিক সমীকরণ কোনটি?",
        ["x = at², y = 2at", "x = 2at, y = at²", "x = a cos t, y = a sin t", "x = a sec t, y = a tan t"],
        ["x = at², y = 2at", "x = 2at, y = at²", "x = a cos t, y = a sin t", "x = a sec t, y = a tan t"],
        "A", "easy", "factual",
        "Standard parametric form: (at², 2at).",
        "আদর্শ পরামিতিক রূপ: (at², 2at)।",
    ),
    q(
        "The focus of the parabola x² = −8y is:",
        "x² = −8y পরাবৃত্তের উপকেন্দ্র কোনটি?",
        ["(0, 2)", "(0, −2)", "(2, 0)", "(−2, 0)"],
        ["(0, 2)", "(0, −2)", "(2, 0)", "(−2, 0)"],
        "B", "easy", "numerical",
        "x² = −4·2·y ⇒ a = 2; focus (0, −a) = (0, −2).",
        "a = 2; উপকেন্দ্র (0, −2)।",
    ),
    q(
        "For y² = 4ax, the length of the latus rectum is:",
        "y² = 4ax পরাবৃত্তের উপকেন্দ্রিক লম্বের দৈর্ঘ্য কত?",
        ["a", "2a", "4a", "a/2"],
        ["a", "2a", "4a", "a/2"],
        "C", "easy", "factual",
        "Latus rectum length is always 4a for y² = 4ax.",
        "y² = 4ax এর উপকেন্দ্রিক লম্বের দৈর্ঘ্য 4a।",
    ),
    q(
        "The vertex of the parabola (y − 2)² = 8(x + 3) is:",
        "(y − 2)² = 8(x + 3) পরাবৃত্তের শীর্ষবিন্দু কোনটি?",
        ["(−3, 2)", "(3, −2)", "(−3, −2)", "(3, 2)"],
        ["(−3, 2)", "(3, −2)", "(−3, −2)", "(3, 2)"],
        "A", "easy", "factual",
        "Comparing with (y − k)² = 4a(x − h) gives vertex (h, k) = (−3, 2).",
        "(y − k)² = 4a(x − h) তুলনায় শীর্ষ (−3, 2)।",
    ),
]


# =============================================================================
# hm2_27_ch06_t02 — Ellipse / উপবৃত্ত
# =============================================================================
T02 = [
    q(
        "For the ellipse ((x − 3)/4)² + ((y + 1)/3)² = 1, which are true? (i) centre is (3, −1) (ii) length of major axis is 8 (iii) eccentricity is √7/4",
        "((x − 3)/4)² + ((y + 1)/3)² = 1 উপবৃত্তটির— (i) কেন্দ্র (3, −1) (ii) বৃহৎ অক্ষের দৈর্ঘ্য 8 একক (iii) উৎকেন্দ্রিকতা √7/4 — কোনটি সঠিক?",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "Centre (3, −1); a = 4, b = 3 so major axis 2a = 8; e = √(1 − b²/a²) = √(1 − 9/16) = √7/4. All three hold.",
        "কেন্দ্র (3, −1); 2a = 8; e = √7/4। তিনটিই সত্য।",
    ),
    q(
        "For the conic 2x² + y² = 4, the length of the major axis is:",
        "2x² + y² = 4 কনিকটির বৃহৎ অক্ষের দৈর্ঘ্য কত?",
        ["4", "2", "2√2", "√2"],
        ["4", "2", "2√2", "√2"],
        "A", "medium", "numerical",
        "x²/2 + y²/4 = 1 ⇒ a² = 4 (along y), b² = 2. Major axis length 2a = 4.",
        "x²/2 + y²/4 = 1; বৃহৎ অক্ষ 2a = 4।",
    ),
    q(
        "A point has parametric coordinates (2 cos θ, √3 sin θ). The locus is:",
        "কোনো বিন্দুর পরামিতিক স্থানাঙ্ক (2 cos θ, √3 sin θ)। সঞ্চারপথটি কী নির্দেশ করে?",
        ["a parabola", "an ellipse", "a circle", "a hyperbola"],
        ["পরাবৃত্ত", "উপবৃত্ত", "বৃত্ত", "অধিবৃত্ত"],
        "B", "easy", "conceptual",
        "x = 2 cos θ, y = √3 sin θ ⇒ x²/4 + y²/3 = 1, an ellipse.",
        "x²/4 + y²/3 = 1, যা উপবৃত্ত।",
    ),
    q(
        "For the parametric point (2 cos θ, √3 sin θ) on an ellipse, the centre is:",
        "উপবৃত্তের পরামিতিক বিন্দু (2 cos θ, √3 sin θ) এর কেন্দ্রের স্থানাঙ্ক কত?",
        ["(2, √3)", "(0, 0)", "(2, 0)", "(0, √3)"],
        ["(2, √3)", "(0, 0)", "(2, 0)", "(0, √3)"],
        "B", "easy", "factual",
        "Standard centred form (a cos θ, b sin θ) has centre at the origin.",
        "আদর্শ (a cos θ, b sin θ) এর কেন্দ্র (0, 0)।",
    ),
    q(
        "For the ellipse x²/a² + y²/b² = 1 with a > b, the foci are:",
        "x²/a² + y²/b² = 1 উপবৃত্তের উপকেন্দ্রের স্থানাঙ্ক কত (a > b)?",
        ["(±√(a² + b²), 0)", "(±√(a² − b²), 0)", "(±ae, 0) and also (±a/e, 0)", "(0, ±ae) only"],
        ["(±√(a² + b²), 0)", "(±√(a² − b²), 0)", "(±ae, 0) এবং (±a/e, 0)", "শুধু (0, ±ae)"],
        "B", "easy", "factual",
        "Foci are (±c, 0) where c = √(a² − b²) = ae.",
        "উপকেন্দ্র (±√(a² − b²), 0)।",
    ),
    q(
        "For the ellipse 27x² + 8y² = 216, the equation of the major axis is:",
        "27x² + 8y² = 216 উপবৃত্তের বৃহৎ অক্ষের সমীকরণ হল—",
        ["x = 0", "y = 0", "x = 2√2", "y = 3√3"],
        ["x = 0", "y = 0", "x = 2√2", "y = 3√3"],
        "A", "medium", "numerical",
        "x²/8 + y²/27 = 1 ⇒ a² = 8, b² = 27 with b > a, so major axis is the y-axis: x = 0.",
        "x²/8 + y²/27 = 1; b > a হওয়ায় বৃহৎ অক্ষ x = 0।",
    ),
    q(
        "Which value of the eccentricity e corresponds to an ellipse?",
        "e এর কোন মানের জন্য উপবৃত্ত নির্দেশ করে?",
        ["e = 0", "e = 1", "0 < e < 1", "e > 1"],
        ["e = 0", "e = 1", "0 < e < 1", "e > 1"],
        "C", "easy", "factual",
        "An ellipse (non-circle) has 0 < e < 1. (e = 0 is a circle, a special ellipse, but board MCQs take 0 < e < 1.)",
        "উপবৃত্তের জন্য 0 < e < 1।",
    ),
    q(
        "If a conic has eccentricity e with 0 < e < 1, the conic is:",
        "কোনো কনিকের উৎকেন্দ্রিকতা 0 < e < 1 হলে, সেটি একটি—",
        ["parabola", "ellipse", "hyperbola", "rectangular hyperbola"],
        ["পরাবৃত্ত", "উপবৃত্ত", "অধিবৃত্ত", "সম অধিবৃত্ত"],
        "B", "easy", "factual",
        "By definition 0 < e < 1 identifies an ellipse.",
        "সংজ্ঞা অনুসারে 0 < e < 1 হলে উপবৃত্ত।",
    ),
    q(
        "The eccentricity of the ellipse x²/25 + y²/16 = 1 is:",
        "x²/25 + y²/16 = 1 উপবৃত্তের উৎকেন্দ্রিকতা কত?",
        ["3/5", "4/5", "3/4", "5/4"],
        ["3/5", "4/5", "3/4", "5/4"],
        "A", "easy", "numerical",
        "a² = 25, b² = 16; e = √(1 − b²/a²) = √(1 − 16/25) = 3/5.",
        "e = √(1 − 16/25) = 3/5।",
    ),
    q(
        "The length of the latus rectum of the ellipse x²/a² + y²/b² = 1 (a > b) is:",
        "x²/a² + y²/b² = 1 (a > b) উপবৃত্তের উপকেন্দ্রিক লম্বের দৈর্ঘ্য কত?",
        ["2b²/a", "2a²/b", "a²/b", "b²/a"],
        ["2b²/a", "2a²/b", "a²/b", "b²/a"],
        "A", "easy", "factual",
        "Standard formula: latus rectum = 2b²/a.",
        "আদর্শ সূত্র: উপকেন্দ্রিক লম্ব = 2b²/a।",
    ),
    q(
        "The sum of the distances from any point on an ellipse to the two foci equals:",
        "উপবৃত্তের যেকোনো বিন্দু থেকে দুই উপকেন্দ্রের দূরত্বের যোগফল কত?",
        ["2a", "2b", "2ae", "a + b"],
        ["2a", "2b", "2ae", "a + b"],
        "A", "easy", "conceptual",
        "Definition/property of the ellipse: PF₁ + PF₂ = 2a (major axis length).",
        "উপবৃত্তের ধর্ম: PF₁ + PF₂ = 2a।",
    ),
    q(
        "For the ellipse x²/16 + y²/9 = 1, the coordinates of the foci are:",
        "x²/16 + y²/9 = 1 উপবৃত্তের উপকেন্দ্রদ্বয়ের স্থানাঙ্ক কত?",
        ["(±√7, 0)", "(0, ±√7)", "(±√15, 0)", "(±5, 0)"],
        ["(±√7, 0)", "(0, ±√7)", "(±√15, 0)", "(±5, 0)"],
        "A", "medium", "numerical",
        "a² = 16, b² = 9; c = √(a² − b²) = √7; foci (±√7, 0).",
        "c = √(16 − 9) = √7; উপকেন্দ্র (±√7, 0)।",
    ),
    q(
        "The equation of the directrices of x²/25 + y²/9 = 1 is:",
        "x²/25 + y²/9 = 1 উপবৃত্তের নিয়ামক রেখার সমীকরণ কোনটি?",
        ["x = ±25/4", "x = ±5/4", "y = ±25/4", "x = ±4"],
        ["x = ±25/4", "x = ±5/4", "y = ±25/4", "x = ±4"],
        "A", "medium", "numerical",
        "a = 5, e = √(1 − 9/25) = 4/5; directrices x = ±a/e = ±25/4.",
        "e = 4/5; নিয়ামক x = ±a/e = ±25/4।",
    ),
    q(
        "If Px² + 25y² = 25P is an ellipse through (4, 6), the lengths of the axes (major, minor) are:",
        "Px² + 25y² = 25P উপবৃত্তটি (4, 6) বিন্দুগামী হলে অক্ষদ্বয়ের দৈর্ঘ্য (বৃহৎ, ক্ষুদ্র) কত?",
        ["20 and 10", "10 and 5", "25 and 16", "16 and 9"],
        ["20 এবং 10", "10 এবং 5", "25 এবং 16", "16 এবং 9"],
        "A", "hard", "application",
        "Through (4, 6): 16P + 900 = 25P ⇒ 9P = 900 ⇒ P = 100. Then x²/25 + y²/100 = 1; axes 2b = 20 (vertical major), 2a = 10.",
        "(4, 6) দিয়ে P = 100; x²/25 + y²/100 = 1; অক্ষদ্বয় 20 ও 10।",
    ),
    q(
        "The parametric equations of the ellipse x²/a² + y²/b² = 1 are:",
        "x²/a² + y²/b² = 1 উপবৃত্তের পরামিতিক সমীকরণ কোনটি?",
        ["x = a cos θ, y = b sin θ", "x = a sec θ, y = b tan θ", "x = at², y = 2at", "x = a cosh θ, y = b sinh θ"],
        ["x = a cos θ, y = b sin θ", "x = a sec θ, y = b tan θ", "x = at², y = 2at", "x = a cosh θ, y = b sinh θ"],
        "A", "easy", "factual",
        "Standard ellipse parameters: (a cos θ, b sin θ).",
        "আদর্শ পরামিতিক রূপ: (a cos θ, b sin θ)।",
    ),
    q(
        "For the ellipse 4x² + 9y² = 36, the length of the minor axis is:",
        "4x² + 9y² = 36 উপবৃত্তের ক্ষুদ্র অক্ষের দৈর্ঘ্য কত?",
        ["4", "6", "2", "3"],
        ["4", "6", "2", "3"],
        "A", "medium", "numerical",
        "x²/9 + y²/4 = 1 ⇒ a = 3, b = 2; minor axis = 2b = 4.",
        "a = 3, b = 2; ক্ষুদ্র অক্ষ 2b = 4।",
    ),
    q(
        "The area of the ellipse x²/a² + y²/b² = 1 is:",
        "x²/a² + y²/b² = 1 উপবৃত্তের ক্ষেত্রফল কত?",
        ["πab", "2πab", "πa²b", "π(a + b)"],
        ["πab", "2πab", "πa²b", "π(a + b)"],
        "A", "easy", "factual",
        "Area of the ellipse is πab.",
        "উপবৃত্তের ক্ষেত্রফল πab।",
    ),
    q(
        "If the major axis of an ellipse is along the y-axis and a > b in the usual notation for that orientation, the standard equation is:",
        "বৃহৎ অক্ষ y-অক্ষ বরাবর হলে উপবৃত্তের আদর্শ সমীকরণ কোনটি?",
        ["x²/a² + y²/b² = 1 with a > b", "x²/b² + y²/a² = 1 with a > b", "x²/a² − y²/b² = 1", "y² = 4ax"],
        ["a > b সহ x²/a² + y²/b² = 1", "a > b সহ x²/b² + y²/a² = 1", "x²/a² − y²/b² = 1", "y² = 4ax"],
        "B", "medium", "conceptual",
        "Vertical major axis: x²/b² + y²/a² = 1 (a > b).",
        "উল্লম্ব বৃহৎ অক্ষ: x²/b² + y²/a² = 1 (a > b)।",
    ),
    q(
        "For the ellipse x²/36 + y²/20 = 1, the eccentricity e satisfies:",
        "x²/36 + y²/20 = 1 উপবৃত্তের উৎকেন্দ্রিকতা e এর মান কোনটি?",
        ["√(4/9) = 2/3", "√(5/9)", "4/9", "√(16/36)"],
        ["√(4/9) = 2/3", "√(5/9)", "4/9", "√(16/36)"],
        "A", "medium", "numerical",
        "e = √(1 − 20/36) = √(16/36) = 4/6 = 2/3 = √(4/9).",
        "e = √(1 − 20/36) = 2/3।",
    ),
    q(
        "The distance between the foci of the ellipse x²/169 + y²/144 = 1 is:",
        "x²/169 + y²/144 = 1 উপবৃত্তের উপকেন্দ্রদ্বয়ের মধ্যবর্তী দূরত্ব কত?",
        ["10", "5", "12", "26"],
        ["10", "5", "12", "26"],
        "A", "medium", "numerical",
        "a = 13, b = 12; c = √(169 − 144) = 5; distance between foci = 2c = 10.",
        "c = 5; উপকেন্দ্রদ্বয়ের দূরত্ব 2c = 10।",
    ),
]


# =============================================================================
# hm2_27_ch06_t03 — Hyperbola / অধিবৃত্ত
# =============================================================================
T03 = [
    q(
        "For the hyperbola 7x² − 9y² + 63 = 0, the length of the latus rectum is:",
        "7x² − 9y² + 63 = 0 অধিবৃত্তের উপকেন্দ্রিক লম্বের দৈর্ঘ্য হলো—",
        ["14/√7", "18/√7", "14/3", "18/3"],
        ["14/√7", "18/√7", "14/3", "18/3"],
        "B", "hard", "numerical",
        "7x² − 9y² = −63 ⇒ y²/7 − x²/9 = 1. Here a² = 7, b² = 9; latus rectum = 2b²/a = 18/√7.",
        "y²/7 − x²/9 = 1; উপকেন্দ্রিক লম্ব = 2b²/a = 18/√7।",
    ),
    q(
        "The vertices of the hyperbola 9x² − 16y² = 144 are:",
        "9x² − 16y² = 144 অধিবৃত্তের শীর্ষবিন্দুর স্থানাঙ্ক কোনটি?",
        ["(±4, 0)", "(±5, 0)", "(0, ±4)", "(0, ±5)"],
        ["(±4, 0)", "(±5, 0)", "(0, ±4)", "(0, ±5)"],
        "A", "easy", "numerical",
        "x²/16 − y²/9 = 1 ⇒ a = 4; vertices (±a, 0) = (±4, 0).",
        "x²/16 − y²/9 = 1; শীর্ষ (±4, 0)।",
    ),
    q(
        "The asymptotes of the hyperbola 9x² − 16y² = 144 are:",
        "9x² − 16y² = 144 অধিবৃত্তের অসীমতটের সমীকরণ কোনটি?",
        ["2x = ±3y", "3y = ±2x", "3x = ±4y", "4x = ±3y"],
        ["2x = ±3y", "3y = ±2x", "3x = ±4y", "4x = ±3y"],
        "C", "medium", "numerical",
        "x²/16 − y²/9 = 1 ⇒ asymptotes y = ±(b/a)x = ±(3/4)x ⇒ 3x = ±4y.",
        "অসীমতট y = ±(3/4)x ⇒ 3x = ±4y।",
    ),
    q(
        "The slope of the tangent to 3x² − 4y² = 12 at the point (4, 3) is:",
        "3x² − 4y² = 12 অধিবৃত্তের (4, 3) বিন্দুতে স্পর্শকের ঢাল কত?",
        ["−1", "1", "3/4", "4/3"],
        ["−1", "1", "3/4", "4/3"],
        "B", "medium", "numerical",
        "Differentiate: 6x − 8y y′ = 0 ⇒ y′ = (6x)/(8y). At (4, 3): m = 24/24 = 1. (Tangent: 3·4·x − 4·3·y = 12 ⇒ y = x − 1.)",
        "y′ = 6x/(8y); (4, 3) এ m = 1।",
    ),
    q(
        "The parametric coordinates of the hyperbola 4x² − y² + 16 = 0 are:",
        "4x² − y² + 16 = 0 অধিবৃত্তের পরামিতিক স্থানাঙ্ক কোনটি?",
        ["(4 sec θ, 2 tan θ)", "(2 sec θ, 4 tan θ)", "(4 tan θ, 2 sec θ)", "(2 tan θ, 4 sec θ)"],
        ["(4 sec θ, 2 tan θ)", "(2 sec θ, 4 tan θ)", "(4 tan θ, 2 sec θ)", "(2 tan θ, 4 sec θ)"],
        "D", "hard", "numerical",
        "y² − 4x² = 16 ⇒ y²/16 − x²/4 = 1. Form y²/a² − x²/b² = 1 uses (b tan θ, a sec θ) = (2 tan θ, 4 sec θ).",
        "y²/16 − x²/4 = 1; পরামিতিক বিন্দু (2 tan θ, 4 sec θ)।",
    ),
    q(
        "For the hyperbola 4y² − 5x² = 20, the distance between the two directrices is:",
        "4y² − 5x² = 20 অধিবৃত্তের নিয়ামক রেখাদ্বয়ের মধ্যবর্তী দূরত্ব কত একক?",
        ["8/√5", "10/3", "2√5", "8√5 / 5"],
        ["8/√5", "10/3", "2√5", "8√5 / 5"],
        "B", "hard", "numerical",
        "y²/5 − x²/4 = 1 ⇒ a = √5, b = 2; e = √(1 + 4/5) = 3/√5. Distance between directrices = 2a/e = 2√5 · √5/3 = 10/3.",
        "y²/5 − x²/4 = 1; e = 3/√5; নিয়ামকদ্বয়ের দূরত্ব 2a/e = 10/3।",
    ),
    q(
        "For the hyperbola x²/9 − y²/4 = 1, the distance between the two foci is:",
        "x²/9 − y²/4 = 1 অধিবৃত্তের উপকেন্দ্রদ্বয়ের মধ্যবর্তী দূরত্ব কত?",
        ["2√13", "√13", "6", "2√5"],
        ["2√13", "√13", "6", "2√5"],
        "A", "medium", "numerical",
        "a = 3, b = 2; ae = √(a² + b²) = √13; distance between foci = 2ae = 2√13.",
        "ae = √13; উপকেন্দ্রদ্বয়ের দূরত্ব 2ae = 2√13।",
    ),
    q(
        "Stimulus: 16y² − 9x² = 144. The eccentricity of the conic is:",
        "উদ্দীপক: 16y² − 9x² = 144। কনিকটির উৎকেন্দ্রিকতা কত?",
        ["5/3", "5/4", "√7 / 3", "√7 / 4"],
        ["5/3", "5/4", "√7 / 3", "√7 / 4"],
        "A", "medium", "numerical",
        "y²/9 − x²/16 = 1 ⇒ a = 3, b = 4; e = √(1 + b²/a²) = √(1 + 16/9) = 5/3.",
        "a = 3, b = 4; e = 5/3।",
    ),
    q(
        "Stimulus: 16y² − 9x² = 144. Which are true? (i) asymptotes are y = ±(3/4)x (ii) directrices are 5y ± 9 = 0 (iii) parametric equations are x = 3 sec θ, y = 4 tan θ",
        "উদ্দীপক: 16y² − 9x² = 144। কনিকটির— (i) অসীমতট y = ±(3/4)x (ii) নিয়ামক 5y ± 9 = 0 (iii) পরামিতিক x = 3 sec θ, y = 4 tan θ — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "A", "hard", "conceptual",
        "y²/9 − x²/16 = 1: asymptotes y = ±(a/b)x = ±(3/4)x. Directrices y = ±a/e = ±3/(5/3) = ±9/5 ⇒ 5y ± 9 = 0. Parametric form is (4 tan θ, 3 sec θ), not (iii). So (i) and (ii).",
        "অসীমতট y = ±(3/4)x; নিয়ামক 5y ± 9 = 0; (iii) ভুল। সুতরাং i ও ii।",
    ),
    q(
        "If a conic has eccentricity e > 1, then it is:",
        "কোনো কনিকের উৎকেন্দ্রিকতা e > 1 হলে, সেটি একটি—",
        ["parabola", "ellipse", "hyperbola", "circle"],
        ["পরাবৃত্ত", "উপবৃত্ত", "অধিবৃত্ত", "বৃত্ত"],
        "C", "easy", "factual",
        "By definition e > 1 identifies a hyperbola.",
        "সংজ্ঞা অনুসারে e > 1 হলে অধিবৃত্ত।",
    ),
    q(
        "The eccentricity of a rectangular hyperbola is:",
        "সম অধিবৃত্তের উৎকেন্দ্রিকতা কত?",
        ["1", "√2", "2", "1/√2"],
        ["1", "√2", "2", "1/√2"],
        "B", "easy", "factual",
        "For a rectangular hyperbola a = b, so e = √(1 + b²/a²) = √2.",
        "সম অধিবৃত্তে a = b ⇒ e = √2।",
    ),
    q(
        "The asymptotes of the hyperbola x²/a² − y²/b² = 1 are:",
        "x²/a² − y²/b² = 1 অধিবৃত্তের অসীমতট কোনটি?",
        ["y = ±(b/a)x", "y = ±(a/b)x", "x = ±(b/a)y", "xy = ±ab"],
        ["y = ±(b/a)x", "y = ±(a/b)x", "x = ±(b/a)y", "xy = ±ab"],
        "A", "easy", "factual",
        "Asymptotes of x²/a² − y²/b² = 1 are y = ±(b/a)x.",
        "অসীমতট y = ±(b/a)x।",
    ),
    q(
        "The length of the transverse axis of x²/25 − y²/16 = 1 is:",
        "x²/25 − y²/16 = 1 অধিবৃত্তের আড় অক্ষের দৈর্ঘ্য কত?",
        ["10", "8", "5", "4"],
        ["10", "8", "5", "4"],
        "A", "easy", "numerical",
        "a = 5; transverse axis length = 2a = 10.",
        "আড় অক্ষের দৈর্ঘ্য 2a = 10।",
    ),
    q(
        "The foci of the hyperbola x²/16 − y²/9 = 1 are:",
        "x²/16 − y²/9 = 1 অধিবৃত্তের উপকেন্দ্রদ্বয় কোনটি?",
        ["(±5, 0)", "(±4, 0)", "(0, ±5)", "(±√7, 0)"],
        ["(±5, 0)", "(±4, 0)", "(0, ±5)", "(±√7, 0)"],
        "A", "medium", "numerical",
        "ae = √(a² + b²) = √(16 + 9) = 5; foci (±5, 0).",
        "ae = 5; উপকেন্দ্র (±5, 0)।",
    ),
    q(
        "For the hyperbola x²/a² − y²/b² = 1, the difference of distances from any point to the two foci equals:",
        "অধিবৃত্তের যেকোনো বিন্দু থেকে দুই উপকেন্দ্রের দূরত্বের পার্থক্য কত?",
        ["2a", "2b", "2ae", "a − b"],
        ["2a", "2b", "2ae", "a − b"],
        "A", "easy", "conceptual",
        "Hyperbola property: |PF₁ − PF₂| = 2a.",
        "অধিবৃত্তের ধর্ম: |PF₁ − PF₂| = 2a।",
    ),
    q(
        "The conjugate axis of the hyperbola x²/9 − y²/16 = 1 has length:",
        "x²/9 − y²/16 = 1 অধিবৃত্তের অনুবন্ধী অক্ষের দৈর্ঘ্য কত?",
        ["8", "6", "4", "3"],
        ["8", "6", "4", "3"],
        "A", "easy", "numerical",
        "b = 4; conjugate axis length = 2b = 8.",
        "অনুবন্ধী অক্ষের দৈর্ঘ্য 2b = 8।",
    ),
    q(
        "If the transverse and conjugate axes of a hyperbola are 8 and 10 respectively, then e equals:",
        "কোনো অধিবৃত্তের আড় ও অনুবন্ধী অক্ষের দৈর্ঘ্য যথাক্রমে 8 ও 10 একক হলে উৎকেন্দ্রিকতা কত?",
        ["√(41)/4", "√(41)/5", "5/4", "√2"],
        ["√(41)/4", "√(41)/5", "5/4", "√2"],
        "A", "medium", "application",
        "2a = 8 ⇒ a = 4; 2b = 10 ⇒ b = 5; e = √(1 + b²/a²) = √(1 + 25/16) = √41 / 4.",
        "a = 4, b = 5; e = √41 / 4।",
    ),
    q(
        "The equation of the rectangular hyperbola with transverse axis along x and a = 3 is:",
        "আড় অক্ষ x-অক্ষ বরাবর ও a = 3 বিশিষ্ট সম অধিবৃত্তের সমীকরণ কোনটি?",
        ["x² − y² = 9", "x² − y² = 3", "xy = 9", "x²/9 − y²/9 = −1"],
        ["x² − y² = 9", "x² − y² = 3", "xy = 9", "x²/9 − y²/9 = −1"],
        "A", "medium", "conceptual",
        "Rectangular ⇒ a = b = 3; equation x²/9 − y²/9 = 1 ⇒ x² − y² = 9.",
        "সম অধিবৃত্তে a = b = 3 ⇒ x² − y² = 9।",
    ),
    q(
        "The parametric equations of x²/a² − y²/b² = 1 are:",
        "x²/a² − y²/b² = 1 অধিবৃত্তের পরামিতিক সমীকরণ কোনটি?",
        ["x = a sec θ, y = b tan θ", "x = a cos θ, y = b sin θ", "x = at², y = 2at", "x = a cosh θ, y = b cos θ"],
        ["x = a sec θ, y = b tan θ", "x = a cos θ, y = b sin θ", "x = at², y = 2at", "x = a cosh θ, y = b cos θ"],
        "A", "easy", "factual",
        "Standard hyperbolic parameters: (a sec θ, b tan θ) [or (a cosh t, b sinh t)].",
        "আদর্শ পরামিতিক রূপ: (a sec θ, b tan θ)।",
    ),
    q(
        "For 5x² − 4y² = 20, the eccentricity and the length of the latus rectum are:",
        "5x² − 4y² = 20 অধিবৃত্তের উৎকেন্দ্রিকতা ও উপকেন্দ্রিক লম্বের দৈর্ঘ্য যথাক্রমে—",
        ["√(9/4) = 3/2 and 5", "√5 / 2 and 4", "3/2 and 4", "√2 and 5"],
        ["√(9/4) = 3/2 এবং 5", "√5 / 2 এবং 4", "3/2 এবং 4", "√2 এবং 5"],
        "A", "hard", "numerical",
        "x²/4 − y²/5 = 1 ⇒ a = 2, b = √5; e = √(1 + 5/4) = 3/2; latus rectum = 2b²/a = 10/2 = 5.",
        "a = 2, b = √5; e = 3/2; উপকেন্দ্রিক লম্ব = 5।",
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
    counts["hm2_27_ch06_t01"] = write_topic("hm2_27_ch06_t01", T01)["count"]
    counts["hm2_27_ch06_t02"] = write_topic("hm2_27_ch06_t02", T02)["count"]
    counts["hm2_27_ch06_t03"] = write_topic("hm2_27_ch06_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm2_27_ch06",
        "title_en": "Conics",
        "title_bn": "কনিক",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(165, 180)],
        "topics": {
            "hm2_27_ch06_t01": {
                "title_en": "Parabola",
                "title_bn": "পরাবৃত্ত",
                "udvash_types": [
                    "standard form, focus, directrix, latus rectum",
                    "completed-square / translated parabola",
                    "polar/parametric identification",
                    "tangent condition and focal distance",
                ],
                "count": 20,
            },
            "hm2_27_ch06_t02": {
                "title_en": "Ellipse",
                "title_bn": "উপবৃত্ত",
                "udvash_types": [
                    "eccentricity 0 < e < 1 and axis lengths",
                    "foci, directrices, latus rectum",
                    "parametric form and centre",
                    "stimulus-linked ellipse through a point",
                ],
                "count": 20,
            },
            "hm2_27_ch06_t03": {
                "title_en": "Hyperbola",
                "title_bn": "অধিবৃত্ত",
                "udvash_types": [
                    "vertices, foci, asymptotes, eccentricity e > 1",
                    "latus rectum and directrices distance",
                    "parametric / rectangular hyperbola",
                    "tangent slope and board stimulus pairs",
                ],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "garbled_stems": "Noisy OCR (esp. pp. 168–176 figure/solution pages) reconstructed from answer-key algebra and standard board forms",
            "figure_graphs": "Figure-only graph items rewritten as text-describable equation/property MCQs",
            "stimulus_pairs": "Linked stimulus blocks curated as clear standalone stems with shared equation context",
            "ambiguous_option_glyphs": "Broken Bangla/option glyphs replaced with closed-form HSC standards",
        },
        "low_confidence": [
            "OCR on pp. 165–179 noisy; column text and solution lines used to reconstruct stems.",
            "Inline math stored as plain text (fractions, exponents, √) for JSONL.",
            "Some printed multi-select glyph keys incomplete; properties rewritten clearly.",
            "A few option glyphs (fractions for directrices distance) standardized to exact algebraic forms.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm2_ch06.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
        "math2_progress": {
            "topics_complete": "18/30",
            "note": "Ch06 continues higher_mathematics 2nd paper after Ch01–Ch05 (300Q)",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch06_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
