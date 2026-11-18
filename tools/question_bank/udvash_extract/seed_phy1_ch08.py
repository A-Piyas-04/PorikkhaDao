#!/usr/bin/env python3
"""Seed Physics 1st Paper Ch8 (Periodic Motion) bilingual MCQs.

Curated from Udvash HSC Question Bank 2026 printed pages 268–277 (OCR + HSC reconstruction).
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
    "physics p1 ch08; curated bilingual"
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
# t01 Periodic and simple harmonic motion / পর্যাবৃত্তিক ও সরল ছন্দিত গতি
# ---------------------------------------------------------------------------
T01 = [
    q(
        "Motion that repeats itself after equal time intervals is called:",
        "সমান সময় অন্তর অন্তর নিজেই পুনরাবৃত্ত হয় এমন গতিকে বলে—",
        ["Rectilinear motion", "Periodic motion", "Relative motion", "Random motion"],
        ["সরলরৈখিক গতি", "পর্যাবৃত্তিক গতি", "আপেক্ষিক গতি", "এলোমেলো গতি"],
        "B", "easy", "factual",
        "Periodic motion repeats identically after a fixed period T.",
        "পর্যাবৃত্তিক গতি নির্দিষ্ট পর্যায়কাল T পর পুনরাবৃত্ত হয়।",
    ),
    q(
        "The motion of the hands of a clock is an example of:",
        "ঘড়ির কাঁটার গতি কোন গতির উদাহরণ?",
        ["Periodic motion", "Simple harmonic motion", "Rectilinear motion", "Relative motion"],
        ["পর্যাবৃত্তিক গতি", "সরল ছন্দিত গতি", "সরলরৈখিক গতি", "আপেক্ষিক গতি"],
        "A", "easy", "factual",
        "Clock hands repeat orientation periodically but are not SHM.",
        "ঘড়ির কাঁটা পর্যাবৃত্তিক; সরল ছন্দিত নয়।",
    ),
    q(
        "Which is a defining feature of simple harmonic motion?",
        "সরল ছন্দিত গতির বৈশিষ্ট্য কোনটি?",
        ["Acceleration proportional to displacement and directed to mean position",
         "Acceleration independent of displacement",
         "Velocity always constant",
         "Force directed away from mean position"],
        ["ত্বরণ সরণের সমানুপাতিক ও সাম্যাবস্থানের দিকে",
         "ত্বরণ সরণনির্ভর নয়",
         "বেগ সবসময় ধ্রুবক",
         "বল সাম্যাবস্থান থেকে দূরে"],
        "A", "easy", "conceptual",
        "SHM: a = −ω²x (restoring, ∝ displacement).",
        "SHM: a = −ω²x (প্রত্যয়নী, সরণের সমানুপাতিক)।",
    ),
    q(
        "For the restoring force in SHM, which statement is correct?",
        "সরল ছন্দিত গতির প্রত্যয়নী বলের ক্ষেত্রে কোনটি সঠিক?",
        ["It obeys Hooke's law", "It does not obey Hooke's law",
         "It is inversely proportional to displacement", "It is not directed toward equilibrium"],
        ["হুকের সূত্র মেনে চলে", "হুকের সূত্র মেনে চলে না",
         "সরণের ব্যস্তানুপাতিক", "সাম্যাবস্থান অভিমুখী নয়"],
        "A", "easy", "conceptual",
        "F = −kx follows Hooke's law and points to equilibrium.",
        "F = −kx হুকের সূত্র মেনে সাম্যাবস্থানের দিকে।",
    ),
    q(
        "Which is the differential equation of SHM?",
        "নিচের কোনটি সরল ছন্দিত স্পন্দনের ব্যবকলনীয় সমীকরণ?",
        ["d²x/dt² = −ω²x", "d²x/dt² = ω²x", "d²x/dt² = −ωx", "d²x/dt² = ωx²"],
        ["d²x/dt² = −ω²x", "d²x/dt² = ω²x", "d²x/dt² = −ωx", "d²x/dt² = ωx²"],
        "A", "easy", "factual",
        "From a = −ω²x, d²x/dt² + ω²x = 0.",
        "a = −ω²x ⇒ d²x/dt² + ω²x = 0।",
    ),
    q(
        "Characteristics of SHM include:",
        "সরল ছন্দিত স্পন্দনের বৈশিষ্ট্য—",
        ["(i) and (ii) only: motion periodic; acceleration ∝ displacement",
         "(ii) and (iii) only: acceleration ∝ displacement; always circular",
         "(i) and (iii) only: periodic; force away from mean",
         "All of: periodic; a ∝ −x; motion along a straight line"],
        ["(i) ও (ii): গতি পর্যাবৃত্ত; ত্বরণ সরণের সমানুপাতিক",
         "(ii) ও (iii): ত্বরণ ∝ সরণ; সবসময় বৃত্তাকার",
         "(i) ও (iii): পর্যাবৃত্ত; বল সাম্যা থেকে দূরে",
         "সবগুলো: পর্যাবৃত্ত; a ∝ −x; সরলরৈখিক"],
        "D", "medium", "conceptual",
        "SHM is periodic, linear, with a = −ω²x.",
        "SHM পর্যাবৃত্ত, সরলরৈখিক এবং a = −ω²x।",
    ),
    q(
        "If SHM is the projection of uniform circular motion, then:",
        "যদি সরলদোলগতি সুষম বৃত্তাকার গতির অভিক্ষেপ হয় তবে—",
        ["Amplitude equals the circle radius; periods equal; ω_SHM equals angular speed",
         "Only amplitudes equal", "Only periods equal", "ω_SHM is unrelated to circular speed"],
        ["বিস্তার = ব্যাসার্ধ; পর্যায়কাল একই; ω_SHM = কৌণিক বেগ",
         "কেবল বিস্তার সমান", "কেবল পর্যায়কাল সমান", "ω_SHM সম্পর্কহীন"],
        "A", "medium", "conceptual",
        "Reference circle: A = R, same T, ω same as circular angular speed.",
        "প্রসঙ্গ বৃত্তে A = R, একই T, একই ω।",
    ),
    q(
        "The angular frequency ω of an SHM oscillator of mass m and spring constant k is:",
        "m ভর ও k স্প্রিং ধ্রুবকের সরল ছন্দিত স্পন্দনে কৌণিক কম্পাঙ্ক—",
        ["ω = √(k/m)", "ω = √(m/k)", "ω = k/m", "ω = 2π√(k/m)"],
        ["ω = √(k/m)", "ω = √(m/k)", "ω = k/m", "ω = 2π√(k/m)"],
        "A", "easy", "factual",
        "From F = −kx = ma ⇒ ω² = k/m.",
        "F = −kx = ma ⇒ ω² = k/m।",
    ),
    q(
        "Time period of SHM for force constant k and mass m is:",
        "বল ধ্রুবক k ও ভর m এর জন্য সরল ছন্দিত গতির পর্যায়কাল—",
        ["T = 2π√(m/k)", "T = 2π√(k/m)", "T = 2π m/k", "T = √(k/m)"],
        ["T = 2π√(m/k)", "T = 2π√(k/m)", "T = 2π m/k", "T = √(k/m)"],
        "A", "easy", "factual",
        "T = 2π/ω with ω = √(k/m).",
        "ω = √(k/m) ⇒ T = 2π√(m/k)।",
    ),
    q(
        "Period of SHM is related to the force constant k as:",
        "সরল দোলন গতি সম্পন্ন কণার পর্যায়কাল বল ধ্রুবকের—",
        ["Directly proportional", "Proportional to square root",
         "Inversely proportional", "Inversely proportional to square root"],
        ["সমানুপাতিক", "বর্গমূলের সমানুপাতিক",
         "ব্যস্তানুপাতিক", "বর্গমূলের ব্যস্তানুপাতিক"],
        "D", "easy", "conceptual",
        "T = 2π√(m/k) ⇒ T ∝ 1/√k.",
        "T = 2π√(m/k) ⇒ T ∝ 1/√k।",
    ),
    q(
        "A spring of constant k is cut into five equal pieces. Constant of each piece is:",
        "k স্প্রিং ধ্রুবকের স্প্রিংকে সমান পাঁচ টুকরা করলে প্রতি টুকরার ধ্রুবক—",
        ["k/5", "k", "2k", "5k"],
        ["k/5", "k", "2k", "5k"],
        "D", "medium", "numerical",
        "k ∝ 1/L; cutting into 5 equal parts multiplies k by 5.",
        "k ∝ 1/L; পাঁচ সমান খণ্ডে k পাঁচগুণ।",
    ),
    q(
        "A spring of 100 N m^-1 is cut into two equal parts. Each part has spring constant:",
        "100 N m^-1 স্প্রিংকে সমান দুই ভাগে কাটলে প্রতি খণ্ডের স্প্রিং ধ্রুবক—",
        ["50 N m^-1", "100 N m^-1", "200 N m^-1", "10^4 N m^-1"],
        ["50 N m^-1", "100 N m^-1", "200 N m^-1", "10^4 N m^-1"],
        "C", "medium", "numerical",
        "Halving length doubles k: 2 × 100 = 200 N m^-1.",
        "দৈর্ঘ্য অর্ধেক ⇒ k দ্বিগুণ = 200 N m^-1।",
    ),
    q(
        "For a mass on a spring, period depends on:",
        "স্প্রিংসংযুক্ত স্পন্দনের ক্ষেত্রে দোলনকাল নির্ভর করে—",
        ["Spring constant and mass only", "g only", "Mass and g only", "Amplitude only"],
        ["স্প্রিং ধ্রুবক ও ভরের উপর", "কেবল g এর উপর", "ভর ও g এর উপর", "কেবল বিস্তারের উপর"],
        "A", "easy", "conceptual",
        "T = 2π√(m/k); independent of g and amplitude (ideal).",
        "T = 2π√(m/k); g ও বিস্তারনির্ভর নয়।",
    ),
    q(
        "If spring constant increases for fixed mass, the oscillation period:",
        "নির্দিষ্ট ভরের জন্য স্প্রিং ধ্রুবক বাড়লে দোলনকাল—",
        ["Increases", "Decreases", "Remains same", "Becomes infinite"],
        ["বাড়ে", "কমে", "একই থাকে", "অসীম হয়"],
        "B", "easy", "conceptual",
        "T ∝ 1/√k, so larger k means smaller T (higher frequency).",
        "T ∝ 1/√k; k বাড়লে T কমে।",
    ),
    q(
        "Phase difference between extreme position and mean position in SHM is:",
        "সরল ছন্দিত স্পন্দনে সর্বোচ্চ অবস্থান ও সাম্যাবস্থানের দশা পার্থক্য—",
        ["0", "π/4", "π/2", "π"],
        ["0", "π/4", "π/2", "π"],
        "C", "easy", "factual",
        "Quarter period separates extreme and mean ⇒ Δφ = π/2.",
        "এক চতুর্থাংশ পর্যায়ে ⇒ Δφ = π/2।",
    ),
    q(
        "Which is equivalent to zero phase?",
        "নিচের কোনটি শূন্য দশার সমতুল্য?",
        ["π/2", "π", "3π/2", "2π"],
        ["π/2", "π", "3π/2", "2π"],
        "D", "easy", "factual",
        "Phase is defined modulo 2π; 2π ≡ 0.",
        "দশা 2π মডুলো; 2π ≡ 0।",
    ),
    q(
        "Initial phase means the phase of the oscillator at:",
        "t = 0 সময়ে সরলদোলন গতি সম্পন্ন কণার দশাকে বলে—",
        ["Angular phase", "Linear phase", "Initial phase", "Instantaneous phase only"],
        ["কৌণিক দশা", "রৈখিক দশা", "আদি দশা", "কেবল তাৎক্ষণিক দশা"],
        "C", "easy", "factual",
        "Phase at t = 0 is called the initial (epoch) phase φ.",
        "t = 0 এ দশা = আদি দশা φ।",
    ),
    q(
        "If a particle starts SHM from the extreme position, initial phase is:",
        "সরল ছন্দিত কণা সর্বোচ্চ সরণ অবস্থান হতে যাত্রা শুরু করলে আদি দশা—",
        ["0", "π/4", "π/2", "π"],
        ["0", "π/4", "π/2", "π"],
        "C", "medium", "conceptual",
        "x = A sin(ωt + φ); at t=0, x=A ⇒ sin φ = 1 ⇒ φ = π/2 (or use cos form with φ=0).",
        "x = A sin(ωt+φ); t=0 এ x=A ⇒ φ = π/2।",
    ),
    q(
        "Two SHM displacements x = A cos ωt and x = A sin ωt have phase difference:",
        "x = A cos ωt ও x = A sin ωt এর মধ্যকার দশা পার্থক্য—",
        ["0", "π/4", "π/2", "2π"],
        ["0", "π/4", "π/2", "2π"],
        "C", "medium", "conceptual",
        "cos ωt = sin(ωt + π/2); phase difference is π/2.",
        "cos ωt = sin(ωt + π/2); দশা পার্থক্য π/2।",
    ),
    q(
        "In the equation x = A sin(ωt + φ), the quantity φ represents:",
        "x = A sin(ωt + φ) সমীকরণে φ নির্দেশ করে—",
        ["Only position", "Only velocity", "Only acceleration", "Oscillatory state (phase) of motion"],
        ["কেবল অবস্থান", "কেবল বেগ", "কেবল ত্বরণ", "গতির দশাগত অবস্থা"],
        "D", "easy", "conceptual",
        "Phase φ (with ωt) fixes the instantaneous state of displacement/velocity.",
        "দশা φ সরণ/বেগের তাৎক্ষণিক অবস্থা নির্ধারণ করে।",
    ),
]


# ---------------------------------------------------------------------------
# t02 SHM displacement, velocity and acceleration
# ---------------------------------------------------------------------------
T02 = [
    q(
        "Relation between acceleration and displacement in SHM is:",
        "সরল ছন্দিত গতি সম্পন্ন কণার ত্বরণ ও সরণের সম্পর্ক—",
        ["Inversely proportional", "Inversely proportional to square",
         "Directly proportional (a = −ω²x)", "Proportional to square"],
        ["ব্যস্তানুপাতিক", "বর্গের ব্যস্তানুপাতিক",
         "সমানুপাতিক (a = −ω²x)", "বর্গের সমানুপাতিক"],
        "C", "easy", "factual",
        "Magnitude of a ∝ |x|; direction opposite (a = −ω²x).",
        "|a| ∝ |x|; দিক বিপরীত (a = −ω²x)।",
    ),
    q(
        "Correct expression for SHM velocity is:",
        "সরল দোলগতির বেগের সঠিক রাশিমালা কোনটি?",
        ["v = ω√(A² − x²)", "v = ω(A² − x²)", "v = A sin(ωt + φ) only as velocity", "v = A cos(ωt + φ) as displacement"],
        ["v = ω√(A² − x²)", "v = ω(A² − x²)", "v = A sin(ωt + φ) কেবল বেগ হিসেবে", "v = A cos(ωt + φ) সরণ হিসেবে"],
        "A", "easy", "factual",
        "From energy or differentiation: v = ±ω√(A² − x²).",
        "v = ±ω√(A² − x²)।",
    ),
    q(
        "In SHM, when displacement is maximum:",
        "সরল ছন্দিত গতিতে সরণ সর্বাধিক হলে—",
        ["Velocity is maximum", "Velocity is infinite",
         "Velocity is maximum and acceleration zero", "Velocity is minimum (zero)"],
        ["বেগ সর্বোচ্চ", "বেগ অসীম",
         "বেগ সর্বোচ্চ ও ত্বরণ শূন্য", "বেগ সর্বনিম্ন (শূন্য)"],
        "D", "easy", "conceptual",
        "At x = ±A, v = 0 and |a| = ω²A is maximum.",
        "x = ±A এ v = 0 এবং |a| সর্বোচ্চ।",
    ),
    q(
        "At the mean position in SHM:",
        "একটি সরলদোলকের সাম্যাবস্থানে—",
        ["Velocity and acceleration both maximum", "Velocity minimum, acceleration maximum",
         "Both velocity and acceleration zero", "Velocity maximum, acceleration minimum (zero)"],
        ["বেগ ও ত্বরণ উভয় সর্বোচ্চ", "বেগ সর্বনিম্ন, ত্বরণ সর্বোচ্চ",
         "বেগ ও ত্বরণ উভয় শূন্য", "বেগ সর্বোচ্চ, ত্বরণ সর্বনিম্ন (শূন্য)"],
        "D", "easy", "conceptual",
        "At x = 0: v = ±ωA (max), a = 0.",
        "x = 0 এ v = ±ωA (সর্বোচ্চ), a = 0।",
    ),
    q(
        "When displacement is maximum in SHM, which are true?",
        "সরল ছন্দিত স্পন্দনে সরণ সর্বোচ্চ হলে সত্য—",
        ["Acceleration maximum and velocity minimum only",
         "Velocity minimum and force maximum (hence all of i,ii,iii)",
         "Only force maximum", "Only velocity minimum"],
        ["কেবল ত্বরণ সর্বোচ্চ ও বেগ সর্বনিম্ন",
         "বেগ সর্বনিম্ন ও বল সর্বোচ্চ (i, ii, iii সব)",
         "কেবল বল সর্বোচ্চ", "কেবল বেগ সর্বনিম্ন"],
        "B", "medium", "conceptual",
        "At extreme: |a| max, v = 0, |F|=m|a| max.",
        "চরমে |a| সর্বোচ্চ, v = 0, |F| সর্বোচ্চ।",
    ),
    q(
        "At maximum displacement (amplitude) in SHM:",
        "সরল ছন্দিত গতিতে সর্বাধিক সরণ (বিস্তার) হলে—",
        ["Velocity zero and acceleration maximum", "Velocity and acceleration both zero",
         "Velocity maximum", "Acceleration zero only"],
        ["বেগ শূন্য ও ত্বরণ সর্বাধিক", "বেগ ও ত্বরণ উভয় শূন্য",
         "বেগ সর্বাধিক", "কেবল ত্বরণ শূন্য"],
        "A", "easy", "conceptual",
        "Extreme: v = 0, |a| = ω²A.",
        "চরমে v = 0, |a| = ω²A।",
    ),
    q(
        "Maximum velocity and maximum acceleration of SHM are 5 m s^-1 and 10 m s^-2. Period is:",
        "সর্বোচ্চ বেগ 5 m s^-1 ও সর্বোচ্চ ত্বরণ 10 m s^-2 হলে পর্যায়কাল—",
        ["0.785 s", "1.57 s", "3.14 s", "6.28 s"],
        ["0.785 s", "1.57 s", "3.14 s", "6.28 s"],
        "C", "medium", "numerical",
        "ω = a_max/v_max = 10/5 = 2 rad s^-1; T = 2π/ω = π ≈ 3.14 s.",
        "ω = 10/5 = 2; T = 2π/2 = π ≈ 3.14 s।",
    ),
    q(
        "For the particle above (v_max = 5, a_max = 10), amplitude is:",
        "উপরের কণার (v_max = 5, a_max = 10) বিস্তার—",
        ["1.0 m", "2.5 m", "5.0 m", "0.5 m"],
        ["1.0 m", "2.5 m", "5.0 m", "0.5 m"],
        "B", "medium", "numerical",
        "A = v_max/ω = 5/2 = 2.5 m (also A = a_max/ω²).",
        "A = v_max/ω = 5/2 = 2.5 m।",
    ),
    q(
        "If v_max = 16 m s^-1 and a_max = 64 m s^-2, angular frequency is:",
        "সর্বোচ্চ বেগ 16 m s^-1 ও সর্বোচ্চ ত্বরণ 64 m s^-2 হলে কৌণিক কম্পাঙ্ক—",
        ["2 rad s^-1", "4 rad s^-1", "8 rad s^-1", "16 rad s^-1"],
        ["2 rad s^-1", "4 rad s^-1", "8 rad s^-1", "16 rad s^-1"],
        "B", "medium", "numerical",
        "ω = a_max/v_max = 64/16 = 4 rad s^-1.",
        "ω = 64/16 = 4 rad s^-1।",
    ),
    q(
        "SHM period is 2 s. Angular frequency is:",
        "সরল ছন্দিত স্পন্দনে দোলনকাল 2 s হলে কৌণিক কম্পাঙ্ক—",
        ["3.14 rad s^-1", "1.57 rad s^-1", "0.637 rad s^-1", "0.318 rad s^-1"],
        ["3.14 rad s^-1", "1.57 rad s^-1", "0.637 rad s^-1", "0.318 rad s^-1"],
        "A", "easy", "numerical",
        "ω = 2π/T = 2π/2 = π ≈ 3.14 rad s^-1.",
        "ω = 2π/2 = π ≈ 3.14 rad s^-1।",
    ),
    q(
        "Displacement x = 0.1 sin(6πt + π/3) m. Which is correct?",
        "x = 0.1 sin(6πt + π/3) m হলে কোনটি সঠিক?",
        ["Period 1/3 s and v_max ≈ 1.88 m s^-1", "Period 3 s only",
         "Initial phase 0°", "v_max = 0.1 m s^-1"],
        ["পর্যায়কাল 1/3 s ও v_max ≈ 1.88 m s^-1", "কেবল পর্যায়কাল 3 s",
         "আদি দশা 0°", "v_max = 0.1 m s^-1"],
        "A", "hard", "numerical",
        "ω = 6π ⇒ T = 2π/ω = 1/3 s; v_max = ωA = 6π×0.1 ≈ 1.88 m s^-1; φ = π/3.",
        "ω = 6π ⇒ T = 1/3 s; v_max = 0.6π ≈ 1.88; φ = π/3।",
    ),
    q(
        "y = 0.5 sin(4πt) m. Period of oscillation is:",
        "y = 0.5 sin(4πt) m হলে স্পন্দনের পর্যায়কাল—",
        ["0.5 s", "1 s", "2 s", "4 s"],
        ["0.5 s", "1 s", "2 s", "4 s"],
        "A", "easy", "numerical",
        "ω = 4π; T = 2π/ω = 0.5 s.",
        "ω = 4π; T = 2π/(4π) = 0.5 s।",
    ),
    q(
        "For y = 0.5 sin(4πt) m, frequency is:",
        "y = 0.5 sin(4πt) m এর কম্পাঙ্ক—",
        ["0.5 Hz", "1 Hz", "2 Hz", "4 Hz"],
        ["0.5 Hz", "1 Hz", "2 Hz", "4 Hz"],
        "C", "easy", "numerical",
        "f = 1/T = 1/0.5 = 2 Hz (also ω = 2πf ⇒ f = 2).",
        "f = 1/0.5 = 2 Hz।",
    ),
    q(
        "Amplitude 0.01 m, frequency 1.2 Hz, displacement 0.005 m. Speed is about:",
        "বিস্তার 0.01 m, কম্পাঙ্ক 1.2 Hz, সরণ 0.005 m হলে বেগ প্রায়—",
        ["0.030 m s^-1", "0.065 m s^-1", "0.12 m s^-1", "0.653 m s^-1"],
        ["0.030 m s^-1", "0.065 m s^-1", "0.12 m s^-1", "0.653 m s^-1"],
        "B", "hard", "numerical",
        "v = 2πf√(A²−x²) = 2π(1.2)√(0.01²−0.005²) ≈ 0.065 m s^-1.",
        "v = 2πf√(A²−x²) ≈ 0.065 m s^-1।",
    ),
    q(
        "If displacement is half the amplitude, speed in terms of v_max is:",
        "সরণ বিস্তারের অর্ধেক হলে বেগ (v_max সর্বোচ্চ বেগ)—",
        ["v_max", "v_max/2", "(√3/2) v_max", "v_max/√2"],
        ["v_max", "v_max/2", "(√3/2) v_max", "v_max/√2"],
        "C", "medium", "numerical",
        "v = ω√(A²−(A/2)²) = (√3/2)ωA = (√3/2)v_max.",
        "v = (√3/2) v_max।",
    ),
    q(
        "Displacement 5 cm and acceleration 80 cm s^-2 in SHM. Period is:",
        "সরণ 5 cm ও ত্বরণ 80 cm s^-2 হলে পর্যায়কাল—",
        ["π/2 s", "π/4 s", "π s", "2π s"],
        ["π/2 s", "π/4 s", "π s", "2π s"],
        "A", "medium", "numerical",
        "|a| = ω²x ⇒ ω² = 80/5 = 16 ⇒ ω = 4; T = 2π/4 = π/2 s.",
        "ω² = 16 ⇒ T = π/2 s।",
    ),
    q(
        "v_max = 6 m s^-1, amplitude 30 cm. Period is approximately:",
        "সর্বোচ্চ বেগ 6 m s^-1, বিস্তার 30 cm হলে পর্যায়কাল প্রায়—",
        ["0.07 s", "0.314 s", "0.785 s", "3.14 s"],
        ["0.07 s", "0.314 s", "0.785 s", "3.14 s"],
        "B", "medium", "numerical",
        "A = 0.30 m; ω = v_max/A = 20; T = 2π/20 ≈ 0.314 s.",
        "ω = 6/0.3 = 20; T ≈ 0.314 s।",
    ),
    q(
        "v_max = 0.03 m s^-1, A = 0.006 m. Angular frequency is:",
        "সর্বোচ্চ বেগ 0.03 m s^-1, বিস্তার 0.006 m হলে কৌণিক কম্পাঙ্ক—",
        ["3 rad s^-1", "5 rad s^-1", "8 rad s^-1", "10 rad s^-1"],
        ["3 rad s^-1", "5 rad s^-1", "8 rad s^-1", "10 rad s^-1"],
        "B", "easy", "numerical",
        "ω = v_max/A = 0.03/0.006 = 5 rad s^-1.",
        "ω = 0.03/0.006 = 5 rad s^-1।",
    ),
    q(
        "T = 10 s. Relation between acceleration a and displacement x is:",
        "দোলনকাল 10 s হলে ত্বরণ a ও সরণ x এর সম্পর্ক—",
        ["a = −(π/5)² x", "a = −(2π)² x", "a = −(π/5) x", "a = −(20π)² x"],
        ["a = −(π/5)² x", "a = −(2π)² x", "a = −(π/5) x", "a = −(20π)² x"],
        "A", "medium", "numerical",
        "ω = 2π/T = 2π/10 = π/5; a = −ω²x = −(π/5)²x.",
        "ω = π/5; a = −(π/5)²x।",
    ),
    q(
        "a_max = 5 m s^-2 and v_max = 1.6 m s^-1. Period is approximately:",
        "সর্বোচ্চ ত্বরণ 5 m s^-2 ও সর্বোচ্চ বেগ 1.6 m s^-1 হলে পর্যায়কাল প্রায়—",
        ["π s", "2 s", "0.4 s", "0.2 s"],
        ["π s", "2 s", "0.4 s", "0.2 s"],
        "B", "hard", "numerical",
        "T = 2π v_max/a_max = 2π(1.6)/5 = 3.2π/5 ≈ 2.01 s ≈ 2 s.",
        "T = 2π×1.6/5 ≈ 2.01 s ≈ 2 s।",
    ),
]


# ---------------------------------------------------------------------------
# t03 Energy in SHM
# ---------------------------------------------------------------------------
T03 = [
    q(
        "Total energy of an SHM particle depends on:",
        "সরল ছন্দিত কণার মোট শক্তি কীসের উপর নির্ভর করে?",
        ["Instantaneous displacement only", "Instantaneous velocity only",
         "Amplitude", "Frequency only (not amplitude)"],
        ["কেবল তাৎক্ষণিক সরণ", "কেবল তাৎক্ষণিক বেগ",
         "বিস্তার", "কেবল কম্পাঙ্ক (বিস্তার নয়)"],
        "C", "easy", "factual",
        "E = (1/2)mω²A² = (1/2)kA²; depends on amplitude (and m, ω).",
        "E = (1/2)mω²A²; বিস্তারের উপর নির্ভর করে।",
    ),
    q(
        "In one full oscillation of a simple pendulum bob, total energy is entirely potential at how many positions?",
        "সরল দোলকের এক পূর্ণ দোলনে সমস্ত শক্তি বিভবশক্তি কতটি অবস্থানে?",
        ["One", "Two", "Three", "Four"],
        ["একটি", "দুইটি", "তিনটি", "চারটি"],
        "B", "easy", "conceptual",
        "At both extremes KE = 0, so E = PE.",
        "দুই চরমে KE = 0 ⇒ E = PE।",
    ),
    q(
        "At the mean position of SHM:",
        "সাম্যাবস্থানে সরল ছন্দিত গতিতে—",
        ["Potential energy is maximum", "Kinetic energy is maximum",
         "Total energy is zero", "Kinetic energy is zero"],
        ["বিভবশক্তি সর্বোচ্চ", "গতিশক্তি সর্বোচ্চ",
         "মোট শক্তি শূন্য", "গতিশক্তি শূন্য"],
        "B", "easy", "conceptual",
        "At mean: PE minimum (often zero), KE = E maximum.",
        "সাম্যায় PE ন্যূনতম, KE = E সর্বোচ্চ।",
    ),
    q(
        "At maximum amplitude in SHM:",
        "সর্বোচ্চ বিস্তারে সরল ছন্দিত গতিতে—",
        ["Kinetic energy is maximum", "Kinetic energy is zero",
         "Potential energy is zero", "Total energy is zero"],
        ["গতিশক্তি সর্বোচ্চ", "গতিশক্তি শূন্য",
         "বিভবশক্তি শূন্য", "মোট শক্তি শূন্য"],
        "B", "easy", "conceptual",
        "At extreme, speed is zero ⇒ KE = 0, PE = E.",
        "চরমে বেগ শূন্য ⇒ KE = 0, PE = E।",
    ),
    q(
        "Which are true for an SHM particle?",
        "সরল ছন্দিত স্পন্দনে গতিশীল কণার ক্ষেত্রে সত্য—",
        ["KE max at mean and velocity max at mean", "KE max at amplitude",
         "Velocity max at amplitude", "KE zero at mean"],
        ["সাম্যায় KE ও বেগ সর্বোচ্চ", "বিস্তারে KE সর্বোচ্চ",
         "বিস্তারে বেগ সর্বোচ্চ", "সাম্যায় KE শূন্য"],
        "A", "easy", "conceptual",
        "Mean position: max speed and max KE.",
        "সাম্যাবস্থানে সর্বোচ্চ বেগ ও KE।",
    ),
    q(
        "Expression (1/2)kA² for SHM represents:",
        "সরলদোলকের গতিতে (1/2)kA² নির্দেশ করে—",
        ["Only elastic PE at mean", "Maximum KE and also total energy",
         "Only instantaneous KE", "Only work against friction"],
        ["কেবল সাম্যায় স্থিতিশক্তি", "সর্বোচ্চ গতিশক্তি এবং মোট শক্তিও",
         "কেবল তাৎক্ষণিক KE", "কেবল ঘর্ষণের বিরুদ্ধে কাজ"],
        "B", "medium", "conceptual",
        "E = (1/2)kA² equals total energy and also max KE.",
        "E = (1/2)kA² = মোট শক্তি = সর্বোচ্চ KE।",
    ),
    q(
        "Mass 0.02 kg, T = 2 s, A = 0.2 m. At x = 0.1 m, ratio KE:PE is:",
        "ভর 0.02 kg, T = 2 s, A = 0.2 m; x = 0.1 m এ KE:PE—",
        ["1:2", "1:3", "3:1", "2:1"],
        ["1:2", "1:3", "3:1", "2:1"],
        "C", "hard", "numerical",
        "KE/PE = (A²−x²)/x² = (0.04−0.01)/0.01 = 3.",
        "KE/PE = (A²−x²)/x² = 3/1।",
    ),
    q(
        "A spring stretches 10 cm under 500 N. With 20 kg hung, elastic PE is about:",
        "500 N এ স্প্রিং 10 cm প্রসারিত; 20 kg ঝুলালে স্থিতিশক্তি প্রায়—",
        ["0.04 J", "1.90 J", "3.80 J", "9.81 J"],
        ["0.04 J", "1.90 J", "3.80 J", "9.81 J"],
        "C", "hard", "numerical",
        "k = 500/0.10 = 5000 N m^-1; δ = mg/k ≈ 0.0392 m; U = (1/2)kδ² ≈ 3.84 J.",
        "k = 5000; δ ≈ 0.0392; U ≈ 3.84 J।",
    ),
    q(
        "For x = A sin(ωt + φ), potential energy is proportional to:",
        "x = A sin(ωt + φ) হলে বিভবশক্তি সমানুপাতিক—",
        ["sin²(ωt + φ)", "cos²(ωt + φ)", "sin(ωt + φ)", "ωt only"],
        ["sin²(ωt + φ)", "cos²(ωt + φ)", "sin(ωt + φ)", "কেবল ωt"],
        "A", "medium", "conceptual",
        "PE = (1/2)k x² ∝ sin²(ωt + φ).",
        "PE = (1/2)kx² ∝ sin²(ωt + φ)।",
    ),
    q(
        "Kinetic energy in SHM with x = A sin(ωt + φ) is proportional to:",
        "x = A sin(ωt + φ) হলে গতিশক্তি সমানুপাতিক—",
        ["sin²(ωt + φ)", "cos²(ωt + φ)", "tan(ωt + φ)", "A only (no time)"],
        ["sin²(ωt + φ)", "cos²(ωt + φ)", "tan(ωt + φ)", "কেবল A (সময়হীন)"],
        "B", "medium", "conceptual",
        "v ∝ cos(ωt + φ) ⇒ KE ∝ cos²(ωt + φ).",
        "v ∝ cos(ωt + φ) ⇒ KE ∝ cos²(ωt + φ)।",
    ),
    q(
        "Total mechanical energy in ideal SHM is:",
        "আদর্শ সরল ছন্দিত গতিতে মোট যান্ত্রিক শক্তি—",
        ["Varies with time like sin²", "Constant and equal to (1/2)mω²A²",
         "Always zero", "Equal only to PE"],
        ["sin² এর মতো সময়ের সাথে বদলায়", "ধ্রুবক এবং (1/2)mω²A² এর সমান",
         "সবসময় শূন্য", "কেবল PE এর সমান"],
        "B", "easy", "factual",
        "E = KE + PE = (1/2)mω²A² is conserved.",
        "E = (1/2)mω²A² সংরক্ষিত।",
    ),
    q(
        "Displacement x = √3 sin(2πt) (in m). At 1 m from mean, KE:PE is:",
        "x = √3 sin(2πt) m; সাম্যা থেকে 1 m দূরে KE:PE—",
        ["1:2", "1:1", "2:1", "√3:1"],
        ["1:2", "1:1", "2:1", "√3:1"],
        "C", "hard", "numerical",
        "A² = 3; KE/PE = (3−1)/1 = 2 ⇒ 2:1.",
        "A² = 3; (A²−x²):x² = 2:1।",
    ),
    q(
        "A bob of mass 0.01 kg swings in a vertical circle of radius 0.3 m. KE at lowest point is:",
        "0.01 kg বব 0.3 m ব্যাসার্ধের উল্লম্ব বৃত্তে; নিম্নতম বিন্দুতে KE—",
        ["0.0245 J", "0.0294 J", "0.0194 J", "0.01 J"],
        ["0.0245 J", "0.0294 J", "0.0194 J", "0.01 J"],
        "B", "hard", "numerical",
        "From height 0.3 m: KE = mgh = 0.01×9.8×0.3 = 0.0294 J (if released from height R).",
        "KE = mgh = 0.01×9.8×0.3 = 0.0294 J।",
    ),
    q(
        "Average kinetic energy over a period in SHM equals:",
        "এক পর্যায়ে গড় গতিশক্তি সমান—",
        ["Total energy E", "E/2", "E/4", "Zero"],
        ["মোট শক্তি E", "E/2", "E/4", "শূন্য"],
        "B", "medium", "conceptual",
        "Time averages: ⟨KE⟩ = ⟨PE⟩ = E/2.",
        "⟨KE⟩ = ⟨PE⟩ = E/2।",
    ),
    q(
        "A mass-spring system obeys energy conservation when:",
        "স্প্রিং-ভর ব্যবস্থায় শক্তি সংরক্ষণ মেনে চলে যখন—",
        ["Friction is present and large", "Ideal undamped SHM (no non-conservative work)",
         "Amplitude grows with time", "Driving force does negative work only"],
        ["ঘর্ষণ বেশি", "আদর্শ অদমিত SHM (অসংরক্ষণশীল কাজ নেই)",
         "বিস্তার সময়ে বাড়ে", "চালক বল কেবল ঋণাত্মক কাজ করে"],
        "B", "easy", "conceptual",
        "Without damping/drive, mechanical energy is conserved.",
        "দমন/চালক ছাড়া যান্ত্রিক শক্তি সংরক্ষিত।",
    ),
    q(
        "Restoring force on SHM mass is proportional to:",
        "সরল ছন্দিত গতিতে প্রত্যয়নী বল সমানুপাতিক—",
        ["Velocity", "Displacement from mean", "Acceleration squared", "Mass only"],
        ["বেগের", "সাম্যা থেকে সরণের", "ত্বরণের বর্গের", "কেবল ভরের"],
        "B", "easy", "factual",
        "F = −kx ∝ displacement toward mean.",
        "F = −kx ∝ সরণ।",
    ),
    q(
        "Force constant of SHM oscillator with mass m and angular frequency ω is:",
        "ভর m ও কৌণিক কম্পাঙ্ক ω হলে বল ধ্রুবক—",
        ["m/ω", "mω", "mω²", "ω/m"],
        ["m/ω", "mω", "mω²", "ω/m"],
        "C", "easy", "factual",
        "k = mω².",
        "k = mω²।",
    ),
    q(
        "If amplitude is doubled keeping m and ω fixed, total energy becomes:",
        "m ও ω অপরিবর্তিত রেখে বিস্তার দ্বিগুণ করলে মোট শক্তি—",
        ["Same", "Double", "Four times", "Half"],
        ["একই", "দ্বিগুণ", "চারগুণ", "অর্ধেক"],
        "C", "easy", "numerical",
        "E ∝ A² ⇒ (2A)² gives 4E.",
        "E ∝ A² ⇒ 4 গুণ।",
    ),
    q(
        "At displacement x = A/√2, the ratio KE:PE is:",
        "সরণ x = A/√2 হলে KE:PE অনুপাত—",
        ["1:1", "1:2", "2:1", "1:3"],
        ["1:1", "1:2", "2:1", "1:3"],
        "A", "medium", "numerical",
        "(A²−x²):x² = (A²−A²/2):(A²/2) = 1:1.",
        "(A²−x²)/x² = 1।",
    ),
    q(
        "Which graph correctly describes PE vs x in SHM (ideal spring)?",
        "আদর্শ স্প্রিং SHM এ PE বনাম x সঠিক চরিত্র—",
        ["PE is minimum at x = 0 and rises as x² toward ±A",
         "PE maximum at x = 0", "PE linear in x", "PE independent of x"],
        ["x = 0 এ PE ন্যূনতম এবং ±A এর দিকে x² অনুসারে বাড়ে",
         "x = 0 এ PE সর্বোচ্চ", "PE x এর রৈখিক", "PE x নির্ভর নয়"],
        "A", "medium", "conceptual",
        "U = (1/2)kx² is a parabola centered at the mean position.",
        "U = (1/2)kx² প্যারাবোলা।",
    ),
]


# ---------------------------------------------------------------------------
# t04 Pendulums / দোলক
# ---------------------------------------------------------------------------
T04 = [
    q(
        "Time period of a simple pendulum is:",
        "সরল দোলকের দোলনকাল—",
        ["T = 2π√(L/g)", "T = 2π√(g/L)", "T = 2π L/g", "T = 2π√(mg/L)"],
        ["T = 2π√(L/g)", "T = 2π√(g/L)", "T = 2π L/g", "T = 2π√(mg/L)"],
        "A", "easy", "factual",
        "For small angles, T = 2π√(L/g).",
        "ক্ষুদ্র কোণে T = 2π√(L/g)।",
    ),
    q(
        "Frequency of a seconds pendulum is:",
        "একটি সেকেন্ড দোলকের কম্পাঙ্ক কত?",
        ["Infinite", "1 Hz", "0.5 Hz", "2 Hz"],
        ["অসীম", "1 Hz", "0.5 Hz", "2 Hz"],
        "C", "easy", "factual",
        "Seconds pendulum has T = 2 s ⇒ f = 0.5 Hz.",
        "সেকেন্ড দোলকে T = 2 s ⇒ f = 0.5 Hz।",
    ),
    q(
        "A pendulum that takes 0.5 s from mean to extreme is called:",
        "সাম্যাবস্থান হতে সর্বাধিক সরণে 0.5 s নেয় এমন দোলককে বলে—",
        ["Simple pendulum", "Compound pendulum", "Seconds pendulum", "Kater's pendulum"],
        ["সরল দোলক", "জটিল দোলক", "সেকেন্ড দোলক", "কেটার দোলক"],
        "C", "easy", "factual",
        "Mean→extreme is T/4; if 0.5 s then T = 2 s (seconds pendulum).",
        "T/4 = 0.5 ⇒ T = 2 s = সেকেন্ড দোলক।",
    ),
    q(
        "If effective length of a seconds pendulum is made 4 times, period becomes:",
        "সেকেন্ড দোলকের কার্যকরী দৈর্ঘ্য 4 গুণ করলে দোলনকাল হবে—",
        ["2 s", "4 s", "8 s", "16 s"],
        ["2 s", "4 s", "8 s", "16 s"],
        "B", "medium", "numerical",
        "T ∝ √L; L→4L ⇒ T→2T = 4 s.",
        "T ∝ √L; 4L ⇒ T = 4 s।",
    ),
    q(
        "To increase simple-pendulum period by 100%, effective length must increase by:",
        "দোলনকাল 100% বৃদ্ধিতে কার্যকরী দৈর্ঘ্য বৃদ্ধি করতে হবে—",
        ["100%", "200%", "300%", "400%"],
        ["100%", "200%", "300%", "400%"],
        "C", "hard", "numerical",
        "T₂ = 2T₁ ⇒ L₂ = 4L₁ ⇒ increase = 3L₁ = 300%.",
        "L₂ = 4L₁ ⇒ বৃদ্ধি 300%।",
    ),
    q(
        "Effective length of a seconds pendulum increased by 25.6%. Period increases by about:",
        "সেকেন্ড দোলকের কার্যকরী দৈর্ঘ্য 25.6% বৃদ্ধিতে দোলনকাল বৃদ্ধি প্রায়—",
        ["12%", "24%", "25.6%", "50%"],
        ["12%", "24%", "25.6%", "50%"],
        "A", "hard", "numerical",
        "ΔT/T ≈ (1/2)ΔL/L = 0.5×0.256 = 0.128 ≈ 12%.",
        "ΔT/T ≈ (1/2)ΔL/L ≈ 12%।",
    ),
    q(
        "Taking a pendulum clock to a mountain top:",
        "দোলক ঘড়িকে পাহাড়ের চূড়ায় নিলে—",
        ["Gains time and runs fast", "Loses time; period increases; runs slow",
         "Period unchanged", "Stops permanently"],
        ["সময় লাভ ও দ্রুত চলে", "সময় হারায়; দোলনকাল বাড়ে; ধীরে চলে",
         "দোলনকাল অপরিবর্তিত", "স্থায়ীভাবে থেমে যায়"],
        "B", "medium", "application",
        "g decreases on mountain ⇒ T increases ⇒ clock loses time.",
        "পাহাড়ে g কমে ⇒ T বাড়ে ⇒ সময় হারায়।",
    ),
    q(
        "Bringing a pendulum clock from mountain top to foot:",
        "দোলক ঘড়ি পাহাড়ের চূড়া থেকে পাদদেশে আনলে—",
        ["Period decreases and clock gains time", "Period increases and loses time",
         "Only loses time", "g decreases"],
        ["দোলনকাল হ্রাস ও সময় লাভ", "দোলনকাল বৃদ্ধি ও সময় হারানো",
         "কেবল সময় হারানো", "g কমে"],
        "A", "medium", "application",
        "g increases downhill ⇒ T decreases ⇒ clock runs fast (gains).",
        "পাদদেশে g বাড়ে ⇒ T কমে ⇒ সময় লাভ।",
    ),
    q(
        "A simple pendulum of length tripled is taken to Earth's center. Period becomes:",
        "কার্যকরী দৈর্ঘ্য তিনগুণ করে পৃথিবীর কেন্দ্রে নিলে দোলনকাল—",
        ["Zero", "Unchanged", "√3 times", "Infinite"],
        ["শূন্য", "একই", "√3 গুণ", "অসীম"],
        "D", "medium", "conceptual",
        "At Earth's center g = 0 ⇒ T = 2π√(L/g) → ∞.",
        "কেন্দ্রে g = 0 ⇒ T অসীম।",
    ),
    q(
        "On a planet with gravity g/4, period of a simple pendulum becomes:",
        "অভিকর্ষজ ত্বরণ g/4 এর গ্রহে সরল দোলকের দোলনকাল—",
        ["T/4", "T/2", "2T", "4T"],
        ["T/4", "T/2", "2T", "4T"],
        "C", "medium", "numerical",
        "T ∝ 1/√g; g→g/4 ⇒ T→2T.",
        "T ∝ 1/√g ⇒ 2T।",
    ),
    q(
        "Maximum angular amplitude for which pendulum motion is approximately SHM is usually taken as:",
        "সরলদোলকের ক্ষেত্রে সর্বোচ্চ কৌণিক বিস্তার সাধারণত ধরা হয়—",
        ["1°", "4°", "30°", "40°"],
        ["1°", "4°", "30°", "40°"],
        "B", "easy", "factual",
        "Small-angle approximation sinθ≈θ is used up to about 4° in many HSC texts.",
        "HSC পাঠ্যে প্রায় 4° পর্যন্ত ক্ষুদ্র কোণ আসন্ন।",
    ),
    q(
        "Length of a simple pendulum is 0.3 m and T = 0.8 s. For T = 2.4 s, length should be:",
        "দৈর্ঘ্য 0.3 m ও T = 0.8 s; T = 2.4 s করতে দৈর্ঘ্য—",
        ["0.9 m", "1.8 m", "2.4 m", "2.7 m"],
        ["0.9 m", "1.8 m", "2.4 m", "2.7 m"],
        "D", "hard", "numerical",
        "T ∝ √L ⇒ L₂/L₁ = (T₂/T₁)² = 9 ⇒ L₂ = 2.7 m.",
        "L₂ = 0.3×9 = 2.7 m।",
    ),
    q(
        "If length of a seconds pendulum increases by 1%, seconds lost per day are about:",
        "সেকেন্ড দোলকের দৈর্ঘ্য 1% বৃদ্ধিতে দিনে সময় হারানো প্রায়—",
        ["130 s", "259 s", "328 s", "430 s"],
        ["130 s", "259 s", "328 s", "430 s"],
        "D", "hard", "numerical",
        "ΔT/T ≈ (1/2)(ΔL/L) = 0.005; in 86400 s lose ≈ 432 s ≈ 430 s.",
        "ΔT/T ≈ 0.5%; 86400×0.005 ≈ 432 s।",
    ),
    q(
        "A child stands up on a swinging swing. The swing then:",
        "দোলনায় শিশু দাঁড়ালে দোলনার গতি—",
        ["Becomes slower", "Becomes faster", "Stops", "First fast then slow always"],
        ["ধীরে চলে", "দ্রুত চলে", "থেমে যায়", "প্রথমে দ্রুত পরে ধীরে"],
        "B", "medium", "application",
        "Standing raises CM, decreases effective L ⇒ T decreases ⇒ faster.",
        "ভরকেন্দ্র উপরে ⇒ L কমে ⇒ T কমে ⇒ দ্রুত।",
    ),
    q(
        "A person descends with acceleration a; period of a hand-held pendulum compared to rest:",
        "a ত্বরণে নিচে নামলে হাতের দোলকের দোলনকাল স্থির অবস্থার তুলনায়—",
        ["Increases", "Decreases", "Same", "Infinite"],
        ["বাড়ে", "কমে", "একই", "অসীম"],
        "A", "hard", "application",
        "Effective g_eff = g−a < g ⇒ T = 2π√(L/g_eff) increases.",
        "g_eff = g−a ⇒ T বাড়ে।",
    ),
    q(
        "Mass of simple-pendulum bob is made 5 times. Period:",
        "সরল দোলকের ববের ভর 5 গুণ করলে দোলনকাল—",
        ["Increases 5 times", "Decreases 5 times", "Decreases √5 times", "Remains the same"],
        ["5 গুণ বাড়ে", "5 গুণ কমে", "√5 গুণ কমে", "একই থাকে"],
        "D", "easy", "conceptual",
        "T = 2π√(L/g) independent of bob mass.",
        "T ভরনির্ভর নয়।",
    ),
    q(
        "A spring stretches 9.8 cm under mass m. Period after a small pull-release is (g = 9.8):",
        "m ভরে স্প্রিং 9.8 cm প্রসারিত; টেনে ছাড়লে পর্যায়কাল (g = 9.8)—",
        ["0.0628 s", "0.628 s", "6.28 s", "62.8 s"],
        ["0.0628 s", "0.628 s", "6.28 s", "62.8 s"],
        "B", "medium", "numerical",
        "T = 2π√(δ/g) = 2π√(0.098/9.8) = 2π×0.1 = 0.628 s.",
        "T = 2π√(δ/g) = 0.628 s।",
    ),
    q(
        "Why does a pendulum clock run slow?",
        "কোন কারণে দোলক ঘড়ি স্লো চলবে?",
        ["Increase L at fixed g (T increases)", "Decrease L at fixed g",
         "Increase g at fixed L", "Increase both L and g equally always"],
        ["g স্থির রেখে L বাড়ালে T বাড়ে", "g স্থির রেখে L কমালে",
         "L স্থির রেখে g বাড়ালে", "L ও g সমানুপাতে বাড়ালে"],
        "A", "medium", "application",
        "Larger L increases T so the clock loses time (runs slow).",
        "L বাড়লে T বাড়ে ⇒ ঘড়ি স্লো।",
    ),
    q(
        "For a seconds pendulum, which relation is correct (L effective length)?",
        "সেকেন্ড দোলকের ক্ষেত্রে সঠিক সম্পর্ক (L কার্যকরী দৈর্ঘ্য)—",
        ["g = 4π²L", "g = π²L", "g = 2πL", "g = L/(4π²)"],
        ["g = 4π²L", "g = π²L", "g = 2πL", "g = L/(4π²)"],
        "A", "medium", "factual",
        "T = 2 = 2π√(L/g) ⇒ g = 4π²L.",
        "T = 2 ⇒ g = 4π²L।",
    ),
    q(
        "Three springs of constants K, 2K, K in parallel with mass m = 0.08 kg, K = 2 N/m. Period is about:",
        "K, 2K, K স্প্রিং সমান্তরালে m = 0.08 kg, K = 2 N/m; পর্যায়কাল প্রায়—",
        ["0.628 s", "0.728 s", "0.828 s", "0.928 s"],
        ["0.628 s", "0.728 s", "0.828 s", "0.928 s"],
        "A", "hard", "numerical",
        "k_eq = K+2K+K = 4K = 8 N/m; T = 2π√(m/k) = 2π√(0.08/8) = 2π×0.1 = 0.628 s.",
        "k_eq = 8; T = 0.628 s।",
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
    write_topic("phy1_27_ch08_t01", T01)
    write_topic("phy1_27_ch08_t02", T02)
    write_topic("phy1_27_ch08_t03", T03)
    write_topic("phy1_27_ch08_t04", T04)

    summary = {
        "paper": "physics_1",
        "chapter": 8,
        "title_en": "Periodic Motion",
        "title_bn": "পর্যাবৃত্তিক গতি",
        "per_topic": 20,
        "topics": {
            "phy1_27_ch08_t01": 20,
            "phy1_27_ch08_t02": 20,
            "phy1_27_ch08_t03": 20,
            "phy1_27_ch08_t04": 20,
        },
        "source": SOURCE,
        "verified": False,
        "mcq_printed_pages": [268, 277],
        "notes": (
            "OCR-noisy pages 268–277 reconstructed as HSC-accurate bilingual MCQs; "
            "figure-only items rewritten in text; SHM definitions, kinematics, "
            "energy and pendulum/spring staples preserved with corrected arithmetic "
            "from printed answer keys where recoverable."
        ),
    }
    out = (
        ROOT
        / "content"
        / "bank"
        / "udvash_raw"
        / "physics_1"
        / "parsed"
        / "ch08_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("summary", out)


if __name__ == "__main__":
    main()
