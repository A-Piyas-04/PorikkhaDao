#!/usr/bin/env python3
"""Seed Physics 1st Paper Ch3 (Dynamics) bilingual MCQs.

Curated from Udvash HSC Question Bank 2026 printed pages 83–89 (OCR + HSC reconstruction).
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
    "physics p1 ch03; curated bilingual"
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
# t01 Displacement, velocity and acceleration
# ---------------------------------------------------------------------------
T01 = [
    q(
        "Which quantity is the shortest directed distance from initial to final position?",
        "আদি অবস্থান থেকে শেষ অবস্থানের ক্ষুদ্রতম দিকনির্দেশক দূরত্ব কোন রাশি?",
        ["Distance", "Displacement", "Speed", "Path length"],
        ["দূরত্ব", "সরণ", "দ্রুতি", "পথের দৈর্ঘ্য"],
        "B", "easy", "factual",
        "Displacement is the shortest directed distance between two positions.",
        "সরণ হলো দুই অবস্থানের মধ্যবর্তী ক্ষুদ্রতম দিকনির্দেশক দূরত্ব।",
    ),
    q(
        "Average velocity equals:",
        "গড় বেগ সমান:",
        ["Total path length / time", "Displacement / time", "Speed / time", "Acceleration × time"],
        ["মোট পথদৈর্ঘ্য / সময়", "সরণ / সময়", "দ্রুতি / সময়", "ত্বরণ × সময়"],
        "B", "easy", "factual",
        "Average velocity = net displacement divided by total time.",
        "গড় বেগ = মোট সরণ ÷ মোট সময়।",
    ),
    q(
        "Instantaneous velocity is the limit of Δs/Δt as Δt approaches:",
        "তাৎক্ষণিক বেগ হলো Δs/Δt-এর সীমা যখন Δt যায়:",
        ["Infinity", "Zero", "One", "Displacement"],
        ["অসীমের দিকে", "শূন্যের দিকে", "একের দিকে", "সরণের দিকে"],
        "B", "easy", "conceptual",
        "v = lim(Δt→0) Δs/Δt = ds/dt.",
        "v = lim(Δt→0) Δs/Δt = ds/dt।",
    ),
    q(
        "A particle has velocity v = (6t² + 3) m s⁻¹. Its displacement in the first 3 s is:",
        "একটি বস্তুর বেগ v = (6t² + 3) m s⁻¹। প্রথম ৩ সেকেন্ডে সরণ কত?",
        ["90 m", "67.5 m", "63 m", "27 m"],
        ["90 m", "67.5 m", "63 m", "27 m"],
        "C", "medium", "numerical",
        "s = ∫₀³ (6t² + 3) dt = [2t³ + 3t]₀³ = 54 + 9 = 63 m.",
        "s = ∫₀³ (6t² + 3) dt = [2t³ + 3t]₀³ = 63 m।",
    ),
    q(
        "A body falls freely from 40 m height (g = 9.8 m s⁻²). Impact speed is approximately:",
        "৪০ m উঁচু থেকে মুক্তভাবে পতিত বস্তুর ভূমিতে পতন বেগ প্রায় (g = 9.8 m s⁻²):",
        ["14 m s⁻¹", "28 m s⁻¹", "39.2 m s⁻¹", "78.4 m s⁻¹"],
        ["14 m s⁻¹", "28 m s⁻¹", "39.2 m s⁻¹", "78.4 m s⁻¹"],
        "B", "medium", "numerical",
        "v² = u² + 2gh = 2×9.8×40 ⇒ v = √784 = 28 m s⁻¹.",
        "v² = 2gh = 2×9.8×40 ⇒ v = 28 m s⁻¹।",
    ),
    q(
        "Dimensions of angular acceleration are:",
        "কৌণিক ত্বরণের মাত্রা কোনটি?",
        ["[M⁰L⁰T⁻²]", "[M⁰LT⁻¹]", "[M⁰L⁰T⁻¹]", "[M⁻¹LT⁻²]"],
        ["[M⁰L⁰T⁻²]", "[M⁰LT⁻¹]", "[M⁰L⁰T⁻¹]", "[M⁻¹LT⁻²]"],
        "A", "easy", "factual",
        "Angular acceleration α = dω/dt has dimensions T⁻².",
        "কৌণিক ত্বরণ α = dω/dt; মাত্রা T⁻²।",
    ),
    q(
        "The correct relation between linear velocity v and angular velocity ω is:",
        "রৈখিক বেগ v ও কৌণিক বেগ ω-এর সঠিক সম্পর্ক:",
        ["ω = v × r", "v = ω − r", "ω = v · r", "v = ω × r"],
        ["ω = v × r", "v = ω − r", "ω = v · r", "v = ω × r"],
        "D", "easy", "factual",
        "In vector form, v = ω × r.",
        "ভেক্টর আকারে v = ω × r।",
    ),
    q(
        "A fan rotates at 30 revolutions per minute. Its angular speed is:",
        "একটি পাখা প্রতি মিনিটে ৩০ বার ঘুরছে। এর কৌণিক বেগ কত?",
        ["π rad s⁻¹", "2π rad s⁻¹", "π/2 rad s⁻¹", "60π rad s⁻¹"],
        ["π rad s⁻¹", "2π rad s⁻¹", "π/2 rad s⁻¹", "60π rad s⁻¹"],
        "A", "medium", "numerical",
        "ω = 30 × (2π/60) = π rad s⁻¹.",
        "ω = 30 × (2π/60) = π rad s⁻¹।",
    ),
    q(
        "A clock minute-hand has length 0.01 m. Speed of its tip is about:",
        "০.০১ m দৈর্ঘ্যের ঘড়ির মিনিট কাঁটার প্রান্তবিন্দুর রৈখিক বেগ প্রায়:",
        ["1.54 × 10⁻⁵ m s⁻¹", "1.64 × 10⁻⁵ m s⁻¹", "1.74 × 10⁻⁵ m s⁻¹", "1.84 × 10⁻⁵ m s⁻¹"],
        ["1.54 × 10⁻⁵ m s⁻¹", "1.64 × 10⁻⁵ m s⁻¹", "1.74 × 10⁻⁵ m s⁻¹", "1.84 × 10⁻⁵ m s⁻¹"],
        "C", "hard", "numerical",
        "ω = 2π/(3600) rad s⁻¹; v = ωr ≈ 1.74 × 10⁻⁵ m s⁻¹.",
        "ω = 2π/3600; v = ωr ≈ 1.74 × 10⁻⁵ m s⁻¹।",
    ),
    q(
        "If the length of a clock’s minute hand decreases, then:",
        "ঘড়ির মিনিট কাঁটার দৈর্ঘ্য কমলে:",
        ["Linear speed increases, angular speed increases", "Both linear and angular speeds decrease", "Linear speed fixed, angular speed increases", "Linear speed decreases, angular speed stays the same"],
        ["রৈখিক বেগ বাড়ে, কৌণিক বেগ বাড়ে", "রৈখিক ও কৌণিক বেগ দুটোই কমে", "রৈখিক বেগ স্থির, কৌণিক বেগ বাড়ে", "রৈখিক বেগ কমে, কৌণিক বেগ অপরিবর্তিত"],
        "D", "medium", "conceptual",
        "Period is fixed so ω is fixed; v = ωr decreases if r decreases.",
        "পর্যায়কাল স্থির বলে ω স্থির; r কমলে v = ωr কমে।",
    ),
    q(
        "Earth’s spin angular speed about its axis is approximately:",
        "পৃথিবীর নিজ অক্ষে ঘূর্ণনের কৌণিক বেগ প্রায়:",
        ["1.99 × 10⁻⁷ rad s⁻¹", "7.26 × 10⁻⁵ deg s⁻¹", "4.167 × 10⁻³ deg s⁻¹", "4.167 × 10⁻³ rad s⁻¹"],
        ["1.99 × 10⁻⁷ rad s⁻¹", "7.26 × 10⁻⁵ deg s⁻¹", "4.167 × 10⁻³ deg s⁻¹", "4.167 × 10⁻³ rad s⁻¹"],
        "C", "hard", "numerical",
        "ω = 360°/86400 s ≈ 4.167 × 10⁻³ deg s⁻¹ (≈ 7.27 × 10⁻⁵ rad s⁻¹).",
        "ω = 360°/86400 ≈ 4.167 × 10⁻³ deg s⁻¹।",
    ),
    q(
        "For uniform circular motion, which statements are true? (i) constant angular speed (ii) tangential acceleration is zero (iii) no centripetal acceleration",
        "সুষম বৃত্তাকার গতিতে: (i) সমকৌণিক বেগ (ii) স্পর্শকীয় ত্বরণ শূন্য (iii) কেন্দ্রমুখী ত্বরণ নেই — কোনটি সঠিক?",
        ["i, ii", "ii, iii", "i, iii", "i, ii, iii"],
        ["i, ii", "ii, iii", "i, iii", "i, ii, iii"],
        "A", "medium", "conceptual",
        "Speed magnitude is constant so α_tangential = 0, but centripetal acceleration ω²r ≠ 0.",
        "মান স্থির বলে স্পর্শকীয় ত্বরণ শূন্য; কেন্দ্রমুখী ত্বরণ থাকে।",
    ),
    q(
        "A particle moves with constant angular speed on a circle. Its linear velocity:",
        "বৃত্তপথে সমকৌণিক বেগে চলমান কণার রৈখিক বেগ:",
        ["Changes only in magnitude", "Remains constant as a vector", "Changes only in direction", "Changes in both magnitude and direction"],
        ["শুধু মান পরিবর্তিত হয়", "ভেক্টর হিসেবে ধ্রুবক", "শুধু দিক পরিবর্তিত হয়", "মান ও দিক উভয়ই পরিবর্তিত হয়"],
        "C", "easy", "conceptual",
        "Magnitude v = ωr is fixed; direction is always tangential and changing.",
        "মান স্থির; দিক সবসময় পরিবর্তনশীল।",
    ),
    q(
        "Acceleration is the time rate of change of:",
        "ত্বরণ হলো কোন রাশির সময়ের সাপেক্ষে পরিবর্তনের হার?",
        ["Displacement", "Distance", "Velocity", "Force"],
        ["সরণ", "দূরত্ব", "বেগ", "বল"],
        "C", "easy", "factual",
        "a = dv/dt by definition.",
        "সংজ্ঞা অনুসারে a = dv/dt।",
    ),
    q(
        "A wheel spinning at 20 rev/s stops in 20 s. Magnitude of angular acceleration is:",
        "প্রতি সেকেন্ডে ২০ বার ঘূর্ণায়মান চাকা ২০ s-এ থামলে কৌণিক ত্বরণের মান:",
        ["π rad s⁻²", "2π rad s⁻²", "4π rad s⁻²", "8π rad s⁻²"],
        ["π rad s⁻²", "2π rad s⁻²", "4π rad s⁻²", "8π rad s⁻²"],
        "B", "medium", "numerical",
        "ω₀ = 40π rad s⁻¹; α = (0 − 40π)/20 = −2π rad s⁻²; |α| = 2π rad s⁻².",
        "ω₀ = 40π; |α| = 40π/20 = 2π rad s⁻²।",
    ),
    q(
        "Angular frequency is measured in which SI unit?",
        "কৌণিক কম্পাঙ্ক কোন SI এককে পরিমাপ করা হয়?",
        ["rad s⁻¹", "m s⁻¹", "Hz only", "N m"],
        ["rad s⁻¹", "m s⁻¹", "শুধু Hz", "N m"],
        "A", "easy", "factual",
        "Angular frequency ω has SI unit rad s⁻¹ (or s⁻¹).",
        "কৌণিক কম্পাঙ্কের SI একক rad s⁻¹।",
    ),
    q(
        "Velocity of a particle is V(t) = (6t² + 2t) m s⁻¹. Displacement in 2 s from rest origin is:",
        "বেগ V(t) = (6t² + 2t) m s⁻¹ হলে ২ s-এ সরণ (আদি অবস্থান শূন্য):",
        ["20 m", "26 m", "28 m", "56 m"],
        ["20 m", "26 m", "28 m", "56 m"],
        "A", "medium", "numerical",
        "s = ∫₀² (6t² + 2t) dt = [2t³ + t²]₀² = 16 + 4 = 20 m.",
        "s = ∫₀² (6t² + 2t) dt = 20 m।",
    ),
    q(
        "1 rpm equals:",
        "1 rpm সমান:",
        ["π/30 rad s⁻¹", "π/60 rad s⁻¹", "2π rad s⁻¹", "π/180 rad s⁻¹"],
        ["π/30 rad s⁻¹", "π/60 rad s⁻¹", "2π rad s⁻¹", "π/180 rad s⁻¹"],
        "A", "easy", "factual",
        "1 rev/min = 2π/60 = π/30 rad s⁻¹.",
        "1 rpm = 2π/60 = π/30 rad s⁻¹।",
    ),
    q(
        "Which is an example of oscillatory motion?",
        "নিচের কোনটি দোলন গতির উদাহরণ?",
        ["Motion of clock hands", "Earth around the Sun", "Electric fan blades", "Motion of a tuning fork prong"],
        ["ঘড়ির কাঁটার গতি", "সূর্যের চারদিকে পৃথিবী", "বৈদ্যুতিক পাখার গতি", "সুরশলাকার গতি"],
        "D", "easy", "factual",
        "A tuning fork prong oscillates about equilibrium; the others are rotational/orbital.",
        "সুরশলাকা সাম্যাবস্থার দুই পাশে দোলে।",
    ),
    q(
        "Position of a particle is x = At + Bt² with A = 2.0, B = −1.0 (SI). Average velocity from t = 0 to t = 5 s is:",
        "x = At + Bt² (A = 2.0, B = −1.0)। t = 0 থেকে 5 s পর্যন্ত গড় বেগ:",
        ["4.2 units", "4.0 units", "3.5 units", "−3.0 units"],
        ["4.2 একক", "4.0 একক", "3.5 একক", "−3.0 একক"],
        "D", "hard", "numerical",
        "x(5) − x(0) = (10 − 25) − 0 = −15; ⟨v⟩ = −15/5 = −3 units.",
        "Δx = −15; গড় বেগ = −15/5 = −3 একক।",
    ),
]

# ---------------------------------------------------------------------------
# t02 Equations and graphs of motion
# ---------------------------------------------------------------------------
T02 = [
    q(
        "A car starts from rest with acceleration 2 m s⁻². Distance covered in 2 s is:",
        "একটি গাড়ি স্থির অবস্থা থেকে 2 m s⁻² ত্বরণে চলতে শুরু করে। ২ s-এ অতিক্রান্ত দূরত্ব:",
        ["1 m", "2 m", "4 m", "8 m"],
        ["1 m", "2 m", "4 m", "8 m"],
        "C", "easy", "numerical",
        "s = ut + ½at² = 0 + ½×2×4 = 4 m.",
        "s = ½at² = ½×2×2² = 4 m।",
    ),
    q(
        "From rest with constant a, distance in 4 s compared with distance in 2 s is:",
        "স্থির থেকে সমত্বরণে, ৪ s-এ অতিক্রান্ত দূরত্ব ২ s-এর দূরত্বের কত গুণ?",
        ["16 times", "8 times", "4 times", "2 times"],
        ["১৬ গুণ", "৮ গুণ", "৪ গুণ", "২ গুণ"],
        "C", "medium", "numerical",
        "s ∝ t² ⇒ s₄/s₂ = 16/4 = 4.",
        "s ∝ t² বলে অনুপাত ১৬/৪ = ৪।",
    ),
    q(
        "Which equation of motion is correct for constant acceleration?",
        "সমত্বরণের জন্য কোন সমীকরণটি সঠিক?",
        ["v = u + at", "v = u − a/t", "s = ut − ½a", "v² = u² − 2as only always"],
        ["v = u + at", "v = u − a/t", "s = ut − ½a", "v² = u² − 2as সবসময়ই"],
        "A", "easy", "factual",
        "The standard first equation is v = u + at.",
        "প্রথম সমীকরণ v = u + at।",
    ),
    q(
        "On a velocity–time graph, the area under the curve represents:",
        "বেগ–সময় লেখচিত্রে বক্ররেখার নিচের ক্ষেত্রফল নির্দেশ করে:",
        ["Acceleration", "Displacement (or distance if signed carefully)", "Jerk", "Force"],
        ["ত্বরণ", "সরণ (বা চিহ্নসহ দূরত্ব)", "ঝাঁকুনি", "বল"],
        "B", "easy", "conceptual",
        "∫v dt equals change in position (displacement).",
        "∫v dt = সরণ।",
    ),
    q(
        "Slope of a velocity–time graph gives:",
        "বেগ–সময় লেখচিত্রের ঢাল দেয়:",
        ["Displacement", "Speed", "Acceleration", "Momentum"],
        ["সরণ", "দ্রুতি", "ত্বরণ", "ভরবেগ"],
        "C", "easy", "factual",
        "a = dv/dt is the slope of the v–t graph.",
        "a = dv/dt = v–t লেখের ঢাল।",
    ),
    q(
        "Slope of a position–time graph gives:",
        "অবস্থান–সময় লেখচিত্রের ঢাল দেয়:",
        ["Acceleration", "Velocity", "Force", "Energy"],
        ["ত্বরণ", "বেগ", "বল", "শক্তি"],
        "B", "easy", "factual",
        "v = ds/dt is the slope of the s–t graph.",
        "v = ds/dt = s–t লেখের ঢাল।",
    ),
    q(
        "A body starts from rest and covers 1 m in the first second under constant acceleration. Time needed to cover the next 1 m (to reach 2 m) is about:",
        "স্থির থেকে সমত্বরণে প্রথম সেকেন্ডে 1 m যায়। পরবর্তী 1 m (মোট 2 m) যেতে প্রায় কত সময় লাগে?",
        ["0.41 s", "1.0 s", "1.41 s", "2.0 s"],
        ["0.41 s", "1.0 s", "1.41 s", "2.0 s"],
        "A", "hard", "numerical",
        "From s = ½at² with a = 2 m s⁻²: t(1 m) = 1 s, t(2 m) = √2 s ⇒ Δt = √2 − 1 ≈ 0.41 s.",
        "a = 2; t₂ − t₁ = √2 − 1 ≈ 0.41 s।",
    ),
    q(
        "Equation s = ½at² (u = 0) is represented by which s–t graph shape?",
        "s = ½at² (u = 0) সমীকরণ কোন আকৃতির s–t লেখ নির্দেশ করে?",
        ["Straight line through origin", "Parabola opening upward from origin", "Horizontal line", "Straight line with negative slope"],
        ["মূলবিন্দুগামী সরলরেখা", "মূলবিন্দু থেকে ঊর্ধ্বমুখী পরাবৃত্ত", "অনুভূমিক রেখা", "ঋণাত্মক ঢালের সরলরেখা"],
        "B", "medium", "conceptual",
        "s ∝ t² is a parabola starting at the origin.",
        "s ∝ t² বলে মূলবিন্দু থেকে পরাবৃত্তাকার লেখ।",
    ),
    q(
        "On an s–t graph: OP rising linearly, PQ flat, QR falling linearly. Which is correct? (i) velocity constant on OP (ii) velocity zero on PQ (iii) velocity constant (negative) on QR",
        "s–t লেখে OP সরল ঊর্ধ্ব, PQ সমতল, QR সরল নিম্ন: (i) OP-তে বেগ ধ্রুব (ii) PQ-তে বেগ শূন্য (iii) QR-তে বেগ ধ্রুব ঋণাত্মক — সঠিক?",
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        "D", "medium", "conceptual",
        "Constant slope ⇒ constant velocity; zero slope ⇒ zero velocity.",
        "ধ্রুব ঢাল = ধ্রুব বেগ; শূন্য ঢাল = শূন্য বেগ।",
    ),
    q(
        "Which s–t graph is physically impossible for a real particle?",
        "বাস্তব কণার জন্য কোন s–t লেখ অসম্ভব?",
        ["Smooth curve with finite slope", "A sudden finite jump in s at one instant of time", "Parabolic arc", "Piecewise linear continuous path"],
        ["সসীম ঢালের মসৃণ বক্র", "এক মুহূর্তে s-এর হঠাৎ সসীম লাফ", "পরাবৃত্ত চাপ", "টুকরো টুকরো রৈখিক অবিচ্ছিন্ন পথ"],
        "B", "medium", "conceptual",
        "Finite displacement in zero time would require infinite speed.",
        "শূন্য সময়ে সসীম সরণ মানে অসীম বেগ — অসম্ভব।",
    ),
    q(
        "A particle’s velocity equation is v = 10 + 4t (SI). Acceleration at t = 6 s is:",
        "v = 10 + 4t হলে t = 6 s-এ ত্বরণ:",
        ["34 m s⁻²", "4 m s⁻²", "24 m s⁻¹", "14 m s⁻²"],
        ["34 m s⁻²", "4 m s⁻²", "24 m s⁻¹", "14 m s⁻²"],
        "B", "easy", "numerical",
        "a = dv/dt = 4 m s⁻² (constant).",
        "a = dv/dt = 4 m s⁻²।",
    ),
    q(
        "A stone is dropped from a 100 m building (g = 9.8 m s⁻²). Time to hit ground is about:",
        "১০০ m উঁচু ভবন থেকে পাথর ছাড়লে ভূমিতে পড়তে প্রায় কত সময় (g = 9.8)?",
        ["3.2 s", "4.5 s", "10.2 s", "20.4 s"],
        ["3.2 s", "4.5 s", "10.2 s", "20.4 s"],
        "B", "medium", "numerical",
        "h = ½gt² ⇒ t = √(2h/g) = √(200/9.8) ≈ 4.5 s.",
        "t = √(2×100/9.8) ≈ 4.5 s।",
    ),
    q(
        "From rest under constant a, ratio of distances in the 4th and 3rd seconds is:",
        "স্থির থেকে সমত্বরণে চতুর্থ ও তৃতীয় সেকেন্ডে অতিক্রান্ত দূরত্বের অনুপাত:",
        ["7:5", "4:3", "16:9", "2:1"],
        ["7:5", "4:3", "16:9", "2:1"],
        "A", "medium", "numerical",
        "s_n = u + a(2n−1)/2; with u=0, s₄:s₃ = 7:5.",
        "s_n ∝ (2n−1) ⇒ ৭:৫।",
    ),
    q(
        "Water drops fall every equal interval from a 45 m pipe (g = 10). When the 1st hits ground the 4th is just leaving. Height of the 3rd drop above ground then is:",
        "৪৫ m নল থেকে সমান ব্যবধানে ফোঁটা পড়ে (g = 10)। ১ম ফোঁটা পড়ার মুহূর্তে ৪র্থ ছেড়েছে। তখন ৩য় ফোঁটার উচ্চতা:",
        ["5 m", "15 m", "20 m", "40 m"],
        ["5 m", "15 m", "20 m", "40 m"],
        "D", "hard", "numerical",
        "t₁ = √(2h/g) = 3 s; interval = 1 s. 3rd has fallen 1 s: y = 5 m down ⇒ height = 40 m.",
        "t = 3 s; ৩য় ফোঁটা ১ s পড়েছে → নিচে 5 m → উচ্চতা 40 m।",
    ),
    q(
        "In the water-drop problem above, ratio of speeds of 3rd to 2nd drop when the 1st hits is:",
        "উপরের ফোঁটা সমস্যায় ১ম পড়ার মুহূর্তে ৩য় ও ২য় ফোঁটার বেগের অনুপাত:",
        ["4:1", "2:1", "1:2", "1:4"],
        ["4:1", "2:1", "1:2", "1:4"],
        "C", "hard", "numerical",
        "Ages: 2nd has fallen 2 s, 3rd 1 s; v ∝ t ⇒ v₃:v₂ = 1:2.",
        "v ∝ t বলে ১:২।",
    ),
    q(
        "A particle moves on a semicircle of radius 2 m from one end to the other in 2 s. Average velocity magnitude is:",
        "ব্যাসার্ধ 2 m অর্ধবৃত্তে এক প্রান্ত থেকে অন্য প্রান্তে 2 s-এ গড় বেগের মান:",
        ["1 m s⁻¹", "π m s⁻¹", "2 m s⁻¹", "π/2 m s⁻¹"],
        ["1 m s⁻¹", "π m s⁻¹", "2 m s⁻¹", "π/2 m s⁻¹"],
        "C", "medium", "numerical",
        "Displacement = diameter = 4 m; ⟨v⟩ = 4/2 = 2 m s⁻¹.",
        "সরণ = ব্যাস 4 m; গড় বেগ = 2 m s⁻¹।",
    ),
    q(
        "A body projected vertically upward with speed u reaches maximum height:",
        "আদিবেগ u দিয়ে খাড়া উপরে নিক্ষিপ্ত বস্তুর সর্বোচ্চ উচ্চতা:",
        ["u²/g", "u²/(2g)", "2u²/g", "u/g"],
        ["u²/g", "u²/(2g)", "2u²/g", "u/g"],
        "B", "easy", "factual",
        "From v² = u² − 2gH with v = 0: H = u²/(2g).",
        "H = u²/(2g)।",
    ),
    q(
        "On a v–t graph, segment CD goes from v = 20 m s⁻¹ to v = 10 m s⁻¹ in 5 s. Acceleration on CD is:",
        "v–t লেখে CD অংশে 5 s-এ বেগ 20 থেকে 10 m s⁻¹ হলে ত্বরণ:",
        ["2.0 m s⁻²", "0.5 m s⁻²", "−0.5 m s⁻²", "−2.0 m s⁻²"],
        ["2.0 m s⁻²", "0.5 m s⁻²", "−0.5 m s⁻²", "−2.0 m s⁻²"],
        "D", "medium", "numerical",
        "a = (10 − 20)/5 = −2.0 m s⁻².",
        "a = Δv/Δt = −2.0 m s⁻²।",
    ),
    q(
        "On a v–t graph from rest: rises linearly to 20 m s⁻¹ in 5 s then continues. Distance in first 5 s (triangle/trapezoid as applicable) if average v = 10 is:",
        "স্থির থেকে 5 s-এ বেগ সরলরেখায় 20 m s⁻¹ হলে প্রথম 5 s-এ দূরত্ব:",
        ["50 m", "100 m", "125 m", "150 m"],
        ["50 m", "100 m", "125 m", "150 m"],
        "A", "easy", "numerical",
        "Area of triangle = ½×5×20 = 50 m.",
        "ত্রিভুজের ক্ষেত্রফল = ½×5×20 = 50 m।",
    ),
    q(
        "Galileo’s odd-number rule for free fall from rest says distances in successive seconds are in ratio:",
        "স্থির থেকে মুক্ত পতনে গ্যালিলিওর বিজোড় সংখ্যা সূত্রানুসারে পরপর সেকেন্ডে দূরত্বের অনুপাত:",
        ["1:2:3:4", "1:3:5:7", "1:4:9:16", "2:4:6:8"],
        ["1:2:3:4", "1:3:5:7", "1:4:9:16", "2:4:6:8"],
        "B", "easy", "factual",
        "s_n ∝ (2n − 1) ⇒ 1:3:5:7:…",
        "s_n ∝ (2n − 1) ⇒ 1:3:5:7।",
    ),
]

# ---------------------------------------------------------------------------
# t03 Projectile motion
# ---------------------------------------------------------------------------
T03 = [
    q(
        "A projectile is launched at 45° with horizontal range 100 m. Maximum height is about:",
        "ভূমির সাথে 45° কোণে নিক্ষিপ্ত প্রাসের অনুভূমিক পাল্লা 100 m হলে সর্বোচ্চ উচ্চতা প্রায়:",
        ["14.43 m", "17.68 m", "25.00 m", "43.00 m"],
        ["14.43 m", "17.68 m", "25.00 m", "43.00 m"],
        "C", "medium", "numerical",
        "For θ = 45°, R = 4H ⇒ H = R/4 = 25 m.",
        "θ = 45° হলে R = 4H ⇒ H = 25 m।",
    ),
    q(
        "At the highest point of a projectile trajectory:",
        "প্রাসের গতিপথের সর্বোচ্চ উচ্চতায়:",
        ["Velocity is zero", "Potential energy is zero", "Velocity · acceleration = 0", "Velocity × acceleration = 0"],
        ["বেগ শূন্য", "স্থিতিশক্তি শূন্য", "বেগ · ত্বরণ = ০", "বেগ × ত্বরণ = ০"],
        "C", "medium", "conceptual",
        "Velocity is horizontal; acceleration g is vertical ⇒ dot product zero.",
        "বেগ অনুভূমিক, ত্বরণ উল্লম্ব ⇒ ডট গুণফল শূন্য।",
    ),
    q(
        "If x = 6t and y = 8t − 5t², launch speed of the projectile is:",
        "x = 6t এবং y = 8t − 5t² হলে নিক্ষেপণ বেগ:",
        ["10 m s⁻¹", "5 m s⁻¹", "6 m s⁻¹", "8 m s⁻¹"],
        ["10 m s⁻¹", "5 m s⁻¹", "6 m s⁻¹", "8 m s⁻¹"],
        "A", "medium", "numerical",
        "At t = 0: v_x = 6, v_y = 8 ⇒ u = √(36+64) = 10 m s⁻¹.",
        "t = 0-এ u_x = 6, u_y = 8 ⇒ u = 10 m s⁻¹।",
    ),
    q(
        "A projectile is thrown at 30° with speed 50 m s⁻¹. Speed after 2 s (g = 9.8) is about:",
        "৩০° কোণে 50 m s⁻¹ বেগে নিক্ষিপ্ত প্রাসের ২ s পর বেগ প্রায় (g = 9.8):",
        ["62.6 m s⁻¹", "43.63 m s⁻¹", "31.89 m s⁻¹", "5.4 m s⁻¹"],
        ["62.6 m s⁻¹", "43.63 m s⁻¹", "31.89 m s⁻¹", "5.4 m s⁻¹"],
        "B", "hard", "numerical",
        "v_x = 50 cos30°, v_y = 50 sin30° − 9.8×2 ⇒ |v| ≈ 43.63 m s⁻¹.",
        "v_x = 25√3, v_y = 5.4 ⇒ |v| ≈ 43.63 m s⁻¹।",
    ),
    q(
        "For a projectile launched at 30° with 50 m s⁻¹ (g = 9.8): (i) range ≈ 220.9 m (ii) max height ≈ 31.9 m (iii) vertical velocity component is zero at max height. Which is correct?",
        "৩০°, 50 m s⁻¹ প্রাসের জন্য: (i) পাল্লা ≈ 220.9 m (ii) সর্বোচ্চ উচ্চতা ≈ 31.9 m (iii) সর্বোচ্চে উল্লম্ব উপাংশ শূন্য — সঠিক?",
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        "D", "hard", "numerical",
        "R = u²sin2θ/g and H = u²sin²θ/(2g) match; v_y = 0 at top.",
        "R ও H সূত্র মিলে; শীর্ষে v_y = 0।",
    ),
    q(
        "Horizontal component of acceleration of a projectile (no air resistance) is:",
        "প্রাসের ত্বরণের অনুভূমিক উপাংশ (বায়ু প্রতিরোধ নেই):",
        ["g", "−g", "g/2", "Zero"],
        ["g", "−g", "g/2", "শূন্য"],
        "D", "easy", "factual",
        "Only gravity acts vertically; a_x = 0.",
        "অনুভূমিকে কোনো বল নেই বলে a_x = 0।",
    ),
    q(
        "Obliquely projected motion is:",
        "তির্যকভাবে প্রক্ষিপ্ত বস্তুর গতি কীরূপ?",
        ["1-D non-uniform acceleration", "1-D uniform acceleration", "2-D non-uniform acceleration", "2-D uniformly accelerated"],
        ["একমাত্রিক অসমত্বরণ", "একমাত্রিক সমত্বরণ", "দ্বিমাত্রিক অসমত্বরণ", "দ্বিমাত্রিক সমত্বরণ"],
        "D", "easy", "conceptual",
        "Motion is in a plane with constant acceleration g downward.",
        "সমতলে ধ্রুব ত্বরণ g — দ্বিমাত্রিক সমত্বরণ।",
    ),
    q(
        "Time of flight of a projectile is:",
        "প্রাসের বিচরণকালের সমীকরণ:",
        ["T = (u sinθ)/g", "T = (2u sinθ)/g", "T = (u² sinθ)/g", "T = (u² sin2θ)/g"],
        ["T = (u sinθ)/g", "T = (2u sinθ)/g", "T = (u² sinθ)/g", "T = (u² sin2θ)/g"],
        "B", "easy", "factual",
        "T = 2u sinθ / g for level ground.",
        "সমতল ভূমিতে T = 2u sinθ / g।",
    ),
    q(
        "A cricket ball is hit at 30° with 25 m s⁻¹ (g = 9.8). Time to return to ground is about:",
        "৩০° কোণে 25 m s⁻¹ বেগে ক্রিকেট বল আঘাত; ভূমিতে ফিরতে প্রায়:",
        ["1.27 s", "2.21 s", "2.55 s", "5.10 s"],
        ["1.27 s", "2.21 s", "2.55 s", "5.10 s"],
        "C", "medium", "numerical",
        "T = 2×25×sin30°/9.8 = 25/9.8 ≈ 2.55 s.",
        "T = 2×25×0.5/9.8 ≈ 2.55 s।",
    ),
    q(
        "Vertical projection straight up has horizontal range R equal to:",
        "খাড়া উপরের দিকে নিক্ষেপের অনুভূমিক পাল্লা R:",
        ["R_max", "R_max/2", "R_max/√2", "Zero"],
        ["R_max", "R_max/2", "R_max/√2", "শূন্য"],
        "D", "easy", "conceptual",
        "θ = 90° ⇒ R = u²sin180°/g = 0.",
        "θ = 90° হলে R = 0।",
    ),
    q(
        "For projectile motion (ideal): (i) only gravity acts after launch (ii) |a| = g (iii) path is two-dimensional. Which is correct?",
        "প্রাস গতিতে: (i) নিক্ষেপের পর শুধু অভিকর্ষ (ii) |a| = g (iii) গতিপথ দ্বিমাত্রিক — সঠিক?",
        ["iii only", "i, ii", "ii, iii", "i, ii, iii"],
        ["শুধু iii", "i, ii", "ii, iii", "i, ii, iii"],
        "D", "easy", "conceptual",
        "All three statements describe ideal projectile motion.",
        "তিনটিই আদর্শ প্রাস গতির বৈশিষ্ট্য।",
    ),
    q(
        "A rifle can fire at 40° or 50° with the same muzzle speed. Then:",
        "একই নিক্ষেপণ বেগে 40° ও 50° কোণে গুলি: (i) flight times unequal (ii) ranges equal (iii) horizontal speed component unchanged during flight",
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        "D", "medium", "conceptual",
        "Complementary angles share R; T ∝ sinθ differs; a_x = 0 so v_x constant.",
        "সম্পূরক কোণে R সমান; T অসমান; v_x ধ্রুব।",
    ),
    q(
        "Projectile launched at 60° with 10 m s⁻¹. Horizontal component of velocity is:",
        "৬০° কোণে 10 m s⁻¹ নিক্ষেপে অনুভূমিক বেগ উপাংশ:",
        ["3 m s⁻¹", "4 m s⁻¹", "5 m s⁻¹", "6 m s⁻¹"],
        ["3 m s⁻¹", "4 m s⁻¹", "5 m s⁻¹", "6 m s⁻¹"],
        "C", "easy", "numerical",
        "u_x = 10 cos60° = 5 m s⁻¹.",
        "u_x = 10 cos60° = 5 m s⁻¹।",
    ),
    q(
        "If horizontal range equals 4 times maximum height, launch angle is about:",
        "অনুভূমিক পাল্লা সর্বোচ্চ উচ্চতার ৪ গুণ হলে নিক্ষেপণ কোণ প্রায়:",
        ["30°", "45°", "26.6°", "90°"],
        ["30°", "45°", "26.6°", "90°"],
        "B", "medium", "numerical",
        "R/H = 4 cotθ; if R = 4H then cotθ = 1 ⇒ θ = 45°.",
        "R = 4H ⇒ cotθ = 1 ⇒ θ = 45°।",
    ),
    q(
        "For same launch speed at 30° and 60°, ratio of maximum heights H₃₀:H₆₀ is:",
        "একই বেগে 30° ও 60° নিক্ষেপে সর্বোচ্চ উচ্চতার অনুপাত:",
        ["1:3", "3:1", "2:1", "1:2"],
        ["1:3", "3:1", "2:1", "1:2"],
        "A", "medium", "numerical",
        "H ∝ sin²θ ⇒ sin²30:sin²60 = (1/4):(3/4) = 1:3.",
        "H ∝ sin²θ ⇒ ১:৩।",
    ),
    q(
        "A shell is fired at 45° with 50 m s⁻¹ and hits a target at the same height. Speed on impact is:",
        "৪৫° কোণে 50 m s⁻¹ গোলা সমউচ্চতায় লক্ষ্যে আঘাত করলে পতন বেগ:",
        ["25 m s⁻¹", "50√2 m s⁻¹", "50 m s⁻¹", "√50 m s⁻¹"],
        ["25 m s⁻¹", "50√2 m s⁻¹", "50 m s⁻¹", "√50 m s⁻¹"],
        "C", "medium", "conceptual",
        "Without air drag, speed at same height equals launch speed.",
        "বায়ু প্রতিরোধ না থাকলে সমউচ্চতায় বেগ = নিক্ষেপণ বেগ।",
    ),
    q(
        "Maximum horizontal range for a given speed occurs at angle:",
        "প্রদত্ত বেগে সর্বাধিক অনুভূমিক পাল্লা কোন কোণে?",
        ["30°", "45°", "60°", "90°"],
        ["30°", "45°", "60°", "90°"],
        "B", "easy", "factual",
        "R = u²sin2θ/g is max when 2θ = 90° ⇒ θ = 45°.",
        "sin2θ সর্বোচ্চ হলে θ = 45°।",
    ),
    q(
        "Which statements are true? (i) range is maximum at 45° (ii) horizontal acceleration of a projectile is zero (iii) projectile motion is two-dimensional",
        "(i) 45°-এ পাল্লা সর্বোচ্চ (ii) অনুভূমিক ত্বরণ শূন্য (iii) প্রাস গতি দ্বিমাত্রিক — সঠিক?",
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        ["i, ii", "i, iii", "ii, iii", "i, ii, iii"],
        "D", "easy", "conceptual",
        "All three are standard ideal-projectile facts.",
        "তিনটিই সঠিক।",
    ),
    q(
        "Equation of trajectory of a projectile is:",
        "প্রাসের গতিপথের সমীকরণ:",
        ["y = x tanθ − (gx²)/(2u² cos²θ)", "y = x tanθ + (gx²)/(2u²)", "y = xt − ½gt² only", "x = y tanθ"],
        ["y = x tanθ − (gx²)/(2u² cos²θ)", "y = x tanθ + (gx²)/(2u²)", "শুধু y = xt − ½gt²", "x = y tanθ"],
        "A", "medium", "factual",
        "Eliminating t from x = (u cosθ)t and y = (u sinθ)t − ½gt² gives the parabola.",
        "t বিলোপ করে পরাবৃত্তাকার গতিপথ পাওয়া যায়।",
    ),
    q(
        "At the highest point of a projectile, the vertical component of velocity is:",
        "প্রাসের সর্বোচ্চ বিন্দুতে বেগের উল্লম্ব উপাংশ:",
        ["Maximum", "Equal to u", "Zero", "Equal to g"],
        ["সর্বোচ্চ", "u-এর সমান", "শূন্য", "g-এর সমান"],
        "C", "easy", "factual",
        "v_y = 0 at the apex; only horizontal component remains.",
        "শীর্ষে v_y = 0।",
    ),
]

# ---------------------------------------------------------------------------
# t04 Relative motion
# ---------------------------------------------------------------------------
T04 = [
    q(
        "Relative velocity of A with respect to B is:",
        "B-এর সাপেক্ষে A-এর আপেক্ষিক বেগ:",
        ["v_A + v_B", "v_A − v_B", "v_B − v_A", "v_A × v_B"],
        ["v_A + v_B", "v_A − v_B", "v_B − v_A", "v_A × v_B"],
        "B", "easy", "factual",
        "By definition v_AB = v_A − v_B.",
        "সংজ্ঞা অনুসারে v_AB = v_A − v_B।",
    ),
    q(
        "Two cars move east at 20 m s⁻¹ and 15 m s⁻¹. Relative speed of the faster w.r.t. the slower is:",
        "দুই গাড়ি পূর্বে 20 ও 15 m s⁻¹। ধীরটির সাপেক্ষে দ্রুতটির আপেক্ষিক দ্রুতি:",
        ["35 m s⁻¹", "5 m s⁻¹", "20 m s⁻¹", "15 m s⁻¹"],
        ["35 m s⁻¹", "5 m s⁻¹", "20 m s⁻¹", "15 m s⁻¹"],
        "B", "easy", "numerical",
        "v_rel = 20 − 15 = 5 m s⁻¹ (same direction).",
        "একই দিকে v_rel = 20 − 15 = 5 m s⁻¹।",
    ),
    q(
        "Two cars approach each other at 20 m s⁻¹ and 15 m s⁻¹. Relative speed is:",
        "দুই গাড়ি পরস্পরের দিকে 20 ও 15 m s⁻¹। আপেক্ষিক দ্রুতি:",
        ["5 m s⁻¹", "15 m s⁻¹", "20 m s⁻¹", "35 m s⁻¹"],
        ["5 m s⁻¹", "15 m s⁻¹", "20 m s⁻¹", "35 m s⁻¹"],
        "D", "easy", "numerical",
        "Opposite directions: relative speed = 20 + 15 = 35 m s⁻¹.",
        "বিপরীত দিকে আপেক্ষিক দ্রুতি = ৩৫ m s⁻¹।",
    ),
    q(
        "From a 180 m tower a body is dropped; at the same instant another is projected upward at 60 m s⁻¹ along the same line (g = 10). They meet after:",
        "১৮০ m মিনার থেকে বস্তু ছাড়া ও একই সময়ে 60 m s⁻¹ উপরে নিক্ষেপ (g = 10)। মিলিত হবে:",
        ["1 s", "2 s", "3 s", "4 s"],
        ["1 s", "2 s", "3 s", "4 s"],
        "C", "hard", "numerical",
        "Closing: 180 = 60t ⇒ t = 3 s (relative acceleration cancels).",
        "আপেক্ষিক: 180 = 60t ⇒ t = 3 s।",
    ),
    q(
        "Rain falls vertically at 3 m s⁻¹. A man walks at 4 m s⁻¹. Relative speed of rain w.r.t. man is:",
        "বৃষ্টি উল্লম্বভাবে 3 m s⁻¹; মানুষ 4 m s⁻¹ হাঁটে। মানুষের সাপেক্ষে বৃষ্টির আপেক্ষিক দ্রুতি:",
        ["1 m s⁻¹", "5 m s⁻¹", "7 m s⁻¹", "12 m s⁻¹"],
        ["1 m s⁻¹", "5 m s⁻¹", "7 m s⁻¹", "12 m s⁻¹"],
        "B", "medium", "numerical",
        "|v_rm| = √(3² + 4²) = 5 m s⁻¹.",
        "|v_rm| = √(9+16) = 5 m s⁻¹।",
    ),
    q(
        "To keep an umbrella vertical while walking in rain that falls vertically, the man must:",
        "উল্লম্ব বৃষ্টিতে ছাতা উল্লম্ব রাখতে মানুষকে কী করতে হবে?",
        ["Walk faster", "Walk slower", "Stand still", "Tilt the umbrella forward always"],
        ["দ্রুত হাঁটতে হবে", "ধীরে হাঁটতে হবে", "স্থির থাকতে হবে", "সবসময় ছাতা সামনে হেলাতে হবে"],
        "C", "medium", "conceptual",
        "Only when man is at rest is rain’s relative velocity vertical.",
        "স্থির থাকলেই আপেক্ষিক বেগ উল্লম্ব থাকে।",
    ),
    q(
        "A boat’s speed in still water is 10 m s⁻¹; river current is 6 m s⁻¹. Speed downstream is:",
        "নীরব জলে নৌকার বেগ 10 m s⁻¹; স্রোত 6 m s⁻¹। অনুস্রোতে বেগ:",
        ["4 m s⁻¹", "6 m s⁻¹", "10 m s⁻¹", "16 m s⁻¹"],
        ["4 m s⁻¹", "6 m s⁻¹", "10 m s⁻¹", "16 m s⁻¹"],
        "D", "easy", "numerical",
        "Downstream: v_b + v_c = 16 m s⁻¹.",
        "অনুস্রোত: 10 + 6 = 16 m s⁻¹।",
    ),
    q(
        "Using the previous boat data, speed upstream is:",
        "পূর্বের নৌকা তথ্যে প্রতিকূলে বেগ:",
        ["4 m s⁻¹", "6 m s⁻¹", "10 m s⁻¹", "16 m s⁻¹"],
        ["4 m s⁻¹", "6 m s⁻¹", "10 m s⁻¹", "16 m s⁻¹"],
        "A", "easy", "numerical",
        "Upstream: 10 − 6 = 4 m s⁻¹.",
        "প্রতিকূল: 10 − 6 = 4 m s⁻¹।",
    ),
    q(
        "To cross a river by the shortest path, the boat’s resultant velocity must be:",
        "নদী সংক্ষিপ্ততম পথে পার হতে নৌকার লব্ধি বেগ হতে হবে:",
        ["Along the current", "Against the current", "Perpendicular to the banks", "At 45° to the current"],
        ["স্রোতের দিকে", "স্রোতের বিপরীতে", "তীরের লম্ব বরাবর", "স্রোতের সাথে 45°"],
        "C", "medium", "conceptual",
        "Shortest path is straight across ⇒ resultant ⊥ to banks.",
        "সংক্ষিপ্ততম পথ তীরের লম্ব বরাবর।",
    ),
    q(
        "If v_b = 10 m s⁻¹ (still water) and v_c = 6 m s⁻¹, minimum time to cross width 120 m requires heading:",
        "v_b = 10, v_c = 6; প্রস্থ 120 m পার হতে ন্যূনতম সময়ে নৌকা চালাতে হবে:",
        ["Straight upstream", "Straight downstream", "Perpendicular to current (heading)", "At arcsin(0.6) upstream of perpendicular"],
        ["সোজা প্রতিকূলে", "সোজা অনুস্রোতে", "স্রোতের লম্ব বরাবর (মুখ)", "লম্ব থেকে arcsin(0.6) উজানে"],
        "C", "hard", "conceptual",
        "Minimum time uses full boat speed across: head perpendicular to current.",
        "ন্যূনতম সময়ে নৌকার পূর্ণ বেগ প্রস্থ বরাবর — মুখ স্রোতের লম্ব।",
    ),
    q(
        "Relative acceleration of two freely falling bodies (neglect air) is:",
        "দুই মুক্ত পতনশীল বস্তুর আপেক্ষিক ত্বরণ (বায়ু উপেক্ষা):",
        ["g", "2g", "Zero", "g/2"],
        ["g", "2g", "শূন্য", "g/2"],
        "C", "medium", "conceptual",
        "Both have acceleration g downward ⇒ a_rel = 0.",
        "উভয়ের ত্বরণ g ⇒ আপেক্ষিক ত্বরণ শূন্য।",
    ),
    q(
        "A train moves at 20 m s⁻¹; a passenger walks forward at 2 m s⁻¹ relative to the train. Speed relative to ground is:",
        "ট্রেন 20 m s⁻¹; যাত্রী ট্রেনের সাপেক্ষে সামনে 2 m s⁻¹। ভূমির সাপেক্ষে বেগ:",
        ["18 m s⁻¹", "20 m s⁻¹", "22 m s⁻¹", "2 m s⁻¹"],
        ["18 m s⁻¹", "20 m s⁻¹", "22 m s⁻¹", "2 m s⁻¹"],
        "C", "easy", "numerical",
        "v_pg = v_pt + v_tg = 2 + 20 = 22 m s⁻¹.",
        "v_pg = 2 + 20 = 22 m s⁻¹।",
    ),
    q(
        "If the passenger walks backward at 2 m s⁻¹ relative to the same train, ground speed is:",
        "একই ট্রেনের সাপেক্ষে যাত্রী পেছনে 2 m s⁻¹ হাঁটলে ভূমির সাপেক্ষে বেগ:",
        ["18 m s⁻¹", "20 m s⁻¹", "22 m s⁻¹", "2 m s⁻¹"],
        ["18 m s⁻¹", "20 m s⁻¹", "22 m s⁻¹", "2 m s⁻¹"],
        "A", "easy", "numerical",
        "v_pg = −2 + 20 = 18 m s⁻¹.",
        "v_pg = 20 − 2 = 18 m s⁻¹।",
    ),
    q(
        "Velocity of approach of two bodies moving toward each other is the magnitude of:",
        "পরস্পরের দিকে আসা দুই বস্তুর অভিগমন বেগ হলো কোনটির মান?",
        ["v_A + v_B as vectors summed wrongly", "Their relative velocity", "Difference of accelerations", "Product of speeds"],
        ["v_A + v_B ভুল যোগ", "তাদের আপেক্ষিক বেগ", "ত্বরণের পার্থক্য", "দ্রুতির গুণফল"],
        "B", "medium", "conceptual",
        "Rate of decrease of separation equals |v_rel| along the line joining them.",
        "দূরত্ব হ্রাসের হার = আপেক্ষিক বেগের মান।",
    ),
    q(
        "A bird flies at 12 m s⁻¹ in still air; wind blows at 5 m s⁻¹ east. To fly due north, the bird must head:",
        "নীরব বাতাসে পাখি 12 m s⁻¹; বাতাস পূর্বে 5 m s⁻¹। সরাসরি উত্তরে যেতে মুখ রাখতে হবে:",
        ["Due north", "Slightly east of north", "Slightly west of north", "Due west"],
        ["সরাসরি উত্তরে", "উত্তরের সামান্য পূর্বে", "উত্তরের সামান্য পশ্চিমে", "সরাসরি পশ্চিমে"],
        "C", "hard", "application",
        "Head west of north so the east wind is cancelled in the resultant.",
        "পূর্ব বাতাস বাতিল করতে উত্তরের পশ্চিমে মুখ রাখতে হয়।",
    ),
    q(
        "Resultant ground speed of that bird (12 m s⁻¹ airspeed, 5 m s⁻¹ east wind, heading for due north) is:",
        "ওই পাখির ভূমি বেগ (বায়ু বেগ 12, বাতাস 5 পূর্বে, লক্ষ্য উত্তর):",
        ["13 m s⁻¹", "√119 m s⁻¹", "7 m s⁻¹", "17 m s⁻¹"],
        ["13 m s⁻¹", "√119 m s⁻¹", "7 m s⁻¹", "17 m s⁻¹"],
        "B", "hard", "numerical",
        "v_ground = √(12² − 5²) = √119 m s⁻¹ north.",
        "v = √(144 − 25) = √119 m s⁻¹ উত্তরে।",
    ),
    q(
        "v_AB = −v_BA expresses that relative velocities are:",
        "v_AB = −v_BA সম্পর্কটি প্রকাশ করে আপেক্ষিক বেগ:",
        ["Always equal", "Equal in magnitude, opposite in direction", "Perpendicular", "Independent"],
        ["সবসময় সমান", "মানে সমান, দিকে বিপরীত", "পরস্পর লম্ব", "স্বাধীন"],
        "B", "easy", "conceptual",
        "Swapping reference reverses the relative-velocity vector.",
        "প্রসঙ্গ বদলালে আপেক্ষিক বেগের দিক উল্টো হয়।",
    ),
    q(
        "A river is 200 m wide; boat speed in still water 5 m s⁻¹; current 3 m s⁻¹. Minimum time to cross is:",
        "নদীর প্রস্থ 200 m; নীরব জলে নৌকা 5 m s⁻¹; স্রোত 3 m s⁻¹। পার হতে ন্যূনতম সময়:",
        ["40 s", "50 s", "66.7 s", "100 s"],
        ["40 s", "50 s", "66.7 s", "100 s"],
        "A", "medium", "numerical",
        "t_min = width / v_b = 200/5 = 40 s (head ⊥ to current).",
        "t_min = 200/5 = 40 s।",
    ),
    q(
        "In the same river problem, time for the shortest path (straight across) is:",
        "একই নদী সমস্যায় সংক্ষিপ্ততম পথে (সোজা পার) সময়:",
        ["40 s", "50 s", "66.7 s", "100 s"],
        ["40 s", "50 s", "66.7 s", "100 s"],
        "B", "hard", "numerical",
        "v_across = √(5²−3²) = 4 m s⁻¹; t = 200/4 = 50 s.",
        "প্রস্থ বেগ = 4 m s⁻¹; t = 200/4 = 50 s।",
    ),
    q(
        "Two objects have velocities v₁ and v₂. If they have equal velocities, relative velocity is:",
        "দুই বস্তুর বেগ সমান হলে তাদের আপেক্ষিক বেগ:",
        ["2v₁", "v₁", "Zero", "v₁ − 2v₂"],
        ["2v₁", "v₁", "শূন্য", "v₁ − 2v₂"],
        "C", "easy", "conceptual",
        "v₁ = v₂ ⇒ v_rel = 0.",
        "সমান বেগে আপেক্ষিক বেগ শূন্য।",
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
    write_topic("phy1_27_ch03_t01", T01)
    write_topic("phy1_27_ch03_t02", T02)
    write_topic("phy1_27_ch03_t03", T03)
    write_topic("phy1_27_ch03_t04", T04)

    summary = {
        "paper": "physics_1",
        "chapter": 3,
        "title_en": "Dynamics",
        "title_bn": "গতিবিদ্যা",
        "per_topic": 20,
        "topics": {
            "phy1_27_ch03_t01": 20,
            "phy1_27_ch03_t02": 20,
            "phy1_27_ch03_t03": 20,
            "phy1_27_ch03_t04": 20,
        },
        "source": SOURCE,
        "verified": False,
        "mcq_printed_pages": [83, 89],
        "notes": "OCR-noisy pages reconstructed as HSC-accurate bilingual MCQs; figure-only graph items rewritten in text; relative-motion set supplemented for full 20.",
    }
    out = (
        ROOT
        / "content"
        / "bank"
        / "udvash_raw"
        / "physics_1"
        / "parsed"
        / "ch03_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("summary", out)


if __name__ == "__main__":
    main()
