#!/usr/bin/env python3
"""Seed Higher Mathematics 2nd Paper Ch08 (Statics).

Curated from Udvash HSC Question Bank 2026 printed pp. 258–268 (PDF 264–274).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
OCR is noisy (~11 pages; figures and answer-key math often garbled); reconstructs
board-style items from readable stems/solutions and supplements with accurate
HSC-level authored MCQs (esp. moments/couples and friction, thin in printed MCQs).
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
    "higher_mathematics p2 ch08; curated bilingual"
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
# hm2_27_ch08_t01 — Forces and equilibrium / বল ও সাম্যাবস্থা
# =============================================================================
T01 = [
    q(
        "Two forces acting at 60° have greatest resultant 10 N and least resultant 4 N. The magnitude of their resultant at 60° is:",
        "পরস্পর 60° কোণে ক্রিয়াশীল দুইটি বলের বৃহত্তম লব্ধি 10 N এবং ক্ষুদ্রতম লব্ধি 4 N হলে, তাদের লব্ধির মান কত?",
        ["√37 N", "2√19 N", "√79 N", "2√39 N"],
        ["√37 N", "2√19 N", "√79 N", "2√39 N"],
        "C", "medium", "numerical",
        "P + Q = 10 and P − Q = 4 ⇒ P = 7 N, Q = 3 N. Then R² = 49 + 9 + 2·7·3·cos 60° = 58 + 21 = 79, so R = √79 N.",
        "P + Q = 10, P − Q = 4 ⇒ P = 7, Q = 3। R² = 49 + 9 + 42·(1/2) = 79 ⇒ R = √79 N।",
    ),
    q(
        "Two like parallel forces of weights 12 kg and 8 kg act 40 cm apart on a rigid body. The magnitude of their resultant is:",
        "একটি জড়বস্তুর উপর পরস্পর 40 সে.মি. ব্যবধানে 12 কেজি ও 8 কেজি ওজনের দুইটি সদৃশ সমান্তরাল বল ক্রিয়া করে। লব্ধির মান কত কেজি?",
        ["4", "8", "12", "20"],
        ["4", "8", "12", "20"],
        "D", "easy", "numerical",
        "For like parallel forces the resultant is P + Q = 12 + 8 = 20 kg-wt.",
        "সদৃশ সমান্তরাল বলের লব্ধি P + Q = 12 + 8 = 20 কেজি ওজন।",
    ),
    q(
        "If two forces of equal magnitude have resultant equal to either force, the angle between them is:",
        "মানের সমান দুইটি বলের লব্ধি একটি বলের সমান হলে তাদের মধ্যবর্তী কোণ কত?",
        ["30°", "60°", "120°", "180°"],
        ["30°", "60°", "120°", "180°"],
        "C", "medium", "numerical",
        "R² = P² + P² + 2P² cos α = P² ⇒ 2 + 2 cos α = 1 ⇒ cos α = −1/2 ⇒ α = 120°.",
        "R = P ⇒ 2P²(1 + cos α) = P² ⇒ cos α = −1/2 ⇒ α = 120°।",
    ),
    q(
        "Two forces each of 2 N act at 60°. The direction of the resultant makes which angle with either force?",
        "2 N মানের দুইটি বল পরস্পর 60° কোণে ক্রিয়ারত হলে লব্ধির দিক কোন বলের সাথে কত কোণ উৎপন্ন করে?",
        ["15°", "60°", "30°", "45°"],
        ["15°", "60°", "30°", "45°"],
        "C", "medium", "numerical",
        "Equal forces: the resultant bisects the angle, so each side is 30°.",
        "সমান বলের লব্ধি মধ্যবর্তী কোণকে সমদ্বিখণ্ডিত করে; সুতরাং কোণ 30°।",
    ),
    q(
        "Forces 12 and 8 units act at a point so that the resultant makes 45° with the bisector of their included angle. The included angle is:",
        "12 ও 8 একক মানের বলদ্বয় একটি বিন্দুতে এমন কোণে ক্রিয়াশীল যেন লব্ধি তাদের অন্তর্গত কোণের সমদ্বিখণ্ডকের সাথে 45° কোণ উৎপন্ন করে। মধ্যবর্তী কোণ কত?",
        ["2 tan⁻¹ 10", "2 tan⁻¹ 5", "tan⁻¹ 5", "2 tan⁻¹ 2"],
        ["2 tan⁻¹ 10", "2 tan⁻¹ 5", "tan⁻¹ 5", "2 tan⁻¹ 2"],
        "B", "hard", "numerical",
        "By the tangent law with half-angle α: (P + Q)/(P − Q) = tan(α + 45°)/tan(α − 45°) leads to tan α = 5, so included angle 2α = 2 tan⁻¹ 5.",
        "সাইনের সূত্র ও সমদ্বিখণ্ডক শর্ত থেকে tan α = 5; মধ্যবর্তী কোণ 2α = 2 tan⁻¹ 5।",
    ),
    q(
        "For forces P and Q (P > Q) at angle α, which statements are true? (i) α = 0° gives maximum resultant (ii) α = 180° gives minimum resultant (iii) the component of Q along P is Q cos α",
        "P ও Q (P > Q) বলদ্বয় α কোণে ক্রিয়াশীল হলে কোনটি সঠিক? (i) α = 0° হলে লব্ধি বৃহত্তম (ii) α = 180° হলে লব্ধি ক্ষুদ্রতম (iii) P বরাবর Q এর লম্বাংশ Q cos α",
        ["i, ii only", "i, iii only", "ii, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল i, iii", "কেবল ii, iii", "i, ii ও iii"],
        "D", "easy", "conceptual",
        "R = √(P² + Q² + 2PQ cos α) is max at α = 0°, min at α = 180°, and the resolved part of Q along P is Q cos α. All three hold.",
        "α = 0° এ R বৃহত্তম, α = 180° এ ক্ষুদ্রতম; P বরাবর Q এর লম্বাংশ Q cos α। তিনটিই সঠিক।",
    ),
    q(
        "The resultant of two forces is greatest when the angle between them is:",
        "দুটি বলের লব্ধি বৃহত্তম হলে তাদের মধ্যবর্তী কোণ কত?",
        ["180°", "90°", "45°", "0°"],
        ["180°", "90°", "45°", "0°"],
        "D", "easy", "factual",
        "R² = P² + Q² + 2PQ cos α is largest when cos α = 1, i.e. α = 0°.",
        "cos α = 1 হলে R সর্বোচ্চ; সুতরাং কোণ 0°।",
    ),
    q(
        "Two equal forces of √5 units act at 120° at a point. Which are true? (i) resultant = √5 (ii) resultant makes 60° with each force (iii) resultant is smaller than the sum of the forces",
        "√5 এককের দুইটি সমান বল 120° কোণে এক বিন্দুতে ক্রিয়া করলে কোনটি সঠিক? (i) লব্ধি √5 (ii) প্রত্যেক বলের সাথে 60° কোণ (iii) লব্ধি বলদ্বয়ের যোগফল অপেক্ষা ছোট",
        ["i, ii only", "ii, iii only", "i, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল ii, iii", "কেবল i, iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "R² = 5 + 5 + 2·5·(−1/2) = 5 ⇒ R = √5; equal forces ⇒ bisector gives 60° each; √5 < 2√5. All true.",
        "R = √5; সমান বল হওয়ায় 60° করে; √5 < 2√5। তিনটিই সত্য।",
    ),
    q(
        "Which set of three concurrent forces cannot be represented in magnitude and direction by the sides of a triangle taken in order (hence cannot be in equilibrium)?",
        "একই বিন্দুতে ক্রিয়ারত কোন তিনটি বলকে ত্রিভুজের তিন বাহু দ্বারা মানে ও দিকে প্রকাশ করা সম্ভব নয়?",
        ["1 N, 2 N, 6 N", "2 N, 3 N, 4 N", "3 N, 4 N, 5 N", "3 N, 5 N, 7 N"],
        ["1 N, 2 N, 6 N", "2 N, 3 N, 4 N", "3 N, 4 N, 5 N", "3 N, 5 N, 7 N"],
        "A", "medium", "conceptual",
        "Triangle inequality fails for 1, 2, 6 because 1 + 2 < 6; the other sets can form a triangle.",
        "1 + 2 < 6 বলে ত্রিভুজ অসমতা মানা হয় না; অন্যগুলো সম্ভব।",
    ),
    q(
        "For forces P and Q at angle α with resultant R, which are true? (i) R = P + Q when α = 90° (ii) R = |P − Q| when α = 180° (iii) if Q = P then R = 2P cos(α/2)",
        "α কোণে ক্রিয়ারত P ও Q এর লব্ধি R হলে কোনটি সঠিক? (i) α = 90° এ R = P + Q (ii) α = 180° এ R = |P − Q| (iii) Q = P হলে R = 2P cos(α/2)",
        ["i, ii only", "i, iii only", "ii, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল i, iii", "কেবল ii, iii", "i, ii ও iii"],
        "C", "medium", "conceptual",
        "(i) is false: at 90°, R = √(P² + Q²). (ii) and (iii) are standard identities.",
        "(i) ভুল—α = 90° এ R = √(P² + Q²)। (ii) ও (iii) সঠিক।",
    ),
    q(
        "If the resultant of 6 N and 8 N is 2√13 N, the angle between the forces is:",
        "6 N ও 8 N বল দুটির মধ্যবর্তী কোণ কত হলে লব্ধি 2√13 N হবে?",
        ["30°", "60°", "90°", "120°"],
        ["30°", "60°", "90°", "120°"],
        "D", "medium", "numerical",
        "(2√13)² = 36 + 64 + 96 cos α ⇒ 52 = 100 + 96 cos α ⇒ cos α = −1/2 ⇒ α = 120°.",
        "52 = 100 + 96 cos α ⇒ cos α = −1/2 ⇒ α = 120°।",
    ),
    q(
        "If three concurrent forces are in equilibrium, the resultant of any two is, relative to the third:",
        "কোনো বিন্দুতে ক্রিয়ারত তিনটি বল সাম্যাবস্থায় থাকলে যেকোনো দুটির লব্ধি তৃতীয় বলের—",
        ["equal and parallel only", "equal and opposite only", "parallel and opposite only", "equal, parallel and opposite"],
        ["কেবল সমান ও সমান্তরাল", "কেবল সমান ও বিপরীতমুখী", "কেবল সমান্তরাল ও বিপরীতমুখী", "সমান, সমান্তরাল ও বিপরীতমুখী"],
        "D", "easy", "factual",
        "For equilibrium the resultant of any two must cancel the third: same magnitude, parallel, opposite sense.",
        "সাম্যাবস্থায় যেকোনো দুই বলের লব্ধি তৃতীয়ের সমান, সমান্তরাল ও বিপরীতমুখী।",
    ),
    q(
        "Forces P and Q act at a point; their resultant R makes 30° with P and 60° with Q. Then P : Q equals:",
        "এক বিন্দুতে ক্রিয়ারত P ও Q এর লব্ধি R যথাক্রমে 30° ও 60° কোণে আনত হলে P : Q কত?",
        ["2 : √3", "√3 : 1", "√3 : 2", "1 : √3"],
        ["2 : √3", "√3 : 1", "√3 : 2", "1 : √3"],
        "B", "medium", "numerical",
        "By Lami / sine law: P / sin 60° = Q / sin 30° ⇒ P/Q = (√3/2)/(1/2) = √3 : 1.",
        "P/sin 60° = Q/sin 30° ⇒ P : Q = √3 : 1।",
    ),
    q(
        "Forces 5 N and 7 N act in opposite directions along a line. The resultant acts:",
        "5 N ও 7 N মানের দুটি বল পরস্পর বিপরীত দিকে ক্রিয়াশীল। এদের লব্ধি কোন দিকে ক্রিয়া করবে?",
        ["along the line of the 7 N force", "perpendicular to the 7 N force", "perpendicular to the 5 N force", "along the line of the 5 N force"],
        ["7 N বলের ক্রিয়ারেখা বরাবর", "7 N বলের উপর লম্ব", "5 N বলের উপর লম্ব", "5 N বলের ক্রিয়ারেখা বরাবর"],
        "A", "easy", "conceptual",
        "Resultant = 7 − 5 = 2 N along the larger (7 N) force.",
        "লব্ধি = 7 − 5 = 2 N; বৃহত্তর 7 N এর দিকে ক্রিয়া করে।",
    ),
    q(
        "Two equal forces each of magnitude P act at 60° and keep a particle in equilibrium with a third force. Each equal force has magnitude:",
        "কোনো বিন্দুতে 60° কোণে ক্রিয়ারত দুটি সমান বল একটি তৃতীয় বলের সাথে সাম্যাবস্থায় আছে। প্রতিটি সমান বলের মান কত, যদি তৃতীয় বল 9 N হয়?",
        ["√3 N", "3√3 N", "3 N", "9 N"],
        ["√3 N", "3√3 N", "3 N", "9 N"],
        "B", "medium", "numerical",
        "Resultant of the equals is 2P cos 30° = P√3 and balances 9 N ⇒ P√3 = 9 ⇒ P = 3√3 N.",
        "লব্ধি 2P cos 30° = P√3 = 9 ⇒ P = 3√3 N।",
    ),
    q(
        "The least resultant of two forces P and Q occurs when the angle between them is:",
        "দুইটি বলের ক্ষুদ্রতম লব্ধির ক্ষেত্রে বলদ্বয়ের মধ্যবর্তী কোণ কত?",
        ["0°", "90°", "120°", "180°"],
        ["0°", "90°", "120°", "180°"],
        "D", "easy", "factual",
        "cos α is most negative at α = 180°, giving R_min = |P − Q|.",
        "α = 180° এ cos α = −1; লব্ধি ক্ষুদ্রতম |P − Q|।",
    ),
    q(
        "The greatest resultant of two forces P and Q is:",
        "বলদ্বয়ের বৃহত্তম লব্ধি কত?",
        ["|P − Q|", "√(P² + Q²)", "P − Q", "P + Q"],
        ["|P − Q|", "√(P² + Q²)", "P − Q", "P + Q"],
        "D", "easy", "factual",
        "Maximum resultant is P + Q when the forces act in the same direction.",
        "একই দিকে ক্রিয়া করলে বৃহত্তম লব্ধি P + Q।",
    ),
    q(
        "A force has horizontal and vertical components 4 N and 3 N. The magnitude of the force is:",
        "একটি বলের আনুভূমিক ও উলম্ব উপাংশের মান 4 N ও 3 N হলে বলটির মান—",
        ["5 N", "10 N", "2√3 N", "7 N"],
        ["5 N", "10 N", "2√3 N", "7 N"],
        "A", "easy", "numerical",
        "Magnitude = √(4² + 3²) = √25 = 5 N.",
        "মান = √(16 + 9) = 5 N।",
    ),
    q(
        "The least resultant of two forces is 1 N and when they act at right angles the resultant is 5 N. The greatest resultant is:",
        "একই বিন্দুতে ক্রিয়ারত দুটি বলের ক্ষুদ্রতম লব্ধি 1 N এবং লম্বভাবে ক্রিয়াশীল হলে লব্ধি 5 N। বৃহত্তম লব্ধির মান—",
        ["5 N", "2 N", "7 N", "3 N"],
        ["5 N", "2 N", "7 N", "3 N"],
        "C", "hard", "numerical",
        "(P − Q)² = 1 and P² + Q² = 25. Then (P + Q)² + (P − Q)² = 2(P² + Q²) ⇒ (P + Q)² + 1 = 50 ⇒ P + Q = 7 N.",
        "(P − Q)² = 1, P² + Q² = 25 ⇒ (P + Q)² = 49 ⇒ P + Q = 7 N।",
    ),
    q(
        "Forces Q and 2Q act at a point; their resultant is perpendicular to Q. Which are true? (i) included angle is 120° (ii) resultant = √3 Q (iii) resolved part of 2Q along Q is +Q",
        "কোনো বিন্দুতে ক্রিয়ারত Q ও 2Q এর লব্ধি Q এর উপর লম্ব হলে কোনটি সঠিক? (i) মধ্যবর্তী কোণ 120° (ii) লব্ধি √3 Q (iii) Q বরাবর 2Q এর ধনাত্মক লম্বাংশ +Q",
        ["i, ii only", "i, iii only", "ii, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল i, iii", "কেবল ii, iii", "i, ii ও iii"],
        "A", "hard", "conceptual",
        "R ⊥ Q ⇒ Q + 2Q cos α = 0 ⇒ cos α = −1/2 ⇒ α = 120°. Then R = √3 Q. Resolved part of 2Q along Q is 2Q cos 120° = −Q, so (iii) is false.",
        "α = 120°, R = √3 Q; 2Q cos 120° = −Q বলে (iii) ভুল। কেবল i, ii সঠিক।",
    ),
]


# =============================================================================
# hm2_27_ch08_t02 — Moments and couples / বলের ভ্রামক ও বলযুগল
# =============================================================================
T02 = [
    q(
        "The moment of a force F about a point is the product of F and:",
        "কোনো বিন্দু সাপেক্ষে F বলের ভ্রামক হলো F এবং কোনটির গুণফল?",
        ["the distance to the point of application along the force", "the perpendicular distance from the point to the line of action", "the square of the force", "the mass of the body"],
        ["বল বরাবর ক্রিয়াবিন্দুর দূরত্ব", "বিন্দু থেকে ক্রিয়ারেখার উপর লম্ব দূরত্ব", "বলের বর্গ", "বস্তুর ভর"],
        "B", "easy", "factual",
        "Moment = force × perpendicular distance from the point to the line of action.",
        "ভ্রামক = বল × বিন্দু থেকে ক্রিয়ারেখার উপর লম্ব দূরত্ব।",
    ),
    q(
        "A couple consists of two forces that are:",
        "বলযুগল গঠিত হয় এমন দুইটি বল দ্বারা যা—",
        ["equal, parallel and like", "equal, parallel and unlike", "unequal and concurrent", "perpendicular and equal"],
        ["সমান, সমান্তরাল ও সদৃশ", "সমান, সমান্তরাল ও বিসদৃশ", "অসমান ও সমবিন্দু", "লম্ব ও সমান"],
        "B", "easy", "factual",
        "A couple is a pair of equal, parallel, opposite (unlike) forces whose lines of action do not coincide.",
        "বলযুগল = সমান, সমান্তরাল ও বিপরীতমুখী (বিসদৃশ) দুই বল।",
    ),
    q(
        "The moment of a couple of forces ±F with arm (perpendicular separation) d is:",
        "±F বলের বলযুগলের বাহু d হলে যুগলের ভ্রামক কত?",
        ["F + d", "F / d", "F · d", "2F · d"],
        ["F + d", "F / d", "F · d", "2F · d"],
        "C", "easy", "factual",
        "Moment of a couple = F × d (independent of the reference point in the plane).",
        "বলযুগলের ভ্রামক = F × d।",
    ),
    q(
        "Unlike parallel forces 45 N and 15 N act at A and B; their resultant acts at C with AC = 5 m. Then AB equals:",
        "A ও B বিন্দুতে ক্রিয়ারত 45 N ও 15 N বিসদৃশ সমান্তরাল বলের লব্ধি C বিন্দুতে ক্রিয়া করে। AC = 5 m হলে AB = কত?",
        ["5 m", "10 m", "15 m", "20 m"],
        ["5 m", "10 m", "15 m", "20 m"],
        "B", "medium", "numerical",
        "For unlike parallels, R = 45 − 15 = 30 N and 45·AC = 15·BC ⇒ 45·5 = 15·BC ⇒ BC = 15 m ⇒ AB = BC − AC = 10 m (C beyond A away from B is the usual layout: actually 45·AC = 15·(AC+AB) wait). Standard: distances from C satisfy P·CA = Q·CB. With R outside nearer the larger force: 45·5 = 15·CB ⇒ CB = 15, AB = |CB − CA| = 10 m.",
        "বিসদৃশ সমান্তরালে 45·AC = 15·BC ⇒ BC = 15 m ⇒ AB = 10 m।",
    ),
    q(
        "Like parallel forces 8 and 6 units act 21 units apart on a rigid body. If the forces interchange positions, the resultant’s point of action shifts by:",
        "8 ও 6 একক মানের দুইটি সদৃশ সমান্তরাল বল 21 একক দূরত্বে ক্রিয়ারত। অবস্থান বিনিময় করলে লব্ধির ক্রিয়াবিন্দু কত একক সরে যাবে?",
        ["1 unit", "2 units", "3 units", "4 units"],
        ["1 একক", "2 একক", "3 একক", "4 একক"],
        "C", "medium", "numerical",
        "Shift = |P − Q|·d/(P + Q) = 2·21/14 = 3 units.",
        "সরণ = |P − Q|·d/(P + Q) = 2·21/14 = 3 একক।",
    ),
    q(
        "Parallel forces 3 and 6 units act at A and B with AB = 4. Which are true? (i) like ⇒ resultant 9 (ii) unlike ⇒ resultant 3 (iii) unlike with resultant at R beyond A ⇒ BR = 4",
        "4 দূরত্বে A ও B তে ক্রিয়ারত 3 ও 6 একক সমান্তরাল বলদ্বয়— (i) সদৃশ হলে লব্ধি 9 (ii) অসদৃশ হলে লব্ধি 3 (iii) অসদৃশ এবং লব্ধি R তে হলে BR = 4",
        ["i, ii only", "i, iii only", "ii, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল i, iii", "কেবল ii, iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "Like: R = 9. Unlike: R = 3. For unlike with R beyond A: 3·(4 + BR) = 6·BR ⇒ BR = 4. All true.",
        "সদৃশে 9, অসদৃশে 3; BR = 4। তিনটিই সঠিক।",
    ),
    q(
        "Unlike parallel forces 42 N and 24 N act at A and B; the resultant meets the extension of BA at C. Then AB : BC equals:",
        "A ও B তে যথাক্রমে 42 N ও 24 N অসদৃশ সমান্তরাল বল ক্রিয়ারত। লব্ধির ক্রিয়াবিন্দু BA এর বর্ধিতাংশে C তে হলে AB : BC = কত?",
        ["3 : 7", "4 : 7", "7 : 3", "7 : 4"],
        ["3 : 7", "4 : 7", "7 : 3", "7 : 4"],
        "C", "hard", "numerical",
        "Order C–A–B: 42·AC = 24·BC and BC = AC + AB ⇒ 7 AC = 4(AC + AB) ⇒ 3 BC = 7 AB ⇒ AB : BC = 7 : 3.",
        "C–A–B ক্রমে 42·AC = 24·BC ⇒ 3 BC = 7 AB ⇒ AB : BC = 7 : 3।",
    ),
    q(
        "Three equal like parallel forces act at the vertices of a triangle. Their resultant passes through the:",
        "কোনো ত্রিভুজের শীর্ষবিন্দুতে তিনটি সমান সদৃশ সমান্তরাল বল ক্রিয়া করলে তাদের লব্ধি—",
        ["orthocentre", "incentre", "circumcentre", "centroid"],
        ["লম্বকেন্দ্রগামী", "অন্তঃকেন্দ্রগামী", "পরিকেন্দ্রগামী", "ভরকেন্দ্রগামী"],
        "D", "medium", "factual",
        "Equal parallel forces at vertices are equivalent to a single force through the centroid (centre of mass of three equal particles).",
        "সমান সদৃশ সমান্তরাল বলের লব্ধি ভরকেন্দ্রগামী।",
    ),
    q(
        "For triangle ABC, like parallel forces P, Q, R at A, B, C have resultant through the centroid when:",
        "△ABC এর কৌণিক বিন্দুতে P, Q, R সদৃশ সমান্তরাল; লব্ধি ভরকেন্দ্রগামী হলে—",
        ["P : Q : R = sin A : sin B : sin C", "P : Q : R = tan A : tan B : tan C", "P : Q : R = sin 2A : sin 2B : sin 2C", "P : Q : R = 1 : 1 : 1"],
        ["P : Q : R = sin A : sin B : sin C", "P : Q : R = tan A : tan B : tan C", "P : Q : R = sin 2A : sin 2B : sin 2C", "P : Q : R = 1 : 1 : 1"],
        "D", "medium", "conceptual",
        "The centroid is the balance point of equal weights at the vertices, so P = Q = R.",
        "ভরকেন্দ্রগামী হতে হলে P = Q = R অর্থাৎ 1 : 1 : 1।",
    ),
    q(
        "On a uniform rod AB = 14 cm, like parallel forces 10 N and 4 N act at A and B. The resultant acts:",
        "AB = 14 cm সুষম দণ্ডে A ও B তে 10 N ও 4 N সমমুখী সমান্তরাল বল ক্রিয়া করলে লব্ধির অবস্থান—",
        ["4 cm from A", "6 cm from A", "4 cm from B", "10 cm from B"],
        ["A থেকে 4 cm দূরে", "A থেকে 6 cm দূরে", "B থেকে 4 cm দূরে", "B থেকে 10 cm দূরে"],
        "A", "medium", "numerical",
        "Distance from A is Q·AB/(P + Q) = 4·14/14 = 4 cm.",
        "A থেকে দূরত্ব = Q·AB/(P + Q) = 4·14/14 = 4 cm।",
    ),
    q(
        "Like parallel forces P = 6 kg-wt and Q = 4 kg-wt act with AB = 5 m. After interchange, the resultant shifts along AB by:",
        "P = 6 কেজি ওজন, Q = 4 কেজি ওজন এবং AB = 5 মিটার (সদৃশ)। অবস্থান বিনিময় করলে লব্ধি AB বরাবর কত সরে?",
        ["2 m", "0 m", "1 m", "3 m"],
        ["2 মিটার", "0 মিটার", "1 মিটার", "3 মিটার"],
        "C", "medium", "numerical",
        "Shift = |P − Q|·AB/(P + Q) = 2·5/10 = 1 m.",
        "সরণ = |P − Q|·AB/(P + Q) = 2·5/10 = 1 মিটার।",
    ),
    q(
        "Varignon’s theorem states that the algebraic sum of the moments of several coplanar forces about a point equals:",
        "ভেরিগননের উপপাদ্য অনুসারে সমতলীয় কয়েকটি বলের কোনো বিন্দু সাপেক্ষে ভ্রামকের বীজগাণিতিক যোগফল সমান—",
        ["the sum of the forces", "the moment of their resultant about the same point", "zero always", "the product of the forces"],
        ["বলগুলোর যোগফলের", "একই বিন্দু সাপেক্ষে তাদের লব্ধির ভ্রামকের", "সবসময় শূন্যের", "বলগুলোর গুণফলের"],
        "B", "easy", "factual",
        "Varignon: Σ moments of forces = moment of the resultant about the same point.",
        "ভেরিগনন: বলগুলোর ভ্রামকের যোগ = লব্ধির ভ্রামক।",
    ),
    q(
        "A force of 10 N acts along a line 0.5 m from a point O. The moment about O is:",
        "10 N বলের ক্রিয়ারেখা O বিন্দু থেকে 0.5 m লম্ব দূরে। O সাপেক্ষে ভ্রামক কত?",
        ["2 N·m", "5 N·m", "10 N·m", "20 N·m"],
        ["2 N·m", "5 N·m", "10 N·m", "20 N·m"],
        "B", "easy", "numerical",
        "M = F · d = 10 × 0.5 = 5 N·m.",
        "M = 10 × 0.5 = 5 N·m।",
    ),
    q(
        "Two equal unlike parallel forces each of magnitude P form a couple of moment 12 N·m with arm 0.4 m. Then P equals:",
        "প্রত্যেকটির মান P এমন দুইটি সমান বিসদৃশ সমান্তরাল বলের যুগলভ্রামক 12 N·m এবং বাহু 0.4 m হলে P = কত?",
        ["3 N", "12 N", "30 N", "48 N"],
        ["3 N", "12 N", "30 N", "48 N"],
        "C", "medium", "numerical",
        "P · d = 12 ⇒ P · 0.4 = 12 ⇒ P = 30 N.",
        "P × 0.4 = 12 ⇒ P = 30 N।",
    ),
    q(
        "The algebraic sum of moments of two forces forming a couple about any point in their plane is:",
        "বলযুগল গঠনকারী দুই বলের সমতলের যেকোনো বিন্দু সাপেক্ষে ভ্রামকের বীজগাণিতিক যোগফল—",
        ["zero", "equal to the moment of the couple", "equal to either force", "undefined"],
        ["শূন্য", "যুগলের ভ্রামকের সমান", "যেকোনো এক বলের সমান", "অসংজ্ঞাত"],
        "B", "medium", "conceptual",
        "For a couple, the total moment about every point in the plane equals F·d, the couple moment.",
        "বলযুগলের মোট ভ্রামক সমতলের সকল বিন্দুতে F·d।",
    ),
    q(
        "Like parallel forces 12 N and 8 N act at A and B. After they swap positions, the resultant’s point of action moves along AB by what fraction of AB?",
        "12 N ও 8 N দুইটি সমমুখী সমান্তরাল বল A ও B তে ক্রিয়াশীল। অবস্থান বিনিময় করলে লব্ধির ক্রিয়াবিন্দু AB এর কত অংশ সরে?",
        ["(1/5) AB", "(1/4) AB", "(2/5) AB", "(1/2) AB"],
        ["(1/5) AB", "(1/4) AB", "(2/5) AB", "(1/2) AB"],
        "A", "medium", "numerical",
        "Shift/AB = |P − Q|/(P + Q) = 4/20 = 1/5.",
        "সরণ/AB = |12 − 8|/(12 + 8) = 1/5।",
    ),
    q(
        "Downward forces 7 N at A and 13 N at C on a light rod are balanced by an upward force 20 N at B between A and C. Then AB : BC equals:",
        "হালকা দণ্ডে A তে 7 N ও C তে 13 N নিম্নমুখী বল B তে 20 N ঊর্ধ্বমুখী বল দ্বারা সাম্যাবস্থায় থাকলে AB : BC = কত?",
        ["20 : 13", "20 : 7", "13 : 7", "7 : 13"],
        ["20 : 13", "20 : 7", "13 : 7", "7 : 13"],
        "C", "hard", "numerical",
        "Moments about B: 7·AB = 13·BC ⇒ AB : BC = 13 : 7.",
        "B সাপেক্ষে ভ্রামক: 7·AB = 13·BC ⇒ AB : BC = 13 : 7।",
    ),
    q(
        "A light beam has loads 10 kg-wt at A and W at G; the support pressure at C is 30 kg-wt. If C supports both loads alone in the stimulus, W equals:",
        "A প্রান্তে 10 kg ওজন এবং G তে W; C তে চাপ 30 kg ওজন হলে W = কত kg?",
        ["10", "20", "35", "40"],
        ["10", "20", "35", "40"],
        "B", "medium", "numerical",
        "Vertical equilibrium at the single support C: 30 = 10 + W ⇒ W = 20 kg.",
        "C তে চাপ = 10 + W = 30 ⇒ W = 20 kg।",
    ),
    q(
        "A light beam has support reaction at C, a load 10 kg-wt at A with AC = 1 m, and load 20 kg-wt at midpoint G of AB (AG = BG). For rotational equilibrium about C, AB equals:",
        "C তে আলম্ব, A তে 10 kg ওজন (AC = 1 m), AB এর মধ্যবিন্দু G তে 20 kg ওজন (AG = BG)। C সাপেক্ষে সাম্যাবস্থায় AB = কত m?",
        ["2", "3", "4", "6"],
        ["2", "3", "4", "6"],
        "B", "hard", "numerical",
        "Moments about C: 10·1 = 20·(AB/2 − 1) ⇒ 1 = AB − 2 ⇒ AB = 3 m.",
        "10·1 = 20·(AB/2 − 1) ⇒ AB = 3 m।",
    ),
    q(
        "The unit of moment of a force in the SI system is:",
        "SI পদ্ধতিতে বলের ভ্রামকের একক কোনটি?",
        ["newton", "newton·metre", "joule / second", "pascal"],
        ["নিউটন", "নিউটন·মিটার", "জুল / সেকেন্ড", "প্যাসকেল"],
        "B", "easy", "factual",
        "Moment = force × distance, so the SI unit is N·m (newton-metre).",
        "ভ্রামক = বল × দূরত্ব; SI একক N·m।",
    ),
]


# =============================================================================
# hm2_27_ch08_t03 — Friction / ঘর্ষণ
# =============================================================================
T03 = [
    q(
        "The coefficient of friction μ is defined as the ratio of:",
        "ঘর্ষণাঙ্ক μ সংজ্ঞায়িত হয় কোন অনুপাত দ্বারা?",
        ["normal reaction / limiting friction", "limiting friction / normal reaction", "weight / limiting friction", "limiting friction / weight"],
        ["অভিলম্ব প্রতিক্রিয়া / সীমাবদ্ধ ঘর্ষণ", "সীমাবদ্ধ ঘর্ষণ / অভিলম্ব প্রতিক্রিয়া", "ওজন / সীমাবদ্ধ ঘর্ষণ", "সীমাবদ্ধ ঘর্ষণ / ওজন"],
        "B", "easy", "factual",
        "By definition μ = F/R where F is limiting friction and R is the normal reaction.",
        "সংজ্ঞা অনুসারে μ = F/R (সীমাবদ্ধ ঘর্ষণ / অভিলম্ব প্রতিক্রিয়া)।",
    ),
    q(
        "Limiting friction is:",
        "সীমাবদ্ধ ঘর্ষণ হলো—",
        ["friction when the body is at rest with no tendency to move", "the maximum friction that can act before sliding starts", "friction during uniform motion only", "always equal to the weight"],
        ["নড়ার প্রবণতা ছাড়া স্থির অবস্থার ঘর্ষণ", "পিছলানো শুরুর ঠিক আগের সর্বোচ্চ ঘর্ষণ", "কেবল সমবেগে চলাকালীন ঘর্ষণ", "সবসময় ওজনের সমান"],
        "B", "easy", "factual",
        "Limiting friction is the greatest friction available when sliding is just about to begin.",
        "পিছলানো আরম্ভের মুহূর্তে প্রাপ্য সর্বোচ্চ ঘর্ষণই সীমাবদ্ধ ঘর্ষণ।",
    ),
    q(
        "If λ is the angle of friction, then:",
        "λ ঘর্ষণকোণ হলে—",
        ["μ = sin λ", "μ = cos λ", "μ = tan λ", "μ = cot λ"],
        ["μ = sin λ", "μ = cos λ", "μ = tan λ", "μ = cot λ"],
        "C", "easy", "factual",
        "The angle of friction satisfies tan λ = F/R = μ.",
        "tan λ = F/R = μ।",
    ),
    q(
        "The angle of repose α for a rough inclined plane equals:",
        "রুক্ষ হেলানো তলের বিশ্রামকোণ α সমান—",
        ["the angle of friction", "twice the angle of friction", "half the angle of friction", "90° minus the angle of friction"],
        ["ঘর্ষণকোণের", "ঘর্ষণকোণের দ্বিগুণের", "ঘর্ষণকোণের অর্ধেকের", "90° − ঘর্ষণকোণের"],
        "A", "easy", "factual",
        "On an incline, impending slide down gives tan α = μ = tan λ, so α = λ (angle of repose = angle of friction).",
        "tan α = μ = tan λ ⇒ α = λ; বিশ্রামকোণ = ঘর্ষণকোণ।",
    ),
    q(
        "A body of weight W rests on a rough horizontal plane with coefficient μ. The least horizontal force that can move it is:",
        "রুক্ষ আনুভূমিক তলে μ ঘর্ষণাঙ্কে W ওজনের বস্তু স্থির। একে নড়াতে প্রয়োজনীয় ক্ষুদ্রতম আনুভূমিক বল—",
        ["μW", "W/μ", "W√(1 + μ²)", "μW / √(1 + μ²)"],
        ["μW", "W/μ", "W√(1 + μ²)", "μW / √(1 + μ²)"],
        "A", "easy", "numerical",
        "Limiting friction F = μR = μW, so the least horizontal force is μW.",
        "সীমাবদ্ধ ঘর্ষণ F = μW; ক্ষুদ্রতম আনুভূমিক বল μW।",
    ),
    q(
        "A body of weight W rests on a rough horizontal plane (coefficient μ). The magnitude of the least force that can move it is:",
        "রুক্ষ আনুভূমিক তলে W ওজনের বস্তুকে নড়াতে ক্ষুদ্রতম বলের মান—",
        ["μW", "W/μ", "μW / √(1 + μ²)", "W√(1 + μ²)"],
        ["μW", "W/μ", "μW / √(1 + μ²)", "W√(1 + μ²)"],
        "C", "hard", "numerical",
        "Least force F_min = μW/√(1+μ²) = W sin λ, applied at the angle of friction to the horizontal.",
        "ক্ষুদ্রতম বল F_min = μW/√(1+μ²) = W sin λ।",
    ),
    q(
        "On a rough incline of inclination α (< λ), a body of weight W is kept at rest. The friction force acting is:",
        "রুক্ষ হেলানো তলের নতি α (< λ) হলে W ওজনের বস্তু স্থির থাকলে কার্যরত ঘর্ষণ—",
        ["μW", "W sin α", "W cos α", "μW cos α"],
        ["μW", "W sin α", "W cos α", "μW cos α"],
        "B", "medium", "conceptual",
        "Static friction balances the downhill component: f = W sin α (≤ μW cos α since α < λ).",
        "স্থিতি ঘর্ষণ = W sin α (α < λ বলে সীমার নিচে)।",
    ),
    q(
        "A body rests on a rough plane inclined at the angle of repose. The friction force equals:",
        "বিশ্রামকোণে নত রুক্ষ তলে বস্তু স্থির থাকলে ঘর্ষণ বল সমান—",
        ["W", "W cos α", "W sin α", "zero"],
        ["W", "W cos α", "W sin α", "শূন্য"],
        "C", "medium", "numerical",
        "At repose α = λ, friction is limiting and equals the parallel component W sin α.",
        "বিশ্রামে ঘর্ষণ সীমাবদ্ধ এবং W sin α এর সমান।",
    ),
    q(
        "P and Q can each separately hold weight W on a rough inclined plane when acting respectively parallel to the length and parallel to the base. A standard relation is:",
        "হেলানো তলের দৈর্ঘ্য ও ভূমির সমান্তরালে ক্রিয়া করে P ও Q প্রত্যেকে আলাদাভাবে W ওজন ধরে রাখতে পারে। একটি আদর্শ সম্পর্ক কোনটি?",
        ["P + Q = W", "1/P² + 1/Q² = 1/W²", "P − Q = W", "PQ = W²"],
        ["P + Q = W", "1/P² + 1/Q² = 1/W²", "P − Q = W", "PQ = W²"],
        "B", "hard", "conceptual",
        "Resolving for the two directions of support on a rough incline yields the identity 1/P² + 1/Q² = 1/W².",
        "রুক্ষ হেলানো তলে এই দুই দিকের ধারণ থেকে 1/P² + 1/Q² = 1/W² পাওয়া যায়।",
    ),
    q(
        "Kinetic (sliding) friction compared with limiting friction for the same surfaces is usually:",
        "একই তলের জন্য গতিশীল (পিছলানো) ঘর্ষণ সীমাবদ্ধ ঘর্ষণ অপেক্ষা সাধারণত—",
        ["greater", "equal", "smaller", "unrelated"],
        ["বৃহত্তর", "সমান", "ক্ষুদ্রতর", "সম্পর্কহীন"],
        "C", "easy", "factual",
        "Once sliding starts, kinetic friction is typically slightly less than limiting friction.",
        "পিছলানো শুরু হলে গতিশীল ঘর্ষণ সাধারণত সীমাবদ্ধ ঘর্ষণের চেয়ে কম।",
    ),
    q(
        "Friction always acts:",
        "ঘর্ষণ সবসময় ক্রিয়া করে—",
        ["in the direction of motion", "opposite to the relative tendency of motion at the contact", "normal to the surface only", "vertically upward"],
        ["গতির দিকে", "স্পর্শতলে আপেক্ষিক গতিপ্রবণতার বিপরীতে", "কেবল তলের অভিলম্বে", "উল্লম্ব ঊর্ধ্বে"],
        "B", "easy", "conceptual",
        "Friction opposes the relative tendency of motion between the contacting surfaces.",
        "ঘর্ষণ স্পর্শতলে আপেক্ষিক গতিপ্রবণতার বিপরীতে ক্রিয়া করে।",
    ),
    q(
        "A block of mass m on a rough horizontal floor (μ) is pulled by a force F at angle θ above the horizontal. The normal reaction is:",
        "রুক্ষ আনুভূমিক মেঝেতে (μ) m ভরের ব্লককে অনুভূমিকের সাথে θ কোণে F বল দিয়ে টানা হলে অভিলম্ব প্রতিক্রিয়া—",
        ["mg", "mg + F sin θ", "mg − F sin θ", "F cos θ"],
        ["mg", "mg + F sin θ", "mg − F sin θ", "F cos θ"],
        "C", "medium", "numerical",
        "Vertical equilibrium: R + F sin θ = mg ⇒ R = mg − F sin θ.",
        "উল্লম্ব সাম্যাবস্থা: R + F sin θ = mg ⇒ R = mg − F sin θ।",
    ),
    q(
        "A block of weight mg on a rough horizontal floor (μ) is pulled by force F at angle θ above the horizontal. Motion impends when:",
        "রুক্ষ আনুভূমিক মেঝেতে mg ওজনের ব্লককে θ কোণে F দিয়ে টানলে পিছলানো আরম্ভ হয় যখন—",
        ["F = μ mg", "F = μ mg / (cos θ + μ sin θ)", "F = μ mg / (cos θ − μ sin θ)", "F = mg tan θ"],
        ["F = μ mg", "F = μ mg / (cos θ + μ sin θ)", "F = μ mg / (cos θ − μ sin θ)", "F = mg tan θ"],
        "B", "hard", "numerical",
        "F cos θ = μ(mg − F sin θ) ⇒ F = μ mg / (cos θ + μ sin θ).",
        "F cos θ = μ(mg − F sin θ) ⇒ F = μ mg / (cos θ + μ sin θ)।",
    ),
    q(
        "If μ = 1/√3, the angle of friction λ is:",
        "μ = 1/√3 হলে ঘর্ষণকোণ λ কত?",
        ["30°", "45°", "60°", "90°"],
        ["30°", "45°", "60°", "90°"],
        "A", "easy", "numerical",
        "tan λ = μ = 1/√3 ⇒ λ = 30°.",
        "tan λ = 1/√3 ⇒ λ = 30°।",
    ),
    q(
        "A body is just on the point of sliding down a rough incline of inclination 30°. Then μ equals:",
        "30° নতির রুক্ষ তলে বস্তু ঠিক পিছলে যাওয়ার মুহূর্তে থাকলে μ = কত?",
        ["1/√3", "√3", "1", "1/2"],
        ["1/√3", "√3", "1", "1/2"],
        "A", "easy", "numerical",
        "At limiting equilibrium on an incline, μ = tan α = tan 30° = 1/√3.",
        "সীমাবস্থায় μ = tan 30° = 1/√3।",
    ),
    q(
        "To prevent a body from sliding down a rough incline α with μ < tan α, the least force parallel to the incline (up) is:",
        "μ < tan α হলে রুক্ষ তলে বস্তুকে পিছলাতে না দিয়ে তল বরাবর ঊর্ধ্বে প্রযুক্ত ক্ষুদ্রতম বল—",
        ["W(sin α − μ cos α)", "W(sin α + μ cos α)", "W(μ sin α − cos α)", "μW"],
        ["W(sin α − μ cos α)", "W(sin α + μ cos α)", "W(μ sin α − cos α)", "μW"],
        "A", "medium", "numerical",
        "Downhill component W sin α exceeds μW cos α; least uphill force = W sin α − μ W cos α.",
        "ক্ষুদ্রতম ঊর্ধ্বমুখী বল = W(sin α − μ cos α)।",
    ),
    q(
        "The least force parallel to a rough incline that can drag a body up the plane is:",
        "রুক্ষ হেলানো তল বরাবর বস্তুকে উপরে টেনে নেওয়ার ক্ষুদ্রতম সমান্তরাল বল—",
        ["W(sin α − μ cos α)", "W(sin α + μ cos α)", "W cos α", "μ W sin α"],
        ["W(sin α − μ cos α)", "W(sin α + μ cos α)", "W cos α", "μ W sin α"],
        "B", "medium", "numerical",
        "Uphill motion: overcome W sin α and friction μ W cos α (down the plane) ⇒ F = W(sin α + μ cos α).",
        "উপরে টানতে F = W(sin α + μ cos α)।",
    ),
    q(
        "Laws of dry friction include: friction is (i) independent of area of contact (approx.) (ii) proportional to normal reaction (iii) dependent on the nature of the surfaces. Which are accepted?",
        "শুষ্ক ঘর্ষণের সূত্র: ঘর্ষণ (i) স্পর্শতলের ক্ষেত্রফল নিরপেক্ষ (প্রায়) (ii) অভিলম্ব প্রতিক্রিয়ার সমানুপাতিক (iii) তলের প্রকৃতির উপর নির্ভরশীল। কোনটি গ্রহণযোগ্য?",
        ["i, ii only", "ii, iii only", "i, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল ii, iii", "কেবল i, iii", "i, ii ও iii"],
        "D", "easy", "conceptual",
        "All three are classical approximate laws of dry (Coulomb) friction.",
        "তিনটিই শুষ্ক ঘর্ষণের ধ্রুপদী সূত্র।",
    ),
    q(
        "A particle on a rough horizontal plane is acted on by a force equal to half its weight. If μ = 1/√3, the particle:",
        "রুক্ষ আনুভূমিক তলে কণার ওজনের অর্ধেক মানের বল ক্রিয়া করে। μ = 1/√3 হলে কণা—",
        ["remains at rest", "moves with constant speed", "accelerates", "moves vertically"],
        ["স্থির থাকে", "সমবেগে চলে", "ত্বরণসহ চলে", "উল্লম্বভাবে চলে"],
        "A", "medium", "application",
        "Limiting friction = μW = W/√3 ≈ 0.577 W > W/2, so the applied force cannot overcome friction; the particle stays at rest.",
        "সীমাবদ্ধ ঘর্ষণ W/√3 > W/2; বল অপর্যাপ্ত—কণা স্থির।",
    ),
    q(
        "If the normal reaction on a body is 50 N and μ = 0.4, the limiting friction is:",
        "অভিলম্ব প্রতিক্রিয়া 50 N এবং μ = 0.4 হলে সীমাবদ্ধ ঘর্ষণ কত?",
        ["10 N", "20 N", "40 N", "125 N"],
        ["10 N", "20 N", "40 N", "125 N"],
        "B", "easy", "numerical",
        "F = μR = 0.4 × 50 = 20 N.",
        "F = μR = 0.4 × 50 = 20 N।",
    ),
]


def write_topic(topic_id: str, rows: list[dict]) -> dict:
    clean = []
    for i, row in enumerate(rows, 1):
        err = validate_record(row)
        if err:
            raise SystemExit(f"{topic_id}#{i}: {err}")
        clean.append(row)
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
    counts["hm2_27_ch08_t01"] = write_topic("hm2_27_ch08_t01", T01)["count"]
    counts["hm2_27_ch08_t02"] = write_topic("hm2_27_ch08_t02", T02)["count"]
    counts["hm2_27_ch08_t03"] = write_topic("hm2_27_ch08_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm2_27_ch08",
        "title_en": "Statics",
        "title_bn": "স্থিতিবিদ্যা",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{i}_pdf{i+6}.png" for i in range(258, 269)],
        "topics": {
            "hm2_27_ch08_t01": {
                "title_en": "Forces and equilibrium",
                "title_bn": "বল ও সাম্যাবস্থা",
                "udvash_types": [
                    "resultant of two forces R²=P²+Q²+2PQ cos α",
                    "max/min resultant; equal forces; components",
                    "like/unlike parallel forces magnitudes",
                    "triangle law / Lami equilibrium of three forces",
                ],
                "count": 20,
            },
            "hm2_27_ch08_t02": {
                "title_en": "Moments and couples",
                "title_bn": "বলের ভ্রামক ও বলযুগল",
                "udvash_types": [
                    "moment = F × perpendicular distance; SI unit N·m",
                    "couples; Varignon; parallel-force position of resultant",
                    "interchange shift |P−Q|d/(P+Q); unlike external division",
                    "rod/beam equilibrium by moments; centroid of equal parallels",
                ],
                "count": 20,
            },
            "hm2_27_ch08_t03": {
                "title_en": "Friction",
                "title_bn": "ঘর্ষণ",
                "udvash_types": [
                    "μ=F/R; angle of friction λ with μ=tan λ; angle of repose",
                    "limiting vs kinetic friction; laws of dry friction",
                    "horizontal pull at angle; incline up/down limiting force",
                    "P,Q holding W on rough incline identity 1/P²+1/Q²=1/W²",
                ],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "garbled_stems": "Noisy OCR on pp. 258–268 reconstructed from answer-key algebra and standard board forms",
            "figure_only_items": "Figure-dependent stems rewritten as self-contained text MCQs",
            "broken_option_glyphs": "Fraction/√/degree glyphs often unreadable; replaced with closed-form HSC standards",
            "thin_friction_coverage": "Printed MCQs heavily forces/parallels; friction topic largely HSC-accurate authored supplements",
        },
        "low_confidence": [
            "OCR on pp. 258–266 noisy; column text and solution lines used to reconstruct force/parallel stems.",
            "Moments/couples and friction thinner in Udvash MCQ span; supplemented with accurate HSC statics items.",
            "Inline math stored as plain text (√, ⁻¹, μ, λ, N·m) for JSONL.",
            "A few stimulus/figure blocks curated as clear standalone stems.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm2_ch08.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
        "math2_progress": {
            "topics_complete": "24/30",
            "note": "Ch08 continues higher_mathematics 2nd paper after Ch01–Ch07 (420Q); remaining Ch09–Ch10",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch08_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
