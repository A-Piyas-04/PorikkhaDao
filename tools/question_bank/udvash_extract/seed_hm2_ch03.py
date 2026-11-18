#!/usr/bin/env python3
"""Seed Higher Mathematics 2nd Paper Ch03 (Complex Numbers).

Curated from Udvash HSC Question Bank 2026 printed pp. 63–71 (PDF 69–77).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
OCR is noisy (~9 pages); reconstructs board-style items from solutions/column
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
    "higher_mathematics p2 ch03; curated bilingual"
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
# hm2_27_ch03_t01 — Complex number operations / জটিল সংখ্যার ক্রিয়া
# =============================================================================
T01 = [
    q(
        "If i is the imaginary unit, what is the value of i^{2}?",
        "i কাল্পনিক একক হলে i^{2} এর মান কত?",
        ["−1", "1", "i", "−i"],
        ["−1", "1", "i", "−i"],
        "A", "easy", "factual",
        "By definition i^{2} = −1.",
        "সংজ্ঞা অনুসারে i^{2} = −1।",
    ),
    q(
        "The value of i^{59} + i^{15} is:",
        "i^{59} + i^{15} এর মান কত?",
        ["−2i", "2i", "0", "−2"],
        ["−2i", "2i", "0", "−2"],
        "A", "medium", "numerical",
        "i^{59} = i^{4·14+3} = i^{3} = −i and i^{15} = i^{3} = −i, so the sum is −2i.",
        "i^{59} = i^{3} = −i এবং i^{15} = −i; যোগফল −2i।",
    ),
    q(
        "If ω is a complex cube root of unity, then 1 + ω + ω^{2} equals:",
        "ω এককের একটি জটিল ঘনমূল হলে 1 + ω + ω^{2} এর মান কত?",
        ["0", "1", "−1", "ω"],
        ["0", "1", "−1", "ω"],
        "A", "easy", "factual",
        "The non-real cube roots of unity satisfy 1 + ω + ω^{2} = 0.",
        "এককের অবাস্তব ঘনমূলের জন্য 1 + ω + ω^{2} = 0।",
    ),
    q(
        "If a and b are the imaginary cube roots of unity, which statements are true? (i) a^{2} = b (ii) a^{2} + b^{2} = −1 (iii) ab = 1",
        "এককের কাল্পনিক ঘনমূল a ও b হলে— (i) a^{2} = b (ii) a^{2} + b^{2} = −1 (iii) ab = 1 — কোনটি সঠিক?",
        ["i, ii and iii", "i and ii only", "i and iii only", "ii and iii only"],
        ["i, ii ও iii", "শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii"],
        "A", "medium", "conceptual",
        "With a = ω and b = ω^{2}: a^{2} = ω^{2} = b, a^{2} + b^{2} = ω^{2} + ω = −1, and ab = ω^{3} = 1.",
        "a = ω, b = ω^{2} হলে তিনটি বিবৃতিই সত্য।",
    ),
    q(
        "If z = −3 + 2i, then zz̄ equals:",
        "z = −3 + 2i হলে zz̄ এর মান কত?",
        ["13", "5", "−13", "9 − 4i"],
        ["13", "5", "−13", "9 − 4i"],
        "A", "easy", "numerical",
        "z̄ = −3 − 2i, so zz̄ = (−3)^{2} + 2^{2} = 13.",
        "zz̄ = (−3)^{2} + 2^{2} = 13।",
    ),
    q(
        "For z = −3 + 2i, which statements about zz̄ are true? (i) it is real (ii) it is positive (iii) it is a non-real complex number",
        "z = −3 + 2i হলে zz̄ সম্পর্কে— (i) বাস্তব সংখ্যা (ii) ধনাত্মক সংখ্যা (iii) অবাস্তব জটিল সংখ্যা — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "A", "easy", "conceptual",
        "zz̄ = |z|^{2} = 13, which is real and positive; (iii) is false.",
        "zz̄ = 13 বাস্তব ও ধনাত্মক; (iii) মিথ্যা।",
    ),
    q(
        "If x + iy = −2 − i, then the value of y is:",
        "x + iy = −2 − i হলে y এর মান কত?",
        ["−1", "1", "−2", "2"],
        ["−1", "1", "−2", "2"],
        "A", "easy", "numerical",
        "Equating imaginary parts gives y = −1.",
        "কাল্পনিক অংশ তুলনায় y = −1।",
    ),
    q(
        "If ω is an imaginary cube root of unity, then (ω + ω^{2})^{−120} equals:",
        "ω এককের একটি কাল্পনিক ঘনমূল হলে (ω + ω^{2})^{−120} এর মান কত?",
        ["1", "0", "−1", "ω"],
        ["1", "0", "−1", "ω"],
        "A", "medium", "numerical",
        "ω + ω^{2} = −1, so (−1)^{−120} = 1.",
        "ω + ω^{2} = −1; (−1)^{−120} = 1।",
    ),
    q(
        "If the non-real complex cube roots of 8 are z₁ and z₂, then (1/2)(z₁ + z₂) equals:",
        "8 এর অবাস্তব জটিল ঘনমূল z₁ ও z₂ হলে (1/2)(z₁ + z₂) এর মান কত?",
        ["−1", "−2", "1", "2"],
        ["−1", "−2", "1", "2"],
        "A", "medium", "numerical",
        "x^{3} − 8 = 0 ⇒ non-real roots −1 ± √3 i; their average is −1.",
        "অবাস্তব মূল −1 ± √3 i; গড় −1।",
    ),
    q(
        "If x = (1/2)(−1 − √3 i), then 1/x equals:",
        "x = (1/2)(−1 − √3 i) হলে 1/x এর মান কত?",
        ["(1/2)(−1 + √3 i)", "(1/2)(−1 − √3 i)", "2", "−2"],
        ["(1/2)(−1 + √3 i)", "(1/2)(−1 − √3 i)", "2", "−2"],
        "A", "hard", "numerical",
        "x = ω^{2}, so 1/x = ω = (1/2)(−1 + √3 i).",
        "x = ω^{2} হলে 1/x = ω = (1/2)(−1 + √3 i)।",
    ),
    q(
        "If z = (1 − i)^{3}, then z equals:",
        "z = (1 − i)^{3} হলে z এর মান কত?",
        ["−2 − 2i", "−2 + 2i", "2 − 2i", "2 + 2i"],
        ["−2 − 2i", "−2 + 2i", "2 − 2i", "2 + 2i"],
        "A", "medium", "numerical",
        "(1 − i)^{3} = 1 − 3i + 3i^{2} − i^{3} = −2 − 2i.",
        "(1 − i)^{3} = −2 − 2i।",
    ),
    q(
        "If n ∈ N, then i^{4n+3} equals:",
        "n ∈ N হলে i^{4n+3} এর মান কত?",
        ["−i", "i", "1", "−1"],
        ["−i", "i", "1", "−1"],
        "A", "easy", "factual",
        "i^{4n+3} = (i^{4})^{n} · i^{3} = −i.",
        "i^{4n+3} = i^{3} = −i।",
    ),
    q(
        "If p and q are the two imaginary cube roots of unity, which is correct? (i) p = q^{2} (ii) p^{2} = q (iii) p + q = −1",
        "p ও q এককের দুইটি কাল্পনিক ঘনমূল হলে— (i) p = q^{2} (ii) p^{2} = q (iii) p + q = −1 — কোনটি সঠিক?",
        ["i, ii and iii", "i and ii only", "ii and iii only", "i and iii only"],
        ["i, ii ও iii", "শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii"],
        "A", "medium", "conceptual",
        "p = ω, q = ω^{2} gives p = q^{2}, p^{2} = q, and p + q = −1.",
        "p = ω, q = ω^{2} হলে তিনটিই সত্য।",
    ),
    q(
        "If one root of 2x^{3} − 7x^{2} + 10x + 7 = 0 is 2 + i√3, the real root is:",
        "2x^{3} − 7x^{2} + 10x + 7 = 0 এর একটি মূল 2 + i√3 হলে বাস্তব মূলটি কত?",
        ["−1/2", "1/2", "−1", "1"],
        ["−1/2", "1/2", "−1", "1"],
        "A", "hard", "numerical",
        "Conjugate 2 − i√3 is also a root. Sum of roots = 7/2 ⇒ real root = 7/2 − 4 = −1/2.",
        "মূলের যোগফল 7/2; বাস্তব মূল −1/2।",
    ),
    q(
        "If ω is an imaginary cube root of unity, then (1 − ω)(1 − ω^{2}) equals:",
        "ω এককের কাল্পনিক ঘনমূল হলে (1 − ω)(1 − ω^{2}) এর মান কত?",
        ["3", "0", "1", "−1"],
        ["3", "0", "1", "−1"],
        "A", "medium", "numerical",
        "(1 − ω)(1 − ω^{2}) = 1 − ω − ω^{2} + ω^{3} = 1 − (−1) + 1 = 3.",
        "1 − (ω + ω^{2}) + ω^{3} = 1 − (−1) + 1 = 3।",
    ),
    q(
        "If z₁ = −3 + 2i and z₂ = −5 − 3i, then |z₁ − z₂| equals:",
        "z₁ = −3 + 2i এবং z₂ = −5 − 3i হলে |z₁ − z₂| এর মান কত?",
        ["√29", "√5", "5", "√13"],
        ["√29", "√5", "5", "√13"],
        "A", "medium", "numerical",
        "z₁ − z₂ = 2 + 5i, so |z₁ − z₂| = √(4 + 25) = √29.",
        "z₁ − z₂ = 2 + 5i; পরমমান √29।",
    ),
    q(
        "If z₁ = −3 + 2i and z₂ = −5 − 3i, the point representing z₁z₂ lies in which quadrant?",
        "z₁ = −3 + 2i এবং z₂ = −5 − 3i হলে z₁z₂ এর প্রতিরূপী বিন্দু কোন চতুর্ভাগে?",
        ["fourth", "first", "second", "third"],
        ["চতুর্থ", "প্রথম", "দ্বিতীয়", "তৃতীয়"],
        "A", "medium", "application",
        "z₁z₂ = 21 − i, so the point (21, −1) is in the fourth quadrant.",
        "z₁z₂ = 21 − i; বিন্দু (21, −1) চতুর্থ চতুর্ভাগে।",
    ),
    q(
        "The value of i + i^{3} + i^{5} + i^{7} + i^{9} is:",
        "i + i^{3} + i^{5} + i^{7} + i^{9} এর মান কত?",
        ["i", "−i", "0", "1"],
        ["i", "−i", "0", "1"],
        "A", "medium", "numerical",
        "i − i + i − i + i = i.",
        "i − i + i − i + i = i।",
    ),
    q(
        "If A + iB = (2 − 3i)/(5 − 4i), then B equals:",
        "A + iB = (2 − 3i)/(5 − 4i) হলে B এর মান কত?",
        ["−7/41", "7/41", "−22/41", "22/41"],
        ["−7/41", "7/41", "−22/41", "22/41"],
        "A", "hard", "numerical",
        "(2−3i)(5+4i)/41 = (22 − 7i)/41, so B = −7/41.",
        "(22 − 7i)/41; B = −7/41।",
    ),
    q(
        "If x + iy = 2i + 3i^{2} + 4i^{3} + 5i^{4}, then xy equals:",
        "x + iy = 2i + 3i^{2} + 4i^{3} + 5i^{4} হলে xy এর মান কত?",
        ["−4", "4", "2", "−2"],
        ["−4", "4", "2", "−2"],
        "A", "medium", "numerical",
        "Expression simplifies to 2 − 2i, so xy = (2)(−2) = −4.",
        "মান 2 − 2i; xy = −4।",
    ),
]


# =============================================================================
# hm2_27_ch03_t02 — Modulus, argument and conjugate / পরমমান, আর্গুমেন্ট ও অনুবন্ধী
# =============================================================================
T02 = [
    q(
        "If z = √3 + i, which statements are true? (i) |z| = 2 (ii) arg(z) = π/6 (iii) conjugate is −√3 + i",
        "জটিল সংখ্যা √3 + i এর— (i) মডুলাস = 2 (ii) আর্গুমেন্ট = π/6 (iii) অনুবন্ধী −√3 + i — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "A", "medium", "conceptual",
        "|z| = 2 and arg = π/6; conjugate is √3 − i, so (iii) is false.",
        "|z| = 2 ও arg = π/6 সত্য; অনুবন্ধী √3 − i।",
    ),
    q(
        "The principal argument of −1 − i is:",
        "−1 − i এর মুখ্য আর্গুমেন্ট কোনটি?",
        ["−135°", "45°", "135°", "225°"],
        ["−135°", "45°", "135°", "225°"],
        "A", "medium", "numerical",
        "Third-quadrant: −180° + 45° = −135°.",
        "−180° + 45° = −135°।",
    ),
    q(
        "If z₁ and z₂ are complex numbers with z₂ ≠ 0, which are always true? (i) |z₁ − z₂| ≥ ||z₁| − |z₂|| (ii) arg(z₁/z₂) = arg(z₁) − arg(z₂) (iii) |z₁/z₂| = |z₁|/|z₂|",
        "z₁ ও z₂ দুটি জটিল সংখ্যা (z₂ ≠ 0) হলে— (i) |z₁ − z₂| ≥ ||z₁| − |z₂|| (ii) arg(z₁/z₂) = arg(z₁) − arg(z₂) (iii) |z₁/z₂| = |z₁|/|z₂| — কোনটি সঠিক?",
        ["i, ii and iii", "i and ii only", "ii and iii only", "i and iii only"],
        ["i, ii ও iii", "শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii"],
        "A", "medium", "conceptual",
        "Triangle inequality, argument of quotient, and modulus of quotient all hold.",
        "ত্রিভুজ অসমতা ও ভাগের আর্গুমেন্ট/মডুলাস—সব সত্য।",
    ),
    q(
        "The value of |(1 − i)/(1 + i)| is:",
        "|(1 − i)/(1 + i)| এর মান কত?",
        ["1", "0", "√2", "i"],
        ["1", "0", "√2", "i"],
        "A", "easy", "numerical",
        "|1 − i| = |1 + i| = √2, so the quotient has modulus 1.",
        "উভয় পরমমান √2; ভাগফলের মডুলাস 1।",
    ),
    q(
        "If z = 5 + 12i, a square root of z is:",
        "z = 5 + 12i হলে z এর একটি বর্গমূল কোনটি?",
        ["±(3 + 2i)", "±(2 + 3i)", "±(3 − 2i)", "±(−2 + 3i)"],
        ["±(3 + 2i)", "±(2 + 3i)", "±(3 − 2i)", "±(−2 + 3i)"],
        "A", "hard", "numerical",
        "(3 + 2i)^{2} = 9 + 12i + 4i^{2} = 5 + 12i.",
        "(3 + 2i)^{2} = 5 + 12i।",
    ),
    q(
        "The conjugate of 5 + 12i is represented by the point:",
        "5 + 12i এর অনুবন্ধী জটিল সংখ্যাটিকে কোন বিন্দু দ্বারা প্রকাশ করা যায়?",
        ["(5, −12)", "(−5, 12)", "(12, −5)", "(−12, 5)"],
        ["(5, −12)", "(−5, 12)", "(12, −5)", "(−12, 5)"],
        "A", "easy", "factual",
        "Conjugate 5 − 12i corresponds to (5, −12).",
        "অনুবন্ধী 5 − 12i → বিন্দু (5, −12)।",
    ),
    q(
        "If z = −1 − i, which are true? (i) arg(z) = −3π/4 (ii) Re(z) = −1 (iii) conjugate is 1 − i",
        "z = −1 − i হলে— (i) আর্গুমেন্ট = −3π/4 (ii) বাস্তব অংশ −1 (iii) অনুবন্ধী 1 − i — কোনটি সঠিক?",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii", "i, ii ও iii"],
        "A", "medium", "conceptual",
        "arg = −3π/4 and Re = −1; conjugate is −1 + i, not 1 − i.",
        "(i) ও (ii) সত্য; অনুবন্ধী −1 + i।",
    ),
    q(
        "If z = 2x + 3iy and |z| = 1, the locus is:",
        "z = 2x + 3iy এবং |z| = 1 হলে সঞ্চারপথ কোনটি?",
        ["ellipse", "circle", "parabola", "hyperbola"],
        ["উপবৃত্ত", "বৃত্ত", "পরাবৃত্ত", "অধিবৃত্ত"],
        "A", "medium", "application",
        "4x^{2} + 9y^{2} = 1 is an ellipse.",
        "4x^{2} + 9y^{2} = 1 একটি উপবৃত্ত।",
    ),
    q(
        "If z = 1 − i, which are true? (i) |z| = √2 (ii) arg(z) = −π/4 (iii) z + z̄ = 2",
        "z = 1 − i হলে— (i) |z| = √2 (ii) arg(z) = −π/4 (iii) z + z̄ = 2 — কোনটি সঠিক?",
        ["i, ii and iii", "i and ii only", "ii and iii only", "i and iii only"],
        ["i, ii ও iii", "শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii"],
        "A", "easy", "conceptual",
        "|1 − i| = √2, arg = −π/4, and z + z̄ = 2.",
        "তিনটি বিবৃতিই সত্য।",
    ),
    q(
        "The sum of the real and imaginary parts of (1 − i)/(1 + i) is:",
        "(1 − i)/(1 + i) এর বাস্তব ও কাল্পনিক অংশের সমষ্টি কত?",
        ["−1", "0", "1", "2"],
        ["−1", "0", "1", "2"],
        "A", "medium", "numerical",
        "(1 − i)/(1 + i) = −i, so Re + Im = −1.",
        "মান −i; বাস্তব+কাল্পনিক = −1।",
    ),
    q(
        "If z = x + iy, then |z + 1| = |z − 2| represents:",
        "z = x + iy হলে |z + 1| = |z − 2| দ্বারা নির্দেশিত রেখা কোনটি?",
        ["a straight line", "a circle", "a parabola", "an ellipse"],
        ["একটি সরলরেখা", "একটি বৃত্ত", "একটি পরাবৃত্ত", "একটি উপবৃত্ত"],
        "A", "medium", "application",
        "Equidistance from (−1, 0) and (2, 0) gives the line x = 1/2.",
        "(−1,0) ও (2,0) থেকে সমদূর—সরলরেখা x = 1/2।",
    ),
    q(
        "The modulus of −2 + i√5 is:",
        "−2 + i√5 এর মডুলাস কোনটি?",
        ["3", "−2", "√5", "9"],
        ["3", "−2", "√5", "9"],
        "A", "easy", "numerical",
        "|z| = √(4 + 5) = 3.",
        "√(4 + 5) = 3।",
    ),
    q(
        "If z = x + iy, which are true? (i) |z| = |z̄| (ii) z·z̄ = |z|^{2} (iii) arg(z̄) = arg(z) for all z ≠ 0",
        "z = x + iy হলে— (i) |z| = |z̄| (ii) z·z̄ = |z|^{2} (iii) সব z ≠ 0 এর জন্য arg(z̄) = arg(z) — কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "A", "easy", "conceptual",
        "Modulus and product identities hold; generally arg(z̄) = −arg(z).",
        "(i) ও (ii) সত্য; arg(z̄) = −arg(z)।",
    ),
    q(
        "If z₁ = 1 − 2i and z₂ = 3 + i, then |z₁ − z₂| equals:",
        "z₁ = 1 − 2i এবং z₂ = 3 + i হলে |z₁ − z₂| এর মান কত?",
        ["√13", "√5", "5", "√2"],
        ["√13", "√5", "5", "√2"],
        "A", "easy", "numerical",
        "z₁ − z₂ = −2 − 3i; modulus √(4 + 9) = √13.",
        "−2 − 3i এর পরমমান √13।",
    ),
    q(
        "If −i is given, its modulus and argument are:",
        "−i এর মডুলাস ও আর্গুমেন্ট কোনটি?",
        ["1 and −π/2", "1 and π/2", "1 and π", "−1 and −π/2"],
        ["1 এবং −π/2", "1 এবং π/2", "1 এবং π", "−1 এবং −π/2"],
        "A", "easy", "factual",
        "|−i| = 1 and arg(−i) = −π/2.",
        "মডুলাস 1, আর্গুমেন্ট −π/2।",
    ),
    q(
        "If z = 2 − 2i, which are true? (i) Re(z) + Im(z) = 0 (ii) z·z̄ = 8 (iii) polar form is 2√2 (cos(−π/4) + i sin(−π/4))",
        "z = 2 − 2i হলে— (i) Re(z) + Im(z) = 0 (ii) z·z̄ = 8 (iii) পোলার আকার 2√2 (cos(−π/4) + i sin(−π/4)) — কোনটি সঠিক?",
        ["i, ii and iii", "i and ii only", "ii and iii only", "i and iii only"],
        ["i, ii ও iii", "শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii"],
        "A", "medium", "conceptual",
        "2 − 2 = 0; |z|^{2} = 8; r = 2√2 and θ = −π/4.",
        "তিনটি বিবৃতিই সত্য।",
    ),
    q(
        "If z = x + iy with y > 0, then √(z − z̄) equals:",
        "z = x + iy এবং y > 0 হলে √(z − z̄) এর মান কোনটি?",
        ["√y (1 + i)", "√y (1 − i)", "√x (1 + i)", "√x (1 − i)"],
        ["√y (1 + i)", "√y (1 − i)", "√x (1 + i)", "√x (1 − i)"],
        "A", "hard", "numerical",
        "z − z̄ = 2iy and [√y(1 + i)]^{2} = 2iy.",
        "[√y(1+i)]^{2} = 2iy = z − z̄।",
    ),
    q(
        "For conjugates, which are true? (i) z̄̄ = z (ii) |z̄| = |z| (iii) (z₁z₂)̄ = z̄₁ z̄₂",
        "অনুবন্ধী জটিল সংখ্যার ক্ষেত্রে— (i) z̄̄ = z (ii) |z̄| = |z| (iii) (z₁z₂)̄ = z̄₁ z̄₂ — কোনটি সঠিক?",
        ["i, ii and iii", "i and ii only", "ii and iii only", "i and iii only"],
        ["i, ii ও iii", "শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii"],
        "A", "easy", "conceptual",
        "All three are standard conjugate properties.",
        "অনুবন্ধীর তিনটি ধর্মই সত্য।",
    ),
    q(
        "If z = −1 + i√3, which are true? (i) |z| = 2 (ii) principal arg(z) = 2π/3 (iii) z̄ = −1 − i√3",
        "z = −1 + i√3 হলে— (i) |z| = 2 (ii) মুখ্য আর্গুমেন্ট 2π/3 (iii) z̄ = −1 − i√3 — কোনটি সঠিক?",
        ["i, ii and iii", "i and ii only", "ii and iii only", "i and iii only"],
        ["i, ii ও iii", "শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii"],
        "A", "medium", "conceptual",
        "|z| = 2, arg = 2π/3, and conjugate −1 − i√3.",
        "তিনটি বিবৃতিই সত্য।",
    ),
    q(
        "If z = 2x − 3iy and zz̄ = 36, the locus is:",
        "z = 2x − 3iy এবং zz̄ = 36 হলে সঞ্চারপথ একটি—",
        ["ellipse", "circle", "parabola", "hyperbola"],
        ["উপবৃত্ত", "বৃত্ত", "পরাবৃত্ত", "অধিবৃত্ত"],
        "A", "medium", "application",
        "4x^{2} + 9y^{2} = 36 ⇒ x^{2}/9 + y^{2}/4 = 1, an ellipse.",
        "4x^{2} + 9y^{2} = 36 একটি উপবৃত্ত।",
    ),
]


# =============================================================================
# hm2_27_ch03_t03 — Polar form and roots / পোলার রূপ ও মূল
# =============================================================================
T03 = [
    q(
        "A square root of 8 − 6i is:",
        "8 − 6i এর বর্গমূল কোনটি?",
        ["±(3 − i)", "±(1 + 3i)", "±(1 − 3i)", "±(3 + i)"],
        ["±(3 − i)", "±(1 + 3i)", "±(1 − 3i)", "±(3 + i)"],
        "A", "hard", "numerical",
        "(3 − i)^{2} = 9 − 6i + i^{2} = 8 − 6i.",
        "(3 − i)^{2} = 8 − 6i।",
    ),
    q(
        "A value of √(2i) is:",
        "√(2i) এর মান নিচের কোনটি?",
        ["±(1 + i)", "±√2 i", "±√2 (1 − i)", "±√2 (1 + i)"],
        ["±(1 + i)", "±√2 i", "±√2 (1 − i)", "±√2 (1 + i)"],
        "A", "medium", "numerical",
        "(1 + i)^{2} = 1 + 2i − 1 = 2i.",
        "(1 + i)^{2} = 2i।",
    ),
    q(
        "The cube roots of i include the set:",
        "i এর ঘনমূলসমূহের মধ্যে কোন সেটটি সঠিক?",
        [
            "−i, (1/2)(√3 + i), (1/2)(−√3 + i)",
            "i, (1/2)(i + √3), (1/2)(−i − √3)",
            "1, (1/2)(−1 + √3 i), (1/2)(−1 − √3 i)",
            "(1/2)(−i + √3), (1/2)(−i − √3), i",
        ],
        [
            "−i, (1/2)(√3 + i), (1/2)(−√3 + i)",
            "i, (1/2)(i + √3), (1/2)(−i − √3)",
            "1, (1/2)(−1 + √3 i), (1/2)(−1 − √3 i)",
            "(1/2)(−i + √3), (1/2)(−i − √3), i",
        ],
        "A", "hard", "numerical",
        "Cube roots of i are −i, −iω, −iω^{2}, matching −i and (1/2)(±√3 + i).",
        "i এর ঘনমূল −i, −iω, −iω^{2} যা A তে দেওয়া।",
    ),
    q(
        "The sum of the three cube roots of −i is:",
        "−i এর ঘনমূলত্রয়ের সমষ্টি কত?",
        ["0", "−2", "−2i", "2i"],
        ["0", "−2", "−2i", "2i"],
        "A", "medium", "numerical",
        "Roots ρ, ρω, ρω^{2} sum to ρ(1 + ω + ω^{2}) = 0.",
        "মূলত্রয়ের যোগফল ρ(1+ω+ω^{2}) = 0।",
    ),
    q(
        "If z = −1/2 + i(√3/2), which are true? (i) |z| = 1 (ii) principal arg = 2π/3 (iii) polar form e^{i 2π/3}",
        "z = −1/2 + i(√3/2) হলে— (i) মডুলাস 1 (ii) মুখ্য আর্গুমেন্ট 2π/3 (iii) পোলার আকার e^{i 2π/3} — কোনটি সঠিক?",
        ["i, ii and iii", "i and ii only", "ii and iii only", "i and iii only"],
        ["i, ii ও iii", "শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii"],
        "A", "medium", "conceptual",
        "This is cis(2π/3) on the unit circle; all three hold.",
        "একক বৃত্তে cis(2π/3); তিনটিই সত্য।",
    ),
    q(
        "If ω is a complex cube root of unity, then 1/ω + 1/ω^{2} equals:",
        "ω এককের জটিল ঘনমূল হলে 1/ω + 1/ω^{2} এর মান কত?",
        ["−1", "1", "3", "4"],
        ["−1", "1", "3", "4"],
        "A", "easy", "numerical",
        "1/ω + 1/ω^{2} = ω^{2} + ω = −1.",
        "ω^{2} + ω = −1।",
    ),
    q(
        "The general argument of 3 − √3 i (n ∈ Z) is:",
        "3 − √3 i এর সাধারণ আর্গুমেন্ট কোনটি? (n ∈ Z)",
        ["2nπ − π/6", "2nπ − π/3", "2nπ + π/6", "2nπ + π/3"],
        ["2nπ − π/6", "2nπ − π/3", "2nπ + π/6", "2nπ + π/3"],
        "A", "medium", "numerical",
        "Fourth-quadrant arg = −π/6; general form 2nπ − π/6.",
        "আর্গুমেন্ট −π/6; সাধারণ রূপ 2nπ − π/6।",
    ),
    q(
        "If z = (1 − i)^{3}, then arg(z) equals:",
        "z = (1 − i)^{3} হলে arg(z) কত?",
        ["−3π/4", "−π/4", "π/4", "3π/4"],
        ["−3π/4", "−π/4", "π/4", "3π/4"],
        "A", "medium", "numerical",
        "arg(1 − i) = −π/4, so arg(z) = 3(−π/4) = −3π/4.",
        "3 · (−π/4) = −3π/4।",
    ),
    q(
        "A square root of i is:",
        "i এর বর্গমূল কোনটি?",
        ["±(1/√2)(1 + i)", "±(1/√2)(1 − i)", "±(1 + i)", "±(1 − i)"],
        ["±(1/√2)(1 + i)", "±(1/√2)(1 − i)", "±(1 + i)", "±(1 − i)"],
        "A", "medium", "numerical",
        "[(1 + i)/√2]^{2} = i.",
        "[(1+i)/√2]^{2} = i।",
    ),
    q(
        "If √(3 − 4i) = x + iy, which is correct?",
        "√(3 − 4i) = x + iy হলে নিচের কোনটি সঠিক?",
        ["x^{2} + y^{2} = 5", "x^{2} − y^{2} = 5", "x^{2} + y^{2} = 3", "x^{2} − y^{2} = 4"],
        ["x^{2} + y^{2} = 5", "x^{2} − y^{2} = 5", "x^{2} + y^{2} = 3", "x^{2} − y^{2} = 4"],
        "A", "hard", "numerical",
        "From (x + iy)^{2} = 3 − 4i one gets (x^{2} + y^{2})^{2} = 25, so x^{2} + y^{2} = 5.",
        "(x^{2}+y^{2})^{2} = 25 ⇒ x^{2}+y^{2} = 5।",
    ),
    q(
        "If p = (1/2)(−1 + √(−3)), then (p^{2} + p)^{2} equals:",
        "p = (1/2)(−1 + √(−3)) হলে (p^{2} + p)^{2} এর মান কত?",
        ["1", "p", "−1", "p^{2}"],
        ["1", "p", "−1", "p^{2}"],
        "A", "hard", "numerical",
        "p = ω ⇒ p + p^{2} = −1 and (−1)^{2} = 1.",
        "p + p^{2} = −1; বর্গ 1।",
    ),
    q(
        "If p = (1/2)(−1 + √(−3)), then √(p^{2} + p) equals:",
        "p = (1/2)(−1 + √(−3)) হলে √(p^{2} + p) এর মান কত?",
        ["i", "−i", "−1", "1"],
        ["i", "−i", "−1", "1"],
        "A", "hard", "numerical",
        "p^{2} + p = −1; a square root is i.",
        "√(−1) = i।",
    ),
    q(
        "The sum of the three cube roots of 8 is:",
        "8 এর ঘনমূলত্রয়ের যোগফল কত?",
        ["0", "2", "2ω", "2ω^{2}"],
        ["0", "2", "2ω", "2ω^{2}"],
        "A", "easy", "numerical",
        "Roots of x^{3} − 8 = 0 sum to 0 (no x^{2} term).",
        "x^{3} − 8 = 0 এ x^{2} পদ নেই; যোগফল 0।",
    ),
    q(
        "If p and q are imaginary cube roots of unity, then p^{5} + q^{5} equals:",
        "এককের জটিল ঘনমূলদ্বয় p ও q হলে p^{5} + q^{5} এর মান কত?",
        ["−1", "1", "ω", "ω^{2}"],
        ["−1", "1", "ω", "ω^{2}"],
        "A", "medium", "numerical",
        "ω^{5} + (ω^{2})^{5} = ω^{2} + ω^{10} = ω^{2} + ω = −1.",
        "ω^{5} + ω^{10} = ω^{2} + ω = −1।",
    ),
    q(
        "The principal argument of −1 − √3 i is:",
        "−1 − √3 i এর মুখ্য আর্গুমেন্ট কত?",
        ["−2π/3", "−π/3", "2π/3", "π/3"],
        ["−2π/3", "−π/3", "2π/3", "π/3"],
        "A", "medium", "numerical",
        "Third quadrant: −π + π/3 = −2π/3.",
        "−π + π/3 = −2π/3।",
    ),
    q(
        "A square root of −i is:",
        "−i এর বর্গমূল কত?",
        ["±(1/√2)(1 − i)", "±(1/√2)(1 + i)", "±(1 + i)", "±(1 − i)"],
        ["±(1/√2)(1 − i)", "±(1/√2)(1 + i)", "±(1 + i)", "±(1 − i)"],
        "A", "medium", "numerical",
        "[(1 − i)/√2]^{2} = −i.",
        "[(1−i)/√2]^{2} = −i।",
    ),
    q(
        "The polar form of −1 + i is:",
        "−1 + i এর পোলার আকার কোনটি?",
        [
            "√2 (cos(3π/4) + i sin(3π/4))",
            "√2 (cos(π/4) + i sin(π/4))",
            "√2 (cos(π/4) − i sin(π/4))",
            "√2 (cos(3π/4) − i sin(3π/4))",
        ],
        [
            "√2 (cos(3π/4) + i sin(3π/4))",
            "√2 (cos(π/4) + i sin(π/4))",
            "√2 (cos(π/4) − i sin(π/4))",
            "√2 (cos(3π/4) − i sin(3π/4))",
        ],
        "A", "medium", "application",
        "|−1 + i| = √2 and arg = 3π/4.",
        "মডুলাস √2 ও আর্গুমেন্ট 3π/4।",
    ),
    q(
        "For the equation x^{3} = 1, the product of the roots is:",
        "x^{3} = 1 সমীকরণের মূলগুলোর গুণফল কত?",
        ["1", "0", "−1", "1 + i"],
        ["1", "0", "−1", "1 + i"],
        "A", "easy", "numerical",
        "Roots 1, ω, ω^{2} have product ω^{3} = 1.",
        "1 · ω · ω^{2} = 1।",
    ),
    q(
        "For the equation x^{3} = 1, the sum of the roots is:",
        "x^{3} = 1 সমীকরণের মূলগুলোর যোগফল কত?",
        ["0", "1", "ω", "ω^{2}"],
        ["0", "1", "ω", "ω^{2}"],
        "A", "easy", "numerical",
        "1 + ω + ω^{2} = 0.",
        "1 + ω + ω^{2} = 0।",
    ),
    q(
        "If ω is an imaginary cube root of unity, (1 − ω + ω^{2})^{2} + (1 + ω − ω^{2})^{2} equals:",
        "ω এককের কাল্পনিক মূল হলে (1 − ω + ω^{2})^{2} + (1 + ω − ω^{2})^{2} এর মান কত?",
        ["−4", "−3", "3", "4"],
        ["−4", "−3", "3", "4"],
        "A", "hard", "numerical",
        "Expressions simplify to −2ω and −2ω^{2}; sum of squares = 4(ω + ω^{2}) = −4.",
        "4(ω + ω^{2}) = −4।",
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
    counts["hm2_27_ch03_t01"] = write_topic("hm2_27_ch03_t01", T01)["count"]
    counts["hm2_27_ch03_t02"] = write_topic("hm2_27_ch03_t02", T02)["count"]
    counts["hm2_27_ch03_t03"] = write_topic("hm2_27_ch03_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm2_27_ch03",
        "title_en": "Complex Numbers",
        "title_bn": "জটিল সংখ্যা",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(63, 72)],
        "topics": {
            "hm2_27_ch03_t01": {
                "title_en": "Complex number operations",
                "title_bn": "জটিল সংখ্যার ক্রিয়া",
                "udvash_types": [
                    "powers of i and algebraic products",
                    "cube roots of unity (ω)",
                    "zz̄ and arithmetic of z₁, z₂",
                    "real/imaginary parts and quadrants",
                ],
                "count": 20,
            },
            "hm2_27_ch03_t02": {
                "title_en": "Modulus, argument and conjugate",
                "title_bn": "পরমমান, আর্গুমেন্ট ও অনুবন্ধী",
                "udvash_types": [
                    "modulus and principal argument",
                    "conjugate identities",
                    "loci |z−a|=r and |z−a|=|z−b|",
                    "arg and Re/Im properties",
                ],
                "count": 20,
            },
            "hm2_27_ch03_t03": {
                "title_en": "Polar form and roots",
                "title_bn": "পোলার রূপ ও মূল",
                "udvash_types": [
                    "square and cube roots of complex numbers",
                    "polar / cis form",
                    "general argument",
                    "roots of unity sums and products",
                ],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "garbled_stems": "Noisy OCR reconstructed from answer-key algebra and standard board forms",
            "figure_loci": "Locus items kept as text inequalities without diagrams",
            "stimulus_pairs": "Linked stimulus blocks curated as standalone clear stems",
            "ambiguous_option_glyphs": "Broken Bangla/option glyphs replaced with closed-form HSC standards",
        },
        "low_confidence": [
            "OCR on pp. 63–71 noisy; column text and solution lines used to reconstruct stems.",
            "Inline math stored as plain text (√, π, ω, arg) for JSONL.",
            "Some printed multi-select glyph keys incomplete; properties rewritten clearly.",
            "A few cube-root option listings standardized to closed algebraic forms.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm2_ch03.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
        "math2_progress": {
            "topics_complete": "9/30",
            "note": "Ch03 continues higher_mathematics 2nd paper after Ch01–Ch02 (120Q)",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch03_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
