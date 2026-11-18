#!/usr/bin/env python3
"""Seed Physics 1st Paper Ch6 (Gravitation and Gravity) bilingual MCQs.

Curated from Udvash HSC Question Bank 2026 printed pages 199–206 (OCR + HSC reconstruction).
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
    "physics p1 ch06; curated bilingual"
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
# t01 Newton's law of gravitation / নিউটনের মহাকর্ষ সূত্র
# ---------------------------------------------------------------------------
T01 = [
    q(
        "Dimensional formula of the universal gravitational constant G is:",
        "সার্বজনীন মহাকর্ষ ধ্রুবক G এর মাত্রা কোনটি?",
        ["[M^-1 L^3 T^-2]", "[M^-1 L^2 T^-1]", "[M L^-1 T^-2]", "[M^-2 L^3 T^-2]"],
        ["[M^-1 L^3 T^-2]", "[M^-1 L^2 T^-1]", "[M L^-1 T^-2]", "[M^-2 L^3 T^-2]"],
        "A", "easy", "factual",
        "From F = G m1 m2 / r^2 ⇒ G = F r^2 /(m1 m2) ⇒ [M^-1 L^3 T^-2].",
        "F = G m1 m2 / r^2 থেকে G এর মাত্রা [M^-1 L^3 T^-2]।",
    ),
    q(
        "Accepted approximate value of G is:",
        "G এর গৃহীত আনুমানিক মান কোনটি?",
        ["8.854 × 10^-12 Nm^2 kg^-2", "1.256 × 10^-6 Nm^2 kg^-2",
         "6.673 × 10^-8 Nm^2 kg^-2", "6.673 × 10^-11 Nm^2 kg^-2"],
        ["8.854 × 10^-12 Nm^2 kg^-2", "1.256 × 10^-6 Nm^2 kg^-2",
         "6.673 × 10^-8 Nm^2 kg^-2", "6.673 × 10^-11 Nm^2 kg^-2"],
        "D", "easy", "factual",
        "G ≈ 6.67 × 10^-11 N m^2 kg^-2.",
        "G ≈ ৬.৬৭ × ১০^-১১ N m^2 kg^-2।",
    ),
    q(
        "Two point masses of 1 kg each are 1 m apart. Magnitude of the gravitational force between them is:",
        "১ kg ভরের দুটি বিন্দু ভর ১ m দূরে থাকলে তাদের মধ্যে মহাকর্ষ বলের মান:",
        ["6.67 × 10^-11 N", "6.67 × 10^-8 N", "6.67 N", "1 N"],
        ["6.67 × 10^-11 N", "6.67 × 10^-8 N", "6.67 N", "1 N"],
        "A", "easy", "numerical",
        "F = G (1)(1)/1^2 = G ≈ 6.67 × 10^-11 N.",
        "F = G = ৬.৬৭ × ১০^-১১ N।",
    ),
    q(
        "Gravitational force between two masses is always:",
        "দুটি ভরের মধ্যে মহাকর্ষ বল সর্বদা—",
        ["Repulsive", "Attractive", "Zero in vacuum", "Depends on charge"],
        ["বিকর্ষণধর্মী", "আকর্ষণধর্মী", "শূন্যে শূন্য", "চার্জের উপর নির্ভরশীল"],
        "B", "easy", "conceptual",
        "Gravity is always attractive between masses.",
        "ভরের মধ্যে মহাকর্ষ সর্বদা আকর্ষণধর্মী।",
    ),
    q(
        "If the distance between two masses becomes three times, the gravitational force becomes:",
        "দুটি বস্তুর মধ্যে দূরত্ব তিনগুণ হলে মহাকর্ষীয় বল হবে—",
        ["3 times", "1/3 times", "9 times", "1/9 times"],
        ["৩ গুণ", "১/৩ গুণ", "৯ গুণ", "১/৯ গুণ"],
        "D", "easy", "numerical",
        "F ∝ 1/r^2 ⇒ F' = F/9.",
        "F ∝ 1/r^2 ⇒ F' = F/৯।",
    ),
    q(
        "According to Kepler’s third law, for planets around the Sun:",
        "কেপলারের তৃতীয় সূত্রানুসারে সূর্যকে প্রদক্ষিণকারী গ্রহের জন্য—",
        ["T^2 ∝ r^3", "T ∝ r^2", "T ∝ r", "T^2 ∝ r"],
        ["T^2 ∝ r^3", "T ∝ r^2", "T ∝ r", "T^2 ∝ r"],
        "A", "easy", "factual",
        "Square of period is proportional to cube of semi-major axis.",
        "পর্যায়কালের বর্গ অর্ধ-দীর্ঘ অক্ষের ঘনফলের সমানুপাতিক।",
    ),
    q(
        "Kepler’s second law (equal areas in equal times) follows from conservation of:",
        "কেপলারের দ্বিতীয় সূত্র কোন ভৌত রাশির সংরক্ষণ থেকে পাওয়া যায়?",
        ["Angular momentum", "Linear momentum", "Energy only", "Mass"],
        ["কৌণিক ভরবেগ", "রৈখিক ভরবেগ", "কেবল শক্তি", "ভর"],
        "A", "medium", "conceptual",
        "Central gravitational force ⇒ torque = 0 ⇒ angular momentum conserved ⇒ equal areas.",
        "কেন্দ্রীয় বল হলে টর্ক শূন্য; কৌণিক ভরবেগ সংরক্ষিত → সমান ক্ষেত্রফল।",
    ),
    q(
        "Who stated that planets move in elliptical orbits around the Sun?",
        "“গ্রহ সূর্যের চারদিকে উপবৃত্তাকার পথে পরিভ্রমণ করে”—এই সূত্র কে প্রদান করেন?",
        ["Kepler", "Newton", "Galileo", "Copernicus"],
        ["কেপলার", "নিউটন", "গ্যালিলিও", "কোপারনিকাস"],
        "A", "easy", "factual",
        "Kepler’s first law: elliptical orbits with the Sun at one focus.",
        "কেপলারের প্রথম সূত্র: উপবৃত্তাকার কক্ষ; সূর্য এক ফোকাসে।",
    ),
    q(
        "Earth’s orbital period about the Sun is 365 days and mean distance is 1.5 × 10^11 m. With G = 6.7 × 10^-11 N m^2 kg^-2, Sun’s mass is approximately:",
        "পৃথিবীর আবর্তনকাল ৩৬৫ দিন ও সূর্য থেকে গড় দূরত্ব 1.5 × 10^11 m হলে সূর্যের ভর প্রায় (G = 6.7 × 10^-11):",
        ["1.56 × 10^17 kg", "2 × 10^20 kg", "6 × 10^24 kg", "2 × 10^30 kg"],
        ["1.56 × 10^17 kg", "2 × 10^20 kg", "6 × 10^24 kg", "2 × 10^30 kg"],
        "D", "hard", "numerical",
        "M = 4π^2 r^3 /(G T^2) ≈ 2 × 10^30 kg.",
        "M = 4π^2 r^3 /(G T^2) ≈ ২ × ১০^৩০ kg।",
    ),
    q(
        "Expression for the Sun’s mass in terms of a planet’s mean distance r and period T is:",
        "সূর্যের ভরের রাশিমালা (গ্রহের গড় দূরত্ব r, পর্যায়কাল T) কোনটি?",
        ["4π^2 r^3 /(G T^2)", "G T^2 /(4π^2 r^3)", "4π^2 G r^3 / T^2", "G r / T^2"],
        ["4π^2 r^3 /(G T^2)", "G T^2 /(4π^2 r^3)", "4π^2 G r^3 / T^2", "G r / T^2"],
        "A", "medium", "factual",
        "From centripetal force = gravity: GM/r^2 = 4π^2 r / T^2 ⇒ M = 4π^2 r^3 /(G T^2).",
        "GM/r^2 = 4π^2 r/T^2 থেকে M = 4π^2 r^3 /(G T^2)।",
    ),
    q(
        "If a planet’s mean distance from the Sun is doubled, its orbital speed becomes how many times?",
        "সূর্য থেকে কোনো গ্রহের গড় দূরত্ব দ্বিগুণ করা হলে গ্রহের কক্ষীয় বেগ কতগুণ হবে?",
        ["2 times", "1/√2 times", "4 times", "8 times"],
        ["২ গুণ", "১/√২ গুণ", "৪ গুণ", "৮ গুণ"],
        "B", "medium", "numerical",
        "v = √(GM/r) ⇒ v' / v = √(1/2) = 1/√2.",
        "v = √(GM/r) ⇒ v'/v = ১/√২।",
    ),
    q(
        "Earth orbits the Sun in 365 days and Mercury in 88 days. If Earth’s mean solar distance is 1.5 × 10^11 m, Mercury’s mean distance is about:",
        "পৃথিবী ৩৬৫ দিনে ও বুধ ৮৮ দিনে সূর্য প্রদক্ষিণ করে; পৃথিবীর গড় দূরত্ব 1.5 × 10^11 m হলে বুধের গড় দূরত্ব প্রায়:",
        ["5.81 × 10^10 m", "38.68 × 10^10 m", "1.28 × 10^10 m", "1.77 × 10^20 m"],
        ["5.81 × 10^10 m", "38.68 × 10^10 m", "1.28 × 10^10 m", "1.77 × 10^20 m"],
        "A", "hard", "numerical",
        "r_M / r_E = (T_M / T_E)^{2/3} ⇒ r_M ≈ 5.81 × 10^10 m.",
        "r ∝ T^{2/3} ⇒ বুধের দূরত্ব ≈ ৫.৮১ × ১০^১০ m।",
    ),
    q(
        "If the mean Sun–Earth distance becomes two-thirds of the present value, the length of the year becomes about:",
        "সূর্য–পৃথিবী দূরত্ব বর্তমানের দুই-তৃতীয়াংশ হলে এক বছরের দিন সংখ্যা প্রায়:",
        ["108.15 days", "121.66 days", "198.68 days", "243.33 days"],
        ["১০৮.১৫ দিন", "১২১.৬৬ দিন", "১৯৮.৬৮ দিন", "২৪৩.৩৩ দিন"],
        "C", "hard", "numerical",
        "T' / T = (r'/r)^{3/2} = (2/3)^{3/2} ⇒ T' ≈ 198.68 days.",
        "T ∝ r^{3/2} ⇒ T' ≈ ১৯৮.৬৮ দিন।",
    ),
    q(
        "If the average distance of a planet from the Sun decreases, its orbital period:",
        "সূর্য থেকে কোনো গ্রহের গড় দূরত্ব কমে গেলে গ্রহটির পর্যায়কাল—",
        ["Decreases", "Increases", "Remains constant", "Becomes infinite"],
        ["কমে যায়", "বেড়ে যায়", "স্থির থাকে", "অসীম হয়"],
        "A", "easy", "conceptual",
        "T^2 ∝ r^3 ⇒ smaller r gives smaller T.",
        "T^2 ∝ r^3; r কমলে T কমে।",
    ),
    q(
        "The name of Kepler’s third law is commonly:",
        "কেপলারের তৃতীয় সূত্রের নাম কোনটি?",
        ["Law of orbits", "Law of areas", "Law of periods (harmonic law)", "Law of inertia"],
        ["কক্ষপথের সূত্র", "ক্ষেত্রফলের সূত্র", "পর্যায়কালের সূত্র (হারমোনিক সূত্র)", "জড়তার সূত্র"],
        "C", "easy", "factual",
        "Kepler’s third law is the harmonic / period law: T^2 ∝ a^3.",
        "তৃতীয় সূত্র পর্যায়কালের (হারমোনিক) সূত্র।",
    ),
    q(
        "Gravitational attraction between two masses does NOT depend on:",
        "দুই ভরের মধ্যে মহাকর্ষ আকর্ষণ নির্ভর করে না কোনটির উপর?",
        ["Product of masses", "Distance between centres", "Medium’s electric permittivity", "Value of G"],
        ["ভরের গুণফল", "কেন্দ্রদ্বয়ের দূরত্ব", "মাধ্যমের তড়িৎ প্রবেশ্যতা", "G এর মান"],
        "C", "medium", "conceptual",
        "Newton’s gravity depends on masses, separation and G—not on electric permittivity.",
        "মহাকর্ষ ভর, দূরত্ব ও G এর উপর নির্ভর করে; তড়িৎ প্রবেশ্যতার উপর নয়।",
    ),
    q(
        "Action–reaction gravitational forces between two masses are equal in magnitude and:",
        "দুই ভরের মধ্যে ক্রিয়া–প্রতিক্রিয়া মহাকর্ষ বল সমান মানের এবং—",
        ["Opposite in direction", "Same in direction", "Perpendicular", "Zero if masses differ"],
        ["বিপরীত দিকে", "একই দিকে", "লম্বভাবে", "ভর ভিন্ন হলে শূন্য"],
        "A", "easy", "conceptual",
        "Newton’s third law: equal and opposite forces along the line joining centres.",
        "নিউটনের তৃতীয় সূত্র: সমান ও বিপরীত বল।",
    ),
    q(
        "If separation between two masses is halved, gravitational force becomes:",
        "দুই ভরের দূরত্ব অর্ধেক হলে মহাকর্ষ বল হয়—",
        ["Half", "Double", "Four times", "One-fourth"],
        ["অর্ধেক", "দ্বিগুণ", "চারগুণ", "এক-চতুর্থাংশ"],
        "C", "easy", "numerical",
        "F ∝ 1/r^2 ⇒ (1/(1/2))^2 = 4.",
        "F ∝ 1/r^2 ⇒ চারগুণ।",
    ),
    q(
        "Galileo’s free-fall idea (same acceleration) applies best to:",
        "গ্যালিলিওর সূত্র সবচেয়ে প্রযোজ্য—",
        ["Motion on a rough plane", "Bodies falling without air resistance",
         "Bodies with air drag", "Only charged particles"],
        ["রুক্ষ তলে গতি", "বাতাসের বাধাহীন পতন", "বায়ু বাধাযুক্ত পতন", "কেবল চার্জিত কণা"],
        "B", "easy", "conceptual",
        "In vacuum (no drag), all bodies fall with the same g.",
        "বাধাহীন পতনে সব বস্তুর ত্বরণ একই g।",
    ),
    q(
        "For a planet of mass M and radius R, surface gravity g equals:",
        "ভর M ও ব্যাসার্ধ R এর গ্রহের পৃষ্ঠে অভিকর্ষজ ত্বরণ g এর মান:",
        ["GM / R^2", "GM / R", "G M^2 / R^2", "G / R^2"],
        ["GM / R^2", "GM / R", "G M^2 / R^2", "G / R^2"],
        "A", "easy", "factual",
        "mg = GMm / R^2 ⇒ g = GM / R^2.",
        "g = GM / R^2।",
    ),
]


# ---------------------------------------------------------------------------
# t02 Gravitational field and potential / মহাকর্ষ ক্ষেত্র ও বিভব
# ---------------------------------------------------------------------------
T02 = [
    q(
        "SI unit of gravitational potential is:",
        "মহাকর্ষীয় বিভবের একক কোনটি?",
        ["N m^2 kg^-2", "J kg^-1", "kg m s^-1", "N kg"],
        ["N m^2 kg^-2", "J kg^-1", "kg m s^-1", "N kg"],
        "B", "easy", "factual",
        "Potential = work per unit mass ⇒ J/kg.",
        "বিভব = একক ভরে কাজ ⇒ J kg^-1।",
    ),
    q(
        "Which quantity is associated with a scalar field?",
        "নিচের কোন ভৌত রাশিটি স্কেলার ক্ষেত্রের সাথে সংশ্লিষ্ট?",
        ["Gravitational field intensity", "Linear momentum", "Gravitational potential", "Angular momentum"],
        ["মহাকর্ষ ক্ষেত্র প্রাবল্য", "রৈখিক ভরবেগ", "মহাকর্ষীয় বিভব", "কৌণিক ভরবেগ"],
        "C", "easy", "conceptual",
        "Gravitational potential is a scalar; intensity is a vector.",
        "মহাকর্ষীয় বিভব স্কেলার; প্রাবল্য ভেক্টর।",
    ),
    q(
        "Relation between gravitational intensity E and potential V is:",
        "মহাকর্ষীয় প্রাবল্য ও বিভবের মধ্যে সম্পর্ক—",
        ["E = dV/dr", "E = −dV/dr", "V = −dE/dr", "V = E^2"],
        ["E = dV/dr", "E = −dV/dr", "V = −dE/dr", "V = E^2"],
        "B", "medium", "factual",
        "Field is the negative gradient of potential.",
        "ক্ষেত্র প্রাবল্য = বিভবের ঋণাত্মক গ্রেডিয়েন্ট।",
    ),
    q(
        "For a large spherical mass, gravitational potential has its maximum (least negative / zero convention) value at:",
        "বৃহদাকার বস্তুর জন্য মহাকর্ষীয় বিভবের সর্বোচ্চ মান কোথায়?",
        ["At the centre", "On the surface", "Anywhere just outside", "At infinity"],
        ["বস্তুর কেন্দ্রে", "বস্তুর পৃষ্ঠে", "পৃষ্ঠের ঠিক বাইরে", "অসীম দূরত্বে"],
        "D", "medium", "conceptual",
        "With V(∞)=0, potential is zero at infinity and more negative nearer the mass.",
        "V(∞)=০ ধরলে অসীমে সর্বোচ্চ (শূন্য); কেন্দ্রে সবচেয়ে ঋণাত্মক।",
    ),
    q(
        "Work done in taking a mass m from Earth’s surface to infinity (g surface gravity, R radius) is:",
        "পৃথিবী পৃষ্ঠ থেকে m ভর অসীমে নিতে সম্পাদিত কাজ (অভিকর্ষজ ত্বরণ g, ব্যাসার্ধ R):",
        ["(1/2) mgR", "mgR", "G m / R", "2 mgR"],
        ["(1/2) mgR", "mgR", "G m / R", "2 mgR"],
        "B", "medium", "numerical",
        "W = GMm/R = (g R^2)m / R = mgR.",
        "W = GMm/R = mgR।",
    ),
    q(
        "Slope of the gravitational potential energy versus height graph indicates:",
        "মহাকর্ষীয় বিভবশক্তি ও উচ্চতার লেখচিত্রের ঢাল কী নির্দেশ করে?",
        ["Gravitational force", "Reaction force", "Electric intensity", "Magnetic force"],
        ["মহাকর্ষীয় বল", "প্রতিক্রিয়া বল", "তড়িৎ তীব্রতা", "চৌম্বক বল"],
        "A", "medium", "conceptual",
        "F = −dU/dh; magnitude of slope gives gravitational force.",
        "F = −dU/dh; ঢালের মান মহাকর্ষ বল।",
    ),
    q(
        "A person’s weight is 785 N on Earth and 298 N on Mars. If g_Earth = 9.8 m s^-2, Mars surface field intensity is about:",
        "ওজন পৃথিবীতে ৭৮৫ N ও মঙ্গলে ২৯৮ N; g_পৃথিবী = 9.8 m s^-2 হলে মঙ্গল পৃষ্ঠে ক্ষেত্র তীব্রতা প্রায়:",
        ["2.63 N kg^-1", "3.72 N kg^-1", "6.09 N kg^-1", "9.81 N kg^-1"],
        ["2.63 N kg^-1", "3.72 N kg^-1", "6.09 N kg^-1", "9.81 N kg^-1"],
        "B", "medium", "numerical",
        "m = 785/9.8; g_Mars = 298/m ≈ 3.72 N/kg.",
        "m = ৭৮৫/৯.৮; g_মঙ্গল ≈ ৩.৭২ N kg^-1।",
    ),
    q(
        "Dimensional formula of gravitational field intensity is:",
        "মহাকর্ষ ক্ষেত্র প্রাবল্যের মাত্রা কোনটি?",
        ["[M T^-2]", "[L T^-2]", "[M L T^-2]", "[M L^-1 T^-2]"],
        ["[M T^-2]", "[L T^-2]", "[M L T^-2]", "[M L^-1 T^-2]"],
        "B", "easy", "factual",
        "Intensity = force/mass = acceleration ⇒ [L T^-2].",
        "প্রাবল্য = বল/ভর = ত্বরণ ⇒ [L T^-2]।",
    ),
    q(
        "Gravitational potential due to a point mass M at distance r is:",
        "বিন্দু ভর M থেকে r দূরত্বে মহাকর্ষীয় বিভব:",
        ["−GM / r", "GM / r", "−GM / r^2", "GM / r^2"],
        ["−GM / r", "GM / r", "−GM / r^2", "GM / r^2"],
        "A", "easy", "factual",
        "V = −GM/r (zero at infinity).",
        "V = −GM/r (অসীমে শূন্য)।",
    ),
    q(
        "Which statements about gravitational potential are correct? (i) V = −GM/r (ii) unit J kg^-1 (iii) it is a scalar",
        "মহাকর্ষীয় বিভব সম্পর্কে সঠিক—(i) V = −GM/r (ii) একক J kg^-1 (iii) স্কেলার রাশি",
        ["(i),(ii) only", "(ii),(iii) only", "(i),(iii) only", "(i),(ii),(iii)"],
        ["কেবল (i),(ii)", "কেবল (ii),(iii)", "কেবল (i),(iii)", "(i),(ii),(iii)"],
        "D", "easy", "conceptual",
        "All three statements are standard properties of V.",
        "তিনটিই মহাকর্ষীয় বিভবের মানক ধর্ম।",
    ),
    q(
        "At Earth’s centre, gravitational field intensity is:",
        "পৃথিবীর কেন্দ্রে মহাকর্ষ ক্ষেত্র প্রাবল্য—",
        ["Maximum", "Equal to surface value", "Zero", "Infinite"],
        ["সর্বোচ্চ", "পৃষ্ঠের সমান", "শূন্য", "অসীম"],
        "C", "easy", "conceptual",
        "Inside a uniform sphere, g ∝ r ⇒ g = 0 at centre.",
        "সুষম গোলকের ভিতরে g ∝ r; কেন্দ্রে g = ০।",
    ),
    q(
        "Masses 5 kg and 10 kg are placed 2 m apart. Magnitude of net gravitational field at the midpoint is:",
        "৫ kg ও ১০ kg ভর ২ m দূরে; মধ্যবিন্দুতে নিট মহাকর্ষ ক্ষেত্র প্রাবল্যের মান:",
        ["G × 5", "G × 10", "G × 2.5", "Zero"],
        ["G × ৫", "G × ১০", "G × ২.৫", "শূন্য"],
        "A", "medium", "numerical",
        "E_net = G(10−5)/1^2 = 5G toward the heavier mass.",
        "E = G(১০−৫)/১^2 = ৫G (ভারী ভরের দিকে)।",
    ),
    q(
        "Gravitational potential energy of mass m at distance r from Earth (mass M) is:",
        "পৃথিবী (ভর M) থেকে r দূরত্বে m ভরের মহাকর্ষীয় বিভবশক্তি:",
        ["−GMm / r", "GMm / r", "mgh only", "GMm / r^2"],
        ["−GMm / r", "GMm / r", "কেবল mgh", "GMm / r^2"],
        "A", "easy", "factual",
        "U = mV = −GMm/r.",
        "U = −GMm/r।",
    ),
    q(
        "On the surface of a uniform spherical planet, the surface is approximately an:",
        "সুষম গোলক গ্রহের পৃষ্ঠ প্রায় একটি—",
        ["Equipotential surface", "Equiforce surface with zero g", "Magnetic shell", "Null potential only"],
        ["সমবিভব তল", "শূন্য g এর সমবল তল", "চৌম্বক খোলক", "কেবল শূন্য বিভব"],
        "A", "medium", "conceptual",
        "For a spherical mass, V is constant on the surface ⇒ equipotential.",
        "গোলকীয় ভরের পৃষ্ঠে V ধ্রুব ⇒ সমবিভব তল।",
    ),
    q(
        "Inside Earth at distance x from centre (x < R), g varies as:",
        "পৃথিবীর কেন্দ্র হতে দূরত্ব x (x < R) এ অভিকর্ষজ ত্বরণের সম্পর্ক—",
        ["g ∝ x", "g ∝ 1/x", "g ∝ 1/x^2", "g ∝ x^2"],
        ["g ∝ x", "g ∝ 1/x", "g ∝ 1/x^2", "g ∝ x^2"],
        "A", "medium", "factual",
        "g(x) = (GM/R^3) x ⇒ proportional to x.",
        "g(x) = (GM/R^3)x ⇒ g ∝ x।",
    ),
    q(
        "Outside Earth (x > R), g varies as:",
        "পৃথিবীর বাইরে (x > R) অভিকর্ষজ ত্বরণের সম্পর্ক—",
        ["g ∝ x", "g ∝ 1/x", "g ∝ 1/x^2", "g independent of x"],
        ["g ∝ x", "g ∝ 1/x", "g ∝ 1/x^2", "x নির্ভর নয়"],
        "C", "easy", "factual",
        "Outside, g = GM/x^2.",
        "বাইরে g = GM/x^2।",
    ),
    q(
        "Magnitude of gravitational intensity due to Earth at its surface equals:",
        "পৃথিবী পৃষ্ঠে মহাকর্ষীয় প্রাবল্যের মান সমান—",
        ["Surface gravity g", "Universal constant G", "Product GM", "Earth radius R"],
        ["পৃষ্ঠের অভিকর্ষজ ত্বরণ g", "সার্বজনীন ধ্রুবক G", "গুণফল GM", "পৃথিবীর ব্যাসার্ধ R"],
        "A", "easy", "conceptual",
        "Field intensity numerically equals gravitational acceleration g.",
        "প্রাবল্যের মান অভিকর্ষজ ত্বরণ g এর সমান।",
    ),
    q(
        "An 80 kg body is taken from Earth’s surface to a height h = R/2. Using the linear approximation g' = g(1 − h/R) with g = 9.8 m s^-2, its weight there is:",
        "৮০ kg ভরের বস্তুকে ভূপৃষ্ঠ থেকে h = R/2 উচ্চতায় নিলে আসন্ন সূত্র g' = g(1 − h/R) ও g = 9.8 m s^-2 এ ওজন:",
        ["245 N", "272 N", "392 N", "490 N"],
        ["২৪৫ N", "২৭২ N", "৩৯২ N", "৪৯০ N"],
        "C", "hard", "numerical",
        "g' = g(1 − 1/2) = g/2 ⇒ W = 80 × 9.8 × 1/2 = 392 N.",
        "g' = g/২ ⇒ W = ৮০ × ৯.৮ × ১/২ = ৩৯২ N।",
    ),
    q(
        "Two equal masses m = 1 kg are separated by 1 m. Correct statements about the force between them: (i) gravitational (ii) weight-force (অভিকর্ষ) of Earth type only (iii) attractive",
        "১ kg দুই ভর ১ m দূরে; তাদের মধ্যে বল সম্পর্কে সঠিক—(i) মহাকর্ষ বল (ii) কেবল পৃথিবীর অভিকর্ষ বল (iii) আকর্ষণধর্মী",
        ["(i),(ii)", "(ii),(iii)", "(i),(iii)", "(i),(ii),(iii)"],
        ["(i),(ii)", "(ii),(iii)", "(i),(iii)", "(i),(ii),(iii)"],
        "C", "easy", "conceptual",
        "Mutual force is universal gravitation and attractive; it is not specifically Earth’s gravity (weight).",
        "পারস্পরিক বল মহাকর্ষ ও আকর্ষণধর্মী; পৃথিবীর ওজন বল নয়।",
    ),
    q(
        "Gravitational potential is a:",
        "মহাকর্ষীয় বিভব হলো একটি—",
        ["Vector quantity", "Scalar quantity", "Tensor only", "Dimensionless number"],
        ["ভেক্টর রাশি", "স্কেলার রাশি", "কেবল টেনসর", "মাত্রাহীন সংখ্যা"],
        "B", "easy", "factual",
        "Potential has magnitude and sign but no direction.",
        "বিভবের দিক নেই; এটি স্কেলার।",
    ),
]


# ---------------------------------------------------------------------------
# t03 Variation of gravitational acceleration / অভিকর্ষজ ত্বরণের পরিবর্তন
# ---------------------------------------------------------------------------
T03 = [
    q(
        "Compared with the poles, g at the equator is smaller by approximately:",
        "মেরু অঞ্চল অপেক্ষা বিষুবীয় অঞ্চলে অভিকর্ষজ ত্বরণ কত কম?",
        ["ω^2 R", "ω R", "ω^2 R cos^2 λ", "ω R cos^2 λ"],
        ["ω^2 R", "ω R", "ω^2 R cos^2 λ", "ω R cos^2 λ"],
        "A", "medium", "factual",
        "At equator λ = 0°, g' = g − ω^2 R.",
        "বিষুবে λ = ০°; g' = g − ω^2 R।",
    ),
    q(
        "Depths and heights from Earth’s surface where g has the same value have the ratio (depth : height):",
        "ভূ-পৃষ্ঠ থেকে যে গভীরতা ও উচ্চতায় g সমান, তাদের অনুপাত (গভীরতা : উচ্চতা):",
        ["1 : 2", "2 : 1", "1 : 1", "1 : 3"],
        ["১ : ২", "২ : ১", "১ : ১", "১ : ৩"],
        "B", "medium", "numerical",
        "g(1 − d/R) = g(1 − 2h/R) ⇒ d = 2h ⇒ d : h = 2 : 1.",
        "d = ২h ⇒ দ : উ = ২ : ১।",
    ),
    q(
        "Which has NO effect on the value of g?",
        "অভিকর্ষজ ত্বরণের উপর কোনটির প্রভাব নেই?",
        ["Longitude", "Altitude", "Latitude", "Earth’s rotation"],
        ["দ্রাঘিমা", "উচ্চতা", "অক্ষাংশ", "পৃথিবীর ঘূর্ণন"],
        "A", "easy", "conceptual",
        "g varies with latitude, height, depth and rotation—not with longitude.",
        "g দ্রাঘিমার সাথে পরিবর্তিত হয় না।",
    ),
    q(
        "Standard (ideal) value of g is taken at latitude:",
        "কত অক্ষাংশে g এর আদর্শ মান ধরা হয়?",
        ["0°", "45°", "90°", "180°"],
        ["০°", "৪৫°", "৯০°", "১৮০°"],
        "B", "easy", "factual",
        "Conventionally g = 9.80665 m s^-2 near 45° latitude at sea level.",
        "আদর্শ g ≈ ৪৫° অক্ষাংশে সমুদ্র সমতলে।",
    ),
    q(
        "Due to Earth’s daily rotation, g is:",
        "আহ্নিক গতির জন্য অভিকর্ষজ ত্বরণের মান—",
        ["Maximum at 45° sea level only", "Maximum at poles and minimum at equator",
         "Minimum at poles", "Same everywhere"],
        ["কেবল ৪৫° তে সর্বাধিক", "মেরুতে সর্বাধিক ও বিষুবে সর্বনিম্ন",
         "মেরুতে সর্বনিম্ন", "সব জায়গায় সমান"],
        "B", "easy", "conceptual",
        "Effective g is largest at poles and smallest at equator.",
        "মেরুতে g সর্বোচ্চ; বিষুবে সর্বনিম্ন।",
    ),
    q(
        "At height h above Earth’s surface (R ≫ h), approximate g' is:",
        "ভূ-পৃষ্ঠ হতে h উচ্চতায় (R ≫ h) অভিকর্ষজ ত্বরণ আসন্নমান:",
        ["g(R − h)/(R + h)", "g R^2 /(R + h)^2", "g(R + h)/R", "g R /(R − h)"],
        ["g(R − h)/(R + h)", "g R^2 /(R + h)^2", "g(R + h)/R", "g R /(R − h)"],
        "B", "medium", "factual",
        "Exact: g' = GM/(R+h)^2 = g R^2/(R+h)^2.",
        "g' = g R^2 /(R+h)^2।",
    ),
    q(
        "At what height above Earth’s surface is g equal to 25% of its surface value? (R = 6400 km)",
        "ভূ-পৃষ্ঠ হতে কত km উচ্চতায় g এর মান পৃষ্ঠের ২৫% হবে? (R = ৬৪০০ km)",
        ["6400", "640", "3200", "1600"],
        ["৬৪০০", "৬৪০", "৩২০০", "১৬০০"],
        "A", "medium", "numerical",
        "(R/(R+h))^2 = 1/4 ⇒ R+h = 2R ⇒ h = R = 6400 km.",
        "h = R = ৬৪০০ km।",
    ),
    q(
        "At what depth below Earth’s surface is g one-fourth of the surface value?",
        "পৃথিবীর ব্যাসার্ধ R বরাবর কত গভীরতায় g ভূপৃষ্ঠের এক-চতুর্থাংশ হবে?",
        ["R/4", "R/2", "3R/4", "R"],
        ["R/৪", "R/২", "৩R/৪", "R"],
        "C", "medium", "numerical",
        "g(1 − d/R) = g/4 ⇒ d/R = 3/4.",
        "d = ৩R/৪।",
    ),
    q(
        "Height above Earth where g becomes half the surface value is about:",
        "ভূ-পৃষ্ঠ হতে কত উচ্চতায় g এর মান অর্ধেক হবে?",
        ["0.207 R", "0.414 R", "2 R", "4 R"],
        ["০.২০৭ R", "০.৪১৪ R", "২ R", "৪ R"],
        "B", "hard", "numerical",
        "(R/(R+h))^2 = 1/2 ⇒ R+h = R√2 ⇒ h = (√2 − 1)R ≈ 0.414 R.",
        "h = (√২ − ১)R ≈ ০.৪১৪ R।",
    ),
    q(
        "Variation of g does NOT involve:",
        "অভিকর্ষজ ত্বরণ g এর তারতম্যে কোনটির ভূমিকা নেই?",
        ["Earth’s shape", "Earth’s revolution around the Sun",
         "Earth’s spin about its axis", "Height above surface"],
        ["পৃথিবীর আকার", "সূর্যের চারদিকে পৃথিবীর পরিক্রমণ",
         "নিজ অক্ষে ঘূর্ণন", "ভূ-পৃষ্ঠ থেকে উচ্চতা"],
        "B", "medium", "conceptual",
        "Annual orbital motion around the Sun does not change local g.",
        "বার্ষিক গতি স্থানীয় g পরিবর্তন করে না।",
    ),
    q(
        "A 30 kg object weighs how much on the Moon if g_Moon = g_Earth / 6?",
        "৩০ kg ভরের বস্তুর ওজন চন্দ্রপৃষ্ঠে কত? (চন্দ্রের g = পৃথিবীর ১/৬)",
        ["490 N", "480 N", "294 N", "49 N"],
        ["৪৯০ N", "৪৮০ N", "২৯৪ N", "৪৯ N"],
        "D", "easy", "numerical",
        "W = 30 × (9.8/6) ≈ 49 N.",
        "W = ৩০ × (৯.৮/৬) ≈ ৪৯ N।",
    ),
    q(
        "If Earth’s radius is doubled keeping mass fixed, weight of a body becomes:",
        "ভর ধ্রুব রেখে পৃথিবীর ব্যাসার্ধ দ্বিগুণ হলে কোনো বস্তুর ওজন হবে—",
        ["One-fourth", "Half", "Double", "Four times"],
        ["এক-চতুর্থাংশ", "অর্ধেক", "দ্বিগুণ", "চারগুণ"],
        "A", "medium", "numerical",
        "g ∝ 1/R^2 ⇒ g' = g/4 ⇒ weight quartered.",
        "g ∝ 1/R^2 ⇒ ওজন এক-চতুর্থাংশ।",
    ),
    q(
        "A planet has mass and radius each half of Earth’s. Its surface g compared with Earth’s g is:",
        "কোনো গ্রহের ভর ও ব্যাসার্ধ পৃথিবীর অর্ধেক হলে পৃষ্ঠে g পৃথিবীর g এর—",
        ["Equal", "Half", "Double", "Four times"],
        ["সমান", "অর্ধেক", "দ্বিগুণ", "চারগুণ"],
        "C", "medium", "numerical",
        "g' = G(M/2)/(R/2)^2 = 2 (GM/R^2) = 2g.",
        "g' = ২g।",
    ),
    q(
        "At which latitude is effective g the smallest (rotation included)?",
        "কত অক্ষাংশে অভিকর্ষজ ত্বরণের মান সবচেয়ে কম?",
        ["0°", "30°", "45°", "90°"],
        ["০°", "৩০°", "৪৫°", "৯০°"],
        "A", "easy", "conceptual",
        "g' = g − ω^2 R cos^2 λ is minimum at λ = 0° (equator).",
        "λ = ০° (বিষুব) এ g সর্বনিম্ন।",
    ),
    q(
        "A simple pendulum is taken from the equator to the pole. Its time period:",
        "সরল দোলককে নিরক্ষীয় অঞ্চল হতে মেরুতে আনলে দোলনকাল—",
        ["Remains same", "Becomes zero", "Increases", "Decreases"],
        ["সমান থাকে", "শূন্য হয়", "বাড়ে", "কমে"],
        "D", "medium", "application",
        "T = 2π√(l/g); g increases toward poles ⇒ T decreases.",
        "মেরুতে g বাড়ে ⇒ T কমে।",
    ),
    q(
        "At the equator, effective gravity with Earth’s spin is:",
        "নিরক্ষরেখায় অভিকর্ষজ ত্বরণের মান—",
        ["g' = g + ω^2 R", "g' = 1 − ω^2 R", "g' = g − ω^2 R", "g' = g + ω R"],
        ["g' = g + ω^2 R", "g' = 1 − ω^2 R", "g' = g − ω^2 R", "g' = g + ω R"],
        "C", "easy", "factual",
        "At equator cos λ = 1 ⇒ g' = g − ω^2 R.",
        "বিষুবে g' = g − ω^2 R।",
    ),
    q(
        "If Earth stopped rotating, weight of a body at a place would:",
        "পৃথিবীর ঘূর্ণন না থাকলে পৃথিবীপৃষ্ঠের কোনো স্থানে বস্তুর ওজন—",
        ["Increase", "Become zero", "Become infinite", "Remain unchanged"],
        ["বৃদ্ধি পাবে", "শূন্য হবে", "অসীম হবে", "অপরিবর্তিত থাকবে"],
        "A", "medium", "conceptual",
        "Removing the outward centrifugal effect increases effective weight.",
        "কেন্দ্রবিমুখী কমানো বন্ধ হলে কার্যকর ওজন বাড়ে।",
    ),
    q(
        "For the same small h, comparing surface g, height value g_h and depth value g_d:",
        "একই ছোট h এর জন্য ভূপৃষ্ঠের g, উচ্চতার g_h ও গভীরতার g_d সম্পর্কে সঠিক:",
        ["g_h < g_d < g", "g_d < g_h < g", "g < g_h < g_d", "g_h > g > g_d"],
        ["g_h < g_d < g", "g_d < g_h < g", "g < g_h < g_d", "g_h > g > g_d"],
        "A", "hard", "conceptual",
        "g_d = g(1 − h/R), g_h ≈ g(1 − 2h/R) ⇒ g_h < g_d < g.",
        "g_h ≈ g(1−২h/R) ছোট; তাই g_h < g_d < g।",
    ),
    q(
        "Causes of variation of g include: (i) Earth’s shape (ii) daily rotation (iii) height and depth",
        "g এর পরিবর্তনের কারণ—(i) পৃথিবীর আকার (ii) আহ্নিক গতি (iii) উচ্চতা ও গভীরতা",
        ["(i),(ii) only", "(ii),(iii) only", "(i),(iii) only", "(i),(ii),(iii)"],
        ["কেবল (i),(ii)", "কেবল (ii),(iii)", "কেবল (i),(iii)", "(i),(ii),(iii)"],
        "D", "easy", "conceptual",
        "Shape (oblateness), spin, and height/depth all change g.",
        "আকার, ঘূর্ণন ও উচ্চতা/গভীরতা—সবই g পরিবর্তন করে।",
    ),
    q(
        "A fictional planet has twice Earth’s radius and the same mass. Its surface g is Earth’s g times:",
        "পৃথিবীর দ্বিগুণ ব্যাসার্ধ ও সমান ভরের কাল্পনিক গ্রহের পৃষ্ঠে g পৃথিবীর—",
        ["4 times", "2 times", "1/2 times", "1/4 times"],
        ["৪ গুণ", "২ গুণ", "১/২ গুণ", "১/৪ গুণ"],
        "D", "easy", "numerical",
        "g' = GM/(2R)^2 = g/4.",
        "g' = g/৪।",
    ),
]


# ---------------------------------------------------------------------------
# t04 Satellites and escape speed / উপগ্রহ ও মুক্তিবেগ
# ---------------------------------------------------------------------------
T04 = [
    q(
        "Escape speed from Earth’s surface is approximately:",
        "পৃথিবীতে মুক্তিবেগের মান কত?",
        ["7.9 km s^-1", "11.2 km s^-1", "1.2 km s^-1", "112 m s^-1"],
        ["৭.৯ km s^-1", "১১.২ km s^-1", "১.২ km s^-1", "১১২ m s^-1"],
        "B", "easy", "factual",
        "v_e = √(2gR) ≈ 11.2 km/s.",
        "v_e ≈ ১১.২ km s^-1।",
    ),
    q(
        "Minimum speed to put a body into a near-Earth circular satellite orbit is about:",
        "ভূ-পৃষ্ঠ হতে কত বেগে ছুঁড়লে বস্তু কৃত্রিম উপগ্রহে পরিণত হবে?",
        ["11.2 km s^-1", "7.9 km s^-1", "11.2 m s^-1", "7.9 m s^-1"],
        ["১১.২ km s^-1", "৭.৯ km s^-1", "১১.২ m s^-1", "৭.৯ m s^-1"],
        "B", "easy", "factual",
        "Orbital speed v_o = √(gR) ≈ 7.9 km/s.",
        "কক্ষীয় বেগ ≈ ৭.৯ km s^-1।",
    ),
    q(
        "Escape speed from a planet of gravity g and radius R is:",
        "অভিকর্ষজ ত্বরণ g ও ব্যাসার্ধ R এর গ্রহে মুক্তিবেগ:",
        ["√(2gR)", "√(gR)", "2gR", "gR"],
        ["√(2gR)", "√(gR)", "2gR", "gR"],
        "A", "easy", "factual",
        "From energy: (1/2)mv_e^2 = GMm/R = mgR ⇒ v_e = √(2gR).",
        "v_e = √(2gR)।",
    ),
    q(
        "Relation between escape speed v_e and circular orbital speed v_o near the surface is:",
        "মুক্তিবেগ v_e ও পৃষ্ঠের কাছাকাছি বৃত্তাকার কক্ষীয় বেগ v_o এর সম্পর্ক:",
        ["v_o = v_e / √2", "v_o = √2 v_e", "v_o = 2 v_e", "v_o = v_e"],
        ["v_o = v_e / √2", "v_o = √2 v_e", "v_o = ২ v_e", "v_o = v_e"],
        "A", "medium", "factual",
        "v_e = √2 v_o ⇒ v_o = v_e/√2.",
        "v_e = √২ v_o।",
    ),
    q(
        "A planet has radius twice Earth’s and surface gravity eight times Earth’s. Its escape speed is about:",
        "গ্রহের ব্যাসার্ধ পৃথিবীর দ্বিগুণ ও পৃষ্ঠে g আটগুণ হলে মুক্তিবেগ প্রায়:",
        ["11.2 km s^-1", "22.4 km s^-1", "44.8 km s^-1", "5.6 km s^-1"],
        ["১১.২ km s^-1", "২২.৪ km s^-1", "৪৪.৮ km s^-1", "৫.৬ km s^-1"],
        "C", "hard", "numerical",
        "v_e' = √(2 × 8g × 2R) = 4 √(2gR) ≈ 4 × 11.2 = 44.8 km/s.",
        "v_e' = ৪ × ১১.২ = ৪৪.৮ km s^-1।",
    ),
    q(
        "Linear speed of an artificial satellite at height h is:",
        "কৃত্রিম উপগ্রহের রৈখিক বেগের সঠিক রাশিমালা:",
        ["√(GM/(R+h))", "√(GM(R+h))", "GM/(R+h)", "g(R+h)"],
        ["√(GM/(R+h))", "√(GM(R+h))", "GM/(R+h)", "g(R+h)"],
        "A", "medium", "factual",
        "Centripetal force = gravity ⇒ v = √(GM/(R+h)).",
        "v = √(GM/(R+h))।",
    ),
    q(
        "Period of a geostationary (parking-orbit) satellite is:",
        "ভূ-স্থির / পার্কিং কক্ষপথের উপগ্রহের পর্যায়কাল কত?",
        ["12 hours", "24 hours", "1 month", "1 year"],
        ["১২ ঘণ্টা", "২৪ ঘণ্টা", "১ মাস", "১ বছর"],
        "B", "easy", "factual",
        "It matches Earth’s sidereal rotation ≈ 24 h.",
        "পৃথিবীর আহ্নিক ঘূর্ণনের সাথে মিলে ≈ ২৪ ঘণ্টা।",
    ),
    q(
        "Parking orbit means the orbit of a:",
        "পার্কিং কক্ষপথ হলো—",
        ["Planet’s heliocentric path", "Geostationary satellite", "Polar satellite only", "Earth’s solar orbit"],
        ["গ্রহের সৌরপথ", "ভূ-স্থির উপগ্রহের কক্ষপথ", "কেবল মেরু উপগ্রহ", "পৃথিবীর সৌরকক্ষ"],
        "B", "easy", "factual",
        "Parking orbit refers to the geostationary orbit.",
        "পার্কিং কক্ষ = ভূ-স্থির উপগ্রহের কক্ষ।",
    ),
    q(
        "Escape speed from a planet depends on:",
        "পৃথিবীতে মুক্তিবেগ নির্ভর করে—",
        ["Mass of the projected body", "Radius (and mass/g) of the planet",
         "Radius of the body", "Colour of the body"],
        ["নিক্ষিপ্ত বস্তুর ভর", "গ্রহের ব্যাসার্ধ (ও ভর/g)",
         "বস্তুর ব্যাসার্ধ", "বস্তুর রঙ"],
        "B", "easy", "conceptual",
        "v_e = √(2GM/R) = √(2gR); independent of the body’s mass.",
        "v_e বস্তুর ভরের উপর নির্ভর করে না; গ্রহের R ও g এর উপর করে।",
    ),
    q(
        "Correct statements about escape speed: (i) depends on body’s mass (ii) ≈ 11.2 km/s on Earth (iii) depends on g",
        "মুক্তিবেগ সম্পর্কে সঠিক—(i) বস্তুর ভরের উপর নির্ভর (ii) পৃথিবীতে ≈ ১১.২ km/s (iii) g এর উপর নির্ভর",
        ["(i),(ii)", "(i),(iii)", "(ii),(iii)", "(i),(ii),(iii)"],
        ["(i),(ii)", "(i),(iii)", "(ii),(iii)", "(i),(ii),(iii)"],
        "C", "medium", "conceptual",
        "Independent of projectile mass; depends on planet via g and R.",
        "বস্তুর ভর নিরপেক্ষ; g ও R নির্ভর।",
    ),
    q(
        "A satellite orbits at height equal to Earth’s radius R. Its orbital speed is:",
        "কৃত্রিম উপগ্রহ পৃথিবীপৃষ্ঠ হতে R উচ্চতায় ঘুরলে এর বেগ:",
        ["√(2gR)", "√(gR)", "√(gR/2)", "√(0.5 g) only"],
        ["√(2gR)", "√(gR)", "√(gR/2)", "কেবল √(০.৫ g)"],
        "C", "medium", "numerical",
        "v = √(GM/(2R)) = √(gR/2).",
        "v = √(gR/২)।",
    ),
    q(
        "Extra speed that must be given to a near-Earth circular satellite to escape Earth is about:",
        "ভূ-পৃষ্ঠের কাছাকাছি বৃত্তাকার উপগ্রহকে পৃথিবী ছাড়তে অতিরিক্ত কত বেগ দিতে হয়?",
        ["3.25 km s^-1", "7.9 km s^-1", "11.2 km s^-1", "1.0 km s^-1"],
        ["৩.২৫ km s^-1", "৭.৯ km s^-1", "১১.২ km s^-1", "১.০ km s^-1"],
        "A", "hard", "numerical",
        "Δv = v_e − v_o = (√2 − 1)√(gR) ≈ 0.414 × 7.9 ≈ 3.27 km/s.",
        "Δv ≈ (√২ − ১) × ৭.৯ ≈ ৩.২৫ km s^-1।",
    ),
    q(
        "For geostationary satellites: (i) orbit in equatorial plane (ii) revolve west to east (iii) move at Earth’s escape speed",
        "ভূ-স্থির উপগ্রহের ক্ষেত্রে—(i) নিরক্ষীয় তলে কক্ষ (ii) পশ্চিম থেকে পূর্বে আবর্তন (iii) মুক্তিবেগে চলে",
        ["(i),(ii)", "(i),(iii)", "(ii),(iii)", "(i),(ii),(iii)"],
        ["(i),(ii)", "(i),(iii)", "(ii),(iii)", "(i),(ii),(iii)"],
        "A", "medium", "conceptual",
        "Geostationary: equatorial, same sense as Earth; orbital speed ≪ escape speed.",
        "নিরক্ষীয় ও পূর্বাভিমুখী; বেগ মুক্তিবেগ নয়।",
    ),
    q(
        "Two satellites in circular orbits of radii R and 2R have period ratio:",
        "ব্যাসার্ধ R ও 2R এর বৃত্তাকার কক্ষে দুই উপগ্রহের পর্যায়কালের অনুপাত:",
        ["1 : 2√2", "2√2 : 1", "1 : 2", "1 : 8"],
        ["১ : ২√২", "২√২ : ১", "১ : ২", "১ : ৮"],
        "A", "hard", "numerical",
        "T ∝ r^{3/2} ⇒ T2/T1 = (2)^{3/2} = 2√2.",
        "T₂/T₁ = ২√২।",
    ),
    q(
        "A satellite orbits 1600 km above Earth (R = 6400 km, g = 9.8 m s^-2). Its orbital speed is about:",
        "পৃথিবী পৃষ্ঠ হতে ১৬০০ km উপরে উপগ্রহের বেগ প্রায় (R = ৬৪০০ km, g = 9.8):",
        ["3.13 km s^-1", "7.09 km s^-1", "7.9 km s^-1", "11.2 km s^-1"],
        ["৩.১৩ km s^-1", "৭.০৯ km s^-1", "৭.৯ km s^-1", "১১.২ km s^-1"],
        "B", "hard", "numerical",
        "r = R+h = 8000 km; v = √(g R^2 / r) ≈ 7.09 km/s.",
        "r = ৮০০০ km; v = √(g R^2 / r) ≈ ৭.০৯ km/s।",
    ),
    q(
        "If g is constant, escape speed is proportional to the planet’s radius as:",
        "অভিকর্ষজ ত্বরণ ধ্রুব হলে মুক্তিবেগ গ্রহের ব্যাসার্ধের—",
        ["Directly proportional", "Inversely proportional",
         "Proportional to square root", "Inversely to square root"],
        ["সমানুপাতিক", "ব্যস্তানুপাতিক", "বর্গমূলের সমানুপাতিক", "বর্গমূলের ব্যস্তানুপাতিক"],
        "C", "medium", "conceptual",
        "v_e = √(2gR) ⇒ v_e ∝ √R when g fixed.",
        "g ধ্রুব হলে v_e ∝ √R।",
    ),
    q(
        "A planet with same mass as Earth has radius half and surface g twice Earth’s. Its escape speed compared with Earth’s is:",
        "পৃথিবীর সমভর গ্রহের ব্যাসার্ধ অর্ধেক ও g দ্বিগুণ হলে মুক্তিবেগ পৃথিবীর তুলনায়—",
        ["Double", "Equal", "Half", "One-fourth"],
        ["দ্বিগুণ", "সমান", "অর্ধেক", "এক-চতুর্থাংশ"],
        "B", "hard", "numerical",
        "v_e' = √(2g'(R/2)) = √(2·2g·R/2) = √(2gR) = v_e.",
        "v_e' = √(2gR) = পৃথিবীর সমান।",
    ),
    q(
        "Minimum upward launch speed so a body never returns to Earth is:",
        "ভূ-পৃষ্ঠ হতে উপরের দিকে সর্বনিম্ন কত বেগে নিক্ষেপ করলে বস্তু আর ফিরে আসে না?",
        ["2gR", "gR", "√(2gR)", "√(gR)"],
        ["2gR", "gR", "√(2gR)", "√(gR)"],
        "C", "easy", "factual",
        "That minimum speed is the escape speed √(2gR).",
        "সর্বনিম্ন বেগ = মুক্তিবেগ √(2gR)।",
    ),
    q(
        "If mean Sun–Earth distance decreases, the length of the year:",
        "সূর্য থেকে পৃথিবীর গড় দূরত্ব কমে গেলে বছরের দৈর্ঘ্য—",
        ["Decreases", "Increases", "Stays fixed", "Becomes infinite"],
        ["কমে যায়", "বেড়ে যায়", "স্থির থাকে", "অসীম হয়"],
        "A", "easy", "application",
        "Kepler III: smaller a ⇒ smaller T.",
        "ছোট কক্ষ ⇒ ছোট বছর।",
    ),
    q(
        "An astronaut of mass 80 kg on the Moon still has mass:",
        "৮০ kg ভরের নভোচারীর চাঁদে ভর কত?",
        ["784 kg", "784 N", "80 N", "80 kg"],
        ["৭৮৪ kg", "৭৮৪ N", "৮০ N", "৮০ kg"],
        "D", "easy", "conceptual",
        "Mass is invariant; weight changes with g.",
        "ভর অপরিবর্তিত; ওজন g অনুসারে বদলায়।",
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
    write_topic("phy1_27_ch06_t01", T01)
    write_topic("phy1_27_ch06_t02", T02)
    write_topic("phy1_27_ch06_t03", T03)
    write_topic("phy1_27_ch06_t04", T04)

    summary = {
        "paper": "physics_1",
        "chapter": 6,
        "title_en": "Gravitation and Gravity",
        "title_bn": "মহাকর্ষ ও অভিকর্ষ",
        "per_topic": 20,
        "topics": {
            "phy1_27_ch06_t01": 20,
            "phy1_27_ch06_t02": 20,
            "phy1_27_ch06_t03": 20,
            "phy1_27_ch06_t04": 20,
        },
        "source": SOURCE,
        "verified": False,
        "mcq_printed_pages": [199, 206],
        "notes": (
            "OCR-noisy pages 199–206 reconstructed as HSC-accurate bilingual MCQs; "
            "figure-only items rewritten in text; Newton/Kepler, field/potential, "
            "g-variation and satellite/escape staples preserved with corrected arithmetic."
        ),
    }
    out = (
        ROOT
        / "content"
        / "bank"
        / "udvash_raw"
        / "physics_1"
        / "parsed"
        / "ch06_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("summary", out)


if __name__ == "__main__":
    main()
