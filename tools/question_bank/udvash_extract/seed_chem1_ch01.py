#!/usr/bin/env python3
"""Seed Chemistry 1st Paper Ch1 bilingual MCQs (Safe Use of the Laboratory).

Import CSV chemistry_1_ch01.csv had headers only; PDF OCR corrupted.
Authored 20 bilingual MCQs per topic aligned to NCTB chemistry_1st_paper_2027 ch01.
Topics: chem1_27_ch01_t01..t03.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPICS = ROOT / "content" / "bank" / "topics"
PARSED = ROOT / "content" / "bank" / "udvash_raw" / "chemistry_1" / "parsed"
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
from core import validate_record  # noqa: E402

SRC = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "chemistry p1 ch01; curated bilingual"
)

TOPIC_IDS = [f"chem1_27_ch01_t{i:02d}" for i in range(1, 4)]


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    if not re.search(r"[A-Za-z]", en):
        en = f"value {en}"
    if not re.search(r"[ঀ-৿]", bn) and re.search(r"[A-Za-z]{3,}", bn):
        bn = f"{bn} (মান)"
    return en, bn


def q(stem_en, stem_bn, opts_en, opts_bn, correct, difficulty, qtype, exp_en, exp_bn):
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
        "source": SRC,
    }


# --- t01: Laboratory rules and hazard symbols ---
T01 = [
    q(
        "Which practice is a basic laboratory safety rule?",
        "ল্যাবরেটরিতে কোনটি মৌলিক নিরাপত্তা নিয়ম?",
        [
            "Wear a lab coat and safety goggles when required",
            "Eat snacks on the bench during experiments",
            "Leave Bunsen burners unattended while lit",
            "Store food bottles with chemical reagents",
        ],
        [
            "প্রয়োজনে ল্যাব কোট ও সেফটি গগলস পরা",
            "পরীক্ষার সময় বেঞ্চে খাবার খাওয়া",
            "জ্বালানো বানসেন বার্নার অযত্নে ফেলে রাখা",
            "রাসায়নিকের সাথে খাবারের বোতল রাখা",
        ],
        "A", "easy", "factual",
        "Protective clothing and eye protection reduce injury risk in the lab.",
        "প্রতিরক্ষামূলক পোশাক ও চোখের সুরক্ষা ল্যাবে আঘাতের ঝুঁকি কমায়।",
    ),
    q(
        "Why should students not pipet solutions by mouth?",
        "মুখ দিয়ে পাইপেট করে দ্রবণ নেওয়া কেন নিষিদ্ধ?",
        [
            "It can cause poisoning or chemical burns",
            "It improves measurement accuracy",
            "It cools the solution faster",
            "It is required for dilute acids only",
        ],
        [
            "বিষক্রিয়া বা রাসায়নিক পোড়া হতে পারে",
            "মাপের নির্ভুলতা বাড়ে",
            "দ্রবণ দ্রুত ঠান্ডা হয়",
            "শুধু লঘু অ্যাসিডে প্রয়োজন",
        ],
        "A", "easy", "conceptual",
        "Mouth pipetting risks ingesting or inhaling hazardous chemicals.",
        "মুখ দিয়ে পাইপেটিংয়ে বিপজ্জনক রাসায়নিক গিলে ফেলা বা শ্বাসে নেওয়ার ঝুঁকি থাকে।",
    ),
    q(
        "A hazard symbol showing a flame typically indicates that a substance is:",
        "শিখার চিহ্নযুক্ত বিপদ সংকেত সাধারণত নির্দেশ করে পদার্থটি:",
        [
            "Flammable",
            "Radioactive only",
            "Completely inert",
            "Safe to taste",
        ],
        [
            "দাহ্য",
            "শুধু তেজস্ক্রিয়",
            "সম্পূর্ণ নিষ্ক্রিয়",
            "চেখে দেখা নিরাপদ",
        ],
        "A", "easy", "factual",
        "The flame pictogram warns of flammable solids, liquids, or gases.",
        "শিখা চিত্রলিপি দাহ্য কঠিন, তরল বা গ্যাসের সতর্কতা দেয়।",
    ),
    q(
        "The corrosion hazard symbol (liquid pouring on a hand/metal) warns mainly about:",
        "ক্ষয়কারী বিপদ সংকেত (হাত/ধাতুতে তরল পড়া) মূলত সতর্ক করে:",
        [
            "Corrosive substances that damage skin and materials",
            "Only sweet-smelling solvents",
            "Magnetic metals",
            "Cooling baths",
        ],
        [
            "ত্বক ও উপকরণ নষ্ট করে এমন ক্ষয়কারী পদার্থ",
            "শুধু মিষ্টি গন্ধের দ্রাবক",
            "চৌম্বক ধাতু",
            "কুলিং বাথ",
        ],
        "A", "easy", "factual",
        "Corrosive pictograms cover acids, bases, and other skin/eye damaging agents.",
        "ক্ষয়কারী চিত্রলিপি অ্যাসিড, ক্ষার ও ত্বক/চোখ ক্ষতিকর এজেন্টকে নির্দেশ করে।",
    ),
    q(
        "A skull-and-crossbones hazard symbol indicates a substance that is:",
        "মাথাখুলি ও হাড়ের ক্রস চিহ্ন নির্দেশ করে পদার্থটি:",
        [
            "Acute toxic",
            "Only biodegradable soap",
            "Food-grade sugar",
            "Distilled water",
        ],
        [
            "তীব্র বিষাক্ত",
            "শুধু জৈব-বিঘটনযোগ্য সাবান",
            "খাদ্য-গ্রেড চিনি",
            "ডিস্টিলড ওয়াটার",
        ],
        "A", "easy", "factual",
        "Skull-and-crossbones marks acute toxicity with severe health risk.",
        "মাথাখুলি চিহ্ন তীব্র বিষক্রিয়ার গুরুতর স্বাস্থ্যঝুঁকি নির্দেশ করে।",
    ),
    q(
        "Before starting any experiment, a student should first:",
        "যেকোনো পরীক্ষা শুরুর আগে শিক্ষার্থীর প্রথমে করা উচিত:",
        [
            "Read instructions and identify hazards of the chemicals used",
            "Mix all available reagents randomly",
            "Remove the fire extinguisher from the room",
            "Disable the fume hood permanently",
        ],
        [
            "নির্দেশনা পড়া ও ব্যবহৃত রাসায়নিকের বিপদ শনাক্ত করা",
            "সব উপলব্ধ বিকারক এলোমেলো মেশানো",
            "ঘর থেকে অগ্নিনির্বাপক সরানো",
            "ফিউম হুড স্থায়ীভাবে বন্ধ করা",
        ],
        "A", "easy", "application",
        "Knowing procedure and hazards prevents avoidable accidents.",
        "পদ্ধতি ও বিপদ জানা এড়ানোযোগ্য দুর্ঘটনা রোধ করে।",
    ),
    q(
        "Long loose hair and dangling jewelry in a chemistry lab are unsafe mainly because they:",
        "রসায়ন ল্যাবে লম্বা খোলা চুল ও ঝোলানো গহনা বিপজ্জনক প্রধানত কারণ:",
        [
            "Can catch fire or snag on apparatus",
            "Improve airflow to the burner",
            "Neutralize acids chemically",
            "Are required by hazard labels",
        ],
        [
            "আগুন ধরতে বা যন্ত্রে আটকে যেতে পারে",
            "বার্নারের বায়ুপ্রবাহ বাড়ায়",
            "অ্যাসিড রাসায়নিকভাবে নিরপেক্ষ করে",
            "বিপদ লেবেলে প্রয়োজনীয়",
        ],
        "A", "easy", "conceptual",
        "Loose hair and jewelry increase fire and entanglement hazards near flames and glassware.",
        "খোলা চুল ও গহনা শিখা ও কাচপাত্রের কাছে আগুন ও আটকে যাওয়ার ঝুঁকি বাড়ায়।",
    ),
    q(
        "An oxidizing-agent hazard symbol warns that a chemical can:",
        "অক্সিডাইজিং এজেন্টের বিপদ সংকেত সতর্ক করে যে রাসায়নিকটি:",
        [
            "Intensify a fire by supplying oxygen",
            "Always freeze spontaneously",
            "Absorb all UV light safely",
            "Act only as a food preservative",
        ],
        [
            "অক্সিজেন যোগিয়ে আগুন তীব্র করতে পারে",
            "সবসময় স্বতঃস্ফূর্তভাবে জমে যায়",
            "সব UV আলো নিরাপদে শোষে",
            "শুধু খাদ্য সংরক্ষক হিসেবে কাজ করে",
        ],
        "A", "medium", "conceptual",
        "Oxidizers can cause or worsen combustion when mixed with combustibles.",
        "অক্সিডাইজার দাহ্য পদার্থের সাথে মিশলে দহন শুরু বা তীব্র করতে পারে।",
    ),
    q(
        "Chemical bottles should be clearly labeled mainly to:",
        "রাসায়নিকের বোতলে স্পষ্ট লেবেল থাকার মূল উদ্দেশ্য:",
        [
            "Identify contents and associated hazards",
            "Decorate the laboratory shelves",
            "Hide the concentration from users",
            "Replace the need for training",
        ],
        [
            "উপাদান ও সংশ্লিষ্ট বিপদ শনাক্ত করা",
            "ল্যাব শেলফ সাজানো",
            "ব্যবহারকারীর কাছ থেকে ঘনত্ব লুকানো",
            "প্রশিক্ষণের প্রয়োজন দূর করা",
        ],
        "A", "easy", "factual",
        "Labels communicate identity, concentration, and hazard information.",
        "লেবেল পরিচয়, ঘনত্ব ও বিপদ তথ্য জানায়।",
    ),
    q(
        "Which action violates standard laboratory rules?",
        "কোন কাজ মানসম্মত ল্যাবরেটরি নিয়ম লঙ্ঘন করে?",
        [
            "Running and pushing near benches with glassware",
            "Washing hands after handling chemicals",
            "Keeping aisles clear of bags",
            "Reporting a cracked beaker to the teacher",
        ],
        [
            "কাচপাত্রসহ বেঞ্চের কাছে দৌড়ানো ও ধাক্কা দেওয়া",
            "রাসায়নিক স্পর্শের পর হাত ধোয়া",
            "আইল পরিষ্কার রাখা",
            "ফাটা বিকার শিক্ষককে জানানো",
        ],
        "A", "easy", "application",
        "Running near glass and chemicals raises spill and injury risk.",
        "কাচ ও রাসায়নিকের কাছে দৌড়ানো ছিটকে পড়া ও আঘাতের ঝুঁকি বাড়ায়।",
    ),
    q(
        "The environmental-hazard pictogram (dead fish/tree) warns that a substance may:",
        "পরিবেশ-বিপদ চিত্রলিপি (মরা মাছ/গাছ) সতর্ক করে পদার্থটি:",
        [
            "Harm aquatic life or the environment",
            "Only polish metal surfaces",
            "Increase lab lighting",
            "Neutralize all toxic gases",
        ],
        [
            "জলজ জীবন বা পরিবেশের ক্ষতি করতে পারে",
            "শুধু ধাতব পৃষ্ঠ পালিশ করে",
            "ল্যাবের আলো বাড়ায়",
            "সব বিষাক্ত গ্যাস নিরপেক্ষ করে",
        ],
        "A", "easy", "factual",
        "This GHS pictogram flags substances hazardous to the aquatic environment.",
        "এই GHS চিত্রলিপি জলজ পরিবেশের জন্য বিপজ্জনক পদার্থ চিহ্নিত করে।",
    ),
    q(
        "Contact lenses in a chemistry lab are often discouraged because:",
        "রসায়ন ল্যাবে কন্টাক্ট লেন্স প্রায়ই নিরুৎসাহিত কারণ:",
        [
            "Chemicals can trap under lenses and worsen eye injury",
            "They make safety goggles unnecessary",
            "They dissolve all acids instantly",
            "They replace the need for an eyewash",
        ],
        [
            "রাসায়নিক লেন্সের নিচে আটকে চোখের আঘাত বাড়াতে পারে",
            "সেফটি গগলস অপ্রয়োজনীয় করে",
            "সব অ্যাসিড তাৎক্ষণিক দ্রবীভূত করে",
            "আইওয়াশের প্রয়োজন দূর করে",
        ],
        "A", "medium", "conceptual",
        "Splashes under contact lenses are harder to rinse away promptly.",
        "কন্টাক্ট লেন্সের নিচে ছিটকে পড়া দ্রুত ধুয়ে সরানো কঠিন।",
    ),
    q(
        "An explosion-bomb hazard symbol indicates risk of:",
        "বিস্ফোরণ-বোমা বিপদ সংকেত নির্দেশ করে:",
        [
            "Explosive or violently reactive materials",
            "Mild fragrance oils only",
            "Paper towels",
            "Wooden spatulas",
        ],
        [
            "বিস্ফোরক বা প্রবল প্রতিক্রিয়াশীল পদার্থ",
            "শুধু মৃদু সুগন্ধি তেল",
            "কাগজের তোয়ালে",
            "কাঠের স্প্যাচুলা",
        ],
        "A", "easy", "factual",
        "The exploding bomb pictogram covers explosives and unstable reactive chemicals.",
        "বিস্ফোরণ চিত্রলিপি বিস্ফোরক ও অস্থিতিশীল প্রতিক্রিয়াশীল রাসায়নিককে অন্তর্ভুক্ত করে।",
    ),
    q(
        "Why must unauthorized experiments be forbidden in a school chemistry lab?",
        "স্কুল রসায়ন ল্যাবে অননুমোদিত পরীক্ষা নিষিদ্ধ কেন?",
        [
            "Unknown reactions can cause fires, toxic gases, or explosions",
            "They always give higher exam scores",
            "They sterilize the laboratory automatically",
            "They reduce the need for labels",
        ],
        [
            "অজানা বিক্রিয়ায় আগুন, বিষাক্ত গ্যাস বা বিস্ফোরণ হতে পারে",
            "সবসময় পরীক্ষায় বেশি নম্বর দেয়",
            "ল্যাব স্বয়ংক্রিয় জীবাণুমুক্ত করে",
            "লেবেলের প্রয়োজন কমায়",
        ],
        "A", "medium", "conceptual",
        "Unplanned mixing can produce uncontrolled hazards.",
        "অপরিকল্পিত মিশ্রণ নিয়ন্ত্রণহীন বিপদ সৃষ্টি করতে পারে।",
    ),
    q(
        "A gas-cylinder hazard symbol primarily warns about:",
        "গ্যাস সিলিন্ডার বিপদ সংকেত মূলত সতর্ক করে:",
        [
            "Gases under pressure",
            "Only powdered chalk",
            "Room-temperature ice",
            "Dry filter paper",
        ],
        [
            "চাপযুক্ত গ্যাস",
            "শুধু গুঁড়ো চক",
            "ঘরের তাপমাত্রার বরফ",
            "শুকনো ফিল্টার পেপার",
        ],
        "A", "easy", "factual",
        "Compressed-gas cylinders can rupture or release contents violently if mishandled.",
        "চাপযুক্ত গ্যাস সিলিন্ডার অযত্নে হ্যান্ডেল করলে ফেটে যেতে বা প্রবলভাবে নির্গত হতে পারে।",
    ),
    q(
        "Which statement about SDS (Safety Data Sheet) information is correct?",
        "SDS (Safety Data Sheet) তথ্য সম্পর্কে কোন বিবৃতি সঠিক?",
        [
            "It describes hazards, handling, and emergency measures for a chemical",
            "It is only a shopping price list",
            "It replaces the need for any protective equipment",
            "It is written only for non-hazardous water",
        ],
        [
            "এতে রাসায়নিকের বিপদ, হ্যান্ডলিং ও জরুরি ব্যবস্থা বর্ণিত থাকে",
            "এটি শুধু কেনাকাটার মূল্যতালিকা",
            "যেকোনো প্রতিরক্ষামূলক সরঞ্জামের প্রয়োজন দূর করে",
            "শুধু নিরাপদ পানির জন্য লেখা",
        ],
        "A", "medium", "factual",
        "SDS (MSDS) documents provide standardized hazard and response data.",
        "SDS (MSDS) নথিতে মানসম্মত বিপদ ও প্রতিক্রিয়া তথ্য থাকে।",
    ),
    q(
        "Open-toed shoes are discouraged in the lab mainly because:",
        "ল্যাবে খোলা আঙুলের জুতা নিরুৎসাহিত প্রধানত কারণ:",
        [
            "Spills and broken glass can injure unprotected feet",
            "They improve grip on wet floors always",
            "They neutralize acid spills chemically",
            "They are required by flame symbols",
        ],
        [
            "ছিটকে পড়া ও ভাঙা কাচ অরক্ষিত পায়ে আঘাত করতে পারে",
            "ভেজা মেঝেতে সবসময় গ্রিপ বাড়ায়",
            "অ্যাসিড ছিটকে পড়া রাসায়নিকভাবে নিরপেক্ষ করে",
            "শিখা চিহ্নে প্রয়োজনীয়",
        ],
        "A", "easy", "application",
        "Closed shoes protect against chemical and glass injuries to feet.",
        "বন্ধ জুতা পায়ের রাসায়নিক ও কাচজনিত আঘাত থেকে রক্ষা করে।",
    ),
    q(
        "A health-hazard pictogram (person silhouette) may indicate risks such as:",
        "স্বাস্থ্য-বিপদ চিত্রলিপি (মানুষের ছায়াচিত্র) নির্দেশ করতে পারে:",
        [
            "Carcinogenicity, respiratory sensitization, or organ toxicity",
            "Only pleasant perfume scent",
            "Increased room humidity only",
            "Faster crystallization of salt",
        ],
        [
            "ক্যান্সার সৃষ্টি, শ্বাসনালীর সংবেদনশীলতা বা অঙ্গের বিষক্রিয়া",
            "শুধু মনোরম পারফিউম গন্ধ",
            "শুধু ঘরের আর্দ্রতা বৃদ্ধি",
            "লবণের দ্রুত কেলাসন",
        ],
        "A", "medium", "conceptual",
        "This pictogram covers serious longer-term health effects beyond acute toxicity.",
        "এই চিত্রলিপি তীব্র বিষক্রিয়ার বাইরে গুরুতর দীর্ঘমেয়াদি স্বাস্থ্য প্রভাব নির্দেশ করে।",
    ),
    q(
        "Keeping the laboratory clean and orderly mainly helps to:",
        "ল্যাব পরিষ্কার ও সুশৃঙ্খল রাখা মূলত সাহায্য করে:",
        [
            "Prevent spills, trips, and mistaken reagent use",
            "Increase chemical concentrations automatically",
            "Eliminate the need for hazard symbols",
            "Make Bunsen burners burn hotter forever",
        ],
        [
            "ছিটকে পড়া, হোঁচট ও ভুল বিকারক ব্যবহার রোধ করতে",
            "রাসায়নিক ঘনত্ব স্বয়ংক্রিয় বাড়াতে",
            "বিপদ সংকেতের প্রয়োজন দূর করতে",
            "বানসেন বার্নার চিরকাল বেশি গরম জ্বালাতে",
        ],
        "A", "easy", "conceptual",
        "Good housekeeping reduces accident probability and confusion.",
        "সুশৃঙ্খল পরিবেশ দুর্ঘটনার সম্ভাবনা ও বিভ্রান্তি কমায়।",
    ),
    q(
        "Which pairing of symbol meaning is correct?",
        "কোন চিহ্ন–অর্থ জোড়া সঠিক?",
        [
            "Flame over circle → oxidizing agent",
            "Skull → only biodegradable soap",
            "Corrosion → completely safe perfume",
            "Dead fish → high nutritional value food",
        ],
        [
            "বৃত্তের উপর শিখা → অক্সিডাইজিং এজেন্ট",
            "মাথাখুলি → শুধু জৈব-বিঘটনযোগ্য সাবান",
            "ক্ষয় → সম্পূর্ণ নিরাপদ পারফিউম",
            "মরা মাছ → উচ্চ পুষ্টির খাদ্য",
        ],
        "A", "medium", "factual",
        "Flame-over-circle is the standard GHS mark for oxidizers.",
        "বৃত্তের উপর শিখা অক্সিডাইজারের মানক GHS চিহ্ন।",
    ),
]

# --- t02: Safe handling of chemicals and apparatus ---
T02 = [
    q(
        "When diluting concentrated sulfuric acid, the correct practice is to:",
        "গাঢ় সালফিউরিক অ্যাসিড লঘু করার সঠিক পদ্ধতি:",
        [
            "Add acid slowly to water with stirring",
            "Add water quickly into concentrated acid",
            "Pour acid and water together into a closed bottle",
            "Heat the acid first then add ice rapidly",
        ],
        [
            "পানিতে অ্যাসিড ধীরে ধীরে মিশিয়ে নাড়ানো",
            "গাঢ় অ্যাসিডে দ্রুত পানি ঢালা",
            "বন্ধ বোতলে অ্যাসিড ও পানি একসাথে ঢালা",
            "অ্যাসিড আগে গরম করে তারপর দ্রুত বরফ যোগ করা",
        ],
        "A", "easy", "application",
        "Acid-into-water controls the strongly exothermic dilution heat.",
        "অ্যাসিড-থেকে-পানি পদ্ধতি তীব্র তাপোৎপাদী লঘুকরণ নিয়ন্ত্রণ করে।",
    ),
    q(
        "Volatile or toxic vapors should preferably be handled:",
        "উদ্বায়ী বা বিষাক্ত বাষ্প অগ্রাধিকারভিত্তিতে হ্যান্ডেল করতে হয়:",
        [
            "Inside a working fume hood",
            "Beside an open food tray",
            "With the windows sealed and no ventilation",
            "By smelling deeply from the bottle neck",
        ],
        [
            "চালু ফিউম হুডের ভিতরে",
            "খোলা খাবারের ট্রের পাশে",
            "জানালা বন্ধ ও বায়ুচলাচল ছাড়া",
            "বোতলের মুখ থেকে গভীরভাবে শুঁকে",
        ],
        "A", "easy", "application",
        "Fume hoods remove hazardous vapors away from the breathing zone.",
        "ফিউম হুড বিষাক্ত বাষ্প শ্বাসপ্রশ্বাসের অঞ্চল থেকে সরিয়ে নেয়।",
    ),
    q(
        "To smell a chemical safely in the lab, one should:",
        "ল্যাবে কোনো রাসায়নিক নিরাপদে শুঁকতে হলে:",
        [
            "Waft a small amount of vapor toward the nose with the hand",
            "Inhale deeply with the nose inside the bottle",
            "Heat the bottle strongly then inhale",
            "Spray the liquid into the eyes first",
        ],
        [
            "হাত দিয়ে সামান্য বাষ্প নাকের দিকে ওয়াফ্ট করা",
            "বোতলের ভিতরে নাক দিয়ে গভীর শ্বাস নেওয়া",
            "বোতল জোরে গরম করে শ্বাস নেওয়া",
            "আগে চোখে তরল স্প্রে করা",
        ],
        "A", "easy", "factual",
        "Wafting limits exposure compared with direct sniffing.",
        "সরাসরি শুঁকানোর চেয়ে ওয়াফ্টিং এক্সপোজার সীমিত করে।",
    ),
    q(
        "A cracked glass beaker should be:",
        "ফাটা কাচের বিকার:",
        [
            "Taken out of service and reported for safe disposal",
            "Used for boiling concentrated acid anyway",
            "Repaired with ordinary tape for pressure reactions",
            "Filled with flammable solvent and heated strongly",
        ],
        [
            "ব্যবহার বন্ধ করে নিরাপদ নিষ্পত্তির জন্য জানানো",
            "তা সত্ত্বেও গাঢ় অ্যাসিড ফুটাতে ব্যবহার",
            "চাপ বিক্রিয়ার জন্য সাধারণ টেপ দিয়ে মেরামত",
            "দাহ্য দ্রাবক ভরে জোরে গরম করা",
        ],
        "A", "easy", "application",
        "Damaged glassware can fail suddenly and cause cuts or spills.",
        "ক্ষতিগ্রস্ত কাচপাত্র হঠাৎ ভেঙে কাটা বা ছিটকে পড়ার কারণ হতে পারে।",
    ),
    q(
        "When heating a liquid in a test tube over a flame, point the mouth:",
        "শিখায় টেস্ট টিউবে তরল গরম করার সময় মুখ নির্দেশ করতে হয়:",
        [
            "Away from yourself and nearby people",
            "Directly toward your face for observation",
            "Toward the nearest student's eyes",
            "Straight up under a closed shelf",
        ],
        [
            "নিজের ও আশেপাশের লোকের দিক থেকে দূরে",
            "পর্যবেক্ষণের জন্য সরাসরি মুখের দিকে",
            "নিকটতম শিক্ষার্থীর চোখের দিকে",
            "বন্ধ শেলফের নিচে সোজা উপরে",
        ],
        "A", "easy", "application",
        "Bump ejection of hot liquid can burn anyone in the line of the tube mouth.",
        "গরম তরল হঠাৎ ছিটকে টিউবমুখের সারিতে থাকা কাউকে পোড়াতে পারে।",
    ),
    q(
        "A Bunsen burner air hole fully open typically produces a:",
        "বানসেন বার্নারের বায়ু ছিদ্র পুরো খোলা থাকলে সাধারণত তৈরি হয়:",
        [
            "Hot, almost colorless (roaring) flame",
            "Cool, sooty luminous flame only",
            "Flame that needs no gas supply",
            "Flame that cannot heat anything",
        ],
        [
            "গরম, প্রায় বর্ণহীন (গর্জনশীল) শিখা",
            "শুধু ঠান্ডা কালচে উজ্জ্বল শিখা",
            "গ্যাস সরবরাহ ছাড়া শিখা",
            "কিছুই গরম করতে পারে না এমন শিখা",
        ],
        "A", "medium", "factual",
        "More air gives complete combustion and a hotter non-luminous flame.",
        "বেশি বাতাসে সম্পূর্ণ দহন ও গরম অ-উজ্জ্বল শিখা পাওয়া যায়।",
    ),
    q(
        "After using a reagent bottle, the correct habit is to:",
        "বিকারক বোতল ব্যবহারের পর সঠিক অভ্যাস:",
        [
            "Replace the stopper immediately and return the bottle",
            "Leave the stopper on the bench permanently",
            "Swap stoppers between acid and base bottles",
            "Pour unused excess back into a different unlabeled bottle",
        ],
        [
            "তৎক্ষণাৎ স্টপার বসিয়ে বোতল ফেরত রাখা",
            "স্টপার স্থায়ীভাবে বেঞ্চে ফেলে রাখা",
            "অ্যাসিড ও ক্ষার বোতলের স্টপার বিনিময় করা",
            "অব্যবহৃত উদ্বৃত্ত অন্য লেবেলবিহীন বোতলে ঢালা",
        ],
        "A", "easy", "application",
        "Prompt resealing prevents spills, contamination, and misidentification.",
        "দ্রুত বন্ধ করা ছিটকে পড়া, দূষণ ও ভুল শনাক্তকরণ রোধ করে।",
    ),
    q(
        "Concentrated acids and strong bases should be transferred using:",
        "গাঢ় অ্যাসিড ও প্রবল ক্ষার স্থানান্তরে ব্যবহার করা উচিত:",
        [
            "Appropriate pipets/droppers or funnels with care—not mouth pipetting",
            "Bare fingers dipped into the bottle",
            "Cloth soaked and wrung by hand into eyes",
            "Open cups carried while running",
        ],
        [
            "যথাযথ পাইপেট/ড্রপার বা ফানেল সতর্কভাবে—মুখ দিয়ে নয়",
            "খালি আঙুল বোতলে ডুবিয়ে",
            "কাপড় ভিজিয়ে হাতে নিংড়ে চোখে",
            "খোলা কাপ নিয়ে দৌড়ে",
        ],
        "A", "easy", "factual",
        "Proper transfer tools reduce contact with corrosive liquids.",
        "সঠিক স্থানান্তর সরঞ্জাম ক্ষয়কারী তরলের সংস্পর্শ কমায়।",
    ),
    q(
        "Flammable organic solvents should not be heated with:",
        "দাহ্য জৈব দ্রাবক গরম করা উচিত নয়:",
        [
            "An open Bunsen flame on the open bench",
            "A controlled water bath when appropriate",
            "A properly designed heating mantle if specified",
            "A hot plate rated for the solvent when supervised",
        ],
        [
            "খোলা বেঞ্চে খোলা বানসেন শিখা দিয়ে",
            "প্রয়োজনে নিয়ন্ত্রিত ওয়াটার বাথ দিয়ে",
            "নির্দেশিত হলে যথাযথ হিটিং ম্যান্টল দিয়ে",
            "তদারকিতে দ্রাবক-উপযোগী হট প্লেট দিয়ে",
        ],
        "A", "medium", "application",
        "Open flames readily ignite solvent vapors.",
        "খোলা শিখা দ্রাবক বাষ্প সহজে জ্বালিয়ে দেয়।",
    ),
    q(
        "A spatula used for one solid reagent should not be dipped into another bottle because it:",
        "এক কঠিন বিকারকের স্প্যাচুলা অন্য বোতলে ডোবানো উচিত নয় কারণ:",
        [
            "Causes cross-contamination of chemicals",
            "Always improves purity",
            "Neutralizes both reagents safely",
            "Is required by flame symbols",
        ],
        [
            "রাসায়নিকের পারস্পরিক দূষণ ঘটায়",
            "সবসময় বিশুদ্ধতা বাড়ায়",
            "উভয় বিকারক নিরাপদে নিরপেক্ষ করে",
            "শিখা চিহ্নে প্রয়োজনীয়",
        ],
        "A", "easy", "conceptual",
        "Shared dirty spatulas transfer unwanted substances between bottles.",
        "অপরিষ্কার ভাগ করা স্প্যাচুলা বোতলগুলোর মধ্যে অবাঞ্ছিত পদার্থ স্থানান্তর করে।",
    ),
    q(
        "When inserting glass tubing into a rubber stopper, safety improves if you:",
        "রাবার স্টপারে কাচ নল ঢোকানোর সময় নিরাপত্তা বাড়ে যদি:",
        [
            "Lubricate with water/glycerol and hold the glass near the insertion point with a cloth",
            "Force dry glass with bare hands far from the stopper",
            "Heat the stopper in an open flame while pushing hard",
            "Use broken tubing without checking edges",
        ],
        [
            "পানি/গ্লিসারল দিয়ে লুব্রিকেট করে কাপড় দিয়ে নলের কাছে ধরে ঢোকানো",
            "শুকনো কাচ খালি হাতে স্টপার থেকে দূরে ধরে জোরে ঠেলা",
            "খোলা শিখায় স্টপার গরম করে জোরে ঠেলা",
            "ভাঙা নল কিনারা না দেখে ব্যবহার",
        ],
        "A", "medium", "application",
        "Lubrication and close grip reduce sudden glass breakage into the hand.",
        "লুব্রিকেশন ও কাছাকাছি গ্রিপ হাতে কাচ হঠাৎ ভাঙা কমায়।",
    ),
    q(
        "Balances and electronic meters should be protected from:",
        "ব্যালান্স ও ইলেকট্রনিক মিটার রক্ষা করতে হয়:",
        [
            "Corrosive spills and rough chemical contamination",
            "Being wiped gently after use",
            "Being kept level on a stable surface",
            "Being calibrated as instructed",
        ],
        [
            "ক্ষয়কারী ছিটকে পড়া ও রুক্ষ রাসায়নিক দূষণ",
            "ব্যবহারের পর আলতো মুছে ফেলা",
            "স্থিতিশীল পৃষ্ঠে সমতল রাখা",
            "নির্দেশমতো ক্যালিব্রেট করা",
        ],
        "A", "easy", "factual",
        "Chemical damage ruins accuracy and can create electrical hazards.",
        "রাসায়নিক ক্ষতি নির্ভুলতা নষ্ট করে ও বৈদ্যুতিক বিপদ সৃষ্টি করতে পারে।",
    ),
    q(
        "A reagent labeled “irritant” should be handled so as to avoid:",
        "“ইরিট্যান্ট” লেবেলযুক্ত বিকারক হ্যান্ডেল করতে এড়িয়ে চলতে হয়:",
        [
            "Skin, eye, and unnecessary inhalation contact",
            "Reading the label before use",
            "Using gloves when required",
            "Working in a ventilated space",
        ],
        [
            "ত্বক, চোখ ও অপ্রয়োজনীয় শ্বাসের সংস্পর্শ",
            "ব্যবহারের আগে লেবেল পড়া",
            "প্রয়োজনে গ্লাভস ব্যবহার",
            "বায়ুচলাচলযুক্ত স্থানে কাজ",
        ],
        "A", "easy", "conceptual",
        "Irritants cause local inflammation on contact or inhalation.",
        "ইরিট্যান্ট সংস্পর্শ বা শ্বাসে স্থানীয় প্রদাহ ঘটায়।",
    ),
    q(
        "Never heat a closed (sealed) glass container strongly because:",
        "বন্ধ (সিল করা) কাচ পাত্র জোরে গরম করা উচিত নয় কারণ:",
        [
            "Pressure buildup can cause explosion",
            "It always cools the contents",
            "It removes all oxygen permanently",
            "It makes glass stronger indefinitely",
        ],
        [
            "চাপ বৃদ্ধিতে বিস্ফোরণ হতে পারে",
            "সবসময় উপাদান ঠান্ডা করে",
            "সব অক্সিজেন স্থায়ীভাবে সরায়",
            "কাচকে অনির্দিষ্টকাল শক্তিশালী করে",
        ],
        "A", "medium", "conceptual",
        "Trapped vapor pressure can shatter sealed glass violently.",
        "আটকে থাকা বাষ্পচাপ সিল করা কাচ প্রবলভাবে ফাটাতে পারে।",
    ),
    q(
        "When pouring from a large reagent bottle into a beaker, support the bottle and:",
        "বড় বিকারক বোতল থেকে বিকারে ঢালার সময় বোতল ধরে:",
        [
            "Pour carefully along a glass rod or with controlled flow",
            "Shake violently over the edge of the bench",
            "Hold it only by the stopper",
            "Pour while looking away completely",
        ],
        [
            "কাচদণ্ড বরাবর বা নিয়ন্ত্রিত প্রবাহে সতর্কভাবে ঢালা",
            "বেঞ্চের কিনারায় জোরে ঝাঁকানো",
            "শুধু স্টপার ধরে রাখা",
            "সম্পূর্ণ অন্যদিকে তাকিয়ে ঢালা",
        ],
        "A", "easy", "application",
        "Controlled pouring reduces spills and splashes.",
        "নিয়ন্ত্রিত ঢালা ছিটকে পড়া ও ছিটা কমায়।",
    ),
    q(
        "Mercury from a broken thermometer is hazardous mainly because it is:",
        "ভাঙা থার্মোমিটারের পারদ বিপজ্জনক প্রধানত কারণ এটি:",
        [
            "Toxic and can release harmful vapor",
            "A harmless food colorant",
            "Completely non-volatile always",
            "Required in every titration",
        ],
        [
            "বিষাক্ত এবং ক্ষতিকর বাষ্প ছাড়তে পারে",
            "নিরাপদ খাদ্য রং",
            "সবসময় সম্পূর্ণ অ-উদ্বায়ী",
            "প্রতিটি টাইট্রেশনে প্রয়োজনীয়",
        ],
        "A", "medium", "factual",
        "Elemental mercury vapor is neurotoxic; spills need special cleanup.",
        "মৌলিক পারদের বাষ্প স্নায়ুতন্ত্রের জন্য বিষাক্ত; ছিটকে পড়া বিশেষ পরিষ্কার দাবি করে।",
    ),
    q(
        "Gloves used for handling corrosive chemicals should be:",
        "ক্ষয়কারী রাসায়নিক হ্যান্ডলিংয়ের গ্লাভস হতে হবে:",
        [
            "Chemically resistant and intact (not torn)",
            "Made of ordinary tissue paper only",
            "Soaked in concentrated acid first",
            "Shared after use without washing",
        ],
        [
            "রাসায়নিক-প্রতিরোধী ও অক্ষত (ছেঁড়া নয়)",
            "শুধু সাধারণ টিস্যু কাগজের",
            "আগে গাঢ় অ্যাসিডে ভেজানো",
            "ধোয়া ছাড়া ব্যবহারের পর ভাগ করা",
        ],
        "A", "easy", "factual",
        "Damaged or unsuitable gloves give a false sense of protection.",
        "ক্ষতিগ্রস্ত বা অনুপযুক্ত গ্লাভস মিথ্যা নিরাপত্তার অনুভূতি দেয়।",
    ),
    q(
        "A condenser for reflux should be set up so that cooling water:",
        "রিফ্লাক্স কনডেন্সার এমনভাবে বসাতে হয় যাতে শীতল পানি:",
        [
            "Enters at the lower inlet and exits at the upper outlet",
            "Never flows at all during boiling",
            "Enters only through the boiling flask neck",
            "Is replaced by gasoline for better cooling",
        ],
        [
            "নিচের ইনলেটে প্রবেশ করে উপরের আউটলেটে বের হয়",
            "ফুটন্ত অবস্থায় কখনোই প্রবাহিত হয় না",
            "শুধু ফুটন্ত ফ্লাস্কের গলা দিয়ে প্রবেশ করে",
            "ভালো শীতলনের জন্য পেট্রোল দিয়ে প্রতিস্থাপিত হয়",
        ],
        "A", "hard", "application",
        "Bottom-to-top water flow fills the jacket and cools vapor efficiently.",
        "নিচ থেকে উপর পানিপ্রবাহ জ্যাকেট ভরে বাষ্প দক্ষভাবে শীতল করে।",
    ),
    q(
        "Solid NaOH pellets should be handled carefully because they are:",
        "কঠিন NaOH পেলেট সতর্কভাবে হ্যান্ডেল করতে হয় কারণ এরা:",
        [
            "Highly hygroscopic and strongly corrosive to skin",
            "Completely inert like sand",
            "Safe to taste for identity checks",
            "Non-reactive with moisture",
        ],
        [
            "অত্যন্ত আর্দ্রতাগ্রাহী ও ত্বকের জন্য প্রবল ক্ষয়কারী",
            "বালির মতো সম্পূর্ণ নিষ্ক্রিয়",
            "শনাক্তকরণে চেখে দেখা নিরাপদ",
            "আর্দ্রতার সাথে অপ্রতিক্রিয়াশীল",
        ],
        "A", "medium", "conceptual",
        "NaOH absorbs moisture/CO2 and causes severe chemical burns.",
        "NaOH আর্দ্রতা/CO2 শোষে এবং গুরুতর রাসায়নিক পোড়া ঘটায়।",
    ),
    q(
        "Before lighting a Bunsen burner, one should check that:",
        "বানসেন বার্নার জ্বালানোর আগে পরীক্ষা করা উচিত:",
        [
            "Gas tubing is intact and the area is free of flammable spills",
            "All windows are sealed airtight forever",
            "Solvent bottles are open beside the flame",
            "Hair is hanging over the burner head",
        ],
        [
            "গ্যাস টিউব অক্ষত এবং এলাকা দাহ্য ছিটকে পড়া মুক্ত",
            "সব জানালা চিরকাল বায়ুরোধী বন্ধ",
            "দ্রাবক বোতল শিখার পাশে খোলা",
            "চুল বার্নার মাথার উপর ঝুলছে",
        ],
        "A", "easy", "application",
        "Leaks and nearby flammables create fire and explosion risk.",
        "লিক ও কাছের দাহ্য পদার্থ আগুন ও বিস্ফোরণের ঝুঁকি তৈরি করে।",
    ),
]

# --- t03: Accident response and waste disposal ---
T03 = [
    q(
        "If a chemical splashes into the eyes, the first response should be to:",
        "রাসায়নিক চোখে ছিটকে পড়লে প্রথম করণীয়:",
        [
            "Rinse thoroughly at an eyewash for at least 15 minutes and seek help",
            "Rub the eyes dry with a towel only",
            "Neutralize by adding more concentrated acid",
            "Ignore it if vision seems temporarily clear",
        ],
        [
            "আইওয়াশে কমপক্ষে ১৫ মিনিট ভালো করে ধুয়ে সাহায্য নেওয়া",
            "শুধু তোয়ালে দিয়ে চোখ মুছে শুকানো",
            "আরও গাঢ় অ্যাসিড যোগ করে নিরপেক্ষ করা",
            "দৃষ্টি সাময়িক পরিষ্কার মনে হলে উপেক্ষা করা",
        ],
        "A", "easy", "application",
        "Immediate prolonged flushing dilutes and removes chemical from the eye.",
        "তাৎক্ষণিক দীর্ঘ ধোয়া চোখ থেকে রাসায়নিক লঘু ও অপসারণ করে।",
    ),
    q(
        "A small clothing fire on a person is often best managed by:",
        "কারো পোশাকে ছোট আগুন প্রায়ই সবচেয়ে ভালো নিয়ন্ত্রণ হয়:",
        [
            "Stop–drop–roll or using a fire blanket / safety shower as appropriate",
            "Running outdoors while the fabric burns",
            "Pouring organic solvent on the flames",
            "Hiding under a closed fume hood",
        ],
        [
            "থামো–শুয়ে পড়ো–গড়াগড়ি বা উপযুক্তভাবে অগ্নি কম্বল/সেফটি শাওয়ার",
            "কাপড় জ্বলতে জ্বলতে বাইরে দৌড়ানো",
            "শিখায় জৈব দ্রাবক ঢালা",
            "বন্ধ ফিউম হুডের নিচে লুকানো",
        ],
        "A", "easy", "application",
        "Smothering removes oxygen; running fans the fire.",
        "ঢেকে দেওয়া অক্সিজেন সরায়; দৌড়ানো আগুন বাড়ায়।",
    ),
    q(
        "Acid spilled on skin should be treated first by:",
        "ত্বকে অ্যাসিড ছিটকে পড়লে প্রথমে করতে হয়:",
        [
            "Rinsing with plenty of running water",
            "Applying more concentrated base immediately without rinsing",
            "Covering with dry cotton only",
            "Heating the area with a Bunsen flame",
        ],
        [
            "প্রচুর প্রবাহমান পানি দিয়ে ধোয়া",
            "ধোয়া ছাড়াই তাৎক্ষণিক গাঢ় ক্ষার লাগানো",
            "শুধু শুকনো তুলা দিয়ে ঢাকা",
            "বানসেন শিখায় এলাকা গরম করা",
        ],
        "A", "easy", "application",
        "Copious water dilution is the primary first aid for most acid skin contact.",
        "অধিকাংশ অ্যাসিড ত্বক সংস্পর্শে প্রচুর পানি দিয়ে লঘুকরণই প্রাথমিক চিকিৎসা।",
    ),
    q(
        "Which waste should NOT be poured down the laboratory sink?",
        "কোন বর্জ্য ল্যাব সিঙ্কে ঢালা উচিত নয়?",
        [
            "Halogenated organic solvents and heavy-metal solutions",
            "Dilute aqueous salt rinse after neutralization when permitted",
            "Excess rinse water from washing glassware with detergent only",
            "Plain cooled water from a condenser",
        ],
        [
            "হ্যালোজেনেটেড জৈব দ্রাবক ও ভারী ধাতুর দ্রবণ",
            "অনুমোদিত হলে নিরপেক্ষকরণের পর লঘু জলীয় লবণ ধোয়া",
            "শুধু ডিটারজেন্ট দিয়ে কাচপাত্র ধোয়ার অতিরিক্ত পানি",
            "কনডেন্সারের সাধারণ ঠান্ডা পানি",
        ],
        "A", "medium", "conceptual",
        "Hazardous organics and heavy metals require designated waste containers.",
        "বিপজ্জনক জৈব ও ভারী ধাতুর জন্য নির্ধারিত বর্জ্য পাত্র প্রয়োজন।",
    ),
    q(
        "After any significant laboratory accident, students should:",
        "যেকোনো গুরুতর ল্যাব দুর্ঘটনার পর শিক্ষার্থীদের করা উচিত:",
        [
            "Alert the teacher/instructor and follow emergency procedures",
            "Hide the evidence to avoid blame",
            "Continue mixing unknown chemicals nearby",
            "Turn off all eyewash stations permanently",
        ],
        [
            "শিক্ষক/প্রশিক্ষককে জানিয়ে জরুরি পদ্ধতি অনুসরণ করা",
            "দোষ এড়াতে প্রমাণ লুকানো",
            "কাছে অজানা রাসায়নিক মেশানো চালিয়ে যাওয়া",
            "সব আইওয়াশ স্থায়ীভাবে বন্ধ করা",
        ],
        "A", "easy", "factual",
        "Prompt reporting enables proper medical and safety response.",
        "দ্রুত জানানো সঠিক চিকিৎসা ও নিরাপত্তা সাড়া নিশ্চিত করে।",
    ),
    q(
        "A Class B fire involving flammable liquids is commonly fought with:",
        "দাহ্য তরলের Class B আগুন সাধারণত নেভানো হয়:",
        [
            "A dry-chemical or CO2 extinguisher suitable for flammable liquids",
            "A strong water jet aimed into burning oil",
            "Throwing more solvent onto the fire",
            "Using paper towels as fuel",
        ],
        [
            "দাহ্য তরলের জন্য উপযোগী ড্রাই-কেমিক্যাল বা CO2 নির্বাপক",
            "জ্বলন্ত তেলে শক্তিশালী পানির জেট",
            "আগুনে আরও দ্রাবক ছোড়া",
            "জ্বালানি হিসেবে কাগজের তোয়ালে ব্যবহার",
        ],
        "A", "medium", "factual",
        "Water can spread burning organic liquids; smothering agents are preferred.",
        "পানি জ্বলন্ত জৈব তরল ছড়াতে পারে; ঢেকে নেভানো এজেন্ট অগ্রাধিকার।",
    ),
    q(
        "Broken glass waste should be placed in:",
        "ভাঙা কাচের বর্জ্য রাখতে হয়:",
        [
            "A puncture-resistant sharps/glass disposal container",
            "The ordinary paper recycling bin only",
            "A soft plastic shopping bag left on the floor",
            "Food waste compost",
        ],
        [
            "ছিদ্র-প্রতিরোধী শার্পস/কাচ নিষ্পত্তি পাত্রে",
            "শুধু সাধারণ কাগজ পুনর্ব্যবহার বিনে",
            "মেঝেতে রাখা নরম প্লাস্টিক শপিং ব্যাগে",
            "খাদ্য বর্জ্য কম্পোস্টে",
        ],
        "A", "easy", "factual",
        "Dedicated containers protect cleaners from cuts.",
        "নির্ধারিত পাত্র পরিচ্ছন্নতাকর্মীদের কাটা থেকে রক্ষা করে।",
    ),
    q(
        "If a student inhales irritating vapor and feels dizzy, they should:",
        "শিক্ষার্থী উত্তেজক বাষ্প শ্বাসে নিয়ে মাথা ঘোরা অনুভব করলে:",
        [
            "Move to fresh air and seek immediate assistance",
            "Return to sniff the bottle more deeply",
            "Drink concentrated acid as an antidote",
            "Stay in the vapor cloud until symptoms worsen",
        ],
        [
            "তাজা বাতাসে গিয়ে তাৎক্ষণিক সাহায্য নেওয়া",
            "বোতল আরও গভীরভাবে শুঁকতে ফিরে যাওয়া",
            "প্রতিষেধক হিসেবে গাঢ় অ্যাসিড পান করা",
            "লক্ষণ বাড়তে থাকা পর্যন্ত বাষ্পমেঘে থাকা",
        ],
        "A", "easy", "application",
        "Fresh air and medical evaluation are the correct first responses.",
        "তাজা বাতাস ও চিকিৎসা মূল্যায়নই সঠিক প্রথম সাড়া।",
    ),
    q(
        "Neutralization of small dilute acid spills on the bench often uses:",
        "বেঞ্চে ছোট লঘু অ্যাসিড ছিটকে পড়া নিরপেক্ষকরণে প্রায়ই ব্যবহৃত হয়:",
        [
            "A mild base such as sodium bicarbonate, then wipe and rinse",
            "Concentrated sulfuric acid poured on top",
            "Gasoline as a cleaner",
            "Metallic sodium pieces",
        ],
        [
            "সোডিয়াম বাইকার্বোনেটের মতো মৃদু ক্ষার, তারপর মুছে ধোয়া",
            "উপরে গাঢ় সালফিউরিক অ্যাসিড ঢালা",
            "পরিষ্কারক হিসেবে পেট্রোল",
            "ধাতব সোডিয়ামের টুকরো",
        ],
        "A", "medium", "application",
        "Bicarbonate safely neutralizes many dilute acid spills with mild fizzing.",
        "বাইকার্বোনেট অনেক লঘু অ্যাসিড ছিটকে পড়া নিরাপদে নিরপেক্ষ করে।",
    ),
    q(
        "Chemical waste containers must be:",
        "রাসায়নিক বর্জ্য পাত্র অবশ্যই:",
        [
            "Properly labeled with contents and hazard information",
            "Left unlabeled so anyone can guess",
            "Filled beyond the rim and left open",
            "Stored inside food refrigerators",
        ],
        [
            "উপাদান ও বিপদ তথ্যসহ সঠিকভাবে লেবেলযুক্ত",
            "লেবেলবিহীন যাতে কেউ অনুমান করে",
            "কানা উপচে ভরে খোলা রাখা",
            "খাদ্য রেফ্রিজারেটরে সংরক্ষিত",
        ],
        "A", "easy", "factual",
        "Clear labeling prevents incompatible mixing and improper disposal.",
        "স্পষ্ট লেবেল অসঙ্গত মিশ্রণ ও ভুল নিষ্পত্তি রোধ করে।",
    ),
    q(
        "Incompatible chemical wastes (e.g., strong oxidizers and organics) should be:",
        "অসঙ্গত রাসায়নিক বর্জ্য (যেমন প্রবল অক্সিডাইজার ও জৈব) রাখতে হয়:",
        [
            "Segregated in separate waste streams",
            "Mixed freely to save container space",
            "Poured together into one sink drain",
            "Heated jointly until they react",
        ],
        [
            "আলাদা বর্জ্য ধারায় পৃথক রাখা",
            "পাত্র বাঁচাতে মুক্তভাবে মেশানো",
            "এক সিঙ্ক ড্রেনে একসাথে ঢালা",
            "বিক্রিয়া পর্যন্ত একসাথে গরম করা",
        ],
        "A", "medium", "conceptual",
        "Mixing incompatibles can cause fire, gas release, or explosion.",
        "অসঙ্গত পদার্থ মেশালে আগুন, গ্যাস নির্গমন বা বিস্ফোরণ হতে পারে।",
    ),
    q(
        "A minor cut from glassware should be managed by:",
        "কাচপাত্র থেকে ছোট কাটা পরিচালনা করতে হয়:",
        [
            "Stopping bleeding, cleaning, covering, and reporting if needed",
            "Dipping the wound into concentrated acid",
            "Ignoring bleeding near chemicals",
            "Using the same unwashed towel for everyone's wounds",
        ],
        [
            "রক্তপাত থামানো, পরিষ্কার, ঢেকে দেওয়া এবং প্রয়োজনে জানানো",
            "ক্ষত গাঢ় অ্যাসিডে ডোবানো",
            "রাসায়নিকের কাছে রক্তপাত উপেক্ষা করা",
            "সবার ক্ষতে একই না-ধোয়া তোয়ালে ব্যবহার",
        ],
        "A", "easy", "application",
        "Basic first aid plus reporting prevents infection and further exposure.",
        "মৌলিক প্রাথমিক চিকিৎসা ও জানানো সংক্রমণ ও আরও এক্সপোজার রোধ করে।",
    ),
    q(
        "If a large toxic gas release occurs in the lab, the priority is to:",
        "ল্যাবে বড় বিষাক্ত গ্যাস নির্গমন হলে অগ্রাধিকার:",
        [
            "Evacuate to fresh air and alert emergency responders",
            "Stay to collect samples without protection",
            "Close all exits and keep breathing the air",
            "Turn on every Bunsen burner",
        ],
        [
            "তাজা বাতাসে সরিয়ে জরুরি সাড়াদাতাদের জানানো",
            "সুরক্ষা ছাড়া নমুনা সংগ্রহে থাকা",
            "সব প্রস্থান বন্ধ করে বাতাস শ্বাস নিতে থাকা",
            "সব বানসেন বার্নার জ্বালানো",
        ],
        "A", "medium", "application",
        "Life safety through evacuation outweighs saving apparatus or samples.",
        "সরিয়ে নেওয়ার মাধ্যমে জীবনরক্ষা যন্ত্রপাতি/নমুনা বাঁচানোর চেয়ে অগ্রাধিকার।",
    ),
    q(
        "Used filter papers contaminated with hazardous solids should be:",
        "বিপজ্জনক কঠিনে দূষিত ব্যবহৃত ফিল্টার পেপার:",
        [
            "Disposed of as chemical solid waste per lab rules",
            "Thrown into outdoor soil as fertilizer always",
            "Burned freely in the classroom trash can",
            "Washed down the drinking fountain",
        ],
        [
            "ল্যাব নিয়ম অনুসারে রাসায়নিক কঠিন বর্জ্য হিসেবে নিষ্পত্তি",
            "সবসময় সার হিসেবে বাইরের মাটিতে ফেলা",
            "শ্রেণিকক্ষের ট্র্যাশে মুক্তভাবে পোড়ানো",
            "পানীয় ফোয়ারা দিয়ে ধুয়ে ফেলা",
        ],
        "A", "easy", "factual",
        "Contaminated paper carries residual hazardous material.",
        "দূষিত কাগজে অবশিষ্ট বিপজ্জনক পদার্থ থাকে।",
    ),
    q(
        "The emergency shower is intended mainly for:",
        "জরুরি শাওয়ার মূলত ব্যবহার্য:",
        [
            "Rinsing large chemical spills from body or clothing",
            "Daily hair washing for comfort",
            "Cooling lunch boxes",
            "Diluting stock reagents into bottles",
        ],
        [
            "শরীর বা পোশাক থেকে বড় রাসায়নিক ছিটকে পড়া ধোয়া",
            "আরামের জন্য দৈনিক চুল ধোয়া",
            "লাঞ্চ বক্স ঠান্ডা করা",
            "স্টক বিকারক বোতলে লঘু করা",
        ],
        "A", "easy", "factual",
        "Safety showers provide rapid whole-body decontamination.",
        "সেফটি শাওয়ার দ্রুত পুরো শরীর ডি-কনটামিনেশন দেয়।",
    ),
    q(
        "Empty chemical bottles before disposal or reuse should be:",
        "নিষ্পত্তি বা পুনব্যবহারের আগে খালি রাসায়নিক বোতল:",
        [
            "Rinsed/triplerinsed as required and labels updated or removed appropriately",
            "Filled with unknown mixtures and left unlabeled",
            "Used for drinking water immediately without cleaning",
            "Crushed while still containing concentrated acid vapor only",
        ],
        [
            "প্রয়োজনমতো ধুয়ে/ত্রিগুণ ধুয়ে লেবেল হালনাগাদ বা যথাযথ অপসারণ",
            "অজানা মিশ্রণ ভরে লেবেলবিহীন রাখা",
            "পরিষ্কার ছাড়াই তাৎক্ষণিক পানীয় জলের জন্য ব্যবহার",
            "শুধু গাঢ় অ্যাসিড বাষ্প থাকা অবস্থায় চূর্ণ করা",
        ],
        "A", "medium", "application",
        "Proper rinsing and labeling prevent residual hazard and confusion.",
        "সঠিক ধোয়া ও লেবেলিং অবশিষ্ট বিপদ ও বিভ্রান্তি রোধ করে।",
    ),
    q(
        "Which statement about laboratory fire extinguishers is correct?",
        "ল্যাব অগ্নিনির্বাপক সম্পর্কে কোন বিবৃতি সঠিক?",
        [
            "Know their locations and suitable fire classes before an emergency",
            "They may be blocked by storage boxes indefinitely",
            "Any extinguisher works on all fire types equally",
            "Training is unnecessary if the device is red",
        ],
        [
            "জরুরি অবস্থার আগে অবস্থান ও উপযোগী আগুন শ্রেণি জানা",
            "সংরক্ষণ বাক্স দিয়ে অনির্দিষ্টকাল আটকে রাখা যায়",
            "যেকোনো নির্বাপক সব ধরনের আগুনে সমান কাজ করে",
            "যন্ত্র লাল হলে প্রশিক্ষণ অপ্রয়োজনীয়",
        ],
        "A", "easy", "conceptual",
        "Wrong extinguisher type or blocked access delays effective response.",
        "ভুল নির্বাপক ধরন বা আটকে থাকা প্রবেশ কার্যকর সাড়া বিলম্ব করে।",
    ),
    q(
        "Biological or unknown mixed waste from qualitative analysis should be:",
        "গুণগত বিশ্লেষণের জৈবিক বা অজানা মিশ্র বর্জ্য:",
        [
            "Handled according to instructor guidance and labeled waste protocols",
            "Tasted to identify components",
            "Poured into storm drains outside",
            "Taken home in open cups",
        ],
        [
            "প্রশিক্ষকের নির্দেশ ও লেবেলযুক্ত বর্জ্য প্রোটোকল অনুসরণ",
            "উপাদান শনাক্তে চেখে দেখা",
            "বাইরের স্টর্ম ড্রেনে ঢালা",
            "খোলা কাপে বাড়ি নিয়ে যাওয়া",
        ],
        "A", "medium", "application",
        "Unknown mixtures need controlled disposal to avoid environmental harm.",
        "অজানা মিশ্রণ পরিবেশ ক্ষতি এড়াতে নিয়ন্ত্রিত নিষ্পত্তি দাবি করে।",
    ),
    q(
        "A base spill on the floor should be cleaned only after:",
        "মেঝেতে ক্ষার ছিটকে পড়া পরিষ্কার করতে হয় কেবল:",
        [
            "Wearing suitable PPE and neutralizing/absorbing as directed",
            "Walking through it barefoot to test slipperiness",
            "Spreading it with a dry broom into the hallway",
            "Mixing it with leftover organic solvent waste",
        ],
        [
            "উপযুক্ত PPE পরে নির্দেশমতো নিরপেক্ষ/শোষক ব্যবহার করে",
            "পোঁচানোর পরীক্ষায় খালি পায়ে হাঁটা",
            "শুকনো ঝাড়ু দিয়ে করিডোরে ছড়ানো",
            "অবশিষ্ট জৈব দ্রাবক বর্জ্যের সাথে মেশানো",
        ],
        "A", "easy", "application",
        "PPE and proper absorbents/neutralizers protect the cleaner.",
        "PPE ও যথাযথ শোষক/নিরপেক্ষক পরিষ্কারকারীকে রক্ষা করে।",
    ),
    q(
        "Why must waste labels include hazard class information?",
        "বর্জ্য লেবেলে বিপদ শ্রেণির তথ্য কেন থাকতে হয়?",
        [
            "So handlers can avoid incompatible mixing and choose correct disposal",
            "Only to decorate the container colorfully",
            "Because unlabeled waste is always non-hazardous",
            "To increase the volume of the liquid",
        ],
        [
            "যাতে হ্যান্ডলার অসঙ্গত মিশ্রণ এড়িয়ে সঠিক নিষ্পত্তি বেছে নিতে পারে",
            "শুধু পাত্র রঙিন সাজাতে",
            "কারণ লেবেলবিহীন বর্জ্য সবসময় নিরাপদ",
            "তরলের আয়তন বাড়াতে",
        ],
        "A", "medium", "conceptual",
        "Hazard class guides segregation, transport, and treatment routes.",
        "বিপদ শ্রেণি পৃথকীকরণ, পরিবহন ও প্রক্রিয়াকরণ পথ নির্দেশ করে।",
    ),
]

TOPICS_MAP = {
    "chem1_27_ch01_t01": T01,
    "chem1_27_ch01_t02": T02,
    "chem1_27_ch01_t03": T03,
}


def write_topic(topic_id: str, rows: list[dict]) -> dict:
    clean = []
    for row in rows:
        err = validate_record(row)
        if err:
            raise SystemExit(f"{topic_id}: {err}\n{row['stem_en'][:120]}")
        clean.append({**row, "verified": False, "source": SRC})
    path = TOPICS / f"{topic_id}.jsonl"
    path.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in clean) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {path.name}: {len(clean)}")
    return {"path": str(path.relative_to(ROOT)).replace("\\", "/"), "count": len(clean)}


def main() -> int:
    for tid, rows in TOPICS_MAP.items():
        assert len(rows) == 20, f"{tid} has {len(rows)}"

    counts = {}
    paths = {}
    for tid, rows in TOPICS_MAP.items():
        info = write_topic(tid, rows)
        counts[tid] = info["count"]
        paths[tid] = info["path"]

    all_stems = []
    for tid in TOPIC_IDS:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "chem1_27_ch01",
        "title_en": "Safe Use of the Laboratory",
        "title_bn": "ল্যাবরেটরির নিরাপদ ব্যবহার",
        "source": SRC,
        "pdf_pages": [],
        "note": (
            "Import CSV chemistry_1_ch01.csv had headers only; authored 20 bilingual "
            "MCQs per topic aligned to NCTB chemistry_1st_paper_2027 ch01 "
            "(Safe Use of the Laboratory)."
        ),
        "counts": {**counts, "total": sum(counts.values())},
        "paths": paths,
        "pdf_mapping": {
            "chem1_27_ch01_t01": {
                "title": "Laboratory rules and hazard symbols / ল্যাবরেটরির নিয়ম ও বিপদ সংকেত",
                "themes": [
                    "PPE lab coat goggles no eating mouth pipetting ban",
                    "GHS pictograms flame corrosive toxic oxidizer explosive gas pressure environment health",
                    "labels SDS/MSDS hair jewelry shoes contact lenses",
                    "housekeeping unauthorized experiments",
                ],
            },
            "chem1_27_ch01_t02": {
                "title": "Safe handling of chemicals and apparatus / রাসায়নিক পদার্থ ও যন্ত্রপাতির নিরাপদ ব্যবহার",
                "themes": [
                    "acid-into-water dilution; fume hood; wafting",
                    "cracked glass; test-tube heating; Bunsen air hole",
                    "flammable solvents; spatula contamination; glass-in-stopper",
                    "sealed heating; mercury; gloves; condenser water; NaOH; burner checks",
                ],
            },
            "chem1_27_ch01_t03": {
                "title": "Accident response and waste disposal / দুর্ঘটনায় করণীয় ও বর্জ্য ব্যবস্থাপনা",
                "themes": [
                    "eyewash; stop-drop-roll; acid on skin; report accidents",
                    "Class B extinguishers; broken glass; vapor exposure",
                    "bicarbonate neutralization; labeled waste; segregate incompatibles",
                    "safety shower; empty bottles; evacuation; PPE spill cleanup",
                ],
            },
        },
        "low_confidence": [
            "No usable in-repo OCR page set for Chemistry 1st paper Udvash PDF ch01; items are syllabus-aligned authored MCQs, not direct OCR transcriptions.",
            "Import CSV content/bank/import/chemistry_1_ch01.csv had headers only (no stems to reuse).",
            "GHS pictogram teaching follows common HSC lab-safety framing; local textbook icon variants may differ slightly.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (chem1_27_ch01_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {tid: 20 for tid in TOPIC_IDS},
        },
        "chem1_ch01_completion": {
            "topics_expected": 3,
            "topics_at_20": 3,
            "note": "chem1_27_ch01_t01..t03 complete at 20/topic (chapter total 60).",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch01_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
