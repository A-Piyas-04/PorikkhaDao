#!/usr/bin/env python3
"""Seed Biology 1st Paper Ch8 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio1_27_ch08_t01..t03 (plant tissues; tissue systems; secondary growth).
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
    "biology p1 ch08; curated bilingual"
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


# --- t01: Plant tissues / উদ্ভিদ টিস্যু ---
T01 = [
    q(
        "Which tissue has small cells that are roughly equal in length and breadth?",
        "কোন টিস্যুর কোষগুলো আকারে ছোট এবং দৈর্ঘ্য ও প্রস্থ প্রায় সমান?",
        ["Meristematic tissue", "Simple permanent tissue", "Complex permanent tissue", "Secretory tissue"],
        ["ভাজক টিস্যু", "সরল স্থায়ী টিস্যু", "জটিল স্থায়ী টিস্যু", "ক্ষরণকারী টিস্যু"],
        "A", "easy", "factual",
        "Meristematic cells are typically small, isodiametric and densely packed with thin walls.",
        "ভাজক টিস্যুর কোষ সাধারণত ছোট, প্রায় সমমাত্রিক এবং পাতলা প্রাচীরযুক্ত ঘন সন্নিবেশিত হয়।",
    ),
    q(
        "Which is a characteristic of permanent tissue?",
        "স্থায়ী টিস্যুর বৈশিষ্ট্য কোনটি?",
        [
            "Cells remain continuously dividing",
            "Cells lack a definite shape",
            "Cells are mature and differentiated",
            "Cells always lack vacuoles",
        ],
        [
            "কোষগুলো নিরন্তর বিভাজিত হয়",
            "কোষের নির্দিষ্ট আকৃতি নেই",
            "কোষগুলো পরিণত ও বিভেদিত",
            "কোষে সবসময় ভ্যাকুওল থাকে না",
        ],
        "C", "easy", "conceptual",
        "Permanent tissues are composed of mature, differentiated cells that have largely lost meristematic activity.",
        "স্থায়ী টিস্যু পরিণত ও বিভেদিত কোষ দিয়ে গঠিত; এদের ভাজক ক্ষমতা সাধারণত লুপ্ত।",
    ),
    q(
        "Which is a living component of mature xylem tissue?",
        "পরিণত জাইলেম টিস্যুর সজীব উপাদান কোনটি?",
        ["Tracheid", "Vessel", "Xylem parenchyma", "Xylem fibre"],
        ["ট্রাকিড", "ভেসেল", "জাইলেম প্যারেনকাইমা", "জাইলেম ফাইবার"],
        "C", "easy", "factual",
        "Tracheids, vessels and xylem fibres are dead at maturity; xylem parenchyma remains living.",
        "পরিণত অবস্থায় ট্রাকিড, ভেসেল ও জাইলেম ফাইবার মৃত; জাইলেম প্যারেনকাইমা সজীব থাকে।",
    ),
    q(
        "Which structure is an example of mass meristem?",
        "মাস ভাজক টিস্যুর উদাহরণ কোনটি?",
        ["Medullary rays of stem", "Leaf blade", "Endosperm tissue", "Stem epidermis"],
        ["কাণ্ডের মজ্জারশ্মি", "পাতার ফলক", "সস্য টিস্যু", "কাণ্ডের বহিস্ত্বক"],
        "C", "medium", "factual",
        "Mass meristem divides in all planes; endosperm and pollen-sac tissues are classic examples.",
        "মাস ভাজক সব তলে বিভাজিত হয়; সস্য ও রেণুথলি এর উদাহরণ।",
    ),
    q(
        "Which meristem increases the surface area of a leaf?",
        "কোন ভাজক টিস্যুর কারণে উদ্ভিদের পাতার আয়তন বৃদ্ধি পায়?",
        ["Mass meristem", "Plate meristem", "Secondary meristem", "Rib meristem"],
        ["মাস ভাজক টিস্যু", "প্লেট ভাজক টিস্যু", "সেকেন্ডারি ভাজক টিস্যু", "রিব ভাজক টিস্যু"],
        "B", "medium", "conceptual",
        "Plate (lamellar) meristem divides mainly in one plane, expanding leaf area.",
        "প্লেট ভাজক প্রধানত এক তলে বিভাজিত হয়ে পাতার আয়তন বাড়ায়।",
    ),
    q(
        "Medullary rays arise from which meristematic tissue?",
        "মজ্জারশ্মি কোন ভাজক টিস্যু থেকে তৈরি?",
        ["Mass meristem", "Rib meristem", "Procambium", "Protoderm"],
        ["মাস মেরিস্টেম", "রিব মেরিস্টেম", "প্রোক্যাম্বিয়াম", "প্রোটোডার্ম"],
        "B", "medium", "factual",
        "Rib (file) meristem produces elongated rows of cells such as medullary rays and root cortex files.",
        "রিব ভাজক দীর্ঘ সারি তৈরি করে; মজ্জারশ্মি ও মূলের কর্টেক্স এর উদাহরণ।",
    ),
    q(
        "According to the plane of cell division, meristems are of how many types?",
        "কোষ বিভাজন তল অনুসারে ভাজক টিস্যু কত প্রকার?",
        ["2", "3", "4", "5"],
        ["২", "৩", "৪", "৫"],
        "B", "easy", "factual",
        "By division plane: plate, rib and mass meristems — three types.",
        "বিভাজন তল অনুসারে প্লেট, রিব ও মাস — তিন প্রকার ভাজক টিস্যু।",
    ),
    q(
        "According to function (histogen concept), primary meristems are of how many types?",
        "কাজ অনুসারে প্রাইমারি ভাজক টিস্যু কত প্রকার?",
        ["2", "3", "4", "5"],
        ["২", "৩", "৪", "৫"],
        "B", "easy", "factual",
        "Functionally: protoderm, procambium and ground meristem — three types.",
        "কাজ অনুসারে প্রোটোডার্ম, প্রোক্যাম্বিয়াম ও গ্রাউন্ড মেরিস্টেম — তিন প্রকার।",
    ),
    q(
        "Epidermis is formed from which meristem?",
        "এপিডার্মিস কোন ধরনের ভাজক টিস্যু হতে সৃষ্টি হয়?",
        ["Protoderm", "Procambium", "Ground meristem", "Intercalary meristem"],
        ["প্রোটোডার্ম", "প্রোক্যাম্বিয়াম", "গ্রাউন্ড মেরিস্টেম", "ইন্টারক্যালারি মেরিস্টেম"],
        "A", "easy", "factual",
        "Protoderm is the outermost primary meristem that forms the epidermis/epiblema.",
        "প্রোটোডার্ম থেকে এপিডার্মিস/এপিব্লেমা সৃষ্টি হয়।",
    ),
    q(
        "Which of the following is NOT formed from procambium?",
        "নিচের কোনটি প্রোক্যাম্বিয়াম হতে সৃষ্টি হয় না?",
        ["Cortex", "Phloem", "Xylem", "Cambium"],
        ["কর্টেক্স", "ফ্লোয়েম", "জাইলেম", "ক্যাম্বিয়াম"],
        "A", "medium", "conceptual",
        "Procambium gives primary xylem, primary phloem and (in dicots) cambium; cortex comes from ground meristem.",
        "প্রোক্যাম্বিয়াম থেকে জাইলেম, ফ্লোয়েম ও ক্যাম্বিয়াম; কর্টেক্স গ্রাউন্ড মেরিস্টেম থেকে আসে।",
    ),
    q(
        "Which tissue is found at the tips of root and shoot?",
        "উদ্ভিদের মূল ও কাণ্ডের শীর্ষের টিস্যু কোনটি?",
        ["Meristematic tissue", "Simple permanent tissue", "Complex permanent tissue", "Secretory tissue"],
        ["ভাজক টিস্যু", "সরল টিস্যু", "জটিল টিস্যু", "ক্ষরণকারী টিস্যু"],
        "A", "easy", "factual",
        "Apical meristems at root and shoot tips produce primary growth.",
        "মূল ও কাণ্ডের শীর্ষে শীর্ষস্থ ভাজক টিস্যু প্রাইমারি বৃদ্ধি ঘটায়।",
    ),
    q(
        "Which is a secondary meristematic tissue?",
        "সেকেন্ডারি ভাজক টিস্যু কোনটি?",
        ["Protoderm", "Procambium", "Ground meristem", "Cambium"],
        ["প্রোটোডার্ম", "প্রোক্যাম্বিয়াম", "গ্রাউন্ড মেরিস্টেম", "ক্যাম্বিয়াম"],
        "D", "easy", "factual",
        "Vascular and cork cambia are secondary (lateral) meristems arising later in development.",
        "ভাস্কুলার ও কর্ক ক্যাম্বিয়াম পরবর্তীকালে সৃষ্ট সেকেন্ডারি/পার্শ্বীয় ভাজক টিস্যু।",
    ),
    q(
        "Which structure is present in both xylem and phloem?",
        "নিচের কোনটি জাইলেম ও ফ্লোয়েম উভয় টিস্যুতেই বিদ্যমান?",
        ["Tracheid", "Vessel", "Sieve tube", "Fibre"],
        ["ট্রাকিড", "ভেসেল", "সিভনল", "ফাইবার"],
        "D", "medium", "conceptual",
        "Fibres occur as xylem fibres and phloem (bast) fibres; tracheids/vessels are xylem-only and sieve tubes are phloem-only.",
        "ফাইবার জাইলেম ও ফ্লোয়েম উভয়ে থাকে; ট্রাকিড/ভেসেল কেবল জাইলেমে, সিভনল কেবল ফ্লোয়েমে।",
    ),
    q(
        "Medullary rays are composed mainly of which tissue?",
        "মজ্জারশ্মি কোন টিস্যু দিয়ে গঠিত?",
        ["Sclerenchyma", "Parenchyma", "Collenchyma", "Aerenchyma"],
        ["স্ক্লেরেনকাইমা", "প্যারেনকাইমা", "কোলেনকাইমা", "অ্যারেনকাইমা"],
        "B", "easy", "factual",
        "Medullary (pith) rays are radial parenchyma sheets linking pith and cortex/pericycle regions.",
        "মজ্জারশ্মি মূলত প্যারেনকাইমা কোষের অরীয় স্তর।",
    ),
    q(
        "Which statement about meristematic tissue is correct?",
        "ভাজক টিস্যু সম্পর্কে কোন বাক্যটি সঠিক?",
        [
            "Metabolic rate of the cells is low",
            "Xylem and phloem are types of meristem",
            "The outer covering of the root is called epidermis only",
            "Cells usually lack large vacuoles and divide actively",
        ],
        [
            "কোষগুলোর বিপাকীয় হার কম",
            "জাইলেম ও ফ্লোয়েম এক ধরনের ভাজক টিস্যু",
            "মূলের বহিরাবরণকে কেবল এপিডার্মিস বলে",
            "কোষে সাধারণত বড় ভ্যাকুওল থাকে না এবং সক্রিয়ভাবে বিভাজিত হয়",
        ],
        "D", "medium", "conceptual",
        "Meristem cells are metabolically active, often with dense cytoplasm and no large central vacuole.",
        "ভাজক কোষের বিপাক হার বেশি, সাইটোপ্লাজম ঘন এবং বড় কেন্দ্রীয় ভ্যাকুওল সাধারণত অনুপস্থিত।",
    ),
    q(
        "Axillary and terminal buds are produced by the activity of which meristem?",
        "কক্ষমুকুল ও শীর্ষমুকুল যেটির ক্রিয়ার ফলে উৎপন্ন হয়?",
        ["Lateral meristem", "Intercalary meristem", "Apical meristem", "Parenchyma"],
        ["পার্শ্ব মেরিস্টেম", "ইন্টারক্যালারি মেরিস্টেম", "শীর্ষ মেরিস্টেম", "প্যারেনকাইমা"],
        "C", "medium", "conceptual",
        "Shoot apical meristem activity produces the terminal bud and axillary buds in leaf axils.",
        "কাণ্ডের শীর্ষ মেরিস্টেম থেকে শীর্ষমুকুল ও পত্রকক্ষে কক্ষমুকুল সৃষ্টি হয়।",
    ),
    q(
        "From which tissue do meristems originally arise?",
        "কোথায় হতে ভাজক টিস্যু সৃষ্টি হয়?",
        ["Pith", "Permanent tissue only", "Cambium only", "Promeristem"],
        ["মজ্জা", "কেবল স্থায়ী টিস্যু", "কেবল ক্যাম্বিয়াম", "প্রোমেরিস্টেম"],
        "D", "medium", "factual",
        "Promeristem is the earliest embryonic meristem from which primary meristems differentiate.",
        "প্রোমেরিস্টেম থেকে প্রাইমারি ভাজক টিস্যুসমূহ উদ্ভূত হয়।",
    ),
    q(
        "Which tissues are formed from ground meristem?",
        "গ্রাউন্ড মেরিস্টেম থেকে কোন কোন টিস্যু গঠিত হয়?",
        [
            "Epidermis and stomata",
            "Xylem and phloem only",
            "Cortex, pith and medullary rays",
            "Root hairs only",
        ],
        [
            "এপিডার্মিস ও পত্ররন্ধ্র",
            "কেবল জাইলেম ও ফ্লোয়েম",
            "কর্টেক্স, মজ্জা ও মজ্জারশ্মি",
            "কেবল মূলরোম",
        ],
        "C", "medium", "conceptual",
        "Ground meristem produces the ground tissue system: cortex, pith and related parenchyma including rays.",
        "গ্রাউন্ড মেরিস্টেম থেকে কর্টেক্স, মজ্জা ও মজ্জারশ্মিসহ গ্রাউন্ড টিস্যু গঠিত হয়।",
    ),
    q(
        "A leaf is an example of which meristem type by plane of division?",
        "পাতা কোন ভাজক টিস্যুর উদাহরণ?",
        ["Mass meristem", "Rib meristem", "Plate meristem", "Protoderm"],
        ["মাস", "রিব", "প্লেট", "প্রোটোডার্ম"],
        "C", "easy", "factual",
        "Leaf expansion is largely due to plate meristem activity.",
        "পাতার সম্প্রসারণ মূলত প্লেট ভাজক টিস্যুর কার্যক্রমে ঘটে।",
    ),
    q(
        "Which simple tissue provides flexible mechanical support in young stems?",
        "কোন সরল টিস্যু তরুণ কাণ্ডে নমনীয় যান্ত্রিক দৃঢ়তা দেয়?",
        ["Parenchyma", "Collenchyma", "Sclerenchyma", "Aerenchyma"],
        ["প্যারেনকাইমা", "কোলেনকাইমা", "স্ক্লেরেনকাইমা", "অ্যারেনকাইমা"],
        "B", "easy", "conceptual",
        "Living collenchyma with unevenly thickened cellulose walls supports growing organs flexibly.",
        "সজীব কোলেনকাইমার অসম পুরু সেলুলোজ প্রাচীর তরুণ অঙ্গে নমনীয় দৃঢ়তা দেয়।",
    ),
]


# --- t02: Tissue systems / টিস্যুতন্ত্র ---
T02 = [
    q(
        "In which plant are sunken stomata found?",
        "'লুক্কায়িত পত্ররন্ধ্র' পাওয়া যায় কোন উদ্ভিদে?",
        ["Nerium (oleander)", "Hydrilla", "Water lily", "Water hyacinth"],
        ["করবী", "হাইড্রিলা", "শাপলা", "কচুরিপানা"],
        "A", "easy", "factual",
        "Xerophytic Nerium has sunken stomata to reduce transpiration.",
        "শুষ্কসহিষ্ণু করবীতে প্রস্বেদন কমাতে লুক্কায়িত পত্ররন্ধ্র থাকে।",
    ),
    q(
        "Epithem is associated with which structure?",
        "নিচের কোন গঠনটিতে এপিথেম দেখা যায়?",
        ["Hydathode", "Stomata", "Trichome", "Collecters"],
        ["হাইডাথোড", "স্টোমাটা", "ট্রাইকোম", "কোলেটার্স"],
        "A", "medium", "factual",
        "Hydathodes have a water pore above loosely arranged epithem cells linked to vein endings.",
        "হাইডাথোডে পানিগহ্বরের নিচে অসংলগ্ন এপিথেম কোষ থাকে।",
    ),
    q(
        "Which organelle is typically absent in the subsidiary cells of a stoma?",
        "পত্ররন্ধ্রের সহকারী কোষে নিচের কোন অঙ্গাণুটি অনুপস্থিত?",
        ["Ribosome", "Mitochondrion", "Nucleus", "Chloroplast"],
        ["রাইবোসোম", "মাইটোকন্ড্রিয়া", "নিউক্লিয়াস", "ক্লোরোপ্লাস্ট"],
        "D", "medium", "factual",
        "Guard cells contain chloroplasts; subsidiary cells generally lack them.",
        "রক্ষীকোষে ক্লোরোপ্লাস্ট থাকে; সহকারী কোষে সাধারণত থাকে না।",
    ),
    q(
        "Casparian strips are present in which layer?",
        "নিচের কোনটিতে ক্যাসপেরিয়ান স্ট্রিপ বিদ্যমান?",
        ["Epidermis", "Hypodermis", "Pericycle", "Endodermis"],
        ["এপিডার্মিস", "হাইপোডার্মিস", "পেরিসাইকল", "এন্ডোডার্মিস"],
        "D", "easy", "factual",
        "Endodermal radial/transverse walls bear suberin Casparian strips controlling apoplastic flow.",
        "এন্ডোডার্মিসের অরীয়/প্রস্থ প্রাচীরে সুবেরিনযুক্ত ক্যাসপেরিয়ান স্ট্রিপ থাকে।",
    ),
    q(
        "Which stomatal type is surrounded by three subsidiary cells of unequal size?",
        "নিচের কোন স্টোমাটা তিনটি অসমান সহকারী কোষ দ্বারা পরিবেষ্টিত?",
        ["Paracytic", "Anisocytic", "Actinocytic", "Anomocytic"],
        ["প্যারাসাইটিক", "অ্যানিসোসাইটিক", "অ্যাক্টিনোসাইটিক", "অ্যানোমোসাইটিক"],
        "B", "medium", "factual",
        "Anisocytic (cruciferous) stomata have three unequal subsidiaries.",
        "অ্যানিসোসাইটিক পত্ররন্ধ্রে তিনটি অসমান সহকারী কোষ থাকে।",
    ),
    q(
        "A stomatal complex whose subsidiaries resemble ordinary epidermal cells is called—",
        "যে পত্ররন্ধ্রের চতুর্দিকের সহকারী কোষগুলো সাধারণ ত্বকীয় কোষের ন্যায় তাকে বলে—",
        ["Anisocytic", "Actinocytic", "Anomocytic", "Tetracytic"],
        ["অ্যানিসোসাইটিক", "অ্যাক্টিনোসাইটিক", "অ্যানোমোসাইটিক", "টেট্রাসাইটিক"],
        "C", "medium", "conceptual",
        "Anomocytic (ranunculaceous) stomata lack distinct specialized subsidiaries.",
        "অ্যানোমোসাইটিক পত্ররন্ধ্রে বিশেষায়িত সহকারী কোষ নেই।",
    ),
    q(
        "Ground tissue of the leaf is called—",
        "পাতার গ্রাউন্ড টিস্যুকে কী বলে?",
        ["Mesophyll", "Pith", "Medullary ray", "Pericycle"],
        ["মেসোফিল", "মজ্জা", "মজ্জারশ্মি", "পরিচক্র"],
        "A", "easy", "factual",
        "Leaf ground tissue between epidermises is mesophyll (palisade/spongy).",
        "পাতার দুই ত্বকের মধ্যবর্তী গ্রাউন্ড টিস্যু মেসোফিল।",
    ),
    q(
        "Hydathodes may be present on which organ?",
        "কোনটিতে হাইডাথোড থাকতে পারে?",
        ["Leaf", "Flower", "Root", "Stem only"],
        ["পাতা", "ফুল", "মূল", "কেবল কাণ্ড"],
        "A", "easy", "factual",
        "Hydathodes occur at leaf margins/tips (e.g., tomato, grasses) and enable guttation.",
        "হাইডাথোড পাতার কিনারা/অগ্রভাগে থাকে এবং গ্যাটেশন ঘটায়।",
    ),
    q(
        "Leptocentric vascular bundles are found in which plant?",
        "লেপ্টোসেন্ট্রিক ভাস্কুলার বান্ডলের উদাহরণ কোনটি?",
        ["Pteris", "Cycas", "Dracaena", "Lycopodium"],
        ["Pteris", "Cycas", "Dracaena", "Lycopodium"],
        "C", "medium", "factual",
        "In leptocentric (amphivasal) bundles, xylem surrounds central phloem — e.g., Dracaena, Yucca.",
        "লেপ্টোসেন্ট্রিকে কেন্দ্রে ফ্লোয়েম ও চারপাশে জাইলেম; Dracaena, Yucca উদাহরণ।",
    ),
    q(
        "Hadrocentric vascular bundles are found in which plant?",
        "হ্যাড্রোসেন্ট্রিক ভাস্কুলার বান্ডল কোন উদ্ভিদে পাওয়া যায়?",
        ["Pteris", "Dracaena", "Gnetum", "Yucca"],
        ["Pteris", "Dracaena", "Gnetum", "Yucca"],
        "A", "medium", "factual",
        "Hadrocentric (amphicribral) bundles have central xylem surrounded by phloem — e.g., Pteris, Lycopodium, Selaginella.",
        "হ্যাড্রোসেন্ট্রিকে কেন্দ্রে জাইলেম ও চারপাশে ফ্লোয়েম; Pteris ইত্যাদি উদাহরণ।",
    ),
    q(
        "What type of vascular bundle occurs in Selaginella?",
        "Selaginella উদ্ভিদের পরিবহণ টিস্যু কোন ধরনের?",
        ["Radial", "Conjoint", "Hadrocentric", "Leptocentric"],
        ["অরীয়", "সংযুক্ত", "হ্যাড্রোসেন্ট্রিক", "লেপ্টোসেন্ট্রিক"],
        "C", "hard", "factual",
        "Selaginella (like many pteridophytes) has hadrocentric (xylem-centric) bundles.",
        "Selaginella-এর ভাস্কুলার বান্ডল হ্যাড্রোসেন্ট্রিক (জাইলেমকেন্দ্রিক)।",
    ),
    q(
        "What type of vascular bundle is seen in rice stem?",
        "ধানে কোন ধরনের ভাস্কুলার বান্ডল দেখা যায়?",
        ["Collateral closed", "Collateral open", "Bicollateral", "Radial"],
        ["সমপাশ্বীয় বদ্ধ", "সমপাশ্বীয় মুক্ত", "সমদ্বিপাশ্বীয়", "অরীয়"],
        "A", "easy", "factual",
        "Monocot stems like rice have conjoint collateral closed bundles (no cambium).",
        "ধানসহ একবীজপত্রী কাণ্ডে সংযুক্ত সমপাশ্বীয় বদ্ধ বান্ডল থাকে।",
    ),
    q(
        "Pumpkin stem vascular bundles are—",
        "কুমড়া উদ্ভিদের কাণ্ডের ভাস্কুলার বান্ডল—",
        ["Radial", "Bicollateral", "Hadrocentric", "Leptocentric"],
        ["অরীয়", "সমদ্বিপাশ্বীয়", "হ্যাড্রোসেন্ট্রিক", "লেপ্টোসেন্ট্রিক"],
        "B", "medium", "factual",
        "Cucurbita (pumpkin/gourd) stems have bicollateral bundles with phloem on both sides of xylem.",
        "কুমড়া/লাউ জাতীয় কাণ্ডে সমদ্বিপাশ্বীয় বান্ডল থাকে।",
    ),
    q(
        "In angiosperms, radial vascular bundles are typically found in the—",
        "আবৃতবীজী উদ্ভিদের কোন অংশে অরীয় ভাস্কুলার বান্ডল দেখা যায়?",
        ["Root", "Stem", "Leaf", "Flower"],
        ["মূলে", "কাণ্ডে", "পাতায়", "ফুলে"],
        "A", "easy", "factual",
        "Roots have radial (separate) xylem and phloem on different radii.",
        "মূলে জাইলেম ও ফ্লোয়েম ভিন্ন ব্যাসার্ধে অরীয়ভাবে থাকে।",
    ),
    q(
        "What is the root epidermis called?",
        "মূলের ত্বককে কী বলে?",
        ["Pith", "Endodermis", "Epiblema", "Pericycle"],
        ["মজ্জা", "এন্ডোডার্মিস", "এপিব্লেমা", "পেরিসাইকল"],
        "C", "easy", "factual",
        "The outermost covering of the root is epiblema (piliferous layer).",
        "মূলের বহিস্ত্বককে এপিব্লেমা বলে।",
    ),
    q(
        "Which is part of the stele?",
        "স্টিলির অংশ হলো—",
        ["Hypodermis", "Endodermis", "Cortex", "Pericycle"],
        ["অধস্ত্বক", "অন্তস্ত্বক", "কর্টেক্স", "পরিচক্র"],
        "D", "medium", "conceptual",
        "Stele includes pericycle, vascular bundles, pith and medullary rays; cortex/endodermis are extrastelar.",
        "স্টিলিতে পেরিসাইকেল, ভাস্কুলার বান্ডল, মজ্জা ও মজ্জারশ্মি; কর্টেক্স/এন্ডোডার্মিস বহিঃস্টিলীয়।",
    ),
    q(
        "Which statements apply to a monocot stem? (i) cuticle present on epidermis (ii) vascular bundles conjoint (iii) bundles scattered",
        "একবীজপত্রী কাণ্ডের ক্ষেত্রে প্রযোজ্য— (i) বহিস্ত্বকে কিউটিকল উপস্থিত (ii) পরিবহণ কলাগুচ্ছ সংযুক্ত (iii) পরিবহণ টিস্যু বিক্ষিপ্তভাবে থাকে",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "Monocot stems typically have cuticularized epidermis, conjoint closed bundles scattered in ground tissue.",
        "একবীজপত্রী কাণ্ডে কিউটিকল, সংযুক্ত বদ্ধ বান্ডল এবং বিক্ষিপ্ত বিন্যাস সাধারণ।",
    ),
    q(
        "In a monocot stem, xylem of the vascular bundle is typically arranged like the letter—",
        "একবীজপত্রী উদ্ভিদের কাণ্ডের ভাস্কুলার বান্ডলে জাইলেম টিস্যুর গঠন অনেকটা কোন অক্ষরের মতো?",
        ["O-shaped only", "V or Y-shaped", "Completely circular ring", "Scattered single cells"],
        ["কেবল O-আকৃতি", "V বা Y আকৃতি", "সম্পূর্ণ বৃত্তাকার বলয়", "বিক্ষিপ্ত একক কোষ"],
        "B", "medium", "factual",
        "Monocot stem bundles often show Y/V-shaped xylem with protoxylem toward the center (endarch).",
        "একবীজপত্রী কাণ্ডের বান্ডলে জাইলেম প্রায়শই V/Y আকৃতির ও এন্ডার্ক।",
    ),
    q(
        "Which feature identifies a monocot root internally?",
        "একবীজপত্রী মূলের অন্তর্গঠনগত শনাক্তকারী বৈশিষ্ট্য কোনটি?",
        [
            "Cuticle present on epidermis",
            "Hypodermis of sclerenchyma always present",
            "Xylem shaped like English Y",
            "Vascular bundles radial in nature",
        ],
        [
            "বহিস্ত্বকে কিউটিকল উপস্থিত",
            "অধস্ত্বকে সবসময় স্ক্লেরেনকাইমা আছে",
            "জাইলেম ইংরেজি Y আকৃতিবিশিষ্ট",
            "ভাস্কুলার বান্ডল অরীয় প্রকৃতির",
        ],
        "D", "hard", "conceptual",
        "Roots (mono- and dicot) have radial bundles; Y-shaped xylem is a stem feature, not a root identifier.",
        "মূলে অরীয় বান্ডল শনাক্তকারী; Y-আকৃতির জাইলেম কাণ্ডের বৈশিষ্ট্য।",
    ),
    q(
        "Passage cells are present in which layer?",
        "কোন স্তরে প্যাসেজ কোষ বিদ্যমান?",
        ["Hypodermis", "Pith", "Endodermis", "Pericycle"],
        ["হাইপোডার্মিস", "মজ্জা", "এন্ডোডার্মিস", "পেরিসাইকল"],
        "C", "medium", "factual",
        "Thin-walled passage cells in the endodermis opposite protoxylem poles allow controlled transport.",
        "এন্ডোডার্মিসে প্রোটোজাইলেমের বিপরীতে পাতলা প্রাচীরযুক্ত প্যাসেজ কোষ থাকে।",
    ),
]


# --- t03: Secondary growth / গৌণ বৃদ্ধি ---
T03 = [
    q(
        "Which meristem is mainly responsible for increase in girth (secondary growth)?",
        "উদ্ভিদের ব্যাস বৃদ্ধি বা গৌণ বৃদ্ধির জন্য প্রধানত কোন ভাজক টিস্যু দায়ী?",
        ["Apical meristem", "Intercalary meristem", "Lateral meristem (cambium)", "Plate meristem"],
        ["শীর্ষস্থ ভাজক টিস্যু", "ইন্টারক্যালারি মেরিস্টেম", "পার্শ্বীয় ভাজক টিস্যু (ক্যাম্বিয়াম)", "প্লেট মেরিস্টেম"],
        "C", "easy", "conceptual",
        "Lateral meristems (vascular cambium and cork cambium) add secondary tissues and increase girth.",
        "পার্শ্বীয় ভাজক (ভাস্কুলার ও কর্ক ক্যাম্বিয়াম) গৌণ টিস্যু যোগ করে ব্যাস বাড়ায়।",
    ),
    q(
        "Why do most monocot stems lack typical secondary growth?",
        "অধিকাংশ একবীজপত্রী কাণ্ডে সাধারণ গৌণ বৃদ্ধি অনুপস্থিত কেন?",
        [
            "They lack xylem",
            "Vascular bundles are closed (no cambium)",
            "They have no epidermis",
            "They have only radial bundles",
        ],
        [
            "এদের জাইলেম নেই",
            "ভাস্কুলার বান্ডল বদ্ধ (ক্যাম্বিয়ামহীন)",
            "এদের এপিডার্মিস নেই",
            "এদের কেবল অরীয় বান্ডল আছে",
        ],
        "B", "easy", "conceptual",
        "Closed collateral bundles lack fascicular cambium, so ordinary secondary growth does not occur.",
        "বদ্ধ সমপাশ্বীয় বান্ডলে ক্যাম্বিয়াম না থাকায় সাধারণ গৌণ বৃদ্ধি ঘটে না।",
    ),
    q(
        "In a typical dicot stem, open collateral bundles allow secondary growth because they contain—",
        "দ্বিবীজপত্রী কাণ্ডের মুক্ত সমপাশ্বীয় বান্ডলে গৌণ বৃদ্ধি সম্ভব হয় কারণ তাতে থাকে—",
        ["Only sclerenchyma", "Cambium between xylem and phloem", "Only leptocentric xylem", "No living cells"],
        ["কেবল স্ক্লেরেনকাইমা", "জাইলেম ও ফ্লোয়েমের মাঝে ক্যাম্বিয়াম", "কেবল লেপ্টোসেন্ট্রিক জাইলেম", "কোনো সজীব কোষ নেই"],
        "B", "easy", "factual",
        "Fascicular cambium between xylem and phloem, plus interfascicular cambium, forms a continuous cambium ring.",
        "জাইলেম-ফ্লোয়েমের মধ্যবর্তী ফ্যাসিকুলার ক্যাম্বিয়াম ও ইন্টারফ্যাসিকুলার ক্যাম্বিয়াম মিলে বলয় গঠন করে।",
    ),
    q(
        "Interfascicular cambium is an example of—",
        "ইন্টারফ্যাসিকুলার ক্যাম্বিয়াম কোনটির উদাহরণ?",
        ["Protoderm", "Primary apical meristem", "Secondary meristem", "Mass meristem only"],
        ["প্রোটোডার্ম", "প্রাইমারি শীর্ষ মেরিস্টেম", "সেকেন্ডারি ভাজক টিস্যু", "কেবল মাস মেরিস্টেম"],
        "C", "medium", "conceptual",
        "Interfascicular cambium arises from medullary-ray parenchyma and is secondary meristem.",
        "মজ্জারশ্মির প্যারেনকাইমা থেকে সৃষ্ট ইন্টারফ্যাসিকুলার ক্যাম্বিয়াম সেকেন্ডারি ভাজক।",
    ),
    q(
        "Secondary xylem is commonly called—",
        "সেকেন্ডারি জাইলেমকে সাধারণত কী বলে?",
        ["Bast", "Wood", "Cork", "Mesophyll"],
        ["বাস্ট", "কাঠ", "কর্ক", "মেসোফিল"],
        "B", "easy", "factual",
        "Secondary xylem produced inward by vascular cambium constitutes wood.",
        "ভাস্কুলার ক্যাম্বিয়াম ভিতরের দিকে সেকেন্ডারি জাইলেম (কাঠ) তৈরি করে।",
    ),
    q(
        "Secondary phloem is also known as—",
        "সেকেন্ডারি ফ্লোয়েমকে আর কী বলা হয়?",
        ["Wood", "Bast / inner bark component", "Pith", "Epiblema"],
        ["কাঠ", "বাস্ট / অন্তঃবাকল উপাদান", "মজ্জা", "এপিব্লেমা"],
        "B", "medium", "factual",
        "Cambium forms secondary phloem (bast) outward; together with cork it contributes to bark.",
        "ক্যাম্বিয়াম বাইরের দিকে সেকেন্ডারি ফ্লোয়েম (বাস্ট) তৈরি করে; এটি বাকলের অংশ।",
    ),
    q(
        "Cork cambium (phellogen) produces cork (phellem) toward the—",
        "কর্ক ক্যাম্বিয়াম (ফেলোজেন) কর্ক (ফেলেম) কোন দিকে তৈরি করে?",
        ["Toward the pith only", "Outward", "Only into the xylem", "Only into the phloem"],
        ["কেবল মজ্জার দিকে", "বাইরের দিকে", "কেবল জাইলেমের ভিতরে", "কেবল ফ্লোয়েমের ভিতরে"],
        "B", "medium", "factual",
        "Phellogen cuts off phellem outward and phelloderm inward; together they form periderm.",
        "ফেলোজেন বাইরে ফেলেম ও ভিতরে ফেলোডার্ম তৈরি করে; একত্রে পেরিডার্ম।",
    ),
    q(
        "Annual rings in a woody stem result mainly from activity of—",
        "কাষ্ঠল কাণ্ডে বার্ষিক বলয় প্রধানত কোনটির কার্যক্রমে সৃষ্টি হয়?",
        ["Apical meristem", "Vascular cambium", "Protoderm", "Root hair meristem"],
        ["শীর্ষস্থ ভাজক", "ভাস্কুলার ক্যাম্বিয়াম", "প্রোটোডার্ম", "মূলরোম মেরিস্টেম"],
        "B", "easy", "conceptual",
        "Seasonal variation in cambial activity produces earlywood and latewood, forming annual rings.",
        "ক্যাম্বিয়ামের ঋতুভিত্তিক কার্যক্রমে বসন্তকাষ্ঠ ও শরৎকাষ্ঠ মিলে বার্ষিক বলয় হয়।",
    ),
    q(
        "Which plant shows anomalous secondary growth among monocots?",
        "একবীজপত্রীদের মধ্যে কোনটিতে অস্বাভাবিক গৌণ বৃদ্ধি দেখা যায়?",
        ["Rice", "Wheat", "Dracaena", "Onion"],
        ["ধান", "গম", "ড্রাসিনা", "পেঁয়াজ"],
        "C", "medium", "factual",
        "Dracaena and Yucca show anomalous secondary growth via successive cambium-like rings.",
        "Dracaena ও Yucca-তে পর্যায়ক্রমিক ক্যাম্বিয়াম-সদৃশ কার্যক্রমে অস্বাভাবিক গৌণ বৃদ্ধি হয়।",
    ),
    q(
        "Heartwood differs from sapwood mainly because heartwood—",
        "অন্তঃকাঠ (hartwood) সরকাঠ (sapwood) থেকে প্রধানত আলাদা কারণ অন্তঃকাঠ—",
        [
            "Is the only living tissue",
            "Is non-conducting and often darker due to tannins/resins",
            "Contains only phloem",
            "Is produced by apical meristem alone",
        ],
        [
            "একমাত্র সজীব টিস্যু",
            "অপরিবাহী এবং প্রায়শই ট্যানিন/রেজিনে গাঢ় রঙের",
            "কেবল ফ্লোয়েম ধারণ করে",
            "কেবল শীর্ষ মেরিস্টেম থেকে তৈরি",
        ],
        "B", "medium", "conceptual",
        "Older secondary xylem becomes heartwood: vessels clogged, often impregnated, no longer conducts water.",
        "পুরাণো সেকেন্ডারি জাইলেম অন্তঃকাঠে পরিণত হয়ে অপরিবাহী ও প্রায়শই গাঢ় হয়।",
    ),
    q(
        "Lenticels are mainly associated with—",
        "লেন্টিসেল প্রধানত কোনটির সাথে সম্পর্কিত?",
        ["Primary root hairs", "Periderm of woody stems", "Only mesophyll chloroplasts", "Only closed monocot bundles"],
        ["প্রাইমারি মূলরোম", "কাষ্ঠল কাণ্ডের পেরিডার্ম", "কেবল মেসোফিল ক্লোরোপ্লাস্ট", "কেবল বদ্ধ একবীজপত্রী বান্ডল"],
        "B", "medium", "factual",
        "Lenticels are porous periderm regions allowing gas exchange after cork replaces epidermis.",
        "কর্ক গঠনের পর পেরিডার্মে লেন্টিসেল গ্যাস বিনিময়ে সাহায্য করে।",
    ),
    q(
        "During secondary growth in dicot stem, which tissue is pushed outward and often crushed?",
        "দ্বিবীজপত্রী কাণ্ডের গৌণ বৃদ্ধিতে কোন টিস্যু বাইরের দিকে চাপা পড়ে প্রায়শই বিপর্যস্ত হয়?",
        ["Secondary xylem", "Primary phloem", "Pith only", "Protoxylem only"],
        ["সেকেন্ডারি জাইলেম", "প্রাইমারি ফ্লোয়েম", "কেবল মজ্জা", "কেবল প্রোটোজাইলেম"],
        "B", "hard", "conceptual",
        "New secondary phloem and xylem displace primary phloem outward where it is often obliterated.",
        "নতুন গৌণ টিস্যু প্রাইমারি ফ্লোয়েমকে বাইরে ঠেলে প্রায়শই বিলুপ্ত করে।",
    ),
    q(
        "Which statement about dicot root secondary growth is correct?",
        "দ্বিবীজপত্রী মূলের গৌণ বৃদ্ধি সম্পর্কে কোনটি সঠিক?",
        [
            "Cambium arises as a complete ring from day one",
            "Conjunctive parenchyma and pericycle contribute to a wavy then circular cambium",
            "Only cork forms; no secondary xylem",
            "Bundles remain permanently closed",
        ],
        [
            "প্রথম দিন থেকেই সম্পূর্ণ বৃত্তাকার ক্যাম্বিয়াম থাকে",
            "কনজাংকটিভ প্যারেনকাইমা ও পেরিসাইকেল মিলে ঢেউখেলানো পরে বৃত্তাকার ক্যাম্বিয়াম গঠন করে",
            "কেবল কর্ক হয়; সেকেন্ডারি জাইলেম হয় না",
            "বান্ডল স্থায়ীভাবে বদ্ধ থাকে",
        ],
        "B", "hard", "conceptual",
        "In dicot roots, cambium patches form between xylem and phloem then join via pericycle opposite protoxylem.",
        "দ্বিবীজপত্রী মূলে জাইলেম-ফ্লোয়েমের মাঝে ক্যাম্বিয়াম প্যাচ ও পেরিসাইকেল মিলে বলয় সম্পূর্ণ হয়।",
    ),
    q(
        "Cuticle on aerial epidermis is mainly made of—",
        "কিউটিকল স্তর তৈরি হয় প্রধানত কী দিয়ে?",
        [
            "Cellulose and hemicellulose only",
            "Cellulose and pectin only",
            "Cutin (often with waxes)",
            "Lignin only",
        ],
        [
            "কেবল সেলুলোজ ও হেমিসেলুলোজ",
            "কেবল সেলুলোজ ও পেকটিন",
            "কিউটিন (প্রায়শই মোমসহ)",
            "কেবল লিগনিন",
        ],
        "C", "medium", "factual",
        "Cuticle is a cutinized protective layer reducing water loss; some texts also mention associated waxes/suberin in related coverings.",
        "কিউটিকল কিউটিনযুক্ত আবরণ যা পানি হ্রাস কমায়।",
    ),
    q(
        "Which region connects pericycle with the pith?",
        "পরিচক্র ও মজ্জার মধ্যে যোগাযোগ রক্ষা করা কার কাজ?",
        ["Cortex", "Endodermis alone", "Medullary ray", "Only stomata"],
        ["কর্টেক্স", "কেবল এন্ডোডার্মিস", "মজ্জারশ্মি", "কেবল পত্ররন্ধ্র"],
        "C", "medium", "factual",
        "Medullary rays are radial parenchyma bridges involved in lateral transport and storage, linking pith and outer regions.",
        "মজ্জারশ্মি মজ্জা ও বাইরের অঞ্চলের মধ্যে অরীয় সংযোগ ও সঞ্চয় করে।",
    ),
    q(
        "Functions of medullary rays include—(i) food storage (ii) radial transport of water and food (iii) some mechanical support",
        "মজ্জারশ্মির কাজ—(i) খাদ্য সঞ্চয় (ii) পানি ও খাদ্যের অরীয় পরিবহণ (iii) কিছু যান্ত্রিক শক্তি প্রদান",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "Rays store food, conduct radially, and contribute modest mechanical cohesion in the stem.",
        "মজ্জারশ্মি সঞ্চয়, অরীয় পরিবহণ ও আংশিক দৃঢ়তা প্রদান করে।",
    ),
    q(
        "In a dicot stem undergoing secondary growth, which bundle type is initially present?",
        "গৌণ বৃদ্ধিসম্পন্ন দ্বিবীজপত্রী কাণ্ডে প্রাথমিকভাবে কোন ধরনের বান্ডল থাকে?",
        ["Closed collateral", "Open collateral", "Only hadrocentric", "Only radial"],
        ["বদ্ধ সমপাশ্বীয়", "মুক্ত সমপাশ্বীয়", "কেবল হ্যাড্রোসেন্ট্রিক", "কেবল অরীয়"],
        "B", "easy", "factual",
        "Open collateral bundles with cambium are the starting point for ordinary stem secondary growth.",
        "ক্যাম্বিয়ামযুক্ত মুক্ত সমপাশ্বীয় বান্ডল থেকেই সাধারণ কাণ্ডের গৌণ বৃদ্ধি শুরু।",
    ),
    q(
        "Which extrastelar part is typically absent in a dicot root (mango root framing)?",
        "একটি আম গাছের মূলের বহিঃস্টিলীয় অঞ্চলে কোন অংশটি সাধারণত পাওয়া যাবে না?",
        ["Endodermis", "Epiblema", "Hypodermis", "Cortex"],
        ["অন্তস্ত্বক", "এপিব্লেমা", "অধস্ত্বক", "কর্টেক্স"],
        "C", "hard", "conceptual",
        "Dicot roots usually lack a distinct hypodermis; epiblema, cortex and endodermis are present.",
        "দ্বিবীজপত্রী মূলে সাধারণত সুস্পষ্ট হাইপোডার্মিস থাকে না।",
    ),
    q(
        "Which statements apply to endodermis? (i) called starch sheath in dicot stem (ii) has Casparian strips in root (iii) may have passage cells",
        "এন্ডোডার্মিসের ক্ষেত্রে প্রযোজ্য—(i) দ্বিবীজপত্রী কাণ্ডে স্টার্চ আবরণ বলে (ii) মূলে ক্যাসপেরিয়ান স্ট্রিপ থাকে (iii) প্যাসেজ কোষ থাকতে পারে",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "hard", "conceptual",
        "All three are standard HSC points about endodermis in stem vs root.",
        "দ্বিবীজপত্রী কাণ্ডে স্টার্চশীথ, মূলে ক্যাসপেরিয়ান স্ট্রিপ ও প্যাসেজ কোষ — তিনটিই প্রযোজ্য।",
    ),
    q(
        "Hard bast is located chiefly—",
        "হার্ডবাস্ট কোথায় অবস্থিত?",
        ["In the stele pith only", "In the cortex only", "On the outer side of phloem (phloem fibres)", "Inside protoxylem cavities only"],
        ["কেবল মজ্জায়", "কেবল কর্টেক্সে", "ফ্লোয়েমের বাইরের দিকে (ফ্লোয়েম ফাইবার)", "কেবল প্রোটোজাইলেম গহ্বরে"],
        "C", "hard", "factual",
        "Hard bast refers to sclerenchymatous phloem fibres lying peripheral to conducting phloem.",
        "হার্ডবাস্ট ফ্লোয়েম ফাইবার যা পরিবাহী ফ্লোয়েমের বাইরে দৃঢ়তা দেয়।",
    ),
]


TOPICS_MAP = {
    "bio1_27_ch08_t01": T01,
    "bio1_27_ch08_t02": T02,
    "bio1_27_ch08_t03": T03,
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
        "chapter": "bio1_27_ch08",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p245_pdf251.png",
            "p246_pdf252.png",
            "p247_pdf253.png",
            "p248_pdf254.png",
            "p249_pdf255.png",
            "p250_pdf256.png",
            "p251_pdf257.png",
            "p252_pdf258.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio1_27_ch08_t01": {
                "title": "Plant tissues / উদ্ভিদ টিস্যু",
                "themes": [
                    "meristem characters; isodiametric cells; permanent tissue maturity",
                    "mass/plate/rib meristems; endosperm; leaf expansion; medullary rays",
                    "protoderm→epidermis; procambium→xylem/phloem/cambium (not cortex)",
                    "living xylem parenchyma; fibres in both xylem and phloem",
                    "secondary meristem cambium; promeristem origin; apical buds",
                    "collenchyma flexible support; ground meristem products",
                ],
            },
            "bio1_27_ch08_t02": {
                "title": "Tissue systems / টিস্যুতন্ত্র",
                "themes": [
                    "sunken stomata Nerium; hydathode epithem; guard vs subsidiary chloroplast",
                    "Casparian strip; anisocytic/anomocytic stomata; mesophyll; hydathode on leaf",
                    "hadrocentric Pteris/Selaginella; leptocentric Dracaena; rice closed collateral",
                    "pumpkin bicollateral; radial bundles in root; epiblema",
                    "stele vs extrastelar; monocot stem cuticle/scattered/conjoint; V/Y xylem",
                    "passage cells; monocot root radial identifier",
                ],
            },
            "bio1_27_ch08_t03": {
                "title": "Secondary growth / গৌণ বৃদ্ধি",
                "themes": [
                    "lateral meristem girth; closed monocot bundles lack ordinary SG",
                    "open collateral + fascicular/interfascicular cambium ring",
                    "secondary xylem=wood; secondary phloem=bast; cork cambium polarity",
                    "annual rings; Dracaena anomalous SG; heartwood vs sapwood; lenticels",
                    "primary phloem crushed; dicot root cambium formation",
                    "cuticle cutin; medullary ray roles; dicot root no hypodermis; endodermis triad; hard bast",
                ],
            },
        },
        "low_confidence": [
            "OCR on p245–252 is noisy; many figure-stimulus items rewritten as standalone named stems.",
            "Cuticle composition keyed to cutin (with waxes); some board keys list cutin+pectin/suberin variants.",
            "Hard bast location framed as peripheral phloem fibres per common HSC notes.",
            "Monocot-root identifier item stresses radial bundles; avoid confusing with stem Y-xylem distractors.",
            "Secondary-growth topic supplements OCR-light SG coverage with accurate board-level anatomy.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio1_27_ch08_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio1_27_ch08_t01": 20,
                "bio1_27_ch08_t02": 20,
                "bio1_27_ch08_t03": 20,
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
        / "ch08_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
