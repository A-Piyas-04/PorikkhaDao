#!/usr/bin/env python3
"""Seed Chemistry 1st Paper Ch5 bilingual MCQs (Applied Chemistry).

Import CSV chemistry_1_ch05.csv had headers only; authored 20 bilingual MCQs
per topic aligned to NCTB chemistry_1st_paper_2027 ch05.
Writes chem1_27_ch05_t01..t04 under content/bank/topics/.
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
    "chemistry p1 ch05; curated bilingual"
)

TOPIC_IDS = [f"chem1_27_ch05_t{i:02d}" for i in range(1, 5)]


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    if not re.search(r"[A-Za-z]", en):
        if "%" in en:
            en = f"about {en}"
        else:
            en = f"value {en}"
        if not re.search(r"[ঀ-৿]", bn):
            bn = f"মান {bn}"
        elif en.startswith("about ") and "শতাংশ" not in bn and "%" in bn:
            bn = f"প্রায় {bn}"
    if not re.search(r"[ঀ-৿]", bn) and re.search(r"[A-Za-z]{3,}", bn):
        bn = f"মান {bn}"
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


# --- t01: Food chemistry and preservation ---
T01 = [
    q(
        "The main role of food preservatives is to:",
        "খাদ্য সংরক্ষকের প্রধান ভূমিকা:",
        ["Increase nuclear radiation", "Slow spoilage by microbes or oxidation", "Remove all nutrients", "Make food radioactive"],
        ["নিউক্লিয়ার বিকিরণ বাড়ানো", "জীবাণু বা জারণ দ্বারা নষ্ট হওয়া মন্থর করা", "সব পুষ্টি অপসারণ", "খাদ্য তেজস্ক্রিয় করা"],
        "B", "easy", "factual",
        "Preservatives extend shelf life by inhibiting microbes or oxidation.",
        "সংরক্ষক জীবাণু/জারণ প্রতিরোধ করে সংরক্ষণকাল বাড়ায়।",
    ),
    q(
        "Refrigeration preserves food mainly by:",
        "রেফ্রিজারেশন খাদ্য সংরক্ষণ করে প্রধানত:",
        ["Killing all enzymes permanently at once", "Slowing microbial growth and enzyme activity", "Adding strong acids only", "Removing all water instantly"],
        ["একবারে সব এনজাইম স্থায়ী ধ্বংস", "জীবাণু বৃদ্ধি ও এনজাইম ক্রিয়া মন্থর করা", "শুধু সবল অম্ল যোগ", "তাৎক্ষণিক সব পানি অপসারণ"],
        "B", "easy", "conceptual",
        "Low temperature slows metabolism of spoilage organisms.",
        "নিম্ন তাপমাত্রা নষ্টকারী জীবাণুর বিপাক মন্থর করে।",
    ),
    q(
        "Salting fish or meat preserves them primarily because:",
        "মাছ বা মাংস লবণাক্ত করে সংরক্ষণ প্রধানত কারণ:",
        ["Salt adds vitamins", "High osmotic pressure dehydrates microbes", "Salt raises temperature", "Salt creates anaerobic vacuum automatically"],
        ["লবণ ভিটামিন যোগ করে", "উচ্চ অসমোটিক চাপে জীবাণু নিরুদিত হয়", "লবণ তাপমাত্রা বাড়ায়", "লবণ স্বয়ংক্রিয় শূন্য অ্যানেরোবিক তৈরি করে"],
        "B", "medium", "conceptual",
        "Hypertonic salt draws water out of microbial cells.",
        "অতিঅসমোটিক লবণ জীবাণু কোষ থেকে পানি টেনে নেয়।",
    ),
    q(
        "Which gas is commonly used in modified-atmosphere packaging to inhibit aerobic spoilage?",
        "বায়বীয় নষ্ট রোধে পরিবর্তিত-বায়ুমণ্ডল প্যাকেজিংয়ে সাধারণ কোন গ্যাস?",
        ["Pure O2 at high pressure always", "CO2 or N2 (reducing oxygen)", "Chlorine gas freely mixed in food", "Ozone pumped into every home fridge"],
        ["সবসময় উচ্চ চাপে বিশুদ্ধ O2", "CO2 বা N2 (অক্সিজেন কমানো)", "খাদ্যে মুক্ত ক্লোরিন গ্যাস", "প্রতি ঘরে ওজোন পাম্প"],
        "B", "medium", "application",
        "Lowering O2 and raising CO2/N2 slows aerobic microbes and oxidation.",
        "O2 কমিয়ে CO2/N2 বাড়ালে বায়বীয় জীবাণু ও জারণ মন্থর হয়।",
    ),
    q(
        "Pasteurization of milk typically aims to:",
        "দুধের পাস্তুরাইজেশনের লক্ষ্য সাধারণত:",
        ["Completely sterilize and destroy all nutrients", "Kill pathogenic microbes without boiling away quality", "Add artificial color only", "Freeze milk solid"],
        ["সম্পূর্ণ জীবাণুমুক্ত ও সব পুষ্টি ধ্বংস", "গুণমান নষ্ট না করে রোগজীবাণু মারা", "শুধু কৃত্রিম রঙ যোগ", "দুধ কঠিন বরফ করা"],
        "B", "easy", "factual",
        "Controlled heating reduces pathogens while retaining nutritional quality.",
        "নিয়ন্ত্রিত উত্তাপে পুষ্টি রেখে রোগজীবাণু কমানো হয়।",
    ),
    q(
        "Antioxidants in food help by:",
        "খাদ্যে অ্যান্টিঅক্সিডেন্ট সাহায্য করে:",
        ["Speeding rancidity", "Slowing oxidative spoilage of fats and oils", "Increasing microbial growth", "Removing all proteins"],
        ["তেল নষ্ট দ্রুত করা", "চর্বি/তেলের জারণজনিত নষ্ট মন্থর করা", "জীবাণু বৃদ্ধি বাড়ানো", "সব প্রোটিন অপসারণ"],
        "B", "easy", "conceptual",
        "They interrupt free-radical oxidation that causes rancidity.",
        "র্যান্সিডিটির মুক্ত র্যাডিক্যাল জারণ তারা বাধা দেয়।",
    ),
    q(
        "Vitamin C (ascorbic acid) in foods can act as:",
        "খাদ্যে ভিটামিন C (অ্যাসকরবিক অম্ল) কাজ করতে পারে:",
        ["Only a toxic heavy metal", "An antioxidant and nutrient", "A plasticizer for packaging only", "A nuclear fuel"],
        ["শুধু বিষাক্ত ভারী ধাতু", "অ্যান্টিঅক্সিডেন্ট ও পুষ্টি", "শুধু প্যাকেজিং প্লাস্টিসাইজার", "নিউক্লিয়ার জ্বালানি"],
        "B", "easy", "factual",
        "Ascorbic acid protects against oxidation and is an essential vitamin.",
        "অ্যাসকরবিক অম্ল জারণ রোধ করে ও অত্যাবশ্যক ভিটামিন।",
    ),
    q(
        "Drying fruits preserves them mainly by:",
        "ফল শুকিয়ে সংরক্ষণ প্রধানত:",
        ["Increasing water activity for microbes", "Reducing water available for microbial growth", "Adding live bacteria", "Raising pH above 14"],
        ["জীবাণুর জন্য পানি অ্যাক্টিভিটি বাড়ানো", "জীবাণু বৃদ্ধির পানি কমানো", "জীবিত ব্যাকটেরিয়া যোগ", "pH ১৪ এর উপরে তোলা"],
        "B", "easy", "conceptual",
        "Low moisture limits bacterial and fungal growth.",
        "কম আর্দ্রতা ব্যাকটেরিয়া ও ছত্রাক বৃদ্ধি সীমিত করে।",
    ),
    q(
        "Which acid is commonly associated with vinegar used in pickling?",
        "আচার তৈরিতে ব্যবহৃত ভিনেগারের সাথে সাধারণ কোন অম্ল?",
        ["Hydrochloric acid", "Acetic acid", "Nitric acid", "Sulfuric acid"],
        ["হাইড্রোক্লোরিক অম্ল", "অ্যাসিটিক অম্ল", "নাইট্রিক অম্ল", "সালফিউরিক অম্ল"],
        "B", "easy", "factual",
        "Vinegar is dilute acetic acid; low pH inhibits many spoilage organisms.",
        "ভিনেগার তরল অ্যাসিটিক অম্ল; নিম্ন pH নষ্টকারী জীবাণু রোধ করে।",
    ),
    q(
        "Rancidity of oils is mainly due to:",
        "তেলের র্যান্সিডিটি প্রধানত কারণ:",
        ["Oxidation or hydrolysis of fats", "Addition of sugar only", "Freezing at −80 °C", "Dissolving in pure helium"],
        ["চর্বির জারণ বা জলবিশ্লেষণ", "শুধু চিনি যোগ", "−৮০ °C তে হিমায়ন", "বিশুদ্ধ হিলিয়ামে দ্রবীভূতকরণ"],
        "A", "medium", "conceptual",
        "Oxidative rancidity yields off-flavors from lipid peroxidation.",
        "জারণজাত র্যান্সিডিটিতে লিপিড পারঅক্সিডেশন থেকে খারাপ গন্ধ আসে।",
    ),
    q(
        "Sodium benzoate is used in acidic foods as a:",
        "অম্লীয় খাদ্যে সোডিয়াম বেনজোয়েট ব্যবহৃত হয়:",
        ["Sweetener only", "Antimicrobial preservative", "Bleaching agent for flour only", "Metal catalyst"],
        ["শুধু মিষ্টিকারক", "অ্যান্টিমাইক্রোবিয়াল সংরক্ষক", "শুধু ময়দার ব্লিচ", "ধাতব অনুঘটক"],
        "B", "medium", "factual",
        "Benzoic acid/benzoate inhibits yeasts and molds in acidic media.",
        "অম্লীয় মাধ্যমে বেনজোয়িক অম্ল/বেনজোয়েট ইস্ট ও ছত্রাক রোধ করে।",
    ),
    q(
        "Carbohydrates in food primarily provide:",
        "খাদ্যে কার্বোহাইড্রেট প্রধানত সরবরাহ করে:",
        ["Structural steel", "Energy (and some fiber)", "Only heavy metals", "Inert gases"],
        ["কাঠামোগত ইস্পাত", "শক্তি (ও কিছু আঁশ)", "শুধু ভারী ধাতু", "নিষ্ক্রিয় গ্যাস"],
        "B", "easy", "factual",
        "Sugars and starches are major dietary energy sources.",
        "শর্করা ও স্টার্চ প্রধান খাদ্যশক্তি উৎস।",
    ),
    q(
        "Proteins in the diet are important as sources of:",
        "খাদ্যে প্রোটিন গুরুত্বপূর্ণ উৎস হিসেবে:",
        ["Only cellulose", "Amino acids for body tissues and enzymes", "Only sodium chloride", "Helium"],
        ["শুধু সেলুলোজ", "দেহ কলা ও এনজাইমের অ্যামিনো অম্ল", "শুধু সোডিয়াম ক্লোরাইড", "হিলিয়াম"],
        "B", "easy", "factual",
        "Dietary proteins supply essential and non-essential amino acids.",
        "খাদ্য প্রোটিন অত্যাবশ্যক ও অনাত্যাবশ্যক অ্যামিনো অম্ল দেয়।",
    ),
    q(
        "Maillard browning during cooking involves reaction between:",
        "রান্নাকালে ম্যেলার্ড বাদামি রঙে বিক্রিয়া হয়:",
        ["Only pure metals", "Reducing sugars and amino compounds", "Only noble gases", "Sand and glass"],
        ["শুধু বিশুদ্ধ ধাতু", "রিডিউসিং শর্করা ও অ্যামিনো যৌগ", "শুধু নিষ্ক্রিয় গ্যাস", "বালি ও কাচ"],
        "B", "hard", "conceptual",
        "Amino–carbonyl reactions create browned flavors and colors.",
        "অ্যামিনো–কার্বনিল বিক্রিয়ায় বাদামি স্বাদ ও রঙ তৈরি হয়।",
    ),
    q(
        "Canning preserves food by:",
        "ক্যানিং খাদ্য সংরক্ষণ করে:",
        ["Leaving containers open to air", "Heat sterilization and sealing to exclude microbes", "Adding live pathogens", "Only painting labels"],
        ["পাত্র বাতাসে খোলা রাখা", "তাপ জীবাণুমুক্তকরণ ও সিল করে জীবাণু বন্ধ", "জীবিত রোগজীবাণু যোগ", "শুধু লেবেল রঙ"],
        "B", "easy", "application",
        "Commercial sterilization plus hermetic seals prevent recontamination.",
        "বাণিজ্যিক জীবাণুমুক্তকরণ ও বায়ুরোধী সিল পুনঃদূষণ রোধ করে।",
    ),
    q(
        "Which statement about food additives is correct?",
        "খাদ্য সংযোজক সম্পর্কে কোন বিবৃতি সঠিক?",
        ["All additives are illegally toxic always", "Approved additives serve roles like preservation, color, or flavor within limits", "Additives replace the need for hygiene", "Additives are only radioactive isotopes"],
        ["সব সংযোজক সবসময় অবৈধ বিষ", "অনুমোদিত সংযোজক সীমার মধ্যে সংরক্ষণ/রঙ/স্বাদ কাজে লাগে", "সংযোজক স্বাস্থ্যবিধির প্রয়োজন সরায়", "সংযোজক শুধু তেজস্ক্রিয় আইসোটোপ"],
        "B", "medium", "conceptual",
        "Regulated additives improve quality/safety when used as permitted.",
        "নিয়ন্ত্রিত সংযোজক অনুমোদিত ব্যবহারে গুণমান/নিরাপত্তা বাড়ায়।",
    ),
    q(
        "Fermentation of milk to yogurt involves mainly:",
        "দই তৈরির দুধের ফার্মেন্টেশনে প্রধানত:",
        ["Lactic acid bacteria converting lactose to lactic acid", "Nuclear fission of calcium", "Only adding motor oil", "Complete removal of all microbes forever"],
        ["ল্যাকটিক অম্ল ব্যাকটেরিয়া ল্যাকটোজকে ল্যাকটিক অম্লে রূপান্তর", "ক্যালসিয়ামের নিউক্লিয়ার ফিশন", "শুধু মোটর অয়েল যোগ", "চিরকাল সব জীবাণু সম্পূর্ণ অপসারণ"],
        "A", "medium", "application",
        "Acidification coagulates proteins and inhibits many pathogens.",
        "অম্লীকরণে প্রোটিন জমাট বাঁধে ও অনেক রোগজীবাণু রোধ হয়।",
    ),
    q(
        "Sulfur dioxide / sulfites in dried fruits mainly act as:",
        "শুকনো ফলে সালফার ডাইঅক্সাইড/সালফাইট প্রধানত কাজ করে:",
        ["Flavor enhancers only with no other role", "Antimicrobial and anti-browning agents", "Sources of protein", "Emulsifiers for metals"],
        ["অন্য ভূমিকাহীন শুধু স্বাদবর্ধক", "অ্যান্টিমাইক্রোবিয়াল ও বাদামি রোধক", "প্রোটিনের উৎস", "ধাতুর ইমালসিফায়ার"],
        "B", "medium", "factual",
        "SO2 inhibits microbes and enzymatic browning; some people are sensitive.",
        "SO2 জীবাণু ও এনজাইমজনিত বাদামি রোধ করে; কেউ কেউ সংবেদনশীল।",
    ),
    q(
        "Emulsifiers in processed foods help to:",
        "প্রক্রিয়াজাত খাদ্যে ইমালসিফায়ার সাহায্য করে:",
        ["Separate oil and water permanently into layers always", "Stabilize mixtures of immiscible liquids like oil and water", "Remove all calories", "Create pure crystals of NaCl only"],
        ["তেল ও পানি সবসময় স্থায়ী স্তরে আলাদা", "তেল–পানির মতো অমিশ্র তরল মিশ্রণ স্থিতিশীল করা", "সব ক্যালোরি অপসারণ", "শুধু বিশুদ্ধ NaCl স্ফটিক"],
        "B", "medium", "conceptual",
        "Molecules with polar and nonpolar parts stabilize emulsions (e.g., mayonnaise).",
        "পোলার ও অপোলার অংশযুক্ত অণু ইমালশন স্থিতিশীল করে (যেমন মেয়োনিজ)।",
    ),
    q(
        "Why must refrigerated cooked food still be handled hygienically?",
        "রেফ্রিজারেটেড রান্না করা খাবারও স্বাস্থ্যসম্মতভাবে ব্যবহার করতে হয় কেন?",
        ["Cold kills every microbe instantly forever", "Some microbes survive and can grow if temperature abuse occurs", "Refrigerators sterilize packaging chemically", "Hygiene is unrelated to food safety"],
        ["ঠান্ডা সব জীবাণু তাৎক্ষণিক চিরকাল মারে", "কিছু জীবাণু বেঁচে থাকে ও তাপমাত্রা অপব্যবহারে বাড়তে পারে", "রেফ্রিজারেটর রাসায়নিকভাবে প্যাকেজ জীবাণুমুক্ত করে", "স্বাস্থ্যবিধি খাদ্য নিরাপত্তার সাথে অসংযুক্ত"],
        "B", "easy", "application",
        "Chilling slows but does not eliminate all pathogens; cross-contamination remains a risk.",
        "ঠান্ডা সব রোগজীবাণু ধ্বংস করে না; ক্রস-দূষণ ঝুঁকি থাকে।",
    ),
]

# --- t02: Cleaning agents and everyday chemicals ---
T02 = [
    q(
        "Soap molecules clean grease mainly because they are:",
        "সাবান অণু গ্রিজ পরিষ্কার করে প্রধানত কারণ তারা:",
        ["Completely nonpolar only", "Amphiphilic — hydrophobic tail and hydrophilic head", "Pure metals", "Strong oxidizing gases"],
        ["শুধু সম্পূর্ণ অপোলার", "অ্যাম্ফিফিলিক — হাইড্রোফোবিক লেজ ও হাইড্রোফিলিক মাথা", "বিশুদ্ধ ধাতু", "সবল জারক গ্যাস"],
        "B", "easy", "conceptual",
        "Tails dissolve in oil; heads face water, forming micelles that rinse away dirt.",
        "লেজ তেলে দ্রবীভূত; মাথা পানির দিকে — মাইসেল গঠন করে ময়লা ধুয়ে যায়।",
    ),
    q(
        "Hard water reduces soap effectiveness because:",
        "কঠিন পানি সাবানের কার্যকারিতা কমায় কারণ:",
        ["Ca2+/Mg2+ form insoluble scum with soap", "Hard water is always boiling", "Soap becomes radioactive", "Air pressure falls to zero"],
        ["Ca2+/Mg2+ সাবানের সাথে অদ্রবণীয় স্কাম গঠন করে", "কঠিন পানি সবসময় ফুটন্ত", "সাবান তেজস্ক্রিয় হয়", "বায়ুচাপ শূন্য হয়"],
        "A", "easy", "conceptual",
        "Calcium and magnesium salts precipitate soap as scum.",
        "ক্যালসিয়াম ও ম্যাগনেসিয়াম লবণ সাবানকে স্কাম হিসেবে অধঃক্ষিপ্ত করে।",
    ),
    q(
        "Synthetic detergents often work better than soap in hard water because:",
        "কঠিন পানিতে সিন্থেটিক ডিটারজেন্ট সাবানের চেয়ে ভালো কাজ করে প্রায়ই কারণ:",
        ["They never dissolve", "Their calcium/magnesium salts are usually more soluble", "They contain only sand", "They raise hardness further"],
        ["তারা কখনো দ্রবীভূত হয় না", "তাদের ক্যালসিয়াম/ম্যাগনেসিয়াম লবণ সাধারণত অধিক দ্রবণীয়", "শুধু বালি থাকে", "কঠোরতা আরও বাড়ায়"],
        "B", "medium", "conceptual",
        "Detergent anions often do not form heavy scum with hardness ions.",
        "ডিটারজেন্ট অ্যানায়ন প্রায়ই কঠোরতা আয়নের সাথে ভারী স্কাম গঠন করে না।",
    ),
    q(
        "Bleaching powder used for whitening/disinfecting is chemically related to:",
        "সাদা/জীবাণুনাশনে ব্যবহৃত ব্লিচিং পাউডার রাসায়নিকভাবে সম্পর্কিত:",
        ["Calcium hypochlorite (approx.)", "Pure gold", "Sodium metal only", "Graphite electrodes only"],
        ["ক্যালসিয়াম হাইপোক্লোরাইট (প্রায়)", "বিশুদ্ধ সোনা", "শুধু সোডিয়াম ধাতু", "শুধু গ্রাফাইট ইলেকট্রোড"],
        "A", "medium", "factual",
        "Bleaching powder releases chlorine/hypochlorite that oxidize stains and microbes.",
        "ব্লিচিং পাউডার ক্লোরিন/হাইপোক্লোরাইট মুক্ত করে দাগ ও জীবাণু জারিত করে।",
    ),
    q(
        "Household ammonia solution is used as a cleaner mainly because it is:",
        "গৃহস্থালি অ্যামোনিয়া দ্রবণ পরিষ্কারক হিসেবে ব্যবহৃত প্রধানত কারণ এটি:",
        ["A strong acid", "A basic solution that helps dissolve greasy soils", "An inert noble gas", "A solid metal alloy"],
        ["সবল অম্ল", "ক্ষারীয় দ্রবণ যা গ্রিজি ময়লা দ্রবীভূত করতে সাহায্য করে", "নিষ্ক্রিয় নিষ্ক্রিয় গ্যাস", "কঠিন ধাতব সংকর"],
        "B", "easy", "application",
        "Aqueous NH3 is a weak base useful on some glass and grease films.",
        "জলীয় NH3 দুর্বল ক্ষার; কিছু কাচ ও গ্রিজ ফিল্মে কাজে লাগে।",
    ),
    q(
        "Baking soda used in cleaning and cooking is:",
        "পরিষ্কার ও রান্নায় ব্যবহৃত বেকিং সোডা হলো:",
        ["NaHCO3", "NaOH", "H2SO4", "KMnO4"],
        ["NaHCO3", "NaOH", "H2SO4", "KMnO4"],
        "A", "easy", "factual",
        "Sodium hydrogen carbonate is a mild base and CO2 source with acids.",
        "সোডিয়াম হাইড্রোজেন কার্বনেট মৃদু ক্ষার; অম্লের সাথে CO2 দেয়।",
    ),
    q(
        "Washing soda is primarily:",
        "ওয়াশিং সোডা প্রধানত:",
        ["Na2CO3·10H2O (hydrated sodium carbonate)", "NaCl only", "CaO only", "SiO2 sand"],
        ["Na2CO3·10H2O (জলীয় সোডিয়াম কার্বনেট)", "শুধু NaCl", "শুধু CaO", "SiO2 বালি"],
        "A", "easy", "factual",
        "Washing soda softens water and aids alkaline cleaning.",
        "ওয়াশিং সোডা পানি নরম করে ও ক্ষারীয় পরিষ্কারে সাহায্য করে।",
    ),
    q(
        "A surfactant lowers:",
        "সারফ্যাক্ট্যান্ট কমায়:",
        ["Nuclear binding energy", "Surface tension of water, aiding wetting and cleaning", "Only the mass of dirt", "Atmospheric O2 permanently"],
        ["নিউক্লিয়ার বন্ধন শক্তি", "পানির পৃষ্ঠটান; ভেজানো ও পরিষ্কার সহজ করে", "শুধু ময়লার ভর", "স্থায়ীভাবে বায়ুমণ্ডলীয় O2"],
        "B", "medium", "conceptual",
        "Lower surface tension lets water spread into fabrics and soils.",
        "কম পৃষ্ঠটানে পানি কাপড় ও ময়লায় ছড়িয়ে পড়ে।",
    ),
    q(
        "Toilet cleaners that contain strong acids should NOT be mixed with bleach because:",
        "সবল অম্লযুক্ত টয়লেট ক্লিনার ব্লিচের সাথে মেশানো উচিত নয় কারণ:",
        ["They form harmless sugar", "Dangerous chlorine gas can be released", "They create edible salt only", "Nothing happens ever"],
        ["নিরাপদ চিনি গঠিত হয়", "বিপজ্জনক ক্লোরিন গ্যাস মুক্ত হতে পারে", "শুধু খাদ্যযোগ্য লবণ তৈরি হয়", "কখনো কিছু হয় না"],
        "B", "medium", "application",
        "Acid + hypochlorite → Cl2 gas, which is toxic.",
        "অম্ল + হাইপোক্লোরাইট → বিষাক্ত Cl2 গ্যাস।",
    ),
    q(
        "Disinfectants differ from antiseptics mainly in that disinfectants are:",
        "জীবাণুনাশক ও অ্যান্টিসেপটিকের প্রধান পার্থক্য — জীবাণুনাশক:",
        ["Always swallowed as vitamins", "Generally for inanimate surfaces; antiseptics for living tissue", "Weaker than water always", "Only used in space"],
        ["সবসময় ভিটামিন হিসেবে গিলে খাওয়া", "সাধারণত নির্জীব তলে; অ্যান্টিসেপটিক জীবন্ত কলায়", "সবসময় পানির চেয়ে দুর্বল", "শুধু মহাকাশে"],
        "B", "medium", "conceptual",
        "Concentration and intended use distinguish the two categories.",
        "ঘনমাত্রা ও ব্যবহারের উদ্দেশ্য দুই শ্রেণি আলাদা করে।",
    ),
    q(
        "Ethanol or isopropanol in hand sanitizers acts mainly as:",
        "হ্যান্ড স্যানিটাইজারে ইথানল বা আইসোপ্রোপানল প্রধানত কাজ করে:",
        ["A nutrient broth for bacteria", "An antimicrobial agent denaturing proteins", "A source of Ca2+ hardness", "A plastic explosive"],
        ["ব্যাকটেরিয়ার পুষ্টি ব্রথ", "প্রোটিন বিকৃতকারী অ্যান্টিমাইক্রোবিয়াল", "Ca2+ কঠোরতার উৎস", "প্লাস্টিক বিস্ফোরক"],
        "B", "easy", "application",
        "Alcohols disrupt microbial membranes and proteins at proper concentration.",
        "উপযুক্ত ঘনমাত্রায় অ্যালকোহল জীবাণুর ঝিল্লি ও প্রোটিন নষ্ট করে।",
    ),
    q(
        "Detergent builders (e.g., phosphates historically) were added to:",
        "ডিটারজেন্ট বিল্ডার (ঐতিহাসিকভাবে ফসফেট) যোগ করা হতো:",
        ["Increase water hardness", "Bind hardness ions and improve cleaning", "Remove surfactant entirely", "Make water radioactive"],
        ["পানির কঠোরতা বাড়াতে", "কঠোরতা আয়ন বাঁধতে ও পরিষ্কার উন্নত করতে", "সারফ্যাক্ট্যান্ট সম্পূর্ণ সরাতে", "পানি তেজস্ক্রিয় করতে"],
        "B", "hard", "factual",
        "Builders sequester Ca2+/Mg2+; environmental concerns led to alternatives.",
        "বিল্ডার Ca2+/Mg2+ আবদ্ধ করে; পরিবেশ উদ্বেগে বিকল্প আসে।",
    ),
    q(
        "Abrasive cleaners remove dirt primarily by:",
        "অ্যাব্রেসিভ ক্লিনার ময়লা সরায় প্রধানত:",
        ["Only chemical dissolution always", "Mechanical scouring with fine particles", "Nuclear fusion", "Magnetic levitation"],
        ["সবসময় শুধু রাসায়নিক দ্রবীভূতকরণ", "সূক্ষ্ম কণার যান্ত্রিক ঘষা", "নিউক্লিয়ার ফিউশন", "চৌম্বক ভাসমানতা"],
        "B", "easy", "conceptual",
        "Fine silica or similar powders scrub deposits from surfaces.",
        "সূক্ষ্ম সিলিকা বা অনুরূপ গুঁড়ো তল থেকে আস্তরণ ঘষে তোলে।",
    ),
    q(
        "Which everyday chemical is commonly used as a mild antiseptic in dilute solution?",
        "তরল দ্রবণে মৃদু অ্যান্টিসেপটিক হিসেবে সাধারণ কোন দৈনন্দিন রাসায়নিক?",
        ["Concentrated H2SO4", "Hydrogen peroxide (dilute)", "Liquid mercury", "Pure sodium metal"],
        ["গাঢ় H2SO4", "হাইড্রোজেন পারঅক্সাইড (তরল)", "তরল পারদ", "বিশুদ্ধ সোডিয়াম ধাতু"],
        "B", "easy", "application",
        "Dilute H2O2 releases oxygen and helps clean minor wounds/surfaces.",
        "তরল H2O2 অক্সিজেন মুক্ত করে ছোট ক্ষত/তল পরিষ্কারে সাহায্য করে।",
    ),
    q(
        "Limescale in kettles is mainly:",
        "কেটলিতে লাইমস্কেল প্রধানত:",
        ["Calcium carbonate deposits from hard water", "Pure sugar crystals", "Metallic sodium", "Frozen nitrogen"],
        ["কঠিন পানি থেকে ক্যালসিয়াম কার্বনেট আস্তরণ", "বিশুদ্ধ চিনি স্ফটিক", "ধাতব সোডিয়াম", "হিমায়িত নাইট্রোজেন"],
        "A", "easy", "factual",
        "Heating hard water precipitates CaCO3 scale.",
        "কঠিন পানি গরম করলে CaCO3 স্কেল অধঃক্ষিপ্ত হয়।",
    ),
    q(
        "Vinegar can help remove limescale because it:",
        "ভিনেগার লাইমস্কেল সরাতে সাহায্য করে কারণ এটি:",
        ["Is a strong base", "Contains acetic acid that reacts with carbonate scale", "Is pure hydrocarbon oil", "Increases Ca2+ concentration"],
        ["সবল ক্ষার", "অ্যাসিটিক অম্ল কার্বনেট স্কেলের সাথে বিক্রিয়া করে", "বিশুদ্ধ হাইড্রোকার্বন তেল", "Ca2+ ঘনমাত্রা বাড়ায়"],
        "B", "easy", "application",
        "Acid dissolves CaCO3, releasing CO2 and soluble salts.",
        "অম্ল CaCO3 দ্রবীভূত করে CO2 ও দ্রবণীয় লবণ দেয়।",
    ),
    q(
        "Optical brighteners in detergents:",
        "ডিটারজেন্টে অপটিক্যাল ব্রাইটনার:",
        ["Remove dirt by abrasion only", "Absorb UV and emit blue light making fabrics look whiter", "Are sources of hardness", "Neutralize all acids in laundry"],
        ["শুধু ঘষা দিয়ে ময়লা সরায়", "UV শোষণ করে নীল আলো নির্গত করে কাপড় সাদা দেখায়", "কঠোরতার উৎস", "লন্ড্রির সব অম্ল প্রশমিত করে"],
        "B", "hard", "conceptual",
        "Fluorescent whitening agents mask yellowing visually.",
        "ফ্লুরোসেন্ট হোয়াইটেনার দৃশ্যত হলুদ ভাব ঢাকে।",
    ),
    q(
        "Sodium hydroxide (caustic soda) in drain cleaners is hazardous because it is:",
        "ড্রেন ক্লিনারে সোডিয়াম হাইড্রোক্সাইড (কস্টিক সোডা) বিপজ্জনক কারণ এটি:",
        ["A mild sugar", "A strongly corrosive base", "An inert gas", "A vitamin supplement"],
        ["মৃদু চিনি", "সবল ক্ষয়কারী ক্ষার", "নিষ্ক্রিয় গ্যাস", "ভিটামিন সম্পূরক"],
        "B", "easy", "application",
        "Concentrated NaOH saponifies grease but burns skin and eyes.",
        "গাঢ় NaOH গ্রিজ সাবানায়িত করে কিন্তু ত্বক ও চোখ পোড়ায়।",
    ),
    q(
        "Micelles in soapy water are:",
        "সাবান পানিতে মাইসেল হলো:",
        ["Single Na+ ions only", "Aggregates of soap molecules with hydrophobic interiors", "Pieces of glass", "Solid metal crystals"],
        ["শুধু একক Na+ আয়ন", "হাইড্রোফোবিক অভ্যন্তরসহ সাবান অণুর সমষ্টি", "কাচের টুকরো", "কঠিন ধাতব স্ফটিক"],
        "B", "medium", "conceptual",
        "Grease dissolves in micelle cores and stays suspended in water.",
        "গ্রিজ মাইসেল কেন্দ্রে দ্রবীভূত হয়ে পানিতে ঝুলে থাকে।",
    ),
    q(
        "Which practice is safest when using household cleaners?",
        "গৃহস্থালি ক্লিনার ব্যবহারে কোন অভ্যাস সবচেয়ে নিরাপদ?",
        ["Mixing bleach with acid toilet cleaner for extra power", "Reading labels, ventilating, and never mixing incompatible chemicals", "Storing cleaners in drink bottles", "Using undiluted industrial NaOH on bare hands"],
        ["অতিরিক্ত শক্তির জন্য ব্লিচ ও অম্ল টয়লেট ক্লিনার মেশানো", "লেবেল পড়া, বায়ুচলাচল, অসামঞ্জস্য রাসায়নিক না মেশানো", "পানীয় বোতলে ক্লিনার রাখা", "খালি হাতে অতরল শিল্প NaOH"],
        "B", "easy", "application",
        "Label instructions and avoiding dangerous mixtures prevent poisoning and burns.",
        "লেবেল মেনে বিপজ্জনক মিশ্রণ এড়ালে বিষক্রিয়া ও পোড়া রোধ হয়।",
    ),
]

# --- t03: Industrial materials ---
T03 = [
    q(
        "Cement hardens mainly by:",
        "সিমেন্ট শক্ত হয় প্রধানত:",
        ["Simple melting of sand only", "Hydration reactions with water forming interlocking solids", "Dissolving completely in oil", "Nuclear decay of calcium"],
        ["শুধু বালির সরল গলন", "পানির সাথে হাইড্রেশন বিক্রিয়ায় আন্তঃবন্ধন কঠিন গঠন", "তেলে সম্পূর্ণ দ্রবীভূতকরণ", "ক্যালসিয়ামের নিউক্লিয়ার ক্ষয়"],
        "B", "easy", "conceptual",
        "Cement compounds hydrate to give a rigid set mass (concrete with aggregate).",
        "সিমেন্ট যৌগ হাইড্রেট হয়ে দৃঢ় ভর দেয় (অ্যাগ্রিগেটসহ কংক্রিট)।",
    ),
    q(
        "The main raw materials for ordinary Portland cement include:",
        "সাধারণ পোর্টল্যান্ড সিমেন্টের প্রধান কাঁচামাল:",
        ["Only pure gold and silver", "Limestone and clay (plus corrections)", "Only helium gas", "Only table sugar"],
        ["শুধু বিশুদ্ধ সোনা ও রূপা", "চুনাপাথর ও কাদামাটি (সংশোধনসহ)", "শুধু হিলিয়াম গ্যাস", "শুধু টেবিল চিনি"],
        "B", "easy", "factual",
        "CaO from limestone and silica/alumina from clay are key.",
        "চুনাপাথর থেকে CaO ও কাদা থেকে সিলিকা/অ্যালুমিনা মূল উপাদান।",
    ),
    q(
        "Glass is best described as:",
        "কাচকে সবচেয়ে ভালো বর্ণনা:",
        ["A crystalline metal", "An amorphous (non-crystalline) solid, often silica-based", "A pure gas at room temperature", "A living polymer only"],
        ["স্ফটিকাকার ধাতু", "অনিয়তাকার (অস্ফটিক) কঠিন, প্রায়ই সিলিকাভিত্তিক", "কক্ষতাপমাত্রায় বিশুদ্ধ গ্যাস", "শুধু জীবিত পলিমার"],
        "B", "easy", "conceptual",
        "Silicate glasses lack long-range crystal order.",
        "সিলিকেট কাচে দীর্ঘ-পরিসর স্ফটিক বিন্যাস নেই।",
    ),
    q(
        "Soda-lime glass typically contains silica with:",
        "সোডা-লাইম কাচে সিলিকার সাথে সাধারণত থাকে:",
        ["Only pure fluorine gas", "Na2O and CaO as fluxes/stabilizers", "Only uranium", "Only protein"],
        ["শুধু বিশুদ্ধ ফ্লুরিন গ্যাস", "ফ্লাক্স/স্থিতিকারক হিসেবে Na2O ও CaO", "শুধু ইউরেনিয়াম", "শুধু প্রোটিন"],
        "B", "medium", "factual",
        "Sodium oxide lowers melting point; calcium oxide improves durability.",
        "সোডিয়াম অক্সাইড গলনাঙ্ক কমায়; ক্যালসিয়াম অক্সাইড স্থায়িত্ব বাড়ায়।",
    ),
    q(
        "Steel is an alloy primarily of:",
        "ইস্পাত প্রধানত কোনটির সংকর?",
        ["Copper and zinc only", "Iron with controlled carbon (and other elements)", "Only aluminum foil", "Pure silicon wafers only"],
        ["শুধু তামা ও দস্তা", "নিয়ন্ত্রিত কার্বনসহ লোহা (ও অন্য মৌল)", "শুধু অ্যালুমিনিয়াম ফয়েল", "শুধু বিশুদ্ধ সিলিকন ওয়েফার"],
        "B", "easy", "factual",
        "Carbon content and alloying elements tune strength and properties.",
        "কার্বন ও সংকর মৌল শক্তি ও ধর্ম নিয়ন্ত্রণ করে।",
    ),
    q(
        "Annealing of glass is done to:",
        "কাচের অ্যানিলিং করা হয়:",
        ["Increase internal stress deliberately", "Remove internal stresses by slow cooling", "Dissolve the glass in acid", "Make it magnetic"],
        ["ইচ্ছাকৃত অভ্যন্তরীণ চাপ বাড়ানো", "ধীরে ঠান্ডা করে অভ্যন্তরীণ চাপ দূর করা", "অম্লে কাচ দ্রবীভূত করা", "চৌম্বক করা"],
        "B", "medium", "application",
        "Slow cooling prevents cracking from trapped thermal stresses.",
        "ধীর শীতলীকরণ আটকে থাকা তাপীয় চাপে ফাটল রোধ করে।",
    ),
    q(
        "Plaster of Paris is chemically:",
        "প্লাস্টার অব প্যারিস রাসায়নিকভাবে:",
        ["CaSO4·½H2O", "CaSO4·2H2O only as gypsum unchanged", "NaCl", "SiC"],
        ["CaSO4·½H2O", "অপরিবর্তিত জিপসাম হিসেবে শুধু CaSO4·2H2O", "NaCl", "SiC"],
        "A", "easy", "factual",
        "Heating gypsum yields plaster of Paris, which rehydrates to set.",
        "জিপসাম উত্তপ্ত করে প্লাস্টার অব প্যারিস; পুনরায় হাইড্রেট হয়ে সেট হয়।",
    ),
    q(
        "Ceramics are valued industrially for:",
        "শিল্পে সিরামিক মূল্যবান কারণ:",
        ["Always being soft metals", "Hardness, heat resistance, and chemical durability", "Being edible sugars", "Conducting like copper always"],
        ["সবসময় নরম ধাতু", "কঠোরতা, তাপ সহনশীলতা ও রাসায়নিক স্থায়িত্ব", "খাদ্যযোগ্য চিনি", "সবসময় তামার মতো পরিবাহী"],
        "B", "easy", "conceptual",
        "Fired clay and advanced ceramics serve as bricks, tiles, insulators, etc.",
        "পোড়ানো মাটি ও উন্নত সিরামিক ইট, টালি, অন্তরক ইত্যাদিতে ব্যবহৃত।",
    ),
    q(
        "Polymerization produces:",
        "পলিমারাইজেশন উৎপন্ন করে:",
        ["Only small inorganic salts", "Large molecules (polymers) from monomers", "Only noble gases", "Only free electrons in vacuum"],
        ["শুধু ছোট অজৈব লবণ", "মোনোমার থেকে বৃহৎ অণু (পলিমার)", "শুধু নিষ্ক্রিয় গ্যাস", "শুধু শূন্যে মুক্ত ইলেকট্রন"],
        "B", "easy", "factual",
        "Plastics like polyethylene form by linking many monomer units.",
        "পলিথিনের মতো প্লাস্টিক অনেক মোনোমার একত্রে যুক্ত হয়ে গঠিত।",
    ),
    q(
        "Vulcanization of rubber typically involves:",
        "রাবারের ভলকানাইজেশনে সাধারণত জড়িত:",
        ["Adding sulfur cross-links to improve elasticity and strength", "Removing all carbon", "Freezing rubber into glass only", "Dissolving rubber in aqua regia"],
        ["স্থিতিস্থাপকতা ও শক্তি বাড়াতে সালফার ক্রস-লিংক যোগ", "সব কার্বন অপসারণ", "শুধু রাবারকে কাচে হিমায়িত", "অ্যাকোয়া রেজিয়ায় রাবার দ্রবীভূত"],
        "A", "medium", "factual",
        "Sulfur bridges between polymer chains toughen natural rubber.",
        "পলিমার শৃঙ্খলের মধ্যে সালফার সেতু প্রাকৃতিক রাবার মজবুত করে।",
    ),
    q(
        "Aluminum is widely used in aircraft partly because of its:",
        "বিমানে অ্যালুমিনিয়াম ব্যাপক ব্যবহৃত আংশিক কারণ এর:",
        ["Extremely high density like lead", "Low density and protective oxide film", "Radioactivity", "Inability to form alloys"],
        ["সিসের মতো অত্যধিক ঘনত্ব", "কম ঘনত্ব ও প্রতিরক্ষামূলক অক্সাইড আবরণ", "তেজস্ক্রিয়তা", "সংকর গঠনে অক্ষমতা"],
        "B", "medium", "application",
        "Light weight plus corrosion-resistant Al2O3 skin is advantageous.",
        "হালকা ও ক্ষয়রোধী Al2O3 আবরণ সুবিধাজনক।",
    ),
    q(
        "Brass is an alloy of:",
        "পিতল কোনটির সংকর?",
        ["Iron and carbon only", "Copper and zinc", "Aluminum and mercury only", "Sodium and potassium"],
        ["শুধু লোহা ও কার্বন", "তামা ও দস্তা", "শুধু অ্যালুমিনিয়াম ও পারদ", "সোডিয়াম ও পটাশিয়াম"],
        "B", "easy", "factual",
        "Cu–Zn brass is used for fittings, instruments, and decoration.",
        "Cu–Zn পিতল ফিটিং, যন্ত্র ও অলংকরণে ব্যবহৃত।",
    ),
    q(
        "Bronze traditionally is an alloy of:",
        "ব্রোঞ্জ ঐতিহ্যগতভাবে কোনটির সংকর?",
        ["Copper and tin", "Iron and sulfur only", "Lead and helium", "Silicon and neon"],
        ["তামা ও টিন", "শুধু লোহা ও সালফার", "সিসা ও হিলিয়াম", "সিলিকন ও নিয়ন"],
        "A", "easy", "factual",
        "Cu–Sn bronze is harder than pure copper for tools and statues.",
        "Cu–Sn ব্রোঞ্জ বিশুদ্ধ তামার চেয়ে শক্ত; সরঞ্জাম ও মূর্তিতে ব্যবহৃত।",
    ),
    q(
        "Silicon dioxide (silica) is a key constituent of:",
        "সিলিকন ডাইঅক্সাইড (সিলিকা) মূল উপাদান:",
        ["Only living proteins", "Sand, quartz, and many glasses/ceramics", "Only liquid mercury", "Pure nitrogen air alone"],
        ["শুধু জীবিত প্রোটিন", "বালি, কোয়ার্টজ ও অনেক কাচ/সিরামিক", "শুধু তরল পারদ", "শুধু বিশুদ্ধ নাইট্রোজেন বায়ু"],
        "B", "easy", "factual",
        "SiO2 networks dominate many industrial silicate materials.",
        "অনেক শিল্প সিলিকেট উপকরণে SiO2 নেটওয়ার্ক প্রাধান্য পায়।",
    ),
    q(
        "Refractory materials are chosen because they:",
        "রিফ্র্যাক্টরি উপকরণ বাছাই হয় কারণ তারা:",
        ["Melt at very low temperatures", "Withstand high temperatures without softening", "Dissolve instantly in water", "Are always edible"],
        ["খুব কম তাপমাত্রায় গলে", "উচ্চ তাপমাত্রায় নরম না হয়ে সহ্য করে", "পানিতে তাৎক্ষণিক দ্রবীভূত", "সবসময় খাদ্যযোগ্য"],
        "B", "medium", "conceptual",
        "Furnace linings use refractories like fireclay and silica bricks.",
        "চুল্লির আস্তরণে ফায়ারক্লে ও সিলিকা ইটের মতো রিফ্র্যাক্টরি ব্যবহৃত।",
    ),
    q(
        "Composite materials combine:",
        "কম্পোজিট উপকরণ একত্র করে:",
        ["Only identical gases", "Two or more constituents to get superior combined properties", "Only vacuum and light", "Only radioactive waste"],
        ["শুধু অভিন্ন গ্যাস", "উন্নত সম্মিলিত ধর্মের জন্য দুই বা ততোধিক উপাদান", "শুধু শূন্য ও আলো", "শুধু তেজস্ক্রিয় বর্জ্য"],
        "B", "medium", "conceptual",
        "Examples: reinforced concrete, fiberglass, carbon-fiber composites.",
        "উদাহরণ: রিইনফোর্সড কংক্রিট, ফাইবারগ্লাস, কার্বন-ফাইবার কম্পোজিট।",
    ),
    q(
        "Galvanization protects iron by coating it with:",
        "গ্যালভানাইজেশন লোহা রক্ষা করে আবরণ দিয়ে:",
        ["Zinc", "Sodium metal", "Liquid nitrogen permanently", "Pure sugar"],
        ["দস্তা", "সোডিয়াম ধাতু", "স্থায়ী তরল নাইট্রোজেন", "বিশুদ্ধ চিনি"],
        "A", "easy", "application",
        "Zn corrodes preferentially (sacrificial protection) and forms a barrier.",
        "Zn অগ্রাধিকার ক্ষয় হয় (বলিদান রক্ষা) ও বাধা স্তর গঠন করে।",
    ),
    q(
        "Optical fiber communication relies mainly on fibers of:",
        "অপটিক্যাল ফাইবার যোগাযোগ প্রধানত নির্ভর করে কোন তন্তুর উপর?",
        ["Pure copper rods only", "High-purity glass (silica) guiding light by total internal reflection", "Wooden sticks", "Solid gold wires only"],
        ["শুধু বিশুদ্ধ তামার দণ্ড", "উচ্চ বিশুদ্ধ কাচ (সিলিকা) মোট অভ্যন্তরীণ প্রতিফলনে আলো চালনা", "কাঠের লাঠি", "শুধু কঠিন সোনার তার"],
        "B", "medium", "application",
        "Silica fibers transmit data as light pulses with low loss.",
        "সিলিকা তন্তু কম ক্ষতিতে আলোক পালস হিসেবে তথ্য বহন করে।",
    ),
    q(
        "Concrete differs from pure cement paste mainly by including:",
        "বিশুদ্ধ সিমেন্ট পেস্ট থেকে কংক্রিটের প্রধান পার্থক্য — এতে থাকে:",
        ["Only air always", "Aggregates such as sand and gravel", "Only ethanol", "Only helium bubbles as the sole solid"],
        ["সবসময় শুধু বায়ু", "বালি ও নুড়ির মতো অ্যাগ্রিগেট", "শুধু ইথানল", "শুধু হিলিয়াম বুদবুদই একমাত্র কঠিন"],
        "B", "easy", "conceptual",
        "Aggregates provide bulk and strength economically.",
        "অ্যাগ্রিগেট অর্থনৈতিকভাবে আয়তন ও শক্তি দেয়।",
    ),
    q(
        "Which property makes ceramics useful as electrical insulators?",
        "তড়িৎ অন্তরক হিসেবে সিরামিক উপযোগী কোন ধর্মের জন্য?",
        ["Very high electrical conductivity like metals", "Low electrical conductivity / high resistivity", "Being liquid at room temperature", "Ferromagnetism always"],
        ["ধাতুর মতো অত্যধিক তড়িৎ পরিবাহিতা", "কম তড়িৎ পরিবাহিতা / উচ্চ রোধকত্ব", "কক্ষতাপমাত্রায় তরল", "সবসময় ফেরোম্যাগনেটিজম"],
        "B", "medium", "application",
        "Porcelain and similar ceramics isolate conductors in power systems.",
        "পোরসেলিন ও অনুরূপ সিরামিক বিদ্যুৎ ব্যবস্থায় পরিবাহী পৃথক করে।",
    ),
]

# --- t04: Health, safety and chemical applications ---
T04 = [
    q(
        "The first action if a chemical splashes in the eyes should usually be:",
        "চোখে রাসায়নিক ছিটকে পড়লে সাধারণত প্রথম করণীয়:",
        ["Rub with contaminated gloves", "Flush with plenty of clean water and seek help", "Neutralize with unknown strong acid immediately", "Ignore until tomorrow"],
        ["দূষিত গ্লাভস দিয়ে ঘষা", "প্রচুর পরিষ্কার পানি দিয়ে ধোয়া ও সাহায্য নেওয়া", "অজানা সবল অম্ল দিয়ে তাৎক্ষণিক প্রশমন", "কাল পর্যন্ত উপেক্ষা"],
        "B", "easy", "application",
        "Immediate irrigation reduces injury; then get medical attention.",
        "তাৎক্ষণিক ধোয়া ক্ষতি কমায়; এরপর চিকিৎসা সহায়তা নিন।",
    ),
    q(
        "MSDS / SDS documents provide:",
        "MSDS / SDS নথি সরবরাহ করে:",
        ["Only marketing slogans", "Hazard, handling, and emergency information for chemicals", "Restaurant menus", "Sports scores"],
        ["শুধু বিপণন স্লোগান", "রাসায়নিকের বিপদ, ব্যবহার ও জরুরি তথ্য", "রেস্তোরাঁর মেনু", "ক্রীড়ার স্কোর"],
        "B", "easy", "factual",
        "Safety Data Sheets summarize risks, PPE, and spill response.",
        "সেফটি ডেটা শিটে ঝুঁকি, PPE ও ছিটা মোকাবিলার সারাংশ থাকে।",
    ),
    q(
        "Personal protective equipment (PPE) in a lab may include:",
        "ল্যাবে ব্যক্তিগত সুরক্ষা সরঞ্জাম (PPE) অন্তর্ভুক্ত করতে পারে:",
        ["Only jewelry for style", "Goggles, gloves, lab coat as appropriate", "Open sandals only", "Food stored with reagents"],
        ["শুধু স্টাইলের গহনা", "প্রয়োজনমতো গগলস, গ্লাভস, ল্যাব কোট", "শুধু খোলা স্যান্ডেল", "বিকারকের সাথে খাদ্য সংরক্ষণ"],
        "B", "easy", "factual",
        "PPE is selected to match chemical and physical hazards.",
        "রাসায়নিক ও ভৌত বিপদ অনুসারে PPE বেছে নেওয়া হয়।",
    ),
    q(
        "Flammable organic solvents should be kept away from:",
        "দাহ্য জৈব দ্রাবক দূরে রাখা উচিত:",
        ["Open flames and ignition sources", "Only blue labels", "Cold water baths always", "Glassware catalogs"],
        ["মুক্ত শিখা ও স্ফুলিঙ্গ উৎস", "শুধু নীল লেবেল", "সবসময় ঠান্ডা ওয়াটার বাথ", "গ্লাসওয়্যার ক্যাটালগ"],
        "A", "easy", "application",
        "Vapors can ignite; store and use with ventilation and no sparks.",
        "বাষ্প জ্বলতে পারে; বায়ুচলাচল ও স্ফুলিঙ্গমুক্ত ব্যবহারে সংরক্ষণ।",
    ),
    q(
        "The hazard pictogram of a flame indicates:",
        "শিখার হ্যাজার্ড পিকটোগ্রাম নির্দেশ করে:",
        ["Oxidizing or flammable hazards (depending on context)", "Only radioactive decay", "Only environmental friendliness", "Edible product"],
        ["জারক বা দাহ্য বিপদ (প্রসঙ্গভেদে)", "শুধু তেজস্ক্রিয় ক্ষয়", "শুধু পরিবেশবান্ধবতা", "খাদ্যযোগ্য পণ্য"],
        "A", "medium", "factual",
        "GHS flame symbols warn about fire-related chemical hazards.",
        "GHS শিখা প্রতীক অগ্নি-সংক্রান্ত রাসায়নিক বিপদ সতর্ক করে।",
    ),
    q(
        "Chlorine used for water disinfection works mainly by:",
        "পানি জীবাণুমুক্তকরণে ক্লোরিন কাজ করে প্রধানত:",
        ["Adding sugar", "Oxidizing and destroying microbes", "Increasing hardness only", "Removing all dissolved oxygen permanently for fish health"],
        ["চিনি যোগ", "জীবাণু জারণ ও ধ্বংস", "শুধু কঠোরতা বাড়ানো", "মাছের স্বাস্থ্যে স্থায়ী সব দ্রবীভূত অক্সিজেন অপসারণ"],
        "B", "medium", "application",
        "Hypochlorous species from chlorine kill pathogens in water treatment.",
        "ক্লোরিন থেকে হাইপোক্লোরাস প্রজাতি পানি শোধনে রোগজীবাণু মারে।",
    ),
    q(
        "Aspirin is chemically related to:",
        "অ্যাসপিরিন রাসায়নিকভাবে সম্পর্কিত:",
        ["Acetylsalicylic acid", "Sodium chloride only", "Pure methane", "Silicon carbide"],
        ["অ্যাসিটাইলস্যালিসাইলিক অম্ল", "শুধু সোডিয়াম ক্লোরাইড", "বিশুদ্ধ মিথেন", "সিলিকন কার্বাইড"],
        "A", "easy", "factual",
        "Aspirin is acetylsalicylic acid, an analgesic/antipyretic drug.",
        "অ্যাসপিরিন অ্যাসিটাইলস্যালিসাইলিক অম্ল; ব্যথানাশক/জ্বরনাশক।",
    ),
    q(
        "Oral rehydration salts (ORS) help treat dehydration by providing:",
        "ওরাল রিহাইড্রেশন সল্ট (ORS) পানিশূন্যতায় সাহায্য করে সরবরাহ করে:",
        ["Only pure ethanol", "Glucose and electrolytes (e.g., Na+, K+, citrate) in balanced amounts", "Only concentrated HCl", "Heavy metals"],
        ["শুধু বিশুদ্ধ ইথানল", "ভারসাম্যে গ্লুকোজ ও ইলেকট্রোলাইট (যেমন Na+, K+, সাইট্রেট)", "শুধু গাঢ় HCl", "ভারী ধাতু"],
        "B", "medium", "application",
        "Glucose-facilitated sodium absorption restores fluid balance.",
        "গ্লুকোজ-সহায়ক সোডিয়াম শোষণ তরল ভারসাম্য ফেরায়।",
    ),
    q(
        "Iodine solutions (tincture) have been used as:",
        "আয়োডিন দ্রবণ (টিংচার) ব্যবহৃত হয়েছে:",
        ["Only rocket fuel", "Antiseptics on skin", "Food sweeteners", "Glass softeners"],
        ["শুধু রকেট জ্বালানি", "ত্বকের অ্যান্টিসেপটিক", "খাদ্য মিষ্টিকারক", "কাচ নরমকারক"],
        "B", "easy", "factual",
        "Iodine has broad antimicrobial activity for topical use.",
        "আয়োডিনের ব্যাপক অ্যান্টিমাইক্রোবিয়াল ক্রিয়া স্থানীয় ব্যবহারে কাজে লাগে।",
    ),
    q(
        "Carbon monoxide is dangerous because it:",
        "কার্বন মনোক্সাইড বিপজ্জনক কারণ এটি:",
        ["Smells strongly like roses always", "Binds hemoglobin more strongly than oxygen, impairing O2 transport", "Is a solid vitamin", "Increases blood oxygen automatically"],
        ["সবসময় গোলাপের তীব্র গন্ধ", "অক্সিজেনের চেয়ে হিমোগ্লোবিনে শক্তভাবে আবদ্ধ হয়ে O2 পরিবহন ব্যাহত করে", "কঠিন ভিটামিন", "স্বয়ংক্রিয়ভাবে রক্তের অক্সিজেন বাড়ায়"],
        "B", "medium", "conceptual",
        "Colorless, odorless CO causes poisoning; detectors and ventilation matter.",
        "বর্ণহীন, গন্ধহীন CO বিষক্রিয়া ঘটায়; ডিটেক্টর ও বায়ুচলাচল জরুরি।",
    ),
    q(
        "Ozone in the upper atmosphere is beneficial because it:",
        "উচ্চ বায়ুমণ্ডলে ওজোন উপকারী কারণ এটি:",
        ["Absorbs harmful UV radiation", "Is a major greenhouse nutrient for plants at ground level always", "Removes all oxygen", "Creates pure CO"],
        ["ক্ষতিকর UV বিকিরণ শোষণ করে", "ভূমিতে সবসময় উদ্ভিদের প্রধান গ্রিনহাউস পুষ্টি", "সব অক্সিজেন সরায়", "বিশুদ্ধ CO তৈরি করে"],
        "A", "easy", "conceptual",
        "Stratospheric ozone shields life from UV-B; ground-level ozone is a pollutant.",
        "স্ট্র্যাটোস্ফিয়ারিক ওজোন UV-B থেকে রক্ষা করে; ভূমির ওজোন দূষক।",
    ),
    q(
        "Proper disposal of chemical waste generally requires:",
        "রাসায়নিক বর্জ্যের সঠিক নিষ্পত্তিতে সাধারণত প্রয়োজন:",
        ["Pouring everything down the sink without thought", "Following institutional rules for segregation and labeled waste streams", "Burning all plastics indoors", "Mixing acids and cyanides for convenience"],
        ["চিন্তা না করে সব সিঙ্কে ঢালা", "পৃথকীকরণ ও লেবেলযুক্ত বর্জ্য ধারার প্রতিষ্ঠান নিয়ম মেনে চলা", "ঘরে সব প্লাস্টিক পোড়ানো", "সুবিধার্থে অম্ল ও সায়ানাইড মেশানো"],
        "B", "easy", "application",
        "Incompatible wastes can react violently; trained disposal protects people and environment.",
        "অসামঞ্জস্য বর্জ্য হিংস্র বিক্রিয়া করতে পারে; প্রশিক্ষিত নিষ্পত্তি মানুষ ও পরিবেশ রক্ষা করে।",
    ),
    q(
        "Vaccines protect health by:",
        "টিকা স্বাস্থ্য রক্ষা করে:",
        ["Replacing the need for all hygiene forever", "Training the immune system to recognize pathogens or toxins", "Acting as strong acids in blood", "Removing DNA from all cells"],
        ["চিরকাল সব স্বাস্থ্যবিধির প্রয়োজন সরিয়ে", "রোগজীবাণু/টক্সিন চিনতে রোগপ্রতিরোধ তন্ত্রকে প্রশিক্ষণ দিয়ে", "রক্তে সবল অম্ল হিসেবে কাজ করে", "সব কোষ থেকে DNA সরিয়ে"],
        "B", "medium", "conceptual",
        "Immunological memory reduces severity of later infections.",
        "রোগপ্রতিরোধ স্মৃতি পরবর্তী সংক্রমণের তীব্রতা কমায়।",
    ),
    q(
        "Radiopaque contrast agents in medical imaging often contain:",
        "মেডিকেল ইমেজিংয়ের রেডিওপ্যাক কনট্রাস্ট এজেন্টে প্রায়ই থাকে:",
        ["Only helium balloons", "Iodine or barium compounds that block X-rays", "Pure sugar glass", "Liquid sodium"],
        ["শুধু হিলিয়াম বেলুন", "এক্স-রে বাধা দেয় এমন আয়োডিন বা ব্যারিয়াম যৌগ", "বিশুদ্ধ চিনি কাচ", "তরল সোডিয়াম"],
        "B", "hard", "factual",
        "High-Z elements absorb X-rays, outlining organs or vessels.",
        "উচ্চ-Z মৌল এক্স-রে শোষণ করে অঙ্গ/নালি চিত্রিত করে।",
    ),
    q(
        "Antacids relieve heartburn by:",
        "অ্যান্টাসিড বুকজ্বালা উপশম করে:",
        ["Increasing stomach acid further", "Neutralizing excess gastric acid with bases like carbonates/hydroxides", "Adding HCl tablets", "Blocking all enzyme production permanently"],
        ["পাকস্থলীর অম্ল আরও বাড়িয়ে", "কার্বনেট/হাইড্রোক্সাইড ক্ষার দিয়ে অতিরিক্ত গ্যাস্ট্রিক অম্ল প্রশমিত করে", "HCl ট্যাবলেট যোগ করে", "স্থায়ী সব এনজাইম উৎপাদন বন্ধ করে"],
        "B", "easy", "application",
        "Mg(OH)2, Al(OH)3, CaCO3, and NaHCO3 are common antacid bases.",
        "Mg(OH)2, Al(OH)3, CaCO3 ও NaHCO3 সাধারণ অ্যান্টাসিড ক্ষার।",
    ),
    q(
        "Lead exposure is a public-health concern because lead is:",
        "সিসা এক্সপোজার জনস্বাস্থ্য উদ্বেগ কারণ সিসা:",
        ["An essential vitamin in large doses", "A toxic heavy metal harming nervous and other systems", "Completely harmless always", "A noble gas"],
        ["বড় মাত্রায় অত্যাবশ্যক ভিটামিন", "স্নায়ু ও অন্য তন্ত্রক্ষতিকর বিষাক্ত ভারী ধাতু", "সবসময় সম্পূর্ণ নিরাপদ", "নিষ্ক্রিয় গ্যাস"],
        "B", "medium", "conceptual",
        "Lead paints, pipes, and polluted sites require control and remediation.",
        "সিসা রং, পাইপ ও দূষিত স্থানে নিয়ন্ত্রণ ও প্রতিকার দরকার।",
    ),
    q(
        "Fire triangle elements needed for most ordinary fires are:",
        "সাধারণ অগ্নিকান্ডে ফায়ার ট্রায়াঙ্গেলের উপাদান:",
        ["Only vacuum", "Fuel, oxidizer (often O2), and heat/ignition", "Only nitrogen and argon", "Only water vapor"],
        ["শুধু শূন্য", "জ্বালানি, জারক (প্রায়ই O2) ও তাপ/স্ফুলিঙ্গ", "শুধু নাইট্রোজেন ও আর্গন", "শুধু জলীয় বাষ্প"],
        "B", "easy", "factual",
        "Removing any leg of the triangle extinguishes the fire.",
        "ত্রিভুজের যেকোনো বাহু সরালে আগুন নিভে।",
    ),
    q(
        "Class B fire extinguishers are intended for:",
        "ক্লাস B অগ্নি নির্বাপক উদ্দিষ্ট:",
        ["Only ordinary combustibles like wood/paper (Class A)", "Flammable liquids (oils, solvents)", "Only cooking metal fires exclusively always", "Only electrical equipment with water jets"],
        ["শুধু কাঠ/কাগজের মতো সাধারণ দাহ্য (ক্লাস A)", "দাহ্য তরল (তেল, দ্রাবক)", "সবসময় শুধু রান্নার ধাতব আগুন", "শুধু পানির জেটসহ বৈদ্যুতিক সরঞ্জাম"],
        "B", "medium", "application",
        "Use the correct extinguisher class; water on oil fires can spread them.",
        "সঠিক শ্রেণির এক্সটিংগুইশার ব্যবহার করুন; তেলে পানি আগুন ছড়াতে পারে।",
    ),
    q(
        "Chemist’s role in pharmaceutical quality includes:",
        "ঔষধের মানে রসায়নবিদের ভূমিকা অন্তর্ভুক্ত করে:",
        ["Ignoring purity assays", "Analyzing identity, purity, and dosage of active ingredients", "Adding random unlabeled solvents to pills", "Removing all regulations"],
        ["বিশুদ্ধতা পরীক্ষা উপেক্ষা", "সক্রিয় উপাদানের পরিচয়, বিশুদ্ধতা ও মাত্রা বিশ্লেষণ", "বড়িতে এলোমেলো অচিহ্নিত দ্রাবক যোগ", "সব নিয়ম অপসারণ"],
        "B", "medium", "application",
        "Analytical chemistry ensures safe, effective medicines.",
        "বিশ্লেষণী রসায়ন নিরাপদ, কার্যকর ঔষধ নিশ্চিত করে।",
    ),
    q(
        "Why should unused medicines not be flushed into waterways casually?",
        "অব্যবহৃত ঔষধ এলোমেলো জলাশয়ে ফেলা উচিত নয় কেন?",
        ["They always improve aquatic ecosystems", "They can pollute water and affect organisms; follow take-back/disposal guidance", "They instantly become vitamins for fish", "Flushing is required by all labels"],
        ["তারা সবসময় জলজ বাস্তুতন্ত্র উন্নত করে", "পানি দূষিত ও জীবকে প্রভাবিত করতে পারে; রিটার্ন/নিষ্পত্তি নির্দেশ মেনে চলুন", "তারা তাৎক্ষণিক মাছের ভিটামিন হয়", "সব লেবেলে ফ্লাশ বাধ্যতামূলক"],
        "B", "easy", "application",
        "Pharmaceutical residues are environmental contaminants; proper disposal reduces risk.",
        "ঔষধ অবশিষ্টাংশ পরিবেশ দূষক; সঠিক নিষ্পত্তি ঝুঁকি কমায়।",
    ),
]

TOPICS_MAP = {
    "chem1_27_ch05_t01": T01,
    "chem1_27_ch05_t02": T02,
    "chem1_27_ch05_t03": T03,
    "chem1_27_ch05_t04": T04,
}


def write_topic(topic_id: str, items: list[dict]) -> dict:
    assert len(items) == 20, f"{topic_id} has {len(items)}"
    clean = []
    for item in items:
        row = {k: v for k, v in item.items() if not k.startswith("_")}
        row["verified"] = False
        row["source"] = SRC
        err = validate_record(row)
        if err:
            raise SystemExit(f"{topic_id}: {err}\n{row['stem_en'][:120]}")
        clean.append(row)
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
        "chapter": "chem1_27_ch05",
        "title_en": "Applied Chemistry",
        "title_bn": "কর্মমুখী রসায়ন",
        "source": SRC,
        "pdf_pages": [],
        "note": (
            "Import CSV chemistry_1_ch05.csv had headers only; authored 20 bilingual MCQs "
            "per topic aligned to NCTB chemistry_1st_paper_2027 ch05 (Applied Chemistry)."
        ),
        "counts": {**counts, "total": sum(counts.values())},
        "paths": paths,
        "pdf_mapping": {
            "chem1_27_ch05_t01": {
                "title": "Food chemistry and preservation / খাদ্য রসায়ন ও সংরক্ষণ",
                "themes": [
                    "preservatives refrigeration salting drying canning pasteurization",
                    "antioxidants benzoate SO2 fermentation Maillard emulsifiers",
                    "carbs proteins rancidity MAP hygiene",
                ],
            },
            "chem1_27_ch05_t02": {
                "title": "Cleaning agents and everyday chemicals / পরিষ্কারক ও দৈনন্দিন রাসায়নিক",
                "themes": [
                    "soap micelles hard water detergents surfactants builders",
                    "bleach ammonia baking/washing soda vinegar limescale",
                    "disinfectant vs antiseptic alcohol NaOH safety mixing",
                ],
            },
            "chem1_27_ch05_t03": {
                "title": "Industrial materials / শিল্পে ব্যবহৃত পদার্থ",
                "themes": [
                    "cement concrete glass annealing plaster ceramics polymers",
                    "steel brass bronze vulcanization Al galvanization",
                    "silica refractories composites optical fiber insulators",
                ],
            },
            "chem1_27_ch05_t04": {
                "title": "Health, safety and chemical applications / স্বাস্থ্য, নিরাপত্তা ও রাসায়নিক প্রয়োগ",
                "themes": [
                    "eye wash SDS PPE flammables GHS pictograms waste",
                    "chlorine water aspirin ORS iodine CO ozone vaccines",
                    "contrast agents antacids lead fire classes pharma quality",
                ],
            },
        },
        "low_confidence": [
            "No usable OCR for Chemistry 1st paper Udvash PDF ch05; syllabus-authored MCQs.",
            "Import CSV content/bank/import/chemistry_1_ch05.csv had headers only.",
            "Applied topics blend NCTB applied chemistry with standard HSC board safety/materials items.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (chem1_27_ch05_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {tid: 20 for tid in TOPIC_IDS},
        },
        "chem1_ch05_completion": {
            "topics_expected": 4,
            "topics_at_20": 4,
            "note": "chem1_27_ch05_t01..t04 complete at 20/topic (chapter total 80).",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch05_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
