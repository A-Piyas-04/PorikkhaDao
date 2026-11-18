#!/usr/bin/env python3
"""Seed Biology 1st Paper Ch2 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio1_27_ch02_t01..t03 (cell cycle; mitosis; meiosis).
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
    "biology p1 ch02; curated bilingual"
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


# --- t01: Cell cycle / কোষচক্র ---
T01 = [
    q(
        "In G1 of the cell cycle: (i) proteins and RNA are synthesized (ii) DNA is replicated (iii) about 30–40% of cycle time is spent. Which is correct?",
        "কোষ চক্রের G1-এ: (i) প্রোটিন ও RNA সংশ্লেষিত হয় (ii) DNA অনুলিপন ঘটে (iii) প্রায় ৩০–৪০% সময় ব্যয় হয়। কোনটি সঠিক?",
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
        "G1 synthesizes proteins/RNA and takes ~30–40% of cycle time; DNA replication is in S, not G1.",
        "G1-এ প্রোটিন ও RNA সংশ্লেষ হয় এবং চক্রের প্রায় ৩০–৪০% সময় ব্যয় হয়; DNA অনুলিপন S দশায় ঘটে, G1-এ নয়।",
    ),
    q(
        "In which phase of the cell cycle does DNA synthesis occur?",
        "কোষ চক্রের কোন পর্যায়ে DNA সংশ্লেষণ ঘটে?",
        ["G1", "S", "G2", "M"],
        ["G1", "S", "G2", "M"],
        "B", "easy", "factual",
        "DNA replication occurs in the S (synthesis) phase.",
        "DNA প্রতিলিপন সংশ্লেষণ বা S দশায় ঘটে।",
    ),
    q(
        "Time spent in the synthesis (S) phase of the cell cycle is about:",
        "কোষ চক্রের সংশ্লেষণ (S) দশায় ব্যয়িত সময় প্রায়:",
        ["10–20%", "30–40%", "30–50%", "90–95%"],
        ["১০–২০%", "৩০–৪০%", "৩০–৫০%", "৯০–৯৫%"],
        "C", "easy", "factual",
        "In the standard Udvash/board table, S phase occupies about 30–50% of the cell cycle.",
        "উদ্ভাস/বোর্ড সারণি অনুসারে S দশায় প্রায় ৩০–৫০% সময় ব্যয় হয়।",
    ),
    q(
        "Time spent in the G1 phase of the cell cycle is about:",
        "কোষ চক্রের G1 (বিরাম-১) দশায় ব্যয়িত সময় প্রায়:",
        ["10–20%", "30–40%", "30–50%", "90–95%"],
        ["১০–২০%", "৩০–৪০%", "৩০–৫০%", "৯০–৯৫%"],
        "B", "easy", "factual",
        "G1 typically occupies about 30–40% of the cell cycle.",
        "G1 দশায় সাধারণত প্রায় ৩০–৪০% সময় ব্যয় হয়।",
    ),
    q(
        "Time spent in the G2 phase of the cell cycle is about:",
        "কোষ চক্রের G2 দশায় ব্যয়িত সময় প্রায়:",
        ["5–10%", "10–20%", "30–40%", "30–50%"],
        ["৫–১০%", "১০–২০%", "৩০–৪০%", "৩০–৫০%"],
        "B", "easy", "factual",
        "G2 occupies about 10–20% of the cell cycle in the printed bank table.",
        "মুদ্রিত সারণি অনুসারে G2 দশায় প্রায় ১০–২০% সময় ব্যয় হয়।",
    ),
    q(
        "Histone proteins are synthesized mainly in which cell-cycle phase?",
        "হিস্টোন প্রোটিন সংশ্লেষ হয় কোষ চক্রের কোন দশায়?",
        ["G1 phase", "G2 phase", "S phase", "M phase"],
        ["G1 দশা", "G2 দশা", "S দশা", "M দশা"],
        "C", "medium", "factual",
        "Histones are produced during S phase alongside DNA replication for chromatin assembly.",
        "DNA অনুলিপনের সাথে মিল রেখে হিস্টোন প্রধানত S দশায় সংশ্লেষিত হয়।",
    ),
    q(
        "The nucleus of which stage is called the metabolic nucleus?",
        "কোন ধাপের নিউক্লিয়াসকে বিপাকীয় নিউক্লিয়াস বলে?",
        ["Prophase", "Interphase", "Metaphase", "Prometaphase"],
        ["প্রোফেজ", "ইন্টারফেজ", "মেটাফেজ", "প্রোমেটাফেজ"],
        "B", "easy", "factual",
        "During interphase the nucleus is metabolically active (growth, transcription, preparation).",
        "ইন্টারফেজে নিউক্লিয়াস বিপাকীয়ভাবে সক্রিয় থাকে বলে একে বিপাকীয় নিউক্লিয়াস বলে।",
    ),
    q(
        "In which sub-stage does DNA replication occur?",
        "কোন উপ-পর্যায়ে DNA অনুলিপন ঘটে?",
        ["Interphase", "Prophase", "Metaphase", "Telophase"],
        ["ইন্টারফেজ", "প্রোফেজ", "মেটাফেজ", "টেলোফেজ"],
        "A", "easy", "factual",
        "DNA replication is completed in interphase (specifically S phase) before mitosis.",
        "মাইটোসিসের আগে ইন্টারফেজের (S দশা) মধ্যে DNA অনুলিপন সম্পন্ন হয়।",
    ),
    q(
        "What is genetically controlled cell death called?",
        "জেনেটিকালি নিয়ন্ত্রিত কোষ মৃত্যুকে কী বলে?",
        ["Meiosis", "Mitosis", "Necrosis", "Apoptosis"],
        ["মিয়োসিস", "মাইটোসিস", "নেক্রোসিস", "অ্যাপোপটোসিস"],
        "D", "easy", "factual",
        "Apoptosis is programmed (genetically controlled) cell death.",
        "অ্যাপোপটোসিস হলো জেনেটিকভাবে নিয়ন্ত্রিত প্রোগ্রামড কোষমৃত্যু।",
    ),
    q(
        "Cell death due to nutrient deficiency (or toxins) is called:",
        "পুষ্টির অভাবজনিত (বা বিষাক্ততার) কোষের মৃত্যুকে কী বলে?",
        ["Apoptosis", "Toxicosis", "Neutrotopsis", "Necrosis"],
        ["অ্যাপোপটোসিস", "টক্সিকটোসিস", "নিউট্রোটপসিস", "নেক্রোসিস"],
        "D", "easy", "factual",
        "Necrosis is unplanned cell death from injury, toxins, or nutrient lack; apoptosis is programmed.",
        "নেক্রোসিস আঘাত/বিষ/পুষ্টির অভাবে অপরিকল্পিত মৃত্যু; অ্যাপোপটোসিস প্রোগ্রামড মৃত্যু।",
    ),
    q(
        "In interkinesis: (i) protein synthesis occurs (ii) DNA replication occurs (iii) necessary RNA is made. Which is correct?",
        "ইন্টারকাইনেসিসে: (i) প্রোটিন সংশ্লেষ ঘটে (ii) DNA অনুলিপন ঘটে (iii) প্রয়োজনীয় RNA তৈরি হয়। কোনটি সঠিক?",
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
        "Interkinesis has protein and needed RNA synthesis, but no DNA replication.",
        "ইন্টারকাইনেসিসে প্রোটিন ও প্রয়োজনীয় RNA তৈরি হয়, কিন্তু DNA অনুলিপন হয় না।",
    ),
    q(
        "In G2 of the cell cycle: (i) nuclear volume increases (ii) DNA is synthesized (iii) about 10–20% of time is spent. Which is correct?",
        "কোষ চক্রের G2-এ: (i) নিউক্লিয়াসের আয়তন বাড়ে (ii) DNA সংশ্লেষ হয় (iii) প্রায় ১০–২০% সময় ব্যয় হয়। কোনটি সঠিক?",
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
        "G2: nuclear volume may increase and ~10–20% time is spent; DNA synthesis is not in G2.",
        "G2-এ নিউক্লিয়াসের আয়তন বাড়তে পারে ও প্রায় ১০–২০% সময় ব্যয় হয়; DNA সংশ্লেষ G2-এ হয় না।",
    ),
    q(
        "About what fraction of the cell cycle is the mitotic (M) phase?",
        "কোষ চক্রের মাইটোটিক (M) দশায় প্রায় কত সময় ব্যয় হয়?",
        ["5–10%", "30–40%", "30–50%", "90–95%"],
        ["৫–১০%", "৩০–৪০%", "৩০–৫০%", "৯০–৯৫%"],
        "A", "easy", "factual",
        "Printed cell-cycle pie tables list the mitotic phase as about 5–10%.",
        "মুদ্রিত কোষচক্র সারণিতে M দশা প্রায় ৫–১০%।",
    ),
    q(
        "In a standard cell-cycle diagram (G1–S–G2–M), DNA molecule replication occurs in:",
        "মানক কোষচক্র চিত্রে (G1–S–G2–M) DNA অণুর রেপ্লিকেশন ঘটে:",
        ["G1 only", "G2 only", "S phase", "M phase only"],
        ["কেবল G1", "কেবল G2", "S দশা", "কেবল M দশা"],
        "C", "easy", "factual",
        "Replication is confined to S phase between the two gap phases.",
        "দুই গ্যাপ দশার মাঝের S দশায়ই রেপ্লিকেশন সীমাবদ্ধ।",
    ),
    q(
        "Which statement set about interphase events is correct?",
        "ইন্টারফেজ দশায় কোন সেট সঠিক?",
        [
            "DNA replication, microtubule preparation, and ATP production occur across interphase subphases",
            "Only spindle fibers fully separate chromatids throughout G1",
            "Only cytokinesis completes before S begins",
            "Only crossing over occurs in G2",
        ],
        [
            "ইন্টারফেজের উপদশাগুলোতে DNA প্রতিলিপন, মাইক্রোটিউবিউল প্রস্তুতি ও ATP উৎপাদন ঘটে",
            "কেবল G1 জুড়ে স্পিন্ডল তন্তু ক্রোমাটিড আলাদা করে",
            "কেবল S শুরুর আগেই সাইটোকাইনেসিস শেষ হয়",
            "কেবল G2-এ ক্রসিংওভার ঘটে",
        ],
        "A", "medium", "conceptual",
        "G1/S/G2 cover DNA/RNA/protein work, microtubule initiation, and ATP store for mitosis.",
        "G1/S/G2-এ DNA–RNA–প্রোটিন কাজ, মাইক্রোটিউবিউল সূচনা ও মাইটোসিসের জন্য ATP মজুদ হয়।",
    ),
    q(
        "Cyclin proteins associated with preparing for mitosis are produced mainly around:",
        "মাইটোসিসের প্রস্তুতির সাথে সম্পর্কিত সাইক্লিন প্রোটিন প্রধানত তৈরি হয়:",
        ["Late G2 / pre-mitotic gap", "Only anaphase of meiosis I", "Only leptotene", "Only cytokinesis of plants"],
        ["অন্তিম G2 / মাইটোসিস-পূর্ব গ্যাপ", "কেবল মিয়োসিস-১ এর অ্যানাফেজ", "কেবল লেপ্টোটিন", "কেবল উদ্ভিদের সাইটোকাইনেসিস"],
        "A", "hard", "conceptual",
        "Board items link cyclin buildup in the late gap before M for orderly entry into mitosis.",
        "বোর্ড প্রশ্নে M-এর আগের গ্যাপে সাইক্লিন জমা হয়ে মাইটোসিসে প্রবেশ নিয়ন্ত্রণ করে।",
    ),
    q(
        "Which is a defining feature of the cell cycle as a whole?",
        "কোষ চক্রের সামগ্রিক বৈশিষ্ট্য কোনটি?",
        [
            "Ordered progression through interphase and M with checkpoints",
            "Only random chromosome loss each hour",
            "Only meiosis in every somatic skin cell",
            "Only necrosis in every G1 cell",
        ],
        [
            "চেকপয়েন্টসহ ইন্টারফেজ ও M-এর সুবিন্যস্ত অগ্রগতি",
            "প্রতি ঘণ্টায় কেবল এলোমেলো ক্রোমোজোম ক্ষয়",
            "প্রতিটি দেহকোষে কেবল মিয়োসিস",
            "প্রতিটি G1 কোষে কেবল নেক্রোসিস",
        ],
        "A", "easy", "conceptual",
        "The cell cycle is a regulated sequence (G1–S–G2–M) ensuring faithful duplication and division.",
        "কোষ চক্র নিয়ন্ত্রিত ক্রম (G1–S–G2–M) যা সঠিক অনুলিপন ও বিভাজন নিশ্চিত করে।",
    ),
    q(
        "Abnormal cell-cycle control most directly tends to:",
        "কোষ চক্রের অস্বাভাবিক নিয়ন্ত্রণ সবচেয়ে সরাসরি:",
        [
            "Hinder normal growth and can promote uncontrolled division",
            "Always create healthy gametes only",
            "Always stop all transcription forever",
            "Always convert necrosis into synapsis",
        ],
        [
            "স্বাভাবিক বৃদ্ধি বাধাগ্রস্ত করে এবং অনিয়ন্ত্রিত বিভাজন ঘটাতে পারে",
            "সবসময় কেবল সুস্থ গ্যামেট তৈরি করে",
            "সবসময় চিরতরে সব ট্রান্সক্রিপশন বন্ধ করে",
            "সবসময় নেক্রোসিসকে সিন্যাপসিসে রূপান্তর করে",
        ],
        "A", "medium", "conceptual",
        "Printed items note that cycle abnormalities hinder normal growth (and underlie proliferative disorders).",
        "মুদ্রিত প্রশ্নে চক্রের অস্বাভাবিকতা স্বাভাবিক বৃদ্ধি বাধাগ্রস্ত করে বলে উল্লেখ আছে।",
    ),
    q(
        "Which phase prepares the cell for mitosis after DNA has already been copied?",
        "DNA অনুলিপনের পর মাইটোসিসের জন্য কোন দশা কোষকে প্রস্তুত করে?",
        ["G1", "S", "G2", "Only cytokinesis without G2"],
        ["G1", "S", "G2", "G2 ছাড়া কেবল সাইটোকাইনেসিস"],
        "C", "easy", "conceptual",
        "After S, G2 checks DNA, builds microtubules/ATP, then M begins.",
        "S-এর পর G2-এ DNA যাচাই, মাইক্রোটিউবিউল/ATP তৈরি হয়ে M শুরু হয়।",
    ),
    q(
        "Which pair correctly matches phase and major event?",
        "কোন জোড়া দশা ও প্রধান ঘটনার সঠিক মিল?",
        [
            "S — DNA replication; G1 — growth with RNA/protein synthesis",
            "G1 — crossing over; S — cytokinesis only",
            "G2 — synapsis of homologues; M — DNA replication",
            "M — histone synthesis only; S — necrosis only",
        ],
        [
            "S — DNA অনুলিপন; G1 — RNA/প্রোটিন সংশ্লেষসহ বৃদ্ধি",
            "G1 — ক্রসিংওভার; S — কেবল সাইটোকাইনেসিস",
            "G2 — হোমোলোগের সিন্যাপসিস; M — DNA অনুলিপন",
            "M — কেবল হিস্টোন সংশ্লেষ; S — কেবল নেক্রোসিস",
        ],
        "A", "medium", "conceptual",
        "Standard mapping: G1 growth/macromolecules, S DNA (+ histones), G2 preparation, M division.",
        "মানক মিল: G1 বৃদ্ধি/ম্যাক্রোমলিকিউল, S-এ DNA (+হিস্টোন), G2 প্রস্তুতি, M বিভাজন।",
    ),
]


# --- t02: Mitosis / মাইটোসিস ---
T02 = [
    q(
        "Arrangement of chromosomes at the equatorial plane of the spindle is called:",
        "স্পিন্ডল যন্ত্রের বিষুবীয় তলে ক্রোমোজোমের বিন্যস্ত হওয়াকে বলে:",
        ["Cytokinesis", "Karyokinesis", "Metakinesis", "Interkinesis"],
        ["সাইটোকাইনেসিস", "ক্যারিওকাইনেসিস", "মেটাকাইনেসিস", "ইন্টারকাইনেসিস"],
        "C", "easy", "factual",
        "Metakinesis refers to metaphase alignment of chromosomes at the equator.",
        "মেটাকাইনেসিস হলো মেটাফেজে বিষুবরেখায় ক্রোমোজোম সাজানো।",
    ),
    q(
        "In which stage of mitosis does the nuclear membrane completely disappear?",
        "মাইটোসিসের কোন ধাপে নিউক্লিয়ার মেমব্রেন সম্পূর্ণরূপে বিলুপ্ত হয়?",
        ["Prophase", "Prometaphase", "Metaphase", "Anaphase"],
        ["প্রোফেজ", "প্রোমেটাফেজ", "মেটাফেজ", "অ্যানাফেজ"],
        "B", "medium", "factual",
        "Board keys place complete nuclear-envelope breakdown in prometaphase.",
        "বোর্ড উত্তরমালা অনুসারে নিউক্লিয়ার আবরণের সম্পূর্ণ বিলুপ্তি প্রোমেটাফেজে।",
    ),
    q(
        "Which is applicable to mitosis?",
        "মাইটোসিসের ক্ষেত্রে কোনটি প্রযোজ্য?",
        [
            "It occurs only in meiocytes as reduction division",
            "It always creates new allelic diversity like crossing over",
            "It can increase the number of germ cells before meiosis",
            "It occurs only in haploid zygotes of all plants",
        ],
        [
            "কেবল মিয়োসাইটে হ্রাস বিভাজন হিসেবে ঘটে",
            "সবসময় ক্রসিংওভারের মতো নতুন অ্যালিল বৈচিত্র্য আনে",
            "মিয়োসিসের আগে জনন কোষের সংখ্যা বৃদ্ধি করতে পারে",
            "সব উদ্ভিদের কেবল হ্যাপ্লয়েড জাইগোটে ঘটে",
        ],
        "C", "medium", "conceptual",
        "Printed key: mitosis multiplies germ-line cells; it is not reductional and lacks crossing over.",
        "মুদ্রিত চাবি: মাইটোসিস জনন কোষের সংখ্যা বাড়ায়; এটি হ্রাসমূলক নয় এবং ক্রসিংওভারহীন।",
    ),
    q(
        "In which stage of mitosis does the cell plate begin to form (plant cells)?",
        "মাইটোসিসের কোন ধাপে কোষ প্লেটের গঠন শুরু হয়?",
        ["Prophase", "Prometaphase", "Anaphase", "Telophase"],
        ["প্রোফেজ", "প্রোমেটাফেজ", "অ্যানাফেজ", "টেলোফেজ"],
        "D", "medium", "factual",
        "Cell-plate formation starts in telophase as cytokinesis proceeds in plant cells.",
        "উদ্ভিদ কোষে টেলোফেজ থেকে কোষ প্লেট গঠন শুরু হয়ে সাইটোকাইনেসিস এগোয়।",
    ),
    q(
        "Spindle fibers disappear in which mitotic stage?",
        "মাইটোসিসের কোন ধাপে স্পিন্ডল তন্তু লুপ্ত হয়?",
        ["Prometaphase", "Metaphase", "Anaphase", "Telophase"],
        ["প্রোমেটাফেজ", "মেটাফেজ", "অ্যানাফেজ", "টেলোফেজ"],
        "D", "easy", "factual",
        "The spindle apparatus disassembles in telophase as nuclei reform.",
        "টেলোফেজে নিউক্লিয়াস পুনর্গঠনের সময় স্পিন্ডল যন্ত্র বিলুপ্ত হয়।",
    ),
    q(
        "Which stage is called the movement stage?",
        "কোনটিকে গতি পর্যায় বলা হয়?",
        ["Prophase", "Metaphase", "Anaphase", "Telophase"],
        ["প্রোফেজ", "মেটাফেজ", "অ্যানাফেজ", "টেলোফেজ"],
        "C", "easy", "factual",
        "Anaphase is the movement stage: chromatids/chromosomes move to poles.",
        "অ্যানাফেজ গতি পর্যায়—ক্রোমাটিড/ক্রোমোজোম মেরুর দিকে সরে।",
    ),
    q(
        "If 2n = 8, how many chromatids are seen at mitotic metaphase?",
        "যদি 2n = 8 হয়, মাইটোসিস মেটাফেজ দশায় মোট কতটি ক্রোমাটিড দেখা যায়?",
        ["4", "8", "16", "24"],
        ["৪", "৮", "১৬", "২৪"],
        "C", "medium", "numerical",
        "Each of 8 chromosomes has 2 chromatids → 16 chromatids at metaphase.",
        "৮টি ক্রোমোজোমের প্রত্যেকটিতে ২টি ক্রোমাটিড → মেটাফেজে ১৬টি ক্রোমাটিড।",
    ),
    q(
        "Division of the nucleus is called:",
        "নিউক্লিয়াসের বিভাজনকে কী বলে?",
        ["Karyokinesis", "Metakinesis", "Diakinesis", "Cytokinesis"],
        ["ক্যারিওকাইনেসিস", "মেটাকাইনেসিস", "ডায়াকাইনেসিস", "সাইটোকাইনেসিস"],
        "A", "easy", "factual",
        "Karyokinesis = nuclear division; cytokinesis = cytoplasmic division.",
        "ক্যারিওকাইনেসিস = নিউক্লিয়াস বিভাজন; সাইটোকাইনেসিস = সাইটোপ্লাজম বিভাজন।",
    ),
    q(
        "Division of the cytoplasm is called:",
        "সাইটোপ্লাজমের বিভাজনকে কী বলে?",
        ["Karyokinesis", "Cytokinesis", "Metakinesis", "Diakinesis"],
        ["ক্যারিওকাইনেসিস", "সাইটোকাইনেসিস", "মেটাকাইনেসিস", "ডায়াকাইনেসিস"],
        "B", "easy", "factual",
        "Cytokinesis partitions cytoplasm and usually completes cell number increase.",
        "সাইটোকাইনেসিস সাইটোপ্লাজম ভাগ করে সাধারণত কোষসংখ্যা বৃদ্ধি সম্পন্ন করে।",
    ),
    q(
        "In which mitotic stage is the spindle apparatus fully formed?",
        "মাইটোসিসের কোন ধাপে স্পিন্ডল যন্ত্র পূর্ণাঙ্গ হয়?",
        ["Prophase", "Prometaphase", "Metaphase", "Anaphase"],
        ["প্রোফেজ", "প্রোমেটাফেজ", "মেটাফেজ", "অ্যানাফেজ"],
        "B", "medium", "factual",
        "Spindle initiation may start in prophase, but the apparatus is completed in prometaphase (printed explanation).",
        "স্পিন্ডল সূচনা প্রোফেজে হতে পারে, কিন্তু যন্ত্র প্রোমেটাফেজে সম্পূর্ণ হয় (মুদ্রিত ব্যাখ্যা)।",
    ),
    q(
        "Shortening and thickening of chromosomes is called:",
        "ক্রোমোসোমের খাটো ও মোটা হওয়াকে বলে:",
        ["Synapsis", "Bivalent", "Apoptosis", "Condensation"],
        ["সিন্যাপসিস", "বাইভ্যালেন্ট", "অ্যাপোপটোসিস", "কনডেনসেশন"],
        "D", "easy", "factual",
        "Chromosome condensation packs chromatin into short, thick mitotic chromosomes.",
        "কনডেনসেশনে ক্রোমাটিন খাটো-মোটা মাইটোটিক ক্রোমোসোমে প্যাক হয়।",
    ),
    q(
        "In mitotic anaphase, a metacentric chromosome appears like which letter?",
        "মাইটোসিস অ্যানাফেজে মেটাসেন্ট্রিক ক্রোমোসোম কোন অক্ষরের আকৃতি দেখায়?",
        ["V", "J", "L", "I"],
        ["V", "J", "L", "I"],
        "A", "medium", "factual",
        "Metacentric chromosomes pulled at a median centromere look V-shaped in anaphase.",
        "মধ্যস্থ সেন্ট্রোমিয়ারে টানা মেটাসেন্ট্রিক ক্রোমোসোম অ্যানাফেজে V-আকৃতির।",
    ),
    q(
        "In anaphase, a sub-metacentric chromosome typically looks like:",
        "অ্যানাফেজে সাব-মেটাসেন্ট্রিক ক্রোমোসোম সাধারণত কোন আকৃতি ধরে?",
        ["I", "J", "L", "V"],
        ["I", "J", "L", "V"],
        "C", "medium", "factual",
        "Unequal arms of submetacentrics give an L-like appearance in anaphase (printed key).",
        "সাবমেটাসেন্ট্রিকের অসম বাহু অ্যানাফেজে L-সদৃশ দেখায় (মুদ্রিত চাবি)।",
    ),
    q(
        "Chromatids move toward opposite poles in:",
        "ক্রোমাটিড বিপরীত মেরুর দিকে সরে কোন ধাপে?",
        ["Prophase", "Metaphase", "Anaphase", "Telophase"],
        ["প্রোফেজ", "মেটাফেজ", "অ্যানাফেজ", "টেলোফেজ"],
        "C", "easy", "factual",
        "Sister chromatids separate and migrate in anaphase.",
        "অ্যানাফেজে সিস্টার ক্রোমাটিড আলাদা হয়ে মেরুমুখী যায়।",
    ),
    q(
        "In which mitotic stage do chromosomes look like various letter shapes?",
        "মাইটোসিসের কোন পর্যায়ে ক্রোমোসোমগুলো বিভিন্ন অক্ষরের মতো দেখায়?",
        ["Prophase", "Metaphase", "Anaphase", "Telophase"],
        ["প্রোফেজ", "মেটাফেজ", "অ্যানাফেজ", "টেলোফেজ"],
        "C", "easy", "factual",
        "Anaphase shapes (V, J, L, I) reflect centromere position while chromosomes move poleward.",
        "অ্যানাফেজের V/J/L/I আকৃতি সেন্ট্রোমিয়ার অবস্থান ও মেরুমুখী চলন নির্দেশ করে।",
    ),
    q(
        "Cytokinesis involves: (i) nuclear division (ii) cytoplasmic division (iii) increase in cell number. Which is correct?",
        "সাইটোকাইনেসিসে: (i) নিউক্লিয়াসের বিভাজন (ii) সাইটোপ্লাজমের বিভাজন (iii) কোষের সংখ্যা বৃদ্ধি। কোনটি সঠিক?",
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
        "C", "medium", "conceptual",
        "Cytokinesis is cytoplasmic division that increases cell number; nuclear division is karyokinesis.",
        "সাইটোকাইনেসিস সাইটোপ্লাজম ভাগ করে কোষসংখ্যা বাড়ায়; নিউক্লিয়াস ভাগ ক্যারিওকাইনেসিস।",
    ),
    q(
        "Chromosomal dance is characteristically associated with:",
        "ক্রোমোজোমীয় নৃত্য বৈশিষ্ট্যগতভাবে কোন পর্যায়ের সাথে যুক্ত?",
        ["Prometaphase", "Metaphase", "Anaphase", "Telophase"],
        ["প্রোমেটাফেজ", "মেটাফেজ", "অ্যানাফেজ", "টেলোফেজ"],
        "B", "medium", "factual",
        "Many board/Udvash items place chromosomal dance at metaphase (equatorial jostling before anaphase).",
        "অনেক বোর্ড/উদ্ভাস আইটেমে ক্রোমোজোমীয় নৃত্য মেটাফেজের বিষুবীয় সজ্জার সাথে যুক্ত।",
    ),
    q(
        "Centromere division in mitosis occurs at:",
        "মাইটোসিসে সেন্ট্রোমিয়ার বিভাজন ঘটে:",
        ["Prometaphase", "Metaphase only without separation", "Anaphase", "Telophase"],
        ["প্রোমেটাফেজ", "বিভাজনহীন কেবল মেটাফেজ", "অ্যানাফেজ", "টেলোফেজ"],
        "C", "medium", "factual",
        "Sister chromatids separate when centromeres split at the start of anaphase.",
        "অ্যানাফেজের শুরুতে সেন্ট্রোমিয়ার বিভক্ত হয়ে সিস্টার ক্রোমাটিড আলাদা হয়।",
    ),
    q(
        "Formation of the cell wall middle lamella begins from which stage?",
        "কোষপ্রাচীরের মধ্যপর্দার গঠন প্রক্রিয়া কোন দশা থেকে শুরু হয়?",
        ["Prophase", "Telophase", "Metaphase", "Anaphase"],
        ["প্রোফেজ", "টেলোফেজ", "মেটাফেজ", "অ্যানাফেজ"],
        "B", "medium", "factual",
        "Middle-lamella/cell-plate deposition begins in telophase of plant mitosis.",
        "উদ্ভিদ মাইটোসিসের টেলোফেজ থেকে মধ্যপর্দা/কোষ প্লেট জমা শুরু হয়।",
    ),
    q(
        "Furrowing of the plasma membrane in animal cytokinesis depends mainly on:",
        "প্রাণী সাইটোকাইনেসিসে প্লাজমা মেমব্রেনের খাঁজ সৃষ্টিতে প্রধানত দায়ী:",
        [
            "Actin and myosin",
            "Actin and niacin only",
            "Myosin and niacin only",
            "Actin and cytosine only",
        ],
        [
            "অ্যাকটিন ও মায়োসিন",
            "কেবল অ্যাকটিন ও নায়াসিন",
            "কেবল মায়োসিন ও নায়াসিন",
            "কেবল অ্যাকটিন ও সাইটোসিন",
        ],
        "A", "medium", "factual",
        "A contractile ring of actin and myosin pinches the animal cell membrane.",
        "অ্যাকটিন–মায়োসিন সংকোচন বলয় প্রাণী কোষঝিল্লিতে খাঁজ তৈরি করে।",
    ),
]


# --- t03: Meiosis / মিয়োসিস ---
T03 = [
    q(
        "Synapsis occurs in which sub-stage?",
        "সিন্যাপসিস ঘটে কোন উপপর্যায়ে?",
        ["Leptotene", "Zygotene", "Pachytene", "Diplotene"],
        ["লেপ্টোটিন", "জাইগোটিন", "প্যাকাইটিন", "ডিপ্লোটিন"],
        "B", "easy", "factual",
        "Homologous pairing (synapsis) occurs in zygotene of prophase I.",
        "প্রোফেজ-১ এর জাইগোটিনে হোমোলোগাস জোড় বাঁধা (সিন্যাপসিস) ঘটে।",
    ),
    q(
        "Where does meiosis occur in a rice (paddy) plant?",
        "ধান গাছের কোথায় মিয়োসিস ঘটে?",
        ["Zygote", "Somatic body cell", "Germ mother cell", "Mature gamete only"],
        ["জাইগোট", "দেহকোষ", "জনন মাতৃকোষ", "কেবল পরিণত গ্যামেট"],
        "C", "easy", "factual",
        "Rice is sporophytic; meiosis occurs in diploid germ mother cells (meiocytes).",
        "ধান স্পোরোফাইটিক; ডিপ্লয়েড জনন মাতৃকোষে (মিয়োসাইট) মিয়োসিস ঘটে।",
    ),
    q(
        "In which sub-stage of meiosis does crossing over occur?",
        "মিয়োসিসের কোন উপ-পর্যায়ে ক্রসিংওভার ঘটে?",
        ["Zygotene", "Pachytene", "Diplotene", "Diakinesis"],
        ["জাইগোটিন", "প্যাকাইটিন", "ডিপ্লোটিন", "ডায়াকাইনেসিস"],
        "B", "easy", "factual",
        "Crossing over between non-sister chromatids occurs in pachytene.",
        "প্যাকাইটিনে নন-সিস্টার ক্রোমাটিডের মধ্যে ক্রসিংওভার ঘটে।",
    ),
    q(
        "In which stage of cell division is the tetrad formed?",
        "কোষ বিভাজনের কোন দশায় টেট্রাড অবস্থা তৈরি হয়?",
        ["Pachytene", "Leptotene", "Diakinesis", "Synapsis only as a stage name"],
        ["প্যাকাইটিন", "লেপ্টোটিন", "ডায়াকাইনেসিস", "কেবল সিন্যাপসিস নামক দশা"],
        "A", "medium", "factual",
        "A tetrad (four chromatids of a bivalent) is clear in pachytene.",
        "বাইভ্যালেন্টের চার ক্রোমাটিডের টেট্রাড প্যাকাইটিনে স্পষ্ট।",
    ),
    q(
        "Who first developed the concept of crossing over?",
        "ক্রসিংওভার সম্পর্কে সর্বপ্রথম ধারণা কে দেন?",
        [
            "Thomas Hunt Morgan",
            "James Watson",
            "Gregor Johann Mendel",
            "Strasburger",
        ],
        [
            "থমাস হান্ট মর্গান",
            "জেমস ওয়াটসন",
            "গ্রেগর জোহান মেন্ডেল",
            "স্ট্রাসবার্জার",
        ],
        "A", "easy", "factual",
        "T. H. Morgan established the concept of crossing over in genetics.",
        "থমাস হান্ট মর্গান জিনেটিক্সে ক্রসিংওভারের ধারণা প্রতিষ্ঠা করেন।",
    ),
    q(
        "Pairing of homologous chromosomes is called:",
        "হোমোলোগাস ক্রোমোসোমের জোড় বাঁধার প্রক্রিয়াকে কী বলে?",
        ["Bivalent", "Synapsis", "Tetrad", "Chiasma"],
        ["বাইভ্যালেন্ট", "সিন্যাপসিস", "টেট্রাড", "কায়াজমা"],
        "B", "easy", "factual",
        "The pairing process is synapsis; the paired structure is a bivalent.",
        "জোড় বাঁধার প্রক্রিয়া সিন্যাপসিস; জোড়া কাঠামো বাইভ্যালেন্ট।",
    ),
    q(
        "Meiosis plays a role in:",
        "মিয়োসিস ভূমিকা রাখে:",
        [
            "Only body formation without reduction",
            "Alternation of generations / keeping chromosome number across sexual cycles",
            "Only wound repair like mitosis alone",
            "Only vegetative propagation",
        ],
        [
            "হ্রাস ছাড়া কেবল দেহ গঠন",
            "জনুক্রম / যৌন চক্রে ক্রোমোজোম সংখ্যা স্থিতিশীল রাখা",
            "কেবল মাইটোসিসের মতো ক্ষয়পূরণ",
            "কেবল অঙ্গজ জনন",
        ],
        "B", "medium", "conceptual",
        "Meiosis enables alternation of generations and restores chromosome number via fertilization.",
        "মিয়োসিস জনুক্রম সম্ভব করে এবং নিষেকের সাথে ক্রোমোজোম সংখ্যা স্থিতিশীল রাখে।",
    ),
    q(
        "In which stage of meiosis do the two chromatids of a chromosome completely separate?",
        "মিয়োসিসের কোন ধাপে ক্রোমোসোমের দুই ক্রোমাটিড সম্পূর্ণ আলাদা হয়?",
        ["Metaphase I", "Metaphase II", "Anaphase I", "Anaphase II"],
        ["মেটাফেজ-১", "মেটাফেজ-২", "অ্যানাফেজ-১", "অ্যানাফেজ-২"],
        "D", "medium", "factual",
        "Homologues separate in anaphase I; sister chromatids separate in anaphase II.",
        "অ্যানাফেজ-১-এ হোমোলোগ আলাদা; অ্যানাফেজ-২-এ সিস্টার ক্রোমাটিড আলাদা।",
    ),
    q(
        "Diploid cells in which meiosis occurs are called:",
        "যেসকল ডিপ্লয়েড কোষে মিয়োসিস ঘটে তাদের বলে:",
        ["Oocyte only as the general term", "Phagocyte", "Pinocyte", "Meiocyte"],
        ["সাধারণ নাম হিসেবে কেবল ওওসাইট", "ফ্যাগোসাইট", "পিনোসাইট", "মিয়োসাইট"],
        "D", "easy", "factual",
        "Meiocytes are diploid cells that undergo meiosis.",
        "মিয়োসাইট হলো যেসব ডিপ্লয়েড কোষে মিয়োসিস ঘটে।",
    ),
    q(
        "The intermediate stage between the first and second nuclear divisions of meiosis is:",
        "মিয়োসিসের প্রথম ও দ্বিতীয় নিউক্লিয়াস বিভাজনের মধ্যবর্তী দশা:",
        ["Karyokinesis", "Cytokinesis", "Metakinesis", "Interkinesis"],
        ["ক্যারিওকাইনেসিস", "সাইটোকাইনেসিস", "মেটাকাইনেসিস", "ইন্টারকাইনেসিস"],
        "D", "easy", "factual",
        "Interkinesis lies between meiosis I and II (RNA/protein synthesis; no DNA replication).",
        "মিয়োসিস-১ ও ২-এর মাঝে ইন্টারকাইনেসিস (RNA/প্রোটিন; DNA অনুলিপন নেই)।",
    ),
    q(
        "Chiasma is formed / becomes evident in which sub-stage?",
        "কায়াজমা কোন উপপর্যায়ে গঠিত/স্পষ্ট হয়?",
        ["Leptotene", "Zygotene", "Pachytene", "Diplotene"],
        ["লেপ্টোটিন", "জাইগোটিন", "প্যাকাইটিন", "ডিপ্লোটিন"],
        "D", "medium", "factual",
        "After crossing over in pachytene, chiasmata become visible as homologues begin to separate in diplotene.",
        "প্যাকাইটিনে ক্রসিংওভারের পর ডিপ্লোটিনে হোমোলোগ আলগা হতে কায়াজমা স্পষ্ট হয়।",
    ),
    q(
        "Homologous chromosomes pair up in which sub-phase?",
        "হোমোলোগাস ক্রোমোসোম কোন উপদশায় জোড় বাঁধে?",
        ["Leptotene", "Zygotene", "Pachytene", "Diplotene"],
        ["লেপ্টোটিন", "জাইগোটিন", "প্যাকাইটিন", "ডিপ্লোটিন"],
        "B", "easy", "factual",
        "Pairing begins in zygotene forming bivalents.",
        "জাইগোটিনে জোড় বাঁধা শুরু হয়ে বাইভ্যালেন্ট গঠিত হয়।",
    ),
    q(
        "Terminalization occurs in which sub-stage?",
        "প্রান্তীয়করণ কোন উপপর্যায়ে ঘটে?",
        ["Zygotene", "Pachytene", "Diplotene", "Diakinesis"],
        ["জাইগোটিন", "প্যাকাইটিন", "ডিপ্লোটিন", "ডায়াকাইনেসিস"],
        "C", "medium", "factual",
        "Chiasmata terminalize during diplotene (continuing into diakinesis).",
        "ডিপ্লোটিনে (ডায়াকাইনেসিস পর্যন্ত) কায়াজমার প্রান্তীয়করণ ঘটে।",
    ),
    q(
        "In which organism does meiosis occur in the zygote?",
        "কোন জীবে জাইগোটে মিয়োসিস ঘটে?",
        ["Ulothrix", "Pteris", "Oryza", "Hibiscus"],
        ["ইউলোথ্রিক্স", "টেরিস", "ওরাইজা", "হিবিস্কাস"],
        "A", "medium", "factual",
        "Ulothrix (alga) shows zygotic meiosis; ferns/flowering plants are sporophytic meiocytes.",
        "ইউলোথ্রিক্স (শৈবাল) জাইগোটিক মিয়োসিস দেখায়; ফার্ন/সপুষ্পকে স্পোরোফাইটিক মিয়োসাইট।",
    ),
    q(
        "Correct sequence of meiosis prophase I stages is:",
        "মিয়োসিস প্রোফেজ-১ এর সঠিক ক্রম:",
        [
            "Zygotene → Diplotene → Pachytene → Diakinesis",
            "Leptotene → Pachytene → Diplotene → Zygotene",
            "Zygotene → Leptotene → Pachytene → Diplotene",
            "Leptotene → Zygotene → Pachytene → Diplotene",
        ],
        [
            "জাইগোটিন → ডিপ্লোটিন → প্যাকাইটিন → ডায়াকাইনেসিস",
            "লেপ্টোটিন → প্যাকাইটিন → ডিপ্লোটিন → জাইগোটিন",
            "জাইগোটিন → লেপ্টোটিন → প্যাকাইটিন → ডিপ্লোটিন",
            "লেপ্টোটিন → জাইগোটিন → প্যাকাইটিন → ডিপ্লোটিন",
        ],
        "D", "medium", "factual",
        "Order: leptotene → zygotene → pachytene → diplotene (then diakinesis).",
        "ক্রম: লেপ্টোটিন → জাইগোটিন → প্যাকাইটিন → ডিপ্লোটিন (তারপর ডায়াকাইনেসিস)।",
    ),
    q(
        "Nuclear membrane disappears in which prophase I sub-stage?",
        "প্রোফেজ-১ এর কোন উপ-পর্যায়ে নিউক্লিয়ার মেমব্রেনের অবলুপ্তি ঘটে?",
        ["Zygotene", "Pachytene", "Diplotene", "Diakinesis"],
        ["জাইগোটিন", "প্যাকাইটিন", "ডিপ্লোটিন", "ডায়াকাইনেসিস"],
        "D", "medium", "factual",
        "Diakinesis ends prophase I with nuclear envelope breakdown.",
        "ডায়াকাইনেসিসে প্রোফেজ-১ শেষে নিউক্লিয়ার আবরণ বিলুপ্ত হয়।",
    ),
    q(
        "How many chromatids are present in two bivalents?",
        "দুইটি বাইভ্যালেন্টে কয়টি ক্রোমাটিড থাকে?",
        ["2", "4", "6", "8"],
        ["২", "৪", "৬", "৮"],
        "D", "medium", "numerical",
        "One bivalent = 2 chromosomes × 2 chromatids = 4; two bivalents = 8 chromatids.",
        "এক বাইভ্যালেন্ট = ২ ক্রোমোজোম × ২ ক্রোমাটিড = ৪; দুই বাইভ্যালেন্টে ৮ ক্রোমাটিড।",
    ),
    q(
        "Crossing over occurs: (i) in leptotene (ii) between non-sister chromatids (iii) between homologous chromosomes. Which is correct?",
        "ক্রসিংওভার ঘটে: (i) লেপ্টোটিন দশায় (ii) নন-সিস্টার ক্রোমাটিডের মধ্যে (iii) হোমোলোগাস ক্রোমোসোমের মধ্যে। কোনটি সঠিক?",
        [
            "i only",
            "ii and iii only",
            "i and ii only",
            "i, ii and iii",
        ],
        [
            "কেবল i",
            "কেবল ii ও iii",
            "কেবল i ও ii",
            "i, ii ও iii",
        ],
        "B", "medium", "conceptual",
        "Crossing over is between non-sister chromatids of homologous chromosomes, not in leptotene.",
        "ক্রসিংওভার হোমোলোগাস ক্রোমোসোমের নন-সিস্টার ক্রোমাটিডে; লেপ্টোটিনে নয়।",
    ),
    q(
        "Meiosis results in: (i) variation in organisms (ii) wound healing (iii) maintaining species identity. Which is correct?",
        "মিয়োসিসের ফলে: (i) জীবে বৈচিত্র্য সৃষ্টি (ii) ক্ষতস্থান পূরণ (iii) প্রজাতির স্বকীয়তা ঠিক থাকা। কোনটি সঠিক?",
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
        "C", "medium", "conceptual",
        "Meiosis creates variation and helps keep species chromosome identity; wound healing is mitotic.",
        "মিয়োসিস বৈচিত্র্য আনে ও প্রজাতির ক্রোমোজোম স্বকীয়তা রক্ষায় সাহায্য করে; ক্ষতপূরণ মাইটোটিক।",
    ),
    q(
        "The X-shaped structure formed by exchange between homologous chromosomes is a:",
        "হোমোলোগাস ক্রোমোসোমের অংশ বিনিময়ে সৃষ্ট X-আকৃতির কাঠামো:",
        ["Chiasma", "Bivalent only without exchange point", "Tetrad name only", "Diad only"],
        ["কায়াজমা", "বিনিময়বিন্দুহীন কেবল বাইভ্যালেন্ট", "কেবল টেট্রাড নাম", "কেবল ডায়াড"],
        "A", "easy", "factual",
        "The chiasma is the X-shaped contact marking crossover sites.",
        "কায়াজমা ক্রসিংওভার স্থলের X-আকৃতির সংযোগবিন্দু।",
    ),
]


TOPICS_MAP = {
    "bio1_27_ch02_t01": T01,
    "bio1_27_ch02_t02": T02,
    "bio1_27_ch02_t03": T03,
}


def write_topic(topic_id: str, rows: list[dict]) -> None:
    assert len(rows) == 20, f"{topic_id}: expected 20, got {len(rows)}"
    for i, row in enumerate(rows, 1):
        err = validate_record(row)
        if err:
            raise SystemExit(f"{topic_id} Q{i}: {err}\n{json.dumps(row, ensure_ascii=False)}")
    # Dedup stems within topic
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

    # Cross-topic duplicate check on stem_en
    all_stems: dict[str, str] = {}
    for tid, rows in TOPICS_MAP.items():
        for r in rows:
            key = r["stem_en"].casefold().strip()
            if key in all_stems:
                raise SystemExit(f"duplicate stem across {all_stems[key]} and {tid}: {r['stem_en']}")
            all_stems[key] = tid

    summary = {
        "chapter": "bio1_27_ch02",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p083_pdf089.png",
            "p084_pdf090.png",
            "p085_pdf091.png",
            "p086_pdf092.png",
            "p087_pdf093.png",
            "p088_pdf094.png",
            "p089_pdf095.png",
            "p090_pdf096.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio1_27_ch02_t01": {
                "title": "Cell cycle / কোষচক্র",
                "themes": [
                    "G1/S/G2/M timing percentages",
                    "DNA replication in S",
                    "histone synthesis",
                    "metabolic nucleus / interphase",
                    "apoptosis vs necrosis",
                    "interkinesis without DNA replication",
                    "cyclin / cycle control",
                ],
            },
            "bio1_27_ch02_t02": {
                "title": "Mitosis / মাইটোসিস",
                "themes": [
                    "metakinesis / metaphase alignment",
                    "prometaphase envelope/spindle",
                    "anaphase movement and letter shapes",
                    "karyokinesis vs cytokinesis",
                    "cell plate / middle lamella",
                    "chromatid counts",
                    "actin-myosin furrow",
                ],
            },
            "bio1_27_ch02_t03": {
                "title": "Meiosis / মিয়োসিস",
                "themes": [
                    "synapsis / zygotene",
                    "crossing over / pachytene",
                    "chiasma / diplotene / terminalization",
                    "diakinesis envelope loss",
                    "meiocyte / sporophytic site",
                    "zygotic meiosis (Ulothrix)",
                    "anaphase II chromatid separation",
                    "prophase I sequence",
                ],
            },
        },
        "low_confidence": [
            "Diagram-linked bank items rewritten as standalone bilingual stems for bank import.",
            "Skipped conflicting/faulty printed items (e.g. ambiguous centromere-stage keys).",
            "Q numbering in source bank spans ~01–118; curated subset mapped to syllabus topics.",
            "Some i/ii/iii combination stems state the roman facts in explanations for clarity.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio1_27_ch02_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio1_27_ch02_t01": 20,
                "bio1_27_ch02_t02": 20,
                "bio1_27_ch02_t03": 20,
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
        / "ch02_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
