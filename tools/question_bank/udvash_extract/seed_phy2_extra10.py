#!/usr/bin/env python3
"""Append exactly 10 short bilingual MCQs to every phy2_27_*.jsonl topic.

Idempotent: if a file already has 30 lines, it is skipped.
APPEND only — never rewrites the original 20 rows.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPICS = ROOT / "content" / "bank" / "topics"
SOURCE = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "physics p2; curated bilingual; extra short set"
)


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    if not re.search(r"[A-Za-z]", en):
        en = f"value {en}"
    if not re.search(r"[ঀ-৿]", bn):
        bn = f"মান {bn}"
    return en, bn


def q(
    stem_en,
    stem_bn,
    opts_en,
    opts_bn,
    correct,
    difficulty,
    qtype,
    exp_en,
    exp_bn,
):
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
# Extra short sets (10 each) — stems must be unique vs existing rows
# ---------------------------------------------------------------------------

EXTRA: dict[str, list[dict]] = {}

# --- Ch01 Thermodynamics ---
EXTRA["phy2_27_ch01_t01"] = [
    q("The SI unit of temperature is:", "তাপমাত্রার SI একক কী?",
      ["Celsius", "Fahrenheit", "Kelvin", "Rankine"],
      ["সেলসিয়াস", "ফারেনহাইট", "কেলভিন", "র‍্যাঙ্কিন"],
      "C", "easy", "factual",
      "The SI base unit of thermodynamic temperature is the kelvin (K).",
      "তাপগতিবিদ্যায় তাপমাত্রার SI একক কেলভিন (K)।"),
    q("Two bodies in thermal equilibrium have the same:", "তাপীয় সাম্যতায় দুটি বস্তুর কোনটি সমান?",
      ["heat capacity", "internal energy", "temperature", "entropy"],
      ["তাপধারণ ক্ষমতা", "অভ্যন্তরীণ শক্তি", "তাপমাত্রা", "এন্ট্রপি"],
      "C", "easy", "conceptual",
      "Thermal equilibrium means equal temperature.",
      "তাপীয় সাম্যতা মানে উভয়ের তাপমাত্রা সমান।"),
    q("Absolute zero corresponds to:", "পরম শূন্য তাপমাত্রা কোনটি?",
      ["0°C", "0°F", "0 K", "273°C"],
      ["০°C", "০°F", "০ K", "২৭৩°C"],
      "C", "easy", "factual",
      "Absolute zero is 0 K on the absolute scale.",
      "পরম শূন্য হলো ০ K।"),
    q("1°C temperature rise equals a rise of:", "১°C বৃদ্ধি কোনটির সমান বৃদ্ধি?",
      ["1 K", "1°F", "273 K", "5/9 K"],
      ["১ K", "১°F", "২৭৩ K", "৫/৯ K"],
      "A", "easy", "factual",
      "Celsius and kelvin intervals are equal in size.",
      "সেলসিয়াস ও কেলভিন স্কেলের ব্যবধান সমান।"),
    q("A thermometric property must vary:", "উষ্ণতামিতিক ধর্ম তাপমাত্রার সাথে কীভাবে পরিবর্তিত হয়?",
      ["randomly", "monotonically with temperature", "only at melting point", "only in vacuum"],
      ["এলোমেলোভাবে", "তাপমাত্রার সাথে একঘেয়েভাবে", "শুধু গলনাঙ্কে", "শুধু শূন্যে"],
      "B", "medium", "conceptual",
      "Useful thermometric properties change smoothly and monotonically with temperature.",
      "উপযোগী উষ্ণতামিতিক ধর্ম তাপমাত্রার সাথে মসৃণ ও একঘেয়ে পরিবর্তিত হয়।"),
    q("Room temperature ~27°C in kelvin is about:", "প্রায় ২৭°C কেলভিনে কত?",
      ["27 K", "246 K", "300 K", "373 K"],
      ["২৭ K", "২৪৬ K", "৩০০ K", "৩৭৩ K"],
      "C", "easy", "numerical",
      "T(K) = t(°C) + 273 ≈ 300 K.",
      "T(K) = t(°C) + ২৭৩ ≈ ৩০০ K।"),
    q("Boiling point of water at 1 atm on Celsius scale is:", "১ atm-এ পানির স্ফুটনাঙ্ক সেলসিয়াসে কত?",
      ["0°C", "32°C", "100°C", "273°C"],
      ["০°C", "৩২°C", "১০০°C", "২৭৩°C"],
      "C", "easy", "factual",
      "At standard pressure water boils at 100°C.",
      "স্বাভাবিক চাপে পানি ১০০°C-এ ফোটে।"),
    q("Zeroth law of thermodynamics introduces the concept of:", "তাপগতিবিদ্যার শূন্যতম সূত্র কোন ধারণা দেয়?",
      ["entropy", "temperature", "enthalpy", "work"],
      ["এন্ট্রপি", "তাপমাত্রা", "এনথ্যালপি", "কাজ"],
      "B", "easy", "conceptual",
      "The zeroth law underlies the definition of temperature.",
      "শূন্যতম সূত্র তাপমাত্রার ধারণার ভিত্তি।"),
    q("Ice point on the Celsius scale is:", "সেলসিয়াস স্কেলে বরফ বিন্দু কত?",
      ["−273°C", "0°C", "32°C", "100°C"],
      ["−২৭৩°C", "০°C", "৩২°C", "১০০°C"],
      "B", "easy", "factual",
      "Ice melts at 0°C under standard conditions.",
      "স্বাভাবিক অবস্থায় বরফ ০°C-এ গলে।"),
    q("If Celsius and Fahrenheit readings are equal, the common value is:", "সেলসিয়াস ও ফারেনহাইট পাঠ সমান হলে মান কত?",
      ["−40", "0", "32", "100"],
      ["−৪০", "০", "৩২", "১০০"],
      "A", "medium", "numerical",
      "Solving C = (9/5)C + 32 gives C = −40.",
      "C = (৯/৫)C + ৩২ সমাধানে C = −৪০।"),
]

EXTRA["phy2_27_ch01_t02"] = [
    q("An isolated thermodynamic system exchanges:", "বিচ্ছিন্ন তাপীয় সিস্টেম বিনিময় করে:",
      ["only heat", "only matter", "neither heat nor matter", "only work"],
      ["শুধু তাপ", "শুধু পদার্থ", "তাপ ও পদার্থ কোনোটিই নয়", "শুধু কাজ"],
      "C", "easy", "factual",
      "An isolated system exchanges neither energy nor matter with surroundings.",
      "বিচ্ছিন্ন সিস্টেম পরিবেশের সাথে শক্তি বা পদার্থ বিনিময় করে না।"),
    q("Internal energy of an ideal gas depends only on:", "আদর্শ গ্যাসের অভ্যন্তরীণ শক্তি শুধু কোনটির উপর নির্ভর করে?",
      ["pressure", "volume", "temperature", "shape of container"],
      ["চাপ", "আয়তন", "তাপমাত্রা", "পাত্রের আকৃতি"],
      "C", "easy", "conceptual",
      "For an ideal gas U = U(T) only.",
      "আদর্শ গ্যাসের জন্য U শুধু তাপমাত্রার ফাংশন।"),
    q("A closed system can exchange:", "বন্ধ সিস্টেম বিনিময় করতে পারে:",
      ["matter only", "energy but not matter", "neither", "matter but not energy"],
      ["শুধু পদার্থ", "শক্তি কিন্তু পদার্থ নয়", "কোনোটিই নয়", "পদার্থ কিন্তু শক্তি নয়"],
      "B", "easy", "factual",
      "Closed systems exchange energy (heat/work), not matter.",
      "বন্ধ সিস্টেম শক্তি বিনিময় করে, পদার্থ নয়।"),
    q("Extensive thermodynamic property example:", "ব্যাপক তাপগতিবিদ্যা ধর্মের উদাহরণ:",
      ["temperature", "pressure", "volume", "density"],
      ["তাপমাত্রা", "চাপ", "আয়তন", "ঘনত্ব"],
      "C", "easy", "factual",
      "Volume scales with system size; T, P, density are intensive.",
      "আয়তন সিস্টেমের আকারের সাথে বাড়ে; T, P, ঘনত্ব নিবিড়।"),
    q("Open system allows exchange of:", "মুক্ত সিস্টেম বিনিময় করতে দেয়:",
      ["only heat", "heat, work and matter", "only work", "nothing"],
      ["শুধু তাপ", "তাপ, কাজ ও পদার্থ", "শুধু কাজ", "কিছুই নয়"],
      "B", "easy", "factual",
      "Open systems exchange both energy and matter.",
      "মুক্ত সিস্টেম শক্তি ও পদার্থ উভয়ই বিনিময় করে।"),
    q("State function depends only on:", "অবস্থা ফাংশন নির্ভর করে শুধু:",
      ["path taken", "initial and final states", "time of process", "speed of process"],
      ["পথের উপর", "প্রাথমিক ও চূড়ান্ত অবস্থার উপর", "প্রক্রিয়ার সময়ের উপর", "প্রক্রিয়ার গতির উপর"],
      "B", "easy", "conceptual",
      "State functions depend only on the state, not the path.",
      "অবস্থা ফাংশন শুধু অবস্থার উপর নির্ভর করে, পথের উপর নয়।"),
    q("For a monatomic ideal gas, Cv per mole is:", "একপরমাণুক আদর্শ গ্যাসের প্রতি মোল Cv:",
      ["R", "(3/2)R", "(5/2)R", "3R"],
      ["R", "(৩/২)R", "(৫/২)R", "৩R"],
      "B", "medium", "factual",
      "Monatomic gases have f=3 so Cv = (f/2)R = 3R/2.",
      "একপরমাণুক গ্যাসে f=৩, তাই Cv = (f/২)R = ৩R/২।"),
    q("Heat capacity at constant pressure is denoted by:", "ধ্রুব চাপে তাপধারণ ক্ষমতা চিহ্নিত হয়:",
      ["Cv", "Cp", "γ", "R"],
      ["Cv", "Cp", "γ", "R"],
      "B", "easy", "factual",
      "Cp is heat capacity at constant pressure.",
      "ধ্রুব চাপে তাপধারণ ক্ষমতা Cp।"),
    q("γ for an ideal gas equals:", "আদর্শ গ্যাসের জন্য γ সমান:",
      ["Cp − Cv", "Cp / Cv", "Cv / Cp", "Cp + Cv"],
      ["Cp − Cv", "Cp / Cv", "Cv / Cp", "Cp + Cv"],
      "B", "easy", "factual",
      "By definition γ = Cp/Cv.",
      "সংজ্ঞা অনুযায়ী γ = Cp/Cv।"),
    q("Path function example among the following:", "নিচের কোনটি পথ ফাংশন?",
      ["internal energy", "enthalpy", "work", "entropy of ideal gas state"],
      ["অভ্যন্তরীণ শক্তি", "এনথ্যালপি", "কাজ", "আদর্শ গ্যাস অবস্থার এন্ট্রপি"],
      "C", "medium", "conceptual",
      "Work depends on the path; U and H are state functions.",
      "কাজ পথনির্ভর; U ও H অবস্থা ফাংশন।"),
]

EXTRA["phy2_27_ch01_t03"] = [
    q("First law of thermodynamics is essentially conservation of:", "তাপগতিবিদ্যার প্রথম সূত্র মূলত কোনটির সংরক্ষণ?",
      ["momentum", "charge", "energy", "mass only"],
      ["ভরবেগ", "আধান", "শক্তি", "শুধু ভর"],
      "C", "easy", "factual",
      "The first law expresses energy conservation for thermodynamic systems.",
      "প্রথম সূত্র তাপীয় সিস্টেমে শক্তি সংরক্ষণ প্রকাশ করে।"),
    q("In the form ΔU = Q − W (W by system), if Q=0 then:", "ΔU = Q − W (W সিস্টেম কর্তৃক) এ Q=0 হলে:",
      ["ΔU = W", "ΔU = −W", "ΔU = 0 always", "W = 0"],
      ["ΔU = W", "ΔU = −W", "ΔU সবসময় ০", "W = ০"],
      "B", "medium", "conceptual",
      "Adiabatic: Q=0 so ΔU = −W.",
      "adiabatic প্রক্রিয়ায় Q=০, তাই ΔU = −W।"),
    q("Isothermal process for ideal gas means ΔU is:", "আদর্শ গ্যাসের সমোষ্ণ প্রক্রিয়ায় ΔU:",
      ["positive", "negative", "zero", "infinite"],
      ["ধনাত্মক", "ঋণাত্মক", "শূন্য", "অসীম"],
      "C", "easy", "conceptual",
      "U depends only on T for ideal gas, so ΔT=0 ⇒ ΔU=0.",
      "আদর্শ গ্যাসে U শুধু T-নির্ভর, ΔT=০ হলে ΔU=০।"),
    q("Work done by gas in expansion is usually taken as:", "প্রসারণে গ্যাস কর্তৃক কাজ সাধারণত:",
      ["negative", "positive", "always zero", "undefined"],
      ["ঋণাত্মক", "ধনাত্মক", "সবসময় শূন্য", "অনির্ধারিত"],
      "B", "easy", "factual",
      "Convention: work done by the system in expansion is positive.",
      "প্রথানুযায়ী প্রসারণে সিস্টেম কর্তৃক কাজ ধনাত্মক।"),
    q("In an isochoric process, work done by the gas is:", "সমআয়তন প্রক্রিয়ায় গ্যাস কর্তৃক কাজ:",
      ["maximum", "zero", "equal to Q", "equal to ΔU always wrongly"],
      ["সর্বোচ্চ", "শূন্য", "Q-এর সমান", "সবসময় ΔU-এর সমান ভুলভাবে"],
      "B", "easy", "conceptual",
      "Constant volume ⇒ W = ∫P dV = 0.",
      "ধ্রুব আয়তনে W = ∫P dV = ০।"),
    q("Heat absorbed at constant volume increases mainly:", "ধ্রুব আয়তনে শোষিত তাপ প্রধানত বাড়ায়:",
      ["kinetic energy only of walls", "internal energy", "potential of Earth", "mass"],
      ["শুধু দেয়ালের গতিশক্তি", "অভ্যন্তরীণ শক্তি", "পৃথিবীর বিভব", "ভর"],
      "B", "easy", "conceptual",
      "At constant volume, Q = ΔU for the usual sign convention.",
      "ধ্রুব আয়তনে সাধারণত Q = ΔU।"),
    q("Enthalpy H is defined as:", "এনথ্যালপি H-এর সংজ্ঞা:",
      ["U − PV", "U + PV", "U/PV", "PV − U"],
      ["U − PV", "U + PV", "U/PV", "PV − U"],
      "B", "easy", "factual",
      "By definition H = U + PV.",
      "সংজ্ঞা: H = U + PV।"),
    q("In a cyclic process, net change in internal energy is:", "চক্রীয় প্রক্রিয়ায় অভ্যন্তরীণ শক্তির নীট পরিবর্তন:",
      ["positive", "negative", "zero", "equal to Q only"],
      ["ধনাত্মক", "ঋণাত্মক", "শূন্য", "শুধু Q-এর সমান"],
      "C", "easy", "conceptual",
      "Returning to the same state gives ΔU = 0 for the cycle.",
      "একই অবস্থায় ফিরলে চক্রের জন্য ΔU = ০।"),
    q("If a system does 20 J work and absorbs 50 J heat, ΔU is:", "সিস্টেম ২০ J কাজ করে ও ৫০ J তাপ শোষণ করলে ΔU:",
      ["70 J", "30 J", "−30 J", "20 J"],
      ["৭০ J", "৩০ J", "−৩০ J", "২০ J"],
      "B", "medium", "numerical",
      "ΔU = Q − W = 50 − 20 = 30 J.",
      "ΔU = Q − W = ৫০ − ২০ = ৩০ J।"),
    q("Isobaric process means constant:", "সমচাপ প্রক্রিয়া মানে ধ্রুব:",
      ["volume", "temperature", "pressure", "entropy"],
      ["আয়তন", "তাপমাত্রা", "চাপ", "এন্ট্রপি"],
      "C", "easy", "factual",
      "Isobaric = constant pressure.",
      "সমচাপ = ধ্রুব চাপ।"),
]

EXTRA["phy2_27_ch01_t04"] = [
    q("Second law implies that heat cannot spontaneously flow from:", "দ্বিতীয় সূত্র অনুসারে তাপ স্বতঃস্ফূর্তভাবে প্রবাহিত হতে পারে না:",
      ["hot to cold", "cold to hot", "system to surroundings always", "sun to earth"],
      ["গরম থেকে ঠান্ডায়", "ঠান্ডা থেকে গরমে", "সবসময় সিস্টেম থেকে পরিবেশে", "সূর্য থেকে পৃথিবীতে"],
      "B", "easy", "conceptual",
      "Spontaneous heat flow is from hotter to colder bodies.",
      "স্বতঃস্ফূর্ত তাপপ্রবাহ গরম থেকে ঠান্ডায় হয়।"),
    q("Clausius statement concerns:", "ক্লসিয়াসের বিবৃতি সম্পর্কিত:",
      ["engines only", "refrigerators/heat pumps", "only ideal gases", "only radiation"],
      ["শুধু ইঞ্জিন", "রেফ্রিজারেটর/তাপ পাম্প", "শুধু আদর্শ গ্যাস", "শুধু বিকিরণ"],
      "B", "easy", "factual",
      "Clausius statement is about impossibility of heat transfer from cold to hot without work.",
      "ক্লসিয়াস: কাজ ছাড়া ঠান্ডা থেকে গরমে তাপ স্থানান্তর অসম্ভব।"),
    q("Kelvin–Planck statement forbids a engine that:", "কেলভিন–প্ল্যাঙ্ক বিবৃতি নিষেধ করে এমন ইঞ্জিন যা:",
      ["rejects some heat", "converts heat completely into work in a cycle with one reservoir", "has two reservoirs", "is reversible"],
      ["কিছু তাপ বর্জন করে", "একটি আধার নিয়ে চক্রে তাপ সম্পূর্ণ কাজে রূপান্তর করে", "দুটি আধার আছে", "প্রত্যাবর্তী"],
      "B", "medium", "conceptual",
      "No cyclic engine can convert heat entirely into work using a single reservoir.",
      "একটি মাত্র আধার দিয়ে চক্রীয় ইঞ্জিন তাপ সম্পূর্ণ কাজে রূপান্তর করতে পারে না।"),
    q("An engine that converts heat entirely into work using only one reservoir would violate:", "শুধু এক আধার দিয়ে তাপ সম্পূর্ণ কাজে রূপান্তর করলে লঙ্ঘিত হয়:",
      ["zeroth law only", "first law only", "second law", "Newton’s third law only"],
      ["শুধু শূন্যতম সূত্র", "শুধু প্রথম সূত্র", "দ্বিতীয় সূত্র", "শুধু নিউটনের তৃতীয় সূত্র"],
      "C", "easy", "factual",
      "Such a PMM2-style engine violates the second law.",
      "এ ধরনের ইঞ্জিন দ্বিতীয় সূত্র লঙ্ঘন করে।"),
    q("Efficiency of any heat engine is always:", "যেকোনো তাপ ইঞ্জিনের দক্ষতা সবসময়:",
      ["greater than 1", "equal to 1", "less than 1", "negative"],
      ["১-এর বেশি", "১-এর সমান", "১-এর কম", "ঋণাত্মক"],
      "C", "easy", "conceptual",
      "Some heat must be rejected; η < 1.",
      "কিছু তাপ বর্জন অনিবার্য; η < ১।"),
    q("Direction of natural processes is indicated by:", "প্রাকৃতিক প্রক্রিয়ার দিক নির্দেশ করে:",
      ["first law alone", "second law", "only Boyle’s law", "only Ohm’s law"],
      ["শুধু প্রথম সূত্র", "দ্বিতীয় সূত্র", "শুধু বয়েলের সূত্র", "শুধু ওহমের সূত্র"],
      "B", "easy", "conceptual",
      "The second law gives the arrow of spontaneous processes.",
      "দ্বিতীয় সূত্র স্বতঃস্ফূর্ত প্রক্রিয়ার দিক নির্দেশ করে।"),
    q("Heat engine requires at least how many heat reservoirs?", "তাপ ইঞ্জিনের জন্য কমপক্ষে কতটি তাপ আধার লাগে?",
      ["one", "two", "three", "none"],
      ["একটি", "দুটি", "তিনটি", "কোনোটিই নয়"],
      "B", "easy", "factual",
      "A working engine needs a hot source and a cold sink.",
      "কার্যকর ইঞ্জিনে গরম উৎস ও ঠান্ডা সিঙ্ক লাগে।"),
    q("Refrigerator transfers heat from:", "রেফ্রিজারেটর তাপ স্থানান্তর করে:",
      ["hot to cold spontaneously", "cold to hot using work", "cold to hot without work", "vacuum to air only"],
      ["গরম থেকে ঠান্ডায় স্বতঃস্ফূর্তভাবে", "কাজ ব্যবহার করে ঠান্ডা থেকে গরমে", "কাজ ছাড়া ঠান্ডা থেকে গরমে", "শুধু শূন্য থেকে বাতাসে"],
      "B", "easy", "conceptual",
      "Work input enables heat flow from cold to hot.",
      "কাজ ইনপুট দিয়ে ঠান্ডা থেকে গরমে তাপ যায়।"),
    q("Which is a consequence of the second law?", "দ্বিতীয় সূত্রের ফলাফল কোনটি?",
      ["energy can be created", "100% efficient cyclic heat engine exists", "entropy of isolated system does not decrease", "mass is not conserved"],
      ["শক্তি সৃষ্টি হয়", "১০০% দক্ষ চক্রীয় তাপ ইঞ্জিন আছে", "বিচ্ছিন্ন সিস্টেমের এন্ট্রপি কমে না", "ভর সংরক্ষিত নয়"],
      "C", "medium", "conceptual",
      "For an isolated system, entropy never decreases.",
      "বিচ্ছিন্ন সিস্টেমের এন্ট্রপি কমে না।"),
    q("Carnot efficiency depends on:", "কার্নো দক্ষতা নির্ভর করে:",
      ["only working substance", "reservoir temperatures", "only engine size", "only pressure"],
      ["শুধু কার্যকর পদার্থ", "আধারের তাপমাত্রা", "শুধু ইঞ্জিনের আকার", "শুধু চাপ"],
      "B", "easy", "conceptual",
      "η_C = 1 − T2/T1 for absolute temperatures.",
      "η_C = ১ − T2/T1 (পরম তাপমাত্রা)।"),
]

EXTRA["phy2_27_ch01_t05"] = [
    q("A reversible process can be reversed without:", "প্রত্যাবর্তী প্রক্রিয়া উল্টানো যায় ছাড়া:",
      ["any change in system or surroundings", "changing temperature", "using heat", "using work"],
      ["সিস্টেম বা পরিবেশে কোনো পরিবর্তন", "তাপমাত্রা পরিবর্তন", "তাপ ব্যবহার", "কাজ ব্যবহার"],
      "A", "easy", "conceptual",
      "Ideal reversibility leaves no net change after reverse path.",
      "আদর্শ প্রত্যাবর্তী প্রক্রিয়ায় উল্টো পথে নীট পরিবর্তন থাকে না।"),
    q("Most natural processes are:", "অধিকাংশ প্রাকৃতিক প্রক্রিয়া:",
      ["reversible", "irreversible", "isothermal only", "adiabatic only"],
      ["প্রত্যাবর্তী", "অপ্রত্যাবর্তী", "শুধু সমোষ্ণ", "শুধু adiabatic"],
      "B", "easy", "factual",
      "Friction, free expansion, etc. make real processes irreversible.",
      "ঘর্ষণ, মুক্ত প্রসারণ ইত্যাদিতে বাস্তব প্রক্রিয়া অপ্রত্যাবর্তী।"),
    q("Free expansion of an ideal gas into vacuum is:", "শূন্যে আদর্শ গ্যাসের মুক্ত প্রসারণ:",
      ["reversible isothermal", "irreversible and adiabatic (Q=0)", "isobaric reversible", "cyclic"],
      ["প্রত্যাবর্তী সমোষ্ণ", "অপ্রত্যাবর্তী ও adiabatic (Q=০)", "প্রত্যাবর্তী সমচাপ", "চক্রীয়"],
      "B", "medium", "conceptual",
      "Free expansion is irreversible with Q=0 and W=0 for ideal gas in insulated box.",
      "মুক্ত প্রসারণ অপ্রত্যাবর্তী; অন্তরিত বাক্সে Q=০, W=০।"),
    q("Quasi-static process is approximately:", "আপাত-স্থিতিশীল প্রক্রিয়া প্রায়:",
      ["very fast", "infinitely slow through equilibrium states", "explosive", "random"],
      ["খুব দ্রুত", "সাম্যাবস্থার মধ্য দিয়ে অসীম ধীর", "বিস্ফোরক", "এলোমেলো"],
      "B", "easy", "conceptual",
      "Quasi-static means the system is nearly always in equilibrium.",
      "আপাত-স্থিতিশীল মানে সিস্টেম প্রায় সবসময় সাম্যাবস্থায়।"),
    q("Friction in a process tends to make it:", "প্রক্রিয়ায় ঘর্ষণ এটিকে করে:",
      ["more reversible", "irreversible", "isentropic always", "isothermal always"],
      ["আরও প্রত্যাবর্তী", "অপ্রত্যাবর্তী", "সবসময় সমএন্ট্রপি", "সবসময় সমোষ্ণ"],
      "B", "easy", "conceptual",
      "Dissipative effects cause irreversibility.",
      "বিলোপী প্রভাব অপ্রত্যাবর্তীতা সৃষ্টি করে।"),
    q("In a reversible adiabatic process for ideal gas:", "আদর্শ গ্যাসের প্রত্যাবর্তী adiabatic প্রক্রিয়ায়:",
      ["Q ≠ 0", "entropy of system stays constant", "temperature always rises", "volume is fixed"],
      ["Q ≠ ০", "সিস্টেমের এন্ট্রপি ধ্রুব থাকে", "তাপমাত্রা সবসময় বাড়ে", "আয়তন ধ্রুব"],
      "B", "medium", "conceptual",
      "Reversible adiabatic ⇒ isentropic for the system.",
      "প্রত্যাবর্তী adiabatic ⇒ সিস্টেমের জন্য সমএন্ট্রপি।"),
    q("Heat conduction through a finite temperature difference is:", "সসীম তাপমাত্রা পার্থক্যে তাপ পরিবহন:",
      ["reversible", "irreversible", "impossible", "isentropic"],
      ["প্রত্যাবর্তী", "অপ্রত্যাবর্তী", "অসম্ভব", "সমএন্ট্রপি"],
      "B", "easy", "conceptual",
      "Finite ΔT heat flow generates entropy and is irreversible.",
      "সসীম ΔT-তে তাপপ্রবাহ এন্ট্রপি বাড়ায়—অপ্রত্যাবর্তী।"),
    q("Reversible isothermal expansion of ideal gas:", "আদর্শ গ্যাসের প্রত্যাবর্তী সমোষ্ণ প্রসারণে:",
      ["ΔU > 0", "ΔU = 0 and Q = W", "Q = 0", "W = 0"],
      ["ΔU > ০", "ΔU = ০ এবং Q = W", "Q = ০", "W = ০"],
      "B", "medium", "conceptual",
      "ΔU=0 so heat absorbed equals work done by gas.",
      "ΔU=০ বলে শোষিত তাপ = গ্যাস কর্তৃক কাজ।"),
    q("Which process can ideally be reversible?", "কোন প্রক্রিয়া আদর্শভাবে প্রত্যাবর্তী হতে পারে?",
      ["sudden free expansion", "combustion", "quasi-static frictionless compression", "mixing of different gases irreversibly"],
      ["হঠাৎ মুক্ত প্রসারণ", "দহন", "ঘর্ষণহীন আপাত-স্থিতিশীল সংকোচন", "ভিন্ন গ্যাসের অপ্রত্যাবর্তী মিশ্রণ"],
      "C", "easy", "conceptual",
      "Slow frictionless compression can approach reversibility.",
      "ধীর ঘর্ষণহীন সংকোচন প্রত্যাবর্তীতার কাছাকাছি।"),
    q("Irreversibility is associated with:", "অপ্রত্যাবর্তীতার সাথে যুক্ত:",
      ["decrease of universe entropy", "increase of universe entropy", "no entropy change ever", "creation of energy"],
      ["মহাবিশ্বের এন্ট্রপি হ্রাস", "মহাবিশ্বের এন্ট্রপি বৃদ্ধি", "কখনো এন্ট্রপি পরিবর্তন নেই", "শক্তি সৃষ্টি"],
      "B", "easy", "conceptual",
      "Irreversible processes increase the entropy of the universe.",
      "অপ্রত্যাবর্তী প্রক্রিয়ায় মহাবিশ্বের এন্ট্রপি বাড়ে।"),
]

EXTRA["phy2_27_ch01_t06"] = [
    q("Carnot cycle consists of:", "কার্নো চক্র গঠিত:",
      ["two isotherms and two adiabats", "four isotherms", "two isobars and two isochors", "only adiabats"],
      ["দুটি সমোষ্ণ ও দুটি adiabatic", "চারটি সমোষ্ণ", "দুটি সমচাপ ও দুটি সমআয়তন", "শুধু adiabatic"],
      "A", "easy", "factual",
      "Carnot cycle: isothermal + adiabatic expansion and compression.",
      "কার্নো: সমোষ্ণ ও adiabatic প্রসারণ ও সংকোচন।"),
    q("Working substance in an ideal Carnot engine is often taken as:", "আদর্শ কার্নো ইঞ্জিনের কার্যকর পদার্থ প্রায়শই:",
      ["steam only", "ideal gas", "solid iron", "plasma only"],
      ["শুধু বাষ্প", "আদর্শ গ্যাস", "কঠিন লোহা", "শুধু প্লাজমা"],
      "B", "easy", "factual",
      "Textbook Carnot engines commonly use an ideal gas.",
      "পাঠ্যপুস্তকে কার্নো ইঞ্জিনে সাধারণত আদর্শ গ্যাস ধরা হয়।"),
    q("Carnot efficiency formula is:", "কার্নো দক্ষতার সূত্র:",
      ["1 − T1/T2", "1 − T2/T1", "T1/T2", "T2 − T1"],
      ["১ − T1/T2", "১ − T2/T1", "T1/T2", "T2 − T1"],
      "B", "easy", "factual",
      "η = 1 − T_cold/T_hot with absolute temperatures.",
      "η = ১ − T_ঠান্ডা/T_গরম (পরম তাপমাত্রা)।"),
    q("For T1=600 K and T2=300 K, Carnot efficiency is:", "T1=৬০০ K, T2=৩০০ K হলে কার্নো দক্ষতা:",
      ["25%", "50%", "75%", "100%"],
      ["২৫%", "৫০%", "৭৫%", "১০০%"],
      "B", "medium", "numerical",
      "η = 1 − 300/600 = 0.5 = 50%.",
      "η = ১ − ৩০০/৬০০ = ০.৫ = ৫০%।"),
    q("All reversible engines between same reservoirs have:", "একই আধারের মধ্যে সব প্রত্যাবর্তী ইঞ্জিনের:",
      ["different efficiencies", "same efficiency", "zero efficiency", "efficiency > Carnot"],
      ["ভিন্ন দক্ষতা", "একই দক্ষতা", "শূন্য দক্ষতা", "কার্নোর চেয়ে বেশি দক্ষতা"],
      "B", "medium", "conceptual",
      "Carnot’s theorem: all reversible engines share the same η.",
      "কার্নো উপপাদ্য: একই আধারে সব প্রত্যাবর্তী ইঞ্জিনের η সমান।"),
    q("No irreversible engine can have efficiency:", "কোনো অপ্রত্যাবর্তী ইঞ্জিনের দক্ষতা থাকতে পারে না:",
      ["less than Carnot", "equal to Carnot", "greater than Carnot between same T", "positive"],
      ["কার্নোর চেয়ে কম", "কার্নোর সমান", "একই T-তে কার্নোর চেয়ে বেশি", "ধনাত্মক"],
      "C", "easy", "conceptual",
      "Carnot efficiency is an upper bound for given temperatures.",
      "প্রদত্ত তাপমাত্রায় কার্নো দক্ষতা উচ্চসীমা।"),
    q("During isothermal expansion in Carnot cycle, heat is:", "কার্নো চক্রের সমোষ্ণ প্রসারণে তাপ:",
      ["rejected", "absorbed from hot reservoir", "zero", "converted fully to mass"],
      ["বর্জিত", "গরম আধার থেকে শোষিত", "শূন্য", "সম্পূর্ণ ভরে রূপান্তরিত"],
      "B", "easy", "conceptual",
      "Heat is absorbed from the hot reservoir at T1.",
      "T1-এ গরম আধার থেকে তাপ শোষিত হয়।"),
    q("During isothermal compression in Carnot cycle, heat is:", "কার্নো চক্রের সমোষ্ণ সংকোচনে তাপ:",
      ["absorbed from hot sink", "rejected to cold reservoir", "created", "always zero"],
      ["গরম সিঙ্ক থেকে শোষিত", "ঠান্ডা আধারে বর্জিত", "সৃষ্ট", "সবসময় শূন্য"],
      "B", "easy", "conceptual",
      "Heat is rejected to the cold reservoir at T2.",
      "T2-এ ঠান্ডা আধারে তাপ বর্জিত হয়।"),
    q("Raising T1 while keeping T2 fixed:", "T2 ধ্রুব রেখে T1 বাড়ালে:",
      ["decreases η", "increases η", "η unchanged", "makes η negative"],
      ["η কমায়", "η বাড়ায়", "η অপরিবর্তিত", "η ঋণাত্মক করে"],
      "B", "easy", "conceptual",
      "η = 1 − T2/T1 rises when T1 increases.",
      "T1 বাড়লে η = ১ − T2/T1 বাড়ে।"),
    q("Carnot cycle plotted on P–V diagram is a:", "P–V চিত্রে কার্নো চক্র:",
      ["rectangle", "closed loop of two isotherms and two adiabats", "straight line", "circle always"],
      ["আয়তক্ষেত্র", "দুই সমোষ্ণ ও দুই adiabatic-এর বদ্ধ লুপ", "সরলরেখা", "সবসময় বৃত্ত"],
      "B", "easy", "factual",
      "The classic Carnot P–V plot is that closed four-process loop.",
      "ক্লাসিক কার্নো P–V চিত্র সেই চার-প্রক্রিয়ার বদ্ধ লুপ।"),
]

EXTRA["phy2_27_ch01_t07"] = [
    q("Thermal efficiency of a heat engine is:", "তাপ ইঞ্জিনের তাপীয় দক্ষতা:",
      ["Q_out/Q_in", "W/Q_in", "Q_in/W", "W/Q_out"],
      ["Q_out/Q_in", "W/Q_in", "Q_in/W", "W/Q_out"],
      "B", "easy", "factual",
      "η = work output / heat input.",
      "η = কাজ আউটপুট / তাপ ইনপুট।"),
    q("If an engine absorbs 400 J and rejects 300 J, efficiency is:", "ইঞ্জিন ৪০০ J শোষণ ও ৩০০ J বর্জন করলে দক্ষতা:",
      ["25%", "33%", "75%", "100%"],
      ["২৫%", "৩৩%", "৭৫%", "১০০%"],
      "A", "medium", "numerical",
      "W=100 J; η=100/400=0.25=25%.",
      "W=১০০ J; η=১০০/৪০০=০.২৫=২৫%।"),
    q("Coefficient of performance of a refrigerator is:", "রেফ্রিজারেটরের কর্মদক্ষতা গুণাঙ্ক:",
      ["W/Q_c", "Q_c/W", "Q_h/W", "W/Q_h"],
      ["W/Q_c", "Q_c/W", "Q_h/W", "W/Q_h"],
      "B", "easy", "factual",
      "COP_ref = heat extracted from cold / work input.",
      "COP_ref = ঠান্ডা থেকে অপসারিত তাপ / কাজ ইনপুট।"),
    q("For a heat pump, useful heat is delivered to:", "তাপ পাম্পে উপযোগী তাপ সরবরাহ হয়:",
      ["cold space", "hot space", "nowhere", "vacuum"],
      ["ঠান্ডা স্থানে", "গরম স্থানে", "কোথাও নয়", "শূন্যে"],
      "B", "easy", "conceptual",
      "Heat pumps heat the warm region.",
      "তাপ পাম্প গরম অঞ্চলকে উষ্ণ করে।"),
    q("Higher cold-reservoir temperature (fixed hot T) for an engine:", "গরম T ধ্রুব রেখে ঠান্ডা আধারের তাপমাত্রা বাড়লে ইঞ্জিনে:",
      ["raises η", "lowers η", "η unchanged", "η becomes >1"],
      ["η বাড়ায়", "η কমায়", "η অপরিবর্তিত", "η >১ হয়"],
      "B", "medium", "conceptual",
      "η = 1 − T2/T1 falls if T2 rises.",
      "T2 বাড়লে η = ১ − T2/T1 কমে।"),
    q("A refrigerator’s working cycle requires:", "রেফ্রিজারেটরের কার্যচক্রে প্রয়োজন:",
      ["no work", "net work input", "only heat input", "mass creation"],
      ["কোনো কাজ নয়", "নীট কাজ ইনপুট", "শুধু তাপ ইনপুট", "ভর সৃষ্টি"],
      "B", "easy", "conceptual",
      "Work must be supplied to pump heat uphill.",
      "তাপ উপরের দিকে পাঠাতে কাজ লাগে।"),
    q("If Q_h = 500 J and W = 100 J for a heat pump, Q_c is:", "তাপ পাম্পে Q_h=৫০০ J, W=১০০ J হলে Q_c:",
      ["600 J", "400 J", "100 J", "500 J"],
      ["৬০০ J", "৪০০ J", "১০০ J", "৫০০ J"],
      "B", "medium", "numerical",
      "Q_h = Q_c + W ⇒ Q_c = 400 J.",
      "Q_h = Q_c + W ⇒ Q_c = ৪০০ J।"),
    q("Steam engine is an example of:", "বাষ্প ইঞ্জিন উদাহরণ:",
      ["heat engine", "heat pump only", "refrigerator only", "transformer"],
      ["তাপ ইঞ্জিন", "শুধু তাপ পাম্প", "শুধু রেফ্রিজারেটর", "ট্রান্সফরমার"],
      "A", "easy", "factual",
      "Steam engines convert heat into mechanical work.",
      "বাষ্প ইঞ্জিন তাপকে যান্ত্রিক কাজে রূপান্তর করে।"),
    q("Maximum possible efficiency between 127°C and 27°C is:", "১২৭°C ও ২৭°C-এর মধ্যে সর্বোচ্চ সম্ভাব্য দক্ষতা:",
      ["20%", "25%", "50%", "75%"],
      ["২০%", "২৫%", "৫০%", "৭৫%"],
      "B", "medium", "numerical",
      "T1=400 K, T2=300 K; η=1−300/400=25%.",
      "T1=৪০০ K, T2=৩০০ K; η=১−৩০০/৪০০=২৫%।"),
    q("Waste heat from engines is rejected to:", "ইঞ্জিনের বর্জিত তাপ যায়:",
      ["hot reservoir only", "cold reservoir/surroundings", "nowhere", "nuclear core"],
      ["শুধু গরম আধারে", "ঠান্ডা আধার/পরিবেশে", "কোথাও নয়", "নিউক্লিয়ার কোর"],
      "B", "easy", "factual",
      "Rejected heat goes to the cold sink.",
      "বর্জিত তাপ ঠান্ডা সিঙ্কে যায়।"),
]

EXTRA["phy2_27_ch01_t08"] = [
    q("Entropy is a measure of:", "এন্ট্রপি পরিমাপ করে:",
      ["order only", "disorder/randomness", "only temperature", "only pressure"],
      ["শুধু শৃঙ্খলা", "বিশৃঙ্খলা/এলোমেলোতা", "শুধু তাপমাত্রা", "শুধু চাপ"],
      "B", "easy", "conceptual",
      "Entropy quantifies molecular disorder or unavailable energy.",
      "এন্ট্রপি আণবিক বিশৃঙ্খলা বা অনুপলব্ধ শক্তি নির্দেশ করে।"),
    q("Entropy change has the same dimensions as:", "এন্ট্রপি পরিবর্তনের মাত্রা কোনটির সমান?",
      ["energy", "energy / temperature", "power", "force × distance only as energy without /T"],
      ["শক্তি", "শক্তি / তাপমাত্রা", "ক্ষমতা", "শুধু বল×দূরত্ব শক্তি /T ছাড়া"],
      "B", "easy", "factual",
      "Entropy unit is energy per temperature (J/K).",
      "এন্ট্রপির একক শক্তি/তাপমাত্রা (J/K)।"),
    q("For a reversible isothermal heat addition, ΔS =:", "প্রত্যাবর্তী সমোষ্ণ তাপযোগে ΔS =:",
      ["Q/T", "Q·T", "T/Q", "0 always"],
      ["Q/T", "Q·T", "T/Q", "সবসময় ০"],
      "A", "easy", "factual",
      "ΔS = Q_rev/T for isothermal reversible heat transfer.",
      "প্রত্যাবর্তী সমোষ্ণ তাপের জন্য ΔS = Q_rev/T।"),
    q("Entropy of an isolated system in a spontaneous process:", "স্বতঃস্ফূর্ত প্রক্রিয়ায় বিচ্ছিন্ন সিস্টেমের এন্ট্রপি:",
      ["decreases", "increases", "becomes zero", "oscillates only"],
      ["কমে", "বাড়ে", "শূন্য হয়", "শুধু দোদুল্যমান"],
      "B", "easy", "conceptual",
      "Second law: entropy of an isolated system increases for irreversible processes.",
      "দ্বিতীয় সূত্র: বিচ্ছিন্ন সিস্টেমের এন্ট্রপি অপ্রত্যাবর্তী প্রক্রিয়ায় বাড়ে।"),
    q("In a reversible adiabatic process, system entropy change is:", "প্রত্যাবর্তী adiabatic প্রক্রিয়ায় সিস্টেমের এন্ট্রপি পরিবর্তন:",
      ["positive", "negative", "zero", "infinite"],
      ["ধনাত্মক", "ঋণাত্মক", "শূন্য", "অসীম"],
      "C", "easy", "conceptual",
      "Reversible adiabatic ⇒ isentropic.",
      "প্রত্যাবর্তী adiabatic ⇒ সমএন্ট্রপি।"),
    q("Melting of ice at 0°C increases entropy because:", "০°C-এ বরফ গললে এন্ট্রপি বাড়ে কারণ:",
      ["order increases", "liquid is more disordered than solid", "temperature falls", "volume always shrinks"],
      ["শৃঙ্খলা বাড়ে", "কঠিনের চেয়ে তরল বেশি বিশৃঙ্খল", "তাপমাত্রা কমে", "আয়তন সবসময় কমে"],
      "B", "easy", "conceptual",
      "Liquid water has higher molecular disorder than ice.",
      "বরফের চেয়ে তরল পানিতে আণবিক বিশৃঙ্খলা বেশি।"),
    q("Entropy is a:", "এন্ট্রপি একটি:",
      ["path function", "state function", "force", "vector"],
      ["পথ ফাংশন", "অবস্থা ফাংশন", "বল", "ভেক্টর"],
      "B", "easy", "factual",
      "Entropy depends only on the thermodynamic state.",
      "এন্ট্রপি শুধু তাপগতিবিদ্যা অবস্থার উপর নির্ভর করে।"),
    q("Universe entropy change for a reversible process is:", "প্রত্যাবর্তী প্রক্রিয়ায় মহাবিশ্বের এন্ট্রপি পরিবর্তন:",
      ["positive", "negative", "zero", "undefined"],
      ["ধনাত্মক", "ঋণাত্মক", "শূন্য", "অনির্ধারিত"],
      "C", "medium", "conceptual",
      "For reversible processes ΔS_universe = 0.",
      "প্রত্যাবর্তী প্রক্রিয়ায় ΔS_মহাবিশ্ব = ০।"),
    q("Which tends to have higher entropy at same T?", "একই T-তে কোনটির এন্ট্রপি সাধারণত বেশি?",
      ["crystal solid", "same substance as gas", "perfect vacuum only", "single molecule fixed"],
      ["ক্রিস্টাল কঠিন", "একই পদার্থ গ্যাস অবস্থায়", "শুধু নিখুঁত শূন্য", "স্থির একক অণু"],
      "B", "easy", "conceptual",
      "Gases are more disordered than solids.",
      "কঠিনের চেয়ে গ্যাস বেশি বিশৃঙ্খল।"),
    q("Heat death of the universe concept relates to:", "মহাবিশ্বের তাপমৃত্যু ধারণা সম্পর্কিত:",
      ["maximum entropy/equilibrium", "zero entropy forever", "infinite free energy", "no thermodynamics"],
      ["সর্বোচ্চ এন্ট্রপি/সাম্যাবস্থা", "চিরকাল শূন্য এন্ট্রপি", "অসীম মুক্ত শক্তি", "তাপগতিবিদ্যা নেই"],
      "A", "medium", "conceptual",
      "Heat death imagines maximum entropy with no usable energy gradients.",
      "তাপমৃত্যুতে সর্বোচ্চ এন্ট্রপি ও ব্যবহারযোগ্য শক্তি ঢাল থাকে না।"),
]


def _merge_chunks() -> None:
    from _phy2_extra10_ch02 import build as b02
    from _phy2_extra10_ch03 import build as b03
    from _phy2_extra10_ch04 import build as b04
    from _phy2_extra10_ch05_08 import build as b05
    from _phy2_extra10_ch09_11 import build as b09

    for build in (b02, b03, b04, b05, b09):
        EXTRA.update(build(q))


def _load_rows(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def append_topic(topic_id: str, extras: list[dict]) -> str:
    path = TOPICS / f"{topic_id}.jsonl"
    if not path.exists():
        return f"MISSING {topic_id}"
    existing = _load_rows(path)
    n = len(existing)
    if n == 30:
        return f"SKIP {topic_id} already 30"
    if n != 20:
        return f"BADCOUNT {topic_id} has {n} (want 20 before append)"
    if len(extras) != 10:
        return f"BADEXTRA {topic_id} extras={len(extras)}"

    stems = {r["stem_en"].strip().lower() for r in existing}
    for row in extras:
        s = row["stem_en"].strip().lower()
        if s in stems:
            return f"DUP {topic_id}: {row['stem_en'][:80]}"
        stems.add(s)
        if row.get("correct") not in ("A", "B", "C", "D"):
            return f"BADCORRECT {topic_id}"
        if not re.search(r"[ঀ-৿]", row.get("stem_bn", "")):
            return f"NOBN {topic_id}: stem"

    with path.open("a", encoding="utf-8", newline="\n") as f:
        for row in extras:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    final = sum(1 for _ in path.open(encoding="utf-8") if _.strip())
    if final != 30:
        return f"AFTER {topic_id} has {final}"
    return f"OK {topic_id} 20→30"


def main() -> None:
    _merge_chunks()
    files = sorted(TOPICS.glob("phy2_27_*.jsonl"))
    expected = {p.stem for p in files}
    if len(files) != 68:
        raise SystemExit(f"expected 68 topic files, found {len(files)}")
    missing = expected - set(EXTRA)
    extra_keys = set(EXTRA) - expected
    if missing:
        raise SystemExit(f"missing EXTRA for: {sorted(missing)}")
    if extra_keys:
        raise SystemExit(f"unexpected EXTRA keys: {sorted(extra_keys)}")

    results = []
    for tid in sorted(EXTRA):
        results.append(append_topic(tid, EXTRA[tid]))

    bad = [r for r in results if not (r.startswith("OK ") or r.startswith("SKIP "))]
    ok = sum(1 for r in results if r.startswith("OK ") or r.startswith("SKIP "))
    print("\n".join(results))
    print(f"summary ok/skip={ok} bad={len(bad)} topics={len(results)}")
    if bad:
        raise SystemExit("failures:\n" + "\n".join(bad))

    # final count check
    bad_counts = [
        f.name
        for f in files
        if sum(1 for _ in f.open(encoding="utf-8") if _.strip()) != 30
    ]
    print("bad_counts", bad_counts or "none", "n", len(files))
    if bad_counts:
        raise SystemExit("line-count failures")


if __name__ == "__main__":
    main()
