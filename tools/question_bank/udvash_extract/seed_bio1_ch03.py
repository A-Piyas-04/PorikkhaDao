#!/usr/bin/env python3
"""Seed Biology 1st Paper Ch3 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio1_27_ch03_t01..t03 (biomolecules; enzymes; metabolism).
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
    "biology p1 ch03; curated bilingual"
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


# --- t01: Biomolecules / জৈব অণু ---
T01 = [
    q(
        "How many amino acids commonly make up proteins in living cells?",
        "জীবকোষের প্রোটিন গঠনকারী অ্যামাইনো এসিড মোট কতটি?",
        ["10", "15", "20", "25"],
        ["১০", "১৫", "২০", "২৫"],
        "C", "easy", "factual",
        "About 20 standard amino acids are the building blocks of cellular proteins.",
        "কোষীয় প্রোটিনের গাঠনিক একক হিসেবে সাধারণত প্রায় ২০টি মানক অ্যামাইনো এসিড থাকে।",
    ),
    q(
        "Which of the following is a monosaccharide?",
        "নিচের কোনটি মনোস্যাকারাইড?",
        ["Ribose", "Maltose", "Cellobiose", "Sucrose"],
        ["রাইবোজ", "মলটোজ", "সেলোবায়োজ", "সুক্রোজ"],
        "A", "easy", "factual",
        "Ribose is a pentose monosaccharide; maltose, cellobiose and sucrose are disaccharides.",
        "রাইবোজ একটি পেন্টোজ মনোস্যাকারাইড; মলটোজ, সেলোবায়োজ ও সুক্রোজ ডাইস্যাকারাইড।",
    ),
    q(
        "Which is the smallest protein among the following?",
        "সবচেয়ে ক্ষুদ্র প্রোটিন কোনটি?",
        ["Prolamin", "Histone", "Protamine", "Glutelin"],
        ["প্রোলামিন", "হিস্টোন", "প্রোটামিন", "গুটেলিন"],
        "C", "easy", "factual",
        "Protamine is among the smallest known proteins (rich in basic amino acids).",
        "প্রোটামিন ক্ষুদ্রতম প্রোটিনগুলোর একটি (বেসিক অ্যামাইনো এসিডসমৃদ্ধ)।",
    ),
    q(
        "Which is an example of a phospholipid?",
        "কোনটি ফসফোলিপিডের উদাহরণ?",
        ["Lecithin", "Suberin", "Cutin", "Terpene"],
        ["লেসিথিন", "সুবেরিন", "কিউটিন", "টারপিন"],
        "A", "easy", "factual",
        "Lecithin (phosphatidylcholine) is a classic phospholipid of membranes.",
        "লেসিথিন (ফসফাটিডিলকোলিন) ঝিল্লির ক্লাসিক ফসফোলিপিড উদাহরণ।",
    ),
    q(
        "Which compound is mainly responsible for fragrance in many plants?",
        "উদ্ভিদে সুগন্ধি সৃষ্টির জন্য প্রধানত কোনটি দায়ী?",
        ["Steroid", "Terpenoid", "Triglyceride", "Glycolipid"],
        ["স্টেরয়েড", "টারপিনয়েড", "ট্রাইগ্লিসারাইড", "গ্লাইকোলিপিড"],
        "B", "easy", "factual",
        "Terpenoids (essential oils) give characteristic plant fragrances.",
        "টারপিনয়েড (অত্যাবশ্যকীয় তেল) উদ্ভিদের বৈশিষ্ট্যমূলক সুগন্ধ দেয়।",
    ),
    q(
        "Which biomolecule mainly provides mechanical support/load-bearing in plants?",
        "উদ্ভিদের ভার বহনে প্রধান ভূমিকা রাখে কোনটি?",
        ["Cellulose", "Glycogen", "Amino acid", "Cholesterol"],
        ["সেলুলোজ", "গ্লাইকোজেন", "অ্যামাইনো এসিড", "কোলেস্টেরল"],
        "A", "easy", "factual",
        "Cellulose microfibrils in the cell wall give tensile strength and support.",
        "কোষপ্রাচীরের সেলুলোজ মাইক্রোফাইব্রিল টানসহনশীলতা ও যান্ত্রিক ভারবহন দেয়।",
    ),
    q(
        "Cholesterol belongs to which class of biomolecules?",
        "কোলেস্টেরল কোন জাতীয় পদার্থ?",
        ["Carbohydrate", "Protein", "Lipid", "Vitamin"],
        ["কার্বোহাইড্রেট", "প্রোটিন", "লিপিড", "ভিটামিন"],
        "C", "easy", "factual",
        "Cholesterol is a sterol lipid (often classed with derived lipids in HSC texts).",
        "কোলেস্টেরল একটি স্টেরল লিপিড (HSC পাঠে প্রায়শই উদ্ভূত লিপিড)।",
    ),
    q(
        "Which sugar is commonly known as cane sugar or beet sugar?",
        "কোনটি ইক্ষু ও বীটের চিনি নামে পরিচিত?",
        ["Maltose", "Sucrose", "Glucose", "Fructose"],
        ["মলটোজ", "সুক্রোজ", "গ্লুকোজ", "ফ্রুক্টোজ"],
        "B", "easy", "factual",
        "Sucrose is the disaccharide obtained commercially from sugarcane and sugar beet.",
        "সুক্রোজ ইক্ষু ও চিনিবীট থেকে বাণিজ্যিকভাবে পাওয়া ডাইস্যাকারাইড।",
    ),
    q(
        "Carotenoids are classified as:",
        "ক্যারোটিনয়েড হলো:",
        ["Mineral", "Carbohydrate", "Protein", "Lipid"],
        ["মিনারেল", "কার্বোহাইড্রেট", "প্রোটিন", "লিপিড"],
        "D", "easy", "factual",
        "Carotenoids are lipid-soluble pigments (derived lipids in many HSC classifications).",
        "ক্যারোটিনয়েড লিপিড-দ্রবণীয় রঞ্জক (অনেক HSC শ্রেণিতে উদ্ভূত লিপিড)।",
    ),
    q(
        "Glycosidic bonds are involved in forming: (i) disaccharides (ii) oligosaccharides (iii) polysaccharides. Which is correct?",
        "গ্লাইকোসাইডিক বন্ধনে তৈরি হয়: (i) ডাইস্যাকারাইড (ii) অলিগোস্যাকারাইড (iii) পলিস্যাকারাইড। কোনটি সঠিক?",
        [
            "i and ii only",
            "i and iii only",
            "ii and iii only",
            "i, ii and iii",
        ],
        [
            "কেবল i ও ii",
            "কেবল i ও iii",
            "কেবল ii ও iii",
            "i, ii ও iii",
        ],
        "D", "medium", "conceptual",
        "All sugar polymers beyond monosaccharides are linked by glycosidic bonds.",
        "মনোস্যাকারাইডের ঊর্ধ্বে সব শর্করা পলিমার গ্লাইকোসাইডিক বন্ধনে যুক্ত।",
    ),
    q(
        "A tasteless, water-insoluble plant carbohydrate with little nutritive value for humans is:",
        "স্বাদহীন, পানিতে অদ্রবণীয় এবং মানুষের জন্য পুষ্টিগুণহীন উদ্ভিদ কার্বোহাইড্রেট কোনটি?",
        ["Starch", "Cellulose", "Glycogen", "Dextrin"],
        ["স্টার্চ", "সেলুলোজ", "গ্লাইকোজেন", "ডেক্সট্রিন"],
        "B", "easy", "factual",
        "Cellulose is the main structural polysaccharide; humans lack cellulase.",
        "সেলুলোজ প্রধান গাঠনিক পলিস্যাকারাইড; মানুষের দেহে সেলুলেজ নেই।",
    ),
    q(
        "Which protein type is abundant in egg white?",
        "ডিমের সাদা অংশে কোন ধরনের প্রোটিন থাকে?",
        ["Globulin", "Albumin", "Histone", "Protamine"],
        ["গ্লোবিউলিন", "অ্যালবুমিন", "হিস্টোন", "প্রোটামিন"],
        "B", "easy", "factual",
        "Egg white is rich in albumins (e.g. ovalbumin).",
        "ডিমের সাদা অংশে অ্যালবুমিন (যেমন ওভ্যালবুমিন) অধিক থাকে।",
    ),
    q(
        "If the non-protein part of a conjugated protein is a metal, it is called a:",
        "যুগ্ম প্রোটিনের অপ্রোটিন অংশ ধাতব পদার্থ হলে তাকে বলে:",
        ["Cofactor", "Coenzyme", "Apoenzyme", "Substrate"],
        ["কো-ফ্যাক্টর", "কো-এনজাইম", "অ্যাপো-এনজাইম", "সাবস্ট্রেট"],
        "A", "medium", "factual",
        "Inorganic metal helpers are cofactors; organic helpers are coenzymes.",
        "অজৈব ধাতব সহায়ক কো-ফ্যাক্টর; জৈব সহায়ক কো-এনজাইম।",
    ),
    q(
        "Which are reducing sugars? (i) glucose (ii) sucrose (iii) fructose. Which is correct?",
        "বিজারক শর্করার উদাহরণ: (i) গ্লুকোজ (ii) সুক্রোজ (iii) ফ্রুক্টোজ। কোনটি সঠিক?",
        [
            "i only",
            "i and iii only",
            "ii and iii only",
            "i, ii and iii",
        ],
        [
            "কেবল i",
            "কেবল i ও iii",
            "কেবল ii ও iii",
            "i, ii ও iii",
        ],
        "B", "medium", "conceptual",
        "Glucose and fructose are reducing; sucrose is non-reducing (both anomeric carbons tied).",
        "গ্লুকোজ ও ফ্রুক্টোজ বিজারক; সুক্রোজে উভয় অ্যানোমেরিক কার্বন বন্ধনে আটকা, তাই অবিজারক।",
    ),
    q(
        "Oryzenin of rice belongs to which protein group?",
        "ধানের ওরাইজেনিন কোন ধরনের প্রোটিন?",
        ["Globulin", "Glutelin", "Prolamin", "Protamine"],
        ["গ্লোবিউলিন", "গুটেলিন", "প্রোলামিন", "প্রোটামিন"],
        "B", "medium", "factual",
        "Oryzenin is the major glutelin storage protein of rice grains.",
        "ওরাইজেনিন ধানের প্রধান গুটেলিন জাতীয় সঞ্চয়ী প্রোটিন।",
    ),
    q(
        "Glycosidic bonds are characteristically found in:",
        "গ্লাইকোসাইডিক বন্ধন দেখা যায়:",
        ["Carbohydrates", "Proteins", "Lipids", "Enzymes only as a class"],
        ["কার্বোহাইড্রেটে", "প্রোটিনে", "লিপিডে", "কেবল এনজাইম শ্রেণিতে"],
        "A", "easy", "factual",
        "Glycosidic linkages join sugar units in carbohydrates.",
        "কার্বোহাইড্রেটে শর্করা এককগুলো গ্লাইকোসাইডিক বন্ধনে যুক্ত হয়।",
    ),
    q(
        "Peptide bonds are found in which biomolecules?",
        "পেপটাইড বন্ধনী কোন যৌগে দেখা যায়?",
        ["Carbohydrate", "Lipid", "Protein", "Vitamin"],
        ["কার্বোহাইড্রেট", "লিপিড", "প্রোটিন", "ভিটামিন"],
        "C", "easy", "factual",
        "Peptide bonds link amino acids in proteins and peptides.",
        "প্রোটিন ও পেপটাইডে অ্যামাইনো এসিড পেপটাইড বন্ধনে যুক্ত থাকে।",
    ),
    q(
        "Hemoglobin is an example of a:",
        "হিমোগ্লোবিন হলো:",
        ["Conjugated protein", "Phospholipid", "Enzyme", "Cholesterol"],
        ["যুগ্ম প্রোটিন", "ফসফোলিপিড", "এনজাইম", "কোলেস্টেরল"],
        "A", "easy", "factual",
        "Hemoglobin is a conjugated protein (globin + heme prosthetic group).",
        "হিমোগ্লোবিন যুগ্ম প্রোটিন (গ্লোবিন + হিম প্রোস্থেটিক গ্রুপ)।",
    ),
    q(
        "In carbohydrates, the typical atomic ratio of C : H : O is:",
        "কার্বোহাইড্রেটে কার্বন, হাইড্রোজেন ও অক্সিজেনের অনুপাত সাধারণত:",
        ["1 : 1 : 2", "2 : 1 : 1", "1 : 2 : 1", "1 : 2 : 3"],
        ["১ : ১ : ২", "২ : ১ : ১", "১ : ২ : ১", "১ : ২ : ৩"],
        "C", "easy", "factual",
        "General formula approximates Cn(H2O)n, so C:H:O ≈ 1:2:1.",
        "সাধারণ সূত্র Cn(H2O)n অনুসারে C:H:O ≈ ১:২:১।",
    ),
    q(
        "Which lipid type is obtained from tulsi, mint and pine plants?",
        "তুলসি, পুদিনা ও পাইন উদ্ভিদ থেকে কোন লিপিড পাওয়া যায়?",
        ["Terpenes", "Cholesterol", "Phospholipid", "Glyceride only"],
        ["টারপিনস", "কোলেস্টেরল", "ফসফোলিপিড", "কেবল গ্লিসারাইড"],
        "A", "medium", "factual",
        "Essential oil terpenes are characteristic of aromatic plants like basil, mint and pine.",
        "সুগন্ধি উদ্ভিদ যেমন তুলসি, পুদিনা ও পাইনে অত্যাবশ্যকীয় তেল/টারপিন পাওয়া যায়।",
    ),
]


# --- t02: Enzymes / এনজাইম ---
T02 = [
    q(
        "The conversion glucose-6-phosphate ⇌ fructose-6-phosphate is catalyzed by which enzyme class?",
        "গ্লুকোজ-৬-ফসফেট ⇌ ফ্রুক্টোজ-৬-ফসফেট বিক্রিয়া কোন এনজাইম দ্বারা প্রভাবিত হয়?",
        ["Hydrolase", "Isomerase", "Transferase", "Lyase"],
        ["হাইড্রোলেজ", "আইসোমারেজ", "ট্রান্সফারেজ", "লাইয়েজ"],
        "B", "medium", "factual",
        "Phosphoglucose isomerase (an isomerase) interconverts these hexose phosphates.",
        "ফসফোগ্লুকোজ আইসোমারেজ (আইসোমারেজ শ্রেণি) এ দুই হেক্সোজ ফসফেটকে আন্তরূপান্তর করে।",
    ),
    q(
        "About coenzymes: (i) they are not proteins (ii) they can be dialyzed (iii) they can catalyze alone. Which is correct?",
        "কো-এনজাইম সম্পর্কে: (i) প্রোটিন নয় (ii) ডায়ালাইসিস করা যায় (iii) স্বতন্ত্রভাবে কাজ করতে পারে। কোনটি সঠিক?",
        [
            "i only",
            "i and ii only",
            "ii and iii only",
            "i, ii and iii",
        ],
        [
            "কেবল i",
            "কেবল i ও ii",
            "কেবল ii ও iii",
            "i, ii ও iii",
        ],
        "B", "medium", "conceptual",
        "Coenzymes are non-protein, often dialyzable helpers; catalysis needs the apoenzyme too.",
        "কো-এনজাইম অপ্রোটিন ও প্রায়শই ডায়ালাইজেবল সহায়ক; একাকী নয়, অ্যাপো-এনজাইমের সাথে কাজ করে।",
    ),
    q(
        "What is the physical nature of enzymes?",
        "এনজাইমের প্রকৃতি কীরূপ?",
        ["Colloidal", "Solid crystal only", "Pure liquid only", "Gas only"],
        ["কলয়েড", "কেবল কঠিন স্ফটিক", "কেবল বিশুদ্ধ তরল", "কেবল গ্যাস"],
        "A", "easy", "factual",
        "Enzymes behave as colloids in aqueous systems (protein sols).",
        "জলীয় মাধ্যমে এনজাইম কলয়েড (প্রোটিন সল) হিসেবে আচরণ করে।",
    ),
    q(
        "If the non-protein organic part of a conjugated protein/enzyme is organic, it is called a:",
        "যুগ্ম প্রোটিনের অপ্রোটিন অংশ জৈব রাসায়নিক পদার্থ হলে তাকে বলা হয়:",
        ["Activator", "Cofactor (general metal term only)", "Coenzyme", "Apoenzyme"],
        ["অ্যাকটিভেটর", "কেবল ধাতব কো-ফ্যাক্টর", "কো-এনজাইম", "অ্যাপো-এনজাইম"],
        "C", "medium", "factual",
        "Organic non-protein helpers are coenzymes; the protein alone is the apoenzyme.",
        "জৈব অপ্রোটিন সহায়ক কো-এনজাইম; কেবল প্রোটিন অংশ অ্যাপো-এনজাইম।",
    ),
    q(
        "Which scientist proposed the lock-and-key theory of enzyme action?",
        "কোন বিজ্ঞানী তালা-চাবি মতবাদ প্রদান করেন?",
        ["Emil Fischer", "D. Koshland", "Diener", "T. H. Morgan"],
        ["এমিল ফিশার", "ডি. কোশল্যান্ড", "ডিনার", "টি. এইচ. মর্গান"],
        "A", "easy", "factual",
        "Emil Fischer proposed the lock-and-key model; Koshland later proposed induced fit.",
        "এমিল ফিশার তালা-চাবি মডেল দেন; কোশল্যান্ড পরে ইনডিউসড ফিট দেন।",
    ),
    q(
        "Which enzyme digests lipids?",
        "কোনটি লিপিড পরিপাককারী এনজাইম?",
        ["Invertase", "Cellulase", "Lipase", "Sucrase only as a name for starch"],
        ["ইনভারটেজ", "সেলুলেজ", "লাইপেজ", "স্টার্চের নাম হিসেবে কেবল সুক্রেজ"],
        "C", "easy", "factual",
        "Lipases hydrolyze fats/oils into fatty acids and glycerol.",
        "লাইপেজ চর্বি/তেলকে ফ্যাটি এসিড ও গ্লিসারলে হাইড্রোলাইজ করে।",
    ),
    q(
        "Which enzyme helps cattle digest grass cellulose?",
        "গবাদিপশুকে ঘাস হজম করতে সহায়তা করে কোন এনজাইম?",
        ["Trypsin", "Pepsin", "Cellulase", "Zymase"],
        ["ট্রিপসিন", "পেপসিন", "সেলুলেজ", "জাইমেজ"],
        "C", "easy", "factual",
        "Rumen microbes produce cellulase that breaks down cellulose in forage.",
        "রূমেনের অণুজীব সেলুলেজ তৈরি করে যা ঘাসের সেলুলোজ ভেঙে দেয়।",
    ),
    q(
        "According to lock-and-key style enzyme use in industry, enzymes are applied in:",
        "তালা-চাবি মডেল অনুসরণকারী এনজাইমের শিল্প প্রয়োগের উদাহরণ:",
        [
            "Fruit-juice clarification/preparation",
            "Cellulose synthesis in factories only",
            "Hormone manufacture as the only use",
            "Sucrose photosynthesis in chloroplasts only",
        ],
        [
            "ফলের রস প্রস্তুতি/স্বচ্ছকরণে",
            "কেবল কারখানায় সেলুলোজ সংশ্লেষে",
            "কেবল হরমোন তৈরিতে",
            "কেবল ক্লোরোপ্লাস্টে সুক্রোজ সালোকসংশ্লেষে",
        ],
        "A", "medium", "application",
        "Board stems link enzyme catalysts (e.g. pectinases) to fruit-juice processing.",
        "বোর্ড উদ্দীপকে এনজাইম (যেমন পেকটিনেজ) ফলের রস প্রস্তুতির সাথে যুক্ত।",
    ),
    q(
        "Enzyme properties: (i) colloidal nature (ii) unchanged after reaction (iii) slow the reaction rate. Which is correct?",
        "এনজাইমের বৈশিষ্ট্য: (i) কলয়েড প্রকৃতির (ii) বিক্রিয়া শেষে অপরিবর্তিত থাকে (iii) বিক্রিয়ার গতিকে মন্থর করে। কোনটি সঠিক?",
        [
            "i and ii only",
            "ii and iii only",
            "i and iii only",
            "i, ii and iii",
        ],
        [
            "কেবল i ও ii",
            "কেবল ii ও iii",
            "কেবল i ও iii",
            "i, ii ও iii",
        ],
        "A", "medium", "conceptual",
        "Enzymes are colloidal biocatalysts regenerated after use; they accelerate, not slow, reactions.",
        "এনজাইম কলয়েড জৈব অনুঘটক এবং পুনরুত্থিত হয়; এরা বিক্রিয়া দ্রুত করে, মন্থর করে না।",
    ),
    q(
        "Which metal ion commonly increases enzyme activity as an activator?",
        "কোনটি এনজাইমের কর্মক্ষমতা বাড়িয়ে দেয় (অ্যাকটিভেটর হিসেবে)?",
        ["Ag", "Zn", "Pb only as activator", "Hg only as activator"],
        ["Ag", "Zn", "কেবল অ্যাকটিভেটর হিসেবে Pb", "কেবল অ্যাকটিভেটর হিসেবে Hg"],
        "B", "medium", "factual",
        "Zn (and often Mn, Mg, Cu) can activate enzymes; heavy metals like Ag/Hg often inhibit.",
        "Zn (এবং প্রায়শই Mn, Mg, Cu) অ্যাকটিভেটর হতে পারে; Ag/Hg প্রায়শই ইনহিবিটর।",
    ),
    q(
        "The special biochemical used to clarify cloudy grape juice is typically:",
        "আঙ্গুরের রস স্বচ্ছ করতে ব্যবহৃত বিশেষ জৈব রাসায়নিক পদার্থ সাধারণত:",
        ["Pectinase", "Trypsin", "Rennin", "Zymase"],
        ["পেকটিনেজ", "ট্রিপসিন", "রেনিন", "জাইমেজ"],
        "A", "medium", "application",
        "Pectinase breaks pectin that causes haze in fruit juices.",
        "পেকটিনেজ পেকটিন ভেঙে ফলের রসের ঘোলাভাব কমায়।",
    ),
    q(
        "Features of the clarifying enzyme (pectinase-type): (i) biocatalyst (ii) proteinaceous (iii) unchanged after reaction. Which is correct?",
        "রস স্বচ্ছকরণ এনজাইমের বৈশিষ্ট্য: (i) জৈব অনুঘটক (ii) প্রোটিন দ্বারা গঠিত (iii) বিক্রিয়া শেষে অপরিবর্তিত থাকে। কোনটি সঠিক?",
        [
            "i only",
            "i and iii only",
            "ii and iii only",
            "i, ii and iii",
        ],
        [
            "কেবল i",
            "কেবল i ও iii",
            "কেবল ii ও iii",
            "i, ii ও iii",
        ],
        "D", "medium", "conceptual",
        "Enzymes are protein biocatalysts regenerated after the reaction.",
        "এনজাইম প্রোটিন জৈব অনুঘটক এবং বিক্রিয়ার পর অপরিবর্তিত/পুনরুত্থিত থাকে।",
    ),
    q(
        "Which enzyme is used in removing cataract of the eye lens (board item)?",
        "চোখের ছানি অপসারণে লেন্সে ব্যবহৃত এনজাইম কোনটি?",
        ["Pectin", "Pepsin", "Zymase", "Trypsin"],
        ["পেকটিন", "পেপসিন", "জাইমেজ", "ট্রিপসিন"],
        "D", "hard", "factual",
        "HSC/Udvash keys commonly list trypsin among enzymes used in cataract-related procedures.",
        "HSC/উদ্ভাস উত্তরমালায় ছানি-সংক্রান্ত প্রক্রিয়ায় ট্রিপসিন উল্লেখিত।",
    ),
    q(
        "Enzymes are generally destroyed/denatured by:",
        "এনজাইম সাধারণত বিনষ্ট/বিকৃত হয়:",
        [
            "High heat (excessive temperature)",
            "Only very low substrate amount forever",
            "Only darkness without exception",
            "Only distilled water at all temperatures",
        ],
        [
            "অধিক তাপে (অতিরিক্ত উষ্ণতায়)",
            "কেবল চিরদিন অতি অল্প সাবস্ট্রেটে",
            "ব্যতিক্রমহীনভাবে কেবল অন্ধকারে",
            "সব তাপমাত্রায় কেবল ডিস্টিলড পানিতে",
        ],
        "A", "easy", "factual",
        "Excess heat denatures the protein structure of enzymes.",
        "অতিরিক্ত তাপ এনজাইমের প্রোটিন গঠন বিকৃত (ডিন্যাচার) করে।",
    ),
    q(
        "Solubility traits often listed for enzymes include: (i) soluble in water, dilute acid and dilute alcohol (ii) used in tannery for dehairing hides (iii) destroyed at low heat only and never at high heat. Which is correct?",
        "এনজাইমের বৈশিষ্ট্য হিসেবে: (i) পানি, লঘু অ্যাসিড ও লঘু অ্যালকোহলে দ্রবণীয় (ii) ট্যানারিতে চামড়ার লোম ছাড়ায় (iii) কেবল কম তাপে নষ্ট হয়, অধিক তাপে নয়। কোনটি সঠিক?",
        [
            "i and ii only",
            "i and iii only",
            "ii and iii only",
            "i, ii and iii",
        ],
        [
            "কেবল i ও ii",
            "কেবল i ও iii",
            "কেবল ii ও iii",
            "i, ii ও iii",
        ],
        "A", "hard", "conceptual",
        "Board keys accept solubility and tannery protease use; enzymes are destroyed by high heat, not only low heat.",
        "বোর্ড চাবিতে দ্রবণীয়তা ও ট্যানারি প্রোটিয়েজ ব্যবহার গৃহীত; এনজাইম অধিক তাপে বিনষ্ট হয়।",
    ),
    q(
        "Which protein is insoluble in water among the following?",
        "কোন প্রোটিন পানিতে অদ্রবণীয়?",
        ["Glutelin", "Protamine", "Albumin", "Histone"],
        ["গুটেলিন", "প্রোটামিন", "অ্যালবুমিন", "হিস্টোন"],
        "A", "medium", "factual",
        "Glutelins dissolve in dilute acid/alkali but not in water; albumins/histones/protamines are more soluble.",
        "গুটেলিন পানিতে অদ্রবণীয় কিন্তু লঘু অ্যাসিড/ক্ষারে দ্রবণীয়; অ্যালবুমিন ইত্যাদি অধিক দ্রবণীয়।",
    ),
    q(
        "Which protein dissolves in alcohol (70–80% ethanol), not water?",
        "কোনটি অ্যালকোহলে (৭০–৮০% ইথানল) দ্রবীভূত হয়?",
        ["Protamine", "Prolamin", "Globulin", "Glutelin"],
        ["প্রোটামিন", "প্রোলামিন", "গ্লোবিউলিন", "গুটেলিন"],
        "B", "medium", "factual",
        "Prolamins (e.g. zein, gliadin) are soluble in aqueous alcohol.",
        "প্রোলামিন (যেমন জেইন, গ্লিয়াডিন) জলীয় অ্যালকোহলে দ্রবণীয়।",
    ),
    q(
        "Protein features: (i) colloidal (ii) soluble in alcohol as a general rule (iii) electrolytic. Which is correct?",
        "প্রোটিনের বৈশিষ্ট্য: (i) কলয়েড ধর্মী (ii) সাধারণ নিয়মে অ্যালকোহলে দ্রবণীয় (iii) তড়িৎধর্মী। কোনটি সঠিক?",
        [
            "i and ii only",
            "i and iii only",
            "ii and iii only",
            "i, ii and iii",
        ],
        [
            "কেবল i ও ii",
            "কেবল i ও iii",
            "কেবল ii ও iii",
            "i, ii ও iii",
        ],
        "B", "medium", "conceptual",
        "Proteins are colloidal and amphoteric/electrolytic; most are not freely alcohol-soluble (prolamins are exceptions).",
        "প্রোটিন কলয়েড ও অ্যামফোটেরিক/তড়িৎধর্মী; অধিকাংশ অ্যালকোহলে অদ্রবণীয় (প্রোলামিন ব্যতিক্রম)।",
    ),
    q(
        "Fish and meat foods: (i) mainly form cell membranes (ii) coagulate with acid (iii) are built of amino acids. Which is correct?",
        "মাছ ও মাংস জাতীয় খাদ্য: (i) প্রধানত কোষঝিল্লি গঠন করে (ii) অ্যাসিড প্রয়োগে তঞ্চিত হয় (iii) অ্যামাইনো এসিড দ্বারা গঠিত। কোনটি সঠিক?",
        [
            "i and ii only",
            "i and iii only",
            "ii and iii only",
            "i, ii and iii",
        ],
        [
            "কেবল i ও ii",
            "কেবল i ও iii",
            "কেবল ii ও iii",
            "i, ii ও iii",
        ],
        "C", "medium", "conceptual",
        "Meat/fish are largely protein (amino acids; acid coagulation); membranes are mainly lipid bilayers.",
        "মাছ-মাংস মূলত প্রোটিন (অ্যামাইনো এসিড; অ্যাসিডে তঞ্চন); কোষঝিল্লি প্রধানত লিপিড দ্বিস্তর।",
    ),
    q(
        "Which statement correctly matches enzyme vocabulary?",
        "কোনটি এনজাইম পরিভাষার সঠিক মিল?",
        [
            "Apoenzyme = protein part; coenzyme = organic helper; holoenzyme = complete active enzyme",
            "Apoenzyme = metal only; coenzyme = whole protein catalyst alone",
            "Holoenzyme = substrate only; apoenzyme = product only",
            "Coenzyme = cellulose fiber only; apoenzyme = starch only",
        ],
        [
            "অ্যাপো-এনজাইম = প্রোটিন অংশ; কো-এনজাইম = জৈব সহায়ক; হলো-এনজাইম = সম্পূর্ণ সক্রিয় এনজাইম",
            "অ্যাপো-এনজাইম = কেবল ধাতু; কো-এনজাইম = একাকী সম্পূর্ণ প্রোটিন অনুঘটক",
            "হলো-এনজাইম = কেবল সাবস্ট্রেট; অ্যাপো-এনজাইম = কেবল উৎপাদ",
            "কো-এনজাইম = কেবল সেলুলোজ তন্তু; অ্যাপো-এনজাইম = কেবল স্টার্চ",
        ],
        "A", "hard", "conceptual",
        "Standard definition: apoenzyme + coenzyme/cofactor → holoenzyme.",
        "মানক সংজ্ঞা: অ্যাপো-এনজাইম + কো-এনজাইম/কো-ফ্যাক্টর → হলো-এনজাইম।",
    ),
]


# --- t03: Metabolism / বিপাক ---
T03 = [
    q(
        "In board-style photosynthesis items, the first carbohydrate commonly said to form in the chloroplast is:",
        "বোর্ড-ধাঁচের সালোকসংশ্লেষ প্রশ্নে ক্লোরোপ্লাস্টে প্রথম তৈরি শর্করা সাধারণত:",
        ["Starch", "Glucose", "Fructose", "Sucrose"],
        ["স্টার্চ", "গ্লুকোজ", "ফ্রুক্টোজ", "সুক্রোজ"],
        "B", "medium", "factual",
        "HSC/Udvash keys often list glucose as the first chloroplast sugar before later conversions.",
        "HSC/উদ্ভাস চাবিতে প্রায়শই গ্লুকোজকে প্রথম ক্লোরোপ্লাস্ট শর্করা হিসেবে ধরা হয়।",
    ),
    q(
        "After the first sugar forms, it may become fructose and sucrose. Their features: (i) one is reducing (ii) one is non-reducing (iii) part of the non-reducing sugar can later enter fat and protein pathways. Which is correct?",
        "প্রথম শর্করা পরিবর্তিত হয়ে ফ্রুক্টোজ ও সুক্রোজ হয়। বৈশিষ্ট্য: (i) একটি বিজারক (ii) একটি অবিজারক (iii) অবিজারকের অংশ পরে চর্বি ও আমিষ পথে যেতে পারে। কোনটি সঠিক?",
        [
            "i and ii only",
            "i and iii only",
            "ii and iii only",
            "i, ii and iii",
        ],
        [
            "কেবল i ও ii",
            "কেবল i ও iii",
            "কেবল ii ও iii",
            "i, ii ও iii",
        ],
        "D", "hard", "conceptual",
        "Fructose is reducing, sucrose non-reducing; sucrose carbons can feed lipid/amino-acid routes after cleavage.",
        "ফ্রুক্টোজ বিজারক, সুক্রোজ অবিজারক; সুক্রোজ ভেঙে কার্বন চর্বি/অ্যামাইনো এসিড পথে যেতে পারে।",
    ),
    q(
        "Erythrose-4-phosphate, common in plant metabolism, has the formula:",
        "উদ্ভিদ বিপাকে সাধারণ ইরিথ্রোজ-৪-ফসফেটের সূত্র:",
        ["C3H6O3", "C4H8O4", "C5H10O5", "C6H12O6"],
        ["C3H6O3", "C4H8O4", "C5H10O5", "C6H12O6"],
        "B", "medium", "factual",
        "Erythrose is a C4 sugar (C4H8O4 as free sugar; phosphate ester in the pathway).",
        "ইরিথ্রোজ C4 শর্করা (মুক্ত অবস্থায় C4H8O4; পথে ফসফেট এস্টার)।",
    ),
    q(
        "Correct stepwise hydrolysis products of dietary starch are typically:",
        "খাদ্য স্টার্চ বিশ্লেষণে ক্রমান্বয়ে যেসব পদার্থ পাওয়া যায়:",
        [
            "Starch → maltose → dextrin → glucose",
            "Starch → dextrin → maltose → glucose",
            "Starch → maltose → glucose → dextrin",
            "Starch → glucose → dextrin → maltose",
        ],
        [
            "স্টার্চ → মলটোজ → ডেক্সট্রিন → গ্লুকোজ",
            "স্টার্চ → ডেক্সট্রিন → মলটোজ → গ্লুকোজ",
            "স্টার্চ → মলটোজ → গ্লুকোজ → ডেক্সট্রিন",
            "স্টার্চ → গ্লুকোজ → ডেক্সট্রিন → মলটোজ",
        ],
        "B", "medium", "factual",
        "Amylase first yields dextrins, then maltose, then glucose via maltase.",
        "অ্যামাইলেজে প্রথমে ডেক্সট্রিন, পরে মলটোজ, অতঃপর মলটেজে গ্লুকোজ তৈরি হয়।",
    ),
    q(
        "Which polysaccharide mainly supplies energy for muscle work?",
        "পেশির কাজে শক্তি যোগান দেয় কোনটি?",
        ["Fructose", "Galactose", "Glycogen", "Maltose"],
        ["ফ্রুক্টোজ", "গ্যালাকটোজ", "গ্লাইকোজেন", "মলটোজ"],
        "C", "easy", "factual",
        "Muscle glycogen is mobilized to glucose-6-P/pyruvate for ATP during activity.",
        "পেশির গ্লাইকোজেন কার্যকালে গ্লুকোজ-৬-পি/পাইরুভেটে ভেঙে ATP দেয়।",
    ),
    q(
        "Which is a non-reducing sugar?",
        "কোনটি অবিজারক শর্করা?",
        ["Glucose", "Fructose", "Ribose", "Sucrose"],
        ["গ্লুকোজ", "ফ্রুক্টোজ", "রাইবোজ", "সুক্রোজ"],
        "D", "easy", "factual",
        "In sucrose both anomeric carbons are involved in the glycosidic bond.",
        "সুক্রোজে উভয় অ্যানোমেরিক কার্বন গ্লাইকোসাইডিক বন্ধনে আবদ্ধ।",
    ),
    q(
        "Bread is primarily which class of food?",
        "রুটি কোন জাতীয় খাদ্য?",
        ["Protein", "Lipid", "Vitamin", "Carbohydrate"],
        ["প্রোটিন", "লিপিড", "ভিটামিন", "শর্করা"],
        "D", "easy", "factual",
        "Bread is mainly starch carbohydrate from cereal flour.",
        "রুটি প্রধানত শস্য ময়দার স্টার্চ/শর্করা জাতীয় খাদ্য।",
    ),
    q(
        "Wax is a type of:",
        "মোম এক প্রকার:",
        ["Protein", "Lipid", "Carbohydrate", "Organic acid only"],
        ["প্রোটিন", "লিপিড", "শর্করা", "কেবল জৈব এসিড"],
        "B", "easy", "factual",
        "Waxes are esters of long-chain alcohols and fatty acids (lipid class).",
        "মোম দীর্ঘ শিকল অ্যালকোহল ও ফ্যাটি এসিডের এস্টার (লিপিড শ্রেণি)।",
    ),
    q(
        "Which of the following is commonly listed as a derived lipid?",
        "কোনটি সাধারণত উদ্ভূত লিপিড হিসেবে ধরা হয়?",
        ["Oil", "Fat", "Wax as simple glyceride only", "Rubber"],
        ["তেল", "চর্বি", "কেবল সরল গ্লিসারাইড হিসেবে মোম", "রাবার"],
        "D", "medium", "factual",
        "HSC classifications place rubber (and often steroids/terpenes/carotenoids) under derived lipids.",
        "HSC শ্রেণিতে রাবার (এবং প্রায়শই স্টেরয়েড/টারপিন/ক্যারোটিনয়েড) উদ্ভূত লিপিড।",
    ),
    q(
        "Correct statement about cholesterol metabolism/health:",
        "কোলেস্টেরল সম্পর্কিত সঠিক তথ্য কোনটি?",
        [
            "Low blood LDL is always harmful",
            "Women always have higher LDL than men as a rule of health",
            "High blood cholesterol can cause coronary atherosclerosis",
            "Cholesterol is a simple triglyceride oil",
        ],
        [
            "রক্তে LDL কম থাকা সবসময় ক্ষতিকর",
            "স্বাস্থ্যের নিয়ম হিসেবে নারীদের LDL সবসময় পুরুষের চেয়ে বেশি",
            "রক্তের উচ্চ কোলেস্টেরলে করোনারি অ্যাথেরোস্ক্লেরোসিস হতে পারে",
            "কোলেস্টেরল একটি সরল ট্রাইগ্লিসারাইড তেল",
        ],
        "C", "medium", "conceptual",
        "Elevated cholesterol promotes coronary artery disease; HDL is protective relative to LDL.",
        "উচ্চ কোলেস্টেরল করোনারি ধমনীরোগ বাড়ায়; HDL LDL-এর তুলনায় সুরক্ষাকারী।",
    ),
    q(
        "Having a higher amount of which blood lipid fraction is generally considered healthier?",
        "রক্তে কোনটির পরিমাণ বেশি থাকা সাধারণত ভালো?",
        ["LDL", "HDL", "Only free cholesterol without carriers", "Only LDL and HDL equally always"],
        [
            "LDL (নিম্ন ঘনত্বের লিপোপ্রোটিন)",
            "HDL (উচ্চ ঘনত্বের লিপোপ্রোটিন)",
            "বাহকহীন কেবল মুক্ত কোলেস্টেরল",
            "সবসময় কেবল LDL ও HDL সমান",
        ],
        "B", "easy", "factual",
        "HDL helps reverse cholesterol transport; high LDL is atherogenic.",
        "HDL কোলেস্টেরল অপসারণে সাহায্য করে; উচ্চ LDL অ্যাথেরোজেনিক।",
    ),
    q(
        "Cellulose about metabolism/use: (i) main structural component of plants (ii) builds the cell membrane (iii) non-reducing. Which is correct?",
        "সেলুলোজ সম্পর্কে: (i) উদ্ভিদের প্রধান গাঠনিক উপাদান (ii) কোষঝিল্লি গঠন করে (iii) বিজারণ ক্ষমতাবিহীন। কোনটি সঠিক?",
        [
            "i and ii only",
            "i and iii only",
            "ii and iii only",
            "i, ii and iii",
        ],
        [
            "কেবল i ও ii",
            "কেবল i ও iii",
            "কেবল ii ও iii",
            "i, ii ও iii",
        ],
        "B", "medium", "conceptual",
        "Cellulose builds walls, not membranes, and is non-reducing.",
        "সেলুলোজ প্রাচীর গঠন করে, ঝিল্লি নয়; এবং অবিজারক।",
    ),
    q(
        "Uses of cellulose: (i) paper industry (ii) furniture making (iii) primary human food nutrient. Which is correct?",
        "সেলুলোজ ব্যবহার: (i) কাগজ শিল্পে (ii) আসবাবপত্র তৈরিতে (iii) মানুষের প্রধান পুষ্টিখাদ্য হিসেবে। কোনটি সঠিক?",
        [
            "i and ii only",
            "i and iii only",
            "ii and iii only",
            "i, ii and iii",
        ],
        [
            "কেবল i ও ii",
            "কেবল i ও iii",
            "কেবল ii ও iii",
            "i, ii ও iii",
        ],
        "A", "medium", "application",
        "Cellulose is used industrially; humans cannot digest it as a primary nutrient.",
        "সেলুলোজ শিল্পে ব্যবহৃত; মানুষ একে প্রধান পুষ্টি হিসেবে হজম করতে পারে না।",
    ),
    q(
        "Anabolism is best described as:",
        "অ্যানাবলিজম বলতে বোঝায়:",
        [
            "Biosynthetic buildup of complex molecules using energy",
            "Only breakdown of glucose to CO2 with no ATP use ever",
            "Only random diffusion without enzymes",
            "Only excretion of urea without pathways",
        ],
        [
            "শক্তি ব্যবহার করে জটিল অণু গঠনের জৈব সংশ্লেষ",
            "কেবল ATP ছাড়াই গ্লুকোজকে CO2-এ ভাঙা",
            "এনজাইম ছাড়া কেবল এলোমেলো ডিফিউশন",
            "পথ ছাড়া কেবল ইউরিয়া নিষ্কাশন",
        ],
        "A", "easy", "conceptual",
        "Anabolism builds macromolecules; catabolism breaks them down for energy.",
        "অ্যানাবলিজম বৃহৎ অণু গঠন করে; ক্যাটাবলিজম শক্তির জন্য ভেঙে ফেলে।",
    ),
    q(
        "Catabolism is best described as:",
        "ক্যাটাবলিজম বলতে বোঝায়:",
        [
            "Degradative breakdown of molecules releasing usable energy",
            "Only DNA replication without enzymes",
            "Only peptide bond formation forever",
            "Only cellulose synthesis in animals",
        ],
        [
            "অণু ভাঙনের মাধ্যমে ব্যবহারযোগ্য শক্তি মুক্ত করা",
            "এনজাইম ছাড়া কেবল DNA অনুলিপন",
            "চিরদিন কেবল পেপটাইড বন্ধন গঠন",
            "প্রাণীদেহে কেবল সেলুলোজ সংশ্লেষ",
        ],
        "A", "easy", "conceptual",
        "Catabolic pathways (e.g. glycolysis, respiration) release energy from fuels.",
        "ক্যাটাবলিক পথ (যেমন গ্লাইকোলাইসিস, শ্বসন) জ্বালানি থেকে শক্তি মুক্ত করে।",
    ),
    q(
        "In glycolysis, glucose is ultimately converted toward:",
        "গ্লাইকোলাইসিসে গ্লুকোজ শেষ পর্যন্ত প্রধানত রূপান্তরিত হয়:",
        [
            "Pyruvate (then linked to acetyl-CoA under aerobic conditions)",
            "Only cellulose fibers in muscle",
            "Only cholesterol esters in the nucleus",
            "Only atmospheric N2 fixation",
        ],
        [
            "পাইরুভেট (বায়বীয় অবস্থায় অ্যাসিটাইল-CoA-এর সাথে যুক্ত)",
            "পেশিতে কেবল সেলুলোজ তন্তু",
            "নিউক্লিয়াসে কেবল কোলেস্টেরল এস্টার",
            "কেবল বায়ুমণ্ডলীয় N2 স্থিতিকরণ",
        ],
        "A", "medium", "factual",
        "Glycolysis yields pyruvate; aerobically pyruvate enters acetyl-CoA and the TCA cycle.",
        "গ্লাইকোলাইসিসে পাইরুভেট হয়; বায়বীয় অবস্থায় অ্যাসিটাইল-CoA ও TCA চক্রে যায়।",
    ),
    q(
        "ATP is the immediate energy currency because it:",
        "ATP তাৎক্ষণিক শক্তি মুদ্রা কারণ এটি:",
        [
            "Stores usable free energy in phosphoanhydride bonds for cellular work",
            "Is a storage polysaccharide like starch",
            "Is a structural protein of hair only",
            "Is a vitamin insoluble in all cells",
        ],
        [
            "ফসফোঅ্যানহাইড্রাইড বন্ধনে ব্যবহারযোগ্য মুক্ত শক্তি ধরে কোষীয় কাজে দেয়",
            "স্টার্চের মতো সঞ্চয়ী পলিস্যাকারাইড",
            "কেবল চুলের গাঠনিক প্রোটিন",
            "সব কোষে অদ্রবণীয় ভিটামিন",
        ],
        "A", "easy", "conceptual",
        "Hydrolysis/transfer of ATP phosphates powers endergonic metabolism.",
        "ATP-এর ফসফেট স্থানান্তর/হাইড্রোলাইসিস এন্ডারগনিক বিপাক চালায়।",
    ),
    q(
        "Which sugar contains a ketone (>C=O) group?",
        "কোনটিতে কিটোন (>C=O) গ্রুপ থাকে?",
        ["Fructose", "Ribose", "Glucose", "Erythrose"],
        ["ফ্রুক্টোজ", "রাইবোজ", "গ্লুকোজ", "ইরিথ্রোজ"],
        "A", "easy", "factual",
        "Fructose is a ketose; glucose, ribose and erythrose are aldoses.",
        "ফ্রুক্টোজ কিটোজ; গ্লুকোজ, রাইবোজ ও ইরিথ্রোজ অ্যালডোজ।",
    ),
    q(
        "Lipid traits relevant to metabolism: (i) soluble in water but insoluble in alcohol (ii) hydrolysis yields fatty acids and glycerol (iii) lighter than water. Which is correct?",
        "লিপিডের বৈশিষ্ট্য: (i) পানিতে দ্রবণীয় কিন্তু অ্যালকোহলে অদ্রবণীয় (ii) আর্দ্রবিশ্লেষণে ফ্যাটি এসিড ও গ্লিসারল উৎপন্ন হয় (iii) পানি অপেক্ষা হালকা। কোনটি সঠিক?",
        [
            "i and ii only",
            "ii and iii only",
            "i and iii only",
            "i, ii and iii",
        ],
        [
            "কেবল i ও ii",
            "কেবল ii ও iii",
            "কেবল i ও iii",
            "i, ii ও iii",
        ],
        "B", "medium", "conceptual",
        "Lipids are hydrophobic (alcohol/ether soluble), hydrolyze to fatty acids + glycerol, and float on water.",
        "লিপিড পানিবিদ্বেষী (অ্যালকোহল/ইথারে দ্রবণীয়), হাইড্রোলাইসিসে ফ্যাটি এসিড+গ্লিসারল দেয় এবং পানিতে ভেসে থাকে।",
    ),
    q(
        "Metabolism as a whole is:",
        "বিপাক সামগ্রিকভাবে হলো:",
        [
            "The sum of anabolic and catabolic enzyme-catalyzed pathways in the cell",
            "Only mitosis without chemistry",
            "Only passive diffusion of sand grains",
            "Only naming of organs without reactions",
        ],
        [
            "কোষের অ্যানাবলিক ও ক্যাটাবলিক এনজাইম-নির্ভর পথের সমষ্টি",
            "রসায়ন ছাড়া কেবল মাইটোসিস",
            "কেবল বালুকণার নিষ্ক্রিয় ডিফিউশন",
            "বিক্রিয়া ছাড়া কেবল অঙ্গের নামকরণ",
        ],
        "A", "easy", "conceptual",
        "Metabolism = ordered network of enzyme pathways balancing synthesis and breakdown.",
        "বিপাক = সংশ্লেষ ও ভাঙনের ভারসাম্য রক্ষাকারী এনজাইম পথের সুবিন্যস্ত জাল।",
    ),
]


TOPICS_MAP = {
    "bio1_27_ch03_t01": T01,
    "bio1_27_ch03_t02": T02,
    "bio1_27_ch03_t03": T03,
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
        "chapter": "bio1_27_ch03",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p109_pdf115.png",
            "p110_pdf116.png",
            "p111_pdf117.png",
            "p112_pdf118.png",
            "p113_pdf119.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio1_27_ch03_t01": {
                "title": "Biomolecules / জৈব অণু",
                "themes": [
                    "20 amino acids / protein building blocks",
                    "monosaccharides vs di/polysaccharides",
                    "protamine / glutelin / albumin / prolamin",
                    "lecithin phospholipid; terpenoids; carotenoids",
                    "cellulose structural role",
                    "cholesterol as lipid; C:H:O 1:2:1",
                    "glycosidic vs peptide bonds; hemoglobin conjugated",
                    "reducing vs non-reducing sugars",
                ],
            },
            "bio1_27_ch03_t02": {
                "title": "Enzymes / এনজাইম",
                "themes": [
                    "isomerase (G6P–F6P)",
                    "coenzyme vs cofactor vs apoenzyme / holoenzyme",
                    "colloidal nature; heat denaturation",
                    "lock-and-key (Emil Fischer)",
                    "lipase / cellulase / pectinase applications",
                    "activators (Zn) vs inhibitors",
                    "enzyme properties i/ii/iii stems",
                    "protein solubility classes tied to enzyme stems",
                ],
            },
            "bio1_27_ch03_t03": {
                "title": "Metabolism / বিপাক",
                "themes": [
                    "anabolism vs catabolism definition",
                    "chloroplast first sugar / fructose–sucrose fate",
                    "erythrose-4-P formula",
                    "starch → dextrin → maltose → glucose",
                    "glycogen muscle fuel; ATP currency",
                    "glycolysis → pyruvate / acetyl-CoA",
                    "cholesterol / HDL–LDL health",
                    "cellulose uses and non-nutrient status",
                    "lipid hydrolysis and density",
                ],
            },
        },
        "low_confidence": [
            "Diagram-linked bank items (sugar structures, ATP figure) rewritten as standalone bilingual stems.",
            "OCR noisy on several option glyphs; factual answers cross-checked against standard HSC keys.",
            "Metabolism topic underrepresented on printed pages relative to biomolecules/enzymes; authored accurate HSC-level items on chapter themes.",
            "Cataract-enzyme and some industrial-enzyme stems follow board/Udvash keys rather than clinical nuance.",
            "Photosynthesis 'first product = glucose' retained as board convention (biochemically G3P).",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio1_27_ch03_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio1_27_ch03_t01": 20,
                "bio1_27_ch03_t02": 20,
                "bio1_27_ch03_t03": 20,
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
        / "ch03_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
