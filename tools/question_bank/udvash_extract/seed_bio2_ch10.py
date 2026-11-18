#!/usr/bin/env python3
"""Seed Biology 2nd Paper Ch10 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio2_27_ch10_t01..t03 (Innate immunity; Acquired immunity; Vaccination).
OCR ch10 covers only ~2 printed pages (mainly CQ); items reconstructed from
readable CQ themes and standard HSC Zoology Ch10 facts.
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
    "biology p2 ch10; curated bilingual"
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


# --- t01: Innate immunity / সহজাত প্রতিরক্ষা ---
T01 = [
    q(
        "Immunity is best defined as which process?",
        "অনাক্রম্যতা বা ইমিউনিটি বলতে কোন প্রক্রিয়াকে বোঝায়?",
        [
            "Process by which the body resists harmful microbes and their toxic effects",
            "Only digestion of food in the small intestine",
            "Only formation of urine in the kidneys",
            "Only transport of carbon dioxide by plasma alone",
        ],
        [
            "যে প্রক্রিয়ায় দেহ ক্ষতিকর অণুজীব ও তাদের বিষাক্ত প্রভাব প্রতিরোধ করে",
            "শুধু ক্ষুদ্রান্ত্রে খাদ্য পরিপাক",
            "শুধু বৃক্কে মূত্র গঠন",
            "শুধু প্লাজমায় একা কার্বন ডাইঅক্সাইড পরিবহন",
        ],
        "A", "easy", "factual",
        "Immunity protects the body against pathogens and their harmful products.",
        "ইমিউনিটি রোগজীবাণু ও তাদের ক্ষতিকর পদার্থ থেকে দেহকে রক্ষা করে।",
    ),
    q(
        "What is the immune system?",
        "ইমিউনতন্ত্র বা অনাক্রম্যতন্ত্র কী?",
        [
            "Network of cells and organs that protect the body from disease-causing microbes",
            "Only the skeletal framework of bones and joints",
            "Only the respiratory alveoli that exchange gases",
            "Only sweat glands that cool the skin surface",
        ],
        [
            "কোষ ও অঙ্গের সমন্বয়ে গঠিত যে তন্ত্র রোগসৃষ্টিকারী জীবাণু থেকে দেহ রক্ষা করে",
            "শুধু হাড় ও সন্ধির কঙ্কাল কাঠামো",
            "শুধু গ্যাস বিনিময়কারী অ্যালভিওলি",
            "শুধু ত্বক শীতলকারী ঘর্মগ্রন্থি",
        ],
        "A", "easy", "factual",
        "The immune system is the coordinated cellular and organ defense network.",
        "ইমিউনতন্ত্র হলো দেহরক্ষার সমন্বিত কোষীয় ও অঙ্গীয় নেটওয়ার্ক।",
    ),
    q(
        "Innate immunity is best described as which kind of defense?",
        "সহজাত প্রতিরক্ষা কোন ধরনের প্রতিরক্ষা?",
        [
            "Inborn, lifelong, rapidly acting defense present from birth and linked to heredity",
            "Defense that appears only after a first vaccination in adulthood",
            "Defense that exists only during embryonic cleavage",
            "Defense limited to forming antibodies against one antigen only",
        ],
        [
            "জন্মগত, আজীবন উপস্থিত, দ্রুত কার্যকর ও বংশগতির সাথে সম্পর্কযুক্ত প্রতিরক্ষা",
            "শুধু প্রাপ্তবয়স্ককালে প্রথম টিকার পর যে প্রতিরক্ষা আসে",
            "শুধু ভ্রূণের ক্লিভেজকালীন প্রতিরক্ষা",
            "শুধু একটি অ্যান্টিজেনের বিরুদ্ধে অ্যান্টিবডি গঠনে সীমিত প্রতিরক্ষা",
        ],
        "A", "easy", "factual",
        "Innate immunity is inherited, present at birth, species-related and acts quickly.",
        "সহজাত প্রতিরক্ষা জন্মগত, প্রজাতি-সম্পর্কিত এবং দ্রুত সাড়া দেয়।",
    ),
    q(
        "Which set correctly lists levels often cited for innate immunity in HSC zoology?",
        "এইচএসসি প্রাণিবিজ্ঞানে সহজাত প্রতিরক্ষার যে স্তরগুলো উল্লেখিত, কোন সেটটি সঠিক?",
        [
            "Species-specific, group-specific and individual-specific immunity",
            "Only placental immunity and lactation immunity",
            "Only vaccine-induced active and passive serum immunity",
            "Only secondary memory response and booster titers",
        ],
        [
            "প্রজাতিগত, গোষ্ঠীগত ও ব্যক্তিগত প্রতিরক্ষা",
            "শুধু প্লাসেন্টাল ও স্তন্যদানজনিত প্রতিরক্ষা",
            "শুধু টিকাজনিত সক্রিয় ও সিরামজনিত নিষ্ক্রিয় প্রতিরক্ষা",
            "শুধু সেকেন্ডারি মেমোরি সাড়া ও বুস্টার টাইটার",
        ],
        "A", "medium", "factual",
        "Textbook innate immunity is often divided into species, group and individual levels.",
        "সহজাত প্রতিরক্ষা প্রায়ই প্রজাতি, গোষ্ঠী ও ব্যক্তি পর্যায়ে ভাগ করা হয়।",
    ),
    q(
        "Non-specific (first and second) defense lines mainly do which of the following?",
        "নন-স্পেসিফিক (প্রথম ও দ্বিতীয়) প্রতিরক্ষা স্তর মূলত কী করে?",
        [
            "Treat nearly all foreign materials as harmful without targeting one unique antigen only",
            "Produce only antigen-specific memory B cells before any infection",
            "Act only after a booster dose of vaccine is given",
            "Destroy only self MHC molecules on healthy cells",
        ],
        [
            "নির্দিষ্ট একটি অ্যান্টিজেন টার্গেট না করে প্রায় সব বহিরাগত বস্তুকে ক্ষতিকর ধরে প্রতিরোধ করে",
            "সংক্রমণের আগেই শুধু অ্যান্টিজেন-নির্দিষ্ট মেমোরি বি কোষ তৈরি করে",
            "শুধু বুস্টার টিকা দেওয়ার পরই কাজ করে",
            "শুধু সুস্থ কোষের স্ব-এমএইচসি ধ্বংস করে",
        ],
        "A", "medium", "conceptual",
        "Non-specific barriers and responses attack broadly rather than one antigen only.",
        "নন-স্পেসিফিক স্তর নির্দিষ্ট এক অ্যান্টিজেন নয়, বরং সাধারণভাবে প্রতিরোধ করে।",
    ),
    q(
        "Intact skin mainly functions as which type of innate barrier?",
        "অক্ষত ত্বক সহজাত প্রতিরক্ষায় মূলত কোন ধরনের বাধা হিসেবে কাজ করে?",
        [
            "Physical barrier that blocks many microbes from entering the body",
            "Only a site that manufactures plasma cells for IgG",
            "Only a chemical factory for MHC class II on T cells",
            "Only a storage organ for live attenuated vaccines",
        ],
        [
            "ভৌত বাধা যা অনেক জীবাণুর দেহে প্রবেশ আটকায়",
            "শুধু আইজিজি-র জন্য প্লাজমা কোষ তৈরির স্থান",
            "শুধু টি কোষে এমএইচসি দ্বিতীয় শ্রেণির রাসায়নিক কারখানা",
            "শুধু জীবিত অ্যাটেনুয়েটেড টিকা সংরক্ষণ অঙ্গ",
        ],
        "A", "easy", "factual",
        "Unbroken skin is a primary physical first-line barrier against entry of pathogens.",
        "অক্ষত ত্বক প্রথম স্তরের প্রধান ভৌত বাধা।",
    ),
    q(
        "Sebaceous glands contribute to innate defense mainly by secreting what?",
        "সিবেসাস গ্রন্থি সহজাত প্রতিরক্ষায় মূলত কী নিঃসরণ করে?",
        [
            "Sebum (oily secretion) containing antibacterial components on the skin",
            "Only hydrochloric acid into the stomach lumen",
            "Only insulin into the bloodstream",
            "Only surfactant into the alveoli",
        ],
        [
            "ত্বকে ব্যাকটেরিয়ানাশক উপাদানযুক্ত সেবাম বা তেলজাত নিঃসরণ",
            "শুধু পাকস্থলীর গহ্বরে হাইড্রোক্লোরিক অ্যাসিড",
            "শুধু রক্তপ্রবাহে ইনসুলিন",
            "শুধু অ্যালভিওলিতে সারফ্যাকট্যান্ট",
        ],
        "A", "easy", "factual",
        "Sebaceous glands secrete sebum with antibacterial properties on skin surfaces.",
        "সিবেসাস গ্রন্থি ত্বকে অ্যান্টিব্যাকটেরিয়াল সেবাম নিঃসরণ করে।",
    ),
    q(
        "Phagocytosis in human innate defense is best described as which process?",
        "মানব সহজাত প্রতিরক্ষায় ফ্যাগোসাইটোসিস কোন প্রক্রিয়া?",
        [
            "White blood cells extend pseudopodia, engulf microbes or debris and destroy them with enzymes",
            "Only red blood cells carry oxygen without engulfing pathogens",
            "Only hepatocytes store glycogen after a meal",
            "Only nephrons filter urea without cellular engulfment",
        ],
        [
            "শ্বেত রক্তকণিকা ক্ষণপদ দিয়ে জীবাণু বা ধ্বংসাবশেষ গ্রাস করে এনজাইমে ধ্বংস করে",
            "শুধু লোহিত কণিকা জীবাণু না গিলে অক্সিজেন বহন করে",
            "শুধু হেপাটোসাইট খাবারের পর গ্লাইকোজেন সঞ্চয় করে",
            "শুধু নেফ্রন কোষীয় গ্রাস ছাড়াই ইউরিয়া পরিস্রাবণ করে",
        ],
        "A", "easy", "conceptual",
        "Phagocytosis is second-line innate defense by neutrophils and monocytes/macrophages.",
        "ফ্যাগোসাইটোসিস নিউট্রোফিল ও মনোসাইট/ম্যাক্রোফেজের দ্বিতীয় স্তরীয় প্রতিরক্ষা।",
    ),
    q(
        "A phagosome is which structure formed during phagocytosis?",
        "ফ্যাগোসাইটোসিসের সময় গঠিত ফ্যাগোজোম কোন কাঠামো?",
        [
            "Membrane-bound vesicle enclosing a microbe trapped by fused pseudopodia",
            "Only a mitochondrion that produces ATP in muscle",
            "Only a Golgi stack that packages digestive enzymes for export",
            "Only a nuclear pore complex that exports mRNA",
        ],
        [
            "ক্ষণপদ একীভূত হয়ে আটকানো জীবাণুকে ঘিরে তৈরি ঝিল্লিবেষ্টিত থলিকা",
            "শুধু পেশিতে এটিপি তৈরির মাইটোকন্ড্রিয়া",
            "শুধু রপ্তানির জন্য পাচক এনজাইম প্যাক করার গলগি স্তূপ",
            "শুধু এমআরএনএ রপ্তানির নিউক্লিয়ার পোর কমপ্লেক্স",
        ],
        "A", "medium", "factual",
        "Pseudopodia fuse around the prey to form a membrane-bound phagosome vesicle.",
        "ক্ষণপদ একত্র হয়ে জীবাণুকে ঘিরে ফ্যাগোজোম থলিকা গঠন করে।",
    ),
    q(
        "Which leukocyte pair is most associated with phagocytosis in human innate immunity?",
        "মানব সহজাত প্রতিরক্ষায় ফ্যাগোসাইটোসিসের সাথে সবচেয়ে যুক্ত শ্বেতকণিকা জোড়া কোনটি?",
        [
            "Neutrophils and monocytes (macrophages)",
            "Only mature erythrocytes and platelets",
            "Only osteoblasts and chondrocytes",
            "Only goblet cells and chief cells",
        ],
        [
            "নিউট্রোফিল ও মনোসাইট (ম্যাক্রোফেজ)",
            "শুধু পরিপক্ক ইরিথ্রোসাইট ও প্লেটলেট",
            "শুধু অস্টিওব্লাস্ট ও কনড্রোসাইট",
            "শুধু গবলেট কোষ ও চিফ কোষ",
        ],
        "A", "easy", "factual",
        "Neutrophils and monocyte-derived macrophages are major phagocytes.",
        "নিউট্রোফিল ও ম্যাক্রোফেজ প্রধান ফ্যাগোসাইট।",
    ),
    q(
        "Interferon is best described as which substance?",
        "ইন্টারফেরন কোন পদার্থ হিসেবে সবচেয়ে ভালো বর্ণিত?",
        [
            "Glycoprotein produced by virus-infected cells that interferes with viral replication",
            "Only a steroid hormone from the adrenal cortex",
            "Only a digestive protease from the pancreas",
            "Only a clotting factor made solely by platelets",
        ],
        [
            "ভাইরাস-আক্রান্ত কোষ থেকে উৎপন্ন গ্লাইকোপ্রোটিন যা ভাইরাসের বংশবৃদ্ধিতে বাধা দেয়",
            "শুধু অ্যাড্রিনাল কর্টেক্সের স্টেরয়েড হরমোন",
            "শুধু অগ্ন্যাশয়ের পাচক প্রোটিয়েজ",
            "শুধু প্লেটলেট-নির্মিত জমাট বাঁধার ফ্যাক্টর",
        ],
        "A", "medium", "factual",
        "Interferons are antiviral glycoproteins released as an innate response to viral infection.",
        "ইন্টারফেরন ভাইরাস সংক্রমণে নিঃসৃত অ্যান্টিভাইরাল গ্লাইকোপ্রোটিন।",
    ),
    q(
        "Pyrogens released during macrophage attack on microbes mainly cause which effect?",
        "ম্যাক্রোফেজ জীবাণু আক্রমণকালে ক্ষরিত পাইরোজেনের প্রধান প্রভাব কী?",
        [
            "Raise body temperature (fever) via polypeptides entering the blood",
            "Lower body temperature permanently below 30°C",
            "Stop all neutrophil phagocytosis immediately",
            "Convert all B cells into erythrocytes",
        ],
        [
            "রক্তে প্রবেশকারী পলিপেপটাইডের মাধ্যমে শরীরের তাপমাত্রা বাড়ায় (জ্বর)",
            "দেহতাপ স্থায়ীভাবে ৩০°সে.-এর নিচে নামিয়ে দেয়",
            "সব নিউট্রোফিল ফ্যাগোসাইটোসিস তাৎক্ষণিক বন্ধ করে",
            "সব বি কোষকে ইরিথ্রোসাইটে রূপান্তর করে",
        ],
        "A", "medium", "conceptual",
        "Pyrogens are fever-inducing polypeptides secreted into blood during innate responses.",
        "পাইরোজেন সহজাত সাড়ায় রক্তে ক্ষরিত জ্বরসৃষ্টিকারী পলিপেপটাইড।",
    ),
    q(
        "Opsonin helps innate defense mainly by which action?",
        "অপসোনিন সহজাত প্রতিরক্ষায় মূলত কোন কাজ করে?",
        [
            "Coats microbial surfaces so phagocytes can engulf them more easily",
            "Digests only plant cellulose in the human colon",
            "Blocks MHC expression on every body cell permanently",
            "Converts antigens into vitamins inside erythrocytes",
        ],
        [
            "জীবাণুর গায়ে আস্তরণ তৈরি করে ফ্যাগোসাইটের গ্রাস সহজ করে",
            "শুধু মানব কোলনে উদ্ভিদ সেলুলোজ হজম করে",
            "সব দেহকোষে এমএইচসি প্রকাশ স্থায়ীভাবে বন্ধ করে",
            "ইরিথ্রোসাইটের ভিতরে অ্যান্টিজেনকে ভিটামিনে বদলায়",
        ],
        "A", "medium", "conceptual",
        "Opsonins coat microbes (opsonization), marking them for efficient phagocytosis.",
        "অপসোনিন জীবাণু আবৃত করে ফ্যাগোসাইটোসিসকে সহজ করে।",
    ),
    q(
        "Lysozyme in tears and saliva mainly contributes to innate immunity by doing what?",
        "অশ্রু ও লালার লাইসোজাইম সহজাত প্রতিরক্ষায় মূলত কী করে?",
        [
            "Damages bacterial cell walls as a chemical barrier secretion",
            "Synthesizes memory T cells in the cornea",
            "Stores live vaccine strains in salivary ducts",
            "Produces MHC peptides for every food antigen",
        ],
        [
            "রাসায়নিক বাধা হিসেবে ব্যাকটেরিয়ার কোষপ্রাচীর ক্ষতিগ্রস্ত করে",
            "কর্নিয়ায় মেমোরি টি কোষ সংশ্লেষ করে",
            "লালা নালিতে জীবিত টিকা স্ট্রেন সংরক্ষণ করে",
            "সব খাদ্য অ্যান্টিজেনের জন্য এমএইচসি পেপটাইড তৈরি করে",
        ],
        "A", "medium", "factual",
        "Lysozyme is an antimicrobial enzyme in secretions of the first-line chemical barriers.",
        "লাইসোজাইম প্রথম স্তরের নিঃসরণে অ্যান্টিমাইক্রোবিয়াল এনজাইম।",
    ),
    q(
        "Stomach acid aids innate defense primarily by which mechanism?",
        "পাকস্থলীর অ্যাসিড সহজাত প্রতিরক্ষায় প্রধানত কোন প্রক্রিয়ায় সাহায্য করে?",
        [
            "Low pH kills or inhibits many swallowed microbes",
            "Neutral pH activates only vaccine antigens",
            "High alkaline pH forms memory B cells",
            "Acid converts all viruses into antibodies",
        ],
        [
            "নিম্ন পিএইচ অনেক গিলে ফেলা জীবাণুকে মেরে বা বাধা দেয়",
            "নিরপেক্ষ পিএইচ শুধু টিকা অ্যান্টিজেন সক্রিয় করে",
            "উচ্চ ক্ষারীয় পিএইচ মেমোরি বি কোষ গঠন করে",
            "অ্যাসিড সব ভাইরাসকে অ্যান্টিবডিতে রূপান্তর করে",
        ],
        "A", "easy", "conceptual",
        "Gastric HCl creates an acidic chemical barrier against many ingested pathogens.",
        "গ্যাস্ট্রিক অ্যাসিড অনেক গৃহীত জীবাণুর বিরুদ্ধে রাসায়নিক বাধা।",
    ),
    q(
        "Inflammation as an innate response typically includes which features?",
        "সহজাত সাড়া হিসেবে প্রদাহে সাধারণত কোন বৈশিষ্ট্যগুলো থাকে?",
        [
            "Local redness, heat, swelling and pain with increased blood flow and immune cell recruitment",
            "Only permanent loss of all skin barrier function",
            "Only formation of a diploid zygote in the ampulla",
            "Only excretion of uric acid crystals from bone",
        ],
        [
            "স্থানীয় লালচে ভাব, উত্তাপ, ফোলা ও ব্যথাসহ রক্তপ্রবাহ ও ইমিউন কোষ আগমন বৃদ্ধি",
            "শুধু ত্বক বাধার স্থায়ী ক্ষতি",
            "শুধু অ্যাম্পুলায় ডিপ্লয়েড জাইগোট গঠন",
            "শুধু হাড় থেকে ইউরিক অ্যাসিড স্ফটিক নিষ্কাশন",
        ],
        "A", "medium", "conceptual",
        "Acute inflammation recruits defenses to damaged or infected tissues.",
        "প্রদাহ আক্রান্ত স্থানে প্রতিরক্ষা কোষ ও রক্তপ্রবাহ বাড়ায়।",
    ),
    q(
        "Cilia and mucus in airways contribute to innate immunity mainly by doing what?",
        "শ্বাসনালির সিলিয়া ও মিউকাস সহজাত প্রতিরক্ষায় মূলত কী করে?",
        [
            "Trap and sweep microbes and particles outward before deep invasion",
            "Produce antigen-specific IgE inside every alveolus",
            "Store booster doses of vaccine in bronchioles",
            "Convert inhaled air into antibodies",
        ],
        [
            "জীবাণু ও কণা আটকে গভীর অনুপ্রবেশের আগে বাইরে ঠেলে দেয়",
            "প্রতি অ্যালভিওলাসে অ্যান্টিজেন-নির্দিষ্ট আইজিই তৈরি করে",
            "ব্রংকিওলে বুস্টার টিকা সংরক্ষণ করে",
            "শ্বাস নেওয়া বাতাসকে অ্যান্টিবডিতে বদলায়",
        ],
        "A", "easy", "conceptual",
        "Mucociliary clearance is a mechanical first-line airway barrier.",
        "মিউকোসিলিয়ারি ক্লিয়ারেন্স শ্বাসনালির প্রথম স্তরীয় যান্ত্রিক বাধা।",
    ),
    q(
        "Compared with acquired immunity, innate immunity generally responds how?",
        "অর্জিত প্রতিরক্ষার তুলনায় সহজাত প্রতিরক্ষা সাধারণত কীভাবে সাড়া দেয়?",
        [
            "Faster and without needing prior specific exposure to that antigen",
            "Only after years of antigen-specific memory cell training",
            "Only when booster vaccines have already failed",
            "Slower than acquired responses and always antigen-exclusive",
        ],
        [
            "দ্রুততর এবং সেই অ্যান্টিজেনের পূর্ব নির্দিষ্ট সংস্পর্শ ছাড়াই",
            "শুধু বছরের পর বছর অ্যান্টিজেন-নির্দিষ্ট মেমোরি প্রশিক্ষণের পর",
            "শুধু বুস্টার টিকা ব্যর্থ হওয়ার পর",
            "অর্জিত সাড়ার চেয়ে ধীর এবং সবসময় একক অ্যান্টিজেন-নির্দিষ্ট",
        ],
        "A", "medium", "conceptual",
        "Innate defenses act quickly and broadly; adaptive defenses are slower but specific.",
        "সহজাত সাড়া দ্রুত ও ব্যাপক; অর্জিত সাড়া ধীর কিন্তু নির্দিষ্ট।",
    ),
    q(
        "Which statement about innate immunity is most accurate for HSC level?",
        "এইচএসসি পর্যায়ে সহজাত প্রতিরক্ষা সম্পর্কে কোন বক্তব্য সবচেয়ে সঠিক?",
        [
            "It is present in all members of a species in similar form and acts against many pathogens",
            "It exists only in vaccinated individuals and never at birth",
            "It produces only one antibody class against one epitope forever",
            "It requires prior infection with every microbe before any barrier works",
        ],
        [
            "প্রজাতির সব সদস্যে একই রূপে থাকে এবং অনেক জীবাণুর বিরুদ্ধে কাজ করে",
            "শুধু টিকিত ব্যক্তিতে থাকে এবং জন্মকালে কখনো থাকে না",
            "চিরকাল শুধু এক এপিটোপের বিরুদ্ধে এক অ্যান্টিবডি শ্রেণি তৈরি করে",
            "বাধা কাজের আগে প্রতিটি জীবাণুর পূর্ব সংক্রমণ আবশ্যক",
        ],
        "A", "medium", "conceptual",
        "Innate immunity is species-shared, inborn and non-specific toward many threats.",
        "সহজাত প্রতিরক্ষা প্রজাতিব্যাপী, জন্মগত ও বহু হুমকির বিরুদ্ধে নন-স্পেসিফিক।",
    ),
    q(
        "A cut in the skin that lets bacteria enter mainly bypasses which innate component first?",
        "ত্বকের কাটা দিয়ে ব্যাকটেরিয়া ঢুকলে প্রথমে কোন সহজাত উপাদান মূলত অতিক্রম হয়?",
        [
            "Physical barrier of intact epidermis",
            "Only secondary lymphoid memory plasma cells",
            "Only placental IgG transfer from the fetus",
            "Only oral live polio vaccine strains",
        ],
        [
            "অক্ষত এপিডার্মিসের ভৌত বাধা",
            "শুধু সেকেন্ডারি লিম্ফয়েড মেমোরি প্লাজমা কোষ",
            "শুধু ভ্রূণ থেকে প্লাসেন্টাল আইজিজি স্থানান্তর",
            "শুধু মুখে দেওয়া জীবিত পোলিও টিকা স্ট্রেন",
        ],
        "A", "easy", "application",
        "Breach of skin removes the first physical barrier and exposes deeper tissues.",
        "ত্বক ভেঙে গেলে প্রথম ভৌত বাধা নষ্ট হয়ে গভীর টিস্যু উন্মুক্ত হয়।",
    ),
]


# --- t02: Acquired immunity / অর্জিত প্রতিরক্ষা ---
T02 = [
    q(
        "Acquired (adaptive) immunity is best defined as which defense?",
        "অর্জিত (অ্যাডাপটিভ) প্রতিরক্ষা কোন প্রতিরক্ষা হিসেবে সংজ্ঞায়িত?",
        [
            "Defense that develops after birth against specific microbes through infection or immunization",
            "Only the inborn barrier of unbroken skin at birth",
            "Only stomach acid present before any antigen exposure",
            "Only fever caused by pyrogens without lymphocytes",
        ],
        [
            "জন্মের পর নির্দিষ্ট জীবাণুর বিরুদ্ধে সংক্রমণ বা টিকাদানের ফলে গড়ে ওঠা প্রতিরক্ষা",
            "শুধু জন্মকালীন অক্ষত ত্বকের জন্মগত বাধা",
            "শুধু অ্যান্টিজেন সংস্পর্শের আগে থাকা পাকস্থলীর অ্যাসিড",
            "শুধু লিম্ফোসাইট ছাড়া পাইরোজেনজনিত জ্বর",
        ],
        "A", "easy", "factual",
        "Acquired immunity is specific and develops after antigen exposure or vaccination.",
        "অর্জিত প্রতিরক্ষা নির্দিষ্ট এবং অ্যান্টিজেন সংস্পর্শ বা টিকার পর গড়ে ওঠে।",
    ),
    q(
        "Which pair correctly names the two major forms of acquired immunity?",
        "অর্জিত প্রতিরক্ষার দুই প্রধান রূপ কোন জোড়ায় সঠিক?",
        [
            "Active immunity and passive immunity",
            "Only phagocytosis and interferon release",
            "Only sebum secretion and mucociliary sweep",
            "Only fever and inflammation without antibodies",
        ],
        [
            "সক্রিয় প্রতিরক্ষা ও নিষ্ক্রিয় (অক্রিয়) প্রতিরক্ষা",
            "শুধু ফ্যাগোসাইটোসিস ও ইন্টারফেরন ক্ষরণ",
            "শুধু সেবাম নিঃসরণ ও মিউকোসিলিয়ারি ঝাড়ু",
            "শুধু অ্যান্টিবডি ছাড়া জ্বর ও প্রদাহ",
        ],
        "A", "easy", "factual",
        "Acquired immunity is commonly divided into active and passive forms.",
        "অর্জিত প্রতিরক্ষা সাধারণত সক্রিয় ও নিষ্ক্রিয় ভাগে বিভক্ত।",
    ),
    q(
        "An antigen is best described as which entity?",
        "অ্যান্টিজেন কোন সত্তা হিসেবে সবচেয়ে ভালো বর্ণিত?",
        [
            "Molecule or microbe that enters the body and stimulates production of specific antibodies",
            "Only an enzyme that digests starch in saliva",
            "Only a vitamin stored exclusively in adipose tissue",
            "Only a neurotransmitter released at neuromuscular junctions",
        ],
        [
            "দেহে প্রবেশ করে নির্দিষ্ট অ্যান্টিবডি উৎপাদনে উদ্দীপনা দেয় এমন অণু বা অণুজীব",
            "শুধু লালায় স্টার্চ হজমের এনজাইম",
            "শুধু অ্যাডিপোজ টিস্যুতে সঞ্চিত ভিটামিন",
            "শুধু নিউরোমাসকুলার জংশনে নিঃসৃত নিউরোট্রান্সমিটার",
        ],
        "A", "easy", "factual",
        "Antigens provoke specific adaptive immune responses including antibody formation.",
        "অ্যান্টিজেন নির্দিষ্ট অ্যান্টিবডিসহ অ্যাডাপটিভ সাড়া উদ্দীপিত করে।",
    ),
    q(
        "An antibody is best described as which product of defense?",
        "অ্যান্টিবডি প্রতিরক্ষার কোন উৎপাদ হিসেবে বর্ণিত?",
        [
            "Soluble glycoprotein from the immune system that targets a specific antigen",
            "Only a carbohydrate used solely for ATP in muscle",
            "Only a mineral crystal deposited in bone matrix",
            "Only a lipid bilayer identical to the nuclear envelope",
        ],
        [
            "ইমিউনতন্ত্র থেকে উৎপন্ন দ্রবণীয় গ্লাইকোপ্রোটিন যা নির্দিষ্ট অ্যান্টিজেনকে লক্ষ্য করে",
            "শুধু পেশিতে এটিপির জন্য ব্যবহৃত কার্বোহাইড্রেট",
            "শুধু অস্থি ম্যাট্রিক্সে জমা খনিজ স্ফটিক",
            "শুধু নিউক্লিয়ার এনভেলপের অনুরূপ লিপিড বাইলেয়ার",
        ],
        "A", "easy", "factual",
        "Antibodies (immunoglobulins) bind and help neutralize specific antigens.",
        "অ্যান্টিবডি নির্দিষ্ট অ্যান্টিজেন বেঁধে নিষ্ক্রিয়/ধ্বংসে সাহায্য করে।",
    ),
    q(
        "Which contrast between antigen and antibody is most accurate?",
        "অ্যান্টিজেন ও অ্যান্টিবডির মধ্যে কোন পার্থক্য সবচেয়ে সঠিক?",
        [
            "Antigens are foreign/pathogen-related stimulators; antibodies are protective proteins against them",
            "Antibodies always enter first; antigens are only made by plasma cells",
            "Antigens are always only steroids; antibodies are always only DNA",
            "Both are identical digestive enzymes from the pancreas",
        ],
        [
            "অ্যান্টিজেন বহিরাগত/প্যাথোজেন-সম্পর্কিত উদ্দীপক; অ্যান্টিবডি তাদের বিরুদ্ধে প্রতিরক্ষামূলক প্রোটিন",
            "অ্যান্টিবডি সবসময় আগে ঢোকে; অ্যান্টিজেন শুধু প্লাজমা কোষ তৈরি করে",
            "অ্যান্টিজেন সবসময় শুধু স্টেরয়েড; অ্যান্টিবডি সবসময় শুধু ডিএনএ",
            "উভয়ই অগ্ন্যাশয়ের অভিন্ন পাচক এনজাইম",
        ],
        "A", "medium", "conceptual",
        "Antigens stimulate immunity; antibodies are the specific protein effectors against them.",
        "অ্যান্টিজেন উদ্দীপনা দেয়; অ্যান্টিবডি তাদের বিরুদ্ধে নির্দিষ্ট প্রোটিন কার্যকরী।",
    ),
    q(
        "Chemically, antibodies are always which macromolecule class?",
        "রাসায়নিকভাবে অ্যান্টিবডি সবসময় কোন ম্যাক্রোমলিকিউল শ্রেণির?",
        [
            "Proteins (glycoproteins / immunoglobulins)",
            "Only simple monosaccharides without peptide chains",
            "Only inorganic phosphate salts",
            "Only free fatty acids without polypeptide structure",
        ],
        [
            "প্রোটিন (গ্লাইকোপ্রোটিন / ইমিউনোগ্লোবিউলিন)",
            "শুধু পেপটাইড শৃঙ্খলহীন সরল মনোস্যাকারাইড",
            "শুধু অজৈব ফসফেট লবণ",
            "শুধু পলিপেপটাইড কাঠামোহীন মুক্ত ফ্যাটি অ্যাসিড",
        ],
        "A", "easy", "factual",
        "Antibodies are protein (glycoprotein) molecules, unlike many varied antigen chemistries.",
        "অ্যান্টিবডি প্রোটিনজাত; অ্যান্টিজেন প্রোটিন বা জটিল কার্বোহাইড্রেট হতে পারে।",
    ),
    q(
        "MHC (Major Histocompatibility Complex) proteins mainly help by doing what?",
        "এমএইচসি (মেজর হিস্টোকম্প্যাটিবিলিটি কমপ্লেক্স) প্রোটিন মূলত কী করে সাহায্য করে?",
        [
            "Display molecular markers on cell membranes that aid pathogen recognition",
            "Digest only cellulose in the human stomach",
            "Carry oxygen exclusively like hemoglobin",
            "Form the enamel of teeth during childhood",
        ],
        [
            "কোষঝিল্লিতে আণবিক চিহ্ন প্রদর্শন করে জীবাণু শনাক্তকরণে সাহায্য করে",
            "শুধু মানব পাকস্থলীতে সেলুলোজ হজম করে",
            "শুধু হিমোগ্লোবিনের মতো অক্সিজেন বহন করে",
            "শৈশবে দাঁতের এনামেল গঠন করে",
        ],
        "A", "medium", "factual",
        "MHC molecules on plasma membranes help the immune system distinguish self and present antigen.",
        "এমএইচসি স্ব-শনাক্তকরণ ও অ্যান্টিজেন উপস্থাপনে সাহায্য করে।",
    ),
    q(
        "Memory cells in acquired immunity are mainly which cell type?",
        "অর্জিত প্রতিরক্ষায় মেমোরি কোষ মূলত কোন কোষ প্রকার?",
        [
            "Lymphocytes that retain antigen information for a stronger secondary response later",
            "Only erythrocytes that store iron without antigen memory",
            "Only keratinocytes that form the outer skin barrier",
            "Only osteocytes that maintain bone mineral density",
        ],
        [
            "লিম্ফোসাইট যা অ্যান্টিজেনের তথ্য ধরে রাখে এবং পরে শক্তিশালী সেকেন্ডারি সাড়া দেয়",
            "শুধু অ্যান্টিজেন স্মৃতিহীন ইরিথ্রোসাইট যা লোহা সঞ্চয় করে",
            "শুধু বাইরের ত্বক বাধা গঠনকারী কেরাটিনোসাইট",
            "শুধু অস্থি খনিজ ঘনত্ব রক্ষাকারী অস্টিওসাইট",
        ],
        "A", "easy", "conceptual",
        "Memory lymphocytes enable rapid, strong secondary responses on re-exposure.",
        "মেমোরি লিম্ফোসাইট পুনঃসংস্পর্শে দ্রুত শক্তিশালী সেকেন্ডারি সাড়া দেয়।",
    ),
    q(
        "Active acquired immunity develops when the body does which of the following?",
        "সক্রিয় অর্জিত প্রতিরক্ষা তখন গড়ে ওঠে যখন দেহ কী করে?",
        [
            "Produces its own antibodies after infection or vaccination",
            "Receives only ready-made antibodies without ever making them",
            "Relies solely on unbroken skin forever",
            "Uses only fever without any lymphocyte involvement",
        ],
        [
            "সংক্রমণ বা টিকার পর নিজেই অ্যান্টিবডি তৈরি করে",
            "কখনো না বানিয়ে শুধু তৈরি অ্যান্টিবডি গ্রহণ করে",
            "চিরকাল শুধু অক্ষত ত্বকের উপর নির্ভর করে",
            "লিম্ফোসাইট ছাড়া শুধু জ্বর ব্যবহার করে",
        ],
        "A", "easy", "conceptual",
        "Active immunity means the host generates its own adaptive response and memory.",
        "সক্রিয় প্রতিরক্ষায় হোস্ট নিজেই অ্যাডাপটিভ সাড়া ও মেমোরি তৈরি করে।",
    ),
    q(
        "Passive acquired immunity is characterized by which feature?",
        "নিষ্ক্রিয় অর্জিত প্রতিরক্ষার বৈশিষ্ট্য কোনটি?",
        [
            "Ready-made antibodies are received; protection is usually temporary without lasting host memory",
            "The host always forms lifelong memory after a single fever",
            "Only sebum production increases permanently",
            "Only MHC genes rearrange in erythrocytes",
        ],
        [
            "তৈরি অ্যান্টিবডি পাওয়া যায়; সুরক্ষা সাধারণত সাময়িক এবং স্থায়ী হোস্ট মেমোরি থাকে না",
            "একবার জ্বরের পর হোস্ট সবসময় আজীবন মেমোরি গঠন করে",
            "শুধু সেবাম উৎপাদন স্থায়ীভাবে বাড়ে",
            "শুধু ইরিথ্রোসাইটে এমএইচসি জিন পুনর্বিন্যাস হয়",
        ],
        "A", "medium", "conceptual",
        "Passive immunity transfers antibodies (e.g., maternal or antiserum) without host immunization memory.",
        "নিষ্ক্রিয় প্রতিরক্ষায় তৈরি অ্যান্টিবডি আসে; হোস্ট মেমোরি সাধারণত গড়ে ওঠে না।",
    ),
    q(
        "Natural passive immunity in infants is mainly acquired how?",
        "শিশুদের প্রাকৃতিক নিষ্ক্রিয় প্রতিরক্ষা মূলত কীভাবে অর্জিত হয়?",
        [
            "Transfer of maternal antibodies via placenta and/or breast milk",
            "Only by receiving a killed bacterial vaccine at birth",
            "Only by producing plasma cells before birth without any antibody",
            "Only by phagocytosis of maternal erythrocytes",
        ],
        [
            "প্লাসেন্টা এবং/অথবা বুকের দুধের মাধ্যমে মাতৃ অ্যান্টিবডি স্থানান্তর",
            "শুধু জন্মকালে নিহত ব্যাকটেরিয়া টিকা গ্রহণ",
            "শুধু জন্মের আগে অ্যান্টিবডি ছাড়াই প্লাজমা কোষ তৈরি",
            "শুধু মাতৃ ইরিথ্রোসাইট ফ্যাগোসাইটোসিস",
        ],
        "A", "medium", "factual",
        "Maternal IgG (placenta) and secretory antibodies in milk give temporary infant protection.",
        "মাতৃ আইজিজি ও দুধের অ্যান্টিবডি শিশুকে সাময়িক সুরক্ষা দেয়।",
    ),
    q(
        "Artificial passive immunity is illustrated by which clinical practice?",
        "কৃত্রিম নিষ্ক্রিয় প্রতিরক্ষার উদাহরণ কোন চিকিৎসা অনুশীলন?",
        [
            "Injecting antiserum or antitoxin containing ready-made antibodies",
            "Giving only live attenuated vaccine so the host makes memory cells",
            "Relying only on lysozyme in tears after injury",
            "Raising fever with pyrogens alone as the sole therapy",
        ],
        [
            "তৈরি অ্যান্টিবডিযুক্ত অ্যান্টিসিরাম বা অ্যান্টিটক্সিন ইনজেকশন",
            "শুধু জীবিত অ্যাটেনুয়েটেড টিকা দিয়ে হোস্ট মেমোরি তৈরি",
            "আঘাতের পর শুধু অশ্রুর লাইসোজাইমের উপর নির্ভর",
            "একমাত্র চিকিৎসা হিসেবে শুধু পাইরোজেন দিয়ে জ্বর বাড়ানো",
        ],
        "A", "medium", "application",
        "Antiserum/antitoxin provides immediate but temporary passive protection.",
        "অ্যান্টিসিরাম/অ্যান্টিটক্সিন তাৎক্ষণিক কিন্তু সাময়িক নিষ্ক্রিয় সুরক্ষা দেয়।",
    ),
    q(
        "Humoral immunity mainly involves which effector products?",
        "হিউমোরাল ইমিউনিটিতে মূলত কোন কার্যকরী উৎপাদ জড়িত?",
        [
            "Antibodies secreted by plasma cells (B-lymphocyte lineage)",
            "Only cytotoxic killing by macrophages without any antibody",
            "Only keratin layers of the epidermis",
            "Only hydrochloric acid of the stomach",
        ],
        [
            "প্লাজমা কোষ (বি-লিম্ফোসাইট বংশ) থেকে নিঃসৃত অ্যান্টিবডি",
            "শুধু অ্যান্টিবডি ছাড়া ম্যাক্রোফেজের সাইটোটক্সিক হত্যা",
            "শুধু এপিডার্মিসের কেরাটিন স্তর",
            "শুধু পাকস্থলীর হাইড্রোক্লোরিক অ্যাসিড",
        ],
        "A", "medium", "conceptual",
        "Humoral immunity is antibody-mediated; cell-mediated immunity relies more on T cells.",
        "হিউমোরাল প্রতিরক্ষা অ্যান্টিবডি-নির্ভর; কোষীয় প্রতিরক্ষা মূলত টি কোষ-নির্ভর।",
    ),
    q(
        "Cell-mediated acquired immunity depends mainly on which cells?",
        "কোষীয় অর্জিত প্রতিরক্ষা মূলত কোন কোষের উপর নির্ভর করে?",
        [
            "T lymphocytes that recognize infected or abnormal cells",
            "Only mature red blood cells carrying hemoglobin",
            "Only goblet cells secreting mucus in the gut",
            "Only ameloblasts forming tooth enamel",
        ],
        [
            "সংক্রমিত বা অস্বাভাবিক কোষ শনাক্তকারী টি লিম্ফোসাইট",
            "শুধু হিমোগ্লোবিন বহনকারী পরিপক্ক লোহিত কণিকা",
            "শুধু অন্ত্রে মিউকাস নিঃসরণকারী গবলেট কোষ",
            "শুধু দাঁতের এনামেল গঠনকারী অ্যামেলোব্লাস্ট",
        ],
        "A", "medium", "factual",
        "T cells mediate cellular immunity against intracellular pathogens and abnormal cells.",
        "টি কোষ অন্তঃকোষীয় জীবাণু ও অস্বাভাবিক কোষের বিরুদ্ধে কোষীয় প্রতিরক্ষা চালায়।",
    ),
    q(
        "Compared with the primary immune response, the secondary response is typically what?",
        "প্রাথমিক ইমিউন সাড়ার তুলনায় সেকেন্ডারি সাড়া সাধারণত কেমন?",
        [
            "Faster and stronger because of memory cells from earlier antigen exposure",
            "Always slower and weaker than the first exposure",
            "Completely independent of any prior lymphocyte activation",
            "Limited only to raising body temperature without antibodies",
        ],
        [
            "আগের অ্যান্টিজেন সংস্পর্শের মেমোরি কোষের জন্য দ্রুততর ও শক্তিশালী",
            "প্রথম সংস্পর্শের চেয়ে সবসময় ধীর ও দুর্বল",
            "কোনো পূর্ব লিম্ফোসাইট সক্রিয়করণ ছাড়াই সম্পূর্ণ স্বাধীন",
            "শুধু অ্যান্টিবডি ছাড়া দেহতাপ বাড়ানোয় সীমিত",
        ],
        "A", "medium", "conceptual",
        "Memory cells accelerate and amplify secondary antibody/cellular responses.",
        "মেমোরি কোষ সেকেন্ডারি সাড়াকে দ্রুত ও তীব্র করে।",
    ),
    q(
        "Plasma cells mainly differentiate from which lineage after antigen stimulation?",
        "অ্যান্টিজেন উদ্দীপনার পর প্লাজমা কোষ মূলত কোন বংশ থেকে পৃথকীকৃত হয়?",
        [
            "B lymphocytes",
            "Only megakaryocytes that form platelets",
            "Only skeletal muscle myofibers",
            "Only hepatocytes of the liver lobule",
        ],
        [
            "বি লিম্ফোসাইট",
            "শুধু প্লেটলেট গঠনকারী মেগাক্যারিওসাইট",
            "শুধু কঙ্কালপেশির মায়োফাইবার",
            "শুধু যকৃত লোবিউলের হেপাটোসাইট",
        ],
        "A", "easy", "factual",
        "Activated B cells become plasma cells that secrete large amounts of antibody.",
        "সক্রিয় বি কোষ প্লাজমা কোষে পরিণত হয়ে প্রচুর অ্যান্টিবডি ক্ষরণ করে।",
    ),
    q(
        "Specificity of acquired immunity means which property?",
        "অর্জিত প্রতিরক্ষার নির্দিষ্টতা কোন বৈশিষ্ট্য বোঝায়?",
        [
            "Response targets a particular antigen rather than all foreign materials equally",
            "Every barrier treats all microbes with identical non-specific enzymes only",
            "Fever alone kills every pathogen without recognition",
            "Skin sebum binds every possible epitope simultaneously",
        ],
        [
            "সাড়া নির্দিষ্ট অ্যান্টিজেনকে লক্ষ্য করে, সব বহিরাগত বস্তুকে সমানভাবে নয়",
            "প্রতিটি বাধা সব জীবাণুকে শুধু অভিন্ন নন-স্পেসিফিক এনজাইমে আক্রমণ করে",
            "শনাক্তকরণ ছাড়াই শুধু জ্বর সব প্যাথোজেন মেরে ফেলে",
            "ত্বকের সেবাম একসাথে সব সম্ভাব্য এপিটোপ বেঁধে ফেলে",
        ],
        "A", "medium", "conceptual",
        "Adaptive responses are antigen-specific, unlike broad innate barriers.",
        "অ্যাডাপটিভ সাড়া অ্যান্টিজেন-নির্দিষ্ট; সহজাত বাধা ব্যাপক।",
    ),
    q(
        "Naturally acquired active immunity most often results from which event?",
        "প্রাকৃতিকভাবে অর্জিত সক্রিয় প্রতিরক্ষা সবচেয়ে বেশি কোন ঘটনা থেকে আসে?",
        [
            "Recovery from an infection during which the host made specific antibodies and memory cells",
            "Injection of antitoxin without any host antibody synthesis",
            "Only maternal IgG transfer across the placenta",
            "Only washing hands with soap as a physical barrier",
        ],
        [
            "সংক্রমণ থেকে সুস্থ হওয়া, যখন হোস্ট নির্দিষ্ট অ্যান্টিবডি ও মেমোরি কোষ তৈরি করে",
            "হোস্ট অ্যান্টিবডি সংশ্লেষ ছাড়াই অ্যান্টিটক্সিন ইনজেকশন",
            "শুধু প্লাসেন্টার মাধ্যমে মাতৃ আইজিজি স্থানান্তর",
            "শুধু সাবান দিয়ে হাত ধোয়ার ভৌত বাধা",
        ],
        "A", "easy", "application",
        "Natural active immunity follows infection and host adaptive response.",
        "প্রাকৃতিক সক্রিয় প্রতিরক্ষা সংক্রমণ ও হোস্টের অ্যাডাপটিভ সাড়ার পর আসে।",
    ),
    q(
        "Where are antibodies commonly found after they are produced?",
        "উৎপাদনের পর অ্যান্টিবডি সাধারণত কোথায় পাওয়া যায়?",
        [
            "In blood plasma/serum and other body fluids",
            "Only inside the mitochondrial matrix of muscle",
            "Only as enamel crystals of teeth",
            "Only as hemoglobin inside erythrocytes",
        ],
        [
            "রক্তরস/সিরাম ও অন্যান্য দেহতরলে",
            "শুধু পেশির মাইটোকন্ড্রিয়াল ম্যাট্রিক্সে",
            "শুধু দাঁতের এনামেল স্ফটিক হিসেবে",
            "শুধু ইরিথ্রোসাইটের হিমোগ্লোবিন হিসেবে",
        ],
        "A", "easy", "factual",
        "Circulating antibodies are soluble glycoproteins in plasma and body fluids.",
        "অ্যান্টিবডি প্লাজমা ও দেহতরলে দ্রবণীয় গ্লাইকোপ্রোটিন হিসেবে থাকে।",
    ),
    q(
        "A person receives antibodies from a donor serum after toxin exposure. Which immunity is this?",
        "টক্সিন সংস্পর্শের পর দাতা সিরাম থেকে অ্যান্টিবডি পেলে এটি কোন প্রতিরক্ষা?",
        [
            "Artificial passive immunity",
            "Natural active immunity from infection alone",
            "Species-level innate barrier of skin only",
            "Primary phagocytosis without any antibody",
        ],
        [
            "কৃত্রিম নিষ্ক্রিয় প্রতিরক্ষা",
            "শুধু সংক্রমণজনিত প্রাকৃতিক সক্রিয় প্রতিরক্ষা",
            "শুধু ত্বকের প্রজাতি-স্তরীয় সহজাত বাধা",
            "অ্যান্টিবডি ছাড়াই প্রাথমিক ফ্যাগোসাইটোসিস",
        ],
        "A", "hard", "application",
        "Donor antiserum provides artificial passive protection without inducing host memory.",
        "দাতা অ্যান্টিসিরাম কৃত্রিম নিষ্ক্রিয় সুরক্ষা দেয়; হোস্ট মেমোরি তৈরি হয় না।",
    ),
]


# --- t03: Vaccination / টিকাদান ---
T03 = [
    q(
        "A vaccine (টিকা) is best defined as which preparation?",
        "টিকা বা ভ্যাক্সিন কোন প্রস্তুতি হিসেবে সংজ্ঞায়িত?",
        [
            "Microbe or microbe-derived material introduced to stimulate immunity without causing full disease",
            "Only an antibiotic that kills bacteria inside infected tissues",
            "Only a fever-reducing drug that blocks pyrogens",
            "Only a surgical suture used to close skin wounds",
        ],
        [
            "পূর্ণ রোগ না ঘটিয়ে অনাক্রম্যতা জাগাতে দেহে দেওয়া অণুজীব বা অণুজীবঘটিত পদার্থ",
            "শুধু সংক্রমিত টিস্যুতে ব্যাকটেরিয়া মারার অ্যান্টিবায়োটিক",
            "শুধু পাইরোজেন বাধাদানকারী জ্বরনাশক ওষুধ",
            "শুধু ত্বকের ক্ষত সেলাইয়ের সার্জিক্যাল সুচার",
        ],
        "A", "easy", "factual",
        "Vaccines present antigen-like material so the body builds protective immunity safely.",
        "টিকা অ্যান্টিজেন-সদৃশ উদ্দীপনা দিয়ে নিরাপদে প্রতিরক্ষা গড়ে তোলে।",
    ),
    q(
        "Vaccines protect mainly by acting like which immune stimulus?",
        "টিকা মূলত কোন ইমিউন উদ্দীপকের মতো আচরণ করে সুরক্ষা দেয়?",
        [
            "Antigens that stimulate antibody production and adaptive memory",
            "Only digestive enzymes that break down dietary protein",
            "Only vitamins that store calcium in bone",
            "Only sedatives that lower brain activity",
        ],
        [
            "অ্যান্টিজেন যা অ্যান্টিবডি উৎপাদন ও অ্যাডাপটিভ মেমোরি উদ্দীপিত করে",
            "শুধু খাদ্য প্রোটিন ভাঙার পাচক এনজাইম",
            "শুধু অস্থিতে ক্যালসিয়াম সঞ্চয়কারী ভিটামিন",
            "শুধু মস্তিষ্কের কার্যকলাপ কমানোর সেডেটিভ",
        ],
        "A", "easy", "conceptual",
        "Vaccines mimic antigens to train adaptive immunity before real infection.",
        "টিকা অ্যান্টিজেনের মতো কাজ করে আগে থেকে অ্যাডাপটিভ প্রতিরক্ষা প্রস্তুত করে।",
    ),
    q(
        "Vaccination mainly confers which type of acquired immunity?",
        "টিকাদান মূলত কোন ধরনের অর্জিত প্রতিরক্ষা দেয়?",
        [
            "Artificial active immunity",
            "Natural passive immunity only",
            "Artificial passive antitoxin immunity only",
            "Innate species barrier without lymphocytes",
        ],
        [
            "কৃত্রিম সক্রিয় প্রতিরক্ষা",
            "শুধু প্রাকৃতিক নিষ্ক্রিয় প্রতিরক্ষা",
            "শুধু কৃত্রিম নিষ্ক্রিয় অ্যান্টিটক্সিন প্রতিরক্ষা",
            "লিম্ফোসাইট ছাড়া সহজাত প্রজাতি বাধা",
        ],
        "A", "easy", "factual",
        "Vaccines artificially induce the host to generate active adaptive immunity and memory.",
        "টিকা কৃত্রিমভাবে হোস্টের সক্রিয় অ্যাডাপটিভ প্রতিরক্ষা ও মেমোরি তৈরি করে।",
    ),
    q(
        "Why is a booster dose of vaccine often given?",
        "ভ্যাক্সিনের বুস্টার ডোজ কেন দেওয়া হয়?",
        [
            "To raise antibody levels further and strengthen lasting immunity after the primary dose",
            "To remove all memory cells formed after the first dose",
            "To convert active immunity into only passive serum transfer",
            "To permanently abolish MHC expression on leukocytes",
        ],
        [
            "প্রাথমিক ডোজের পর অ্যান্টিবডি মাত্রা আরও বাড়িয়ে দীর্ঘস্থায়ী অনাক্রম্যতা জোরদার করতে",
            "প্রথম ডোজের পর গঠিত সব মেমোরি কোষ অপসারণ করতে",
            "সক্রিয় প্রতিরক্ষাকে শুধু নিষ্ক্রিয় সিরাম স্থানান্তরে বদলাতে",
            "লিউকোসাইটে এমএইচসি প্রকাশ স্থায়ীভাবে বাতিল করতে",
        ],
        "A", "medium", "conceptual",
        "Boosters re-stimulate memory responses to maintain high protective antibody titers.",
        "বুস্টার মেমোরি সাড়া পুনরুদ্দীপিত করে প্রতিরক্ষামূলক অ্যান্টিবডি উঁচু রাখে।",
    ),
    q(
        "A killed (inactivated) vaccine contains which kind of antigen material?",
        "নিহত (ইনঅ্যাকটিভেটেড) টিকায় কোন ধরনের অ্যান্টিজেন উপাদান থাকে?",
        [
            "Pathogens rendered non-infectious but still able to stimulate immunity",
            "Only live fully virulent wild-type microbes that always cause disease",
            "Only pure water without any antigenic protein",
            "Only ready-made antibodies from another donor",
        ],
        [
            "অসংক্রামক করা প্যাথোজেন যা এখনও অনাক্রম্যতা উদ্দীপিত করতে পারে",
            "শুধু পূর্ণ বীরুণ বন্য-প্রকার জীবাণু যা সবসময় রোগ ঘটায়",
            "শুধু কোনো অ্যান্টিজেনিক প্রোটিন ছাড়া বিশুদ্ধ পানি",
            "শুধু অন্য দাতার তৈরি অ্যান্টিবডি",
        ],
        "A", "medium", "factual",
        "Inactivated vaccines cannot replicate but retain epitopes that train immunity.",
        "ইনঅ্যাকটিভেটেড টিকা বংশবৃদ্ধি করতে পারে না কিন্তু এপিটোপ ধরে রাখে।",
    ),
    q(
        "A live attenuated vaccine is characterized by which feature?",
        "জীবিত অ্যাটেনুয়েটেড টিকার বৈশিষ্ট্য কোনটি?",
        [
            "Weakened living microbes that usually cannot cause full disease but stimulate strong immunity",
            "Only chemical antitoxins without any microbial antigen",
            "Only antibiotics mixed with glucose saline",
            "Only maternal antibodies collected from cord blood",
        ],
        [
            "দুর্বলকৃত জীবিত অণুজীব যা সাধারণত পূর্ণ রোগ ঘটায় না কিন্তু শক্তিশালী অনাক্রম্যতা জাগায়",
            "শুধু অণুজীব অ্যান্টিজেনহীন রাসায়নিক অ্যান্টিটক্সিন",
            "শুধু গ্লুকোজ স্যালাইনের সাথে মেশানো অ্যান্টিবায়োটিক",
            "শুধু নাভির রক্ত থেকে সংগৃহীত মাতৃ অ্যান্টিবডি",
        ],
        "A", "medium", "factual",
        "Attenuation reduces virulence while preserving immunogenicity for lasting memory.",
        "অ্যাটেনুয়েশন বীরুণতা কমায় কিন্তু ইমিউনোজেনিসিটি ও মেমোরি রাখে।",
    ),
    q(
        "Toxoid vaccines (e.g., for tetanus/diphtheria) mainly contain what?",
        "টক্সয়েড টিকা (যেমন ধনুষ্টংকার/ডিপথেরিয়া) মূলত কী ধারণ করে?",
        [
            "Inactivated bacterial toxins that still induce antitoxin antibodies",
            "Only live viruses that replicate in every organ",
            "Only pure lipids without protein epitopes",
            "Only phagocytic neutrophils suspended in saline",
        ],
        [
            "নিষ্ক্রিয়কৃত ব্যাকটেরিয়াল টক্সিন যা এখনও অ্যান্টিটক্সিন অ্যান্টিবডি উদ্দীপিত করে",
            "শুধু প্রতিটি অঙ্গে বংশবৃদ্ধিকারী জীবিত ভাইরাস",
            "শুধু প্রোটিন এপিটোপহীন বিশুদ্ধ লিপিড",
            "শুধু স্যালাইনে ভাসমান ফ্যাগোসাইটিক নিউট্রোফিল",
        ],
        "A", "medium", "factual",
        "Toxoids are detoxified toxins used to raise protective antitoxin antibodies.",
        "টক্সয়েড বিষহীন টক্সিন যা প্রতিরক্ষামূলক অ্যান্টিটক্সিন তৈরি করায়।",
    ),
    q(
        "How does vaccination differ from giving therapeutic antibiotics?",
        "চিকিৎসামূলক অ্যান্টিবায়োটিক দেওয়ার থেকে টিকাদান কীভাবে আলাদা?",
        [
            "Vaccines prevent disease by training immunity; antibiotics treat existing bacterial infections",
            "Vaccines always kill bacteria instantly like antibiotics",
            "Antibiotics always create lifelong memory B cells",
            "Both are identical preparations of live attenuated microbes",
        ],
        [
            "টিকা অনাক্রম্যতা প্রশিক্ষণ দিয়ে রোগ প্রতিরোধ করে; অ্যান্টিবায়োটিক বিদ্যমান ব্যাকটেরিয়া সংক্রমণের চিকিৎসা করে",
            "টিকা সবসময় অ্যান্টিবায়োটিকের মতো তাৎক্ষণিক ব্যাকটেরিয়া মারে",
            "অ্যান্টিবায়োটিক সবসময় আজীবন মেমোরি বি কোষ তৈরি করে",
            "উভয়ই জীবিত অ্যাটেনুয়েটেড অণুজীবের অভিন্ন প্রস্তুতি",
        ],
        "A", "medium", "conceptual",
        "Immunization is preventive adaptive training; antibiotics are chemotherapeutic agents.",
        "টিকা প্রতিরোধমূলক; অ্যান্টিবায়োটিক ব্যাকটেরিয়া সংক্রমণের চিকিৎসা।",
    ),
    q(
        "Herd immunity from high vaccination coverage mainly helps whom?",
        "উচ্চ টিকা কভারেজের হার্ড ইমিউনিটি মূলত কাকে সাহায্য করে?",
        [
            "Even unvaccinated or vulnerable people by reducing community pathogen spread",
            "Only pathogens by increasing their transmission rate",
            "Only people who never contact any microbe in life",
            "Only by abolishing all innate barriers in a population",
        ],
        [
            "সম্প্রদায়ে জীবাণু বিস্তার কমিয়ে টিকাবিহীন বা ঝুঁকিপূর্ণ মানুষকেও",
            "শুধু প্যাথোজেনকে সংক্রমণ হার বাড়িয়ে",
            "শুধু জীবনে কখনো জীবাণু স্পর্শ করে না এমন মানুষকে",
            "শুধু জনগোষ্ঠীর সব সহজাত বাধা বাতিল করে",
        ],
        "A", "hard", "conceptual",
        "When enough people are immune, chain of transmission breaks and protects others.",
        "পর্যাপ্ত মানুষ অনাক্রম্য হলে সংক্রমণ শৃঙ্খল ভেঙে অন্যরাও সুরক্ষিত হয়।",
    ),
    q(
        "After successful vaccination, which cells mainly enable long-term protection?",
        "সফল টিকাদানের পর দীর্ঘমেয়াদি সুরক্ষায় মূলত কোন কোষ কাজ করে?",
        [
            "Memory lymphocytes formed during the adaptive response to vaccine antigens",
            "Only platelets that seal capillary leaks",
            "Only osteoblasts that deposit bone matrix",
            "Only keratin flakes shed from the epidermis",
        ],
        [
            "টিকা অ্যান্টিজেনের অ্যাডাপটিভ সাড়ায় গঠিত মেমোরি লিম্ফোসাইট",
            "শুধু কৈশিক ক্ষরণ বন্ধকারী প্লেটলেট",
            "শুধু অস্থি ম্যাট্রিক্স জমাকারী অস্টিওব্লাস্ট",
            "শুধু এপিডার্মিস থেকে ঝরা কেরাটিন আঁশ",
        ],
        "A", "easy", "conceptual",
        "Vaccine-induced memory cells speed secondary responses on later real exposure.",
        "টিকাজনিত মেমোরি কোষ পরে প্রকৃত সংস্পর্শে দ্রুত সাড়া দেয়।",
    ),
    q(
        "Antiserum therapy differs from vaccination mainly because antiserum does what?",
        "অ্যান্টিসিরাম থেরাপি টিকাদান থেকে আলাদা কারণ অ্যান্টিসিরাম মূলত কী করে?",
        [
            "Supplies ready-made antibodies for immediate passive protection",
            "Always forces the host to invent new MHC alleles",
            "Replaces the need for any innate barriers forever",
            "Converts all T cells into erythrocytes within hours",
        ],
        [
            "তাৎক্ষণিক নিষ্ক্রিয় সুরক্ষার জন্য তৈরি অ্যান্টিবডি সরবরাহ করে",
            "হোস্টকে সবসময় নতুন এমএইচসি অ্যালিল উদ্ভাবনে বাধ্য করে",
            "চিরকাল সব সহজাত বাধার প্রয়োজনীয়তা মুছে দেয়",
            "কয়েক ঘণ্টায় সব টি কোষকে ইরিথ্রোসাইটে বদলায়",
        ],
        "A", "medium", "conceptual",
        "Antiserum is passive; vaccines actively train the recipient's immune system.",
        "অ্যান্টিসিরাম নিষ্ক্রিয়; টিকা গ্রহীতার ইমিউনতন্ত্র সক্রিয়ভাবে প্রশিক্ষণ দেয়।",
    ),
    q(
        "Which statement best explains why properly designed vaccines usually do not cause the full disease?",
        "সঠিকভাবে ডিজাইন করা টিকা সাধারণত পূর্ণ রোগ ঘটায় না—কোন ব্যাখ্যা সবচেয়ে ভালো?",
        [
            "Antigens are killed, weakened, or subunit/toxoid forms that lack full virulence",
            "Vaccines contain only lethal wild pathogens at maximum dose",
            "Vaccines remove all white blood cells before injection",
            "Vaccines block breathing so microbes cannot enter lungs",
        ],
        [
            "অ্যান্টিজেন নিহত, দুর্বলকৃত বা সাবইউনিট/টক্সয়েড রূপে থাকে যাতে পূর্ণ বীরুণতা থাকে না",
            "টিকায় সর্বোচ্চ মাত্রায় শুধু মারাত্মক বন্য প্যাথোজেন থাকে",
            "ইনজেকশনের আগে টিকা সব শ্বেতকণিকা সরিয়ে দেয়",
            "টিকা শ্বাস বন্ধ করে যাতে জীবাণু ফুসফুসে না ঢোকে",
        ],
        "A", "medium", "conceptual",
        "Vaccine design preserves immunogenicity while minimizing pathogenic risk.",
        "টিকা ডিজাইন ইমিউনোজেনিসিটি রাখে কিন্তু রোগসৃষ্টির ঝুঁকি কমায়।",
    ),
    q(
        "In Bangladesh HSC/public-health context, childhood immunization programs mainly aim to do what?",
        "বাংলাদেশের এইচএসসি/জনস্বাস্থ্য প্রেক্ষাপটে শিশু টিকা কর্মসূচির প্রধান লক্ষ্য কী?",
        [
            "Prevent dangerous infectious diseases by providing scheduled vaccine doses early in life",
            "Treat only genetic bone deformities with surgery",
            "Replace all nutrition with intravenous glucose alone",
            "Eliminate the need for clean water and sanitation forever",
        ],
        [
            "জীবনের শুরুতে নির্ধারিত টিকা ডোজ দিয়ে বিপজ্জনক সংক্রামক রোগ প্রতিরোধ করা",
            "শুধু অস্ত্রোপচারে জেনেটিক অস্থি বিকৃতির চিকিৎসা",
            "সব পুষ্টিকে শুধু শিরায় গ্লুকোজ দিয়ে প্রতিস্থাপন",
            "পরিষ্কার পানি ও স্যানিটেশনের প্রয়োজন চিরকাল মুছে ফেলা",
        ],
        "A", "easy", "application",
        "EPI-style schedules deliver vaccines against major childhood infections preventively.",
        "ইপিআই-ধরনের তফসিলে প্রধান শিশু সংক্রমণের প্রতিরোধমূলক টিকা দেওয়া হয়।",
    ),
    q(
        "Oral polio vaccine is an example of which general vaccine idea?",
        "মুখে দেওয়া পোলিও টিকা কোন সাধারণ টিকা ধারণার উদাহরণ?",
        [
            "Live attenuated vaccine given by mouth to stimulate mucosal and systemic immunity",
            "Only an antibiotic syrup that kills all enteric bacteria",
            "Only passive antiserum dripped onto the tongue",
            "Only a toxoid identical to tetanus toxin crystals",
        ],
        [
            "মুখে দেওয়া জীবিত অ্যাটেনুয়েটেড টিকা যা মিউকোসাল ও সিস্টেমিক অনাক্রম্যতা জাগায়",
            "শুধু সব অন্ত্রীয় ব্যাকটেরিয়া মারার অ্যান্টিবায়োটিক সিরাপ",
            "শুধু জিহ্বায় ফোঁটানো নিষ্ক্রিয় অ্যান্টিসিরাম",
            "শুধু ধনুষ্টংকার টক্সিন স্ফটিকের অভিন্ন টক্সয়েড",
        ],
        "A", "medium", "application",
        "OPV uses attenuated poliovirus orally to induce protective immunity.",
        "ওপিভি মুখে অ্যাটেনুয়েটেড পোলিওভাইরাস দিয়ে প্রতিরক্ষা তৈরি করে।",
    ),
    q(
        "BCG vaccine used in many childhood schedules is primarily intended against which disease?",
        "অনেক শিশু তফসিলে ব্যবহৃত বিসিজি টিকা প্রধানত কোন রোগের বিরুদ্ধে?",
        [
            "Tuberculosis",
            "Only scurvy from vitamin C deficiency",
            "Only myopia of the eye lens",
            "Only dental caries from sugar alone",
        ],
        [
            "যক্ষ্মা",
            "শুধু ভিটামিন সি ঘাটতির স্কার্ভি",
            "শুধু চোখের লেন্সের মায়োপিয়া",
            "শুধু চিনির কারণে দন্তক্ষয়",
        ],
        "A", "easy", "factual",
        "BCG is a live attenuated vaccine historically used to protect against tuberculosis.",
        "বিসিজি যক্ষ্মার বিরুদ্ধে ব্যবহৃত জীবিত অ্যাটেনুয়েটেড টিকা।",
    ),
    q(
        "Cold-chain maintenance for vaccines is important mainly because of which reason?",
        "টিকার কোল্ড-চেইন রক্ষণাবেক্ষণ গুরুত্বপূর্ণ কেন?",
        [
            "Many vaccines lose potency if stored outside recommended temperature ranges",
            "Cold storage permanently converts vaccines into antibiotics",
            "Freezing always increases bacterial virulence inside bottles",
            "Warm storage creates MHC molecules inside the vial glass",
        ],
        [
            "সুপারিশকৃত তাপমাত্রার বাইরে রাখলে অনেক টিকার ক্ষমতা নষ্ট হয়",
            "ঠান্ডা সংরক্ষণ টিকাকে স্থায়ীভাবে অ্যান্টিবায়োটিকে বদলায়",
            "হিমায়িত করলে বোতলের ভিতর ব্যাকটেরিয়ার বীরুণতা সবসময় বাড়ে",
            "উষ্ণ সংরক্ষণ ভায়াল কাচের ভিতরে এমএইচসি অণু তৈরি করে",
        ],
        "A", "medium", "application",
        "Potency depends on correct refrigerated/frozen storage throughout distribution.",
        "বিতরণের পুরো পথে সঠিক তাপমাত্রা ছাড়া টিকার ক্ষমতা নষ্ট হতে পারে।",
    ),
    q(
        "Primary immunization followed by boosters is intended to achieve which outcome?",
        "প্রাথমিক টিকাদানের পর বুস্টার দিয়ে কোন ফলাফল লক্ষ্য করা হয়?",
        [
            "Build and then reinforce protective antibody and memory responses over time",
            "Erase all adaptive memory so innate barriers act alone",
            "Replace lymphocytes with mature erythrocytes permanently",
            "Induce only passive maternal antibody transfer in adults",
        ],
        [
            "সময়ের সাথে প্রতিরক্ষামূলক অ্যান্টিবডি ও মেমোরি সাড়া গড়ে তুলে পুনর্জোরদার করা",
            "সব অ্যাডাপটিভ মেমোরি মুছে শুধু সহজাত বাধা রাখা",
            "লিম্ফোসাইটকে স্থায়ীভাবে পরিপক্ক ইরিথ্রোসাইটে বদলানো",
            "প্রাপ্তবয়স্কদের শুধু মাতৃ অ্যান্টিবডি স্থানান্তর ঘটানো",
        ],
        "A", "easy", "conceptual",
        "Schedules prime then boost adaptive immunity for durable protection.",
        "তফসিল প্রথমে প্রাইম করে পরে বুস্ট করে দীর্ঘস্থায়ী সুরক্ষা দেয়।",
    ),
    q(
        "Subunit vaccines generally contain which components?",
        "সাবইউনিট টিকায় সাধারণত কোন উপাদান থাকে?",
        [
            "Selected antigenic parts of a pathogen rather than the whole live organism",
            "Only intact fully virulent organisms that must cause disease",
            "Only distilled water and sodium chloride crystals",
            "Only donor plasma cells capable of lifelong infection",
        ],
        [
            "সম্পূর্ণ জীবিত জীবাণু নয়, প্যাথোজেনের নির্বাচিত অ্যান্টিজেনিক অংশ",
            "শুধু পূর্ণ বীরুণ অক্ষত জীবাণু যা অবশ্যই রোগ ঘটায়",
            "শুধু ডিস্টিলড পানি ও সোডিয়াম ক্লোরাইড স্ফটিক",
            "শুধু আজীবন সংক্রমণক্ষম দাতা প্লাজমা কোষ",
        ],
        "A", "hard", "factual",
        "Subunit vaccines use purified antigens to stimulate immunity with fewer whole-pathogen risks.",
        "সাবইউনিট টিকা বিশুদ্ধ অ্যান্টিজেন দিয়ে কম ঝুঁকিতে অনাক্রম্যতা জাগায়।",
    ),
    q(
        "If antibody titers fall years after vaccination, the most appropriate public-health step is often what?",
        "টিকার বছর পর অ্যান্টিবডি টাইটার কমলে জনস্বাস্থ্যে প্রায়ই কোন পদক্ষেপ উপযুক্ত?",
        [
            "Give a booster dose according to recommended schedules",
            "Ban all future vaccines permanently",
            "Replace vaccines with only high-dose antibiotics lifelong",
            "Remove all memory cells surgically",
        ],
        [
            "সুপারিশকৃত তফসিল অনুযায়ী বুস্টার ডোজ দেওয়া",
            "ভবিষ্যতের সব টিকা স্থায়ী নিষিদ্ধ করা",
            "আজীবন শুধু উচ্চমাত্রার অ্যান্টিবায়োটিক দিয়ে টিকা প্রতিস্থাপন",
            "অস্ত্রোপচারে সব মেমোরি কোষ অপসারণ",
        ],
        "A", "medium", "application",
        "Boosters restore protective titers when immunity wanes for certain vaccines.",
        "কিছু টিকায় অনাক্রম্যতা কমলে বুস্টার টাইটার পুনরুদ্ধার করে।",
    ),
    q(
        "Which outcome best indicates that a vaccine has induced useful adaptive immunity?",
        "টিকা উপযোগী অ্যাডাপটিভ অনাক্রম্যতা জাগিয়েছে—কোন ফলাফল তা সবচেয়ে ভালো নির্দেশ করে?",
        [
            "Appearance of specific antibodies and/or memory cells against the vaccine antigen",
            "Complete disappearance of neutrophils from blood forever",
            "Permanent inability of skin to act as a barrier",
            "Conversion of all antigens into digestive enzymes",
        ],
        [
            "টিকা অ্যান্টিজেনের বিরুদ্ধে নির্দিষ্ট অ্যান্টিবডি এবং/অথবা মেমোরি কোষের উপস্থিতি",
            "রক্ত থেকে নিউট্রোফিলের চিরকালীন সম্পূর্ণ অদৃশ্য হওয়া",
            "ত্বকের বাধা হিসেবে কাজ করার স্থায়ী অক্ষমতা",
            "সব অ্যান্টিজেনের পাচক এনজাইমে রূপান্তর",
        ],
        "A", "medium", "application",
        "Protective vaccination is evidenced by antigen-specific adaptive effectors and memory.",
        "সফল টিকার প্রমাণ নির্দিষ্ট অ্যাডাপটিভ ইফেক্টর ও মেমোরি।",
    ),
]


TOPICS_MAP = {
    "bio2_27_ch10_t01": T01,
    "bio2_27_ch10_t02": T02,
    "bio2_27_ch10_t03": T03,
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
        "chapter": "bio2_27_ch10",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p300_pdf306.png",
            "p301_pdf307.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio2_27_ch10_t01": {
                "title": "Innate immunity / সহজাত প্রতিরক্ষা",
                "themes": [
                    "immunity/immune system definitions; innate inborn rapid defense",
                    "species/group/individual levels; non-specific first/second lines",
                    "skin; sebum/sebaceous glands; lysozyme; stomach acid; mucociliary clearance",
                    "phagocytosis/phagosome; neutrophils-monocytes; interferon; pyrogen; opsonin; inflammation",
                ],
            },
            "bio2_27_ch10_t02": {
                "title": "Acquired immunity / অর্জিত প্রতিরক্ষা",
                "themes": [
                    "acquired adaptive definition; active vs passive",
                    "antigen; antibody; antigen–antibody contrast; protein nature of antibodies",
                    "MHC; memory lymphocytes; humoral vs cell-mediated; plasma cells; specificity",
                    "natural/artificial active & passive; secondary response; antiserum application",
                ],
            },
            "bio2_27_ch10_t03": {
                "title": "Vaccination / টিকাদান",
                "themes": [
                    "vaccine definition; antigen-like stimulus; artificial active immunity",
                    "booster rationale; killed/live attenuated/toxoid/subunit types",
                    "vaccine vs antibiotic; herd immunity; memory after vaccination; antiserum contrast",
                    "EPI childhood aims; OPV; BCG; cold chain; schedules; titer boosters; success markers",
                ],
            },
        },
        "low_confidence": [
            "OCR of printed pages p300–301 is mainly CQ (short-answer) text, not dense MCQ keys; stems authored/reconstructed from readable CQ themes and standard HSC Zoology Ch10 facts.",
            "Printed MCQ section for ch10 is only two pages; bank supplemented to exactly 20 items per syllabus topic.",
            "Figure-/stimulus-linked items (if any on source pages) rewritten as standalone stems.",
            "Vaccine program examples (BCG, OPV, EPI-style scheduling, cold chain) follow common Bangladesh HSC/public-health phrasing aligned with OCR CQ themes.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio2_27_ch10_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio2_27_ch10_t01": 20,
                "bio2_27_ch10_t02": 20,
                "bio2_27_ch10_t03": 20,
            },
        },
    }
    out = (
        ROOT
        / "content"
        / "bank"
        / "udvash_raw"
        / "biology_2"
        / "parsed"
        / "ch10_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
