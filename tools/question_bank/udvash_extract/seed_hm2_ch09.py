#!/usr/bin/env python3
"""Seed Higher Mathematics 2nd Paper Ch09 (Motion of Particles in a Plane).

Curated from Udvash HSC Question Bank 2026 printed pp. 303–310 (PDF 309–316).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
OCR is noisy (~8 pages; figures and answer-key math often garbled); reconstructs
board-style items from readable stems/solutions and supplements with accurate
HSC-level authored MCQs (esp. circular motion, thin in printed MCQs).
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
    "higher_mathematics p2 ch09; curated bilingual"
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
# hm2_27_ch09_t01 — Displacement, velocity and acceleration / সরণ, বেগ ও ত্বরণ
# =============================================================================
T01 = [
    q(
        "A particle starts from rest with acceleration 3 cm/s². Its speed after 1 minute is:",
        "একটি কণা স্থিরাবস্থা হতে 3 cm/s² ত্বরণে চলতে শুরু করলে 1 মিনিট পর তার বেগ কত হবে?",
        ["3 cm/s", "60 cm/s", "120 cm/s", "180 cm/s"],
        ["3 cm/s", "60 cm/s", "120 cm/s", "180 cm/s"],
        "D", "easy", "numerical",
        "v = u + at = 0 + 3 × 60 = 180 cm/s.",
        "v = u + at = 0 + 3 × 60 = 180 cm/s।",
    ),
    q(
        "A particle starts from rest under uniform acceleration and travels 16 m in 4 s. Distance covered in the 5th second is:",
        "স্থিরাবস্থা হতে সমত্বরণে চলমান একটি কণা 4 সেকেন্ডে 16 মিটার দূরত্ব অতিক্রম করে। ৫ম সেকেন্ডে কণাটি কত দূরত্ব অতিক্রম করবে?",
        ["9 m", "11 m", "18 m", "22 m"],
        ["9 মিটার", "11 মিটার", "18 মিটার", "22 মিটার"],
        "A", "medium", "numerical",
        "s = (1/2)at² ⇒ 16 = 8a ⇒ a = 2 m/s². Then s₅ = (a/2)(2·5 − 1) = 9 m.",
        "a = 2 m/s²; s₅ = (a/2)(9) = 9 m।",
    ),
    q(
        "A body falls freely from rest for 5 s (g = 32 ft/s²). Distance fallen in the last 3 seconds is:",
        "একটি বস্তু উপর থেকে মুক্তভাবে 5 সেকেন্ডে পড়ল। বস্তুটি শেষের 3 সেকেন্ডে কত ফুট পড়েছিল? (g = 32 ft/s²)",
        ["336", "256", "192", "128"],
        ["336", "256", "192", "128"],
        "A", "medium", "numerical",
        "s₅ − s₂ = (1/2)g(25 − 4) = 16 × 21 = 336 ft.",
        "শেষ 3 সেকেন্ড = (1/2)·32·(25 − 4) = 336 ft।",
    ),
    q(
        "A particle with uniform acceleration has u = 5 m/s, covers 50 cm and then has speed 10 m/s. Its acceleration is:",
        "একটি কণা সমত্বরণে 5 m/s আদিবেগে 50 cm অতিক্রম করে 10 m/s গতিবেগ অর্জন করে। কণাটির ত্বরণ কত?",
        ["−75 m/s²", "75 m/s²", "75 cm/s²", "7.5 m/s²"],
        ["−75 m/s²", "75 m/s²", "75 cm/s²", "7.5 m/s²"],
        "B", "medium", "numerical",
        "v² = u² + 2as ⇒ 100 = 25 + 2a·0.5 ⇒ a = 75 m/s².",
        "100 = 25 + a ⇒ a = 75 m/s²।",
    ),
    q(
        "A car with uniform acceleration has u = 25 km/h, covers 150 km and reaches 60 km/h. Its acceleration is approximately:",
        "একখানা গাড়ি সমত্বরণে 25 km/h আদিবেগে 150 km অতিক্রম করে 60 km/h চূড়ান্ত বেগ প্রাপ্ত হয়। গাড়িটির ত্বরণ কত?",
        ["9.92 km/h²", "14.08 km/h²", "19.83 km/h²", "28.16 km/h²"],
        ["9.92 km/h²", "14.08 km/h²", "19.83 km/h²", "28.16 km/h²"],
        "A", "medium", "numerical",
        "v² − u² = 2as ⇒ 3600 − 625 = 300a ⇒ a ≈ 9.92 km/h².",
        "a = (3600 − 625)/300 ≈ 9.92 km/h²।",
    ),
    q(
        "A car starts with u = 15 m/s and uniform acceleration 4 m/s². Speed after travelling 150 m is:",
        "একটি গাড়ী 15 m/s আদিবেগে এবং 4 m/s² সমত্বরণে 150 m দূরত্ব অতিক্রম করলে বেগ কত?",
        ["37.75 m/s", "30.75 m/s", "29.75 m/s", "28.75 m/s"],
        ["37.75 m/s", "30.75 m/s", "29.75 m/s", "28.75 m/s"],
        "A", "easy", "numerical",
        "v² = 15² + 2·4·150 = 1425 ⇒ v ≈ 37.75 m/s.",
        "v² = 225 + 1200 = 1425 ⇒ v ≈ 37.75 m/s।",
    ),
    q(
        "A particle starts from rest with a = 2 m/s². Distance covered in the 2nd second is:",
        "একটি কণা স্থিরাবস্থা হতে 2 m/s² সমত্বরণে চলে। ২য় সেকেন্ডে অতিক্রান্ত দূরত্ব কত?",
        ["1 m", "2 m", "3 m", "4 m"],
        ["1 m", "2 m", "3 m", "4 m"],
        "C", "easy", "numerical",
        "s₂ = (a/2)(2·2 − 1) = 1·3 = 3 m.",
        "s₂ = (a/2)(3) = 3 m।",
    ),
    q(
        "Which is a correct equation of motion for uniform acceleration f along a straight line?",
        "সরলরেখায় সমত্বরণে চলমান বস্তুর গতিসূত্র কোনটি?",
        ["v = u + ft", "s = ut − ft²", "v² = u² − 2fs (always)", "v = u − ft only"],
        ["v = u + ft", "s = ut − ft²", "v² = u² − 2fs (সর্বদা)", "কেবল v = u − ft"],
        "A", "easy", "factual",
        "The standard relation is v = u + ft.",
        "মানক সূত্র: v = u + ft।",
    ),
    q(
        "A stone dropped into an empty well hits the bottom at 18 m/s. Depth is approximately (g = 9.8):",
        "একটি শূন্য কূপে পাথর ফেললে তা 18 m/s বেগে তলদেশে পতিত হয়। কূপের গভীরতা প্রায় কত? (g = 9.8)",
        ["9.18 m", "16.53 m", "18.36 m", "33.00 m"],
        ["9.18 মি.", "16.53 মি.", "18.36 মি.", "33.00 মি."],
        "B", "medium", "numerical",
        "v² = 2gh ⇒ h = 324/(19.6) ≈ 16.53 m.",
        "h = 324/(2·9.8) ≈ 16.53 m।",
    ),
    q(
        "A body released from rest falls through which distance in the first second? (g = 9.8 m/s²)",
        "একটি বস্তুকে ছেড়ে দিলে এক সেকেন্ডে যে দূরত্ব নিচে নামবে তা হলো—",
        ["4.9 m", "9.8 m", "−4.9 m", "−9.8 m"],
        ["4.9 মিটার", "9.8 মিটার", "−4.9 মিটার", "−9.8 মিটার"],
        "A", "easy", "numerical",
        "s = (1/2)gt² = 4.9 m downward.",
        "s = (1/2)·9.8·1 = 4.9 মিটার।",
    ),
    q(
        "Which statements about acceleration are true? (i) it is a vector (ii) SI unit is m/s² (iii) it is zero for uniform velocity",
        "ত্বরণ সম্পর্কে কোনটি সঠিক? (i) এটি ভেক্টর (ii) SI একক m/s² (iii) সুষম বেগে শূন্য",
        ["i, ii only", "ii, iii only", "i, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল ii, iii", "কেবল i, iii", "i, ii ও iii"],
        "D", "easy", "conceptual",
        "All three statements are correct.",
        "তিনটিই সঠিক।",
    ),
    q(
        "If acceleration is zero, velocity with respect to time is:",
        "ত্বরণ শূন্য হলে সময়ের সাপেক্ষে বেগ—",
        ["increasing", "decreasing", "tripling", "constant"],
        ["বৃদ্ধি পায়", "হ্রাস পায়", "তিনগুণ হয়", "সমান থাকে"],
        "D", "easy", "factual",
        "a = dv/dt = 0 ⇒ v is constant.",
        "a = 0 হলে বেগ অপরিবর্তিত।",
    ),
    q(
        "A body moves with uniform speed and covers 45 m in 5 s. Its speed is:",
        "সমবেগে 5 সেকেন্ডে 45 মিটার অতিক্রম করলে বেগ কত m/s?",
        ["6", "7", "8", "9"],
        ["6", "7", "8", "9"],
        "D", "easy", "numerical",
        "v = 45/5 = 9 m/s.",
        "v = 45/5 = 9 m/s।",
    ),
    q(
        "A car with u = 5 m/s covers 100 m under uniform acceleration and reaches 25 m/s. Acceleration is:",
        "একটি গাড়ি 5 m/s বেগে সুষম ত্বরণে 100 m অতিক্রম করে 25 m/s বেগ পেলে ত্বরণ কত?",
        ["1.5 m/s²", "2 m/s²", "3 m/s²", "2.5 m/s²"],
        ["1.5 মি/সে²", "2 মি/সে²", "3 মি/সে²", "2.5 মি/সে²"],
        "C", "easy", "numerical",
        "625 − 25 = 200a ⇒ a = 3 m/s².",
        "600 = 200a ⇒ a = 3 m/s²।",
    ),
    q(
        "Distance covered in the t-th second by a body with initial speed u and uniform acceleration f is:",
        "u আদিবেগে f সমত্বরণে চলন্ত বস্তুর t-তম সেকেন্ডে অতিক্রান্ত দূরত্ব—",
        ["u + (f/2)(2t + 1)", "u + (f/2)(2t − 1)", "u − (f/2)(2t + 1)", "u − (f/2)(2t − 1)"],
        ["u + (f/2)(2t + 1)", "u + (f/2)(2t − 1)", "u − (f/2)(2t + 1)", "u − (f/2)(2t − 1)"],
        "B", "medium", "factual",
        "s_t = u + (f/2)(2t − 1).",
        "s_t = u + (f/2)(2t − 1)।",
    ),
    q(
        "A bullet with initial speed 4 m/s enters a wall 2 m deep and stops. Magnitude of retardation is:",
        "একটি বুলেট 4 m/s আদি বেগে দেওয়ালে 2 m প্রবেশ করে থেমে যায়। মন্দন কত m/s²?",
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        "D", "easy", "numerical",
        "0 = 16 − 2a·2 ⇒ a = 4 m/s².",
        "0 = 16 − 4a ⇒ a = 4 m/s²।",
    ),
    q(
        "A stone dropped into an empty well reaches the bottom in 3 s. Depth is (g = 9.8):",
        "শূন্য কূপে পাথর ফেললে 3 s এ তলদেশে পৌঁছায়। গভীরতা কত মিটার? (g = 9.8)",
        ["44.1", "45.1", "46.1", "47.1"],
        ["44.1", "45.1", "46.1", "47.1"],
        "A", "easy", "numerical",
        "h = (1/2)·9.8·9 = 44.1 m.",
        "h = 4.9 × 9 = 44.1 m।",
    ),
    q(
        "A car moving at 50 m/s has brakes applied with retardation 5 m/s². Speed after 8 s is:",
        "50 m/s বেগে চলা গাড়িতে 5 m/s² মন্দন সৃষ্টি হলে 8 সেকেন্ড পর বেগ কত?",
        ["10 m/s", "40 m/s", "60 m/s", "90 m/s"],
        ["10 m/s", "40 m/s", "60 m/s", "90 m/s"],
        "A", "easy", "numerical",
        "v = 50 − 5·8 = 10 m/s.",
        "v = 50 − 40 = 10 m/s।",
    ),
    q(
        "From rest under uniform acceleration, times to cover three successive equal distances are in the ratio:",
        "স্থিরাবস্থা হতে সমত্বরণে তিনটি সমান ক্রমিক দূরত্ব অতিক্রমের সময়ের অনুপাত—",
        ["1 : 2 : 3", "1 : 3 : 5", "1 : (√2 − 1) : (√3 − √2)", "1 : 1 : 1"],
        ["1 : 2 : 3", "1 : 3 : 5", "1 : (√2 − 1) : (√3 − √2)", "1 : 1 : 1"],
        "C", "hard", "conceptual",
        "Since s ∝ t² from rest, successive equal distances need times 1 : (√2−1) : (√3−√2).",
        "s ∝ t² হওয়ায় অনুপাত 1 : (√2−1) : (√3−√2)।",
    ),
    q(
        "A bullet loses half its speed after penetrating 2 cm into a wall (uniform retardation). Further distance before stopping is:",
        "একটি বুলেট দেয়ালে 2 cm ঢুকে অর্ধেক বেগ হারায়। থামার আগে আর কতদূর ঢুকবে?",
        ["2/3 cm", "1 cm", "4/3 cm", "2 cm"],
        ["2/3 cm", "1 cm", "4/3 cm", "2 cm"],
        "A", "hard", "numerical",
        "(u/2)² = u² − 2a·2 ⇒ remaining s₂ = 2/3 cm.",
        "অবশিষ্ট দূরত্ব s₂ = s₁/3 = 2/3 cm।",
    ),
]


# =============================================================================
# hm2_27_ch09_t02 — Projectile motion / প্রাসের গতি
# =============================================================================
T02 = [
    q(
        "In vacuum, the path of a projected particle is a:",
        "বায়ুশূন্য স্থানে নিক্ষিপ্ত বস্তুর গতিপথ একটি—",
        ["parabola", "ellipse", "hyperbola", "circle"],
        ["পরাবৃত্ত", "উপবৃত্ত", "অধিবৃত্ত", "বৃত্ত"],
        "A", "easy", "factual",
        "Under constant gravity with no air resistance the trajectory is a parabola.",
        "ধ্রুব অভিকর্ষ ও বায়ুরোধহীন অবস্থায় গতিপথ পরাবৃত্ত।",
    ),
    q(
        "Horizontal range of a projectile with speed u at angle α is:",
        "u গতিবেগে α কোণে প্রক্ষিপ্ত বস্তুর আনুভূমিক পাল্লা—",
        ["(u sin 2α)/g", "(u² sin 2α)/g", "(u sin 2α)/(2g)", "(u² sin 2α)/(2g)"],
        ["(u sin 2α)/g", "(u² sin 2α)/g", "(u sin 2α)/(2g)", "(u² sin 2α)/(2g)"],
        "B", "easy", "factual",
        "R = (u² sin 2α)/g.",
        "R = (u² sin 2α)/g।",
    ),
    q(
        "For maximum horizontal range, the angle of projection is:",
        "আনুভূমিক পাল্লা বৃহত্তম হলে প্রক্ষেপণ কোণ কত?",
        ["30°", "45°", "60°", "90°"],
        ["30°", "45°", "60°", "90°"],
        "B", "easy", "factual",
        "sin 2α = 1 ⇒ α = 45°.",
        "sin 2α = 1 ⇒ α = 45°।",
    ),
    q(
        "A projectile thrown at 30 m/s has range 60 m (g = 9.8). Angle of projection is approximately:",
        "30 m/s বেগে নিক্ষিপ্ত প্রক্ষেপকের পাল্লা 60 m হলে নিক্ষেপণ কোণ প্রায় কত?",
        ["20.39°", "25°", "30°", "32.35°"],
        ["20.39°", "25°", "30°", "32.35°"],
        "A", "medium", "numerical",
        "sin 2α = 60·9.8/900 ≈ 0.653 ⇒ α ≈ 20.39°.",
        "sin 2α ≈ 0.653 ⇒ α ≈ 20.39°।",
    ),
    q(
        "A particle is projected at 30° with speed 9.8 m/s. Time until its velocity is horizontal (g = 9.8):",
        "30° কোণে 9.8 m/s বেগে প্রক্ষিপ্ত বস্তু কত সময় পর আনুভূমিকভাবে চলবে?",
        ["0.25 s", "0.5 s", "1 s", "2 s"],
        ["0.25 সে.", "0.5 সে.", "1 সে.", "2 সে."],
        "B", "medium", "numerical",
        "t = (u sin 30°)/g = 0.5 s.",
        "t = (u sin 30°)/g = 0.5 সেকেন্ড।",
    ),
    q(
        "For speed u at angle α, which are true? (i) path in vacuum is a parabola (ii) range max at α = 45° (iii) T = (2u sin α)/g",
        "u বেগে α কোণে প্রক্ষেপে— (i) বায়ুশূন্যে গতিপথ পরাবৃত্ত (ii) α = 45° এ পাল্লা বৃহত্তম (iii) বিচরণকাল T = (2u sin α)/g",
        ["i, ii only", "i, iii only", "ii, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল i, iii", "কেবল ii, iii", "i, ii ও iii"],
        "D", "easy", "conceptual",
        "All three are standard projectile results.",
        "তিনটিই মানক ফলাফল।",
    ),
    q(
        "Maximum height for vertical projection with speed v is:",
        "v বেগে খাড়া উপরের দিকে নিক্ষিপ্ত বস্তুর সর্বাধিক উচ্চতা—",
        ["v/g", "v/(2g)", "v²/(2g)", "2v²/g"],
        ["v/g", "v/(2g)", "v²/(2g)", "2v²/g"],
        "C", "easy", "factual",
        "0 = v² − 2gh ⇒ h = v²/(2g).",
        "h = v²/(2g)।",
    ),
    q(
        "A particle projected with speed u at 30° has speed at maximum height:",
        "u বেগে 30° কোণে প্রক্ষিপ্ত কণার সর্বোচ্চ উচ্চতায় বেগ—",
        ["u/2", "(√3/2)u", "u", "√3 u"],
        ["u/2", "(√3/2)u", "u", "√3 u"],
        "B", "medium", "numerical",
        "Only horizontal component remains: u cos 30° = (√3/2)u.",
        "বেগ = u cos 30° = (√3/2)u।",
    ),
    q(
        "A stone projected vertically upward returns after 5 s. Impact speed is (g = 9.8):",
        "খাড়া উপরের দিকে নিক্ষিপ্ত পাথর 5 সেকেন্ডে ফিরে আসে। পতন বেগ কত? (g = 9.8)",
        ["19.6 m/s", "24.5 m/s", "25.57 m/s", "22.40 m/s"],
        ["19.6 m/s", "24.5 m/s", "25.57 m/s", "22.40 m/s"],
        "B", "medium", "numerical",
        "T = 2u/g = 5 ⇒ u = 24.5 m/s = impact speed.",
        "u = (5·9.8)/2 = 24.5 m/s।",
    ),
    q(
        "For projection at 45°, if range is R and max height is H, then:",
        "45° কোণে নিক্ষেপে পাল্লা R ও সর্বোচ্চ উচ্চতা H হলে—",
        ["2R = H", "R = H", "R = 2H", "R = 4H"],
        ["2R = H", "R = H", "R = 2H", "R = 4H"],
        "D", "medium", "conceptual",
        "R = u²/g and H = u²/(4g) ⇒ R = 4H.",
        "R = 4H।",
    ),
    q(
        "For u = 30 m/s at 30° (g ≈ 9.8), which are approximately true? (i) R ≈ 79.53 m (ii) H ≈ 11.48 m (iii) T ≈ 3.06 s",
        "30 m/s বেগে 30° কোণে— (i) পাল্লা ≈ 79.53 m (ii) উচ্চতা ≈ 11.48 m (iii) বিচরণকাল ≈ 3.06 s",
        ["i, ii only", "ii, iii only", "i, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল ii, iii", "কেবল i, iii", "i, ii ও iii"],
        "D", "medium", "numerical",
        "Standard R, H, T formulas match all three values.",
        "R, H, T সব মিলে; তিনটিই সত্য।",
    ),
    q(
        "A body is projected with speed u at 60° to the ground. Vertical component of u is:",
        "u বেগে 60° কোণে নিক্ষেপে উল্লম্ব উপাংশ—",
        ["u/2", "u/√2", "(√3/2)u", "u"],
        ["u/2", "u/√2", "(√3/2)u", "u"],
        "C", "easy", "numerical",
        "u_y = u sin 60° = (√3/2)u.",
        "u_y = (√3/2)u।",
    ),
    q(
        "For the same projection (u at 60°), horizontal range is:",
        "u বেগে 60° কোণে আনুভূমিক পাল্লা—",
        ["u²/(2g)", "u²/g", "(√3 u²)/(2g)", "2u²/g"],
        ["u²/(2g)", "u²/g", "(√3 u²)/(2g)", "2u²/g"],
        "C", "medium", "numerical",
        "R = u² sin 120°/g = (√3 u²)/(2g).",
        "R = (√3 u²)/(2g)।",
    ),
    q(
        "A player can throw a ball vertically to 90 m. Maximum horizontal range with the same speed is:",
        "একজন খেলোয়াড় বলকে খাড়া 90 m উঁচুতে নিক্ষেপ করতে পারে। একই বেগে সর্বাধিক আনুভূমিক পাল্লা—",
        ["120 m", "140 m", "180 m", "200 m"],
        ["120 m", "140 m", "180 m", "200 m"],
        "C", "medium", "numerical",
        "H = u²/(2g) = 90 ⇒ R_max = u²/g = 180 m.",
        "R_max = 2H = 180 m।",
    ),
    q(
        "Equation of the trajectory with range R and angle α is:",
        "পাল্লা R ও কোণ α হলে গতিপথের সমীকরণ—",
        ["y = x cot α (1 − x/R)", "x = y tan α (1 − x/R)", "y = x tan α (1 − x/R)", "x = y tan α (1 − y/R)"],
        ["y = x cot α (1 − x/R)", "x = y tan α (1 − x/R)", "y = x tan α (1 − x/R)", "x = y tan α (1 − y/R)"],
        "C", "hard", "factual",
        "y = x tan α (1 − x/R).",
        "y = x tan α (1 − x/R)।",
    ),
    q(
        "A projectile just clears a 3 m wall 10 m away while flying horizontally there, 5 s after launch. Which are true? (i) R = 20 m (ii) H = 3 m (iii) T = 10 s",
        "10 m দূরে 3 m উঁচু দেয়াল আনুভূমিকভাবে অতিক্রমে 5 s লাগে। (i) পাল্লা 20 m (ii) উচ্চতা 3 m (iii) বিচরণকাল 10 s",
        ["i, ii only", "ii, iii only", "i, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল ii, iii", "কেবল i, iii", "i, ii ও iii"],
        "D", "hard", "conceptual",
        "Apex at the wall ⇒ H = 3, T/2 = 5 ⇒ T = 10, R = 20. All true.",
        "শীর্ষে দেয়াল ⇒ H = 3, T = 10, R = 20। তিনটিই সত্য।",
    ),
    q(
        "Maximum range of a projectile with speed 9.8 m/s is (g = 9.8):",
        "9.8 m/s বেগে প্রক্ষিপ্ত বস্তুর সর্বাধিক পাল্লা (g = 9.8)—",
        ["1.5 m", "3 m", "4.9 m", "9.8 m"],
        ["1.5 m", "3 m", "4.9 m", "9.8 m"],
        "D", "easy", "numerical",
        "R_max = u²/g = 9.8 m.",
        "R_max = 9.8 m।",
    ),
    q(
        "A body projected vertically with speed u reaches height h at two times whose difference is:",
        "u বেগে খাড়া নিক্ষেপে h উচ্চতায় দুই সময়ের পার্থক্য—",
        ["√(u² − 2gh)/g", "2√(u² − 2gh)/g", "√(u² − 2gh)/(2g)", "g/√(u² − 2gh)"],
        ["√(u² − 2gh)/g", "2√(u² − 2gh)/g", "√(u² − 2gh)/(2g)", "g/√(u² − 2gh)"],
        "B", "hard", "numerical",
        "From (1/2)gt² − ut + h = 0, |t₁ − t₂| = 2√(u² − 2gh)/g.",
        "পার্থক্য = 2√(u² − 2gh)/g।",
    ),
    q(
        "Angles of projection α and (90° − α) with the same speed give:",
        "α ও (90° − α) কোণে একই বেগে নিক্ষেপে—",
        ["same range only", "same max height only", "same time of flight only", "equal range and height"],
        ["কেবল একই পাল্লা", "কেবল একই সর্বোচ্চ উচ্চতা", "কেবল একই বিচরণকাল", "পাল্লা ও উচ্চতা উভয়ই সমান"],
        "A", "medium", "conceptual",
        "sin 2α = sin 2(90°−α) so ranges coincide; heights differ.",
        "পাল্লা সমান; উচ্চতা ভিন্ন।",
    ),
    q(
        "A stone dropped from a balloon ascending at 20 m/s hits ground after 20 s (g = 9.8). Release height is:",
        "20 m/s উর্ধ্বগামী বেলুন থেকে পাথর ফেললে 20 s পর ভূমিতে পড়ে। ফেলার সময় উচ্চতা (g = 9.8)—",
        ["390 m", "560 m", "1250 m", "1560 m"],
        ["390 m", "560 m", "1250 m", "1560 m"],
        "D", "hard", "numerical",
        "h = −ut + (1/2)gt² = −400 + 1960 = 1560 m.",
        "h = −20·20 + (1/2)·9.8·400 = 1560 m।",
    ),
]


# =============================================================================
# hm2_27_ch09_t03 — Relative and circular motion / আপেক্ষিক ও বৃত্তীয় গতি
# =============================================================================
T03 = [
    q(
        "Two buses X and Y travel the same direction at 20 km/h and 10 km/h. Relative velocity of X w.r.t. Y is:",
        "X ও Y বাস একই দিকে 20 ও 10 km/h বেগে চললে Y-এর সাপেক্ষে X-এর আপেক্ষিক বেগ—",
        ["0 km/h", "10 km/h", "20 km/h", "30 km/h"],
        ["0 km/h", "10 km/h", "20 km/h", "30 km/h"],
        "B", "easy", "numerical",
        "v_XY = 20 − 10 = 10 km/h.",
        "v_XY = 10 km/h।",
    ),
    q(
        "If velocities u and v act in opposite directions, magnitude of relative velocity is:",
        "u ও v বিপরীত দিকে ক্রিয়া করলে আপেক্ষিক বেগের মান—",
        ["√(u + v)", "u + v", "|u − v| only always", "√|u − v|"],
        ["√(u + v)", "u + v", "কেবল |u − v|", "√|u − v|"],
        "B", "easy", "factual",
        "Opposite directions: |v_rel| = u + v.",
        "বিপরীত দিকে |v_rel| = u + v।",
    ),
    q(
        "For speeds u < v, which are true? (i) max relative speed = u + v (ii) min relative speed = v − u (iii) at 90°, relative speed = √(u² + v²)",
        "u < v হলে— (i) বৃহত্তম আপেক্ষিক বেগ u + v (ii) ক্ষুদ্রতম v − u (iii) 90° এ √(u² + v²)",
        ["i, ii only", "i, iii only", "ii, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল i, iii", "কেবল ii, iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "All three follow from |v_rel| = √(u² + v² − 2uv cos θ).",
        "তিনটিই সত্য।",
    ),
    q(
        "A car moves at 8 km/h. An object is thrown at 16 km/h relative to the car so its ground path is perpendicular to the road. Angle with the forward direction is:",
        "গাড়ি 8 km/h চলছে। 16 km/h বেগে নিক্ষেপে গতিপথ গাড়ির সাথে সমকোণ হলে নিক্ষেপণ কোণ—",
        ["30°", "45°", "90°", "120°"],
        ["30°", "45°", "90°", "120°"],
        "D", "hard", "numerical",
        "16 cos α + 8 = 0 ⇒ cos α = −1/2 ⇒ α = 120°.",
        "cos α = −1/2 ⇒ α = 120°।",
    ),
    q(
        "A swimmer crosses a still river 450 m wide straight across in 15 min. Speed is:",
        "স্রোতহীন 450 m চওড়া নদী 15 মিনিটে সোজা পার হলে সাঁতারুর বেগ—",
        ["1.2 km/h", "1.5 km/h", "1.8 km/h", "2.0 km/h"],
        ["1.2 কি.মি/ঘণ্টা", "1.5 কি.মি/ঘণ্টা", "1.8 কি.মি/ঘণ্টা", "2.0 কি.মি/ঘণ্টা"],
        "C", "medium", "numerical",
        "v = 0.45/0.25 = 1.8 km/h.",
        "v = 1.8 কি.মি/ঘণ্টা।",
    ),
    q(
        "Two trains approach each other each at 60 m/s and sight each other 1200 m apart. Equal retardation of each to just avoid collision is:",
        "দুই ট্রেন প্রত্যেক 60 m/s বেগে বিপরীত দিক থেকে আসছে; 1200 m দূরে দেখে সংঘর্ষ এড়াতে প্রত্যেকের মন্দন—",
        ["2 m/s²", "3 m/s²", "4 m/s²", "5 m/s²"],
        ["2 m/s²", "3 m/s²", "4 m/s²", "5 m/s²"],
        "B", "hard", "numerical",
        "0 = 120² − 2·(2f)·1200 ⇒ f = 3 m/s².",
        "f = 3 m/s²।",
    ),
    q(
        "A ball moving at 30 m/s is struck so its velocity becomes 50 m/s perpendicular to the original direction. |Δv| is:",
        "30 m/s বেগের বলকে সমকোণে 50 m/s বেগ দিলে বেগ পরিবর্তনের মান—",
        ["20 m/s", "40 m/s", "80 m/s", "√3400 m/s"],
        ["20 m/s", "40 m/s", "80 m/s", "√3400 m/s"],
        "D", "medium", "numerical",
        "|Δv| = √(30² + 50²) = √3400 m/s.",
        "|Δv| = √3400 m/s।",
    ),
    q(
        "Velocities 10 m/s and 5 m/s meet at 120°. Angle between the resultant and the 10 m/s velocity is:",
        "10 m/s ও 5 m/s বেগ 120° কোণে ক্রিয়া করলে লব্ধি 10 m/s-এর সাথে কোণ—",
        ["15°", "30°", "60°", "40°"],
        ["15°", "30°", "60°", "40°"],
        "B", "hard", "numerical",
        "tan θ = (5 sin 120°)/(10 + 5 cos 120°) = √3/3 ⇒ θ = 30°.",
        "θ = 30°।",
    ),
    q(
        "A river is 2.5 km wide with current 3 km/h. A boat of still-water speed 5 km/h heads perpendicular to the banks. Downstream drift is:",
        "2.5 কি.মি. চওড়া নদীতে স্রোত 3 কি.মি/ঘণ্টা। স্থির পানিতে 5 কি.মি/ঘণ্টা বেগের নৌকা তীরের লম্বভাবে চললে ভাটিতে সরণ—",
        ["1.2 km", "1.5 km", "1.8 km", "2.0 km"],
        ["1.2 কি.মি.", "1.5 কি.মি.", "1.8 কি.মি.", "2.0 কি.মি."],
        "B", "medium", "numerical",
        "t = 2.5/5 = 0.5 h; drift = 3·0.5 = 1.5 km.",
        "drift = 3 × (2.5/5) = 1.5 কি.মি।",
    ),
    q(
        "A mouse starts from rest 120 m ahead of a cat with uniform acceleration 1/30 m/s². The cat runs at constant speed and just catches it in 1 min. Cat’s speed is:",
        "বিড়ালের 120 m সামনে ইঁদুর স্থির থেকে 1/30 m/s² ত্বরণে দৌড়ায়। বিড়াল সমবেগে 1 মিনিটে ধরলে তার বেগ—",
        ["3 m/s", "4 m/s", "5 m/s", "6 m/s"],
        ["3 m/s", "4 m/s", "5 m/s", "6 m/s"],
        "A", "hard", "numerical",
        "Mouse travels (1/2)·(1/30)·3600 = 60 m in 60 s; cat covers 180 m ⇒ v = 3 m/s.",
        "ইঁদুর 60 m; বিড়াল 180 m ⇒ v = 3 m/s।",
    ),
    q(
        "A particle moves in a circle of radius r with constant speed v. Magnitude of its acceleration is:",
        "r ব্যাসার্ধের বৃত্তে সমবেগ v-তে চলমান কণার ত্বরণের মান—",
        ["0", "v/r", "v²/r", "v²/r²"],
        ["0", "v/r", "v²/r", "v²/r²"],
        "C", "easy", "factual",
        "Centripetal acceleration a = v²/r toward the centre.",
        "কেন্দ্রমুখী ত্বরণ a = v²/r।",
    ),
    q(
        "Angular speed ω and linear speed v for circular radius r are related by:",
        "বৃত্তীয় গতিতে কৌণিক বেগ ω ও রৈখিক বেগ v-এর সম্পর্ক (ব্যাসার্ধ r)—",
        ["v = ω/r", "v = ωr", "v = ω²r", "v = r/ω"],
        ["v = ω/r", "v = ωr", "v = ω²r", "v = r/ω"],
        "B", "easy", "factual",
        "v = ωr.",
        "v = ωr।",
    ),
    q(
        "A particle completes one revolution in a circle of radius 7 m in 2 s. Its linear speed is approximately (π ≈ 22/7):",
        "7 m ব্যাসার্ধের বৃত্তে 2 s-এ এক পূর্ণ আবর্তন করলে রৈখিক বেগ প্রায় (π ≈ 22/7)—",
        ["11 m/s", "22 m/s", "14 m/s", "7 m/s"],
        ["11 m/s", "22 m/s", "14 m/s", "7 m/s"],
        "B", "medium", "numerical",
        "v = 2πr/T = 2·(22/7)·7/2 = 22 m/s.",
        "v = 2πr/T = 22 m/s।",
    ),
    q(
        "Direction of centripetal acceleration in uniform circular motion is:",
        "সুষম বৃত্তীয় গতিতে কেন্দ্রমুখী ত্বরণের দিক—",
        ["along the tangent forward", "along the tangent backward", "toward the centre", "away from the centre"],
        ["স্পর্শক বরাবর সামনে", "স্পর্শক বরাবর পিছনে", "কেন্দ্রের দিকে", "কেন্দ্র থেকে দূরে"],
        "C", "easy", "factual",
        "Centripetal acceleration is always directed toward the centre.",
        "কেন্দ্রমুখী ত্বরণ সর্বদা কেন্দ্রের দিকে।",
    ),
    q(
        "Period T and angular speed ω for uniform circular motion satisfy:",
        "সুষম বৃত্তীয় গতিতে পর্যায়কাল T ও কৌণিক বেগ ω—",
        ["ω = 2πT", "ω = 2π/T", "ω = T/(2π)", "ω = π/T"],
        ["ω = 2πT", "ω = 2π/T", "ω = T/(2π)", "ω = π/T"],
        "B", "easy", "factual",
        "ω = 2π/T.",
        "ω = 2π/T।",
    ),
    q(
        "A particle moves with constant angular speed 4 rad/s in a circle of radius 0.5 m. Centripetal acceleration is:",
        "0.5 m ব্যাসার্ধের বৃত্তে 4 rad/s সমকৌণিক বেগে কেন্দ্রমুখী ত্বরণ—",
        ["2 m/s²", "4 m/s²", "8 m/s²", "16 m/s²"],
        ["2 m/s²", "4 m/s²", "8 m/s²", "16 m/s²"],
        "C", "medium", "numerical",
        "a = ω²r = 16·0.5 = 8 m/s².",
        "a = ω²r = 8 m/s²।",
    ),
    q(
        "In uniform circular motion, which is true? (i) speed is constant (ii) velocity is constant (iii) acceleration is nonzero",
        "সুষম বৃত্তীয় গতিতে কোনটি সত্য? (i) গতিবেগ ধ্রুব (ii) বেগ ধ্রুব (iii) ত্বরণ অশূন্য",
        ["i, ii only", "i, iii only", "ii, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল i, iii", "কেবল ii, iii", "i, ii ও iii"],
        "B", "medium", "conceptual",
        "Speed is constant but direction changes, so velocity changes and centripetal acceleration is nonzero.",
        "গতিবেগ ধ্রুব কিন্তু দিক বদলায়; ত্বরণ অশূন্য।",
    ),
    q(
        "Relative velocity of A w.r.t. B is defined as:",
        "B-এর সাপেক্ষে A-এর আপেক্ষিক বেগ—",
        ["v_A + v_B", "v_A − v_B", "v_B − v_A", "|v_A| − |v_B|"],
        ["v_A + v_B", "v_A − v_B", "v_B − v_A", "|v_A| − |v_B|"],
        "B", "easy", "factual",
        "v_AB = v_A − v_B.",
        "v_AB = v_A − v_B।",
    ),
    q(
        "A particle in a horizontal circle of radius 2 m has period 2 s. Magnitude of its acceleration is (π² ≈ 10):",
        "2 m ব্যাসার্ধের অনুভূমিক বৃত্তে পর্যায়কাল 2 s হলে ত্বরণের মান (π² ≈ 10)—",
        ["5 m/s²", "10 m/s²", "20 m/s²", "40 m/s²"],
        ["5 m/s²", "10 m/s²", "20 m/s²", "40 m/s²"],
        "C", "medium", "numerical",
        "ω = 2π/T = π; a = ω²r = π²·2 ≈ 20 m/s².",
        "a = (2π/T)² · r ≈ 20 m/s²।",
    ),
    q(
        "Variable speed and variable acceleration: which are true? (i) both may change with time (ii) both are vector quantities (iii) neither changes with time",
        "অসমবেগ ও অসমত্বরণ সম্পর্কে— (i) সময়ের সাথে ভিন্ন হতে পারে (ii) উভয়ই ভেক্টর (iii) সময়ের সাথে পরিবর্তন হয় না",
        ["i, ii only", "i, iii only", "ii, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল i, iii", "কেবল ii, iii", "i, ii ও iii"],
        "A", "easy", "conceptual",
        "(i) and (ii) hold; (iii) contradicts the meaning of variable.",
        "(i) ও (ii) সত্য; (iii) মিথ্যা।",
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
    counts["hm2_27_ch09_t01"] = write_topic("hm2_27_ch09_t01", T01)["count"]
    counts["hm2_27_ch09_t02"] = write_topic("hm2_27_ch09_t02", T02)["count"]
    counts["hm2_27_ch09_t03"] = write_topic("hm2_27_ch09_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm2_27_ch09",
        "title_en": "Motion of Particles in a Plane",
        "title_bn": "সমতলে বস্তুকণার গতি",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{i}_pdf{i+6}.png" for i in range(303, 311)],
        "topics": {
            "hm2_27_ch09_t01": {
                "title_en": "Displacement, velocity and acceleration",
                "title_bn": "সরণ, বেগ ও ত্বরণ",
                "udvash_types": [
                    "v=u+at; s=ut+(1/2)at²; v²=u²+2as",
                    "distance in nth second; free-fall depths",
                    "uniform acceleration car/bullet problems",
                    "successive equal distances time ratios; half-speed wall penetration",
                ],
                "count": 20,
            },
            "hm2_27_ch09_t02": {
                "title_en": "Projectile motion",
                "title_bn": "প্রাসের গতি",
                "udvash_types": [
                    "parabolic path; R=(u² sin 2α)/g; max range at 45°",
                    "H=u²sin²α/(2g); T=2u sin α/g; apex horizontal velocity",
                    "R=4H at 45°; complementary angles same range",
                    "trajectory y=x tan α(1−x/R); balloon/vertical throw",
                ],
                "count": 20,
            },
            "hm2_27_ch09_t03": {
                "title_en": "Relative and circular motion",
                "title_bn": "আপেক্ষিক ও বৃত্তীয় গতি",
                "udvash_types": [
                    "v_AB=v_A−v_B; max/min relative speed; 90° case",
                    "throw from moving car; river crossing drift; colliding trains",
                    "centripetal a=v²/r=ω²r; v=ωr; ω=2π/T",
                    "uniform circular motion: constant speed, changing velocity",
                ],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "garbled_stems": "Noisy OCR on pp. 303–310 reconstructed from answer-key algebra and standard board forms",
            "figure_only_items": "Figure-dependent stems (v–t graphs, river diagrams) rewritten as self-contained text MCQs",
            "broken_option_glyphs": "Fraction/√/degree glyphs often unreadable; replaced with closed-form HSC standards",
            "thin_circular_coverage": "Printed MCQs heavily relative/projectile/kinematics; circular motion largely HSC-accurate authored supplements",
        },
        "low_confidence": [
            "OCR on pp. 303–307 noisy; column text and solution lines used to reconstruct kinematics/projectile stems.",
            "Circular motion thinner in Udvash MCQ span; supplemented with accurate HSC plane-motion items.",
            "Inline math stored as plain text (√, ², α, ω, m/s²) for JSONL.",
            "Practice-test / creative CQ pages (308+) used only for formula cross-checks, not as MCQ sources.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm2_ch09.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
        "math2_progress": {
            "topics_complete": "27/30",
            "note": "Ch09 continues higher_mathematics 2nd paper after Ch01–Ch08 (480Q); remaining Ch10 only",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch09_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
