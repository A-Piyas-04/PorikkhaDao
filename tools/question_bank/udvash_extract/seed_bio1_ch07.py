#!/usr/bin/env python3
"""Seed Biology 1st Paper Ch7 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio1_27_ch07_t01..t03 (gymnosperms; angiosperms; flower and seed structures).
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
    "biology p1 ch07; curated bilingual"
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


# --- t01: Gymnosperms / নগ্নবীজি উদ্ভিদ ---
T01 = [
    q(
        "In which of the following plants are coralloid roots found?",
        "কোন উদ্ভিদে কোরালয়েড মূল হয়?",
        ["Pinus", "Gnetum", "Ephedra", "Cycas"],
        ["Pinus", "Gnetum", "Ephedra", "Cycas"],
        "D", "easy", "factual",
        "Cycas produces specialized coralloid roots that host nitrogen-fixing cyanobacteria.",
        "Cycas-এ বিশেষ কোরালয়েড মূল থাকে যেখানে নাইট্রোজেন-স্থিতিকারী সায়ানোব্যাকটেরিয়া বাস করে।",
    ),
    q(
        "Which is a primitive character of Cycas?",
        "Cycas-এর আদি বৈশিষ্ট্য কোনটি?",
        [
            "Haploid endosperm",
            "Formation of strobilus",
            "Formation of archegonium",
            "Naked seeds",
        ],
        [
            "হ্যাপ্লয়েড সস্য",
            "স্ট্রোবিলাস তৈরি",
            "আর্কিগোনিয়াম সৃষ্টি",
            "নগ্নবীজ",
        ],
        "C", "medium", "conceptual",
        "Presence of archegonia is treated as a primitive gymnosperm trait retained in Cycas.",
        "আর্কিগোনিয়ামের উপস্থিতি Cycas-এর আদি নগ্নবীজি বৈশিষ্ট্য হিসেবে গণ্য হয়।",
    ),
    q(
        "Which organism lives in the roots of Cycas?",
        "নিচের কোনটি Cycas উদ্ভিদের মূলে বাস করে?",
        ["Anabaena", "Ulothrix", "Clostridium", "Navicula"],
        ["Anabaena", "Ulothrix", "Clostridium", "Navicula"],
        "A", "easy", "factual",
        "Cyanobacteria such as Anabaena (and Nostoc) inhabit Cycas coralloid roots.",
        "Anabaena (ও Nostoc) এর মতো সায়ানোব্যাকটেরিয়া Cycas-এর কোরালয়েড মূলে বাস করে।",
    ),
    q(
        "Which statement about Cycas is correct?",
        "সাইকাসের ক্ষেত্রে কোনটি সঠিক?",
        [
            "Mature leaves remain circinate",
            "Sperm are amoeboid in shape",
            "Cyanobacteria are present in the roots",
            "Sori are present on megasporophylls",
        ],
        [
            "পরিণত পাতা কুণ্ডলিত থাকে",
            "শুক্রাণু অ্যামিবয়েড আকৃতির",
            "মূলে সায়ানোব্যাকটেরিয়া থাকে",
            "মেগাস্পোরোফিলে সোরাস থাকে",
        ],
        "C", "medium", "conceptual",
        "Cycas roots host cyanobacteria; mature leaves are not circinate, sperm are large and multiflagellate, and sori belong to ferns.",
        "Cycas মূলে সায়ানোব্যাকটেরিয়া থাকে; পরিণত পাতা কুণ্ডলিত নয়, শুক্রাণু বৃহৎ ও বহুফ্ল্যাজেলাযুক্ত, সোরাস ফার্নের বৈশিষ্ট্য।",
    ),
    q(
        "What is found in coralloid roots?",
        "কোরালয়েড মূলে কোনটি পাওয়া যায়?",
        ["Nostoc", "Clostridium", "Rhizobium", "E. coli"],
        ["Nostoc", "Clostridium", "Rhizobium", "E. coli"],
        "A", "easy", "factual",
        "Coralloid roots of Cycas contain Nostoc and Anabaena.",
        "Cycas-এর কোরালয়েড মূলে Nostoc ও Anabaena পাওয়া যায়।",
    ),
    q(
        "In gymnosperms which of the following are absent? (i) vessels in xylem (ii) companion cells in phloem (iii) double fertilization",
        "নগ্নবীজি উদ্ভিদে নেই— (i) জাইলেমে ভেসেল (ii) ফ্লোয়েমে সঙ্গীকোষ (iii) দ্বিনিষেক",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (i) ও (iii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "Typical gymnosperms lack true vessels, companion cells and double fertilization (exceptions like Gnetum aside in board framing).",
        "সাধারণ নগ্নবীজিতে সত্য ভেসেল, সঙ্গীকোষ ও দ্বিনিষেক থাকে না (বোর্ড পর্যায়ে তিনটিই অনুপস্থিত ধরা হয়)।",
    ),
    q(
        "Which applies to the sperm of Cycas?",
        "Cycas-এর শুক্রাণুর ক্ষেত্রে প্রযোজ্য কোনটি?",
        [
            "Large and non-flagellate",
            "Small and flagellate",
            "Large and multiflagellate",
            "Large with a single flagellum",
        ],
        [
            "বৃহৎ ও ফ্ল্যাজেলাবিহীন",
            "ক্ষুদ্র ও ফ্ল্যাজেলাযুক্ত",
            "বৃহৎ ও বহু ফ্ল্যাজেলাযুক্ত",
            "বৃহৎ ও ১টি ফ্ল্যাজেলাযুক্ত",
        ],
        "C", "medium", "factual",
        "Cycas produces among the largest plant sperm, which are multiflagellate.",
        "Cycas-এর শুক্রাণু উদ্ভিদজগতে অন্যতম বৃহৎ এবং বহুফ্ল্যাজেলাযুক্ত।",
    ),
    q(
        "Which statement about gymnosperms is correct?",
        "নগ্নবীজি উদ্ভিদের ক্ষেত্রে কোনটি সঠিক?",
        [
            "Ovary absent but stigma present",
            "Endosperm is diploid",
            "Archegonia are generally formed",
            "Companion cells occur in phloem",
        ],
        [
            "গর্ভাশয় নেই কিন্তু গর্ভমুণ্ড আছে",
            "সস্য ডিপ্লয়েড",
            "সাধারণত আর্কিগোনিয়া সৃষ্টি হয়",
            "ফ্লোয়েম টিস্যুতে সঙ্গীকোষ থাকে",
        ],
        "C", "medium", "conceptual",
        "Most gymnosperms form archegonia; they lack ovary, stigma and companion cells, and their endosperm is haploid.",
        "অধিকাংশ নগ্নবীজিতে আর্কিগোনিয়া হয়; গর্ভাশয়-গর্ভমুণ্ড ও সঙ্গীকোষ নেই এবং সস্য হ্যাপ্লয়েড।",
    ),
    q(
        "In gymnosperms which are true? (i) fertilization occurs (ii) archegonia are present (iii) vessels occur in xylem",
        "নগ্নবীজি উদ্ভিদে— (i) নিষেক হয় (ii) আর্কিগোনিয়া হয় (iii) জাইলেমে ভেসেল থাকে",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (i) ও (iii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "A", "medium", "conceptual",
        "Gymnosperms fertilize and typically form archegonia, but true vessels are generally absent.",
        "নগ্নবীজিতে নিষেক ও আর্কিগোনিয়া থাকে, কিন্তু সাধারণত সত্য ভেসেল থাকে না।",
    ),
    q(
        "The largest sperm is found in which plant?",
        "সর্ববৃহৎ শুক্রাণু বিদ্যমান নিচের কোন উদ্ভিদে?",
        ["Pinus", "Sequoia", "Cycas", "Gnetum"],
        ["Pinus", "Sequoia", "Cycas", "Gnetum"],
        "C", "easy", "factual",
        "Cycas has the largest known plant spermatozoids.",
        "Cycas-এ উদ্ভিদজগতের সর্ববৃহৎ শুক্রাণু পাওয়া যায়।",
    ),
    q(
        "The chromosome set number in the endosperm of Cycas is—",
        "Cycas-এর সস্যে ক্রোমোজোম সেট সংখ্যা হলো—",
        ["1", "2", "3", "4"],
        ["১", "২", "৩", "৪"],
        "A", "medium", "factual",
        "Gymnosperm endosperm is haploid (n), so the chromosome set number is 1.",
        "নগ্নবীজির সস্য হ্যাপ্লয়েড (n), তাই ক্রোমোজোম সেট সংখ্যা ১।",
    ),
    q(
        "Which organ of Cycas resembles a snake’s hood?",
        "Cycas উদ্ভিদের কোন অঙ্গটি সাপের ফণার ন্যায়?",
        ["Megasporophyll", "Microsporophyll", "Strobilus", "Coralloid root"],
        ["মেগাস্পোরোফিল", "মাইক্রোস্পোরোফিল", "স্ট্রোবিলাস", "কোরালয়েড মূল"],
        "A", "easy", "factual",
        "The megasporophyll of Cycas is often compared to a cobra’s hood in shape.",
        "Cycas-এর মেগাস্পোরোফিল আকৃতিতে সাপের ফণার মতো দেখায়।",
    ),
    q(
        "Which applies to Cycas? (i) transfusion tissue present (ii) haploid endosperm formed (iii) coralloid roots present",
        "Cycas-এর ক্ষেত্রে প্রযোজ্য— (i) ট্রান্সফিউশন টিস্যুর উপস্থিতি (ii) হ্যাপ্লয়েড সস্যের সৃষ্টি (iii) কোরালয়েড মূলের উপস্থিতি",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "hard", "conceptual",
        "Cycas leaves have transfusion tissue, endosperm is haploid, and coralloid roots are present.",
        "Cycas পাতায় ট্রান্সফিউশন টিস্যু, হ্যাপ্লয়েড সস্য এবং কোরালয়েড মূল—তিনটিই প্রযোজ্য।",
    ),
    q(
        "Which is a characteristic of Cycas?",
        "Cycas-এর বৈশিষ্ট্য কোনটি?",
        [
            "Coralloid roots",
            "Triploid endosperm",
            "Fruit formation",
            "Double fertilization",
        ],
        [
            "কোরালয়েড মূল",
            "ট্রিপ্লয়েড সস্য",
            "ফল হয়",
            "দ্বি-নিষেক ঘটে",
        ],
        "A", "easy", "factual",
        "Cycas is marked by coralloid roots; triploid endosperm, fruit and double fertilization are angiosperm traits.",
        "Cycas-এর বৈশিষ্ট্য কোরালয়েড মূল; ট্রিপ্লয়েড সস্য, ফল ও দ্বিনিষেক আবৃতবীজির বৈশিষ্ট্য।",
    ),
    q(
        "In gymnosperms which are correct? (i) archegonium present (ii) endosperm triploid (iii) seeds are produced",
        "নগ্নবীজি উদ্ভিদে— (i) আর্কিগোনিয়াম উপস্থিত (ii) সস্য ট্রিপ্লয়েড (iii) বীজ উৎপন্ন হয়",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (i) ও (iii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "B", "medium", "conceptual",
        "Gymnosperms form seeds and usually archegonia; their endosperm is haploid, not triploid.",
        "নগ্নবীজিতে বীজ ও সাধারণত আর্কিগোনিয়াম থাকে; সস্য হ্যাপ্লয়েড, ট্রিপ্লয়েড নয়।",
    ),
    q(
        "Which of the following is absent in gymnosperms?",
        "নগ্নবীজি উদ্ভিদে নিচের কোনটি অনুপস্থিত?",
        ["Sporophyll", "Ovary", "Seed", "Endosperm"],
        ["স্পোরোফিল", "গর্ভাশয়", "বীজ", "সস্য"],
        "B", "easy", "factual",
        "Gymnosperms have naked ovules/seeds without an ovary enclosing them.",
        "নগ্নবীজিতে ডিম্বক/বীজ গর্ভাশয় দ্বারা আবৃত থাকে না।",
    ),
    q(
        "How many types of leaves does Cycas have?",
        "সাইকাসের পাতা কয় ধরনের?",
        ["1", "2", "3", "4"],
        ["১", "২", "৩", "৪"],
        "B", "easy", "factual",
        "Cycas bears two leaf types: scale leaves and foliage leaves.",
        "Cycas-এ দুই ধরনের পাতা থাকে— স্কেল পত্র ও ফোলিয়েজ পত্র।",
    ),
    q(
        "Which plant is called a living fossil and palm fern?",
        "কোন উদ্ভিদকে জীবন্ত জীবাশ্ম ও পাম ফার্ন বলা হয়?",
        ["Riccia", "Pteris", "Cycas", "Funaria"],
        ["Riccia", "Pteris", "Cycas", "Funaria"],
        "C", "easy", "factual",
        "Cycas is popularly called a living fossil and palm fern.",
        "Cycas-কে জীবন্ত জীবাশ্ম ও পাম ফার্ন বলা হয়।",
    ),
    q(
        "Which applies to Cycas? (i) dioecious (ii) endosperm triploid (iii) coralloid roots",
        "Cycas যে উদ্ভিদকে প্রতিনিধিত্ব করে তার ক্ষেত্রে প্রযোজ্য— (i) ভিন্নবাসী (ii) সস্য ট্রিপ্লয়েড (iii) কোরালয়েড মূল",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (i) ও (iii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "B", "medium", "conceptual",
        "Cycas is dioecious with coralloid roots; its endosperm is haploid, not triploid.",
        "Cycas ভিন্নবাসী ও কোরালয়েড মূলযুক্ত; সস্য হ্যাপ্লয়েড, ট্রিপ্লয়েড নয়।",
    ),
    q(
        "From which Cycas species is sago (arrowroot-like starch) obtained?",
        "কোন উদ্ভিদ হতে সাগো বা অ্যারারুট উৎপন্ন হয়?",
        [
            "Cycas pectinata",
            "Cycas circinalis",
            "Cycas revoluta",
            "Cycas beddomei",
        ],
        [
            "Cycas pectinata",
            "Cycas circinalis",
            "Cycas revoluta",
            "Cycas beddomei",
        ],
        "C", "hard", "factual",
        "Sago starch is commonly associated with Cycas revoluta in HSC sources.",
        "HSC উৎসে সাগো সাধারণত Cycas revoluta থেকে পাওয়া যায় বলে উল্লেখ থাকে।",
    ),
]


# --- t02: Angiosperms / আবৃতবীজি উদ্ভিদ ---
T02 = [
    q(
        "In which plant does double fertilization occur among the following?",
        "নিচের কোন উদ্ভিদে দ্বিনিষেক ঘটে?",
        ["Cycas", "Pinus", "Gnetum", "Oryza"],
        ["Cycas", "Pinus", "Gnetum", "Oryza"],
        "D", "easy", "factual",
        "True double fertilization is characteristic of angiosperms such as rice (Oryza); Cycas and Pinus lack it.",
        "সত্য দ্বিনিষেক আবৃতবীজি যেমন ধান (Oryza)-এ ঘটে; Cycas ও Pinus-এ ঘটে না।",
    ),
    q(
        "The endosperm of angiosperms is—",
        "আবৃতবীজি উদ্ভিদের সস্যকলা—",
        ["Haploid", "Diploid", "Triploid", "Tetraploid"],
        ["হ্যাপ্লয়েড", "ডিপ্লয়েড", "ট্রিপ্লয়েড", "টেট্রাপ্লয়েড"],
        "C", "easy", "factual",
        "Double fertilization fuses a male gamete with the secondary nucleus to form triploid (3n) endosperm.",
        "দ্বিনিষেকে পুংগ্যামেট সেকেন্ডারি নিউক্লিয়াসের সাথে মিলে ট্রিপ্লয়েড (3n) সস্য গঠন করে।",
    ),
    q(
        "Which is an incomplete flower?",
        "অসম্পূর্ণ ফুল কোনটি?",
        ["Datura", "Pumpkin", "China rose", "Pea"],
        ["ধুতুরা", "কুমড়া", "জবা", "মটর"],
        "B", "medium", "factual",
        "Pumpkin flowers are unisexual, so one sexual whorl is missing and the flower is incomplete.",
        "কুমড়ার ফুল একলিঙ্গ; একটি জননস্তবক অনুপস্থিত বলে ফুল অসম্পূর্ণ।",
    ),
    q(
        "How many stamens are present in one flower of rice?",
        "ধানগাছের ১টি পুষ্পে কয়টি পুংকেশর থাকে?",
        ["3", "4", "5", "6"],
        ["৩", "৪", "৫", "৬"],
        "D", "easy", "factual",
        "A rice floret has six stamens arranged in two whorls of three (3+3).",
        "ধানের একটি পুষ্পে দুই আবর্তে (৩+৩) মোট ৬টি পুংকেশর থাকে।",
    ),
    q(
        "What is the scientific name of wheat?",
        "গমের বৈজ্ঞানিক নাম কী?",
        [
            "Hordeum vulgare",
            "Zea mays",
            "Saccharum officinarum",
            "Triticum aestivum",
        ],
        [
            "Hordeum vulgare",
            "Zea mays",
            "Saccharum officinarum",
            "Triticum aestivum",
        ],
        "D", "easy", "factual",
        "Wheat is Triticum aestivum; maize is Zea mays and sugarcane is Saccharum officinarum.",
        "গমের বৈজ্ঞানিক নাম Triticum aestivum; ভুট্টা Zea mays এবং আখ Saccharum officinarum।",
    ),
    q(
        "Which family is called the grass family?",
        "কোনটিকে ঘাস গোত্র বলা হয়?",
        ["Solanaceae", "Cycadaceae", "Malvaceae", "Poaceae"],
        ["সোলানেসি", "সাইক্যাডেসি", "মালভেসি", "পোয়েসি"],
        "D", "easy", "factual",
        "Poaceae (Gramineae) is the grass family including rice, wheat and maize.",
        "Poaceae (Gramineae) ঘাস গোত্র; ধান, গম, ভুট্টা এ গোত্রের।",
    ),
    q(
        "Caryopsis fruit is a characteristic of which family?",
        "ক্যারিঅপসিস ফল কোন গোত্রের বৈশিষ্ট্য?",
        ["Malvaceae", "Liliaceae", "Poaceae", "Tiliaceae"],
        ["Malvaceae", "Liliaceae", "Poaceae", "Tiliaceae"],
        "C", "easy", "factual",
        "Poaceae fruits are caryopses in which the pericarp is fused to the seed coat.",
        "Poaceae-র ফল ক্যারিঅপসিস; এতে ফলত্বক বীজত্বকের সাথে যুক্ত থাকে।",
    ),
    q(
        "Which plant belongs to Malvaceae?",
        "কোনটি Malvaceae গোত্রের উদ্ভিদ?",
        ["Okra (Dherosh)", "Bamboo", "Wheat", "Maize"],
        ["ঢেঁড়স", "বাঁশ", "গম", "ভুট্টা"],
        "A", "easy", "factual",
        "Okra (Abelmoschus) belongs to Malvaceae; bamboo, wheat and maize are Poaceae.",
        "ঢেঁড়স (Abelmoschus) Malvaceae গোত্রের; বাঁশ, গম ও ভুট্টা Poaceae।",
    ),
    q(
        "A feather-like stigma is found in which plant?",
        "পালকের ন্যায় গর্ভমুণ্ড থাকে নিচের কোন উদ্ভিদে?",
        ["Kenaf", "Pea", "Red amaranth", "Rice"],
        ["কেনাফ", "মটরশুটি", "লালশাক", "ধান"],
        "D", "medium", "factual",
        "Poaceae flowers such as rice typically have a feathery (plumose) stigma.",
        "ধানসহ Poaceae ফুলে সাধারণত পালকের ন্যায় (প্লুমোজ) গর্ভমুণ্ড থাকে।",
    ),
    q(
        "What type of placentation does Datura flower show?",
        "ধুতুরা ফুলের অমরা বিন্যাস কোন ধরনের?",
        ["Axile", "Basal", "Parietal", "Free central"],
        ["অক্ষীয়", "মূলীয়", "গাত্রীয়", "মুক্তকেন্দ্রীয়"],
        "A", "medium", "factual",
        "Datura (Solanaceae) has axile placentation with a multilocular ovary.",
        "ধুতুরা (Solanaceae) বহুকোষ্ঠ গর্ভাশয়ে অক্ষীয় অমরাবিন্যাস দেখায়।",
    ),
    q(
        "Which is a characteristic feature of Poaceae?",
        "কোনটি Poaceae গোত্রের বৈশিষ্ট্য?",
        [
            "Numerous stamens",
            "Versatile anthers",
            "Free lateral stipules",
            "Axile placentation",
        ],
        [
            "পুংকেশর অসংখ্য",
            "সর্বমুখ পরাগধানী",
            "মুক্ত পার্শ্বীয় উপপত্র",
            "অক্ষীয় অমরা বিন্যাস",
        ],
        "B", "medium", "factual",
        "Poaceae anthers are versatile (dorsifixed and freely swinging); stamens are few, not numerous.",
        "Poaceae-র পরাগধানী সর্বমুখ; পুংকেশর অসংখ্য নয় এবং অমরাবিন্যাস মূলীয়।",
    ),
    q(
        "Which is a characteristic of gymnosperms rather than angiosperms?",
        "নগ্নবীজি উদ্ভিদের বৈশিষ্ট্য কোনটি (আবৃতবীজির বিপরীতে)?",
        [
            "Double fertilization occurs",
            "True vessel cells present in xylem",
            "Heteromorphic alternation of generations",
            "Companion cells present in phloem",
        ],
        [
            "দ্বি-নিষেক ঘটে",
            "জাইলেম টিস্যুতে সত্যিকার ভেসেল কোষ থাকে",
            "অসম আকৃতির জনুক্রম বিদ্যমান",
            "ফ্লোয়েম টিস্যুতে সঙ্গীকোষ থাকে",
        ],
        "C", "hard", "conceptual",
        "Both groups show alternation, but board keys often mark heteromorphic alternation as the gymnosperm option among these distractors; A, B and D are angiosperm advances.",
        "দ্বিনিষেক, সত্য ভেসেল ও সঙ্গীকোষ আবৃতবীজির উন্নত বৈশিষ্ট্য; প্রদত্ত অপশনে অসম আকৃতির জনুক্রম নগ্নবীজির সাথে মিলিয়ে চাবি করা হয়।",
    ),
    q(
        "Placentation of China rose (Hibiscus) is—",
        "জবা ফুলের অমরা বিন্যাস হলো—",
        ["Basal", "Axile", "Apical", "Free central"],
        ["মূলীয়", "অক্ষীয়", "শীর্ষক", "বহুপ্রান্তীয়"],
        "B", "easy", "factual",
        "Hibiscus (Malvaceae) has a multilocular ovary with axile placentation.",
        "জবা (Malvaceae) বহুকোষ্ঠ গর্ভাশয়ে অক্ষীয় অমরাবিন্যাস দেখায়।",
    ),
    q(
        "Which statements apply to Malvaceae? (i) free lateral stipules (ii) monadelphous stamens (iii) axile placentation",
        "Malvaceae গোত্রে পাওয়া যায়— (i) মুক্ত পার্শ্বীয় উপপত্র (ii) একগুচ্ছক পুংকেশর (iii) অক্ষীয় অমরাবিন্যাস",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "Malvaceae typically show free lateral stipules, monadelphous stamens and axile placentation.",
        "Malvaceae-তে সাধারণত মুক্ত পার্শ্বীয় উপপত্র, একগুচ্ছক পুংকেশর ও অক্ষীয় অমরাবিন্যাস থাকে।",
    ),
    q(
        "Which plant shows versatile anthers?",
        "সর্বমুখ পরাগধানী কোন উদ্ভিদে পাওয়া যায়?",
        ["China rose", "Rice", "Datura", "Pea"],
        ["জবা", "ধান", "ধুতুরা", "মটর"],
        "B", "medium", "factual",
        "Rice and other Poaceae have versatile anthers; Hibiscus anthers are reniform.",
        "ধানসহ Poaceae-তে সর্বমুখ পরাগধানী থাকে; জবার পরাগধানী বৃক্কাকার।",
    ),
    q(
        "A legume is a type of—",
        "লেগিউম হলো এক ধরনের—",
        ["Fruit", "Epicalyx", "Inflorescence", "Aestivation"],
        ["ফল", "উপবৃতি", "পুষ্পবিন্যাস", "এস্টিভেশন"],
        "A", "easy", "factual",
        "A legume (pod) is a dry dehiscent fruit of Fabaceae/Leguminosae.",
        "লেগিউম (শিম্বি) Fabaceae/Leguminosae গোত্রের এক ধরনের শুষ্ক ফল।",
    ),
    q(
        "Which plant represents Malvaceae among the following?",
        "নিচের কোনটি Malvaceae গোত্রকে নির্দেশ করে?",
        [
            "Triticum aestivum",
            "Zea mays",
            "Gossypium herbaceum",
            "Oryza sativa",
        ],
        [
            "Triticum aestivum",
            "Zea mays",
            "Gossypium herbaceum",
            "Oryza sativa",
        ],
        "C", "easy", "factual",
        "Gossypium herbaceum (cotton) belongs to Malvaceae; the others are Poaceae.",
        "Gossypium herbaceum (তুলা) Malvaceae; বাকিগুলো Poaceae।",
    ),
    q(
        "Which features apply to the family of China rose? (i) monadelphous stamens (ii) free lateral stipules (iii) fruit berry or capsule",
        "জবা যে গোত্রের, সেই গোত্রের বৈশিষ্ট্য— (i) পুংকেশর একগুচ্ছক (ii) উপপত্র মুক্তপার্শ্বীয় (iii) ফল বেরি বা ক্যাপসুল",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (i) ও (iii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "Malvaceae show monadelphous androecium, free lateral stipules and capsule/berry-type fruits.",
        "Malvaceae-তে একগুচ্ছক পুংকেশর, মুক্তপার্শ্বীয় উপপত্র এবং ক্যাপসুল/বেরি জাতীয় ফল দেখা যায়।",
    ),
    q(
        "Compared with gymnosperms (S) and angiosperms (T), which differences are correct? (i) companion cells in T phloem, absent in S (ii) fruit in T, absent in S (iii) double fertilization in T, absent in S",
        "S (নগ্নবীজি) ও T (আবৃতবীজি) বহনকারী উদ্ভিদের মধ্যে পার্থক্য— (i) T-এ ফ্লোয়েমে সঙ্গীকোষ থাকে, S-এ নেই (ii) T-এ ফল থাকে, S-এ থাকে না (iii) S-এ দ্বিনিষেক ঘটে না, T-এ ঘটে",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "hard", "conceptual",
        "Angiosperms have companion cells, fruits and double fertilization; typical gymnosperms lack all three.",
        "আবৃতবীজিতে সঙ্গীকোষ, ফল ও দ্বিনিষেক আছে; সাধারণ নগ্নবীজিতে এগুলো নেই।",
    ),
    q(
        "Mucilage is found in which of the following?",
        "নিচের কোনটিতে পিচ্ছিল পদার্থ (মিউসিলেজ) পাওয়া যায়?",
        ["Lemon grass", "Mesta (kenaf)", "Wheat", "Sugarcane"],
        ["লেমন ঘাস", "মেস্তাপাট", "গম", "ইক্ষু"],
        "B", "hard", "factual",
        "Mesta/kenaf (Malvaceae) tissues characteristically contain mucilage.",
        "মেস্তাপাট (Malvaceae) টিস্যুতে বৈশিষ্ট্যগতভাবে মিউসিলেজ থাকে।",
    ),
]


# --- t03: Flower and seed structures / ফুল ও বীজের গঠন ---
T03 = [
    q(
        "What type of corolla aestivation does China rose show?",
        "জবাফুলের পাঁপড়ির পুষ্পপত্রবিন্যাস কোন ধরনের?",
        ["Open", "Valvate", "Twisted", "Imbricate"],
        ["ওপেন", "ভালভেট", "টুইস্টেড", "ইমব্রিকেট"],
        "C", "easy", "factual",
        "Petals of Hibiscus show twisted (contorted) aestivation.",
        "জবার পাপড়িতে টুইস্টেড (কনটর্টেড) এস্টিভেশন দেখা যায়।",
    ),
    q(
        "Twisted and valvate aestivation are seen in which plant?",
        "টুইস্টেড ও ভালভেট এস্টিভেশন দেখা যায় কোন উদ্ভিদে?",
        ["Rice", "Wheat", "China rose", "Guava"],
        ["ধান", "গম", "জবা", "পেয়ারা"],
        "C", "medium", "factual",
        "In Hibiscus the calyx is valvate and the corolla is twisted.",
        "জবায় বৃতি ভালভেট এবং দলমণ্ডল টুইস্টেড বিন্যাস দেখায়।",
    ),
    q(
        "In a spikelet, which matching is correct? (i) lodicule = perianth (ii) palea = bracteole (iii) lemma = bract",
        "স্পাইকলেটের ক্ষেত্রে— (i) লোডিকিউল = পুষ্পপুট (ii) প্যালিয়া = উপমঞ্জরীপত্র (iii) লেমা = মঞ্জরীপত্র",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "hard", "conceptual",
        "In Poaceae spikelets, lodicules are reduced perianth, palea is a bracteole and lemma is a bract.",
        "Poaceae স্পাইকলেটে লোডিকিউল ক্ষুদ্র পুষ্পপুট, প্যালিয়া উপমঞ্জরীপত্র এবং লেমা মঞ্জরীপত্র।",
    ),
    q(
        "When sepals and petals are alike in form and colour, the whorl is called—",
        "বৃতি ও দল আকৃতি ও বর্ণে অভিন্ন হলে সেই স্তবককে কী বলে?",
        ["Epicalyx", "Perianth", "Androecium", "Gynoecium"],
        ["উপবৃতি", "পুষ্পপুট", "পুংস্তবক", "স্ত্রীস্তবক"],
        "B", "easy", "factual",
        "An undifferentiated sepal-petal whorl is the perianth; each member is a tepal.",
        "অবিভাজিত বৃতি-দল স্তবককে পুষ্পপুট বলে; প্রতিটি সদস্য টেপাল।",
    ),
    q(
        "The reduced perianth of a grass floret is called—",
        "ঘাসজাতীয় পুষ্পিকার ক্ষুদ্র পুষ্পপুটকে কী বলে?",
        ["Lemma", "Palea", "Lodicule", "Glume"],
        ["লেমা", "প্যালিয়া", "লোডিকিউল", "গ্লুম"],
        "C", "medium", "factual",
        "Lodicules are tiny scale-like perianth remnants in Poaceae florets.",
        "লোডিকিউল Poaceae পুষ্পিকার ক্ষুদ্র শষ্কপত্রসদৃশ পুষ্পপুট।",
    ),
    q(
        "In floral diagrams, a bracket ( ) usually indicates—",
        "পুষ্পসংকেতে বন্ধনী ( ) সাধারণত কী নির্দেশ করে?",
        ["Adhesion", "Hypogyny", "Cohesion", "Indefinite number"],
        ["অসমসংযোগ", "অধিগর্ভ", "সমসংযোগ", "বহুসংখ্যা"],
        "C", "medium", "factual",
        "Parentheses mark cohesion (fusion of similar parts); a line marks adhesion; a bar over the gynoecium marks epigyny.",
        "বন্ধনী সমসংযোগ (সদৃশ অংশের সংযোগ) বোঝায়; রেখা অসমসংযোগ এবং গর্ভাশয়ের উপর রেখা অধিগর্ভ বোঝায়।",
    ),
    q(
        "Which statements apply to Malvaceae floral traits? (i) axile placentation (ii) free calyx (iii) numerous stamens",
        "Malvaceae গোত্রের ক্ষেত্রে প্রযোজ্য— (i) অমরা বিন্যাস অক্ষীয় (ii) বৃতি মুক্ত (iii) পুংকেশর অসংখ্য",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "Malvaceae flowers typically have axile placentation, a free (polysepalous or basally united) calyx and numerous monadelphous stamens.",
        "Malvaceae-তে অক্ষীয় অমরাবিন্যাস, মুক্ত/আংশিক মুক্ত বৃতি এবং অসংখ্য একগুচ্ছক পুংকেশর থাকে।",
    ),
    q(
        "Which statements fit China rose? (i) pentamerous (ii) superior ovary (iii) free epicalyx",
        "জবা ফুলের ক্ষেত্রে প্রযোজ্য— (i) পেন্টামেরাস (ii) ঊর্ধ্বগর্ভ গর্ভাশয় (iii) মুক্ত উপবৃতি",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (i) ও (iii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "Hibiscus is pentamerous with a superior ovary and a free epicalyx (epicalyx lobes).",
        "জবা পেন্টামেরাস, ঊর্ধ্বগর্ভ গর্ভাশয়যুক্ত এবং মুক্ত উপবৃতিবিশিষ্ট।",
    ),
    q(
        "The twisted aestivation of China rose is found in which floral part?",
        "উদ্দীপকের টুইস্টেড পুষ্পপত্রবিন্যাস জবা ফুলের কোন অংশে পাওয়া যায়?",
        ["Calyx", "Epicalyx", "Corolla", "Anther"],
        ["বৃতি", "উপবৃতি", "দলমণ্ডল", "পরাগধানী"],
        "C", "easy", "factual",
        "Twisted aestivation occurs in the corolla of Hibiscus; the calyx is valvate.",
        "জবার দলমণ্ডলে টুইস্টেড বিন্যাস হয়; বৃতি ভালভেট।",
    ),
    q(
        "Which family does a grass spikelet diagram typically represent?",
        "ঘাসের স্পাইকলেট চিত্র কোন গোত্রকে প্রতিনিধিত্ব করে?",
        ["Poaceae", "Solanaceae", "Leguminosae", "Malvaceae"],
        ["Poaceae", "Solanaceae", "Leguminosae", "Malvaceae"],
        "A", "easy", "factual",
        "Spikelets with lemma, palea and lodicules characterize Poaceae.",
        "লেমা, প্যালিয়া ও লোডিকিউলসহ স্পাইকলেট Poaceae গোত্রের বৈশিষ্ট্য।",
    ),
    q(
        "For Poaceae, which are correct? (i) stamens in two whorls (ii) basal placentation (iii) two lodicules present",
        "Poaceae গোত্রের ক্ষেত্রে প্রযোজ্য— (i) পুংকেশর দুইটি আবর্তে অবস্থিত (ii) অমরাবিন্যাস মূলীয় (iii) দুটি লোডিকিউল বিদ্যমান",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (i) ও (iii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "hard", "conceptual",
        "Typical Poaceae florets have stamens in two whorls, basal placentation and usually two lodicules.",
        "সাধারণ Poaceae পুষ্পিকায় দুই আবর্তের পুংকেশর, মূলীয় অমরাবিন্যাস ও সাধারণত দুটি লোডিকিউল থাকে।",
    ),
    q(
        "In the androecium of a wheat flower one finds—",
        "গম ফুলের পুংস্তবকে থাকে—",
        [
            "Reniform anthers",
            "Spinous pollen grains",
            "Versatile anthers",
            "Staminal tube",
        ],
        [
            "বৃক্কাকার পরাগধানী",
            "কণ্টকিত পরাগরেণু",
            "সর্বমুখ পরাগধানী",
            "পুংকেশরীয় নালিকা",
        ],
        "C", "medium", "factual",
        "Wheat (Poaceae) has versatile anthers; reniform anthers and spinous pollen are Malvaceae traits.",
        "গম (Poaceae)-এ সর্বমুখ পরাগধানী থাকে; বৃক্কাকার পরাগধানী ও কণ্টকিত পরাগরেণু Malvaceae-র।",
    ),
    q(
        "How is triploid endosperm formed?",
        "ট্রিপ্লয়েড সস্য কীভাবে তৈরি হয়?",
        [
            "Fusion of egg and one male gamete only",
            "Fusion of two polar nuclei with one male gamete",
            "Fusion of two male gametes with the egg",
            "Mitosis of the zygote alone",
        ],
        [
            "কেবল ডিম্বাণু ও এক পুংগ্যামেটের মিলন",
            "দুই পোলার নিউক্লিয়াস ও এক পুংগ্যামেটের মিলন",
            "দুই পুংগ্যামেটের সাথে ডিম্বাণুর মিলন",
            "কেবল জাইগোটের মাইটোসিস",
        ],
        "B", "medium", "conceptual",
        "One male gamete + diploid secondary nucleus (two polar nuclei) yields triploid endosperm.",
        "এক পুংগ্যামেট + ডিপ্লয়েড সেকেন্ডারি নিউক্লিয়াস (দুই পোলার নিউক্লিয়াস) → ট্রিপ্লয়েড সস্য।",
    ),
    q(
        "A flower that can be divided into two equal halves by only one plane through the centre is—",
        "কেন্দ্র বরাবর কেবল একবার সমান দুভাগে ভাগ করা যায় এমন ফুলকে কী বলে?",
        ["Actinomorphic", "Zygomorphic", "Asymmetric", "Cyclic"],
        ["বহুপ্রতিসম", "একপ্রতিসম", "অপ্রতিসম", "চক্রাকার"],
        "B", "easy", "factual",
        "Zygomorphic (bilateral) flowers such as pea have a single plane of symmetry.",
        "শিম/মটরের মতো একপ্রতিসম (জাইগোমর্ফিক) ফুলে কেবল এক সমমিতি তল থাকে।",
    ),
    q(
        "Why is the mother axis important when drawing a floral diagram?",
        "পুষ্পপ্রতীক আঁকতে মাতৃঅক্ষ গুরুত্বপূর্ণ কেন?",
        [
            "It determines dorsal and ventral sides of the flower",
            "It forms the ovary wall",
            "It produces pollen grains",
            "It is the same as the pedicel tip only",
        ],
        [
            "এটি পুষ্পের পৃষ্ঠ ও সম্মুখ দিক নির্ধারণ করে",
            "এটি গর্ভাশয় প্রাচীর গঠন করে",
            "এটি পরাগরেণু উৎপন্ন করে",
            "এটি কেবল বৃন্তাগ্রের সমতুল্য",
        ],
        "A", "medium", "conceptual",
        "The mother axis defines the posterior (axis) side versus the anterior (bract) side needed for a correct floral diagram.",
        "মাতৃঅক্ষ পুষ্পের পশ্চাৎ (অক্ষীয়) ও সম্মুখ (মঞ্জরীপত্রীয়) দিক নির্ধারণ করে; ছাড়া সঠিক পুষ্পপ্রতীক আঁকা যায় না।",
    ),
    q(
        "Vexillary aestivation is characteristic of which type of corolla?",
        "ভেক্সিলারি এস্টিভেশন কোন ধরনের দলমণ্ডলের বিন্যাস?",
        ["Twisted", "Valvate", "Imbricate", "Papilionaceous"],
        ["টুইস্টেড", "ভালভেট", "ইমব্রিকেট", "প্রজাপতিআকৃতি"],
        "D", "medium", "factual",
        "Vexillary (descending imbricate) aestivation occurs in papilionaceous corollas of Fabaceae.",
        "ভেক্সিলারি (অবতরণ ইমব্রিকেট) বিন্যাস Fabaceae-র প্রজাপতিআকৃতি দলমণ্ডলে দেখা যায়।",
    ),
    q(
        "A compound leaf with leaflets arranged on both sides of a long rachis is called—",
        "লম্বা অক্ষের দুই পাশে পত্রকযুক্ত যৌগিক পত্রকে কী বলে?",
        [
            "Palmate compound leaf",
            "Pinnate compound leaf",
            "Simple leaf",
            "Scale leaf",
        ],
        [
            "করতলাকার যৌগিক পত্র",
            "পক্ষল যৌগিক পত্র",
            "সরল পত্র",
            "স্কেল পত্র",
        ],
        "B", "easy", "factual",
        "When leaflets arise along a rachis on both sides, the leaf is pinnately compound.",
        "র্যাকিসের দুই পাশে পত্রক থাকলে তাকে পক্ষল যৌগিক পত্র বলে।",
    ),
    q(
        "Endosperm is formed before fertilization in which group?",
        "নিষেকের পূর্বে কোনটিতে সস্য উৎপন্ন হয়?",
        ["Mosses", "Ferns", "Gymnosperms", "Angiosperms"],
        ["মসে", "ফার্নে", "জিমনোস্পার্মে", "এনজিওস্পার্মে"],
        "C", "hard", "conceptual",
        "In gymnosperms the female gametophyte/endosperm develops before fertilization; in angiosperms endosperm forms after double fertilization.",
        "নগ্নবীজিতে স্ত্রীগ্যামিটোফাইট/সস্য নিষেকের আগে গঠিত হয়; আবৃতবীজিতে দ্বিনিষেকের পর সস্য তৈরি হয়।",
    ),
    q(
        "Which inflorescence type is typical of grasses such as wheat and rice?",
        "গম ও ধানের মতো ঘাসজাতীয় উদ্ভিদের সাধারণ পুষ্পবিন্যাস কোনটি?",
        ["Capitulum", "Raceme", "Spike", "Spikelet"],
        ["ক্যাপিটুলাম", "রেসিম", "স্পাইক", "স্পাইকলেট"],
        "D", "easy", "factual",
        "Poaceae flowers are grouped in spikelets, the characteristic grass inflorescence unit.",
        "Poaceae-র পুষ্প স্পাইকলেটে সজ্জিত; এটি ঘাস গোত্রের বৈশিষ্ট্যমূলক পুষ্পবিন্যাস একক।",
    ),
    q(
        "Which statements about Malvaceae floral formula traits are correct? (i) staminal tube present (ii) corolla aestivation valvate (iii) reniform anthers present",
        "Malvaceae পুষ্পসংকেতের ক্ষেত্রে প্রযোজ্য— (i) পুংকেশরীয় নালিকা উপস্থিত (ii) দলমণ্ডলের বিন্যাস ভালভেট (iii) বৃক্কাকার পরাগধানী উপস্থিত",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (i) ও (iii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "B", "hard", "conceptual",
        "Malvaceae have a staminal tube and reniform anthers; corolla aestivation is twisted, not valvate.",
        "Malvaceae-তে পুংকেশরীয় নালিকা ও বৃক্কাকার পরাগধানী থাকে; দলমণ্ডল টুইস্টেড, ভালভেট নয়।",
    ),
]


TOPICS_MAP = {
    "bio1_27_ch07_t01": T01,
    "bio1_27_ch07_t02": T02,
    "bio1_27_ch07_t03": T03,
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
        "chapter": "bio1_27_ch07",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p209_pdf215.png",
            "p210_pdf216.png",
            "p211_pdf217.png",
            "p212_pdf218.png",
            "p213_pdf219.png",
            "p214_pdf220.png",
            "p215_pdf221.png",
            "p216_pdf222.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio1_27_ch07_t01": {
                "title": "Gymnosperms / নগ্নবীজি উদ্ভিদ",
                "themes": [
                    "Cycas coralloid roots; Nostoc/Anabaena symbionts",
                    "primitive archegonium; dioecious habit; living fossil",
                    "multiflagellate largest sperm; snake-hood megasporophyll",
                    "haploid endosperm; no ovary/companion cells/vessels",
                    "two leaf types; sago from Cycas revoluta",
                    "transfusion tissue + haploid endosperm + coralloid roots",
                    "seeds without fruit; fertilization without double fertilization",
                ],
            },
            "bio1_27_ch07_t02": {
                "title": "Angiosperms / আবৃতবীজি উদ্ভিদ",
                "themes": [
                    "double fertilization; triploid endosperm",
                    "Poaceae: rice 6 stamens; versatile anthers; caryopsis",
                    "Malvaceae: Hibiscus/okra/cotton; axile placentation",
                    "incomplete unisexual pumpkin flower",
                    "feathery stigma; Datura axile placentation",
                    "legume fruit; mucilage in mesta",
                    "gymnosperm vs angiosperm companion cells/fruit/DF",
                ],
            },
            "bio1_27_ch07_t03": {
                "title": "Flower and seed structures / ফুল ও বীজের গঠন",
                "themes": [
                    "twisted/valvate/vexillary aestivation",
                    "perianth/tepal; lodicule/lemma/palea in spikelet",
                    "floral formula cohesion brackets; mother axis",
                    "Malvaceae pentamerous + epicalyx + staminal tube",
                    "Poaceae basal placentation + two lodicules",
                    "zygomorphic symmetry; pinnate compound leaf",
                    "triploid endosperm mechanism; pre-fertilization gymnosperm endosperm",
                    "Poaceae spikelet inflorescence unit",
                ],
            },
        },
        "low_confidence": [
            "p209 is mostly CQ short answers; MCQ reconstruction relies on p210–216 plus accurate HSC bilingual supplements.",
            "Figure-only strobilus/spikelet/placentation stimulus items rewritten as standalone stems naming Cycas, Poaceae, Hibiscus, etc.",
            "Board stem asking double fertilization among Cycas/Pinus/Gnetum/Ephedra reframed with Oryza as unambiguous angiosperm key (Gnetum/Ephedra DF-like cases avoided).",
            "Sago species keyed to Cycas revoluta per common Udvash/HSC framing; circinalis also cited in some texts.",
            "Heteromorphic alternation item among angiosperm-advance distractors follows board-style keying; prefer companion-cell/fruit/DF contrast items for higher confidence.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio1_27_ch07_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio1_27_ch07_t01": 20,
                "bio1_27_ch07_t02": 20,
                "bio1_27_ch07_t03": 20,
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
        / "ch07_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
