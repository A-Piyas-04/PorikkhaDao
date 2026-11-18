#!/usr/bin/env python3
"""Seed Physics 1st Paper Ch2 (Vectors) bilingual MCQs.

Curated from Udvash HSC Question Bank 2026 printed pages 55–65 (OCR + HSC reconstruction).
Writes exactly 20 JSONL rows per topic under content/bank/topics/.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPICS = ROOT / "content" / "bank" / "topics"
SOURCE = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "physics p1 ch02; curated bilingual"
)


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    if not re.search(r"[A-Za-z]", en):
        en = f"value {en}"
    if not re.search(r"[ঀ-৿]", bn):
        bn = f"মান {bn}"
    return en, bn


def q(stem_en, stem_bn, opts_en, opts_bn, correct, difficulty, qtype, exp_en, exp_bn):
    pairs = [_norm_pair(e, b) for e, b in zip(opts_en, opts_bn)]
    (a, ab), (b, bb), (c, cb), (d, db) = pairs
    if not re.search(r"[ঀ-৿]", exp_bn):
        exp_bn = "ব্যাখ্যা: " + exp_bn
    return {
        "stem_en": stem_en,
        "stem_bn": stem_bn,
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
        "explanation_en": exp_en,
        "explanation_bn": exp_bn,
        "source": SOURCE,
        "verified": False,
    }


# ---------------------------------------------------------------------------
# t01 Scalars and vectors
# ---------------------------------------------------------------------------
T01 = [
    q(
        "Which of the following is NOT a vector quantity?",
        "নিচের কোনটি ভেক্টর রাশি নয়?",
        ["Angular momentum", "Torque", "Work", "Force"],
        ["কৌণিক ভরবেগ", "টর্ক", "কাজ", "বল"],
        "C", "easy", "factual",
        "Work is a scalar; force, torque, and angular momentum are vectors.",
        "কাজ স্কেলার রাশি; বল, টর্ক ও কৌণিক ভরবেগ ভেক্টর।",
    ),
    q(
        "Among these HSC physics quantities, which one is a vector?",
        "নিচের এইচএসসি পদার্থবিজ্ঞানের রাশিগুলোর মধ্যে কোনটি ভেক্টর?",
        ["Mass", "Volume", "Temperature", "Torque"],
        ["ভর", "আয়তন", "তাপমাত্রা", "টর্ক"],
        "D", "easy", "factual",
        "Torque has both magnitude and direction.",
        "টর্কের মান ও দিক উভয়ই আছে।",
    ),
    q(
        "Which product among the following is a scalar?",
        "নিচের কোন গুণফলটি স্কেলার রাশি?",
        ["A · B", "A × B", "(A × B) × A", "(A × B) × B"],
        ["A · B", "A × B", "(A × B) × A", "(A × B) × B"],
        "A", "medium", "conceptual",
        "The dot product A · B is a scalar; the others are vectors.",
        "ডট গুণন A · B স্কেলার; বাকিগুলো ভেক্টর।",
    ),
    q(
        "Vectors that share the same initial (tail) point are called:",
        "যেসব ভেক্টরের পাদবিন্দু অভিন্ন, তাদের কী বলে?",
        ["Position vectors", "Unit vectors", "Collinear vectors", "Coplanar vectors"],
        ["অবস্থান ভেক্টর", "একক ভেক্টর", "সমরেখ ভেক্টর", "সমতলীয় ভেক্টর"],
        "A", "easy", "factual",
        "Position vectors are drawn from a common origin.",
        "অভিন্ন উৎসবিন্দু থেকে টানা ভেক্টরকে অবস্থান ভেক্টর বলে।",
    ),
    q(
        "If the tip and the tail of a vector coincide, the vector is a:",
        "কোনো ভেক্টরের শীর্ষবিন্দু ও পাদবিন্দু একই হলে তাকে কী বলে?",
        ["Free vector", "Unit vector", "Null (zero) vector", "Equal vector"],
        ["স্বাধীন ভেক্টর", "একক ভেক্টর", "নাল (শূন্য) ভেক্টর", "সমান ভেক্টর"],
        "C", "easy", "factual",
        "Tip = tail means magnitude zero → null vector.",
        "শীর্ষ ও পাদ একই হলে মান শূন্য → নাল ভেক্টর।",
    ),
    q(
        "Which quantity does NOT have a definite direction?",
        "নিচের কোনটির দিক নির্দিষ্ট নয়?",
        ["Equal vectors", "Collinear vectors", "Opposite vectors", "Zero (null) vector"],
        ["সমান ভেক্টর", "সমরেখ ভেক্টর", "বিপরীত ভেক্টর", "শূন্য (নাল) ভেক্টর"],
        "D", "easy", "conceptual",
        "A null vector has no unique direction.",
        "শূন্য ভেক্টরের সুনির্দিষ্ট দিক নেই।",
    ),
    q(
        "About the null vector: (i) no definite direction (ii) tip and tail coincide (iii) always has nonzero acceleration. Which is correct?",
        "শূন্য ভেক্টর সম্পর্কে: (i) সুনির্দিষ্ট দিক নেই (ii) আদি ও শেষ বিন্দু একই (iii) সবসময় অশূন্য ত্বরণ থাকে। কোনটি সঠিক?",
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        "A", "medium", "conceptual",
        "Null vector: no unique direction; tip = tail. Acceleration claim is unrelated.",
        "নাল ভেক্টরের দিক অনির্দিষ্ট এবং আদি-শেষ একই; ত্বরণের দাবি অপ্রাসঙ্গিক।",
    ),
    q(
        "Homogeneous vectors of unequal magnitude and opposite sense are called:",
        "সমজাতীয় অসমমানের এবং বিপরীতমুখী ভেক্টরকে কী বলে?",
        ["Equal vectors", "Opposite vectors", "Unlike (dissimilar) vectors", "Like (similar) vectors"],
        ["সমান ভেক্টর", "বিপরীত ভেক্টর", "বিসদৃশ ভেক্টর", "সদৃশ ভেক্টর"],
        "C", "medium", "factual",
        "Unlike vectors: same kind, opposite directions; magnitudes may differ. Opposite vectors are equal in magnitude and opposite.",
        "বিসদৃশ: সমজাতীয়, বিপরীতমুখী, মান অসম হতে পারে।",
    ),
    q(
        "Equal vectors must satisfy: (i) same kind (ii) equal magnitudes (iii) same direction. Which is correct?",
        "সমান ভেক্টরের বৈশিষ্ট্য: (i) সমজাতীয় রাশি (ii) মান সমান (iii) দিক একই। কোনটি সঠিক?",
        ["i, ii", "ii, iii", "i, iii", "i, ii, iii"],
        ["i, ii", "ii, iii", "i, iii", "i, ii, iii"],
        "D", "easy", "factual",
        "Equal vectors are same type, equal magnitude, and same direction.",
        "সমান ভেক্টর সমজাতীয়, সমান মান ও একই দিকবিশিষ্ট।",
    ),
    q(
        "If A · B = 0 and |A × B| = 0, then A and B are:",
        "যদি A · B = 0 এবং |A × B| = 0 হয়, তবে A ও B:",
        ["Opposite vectors", "Unlike vectors", "Equal vectors", "At least one is a null vector"],
        ["বিপরীত ভেক্টর", "বিসদৃশ ভেক্টর", "সমান ভেক্টর", "অন্তত একটি নাল ভেক্টর"],
        "D", "hard", "conceptual",
        "Dot zero ⇒ perpendicular (or null); cross zero ⇒ parallel (or null). Both hold only if at least one is null.",
        "উভয় শর্ত একসাথে সত্য কেবল নাল ভেক্টর থাকলে।",
    ),
    q(
        "A physical quantity that needs both magnitude and direction is a:",
        "যে ভৌত রাশি সম্পূর্ণরূপে প্রকাশ করতে মান ও দিক উভয়ই লাগে, তাকে কী বলে?",
        ["Scalar", "Vector", "Tensor only", "Dimensionless number"],
        ["স্কেলার", "ভেক্টর", "কেবল টেনসর", "মাত্রাহীন সংখ্যা"],
        "B", "easy", "factual",
        "Vectors require magnitude and direction.",
        "ভেক্টর রাশির জন্য মান ও দিক উভয়ই প্রয়োজন।",
    ),
    q(
        "Which of the following is NOT a vector (in the usual HSC classification)?",
        "নিচের কোনটি সাধারণত ভেক্টর রাশি নয়?",
        ["Gradient of a scalar", "Curl of a vector", "Divergence of a vector", "Cross product of two vectors"],
        ["স্কেলারের গ্রেডিয়েন্ট", "ভেক্টরের কার্ল", "ভেক্টরের ডাইভারজেন্স", "দুই ভেক্টরের ক্রস গুণন"],
        "C", "medium", "conceptual",
        "Divergence ∇ · V is a scalar; gradient and curl produce vectors.",
        "ডাইভারজেন্স স্কেলার; গ্রেডিয়েন্ট ও কার্ল ভেক্টর দেয়।",
    ),
    q(
        "If ∇ × A = 0: (i) A is irrotational (ii) A is conservative (usual conditions) (iii) A is solenoidal. Which is correct?",
        "যদি ∇ × A = 0 হয়: (i) A অঘূর্ণনশীল (ii) সাধারণ শর্তে A সংরক্ষণশীল (iii) A সলিনয়ডাল। কোনটি সঠিক?",
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        "A", "hard", "conceptual",
        "Curl zero ⇒ irrotational/conservative. Solenoidal means div A = 0.",
        "কার্ল শূন্য ⇒ অঘূর্ণনশীল/সংরক্ষণশীল; সলিনয়ডাল মানে div A = 0।",
    ),
    q(
        "If ∇ · A = 0: (i) field is solenoidal (ii) fluid interpretation is incompressible (iii) net flux through a closed surface is zero. Which is correct?",
        "যদি ∇ · A = 0 হয়: (i) ক্ষেত্র সলিনয়ডাল (ii) প্রবাহী অপ্রসারণশীল (iii) বদ্ধ পৃষ্ঠে নীট ফ্লাক্স শূন্য। কোনটি সঠিক?",
        ["i, ii", "ii, iii", "i, iii", "i, ii, iii"],
        ["i, ii", "ii, iii", "i, iii", "i, ii, iii"],
        "D", "hard", "conceptual",
        "Zero divergence implies all three listed consequences.",
        "ডাইভারজেন্স শূন্য ⇒ সলিনয়ডাল, অপ্রসারণশীল ও নীট ফ্লাক্স শূন্য।",
    ),
    q(
        "div (∇ × A) equals:",
        "div (∇ × A) এর মান:",
        ["3", "2", "1", "0"],
        ["৩", "২", "১", "০"],
        "D", "medium", "factual",
        "Divergence of any curl is identically zero.",
        "যেকোনো কার্লের ডাইভারজেন্স সর্বদা শূন্য।",
    ),
    q(
        "A vector of magnitude 1 is called a:",
        "মান ১ এমন ভেক্টরকে কী বলে?",
        ["Null vector", "Unit vector", "Position vector", "Equal vector"],
        ["নাল ভেক্টর", "একক ভেক্টর", "অবস্থান ভেক্টর", "সমান ভেক্টর"],
        "B", "easy", "factual",
        "A unit vector has magnitude 1 by definition.",
        "একক ভেক্টরের মান সংজ্ঞা অনুসারে ১।",
    ),
    q(
        "For A = i + j: (i) |A| = 1 so it is a unit vector (ii) it is a valid vector (iii) it is the position vector to (1,1). Which is correct?",
        "A = i + j এর ক্ষেত্রে: (i) |A| = 1 বলে একক ভেক্টর (ii) সঠিক ভেক্টর প্রকাশ (iii) (1,1)-এর অবস্থান ভেক্টর। কোনটি সঠিক?",
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        "C", "medium", "conceptual",
        "|A| = √2 ≠ 1, so not a unit vector; still a valid position vector to (1,1).",
        "|A| = √2 ≠ 1, তাই একক নয়; তবে সঠিক অবস্থান ভেক্টর।",
    ),
    q(
        "The change of position of a body in a specified direction is a:",
        "একটি বস্তুর নির্দিষ্ট দিকে অবস্থান পরিবর্তনকে কী বলে?",
        ["Position vector", "Displacement vector", "Unit vector", "Force vector"],
        ["অবস্থান ভেক্টর", "সরণ ভেক্টর", "একক ভেক্টর", "বল ভেক্টর"],
        "B", "easy", "factual",
        "Displacement is the directed change in position.",
        "নির্দিষ্ট দিকে অবস্থান পরিবর্তনকে সরণ ভেক্টর বলে।",
    ),
    q(
        "If φ(x, y, z) is a differentiable scalar field, ∇φ is called the:",
        "φ(x, y, z) একটি ব্যবকলনীয় স্কেলার ক্ষেত্র হলে ∇φ-কে কী বলে?",
        ["Operator only", "Curl", "Gradient", "Divergence"],
        ["কেবল অপারেটর", "কার্ল", "গ্রেডিয়েন্ট", "ডাইভারজেন্স"],
        "C", "easy", "factual",
        "∇φ is the gradient of the scalar field.",
        "∇φ স্কেলার ক্ষেত্রের গ্রেডিয়েন্ট।",
    ),
    q(
        "A vector field is obtained from a scalar field via the:",
        "স্কেলার ক্ষেত্র থেকে ভেক্টর ক্ষেত্র পাওয়া যায় কোনটির মাধ্যমে?",
        ["Gradient", "Divergence", "Curl", "Scalar triple product"],
        ["গ্রেডিয়েন্ট", "ডাইভারজেন্স", "কার্ল", "স্কেলার ত্রিগুণন"],
        "A", "medium", "conceptual",
        "Gradient maps a scalar field to a vector field.",
        "গ্রেডিয়েন্ট স্কেলার ক্ষেত্রকে ভেক্টর ক্ষেত্রে রূপান্তর করে।",
    ),
]


# ---------------------------------------------------------------------------
# t02 Vector addition and resolution
# ---------------------------------------------------------------------------
T02 = [
    q(
        "How many geometric laws are commonly used for adding vectors?",
        "জ্যামিতিক পদ্ধতিতে ভেক্টর রাশির যোগের সূত্রসংখ্যা সাধারণত কতটি?",
        ["4", "8", "3", "2"],
        ["৪", "৮", "৩", "২"],
        "D", "easy", "factual",
        "Triangle law and parallelogram law are the two standard geometric addition laws.",
        "ত্রিভুজ সূত্র ও সামান্তরিক সূত্র—এই দুটি জ্যামিতিক যোগসূত্র প্রচলিত।",
    ),
    q(
        "Which is the distributive law for vectors (scalar m)?",
        "নিচের কোনটি ভেক্টরের বণ্টন সূত্র (স্কেলার m সহ)?",
        ["P + Q = Q + P", "(P + Q) + R = P + (Q + R)", "m(P + Q) = mP + mQ", "P − Q = P + (−Q)"],
        ["P + Q = Q + P", "(P + Q) + R = P + (Q + R)", "m(P + Q) = mP + mQ", "P − Q = P + (−Q)"],
        "C", "easy", "factual",
        "Distributive law: m(P + Q) = mP + mQ.",
        "বণ্টন সূত্র: m(P + Q) = mP + mQ।",
    ),
    q(
        "The commutative law is obeyed by: (i) vector addition (ii) dot product (iii) cross product. Which is correct?",
        "বিনিময় সূত্র মেনে চলে: (i) দুটি ভেক্টরের যোগ (ii) ডট গুণন (iii) ক্রস গুণন। কোনটি সঠিক?",
        ["i, ii", "ii, iii", "i, iii", "i, ii, iii"],
        ["i, ii", "ii, iii", "i, iii", "i, ii, iii"],
        "A", "medium", "conceptual",
        "Addition and dot product commute; cross product is anticommutative.",
        "যোগ ও ডট বিনিময়যোগ্য; ক্রস গুণন নয়।",
    ),
    q(
        "If |A + B| = |A − B|, the angle between A and B is:",
        "যদি |A + B| = |A − B| হয়, তবে মধ্যবর্তী কোণ:",
        ["0°", "30°", "90°", "180°"],
        ["০°", "৩০°", "৯০°", "১৮০°"],
        "C", "medium", "numerical",
        "Squaring both sides gives A · B = 0 ⇒ θ = 90°.",
        "উভয় পক্ষ বর্গ করে A · B = 0 ⇒ θ = ৯০°।",
    ),
    q(
        "If R = A + B and |R| = |A| + |B|, then A and B are:",
        "R = A + B এবং |R| = |A| + |B| হলে A ও B:",
        ["Unequal and opposite", "Parallel and like-directed", "Equal and opposite", "Perpendicular"],
        ["অসমান ও বিপরীতমুখী", "সমান্তরাল ও সমমুখী", "সমান ও বিপরীতমুখী", "পরস্পর লম্ব"],
        "B", "medium", "conceptual",
        "Maximum resultant |A| + |B| when vectors are parallel and same sense.",
        "লব্ধির সর্বোচ্চ মান সমমুখী সমান্তরাল ভেক্টরে হয়।",
    ),
    q(
        "Three vectors P, Q, R lie in one plane if:",
        "তিনটি ভেক্টর P, Q, R একই তলে অবস্থান করবে যদি:",
        ["P · (Q × R) = 0", "P · (Q × R) = 1", "P · (Q − R) = 0", "P × (Q × R) = 0"],
        ["P · (Q × R) = 0", "P · (Q × R) = 1", "P · (Q − R) = 0", "P × (Q × R) = 0"],
        "A", "medium", "conceptual",
        "Scalar triple product zero ⇔ coplanar.",
        "স্কেলার ত্রিগুণন শূন্য ⇔ সমতলীয়।",
    ),
    q(
        "Three vectors are coplanar if: (i) A · (B × C) = 0 (ii) B · (C × A) = 0 (iii) C · (A × B) = 0. Which is correct?",
        "তিনটি ভেক্টর সমতলীয় হবে যদি: (i) A · (B × C) = 0 (ii) B · (C × A) = 0 (iii) C · (A × B) = 0। কোনটি সঠিক?",
        ["i only", "i, ii", "ii, iii", "i, ii, iii"],
        ["কেবল i", "i, ii", "ii, iii", "i, ii, iii"],
        "D", "medium", "conceptual",
        "The cyclic scalar triple products are equal; any being zero means all are zero.",
        "চক্রীয় স্কেলার ত্রিগুণন সমান; যেকোনোটি শূন্য ⇒ সমতলীয়।",
    ),
    q(
        "A = 2i + 2j − k and B = 6i − 3j + 2k. Magnitude of the projection of B on A is approximately:",
        "A = 2i + 2j − k এবং B = 6i − 3j + 2k হলে A-এর উপর B-এর অভিক্ষেপের মান প্রায়:",
        ["3.33", "2.33", "1.33", "0.33"],
        ["৩.৩৩", "২.৩৩", "১.৩৩", "০.৩৩"],
        "C", "hard", "numerical",
        "A · B = 4; |A| = 3; projection = 4/3 ≈ 1.33.",
        "A · B = ৪, |A| = ৩ ⇒ অভিক্ষেপ = ৪/৩ ≈ ১.৩৩।",
    ),
    q(
        "Points A(3, 2, 2) and B(3, 2, −1). Magnitude of AB is:",
        "A(3, 2, 2) ও B(3, 2, −1) সংযোগকারী AB ভেক্টরের মান:",
        ["1", "√3", "3", "4"],
        ["১", "√৩", "৩", "৪"],
        "C", "easy", "numerical",
        "AB = −3k ⇒ |AB| = 3.",
        "AB = −3k ⇒ |AB| = ৩।",
    ),
    q(
        "For what n are A = 2i + n j − 5k and B = 10i − 5j − 25k parallel?",
        "n-এর কোন মানে A = 2i + n j − 5k এবং B = 10i − 5j − 25k সমান্তরাল?",
        ["1", "−1", "5", "−5"],
        ["১", "−১", "৫", "−৫"],
        "B", "medium", "numerical",
        "A = λB ⇒ λ = 1/5 ⇒ n = −5λ = −1.",
        "λ = ১/৫ ⇒ n = −১।",
    ),
    q(
        "Angle between i + j and i − j is:",
        "i + j এবং i − j-এর মধ্যবর্তী কোণ:",
        ["60°", "90°", "120°", "180°"],
        ["৬০°", "৯০°", "১২০°", "১৮০°"],
        "B", "easy", "numerical",
        "(i+j)·(i−j) = 0 ⇒ 90°.",
        "ডট গুণন শূন্য ⇒ কোণ ৯০°।",
    ),
    q(
        "For r = x i + y j: (i) x is horizontal component (ii) y is vertical component (iii) |r| = x² + y². Which is correct?",
        "r = x i + y j এর ক্ষেত্রে: (i) x অনুভূমিক উপাংশ (ii) y উল্লম্ব উপাংশ (iii) |r| = x² + y²। কোনটি সঠিক?",
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        "A", "easy", "conceptual",
        "|r| = √(x² + y²), not x² + y².",
        "|r| = √(x² + y²); (iii) ভুল।",
    ),
    q(
        "A vector makes 30° with the x-axis; x-component is 3 units. y-component is:",
        "একটি ভেক্টর x-অক্ষের সাথে ৩০° কোণে; x-উপাংশ ৩ একক হলে y-উপাংশ:",
        ["√3 units", "3 units", "3√3 units", "6 units"],
        ["√৩ একক", "৩ একক", "৩√৩ একক", "৬ একক"],
        "A", "medium", "numerical",
        "A cos 30° = 3 ⇒ A = 2√3; A_y = A sin 30° = √3.",
        "A cos 30° = ৩ ⇒ A_y = √৩।",
    ),
    q(
        "Components of A along OX and OY are 5√3 and 5. |A| equals:",
        "A-এর OX ও OY উপাংশ যথাক্রমে 5√3 ও 5। |A| কত?",
        ["10√3", "10", "5√3", "5"],
        ["১০√৩", "১০", "৫√৩", "৫"],
        "B", "easy", "numerical",
        "|A| = √(75 + 25) = 10.",
        "|A| = √(৭৫+২৫) = ১০।",
    ),
    q(
        "Which vector is parallel to A = i + j?",
        "নিচের কোনটি A = i + j-এর সমান্তরাল?",
        ["i + 2j", "j + k", "3i + 3j", "i − j"],
        ["i + 2j", "j + k", "3i + 3j", "i − j"],
        "C", "easy", "conceptual",
        "3i + 3j = 3(i + j).",
        "3(i + j) A-এর স্কেলার গুণিতক।",
    ),
    q(
        "To cross a flowing river in minimum time, a swimmer should start at what angle to the current (along the bank)?",
        "স্রোতযুক্ত নদীতে সর্বনিম্ন সময়ে ওপারে যেতে সাঁতারুকে স্রোতের সাথে কত কোণে যাত্রা শুরু করতে হবে?",
        ["45°", "60°", "90°", "120°"],
        ["৪৫°", "৬০°", "৯০°", "১২০°"],
        "C", "medium", "application",
        "Minimum time: swim perpendicular to the banks (90° to the current).",
        "ন্যূনতম সময়: তীরের লম্ব বরাবর (স্রোতের সাথে ৯০°)।",
    ),
    q(
        "Boat speed in still water 20 km/h; current 12 km/h; width 4 km. Minimum time to cross is:",
        "নৌকার বেগ ২০ km/h, স্রোত ১২ km/h, প্রস্থ ৪ km। ন্যূনতম সময়ে পার হতে কত সময়?",
        ["0.1 h", "0.2 h", "0.25 h", "0.33 h"],
        ["০.১ ঘণ্টা", "০.২ ঘণ্টা", "০.২৫ ঘণ্টা", "০.৩৩ ঘণ্টা"],
        "B", "hard", "numerical",
        "t = width / v_boat = 4/20 = 0.2 h (heading ⊥ to current).",
        "t = ৪/২০ = ০.২ ঘণ্টা।",
    ),
    q(
        "Current P = 9 km/h. To cancel the current, Q sin 30° = 9. The boat speed Q is:",
        "স্রোত P = ৯ km/h। স্রোত নাকচ করতে Q sin 30° = ৯ হলে নৌকার বেগ Q:",
        ["9 km/h", "18 km/h", "27 km/h", "36 km/h"],
        ["৯ km/h", "১৮ km/h", "২৭ km/h", "৩৬ km/h"],
        "B", "hard", "numerical",
        "Q × (1/2) = 9 ⇒ Q = 18 km/h.",
        "Q = ১৮ km/h।",
    ),
    q(
        "Two equal forces each of magnitude P act at right angles. Resultant magnitude is:",
        "এক বিন্দুতে লম্বভাবে ক্রিয়াশীল দুটি সমান বল P-এর লব্ধির মান:",
        ["0", "P", "√2 P", "2P"],
        ["০", "P", "√২ P", "২P"],
        "C", "easy", "numerical",
        "R = √(P² + P²) = P√2.",
        "R = P√২।",
    ),
    q(
        "If P and Q act at 120° and |P| = |Q|, magnitude of the resultant is:",
        "P ও Q ১২০° কোণে ক্রিয়া করে এবং |P| = |Q| হলে লব্ধির মান:",
        ["P + Q", "√(P² + Q² + PQ)", "P − Q", "√(P² + Q² − PQ)"],
        ["P + Q", "√(P² + Q² + PQ)", "P − Q", "√(P² + Q² − PQ)"],
        "D", "medium", "numerical",
        "|P+Q|² = P²+Q²+2PQ(−1/2) = P²+Q²−PQ.",
        "cos 120° = −১/২ ⇒ |R| = √(P²+Q²−PQ)।",
    ),
]


# ---------------------------------------------------------------------------
# t03 Scalar and vector products
# ---------------------------------------------------------------------------
T03 = [
    q(
        "About the cross product: (i) obeys commutative law (ii) follows right-hand screw rule (iii) A × B = −(B × A). Which is correct?",
        "ক্রস গুণন সম্পর্কে: (i) বিনিময় সূত্র মেনে চলে (ii) ডানহাতি স্ক্রু নিয়ম অনুসরণ করে (iii) A × B = −(B × A)। কোনটি সঠিক?",
        ["ii only", "i, iii", "ii, iii", "i, ii, iii"],
        ["কেবল ii", "i, iii", "ii, iii", "i, ii, iii"],
        "C", "medium", "conceptual",
        "Cross product is anticommutative and right-hand directed; not commutative.",
        "ক্রস গুণন অ্যান্টিবিনিময় ও ডানহাতি নিয়ম মেনে চলে।",
    ),
    q(
        "If |A × B| = A · B, the angle between A and B is:",
        "যদি |A × B| = A · B হয়, তবে মধ্যবর্তী কোণ:",
        ["2π", "π", "π/2", "π/4"],
        ["২π", "π", "π/২", "π/৪"],
        "D", "medium", "numerical",
        "tan θ = 1 ⇒ θ = π/4 (acute).",
        "tan θ = ১ ⇒ θ = π/৪।",
    ),
    q(
        "If |A| = 2, |B| = 4 and A · B = 4, the angle between them is:",
        "|A| = ২, |B| = ৪ এবং A · B = ৪ হলে মধ্যবর্তী কোণ:",
        ["30°", "60°", "90°", "120°"],
        ["৩০°", "৬০°", "৯০°", "১২০°"],
        "B", "medium", "numerical",
        "cos θ = 4/(2×4) = 1/2 ⇒ θ = 60°.",
        "cos θ = ১/২ ⇒ θ = ৬০°।",
    ),
    q(
        "If A = −5j, the direction of A is along:",
        "A = −5j হলে A-এর দিক কোন অক্ষ বরাবর?",
        ["+x-axis", "+y-axis", "−x-axis", "−y-axis"],
        ["+x-অক্ষ", "+y-অক্ষ", "−x-অক্ষ", "−y-অক্ষ"],
        "D", "easy", "factual",
        "−5j points along the negative y-axis.",
        "−5j ঋণাত্মক y-অক্ষ বরাবর।",
    ),
    q(
        "Area of the parallelogram with adjacent sides A and B is:",
        "A ও B পাশাপাশি বাহু হলে সামান্তরিকের ক্ষেত্রফল:",
        ["A · B", "−|A × B|", "(1/2)|A × B|", "|A × B|"],
        ["A · B", "−|A × B|", "(১/২)|A × B|", "|A × B|"],
        "D", "easy", "factual",
        "Parallelogram area = |A × B|.",
        "সামান্তরিকের ক্ষেত্রফল = |A × B|।",
    ),
    q(
        "If A · B = 18 and |A × B| = 6√3, the angle between A and B is:",
        "A · B = ১৮ এবং |A × B| = ৬√৩ হলে মধ্যবর্তী কোণ:",
        ["120°", "90°", "60°", "30°"],
        ["১২০°", "৯০°", "৬০°", "৩০°"],
        "D", "hard", "numerical",
        "tan θ = 6√3/18 = 1/√3 ⇒ θ = 30°.",
        "tan θ = ১/√৩ ⇒ θ = ৩০°।",
    ),
    q(
        "For F = 3x i − 2y j + 4z k, div F equals:",
        "F = 3x i − 2y j + 4z k হলে div F = ?",
        ["3", "5", "9", "12"],
        ["৩", "৫", "৯", "১২"],
        "B", "medium", "numerical",
        "div F = 3 − 2 + 4 = 5.",
        "div F = ৩ − ২ + ৪ = ৫।",
    ),
    q(
        "If V = x² i − 2z j + y k, then div V =:",
        "V = x² i − 2z j + y k হলে div V =:",
        ["2x", "3i", "2x i", "x i"],
        ["২x", "৩i", "২x i", "x i"],
        "A", "medium", "numerical",
        "div V = 2x + 0 + 0 = 2x.",
        "div V = ২x।",
    ),
    q(
        "Which expression denotes the curl of vector field V?",
        "নিচের কোনটি ভেক্টর ক্ষেত্র V-এর কার্ল নির্দেশ করে?",
        ["∇V", "∇ · V", "∇ × V", "V · ∇"],
        ["∇V", "∇ · V", "∇ × V", "V · ∇"],
        "C", "easy", "factual",
        "Curl is ∇ × V.",
        "কার্ল = ∇ × V।",
    ),
    q(
        "A unit vector perpendicular to the plane of i and j is:",
        "i ও j যে তলে আছে সে তলের উপর লম্ব একক ভেক্টর:",
        ["±(i × j)", "±(j × k)", "±(k × i)", "±(i × k)"],
        ["±(i × j)", "±(j × k)", "±(k × i)", "±(i × k)"],
        "A", "easy", "factual",
        "i × j = k, so ±(i × j) is normal to the xy-plane.",
        "i × j = k ⇒ ±(i × j) xy-তলের লম্ব।",
    ),
    q(
        "Which of the following is parallel to the z-axis?",
        "নিচের কোনটি z-অক্ষের সমান্তরাল?",
        ["(i × j) × i", "(j × k) × j", "i × j", "(k × i) × k"],
        ["(i × j) × i", "(j × k) × j", "i × j", "(k × i) × k"],
        "C", "medium", "numerical",
        "i × j = k, which is along the z-axis.",
        "i × j = k ⇒ z-অক্ষের সমান্তরাল।",
    ),
    q(
        "If |A × B| = AB sin θ and |A| = |B| = 3, then |A × B| equals:",
        "|A| = |B| = ৩ হলে |A × B| = ?",
        ["9 cos θ", "9 sin θ", "3 sin θ", "6 cos θ"],
        ["৯ cos θ", "৯ sin θ", "৩ sin θ", "৬ cos θ"],
        "B", "easy", "numerical",
        "|A × B| = 3 × 3 × sin θ = 9 sin θ.",
        "|A × B| = ৯ sin θ।",
    ),
    q(
        "Relative to a car of velocity V_c, a motorcycle of velocity V_m in the same direction has relative velocity:",
        "একই দিকে গতিশীল গাড়ি V_c ও মোটরসাইকেল V_m হলে গাড়ির সাপেক্ষে মোটরসাইকেলের আপেক্ষিক বেগ:",
        ["V_c − V_m", "V_m − V_c", "V_c + V_m", "V_c × V_m"],
        ["V_c − V_m", "V_m − V_c", "V_c + V_m", "V_c × V_m"],
        "B", "easy", "application",
        "v_rel = v_m − v_c for relative velocity of motorcycle w.r.t. car.",
        "আপেক্ষিক বেগ = V_m − V_c।",
    ),
    q(
        "The projection of A on B is:",
        "B-এর উপর A-এর অভিক্ষেপ:",
        ["A sin θ", "A cos θ", "B sin θ", "A · B only as a vector"],
        ["A sin θ", "A cos θ", "B sin θ", "কেবল ভেক্টর হিসেবে A · B"],
        "B", "easy", "factual",
        "Scalar projection of A on B is A cos θ = (A · B)/|B|.",
        "অভিক্ষেপ = A cos θ।",
    ),
    q(
        "If A = i + j, B = k, C = i − j, then: (i) A and C are collinear (ii) B is perpendicular to both A and C (iii) A, B, C are coplanar. Which is correct?",
        "A = i + j, B = k, C = i − j হলে: (i) A ও C সমরেখ (ii) B, A ও C উভয়ের লম্ব (iii) A, B, C সমতলীয়। কোনটি সঠিক?",
        ["i, ii", "ii only", "ii, iii", "i, ii, iii"],
        ["i, ii", "কেবল ii", "ii, iii", "i, ii, iii"],
        "B", "hard", "conceptual",
        "A · C = 0 so A ⊥ C (not collinear). B = k is ⊥ A and ⊥ C. A · (B × C) ≠ 0, so not coplanar. Only (ii).",
        "কেবল (ii) সঠিক: B উভয়ের লম্ব; A ও C লম্ব কিন্তু সমরেখ নয় এবং ত্রিগুণন অশূন্য।",
    ),
    q(
        "Two forces of 3 N and 4 N act at right angles. |F1 × F2| equals:",
        "৩ N ও ৪ N দুটি বল পরস্পর লম্বভাবে ক্রিয়া করলে |F1 × F2|-এর মান:",
        ["0", "5", "7", "12"],
        ["০", "৫", "৭", "১২"],
        "D", "medium", "numerical",
        "|F1 × F2| = 3 × 4 × sin 90° = 12.",
        "|F1 × F2| = ৩×৪×১ = ১২।",
    ),
    q(
        "For A = 3i + j and B = i + j, the angle between them is approximately:",
        "A = 3i + j এবং B = i + j হলে মধ্যবর্তী কোণ প্রায়:",
        ["25.12°", "26.57°", "90.67°", "180.25°"],
        ["২৫.১২°", "২৬.৫৭°", "৯০.৬৭°", "১৮০.২৫°"],
        "B", "hard", "numerical",
        "A · B = 4; |A| = √10; |B| = √2; cos θ = 4/√20 ≈ 0.8944 ⇒ θ ≈ 26.57°.",
        "cos θ = ৪/√২০ ≈ ০.৮৯৪ ⇒ θ ≈ ২৬.৫৭°।",
    ),
    q(
        "(i × j) × (i × k) equals:",
        "(i × j) × (i × k) এর মান:",
        ["i", "j", "k", "−i"],
        ["i", "j", "k", "−i"],
        "A", "hard", "numerical",
        "i × j = k and i × k = −j, so k × (−j) = i.",
        "k × (−j) = i।",
    ),
    q(
        "The scalar (dot) product obeys: (i) commutative law (ii) distributive law (iii) associative form A · (B · C). Which is correct?",
        "ডট গুণন মেনে চলে: (i) বিনিময় সূত্র (ii) বণ্টন সূত্র (iii) A · (B · C) রূপে সংযোগ সূত্র। কোনটি সঠিক?",
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        "A", "medium", "conceptual",
        "A · B = B · A and distributive law hold; A · (B · C) is invalid because B · C is a scalar.",
        "ডট গুণনে বিনিময় ও বণ্টন সূত্র প্রযোজ্য; A · (B · C) অর্থহীন।",
    ),
    q(
        "Impulse J = F Δt is best described as:",
        "ঘাত J = F Δt-কে সবচেয়ে ভালোভাবে বলা যায়:",
        ["Cross product of two vectors", "A vector multiplied by a scalar (time)", "Dot product of two vectors", "Curl of the force field"],
        ["দুই ভেক্টরের ক্রস গুণন", "ভেক্টরের সাথে স্কেলার (সময়) গুণন", "দুই ভেক্টরের ডট গুণন", "বল ক্ষেত্রের কার্ল"],
        "B", "medium", "conceptual",
        "Time is a scalar, so impulse is a scaled force vector.",
        "সময় স্কেলার, তাই ঘাত = ভেক্টর × স্কেলার।",
    ),
]

def write_topic(topic_id: str, rows: list[dict]) -> None:
    assert len(rows) == 20, (topic_id, len(rows))
    for r in rows:
        r["verified"] = False
        r["source"] = SOURCE
    path = TOPICS / f"{topic_id}.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"wrote {path.name}: {len(rows)}")


def main() -> None:
    write_topic("phy1_27_ch02_t01", T01)
    write_topic("phy1_27_ch02_t02", T02)
    write_topic("phy1_27_ch02_t03", T03)

    summary = {
        "paper": "physics_1",
        "chapter": 2,
        "title_en": "Vectors",
        "title_bn": "ভেক্টর",
        "per_topic": 20,
        "topics": {
            "phy1_27_ch02_t01": 20,
            "phy1_27_ch02_t02": 20,
            "phy1_27_ch02_t03": 20,
        },
        "source": SOURCE,
        "verified": False,
        "mcq_printed_pages": [55, 65],
        "notes": "OCR-noisy pages reconstructed as HSC-accurate bilingual MCQs; figure-only items rewritten in text.",
    }
    out = (
        ROOT
        / "content"
        / "bank"
        / "udvash_raw"
        / "physics_1"
        / "parsed"
        / "ch02_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("summary", out)


if __name__ == "__main__":
    main()
