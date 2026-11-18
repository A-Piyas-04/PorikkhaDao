#!/usr/bin/env python3
"""Seed Biology 1st Paper Ch5 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio1_27_ch05_t01..t03 (algae; fungi; reproduction and importance).
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
    "biology p1 ch05; curated bilingual"
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
    # Scientific names / Latin-only options: satisfy Bangla-option check.
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


# --- t01: Algae / শৈবাল ---
T01 = [
    q(
        "Which of the following is a leaf-like (foliose thalloid) green alga?",
        "কোনটি পাতা সদৃশ শৈবাল?",
        ["Ulothrix", "Chlorella", "Chara", "Ulva"],
        ["Ulothrix (ইউলোথ্রিক্স)", "Chlorella (ক্লোরেলা)", "Chara (ক্যারা)", "Ulva (আলভা)"],
        "D", "easy", "factual",
        "Ulva has a flat, sheet-like thallus; Ulothrix is unbranched filamentous, Chlorella unicellular, and Chara has node–internode organization.",
        "Ulva সমতল পাতাসদৃশ থ্যালাসবিশিষ্ট; Ulothrix অশাখ ফিলামেন্টাস, Chlorella এককোষী এবং Chara-এর পর্ব–পর্বমধ্য গঠন আছে।",
    ),
    q(
        "Which alga shows distinct nodes and internodes?",
        "পর্ব ও পর্বমধ্যবিশিষ্ট শৈবাল কোনটি?",
        ["Ulothrix", "Chlorella", "Chara", "Volvox"],
        ["Ulothrix", "Chlorella", "Chara", "Volvox"],
        "C", "easy", "factual",
        "Chara is a branched green alga with node–internode organization resembling a stem.",
        "Chara শাখান্বিত সবুজ শৈবাল যার পর্ব–পর্বমধ্য কাণ্ডসদৃশ গঠন দেখা যায়।",
    ),
    q(
        "Which of the following is a unicellular alga?",
        "নিচের কোনটি এককোষী শৈবাল?",
        ["Chara", "Navicula", "Zygnema", "Chaetophora"],
        ["Chara", "Navicula", "Zygnema", "Chaetophora"],
        "B", "easy", "factual",
        "Navicula is a unicellular diatom; Chara, Zygnema and Chaetophora are multicellular filamentous/branched forms.",
        "Navicula এককোষী ডায়াটম; Chara, Zygnema ও Chaetophora বহুকোষী ফিলামেন্টাস/শাখান্বিত।",
    ),
    q(
        "Which is a unicellular motile green alga?",
        "এককোষী সচল শৈবাল হলো—",
        ["Navicula", "Chlorella", "Chlorococcus", "Chlamydomonas"],
        ["Navicula", "Chlorella", "Chlorococcus", "Chlamydomonas"],
        "D", "easy", "factual",
        "Chlamydomonas is a biflagellate unicellular green alga; Chlorella is unicellular but non-motile.",
        "Chlamydomonas দ্বি-ফ্লাজেলাযুক্ত এককোষী সবুজ শৈবাল; Chlorella এককোষী কিন্তু নিশ্চল।",
    ),
    q(
        "Algae growing on rock surfaces are called:",
        "পাথরের গায়ে জন্মায় যে শৈবাল তাকে কী বলে?",
        ["Halophyte", "Lithophyte", "Epiphyte", "Xerophyte"],
        ["হ্যালোফাইট", "লিথোফাইট", "এপিফাইট", "জেরোফাইট"],
        "B", "easy", "factual",
        "Lithophytes grow on rocks; epiphytes grow on other plants, and halophytes tolerate saline habitats.",
        "লিথোফাইট পাথরে জন্মায়; এপিফাইট অন্য উদ্ভিদে এবং হ্যালোফাইট লবণাক্ত আবাসে জন্মায়।",
    ),
    q(
        "Which plant has a pyrenoid in its chloroplast?",
        "কোন উদ্ভিদের ক্লোরোপ্লাস্টে পাইরিনয়েড থাকে?",
        ["Nostoc", "Ulothrix", "Riccia", "Cycas"],
        ["Nostoc", "Ulothrix", "Riccia", "Cycas"],
        "B", "medium", "factual",
        "Ulothrix chloroplasts contain pyrenoids for starch formation; Nostoc is a prokaryotic cyanobacterium without true chloroplasts.",
        "Ulothrix-এর ক্লোরোপ্লাস্টে স্টার্চ গঠনের জন্য পাইরিনয়েড থাকে; Nostoc প্রাককেন্দ্রিক সায়ানোব্যাকটেরিয়া এবং সত্য ক্লোরোপ্লাস্টহীন।",
    ),
    q(
        "Which of the following is a red alga?",
        "কোনটি লোহিত শৈবাল?",
        ["Ulothrix sp.", "Polysiphonia sp.", "Chaetophora sp.", "Volvox sp."],
        ["Ulothrix sp.", "Polysiphonia sp.", "Chaetophora sp.", "Volvox sp."],
        "B", "easy", "factual",
        "Polysiphonia is a classic red alga (Rhodophyta); the others are green algae.",
        "Polysiphonia ক্লাসিক লোহিত শৈবাল (Rhodophyta); বাকিগুলো সবুজ শৈবাল।",
    ),
    q(
        "What is the chief stored food in green algae?",
        "সবুজ শৈবালে কোন খাদ্য সঞ্চিত থাকে?",
        ["Starch", "Cyanophycean starch", "Floridean starch", "Laminarin"],
        ["স্টার্চ", "সায়ানোফাইসিয়ান স্টার্চ", "ফ্লোরিডিয়ান স্টার্চ", "ল্যামিনারিন"],
        "A", "easy", "factual",
        "Green algae store true starch; floridean starch is in red algae and laminarin in brown algae.",
        "সবুজ শৈবালে সত্য স্টার্চ সঞ্চিত হয়; ফ্লোরিডিয়ান স্টার্চ লোহিত এবং ল্যামিনারিন বাদামি শৈবালে থাকে।",
    ),
    q(
        "Floridean starch is characteristic of:",
        "ফ্লোরিডিয়ান স্টার্চ কোন শ্রেণির বৈশিষ্ট্য?",
        ["Green algae", "Blue-green algae", "Red algae", "Brown algae"],
        ["সবুজ শৈবাল", "নীলাভ সবুজ শৈবাল", "লোহিত শৈবাল", "বাদামি শৈবাল"],
        "C", "easy", "factual",
        "Red algae store floridean starch; brown algae store laminarin.",
        "লোহিত শৈবালে ফ্লোরিডিয়ান স্টার্চ এবং বাদামি শৈবালে ল্যামিনারিন সঞ্চিত হয়।",
    ),
    q(
        "Agar-agar is commercially obtained mainly from:",
        "নিচের কোনটি থেকে এগার-এগার পাওয়া যায়?",
        ["Green algae", "Fire algae (dinoflagellates)", "Brown algae", "Red algae"],
        ["সবুজ শৈবাল", "অগ্নি শৈবাল", "বাদামি শৈবাল", "লোহিত শৈবাল"],
        "D", "easy", "factual",
        "Agar is extracted chiefly from red algae such as Gelidium and Gracilaria.",
        "এগার প্রধানত Gelidium, Gracilaria প্রভৃতি লোহিত শৈবাল থেকে পাওয়া যায়।",
    ),
    q(
        "The shape of the Ulothrix chloroplast is typically:",
        "Ulothrix-এর ক্লোরোপ্লাস্টের আকৃতি কোনটি?",
        ["Cup-shaped", "Reticulate", "Spiral", "Girdle-shaped (band-like)"],
        ["পেয়ালা আকৃতির", "জালিকাকার", "সর্পিলাকার", "গার্ডল/বেল্ট সদৃশ"],
        "D", "medium", "factual",
        "Ulothrix has a girdle- or band-shaped chloroplast; Chlamydomonas is cup-shaped and Spirogyra is spiral.",
        "Ulothrix-এর ক্লোরোপ্লাস্ট গার্ডল/বেল্ট সদৃশ; Chlamydomonas পেয়ালা এবং Spirogyra সর্পিলাকার।",
    ),
    q(
        "The basal cell of Ulothrix is known as the holdfast. Which statement set is correct? (i) called holdfast (ii) usually does not divide (iii) colorless and lacks chlorophyll",
        "Ulothrix শৈবালের পাদদেশীয় কোষটি সম্পর্কে সঠিক— (i) হোল্ডফাস্ট নামে পরিচিত (ii) সাধারণত বিভাজন করে না (iii) সূত্রাকার ও ক্লোরোফিলবিহীন",
        ["(iii) only", "(ii) only", "(i) and (ii)", "(i), (ii) and (iii)"],
        ["কেবল (iii)", "কেবল (ii)", "(i) ও (ii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "The basal holdfast anchors the filament, is non-dividing, and lacks chlorophyll.",
        "পাদদেশীয় হোল্ডফাস্ট সূত্রকে আটকে রাখে, বিভাজন করে না এবং ক্লোরোফিলবিহীন।",
    ),
    q(
        "Which alga commonly shows the palmella stage?",
        "পামেলা দশা সৃষ্টিকারী শৈবাল কোনটি?",
        ["Chlamydomonas", "Volvox", "Chlorococcus", "Vaucheria"],
        ["Chlamydomonas", "Volvox", "Chlorococcus", "Vaucheria"],
        "A", "medium", "factual",
        "Under unfavorable conditions Chlamydomonas may enter a gelatinous palmella stage; Ulothrix can also show it.",
        "প্রতিকূল অবস্থায় Chlamydomonas জেলাটিনাস পামেলা দশায় যেতে পারে; Ulothrix-এও এ দশা দেখা যায়।",
    ),
    q(
        "Which organism among the following is haploid as the dominant vegetative phase?",
        "নিচের কোনটির প্রধান ভেজিটেটিভ দশা হ্যাপ্লয়েড?",
        ["Pteris sporophyte", "Ulothrix thallus", "Agaricus diploid basidium stage", "Cycas sporophyte"],
        ["Pteris স্পোরোফাইট", "Ulothrix থ্যালাস", "Agaricus ডিপ্লয়েড ব্যাসিডিয়াম দশা", "Cycas স্পোরোফাইট"],
        "B", "medium", "conceptual",
        "The Ulothrix thallus is haploid; fern and cycad sporophytes are diploid.",
        "Ulothrix থ্যালাস হ্যাপ্লয়েড; ফার্ন ও সাইকাসের স্পোরোফাইট ডিপ্লয়েড।",
    ),
    q(
        "Water bloom in ponds is mainly caused by excessive growth of:",
        "ওয়াটার ব্লুমের প্রধান কারণ কোন জীবগোষ্ঠীর অতিমাত্রায় বৃদ্ধি?",
        ["Red algae only", "Brown algae only", "Cyanobacteria (blue-green algae)", "Mosses"],
        ["কেবল লোহিত শৈবাল", "কেবল বাদামি শৈবাল", "সায়ানোব্যাকটেরিয়া (নীলাভ সবুজ শৈবাল)", "মস"],
        "C", "easy", "factual",
        "Nutrient enrichment favors Oscillatoria, Nostoc, Microcystis and similar cyanobacteria, causing water bloom and fish kills.",
        "পুষ্টি বৃদ্ধিতে Oscillatoria, Nostoc, Microcystis প্রভৃতি সায়ানোব্যাকটেরিয়া অতিমাত্রায় বাড়ে এবং ওয়াটার ব্লুম ও মাছ মৃত্যু ঘটায়।",
    ),
    q(
        "Which stored food is typical of brown algae?",
        "বাদামি শৈবালের বৈশিষ্ট্যপূর্ণ সঞ্চিত খাদ্য কোনটি?",
        ["True starch", "Floridean starch", "Laminarin", "Glycogen"],
        ["সত্য স্টার্চ", "ফ্লোরিডিয়ান স্টার্চ", "ল্যামিনারিন", "গ্লাইকোজেন"],
        "C", "easy", "factual",
        "Brown algae store laminarin (and often mannitol); glycogen is typical of fungi.",
        "বাদামি শৈবালে ল্যামিনারিন (ও প্রায়শই ম্যানিটল) সঞ্চিত হয়; গ্লাইকোজেন ছত্রাকের বৈশিষ্ট্য।",
    ),
    q(
        "Chlorella is best described as:",
        "Chlorella-কে সর্বোত্তমভাবে বর্ণনা করা যায়—",
        [
            "A unicellular non-motile green alga",
            "A multicellular leaf-like alga",
            "A filamentous alga with holdfast",
            "A red alga producing agar",
        ],
        [
            "এককোষী নিশ্চল সবুজ শৈবাল",
            "বহুকোষী পাতাসদৃশ শৈবাল",
            "হোল্ডফাস্টযুক্ত ফিলামেন্টাস শৈবাল",
            "এগার উৎপাদনকারী লোহিত শৈবাল",
        ],
        "A", "easy", "factual",
        "Chlorella is a non-motile unicellular green alga widely used in HSC comparisons with Ulothrix and Ulva.",
        "Chlorella নিশ্চল এককোষী সবুজ শৈবাল; HSC তুলনায় Ulothrix ও Ulva-এর সঙ্গে আলোচিত হয়।",
    ),
    q(
        "Which pigment pair is especially associated with red algae?",
        "লোহিত শৈবালের সঙ্গে বিশেষভাবে যুক্ত বর্ণকণিকা জোড় কোনটি?",
        [
            "Chlorophyll a and b only",
            "Phycoerythrin and phycocyanin (with chlorophyll a)",
            "Fucoxanthin only without chlorophyll",
            "Bacteriochlorophyll only",
        ],
        [
            "কেবল ক্লোরোফিল a ও b",
            "ফাইকোএরিথ্রিন ও ফাইকোসায়ানিন (ক্লোরোফিল a সহ)",
            "ক্লোরোফিল ছাড়া কেবল ফুকোজ্যানথিন",
            "কেবল ব্যাকটেরিওক্লোরোফিল",
        ],
        "B", "medium", "factual",
        "Red algae contain chlorophyll a plus phycobilins (phycoerythrin, phycocyanin) that give the red color.",
        "লোহিত শৈবালে ক্লোরোফিল a-এর সঙ্গে ফাইকোবিলিন (ফাইকোএরিথ্রিন, ফাইকোসায়ানিন) থাকে যা লাল বর্ণ দেয়।",
    ),
    q(
        "Ulothrix is morphologically:",
        "Ulothrix অঙ্গসংস্থানিকভাবে—",
        [
            "An unbranched filamentous green alga",
            "A colonial spherical alga like Volvox",
            "A coenocytic tube like Vaucheria only",
            "A mushroom fruit body",
        ],
        [
            "অশাখ ফিলামেন্টাস সবুজ শৈবাল",
            "Volvox-সদৃশ কলোনিয়াল গোলাকার শৈবাল",
            "কেবল Vaucheria-সদৃশ সিনোসাইটিক নল",
            "মাশরুমের ফ্রুটবডি",
        ],
        "A", "easy", "factual",
        "Ulothrix forms unbranched green filaments attached by a basal holdfast.",
        "Ulothrix পাদদেশীয় হোল্ডফাস্ট দিয়ে আটকানো অশাখ সবুজ সূত্র গঠন করে।",
    ),
    q(
        "Which statement about algal cell walls is generally correct for green algae?",
        "সবুজ শৈবালের কোষপ্রাচীর সম্পর্কে সাধারণত সঠিক কোনটি?",
        [
            "Chiefly chitin like fungi",
            "Chiefly cellulose",
            "Only peptidoglycan",
            "Only silica frustules in all green algae",
        ],
        [
            "ছত্রাকের মতো প্রধানত কাইটিন",
            "প্রধানত সেলুলোজ",
            "কেবল পেপটিডোগ্লাইকান",
            "সব সবুজ শৈবালে কেবল সিলিকা ফ্রাস্টুল",
        ],
        "B", "easy", "conceptual",
        "Most green algae have cellulose walls; fungal walls are chitinous, and silica frustules characterize diatoms.",
        "অধিকাংশ সবুজ শৈবালের প্রাচীর সেলুলোজী; ছত্রাকে কাইটিন এবং সিলিকা ফ্রাস্টুল ডায়াটমের বৈশিষ্ট্য।",
    ),
]


# --- t02: Fungi / ছত্রাক ---
T02 = [
    q(
        "The main component of the fungal cell wall is:",
        "ছত্রাকের কোষপ্রাচীরের প্রধান উপাদান কোনটি?",
        ["Chitin", "Cellulose", "Starch", "Glycogen"],
        ["কাইটিন", "সেলুলোজ", "স্টার্চ", "গ্লাইকোজেন"],
        "A", "easy", "factual",
        "Fungal walls are largely chitin; glycogen is the stored food, not the wall polymer.",
        "ছত্রাকের প্রাচীর প্রধানত কাইটিন; গ্লাইকোজেন সঞ্চিত খাদ্য, প্রাচীরের পলিমার নয়।",
    ),
    q(
        "Which is a general characteristic of fungi?",
        "ছত্রাকের সাধারণ বৈশিষ্ট্য কোনটি?",
        [
            "Dependence on light for photosynthesis",
            "Multicellular sex organs like higher plants always",
            "Cell wall made of peptidoglycan",
            "Cell wall made of chitin",
        ],
        [
            "সালোকসংশ্লেষের জন্য আলোর উপর নির্ভরশীল",
            "উচ্চতর উদ্ভিদের মতো সবসময় বহুকোষী জননাঙ্গ",
            "কোষপ্রাচীর পেপটিডোগ্লাইকান নির্মিত",
            "কোষপ্রাচীর কাইটিন নির্মিত",
        ],
        "D", "easy", "factual",
        "Fungi are heterotrophs with chitinous walls; they are not photosynthetic.",
        "ছত্রাক পরভোজী এবং কাইটিন প্রাচীরবিশিষ্ট; এরা সালোকসংশ্লেষী নয়।",
    ),
    q(
        "The pathogen of late blight of potato is:",
        "গোলআলুর বিলম্বিত ধ্বসা রোগের প্যাথোজেন কোনটি?",
        ["Trichophyton", "Microsporum", "Phytophthora", "Xanthomonas"],
        ["Trichophyton", "Microsporum", "Phytophthora", "Xanthomonas"],
        "C", "easy", "factual",
        "Phytophthora infestans causes late blight of potato; Trichophyton/Microsporum are dermatophytes.",
        "Phytophthora infestans গোলআলুর বিলম্বিত ধ্বসা ঘটায়; Trichophyton/Microsporum ত্বকসংক্রান্ত ছত্রাক।",
    ),
    q(
        "Which of the following is part of the Agaricus fruit body?",
        "কোনটি Agaricus-এর ফ্রুটবডির অংশ?",
        ["Indusium", "Annulus", "Stomium", "Rhizomorph"],
        ["ইন্ডোসিয়াম", "অ্যানুলাস", "স্টোমিয়াম", "রাইজোমর্ফ"],
        "B", "easy", "factual",
        "The annulus (ring) on the stipe is a classic part of the Agaricus basidiocarp; indusium/stomium are fern terms.",
        "স্টাইপের অ্যানুলাস (বলয়) Agaricus ব্যাসিডিওকার্পের ক্লাসিক অংশ; ইন্ডোসিয়াম/স্টোমিয়াম ফার্নের পরিভাষা।",
    ),
    q(
        "The umbrella-like part of Agaricus is called the:",
        "Agaricus-এর ছাতার মতো অংশের নাম কী?",
        ["Mycelium", "Stipe", "Rhizomorph", "Pileus"],
        ["মাইসেলিয়াম", "স্টাইপ", "রাইজোমর্ফ", "পাইলিয়াস"],
        "D", "easy", "factual",
        "The pileus is the cap; the stipe is the stalk supporting it.",
        "পাইলিয়াস হলো টুপি/ছাতা অংশ; স্টাইপ তা ধরে রাখা দণ্ড।",
    ),
    q(
        "The fruiting body of Agaricus is called a:",
        "Agaricus-এর ফলদেহের নাম কী?",
        ["Basidiocarp", "Conidiophore", "Ascocarp", "Rhizomorph"],
        ["ব্যাসিডিওকার্প", "কনিডিওফোর", "অ্যাসকোকার্প", "রাইজোমর্ফ"],
        "A", "easy", "factual",
        "Agaricus produces a basidiocarp; ascocarps belong to ascomycetes such as Penicillium/Aspergillus sexual stages.",
        "Agaricus ব্যাসিডিওকার্প তৈরি করে; অ্যাসকোকার্প অ্যাসকোমাইসিটিসের (যেমন Penicillium-এর যৌন দশা)।",
    ),
    q(
        "Which fungus is aquatic?",
        "কোন ছত্রাকটি জলজ?",
        ["Saprolegnia", "Rhizopus", "Aspergillus", "Cercospora"],
        ["Saprolegnia", "Rhizopus", "Aspergillus", "Cercospora"],
        "A", "easy", "factual",
        "Saprolegnia is a water mold; Rhizopus and Aspergillus are common terrestrial molds.",
        "Saprolegnia জলজ ছত্রাক (ওয়াটার মোল্ড); Rhizopus ও Aspergillus স্থলজ ছত্রাক।",
    ),
    q(
        "The absorbing organ of a parasitic fungus is the:",
        "পরজীবী ছত্রাকের চোষক অঙ্গ হিসেবে ব্যবহৃত হয় কোনটি?",
        ["Rhizomorph", "Stipe", "Sorus", "Haustorium"],
        ["রাইজোমর্ফ", "স্টাইপ", "সোরাস", "হস্টোরিয়াম"],
        "D", "easy", "factual",
        "Haustoria penetrate host cells to absorb nutrients; the stipe is a mushroom stalk.",
        "হস্টোরিয়াম পোষক কোষে প্রবেশ করে পুষ্টি শোষণ করে; স্টাইপ মাশরুমের দণ্ড।",
    ),
    q(
        "Which fungus has coenocytic mycelium?",
        "কোন ছত্রাকে সিনোসাইটিক মাইসেলিয়াম থাকে?",
        ["Penicillium", "Agaricus", "Aspergillus", "Mucor"],
        ["Penicillium", "Agaricus", "Aspergillus", "Mucor"],
        "D", "medium", "factual",
        "Mucor (and Saprolegnia) have aseptate, multinucleate coenocytic hyphae; Penicillium/Aspergillus are septate.",
        "Mucor (ও Saprolegnia) প্রস্থপ্রাচীরবিহীন বহুনিউক্লিয়াসযুক্ত সিনোসাইটিক হাইফিবিশিষ্ট; Penicillium/Aspergillus সেপ্টেট।",
    ),
    q(
        "Coenocytic mycelium means hyphae that are:",
        "সিনোসাইটিক মাইসেলিয়াম বলতে বোঝায় হাইফি যা—",
        [
            "Septate with one nucleus per cell only",
            "Aseptate and multinucleate",
            "Always diploid throughout",
            "Made only of cellulose walls",
        ],
        [
            "সেপ্টেট এবং প্রতি কোষে কেবল এক নিউক্লিয়াস",
            "অ্যাসেপ্টেট ও বহুনিউক্লিয়াসযুক্ত",
            "সর্বদা সম্পূর্ণ ডিপ্লয়েড",
            "কেবল সেলুলোজ প্রাচীরবিশিষ্ট",
        ],
        "B", "medium", "conceptual",
        "In coenocytic mycelia, cross-walls are absent or rare so many nuclei share continuous cytoplasm (e.g., Saprolegnia).",
        "সিনোসাইটিক মাইসেলিয়ামে প্রস্থপ্রাচীর না থাকায় একটানা সাইটোপ্লাজমে অনেক নিউক্লিয়াস থাকে (যেমন Saprolegnia)।",
    ),
    q(
        "Which organism stores glycogen as reserve food?",
        "কোন জীবের সঞ্চিত খাদ্য গ্লাইকোজেন?",
        ["Moss", "Fern", "Alga", "Fungus"],
        ["মস", "ফার্ন", "শৈবাল", "ছত্রাক"],
        "D", "easy", "factual",
        "Fungi store glycogen (animal starch); green algae store starch.",
        "ছত্রাকে গ্লাইকোজেন সঞ্চিত হয়; সবুজ শৈবালে স্টার্চ থাকে।",
    ),
    q(
        "Which plant produces basidiospores?",
        "কোন উদ্ভিদ ব্যাসিডিওস্পোর তৈরি করে?",
        ["Pteris sp.", "Penicillium sp.", "Agaricus sp.", "Riccia sp."],
        ["Pteris sp.", "Penicillium sp.", "Agaricus sp.", "Riccia sp."],
        "C", "easy", "factual",
        "Agaricus is a basidiomycete; Penicillium is an ascomycete producing conidia/ascospores.",
        "Agaricus ব্যাসিডিওমাইসিটিস; Penicillium অ্যাসকোমাইসিটিস যা কনিডিয়া/অ্যাস্কোস্পোর তৈরি করে।",
    ),
    q(
        "Basidia of Agaricus develop on the:",
        "Agaricus-এর ব্যাসিডিয়াম কোন অংশে উৎপন্ন হয়?",
        ["Stipe", "Annulus", "Pileus tissue only without gills", "Gills (lamellae)"],
        ["স্টাইপ", "অ্যানুলাস", "গিল ছাড়া কেবল পাইলিয়াস কলা", "গিল (ল্যামেলি)"],
        "D", "easy", "factual",
        "Fertile basidia line the gill surfaces (lamellae) beneath the pileus.",
        "উর্বর ব্যাসিডিয়াম পাইলিয়াসের নিচের গিল/ল্যামেলির তলে সজ্জিত থাকে।",
    ),
    q(
        "How many basidiospores typically arise from each basidium of Agaricus?",
        "Agaricus-এর প্রতিটি ব্যাসিডিয়াম থেকে সাধারণত কতটি ব্যাসিডিওস্পোর উৎপন্ন হয়?",
        ["Two", "Three", "Four", "Eight"],
        ["দুইটি", "তিনটি", "চারটি", "আটটি"],
        "C", "easy", "factual",
        "Each basidium usually produces four basidiospores after meiosis.",
        "মিয়োসিসের পর প্রতিটি ব্যাসিডিয়াম থেকে সাধারণত চারটি ব্যাসিডিওস্পোর উৎপন্ন হয়।",
    ),
    q(
        "The stored material commonly cited for fungal conidia in HSC texts is:",
        "HSC পাঠে ছত্রাকের কনিডিয়ার সঞ্চিত বস্তু হিসেবে উল্লেখিত হয়—",
        ["Cellulose", "Glycogen", "Oil droplets only in all cases", "Starch"],
        ["সেলুলোজ", "গ্লাইকোজেন", "সব ক্ষেত্রে কেবল তেলবিন্দু", "স্টার্চ"],
        "B", "medium", "factual",
        "Board items commonly key glycogen as the reserve associated with fungal conidia/mycelium.",
        "বোর্ড/উদ্ভাস আইটেমে ছত্রাকের কনিডিয়া/মাইসেলিয়ামের সঞ্চিত বস্তু হিসেবে গ্লাইকোজেন ধরা হয়।",
    ),
    q(
        "Among the following, which is treated as a diploid organism in board MCQs of this chapter set?",
        "এ অধ্যায়ের বোর্ড MCQ সেটে ডিপ্লয়েড জীব হিসেবে ধরা হয় কোনটি?",
        ["Riccia gametophyte", "Ulothrix thallus", "Agaricus (post-karyogamy stage emphasized)", "Chlamydomonas vegetative cell"],
        ["Riccia গ্যামিটোফাইট", "Ulothrix থ্যালাস", "Agaricus (ক্যারিওগ্যামির পরের দশা)", "Chlamydomonas ভেজিটেটিভ কোষ"],
        "C", "hard", "conceptual",
        "Ulothrix/Riccia vegetative phases are haploid; board keys in this set mark Agaricus as the diploid example after karyogamy in basidia.",
        "Ulothrix/Riccia-এর ভেজিটেটিভ দশা হ্যাপ্লয়েড; এ সেটের বোর্ড কী-তে ব্যাসিডিয়ামে ক্যারিওগ্যামির পর Agaricus ডিপ্লয়েড উদাহরণ হিসেবে চিহ্নিত।",
    ),
    q(
        "Rhizopus differs from Saprolegnia mainly in being:",
        "Saprolegnia থেকে Rhizopus-এর প্রধান পার্থক্য হলো এটি—",
        [
            "Typically terrestrial (bread mold) rather than aquatic",
            "A photosynthetic green alga",
            "A vascular fern",
            "A lichen mycobiont only",
        ],
        [
            "জলজের বদলে সাধারণত স্থলজ (ব্রেড মোল্ড)",
            "সালোকসংশ্লেষী সবুজ শৈবাল",
            "পরিবহন টিস্যুযুক্ত ফার্ন",
            "কেবল লাইকেনের মাইকোবায়োন্ট",
        ],
        "A", "medium", "conceptual",
        "Rhizopus is a common terrestrial zygomycete mold; Saprolegnia is aquatic.",
        "Rhizopus সাধারণ স্থলজ জাইগোমাইসিট ছত্রাক; Saprolegnia জলজ।",
    ),
    q(
        "Which structure is the stalk of a mushroom fruit body?",
        "মাশরুম ফ্রুটবডির দণ্ড অংশ কোনটি?",
        ["Pileus", "Gill", "Stipe", "Basidium"],
        ["পাইলিয়াস", "গিল", "স্টাইপ", "ব্যাসিডিয়াম"],
        "C", "easy", "factual",
        "The stipe elevates the pileus; gills bear basidia under the cap.",
        "স্টাইপ পাইলিয়াসকে উঁচু করে রাখে; গিলে ব্যাসিডিয়াম থাকে।",
    ),
    q(
        "Which of the following has true vascular (conducting) tissue?",
        "নিচের কোনটি পরিবহন টিস্যুযুক্ত জীব?",
        ["Ulothrix sp.", "Pteris sp.", "Riccia sp.", "Agaricus sp."],
        ["Ulothrix sp.", "Pteris sp.", "Riccia sp.", "Agaricus sp."],
        "B", "medium", "conceptual",
        "Pteris is a vascular fern; Ulothrix, Riccia and Agaricus lack true xylem/phloem.",
        "Pteris পরিবহন টিস্যুযুক্ত ফার্ন; Ulothrix, Riccia ও Agaricus-এ সত্য জাইলেম/ফ্লোয়েম নেই।",
    ),
    q(
        "Aspergillus and Penicillium hyphae are generally:",
        "Aspergillus ও Penicillium-এর হাইফি সাধারণত—",
        [
            "Septate (with cross-walls)",
            "Always coenocytic like Mucor",
            "Absent; they are unicellular algae",
            "Made of cellulose only",
        ],
        [
            "সেপ্টেট (প্রস্থপ্রাচীরযুক্ত)",
            "Mucor-এর মতো সবসময় সিনোসাইটিক",
            "অনুপস্থিত; এরা এককোষী শৈবাল",
            "কেবল সেলুলোজ নির্মিত",
        ],
        "A", "medium", "factual",
        "These ascomycete molds have septate mycelia, unlike the coenocytic Mucor type.",
        "এই অ্যাসকোমাইসিট ছত্রাকের মাইসেলিয়াম সেপ্টেট; Mucor ধরনের সিনোসাইটিক নয়।",
    ),
]


# --- t03: Reproduction and importance / প্রজনন ও গুরুত্ব ---
T03 = [
    q(
        "A flagellated spore is called a:",
        "ফ্লাজেলাবাহী স্পোরকে কী বলে?",
        ["Aplanospore", "Hypnospore", "Akinete", "Zoospore"],
        ["অ্যাপ্ল্যানোস্পোর", "হিপনোস্পোর", "অ্যাকাইনিট", "জুস্পোর"],
        "D", "easy", "factual",
        "Zoospores are motile flagellated spores; aplanospores are non-motile.",
        "জুস্পোর সচল ফ্লাজেলাযুক্ত স্পোর; অ্যাপ্ল্যানোস্পোর নিশ্চল।",
    ),
    q(
        "An aplanospore is best described as:",
        "অ্যাপ্ল্যানোস্পোর হলো—",
        [
            "A flagellated swimming spore",
            "A non-flagellated non-motile spore",
            "A fungal basidiospore only",
            "A diploid zygote of ferns",
        ],
        [
            "ফ্লাজেলাযুক্ত সাঁতারু স্পোর",
            "ফ্লাজেলাবিহীন নিশ্চল স্পোর",
            "কেবল ছত্রাকের ব্যাসিডিওস্পোর",
            "ফার্নের ডিপ্লয়েড জাইগোট",
        ],
        "B", "easy", "factual",
        "When water is scarce, spores may form without flagella as aplanospores.",
        "পানির অভাবে স্পোর ফ্লাজেলা তৈরি না করে অ্যাপ্ল্যানোস্পোরে পরিণত হতে পারে।",
    ),
    q(
        "Which is an asexual reproductive structure/method in algae among the options?",
        "কোনটি শৈবালের অযৌন জনন?",
        ["Hormogonia", "Fragmentation only as sexual fusion", "Budding of yeast only", "Zoospore"],
        ["হরমোগোনিয়া", "কেবল যৌন মিলনরূপ খণ্ডায়ন", "কেবল ইস্টের বাডিং", "জুস্পোর"],
        "D", "medium", "factual",
        "Zoospore formation is classic algal asexual reproduction; hormogonia are cyanobacterial fragments.",
        "জুস্পোর গঠন শৈবালের ক্লাসিক অযৌন জনন; হরমোগোনিয়া সায়ানোব্যাকটেরিয়ার খণ্ড।",
    ),
    q(
        "Vegetative reproduction in multicellular filamentous algae commonly occurs by:",
        "বহুকোষী ফিলামেন্টাস শৈবালের অঙ্গজ জননে সাধারণত ঘটে—",
        ["Only binary fission of the whole plant", "Fragmentation", "Only conjugation of gametes", "Only basidiospore formation"],
        ["সমগ্র উদ্ভিদের কেবল দ্বিবিভাজন", "খণ্ডায়ন", "কেবল গ্যামিট সংযুগ", "কেবল ব্যাসিডিওস্পোর গঠন"],
        "B", "easy", "factual",
        "Filaments break into fragments that regenerate new filaments.",
        "সূত্র খণ্ডিত হয়ে নতুন সূত্রে পরিণত হয়।",
    ),
    q(
        "Ulothrix shows which type of gamete fusion?",
        "Ulothrix sp.-এ কোন প্রকার গ্যামিটের মিলন?",
        ["Isogamous", "Anisogamous", "Oogamous", "Gametogenesis only without fusion"],
        ["আইসোগ্যামাস", "অ্যানাইসোগ্যামাস", "উগ্যামাস", "মিলন ছাড়া কেবল গ্যামিটোজেনেসিস"],
        "A", "easy", "factual",
        "Ulothrix gametes are morphologically similar (isogamy), as explained in board short answers.",
        "Ulothrix-এর গ্যামিট বাহ্যিকভাবে সমরূপ (আইসোগ্যামি)—বোর্ড সংক্ষিপ্ত উত্তরে উল্লেখিত।",
    ),
    q(
        "Fertilization in Ulothrix is completed:",
        "Ulothrix-এর নিষেক সম্পন্ন হয়— (i) on ‘+’ thallus (ii) on ‘−’ thallus (iii) outside the thallus. Which is correct?",
        ["(i) only", "(ii) only", "(iii) only", "(i) and (ii)"],
        ["কেবল (i)", "কেবল (ii)", "কেবল (iii)", "(i) ও (ii)"],
        "C", "medium", "conceptual",
        "Isogametes fuse in the surrounding water, so syngamy occurs outside the thallus.",
        "আইসোগ্যামিট পার্শ্ববর্তী পানিতে মিলিত হয় বলে নিষেক থ্যালাসের বাইরে সম্পন্ন হয়।",
    ),
    q(
        "How many flagella does a typical Ulothrix asexual zoospore have?",
        "Ulothrix-এর অযৌন জুস্পোরে সাধারণত কতটি ফ্লাজেলা থাকে?",
        ["One", "Two", "Three", "Four"],
        ["১টি", "২টি", "৩টি", "৪টি"],
        "D", "medium", "factual",
        "HSC texts describe Ulothrix zoospores as quadriflagellate; gametes are biflagellate.",
        "HSC পাঠে Ulothrix জুস্পোর চার-ফ্লাজেলাযুক্ত; গ্যামিট দ্বি-ফ্লাজেলাযুক্ত।",
    ),
    q(
        "Isogamy means sexual fusion in which:",
        "আইসোগ্যামী বলতে বোঝায় যৌন মিলন যেখানে—",
        [
            "Male and female gametes are morphologically alike",
            "One gamete is large and non-motile only",
            "No gametes are formed",
            "Only spores fuse without nuclei",
        ],
        [
            "স্ত্রী ও পুরুষ গ্যামিট বাহ্যিকভাবে সমরূপ",
            "এক গ্যামিট কেবল বড় ও নিশ্চল",
            "কোনো গ্যামিট গঠিত হয় না",
            "নিউক্লিয়াস ছাড়া কেবল স্পোর মিলিত হয়",
        ],
        "A", "easy", "conceptual",
        "In isogamy, fusing gametes look alike (e.g., Ulothrix); oogamy has a large non-motile egg.",
        "আইসোগ্যামিতে মিলনকারী গ্যামিট সমরূপ (যেমন Ulothrix); উগ্যামিতে বড় নিশ্চল ডিম্বাণু থাকে।",
    ),
    q(
        "Sexual reproduction in fungi typically involves how many major steps?",
        "ছত্রাকের যৌন জননের ধাপ কয়টি?",
        ["Two", "Three", "Four", "Five"],
        ["২টি", "৩টি", "৪টি", "৫টি"],
        "B", "medium", "factual",
        "The three steps are plasmogamy, karyogamy and meiosis.",
        "তিন ধাপ: প্লাজমোগ্যামি, ক্যারিওগ্যামি ও মিয়োসিস।",
    ),
    q(
        "Lichen is the symbiotic association of:",
        "লাইকেন কোনটির সহাবস্থান?",
        ["Alga–moss", "Fungus–alga", "Moss–fungus only without alga", "Alga–fern"],
        ["শৈবাল–মস", "ছত্রাক–শৈবাল", "শৈবাল ছাড়া কেবল মস–ছত্রাক", "শৈবাল–ফার্ন"],
        "B", "easy", "factual",
        "A lichen combines a mycobiont (fungus) and a photobiont (alga or cyanobacterium).",
        "লাইকেনে মাইকোবায়োন্ট (ছত্রাক) ও ফটোবায়োন্ট (শৈবাল বা সায়ানোব্যাকটেরিয়া) থাকে।",
    ),
    q(
        "The relationship between alga and fungus in a lichen is called:",
        "লাইকেনে শৈবাল ও ছত্রাকের সম্পর্ককে কী বলে?",
        ["Saprophytism", "Symbiosis (mutualism)", "Parasitism only", "Autotrophism of the fungus"],
        ["মৃতজীবিতা", "মিথোজীবিতা", "কেবল পরজীবিতা", "ছত্রাকের স্বভোজিতা"],
        "B", "easy", "factual",
        "Both partners benefit: the alga photosynthesizes and the fungus provides shelter/minerals.",
        "উভয়ে উপকৃত: শৈবাল সালোকসংশ্লেষ করে এবং ছত্রাক আশ্রয়/খনিজ যোগায়।",
    ),
    q(
        "An attractive hanging (shrubby) lichen type is:",
        "আকর্ষণীয় ও ঝুলন্ত লাইকেন কোনটি?",
        ["Crustose", "Fruticose", "Foliose", "Leprose"],
        ["ক্রাস্টোজ", "ফ্রুটিকোজ", "ফোলিয়োজ", "লেপ্রোজ"],
        "B", "easy", "factual",
        "Fruticose lichens are branched and often pendant; crustose are crust-like on the substrate.",
        "ফ্রুটিকোজ লাইকেন শাখান্বিত ও প্রায়শই ঝুলন্ত; ক্রাস্টোজ আবাসের উপর ক্রাস্টসদৃশ।",
    ),
    q(
        "Branched attractive lichens are termed:",
        "শাখা-প্রশাখাবিশিষ্ট আকর্ষণীয় লাইকেনকে কী বলে?",
        ["Leprose", "Foliose", "Fruticose", "Crustose"],
        ["লেপ্রোজ", "ফোলিয়োজ", "ফ্রুটিকোজ", "ক্রাস্টোজ"],
        "C", "easy", "factual",
        "Fruticose = shrubby/branched; foliose = leafy lobes; crustose = crust-like.",
        "ফ্রুটিকোজ = ঝোপসদৃশ/শাখান্বিত; ফোলিয়োজ = পাতাসদৃশ; ক্রাস্টোজ = ক্রাস্টসদৃশ।",
    ),
    q(
        "When air pollution rises, which organism absorbs pollutants and often dies, acting as an indicator?",
        "বায়ু দূষণ বৃদ্ধি পেলে কোন উদ্ভিদ দূষক শোষণ করে মরে যায় (সূচক হিসেবে)?",
        ["Alga only", "Fungus only", "Lichen", "Fern"],
        ["কেবল শৈবাল", "কেবল ছত্রাক", "লাইকেন", "ফার্ন"],
        "C", "easy", "application",
        "Lichens are sensitive bioindicators of air quality, especially SO₂ pollution.",
        "লাইকেন বায়ুর মানের (বিশেষত SO₂) সংবেদনশীল জৈবসূচক।",
    ),
    q(
        "Lichens are called cosmopolitan plants mainly because they:",
        "লাইকেনকে বিশ্বজনীন উদ্ভিদ বলা হয় প্রধানত কারণ এরা—",
        [
            "Grow only in deep oceans",
            "Can colonize extreme/bare habitats where few other plants survive",
            "Are always parasitic on ferns",
            "Photosynthesize without any partner",
        ],
        [
            "কেবল গভীর সমুদ্রে জন্মায়",
            "চরম/বন্ধ্যা আবাসেও জন্মাতে পারে যেখানে অন্য জীব কম থাকে",
            "সবসময় ফার্নের উপর পরজীবী",
            "সঙ্গী ছাড়াই সালোকসংশ্লেষ করে",
        ],
        "B", "medium", "conceptual",
        "They grow on bark, rocks, sterile soil, walls and even in tundra-like extremes.",
        "এরা বাকল, পাথর, বন্ধ্যা মাটি, দেয়াল এমনকি তুন্দ্রা-সদৃশ চরম পরিবেশেও জন্মায়।",
    ),
    q(
        "In a lichen, the fungal partner typically:",
        "লাইকেনের ক্ষেত্রে ছত্রাক সাধারণত— (i) supplies minerals (ii) may aid structure/reproduction housing (iii) forms rhizines. Which is correct?",
        ["(i) only", "(i) and (iii)", "(ii) only", "(i), (ii) and (iii)"],
        ["কেবল (i)", "(i) ও (iii)", "কেবল (ii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "The mycobiont anchors with rhizines and supplies water/minerals while sheltering the photobiont.",
        "মাইকোবায়োন্ট রাইজাইন দিয়ে আটকে থাকে, পানি/খনিজ দেয় এবং ফটোবায়োন্টকে আশ্রয় দেয়।",
    ),
    q(
        "Which distinguishing features separate algae from fungi? (i) stored food (ii) pigments (iii) cell-wall composition",
        "শৈবাল ও ছত্রাকের পার্থক্যকারী উপাদান— (i) সঞ্চিত খাদ্য (ii) বর্ণকণিকা (iii) কোষপ্রাচীরের গঠন",
        ["(i) and (ii) only", "(i), (ii) and (iii)", "(ii) and (iii) only", "(i) and (iii) only"],
        ["কেবল (i) ও (ii)", "(i), (ii) ও (iii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)"],
        "B", "medium", "conceptual",
        "Algae are pigmented autotrophs with cellulose walls and starch-type reserves; fungi are heterotrophs with chitin and glycogen.",
        "শৈবাল বর্ণকণিকায়ুক্ত স্বভোজী, সেলুলোজ প্রাচীর ও স্টার্চ-জাতীয় সঞ্চয়ী; ছত্রাক পরভোজী, কাইটিন ও গ্লাইকোজেনযুক্ত।",
    ),
    q(
        "Edible mushrooms (Agaricus) are valued nutritionally mainly for:",
        "খাদ্য হিসেবে মাশরুম (Agaricus) পুষ্টিগতভাবে মূল্যবান প্রধানত—",
        [
            "Protein and vitamins",
            "Only cellulose fiber with no protein",
            "Only floridean starch",
            "Only chlorophyll pigments",
        ],
        [
            "প্রোটিন ও ভিটামিন",
            "প্রোটিন ছাড়া কেবল সেলুলোজ আঁশ",
            "কেবল ফ্লোরিডিয়ান স্টার্চ",
            "কেবল ক্লোরোফিল বর্ণকণিকা",
        ],
        "A", "easy", "application",
        "Board stimulus items emphasize mushroom protein and vitamins supporting health.",
        "বোর্ড উদ্দীপক আইটেমে মাশরুমের প্রোটিন ও ভিটামিন স্বাস্থ্যসহায়ক হিসেবে গুরুত্ব পায়।",
    ),
    q(
        "Examples of mutualism include: (i) lichen (ii) coralloid roots (iii) root nodules",
        "মিথোজীবিতার উদাহরণ হলো— (i) লাইকেন (ii) কোরালয়েড মূল (iii) নডিউল",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "Lichen, Cycas coralloid roots with cyanobacteria, and legume Rhizobium nodules are mutualistic.",
        "লাইকেন, সাইকাসের কোরালয়েড মূলে সায়ানোব্যাকটেরিয়া এবং শিম্বে Rhizobium নডিউল মিথোজীবী।",
    ),
    q(
        "Algae and fungi together form which of the following?",
        "শৈবাল ও ছত্রাক সম্মিলিতভাবে নিচের কোনটি তৈরি করে?",
        ["Pteridophyta", "Bryophyta", "Bacteria", "Lichen"],
        ["টেরিডোফাইটা", "ব্রায়োফাইটা", "ব্যাকটেরিয়া", "লাইকেন"],
        "D", "easy", "factual",
        "Their stable symbiotic thallus is called a lichen, not a moss or fern group.",
        "তাদের স্থায়ী মিথোজীবী থ্যালাসকে লাইকেন বলে; এটি মস বা ফার্ন গোষ্ঠী নয়।",
    ),
]


TOPICS_MAP = {
    "bio1_27_ch05_t01": T01,
    "bio1_27_ch05_t02": T02,
    "bio1_27_ch05_t03": T03,
}


def write_topic(topic_id: str, rows: list[dict]) -> None:
    assert len(rows) == 20, f"{topic_id}: expected 20, got {len(rows)}"
    for i, row in enumerate(rows, 1):
        err = validate_record(row)
        if err:
            raise SystemExit(f"{topic_id} Q{i}: {err}\n{json.dumps(row, ensure_ascii=False)}")
    stems = [r["stem_en"] for r in rows]
    if len(stems) != len(set(map(str.casefold, stems))):
        raise SystemExit(f"{topic_id}: duplicate stem_en within topic")
    path = TOPICS / f"{topic_id}.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {path} ({len(rows)})")


def main() -> int:
    counts = {}
    for tid, rows in TOPICS_MAP.items():
        write_topic(tid, rows)
        counts[tid] = len(rows)

    all_stems: dict[str, str] = {}
    for tid, rows in TOPICS_MAP.items():
        for r in rows:
            key = r["stem_en"].casefold().strip()
            if key in all_stems:
                raise SystemExit(
                    f"duplicate stem across {all_stems[key]} and {tid}: {r['stem_en']}"
                )
            all_stems[key] = tid

    summary = {
        "chapter": "bio1_27_ch05",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p170_pdf176.png",
            "p171_pdf177.png",
            "p172_pdf178.png",
            "p173_pdf179.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio1_27_ch05_t01": {
                "title": "Algae / শৈবাল",
                "themes": [
                    "Ulva leaf-like; Chara nodes/internodes; Ulothrix filament",
                    "unicellular Navicula / motile Chlamydomonas / non-motile Chlorella",
                    "lithophyte habitat; pyrenoid in Ulothrix chloroplast",
                    "red alga Polysiphonia; pigments phycoerythrin/phycocyanin",
                    "storage: starch / floridean / laminarin; agar from red algae",
                    "Ulothrix girdle chloroplast; holdfast basal cell",
                    "palmella stage; water bloom cyanobacteria",
                    "cellulose wall vs fungal chitin contrast",
                ],
            },
            "bio1_27_ch05_t02": {
                "title": "Fungi / ছত্রাক",
                "themes": [
                    "chitin wall; heterotrophic nature",
                    "Phytophthora late blight of potato",
                    "Agaricus: annulus, pileus, basidiocarp, gills, 4 basidiospores",
                    "aquatic Saprolegnia; terrestrial Rhizopus",
                    "haustorium; coenocytic Mucor/Saprolegnia vs septate molds",
                    "glycogen reserve; Aspergillus/Penicillium septate",
                    "diploid keying of Agaricus in board set",
                    "non-vascular Agaricus vs vascular Pteris",
                ],
            },
            "bio1_27_ch05_t03": {
                "title": "Reproduction and importance / প্রজনন ও গুরুত্ব",
                "themes": [
                    "zoospore vs aplanospore; filament fragmentation",
                    "Ulothrix isogamy; external fertilization; 4-flagellate zoospore",
                    "fungal sexual steps: plasmogamy–karyogamy–meiosis",
                    "lichen = fungus+alga; fruticose vs crustose/foliose",
                    "lichen air-pollution indicator; cosmopolitan habitats",
                    "mycobiont minerals/rhizines; algae–fungi distinguishing traits",
                    "mushroom protein/vitamins; mutualism examples",
                    "alga+fungus → lichen (not bryophyte/pteridophyte)",
                ],
            },
        },
        "low_confidence": [
            "Only ~4 printed MCQ pages (p170–173); many stems reconstructed from noisy OCR and supplemented with accurate HSC-level bilingual items to reach 20/topic.",
            "Figure-only bank items (holdfast/gill labels, numbered anatomy) rewritten as standalone stems.",
            "Q on Agaricus as 'diploid' follows board/Udvash framing (karyogamy in basidium) rather than dikaryon nuance.",
            "Ulothrix zoospore flagella keyed as four per standard HSC texts; some OCR options showed ranges like 2–8.",
            "Conidia stored food keyed as glycogen matching common board explanations.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio1_27_ch05_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio1_27_ch05_t01": 20,
                "bio1_27_ch05_t02": 20,
                "bio1_27_ch05_t03": 20,
            },
        },
    }
    out = (
        ROOT
        / "content"
        / "bank"
        / "udvash_raw"
        / "biology_1"
        / "parsed"
        / "ch05_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
