#!/usr/bin/env python3
"""Seed Physics 1st Paper Ch4 (Newtonian Mechanics) bilingual MCQs.

Curated from Udvash HSC Question Bank 2026 printed pages 127–138 (OCR + HSC reconstruction).
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
    "physics p1 ch04; curated bilingual"
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
# t01 Newton's laws of motion / নিউটনের গতিসূত্র
# ---------------------------------------------------------------------------
T01 = [
    q(
        "A 100 kg person stands in a lift accelerating upward at 2 m s⁻² (g = 9.8 m s⁻²). The upward reaction on the person is:",
        "১০০ kg ভরের একজন লোক লিফটে ২ m s⁻² ত্বরণে উপরে উঠলে লোকটির উপর উর্ধ্বমুখী প্রতিক্রিয়া বল কত? (g = 9.8 m s⁻²)",
        ["780 N", "980 N", "1180 N", "1380 N"],
        ["780 N", "980 N", "1180 N", "1380 N"],
        "C", "medium", "numerical",
        "N = m(g + a) = 100 × (9.8 + 2) = 1180 N.",
        "N = m(g + a) = 100 × (9.8 + 2) = 1180 N।",
    ),
    q(
        "How many fundamental forces exist in nature?",
        "জগতে মৌলিক বলের সংখ্যা কয়টি?",
        ["2", "4", "5", "6"],
        ["২টি", "৪টি", "৫টি", "৬টি"],
        "B", "easy", "factual",
        "The four fundamental forces are gravitational, electromagnetic, strong nuclear and weak nuclear.",
        "মৌলিক বল চারটি: মহাকর্ষ, তড়িৎচৌম্বকীয়, সবল নিউক্লীয় ও দুর্বল নিউক্লীয়।",
    ),
    q(
        "Inertia of a body is proportional to its:",
        "বস্তুর গতি জড়তা কোনটির সমানুপাতিক?",
        ["Mass", "Velocity", "Momentum", "Force"],
        ["ভর", "বেগ", "ভরবেগ", "বল"],
        "A", "easy", "factual",
        "Inertia measures resistance to change of motion and scales with mass.",
        "জড়তা গতি পরিবর্তনের বাধা; এটি ভরের সমানুপাতিক।",
    ),
    q(
        "A person feels weightlessness in a lift when the lift:",
        "একজন ব্যক্তি লিফটে ওজনহীনতা অনুভব করবে, যখন লিফটটি:",
        ["Moves up at constant speed", "Moves down at constant speed", "Accelerates up at g", "Accelerates down at g"],
        ["সমবেগে উপরে উঠে", "সমবেগে নিচে নামে", "g ত্বরণে উপরে উঠে", "g ত্বরণে নিচে নামে"],
        "D", "medium", "conceptual",
        "Apparent weight W′ = m(g − a); if a = g downward, W′ = 0.",
        "আপাত ওজন W′ = m(g − a); নিচে a = g হলে W′ = 0।",
    ),
    q(
        "A constant force on a 0.1 kg body at rest produces acceleration 10 m s⁻². The force magnitude is:",
        "০.১ kg ভরের স্থির বস্তুর উপর সমবল প্রয়োগে ১০ m s⁻² সমত্বরণ হয়। প্রযুক্ত বলের মান কত?",
        ["0.1 N", "1 N", "10 N", "100 N"],
        ["0.1 N", "1 N", "10 N", "100 N"],
        "B", "easy", "numerical",
        "F = ma = 0.1 × 10 = 1 N.",
        "F = ma = 0.1 × 10 = 1 N।",
    ),
    q(
        "The angle between action and reaction forces is:",
        "ক্রিয়া ও প্রতিক্রিয়া বলের মধ্যে কোণের মান কত?",
        ["0 rad", "1 rad", "π/2 rad", "π rad"],
        ["0 rad", "1 rad", "π/2 rad", "π rad"],
        "D", "easy", "factual",
        "Action and reaction are equal, opposite and collinear: angle = 180° = π rad.",
        "ক্রিয়া–প্রতিক্রিয়া সমান, বিপরীত ও একরেখ: কোণ ১৮০° = π rad।",
    ),
    q(
        "A car moves at constant speed 10 m s⁻¹ on a straight road. Which statement is true?",
        "একটি গাড়ি ১০ m s⁻¹ সমবেগে চলছে। নিচের কোনটি সত্য?",
        ["No force acts on the car", "Driving force equals friction", "Driving force exceeds friction", "Driving force is less than friction"],
        ["গাড়ির উপর কোনো বলই ক্রিয়া করছে না", "গাড়ি দ্বারা প্রযুক্ত বল ঘর্ষণ বলের সমান", "গাড়ি দ্বারা প্রযুক্ত বল ঘর্ষণ বলের চেয়ে বেশি", "গাড়ি দ্বারা প্রযুক্ত বল ঘর্ষণ বলের চেয়ে কম"],
        "B", "medium", "conceptual",
        "Constant velocity ⇒ net force zero, so thrust balances friction.",
        "সমবেগে নিট বল শূন্য; তাই চালক বল = ঘর্ষণ।",
    ),
    q(
        "A body has acceleration when:",
        "একটি বস্তুর ত্বরণ থাকবে কখন?",
        ["It has velocity", "It has kinetic energy", "A net force acts on it", "It has momentum"],
        ["বেগ থাকলে", "গতিশক্তি থাকলে", "বল প্রযুক্ত থাকলে", "ভরবেগ থাকলে"],
        "C", "easy", "conceptual",
        "Newton’s second law: net force produces acceleration (a = F/m).",
        "নিউটনের দ্বিতীয় সূত্র: নিট বল থাকলে ত্বরণ হয়।",
    ),
    q(
        "If the net external force on a body is zero, then:",
        "কোনো বস্তুর উপর প্রযুক্ত বলসমূহের লব্ধি শূন্য হলে:",
        ["Only velocity is constant", "Only acceleration is zero", "Only momentum is constant", "Velocity, acceleration (zero) and momentum are all consistent with uniform motion"],
        ["কেবল বেগ ধ্রুব", "কেবল ত্বরণ শূন্য", "কেবল ভরবেগ ধ্রুব", "বেগ ধ্রুব, ত্বরণ শূন্য ও ভরবেগ ধ্রুব—সবই সত্য"],
        "D", "medium", "conceptual",
        "ΣF = 0 ⇒ a = 0 ⇒ constant velocity ⇒ constant momentum.",
        "ΣF = 0 ⇒ a = 0 ⇒ সমবেগ ⇒ ভরবেগ ধ্রুব।",
    ),
    q(
        "A person of weight W stands in a lift accelerating upward with acceleration a. Apparent weight is:",
        "W ওজনের এক ব্যক্তি লিফটে a ত্বরণে উপরে উঠলে ব্যক্তির আপাত ওজন কত হবে?",
        ["W(1 + a/g)", "W(1 − a/g)", "W(1 + g/a)", "W(1 − g/a)"],
        ["W(1 + a/g)", "W(1 − a/g)", "W(1 + g/a)", "W(1 − g/a)"],
        "A", "medium", "factual",
        "N = m(g + a) = W(1 + a/g).",
        "N = m(g + a) = W(1 + a/g)।",
    ),
    q(
        "Which fundamental force has the smallest relative strength?",
        "নিচের কোন মৌলিক বলের আপেক্ষিক মান সবচেয়ে কম?",
        ["Gravitational force", "Electromagnetic force", "Strong nuclear force", "Weak nuclear force"],
        ["মহাকর্ষ বল", "তড়িৎচৌম্বকীয় বল", "সবল নিউক্লীয় বল", "দুর্বল নিউক্লীয় বল"],
        "A", "easy", "factual",
        "Gravity is by far the weakest of the four fundamental interactions.",
        "চার মৌলিক বলের মধ্যে মহাকর্ষ সবচেয়ে দুর্বল।",
    ),
    q(
        "The exchange particle of the electromagnetic force is:",
        "নিচের কোনটি তড়িৎচৌম্বক বলের বিনিময় কণা?",
        ["Meson", "Photon", "Graviton", "Gluon"],
        ["মেসন", "ফোটন", "গ্রাভিটন", "গ্লুয়ন"],
        "B", "easy", "factual",
        "Electromagnetic interaction is mediated by the photon.",
        "তড়িৎচৌম্বকীয় মিথস্ক্রিয়ার বাহক কণা ফোটন।",
    ),
    q(
        "The exchange particle associated with the strong nuclear force is:",
        "কোন কণার বিনিময়ে সবল নিউক্লীয় বল কাজ করে?",
        ["Photon", "Graviton", "Boson (W/Z)", "Meson"],
        ["ফোটন", "গ্রাভিটন", "বোসন (W/Z)", "মেসন"],
        "D", "medium", "factual",
        "At HSC level, strong nuclear force between nucleons is described via meson exchange.",
        "HSC স্তরে নিউক্লিয়নের মধ্যে সবল বল মেসন বিনিময়ে বর্ণিত।",
    ),
    q(
        "Which force is responsible for molecular structure and chemical bonding?",
        "বস্তুর আণবিক গঠন ও রাসায়নিক বন্ধনের জন্য দায়ী কোন বল?",
        ["Gravitational force", "Electromagnetic force", "Strong nuclear force", "Weak nuclear force"],
        ["মহাকর্ষ বল", "তড়িৎচৌম্বকীয় বল", "সবল নিউক্লীয় বল", "দুর্বল নিউক্লীয় বল"],
        "B", "easy", "conceptual",
        "Chemical bonds arise from electromagnetic interactions between charged particles.",
        "রাসায়নিক বন্ধন আধানযুক্ত কণার তড়িৎচৌম্বকীয় মিথস্ক্রিয়া থেকে।",
    ),
    q(
        "A 1 N force acts on a 0.1 kg body at rest. After the force is removed, the body:",
        "০.১ kg স্থির বস্তুর উপর ১ N বল ক্রিয়া করে। বল অপসারিত হলে গতিশীল বস্তুটি:",
        ["Stops immediately", "Moves with constant velocity", "Moves with constant acceleration", "Moves with constant retardation"],
        ["থেমে যাবে", "সমবেগে চলবে", "সমত্বরণে চলবে", "সমমন্দনে চলবে"],
        "B", "medium", "conceptual",
        "With no net force after removal, Newton’s first law gives uniform velocity.",
        "বল সরালে নিট বল শূন্য; প্রথম সূত্র অনুসারে সমবেগে চলে।",
    ),
    q(
        "Newton’s first law is also known as the law of:",
        "নিউটনের প্রথম গতিসূত্রকে আর কী বলা হয়?",
        ["Law of inertia", "Law of momentum", "Law of acceleration", "Law of action–reaction"],
        ["জড়তার সূত্র", "ভরবেগের সূত্র", "ত্বরণের সূত্র", "ক্রিয়া–প্রতিক্রিয়ার সূত্র"],
        "A", "easy", "factual",
        "The first law expresses the property of inertia.",
        "প্রথম সূত্র জড়তার ধর্ম প্রকাশ করে।",
    ),
    q(
        "According to Newton’s third law, action and reaction:",
        "নিউটনের তৃতীয় সূত্র অনুসারে ক্রিয়া ও প্রতিক্রিয়া:",
        ["Act on the same body", "Are equal, opposite and act on different bodies", "Are unequal but opposite", "Cancel on the same free-body diagram always"],
        ["একই বস্তুর উপর ক্রিয়া করে", "সমান, বিপরীত ও ভিন্ন বস্তুর উপর ক্রিয়া করে", "অসমান কিন্তু বিপরীত", "সবসময় একই মুক্তবস্তু চিত্রে বাতিল হয়"],
        "B", "easy", "conceptual",
        "Action–reaction pairs are equal and opposite but act on two different bodies.",
        "ক্রিয়া–প্রতিক্রিয়া সমান ও বিপরীত, কিন্তু দুই ভিন্ন বস্তুর উপর কাজ করে।",
    ),
    q(
        "Two bodies connected by a string accelerate together. If a 15 kg body has acceleration such that the tension equals 75 N and a = 5 m s⁻² (ideal string), the force on that body from the string side is consistent with F = ma =:",
        "একসাথে ত্বরণশীল ব্যবস্থায় ১৫ kg বস্তুর উপর কার্যকর বল ৭৫ N হলে (a = 5 m s⁻²) F = ma থেকে মান:",
        ["50 N", "75 N", "125 N", "150 N"],
        ["50 N", "75 N", "125 N", "150 N"],
        "B", "medium", "numerical",
        "F = ma = 15 × 5 = 75 N.",
        "F = ma = 15 × 5 = 75 N।",
    ),
    q(
        "A rocket in the first second of launch ejects 1/80 of its mass as gas at 2400 m s⁻¹ relative speed (g = 9.8 m s⁻²). Its upward acceleration is:",
        "একটি রকেট উড্ডয়নের ১ম সেকেন্ডে এর ভরের ১/৮০ ভাগ গ্যাস ২৪০০ m s⁻¹ বেগে নির্গমন করে। রকেটটির ত্বরণ কত? (g = 9.8 m s⁻²)",
        ["49.8 m s⁻²", "40.0 m s⁻²", "20.2 m s⁻²", "4.08 m s⁻²"],
        ["49.8 m s⁻²", "40.0 m s⁻²", "20.2 m s⁻²", "4.08 m s⁻²"],
        "C", "hard", "numerical",
        "a = (Δm/m)(v_ex/Δt) − g = (1/80)×2400 − 9.8 = 30 − 9.8 = 20.2 m s⁻².",
        "a = (১/৮০)×২৪০০ − ৯.৮ = ৩০ − ৯.৮ = ২০.২ m s⁻²।",
    ),
    q(
        "According to Newtonian mechanics, for a free particle with zero net force, which quantity is not necessarily constant?",
        "নিউটনীয় বলবিদ্যা অনুসারে নিট বল শূন্য হলে কোনটি ধ্রুব নয়?",
        ["Mass", "Velocity", "Momentum", "Position"],
        ["ভর", "বেগ", "ভরবেগ", "অবস্থান"],
        "D", "medium", "conceptual",
        "Mass, velocity and momentum stay constant; position generally changes as the particle moves uniformly.",
        "ভর, বেগ ও ভরবেগ ধ্রুব; অবস্থান সাধারণত সময়ের সাথে বদলায়।",
    ),
]


# ---------------------------------------------------------------------------
# t02 Momentum and impulse / ভরবেগ ও ঘাতবল
# ---------------------------------------------------------------------------
T02 = [
    q(
        "Impulse of a force equals:",
        "বলের ঘাত সমান:",
        ["Force × displacement", "Force × time of action", "Mass × acceleration", "Power × time"],
        ["বল × সরণ", "বল × ক্রিয়াকাল", "ভর × ত্বরণ", "ক্ষমতা × সময়"],
        "B", "easy", "factual",
        "Impulse J = F Δt (for constant force).",
        "ঘাত J = F Δt (ধ্রুব বলের জন্য)।",
    ),
    q(
        "Regarding impulse: (i) impulse = force × time (ii) SI unit is N·s (iii) impulse = change in momentum. Which is correct?",
        "বলের ঘাতের ক্ষেত্রে— (i) ঘাত = বল × ক্রিয়াকাল (ii) একক N·s (iii) ঘাত = ভরবেগের পরিবর্তন। কোনটি সঠিক?",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "easy", "conceptual",
        "All three statements are standard definitions of impulse.",
        "তিনটিই ঘাতের আদর্শ সংজ্ঞা/সমতুল্য রূপ।",
    ),
    q(
        "Impulse of a force means primarily the change in:",
        "বলের ঘাত দ্বারা বোঝায়:",
        ["Torque", "Moment of inertia", "Linear momentum", "Angular momentum"],
        ["টর্ক", "জড়তার ভ্রামক", "রৈখিক ভরবেগের পরিবর্তন", "কৌণিক ভরবেগের পরিবর্তন"],
        "C", "easy", "factual",
        "J = Δp (change in linear momentum).",
        "J = Δp (রৈখিক ভরবেগের পরিবর্তন)।",
    ),
    q(
        "A 10 g ball hits a wall horizontally at 100 cm s⁻¹ and rebounds with the same speed. Impulse by the wall in dyne·s is:",
        "১০ g ভরের বল ১০০ cm s⁻¹ বেগে দেয়ালে আঘাত করে একই বেগে ফিরে যায়। দেয়াল কর্তৃক ঘাত (dyne·s):",
        ["0", "100", "1000", "2000"],
        ["0", "100", "1000", "2000"],
        "D", "hard", "numerical",
        "Δp = m(v − (−u)) = 0.01 kg × 2 × 1 m s⁻¹ = 0.02 N·s = 2000 dyne·s.",
        "Δp = 0.01 × 2 × 1 = 0.02 N·s = ২০০০ dyne·s।",
    ),
    q(
        "A 600 N force acts for 1 minute on a body. Change in momentum is:",
        "একটি বস্তুর উপর ৬০০ N বল ১ মিনিট ক্রিয়া করে। ভরবেগের পরিবর্তন:",
        ["3.6 × 10² kg m s⁻¹", "3.6 × 10⁴ kg m s⁻¹", "600 kg m s⁻¹", "10 kg m s⁻¹"],
        ["3.6 × 10² kg m s⁻¹", "3.6 × 10⁴ kg m s⁻¹", "600 kg m s⁻¹", "10 kg m s⁻¹"],
        "B", "medium", "numerical",
        "Δp = F Δt = 600 × 60 = 3.6 × 10⁴ kg m s⁻¹.",
        "Δp = 600 × 60 = 3.6 × 10⁴ kg m s⁻¹।",
    ),
    q(
        "If F(t) = (t² + t + 2) N acts from t = 1 s to t = 2 s, the impulse is about:",
        "F(t) = (t² + t + 2) N বল t = 1 s থেকে t = 2 s পর্যন্ত ক্রিয়া করলে ঘাত প্রায়:",
        ["4 N·s", "5.83 N·s", "8 N·s", "12 N·s"],
        ["4 N·s", "5.83 N·s", "8 N·s", "12 N·s"],
        "B", "hard", "numerical",
        "J = ∫₁² (t² + t + 2) dt = [t³/3 + t²/2 + 2t]₁² ≈ 5.83 N·s.",
        "J = ∫₁² (t² + t + 2) dt ≈ ৫.৮৩ N·s।",
    ),
    q(
        "A 2 N force acts for 1 s. The change in momentum is:",
        "২ N বল একটি বস্তুর উপর ১ s ক্রিয়া করলে ভরবেগের পরিবর্তন:",
        ["2 kg m s⁻¹", "4 kg m s⁻¹", "8 kg m s⁻¹", "16 kg m s⁻¹"],
        ["2 kg m s⁻¹", "4 kg m s⁻¹", "8 kg m s⁻¹", "16 kg m s⁻¹"],
        "A", "easy", "numerical",
        "Δp = F Δt = 2 × 1 = 2 kg m s⁻¹.",
        "Δp = 2 × 1 = 2 kg m s⁻¹।",
    ),
    q(
        "Which physical quantity is conserved in any collision (isolated system)?",
        "কোন ভৌত রাশিটি যেকোনো সংঘর্ষে (বিচ্ছিন্ন ব্যবস্থায়) সংরক্ষিত হয়?",
        ["Kinetic energy", "Potential energy", "Total mechanical energy only", "Total linear momentum"],
        ["গতিশক্তি", "স্থিতিশক্তি", "কেবল মোট যান্ত্রিক শক্তি", "মোট রৈখিক ভরবেগ"],
        "D", "medium", "conceptual",
        "Linear momentum is always conserved for an isolated system; KE is not (inelastic).",
        "বিচ্ছিন্ন ব্যবস্থায় রৈখিক ভরবেগ সবসময় সংরক্ষিত; গতিশক্তি নয়।",
    ),
    q(
        "A 3 kg gun fires a 50 g bullet at 150 m s⁻¹. Initial momentum of the gun–bullet system before firing is:",
        "৩ kg ভরের বন্দুক থেকে ৫০ g বুলেট ১৫০ m s⁻¹ বেগে বের হয়। গুলি ছোড়ার আগে ব্যবস্থার আদি ভরবেগ:",
        ["0.75 kg m s⁻¹", "−0.75 kg m s⁻¹", "3 kg m s⁻¹", "0 kg m s⁻¹"],
        ["0.75 kg m s⁻¹", "−0.75 kg m s⁻¹", "3 kg m s⁻¹", "0 kg m s⁻¹"],
        "D", "easy", "numerical",
        "At rest initially, total momentum = 0.",
        "আদিতে স্থির বলে মোট ভরবেগ = ০।",
    ),
    q(
        "In the previous gun problem, recoil speed of the gun is approximately:",
        "পূর্বের বন্দুক সমস্যায় বন্দুকের পশ্চাৎগতি বেগ প্রায়:",
        ["0 m s⁻¹", "0.25 m s⁻¹", "2.5 m s⁻¹", "150 m s⁻¹"],
        ["0 m s⁻¹", "0.25 m s⁻¹", "2.5 m s⁻¹", "150 m s⁻¹"],
        "C", "medium", "numerical",
        "m_g v_g = m_b v_b ⇒ v_g = (0.05 × 150)/3 = 2.5 m s⁻¹.",
        "v_g = (0.05 × 150)/3 = 2.5 m s⁻¹।",
    ),
    q(
        "SI unit of linear momentum is:",
        "রৈখিক ভরবেগের SI একক:",
        ["kg m s⁻²", "kg m s⁻¹", "N m", "N s⁻¹"],
        ["kg m s⁻²", "kg m s⁻¹", "N m", "N s⁻¹"],
        "B", "easy", "factual",
        "p = mv has unit kg m s⁻¹ (also N·s).",
        "p = mv-এর একক kg m s⁻¹ (বা N·s)।",
    ),
    q(
        "Product of force and its time of action is called:",
        "বল ও বলের ক্রিয়াকালের গুণফলকে কী বলা হয়?",
        ["Impulse", "Impact force only", "Torque", "Work"],
        ["বলের ঘাত", "কেবল আঘাত বল", "টর্ক", "কাজ"],
        "A", "easy", "factual",
        "Impulse is defined as force × time of action.",
        "ঘাত = বল × ক্রিয়াকাল।",
    ),
    q(
        "For impulsive force, which is typically true?",
        "ঘাত বলের ক্ষেত্রে সাধারণত কোনটি সঠিক?",
        ["Small force, long duration", "Large force, short duration", "Small force and short duration", "Large force and long duration"],
        ["বলের মান কম কিন্তু ক্রিয়াকাল বেশি", "বলের মান বেশি কিন্তু ক্রিয়াকাল কম", "বল ও ক্রিয়াকাল উভয় কম", "বল ও ক্রিয়াকাল উভয় বেশি"],
        "B", "easy", "conceptual",
        "Impulsive forces are large and act for a very short time.",
        "ঘাত বল বৃহৎ ও অত্যল্প সময়ে ক্রিয়া করে।",
    ),
    q(
        "A 7 kg body collides elastically with a stationary body and afterwards moves in the same direction at one-fourth of its initial speed. Mass of the stationary body is:",
        "৭ kg বস্তু স্থির বস্তুর সাথে স্থিতিস্থাপক সংঘর্ষে আদি বেগের এক-চতুর্থাংশ বেগে একই দিকে চলে। স্থির বস্তুর ভর:",
        ["2.2 kg", "4.2 kg", "8.2 kg", "14.2 kg"],
        ["2.2 kg", "4.2 kg", "8.2 kg", "14.2 kg"],
        "B", "hard", "numerical",
        "For 1D elastic: v₁ = (m₁−m₂)/(m₁+m₂) u ⇒ 1/4 = (7−m)/(7+m) ⇒ m = 4.2 kg.",
        "v₁/u = (m₁−m₂)/(m₁+m₂) = ১/৪ ⇒ m₂ = ৪.২ kg।",
    ),
    q(
        "Rate of change of linear momentum of a body equals:",
        "বস্তুর রৈখিক ভরবেগের পরিবর্তনের হার সমান:",
        ["Impulse", "Net external force", "Torque", "Kinetic energy"],
        ["ঘাত", "নিট বহিঃস্থ বল", "টর্ক", "গতিশক্তি"],
        "B", "easy", "factual",
        "Newton’s second law: F_net = dp/dt.",
        "নিউটনের দ্বিতীয় সূত্র: F_net = dp/dt।",
    ),
    q(
        "Dimensions of impulse are the same as those of:",
        "ঘাতের মাত্রা কোনটির সমান?",
        ["Force", "Momentum", "Power", "Torque"],
        ["বল", "ভরবেগ", "ক্ষমতা", "টর্ক"],
        "B", "easy", "factual",
        "Impulse and momentum share dimensions MLT⁻¹.",
        "ঘাত ও ভরবেগ উভয়ের মাত্রা MLT⁻¹।",
    ),
    q(
        "Two equal masses approach each other with equal speeds and stick together. Final velocity of the combined mass is:",
        "সমান ভরের দুই বস্তু সমান বেগে পরস্পরের দিকে এসে আটকে যায়। লব্ধি ভরের চূড়ান্ত বেগ:",
        ["Equal to initial speed", "Twice initial speed", "Zero", "Half initial speed"],
        ["আদি বেগের সমান", "আদি বেগের দ্বিগুণ", "শূন্য", "আদি বেগের অর্ধেক"],
        "C", "medium", "conceptual",
        "Momenta cancel: m v − m v = 0 ⇒ final velocity zero.",
        "ভরবেগ বাতিল: mv − mv = ০ ⇒ চূড়ান্ত বেগ শূন্য।",
    ),
    q(
        "If net external force on a system is zero, the centre of mass:",
        "কোনো ব্যবস্থায় নিট বহিঃস্থ বল শূন্য হলে ভরকেন্দ্র:",
        ["Must be at rest", "Moves with constant velocity", "Accelerates", "Oscillates"],
        ["অবশ্যই স্থির থাকে", "সমবেগে চলে", "ত্বরণ পায়", "দোলন করে"],
        "B", "medium", "conceptual",
        "a_cm = F_ext/M = 0 ⇒ v_cm is constant (may be zero).",
        "a_cm = ০ ⇒ v_cm ধ্রুব (শূন্যও হতে পারে)।",
    ),
    q(
        "A variable force delivers impulse equal to the area under the:",
        "পরিবর্তনশীল বলের ঘাত কোন গ্রাফের অধীন ক্ষেত্রফলের সমান?",
        ["F–x graph", "F–t graph", "v–t graph", "a–x graph"],
        ["F–x গ্রাফ", "F–t গ্রাফ", "v–t গ্রাফ", "a–x গ্রাফ"],
        "B", "easy", "conceptual",
        "J = ∫ F dt equals area under the force–time graph.",
        "J = ∫ F dt; F–t গ্রাফের অধীন ক্ষেত্রফল।",
    ),
    q(
        "Soft landing pads reduce injury mainly because they:",
        "নরম অবতরণ প্যাড আঘাত কমায় মূলত কারণ সেগুলো:",
        ["Increase impulse for same Δp", "Increase force for same Δp", "Increase collision time, reducing average force", "Eliminate change in momentum"],
        ["একই Δp-তে ঘাত বাড়ায়", "একই Δp-তে বল বাড়ায়", "সংঘর্ষকাল বাড়ায় বলে গড় বল কমায়", "ভরবেগের পরিবর্তন মুছে দেয়"],
        "C", "medium", "application",
        "Δp fixed ⇒ larger Δt means smaller average F = Δp/Δt.",
        "Δp স্থির; Δt বাড়লে গড় F = Δp/Δt কমে।",
    ),
]


# ---------------------------------------------------------------------------
# t03 Friction / ঘর্ষণ
# ---------------------------------------------------------------------------
T03 = [
    q(
        "Friction belongs to which class of fundamental force?",
        "ঘর্ষণ বল কোন বলের অন্তর্গত?",
        ["Gravitational", "Weak nuclear", "Electromagnetic", "Strong nuclear"],
        ["মহাকর্ষ", "দুর্বল নিউক্লীয়", "তড়িৎচৌম্বকীয়", "সবল নিউক্লীয়"],
        "C", "easy", "factual",
        "Friction arises from electromagnetic interactions between surface atoms.",
        "ঘর্ষণ পৃষ্ঠ পরমাণুর তড়িৎচৌম্বকীয় মিথস্ক্রিয়া থেকে উদ্ভূত।",
    ),
    q(
        "The angle between friction force and the velocity of a sliding body is:",
        "ঘর্ষণ বল ও বস্তুর বেগের মধ্যবর্তী কোণ হলো:",
        ["0°", "45°", "90°", "180°"],
        ["0°", "45°", "90°", "180°"],
        "D", "easy", "factual",
        "Kinetic friction opposes relative velocity: angle = 180°.",
        "গতিশীল ঘর্ষণ বেগের বিপরীত: কোণ ১৮০°।",
    ),
    q(
        "Road banking depends on:",
        "রাস্তার ব্যাংকিং নির্ভর করে:",
        ["Radius and speed only (not mass)", "Mass of the car only", "Mass and radius only", "Mass, radius and speed"],
        ["বাঁকের ব্যাসার্ধ ও বেগের উপর (ভর নয়)", "কেবল গাড়ির ভরের উপর", "কেবল ভর ও ব্যাসার্ধের উপর", "ভর, ব্যাসার্ধ ও বেগের উপর"],
        "A", "medium", "conceptual",
        "tan θ = v²/(rg); mass cancels, so banking is independent of car mass.",
        "tan θ = v²/(rg); ভর কাট যায় বলে ব্যাংকিং ভরনির্ভর নয়।",
    ),
    q(
        "Banking angle of a road does NOT depend on:",
        "রাস্তার ব্যাংকিং কোণ কীসের উপর নির্ভরশীল নয়?",
        ["Speed of the vehicle", "Mass of the vehicle", "Acceleration due to gravity", "Radius of the curve"],
        ["বস্তুর বেগ", "বস্তুর ভর", "অভিকর্ষজ ত্বরণ", "রাস্তার ব্যাসার্ধ"],
        "B", "easy", "factual",
        "From tan θ = v²/(rg), mass does not appear.",
        "tan θ = v²/(rg)-এ ভর নেই।",
    ),
    q(
        "For safe turning on a banked road of radius r and angle θ (no friction), the condition is:",
        "r ব্যাসার্ধ ও θ কোণের ব্যাংকড রাস্তায় (ঘর্ষণহীন) নিরাপদ বাঁকের শর্ত:",
        ["v = √(rg tan θ)", "v = rg tan θ", "v² < rg", "v > rg / tan θ"],
        ["v = √(rg tan θ)", "v = rg tan θ", "v² < rg", "v > rg / tan θ"],
        "A", "medium", "factual",
        "Centripetal requirement: v² = rg tan θ ⇒ v = √(rg tan θ).",
        "কেন্দ্রাভিমুখী শর্ত: v² = rg tan θ।",
    ),
    q(
        "On a flat horizontal road without banking, safe turning requires centripetal force supplied by friction f such that:",
        "ব্যাংকিংহীন অনুভূমিক রাস্তায় নিরাপদ বাঁকের জন্য কেন্দ্রাভিমুখী বল ঘর্ষণ f থেকে আসে; শর্ত:",
        ["F_c > f always", "F_c ≤ f", "F_c = 0", "f must be zero"],
        ["সবসময় F_c > f", "F_c ≤ f", "F_c = ০", "f অবশ্যই শূন্য"],
        "B", "medium", "conceptual",
        "Maximum available friction must at least provide mv²/r.",
        "প্রয়োজনীয় mv²/r সর্বোচ্চ ঘর্ষণের চেয়ে বেশি হওয়া চলবে না।",
    ),
    q(
        "A car of mass 1100 kg moves at 40 m s⁻¹ on a flat circular path of radius 400 m. Friction providing centripetal force is:",
        "১১০০ kg গাড়ি ৪০০ m ব্যাসার্ধের সমতল বৃত্তপথে ৪০ m s⁻¹-এ চললে কেন্দ্রাভিমুখী ঘর্ষণ বল:",
        ["4400 N", "440 N", "1100 N", "11 N"],
        ["4400 N", "440 N", "1100 N", "11 N"],
        "A", "medium", "numerical",
        "f = mv²/r = 1100 × 1600/400 = 4400 N.",
        "f = mv²/r = ১১০০ × ১৬০০/৪০০ = ৪৪০০ N।",
    ),
    q(
        "To give a 2 kg body acceleration 5 m s⁻² on a road with 1 N friction, required applied force is:",
        "১ N ঘর্ষণযুক্ত রাস্তায় ২ kg বস্তুতে ৫ m s⁻² ত্বরণ সৃষ্টিতে প্রয়োজনীয় বল:",
        ["8 N", "9 N", "10 N", "11 N"],
        ["8 N", "9 N", "10 N", "11 N"],
        "D", "medium", "numerical",
        "F − f = ma ⇒ F = 2×5 + 1 = 11 N.",
        "F − f = ma ⇒ F = ১০ + ১ = ১১ N।",
    ),
    q(
        "A 1000 kg car accelerates at 4 m s⁻² on a straight road with 300 N friction. Engine force is:",
        "১০০০ kg গাড়ি ৩০০ N ঘর্ষণযুক্ত সোজা রাস্তায় ৪ m s⁻² ত্বরণে চলে। ইঞ্জিনের বল:",
        ["3700 N", "4300 N", "4000 N", "10100 N"],
        ["3700 N", "4300 N", "4000 N", "10100 N"],
        "B", "medium", "numerical",
        "F − f = ma ⇒ F = 1000×4 + 300 = 4300 N.",
        "F = ৪০০০ + ৩০০ = ৪৩০০ N।",
    ),
    q(
        "Maximum static friction is:",
        "সর্বোচ্চ স্থিতি ঘর্ষণ:",
        ["μ_s N", "μ_k N only", "Independent of normal force", "Equal to weight always"],
        ["μ_s N", "কেবল μ_k N", "অভিলম্ব বল নিরপেক্ষ", "সবসময় ওজনের সমান"],
        "A", "easy", "factual",
        "f_s,max = μ_s N.",
        "f_s,max = μ_s N।",
    ),
    q(
        "Kinetic friction compared with maximum static friction is generally:",
        "সর্বোচ্চ স্থিতি ঘর্ষণের তুলনায় গতিশীল ঘর্ষণ সাধারণত:",
        ["Larger", "Smaller", "Always equal", "Infinite"],
        ["বড়", "ছোট", "সবসময় সমান", "অসীম"],
        "B", "easy", "conceptual",
        "Usually μ_k < μ_s so kinetic friction is smaller than limiting static friction.",
        "সাধারণত μ_k < μ_s বলে গতিশীল ঘর্ষণ ছোট।",
    ),
    q(
        "Safe maximum speed on a banked curve depends on:",
        "রাস্তার বাঁকে গাড়ির নিরাপদ সর্বোচ্চ বেগ নির্ভর করে:",
        ["Radius and banking angle (not mass)", "Mass only", "Mass and radius only", "Mass, radius and banking angle"],
        ["ব্যাসার্ধ ও ব্যাংকিং কোণের উপর (ভর নয়)", "কেবল ভরের উপর", "কেবল ভর ও ব্যাসার্ধের উপর", "ভর, ব্যাসার্ধ ও ব্যাংকিং কোণের উপর"],
        "A", "medium", "conceptual",
        "v_max = √(rg tan θ) (ideal); independent of vehicle mass.",
        "v_max = √(rg tan θ); গাড়ির ভরনির্ভর নয়।",
    ),
    q(
        "Two banked curves have radii 9 m and 16 m with the same banking angle. Ratio of maximum safe speeds is:",
        "একই ব্যাংকিং কোণে ৯ m ও ১৬ m ব্যাসার্ধের দুই বাঁকে সর্বোচ্চ নিরাপদ বেগের অনুপাত:",
        ["√3 : √4", "3 : 4", "9 : 16", "81 : 256"],
        ["√3 : √4", "3 : 4", "9 : 16", "81 : 256"],
        "B", "hard", "numerical",
        "v ∝ √r ⇒ v₁:v₂ = √9:√16 = 3:4.",
        "v ∝ √r ⇒ অনুপাত ৩ : ৪।",
    ),
    q(
        "Outer edge of a 5 m wide road banked at 3° is higher than the inner edge by about:",
        "৫ m প্রস্থের রাস্তায় ৩° ব্যাংকিং থাকলে বাইরের পার্শ্ব ভিতরের চেয়ে প্রায় কত উঁচু?",
        ["0.003 m", "0.011 m", "0.262 m", "0.837 m"],
        ["0.003 m", "0.011 m", "0.262 m", "0.837 m"],
        "C", "hard", "numerical",
        "h = b sin θ ≈ 5 × sin 3° ≈ 0.262 m.",
        "h = b sin θ ≈ ৫ × sin ৩° ≈ ০.২৬২ m।",
    ),
    q(
        "Friction can:",
        "ঘর্ষণ বল:",
        ["Only oppose motion always as a motive force never", "Oppose relative tendency of slipping and may allow walking/rolling", "Always increase speed", "Act only on liquids"],
        ["কেবল গতির বিরুদ্ধে; কখনো সহায়ক নয়", "আপেক্ষিক পিছলানোর প্রবণতার বিরুদ্ধে কাজ করে এবং হাঁটা/গড়াতে সহায়ক হতে পারে", "সবসময় বেগ বাড়ায়", "কেবল তরলে কাজ করে"],
        "B", "medium", "conceptual",
        "Static friction can act in the direction that prevents slipping, enabling walking and driving.",
        "স্থিতি ঘর্ষণ পিছলানো রোধ করে হাঁটা ও গাড়ি চালানো সম্ভব করে।",
    ),
    q(
        "Normal force on a body resting on a horizontal surface equals:",
        "অনুভূমিক তলে স্থির বস্তুর উপর অভিলম্ব বল সমান:",
        ["Zero", "Weight of the body", "Friction force", "μ times weight always as normal"],
        ["শূন্য", "বস্তুর ওজন", "ঘর্ষণ বল", "সবসময় μ × ওজন"],
        "B", "easy", "factual",
        "Vertical equilibrium: N = mg on a horizontal surface (no other vertical force).",
        "উল্লম্ব সাম্য: N = mg।",
    ),
    q(
        "If μ = 0 between tyres and road, a car on a flat curve:",
        "টায়ার ও রাস্তার মধ্যে μ = ০ হলে সমতল বাঁকে গাড়ি:",
        ["Turns safely at any speed", "Cannot take a curved path by friction", "Needs less banking", "Has infinite centripetal force"],
        ["যেকোনো বেগে নিরাপদে বাঁক নেয়", "ঘর্ষণ দিয়ে বক্রপথ নিতে পারে না", "কম ব্যাংকিং চায়", "অসীম কেন্দ্রাভিমুখী বল পায়"],
        "B", "medium", "application",
        "Without friction there is no centripetal force on a flat road.",
        "সমতল রাস্তায় ঘর্ষণ ছাড়া কেন্দ্রাভিমুখী বল নেই।",
    ),
    q(
        "Work done by kinetic friction on a sliding block over displacement s (friction f opposite to s) is:",
        "পিছলানো ব্লকে সরণ s-এর জন্য গতিশীল ঘর্ষণ f-এর কাজ (f, s বিপরীত):",
        ["+fs", "−fs", "0", "f/s"],
        ["+fs", "−fs", "0", "f/s"],
        "B", "medium", "numerical",
        "W = F·s = −f s when force opposes displacement.",
        "বল সরণের বিপরীত হলে W = −f s।",
    ),
    q(
        "Pulling a lawn roller with a force at an upward angle reduces friction mainly because:",
        "উর্ধ্বমুখী কোণে লন রোলার টানলে ঘর্ষণ কমে মূলত কারণ:",
        ["Normal force decreases", "Normal force increases", "μ increases", "Weight increases"],
        ["অভিলম্ব বল কমে", "অভিলম্ব বল বাড়ে", "μ বাড়ে", "ওজন বাড়ে"],
        "A", "medium", "application",
        "Upward component reduces N, so f = μN decreases.",
        "উর্ধ্ব উপাংশ N কমায়; ফলে f = μN কমে।",
    ),
    q(
        "Coefficient of friction μ is:",
        "ঘর্ষণের সহগ μ হলো:",
        ["f/N (dimensionless)", "f × N", "Equal to mass", "Measured in newton"],
        ["f/N (মাত্রাহীন)", "f × N", "ভরের সমান", "নিউটন এককে পরিমাপ্য"],
        "A", "easy", "factual",
        "μ = f/N is a dimensionless ratio.",
        "μ = f/N একটি মাত্রাহীন অনুপাত।",
    ),
]


# ---------------------------------------------------------------------------
# t04 Circular motion and centripetal force / বৃত্তীয় গতি ও কেন্দ্রাভিমুখী বল
# ---------------------------------------------------------------------------
T04 = [
    q(
        "If the force that keeps a body in circular motion is suddenly removed, the body moves:",
        "যে বলের কারণে বস্তু বৃত্তাকার পথে ঘুরে সেই বল প্রত্যাহার করলে বস্তুটি:",
        ["Along the tangent / instantaneous velocity", "Toward the centre along the radius", "Opposite to velocity", "Along a larger circle"],
        ["স্পর্শক/তাৎক্ষণিক বেগ বরাবর", "ব্যাসার্ধ বরাবর কেন্দ্রের দিকে", "বেগের বিপরীতে", "বড় বৃত্তে"],
        "A", "medium", "conceptual",
        "Inertia carries it along the instantaneous tangential direction.",
        "গতিজড়তায় তাৎক্ষণিক স্পর্শক বরাবর ছুটে যায়।",
    ),
    q(
        "A 1 kg mass on a 0.5 m string moves in a vertical circle. Difference in string tension between lowest and highest points is:",
        "১ kg ভর ০.৫ m সুতার সাহায্যে উল্লম্ব বৃত্তে ঘুরলে সর্বনিম্ন ও সর্বোচ্চ বিন্দুতে টানের পার্থক্য:",
        ["9.8 N", "19.6 N", "2 N", "0.5 N"],
        ["9.8 N", "19.6 N", "2 N", "0.5 N"],
        "B", "hard", "numerical",
        "T_bottom − T_top = 2 mg = 2 × 1 × 9.8 = 19.6 N (same speed magnitude relation).",
        "T_নিম্ন − T_উচ্চ = 2mg = ১৯.৬ N।",
    ),
    q(
        "A 0.1 kg mass tied to a 0.5 m string whirls in a horizontal circle with ω = 2 rad s⁻¹. Tension is:",
        "০.১ kg ভর ০.৫ m রশিতে বেঁধে ω = ২ rad s⁻¹-এ অনুভূমিক বৃত্তে ঘুরালে টান:",
        ["0.1 N", "0.2 N", "0.4 N", "0.8 N"],
        ["0.1 N", "0.2 N", "0.4 N", "0.8 N"],
        "B", "medium", "numerical",
        "T = mω²r = 0.1 × 4 × 0.5 = 0.2 N.",
        "T = mω²r = ০.১ × ৪ × ০.৫ = ০.২ N।",
    ),
    q(
        "1 revolution per second equals:",
        "১ rps সমান:",
        ["π rad s⁻¹", "1 rad s⁻¹", "2π rad s⁻¹", "4π rad s⁻¹"],
        ["π rad s⁻¹", "1 rad s⁻¹", "2π rad s⁻¹", "4π rad s⁻¹"],
        "C", "easy", "factual",
        "1 rev = 2π rad ⇒ 1 rps = 2π rad s⁻¹.",
        "১ আবর্তন = ২π rad ⇒ ১ rps = ২π rad s⁻¹।",
    ),
    q(
        "A car moves at 72 km h⁻¹ with centripetal acceleration 2 m s⁻². Path radius is:",
        "৭২ km h⁻¹ সমদ্রুতিতে গাড়ির কেন্দ্রমুখী ত্বরণ ২ m s⁻² হলে পথের ব্যাসার্ধ:",
        ["10 m", "144 m", "200 m", "400 m"],
        ["10 m", "144 m", "200 m", "400 m"],
        "C", "medium", "numerical",
        "v = 20 m s⁻¹; r = v²/a = 400/2 = 200 m.",
        "v = ২০ m s⁻¹; r = v²/a = ২০০ m।",
    ),
    q(
        "Centripetal force on a body of mass m, speed v, radius r is:",
        "m ভর, v বেগ, r ব্যাসার্ধে কেন্দ্রাভিমুখী বল:",
        ["mv r", "mv²/r", "m v / r²", "m r / v²"],
        ["mv r", "mv²/r", "m v / r²", "m r / v²"],
        "B", "easy", "factual",
        "F_c = mv²/r = mω²r.",
        "F_c = mv²/r = mω²r।",
    ),
    q(
        "Direction of centripetal acceleration is:",
        "কেন্দ্রাভিমুখী ত্বরণের দিক:",
        ["Along the tangent", "Away from the centre", "Toward the centre", "Vertical always"],
        ["স্পর্শক বরাবর", "কেন্দ্র থেকে দূরে", "কেন্দ্রের দিকে", "সবসময় উল্লম্ব"],
        "C", "easy", "factual",
        "Centripetal acceleration points to the centre of the circle.",
        "কেন্দ্রাভিমুখী ত্বরণ বৃত্তের কেন্দ্রের দিকে।",
    ),
    q(
        "Angular speed of Earth’s rotation about its axis is about:",
        "পৃথিবীর নিজ অক্ষের ঘূর্ণনের জন্য কৌণিক বেগ প্রায়:",
        ["7.27 × 10⁻⁵ rad s⁻¹", "7.27 × 10⁻³ rad s⁻¹", "1.818 × 10⁻² rad s⁻¹", "0.26 rad s⁻¹"],
        ["7.27 × 10⁻⁵ rad s⁻¹", "7.27 × 10⁻³ rad s⁻¹", "1.818 × 10⁻² rad s⁻¹", "0.26 rad s⁻¹"],
        "A", "medium", "numerical",
        "ω = 2π/(86400) ≈ 7.27 × 10⁻⁵ rad s⁻¹.",
        "ω = ২π/৮৬৪০০ ≈ ৭.২৭ × ১০⁻⁵ rad s⁻¹।",
    ),
    q(
        "An electric fan rotates at 90 revolutions per minute. Its angular speed is:",
        "একটি বৈদ্যুতিক পাখা প্রতি মিনিটে ৯০ বার ঘুরছে। এর কৌণিক বেগ:",
        ["π rad s⁻¹", "3π rad s⁻¹", "90π rad s⁻¹", "180π rad s⁻¹"],
        ["π rad s⁻¹", "3π rad s⁻¹", "90π rad s⁻¹", "180π rad s⁻¹"],
        "B", "medium", "numerical",
        "ω = 90 × 2π/60 = 3π rad s⁻¹.",
        "ω = ৯০ × ২π/৬০ = ৩π rad s⁻¹।",
    ),
    q(
        "A 5 kg body moves at 5 m s⁻¹ on a circle of radius 5 m. Centripetal force magnitude is:",
        "৫ kg বস্তু ৫ m ব্যাসার্ধের বৃত্তে ৫ m s⁻¹-এ ঘুরলে কেন্দ্রাভিমুখী বল:",
        ["5 N", "10 N", "25 N", "125 N"],
        ["5 N", "10 N", "25 N", "125 N"],
        "C", "easy", "numerical",
        "F = mv²/r = 5 × 25/5 = 25 N.",
        "F = ৫ × ২৫/৫ = ২৫ N।",
    ),
    q(
        "Relation between linear speed v and angular speed ω is:",
        "রৈখিক বেগ v ও কৌণিক বেগ ω-এর সম্পর্ক:",
        ["v = ω/r", "v = ω r", "v = ω² r", "v = r/ω"],
        ["v = ω/r", "v = ω r", "v = ω² r", "v = r/ω"],
        "B", "easy", "factual",
        "For circular motion, v = ω r.",
        "বৃত্তীয় গতিতে v = ω r।",
    ),
    q(
        "Uniform circular motion has:",
        "সমবৃত্তীয় গতিতে থাকে:",
        ["Constant velocity vector", "Zero acceleration", "Constant speed but changing velocity direction", "Zero net force"],
        ["ধ্রুব বেগ ভেক্টর", "শূন্য ত্বরণ", "ধ্রুব দ্রুতি কিন্তু বেগের দিক পরিবর্তনশীল", "শূন্য নিট বল"],
        "C", "easy", "conceptual",
        "Speed is constant; direction changes, so velocity and centripetal acceleration are nonzero.",
        "দ্রুতি ধ্রুব; দিক বদলায় বলে কেন্দ্রাভিমুখী ত্বরণ থাকে।",
    ),
    q(
        "Time period T and angular speed ω are related by:",
        "পর্যায়কাল T ও কৌণিক বেগ ω-এর সম্পর্ক:",
        ["ω = 2π T", "ω = 2π/T", "ω = T/(2π)", "ω = π/T"],
        ["ω = 2π T", "ω = 2π/T", "ω = T/(2π)", "ω = π/T"],
        "B", "easy", "factual",
        "One revolution in time T ⇒ ω = 2π/T.",
        "T সময়ে এক আবর্তন ⇒ ω = ২π/T।",
    ),
    q(
        "A particle in uniform circular motion has acceleration magnitude a = v²/r. If speed doubles at same r, a becomes:",
        "সমবৃত্তীয় গতিতে r অপরিবর্তিত রেখে বেগ দ্বিগুণ হলে ত্বরণ:",
        ["Half", "Double", "Four times", "Unchanged"],
        ["অর্ধেক", "দ্বিগুণ", "চারগুণ", "অপরিবর্তিত"],
        "C", "medium", "numerical",
        "a ∝ v² ⇒ doubling v multiplies a by 4.",
        "a ∝ v² ⇒ v দ্বিগুণে a চারগুণ।",
    ),
    q(
        "Minimum speed at the top of a vertical circle of radius r for a string-whirled stone (just completing circle) is:",
        "r ব্যাসার্ধের উল্লম্ব বৃত্তের শীর্ষে সুতার পাথরের ন্যূনতম বেগ (বৃত্ত পূর্ণ করতে):",
        ["√(gr)", "√(2gr)", "√(3gr)", "√(5gr)"],
        ["√(gr)", "√(2gr)", "√(3gr)", "√(5gr)"],
        "A", "medium", "factual",
        "At top, mg + T = mv²/r; for T ≥ 0, v ≥ √(gr).",
        "শীর্ষে T ≥ ০ হলে v ≥ √(gr)।",
    ),
    q(
        "Banking of roads is done to:",
        "রাস্তার ব্যাংকিং করা হয় যাতে:",
        ["Reduce necessary reliance on friction for turning", "Increase mass of vehicles", "Eliminate gravity", "Make radius infinite"],
        ["বাঁক নেওয়ায় ঘর্ষণের উপর নির্ভরতা কমে", "গাড়ির ভর বাড়ে", "অভিকর্ষ বাতিল হয়", "ব্যাসার্ধ অসীম হয়"],
        "A", "easy", "application",
        "A component of normal force supplies centripetal requirement.",
        "অভিলম্ব বলের উপাংশ কেন্দ্রাভিমুখী বল যোগায়।",
    ),
    q(
        "For motion in a horizontal circle with a conical pendulum, the vertical component of tension balances:",
        "শঙ্কু দোলকে অনুভূমিক বৃত্তগতির সময় টানের উল্লম্ব উপাংশ ভারসাম্য করে:",
        ["Centripetal force", "Weight mg", "Friction", "Torque"],
        ["কেন্দ্রাভিমুখী বল", "ওজন mg", "ঘর্ষণ", "টর্ক"],
        "B", "medium", "conceptual",
        "T cos θ = mg and T sin θ = mv²/r.",
        "T cos θ = mg; T sin θ = mv²/r।",
    ),
    q(
        "A body moving in a circle of radius r with period T has centripetal acceleration:",
        "r ব্যাসার্ধে পর্যায়কাল T-তে বৃত্তগতির কেন্দ্রাভিমুখী ত্বরণ:",
        ["4π²r/T²", "2π r/T", "T²/(4π²r)", "r T²"],
        ["4π²r/T²", "2π r/T", "T²/(4π²r)", "r T²"],
        "A", "medium", "factual",
        "ω = 2π/T; a = ω²r = 4π²r/T².",
        "a = ω²r = ৪π²r/T²।",
    ),
    q(
        "Which are examples involving centripetal force? (i) Moon orbiting Earth (ii) satellite around Earth (iii) car turning on a curved road",
        "কেন্দ্রাভিমুখী বলের উদাহরণ—(i) পৃথিবীকে কেন্দ্র করে চাঁদ (ii) পৃথিবী-প্রদক্ষিণকারী উপগ্রহ (iii) বক্রপথে গাড়ি। সঠিক:",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i ও ii", "শুধু i ও iii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "easy", "conceptual",
        "All three require a centre-directed net force.",
        "তিনটিতেই কেন্দ্রমুখী নিট বল প্রয়োজন।",
    ),
    q(
        "Dimensions of angular velocity are:",
        "কৌণিক বেগের মাত্রা:",
        ["[T⁻¹]", "[LT⁻¹]", "[T⁻²]", "[MLT⁻¹]"],
        ["[T⁻¹]", "[LT⁻¹]", "[T⁻²]", "[MLT⁻¹]"],
        "A", "easy", "factual",
        "ω = θ/t; angle is dimensionless ⇒ [ω] = T⁻¹.",
        "ω = θ/t; কোণ মাত্রাহীন ⇒ [ω] = T⁻¹।",
    ),
]


# ---------------------------------------------------------------------------
# t05 Torque and equilibrium / ঘূর্ণন বল ও সাম্যাবস্থা
# ---------------------------------------------------------------------------
T05 = [
    q(
        "The vector product of the position vector and the applied force is called:",
        "ব্যাসার্ধ ভেক্টর এবং প্রযুক্ত বলের ভেক্টর গুণনকে বলে:",
        ["Moment of inertia", "Moment of force (torque)", "Linear momentum", "Radius of gyration"],
        ["জড়তার ভ্রামক", "বলের ভ্রামক (টর্ক)", "রৈখিক ভরবেগ", "চক্রগতির ব্যাসার্ধ"],
        "B", "easy", "factual",
        "τ = r × F is the moment of force (torque).",
        "τ = r × F হলো বলের ভ্রামক/টর্ক।",
    ),
    q(
        "Rate of change of angular momentum equals:",
        "কৌণিক ভরবেগের পরিবর্তনের হার:",
        ["Force", "Moment of inertia", "Angular velocity", "Torque"],
        ["বলের সমান", "জড়তার ভ্রামকের সমান", "কৌণিক বেগের সমান", "টর্কের সমান"],
        "D", "easy", "factual",
        "τ_net = dL/dt.",
        "τ_net = dL/dt।",
    ),
    q(
        "Parallel-axis theorem for moment of inertia is:",
        "জড়তার ভ্রামক সংক্রান্ত সমান্তরাল অক্ষের উপপাদ্য:",
        ["I = I_cm + Mh²", "I = I_cm − Mh²", "I = I_cm + M²h", "I_cm = I + M²h"],
        ["I = I_cm + Mh²", "I = I_cm − Mh²", "I = I_cm + M²h", "I_cm = I + M²h"],
        "A", "easy", "factual",
        "I = I_cm + M h² for an axis parallel to one through the CM.",
        "সমান্তরাল অক্ষে I = I_cm + M h²।",
    ),
    q(
        "Dimensions of moment of inertia are:",
        "জড়তার ভ্রামকের মাত্রা কোনটি?",
        ["MLT⁻¹", "ML²", "ML²T⁻²", "MLT⁻²"],
        ["MLT⁻¹", "ML²", "ML²T⁻²", "MLT⁻²"],
        "B", "easy", "factual",
        "I = Σ mr² has dimensions ML².",
        "I = Σ mr²; মাত্রা ML²।",
    ),
    q(
        "Dimensions of torque are:",
        "টর্কের মাত্রা কোনটি?",
        ["ML²T⁻¹", "ML²T⁻²", "MLT⁻²", "MLT⁻¹"],
        ["ML²T⁻¹", "ML²T⁻²", "MLT⁻²", "MLT⁻¹"],
        "B", "easy", "factual",
        "τ = r F ⇒ [τ] = L · MLT⁻² = ML²T⁻².",
        "τ = rF ⇒ মাত্রা ML²T⁻²।",
    ),
    q(
        "A force of 100 N acts perpendicular to a rod at 10 m from axis AB. Torque about AB is:",
        "AB অক্ষ থেকে ১০ m দূরে লম্বভাবে ১০০ N বল কাজ করলে AB সাপেক্ষে টর্ক:",
        ["0", "500 N·m", "1000 N·m", "10000 N·m"],
        ["0", "500 N·m", "1000 N·m", "10000 N·m"],
        "C", "medium", "numerical",
        "τ = r F = 10 × 100 = 1000 N·m.",
        "τ = ১০ × ১০০ = ১০০০ N·m।",
    ),
    q(
        "A wheel of mass 10 kg and radius of gyration 0.5 m has moment of inertia:",
        "১০ kg ভর ও ০.৫ m চক্রগতির ব্যাসার্ধবিশিষ্ট চাকার জড়তার ভ্রামক:",
        ["0.25 kg m²", "2.5 kg m²", "25 kg m²", "50 kg m²"],
        ["0.25 kg m²", "2.5 kg m²", "25 kg m²", "50 kg m²"],
        "B", "medium", "numerical",
        "I = Mk² = 10 × (0.5)² = 2.5 kg m².",
        "I = Mk² = ১০ × ০.২৫ = ২.৫ kg m²।",
    ),
    q(
        "If that wheel (I = 2.5 kg m²) has angular acceleration 2 rad s⁻², applied torque is:",
        "ওই চাকায় (I = 2.5 kg m²) ২ rad s⁻² কৌণিক ত্বরণে প্রয়োগকৃত টর্ক:",
        ["100 N·m", "50 N·m", "5 N·m", "0.5 N·m"],
        ["100 N·m", "50 N·m", "5 N·m", "0.5 N·m"],
        "C", "medium", "numerical",
        "τ = Iα = 2.5 × 2 = 5 N·m.",
        "τ = Iα = ২.৫ × ২ = ৫ N·m।",
    ),
    q(
        "SI unit of moment of inertia is:",
        "জড়তার ভ্রামকের একক কোনটি?",
        ["kg m", "kg m⁻¹", "kg m²", "kg m⁻²"],
        ["kg m", "kg m⁻¹", "kg m²", "kg m⁻²"],
        "C", "easy", "factual",
        "I has unit kg m².",
        "I-এর একক kg m²।",
    ),
    q(
        "Unit of torque includes:",
        "টর্কের একক— (i) N·m (ii) dyne·cm (iii) ft-poundal। সঠিক:",
        ["i only", "i and ii only", "ii and iii only", "i, ii and iii"],
        ["শুধু i", "শুধু i ও ii", "শুধু ii ও iii", "i, ii ও iii"],
        "D", "easy", "factual",
        "All listed are valid torque units in different systems.",
        "তিনটিই টর্কের স্বীকৃত একক (ভিন্ন একক পদ্ধতিতে)।",
    ),
    q(
        "If net external torque on a body is zero, which remains constant?",
        "কোনো বস্তুর উপর বাহ্যিক নিট টর্ক শূন্য হলে কোনটি ধ্রুব থাকবে?",
        ["Linear velocity", "Linear momentum", "Angular momentum", "Change of momentum"],
        ["রৈখিক বেগ", "রৈখিক ভরবেগ", "কৌণিক ভরবেগ", "ভরবেগের পরিবর্তন"],
        "C", "medium", "conceptual",
        "τ_ext = 0 ⇒ L is conserved.",
        "τ_ext = ০ ⇒ কৌণিক ভরবেগ সংরক্ষিত।",
    ),
    q(
        "Torque is zero when:",
        "টর্ক শূন্য হয় যখন:",
        ["Force is maximum", "r = 0 or force is parallel to r (θ = 0° or 180°)", "θ = 90° only", "Moment of inertia is zero"],
        ["বল সর্বোচ্চ", "r = ০ অথবা বল r-এর সমান্তরাল (θ = ০° বা ১৮০°)", "কেবল θ = ৯০°", "জড়তার ভ্রামক শূন্য"],
        "B", "medium", "conceptual",
        "τ = rF sinθ = 0 if r = 0 or sinθ = 0.",
        "τ = rF sinθ; r = ০ বা sinθ = ০ হলে τ = ০।",
    ),
    q(
        "Torque is maximum when the angle between r and F is:",
        "r ও F-এর মধ্যবর্তী কোণ কত হলে টর্ক সর্বোচ্চ?",
        ["0°", "45°", "90°", "180°"],
        ["0°", "45°", "90°", "180°"],
        "C", "easy", "conceptual",
        "sinθ is maximum at 90°.",
        "sinθ সর্বোচ্চ হয় ৯০°-এ।",
    ),
    q(
        "A rotating body has I = 2 kg m². Angular speed needed for rotational KE = 100 J is:",
        "ঘূর্ণায়মান বস্তুর I = ২ kg m²। ঘূর্ণন গতিশক্তি ১০০ J-এর জন্য কৌণিক বেগ:",
        ["10 rad s⁻¹", "100 rad s⁻¹", "200 rad s⁻¹", "400 rad s⁻¹"],
        ["10 rad s⁻¹", "100 rad s⁻¹", "200 rad s⁻¹", "400 rad s⁻¹"],
        "A", "medium", "numerical",
        "K = ½ Iω² ⇒ 100 = ½ × 2 × ω² ⇒ ω = 10 rad s⁻¹.",
        "K = ½ Iω² ⇒ ω = ১০ rad s⁻¹।",
    ),
    q(
        "For rotational motion, power equals:",
        "আবর্ত/ঘূর্ণন গতির ক্ষেত্রে ক্ষমতা:",
        ["Force × time", "Torque × angular displacement", "Torque × angular velocity", "Torque × angular acceleration"],
        ["বল × সময়", "টর্ক × কৌণিক সরণ", "টর্ক × কৌণিক বেগ", "টর্ক × কৌণিক ত্বরণ"],
        "C", "medium", "factual",
        "P = τ ω for rotational dynamics.",
        "ঘূর্ণনে P = τ ω।",
    ),
    q(
        "Moment of a force about a point or axis is also called:",
        "কোনো বিন্দু বা অক্ষের সাপেক্ষে বলের ভ্রামককে কী বলে?",
        ["Radius of gyration", "Moment of inertia", "Couple only", "Torque"],
        ["চক্রগতির ব্যাসার্ধ", "জড়তার ভ্রামক", "কেবল দ্বন্দ", "টর্ক"],
        "D", "easy", "factual",
        "Moment of force about an axis is torque.",
        "অক্ষ সাপেক্ষে বলের ভ্রামকই টর্ক।",
    ),
    q(
        "Which relation is NOT correct?",
        "নিচের কোন সম্পর্কটি সঠিক নয়?",
        ["L = Iω", "τ = r × F", "τ = Iα", "L = F × p"],
        ["L = Iω", "τ = r × F", "τ = Iα", "L = F × p"],
        "D", "medium", "conceptual",
        "Angular momentum L = r × p (or Iω), not F × p.",
        "L = r × p বা Iω; L = F × p নয়।",
    ),
    q(
        "A thin circular disc’s moment of inertia about any diameter is:",
        "একটি পাতলা বৃত্তাকার চাকতির যেকোনো ব্যাসের সাপেক্ষে জড়তার ভ্রামক:",
        ["(1/4) MR²", "(1/2) MR²", "MR²", "(2/5) MR²"],
        ["(1/4) MR²", "(1/2) MR²", "MR²", "(2/5) MR²"],
        "A", "medium", "factual",
        "About a diameter, I = (1/4) MR² (perpendicular-axis theorem).",
        "ব্যাস সাপেক্ষে I = (১/৪) MR²।",
    ),
    q(
        "For static equilibrium of a rigid body:",
        "দৃঢ় বস্তুর স্থিতি সাম্যাবস্থার জন্য:",
        ["Only ΣF = 0", "Only Στ = 0", "ΣF = 0 and Στ = 0", "ΣF ≠ 0 but Στ = 0"],
        ["কেবল ΣF = ০", "কেবল Στ = ০", "ΣF = ০ এবং Στ = ০", "ΣF ≠ ০ কিন্তু Στ = ০"],
        "C", "easy", "conceptual",
        "Both net force and net torque must vanish.",
        "নিট বল ও নিট টর্ক উভয়ই শূন্য হতে হবে।",
    ),
    q(
        "Solid cylinder mass 0.5 kg has I = 0.25 kg m² about its axis. Radius is:",
        "০.৫ kg নিরেট সিলিন্ডারের অক্ষ সাপেক্ষে I = ০.২৫ kg m² হলে ব্যাসার্ধ:",
        ["7.07 m", "5 m", "1 m", "0.5 m"],
        ["7.07 m", "5 m", "1 m", "0.5 m"],
        "C", "hard", "numerical",
        "I = (1/2)MR² ⇒ 0.25 = 0.5 × 0.5 × R² ⇒ R² = 1 ⇒ R = 1 m.",
        "I = ½ MR² ⇒ R = ১ m।",
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
    write_topic("phy1_27_ch04_t01", T01)
    write_topic("phy1_27_ch04_t02", T02)
    write_topic("phy1_27_ch04_t03", T03)
    write_topic("phy1_27_ch04_t04", T04)
    write_topic("phy1_27_ch04_t05", T05)

    summary = {
        "paper": "physics_1",
        "chapter": 4,
        "title_en": "Newtonian Mechanics",
        "title_bn": "নিউটনীয় বলবিদ্যা",
        "per_topic": 20,
        "topics": {
            "phy1_27_ch04_t01": 20,
            "phy1_27_ch04_t02": 20,
            "phy1_27_ch04_t03": 20,
            "phy1_27_ch04_t04": 20,
            "phy1_27_ch04_t05": 20,
        },
        "source": SOURCE,
        "verified": False,
        "mcq_printed_pages": [127, 138],
        "notes": (
            "OCR-noisy pages 127–138 reconstructed as HSC-accurate bilingual MCQs; "
            "figure-only items rewritten in text; rocket/lift/banking/impulse/torque "
            "board staples preserved with corrected arithmetic where OCR garbled numbers."
        ),
    }
    out = (
        ROOT
        / "content"
        / "bank"
        / "udvash_raw"
        / "physics_1"
        / "parsed"
        / "ch04_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("summary", out)


if __name__ == "__main__":
    main()
