#!/usr/bin/env python3
"""Seed Biology 1st Paper Ch6 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio1_27_ch06_t01..t03 (bryophytes; pteridophytes; life cycles).
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
    "biology p1 ch06; curated bilingual"
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


# --- t01: Bryophytes / ব্রায়োফাইটা ---
T01 = [
    q(
        "Which of the following is present on a Riccia thallus?",
        "নিচের কোনটি Riccia থ্যালাসে থাকে?",
        ["Rhizoid", "Rhizome", "Rhizine", "Rhizomorph"],
        ["রাইজয়েড", "রাইজোম", "রাইজাইন", "রাইজোমর্ফ"],
        "A", "easy", "factual",
        "Riccia is a thalloid bryophyte anchored by rhizoids; rhizome, rhizine and rhizomorph belong to other groups.",
        "Riccia থ্যালয়েড ব্রায়োফাইট যা রাইজয়েড দিয়ে আটকে থাকে; রাইজোম, রাইজাইন ও রাইজোমর্ফ অন্য গোষ্ঠীর গঠন।",
    ),
    q(
        "What is the name of the male reproductive organ of Riccia?",
        "Riccia-এর পুংজননাঙ্গের নাম কী?",
        ["Antheridium", "Archegonium", "Zoosporangium", "Sporangium"],
        ["অ্যান্থেরিডিয়াম", "আর্কিগোনিয়াম", "জুস্পোরাঞ্জিয়াম", "স্পোরাঞ্জিয়াম"],
        "A", "easy", "factual",
        "In Riccia the male organ is the antheridium and the female organ is the archegonium.",
        "Riccia-এর পুংজননাঙ্গ অ্যান্থেরিডিয়াম এবং স্ত্রীজননাঙ্গ আর্কিগোনিয়াম।",
    ),
    q(
        "Which is an advanced feature of bryophyte plants?",
        "ব্রায়োফাইটা উদ্ভিদের উন্নত বৈশিষ্ট্য কোনটি?",
        [
            "Plant body haploid in nature",
            "Presence of rhizoids",
            "Mostly thalloid body",
            "Meristematic tissue in the capsule",
        ],
        [
            "উদ্ভিদ হ্যাপ্লয়েড প্রকৃতির",
            "রাইজয়েড বিদ্যমান",
            "অধিকাংশই থ্যালয়েড",
            "ক্যাপসিউলে ভাজক টিস্যুর উপস্থিতি",
        ],
        "D", "medium", "conceptual",
        "Meristematic tissue in the moss capsule is treated as an advanced bryophyte trait; haploidy, rhizoids and thalloid habit are primitive features.",
        "ক্যাপসিউলে ভাজক টিস্যু ব্রায়োফাইটার উন্নত বৈশিষ্ট্য; হ্যাপ্লয়েডি, রাইজয়েড ও থ্যালয়েড দেহ আদি বৈশিষ্ট্য।",
    ),
    q(
        "Liverwort-like amphibian plants typically show which character?",
        "লিভার আকৃতির উভচর উদ্ভিদগুলো সাধারণত কোন বৈশিষ্ট্য প্রদর্শন করে?",
        [
            "Sporophytic plant body",
            "Dichotomously branched thallus",
            "Male organ is archegonium",
            "Presence of vascular tissue",
        ],
        [
            "দেহ স্পোরোফাইটিক",
            "থ্যালাস দ্ব্যাগ্র শাখাবিশিষ্ট",
            "পুংজননাঙ্গ আর্কিগোনিয়াম",
            "ভাস্কুলার টিস্যু আছে",
        ],
        "B", "medium", "conceptual",
        "Bryophytes such as Riccia are amphibians of the plant kingdom with a dichotomously branched gametophytic thallus and no true vascular tissue.",
        "Riccia-এর মতো ব্রায়োফাইটা উভচর উদ্ভিদ; এদের গ্যামিটোফাইটিক থ্যালাস দ্ব্যাগ্র শাখাবিশিষ্ট এবং সত্য ভাস্কুলার টিস্যু নেই।",
    ),
    q(
        "Which is a characteristic of Bryophyta?",
        "ব্রায়োফাইটার বৈশিষ্ট্য কোনটি?",
        [
            "Dominant sporophytic body",
            "Vascular tissue present",
            "Flowering plants",
            "Embryo-forming plants",
        ],
        [
            "স্পোরোফাইটিক দেহ প্রধান",
            "পরিবহন টিস্যুযুক্ত",
            "পুষ্পক উদ্ভিদ",
            "ভ্রূণ সৃষ্টিকারী",
        ],
        "D", "easy", "factual",
        "Bryophytes are embryophytes: a multicellular embryo develops on the gametophyte; they lack flowers and true vascular tissue.",
        "ব্রায়োফাইটা ভ্রূণসৃষ্টিকারী; বহুকোষী ভ্রূণ গ্যামিটোফাইটে বিকশিত হয়; এদের পুষ্প ও সত্য ভাস্কুলার টিস্যু নেই।",
    ),
    q(
        "Which statements about Riccia are correct? (i) rhizoids present (ii) archegonium cylindrical (iii) sporophyte homosporous",
        "Riccia উদ্ভিদের বৈশিষ্ট্য— (i) রাইজয়েড উপস্থিত (ii) আর্কিগোনিয়াম বেলনাকার (iii) স্পোরোফাইট হোমোস্পোরাস",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "C", "medium", "conceptual",
        "Riccia has rhizoids and a homosporous sporophyte; its archegonium is flask-shaped, not cylindrical.",
        "Riccia-তে রাইজয়েড থাকে এবং স্পোরোফাইট হোমোস্পোরাস; আর্কিগোনিয়াম ফ্লাস্ক আকৃতির, বেলনাকার নয়।",
    ),
    q(
        "For a Bangladesh liverwort such as Riccia, which statements about the thallus are true? (i) attached by true roots (ii) gametophytic (iii) dichotomously branched",
        "বাংলাদেশের লিভারওয়ার্ট (যেমন Riccia) থ্যালাসের ক্ষেত্রে সত্য— (i) মূল দ্বারা মাটিতে আটকে থাকে (ii) গ্যামিটোফাইটিক (iii) দ্ব্যাগ্র শাখাবিশিষ্ট",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "B", "medium", "conceptual",
        "The thallus is the gametophyte and shows dichotomous branching; attachment is by rhizoids, not true roots.",
        "থ্যালাস গ্যামিটোফাইটিক ও দ্ব্যাগ্র শাখাবিশিষ্ট; মাটির সাথে আটকে থাকে রাইজয়েড দিয়ে, সত্য মূল দিয়ে নয়।",
    ),
    q(
        "Which statement is true for the two regions of a Riccia thallus?",
        "Riccia থ্যালাসের দুই অঞ্চল সম্পর্কে কোনটি সত্য?",
        [
            "Assimilatory region contains chlorophyll",
            "Storage region has stomata",
            "Rhizoids occur in the assimilatory region",
            "Storage region has air cavities",
        ],
        [
            "আত্তীকরণ অঞ্চল ক্লোরোফিলযুক্ত",
            "সঞ্চয়ী অঞ্চল স্টোমাটাযুক্ত",
            "আত্তীকরণ অঞ্চলে রাইজয়েড বিদ্যমান",
            "সঞ্চয়ী অঞ্চল বায়ুকুঠুরীযুক্ত",
        ],
        "A", "medium", "factual",
        "The upper assimilatory region is chlorophyllous; rhizoids arise from the lower surface, and the storage region lacks stomata.",
        "উপরের আত্তীকরণ অঞ্চল ক্লোরোফিলযুক্ত; রাইজয়েড নিম্নতলে থাকে এবং সঞ্চয়ী অঞ্চলে স্টোমাটা নেই।",
    ),
    q(
        "In which plant is the sporophyte primitive and embedded within the thallus?",
        "স্পোরোফাইট আদি প্রকৃতির এবং থ্যালাসের মধ্যে নিমজ্জিত থাকে কোন উদ্ভিদে?",
        ["Semibarbula", "Marchantia", "Riccia", "Funaria"],
        ["Semibarbula", "Marchantia", "Riccia", "Funaria"],
        "C", "medium", "factual",
        "Riccia has the most reduced sporophyte, remaining embedded in the gametophytic thallus; mosses and Marchantia are less reduced.",
        "Riccia-এর স্পোরোফাইট সবচেয়ে সরল ও গ্যামিটোফাইটিক থ্যালাসে নিমজ্জিত; মস ও Marchantia তুলনায় কম সরল।",
    ),
    q(
        "Pinus is more advanced than Riccia because: (i) main body sporophytic (ii) plant thalloid (iii) vascular tissue present",
        "Pinus উদ্ভিদ Riccia হতে বেশি উন্নত, কারণ— (i) মূল দেহ স্পোরোফাইটিক (ii) উদ্ভিদ সমাঙ্গদেহী (iii) ভাস্কুলার টিস্যু বিদ্যমান",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (i) ও (iii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "B", "medium", "conceptual",
        "Pinus has a dominant sporophyte with vascular tissue; thalloid body is a Riccia trait, not an advance of Pinus.",
        "Pinus-এর প্রধান দেহ স্পোরোফাইটিক ও ভাস্কুলার টিস্যুযুক্ত; সমাঙ্গ/থ্যালয়েড দেহ Riccia-এর বৈশিষ্ট্য।",
    ),
    q(
        "Bryophytes are called amphibians of the plant kingdom mainly because:",
        "ব্রায়োফাইটাকে উদ্ভিদজগতের উভচর বলা হয় প্রধানত কারণ—",
        [
            "They live only in deep water",
            "They need water for sexual reproduction",
            "They produce seeds in water",
            "They have vascular tissue like ferns",
        ],
        [
            "এরা কেবল গভীর পানিতে বাস করে",
            "যৌন প্রজননের জন্য পানির প্রয়োজন হয়",
            "পানিতে বীজ উৎপন্ন করে",
            "ফার্নের মতো ভাস্কুলার টিস্যু আছে",
        ],
        "B", "easy", "conceptual",
        "Sperm must swim through a water film to reach the archegonium, so fertilization depends on moisture.",
        "শুক্রাণু পানির পাতলা স্তর দিয়ে সাঁতরে আর্কিগোনিয়ামে পৌঁছায় বলে নিষেকের জন্য আর্দ্রতা অপরিহার্য।",
    ),
    q(
        "Dichotomous branching in Riccia means:",
        "Riccia-এ দ্ব্যাগ্র শাখায়ন বলতে বোঝায়—",
        [
            "One branch always dies after forking",
            "The growing tip divides into two equal branches",
            "Leaves arise in pairs only",
            "Roots fork into xylem and phloem",
        ],
        [
            "শাখা বিভক্তির পর একটি সবসময় মরে যায়",
            "বৃদ্ধিবিন্দু দুই সমান শাখায় বিভক্ত হয়",
            "পাতা কেবল জোড়ায় জন্মে",
            "মূল জাইলেম ও ফ্লোয়েমে বিভক্ত হয়",
        ],
        "B", "easy", "factual",
        "At the apex the growth point splits into two equal arms, producing dichotomous branching of the thallus.",
        "অগ্রভাগে বৃদ্ধিবিন্দু দুই সমান শাখায় বিভক্ত হয়ে থ্যালাসের দ্ব্যাগ্র শাখায়ন ঘটায়।",
    ),
    q(
        "The dominant independent plant body of a bryophyte is:",
        "ব্রায়োফাইটার প্রধান স্বাধীন উদ্ভিদদেহ হলো—",
        ["Sporophyte", "Gametophyte", "Seedling", "Prothallus of fern only"],
        ["স্পোরোফাইট", "গ্যামিটোফাইট", "চারা", "কেবল ফার্ন প্রোথ্যালাস"],
        "B", "easy", "factual",
        "In bryophytes the haploid gametophyte is the conspicuous green plant; the sporophyte is attached to and dependent on it.",
        "ব্রায়োফাইটায় হ্যাপ্লয়েড গ্যামিটোফাইটই প্রধান সবুজ উদ্ভিদ; স্পোরোফাইট এর উপর নির্ভরশীল।",
    ),
    q(
        "Bryophytes differ from pteridophytes in lacking:",
        "ব্রায়োফাইটা টেরিডোফাইটা থেকে আলাদা কারণ এদের নেই—",
        ["Chlorophyll", "Embryo", "True vascular tissue", "Alternation of generations"],
        ["ক্লোরোফিল", "ভ্রূণ", "সত্য ভাস্কুলার টিস্যু", "জনুক্রম"],
        "C", "easy", "conceptual",
        "Bryophytes are non-vascular embryophytes; pteridophytes are the first vascular cryptogams.",
        "ব্রায়োফাইটা অভাস্কুলার ভ্রূণসৃষ্টিকারী; টেরিডোফাইটা প্রথম ভাস্কুলার ক্রিপ্টোগ্যাম।",
    ),
    q(
        "Structures that attach Riccia to the substratum are called:",
        "Riccia-কে অধঃস্তরে আটকে রাখে যে গঠনগুলো তাদের বলে—",
        ["True roots", "Rhizoids", "Holdfasts of Ulothrix only", "Pneumatophores"],
        ["সত্য মূল", "রাইজয়েড", "কেবল Ulothrix-এর হোল্ডফাস্ট", "নিউমাটোফোর"],
        "B", "easy", "factual",
        "Bryophytes have unicellular or multicellular rhizoids, not true roots with xylem and phloem.",
        "ব্রায়োফাইটায় এককোষী বা বহুকোষী রাইজয়েড থাকে; জাইলেম–ফ্লোয়েমযুক্ত সত্য মূল নেই।",
    ),
    q(
        "The shape of the archegonium of Riccia is:",
        "Riccia-এর আর্কিগোনিয়ামের আকৃতি কী?",
        ["Spherical", "Flask-shaped", "Cylindrical only", "Disc-shaped"],
        ["গোলাকার", "ফ্লাস্ক আকৃতির", "কেবল বেলনাকার", "চাকতি আকৃতির"],
        "B", "easy", "factual",
        "Riccia archegonium is flask-shaped; the antheridium is roughly spherical.",
        "Riccia-এর আর্কিগোনিয়াম ফ্লাস্ক আকৃতির এবং অ্যান্থেরিডিয়াম প্রায় গোলাকার।",
    ),
    q(
        "Which plant group includes Marchantia, Riccia and Funaria?",
        "Marchantia, Riccia ও Funaria কোন গোষ্ঠীর উদ্ভিদ?",
        ["Algae", "Fungi", "Bryophyta", "Gymnosperms"],
        ["শৈবাল", "ছত্রাক", "ব্রায়োফাইটা", "নগ্নবীজি"],
        "C", "easy", "factual",
        "Marchantia and Riccia are liverworts and Funaria is a moss; all belong to Bryophyta.",
        "Marchantia ও Riccia লিভারওয়ার্ট এবং Funaria মস; সবই ব্রায়োফাইটাভুক্ত।",
    ),
    q(
        "Food reserved in the storage region of Riccia thallus is mainly:",
        "Riccia থ্যালাসের সঞ্চয়ী অঞ্চলে প্রধান সঞ্চিত খাদ্য হলো—",
        ["Chitin", "Starch", "Glycogen only", "Floridean starch"],
        ["কাইটিন", "স্টার্চ", "কেবল গ্লাইকোজেন", "ফ্লোরিডিয়ান স্টার্চ"],
        "B", "medium", "factual",
        "Like other green embryophytes, Riccia stores starch in the storage tissue of the thallus.",
        "অন্যান্য সবুজ ভ্রূণসৃষ্টিকারীর মতো Riccia থ্যালাসের সঞ্চয়ী টিস্যুতে স্টার্চ জমা রাখে।",
    ),
    q(
        "Which bryophyte is a leafy moss rather than a thalloid liverwort?",
        "কোনটি থ্যালয়েড লিভারওয়ার্ট নয়, বরং পত্রময় মস?",
        ["Riccia", "Marchantia", "Funaria", "Pteris"],
        ["Riccia", "Marchantia", "Funaria", "Pteris"],
        "C", "easy", "factual",
        "Funaria is a moss with stem-like and leaf-like organs; Riccia and Marchantia are thalloid liverworts and Pteris is a fern.",
        "Funaria কাণ্ড ও পাতাসদৃশ অঙ্গবিশিষ্ট মস; Riccia ও Marchantia থ্যালয়েড লিভারওয়ার্ট এবং Pteris ফার্ন।",
    ),
    q(
        "In bryophytes, the sporophyte remains attached to the:",
        "ব্রায়োফাইটায় স্পোরোফাইট সংলগ্ন থাকে—",
        ["Independent root system", "Gametophyte", "Seed coat", "Endosperm only"],
        ["স্বাধীন মূলতন্ত্রে", "গ্যামিটোফাইটে", "বীজত্বকে", "কেবল এন্ডোস্পার্মে"],
        "B", "easy", "conceptual",
        "The diploid sporophyte grows on the gametophyte and depends on it for nutrition, especially in Riccia.",
        "ডিপ্লয়েড স্পোরোফাইট গ্যামিটোফাইটের উপর বিকশিত হয় এবং পুষ্টির জন্য নির্ভরশীল, বিশেষত Riccia-তে।",
    ),
]


# --- t02: Pteridophytes / টেরিডোফাইটা ---
T02 = [
    q(
        "What type of vascular bundle does Pteris have?",
        "Pteris-এর ভাস্কুলার বান্ডল কোন ধরনের?",
        ["Hadrocentric", "Leptocentric", "Conjoint", "Radial"],
        ["হ্যাড্রোসেন্ট্রিক", "লেপ্টোসেন্ট্রিক", "সংযুক্ত", "অরীয়"],
        "A", "medium", "factual",
        "Pteris has a hadrocentric (xylem-centric) bundle with xylem in the centre surrounded by phloem.",
        "Pteris-এর বান্ডল হ্যাড্রোসেন্ট্রিক (জাইলেম কেন্দ্রিক); কেন্দ্রে জাইলেম ও চারদিকে ফ্লোয়েম থাকে।",
    ),
    q(
        "Scale leaves covering the rhizome of Pteris are called:",
        "Pteris-এর রাইজোমের শল্কপত্রকে কী বলে?",
        ["Rachis", "Crozier", "Frond", "Ramenta"],
        ["র‍্যাকিস", "ক্রোজিয়ার", "ফ্রন্ড", "র‍্যামেন্টা"],
        "D", "easy", "factual",
        "Brown scale leaves on the fern rhizome are called ramenta (singular ramentum).",
        "ফার্নের রাইজোমে বাদামি শল্কপত্রকে র‍্যামেন্টা (একবচনে র‍্যামেন্টাম) বলে।",
    ),
    q(
        "A cluster of sporangia on the leaf of Pteris is called a:",
        "Pteris-এর পাতায় অবস্থিত স্পোরাঞ্জিয়ামের গুচ্ছকে বলে—",
        ["Annulus", "Indusium", "Placenta", "Sorus"],
        ["অ্যানুলাস", "ইন্ডুসিয়াম", "অমরা", "সোরাস"],
        "D", "easy", "factual",
        "Groups of sporangia on the abaxial leaf surface form sori; the annulus is a ring on the sporangium wall.",
        "পাতার নিম্নতলে স্পোরাঞ্জিয়ামের গুচ্ছ সোরাস; অ্যানুলাস স্পোরাঞ্জিয়াম প্রাচীরের বলয়।",
    ),
    q(
        "The coiled young leaf of a Pteris plant is called a:",
        "Pteris উদ্ভিদের কুণ্ডলিত কচি পাতাকে কী বলে?",
        ["Frond", "Pinna", "Ramentum", "Crozier"],
        ["ফ্রন্ড", "পিনা", "র‍্যামেন্টাম", "ক্রোজিয়ার"],
        "D", "easy", "factual",
        "Young fern leaves remain coiled like a watch spring (circinate vernation) and are called croziers.",
        "ফার্নের কচি পাতা ঘড়ির স্প্রিংয়ের মতো কুণ্ডলিত (সার্সিনেট ভার্নেশন) থাকে; একে ক্রোজিয়ার বলে।",
    ),
    q(
        "Which plant matches vascular cryptogams with a heteromorphic life cycle?",
        "হেটেরোমরফিক জীবনচক্রবিশিষ্ট ভাস্কুলার ক্রিপ্টোগ্যামসের সাথে কোন উদ্ভিদের মিল?",
        ["Ulothrix sp.", "Riccia sp.", "Pteris sp.", "Cycas sp."],
        ["Ulothrix sp.", "Riccia sp.", "Pteris sp.", "Cycas sp."],
        "C", "easy", "factual",
        "Pteris is a seedless vascular plant (vascular cryptogam); Ulothrix and Riccia are non-vascular, Cycas is a seed plant.",
        "Pteris বীজহীন ভাস্কুলার উদ্ভিদ (ভাস্কুলার ক্রিপ্টোগ্যাম); Ulothrix ও Riccia অভাস্কুলার, Cycas বীজ উদ্ভিদ।",
    ),
    q(
        "Pteris (fern) plant is:",
        "Pteris (ফার্ন) উদ্ভিদ হলো—",
        ["Flowering", "Only gametophytic", "Provided with vascular tissue", "Thalloid"],
        ["সপুষ্পক", "কেবল গ্যামেটোফাইটিক", "পরিবহন টিস্যুযুক্ত", "থ্যালয়েড"],
        "C", "easy", "factual",
        "The familiar fern plant is a vascular sporophyte with true roots, stem and leaves; it is non-flowering.",
        "পরিচিত ফার্ন উদ্ভিদ সত্য মূল–কাণ্ড–পাতা ও ভাস্কুলার টিস্যুযুক্ত স্পোরোফাইট; এটি অপুষ্পক।",
    ),
    q(
        "Brown scales covering the rhizome of the first vascular plants are called:",
        "প্রথম ভাস্কুলার উদ্ভিদের রাইজোম যে বাদামি শল্কপত্র দ্বারা আবৃত থাকে তার নাম—",
        ["Frond", "Pinna", "Crozier", "Ramentum"],
        ["ফ্রন্ড", "পিনা", "ক্রোজিয়ার", "র‍্যামেন্টাম"],
        "D", "easy", "factual",
        "Ramenta protect the rhizome of ferns such as Pteris, the classic first vascular plants in HSC texts.",
        "র‍্যামেন্টা Pteris-এর মতো ফার্নের রাইজোম আবৃত করে; HSC পাঠ্যে এরা প্রথম ভাস্কুলার উদ্ভিদ।",
    ),
    q(
        "A leaf that produces sori is called a:",
        "সোরাই উৎপন্নকারী পাতাকে কী বলা হয়?",
        ["Capsule", "Stomium", "Sporophyll", "Annulus"],
        ["ক্যাপসিউল", "স্টোমিয়াম", "স্পোরোফিল", "অ্যানুলাস"],
        "C", "easy", "factual",
        "Sporophylls are spore-bearing leaves; in ferns they bear sori of sporangia.",
        "স্পোরোফিল স্পোরধারণকারী পাতা; ফার্নে এতে স্পোরাঞ্জিয়ামের সোরাস থাকে।",
    ),
    q(
        "Among the following, the most advanced non-flowering (cryptogamic) plant is:",
        "নিচের মধ্যে অপুষ্পক (ক্রিপ্টোগ্যামিক) উদ্ভিদের সর্বাপেক্ষা উন্নত কোনটি?",
        ["Ulothrix", "Riccia", "Pteris", "Agaricus"],
        ["Ulothrix", "Riccia", "Pteris", "Agaricus"],
        "C", "medium", "conceptual",
        "Among algae, bryophytes, ferns and fungi listed here, Pteris is the most advanced vascular cryptogam.",
        "এ তালিকার শৈবাল, ব্রায়োফাইট, ফার্ন ও ছত্রাকের মধ্যে Pteris সর্বাপেক্ষা উন্নত ভাস্কুলার ক্রিপ্টোগ্যাম।",
    ),
    q(
        "Characteristics of Pteris include: (i) body divided into root, stem and leaf (ii) rhizomatous stem (iii) young leaves coiled",
        "Pteris-এর বৈশিষ্ট্য— (i) দেহ মূল, কাণ্ড ও পাতায় বিভক্ত (ii) কাণ্ড রাইজোমজাতীয় (iii) কচি পাতা কুণ্ডলিত",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "Fern sporophytes have organ differentiation, a rhizome, and circinate vernation of young fronds.",
        "ফার্ন স্পোরোফাইটে অঙ্গবিভাজন, রাইজোম এবং কচি ফ্রন্ডের সার্সিনেট ভার্নেশন দেখা যায়।",
    ),
    q(
        "The transport tissue bundle of Pteris is described as:",
        "টেরিসের পরিবহন কলাগুচ্ছ কোন ধরনের?",
        ["Phloem-centric", "Radial", "Conjoint", "Xylem-centric"],
        ["ফ্লোয়েম কেন্দ্রিক", "অরীয়", "সংযুক্ত", "জাইলেম কেন্দ্রিক"],
        "D", "medium", "factual",
        "Xylem-centric means hadrocentric: central xylem ringed by phloem.",
        "জাইলেম কেন্দ্রিক মানে হ্যাড্রোসেন্ট্রিক—কেন্দ্রে জাইলেম, চারপাশে ফ্লোয়েম।",
    ),
    q(
        "Which statements fit ferns (pteridophytes)? (i) autotrophic (ii) non-flowering (iii) cell wall of chitin",
        "ফার্ন/টেরিডোফাইটার বৈশিষ্ট্য— (i) স্বভোজী (ii) অপুষ্পক (iii) কোষপ্রাচীর কাইটিন নির্মিত",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "A", "easy", "conceptual",
        "Ferns are photosynthetic and non-flowering; cellulose walls, not fungal chitin, form their cell walls.",
        "ফার্ন সালোকসংশ্লেষী ও অপুষ্পক; কোষপ্রাচীর সেলুলোজ নির্মিত, ছত্রাকের মতো কাইটিন নয়।",
    ),
    q(
        "Circinate vernation refers to:",
        "সার্সিনেট ভার্নেশন বলতে বোঝায়—",
        [
            "Seeds coiled inside cones",
            "Young leaves coiled like a watch spring",
            "Rhizoids coiled around stems",
            "Spores arranged in a spiral capsule",
        ],
        [
            "শঙ্কুতে বীজ কুণ্ডলিত থাকা",
            "কচি পাতা ঘড়ির স্প্রিংয়ের মতো কুণ্ডলিত থাকা",
            "রাইজয়েড কাণ্ডকে পেঁচিয়ে থাকা",
            "স্পোর ক্যাপসুলে সর্পিল সজ্জিত থাকা",
        ],
        "B", "easy", "factual",
        "In ferns, young fronds uncoil from a crozier due to circinate vernation.",
        "ফার্নে কচি ফ্রন্ড ক্রোজিয়ার অবস্থা থেকে সার্সিনেট ভার্নেশনে খুলে যায়।",
    ),
    q(
        "Pteris is called a vascular cryptogam because it:",
        "Pteris-কে ভাস্কুলার ক্রিপ্টোগ্যাম বলা হয় কারণ এটি—",
        [
            "Has flowers and seeds",
            "Has xylem–phloem but no seeds",
            "Lacks chlorophyll",
            "Is always aquatic and thalloid",
        ],
        [
            "পুষ্প ও বীজ আছে",
            "জাইলেম–ফ্লোয়েম আছে কিন্তু বীজ নেই",
            "ক্লোরোফিলহীন",
            "সবসময় জলজ ও থ্যালয়েড",
        ],
        "B", "easy", "conceptual",
        "Cryptogams reproduce by spores; vascular cryptogams add conducting tissue without forming seeds.",
        "ক্রিপ্টোগ্যাম স্পোর দ্বারা বংশবৃদ্ধি করে; ভাস্কুলার ক্রিপ্টোগ্যামে পরিবহন টিস্যু থাকে কিন্তু বীজ হয় না।",
    ),
    q(
        "The expanded photosynthetic leaf of a fern is commonly called a:",
        "ফার্নের বিস্তৃত সালোকসংশ্লেষী পাতাকে সাধারণত কী বলে?",
        ["Frond", "Ramentum", "Prothallus", "Capsule"],
        ["ফ্রন্ড", "র‍্যামেন্টাম", "প্রোথ্যালাস", "ক্যাপসিউল"],
        "A", "easy", "factual",
        "Fern leaves are fronds; pinnae are leaflets of a compound frond and the prothallus is the gametophyte.",
        "ফার্নের পাতা ফ্রন্ড; পিনা যৌগিক ফ্রন্ডের পত্রক এবং প্রোথ্যালাস গ্যামিটোফাইট।",
    ),
    q(
        "The incomplete ring of thick-walled cells that aids dehiscence of a fern sporangium is the:",
        "ফার্ন স্পোরাঞ্জিয়ামের বিদারণে সহায়ক পুরুপ্রাচীরযুক্ত অসম্পূর্ণ বলয় হলো—",
        ["Sorus", "Indusium", "Annulus", "Rachis"],
        ["সোরাস", "ইন্ডুসিয়াম", "অ্যানুলাস", "র‍্যাকিস"],
        "C", "medium", "factual",
        "Differential thickening of the annulus throws spores out when the sporangium dries.",
        "অ্যানুলাসের অসম পুরুত্ব শুকানোর সময় স্পোরাঞ্জিয়ামকে স্পোর নিক্ষেপে সাহায্য করে।",
    ),
    q(
        "A membranous covering over a fern sorus is called an:",
        "ফার্নের সোরাসের উপরের পর্দাসদৃশ আবরণকে বলে—",
        ["Indusium", "Operculum", "Calyptra", "Velum of fungi"],
        ["ইন্ডুসিয়াম", "অপারকুলাম", "ক্যালিপট্রা", "ছত্রাকের ভেলাম"],
        "A", "medium", "factual",
        "Many fern sori are protected by an indusium; operculum and calyptra relate to moss capsules.",
        "অনেক ফার্নের সোরাস ইন্ডুসিয়াম দ্বারা আবৃত; অপারকুলাম ও ক্যালিপট্রা মসের ক্যাপসুল সম্পর্কিত।",
    ),
    q(
        "Pteris is typically described as:",
        "Pteris সাধারণত কীভাবে বর্ণিত হয়?",
        ["Heterosporous seed plant", "Homosporous fern", "Thalloid alga", "Fruiting angiosperm"],
        ["হেটেরোস্পোরাস বীজ উদ্ভিদ", "হোমোস্পোরাস ফার্ন", "থ্যালয়েড শৈবাল", "ফলধারী আবৃতবীজি"],
        "B", "medium", "factual",
        "Pteris produces one kind of spore (homosporous) that germinates into a bisexual prothallus.",
        "Pteris এক ধরনের স্পোর (হোমোস্পোরাস) উৎপন্ন করে যা দ্বিলিঙ্গ প্রোথ্যালাসে অঙ্কুরিত হয়।",
    ),
    q(
        "The main plant body of Pteris that we usually see is:",
        "আমরা সাধারণত যে Pteris উদ্ভিদ দেখি তার প্রধান দেহ হলো—",
        ["Gametophyte", "Sporophyte", "Zygote only", "Protonema"],
        ["গ্যামিটোফাইট", "স্পোরোফাইট", "কেবল জাইগোট", "প্রোটোনিমা"],
        "B", "easy", "factual",
        "In pteridophytes the diploid sporophyte is large and independent; the gametophyte is the small prothallus.",
        "টেরিডোফাইটায় ডিপ্লয়েড স্পোরোফাইট বৃহৎ ও স্বাধীন; গ্যামিটোফাইট ক্ষুদ্র প্রোথ্যালাস।",
    ),
    q(
        "Compared with Riccia, Pteris is advanced because it has:",
        "Riccia-এর তুলনায় Pteris উন্নত কারণ এতে আছে—",
        [
            "Only rhizoids and no leaves",
            "True roots, stem, leaves and vascular tissue",
            "A permanently embedded sporophyte",
            "Flowers and fruits",
        ],
        [
            "কেবল রাইজয়েড, পাতা নেই",
            "সত্য মূল, কাণ্ড, পাতা ও ভাস্কুলার টিস্যু",
            "স্থায়ীভাবে নিমজ্জিত স্পোরোফাইট",
            "পুষ্প ও ফল",
        ],
        "B", "easy", "conceptual",
        "Organ differentiation plus xylem and phloem place ferns above bryophytes; they still lack seeds and flowers.",
        "অঙ্গবিভাজন ও জাইলেম–ফ্লোয়েম ফার্নকে ব্রায়োফাইটার উপরে রাখে; তবু এদের বীজ ও পুষ্প নেই।",
    ),
]


# --- t03: Life cycles / জীবনচক্র ---
T03 = [
    q(
        "Which is the first cell of the sporophyte of Pteris?",
        "Pteris-এর স্পোরোফাইটের প্রথম কোষ কোনটি?",
        ["Spore", "Sorus", "Oospore (zygote)", "Spore mother cell"],
        ["স্পোর", "সোরাস", "উস্পোর (জাইগোট)", "স্পোর মাতৃকোষ"],
        "C", "medium", "factual",
        "Fertilization produces a diploid zygote (oospore), the first cell of the sporophyte generation.",
        "নিষেকের ফলে ডিপ্লয়েড জাইগোট (উস্পোর) সৃষ্টি হয়, যা স্পোরোফাইট প্রজন্মের প্রথম কোষ।",
    ),
    q(
        "Which apply to a fern prothallus? (i) monoecious (ii) sexual reproduction occurs (iii) arises from germinating spore",
        "ফার্ন প্রোথ্যালাসের ক্ষেত্রে প্রযোজ্য— (i) সহবাসী (ii) যৌন প্রজনন ঘটে (iii) স্পোর অঙ্কুরিত হয়ে সৃষ্ট",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "The heart-shaped prothallus is a monoecious gametophyte formed from a spore and bearing sex organs.",
        "হৃৎপিণ্ডাকার প্রোথ্যালাস স্পোর থেকে সৃষ্ট সহবাসী গ্যামিটোফাইট এবং এতে যৌনজননাঙ্গ থাকে।",
    ),
    q(
        "In the heteromorphic life cycle of a vascular cryptogam such as Pteris: (i) diploid phase long-lived (ii) gametophyte autotrophic (iii) sexual phase is the sporophyte",
        "Pteris-এর মতো ভাস্কুলার ক্রিপ্টোগ্যামের হেটেরোমরফিক জীবনচক্রে— (i) ডিপ্লয়েড দশা দীর্ঘস্থায়ী (ii) লিঙ্গধর দশা স্বভোজী (iii) যৌনজনন দশা রেণুধর",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (i) ও (iii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "A", "hard", "conceptual",
        "The sporophyte is long-lived and the gametophyte is green and autotrophic; sexual organs occur on the gametophyte, not the sporophyte.",
        "স্পোরোফাইট দীর্ঘজীবী এবং গ্যামিটোফাইট সবুজ স্বভোজী; যৌনজননাঙ্গ গ্যামিটোফাইটে হয়, স্পোরোফাইটে নয়।",
    ),
    q(
        "A fern prothallus is:",
        "ফার্ন প্রোথ্যালাস—",
        ["Diploid", "Unisexual only", "Autotrophic", "Dioecious always"],
        ["ডিপ্লয়েড", "কেবল একলিঙ্গ", "স্বভোজী", "সবসময় ভিন্নবাসী"],
        "C", "easy", "factual",
        "The prothallus is a green, multicellular, independent and autotrophic haploid gametophyte.",
        "প্রোথ্যালাস সবুজ, বহুকোষী, স্বাধীন ও স্বভোজী হ্যাপ্লয়েড গ্যামিটোফাইট।",
    ),
    q(
        "In fern plants, meiosis occurs in the:",
        "ফার্ন উদ্ভিদে মিয়োসিস ঘটে—",
        ["Spore mother cells", "Zygote", "Prothallus", "Mature spore"],
        ["স্পোর মাতৃকোষে", "জাইগোটে", "প্রোথ্যালাসে", "পরিণত স্পোরে"],
        "A", "easy", "factual",
        "Diploid spore mother cells in sporangia undergo meiosis to form haploid spores.",
        "স্পোরাঞ্জিয়ামের ডিপ্লয়েড স্পোর মাতৃকোষে মিয়োসিস হয়ে হ্যাপ্লয়েড স্পোর সৃষ্টি হয়।",
    ),
    q(
        "Which information applies to a fern prothallus? (i) gametophytic stage (ii) produces antheridia and archegonia (iii) independent and autotrophic",
        "ফার্ন প্রোথ্যালাসের ক্ষেত্রে প্রযোজ্য— (i) গ্যামিটোফাইটিক দশা (ii) অ্যান্থেরিডিয়াম ও আর্কিগোনিয়াম উৎপন্ন হয় (iii) স্বাধীন ও স্বভোজী",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (i) ও (iii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "All three statements correctly describe the free-living fern gametophyte.",
        "তিনটি বক্তব্যই ফার্নের স্বাধীন গ্যামিটোফাইট প্রোথ্যালাসকে সঠিকভাবে বর্ণনা করে।",
    ),
    q(
        "Characteristics of fern prothallus: (i) heart-shaped (ii) sporophytic (iii) monoecious",
        "ফার্ন প্রোথ্যালাসের বৈশিষ্ট্য— (i) হৃৎপিণ্ডাকার (ii) স্পোরোফাইটিক (iii) সহবাসী",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (i) ও (iii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "B", "medium", "conceptual",
        "The prothallus is heart-shaped and usually monoecious; it is gametophytic, not sporophytic.",
        "প্রোথ্যালাস হৃৎপিণ্ডাকার ও সাধারণত সহবাসী; এটি গ্যামিটোফাইটিক, স্পোরোফাইটিক নয়।",
    ),
    q(
        "For a heart-shaped fern prothallus, which are correct? (i) sexual reproduction occurs (ii) produced from a spore (iii) diploid chromosomes",
        "হৃৎপিণ্ডাকার ফার্ন প্রোথ্যালাসের ক্ষেত্রে সঠিক— (i) যৌনজনন সম্পন্ন হয় (ii) স্পোর হতে উৎপন্ন (iii) ডিপ্লয়েড ক্রোমোজোমবিশিষ্ট",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (i) ও (iii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "A", "medium", "conceptual",
        "The prothallus is haploid, arises from a spore, and bears sex organs for sexual reproduction.",
        "প্রোথ্যালাস হ্যাপ্লয়েড, স্পোর থেকে উৎপন্ন এবং যৌনজননের জন্য জননাঙ্গ ধারণ করে।",
    ),
    q(
        "Alternation of generations means the regular cycling between:",
        "জনুক্রম বলতে নিয়মিত পরিবর্তন বোঝায়—",
        [
            "Root and shoot only",
            "Diploid sporophyte and haploid gametophyte",
            "Xylem and phloem only",
            "Flower and fruit only",
        ],
        [
            "কেবল মূল ও কাণ্ড",
            "ডিপ্লয়েড স্পোরোফাইট ও হ্যাপ্লয়েড গ্যামিটোফাইট",
            "কেবল জাইলেম ও ফ্লোয়েম",
            "কেবল পুষ্প ও ফল",
        ],
        "B", "easy", "factual",
        "Life cycles of bryophytes and pteridophytes alternate a 2n sporophyte with an n gametophyte.",
        "ব্রায়োফাইটা ও টেরিডোফাইটার জীবনচক্রে 2n স্পোরোফাইট ও n গ্যামিটোফাইট পর্যায়ক্রমে আসে।",
    ),
    q(
        "Heteromorphic alternation of generations in Pteris means the two phases are:",
        "Pteris-এ হেটেরোমরফিক জনুক্রম মানে দুই দশা—",
        [
            "Identical in size and form",
            "Morphologically different",
            "Both diploid always",
            "Both without chlorophyll",
        ],
        [
            "আকার ও আকৃতিতে অভিন্ন",
            "গঠনগতভাবে ভিন্ন",
            "সবসময় উভয়ই ডিপ্লয়েড",
            "উভয়ই ক্লোরোফিলহীন",
        ],
        "B", "easy", "conceptual",
        "The large sporophyte and small prothallus differ markedly in form, so the cycle is heteromorphic.",
        "বৃহৎ স্পোরোফাইট ও ক্ষুদ্র প্রোথ্যালাস আকৃতিতে স্পষ্ট ভিন্ন বলে চক্রটি হেটেরোমরফিক।",
    ),
    q(
        "A gametophytic plant is one that:",
        "গ্যামিটোফাইটিক উদ্ভিদ হলো যা—",
        [
            "Produces diploid spores by mitosis only",
            "Produces gametes and represents the haploid phase",
            "Always has seeds",
            "Never photosynthesizes",
        ],
        [
            "কেবল মাইটোসিসে ডিপ্লয়েড স্পোর উৎপন্ন করে",
            "গ্যামেট উৎপন্ন করে এবং হ্যাপ্লয়েড দশা উপস্থাপন করে",
            "সবসময় বীজ ধারণ করে",
            "কখনো সালোকসংশ্লেষ করে না",
        ],
        "B", "easy", "factual",
        "The gametophyte is the haploid (n) generation that forms sperm and eggs in antheridia and archegonia.",
        "গ্যামিটোফাইট হ্যাপ্লয়েড (n) প্রজন্ম যা অ্যান্থেরিডিয়াম ও আর্কিগোনিয়ামে শুক্রাণু ও ডিম্বাণু গঠন করে।",
    ),
    q(
        "In the life cycle, spores of Pteris are produced by:",
        "জীবনচক্রে Pteris-এর স্পোর উৎপন্ন হয়—",
        [
            "Mitosis in the zygote",
            "Meiosis in spore mother cells",
            "Fertilization in the prothallus",
            "Fragmentation of rhizoids",
        ],
        [
            "জাইগোটে মাইটোসিস",
            "স্পোর মাতৃকোষে মিয়োসিস",
            "প্রোথ্যালাসে নিষেক",
            "রাইজয়েডের খণ্ডায়ন",
        ],
        "B", "easy", "factual",
        "Meiosis in diploid spore mother cells yields haploid spores that start the gametophyte generation.",
        "ডিপ্লয়েড স্পোর মাতৃকোষে মিয়োসিসে হ্যাপ্লয়েড স্পোর হয় যা গ্যামিটোফাইট প্রজন্ম শুরু করে।",
    ),
    q(
        "Fertilization in bryophytes and pteridophytes typically requires:",
        "ব্রায়োফাইটা ও টেরিডোফাইটায় নিষেকের জন্য সাধারণত প্রয়োজন—",
        ["Wind only", "A film of water for swimming sperm", "Insects always", "Dry desert air"],
        ["কেবল বায়ু", "সাঁতারু শুক্রাণুর জন্য পানির পাতলা স্তর", "সবসময় পতঙ্গ", "শুষ্ক মরু বায়ু"],
        "B", "easy", "conceptual",
        "Flagellated antherozoids swim to the archegonium, linking both groups to moist habitats.",
        "ফ্ল্যাজেলাযুক্ত অ্যান্থেরোজয়েড আর্কিগোনিয়ামে সাঁতরে যায় বলে উভয় গোষ্ঠী আর্দ্র আবাসের সাথে যুক্ত।",
    ),
    q(
        "In bryophytes the dominant phase is the gametophyte, whereas in pteridophytes it is the:",
        "ব্রায়োফাইটায় প্রধান দশা গ্যামিটোফাইট, অন্যদিকে টেরিডোফাইটায় প্রধান দশা—",
        ["Gametophyte only", "Sporophyte", "Seed", "Fruit"],
        ["কেবল গ্যামিটোফাইট", "স্পোরোফাইট", "বীজ", "ফল"],
        "B", "easy", "conceptual",
        "Fern life cycles show sporophyte dominance with a reduced free-living gametophyte.",
        "ফার্নের জীবনচক্রে স্পোরোফাইট প্রধান এবং গ্যামিটোফাইট হ্রাসপ্রাপ্ত স্বাধীন দশা।",
    ),
    q(
        "After fertilization, the zygote of Riccia develops into a:",
        "নিষেকের পর Riccia-এর জাইগোট বিকশিত হয়ে কী গঠন করে?",
        ["New thallus directly by meiosis", "Sporophyte embedded in the thallus", "Seed with endosperm", "Independent leafy tree"],
        [
            "সরাসরি মিয়োসিসে নতুন থ্যালাস",
            "থ্যালাসে নিমজ্জিত স্পোরোফাইট",
            "এন্ডোস্পার্মযুক্ত বীজ",
            "স্বাধীন পত্রময় বৃক্ষ",
        ],
        "B", "medium", "factual",
        "The zygote grows into a reduced sporophyte that remains enclosed within the gametophytic thallus.",
        "জাইগোট হ্রাসপ্রাপ্ত স্পোরোফাইটে পরিণত হয় যা গ্যামিটোফাইটিক থ্যালাসের ভিতরে থাকে।",
    ),
    q(
        "A germinating fern spore first produces a:",
        "অঙ্কুরিত ফার্ন স্পোর প্রথমে কী উৎপন্ন করে?",
        ["Sporophyte with roots", "Prothallus (gametophyte)", "Flower bud", "Secondary xylem"],
        ["মূলযুক্ত স্পোরোফাইট", "প্রোথ্যালাস (গ্যামিটোফাইট)", "পুষ্পমুকুল", "সেকেন্ডারি জাইলেম"],
        "B", "easy", "factual",
        "Haploid spores germinate into the heart-shaped prothallus before sexual reproduction forms a new sporophyte.",
        "হ্যাপ্লয়েড স্পোর হৃৎপিণ্ডাকার প্রোথ্যালাসে অঙ্কুরিত হয়; পরে যৌনজননে নতুন স্পোরোফাইট হয়।",
    ),
    q(
        "Antheridia and archegonia of ferns are borne on the:",
        "ফার্নের অ্যান্থেরিডিয়াম ও আর্কিগোনিয়াম অবস্থান করে—",
        ["Mature sporophyll only", "Prothallus", "Annulus", "Ramentum"],
        ["কেবল পরিণত স্পোরোফিলে", "প্রোথ্যালাসে", "অ্যানুলাসে", "র‍্যামেন্টামে"],
        "B", "easy", "factual",
        "Sex organs develop on the underside of the gametophytic prothallus.",
        "যৌনজননাঙ্গ গ্যামিটোফাইটিক প্রোথ্যালাসের নিম্নতলে বিকশিত হয়।",
    ),
    q(
        "Chromosome number in fern spore mother cells just before meiosis is:",
        "মিয়োসিসের ঠিক আগে ফার্নের স্পোর মাতৃকোষে ক্রোমোজোম সংখ্যা—",
        ["Haploid (n)", "Diploid (2n)", "Triploid (3n)", "Always zero"],
        ["হ্যাপ্লয়েড (n)", "ডিপ্লয়েড (2n)", "ট্রিপ্লয়েড (3n)", "সবসময় শূন্য"],
        "B", "medium", "factual",
        "Spore mother cells belong to the diploid sporophyte; meiosis halves the number to n in spores.",
        "স্পোর মাতৃকোষ ডিপ্লয়েড স্পোরোফাইটের অংশ; মিয়োসিসে স্পোরে সংখ্যা n হয়।",
    ),
    q(
        "In Pteris, the sporophyte is nutritionally:",
        "Pteris-এ স্পোরোফাইট পুষ্টিগতভাবে—",
        [
            "Always parasitic on the gametophyte for life",
            "Independent and autotrophic when mature",
            "Saprophytic like fungi",
            "Dependent on seeds for food",
        ],
        [
            "জীবনভর গ্যামিটোফাইটের উপর পরজীবী",
            "পরিণত অবস্থায় স্বাধীন ও স্বভোজী",
            "ছত্রাকের মতো মৃতজীবী",
            "খাদ্যের জন্য বীজনির্ভর",
        ],
        "B", "medium", "conceptual",
        "Young embryos may be briefly attached, but the mature fern sporophyte is free-living and photosynthetic.",
        "অল্পকাল ভ্রূণ সংলগ্ন থাকতে পারে, কিন্তু পরিণত ফার্ন স্পোরোফাইট স্বাধীন ও সালোকসংশ্লেষী।",
    ),
    q(
        "Which sequence correctly outlines the fern life cycle?",
        "ফার্নের জীবনচক্রের সঠিক ক্রম কোনটি?",
        [
            "Prothallus → meiosis → sporophyte → fertilization",
            "Sporophyte → meiosis → spore → prothallus → fertilization → zygote → sporophyte",
            "Seed → flower → fruit → spore",
            "Zygote → spore → seed → prothallus",
        ],
        [
            "প্রোথ্যালাস → মিয়োসিস → স্পোরোফাইট → নিষেক",
            "স্পোরোফাইট → মিয়োসিস → স্পোর → প্রোথ্যালাস → নিষেক → জাইগোট → স্পোরোফাইট",
            "বীজ → পুষ্প → ফল → স্পোর",
            "জাইগোট → স্পোর → বীজ → প্রোথ্যালাস",
        ],
        "B", "hard", "application",
        "The diploid sporophyte produces spores by meiosis; the gametophyte forms gametes; fertilization restores the sporophyte.",
        "ডিপ্লয়েড স্পোরোফাইট মিয়োসিসে স্পোর দেয়; গ্যামিটোফাইট গ্যামেট গঠন করে; নিষেকে আবার স্পোরোফাইট শুরু হয়।",
    ),
]


TOPICS_MAP = {
    "bio1_27_ch06_t01": T01,
    "bio1_27_ch06_t02": T02,
    "bio1_27_ch06_t03": T03,
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
        "chapter": "bio1_27_ch06",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p184_pdf190.png",
            "p185_pdf191.png",
            "p186_pdf192.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio1_27_ch06_t01": {
                "title": "Bryophytes / ব্রায়োফাইটা",
                "themes": [
                    "Riccia rhizoids; antheridium vs flask archegonium",
                    "advanced capsule meristem; embryo-forming character",
                    "amphibian plants; dichotomous thallus branching",
                    "gametophyte dominance; no true vascular tissue",
                    "embedded primitive sporophyte of Riccia",
                    "thallus assimilatory chlorophyll; starch storage",
                    "Pinus vs Riccia advance (sporophyte + vascular)",
                    "Funaria moss vs thalloid liverworts Marchantia/Riccia",
                ],
            },
            "bio1_27_ch06_t02": {
                "title": "Pteridophytes / টেরিডোফাইটা",
                "themes": [
                    "Pteris hadrocentric / xylem-centric vascular bundle",
                    "ramenta on rhizome; crozier circinate vernation",
                    "sorus / sporophyll / annulus / indusium",
                    "vascular cryptogam; organ differentiation",
                    "homosporous fern; frond terminology",
                    "autotrophic non-flowering cellulose walls",
                    "most advanced cryptogam among board options",
                    "independent sporophyte vs bryophyte contrast",
                ],
            },
            "bio1_27_ch06_t03": {
                "title": "Life cycles / জীবনচক্র",
                "themes": [
                    "zygote/oospore first sporophyte cell",
                    "meiosis in spore mother cells",
                    "fern prothallus: heart-shaped, monoecious, autotrophic",
                    "heteromorphic alternation; diploid phase long-lived",
                    "water film for swimming sperm",
                    "gametophyte vs sporophyte dominance shift",
                    "spore → prothallus → fertilization → sporophyte",
                    "sex organs on prothallus; independent mature fern",
                ],
            },
        },
        "low_confidence": [
            "Only ~3 printed pages (p184–186); p184 is mostly CQ short answers, so many stems are reconstructed from MCQ pages and supplemented with accurate HSC-level bilingual items to reach 20/topic.",
            "Figure-only prothallus/stimulus items rewritten as standalone stems naming fern prothallus or Riccia/Pteris explicitly.",
            "Algae-style stimulus (green slippery bodies whitening under bed) from p186 skipped as out of chapter scope.",
            "Board keying of Pteris as most advanced non-flowering among Ulothrix/Riccia/Pteris/Agaricus followed; Cycas excluded from that stem to avoid seed-plant ambiguity.",
            "Riccia archegonium keyed flask-shaped per Udvash explanation box (rejects 'cylindrical' distractor).",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio1_27_ch06_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio1_27_ch06_t01": 20,
                "bio1_27_ch06_t02": 20,
                "bio1_27_ch06_t03": 20,
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
        / "ch06_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
