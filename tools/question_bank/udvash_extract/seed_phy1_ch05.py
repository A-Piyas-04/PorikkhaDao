#!/usr/bin/env python3
"""Seed Physics 1st Paper Ch5 (Work, Power and Energy) bilingual MCQs.

Curated from Udvash HSC Question Bank 2026 printed pages 163–174 (OCR + HSC reconstruction).
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
    "physics p1 ch05; curated bilingual"
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
# t01 Work and kinetic energy / কাজ ও গতিশক্তি
# ---------------------------------------------------------------------------
T01 = [
    q(
        "A person carries a 10 kg bag 10 m along a horizontal path. Work done by gravity is:",
        "এক ব্যক্তি ১০ kg ভরের ব্যাগ নিয়ে সমতল পথে ১০ m অতিক্রম করলে অভিকর্ষ বল দ্বারা কাজ কত?",
        ["100 J", "980 J", "9.8 J", "0 J"],
        ["100 J", "980 J", "9.8 J", "0 J"],
        "D", "easy", "numerical",
        "Gravity is vertical while displacement is horizontal, so θ = 90° and W = mg s cos 90° = 0.",
        "অভিকর্ষ উল্লম্ব ও সরণ অনুভূমিক; θ = ৯০° হলে W = ০।",
    ),
    q(
        "Work done by a centripetal force on a particle in uniform circular motion is:",
        "কেন্দ্রমুখী বল দ্বারা কৃতকাজ—",
        ["Zero", "Positive", "Negative", "Infinite"],
        ["শূন্য", "ধনাত্মক", "ঋণাত্মক", "অসীম"],
        "A", "easy", "conceptual",
        "Centripetal force is always perpendicular to displacement, so W = 0.",
        "কেন্দ্রমুখী বল সরণের লম্ব; তাই W = ০।",
    ),
    q(
        "According to the work–energy theorem, net work equals the change in:",
        "কাজ–শক্তি উপপাদ্য অনুসারে নিট কাজ নিচের কোনটির পরিবর্তনের সমান?",
        ["Momentum", "Potential energy", "Temperature", "Kinetic energy"],
        ["ভরবেগ", "বিভবশক্তি", "তাপমাত্রা", "গতিশক্তি"],
        "D", "easy", "factual",
        "W_net = ΔK.",
        "W_net = ΔK।",
    ),
    q(
        "If linear momentum of a body increases by 50%, its kinetic energy increases by:",
        "একটি বস্তুর রৈখিক ভরবেগ ৫০% বৃদ্ধি করলে গতিশক্তি কত % বৃদ্ধি পায়?",
        ["25%", "50%", "125%", "225%"],
        ["২৫%", "৫০%", "১২৫%", "২২৫%"],
        "C", "medium", "numerical",
        "p′ = 1.5p ⇒ K′/K = (1.5)² = 2.25 ⇒ increase = 125%.",
        "p′ = ১.৫p ⇒ K′ = ২.২৫K ⇒ বৃদ্ধি ১২৫%।",
    ),
    q(
        "A body of mass m has kinetic energy E. Its momentum magnitude is:",
        "m ভরের কোনো বস্তুর গতিশক্তি E হলে এর ভরবেগের মান:",
        ["m√(2E)", "√(2mE)", "√(2E/m)", "2mE"],
        ["m√(2E)", "√(2mE)", "√(2E/m)", "2mE"],
        "B", "easy", "factual",
        "K = p²/(2m) ⇒ p = √(2mE).",
        "K = p²/(2m) ⇒ p = √(2mE)।",
    ),
    q(
        "For a fixed mass, kinetic energy is proportional to:",
        "নির্দিষ্ট ভরের বস্তুর গতিশক্তি এর ভরবেগের—",
        ["Square", "Square root", "Inverse square", "Inverse square root"],
        ["বর্গের সমানুপাতিক", "বর্গমূলের সমানুপাতিক", "বর্গের ব্যস্তানুপাতিক", "বর্গমূলের ব্যস্তানুপাতিক"],
        "A", "easy", "conceptual",
        "K = p²/(2m) ⇒ K ∝ p².",
        "K = p²/(2m) ⇒ K ∝ p²।",
    ),
    q(
        "Mass and speed of a body both become 4 times. Kinetic energy becomes how many times?",
        "একটি বস্তুর ভর ও বেগ উভয়ই ৪ গুণ হলে এর গতিশক্তি কত গুণ হবে?",
        ["64", "32", "16", "4"],
        ["৬৪", "৩২", "১৬", "৪"],
        "A", "medium", "numerical",
        "K′/K = (4m)(4v)²/(m v²) = 4 × 16 = 64.",
        "K′/K = ৪ × ১৬ = ৬৪।",
    ),
    q(
        "If kinetic energy becomes 9 times the initial value, speed becomes how many times?",
        "গতিশক্তি আদির ৯ গুণ হলে বেগ আদির কত গুণ হবে?",
        ["3", "9", "√3", "81"],
        ["৩", "৯", "√৩", "৮১"],
        "A", "easy", "numerical",
        "K ∝ v² ⇒ v′/v = √9 = 3.",
        "K ∝ v² ⇒ v′/v = √৯ = ৩।",
    ),
    q(
        "Work done by a force is maximum when the angle between force and displacement is:",
        "বল ও সরণের মধ্যবর্তী কোণ কত হলে কাজের মান সর্বাধিক?",
        ["0°", "45°", "90°", "180°"],
        ["০°", "৪৫°", "৯০°", "১৮০°"],
        "A", "easy", "conceptual",
        "W = Fs cos θ is maximum at θ = 0° (cos 0° = 1).",
        "W = Fs cos θ; θ = ০° তে সর্বাধিক।",
    ),
    q(
        "Work against a force occurs when the angle θ between force and displacement satisfies:",
        "বলের বিরুদ্ধে কাজ সম্পন্ন হয় যখন বল ও সরণের মধ্যবর্তী কোণ θ এর মান—",
        ["0° ≤ θ < 90°", "0° < θ ≤ 90°", "90° < θ ≤ 180°", "90° ≤ θ < 180°"],
        ["০° ≤ θ < ৯০°", "০° < θ ≤ ৯০°", "৯০° < θ ≤ ১৮০°", "৯০° ≤ θ < ১৮০°"],
        "C", "medium", "conceptual",
        "cos θ < 0 for 90° < θ ≤ 180°, so work is negative (against the force).",
        "৯০° < θ ≤ ১৮০° তে cos θ ঋণাত্মক; কাজ বলের বিরুদ্ধে।",
    ),
    q(
        "A force F = (5x² − x + 1) N acts along x. Work from x = 0 to x = 3 m is:",
        "F = (5x² − x + 1) N বল x = ০ থেকে x = ৩ m পর্যন্ত সরণে কৃতকাজ কত?",
        ["43.5 J", "43 J", "42 J", "40.5 J"],
        ["৪৩.৫ J", "৪৩ J", "৪২ J", "৪০.৫ J"],
        "A", "hard", "numerical",
        "W = ∫₀³ (5x² − x + 1) dx = [5x³/3 − x²/2 + x]₀³ = 45 − 4.5 + 3 = 43.5 J.",
        "W = ∫₀³(5x² − x + 1) dx = ৪৩.৫ J।",
    ),
    q(
        "A 50 kg person with a 50 kg load descends a 4 m ladder inclined at 60° to a vertical wall. Work done by gravity is approximately:",
        "৫০ kg ভরের বোঝা মাথায় নিয়ে ৫০ kg ভরের এক ব্যক্তি খাড়া দেয়ালের সাথে ৬০° কোণে আনত ৪ m মই বেয়ে নামলে কাজের পরিমাণ প্রায়:",
        ["3920 J", "1960 J", "200 J", "100 J"],
        ["৩৯২০ J", "১৯৬০ J", "২০০ J", "১০০ J"],
        "B", "hard", "numerical",
        "Vertical drop h = 4 cos 60° = 2 m; W = (50+50) g h = 100 × 9.8 × 2 = 1960 J.",
        "উল্লম্ব সরণ h = ৪ cos ৬০° = ২ m; W = ১০০ × ৯.৮ × ২ = ১৯৬০ J।",
    ),
    q(
        "Two moving bodies of masses 4 kg and 9 kg have equal kinetic energy. Ratio of their linear momenta is:",
        "৪ kg ও ৯ kg ভরের দুটি গতিশীল বস্তুর গতিশক্তি একই হলে রৈখিক ভরবেগের অনুপাত:",
        ["4 : 9", "2 : 3", "9 : 4", "3 : 2"],
        ["৪ : ৯", "২ : ৩", "৯ : ৪", "৩ : ২"],
        "B", "medium", "numerical",
        "p = √(2mK); equal K ⇒ p₁ : p₂ = √m₁ : √m₂ = 2 : 3.",
        "p = √(2mK) ⇒ p₁ : p₂ = √৪ : √৯ = ২ : ৩।",
    ),
    q(
        "Kinetic energy of a rotating rigid body is:",
        "ঘূর্ণায়মান বস্তুর গতিশক্তি কোনটি?",
        ["(1/2) I ω", "(1/2) I ω²", "I ω", "I ω²"],
        ["(১/২) I ω", "(১/২) I ω²", "I ω", "I ω²"],
        "B", "easy", "factual",
        "Rotational KE = (1/2) I ω².",
        "ঘূর্ণন গতিশক্তি = (১/২) I ω²।",
    ),
    q(
        "If angular speed of a rotating body increases by 10%, rotational KE increases by about:",
        "ঘূর্ণায়মান বস্তুর কৌণিক বেগ ১০% বৃদ্ধি করলে ঘূর্ণন গতিশক্তি বৃদ্ধি পায় প্রায়—",
        ["10%", "20%", "21%", "40%"],
        ["১০%", "২০%", "২১%", "৪০%"],
        "C", "medium", "numerical",
        "K ∝ ω² ⇒ factor (1.1)² = 1.21 ⇒ +21%.",
        "K ∝ ω² ⇒ (১.১)² = ১.২১ ⇒ +২১%।",
    ),
    q(
        "A brass sphere and a tennis ball of equal volume have equal momenta. Then:",
        "সমআয়তনের পিতলের গোলক ও টেনিস বলের ভরবেগ সমান হলে—",
        ["Tennis ball has larger KE", "Brass sphere has larger KE", "Both have equal KE", "Neither has KE"],
        ["টেনিস বলের গতিশক্তি বেশি", "পিতলের গোলকের গতিশক্তি বেশি", "উভয়ের গতিশক্তি সমান", "কোনোটিরই গতিশক্তি নেই"],
        "A", "medium", "conceptual",
        "K = p²/(2m); equal p and smaller m (tennis) ⇒ larger KE.",
        "K = p²/(2m); সমান p ও কম ভর ⇒ টেনিস বলের KE বেশি।",
    ),
    q(
        "A person applies 49 N horizontally and displaces a block by 2 m. Work done is (g = 9.8 m s⁻²):",
        "এক ব্যক্তি অনুভূমিক তলে ৪৯ N বল প্রয়োগে ২ m সরণ ঘটালে কৃতকাজ (g = ৯.৮ m s⁻²):",
        ["49 J", "96.8 J", "98 J", "9.8 J"],
        ["৪৯ J", "৯৬.৮ J", "৯৮ J", "৯.৮ J"],
        "C", "easy", "numerical",
        "W = F s = 49 × 2 = 98 J.",
        "W = F s = ৪৯ × ২ = ৯৮ J।",
    ),
    q(
        "A 10 N force displaces a body 10 m at 30° to the force. Work done is approximately:",
        "১০ N বল প্রয়োগে বলের সাথে ৩০° কোণে ১০ m সরণ হলে কৃতকাজ প্রায়:",
        ["86.60 J", "100 J", "50 J", "25 J"],
        ["৮৬.৬০ J", "১০০ J", "৫০ J", "২৫ J"],
        "A", "medium", "numerical",
        "W = F s cos 30° = 10 × 10 × (√3/2) ≈ 86.60 J.",
        "W = ১০ × ১০ × cos ৩০° ≈ ৮৬.৬০ J।",
    ),
    q(
        "Work is zero if:",
        "কাজের মান শূন্য হবে, যদি—",
        ["Only displacement is zero", "Only force opposes displacement", "Displacement is zero or θ = 90°", "Force is always nonzero"],
        ["কেবল সরণ শূন্য হলে", "কেবল বল সরণের বিপরীতে হলে", "সরণ শূন্য বা θ = ৯০° হলে", "বল সবসময় অশূন্য হলে"],
        "C", "easy", "conceptual",
        "W = F s cos θ = 0 when s = 0 or θ = 90°.",
        "s = ০ বা θ = ৯০° হলে W = ০।",
    ),
    q(
        "If a bullet’s speed becomes three times, its kinetic energy becomes how many times?",
        "একটি বুলেটের বেগ তিনগুণ হলে গতিশক্তি কতগুণ হবে?",
        ["2 times", "3 times", "9 times", "27 times"],
        ["২ গুণ", "৩ গুণ", "৯ গুণ", "২৭ গুণ"],
        "C", "easy", "numerical",
        "K ∝ v² ⇒ (3)² = 9 times.",
        "K ∝ v² ⇒ ৩² = ৯ গুণ।",
    ),
]


# ---------------------------------------------------------------------------
# t02 Potential energy and conservation / বিভবশক্তি ও শক্তির সংরক্ষণ
# ---------------------------------------------------------------------------
T02 = [
    q(
        "Stretching a spring stores which kind of energy?",
        "স্প্রিংকে প্রসারিত করলে এর মধ্যে কোন ধরনের শক্তি সঞ্চিত হয়?",
        ["Heat energy", "Kinetic energy", "Potential energy", "Chemical energy"],
        ["তাপশক্তি", "গতিশক্তি", "বিভবশক্তি", "রাসায়নিক শক্তি"],
        "C", "easy", "factual",
        "Elastic potential energy U = (1/2) k x² is stored in a stretched spring.",
        "প্রসারিত স্প্রিং-এ স্থিতিস্থাপক বিভবশক্তি সঞ্চিত হয়।",
    ),
    q(
        "Potential energy stored when a spring of force constant k is stretched by x is:",
        "k বল ধ্রুবাঙ্কবিশিষ্ট স্প্রিং-এর মুক্ত প্রান্তের x সরণে সঞ্চিত বিভবশক্তি:",
        ["U = kx", "U = kx²", "U = (1/2) kx²", "U = (1/2) kx"],
        ["U = kx", "U = kx²", "U = (১/২) kx²", "U = (১/২) kx"],
        "C", "easy", "factual",
        "U = (1/2) k x².",
        "U = (১/২) k x²।",
    ),
    q(
        "A 90 N m⁻¹ spring is compressed by 4 cm. Stored energy is:",
        "৯০ N m⁻¹ বল ধ্রুবাঙ্কের স্প্রিংকে ৪ cm সংকুচিত করলে সঞ্চিত শক্তি:",
        ["0.072 J", "0.078 J", "0.082 J", "0.086 J"],
        ["০.০৭২ J", "০.০৭৮ J", "০.০৮২ J", "০.০৮৬ J"],
        "A", "medium", "numerical",
        "U = (1/2) × 90 × (0.04)² = 0.072 J.",
        "U = ½ × ৯০ × (০.০৪)² = ০.০৭২ J।",
    ),
    q(
        "Which is an example of a non-conservative force?",
        "অসংরক্ষণশীল বলের উদাহরণ কোনটি?",
        ["Gravitational force", "Electric force", "Magnetic force", "Friction force"],
        ["অভিকর্ষ বল", "বৈদ্যুতিক বল", "চৌম্বক বল", "ঘর্ষণ বল"],
        "D", "easy", "factual",
        "Friction is path-dependent and dissipative; it is non-conservative.",
        "ঘর্ষণ পথনির্ভর ও অপচয়কারী; এটি অসংরক্ষণশীল।",
    ),
    q(
        "Under a non-conservative force:",
        "অসংরক্ষণশীল বলের ক্রিয়ায়—",
        ["Net work in a closed loop is zero", "Work is path-independent", "Work is fully recoverable", "Mechanical energy is not conserved"],
        ["পূর্ণচক্রে কাজ শূন্য", "কাজ গতিপথনির্ভর নয়", "কাজ পুনরুদ্ধারযোগ্য", "যান্ত্রিক শক্তির নিত্যতা থাকে না"],
        "D", "medium", "conceptual",
        "Non-conservative forces can convert mechanical energy to heat, etc.",
        "অসংরক্ষণশীল বলে যান্ত্রিক শক্তি তাপ ইত্যাদিতে রূপান্তরিত হতে পারে।",
    ),
    q(
        "For a conservative force, which statement is true?",
        "সংরক্ষণশীল বলের ক্ষেত্রে কোনটি সত্য?",
        ["Work depends on path", "Closed-loop work is nonzero", "Mechanical energy is conserved", "Friction is an example"],
        ["কাজ পথনির্ভর", "পূর্ণচক্রে কাজ অশূন্য", "যান্ত্রিক শক্তি সংরক্ষিত", "ঘর্ষণ এর উদাহরণ"],
        "C", "easy", "conceptual",
        "Conservative forces: path-independent work, zero closed-loop work, mechanical energy conserved.",
        "সংরক্ষণশীল বলে যান্ত্রিক শক্তি সংরক্ষিত থাকে।",
    ),
    q(
        "A body falls freely from 10 m. At 8 m above ground, ratio of KE to PE is:",
        "ভূমি থেকে ১০ m উচ্চতায় থাকা বস্তু বিনা বাধায় পড়লে ভূমি থেকে ৮ m উচ্চতায় গতিশক্তি ও স্থিতিশক্তির অনুপাত:",
        ["1 : 4", "4 : 1", "5 : 4", "4 : 5"],
        ["১ : ৪", "৪ : ১", "৫ : ৪", "৪ : ৫"],
        "A", "medium", "numerical",
        "Lost PE = mg(2); remaining PE = mg(8); KE:PE = 2:8 = 1:4.",
        "KE = mg×২, PE = mg×৮ ⇒ KE:PE = ১:৪।",
    ),
    q(
        "A body falls freely from 30 m. At what height above ground is KE twice PE?",
        "৩০ m উচ্চতা থেকে বিনা বাধায় পড়লে ভূমি থেকে কত উচ্চতায় গতিশক্তি বিভবশক্তির দ্বিগুণ?",
        ["10 m", "15 m", "20 m", "30 m"],
        ["১০ m", "১৫ m", "২০ m", "৩০ m"],
        "A", "hard", "numerical",
        "mg(30 − x) = 2 mg x ⇒ 30 = 3x ⇒ x = 10 m.",
        "mg(৩০ − x) = ২ mgx ⇒ x = ১০ m।",
    ),
    q(
        "A spring stores energy U when stretched 2 cm. When stretched 10 cm, energy is:",
        "স্প্রিংকে ২ cm প্রসারিত করলে শক্তি U; ১০ cm প্রসারিত করলে শক্তি কত?",
        ["5U", "10U", "25U", "50U"],
        ["৫U", "১০U", "২৫U", "৫০U"],
        "C", "medium", "numerical",
        "U ∝ x²; stretch factor 5 ⇒ energy factor 25.",
        "U ∝ x²; সরণ ৫ গুণ ⇒ শক্তি ২৫ গুণ।",
    ),
    q(
        "Which is a conservative force?",
        "নিচের কোনটি সংরক্ষণশীল বলের উদাহরণ?",
        ["Friction", "Viscous force", "Gravitational force", "Impulse force"],
        ["ঘর্ষণ বল", "সান্দ্র বল", "অভিকর্ষীয় বল", "ঘাত বল"],
        "C", "easy", "factual",
        "Gravity is a classic conservative force.",
        "অভিকর্ষ একটি ধ্রুপদী সংরক্ষণশীল বল।",
    ),
    q(
        "A body falls from 60 m. Height above ground where PE is half of KE:",
        "৬০ m উচ্চতা থেকে বিনা বাধায় পড়লে ভূমি হতে কত উচ্চতায় বিভবশক্তি গতিশক্তির অর্ধেক?",
        ["10 m", "20 m", "30 m", "40 m"],
        ["১০ m", "২০ m", "৩০ m", "৪০ m"],
        "B", "hard", "numerical",
        "mgx = (1/2) mg(60 − x) ⇒ 2x = 60 − x ⇒ x = 20 m.",
        "mgx = ½ mg(৬০ − x) ⇒ x = ২০ m।",
    ),
    q(
        "A body acquires energy due to its position. That energy is:",
        "কোনো বস্তু তার অবস্থানের কারণে কী অর্জন করে?",
        ["Potential energy", "Kinetic energy", "Work", "Power"],
        ["বিভবশক্তি", "গতিশক্তি", "কাজ", "ক্ষমতা"],
        "A", "easy", "factual",
        "Position-dependent stored energy is potential energy.",
        "অবস্থানজনিত সঞ্চিত শক্তিই বিভবশক্তি।",
    ),
    q(
        "A 200 g body falls from 10 m. KE just before hitting ground (g = 9.8) is:",
        "২০০ g ভরের বস্তু ১০ m উপর থেকে পড়লে ভূমি স্পর্শের পূর্ব মুহূর্তে গতিশক্তি (g = ৯.৮):",
        ["19.6 J", "39.2 J", "78.4 J", "9.8 J"],
        ["১৯.৬ J", "৩৯.২ J", "৭৮.৪ J", "৯.৮ J"],
        "A", "medium", "numerical",
        "K = mgh = 0.2 × 9.8 × 10 = 19.6 J.",
        "K = mgh = ০.২ × ৯.৮ × ১০ = ১৯.৬ J।",
    ),
    q(
        "A uniform rod of length 1.5 m and mass 2 kg is raised from horizontal to vertical. Work done is about:",
        "১.৫ m দীর্ঘ ও ২ kg ভরের রডকে অনুভূমিক হতে উল্লম্ব অবস্থায় নিতে কাজ প্রায়:",
        ["0 J", "14 J", "29 J", "44 J"],
        ["০ J", "১৪ J", "২৯ J", "৪৪ J"],
        "B", "hard", "numerical",
        "CM rises by L/2 = 0.75 m; W = mgh = 2 × 9.8 × 0.75 ≈ 14.7 J ≈ 14 J.",
        "ভরকেন্দ্রের সরণ L/২ = ০.৭৫ m; W ≈ ১৪.৭ J ≈ ১৪ J।",
    ),
    q(
        "Dimensions of potential energy are:",
        "বিভবশক্তির মাত্রা কোনটি?",
        ["ML²T⁻²", "MLT⁻¹", "MLT⁻²", "M²LT⁻²"],
        ["ML²T⁻²", "MLT⁻¹", "MLT⁻²", "M²LT⁻²"],
        "A", "easy", "factual",
        "Energy has dimensions [ML²T⁻²].",
        "শক্তির মাত্রা [ML²T⁻²]।",
    ),
    q(
        "A body falls from 20 m (g = 10). At 5 m above ground, PE : KE is:",
        "২০ m উচ্চতা থেকে পড়লে (g = ১০) ভূমি হতে ৫ m উঁচুতে বিভবশক্তি ও গতিশক্তির অনুপাত:",
        ["1 : 2", "1 : 3", "1 : 4", "2 : 1"],
        ["১ : ২", "১ : ৩", "১ : ৪", "২ : ১"],
        "B", "medium", "numerical",
        "PE = mg×5, KE = mg×15 ⇒ PE:KE = 1:3.",
        "PE = mg×৫, KE = mg×১৫ ⇒ ১:৩।",
    ),
    q(
        "Two springs of 200 N m⁻¹ and 300 N m⁻¹ in series have equivalent k:",
        "২০০ N m⁻¹ ও ৩০০ N m⁻¹ দুটি স্প্রিং শ্রেণি সমবায়ে সমতুল্য বল ধ্রুবাঙ্ক:",
        ["100 N m⁻¹", "120 N m⁻¹", "250 N m⁻¹", "500 N m⁻¹"],
        ["১০০ N m⁻¹", "১২০ N m⁻¹", "২৫০ N m⁻¹", "৫০০ N m⁻¹"],
        "B", "medium", "numerical",
        "1/k = 1/200 + 1/300 ⇒ k = 120 N m⁻¹.",
        "১/k = ১/২০০ + ১/৩০০ ⇒ k = ১২০ N m⁻¹।",
    ),
    q(
        "A 50 kg mass raised 150 m: which statements are correct? (i) weight 490 N (ii) work 7.35×10⁴ J (iii) work is against gravity",
        "৫০ kg ভর ১৫০ m উঁচুতে উঠালে—(i) ওজন ৪৯০ N (ii) কাজ ৭.৩৫×১০⁴ J (iii) অভিকর্ষের বিরুদ্ধে কাজ। সঠিক:",
        ["i, ii only", "ii, iii only", "i, iii only", "i, ii, iii"],
        ["কেবল i, ii", "কেবল ii, iii", "কেবল i, iii", "i, ii, iii"],
        "D", "medium", "application",
        "W = mg = 490 N; work = mgh = 7.35×10⁴ J; lifting is against gravity. All three true.",
        "তিনটিই সত্য: ওজন ৪৯০ N, কাজ ৭.৩৫×১০⁴ J, অভিকর্ষের বিরুদ্ধে।",
    ),
    q(
        "Which quantity has the same dimensions as work?",
        "নিচের জোড়াগুলোর মধ্যে কোনটির মাত্রা একই?",
        ["Work and power", "Work and energy", "Force and work", "Force and energy"],
        ["কাজ ও ক্ষমতা", "কাজ ও শক্তি", "বল ও কাজ", "বল ও শক্তি"],
        "B", "easy", "factual",
        "Work and energy both have dimensions [ML²T⁻²] and unit joule.",
        "কাজ ও শক্তি উভয়ের মাত্রা ও একক একই (জুল)।",
    ),
    q(
        "An ideal spring’s U vs x graph is:",
        "আদর্শ স্প্রিং-এর বিভবশক্তি (U) বনাম সম্প্রসারণ (x) লেখচিত্র কেমন?",
        ["Straight line through origin", "Upward parabola through origin", "Circle", "Horizontal line"],
        ["মূলবিন্দুগামী সরলরেখা", "মূলবিন্দুগামী ঊর্ধ্বমুখী পরাবৃত্ত", "বৃত্ত", "অনুভূমিক রেখা"],
        "B", "medium", "conceptual",
        "U = (1/2) k x² is a parabola opening upward through the origin.",
        "U = ½kx² ⇒ মূলবিন্দুগামী ঊর্ধ্বমুখী পরাবৃত্ত।",
    ),
]


# ---------------------------------------------------------------------------
# t03 Power and efficiency / ক্ষমতা ও দক্ষতা
# ---------------------------------------------------------------------------
T03 = [
    q(
        "10 W power means:",
        "১০ W ক্ষমতা বলতে বোঝায়—",
        ["10 J of work in 1 s", "5 J of work in 2 s", "2 J of work in 5 s", "1 J of work in 10 s"],
        ["১ s এ কাজ ১০ J", "২ s এ কাজ ৫ J", "৫ s এ কাজ ২ J", "১০ s এ কাজ ১ J"],
        "A", "easy", "factual",
        "P = W/t; 10 W = 10 J/s.",
        "P = W/t; ১০ W = ১০ J/s।",
    ),
    q(
        "Dimensions of power are:",
        "ক্ষমতার মাত্রা কোনটি?",
        ["ML²T⁻²", "ML²T⁻³", "MLT⁻²", "MLT⁻³"],
        ["ML²T⁻²", "ML²T⁻³", "MLT⁻²", "MLT⁻³"],
        "B", "easy", "factual",
        "Power = energy/time ⇒ [ML²T⁻³].",
        "ক্ষমতা = শক্তি/সময় ⇒ [ML²T⁻³]।",
    ),
    q(
        "Relation between horsepower and watt is:",
        "অশ্বক্ষমতা (HP) ও ওয়াটের মধ্যে সম্পর্ক:",
        ["1 HP = 467 W", "1 HP = 550 W", "1 HP = 674 W", "1 HP = 746 W"],
        ["১ HP = ৪৬৭ W", "১ HP = ৫৫০ W", "১ HP = ৬৭৪ W", "১ HP = ৭৪৬ W"],
        "D", "easy", "factual",
        "By definition, 1 HP = 746 W (metric electrical/mechanical convention used in HSC).",
        "১ HP = ৭৪৬ W।",
    ),
    q(
        "1 kWh equals:",
        "১ kW-h সমান—",
        ["1000 J", "3600 J", "6000 J", "3.6 × 10⁶ J"],
        ["১০০০ J", "৩৬০০ J", "৬০০০ J", "৩.৬ × ১০⁶ J"],
        "D", "easy", "factual",
        "1 kWh = 1000 × 3600 = 3.6 × 10⁶ J.",
        "১ kWh = ৩.৬ × ১০⁶ J।",
    ),
    q(
        "A pump has useful power 3 kW and efficiency 75%. Input power is:",
        "একটি পাম্পের কার্যকর ক্ষমতা ৩ kW ও কর্মদক্ষতা ৭৫% হলে প্রকৃত (ইনপুট) ক্ষমতা:",
        ["4 kW", "3 kW", "2.25 kW", "1.25 kW"],
        ["৪ kW", "৩ kW", "২.২৫ kW", "১.২৫ kW"],
        "A", "medium", "numerical",
        "η = P_out/P_in ⇒ P_in = 3/0.75 = 4 kW.",
        "P_in = ৩/০.৭৫ = ৪ kW।",
    ),
    q(
        "A crane lifts 500 kg at constant speed 0.20 m s⁻¹. Power of the crane is:",
        "ক্রেন দ্বারা ৫০০ kg ভর ০.২০ m s⁻¹ সমদ্রুতিতে তুললে ক্রেনের ক্ষমতা:",
        ["980 W", "1050 W", "2000 W", "3000 W"],
        ["৯৮০ W", "১০৫০ W", "২০০০ W", "৩০০০ W"],
        "A", "medium", "numerical",
        "P = F v = mg v = 500 × 9.8 × 0.2 = 980 W.",
        "P = mgv = ৫০০ × ৯.৮ × ০.২ = ৯৮০ W।",
    ),
    q(
        "Units of power include:",
        "ক্ষমতার একক হলো—",
        ["Only watt", "J s⁻¹ and watt only", "Watt and erg s⁻¹ only", "J s⁻¹, watt and erg s⁻¹"],
        ["কেবল ওয়াট", "কেবল J s⁻¹ ও ওয়াট", "কেবল ওয়াট ও erg s⁻¹", "J s⁻¹, ওয়াট ও erg s⁻¹"],
        "D", "easy", "factual",
        "Power units: watt, J/s, and CGS erg/s.",
        "ক্ষমতার একক: ওয়াট, J/s এবং erg/s।",
    ),
    q(
        "If a machine applies force F and moves a body at speed v, power is:",
        "যন্ত্র কর্তৃক F বল প্রয়োগে বস্তু v বেগে গতিশীল হলে ক্ষমতা:",
        ["P = F/v", "P = F v²", "P = F v", "P = F² v"],
        ["P = F/v", "P = F v²", "P = F v", "P = F² v"],
        "C", "easy", "factual",
        "Instantaneous power P = F · v = F v when force and velocity are parallel.",
        "সমান্তরাল হলে P = F v।",
    ),
    q(
        "Kilowatt-hour is a unit of:",
        "কিলোওয়াট-ঘণ্টা নিচের কোন রাশির একক?",
        ["Power", "Energy", "Force", "Impulse"],
        ["ক্ষমতা", "শক্তি", "বল", "বলের ঘাত"],
        "B", "easy", "factual",
        "kWh is energy (power × time).",
        "kWh = ক্ষমতা × সময় = শক্তি।",
    ),
    q(
        "Which energy/power unit relation is correct?",
        "শক্তি/ক্ষমতার একক সম্পর্কে কোনটি সঠিক?",
        ["1 W = 1 J N⁻¹", "1 J = 1 N s⁻²", "1 kWh = 3.6 × 10⁶ J", "1 erg = 10⁻⁵ J"],
        ["১ W = ১ J N⁻¹", "১ J = ১ N s⁻²", "১ kWh = ৩.৬ × ১০⁶ J", "১ erg = ১০⁻⁵ J"],
        "C", "medium", "factual",
        "1 kWh = 3.6 × 10⁶ J; also 1 erg = 10⁻⁷ J, 1 W = 1 J/s.",
        "১ kWh = ৩.৬ × ১০⁶ J সঠিক।",
    ),
    q(
        "85% efficient 2.5 kW pump lifts water 6.30 m. Mass lifted per minute is about:",
        "৮৫% দক্ষতাসম্পন্ন ২.৫ kW পাম্পে গড়ে ৬.৩০ m উচ্চতায় পানি উঠালে প্রতি মিনিটে ভর প্রায়:",
        ["2075 kg", "2065 kg", "2045 kg", "2025 kg"],
        ["২০৭৫ kg", "২০৬৫ kg", "২০৪৫ kg", "২০২৫ kg"],
        "B", "hard", "numerical",
        "0.85 × 2500 × 60 = m × 9.8 × 6.30 ⇒ m ≈ 2065 kg.",
        "০.৮৫ × ২৫০০ × ৬০ = m × ৯.৮ × ৬.৩ ⇒ m ≈ ২০৬৫ kg।",
    ),
    q(
        "Useful power of a machine that does 196 J of useful work in 2 s is:",
        "কোনো যন্ত্র ২ s এ ১৯৬ J উপযোগী কাজ করলে কার্যকর ক্ষমতা:",
        ["49 W", "98 W", "196 W", "392 W"],
        ["৪৯ W", "৯৮ W", "১৯৬ W", "৩৯২ W"],
        "B", "easy", "numerical",
        "P = W/t = 196/2 = 98 W.",
        "P = ১৯৬/২ = ৯৮ W।",
    ),
    q(
        "A boy of 20 kg climbs 20 steps of 25 cm each in 10 s. His power is about:",
        "২০ kg ভরের বালক ২৫ cm উচ্চতার ২০টি ধাপ ১০ s এ উঠলে ক্ষমতা প্রায়:",
        ["98 W", "49 W", "196 W", "10 W"],
        ["৯৮ W", "৪৯ W", "১৯৬ W", "১০ W"],
        "A", "medium", "numerical",
        "h = 20 × 0.25 = 5 m; P = mgh/t = 20 × 9.8 × 5 / 10 = 98 W.",
        "h = ৫ m; P = ২০ × ৯.৮ × ৫ / ১০ = ৯৮ W।",
    ),
    q(
        "A crane lifts twelve 50 kg loads to 16 m in 1 min. Approximate horsepower is:",
        "ক্রেন ৫০ kg ভরের ১২টি বস্তু ১৬ m উচ্চতায় ১ মিনিটে উঠালে অশ্বক্ষমতা প্রায়:",
        ["1.6 HP", "2.1 HP", "5.7 HP", "16.7 HP"],
        ["১.৬ HP", "২.১ HP", "৫.৭ HP", "১৬.৭ HP"],
        "B", "hard", "numerical",
        "P = (12 × 50 × 9.8 × 16)/60 ≈ 1568 W ≈ 1568/746 ≈ 2.1 HP.",
        "P ≈ ১৫৬৮ W ≈ ২.১ HP।",
    ),
    q(
        "Power can be expressed as:",
        "ক্ষমতার সমীকরণ—",
        ["Only P = W/t", "Only P = F·v", "P = W/t and P = F·v", "P = F/t only"],
        ["কেবল P = W/t", "কেবল P = F·v", "P = W/t এবং P = F·v", "কেবল P = F/t"],
        "C", "easy", "conceptual",
        "Average power W/t; instantaneous power F·v.",
        "গড় ক্ষমতা W/t; তাৎক্ষণিক ক্ষমতা F·v।",
    ),
    q(
        "If all supplied energy is wasted, efficiency is:",
        "প্রদত্ত শক্তি সম্পূর্ণটাই অপচয় হলে কর্মদক্ষতা:",
        ["100%", "50%", "0%", "Infinite"],
        ["১০০%", "৫০%", "০%", "অসীম"],
        "C", "easy", "conceptual",
        "η = useful/total = 0 when useful work is zero.",
        "উপযোগী কাজ শূন্য হলে η = ০।",
    ),
    q(
        "Force F = (3i + 2j − k) N and velocity v = (i + 2j + k) m s⁻¹. Power is:",
        "F = (3i + 2j − k) N ও v = (i + 2j + k) m s⁻¹ হলে ক্ষমতা:",
        ["4 W", "6 W", "8 W", "(4i + 4j) W"],
        ["৪ W", "৬ W", "৮ W", "(৪i + ৪j) W"],
        "B", "medium", "numerical",
        "P = F·v = 3 + 4 − 1 = 6 W.",
        "P = F·v = ৩ + ৪ − ১ = ৬ W।",
    ),
    q(
        "In the previous case, if the force acts for 2 s, work done is:",
        "উপরের বল ২ s ক্রিয়া করলে কৃতকাজ:",
        ["12 J", "16 J", "6 J", "8 J"],
        ["১২ J", "১৬ J", "৬ J", "৮ J"],
        "A", "medium", "numerical",
        "W = P t = 6 × 2 = 12 J.",
        "W = P t = ৬ × ২ = ১২ J।",
    ),
    q(
        "CGS unit of work is:",
        "CGS পদ্ধতিতে কাজের একক কোনটি?",
        ["Joule", "ft-poundal", "Erg", "N m"],
        ["জুল", "ফুট-পাউন্ডাল", "আর্গ", "N m"],
        "C", "easy", "factual",
        "CGS unit of work/energy is the erg.",
        "CGS-এ কাজের একক আর্গ (erg)।",
    ),
    q(
        "A motor does 100 J of useful work while consuming 125 J. Efficiency is:",
        "এক মোটর ১২৫ J শক্তি খরচ করে ১০০ J উপযোগী কাজ করলে দক্ষতা:",
        ["60%", "75%", "80%", "125%"],
        ["৬০%", "৭৫%", "৮০%", "১২৫%"],
        "C", "easy", "numerical",
        "η = 100/125 × 100% = 80%.",
        "η = ১০০/১২৫ × ১০০% = ৮০%।",
    ),
]


# ---------------------------------------------------------------------------
# t04 Collisions / সংঘর্ষ
# ---------------------------------------------------------------------------
T04 = [
    q(
        "In an inelastic collision, which is conserved?",
        "অস্থিতিস্থাপক সংঘর্ষে সংরক্ষিত হয়—",
        ["Kinetic energy", "Potential energy", "Angular momentum only always", "Linear momentum"],
        ["গতিশক্তি", "স্থিতিশক্তি", "কেবল কৌণিক ভরবেগ সর্বদা", "রৈখিক ভরবেগ"],
        "D", "easy", "factual",
        "Linear momentum is conserved (no external force); KE is not conserved in inelastic collisions.",
        "অস্থিতিস্থাপক সংঘর্ষে ভরবেগ সংরক্ষিত; গতিশক্তি সংরক্ষিত নয়।",
    ),
    q(
        "In a perfectly elastic collision:",
        "পূর্ণ স্থিতিস্থাপক সংঘর্ষে—",
        ["Only momentum is conserved", "Only KE is conserved", "Both momentum and KE are conserved", "Neither is conserved"],
        ["কেবল ভরবেগ সংরক্ষিত", "কেবল গতিশক্তি সংরক্ষিত", "ভরবেগ ও গতিশক্তি উভয় সংরক্ষিত", "কোনোটিই সংরক্ষিত নয়"],
        "C", "easy", "conceptual",
        "Elastic: both linear momentum and kinetic energy conserved.",
        "স্থিতিস্থাপক: ভরবেগ ও গতিশক্তি উভয় সংরক্ষিত।",
    ),
    q(
        "Coefficient of restitution e for a perfectly elastic collision is:",
        "পূর্ণ স্থিতিস্থাপক সংঘর্ষে পুনরুদ্ধার গুণাঙ্ক e এর মান:",
        ["0", "0.5", "1", "Infinity"],
        ["০", "০.৫", "১", "অসীম"],
        "C", "easy", "factual",
        "e = 1 for perfectly elastic; e = 0 for perfectly inelastic.",
        "পূর্ণ স্থিতিস্থাপকে e = ১; পূর্ণ অস্থিতিস্থাপকে e = ০।",
    ),
    q(
        "For a perfectly inelastic collision, e equals:",
        "পূর্ণ অস্থিতিস্থাপক সংঘর্ষে e এর মান:",
        ["0", "0.5", "1", "−1"],
        ["০", "০.৫", "১", "−১"],
        "A", "easy", "factual",
        "Bodies stick together; relative speed of separation is zero ⇒ e = 0.",
        "বস্তুগুলো একত্রে লেগে থাকে; e = ০।",
    ),
    q(
        "A 50 kg person and a 25 kg load jump from height h. Momentum ratio of load to person just before ground contact:",
        "৫০ kg ব্যক্তি ২৫ kg বোঝা নিয়ে h উচ্চতা থেকে লাফালে ভূমি স্পর্শের পূর্বে বোঝা ও ব্যক্তির ভরবেগ অনুপাত:",
        ["1 : 1", "1 : 2", "1 : 4", "2 : 1"],
        ["১ : ১", "১ : ২", "১ : ৪", "২ : ১"],
        "B", "medium", "numerical",
        "Same fall speed v; p_load : p_person = 25v : 50v = 1 : 2.",
        "সমান বেগ; p = mv ⇒ ২৫ : ৫০ = ১ : ২।",
    ),
    q(
        "Two equal masses collide elastically head-on; one was at rest. After collision:",
        "সমান ভরের দুটি বস্তুর মুখোমুখি স্থিতিস্থাপক সংঘর্ষ; একটি স্থির ছিল। সংঘর্ষের পর—",
        ["Both stop", "They exchange velocities", "Both move with half speed", "First continues unchanged"],
        ["উভয় থেমে যায়", "এদের বেগ বিনিময় হয়", "উভয় অর্ধবেগে চলে", "প্রথমটি অপরিবর্তিত থাকে"],
        "B", "medium", "conceptual",
        "1D elastic equal-mass: velocities are exchanged.",
        "সমান ভরের ১D স্থিতিস্থাপক সংঘর্ষে বেগ বিনিময় হয়।",
    ),
    q(
        "A hammer of mass 0.5 kg hits a nail at 10 m s⁻¹ and drives it 2 cm. Work done by the hammer is about:",
        "০.৫ kg হাতুড়ি ১০ m s⁻¹ বেগে পেরেকে আঘাত করে ২ cm ঢোকালে হাতুড়ির কাজ প্রায়:",
        ["10 J", "25 J", "50 J", "100 J"],
        ["১০ J", "২৫ J", "৫০ J", "১০০ J"],
        "B", "hard", "numerical",
        "Loss of KE ≈ work = (1/2)(0.5)(10)² = 25 J (if nail stops hammer).",
        "ΔK ≈ ½ × ০.৫ × ১০² = ২৫ J।",
    ),
    q(
        "A 20 g bullet at 100 m s⁻¹ penetrates 1 m into wood and stops. Work done against resistance is:",
        "২০ g বুলেট ১০০ m s⁻¹ বেগে কাঠে ১ m প্রবেশ করে থামলে প্রতিরোধের বিরুদ্ধে কাজ:",
        ["100 J", "200 J", "400 J", "800 J"],
        ["১০০ J", "২০০ J", "৪০০ J", "৮০০ J"],
        "A", "medium", "numerical",
        "W = ΔK = (1/2)(0.02)(100)² = 100 J.",
        "W = ½ × ০.০২ × ১০০² = ১০০ J।",
    ),
    q(
        "Deceleration of that bullet in the wood is:",
        "উক্ত বুলেটের কাঠের ভেতর মন্দন:",
        ["3000 m s⁻²", "4000 m s⁻²", "5000 m s⁻²", "6000 m s⁻²"],
        ["৩০০০ m s⁻²", "৪০০০ m s⁻²", "৫০০০ m s⁻²", "৬০০০ m s⁻²"],
        "C", "medium", "numerical",
        "v² = u² − 2as ⇒ 0 = 100² − 2a(1) ⇒ a = 5000 m s⁻².",
        "০ = ১০০² − ২a(১) ⇒ a = ৫০০০ m s⁻²।",
    ),
    q(
        "During a collision, impulse equals the change in:",
        "সংঘর্ষকালে ঘাত সমান কোনটির পরিবর্তনের?",
        ["Force", "Energy", "Momentum", "Power"],
        ["বল", "শক্তি", "ভরবেগ", "ক্ষমতা"],
        "C", "easy", "factual",
        "Impulse J = ∫F dt = Δp.",
        "ঘাত J = Δp।",
    ),
    q(
        "A 2 kg body has KE = 1 J. Its momentum is:",
        "২ kg ভরের বস্তুর গতিশক্তি ১ J হলে ভরবেগ:",
        ["1 kg m s⁻¹", "2 kg m s⁻¹", "√2 kg m s⁻¹", "4 kg m s⁻¹"],
        ["১ kg m s⁻¹", "২ kg m s⁻¹", "√২ kg m s⁻¹", "৪ kg m s⁻¹"],
        "B", "easy", "numerical",
        "p = √(2mK) = √(2 × 2 × 1) = 2 kg m s⁻¹.",
        "p = √(২ × ২ × ১) = ২ kg m s⁻¹।",
    ),
    q(
        "Two bodies stick together after collision. The collision is:",
        "সংঘর্ষের পর দুটি বস্তু একত্রে লেগে গেলে সংঘর্ষটি—",
        ["Perfectly elastic", "Perfectly inelastic", "Explosive", "Impossible"],
        ["পূর্ণ স্থিতিস্থাপক", "পূর্ণ অস্থিতিস্থাপক", "বিস্ফোরক", "অসম্ভব"],
        "B", "easy", "conceptual",
        "Sticking together defines a perfectly inelastic collision.",
        "লেগে যাওয়া = পূর্ণ অস্থিতিস্থাপক সংঘর্ষ।",
    ),
    q(
        "In any collision with no external force, which must be true?",
        "বাহ্যিক বলবিহীন যেকোনো সংঘর্ষে কোনটি অবশ্যই সত্য?",
        ["KE conserved", "Total energy only as heat", "Total linear momentum conserved", "Bodies must rebound"],
        ["গতিশক্তি সংরক্ষিত", "সব শক্তি কেবল তাপ", "মোট রৈখিক ভরবেগ সংরক্ষিত", "বস্তুগুলো অবশ্যই বাউন্স করবে"],
        "C", "easy", "conceptual",
        "Isolated system ⇒ total linear momentum conserved in all collision types.",
        "বিচ্ছিন্ন তন্ত্রে সব সংঘর্ষে রৈখিক ভরবেগ সংরক্ষিত।",
    ),
    q(
        "A 200 g mango falls 15 m into mud and makes a 10 cm pit. Average resistive force is about (g = 9.8):",
        "২০০ g আম ১৫ m থেকে কাদায় পড়ে ১০ cm গর্ত করলে গড় প্রতিরোধ বল প্রায় (g = ৯.৮):",
        ["29.4 N", "292 N", "294 N", "296 N"],
        ["২৯.৪ N", "২৯২ N", "২৯৪ N", "২৯৬ N"],
        "D", "hard", "numerical",
        "mg(h+d) = F d ⇒ F = 0.2×9.8×15.1/0.1 ≈ 295.96 N ≈ 296 N.",
        "F = mg(h+d)/d ≈ ২৯৫.৯৬ N ≈ ২৯৬ N।",
    ),
    q(
        "Head-on elastic collision of m with stationary M (M ≫ m). After impact, m approximately:",
        "m ভর স্থির বৃহৎ M (M ≫ m) এর সাথে স্থিতিস্থাপক মুখোমুখি সংঘর্ষে m প্রায়—",
        ["Stops", "Continues with same velocity", "Rebounds with same speed", "Moves with velocity of M"],
        ["থেমে যায়", "সমবেগে এগোয়", "সমদ্রুতিতে ফিরে আসে", "M এর বেগে চলে"],
        "C", "medium", "conceptual",
        "Against a fixed wall-like mass, elastic rebound reverses velocity.",
        "ভারী স্থির লক্ষ্যে স্থিতিস্থাপক সংঘর্ষে হালকা বস্তু সমদ্রুতিতে ফিরে আসে।",
    ),
    q(
        "Loss of kinetic energy is maximum in which collision (same initial conditions)?",
        "একই আদি অবস্থায় গতিশক্তির ক্ষতি সর্বাধিক কোন সংঘর্ষে?",
        ["Perfectly elastic", "Perfectly inelastic", "e = 0.5", "e = 0.9"],
        ["পূর্ণ স্থিতিস্থাপক", "পূর্ণ অস্থিতিস্থাপক", "e = ০.৫", "e = ০.৯"],
        "B", "medium", "conceptual",
        "Maximum KE loss occurs when bodies stick (perfectly inelastic).",
        "পূর্ণ অস্থিতিস্থাপক সংঘর্ষে KE ক্ষতি সর্বাধিক।",
    ),
    q(
        "Definition: e = (relative speed of separation)/(relative speed of approach). For bouncing ball on floor, e is:",
        "e = বিচ্ছেদের আপেক্ষিক দ্রুতি / অভিগমনের আপেক্ষিক দ্রুতি। মেঝেতে বাউন্স করা বলের e:",
        ["Always > 1", "Between 0 and 1 for real balls", "Always = 0", "Always negative"],
        ["সর্বদা ১ এর বেশি", "বাস্তব বলে ০ থেকে ১ এর মধ্যে", "সর্বদা ০", "সর্বদা ঋণাত্মক"],
        "B", "easy", "conceptual",
        "Real collisions: 0 ≤ e ≤ 1.",
        "বাস্তব সংঘর্ষে ০ ≤ e ≤ ১।",
    ),
    q(
        "A neutron collides elastically head-on with a stationary proton (nearly equal mass). After collision the neutron:",
        "নিউট্রন স্থির প্রোটনের সাথে স্থিতিস্থাপক মুখোমুখি সংঘর্ষে নিউট্রন—",
        ["Continues with same speed", "Stops and proton takes its speed", "Both rebound equally", "Both stop"],
        ["সমবেগে এগোয়", "থেমে যায় ও প্রোটন তার বেগ নেয়", "উভয় সমানভাবে ফিরে আসে", "উভয় থেমে যায়"],
        "B", "medium", "application",
        "Equal-mass 1D elastic collision transfers all velocity to the target.",
        "সমান ভরের ১D স্থিতিস্থাপক সংঘর্ষে বেগ বিনিময়; নিউট্রন থামে।",
    ),
    q(
        "In an explosive ‘collision’ (internal energy released), total kinetic energy after explosion:",
        "বিস্ফোরক বিচ্ছিন্নতায় (অভ্যন্তরীণ শক্তি মুক্ত) পরে মোট গতিশক্তি—",
        ["Must equal initial KE", "Is less than initial KE", "Can exceed initial KE", "Must be zero"],
        ["আদি KE এর সমান হতেই হবে", "আদি KE এর চেয়ে কম", "আদি KE এর চেয়ে বেশি হতে পারে", "শূন্য হতেই হবে"],
        "C", "medium", "conceptual",
        "Chemical/internal energy can increase total KE while momentum still conserved.",
        "অভ্যন্তরীণ শক্তি KE বাড়াতে পারে; ভরবেগ তবু সংরক্ষিত।",
    ),
    q(
        "Two masses m and 3m move toward each other at equal speeds v and stick. Common speed is:",
        "m ও ৩m ভর সমান দ্রুতি v তে মুখোমুখি এসে লেগে গেলে সম্মিলিত দ্রুতি:",
        ["v", "v/2", "v/4", "0"],
        ["v", "v/২", "v/৪", "০"],
        "B", "medium", "numerical",
        "Momentum: m v − 3m v = −2m v = 4m V ⇒ V = −v/2; speed = v/2.",
        "mv − ৩mv = ৪m V ⇒ |V| = v/২।",
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
    write_topic("phy1_27_ch05_t01", T01)
    write_topic("phy1_27_ch05_t02", T02)
    write_topic("phy1_27_ch05_t03", T03)
    write_topic("phy1_27_ch05_t04", T04)

    summary = {
        "paper": "physics_1",
        "chapter": 5,
        "title_en": "Work, Power and Energy",
        "title_bn": "কাজ, ক্ষমতা ও শক্তি",
        "per_topic": 20,
        "topics": {
            "phy1_27_ch05_t01": 20,
            "phy1_27_ch05_t02": 20,
            "phy1_27_ch05_t03": 20,
            "phy1_27_ch05_t04": 20,
        },
        "source": SOURCE,
        "verified": False,
        "mcq_printed_pages": [163, 174],
        "notes": (
            "OCR-noisy pages 163–174 reconstructed as HSC-accurate bilingual MCQs; "
            "figure-only items rewritten in text; work–energy, PE conservation, "
            "power/efficiency and collision staples preserved with corrected arithmetic."
        ),
    }
    out = (
        ROOT
        / "content"
        / "bank"
        / "udvash_raw"
        / "physics_1"
        / "parsed"
        / "ch05_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("summary", out)


if __name__ == "__main__":
    main()
