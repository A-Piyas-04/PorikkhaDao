#!/usr/bin/env python3
"""Seed Biology 1st Paper Ch1 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio1_27_ch01_t01..t03 (cell wall/membrane; organelles; nucleus/chromosomes).
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
    "biology p1 ch01; curated bilingual"
)


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    if en == bn and not re.search(r"[A-Za-z]", en):
        en = f"value {en}"
        bn = f"মান {bn}" if not re.search(r"[ঀ-৿]", bn) else bn
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


# --- t01: Cell wall and membrane / কোষপ্রাচীর ও কোষঝিল্লি ---
T01 = [
    q(
        "Which is the main chemical component of the middle lamella?",
        "মধ্যপর্দার প্রধান রাসায়নিক উপাদান কোনটি?",
        ["Cellulose", "Lignin", "Pectin", "Suberin"],
        ["সেলুলোজ", "লিগনিন", "পেকটিন", "সুবেরিন"],
        "C", "easy", "factual",
        "The middle lamella is rich in pectin (pectic substances) that cement adjacent plant cells.",
        "মধ্যপর্দায় পেকটিন (পেকটিক পদার্থ) অধিক থাকে যা পাশাপাশি কোষগুলোকে আটকে রাখে।",
    ),
    q(
        "Which statement about the plasma membrane is correct?",
        "প্লাজমামেমব্রেন সম্পর্কে কোনটি সঠিক?",
        [
            "Phospholipid heads are hydrophobic",
            "It contains no carbohydrate",
            "Peripheral proteins lie on the membrane surface",
            "The two phospholipid layers face the same direction",
        ],
        [
            "ফসফোলিপিড মস্তক পানিবিদ্বেষী",
            "এতে কোনো কার্বোহাইড্রেট থাকে না",
            "পেরিফেরাল প্রোটিন ঝিল্লির পৃষ্ঠে থাকে",
            "ফসফোলিপিডের দুই স্তর একই দিকে মুখ করে থাকে",
        ],
        "C", "medium", "conceptual",
        "Peripheral proteins associate with the membrane surface; phospholipid heads are hydrophilic and bilayer leaflets face oppositely.",
        "পেরিফেরাল প্রোটিন ঝিল্লির সারফেসে থাকে; ফসফোলিপিড মস্তক পানিপ্রিয় এবং দ্বিস্তর পরস্পর বিপরীতমুখী।",
    ),
    q(
        "Which is applicable to the cell membrane?",
        "কোষঝিল্লির ক্ষেত্রে কোনটি প্রযোজ্য?",
        ["Fully permeable", "Triple-layered only", "Always has plasmodesmata", "Elastic"],
        ["সম্পূর্ণ ভেদ্য", "কেবল ত্রিস্তরী", "সবসময় প্লাজমোডেসমাযুক্ত", "স্থিতিস্থাপক"],
        "D", "easy", "factual",
        "The plasma membrane is elastic, selectively permeable, and typically bilayered (fluid mosaic).",
        "কোষঝিল্লি স্থিতিস্থাপক, বৈষম্যভেদ্য এবং সাধারণত দ্বিস্তরী (ফ্লুইড মোজাইক)।",
    ),
    q(
        "According to the fluid mosaic model, phospholipid molecules in a membrane can:",
        "ফ্লুইড মোজাইক মডেল অনুসারে ঝিল্লির ফসফোলিপিড অণু:",
        [
            "Flex laterally and rotate about their axes",
            "Only flip freely between leaflets at high rate",
            "Never move at all",
            "Dissolve completely in water",
        ],
        [
            "পার্শ্বীয়ভাবে ব্যাপ্ত হতে ও অক্ষ বরাবর ঘুরতে পারে",
            "কেবল দুই স্তরের মধ্যে দ্রুত স্থান পরিবর্তন করে",
            "কখনোই নড়াচড়া করে না",
            "সম্পূর্ণ পানিতে দ্রবীভূত হয়",
        ],
        "A", "medium", "conceptual",
        "Lipids can diffuse laterally and rotate; flip-flop between leaflets is rare without flippases.",
        "লিপিড পার্শ্বীয় ব্যাপ্তি ও অক্ষীয় ঘূর্ণন করতে পারে; স্তরান্তর স্থানপরিবর্তন সাধারণত বিরল।",
    ),
    q(
        "Glycocalyx is formed mainly of which components?",
        "গ্লাইকোক্যালিক্স প্রধানত কোন উপাদান দিয়ে গঠিত?",
        [
            "Glycolipid and glycoprotein",
            "Glycolipid and enzyme only",
            "Lipid and carboxylic acid only",
            "Lipid and cholesterol only",
        ],
        [
            "গ্লাইকוליপিড ও গ্লাইকোপ্রোটিন",
            "কেবল গ্লাইকালিপিড ও এনজাইম",
            "কেবল লিপিড ও কার্বক্সিলিক অ্যাসিড",
            "কেবল লিপিড ও কোলেস্টেরল",
        ],
        "A", "medium", "factual",
        "The glycocalyx is a carbohydrate coat of glycolipids and glycoproteins on the outer membrane surface.",
        "গ্লাইকোক্যালিক্স ঝিল্লির বাইরে গ্লাইকালিপিড ও গ্লাইকোপ্রোটিনের কার্বোহাইড্রেট আবরণ।",
    ),
    q(
        "What is the smallest structural unit of the plant cell wall?",
        "কোষপ্রাচীরের ক্ষুদ্রতম গাঠনিক একক কোনটি?",
        ["Cellulose molecule", "Micelle", "Microfibril", "Lignin"],
        ["সেলুলোজ অণু", "মাইসেল", "মাইক্রোফাইব্রিল", "লিগনিন"],
        "B", "hard", "factual",
        "In many HSC framings, cellulose micelles are treated as the smallest structural units that assemble into microfibrils.",
        "এইচএসসি কাঠামোয় সেলুলোজ মাইসেলকে ক্ষুদ্রতম গাঠনিক একক ধরে মাইক্রোফাইব্রিলে সংগঠিত বলা হয়।",
    ),
    q(
        "Which polysaccharide is typical of fungal cell walls (not plant cellulose walls)?",
        "ছত্রাক কোষপ্রাচীরে সাধারণত কোন পলিস্যাকারাইড পাওয়া যায় (উদ্ভিদের সেলুলোজ প্রাচীর নয়)?",
        ["Pectin", "Cellulose", "Chitin", "Lignin"],
        ["পেকটিন", "সেলুলোজ", "কাইটিন", "লিগনিন"],
        "C", "easy", "factual",
        "Most fungi have chitinous cell walls, whereas plant primary walls are cellulose-rich.",
        "অধিকাংশ ছত্রাকের প্রাচীর কাইটিনযুক্ত; উদ্ভিদের প্রাথমিক প্রাচীর সেলুলোজসমৃদ্ধ।",
    ),
    q(
        "The thin membrane surrounding the cell vacuole is called the:",
        "কোষগহ্বরের চারপাশের পাতলা আবরণকে কী বলে?",
        ["Tonoplast", "Aleuroplast", "Elaioplast", "Amyloplast"],
        ["টনোপ্লাস্ট", "অ্যালিউরোপ্লাস্ট", "ইলায়োপ্লাস্ট", "অ্যামাইলোপ্লাস্ট"],
        "A", "easy", "factual",
        "The tonoplast is the vacuolar membrane that encloses cell sap.",
        "টনোপ্লাস্ট হলো কোষরসবদ্ধ গহ্বরঝিল্লি।",
    ),
    q(
        "Middle lamella contains large amounts of:",
        "মধ্যপর্দায় অধিক পরিমাণে থাকে:",
        ["Pectic acid / pectin", "Cellulose only", "Glycoprotein only", "Lignin only"],
        ["পেকটিক অ্যাসিড / পেকটিন", "কেবল সেলুলোজ", "কেবল গ্লাইকোপ্রোটিন", "কেবল লিগনিন"],
        "A", "easy", "factual",
        "Pectin and related pectic acids cement adjacent cell walls at the middle lamella.",
        "পেকটিন ও পেকটিক অ্যাসিড মধ্যপর্দায় কোষপ্রাচীরগুলোকে আটকে রাখে।",
    ),
    q(
        "Functions of the cell vacuole include:",
        "কোষগহ্বরের কাজের মধ্যে রয়েছে:",
        [
            "Holding cell sap and helping turgor / pH control",
            "Only synthesizing ribosomal RNA",
            "Only forming the nuclear envelope",
            "Only carrying out photosynthesis",
        ],
        [
            "কোষরস ধারণ ও রসস্ফীতি/pH নিয়ন্ত্রণে সাহায্য",
            "কেবল রাইবোসোমাল RNA সংশ্লেষণ",
            "কেবল নিউক্লিয়ার এনভেলপ গঠন",
            "কেবল সালোকসংশ্লেষণ",
        ],
        "A", "medium", "conceptual",
        "Vacuoles store cell sap and help regulate turgor pressure and internal pH.",
        "কোষগহ্বর কোষরস ধরে এবং রসস্ফীতি চাপ ও অভ্যন্তরীণ pH নিয়ন্ত্রণে সাহায্য করে।",
    ),
    q(
        "Which describes selective permeability of the plasma membrane?",
        "প্লাজমামেমব্রেনের বৈষম্যভেদ্যতার সঠিক বর্ণনা কোনটি?",
        [
            "All solutes pass equally freely",
            "Some substances pass more readily than others",
            "Nothing can ever enter the cell",
            "Only gases are blocked forever",
        ],
        [
            "সব দ্রব একইভাবে অবাধে যায়",
            "কিছু পদার্থ অন্যগুলোর চেয়ে সহজে যায়",
            "কখনোই কিছু কোষে ঢোকে না",
            "কেবল গ্যাস চিরকাল বাধাপ্রাপ্ত",
        ],
        "B", "easy", "conceptual",
        "Selective (differential) permeability allows regulated passage of substances.",
        "বৈষম্যভেদ্যতায় পদার্থের নিয়ন্ত্রিত প্রবেশ-প্রস্থান ঘটে।",
    ),
    q(
        "Plant primary cell walls are rich mainly in:",
        "উদ্ভিদের প্রাথমিক কোষপ্রাচীর প্রধানত সমৃদ্ধ:",
        ["Cellulose", "Chitin", "Peptidoglycan", "Keratin"],
        ["সেলুলোজ", "কাইটিন", "পেপটিডোগ্লাইকান", "কেরাটিন"],
        "A", "easy", "factual",
        "Cellulose microfibrils are the chief structural polysaccharide of plant primary walls.",
        "উদ্ভিদের প্রাথমিক প্রাচীরের প্রধান গাঠনিক পলিস্যাকারাইড সেলুলোজ।",
    ),
    q(
        "Secondary thickening of plant cell walls often involves deposition of:",
        "উদ্ভিদ কোষপ্রাচীরের গৌণ পুরু হওয়ায় প্রায়শই জমা হয়:",
        ["Lignin", "Glycogen", "Starch only", "Hemoglobin"],
        ["লিগনিন", "গ্লাইকোজেন", "কেবল স্টার্চ", "হিমোগ্লোবিন"],
        "A", "medium", "factual",
        "Lignin impregnation strengthens secondary walls (e.g., xylem).",
        "লিগনিন গৌণ প্রাচীরকে শক্ত করে (যেমন জাইলেম)।",
    ),
    q(
        "Plasmodesmata are:",
        "প্লাজমোডেসমা হলো:",
        [
            "Cytoplasmic channels through plant cell walls linking adjacent cells",
            "Mitochondrial cristae folds",
            "Nuclear pores only in animals",
            "Golgi secretory vesicles only",
        ],
        [
            "উদ্ভিদ কোষপ্রাচীর ভেদ করে পাশাপাশি কোষের সাইটোপ্লাজমীয় সংযোগপথ",
            "মাইটোকন্ড্রিয়ার ক্রিস্টি ভাঁজ",
            "কেবল প্রাণীর নিউক্লিয়ার ছিদ্র",
            "কেবল গলগির নিঃসরণ ভেসিকল",
        ],
        "A", "medium", "conceptual",
        "Plasmodesmata allow intercellular transport between plant cells through wall channels.",
        "প্লাজমোডেসমা প্রাচীরের ছিদ্রপথে উদ্ভিদকোষগুলোর মধ্যে পরিবহন সম্ভব করে।",
    ),
    q(
        "Which membrane protein class is embedded within the lipid bilayer?",
        "কোন শ্রেণির ঝিল্লি প্রোটিন লিপিড দ্বিস্তরের মধ্যে প্রোথিত থাকে?",
        ["Integral / transmembrane proteins", "Only soluble cytoplasmic enzymes", "Only histone proteins", "Only ribosomal proteins"],
        ["ইন্টিগ্রাল / ট্রান্সমেমব্রেন প্রোটিন", "কেবল দ্রবণীয় সাইটোপ্লাজমীয় এনজাইম", "কেবল হিস্টোন প্রোটিন", "কেবল রাইবোসোমাল প্রোটিন"],
        "A", "easy", "factual",
        "Integral proteins span or are deeply embedded in the bilayer; peripheral proteins are surface-associated.",
        "ইন্টিগ্রাল প্রোটিন দ্বিস্তরে প্রোথিত/বিস্তৃত; পেরিফেরাল প্রোটিন পৃষ্ঠসংলগ্ন।",
    ),
    q(
        "Suberin is characteristically associated with:",
        "সুবেরিন সাধারণত কোনটির সাথে যুক্ত?",
        [
            "Cork / waterproofing of some plant walls",
            "Ribosome assembly",
            "Chromosome condensation only",
            "mRNA splicing only",
        ],
        [
            "কর্ক / কিছু উদ্ভিদপ্রাচীরের জলনিরোধকতা",
            "রাইবোসোম গঠন",
            "কেবল ক্রোমোজোম ঘনীভবন",
            "কেবল mRNA স্প্লাইসিং",
        ],
        "A", "medium", "factual",
        "Suberin waterproofs cork and related wall tissues.",
        "সুবেরিন কর্ক ও সংশ্লিষ্ট প্রাচীরকে জলনিরোধক করে।",
    ),
    q(
        "The fluid mosaic model was proposed to describe:",
        "ফ্লুইড মোজাইক মডেল কোনটির গঠন বর্ণনা করে?",
        ["Plasma membrane structure", "Cell wall cellulose only", "Nuclear lamina only", "Centriole triplets only"],
        ["প্লাজমামেমব্রেনের গঠন", "কেবল কোষপ্রাচীরের সেলুলোজ", "কেবল নিউক্লিয়ার ল্যামিনা", "কেবল সেন্ট্রিওল ট্রিপলেট"],
        "A", "easy", "factual",
        "Singer and Nicolson’s fluid mosaic model describes dynamic lipid–protein organization of membranes.",
        "সিঙ্গার ও নিকোলসনের ফ্লুইড মোজাইক মডেল ঝিল্লির গতিশীল লিপিড–প্রোটিন সংগঠন ব্যাখ্যা করে।",
    ),
    q(
        "Which is NOT a typical component of the plant middle lamella?",
        "উদ্ভিদের মধ্যপর্দার সাধারণ উপাদান নয় কোনটি?",
        ["Abundant pectin", "Some calcium pectate", "Large amounts of DNA", "Cementing pectic substances"],
        ["প্রচুর পেকটিন", "কিছু ক্যালসিয়াম পেকটেট", "প্রচুর DNA", "আঠালো পেকটিক পদার্থ"],
        "C", "easy", "conceptual",
        "Middle lamella is pectin-rich cement; DNA is nuclear/organellar, not a middle-lamella bulk component.",
        "মধ্যপর্দা পেকটিনসমৃদ্ধ আঠা; DNA নিউক্লিয়াস/অঙ্গাণুতে থাকে, মধ্যপর্দার প্রধান উপাদান নয়।",
    ),
    q(
        "Cellulose microfibrils in the wall are mainly composed of:",
        "প্রাচীরের সেলুলোজ মাইক্রোফাইব্রিল প্রধানত গঠিত:",
        ["β-glucose polymer chains", "Amino acid polymers only", "Fatty acid chains only", "Nucleotide polymers only"],
        ["β-গ্লুকোজ পলিমার শিকল", "কেবল অ্যামিনো অ্যাসিড পলিমার", "কেবল ফ্যাটি অ্যাসিড শিকল", "কেবল নিউক্লিওটাইড পলিমার"],
        "A", "medium", "conceptual",
        "Cellulose is a β-1,4-linked glucose polysaccharide assembled into microfibrils.",
        "সেলুলোজ β-1,4 সংযুক্ত গ্লুকোজ পলিস্যাকারাইড যা মাইক্রোফাইব্রিল গঠন করে।",
    ),
    q(
        "Which best contrasts cell wall vs plasma membrane in plant cells?",
        "উদ্ভিদকোষে কোষপ্রাচীর ও প্লাজমামেমব্রেনের সেরা পার্থক্য কোনটি?",
        [
            "Wall is rigid/protective outside; membrane is living selective barrier inside",
            "Wall is always absent; membrane is cellulose",
            "Both are identical lipid bilayers only",
            "Membrane is made of lignin; wall of phospholipids",
        ],
        [
            "প্রাচীর বাইরের দৃঢ় আবরণ; ঝিল্লি ভিতরের জীবন্ত বৈষম্যভেদ্য বাধা",
            "প্রাচীর সবসময় অনুপস্থিত; ঝিল্লি সেলুলোজ",
            "উভয়ই কেবল অভিন্ন লিপিড দ্বিস্তর",
            "ঝিল্লি লিগনিনের; প্রাচীর ফসফোলিপিডের",
        ],
        "A", "easy", "conceptual",
        "The wall is a non-living cellulose-rich outer coat; the plasma membrane is the living selective bilayer.",
        "প্রাচীর অজীব সেলুলোজসমৃদ্ধ বাইরের আবরণ; প্লাজমামেমব্রেন জীবন্ত বৈষম্যভেদ্য দ্বিস্তর।",
    ),
]

# --- t02: Cell organelles / কোষীয় অঙ্গাণু ---
T02 = [
    q(
        "Lipochondria (Golgi apparatus) functions include:",
        "লাইপোকন্ড্রিয়া (গলগি যন্ত্র)-এর কাজে অন্তর্ভুক্ত:",
        [
            "Cell-plate formation, acrosome formation, packaging ER products",
            "Only DNA replication in the nucleus",
            "Only forming middle lamella cellulose",
            "Only translating mRNA into protein",
        ],
        [
            "কোষপ্লেট তৈরি, অ্যাক্রোজোম গঠন, ER দ্রব্য প্যাকেজিং",
            "কেবল নিউক্লিয়াসে DNA রেপ্লিকেশন",
            "কেবল মধ্যপর্দার সেলুলোজ গঠন",
            "কেবল mRNA থেকে প্রোটিন অনুবাদ",
        ],
        "A", "medium", "conceptual",
        "Golgi (lipochondria) packages secretions, helps form cell plate/acrosome, and modifies ER products.",
        "গলগি (লাইপোকন্ড্রিয়া) নিঃসরণ প্যাকেজ করে, কোষপ্লেট/অ্যাক্রোজোম গঠনে ও ER দ্রব্য পরিবর্তনে সাহায্য করে।",
    ),
    q(
        "Chloroplasts mainly help in:",
        "ক্লোরোপ্লাস্ট প্রধানত সাহায্য করে:",
        ["Photosynthesis / food preparation", "Intracellular digestion only", "Protein synthesis on ribosomes only", "Spindle fiber formation only"],
        ["সালোকসংশ্লেষণ / খাদ্য প্রস্তুতিতে", "কেবল অন্তঃকোষীয় পরিপাকে", "কেবল রাইবোসোমে প্রোটিন সংশ্লেষণে", "কেবল মাকুতন্তু গঠনে"],
        "A", "easy", "factual",
        "Chloroplasts are the sites of photosynthesis (food factory of the plant cell).",
        "ক্লোরোপ্লাস্ট সালোকসংশ্লেষণের স্থান—উদ্ভিদকোষের খাদ্য কারখানা।",
    ),
    q(
        "Which organelle is involved in autophagy?",
        "অটোফ্যাগির সাথে জড়িত অঙ্গাণু কোনটি?",
        ["Mitochondrion", "Endoplasmic reticulum", "Golgi body", "Lysosome"],
        ["মাইটোকন্ড্রিয়া", "এন্ডোপ্লাজমিক রেটিকুলাম", "গলগিবস্তু", "লাইসোসোম"],
        "D", "easy", "factual",
        "Lysosomes digest worn-out cell components (autophagy) using hydrolytic enzymes.",
        "লাইসোসোম হাইড্রোলাইটিক এনজাইম দিয়ে জীর্ণ কোষীয় উপাদান পরিপাক করে (অটোফ্যাজি)।",
    ),
    q(
        "Which organelle is mainly associated with energy production (ATP) in respiration?",
        "শ্বসনে শক্তি (ATP) উৎপাদনের সাথে প্রধানত কোন অঙ্গাণু জড়িত?",
        ["Chloroplast", "Ribosome", "Mitochondrion", "Nucleus"],
        ["ক্লোরোপ্লাস্ট", "রাইবোসোম", "মাইটোকন্ড্রিয়া", "নিউক্লিয়াস"],
        "C", "easy", "factual",
        "Mitochondria are the powerhouses producing ATP via cellular respiration.",
        "মাইটোকন্ড্রিয়া কোষীয় শ্বসনে ATP তৈরি করে—শক্তির ঘর।",
    ),
    q(
        "Granum is present in which organelle?",
        "কোন অঙ্গাণুতে গ্রানাম বিদ্যমান?",
        ["Nucleus", "Mitochondrion", "Chloroplast", "Ribosome"],
        ["নিউক্লিয়াস", "মাইটোকন্ড্রিয়া", "ক্লোরোপ্লাস্ট", "রাইবোসোম"],
        "C", "easy", "factual",
        "Grana are stacks of thylakoids inside chloroplasts.",
        "গ্রানা ক্লোরোপ্লাস্টের থাইলাকয়েড স্তূপ।",
    ),
    q(
        "Where are thylakoids found?",
        "থাইলাকয়েড কোষের কোন অঙ্গাণুতে থাকে?",
        ["Mitochondrion", "Ribosome", "Chloroplast", "Lysosome"],
        ["মাইটোকন্ড্রিয়ায়", "রাইবোসোমে", "ক্লোরোপ্লাস্টে", "লাইসোসোমে"],
        "C", "easy", "factual",
        "Thylakoid membranes in chloroplasts house photosynthetic pigments and light reactions.",
        "ক্লোরোপ্লাস্টের থাইলাকয়েডে সালোকসংশ্লেষণের রঞ্জক ও আলোক বিক্রিয়া ঘটে।",
    ),
    q(
        "Circular DNA is seen in which of the following?",
        "নিচের কোনটিতে বৃত্তাকার DNA দেখা যায়?",
        ["Nucleus (linear chromosomes)", "Ribosome", "Lysosome", "Mitochondrion"],
        ["নিউক্লিয়াস (রৈখিক ক্রোমোজোম)", "রাইবোসোম", "লাইসোসোম", "মাইটোকন্ড্রিয়া"],
        "D", "medium", "factual",
        "Mitochondria (and chloroplasts) contain circular DNA, reflecting endosymbiotic origin.",
        "মাইটোকন্ড্রিয়ায় (ও ক্লোরোপ্লাস্টে) বৃত্তাকার DNA থাকে—এন্ডোসিম্বায়োসিসের ইঙ্গিত।",
    ),
    q(
        "Who discovered lysosomes?",
        "লাইসোসোম আবিষ্কার করেন কে?",
        ["Keith R. Porter", "Christian de Duve", "George Palade", "Edouard Van Beneden"],
        ["কিথ আর. পোর্টার", "ক্রিস্টিয়ান দ্য ডুভ", "জর্জ প্যালাডে", "এডোয়ার্ড ভ্যান বেনেডেন"],
        "B", "easy", "factual",
        "Christian de Duve discovered lysosomes.",
        "ক্রিস্টিয়ান দ্য ডুভ লাইসোসোম আবিষ্কার করেন।",
    ),
    q(
        "Which is called an endosymbiont organelle?",
        "এন্ডোসিম্বায়ন্ট বলা হয় কোনটিকে?",
        ["Ribosome", "Mitochondrion", "Lysosome", "Golgi body"],
        ["রাইবোসোম", "মাইটোকন্ড্রিয়া", "লাইসোসোম", "গলগিবডি"],
        "B", "medium", "conceptual",
        "Mitochondria arose by endosymbiosis of aerobic prokaryotes and retain their own DNA/ribosomes.",
        "মাইটোকন্ড্রিয়া এন্ডোসিম্বায়োসিসে উদ্ভূত এবং নিজস্ব DNA/রাইবোসোম ধরে রাখে।",
    ),
    q(
        "Which cytoplasmic organelle is NOT membrane-bound?",
        "কোন সাইটোপ্লাজমীয় অঙ্গাণু ঝিল্লিবদ্ধ নয়?",
        ["Golgi body", "Ribosome", "Lysosome", "Peroxisome"],
        ["গলগিবডি", "রাইবোসোম", "লাইসোসোম", "পারঅক্সিসোম"],
        "B", "easy", "factual",
        "Ribosomes lack a bounding membrane; they are RNP particles.",
        "রাইবোসোমের আবরণী ঝিল্লি নেই; এরা RNP কণা।",
    ),
    q(
        "Cristae are characteristic folds of the:",
        "ক্রিস্টি কোন অঙ্গাণুর বৈশিষ্ট্যপূর্ণ ভাঁজ?",
        ["Nucleus", "Lysosome", "Chloroplast stroma only", "Mitochondrion"],
        ["নিউক্লিয়াস", "লাইসোসোম", "কেবল ক্লোরোপ্লাস্ট স্ট্রোমা", "মাইটোকন্ড্রিয়া"],
        "D", "easy", "factual",
        "Inner mitochondrial membrane folds into cristae to increase surface area for ATP synthase.",
        "মাইটোকন্ড্রিয়ার অন্তঃঝিল্লি ক্রিস্টি গঠন করে ATP সিন্থেসিসের ক্ষেত্রফল বাড়ায়।",
    ),
    q(
        "Which forms the spindle apparatus (aster/spindle fibers)?",
        "মাকুতন্তু গঠন করে নিচের কোনটি?",
        ["Ribosome", "Lysosome", "Centriole", "Golgi body"],
        ["রাইবোসোম", "লাইসোসোম", "সেন্ট্রিওল", "গলগিবডি"],
        "C", "easy", "factual",
        "Centrioles organize microtubules of the spindle in animal cells.",
        "সেন্ট্রিওল প্রাণীকোষে মাকুতন্তুর মাইক্রোটিউবিউল সংগঠিত করে।",
    ),
    q(
        "Autolysis occurs in which organelle?",
        "কোন অঙ্গাণুতে অটোলাইসিস ঘটে?",
        ["Golgi body", "Lysosome", "Endoplasmic reticulum", "Ribosome"],
        ["গলগিবডি", "লাইসোসোম", "এন্ডোপ্লাজমিক রেটিকুলাম", "রাইবোসোম"],
        "B", "medium", "factual",
        "Lysosomal enzymes can digest the cell’s own components (autolysis).",
        "লাইসোসোমের এনজাইম কোষের নিজস্ব উপাদান পরিপাক করতে পারে (অটোলাইসিস)।",
    ),
    q(
        "The protein factory of the cell is the:",
        "কোষের প্রোটিন ফ্যাক্টরি কোনটি?",
        ["Ribosome", "Golgi body", "Lysosome", "Endoplasmic reticulum only"],
        ["রাইবোসোম", "গলগিবস্তু", "লাইসোসোম", "কেবল এন্ডোপ্লাজমিক রেটিকুলাম"],
        "A", "easy", "factual",
        "Ribosomes synthesize proteins; rough ER hosts many ribosomes for secretory proteins.",
        "রাইবোসোম প্রোটিন সংশ্লেষ করে; রফ এন্ডোপ্লাজমিক রেটিকুলামে অনেক রাইবোসোম থাকে।",
    ),
    q(
        "Subunits of an 80S eukaryotic ribosome are:",
        "80S ইউক্যারিয়টিক রাইবোসোমের উপ-এককগুলো হলো:",
        ["60S and 40S", "50S and 30S", "60S and 20S", "50S and 40S"],
        ["৬০এস ও ৪০এস", "৫০এস ও ৩০এস", "৬০এস ও ২০এস", "৫০এস ও ৪০এস"],
        "A", "medium", "factual",
        "Eukaryotic cytosolic ribosomes are 80S = 60S + 40S; prokaryotic are 70S = 50S + 30S.",
        "ইউক্যারিয়টিক সাইটোসলিক রাইবোসোম 80S = 60S + 40S; প্রোক্যারিয়টিক 70S = 50S + 30S।",
    ),
    q(
        "Which is NOT another name for the mitochondrion?",
        "মাইটোকন্ড্রিয়ার অন্য নাম নয় কোনটি?",
        ["Sarcosome", "Fila", "Bioplast", "Mitoribosome (as a synonym of the whole organelle)"],
        ["সারকোসোম", "ফিলা", "বায়োপ্লাস্ট", "মাইটোরাইবোসোম (সমগ্র অঙ্গাণুর সমার্থক হিসেবে)"],
        "D", "hard", "factual",
        "Mitochondria are also called powerhouse/sarcosome etc.; mitoribosomes are their ribosomes, not synonym names of the organelle.",
        "মাইটোকন্ড্রিয়াকে শক্তিঘর/সারকোসোম ইত্যাদি বলা হয়; মাইটোরাইবোসোম তার রাইবোসোম, সমগ্র অঙ্গাণুর নাম নয়।",
    ),
    q(
        "Which organelle is known as the traffic police / packaging center of the cell?",
        "কোষের ট্রাফিক পুলিশ / প্যাকেজিং কেন্দ্র কোন অঙ্গাণু?",
        ["Golgi apparatus", "Nucleus (brain)", "Mitochondrion (powerhouse)", "Chloroplast (kitchen)"],
        ["গলগি যন্ত্র", "নিউক্লিয়াস (মস্তিষ্ক)", "মাইটোকন্ড্রিয়া (শক্তিঘর)", "ক্লোরোপ্লাস্ট (রান্নাঘর)"],
        "A", "medium", "conceptual",
        "Golgi sorts and packages materials for secretion or delivery—often called the traffic police.",
        "গলগি দ্রব্য বাছাই ও প্যাকেজ করে—প্রায়ই ট্রাফিক পুলিশ বলা হয়।",
    ),
    q(
        "Functions of the endoplasmic reticulum include:",
        "এন্ডোপ্লাজমিক রেটিকুলামের কাজে রয়েছে:",
        [
            "Providing a cytoplasmic framework and supporting protein/lipid trafficking",
            "Only storing starch in amyloplasts",
            "Only forming the middle lamella",
            "Only carrying out glycolysis in the matrix",
        ],
        [
            "সাইটোপ্লাজমের কাঠামো ও প্রোটিন/লিপিড পরিবহনে সহায়তা",
            "কেবল অ্যামাইলোপ্লাস্টে স্টার্চ সঞ্চয়",
            "কেবল মধ্যপর্দা গঠন",
            "কেবল ম্যাট্রিক্সে গ্লাইকোলাইসিস",
        ],
        "A", "medium", "conceptual",
        "ER forms an intracellular network for synthesis and transport of proteins and lipids.",
        "ER অন্তঃকোষীয় জালিকা হিসেবে প্রোটিন ও লিপিড সংশ্লেষণ-পরিবহনে কাজ করে।",
    ),
    q(
        "Stabilizer and labilizer properties are associated with which organelle?",
        "স্ট্যাবিলাইজার ও ল্যাবিলাইজার কোন অঙ্গাণুর বৈশিষ্ট্য?",
        ["Centrosome", "Lysosome", "Nucleosome", "Ribosome"],
        ["সেন্ট্রোসোম", "লাইসোসোম", "নিউক্লিওসোম", "রাইবোসোম"],
        "B", "hard", "factual",
        "In HSC texts, lysosomal membrane stability (stabilizers/labilizers) regulates enzyme release.",
        "এইচএসসি পাঠে লাইসোসোম ঝিল্লির স্থায়িত্ব (স্ট্যাবিলাইজার/ল্যাবিলাইজার) এনজাইম নিঃসরণ নিয়ন্ত্রণ করে।",
    ),
    q(
        "Which organelle contains enzymes of lipid metabolism among the following?",
        "নিচের কোন অঙ্গাণুতে লিপিড বিপাকের এনজাইম থাকে?",
        ["Peroxisome / glyoxysome lineage", "Only nucleolus", "Only centriole", "Only vacuole tonoplast pectinase only"],
        ["পারঅক্সিসোম / গ্লাইঅক্সিসোম ধরনের", "কেবল নিউক্লিওলাস", "কেবল সেন্ট্রিওল", "কেবল টনোপ্লাস্টের পেকটিনেজ"],
        "A", "hard", "conceptual",
        "Peroxisomes/glyoxysomes house enzymes for fatty-acid/lipid-related pathways.",
        "পারঅক্সিসোম/গ্লাইঅক্সিসোমে ফ্যাটি অ্যাসিড/লিপিড সংশ্লিষ্ট এনজাইম থাকে।",
    ),
]

# --- t03: Nucleus and chromosomes / নিউক্লিয়াস ও ক্রোমোজোম ---
T03 = [
    q(
        "Which is a stop (nonsense) codon?",
        "স্টপ (ননসেন্স) কোডন কোনটি?",
        ["AUG", "AGU", "UGC", "UAA"],
        ["AUG (সূচনা)", "AGU (সেরিন)", "UGC (সিস্টাইন)", "UAA (স্টপ)"],
        "D", "easy", "factual",
        "UAA, UAG and UGA are stop codons; AUG is the usual start codon.",
        "UAA, UAG ও UGA স্টপ কোডন; AUG সাধারণত সূচনাকারী কোডন।",
    ),
    q(
        "Which listed codon is atypical as a stop codon among UAA, UGA, UAG, AUG?",
        "UAA, UGA, UAG, AUG এর মধ্যে কোনটি ভিন্নধর্মী (স্টপ নয়)?",
        ["UAA", "UGA", "UAG", "AUG"],
        ["UAA (স্টপ)", "UGA (স্টপ)", "UAG (স্টপ)", "AUG (সূচনা)"],
        "D", "easy", "conceptual",
        "AUG initiates translation (Met); the other three terminate translation.",
        "AUG অনুবাদ শুরু করে (মেথায়োনিন); অন্য তিনটি অনুবাদ শেষ করে।",
    ),
    q(
        "A chromosome with a satellite is called a:",
        "স্যাটেলাইট যুক্ত ক্রোমোজোমকে কী বলা হয়?",
        ["Acrocentric chromosome", "Metacentric chromosome", "SAT chromosome", "Diffused chromosome"],
        ["অ্যাক্রোসেন্ট্রিক ক্রোমোজোম", "মেটাসেন্ট্রিক ক্রোমোজোম", "স্যাট ক্রোমোজোম", "ডিফিউজড ক্রোমোজোম"],
        "C", "medium", "factual",
        "SAT (satellite) chromosomes bear a secondary constriction and satellite.",
        "স্যাট ক্রোমোজোমে সেকেন্ডারি কনস্ট্রিকশন ও স্যাটেলাইট থাকে।",
    ),
    q(
        "What is removed from pre-mRNA to make mature mRNA?",
        "Pre-mRNA থেকে পরিণত mRNA তৈরিতে কোনটি বাদ যায়?",
        ["Exon", "Cistron", "Intron", "Recon"],
        ["এক্সন", "সিসট্রন", "ইন্ট্রন", "রেকন"],
        "C", "easy", "factual",
        "Splicing removes introns and joins exons in eukaryotic pre-mRNA.",
        "স্প্লাইসিং-এ ইন্ট্রন বাদ দিয়ে এক্সনগুলো জোড়া লাগে।",
    ),
    q(
        "Nucleoplasm is also known as:",
        "নিউক্লিওপ্লাজম অন্য নামে পরিচিত:",
        ["Karyolymph", "Ectoplasm", "Protoplasm (entire cell)", "Endoplasm only"],
        ["ক্যারিওলিম্ফ", "এক্টোপ্লাজম", "সমগ্র কোষের প্রোটোপ্লাজম", "কেবল এন্ডোপ্লাজম"],
        "A", "easy", "factual",
        "Nucleoplasm (karyolymph) is the nuclear ground substance.",
        "নিউক্লিওপ্লাজম (ক্যারিওলিম্ফ) নিউক্লিয়াসের ভিত্তিমাধ্যম।",
    ),
    q(
        "How many nitrogenous bases are in an anticodon?",
        "একটি অ্যান্টিকোডনে কতটি নাইট্রোজেন ক্ষারক থাকে?",
        ["2 bases", "3 bases", "4 bases", "5 bases"],
        ["২টি ক্ষারক", "৩টি ক্ষারক", "৪টি ক্ষারক", "৫টি ক্ষারক"],
        "B", "easy", "factual",
        "An anticodon is a triplet of three bases on tRNA complementary to an mRNA codon.",
        "অ্যান্টিকোডন tRNA-এর তিন ক্ষারকের ট্রিপলেট যা mRNA কোডনের পরিপূরক।",
    ),
    q(
        "Which base is absent from RNA chains?",
        "RNA শিকলে অনুপস্থিত কোনটি?",
        ["Adenine", "Guanine", "Thymine", "Cytosine"],
        ["অ্যাডেনিন", "গুয়ানিন", "থাইমিন", "সাইটোসিন"],
        "C", "easy", "factual",
        "RNA uses uracil instead of thymine.",
        "RNA-তে থাইমিনের পরিবর্তে ইউরাসিল থাকে।",
    ),
    q(
        "Which nitrogenous base pairs only with DNA (not typically as RNA’s U)?",
        "কোন নাইট্রোজেন ক্ষারক প্রধানত DNA-এর সাথে যুক্ত (RNA-এর U নয়)?",
        ["Adenine", "Guanine", "Thymine", "Uracil"],
        ["অ্যাডেনিন", "গুয়ানিন", "থাইমিন", "ইউরাসিল"],
        "C", "easy", "factual",
        "Thymine is characteristic of DNA; RNA has uracil instead.",
        "থাইমিন DNA-এর বৈশিষ্ট্য; RNA-তে ইউরাসিল থাকে।",
    ),
    q(
        "What is the initiator codon?",
        "সূচনাকারী কোডন কোনটি?",
        ["AUG", "UUU", "UAG", "UGA"],
        ["AUG (মেথায়োনিন)", "UUU (ফিনাইলঅ্যালানিন)", "UAG (স্টপ)", "UGA (স্টপ)"],
        "A", "easy", "factual",
        "AUG codes for methionine and usually starts translation.",
        "AUG মেথায়োনিন কোড করে এবং সাধারণত অনুবাদ শুরু করে।",
    ),
    q(
        "DNA → mRNA formation is called:",
        "DNA থেকে mRNA তৈরির প্রক্রিয়াকে কী বলে?",
        ["Replication", "Mutation", "Transcription", "Translation"],
        ["রেপ্লিকেশন", "মিউটেশন", "ট্রান্সক্রিপশন", "ট্রান্সলেশন"],
        "C", "easy", "factual",
        "Transcription copies genetic information from DNA into RNA.",
        "ট্রান্সক্রিপশনে DNA থেকে RNA-তে জেনেটিক তথ্য নকল হয়।",
    ),
    q(
        "Which enzyme unwinds the DNA double helix?",
        "DNA দ্বিসূত্রক খুলতে সাহায্য করে কোন এনজাইম?",
        ["Helicase", "Polymerase", "Lipase", "Isomerase"],
        ["হেলিকেজ", "পলিমারেজ", "লাইপেজ", "আইসোমারেজ"],
        "A", "easy", "factual",
        "Helicase breaks hydrogen bonds and unwinds DNA at the replication fork.",
        "হেলিকেজ হাইড্রোজেন বন্ধন ভেঙে রেপ্লিকেশন ফর্কে DNA খোলে।",
    ),
    q(
        "Which enzyme joins DNA fragments (e.g., Okazaki fragments)?",
        "DNA খণ্ড জোড়াতে ব্যবহৃত হয় কোন এনজাইম?",
        ["Restriction enzyme", "Helicase", "Polymerase", "Ligase"],
        ["রেস্ট্রিকশন এনজাইম", "হেলিকেজ", "পলিমারেজ", "লাইগেজ"],
        "D", "easy", "factual",
        "DNA ligase seals nicks by forming phosphodiester bonds.",
        "DNA লাইগেজ ফসফোডায়েস্টার বন্ধন গঠন করে কাটা স্থান জোড়ে।",
    ),
    q(
        "The brain of the cell is commonly called the:",
        "কোষের মস্তিষ্ক বলা হয় কোনটিকে?",
        ["Nucleus", "Mitochondrion", "Ribosome", "Centrosome"],
        ["নিউক্লিয়াস", "মাইটোকন্ড্রিয়া", "রাইবোসোম", "সেন্ট্রোসোম"],
        "A", "easy", "factual",
        "The nucleus controls cellular activities via genetic information.",
        "নিউক্লিয়াস জেনেটিক তথ্য দিয়ে কোষীয় কার্যক্রম নিয়ন্ত্রণ করে।",
    ),
    q(
        "Onion (Allium) chromosome number is commonly cited as:",
        "পিয়াজের ক্রোমোজোম সংখ্যা সাধারণত কত বলা হয়?",
        ["12 chromosomes", "14 chromosomes", "16 chromosomes", "18 chromosomes"],
        ["১২টি ক্রোমোজোম", "১৪টি ক্রোমোজোম", "১৬টি ক্রোমোজোম", "১৮টি ক্রোমোজোম"],
        "C", "medium", "factual",
        "Allium cepa typically has 2n = 16 chromosomes in HSC references.",
        "অ্যালিয়াম সিপা-এর 2n = ১৬ ক্রোমোজোম এইচএসসি তথ্যে উল্লেখিত।",
    ),
    q(
        "Rice chromosome number (2n) is commonly:",
        "ধানের ক্রোমোজোম সংখ্যা (2n) সাধারণত:",
        ["24 chromosomes", "28 chromosomes", "40 chromosomes", "48 chromosomes"],
        ["২৪টি ক্রোমোজোম", "২৮টি ক্রোমোজোম", "৪০টি ক্রোমোজোম", "৪৮টি ক্রোমোজোম"],
        "A", "medium", "factual",
        "Oryza sativa commonly has 2n = 24.",
        "ওরাইজা স্যাটিভা-এর 2n সাধারণত ২৪।",
    ),
    q(
        "Which molecule is known as the master molecule?",
        "মাস্টার মলিকিউল নামে পরিচিত কোনটি?",
        ["DNA", "RNA", "Protein", "Carbohydrate"],
        ["ডিএনএ (DNA)", "আরএনএ (RNA)", "প্রোটিন", "কার্বোহাইড্রেট"],
        "A", "easy", "factual",
        "DNA stores hereditary information and is called the master molecule.",
        "DNA বংশগতির তথ্য ধারণ করে বলে মাস্টার মলিকিউল বলা হয়।",
    ),
    q(
        "The smallest DNA segment participating in recombination is called a:",
        "রিকম্বিনেশনে অংশ নেওয়া DNA-এর ক্ষুদ্রতম অংশকে বলে:",
        ["Muton", "Replicon", "Recon", "Cistron"],
        ["মিউটন", "রেপ্লিকন", "রেকন", "সিসট্রন"],
        "C", "hard", "factual",
        "In classical gene structure terms: recon (recombination), muton (mutation), cistron (function).",
        "ক্লাসিক্যাল পরিভাষায়: রেকন (রিকম্বিনেশন), মিউটন (মিউটেশন), সিসট্রন (কাজ)।",
    ),
    q(
        "PCR correctly expands as:",
        "PCR-এর সঠিক পূর্ণরূপ কী?",
        [
            "Peptide Chain Reaction",
            "Polysaccharide Chain Reaction",
            "Polyribosome Chain Reaction",
            "Polymerase Chain Reaction",
        ],
        [
            "পেপটাইড চেইন রিঅ্যাকশন",
            "পলিস্যাকারাইড চেইন রিঅ্যাকশন",
            "পলিরাইবোসোম চেইন রিঅ্যাকশন",
            "পলিমারেজ চেইন রিঅ্যাকশন",
        ],
        "D", "easy", "factual",
        "PCR is Polymerase Chain Reaction, amplifying DNA using DNA polymerase.",
        "PCR হলো Polymerase Chain Reaction—DNA পলিমারেজ দিয়ে DNA বৃদ্ধি।",
    ),
    q(
        "At the kinetochore of a chromosome:",
        "ক্রোমোজোমের কাইনেটোকোরে:",
        [
            "Nucleolus is formed",
            "Microtubules attach",
            "Only satellites are always present",
            "Only junk DNA is stored exclusively",
        ],
        [
            "নিউক্লিওলাস তৈরি হয়",
            "মাইক্রোটিউবিউল যুক্ত হয়",
            "সবসময় কেবল স্যাটেলাইট থাকে",
            "কেবল জাঙ্ক DNA সঞ্চিত থাকে",
        ],
        "B", "medium", "conceptual",
        "Spindle microtubules attach at the kinetochore for chromosome movement.",
        "কাইনেটোকোরে মাকুতন্তুর মাইক্রোটিউবিউল যুক্ত হয়ে ক্রোমোজোম চালনা করে।",
    ),
    q(
        "Which carries the genetic code from DNA for protein synthesis?",
        "প্রোটিন সংশ্লেষণের জন্য DNA থেকে জেনেটিক কোড বহন করে কোনটি?",
        ["mRNA", "Only rRNA structural core without message", "Only histone H1", "Only cellulose"],
        ["এমআরএনএ (mRNA)", "কেবল বার্তাহীন rRNA কাঠামো", "কেবল হিস্টোন H1", "কেবল সেলুলোজ"],
        "A", "easy", "conceptual",
        "mRNA carries the transcribed codon sequence that directs polypeptide assembly.",
        "mRNA ট্রান্সক্রাইবড কোডন বহন করে পলিপেপটাইড গঠন নির্দেশ করে।",
    ),
]


TOPICS_MAP = {
    "bio1_27_ch01_t01": T01,
    "bio1_27_ch01_t02": T02,
    "bio1_27_ch01_t03": T03,
}


def write_topic(topic_id: str, rows: list[dict]) -> None:
    assert len(rows) == 20, f"{topic_id}: expected 20, got {len(rows)}"
    for i, row in enumerate(rows, 1):
        err = validate_record(row)
        if err:
            raise SystemExit(f"{topic_id} Q{i}: {err}\n{json.dumps(row, ensure_ascii=False)}")
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
    summary = {
        "chapter": "bio1_27_ch01",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p052_pdf058.png",
            "p053_pdf059.png",
            "p054_pdf060.png",
            "p055_pdf061.png",
            "p056_pdf062.png",
            "p057_pdf063.png",
            "p058_pdf064.png",
            "p059_pdf065.png",
            "p060_pdf066.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio1_27_ch01_t01": {
                "title": "Cell wall and membrane / কোষপ্রাচীর ও কোষঝিল্লি",
                "themes": [
                    "middle lamella/pectin",
                    "plasma membrane fluid mosaic",
                    "glycocalyx",
                    "cellulose/chitin/suberin",
                    "tonoplast/vacuole",
                    "plasmodesmata",
                ],
            },
            "bio1_27_ch01_t02": {
                "title": "Cell organelles / কোষীয় অঙ্গাণু",
                "themes": [
                    "Golgi/lipochondria",
                    "mitochondria/chloroplast",
                    "lysosome/autophagy",
                    "ribosome/ER",
                    "centriole",
                    "endosymbiont DNA",
                ],
            },
            "bio1_27_ch01_t03": {
                "title": "Nucleus and chromosomes / নিউক্লিয়াস ও ক্রোমোজোম",
                "themes": [
                    "codons/anticodons",
                    "transcription/replication enzymes",
                    "SAT chromosomes",
                    "introns/splicing",
                    "chromosome counts",
                    "master molecule DNA",
                ],
            },
        },
        "low_confidence": [
            "Diagram-linked bank items rewritten as standalone bilingual stems for bank import.",
            "Q numbering in source bank spans ~01–140; curated subset mapped to syllabus topics.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
        },
    }
    out = (
        ROOT
        / "content"
        / "bank"
        / "udvash_raw"
        / "biology_1"
        / "parsed"
        / "ch01_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
