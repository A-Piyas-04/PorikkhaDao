#!/usr/bin/env python3
"""Seed Biology 1st Paper Ch12 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio1_27_ch12_t01..t03 (ecosystems; distribution/biodiversity; conservation).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPICS = ROOT / "content" / "bank" / "topics"
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
from core import validate_record  # noqa: E402

SRC = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "biology p1 ch12; curated bilingual"
)


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
        bn = f"{bn} (বৈজ্ঞানিক নাম)"
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
        "verified": False,
        "source": SRC,
    }


# --- t01: Ecosystems / বাস্তুতন্ত্র ---
T01 = [
    q(
        "Bacteria and fungi are generally called—",
        "ব্যাকটেরিয়া ও ছত্রাককে সাধারণত বলা হয়—",
        [
            "Primary producers",
            "Decomposers",
            "Primary consumers",
            "Secondary consumers",
        ],
        [
            "প্রাথমিক উৎপাদক",
            "বিয়োজক",
            "প্রথম স্তরের খাদক",
            "দ্বিতীয় স্তরের খাদক",
        ],
        "B", "easy", "factual",
        "Bacteria and fungi break down dead organic matter and recycle nutrients, so they are decomposers.",
        "ব্যাকটেরিয়া ও ছত্রাক মৃত জৈব পদার্থ ভেঙে পুষ্টি পুনঃচক্রায়নে সহায়তা করে বলে এরা বিয়োজক।",
    ),
    q(
        "What is meant by a pyramid of biomass?",
        "বায়োমাসের পিরামিড বলতে কী বোঝায়?",
        [
            "A chart of rainfall only",
            "A diagram of biomass at successive trophic levels",
            "A map of continental drift",
            "A list of endangered species only",
        ],
        [
            "কেবল বৃষ্টিপাতের তালিকা",
            "খাদ্যস্তর অনুযায়ী বায়োমাসের চিত্র",
            "মহাদেশীয় সঞ্চরণের মানচিত্র",
            "কেবল বিপন্ন প্রজাতির তালিকা",
        ],
        "B", "easy", "conceptual",
        "A biomass pyramid plots the total living mass at each trophic level of an ecosystem.",
        "বায়োমাসের পিরামিডে ইকোসিস্টেমের প্রতিটি খাদ্যস্তরের মোট জীবভর দেখানো হয়।",
    ),
    q(
        "Which statements correctly describe a typical biomass pyramid?",
        "বায়োমাসের পিরামিডের কোন বর্ণনাগুলো সাধারণত সঠিক?",
        [
            "Depends on dry weight; biomass usually decreases upward; top consumers have least mass",
            "Depends only on rainfall; biomass always increases upward",
            "Ignores living mass; top consumers always have most mass",
            "Shows only mineral ions, never organisms",
        ],
        [
            "শুষ্ক ওজনভিত্তিক; উপরের দিকে ভর কমতে থাকে; শীর্ষ খাদকে ভর কম",
            "কেবল বৃষ্টিপাতভিত্তিক; উপরের দিকে ভর বাড়ে",
            "জীবভর উপেক্ষা করে; শীর্ষ খাদকে সবসময় সবচেয়ে বেশি ভর",
            "কেবল খনিজ আয়ন দেখায়, জীব নয়",
        ],
        "A", "medium", "conceptual",
        "Usual upright biomass pyramids are based on dry mass and taper toward higher consumers; parasite chains may invert.",
        "সাধারণ বায়োমাস পিরামিড শুষ্ক ভরভিত্তিক এবং উপরের খাদকস্তরে কমতে থাকে; পরজীবী শৃঙ্খলে বিপরীত হতে পারে।",
    ),
    q(
        "Energy flow in an ecosystem is typically—",
        "ইকোসিস্টেমে শক্তির প্রবাহ সাধারণত—",
        [
            "Bidirectional between all trophic levels equally",
            "Unidirectional from producers toward consumers",
            "Only circular with no loss as heat",
            "Independent of sunlight forever",
        ],
        [
            "সব খাদ্যস্তরে সমান দ্বিমুখী",
            "উৎপাদক থেকে খাদকের দিকে একমুখী",
            "কেবল বৃত্তাকার এবং তাপক্ষয়হীন",
            "সূর্যালোক ছাড়াই চিরকাল স্বতন্ত্র",
        ],
        "B", "easy", "conceptual",
        "Solar energy fixed by producers moves one way through consumers and is largely lost as heat; it does not cycle like matter.",
        "উৎপাদকে আবদ্ধ সৌরশক্তি একমুখীভাবে খাদকে যায় এবং বেশিরভাগ তাপ হিসেবে নষ্ট হয়; পদার্থের মতো চক্রায়িত হয় না।",
    ),
    q(
        "What is a biome?",
        "বায়োম বলতে কী বোঝায়?",
        [
            "A single bacterial colony only",
            "A large ecosystem unit with similar climate, soil, plants and animals",
            "Only a laboratory culture flask",
            "A temporary flood puddle with one alga",
        ],
        [
            "কেবল একটি ব্যাকটেরিয়া কলোনি",
            "সদৃশ জলবায়ু-মাটি-উদ্ভিদ-প্রাণীসহ বৃহৎ ইকোসিস্টেম একক",
            "কেবল ল্যাব কালচার ফ্লাস্ক",
            "একটি শৈবালসহ অস্থায়ী জলা",
        ],
        "B", "easy", "factual",
        "A biome is a major, recognizable ecosystem type shaped by climate, landform and dominant vegetation (e.g. desert, rainforest).",
        "বায়োম হলো জলবায়ু, ভূমিরূপ ও প্রধান গাছপালা দ্বারা নির্ধারিত বৃহৎ পৃথকযোগ্য ইকোসিস্টেম (যেমন মরুভূমি, রেইনফরেস্ট)।",
    ),
    q(
        "Water lily (shapla) is which kind of plant?",
        "শাপলা কোন ধরনের উদ্ভিদ?",
        ["Xerophyte", "Halophyte", "Hydrophyte", "Mesophyte"],
        ["জেরোফাইট", "হ্যালোফাইট", "হাইড্রোফাইট", "মেসোফাইট"],
        "C", "easy", "factual",
        "Shapla lives in water and shows hydrophyte adaptations such as air spaces and weak mechanical tissue.",
        "শাপলা জলজ পরিবেশে জন্মায় এবং বায়ুকুঠুরী ও দুর্বল যান্ত্রিক টিস্যুর মতো হাইড্রোফাইট বৈশিষ্ট্য দেখায়।",
    ),
    q(
        "Which plant typically has structurally weak conducting tissue?",
        "কোনটির পরিবহন টিস্যু গঠনগতভাবে সাধারণত দুর্বল?",
        ["Water lily (shapla)", "Sundari", "Teak", "Rice only as xerophyte"],
        ["শাপলা", "সুন্দরী", "শেগুন", "কেবল ধান জেরোফাইট হিসেবে"],
        "A", "medium", "factual",
        "Many floating/submerged hydrophytes need little mechanical support, so xylem/support tissues are poorly developed.",
        "অনেক ভাসমান/নিমজ্জিত জলজ উদ্ভিদে যান্ত্রিক অবলম্বন কম লাগে বলে পরিবহন/শক্তিশালী টিস্যু দুর্বল থাকে।",
    ),
    q(
        "Sunken stomata are commonly found in which plant?",
        "লুকায়িত রন্ধ্র সাধারণত কোন উদ্ভিদে পাওয়া যায়?",
        ["Water lily", "Hydrilla", "Water hyacinth", "Oleander (karabi)"],
        ["শাপলা", "হাইড্রিলা", "কচুরিপানা", "করবী"],
        "D", "medium", "factual",
        "Xerophytes such as Nerium (karabi) often have sunken stomata to reduce water loss.",
        "করবীর মতো মরুজ/শুষ্কসহিষ্ণু উদ্ভিদে পানিসংরক্ষণে লুকায়িত রন্ধ্র থাকে।",
    ),
    q(
        "Which statements correctly describe xerophyte adaptations?",
        "মরুজ উদ্ভিদের অভিযোজন সম্পর্কে কোনগুলো সঠিক?",
        [
            "Often small size; succulent stem/leaf; thick cuticle present (not absent)",
            "Always large leaves; cuticle always absent; roots never deep",
            "Only viviparous germination; no water storage",
            "Only large air chambers like floating hydrophytes",
        ],
        [
            "আকারে ছোট; কাণ্ড-পাতা রসালো; পুরু কিউটিকল থাকে",
            "সবসময় বড় পাতা; কিউটিকল নেই; মূল কখনো গভীর নয়",
            "কেবল জরায়ুজ অঙ্কুরোদগম; পানি সঞ্চয় নেই",
            "কেবল ভাসমান জলজের মতো বড় বায়ুকুঠুরী",
        ],
        "A", "medium", "conceptual",
        "Xerophytes reduce transpiration and store water; a thick cuticle is typical, not its absence.",
        "মরুজ উদ্ভিদ প্রস্বেদন কমায় ও পানি সঞ্চয় করে; পুরু কিউটিকল সাধারণ, অনুপস্থিতি নয়।",
    ),
    q(
        "Which is a typical xerophyte feature?",
        "মরুজ উদ্ভিদের বৈশিষ্ট্য কোনটি?",
        [
            "Viviparous germination only",
            "Leaves often reduced to spines",
            "Cuticle always absent",
            "Very large air chambers for floating",
        ],
        [
            "কেবল জরায়ুজ অঙ্কুরোদগম",
            "পাতা প্রায়ই কাঁটায় পরিণত হয়",
            "ত্বকে কিউটিকল সবসময় থাকে না",
            "ভাসার জন্য অতি বড় বায়ুকুঠুরী",
        ],
        "B", "easy", "factual",
        "Many desert plants reduce leaf area by forming spines, limiting transpiration.",
        "অনেক মরুজ উদ্ভিদে পাতা কাঁটায় পরিণত হয়ে পাতার ক্ষেত্রফল ও প্রস্বেদন কমায়।",
    ),
    q(
        "Plants adapted to saline habitats are called—",
        "লবণাক্ত পরিবেশে অভিযোজিত উদ্ভিদকে বলে—",
        ["Hydrophytes", "Xerophytes", "Halophytes", "Epiphytes only"],
        ["হাইড্রোফাইট", "জেরোফাইট", "হ্যালোফাইট", "কেবল এপিফাইট"],
        "C", "easy", "factual",
        "Halophytes grow and spread in saline soils such as mangrove coasts.",
        "হ্যালোফাইট লবণাক্ত মাটিতে (যেমন ম্যানগ্রোভ উপকূল) জন্মায় ও বিস্তার লাভ করে।",
    ),
    q(
        "Which set correctly describes saline (mangrove) plant adaptations?",
        "লবণাক্ত (ম্যানগ্রোভ) উদ্ভিদের কোন সেট সঠিক?",
        [
            "Pneumatophores; viviparous germination; roots often shallow/spread near surface",
            "No pneumatophores; deep only roots; dry seeds never germinate on plant",
            "Only floating leaves; no gas exchange structures",
            "Cuticle absent and spines only, never vivipary",
        ],
        [
            "শ্বাসমূল; জরায়ুজ অঙ্কুরোদগম; মূল প্রায়ই উপরের স্তরে বিস্তৃত",
            "শ্বাসমূল নেই; কেবল গভীর মূল; গাছে অঙ্কুর হয় না",
            "কেবল ভাসমান পাতা; গ্যাসবিনিময় কাঠামো নেই",
            "কিউটিকল নেই ও কেবল কাঁটা; জরায়ুজ নয়",
        ],
        "A", "medium", "conceptual",
        "Mangrove/halophyte traits include breathing roots, vivipary, and shallow lateral roots in anaerobic saline mud.",
        "ম্যানগ্রোভে শ্বাসমূল, জরায়ুজ অঙ্কুরোদগম ও অক্সিজেনস্বল্প লবণাক্ত কাদায় অগভীর পার্শ্বমূল সাধারণ।",
    ),
    q(
        "What is viviparous germination?",
        "জরায়ুজ অঙ্কুরোদগম বলতে কী বোঝায়?",
        [
            "Seeds germinate while still attached to the parent plant",
            "Seeds germinate only after 100 years in soil",
            "Pollen germinates inside the ovary only after fruit drop",
            "Spores germinate only in dry desert sand",
        ],
        [
            "বীজ মাতৃগাছে থাকা অবস্থায়ই অঙ্কুরিত হয়",
            "বীজ মাটিতে কেবল ১০০ বছর পর অঙ্কুরিত হয়",
            "পরাগ কেবল ফল ঝরার পর গর্ভাশয়ে অঙ্কুরিত হয়",
            "রেণু কেবল শুষ্ক মরু বালুতে অঙ্কুরিত হয়",
        ],
        "A", "medium", "conceptual",
        "In many mangroves the seed sprouts on the tree; the heavy seedling drops and anchors in mud against tides.",
        "অনেক ম্যানগ্রোভে বীজ গাছে থাকা অবস্থায় অঙ্কুরিত হয়ে ভারী চারা কাদায় পড়ে জোয়ার-ভাটায় ভেসে যায় না।",
    ),
    q(
        "Pneumatophores (breathing roots) are typically seen in—",
        "শ্বাসমূল (নিউমাটোফোর) সাধারণত কোন উদ্ভিদে দেখা যায়?",
        [
            "Typical desert xerophytes only",
            "All freshwater hydrophytes only",
            "Saline mangrove plants",
            "Only alpine mesophytes",
        ],
        [
            "কেবল সাধারণ মরুজ উদ্ভিদে",
            "কেবল সব মিষ্টিজলের জলজে",
            "লবণাক্ত ম্যানগ্রোভ উদ্ভিদে",
            "কেবল আলপাইন মেসোফাইটে",
        ],
        "C", "easy", "factual",
        "Upward breathing roots with air spaces help mangrove roots exchange gases in waterlogged saline soil.",
        "শ্বাসমূলে বায়ুকুঠুরী থাকে বলে জলমগ্ন লবণাক্ত মাটিতে গ্যাসবিনিময় সহজ হয়।",
    ),
    q(
        "Pneumatophores mainly help the plant in—",
        "শ্বাসমূল প্রধানত উদ্ভিদকে সাহায্য করে—",
        [
            "Only increasing transpiration rate",
            "Gas exchange / oxygen supply to submerged roots",
            "Only flowering twice a year",
            "Only pollination by wind",
        ],
        [
            "কেবল প্রস্বেদন হার বাড়াতে",
            "নিমজ্জিত মূলের গ্যাসবিনিময়/অক্সিজেন সরবরাহে",
            "কেবল বছরে দুবার ফুটতে",
            "কেবল বায়ুপরাগায়নে",
        ],
        "B", "medium", "conceptual",
        "Air chambers in pneumatophores allow O2 exchange between atmosphere and roots in anaerobic mud.",
        "শ্বাসমূলের বায়ুকুঠুরী অবায়বীয় কাদায় মূল ও বায়ুর মধ্যে O2 বিনিময় সম্ভব করে।",
    ),
    q(
        "A floating hydrophyte typically shows which feature?",
        "ভাসমান জলজ উদ্ভিদে সাধারণত কোন বৈশিষ্ট্য দেখা যায়?",
        [
            "Very deep tap roots only",
            "Air chambers in stem and leaf tissues",
            "No aerenchyma ever",
            "Thick woody secondary xylem like teak",
        ],
        [
            "কেবল অতি গভীর মুখ্যমূল",
            "কাণ্ড ও পাতায় বায়ুকুঠুরী",
            "কখনো এরেনকাইমা নেই",
            "শেগুনের মতো পুরু কাষ্ঠল জাইলেম",
        ],
        "B", "easy", "factual",
        "Aerenchyma (air spaces) provides buoyancy and gas storage in many aquatic plants.",
        "অনেক জলজ উদ্ভিদে এরেনকাইমা ভাসমানতা ও গ্যাস সঞ্চয়ে সাহায্য করে।",
    ),
    q(
        "Shapla, Hydrilla and water hyacinth are all examples of—",
        "শাপলা, হাইড্রিলা ও কচুরিপানা সবগুলোই উদাহরণ—",
        ["Xerophytes", "Halophytes", "Hydrophytes", "Lithophytes only"],
        ["জেরোফাইটের", "হ্যালোফাইটের", "হাইড্রোফাইটের", "কেবল লিথোফাইটের"],
        "C", "easy", "factual",
        "These plants inhabit aquatic habitats and are classified as hydrophytes.",
        "এরা জলজ পরিবেশে বাস করে বলে হাইড্রোফাইট শ্রেণিতে পড়ে।",
    ),
    q(
        "In a food chain, which group occupies the producer trophic level?",
        "খাদ্যশৃঙ্খলে কোন দল উৎপাদক খাদ্যস্তরে থাকে?",
        [
            "Green plants and other photosynthetic organisms",
            "Only carnivorous mammals",
            "Only fungi and bacteria as consumers",
            "Only tertiary predators",
        ],
        [
            "সবুজ উদ্ভিদ ও অন্য সালোকসংশ্লেষী জীব",
            "কেবল মাংসাশী স্তন্যপায়ী",
            "কেবল ছত্রাক-ব্যাকটেরিয়া খাদক হিসেবে",
            "কেবল তৃতীয় স্তরের শিকারী",
        ],
        "A", "easy", "factual",
        "Producers fix solar energy into organic matter that supports all consumer levels.",
        "উৎপাদক সৌরশক্তি জৈব পদার্থে আবদ্ধ করে সব খাদকস্তরকে সমর্থন করে।",
    ),
    q(
        "An ecosystem includes which combination?",
        "একটি বাস্তুতন্ত্রে কোন সমন্বয় থাকে?",
        [
            "Only abiotic factors, never organisms",
            "Biotic community interacting with abiotic environment",
            "Only animals in a zoo cage",
            "Only climate data without living beings",
        ],
        [
            "কেবল অজৈব উপাদান, জীব নয়",
            "জীবসম্প্রদায় ও অজৈব পরিবেশের মিথস্ক্রিয়া",
            "কেবল চিড়িয়াখানার খাঁচার প্রাণী",
            "কেবল জীববিহীন জলবায়ু তথ্য",
        ],
        "B", "easy", "conceptual",
        "An ecosystem is the functional unit of biotic components plus abiotic factors (soil, water, climate, energy).",
        "বাস্তুতন্ত্র জৈব উপাদান ও অজৈব উপাদান (মাটি, পানি, জলবায়ু, শক্তি)-এর মিথস্ক্রিয়ার একক।",
    ),
    q(
        "In a parasitic food chain, the biomass pyramid is often—",
        "পরজীবী খাদ্যশৃঙ্খলে বায়োমাসের পিরামিড প্রায়ই—",
        [
            "Upright with producers always smallest",
            "Inverted relative to a typical grazing chain",
            "Identical to a rainfall histogram",
            "Impossible to draw",
        ],
        [
            "খাড়া এবং উৎপাদক সবসময় সবচেয়ে ছোট",
            "সাধারণ চারণ শৃঙ্খলের তুলনায় বিপরীতমুখী",
            "বৃষ্টিপাত হিস্টোগ্রামের সমান",
            "আঁকা অসম্ভব",
        ],
        "B", "hard", "conceptual",
        "Many small parasites on a large host can invert the biomass pyramid compared with a grazing chain.",
        "বড় পোষকের উপর অনেক ছোট পরজীবী থাকলে চারণ শৃঙ্খলের তুলনায় বায়োমাস পিরামিড বিপরীত হতে পারে।",
    ),
]


# --- t02: Distribution and biodiversity / বিস্তার ও জীববৈচিত্র্য ---
T02 = [
    q(
        "Which country is included in the Oriental zoogeographic region?",
        "কোন দেশটি ওরিয়েন্টাল অঞ্চলের অন্তর্ভুক্ত?",
        ["Canada", "Brazil", "Australia", "Sri Lanka"],
        ["কানাডা", "ব্রাজিল", "অস্ট্রেলিয়া", "শ্রীলঙ্কা"],
        "D", "easy", "factual",
        "Sri Lanka lies in the Oriental region of Wallace’s zoogeographic division.",
        "শ্রীলঙ্কা ওয়ালেসের প্রাণীভৌগোলিক বিভাগে ওরিয়েন্টাল অঞ্চলভুক্ত।",
    ),
    q(
        "Bangladesh belongs to which zoogeographic region?",
        "বাংলাদেশ কোন প্রাণীভৌগোলিক অঞ্চলের অন্তর্ভুক্ত?",
        ["Australian", "Oriental", "Ethiopian", "Nearctic"],
        ["অস্ট্রেলিয়ান", "ওরিয়েন্টাল", "ইথিওপিয়ান", "নিআর্কটিক"],
        "B", "easy", "factual",
        "South Asian fauna including Bangladesh is classed in the Oriental region.",
        "বাংলাদেশসহ দক্ষিণ এশীয় প্রাণীকুল ওরিয়েন্টাল অঞ্চলে পড়ে।",
    ),
    q(
        "The Ganges river dolphin (shushuk) of Bangladesh is associated with which region?",
        "বাংলাদেশের গঙ্গা শুশুক কোন প্রাণীভৌগোলিক অঞ্চলের সাথে সম্পর্কিত?",
        [
            "Australian region",
            "Neotropical region",
            "Ethiopian region",
            "Oriental region",
        ],
        [
            "অস্ট্রেলিয়ান অঞ্চল",
            "নিওট্রপিক্যাল অঞ্চল",
            "ইথিওপিয়ান অঞ্চল",
            "ওরিয়েন্টাল অঞ্চল",
        ],
        "D", "easy", "factual",
        "River dolphins of the Ganges–Brahmaputra system occur within the Oriental region.",
        "গঙ্গা-ব্রহ্মপুত্র অববাহিকার নদী শুশুক ওরিয়েন্টাল অঞ্চলের অন্তর্গত।",
    ),
    q(
        "Which statements correctly describe the Ganges river dolphin?",
        "গঙ্গা শুশুক সম্পর্কে কোনগুলো সঠিক?",
        [
            "Gives birth to young; lives in rivers; considered endangered/threatened",
            "Lays eggs on land only; never enters rivers",
            "Found only in Australian deserts",
            "Is a freshwater fish that never breathes air",
        ],
        [
            "বাচ্চা প্রসব করে; নদীতে বাস করে; বিপন্ন/হুমকিগ্রস্ত বিবেচিত",
            "কেবল স্থলে ডিম পাড়ে; নদীতে যায় না",
            "কেবল অস্ট্রেলিয়ান মরুভূমিতে থাকে",
            "মিষ্টিজলের মাছ এবং কখনো বাতাস নেয় না",
        ],
        "A", "medium", "conceptual",
        "The shushuk is a mammalian river dolphin that bears live young and faces serious conservation threats.",
        "শুশুক স্তন্যপায়ী নদী ডলফিন; জীবন্ত বাচ্চা দেয় এবং সংরক্ষণ হুমকির মুখে।",
    ),
    q(
        "What is meant by biodiversity?",
        "জীববৈচিত্র্য বলতে কী বোঝায়?",
        [
            "Only the number of mineral types in soil",
            "Genetic, species and ecosystem diversity among living organisms",
            "Only seasonal rainfall variation",
            "Only human population density",
        ],
        [
            "কেবল মাটির খনিজ প্রকারের সংখ্যা",
            "জীবের মধ্যে জিনগত, প্রজাতিগত ও বাস্তুতান্ত্রিক বৈচিত্র্য",
            "কেবল ঋতুভিত্তিক বৃষ্টিপাতের ভিন্নতা",
            "কেবল মানব জনঘনত্ব",
        ],
        "B", "easy", "conceptual",
        "Biodiversity covers variation at gene, species and ecosystem (ecological) levels on Earth.",
        "জীববৈচিত্র্য পৃথিবীর জিন, প্রজাতি ও বাস্তুতন্ত্র/পরিবেশ স্তরের বৈচিত্র্যকে বোঝায়।",
    ),
    q(
        "What is meant by a biological species?",
        "জৈবিক প্রজাতি (বায়োলজিক্যাল স্পিশিস) বলতে কী বোঝায়?",
        [
            "Any two organisms that look vaguely similar",
            "Groups that interbreed to produce fertile offspring but not with other such groups",
            "Only fossils of the same age",
            "Only clones produced in a lab flask",
        ],
        [
            "যেকোনো দৃষ্টিতে সামান্য মিল থাকা দুই জীব",
            "পরস্পর মিলনে উর্বর সন্তান দেয় কিন্তু অন্য দলের সাথে দেয় না",
            "কেবল একই বয়সের জীবাশ্ম",
            "কেবল ল্যাবে তৈরি ক্লোন",
        ],
        "B", "medium", "conceptual",
        "The biological species concept defines species by actual or potential fertile interbreeding.",
        "বায়োলজিক্যাল স্পিশিস কনসেপ্টে উর্বর সন্তান উৎপাদনে সক্ষম দলকে এক প্রজাতি ধরা হয়।",
    ),
    q(
        "Where in Bangladesh is agarwood (agar) tree commonly found?",
        "বাংলাদেশে আগর গাছ সাধারণত কোথায় পাওয়া যায়?",
        ["Faridpur", "Kishoreganj", "Dinajpur", "Moulvibazar"],
        ["ফরিদপুর", "কিশোরগঞ্জ", "দিনাজপুর", "মৌলভীবাজার"],
        "D", "medium", "factual",
        "Commercial agar cultivation/occurrence is especially associated with Moulvibazar in Sylhet region.",
        "বাণিজ্যিক আগর চাষ/প্রাপ্তি সিলেট অঞ্চলের মৌলভীবাজারের সাথে বিশেষভাবে যুক্ত।",
    ),
    q(
        "Why is Madhupur forest soil characteristically red?",
        "মধুপুর বনের মাটি লাল হওয়ার কারণ কী?",
        [
            "High sulfur alone",
            "High phosphorus alone",
            "High nitrate alone",
            "Presence of iron compounds",
        ],
        [
            "কেবল উচ্চ সালফার",
            "কেবল উচ্চ ফসফরাস",
            "কেবল উচ্চ নাইট্রেট",
            "লৌহ জাতীয় পদার্থের উপস্থিতি",
        ],
        "D", "medium", "factual",
        "Red coloration of Madhupur soils is linked to iron-rich (ferruginous) compounds.",
        "মধুপুরের লাল মাটি লৌহজাত যৌগের উপস্থিতির সাথে সম্পর্কিত।",
    ),
    q(
        "Madhabkunda is an example of—",
        "মাধবকুণ্ড একটি—",
        ["Game reserve", "Safari park", "Ecopark", "Wildlife sanctuary only"],
        ["গেম রিজার্ভ", "সাফারি পার্ক", "ইকোপার্ক", "কেবল অভয়ারণ্য"],
        "C", "easy", "factual",
        "Madhabkunda is managed/known as an ecopark site in Bangladesh board materials.",
        "মাধবকুণ্ড বাংলাদেশের বোর্ড উপকরণে ইকোপার্ক হিসেবে পরিচিত।",
    ),
    q(
        "Where is Modhutila ecopark located?",
        "মধুটিলা ইকোপার্ক কোথায় অবস্থিত?",
        [
            "Moulvibazar",
            "Banshkhali, Chattogram",
            "Nalitabari, Sherpur",
            "Gowainghat, Sylhet",
        ],
        [
            "মৌলভীবাজার",
            "চট্টগ্রামের বাঁশখালী",
            "শেরপুরের নালিতাবাড়ী",
            "সিলেটের গোয়াইনঘাট",
        ],
        "C", "medium", "factual",
        "Modhutila ecopark is situated at Nalitabari in Sherpur district.",
        "মধুটিলা ইকোপার্ক শেরপুর জেলার নালিতাবাড়ীতে অবস্থিত।",
    ),
    q(
        "Which is a mangrove plant?",
        "কোনটি ম্যানগ্রোভ উদ্ভিদ?",
        ["Sal (Shorea)", "Sundari", "Teak", "Mahogany"],
        ["শাল", "সুন্দরী", "শেগুন", "মেহগনি"],
        "B", "easy", "factual",
        "Sundari is a characteristic mangrove tree of the Sundarbans.",
        "সুন্দরী সুন্দরবনের বৈশিষ্ট্যপূর্ণ ম্যানগ্রোভ বৃক্ষ।",
    ),
    q(
        "Which scientific name is a mangrove forest plant?",
        "কোন বৈজ্ঞানিক নাম ম্যানগ্রোভ বনের উদ্ভিদ?",
        [
            "Mangifera indica",
            "Oryza sativa",
            "Triticum aestivum",
            "Heritiera fomes",
        ],
        [
            "Mangifera indica",
            "Oryza sativa",
            "Triticum aestivum",
            "Heritiera fomes",
        ],
        "D", "medium", "factual",
        "Heritiera fomes is sundari, a key mangrove species; the others are mango, rice and wheat.",
        "Heritiera fomes সুন্দরী—ম্যানগ্রোভ প্রজাতি; অন্যগুলো আম, ধান ও গম।",
    ),
    q(
        "What is the scientific name of the sundari tree?",
        "সুন্দরী গাছের বৈজ্ঞানিক নাম কী?",
        [
            "Excoecaria agallocha",
            "Nypa fruticans",
            "Heritiera fomes",
            "Acanthus ilicifolius",
        ],
        [
            "Excoecaria agallocha",
            "Nypa fruticans",
            "Heritiera fomes",
            "Acanthus ilicifolius",
        ],
        "C", "medium", "factual",
        "Sundari is Heritiera fomes; the others are gewa, golpata/nipa and hargoza-type mangrove associates.",
        "সুন্দরী = Heritiera fomes; অন্যগুলো গেওয়া, গোলপাতা/নিপা ও হরগোজা জাতীয় ম্যানগ্রোভ সহযোগী।",
    ),
    q(
        "Which group lists typical Sundarbans mangrove plants?",
        "সুন্দরবনের সাধারণ ম্যানগ্রোভ উদ্ভিদের কোন তালিকা সঠিক?",
        [
            "Golpata, gewa, keora (and related mangrove taxa)",
            "Only wheat, maize and potato",
            "Only alpine conifers",
            "Only desert cacti",
        ],
        [
            "গোলপাতা, গেওয়া, কেওড়া (ও সংশ্লিষ্ট ম্যানগ্রোভ)",
            "কেবল গম, ভুট্টা ও আলু",
            "কেবল আলপাইন শঙ্কুবৃক্ষ",
            "কেবল মরু ক্যাকটাস",
        ],
        "A", "easy", "factual",
        "Sundarbans vegetation includes nipa/golpata, gewa, keora, sundari and related mangrove species.",
        "সুন্দরবনে গোলপাতা, গেওয়া, কেওড়া, সুন্দরী ইত্যাদি ম্যানগ্রোভ প্রজাতি দেখা যায়।",
    ),
    q(
        "The world’s largest tropical rainforest is mainly located in which continent?",
        "পৃথিবীর বৃহত্তম ট্রপিক্যাল রেইনফরেস্ট প্রধানত কোন মহাদেশে?",
        ["North America", "Asia", "Africa", "South America"],
        ["উত্তর আমেরিকা", "এশিয়া", "আফ্রিকা", "দক্ষিণ আমেরিকা"],
        "D", "easy", "factual",
        "The Amazon rainforest in South America is the largest tropical rainforest.",
        "দক্ষিণ আমেরিকার আমাজনই বৃহত্তম ট্রপিক্যাল রেইনফরেস্ট।",
    ),
    q(
        "Which statements about talipalm (Corypha) are correct?",
        "তালিপাম সম্পর্কে কোনগুলো সঠিক?",
        [
            "Flowers/fruits once in life; last wild plant in BD died in 2001; IUCN Extinct in the Wild",
            "Flowers every month forever; never rare",
            "Only a marine alga; never a palm",
            "Found only under Antarctic ice",
        ],
        [
            "জীবনে একবার ফুল-ফল; বন্য শেষটি BD-তে ২০০১-এ মারা; IUCN Extinct in the Wild",
            "প্রতি মাসে ফোটে; কখনো বিরল নয়",
            "কেবল সামুদ্রিক শৈবাল; পাম নয়",
            "কেবল অ্যান্টার্কটিক বরফে",
        ],
        "A", "hard", "factual",
        "Talipalm is monocarpic; Bangladesh’s last wild individual died in 2001 and IUCN lists it Extinct in the Wild.",
        "তালিপাম একবার ফোটে; বাংলাদেশের শেষ বন্যটি ২০০১-এ মারা যায় এবং IUCN একে Extinct in the Wild বলে।",
    ),
    q(
        "Roughly how many species of organisms have been identified so far (order of magnitude in HSC notes)?",
        "এ যাবৎ শনাক্তকৃত জীবপ্রজাতির সংখ্যা আনুমানিক কত (HSC নোট অনুসারে)?",
        [
            "About 1.75 million identified (of ~3 million estimated)",
            "Exactly 100 only",
            "Exactly one billion named insects only",
            "Zero; none have been named",
        ],
        [
            "শনাক্ত ~১৭.৫ লক্ষ (অনুমানিত ~৩০ লক্ষের মধ্যে)",
            "ঠিক ১০০টি মাত্র",
            "ঠিক ১০০ কোটি কেবল পোকা",
            "শূন্য; কোনো নামকরণ হয়নি",
        ],
        "A", "medium", "factual",
        "HSC texts often cite ~3 million estimated species with about 1.75 million described.",
        "HSC পাঠে প্রায় ৩০ লক্ষ অনুমান ও প্রায় ১৭.৫ লক্ষ শনাক্তের উল্লেখ থাকে।",
    ),
    q(
        "Distribution of organisms is strongly influenced by—",
        "জীবের বিস্তার প্রধানত প্রভাবিত হয়—",
        [
            "Climate, soil, physiography and biotic interactions",
            "Only the color of classroom walls",
            "Only the brand of laboratory glassware",
            "Only postal zip codes",
        ],
        [
            "জলবায়ু, মাটি, ভূমিরূপ ও জৈব মিথস্ক্রিয়া দ্বারা",
            "কেবল শ্রেণিকক্ষের দেয়ালের রঙে",
            "কেবল ল্যাব কাচপাত্রের ব্র্যান্ডে",
            "কেবল পোস্টাল কোডে",
        ],
        "A", "easy", "conceptual",
        "Abiotic factors and biotic relationships determine where species can live and spread.",
        "অজৈব উপাদান ও জৈব সম্পর্ক প্রজাতির বাসস্থান ও বিস্তার নির্ধারণ করে।",
    ),
    q(
        "Tropical rainforest biomes are characterized by—",
        "ট্রপিক্যাল রেইনফরেস্ট বায়োমের বৈশিষ্ট্য—",
        [
            "High rainfall, high biodiversity and dense multilayer vegetation",
            "Permanent ice cover and no trees",
            "Zero rainfall and only cactus monoculture",
            "Only deep ocean vents",
        ],
        [
            "উচ্চ বৃষ্টিপাত, উচ্চ জীববৈচিত্র্য ও ঘন বহুস্তরীয় গাছপালা",
            "স্থায়ী বরফ ও বৃক্ষহীনতা",
            "শূন্য বৃষ্টি ও কেবল ক্যাকটাস একফসলি",
            "কেবল গভীর সমুদ্রের ফাটল",
        ],
        "A", "easy", "conceptual",
        "Rainforest biomes combine warm wet climate with extraordinary species richness and complex canopies.",
        "রেইনফরেস্টে উষ্ণ-আর্দ্র জলবায়ু, অসাধারণ প্রজাতি সমৃদ্ধি ও জটিল ছাউনি থাকে।",
    ),
    q(
        "Which pair correctly matches plant ecological group and habitat?",
        "কোন জোড়া উদ্ভিদের বাস্তুতান্ত্রিক দল ও বাসস্থান সঠিকভাবে মেলায়?",
        [
            "Halophyte — saline mangrove coast; xerophyte — arid habitat; hydrophyte — aquatic habitat",
            "Halophyte — only alpine snow; xerophyte — only deep ocean; hydrophyte — only desert dunes",
            "All three groups only on polar ice",
            "None of these groups exist in nature",
        ],
        [
            "হ্যালোফাইট — লবণাক্ত ম্যানগ্রোভ; জেরোফাইট — শুষ্ক বাসস্থান; হাইড্রোফাইট — জলজ",
            "হ্যালোফাইট — কেবল আলপাইন তুষার; জেরোফাইট — কেবল গভীর সমুদ্র; হাইড্রোফাইট — কেবল মরু টিলা",
            "তিন দলই কেবল মেরু বরফে",
            "এসব দল প্রকৃতিতে নেই",
        ],
        "A", "medium", "application",
        "Ecological plant groups are named for the habitats they are adapted to occupy.",
        "উদ্ভিদের বাস্তুতান্ত্রিক দল তাদের অভিযোজিত বাসস্থান অনুসারে নামকরণ হয়।",
    ),
]


# --- t03: Conservation / সংরক্ষণ ---
T03 = [
    q(
        "Which of the following is an example of ex-situ conservation?",
        "নিচের কোনটি এক্স-সিটু (Ex-situ) সংরক্ষণ?",
        ["Game reserve", "Safari park", "Ecopark", "Zoo"],
        ["গেম রিজার্ভ", "সাফারি পার্ক", "ইকোপার্ক", "চিড়িয়াখানা"],
        "D", "easy", "factual",
        "Keeping organisms outside their natural habitats (e.g. in zoos) is ex-situ conservation.",
        "প্রাকৃতিক আবাসস্থলের বাইরে (যেমন চিড়িয়াখানায়) সংরক্ষণই এক্স-সিটু সংরক্ষণ।",
    ),
    q(
        "Which is an ex-situ conservation method?",
        "কোনটি এক্স-সিটু সংরক্ষণ পদ্ধতি?",
        ["National park", "Ecopark", "Safari park", "Seed bank"],
        ["ন্যাশনাল পার্ক", "ইকোপার্ক", "সাফারি পার্ক", "সিড ব্যাংক"],
        "D", "easy", "factual",
        "Seed banks store germplasm away from natural ecosystems, a classic ex-situ approach.",
        "সিড ব্যাংকে প্রাকৃতিক বাস্তুতন্ত্রের বাইরে জার্মপ্লাজম সংরক্ষিত হয়।",
    ),
    q(
        "Which of these is ex-situ conservation?",
        "নিচের কোনটি Ex-situ সংরক্ষণ?",
        [
            "National park",
            "Botanical garden",
            "Safari park",
            "Ecopark",
        ],
        [
            "জাতীয় উদ্যান",
            "বোটানিক্যাল গার্ডেন",
            "সাফারি পার্ক",
            "ইকোপার্ক",
        ],
        "B", "easy", "factual",
        "Botanical gardens conserve plant diversity outside wild habitats.",
        "বোটানিক্যাল গার্ডেন বন্য আবাসস্থলের বাইরে উদ্ভিদ বৈচিত্র্য সংরক্ষণ করে।",
    ),
    q(
        "Which is an in-situ conservation approach?",
        "কোনটি ইন-সিটু (In-situ) সংরক্ষণ?",
        ["Ecopark", "Botanical garden", "Seed bank", "Zoo"],
        ["ইকোপার্ক", "বোটানিক্যাল গার্ডেন", "বীজ ব্যাংক", "চিড়িয়াখানা"],
        "A", "easy", "factual",
        "In-situ means protecting species in their natural ecosystems; ecoparks/protected areas fit this approach.",
        "ইন-সিটু মানে প্রাকৃতিক বাস্তুতন্ত্রে সংরক্ষণ; ইকোপার্ক/সংরক্ষিত এলাকা এর অন্তর্গত।",
    ),
    q(
        "Which method is ex-situ conservation?",
        "কোনটি এক্স-সিটু সংরক্ষণ পদ্ধতি?",
        [
            "Safari park",
            "Halda River as a natural breeding ground",
            "Game reserve",
            "Germplasm bank",
        ],
        [
            "সাফারি পার্ক",
            "প্রাকৃতিক প্রজননক্ষেত্র হিসেবে হালদা নদী",
            "গেম রিজার্ভ",
            "জার্মপ্লাজম ব্যাংক",
        ],
        "D", "medium", "factual",
        "Germplasm banks store genetic material off-site; Halda and game reserves protect organisms in nature.",
        "জার্মপ্লাজম ব্যাংক অফ-সাইট জিন উপাদান রাখে; হালদা ও গেম রিজার্ভ প্রকৃতিতে সুরক্ষা দেয়।",
    ),
    q(
        "Which pair correctly lists ex-situ conservation sites/methods?",
        "কোন জোড়া সঠিকভাবে এক্স-সিটু সংরক্ষণ নির্দেশ করে?",
        [
            "Botanical garden and seed bank",
            "Only national parks and sanctuaries",
            "Only game reserves and ecoparks",
            "Only Halda River and Sundarbans wild stands",
        ],
        [
            "বোটানিক্যাল গার্ডেন ও সীড ব্যাংক",
            "কেবল জাতীয় উদ্যান ও অভয়ারণ্য",
            "কেবল গেম রিজার্ভ ও ইকোপার্ক",
            "কেবল হালদা নদী ও সুন্দরবনের বন্য স্থান",
        ],
        "A", "medium", "conceptual",
        "Gardens and seed banks remove/store biodiversity outside wild ecosystems; parks/reserves are typically in-situ.",
        "গার্ডেন ও সীড ব্যাংক বন্য বাস্তুতন্ত্রের বাইরে সংরক্ষণ; পার্ক/রিজার্ভ সাধারণত ইন-সিটু।",
    ),
    q(
        "About 70% of seeds can be dried and stored near −20°C for long periods; the remaining ~30% are called—",
        "প্রায় ৭০% বীজ শুকিয়ে −২০°C-এ দীর্ঘদিন রাখা যায়; বাকি ~৩০% বীজকে বলে—",
        ["Diploid", "Haploid", "Orthodox", "Recalcitrant"],
        ["Diploid", "Haploid", "Orthodox", "Recalcitrant"],
        "D", "hard", "factual",
        "Recalcitrant seeds do not tolerate desiccation/low-temperature orthodox seed-bank storage.",
        "রিক্যালসিট্রান্ট বীজ শুকানো ও নিম্নতাপমাত্রার অর্থোডক্স সীড-ব্যাংক সংরক্ষণ সহ্য করে না।",
    ),
    q(
        "Seeds that tolerate drying and cold storage in seed banks are generally called—",
        "শুকানো ও শীতল সীড-ব্যাংক সংরক্ষণ সহ্য করে এমন বীজকে সাধারণত বলে—",
        ["Recalcitrant only", "Orthodox", "Always diploid only", "Always haploid only"],
        ["কেবল রিক্যালসিট্রান্ট", "অর্থোডক্স", "সবসময় কেবল ডিপ্লয়েড", "সবসময় কেবল হ্যাপ্লয়েড"],
        "B", "medium", "factual",
        "Orthodox seeds can be dried and frozen for long-term ex-situ storage; recalcitrant seeds cannot.",
        "অর্থোডক্স বীজ শুকিয়ে হিমায়িত করে দীর্ঘমেয়াদি এক্স-সিটু রাখা যায়; রিক্যালসিট্রান্ট যায় না।",
    ),
    q(
        "A place where tourists observe free-ranging wildlife from protected vehicles is typically a—",
        "পর্যটকরা সুরক্ষিত যানবাহন থেকে উন্মুক্ত চারণকারী বন্যপ্রাণী দেখে—এমন স্থান সাধারণত—",
        ["Safari park", "Ecopark only", "Game reserve only", "Sanctuary only"],
        ["সাফারি পার্ক", "কেবল ইকোপার্ক", "কেবল গেম রিজার্ভ", "কেবল অভয়ারণ্য"],
        "A", "easy", "application",
        "Safari parks are designed for vehicle-based viewing of animals in open settings.",
        "সাফারি পার্কে যানবাহন থেকে খোলা পরিবেশে প্রাণী পর্যবেক্ষণের ব্যবস্থা থাকে।",
    ),
    q(
        "Main purposes of establishing a safari park usually include—",
        "সাফারি পার্ক প্রতিষ্ঠার প্রধান উদ্দেশ্য সাধারণত—",
        [
            "Conserve/breed threatened wildlife and raise public conservation awareness",
            "Only build a natural history museum without living animals",
            "Only mine ores inside animal enclosures",
            "Only replace all forests with concrete",
        ],
        [
            "বিপন্ন বন্যপ্রাণী সংরক্ষণ/প্রজনন ও জনসচেতনতা বৃদ্ধি",
            "কেবল জীবন্ত প্রাণী ছাড়া প্রাকৃতিক ইতিহাস জাদুঘর",
            "কেবল প্রাণী এলাকায় খনি খনন",
            "কেবল সব বন কংক্রিটে রূপান্তর",
        ],
        "A", "medium", "conceptual",
        "Safari parks support conservation breeding/display and education; a museum alone is not their defining purpose.",
        "সাফারি পার্ক সংরক্ষণ-প্রজনন ও শিক্ষায় সহায়তা করে; কেবল জাদুঘরই এর মূল উদ্দেশ্য নয়।",
    ),
    q(
        "In-situ conservation means—",
        "ইন-সিটু সংরক্ষণ বলতে বোঝায়—",
        [
            "Protecting species within their natural habitats/ecosystems",
            "Only storing DNA in a freezer far from nature",
            "Only displaying stuffed specimens in museums",
            "Only growing crops in hydroponic labs",
        ],
        [
            "প্রাকৃতিক আবাস/বাস্তুতন্ত্রে প্রজাতি সুরক্ষা",
            "কেবল প্রকৃতি থেকে দূরে ফ্রিজারে DNA রাখা",
            "কেবল জাদুঘরে স্টাফড নমুনা প্রদর্শন",
            "কেবল ল্যাবে হাইড্রোপনিক ফসল",
        ],
        "A", "easy", "conceptual",
        "In-situ keeps organisms in the ecosystems where they naturally occur (parks, sanctuaries, reserves).",
        "ইন-সিটুতে জীবকে তাদের স্বাভাবিক বাস্তুতন্ত্রে (পার্ক, অভয়ারণ্য, রিজার্ভ) রাখা হয়।",
    ),
    q(
        "Ex-situ conservation means—",
        "এক্স-সিটু সংরক্ষণ বলতে বোঝায়—",
        [
            "Conserving biodiversity outside natural habitats",
            "Only leaving forests completely unmanaged forever",
            "Only hunting without regulation",
            "Only measuring rainfall",
        ],
        [
            "প্রাকৃতিক আবাসস্থলের বাইরে জীববৈচিত্র্য সংরক্ষণ",
            "কেবল বন চিরকাল অব্যবস্থাপিত রাখা",
            "কেবল নিয়মহীন শিকার",
            "কেবল বৃষ্টিপাত মাপা",
        ],
        "A", "easy", "conceptual",
        "Zoos, botanical gardens, seed/germplasm banks and aquaria are common ex-situ tools.",
        "চিড়িয়াখানা, বোটানিক্যাল গার্ডেন, সীড/জার্মপ্লাজম ব্যাংক ও অ্যাকুয়ারিয়াম এক্স-সিটুর উদাহরণ।",
    ),
    q(
        "National parks and wildlife sanctuaries primarily represent—",
        "জাতীয় উদ্যান ও বন্যপ্রাণী অভয়ারণ্য প্রধানত প্রতিনিধিত্ব করে—",
        [
            "In-situ conservation",
            "Only ex-situ seed freezing",
            "Only industrial logging concessions",
            "Only urban parking lots",
        ],
        [
            "ইন-সিটু সংরক্ষণ",
            "কেবল এক্স-সিটু বীজ হিমায়ন",
            "কেবল শিল্প কাঠ কর্তন ছাড়",
            "কেবল শহরের পার্কিং",
        ],
        "A", "easy", "factual",
        "Protected areas conserve ecosystems and species on-site.",
        "সংরক্ষিত এলাকা বাস্তুতন্ত্র ও প্রজাতিকে স্থানেই সুরক্ষা দেয়।",
    ),
    q(
        "Which IUCN category indicates a species surviving only in cultivation/captivity, not in the wild?",
        "কোন IUCN শ্রেণি বোঝায় প্রজাতি কেবল চাষ/বন্দি অবস্থায় টিকে আছে, বন্যে নয়?",
        [
            "Least Concern",
            "Extinct in the Wild",
            "Data Deficient only",
            "Not Evaluated only",
        ],
        [
            "Least Concern",
            "Extinct in the Wild",
            "কেবল Data Deficient",
            "কেবল Not Evaluated",
        ],
        "B", "medium", "factual",
        "Extinct in the Wild (EW) means no known wild populations remain.",
        "Extinct in the Wild (EW) মানে বন্য জনসংখ্যা আর জানা নেই।",
    ),
    q(
        "A green belt (shelterbelt) of trees is planted mainly to—",
        "সবুজ বেষ্টনী বৃক্ষরোপণের প্রধান উদ্দেশ্য—",
        [
            "Reduce wind damage, hold soil and provide useful products where suitable",
            "Increase desertification deliberately",
            "Remove all soil organic matter",
            "Block all rainfall permanently",
        ],
        [
            "ঝড়ের ক্ষতি কমানো, মাটি ধরে রাখা ও উপযুক্ত স্থানে দরকারি সম্পদ দেওয়া",
            "ইচ্ছাকৃতভাবে মরুকরণ বাড়ানো",
            "সব জৈব পদার্থ সরিয়ে ফেলা",
            "চিরকাল সব বৃষ্টিপাত আটকানো",
        ],
        "A", "medium", "application",
        "Shelterbelt species should resist storms, bind soil with roots and may yield fuel, fodder or timber.",
        "বেষ্টনীর প্রজাতি ঝড়সহনশীল, মূল দিয়ে মাটি ধরে এবং জ্বালানি/পশুখাদ্য/কাঠ দিতে পারে।",
    ),
    q(
        "Which trees may be selected for coastal/saline green belts in Bangladesh contexts?",
        "বাংলাদেশের উপকূলীয়/লবণাক্ত সবুজ বেষ্টনীর জন্য কোন বৃক্ষ নির্বাচন করা যায়?",
        [
            "Keora, sundari, baen/Rhizophora, passar, coconut, betel nut, etc.",
            "Only alpine fir and spruce",
            "Only wheat and barley annuals",
            "Only aquarium algae",
        ],
        [
            "কেওড়া, সুন্দরী, বাইন/রাইজোফোরা, পশুর, নারিকেল, সুপারি ইত্যাদি",
            "কেবল আলপাইন ফার ও স্প্রুস",
            "কেবল গম ও যবের বার্ষিক ফসল",
            "কেবল অ্যাকুয়ারিয়াম শৈবাল",
        ],
        "A", "hard", "application",
        "Coastal belts use salt-tolerant/mangrove and useful coastal trees suited to local conditions.",
        "উপকূলীয় বেষ্টনীতে লবণসহিষ্ণু/ম্যানগ্রোভ ও স্থানীয় উপযোগী উপকূলীয় বৃক্ষ ব্যবহার হয়।",
    ),
    q(
        "Conserving biodiversity is important because—",
        "জীববৈচিত্র্য সংরক্ষণ গুরুত্বপূর্ণ কারণ—",
        [
            "Each species has ecological roles and supports ecosystem services and human needs",
            "Only rare stamps have value",
            "Only one species matters on Earth",
            "Ecosystems function better with zero species",
        ],
        [
            "প্রতিটি প্রজাতির বাস্তুতান্ত্রিক ভূমিকা ও মানুষের উপকারিতা আছে",
            "কেবল দুর্লভ ডাকটিকিটের মূল্য আছে",
            "পৃথিবীতে কেবল এক প্রজাতিই দরকার",
            "শূন্য প্রজাতিতে বাস্তুতন্ত্র ভালো চলে",
        ],
        "A", "easy", "conceptual",
        "Species diversity underpins food webs, medicine, agriculture, culture and ecosystem stability.",
        "প্রজাতি বৈচিত্র্য খাদ্যজাল, ঔষধ, কৃষি, সংস্কৃতি ও বাস্তুতন্ত্র স্থিতিশীলতায় ভিত্তি।",
    ),
    q(
        "Which activity threatens biodiversity most directly?",
        "কোন কার্যক্রম জীববৈচিত্র্যকে সবচেয়ে সরাসরি হুমকি দেয়?",
        [
            "Habitat destruction, overexploitation and pollution",
            "Careful in-situ protected-area management",
            "Scientific monitoring without harvest",
            "Restoring degraded wetlands",
        ],
        [
            "বাসস্থান ধ্বংস, অতিআহরণ ও দূষণ",
            "সতর্ক ইন-সিটু সংরক্ষিত এলাকা ব্যবস্থাপনা",
            "আহরণ ছাড়া বৈজ্ঞানিক পর্যবেক্ষণ",
            "ক্ষয়প্রাপ্ত জলাভূমি পুনরুদ্ধার",
        ],
        "A", "easy", "application",
        "Loss of habitat, overharvest and pollution are major drivers of species decline.",
        "বাসস্থান হ্রাস, অতিআহরণ ও দূষণ প্রজাতি হ্রাসের প্রধান চালক।",
    ),
    q(
        "A germplasm bank primarily stores—",
        "জার্মপ্লাজম ব্যাংক প্রধানত সংরক্ষণ করে—",
        [
            "Genetic material of plants/animals for future use",
            "Only fossil fuels",
            "Only construction cement",
            "Only outdated exam papers",
        ],
        [
            "ভবিষ্যৎ ব্যবহারের জন্য উদ্ভিদ/প্রাণীর জিনগত উপাদান",
            "কেবল জীবাশ্ম জ্বালানি",
            "কেবল নির্মাণ সিমেন্ট",
            "কেবল পুরনো পরীক্ষার খাতা",
        ],
        "A", "medium", "factual",
        "Germplasm banks are ex-situ repositories of seeds, tissues or other genetic resources.",
        "জার্মপ্লাজম ব্যাংক বীজ, টিস্যু বা অন্য জিন উৎসের এক্স-সিটু ভাণ্ডার।",
    ),
    q(
        "Which matching of conservation type is correct?",
        "সংরক্ষণ প্রকারের কোন মিলকরণ সঠিক?",
        [
            "Sundarbans wild stands — in-situ; zoo breeding of a rare bird — ex-situ",
            "Seed bank — in-situ; national park — only ex-situ",
            "Botanical garden — in-situ; sanctuary — only ex-situ freezer",
            "All protected forests — only ex-situ by definition",
        ],
        [
            "সুন্দরবনের বন্য স্থান — ইন-সিটু; দুর্লভ পাখির চিড়িয়াখানা প্রজনন — এক্স-সিটু",
            "সীড ব্যাংক — ইন-সিটু; জাতীয় উদ্যান — কেবল এক্স-সিটু",
            "বোটানিক্যাল গার্ডেন — ইন-সিটু; অভয়ারণ্য — কেবল এক্স-সিটু ফ্রিজার",
            "সব সংরক্ষিত বন — সংজ্ঞাগতভাবে কেবল এক্স-সিটু",
        ],
        "A", "hard", "application",
        "Wild ecosystem protection is in-situ; captive breeding and off-site collections are ex-situ.",
        "বন্য বাস্তুতন্ত্র সুরক্ষা ইন-সিটু; বন্দি প্রজনন ও অফ-সাইট সংগ্রহ এক্স-সিটু।",
    ),
]


def main() -> int:
    bundles = {
        "bio1_27_ch12_t01": T01,
        "bio1_27_ch12_t02": T02,
        "bio1_27_ch12_t03": T03,
    }
    TOPICS.mkdir(parents=True, exist_ok=True)
    counts: dict[str, int] = {}
    all_stems: dict[str, str] = {}
    invalid = 0
    duplicates = 0

    for tid, rows in bundles.items():
        if len(rows) != 20:
            raise SystemExit(f"{tid}: expected 20, got {len(rows)}")
        path = TOPICS / f"{tid}.jsonl"
        lines: list[str] = []
        for i, rec in enumerate(rows, 1):
            err = validate_record(rec)
            if err:
                invalid += 1
                print(f"INVALID {tid}#{i}: {err}")
            key = rec["stem_en"].strip().lower()
            if key in all_stems:
                duplicates += 1
                print(f"DUPLICATE stem with {all_stems[key]}: {tid}#{i}")
            else:
                all_stems[key] = tid
            lines.append(json.dumps(rec, ensure_ascii=False))
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        counts[tid] = len(rows)
        print(f"Wrote {path} ({len(rows)})")

    summary = {
        "chapter": "bio1_27_ch12",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p353_pdf359.png",
            "p354_pdf360.png",
            "p355_pdf361.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio1_27_ch12_t01": {
                "title": "Ecosystems / বাস্তুতন্ত্র",
                "themes": [
                    "producers, consumers, decomposers (bacteria/fungi)",
                    "biomass pyramid; inverted parasite chains; unidirectional energy flow",
                    "biome definition; ecosystem biotic+abiotic unit",
                    "hydrophytes (shapla/hydrilla/hyacinth): aerenchyma, weak xylem",
                    "xerophytes: sunken stomata (karabi), spines, succulence, cuticle",
                    "halophytes/mangroves: pneumatophores, vivipary, shallow roots",
                ],
            },
            "bio1_27_ch12_t02": {
                "title": "Distribution and biodiversity / বিস্তার ও জীববৈচিত্র্য",
                "themes": [
                    "Oriental region: BD, Sri Lanka; river dolphin (shushuk)",
                    "biodiversity = genetic + species + ecosystem diversity",
                    "biological species concept; species richness estimates",
                    "agar (Moulvibazar); Madhupur red iron soil; Madhabkunda; Modhutila",
                    "mangroves: sundari Heritiera fomes; golpata/gewa/keora",
                    "Amazon rainforest; talipalm Extinct in the Wild / monocarpic",
                ],
            },
            "bio1_27_ch12_t03": {
                "title": "Conservation / সংরক্ষণ",
                "themes": [
                    "in-situ: parks, sanctuaries, reserves, ecoparks, Halda",
                    "ex-situ: zoo, botanical garden, seed/germplasm bank",
                    "orthodox vs recalcitrant seeds (−20°C storage)",
                    "safari park viewing + conservation/education aims",
                    "IUCN Extinct in the Wild; green-belt coastal species",
                    "threats: habitat loss, overexploitation, pollution",
                ],
            },
        },
        "low_confidence": [
            "OCR on p353–355 is very noisy; many stems reconstructed from board-style keys and HSC notes.",
            "Short printed MCQ span (~3 pages); accurate HSC-level authored items heavily supplement OCR.",
            "Figure-stimulus plant A/B items rewritten as standalone hydrophyte/adaptation stems.",
            "Safari park listed as NOT ex-situ when contrasted with zoo/seed bank/botanical garden per Udvash keys.",
            "Germplasm-bank item answer is D in source MCQ sets; matching stem uses Germplasm bank as ex-situ.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio1_27_ch12_* checked via validate_record)",
            "invalid": invalid,
            "duplicates": duplicates,
            "per_topic": counts,
        },
    }
    out = (
        ROOT
        / "content"
        / "bank"
        / "udvash_raw"
        / "biology_1"
        / "parsed"
        / "ch12_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    summary["validate"]["invalid"] = invalid
    summary["validate"]["duplicates"] = duplicates
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    if invalid or duplicates:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
