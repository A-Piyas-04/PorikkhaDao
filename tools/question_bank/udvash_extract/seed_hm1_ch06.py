#!/usr/bin/env python3
"""Seed Higher Mathematics 1st Paper Ch6 (Trigonometric Ratios).

Curated from Udvash HSC Question Bank 2026 printed pp. 195–197 (PDF 201–203).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
Short chapter (~30 printed MCQs); supplements with accurate HSC-level authored items.
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
    "higher_mathematics p1 ch06; curated bilingual"
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
# hm1_27_ch06_t01 — Angle measure and trigonometric ratios
# =============================================================================
T01 = [
    q(
        "At 8:30, the angle between the hour hand and the minute hand is:",
        "৮টা ৩০ মিনিটে ঘণ্টার কাঁটা ও মিনিটের কাঁটার মধ্যবর্তী কোণ কত?",
        ["60 deg", "75 deg", "90 deg", "105 deg"],
        ["60 ডিগ্রি", "75 ডিগ্রি", "90 ডিগ্রি", "105 ডিগ্রি"],
        "B", "easy", "numerical",
        "theta = |(60H - 11M)/2| = |(480 - 330)/2| = 75 deg.",
        "theta = |(60H - 11M)/2| = |(480 - 330)/2| = 75 ডিগ্রি।",
    ),
    q(
        "A car wheel has radius 20 cm and rotates 10 times per second. Which statements are true? "
        "(i) circumference = 40 pi cm (ii) one turn covers about 125.66 cm "
        "(iii) linear speed is about 12.57 m/s",
        "একটি গাড়ির চাকার ব্যাসার্ধ ২০ সে.মি. এবং প্রতি সেকেন্ডে ১০ বার আবর্তিত হলে কোনগুলো সঠিক? "
        "(i) পরিধি ৪০π সে.মি. (ii) একবার ঘুরে প্রায় ১২৫.৬৬ সেমি (iii) গতিবেগ প্রায় ১২.৫৭ মি/সে",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii", "i, ii ও iii"],
        "D", "medium", "application",
        "C = 2 pi r = 40 pi ≈ 125.66 cm; speed = 10 × 1.2566 m/s ≈ 12.57 m/s. All three hold.",
        "C = 2πr = 40π ≈ 125.66 সেমি; গতি = 10 × 1.2566 ≈ 12.57 মি/সে। তিনটিই সঠিক।",
    ),
    q(
        "If cot theta = 12/5 and pi < theta < 3pi/2, then sin theta equals:",
        "cot theta = 12/5 এবং pi < theta < 3pi/2 হলে sin theta এর মান:",
        ["5/13", "-5/13", "12/13", "-12/13"],
        ["5/13", "-5/13", "12/13", "-12/13"],
        "B", "medium", "numerical",
        "csc^2 = 1 + cot^2 = 169/25 so |sin| = 5/13; third quadrant ⇒ sin theta = -5/13.",
        "csc^2 = 1 + cot^2 = 169/25 ⇒ |sin| = 5/13; তৃতীয় চতুর্ভাগে sin ঋণাত্মক ⇒ -5/13।",
    ),
    q(
        "If cot x = 5/4 and pi < x < 3pi/2, then sin x equals:",
        "cot x = 5/4 এবং pi < x < 3pi/2 হলে sin x এর মান:",
        ["-sqrt(41)/4", "sqrt(41)/4", "-4/sqrt(41)", "5/sqrt(41)"],
        ["-sqrt(41)/4", "sqrt(41)/4", "-4/sqrt(41)", "5/sqrt(41)"],
        "C", "medium", "numerical",
        "csc^2 x = 1 + (5/4)^2 = 41/16 ⇒ |sin x| = 4/sqrt(41); third quadrant ⇒ negative.",
        "csc^2 x = 1 + 25/16 = 41/16 ⇒ |sin x| = 4/sqrt(41); তৃতীয় চতুর্ভাগে ঋণাত্মক।",
    ),
    q(
        "If the three angles of a triangle are in the ratio 3 : 4 : 5, the angles are:",
        "একটি ত্রিভুজের তিনটি কোণের অনুপাত 3 : 4 : 5 হলে কোণ তিনটি:",
        ["30 deg, 40 deg, 50 deg", "40 deg, 60 deg, 80 deg",
         "45 deg, 60 deg, 75 deg", "50 deg, 60 deg, 75 deg"],
        ["30°, 40°, 50°", "40°, 60°, 80°", "45°, 60°, 75°", "50°, 60°, 75°"],
        "C", "easy", "numerical",
        "3x + 4x + 5x = 180° ⇒ x = 15° ⇒ angles 45°, 60°, 75°.",
        "3x + 4x + 5x = 180° ⇒ x = 15° ⇒ কোণ 45°, 60°, 75°।",
    ),
    q(
        "If sec theta = 13/12, then tan(pi/2 - theta) equals:",
        "sec theta = 13/12 হলে tan(pi/2 - theta) এর মান:",
        ["5/12", "5/13", "13/5", "12/5"],
        ["5/12", "5/13", "13/5", "12/5"],
        "D", "easy", "numerical",
        "tan(pi/2 - theta) = cot theta. With hyp 13, adj 12, opp 5 ⇒ cot = 12/5.",
        "tan(pi/2 - theta) = cot theta। অতিভুজ ১৩, সংলগ্ন ১২, বিপরীত ৫ ⇒ cot = 12/5।",
    ),
    q(
        "Area of a circular sector with radius 4 cm and central angle 30 deg is about:",
        "ব্যাসার্ধ ৪ সে.মি. ও কেন্দ্রীয় কোণ ৩০° বিশিষ্ট বৃত্তকলার ক্ষেত্রফল প্রায়:",
        ["1.05 sq cm", "2.09 sq cm", "4.19 sq cm", "8.38 sq cm"],
        ["1.05 বর্গ সেমি", "2.09 বর্গ সেমি", "4.19 বর্গ সেমি", "8.38 বর্গ সেমি"],
        "C", "medium", "numerical",
        "A = pi r^2 (theta/360) = pi × 16 × (30/360) = 4pi/3 ≈ 4.19 sq cm.",
        "A = πr^2 (θ/360) = π × 16 × 30/360 = 4π/3 ≈ 4.19 বর্গ সেমি।",
    ),
    q(
        "If cos theta = 12/13 and 0 < theta < pi/2, then tan theta equals:",
        "cos theta = 12/13 এবং 0 < theta < pi/2 হলে tan theta এর মান:",
        ["25/144", "5/12", "13/12", "12/5"],
        ["25/144", "5/12", "13/12", "12/5"],
        "B", "easy", "numerical",
        "opp = 5, adj = 12 ⇒ tan theta = 5/12.",
        "বিপরীত বাহু ৫, সংলগ্ন ১২ ⇒ tan theta = 5/12।",
    ),
    q(
        "If csc theta = 13/5 and pi/2 < theta < pi, then tan theta equals:",
        "csc theta = 13/5 এবং pi/2 < theta < pi হলে tan theta এর মান:",
        ["-12/13", "-5/12", "12/13", "13/12"],
        ["-12/13", "-5/12", "12/13", "13/12"],
        "B", "medium", "numerical",
        "sin = 5/13; second quadrant ⇒ cos = -12/13; tan = (5/13)/(-12/13) = -5/12.",
        "sin = 5/13; দ্বিতীয় চতুর্ভাগে cos = -12/13; tan = -5/12।",
    ),
    q(
        "In a circle of diameter AB = 6 cm, if central angle for arc BE is 30 deg, arc BE equals:",
        "ব্যাস AB = 6 সেমি বৃত্তে চাপ BE-এর কেন্দ্রীয় কোণ 30° হলে চাপ BE:",
        ["pi/2 cm", "3pi/2 cm", "pi cm", "2pi cm"],
        ["pi/2 সেমি", "3pi/2 সেমি", "pi সেমি", "2pi সেমি"],
        "A", "medium", "numerical",
        "r = 3 cm, theta = pi/6; s = r theta = 3 × pi/6 = pi/2 cm.",
        "r = 3 সেমি, θ = π/6; s = rθ = π/2 সেমি।",
    ),
    q(
        "A car wheel has radius 25 cm and rotates 10 times per second. Which are true? "
        "(i) circumference = 50 pi cm (ii) one turn ≈ 157 cm (iii) speed = 15.7 m/s",
        "চাকার ব্যাসার্ধ ২৫ সে.মি. ও প্রতি সেকেন্ডে ১০ বার আবর্তিত হলে কোনগুলো সঠিক? "
        "(i) পরিধি ৫০π সে.মি. (ii) একবার ≈ ১৫৭ সেমি (iii) গতিবেগ ১৫.৭ মি/সে",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii", "i, ii ও iii"],
        "D", "medium", "application",
        "C = 50 pi ≈ 157 cm; v = 10 × 1.57 m/s = 15.7 m/s. All three hold.",
        "C = 50π ≈ 157 সেমি; v = 15.7 মি/সে। তিনটিই সঠিক।",
    ),
    q(
        "If tan theta = 5/12 and cos theta is positive, then sin theta equals:",
        "tan theta = 5/12 এবং cos theta ধনাত্মক হলে sin theta এর মান:",
        ["-5/13", "5/13", "-12/13", "12/13"],
        ["-5/13", "5/13", "-12/13", "12/13"],
        "B", "easy", "numerical",
        "First quadrant: hyp = 13 ⇒ sin theta = 5/13.",
        "প্রথম চতুর্ভাগ: অতিভুজ ১৩ ⇒ sin theta = 5/13।",
    ),
    q(
        "If angle AOB = 30 deg and OA = 12 units, the length of arc AB is:",
        "angle AOB = 30° এবং OA = 12 একক হলে চাপ AB এর দৈর্ঘ্য:",
        ["pi", "2pi", "12pi", "24pi"],
        ["pi", "2pi", "12pi", "24pi"],
        "B", "easy", "numerical",
        "s = r theta = 12 × (pi/6) = 2pi.",
        "s = rθ = 12 × (π/6) = 2π।",
    ),
    q(
        "If pi/2 < theta < pi and sin theta = 3/5, then cos theta equals:",
        "pi/2 < theta < pi এবং sin theta = 3/5 হলে cos theta এর মান:",
        ["3/4", "4/5", "-3/4", "-4/5"],
        ["3/4", "4/5", "-3/4", "-4/5"],
        "D", "easy", "numerical",
        "adj = 4; second quadrant ⇒ cos theta = -4/5.",
        "সংলগ্ন বাহু ৪; দ্বিতীয় চতুর্ভাগে cos = -4/5।",
    ),
    q(
        "A sector has central angle pi/4 and the circle has diameter 12 cm. Its area is:",
        "বৃত্তকলার কেন্দ্রীয় কোণ pi/4 এবং বৃত্তের ব্যাস ১২ সে.মি. হলে ক্ষেত্রফল:",
        ["3pi/5", "9pi/2", "3pi/4", "3pi"],
        ["3pi/5", "9pi/2", "3pi/4", "3pi"],
        "B", "medium", "numerical",
        "r = 6; A = (1/2) r^2 theta = (1/2)×36×(pi/4) = 9pi/2.",
        "r = 6; A = (1/2)r^2 θ = 18 × (π/4) = 9π/2।",
    ),
    q(
        "60 degrees in radian measure equals:",
        "৬০ ডিগ্রির রেডিয়ান পরিমাপ:",
        ["pi/6", "pi/4", "pi/3", "pi/2"],
        ["pi/6", "pi/4", "pi/3", "pi/2"],
        "C", "easy", "factual",
        "theta_rad = (pi/180) × 60 = pi/3.",
        "θ_rad = (π/180) × 60 = π/3।",
    ),
    q(
        "pi/6 radians in degree measure equals:",
        "pi/6 রেডিয়ানের ডিগ্রি পরিমাপ:",
        ["15 deg", "30 deg", "45 deg", "60 deg"],
        ["15 ডিগ্রি", "30 ডিগ্রি", "45 ডিগ্রি", "60 ডিগ্রি"],
        "B", "easy", "factual",
        "(180/pi) × (pi/6) = 30 deg.",
        "(180/π) × (π/6) = 30 ডিগ্রি।",
    ),
    q(
        "If sin theta = 4/5 and theta is acute, then cos theta equals:",
        "sin theta = 4/5 এবং theta সূক্ষ্মকোণ হলে cos theta এর মান:",
        ["3/5", "4/5", "5/3", "5/4"],
        ["3/5", "4/5", "5/3", "5/4"],
        "A", "easy", "numerical",
        "cos^2 = 1 - 16/25 = 9/25 ⇒ cos = 3/5 (acute).",
        "cos^2 = 1 - 16/25 = 9/25 ⇒ cos = 3/5 (সূক্ষ্মকোণ)।",
    ),
    q(
        "The length of an arc of radius 6 cm subtending angle pi/3 at the center is:",
        "ব্যাসার্ধ ৬ সেমি ও কেন্দ্রে কোণ pi/3 হলে বৃত্তচাপের দৈর্ঘ্য:",
        ["pi cm", "2pi cm", "3pi cm", "6pi cm"],
        ["pi সেমি", "2pi সেমি", "3pi সেমি", "6pi সেমি"],
        "B", "easy", "numerical",
        "s = r theta = 6 × (pi/3) = 2pi cm.",
        "s = rθ = 6 × (π/3) = 2π সেমি।",
    ),
    q(
        "One full revolution equals how many radians?",
        "এক পূর্ণ আবর্তন কত রেডিয়ান?",
        ["pi/2", "pi", "2pi", "4pi"],
        ["pi/2", "pi", "2pi", "4pi"],
        "C", "easy", "factual",
        "A full circle is 360 deg = 2pi radians.",
        "এক পূর্ণ বৃত্ত ৩৬০° = ২π রেডিয়ান।",
    ),
]


# =============================================================================
# hm1_27_ch06_t02 — Trigonometric identities
# =============================================================================
T02 = [
    q(
        "If cot theta = 12/5, then tan 2theta equals:",
        "cot theta = 12/5 হলে tan 2theta এর মান:",
        ["120/119", "120/169", "60/119", "60/169"],
        ["120/119", "120/169", "60/119", "60/169"],
        "A", "medium", "numerical",
        "tan theta = 5/12; tan 2theta = 2t/(1-t^2) = (10/12)/(1-25/144) = 120/119.",
        "tan θ = 5/12; tan 2θ = 2t/(1-t^2) = 120/119।",
    ),
    q(
        "If tan beta = q/p, then cos 2beta equals:",
        "tan beta = q/p হলে cos 2beta এর মান:",
        ["2pq/(p^2 - q^2)", "2pq/(p^2 + q^2)", "(p^2 - q^2)/(p^2 + q^2)", "(p^2 + q^2)/(p^2 - q^2)"],
        ["2pq/(p^2 - q^2)", "2pq/(p^2 + q^2)", "(p^2 - q^2)/(p^2 + q^2)", "(p^2 + q^2)/(p^2 - q^2)"],
        "C", "medium", "conceptual",
        "cos 2beta = (1 - tan^2 beta)/(1 + tan^2 beta) = (p^2 - q^2)/(p^2 + q^2).",
        "cos 2β = (1 - tan^2 β)/(1 + tan^2 β) = (p^2 - q^2)/(p^2 + q^2)।",
    ),
    q(
        "If pi/2 < theta < pi and sin theta = 3/5, which claims hold? "
        "(i) cos theta = 2/5 (ii) tan^2 theta = 9/16 (iii) sec theta · tan theta = 15/16",
        "pi/2 < theta < pi এবং sin theta = 3/5 হলে কোনগুলো সঠিক? "
        "(i) cos theta = 2/5 (ii) tan^2 theta = 9/16 (iii) sec theta · tan theta = 15/16",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু ii ও iii", "শুধু i ও iii", "i, ii ও iii"],
        "B", "hard", "conceptual",
        "cos = -4/5 so (i) false; tan^2 = 9/16; sec·tan = (-5/4)(-3/4) = 15/16.",
        "cos = -4/5 ⇒ (i) মিথ্যা; tan^2 = 9/16; sec·tan = 15/16।",
    ),
    q(
        "cosec(270 deg + theta) equals:",
        "cosec(270° + theta) এর মান:",
        ["-cosec theta", "-sec theta", "cosec theta", "sec theta"],
        ["-cosec theta", "-sec theta", "cosec theta", "sec theta"],
        "B", "medium", "conceptual",
        "cosec(270° + theta) = 1/sin(270° + theta) = 1/(-cos theta) = -sec theta.",
        "cosec(270° + θ) = 1/sin(270° + θ) = 1/(-cos θ) = -sec θ।",
    ),
    q(
        "sin^4 x - cos^4 x equals:",
        "sin^4 x - cos^4 x এর সমান:",
        ["1 + sin^2 x", "2 cos^2 x + 1", "2 sin^2 x - 1", "2 cos^2 x - 1"],
        ["1 + sin^2 x", "2 cos^2 x + 1", "2 sin^2 x - 1", "2 cos^2 x - 1"],
        "C", "medium", "conceptual",
        "Difference of squares: (sin^2 - cos^2)(sin^2 + cos^2) = sin^2 - cos^2 = 2sin^2 x - 1.",
        "(sin^2 - cos^2)(sin^2 + cos^2) = sin^2 - cos^2 = 2sin^2 x - 1।",
    ),
    q(
        "The Pythagorean identity is:",
        "পাইথাগোরিয়ান অভেদ কোনটি?",
        ["sin^2 theta - cos^2 theta = 1", "sin^2 theta + cos^2 theta = 1",
         "sin theta + cos theta = 1", "tan^2 theta + cot^2 theta = 1"],
        ["sin^2 θ - cos^2 θ = 1", "sin^2 θ + cos^2 θ = 1",
         "sin θ + cos θ = 1", "tan^2 θ + cot^2 θ = 1"],
        "B", "easy", "factual",
        "By definition on the unit circle, sin^2 + cos^2 = 1.",
        "একক বৃত্তে সংজ্ঞা অনুসারে sin^2 + cos^2 = 1।",
    ),
    q(
        "1 + tan^2 theta equals:",
        "1 + tan^2 theta এর মান:",
        ["sin^2 theta", "cos^2 theta", "sec^2 theta", "csc^2 theta"],
        ["sin^2 θ", "cos^2 θ", "sec^2 θ", "csc^2 θ"],
        "C", "easy", "factual",
        "Divide sin^2 + cos^2 = 1 by cos^2 to get tan^2 + 1 = sec^2.",
        "sin^2 + cos^2 = 1 কে cos^2 দিয়ে ভাগ করলে 1 + tan^2 = sec^2।",
    ),
    q(
        "1 + cot^2 theta equals:",
        "1 + cot^2 theta এর মান:",
        ["sec^2 theta", "tan^2 theta", "cos^2 theta", "csc^2 theta"],
        ["sec^2 θ", "tan^2 θ", "cos^2 θ", "csc^2 θ"],
        "D", "easy", "factual",
        "Divide sin^2 + cos^2 = 1 by sin^2 to get 1 + cot^2 = csc^2.",
        "sin^2 + cos^2 = 1 কে sin^2 দিয়ে ভাগ করলে 1 + cot^2 = csc^2।",
    ),
    q(
        "sin 2theta equals:",
        "sin 2theta এর সমান:",
        ["sin^2 theta - cos^2 theta", "2 sin theta cos theta",
         "2 cos^2 theta - 1", "1 - 2 sin^2 theta"],
        ["sin^2 θ - cos^2 θ", "2 sin θ cos θ", "2 cos^2 θ - 1", "1 - 2 sin^2 θ"],
        "B", "easy", "factual",
        "Double-angle formula: sin 2theta = 2 sin theta cos theta.",
        "দ্বিগুণ কোণ সূত্র: sin 2θ = 2 sin θ cos θ।",
    ),
    q(
        "cos 2theta equals which of the following?",
        "cos 2theta নিচের কোনটির সমান?",
        ["2 sin theta cos theta", "cos^2 theta + sin^2 theta",
         "cos^2 theta - sin^2 theta", "2 tan theta / (1 - tan^2 theta)"],
        ["2 sin θ cos θ", "cos^2 θ + sin^2 θ", "cos^2 θ - sin^2 θ", "2 tan θ / (1 - tan^2 θ)"],
        "C", "easy", "factual",
        "Standard form: cos 2theta = cos^2 theta - sin^2 theta.",
        "প্রমাণিত রূপ: cos 2θ = cos^2 θ - sin^2 θ।",
    ),
    q(
        "Which is an equivalent form of cos 2theta?",
        "cos 2theta এর সমতুল্য রূপ কোনটি?",
        ["2 sin^2 theta - 1", "1 - 2 cos^2 theta", "2 cos^2 theta - 1", "sin^2 theta - cos^2 theta"],
        ["2 sin^2 θ - 1", "1 - 2 cos^2 θ", "2 cos^2 θ - 1", "sin^2 θ - cos^2 θ"],
        "C", "easy", "conceptual",
        "cos 2theta = 2 cos^2 theta - 1 = 1 - 2 sin^2 theta.",
        "cos 2θ = 2 cos^2 θ - 1 = 1 - 2 sin^2 θ।",
    ),
    q(
        "tan 2theta equals:",
        "tan 2theta এর সমান:",
        ["2 tan theta / (1 + tan^2 theta)", "2 tan theta / (1 - tan^2 theta)",
         "(1 - tan^2 theta) / (2 tan theta)", "tan^2 theta - 1"],
        ["2 tan θ / (1 + tan^2 θ)", "2 tan θ / (1 - tan^2 θ)",
         "(1 - tan^2 θ) / (2 tan θ)", "tan^2 θ - 1"],
        "B", "easy", "factual",
        "Double-angle formula: tan 2theta = 2 tan theta / (1 - tan^2 theta).",
        "দ্বিগুণ কোণ সূত্র: tan 2θ = 2 tan θ / (1 - tan^2 θ)।",
    ),
    q(
        "sin(90 deg - theta) equals:",
        "sin(90° - theta) এর মান:",
        ["sin theta", "cos theta", "-sin theta", "-cos theta"],
        ["sin θ", "cos θ", "-sin θ", "-cos θ"],
        "B", "easy", "factual",
        "Cofunction identity: sin(90° - theta) = cos theta.",
        "সহফলন অভেদ: sin(90° - θ) = cos θ।",
    ),
    q(
        "cos(90 deg - theta) equals:",
        "cos(90° - theta) এর মান:",
        ["cos theta", "sin theta", "-cos theta", "-sin theta"],
        ["cos θ", "sin θ", "-cos θ", "-sin θ"],
        "B", "easy", "factual",
        "Cofunction identity: cos(90° - theta) = sin theta.",
        "সহফলন অভেদ: cos(90° - θ) = sin θ।",
    ),
    q(
        "sec^2 theta - tan^2 theta equals:",
        "sec^2 theta - tan^2 theta এর মান:",
        ["0", "1", "2", "sec theta"],
        ["0", "1", "2", "sec θ"],
        "B", "easy", "conceptual",
        "From 1 + tan^2 = sec^2, rearrange to sec^2 - tan^2 = 1.",
        "1 + tan^2 = sec^2 হতে sec^2 - tan^2 = 1।",
    ),
    q(
        "sin(180 deg - theta) equals:",
        "sin(180° - theta) এর মান:",
        ["sin theta", "-sin theta", "cos theta", "-cos theta"],
        ["sin θ", "-sin θ", "cos θ", "-cos θ"],
        "A", "easy", "factual",
        "In the second quadrant, sine remains positive: sin(180° - theta) = sin theta.",
        "দ্বিতীয় চতুর্ভাগে সাইন ধনাত্মক: sin(180° - θ) = sin θ।",
    ),
    q(
        "cos(180 deg - theta) equals:",
        "cos(180° - theta) এর মান:",
        ["cos theta", "-cos theta", "sin theta", "-sin theta"],
        ["cos θ", "-cos θ", "sin θ", "-sin θ"],
        "B", "easy", "factual",
        "Cosine is negative in Q2: cos(180° - theta) = -cos theta.",
        "দ্বিতীয় চতুর্ভাগে কসাইন ঋণাত্মক: cos(180° - θ) = -cos θ।",
    ),
    q(
        "(sin theta + cos theta)^2 equals:",
        "(sin theta + cos theta)^2 এর সমান:",
        ["1 + sin 2theta", "1 - sin 2theta", "sin 2theta", "2 sin 2theta"],
        ["1 + sin 2θ", "1 - sin 2θ", "sin 2θ", "2 sin 2θ"],
        "A", "medium", "conceptual",
        "Expand: sin^2 + cos^2 + 2 sin cos = 1 + sin 2theta.",
        "প্রসারণ: sin^2 + cos^2 + 2 sin cos = 1 + sin 2θ।",
    ),
    q(
        "If sin theta + cos theta = 1, then sin theta · cos theta equals:",
        "sin theta + cos theta = 1 হলে sin theta · cos theta এর মান:",
        ["0", "1/2", "1", "-1/2"],
        ["0", "1/2", "1", "-1/2"],
        "A", "medium", "numerical",
        "Square both sides: 1 + 2 sin cos = 1 ⇒ sin cos = 0.",
        "বর্গ করলে: 1 + 2 sin cos = 1 ⇒ sin cos = 0।",
    ),
    q(
        "1 - 2 sin^2 theta equals:",
        "1 - 2 sin^2 theta এর সমান:",
        ["sin 2theta", "cos 2theta", "tan 2theta", "sec 2theta"],
        ["sin 2θ", "cos 2θ", "tan 2θ", "sec 2θ"],
        "B", "easy", "factual",
        "Alternate double-angle form: cos 2theta = 1 - 2 sin^2 theta.",
        "দ্বিগুণ কোণের বিকল্প রূপ: cos 2θ = 1 - 2 sin^2 θ।",
    ),
]


# =============================================================================
# hm1_27_ch06_t03 — Graphs of trigonometric functions
# =============================================================================
T03 = [
    q(
        "The period of cos(x/3 + pi/4) is:",
        "cos(x/3 + pi/4) এর পর্যায়:",
        ["6pi", "3pi", "pi/3", "pi/6"],
        ["6pi", "3pi", "pi/3", "pi/6"],
        "A", "easy", "numerical",
        "Period of cos(ax+b) is 2pi/|a| = 2pi/(1/3) = 6pi.",
        "cos(ax+b) এর পর্যায় 2π/|a| = 2π/(1/3) = 6π।",
    ),
    q(
        "The period of tan 2x is:",
        "tan 2x এর পর্যায়:",
        ["pi/2", "3pi/2", "pi", "2pi"],
        ["pi/2", "3pi/2", "pi", "2pi"],
        "A", "easy", "numerical",
        "Period of tan(ax) is pi/|a| = pi/2.",
        "tan(ax) এর পর্যায় π/|a| = π/2।",
    ),
    q(
        "The period of sin 2x is:",
        "sin 2x এর পর্যায়:",
        ["pi/2", "pi", "2pi", "4pi"],
        ["pi/2", "pi", "2pi", "4pi"],
        "B", "easy", "numerical",
        "Period of sin(ax) is 2pi/|a| = pi.",
        "sin(ax) এর পর্যায় 2π/|a| = π।",
    ),
    q(
        "The fundamental period of sec(x/4) is:",
        "sec(x/4) এর মৌলিক পর্যায়:",
        ["pi/2", "2pi", "4pi", "8pi"],
        ["pi/2", "2pi", "4pi", "8pi"],
        "D", "medium", "numerical",
        "Fundamental period of sec x is 2pi, so for sec(x/4) it is 2pi/(1/4) = 8pi.",
        "sec x এর মৌলিক পর্যায় 2π; sec(x/4) এর পর্যায় 8π।",
    ),
    q(
        "For y = sin(n pi + pi/6) with integer n, which are true? "
        "(i) it is periodic in n (ii) if n is even, y = 1/2 (iii) if n is odd, y = -1/2",
        "y = sin(nπ + π/6) এবং n পূর্ণসংখ্যা হলে কোনগুলো সঠিক? "
        "(i) n-এর সাপেক্ষে পর্যায়বৃত্ত (ii) n জোড় হলে y = 1/2 (iii) n বিজোড় হলে y = -1/2",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "Period 2 in n; even n ⇒ sin(pi/6)=1/2; odd n ⇒ sin(pi+pi/6)=-1/2. All three hold.",
        "n-এ পর্যায় ২; জোড়ে 1/2, বিজোড়ে -1/2। তিনটিই সঠিক।",
    ),
    q(
        "The range of tan x is:",
        "tan x এর রেঞ্জ:",
        ["(-1, 1)", "[-1, 1]", "(-infinity, infinity)", "[-infinity, infinity]"],
        ["(-1, 1)", "[-1, 1]", "(-অসীম, অসীম)", "[-অসীম, অসীম]"],
        "C", "easy", "factual",
        "As x → ±pi/2, tan x → ±infinity, so range is all real numbers (-∞, ∞).",
        "x → ±π/2 এ tan → ±∞; রেঞ্জ (−∞, ∞)।",
    ),
    q(
        "As theta increases from 0 deg to 90 deg, sin theta:",
        "theta কোণ ০° থেকে বেড়ে ৯০° হলে sin theta:",
        ["decreases from 1 to 0", "decreases from 0 to -1",
         "increases from -1 to 0", "increases from 0 to 1"],
        ["১ থেকে কমে ০ হয়", "০ থেকে কমে −১ হয়", "−১ থেকে বেড়ে ০ হয়", "০ থেকে বেড়ে ১ হয়"],
        "D", "easy", "factual",
        "On [0°, 90°], sine increases continuously from 0 to 1.",
        "[0°, 90°]-এ সাইন অবিচ্ছিন্নভাবে ০ থেকে ১ পর্যন্ত বৃদ্ধি পায়।",
    ),
    q(
        "Which statement correctly describes the graph of y = cos^2 x?",
        "y = cos^2 x এর লেখচিত্র সম্পর্কে কোন বক্তব্য সঠিক?",
        ["It takes negative values", "It oscillates between -1 and 1 like cos x",
         "It is always non-negative with period pi", "It is undefined at x = pi/2"],
        ["এটি ঋণাত্মক মান নেয়", "এটি cos x-এর মতো −১ থেকে ১ পর্যন্ত দোলে",
         "এটি সবসময় অঋণাত্মক এবং পর্যায় pi", "x = π/2 এ এটি অসংজ্ঞাত"],
        "C", "medium", "conceptual",
        "cos^2 x ≥ 0 for all x; cos^2(x+pi) = cos^2 x, so fundamental period is pi.",
        "cos^2 x ≥ 0; cos^2(x+π) = cos^2 x ⇒ মৌলিক পর্যায় π।",
    ),
    q(
        "cos^2(pi/2 + x) is identical to:",
        "cos^2(pi/2 + x) এর সমান:",
        ["cos^2 x", "sin^2 x", "-sin^2 x", "1 + sin^2 x"],
        ["cos^2 x", "sin^2 x", "-sin^2 x", "1 + sin^2 x"],
        "B", "medium", "conceptual",
        "cos(pi/2 + x) = -sin x ⇒ squared value is sin^2 x (≥ 0).",
        "cos(π/2 + x) = -sin x ⇒ বর্গ করলে sin^2 x (≥ 0)।",
    ),
    q(
        "For f(x) = -|sin x| on 0 ≤ x ≤ 2pi, which is true?",
        "f(x) = -|sin x|; 0 ≤ x ≤ 2pi হলে কোনটি সঠিক?",
        ["f(x) ≥ 0 everywhere", "f has range [-1, 0] with zeros at 0, pi, 2pi",
         "f has range [0, 1]", "f is positive between 0 and pi"],
        ["সর্বত্র f(x) ≥ 0", "রেঞ্জ [-1, 0] এবং শূন্য 0, π, 2π এ",
         "রেঞ্জ [0, 1]", "0 থেকে π পর্যন্ত f ধনাত্মক"],
        "B", "medium", "conceptual",
        "|sin x| ∈ [0,1] so -|sin x| ∈ [-1,0]; zeros where sin x = 0.",
        "|sin x| ∈ [0,1] ⇒ -|sin x| ∈ [-1,0]; sin = 0 এ শূন্য।",
    ),
    q(
        "The fundamental period of sin x is:",
        "sin x এর মৌলিক পর্যায়:",
        ["pi/2", "pi", "2pi", "4pi"],
        ["pi/2", "pi", "2pi", "4pi"],
        "C", "easy", "factual",
        "sin(x + 2pi) = sin x and 2pi is the smallest positive such number.",
        "sin(x + 2π) = sin x এবং 2π ক্ষুদ্রতম ধনাত্মক পর্যায়।",
    ),
    q(
        "The fundamental period of cos x is:",
        "cos x এর মৌলিক পর্যায়:",
        ["pi/2", "pi", "2pi", "3pi"],
        ["pi/2", "pi", "2pi", "3pi"],
        "C", "easy", "factual",
        "cos(x + 2pi) = cos x; fundamental period is 2pi.",
        "cos(x + 2π) = cos x; মৌলিক পর্যায় 2π।",
    ),
    q(
        "The fundamental period of tan x is:",
        "tan x এর মৌলিক পর্যায়:",
        ["pi/2", "pi", "2pi", "3pi/2"],
        ["pi/2", "pi", "2pi", "3pi/2"],
        "B", "easy", "factual",
        "tan(x + pi) = tan x; fundamental period is pi.",
        "tan(x + π) = tan x; মৌলিক পর্যায় π।",
    ),
    q(
        "The period of cos 3x is:",
        "cos 3x এর পর্যায়:",
        ["2pi/3", "pi/3", "2pi", "6pi"],
        ["2pi/3", "pi/3", "2pi", "6pi"],
        "A", "easy", "numerical",
        "Period = 2pi/|3| = 2pi/3.",
        "পর্যায় = 2π/|3| = 2π/3।",
    ),
    q(
        "The period of sin(x/2) is:",
        "sin(x/2) এর পর্যায়:",
        ["pi", "2pi", "4pi", "pi/2"],
        ["pi", "2pi", "4pi", "pi/2"],
        "C", "easy", "numerical",
        "Period = 2pi/|1/2| = 4pi.",
        "পর্যায় = 2π/(1/2) = 4π।",
    ),
    q(
        "The range of sin x is:",
        "sin x এর রেঞ্জ:",
        ["(-infinity, infinity)", "[0, 1]", "[-1, 1]", "(0, 1)"],
        ["(-অসীম, অসীম)", "[0, 1]", "[-1, 1]", "(0, 1)"],
        "C", "easy", "factual",
        "Sine attains every value in [-1, 1] and no others.",
        "সাইন শুধুমাত্র [-1, 1]-এর মান নেয়।",
    ),
    q(
        "The range of cos x is:",
        "cos x এর রেঞ্জ:",
        ["[0, 1]", "[-1, 1]", "(-1, 1)", "(-infinity, infinity)"],
        ["[0, 1]", "[-1, 1]", "(-1, 1)", "(-অসীম, অসীম)"],
        "B", "easy", "factual",
        "Cosine also has range [-1, 1].",
        "কসাইনের রেঞ্জও [-1, 1]।",
    ),
    q(
        "The amplitude of y = 3 sin x is:",
        "y = 3 sin x এর প্রশস্ততা:",
        ["1", "2", "3", "6"],
        ["1", "2", "3", "6"],
        "C", "easy", "factual",
        "For y = A sin x, amplitude is |A| = 3.",
        "y = A sin x হলে প্রশস্ততা |A| = 3।",
    ),
    q(
        "The range of y = sin x + 2 is:",
        "y = sin x + 2 এর রেঞ্জ:",
        ["[-1, 1]", "[1, 3]", "[0, 2]", "[2, 4]"],
        ["[-1, 1]", "[1, 3]", "[0, 2]", "[2, 4]"],
        "B", "easy", "conceptual",
        "sin x ∈ [-1, 1] ⇒ sin x + 2 ∈ [1, 3].",
        "sin x ∈ [-1, 1] ⇒ sin x + 2 ∈ [1, 3]।",
    ),
    q(
        "Which statement about sin x and cos x is correct?",
        "sin x ও cos x সম্পর্কে কোনটি সঠিক?",
        ["sin x is even and cos x is odd", "both are even",
         "sin x is odd and cos x is even", "both are odd"],
        ["sin x যুগ্ম ও cos x অযুগ্ম", "উভয়ই যুগ্ম",
         "sin x অযুগ্ম ও cos x যুগ্ম", "উভয়ই অযুগ্ম"],
        "C", "easy", "conceptual",
        "sin(-x) = -sin x (odd); cos(-x) = cos x (even).",
        "sin(-x) = -sin x (অযুগ্ম); cos(-x) = cos x (যুগ্ম)।",
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
    counts["hm1_27_ch06_t01"] = write_topic("hm1_27_ch06_t01", T01)["count"]
    counts["hm1_27_ch06_t02"] = write_topic("hm1_27_ch06_t02", T02)["count"]
    counts["hm1_27_ch06_t03"] = write_topic("hm1_27_ch06_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm1_27_ch06",
        "title_en": "Trigonometric Ratios",
        "title_bn": "ত্রিকোণমিতিক অনুপাত",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(195, 198)],
        "topics": {
            "hm1_27_ch06_t01": {
                "title_en": "Angle measure and trigonometric ratios",
                "title_bn": "কোণ পরিমাপ ও ত্রিকোণমিতিক অনুপাত",
                "udvash_types": ["T-01", "T-02", "clock angles", "sectors", "quadrant ratios"],
                "count": 20,
            },
            "hm1_27_ch06_t02": {
                "title_en": "Trigonometric identities",
                "title_bn": "ত্রিকোণমিতিক অভেদ",
                "udvash_types": ["T-02", "double-angle", "Pythagorean", "cofunction"],
                "count": 20,
            },
            "hm1_27_ch06_t03": {
                "title_en": "Graphs of trigonometric functions",
                "title_bn": "ত্রিকোণমিতিক ফাংশনের লেখচিত্র",
                "udvash_types": ["T-03", "T-04", "period", "range", "amplitude", "parity"],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "Q17_graph_cos2x": "Figure-only options; rewritten as text property of y=cos^2 x",
            "Q25_graph_cos2_shift": "Figure-only options; rewritten as cos^2(pi/2+x)=sin^2 x",
            "Q27_graph_neg_abs_sin": "Figure-only options; rewritten as range/zeros of -|sin x|",
            "Q16_printed_key_b": "Printed key listed b (i,iii) but all three statements are true; curated as D",
        },
        "low_confidence": [
            "OCR on pp. 195–197 heavily noisy; column PNGs used to reconstruct stems/keys.",
            "Only ~30 printed MCQs; remaining items authored as accurate HSC-level bilingual supplements.",
            "Inline math stored as plain text (pi, deg, ^, sin/cos/tan) for JSONL.",
            "cosec(270+theta) kept in identities topic though also related to associated angles (ch07).",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm1_ch06.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch06_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
