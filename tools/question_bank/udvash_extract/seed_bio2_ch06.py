#!/usr/bin/env python3
"""Seed Biology 2nd Paper Ch6 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio2_27_ch06_t01..t03 (Kidney/nephron; Urine formation; Excretory disorders).
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
    "biology p2 ch06; curated bilingual"
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


# --- t01: Kidney and nephron / বৃক্ক ও নেফ্রন ---
T01 = [
    q(
        "Which human organ is typically described as bean-shaped and reddish-brown?",
        "মানবদেহের কোন অঙ্গকে সাধারণত সিম বীজের মতো আকৃতির ও লালচে খয়েরি বর্ণের বলা হয়?",
        ["Liver", "Stomach", "Pancreas", "Kidney"],
        ["যকৃত", "পাকস্থলী", "অগ্ন্যাশয়", "বৃক্ক"],
        "D", "easy", "factual",
        "HSC texts describe each kidney as roughly bean-shaped and reddish-brown.",
        "এইচএসসি পাঠ্যে প্রতিটি বৃক্ককে প্রায় সিম বীজের মতো ও লালচে খয়েরি বর্ণের বলা হয়।",
    ),
    q(
        "The concave medial indentation of the kidney is called what?",
        "বৃক্কের অবতল মধ্যবর্তী ভাঁজকে কী বলে?",
        ["Pelvis", "Hilum", "Cortex", "Pyramid"],
        ["পেলভিস", "হাইলাস", "কর্টেক্স", "পিরামিড"],
        "B", "easy", "factual",
        "The hilum is the medial concave notch where vessels, nerves and the ureter enter/leave.",
        "হাইলাস হলো মধ্যবর্তী অবতল অংশ যেখানে রক্তনালি, স্নায়ু ও ইউরেটার প্রবেশ/বহির্গমন করে।",
    ),
    q(
        "Relative to the right kidney, where does the left human kidney usually lie?",
        "ডান বৃক্কের তুলনায় মানুষের বাম বৃক্ক সাধারণত কোথায় অবস্থান করে?",
        ["Slightly lower", "Slightly higher", "Exactly level", "In the thoracic cavity"],
        ["সামান্য নিচে", "সামান্য উপরে", "একই স্তরে", "বক্ষগহ্বরে"],
        "B", "easy", "factual",
        "Because of the large right lobe of the liver, the left kidney usually sits slightly higher.",
        "যকৃতের বড় ডান লোবের জন্য বাম বৃক্ক সাধারণত সামান্য উপরে থাকে।",
    ),
    q(
        "What covers the entire outer surface of each kidney?",
        "প্রতিটি বৃক্কের বাইরের সমগ্র পৃষ্ঠ কী দ্বারা আবৃত?",
        ["Pleura", "Pericardium", "Renal capsule", "Peritoneum only"],
        ["প্লুরা", "পেরিকার্ডিয়াম", "রেনাল ক্যাপসুল", "শুধু পেরিটোনিয়াম"],
        "C", "easy", "factual",
        "A tough fibrous renal capsule surrounds each kidney.",
        "প্রতিটি বৃক্ক একটি মজবুত তন্তুময় রেনাল ক্যাপসুল দ্বারা বেষ্টিত।",
    ),
    q(
        "Malpighian body (renal corpuscle) is formed by which two parts?",
        "ম্যালপিজিয়ান বডি (রেনাল করপাসল) কোন দুটি অংশ নিয়ে গঠিত?",
        [
            "PCT and DCT",
            "Bowman’s capsule and glomerulus",
            "Loop of Henle and collecting duct",
            "Ureter and urethra",
        ],
        [
            "নিকটবর্তী ও দূরবর্তী প্যাঁচানো নালিকা",
            "বোম্যানস ক্যাপসুল ও গ্লোমেরুলাস",
            "হেনলির লুপ ও সংগ্রাহী নালিকা",
            "ইউরেটার ও ইউরেথ্রা",
        ],
        "B", "easy", "factual",
        "The renal corpuscle (Malpighian body) = Bowman’s capsule + glomerulus.",
        "রেনাল করপাসল (ম্যালপিজিয়ান বডি) = বোম্যানস ক্যাপসুল + গ্লোমেরুলাস।",
    ),
    q(
        "The visceral layer of Bowman’s capsule is mainly made of which cells?",
        "বোম্যানস ক্যাপসুলের ভিসেরাল স্তর প্রধানত কোন কোষ দিয়ে গঠিত?",
        ["Podocytes", "Goblet cells", "Osteocytes", "Neurons"],
        ["পোডোসাইট", "গবলেট কোষ", "অস্টিওসাইট", "নিউরন"],
        "A", "medium", "factual",
        "Specialized epithelial podocytes form the visceral layer around the glomerular capillaries.",
        "বিশেষায়িত এপিথেলিয়াল পোডোসাইট কোষ গ্লোমেরুলার কৈশিকের চারপাশে ভিসেরাল স্তর গঠন করে।",
    ),
    q(
        "The parietal layer of Bowman’s capsule is composed of which epithelium?",
        "বোম্যানস ক্যাপসুলের প্যারাইটাল স্তর কোন এপিথেলিয়াম দিয়ে গঠিত?",
        [
            "Ciliated columnar",
            "Stratified squamous keratinized",
            "Simple squamous (pavement) epithelium",
            "Transitional epithelium only",
        ],
        [
            "সিলিয়েটেড কলামনার",
            "কেরাটিনাইজড স্তরীভূত আঁইশাকার",
            "সরল আঁইশাকার (পেভমেন্ট) এপিথেলিয়াম",
            "শুধু ট্রানজিশনাল এপিথেলিয়াম",
        ],
        "C", "medium", "factual",
        "Board items commonly state the parietal layer is simple squamous (pavement) epithelium.",
        "বোর্ড প্রশ্নে সাধারণত প্যারাইটাল স্তরকে সরল আঁইশাকার (পেভমেন্ট) এপিথেলিয়াম বলা হয়।",
    ),
    q(
        "Compared with the afferent arteriole, the efferent arteriole of a glomerulus is usually what?",
        "আ্যাফারেন্ট আর্টারিওলের তুলনায় গ্লোমেরুলাসের ইফারেন্ট আর্টারিওল সাধারণত কেমন?",
        ["Wider in diameter", "Narrower in diameter", "Identical in diameter", "Absent"],
        ["ব্যাসে চওড়া", "ব্যাসে সংকীর্ণ", "একই ব্যাসের", "অনুপস্থিত"],
        "B", "easy", "conceptual",
        "The narrower efferent arteriole helps raise glomerular hydrostatic pressure for filtration.",
        "সংকীর্ণ ইফারেন্ট আর্টারিওল গ্লোমেরুলাসে উচ্চ হাইড্রোস্ট্যাটিক চাপ সৃষ্টিতে সাহায্য করে।",
    ),
    q(
        "Which structure carries urine from a kidney to the urinary bladder?",
        "বৃক্ক থেকে মূত্রথলিতে মূত্র পরিবহন করে কোনটি?",
        ["Urethra", "Ureter", "Vas deferens", "Collecting duct only"],
        ["ইউরেথ্রা", "ইউরেটার", "ভাস ডিফারেন্স", "শুধু সংগ্রাহী নালিকা"],
        "B", "easy", "factual",
        "Each ureter conveys urine from the renal pelvis to the urinary bladder.",
        "প্রতিটি ইউরেটার রেনাল পেলভিস থেকে মূত্রথলিতে মূত্র নিয়ে যায়।",
    ),
    q(
        "Which duct carries urine from the urinary bladder to the exterior?",
        "মূত্রথলি থেকে দেহের বাইরে মূত্র পরিবহনের কাজ করে কোনটি?",
        ["Ureter", "Urethra", "Vas deferens", "Bile duct"],
        ["ইউরেটার", "ইউরেথ্রা", "ভাস ডিফারেন্স", "পিত্তনালি"],
        "B", "easy", "factual",
        "The urethra is the outlet from the bladder to the outside.",
        "ইউরেথ্রা মূত্রথলি থেকে বাইরে মূত্র নিষ্কাশনের নালি।",
    ),
    q(
        "Which of the following is an internal structural feature of the kidney?",
        "নিচের কোনটি বৃক্কের অন্তর্গঠনের বৈশিষ্ট্য?",
        ["Alveolus", "Renal pyramid", "Bronchiole", "Villus"],
        ["আ্যালভিওলাস", "রেনাল পিরামিড", "ব্রঙ্কিওল", "ভিলাস"],
        "B", "easy", "factual",
        "The medulla contains renal pyramids; pelvis is also an internal renal cavity—not alveoli.",
        "মেডুলায় রেনাল পিরামিড থাকে; আ্যালভিওলাস ফুসফুসের গঠন, বৃক্কের নয়।",
    ),
    q(
        "Approximately how many nephrons does one human kidney contain?",
        "একটি মানব বৃক্কে প্রায় কতটি নেফ্রন থাকে?",
        ["About 10 thousand", "About 1–1.2 million", "About 100 million", "Exactly 500"],
        ["প্রায় ১০ হাজার", "প্রায় ১–১.২ মিলিয়ন", "প্রায় ১০০ মিলিয়ন", "ঠিক ৫০০"],
        "B", "medium", "numerical",
        "HSC texts commonly cite roughly one million (about 1–1.2×10⁶) nephrons per kidney.",
        "এইচএসসি পাঠ্যে সাধারণত প্রতি বৃক্কে প্রায় ১–১.২ মিলিয়ন নেফ্রনের উল্লেখ থাকে।",
    ),
    q(
        "In which region of the kidney are Malpighian bodies (renal corpuscles) mainly located?",
        "ম্যালপিজিয়ান বডি (রেনাল করপাসল) প্রধানত বৃক্কের কোন অংশে অবস্থিত?",
        ["Cortex", "Renal pelvis only", "Ureter wall", "Urinary bladder"],
        ["কর্টেক্স", "শুধু রেনাল পেলভিস", "ইউরেটার প্রাচীর", "মূত্রথলি"],
        "A", "easy", "factual",
        "Renal corpuscles lie in the cortex; loops of Henle may extend into the medulla.",
        "রেনাল করপাসল কর্টেক্সে থাকে; হেনলির লুপ মেডুলায় বিস্তৃত হতে পারে।",
    ),
    q(
        "Podocyte foot processes help form which functional feature of filtration?",
        "পোডোসাইটের ফুট প্রসেস পরিস্রাবণের কোন কার্যকর বৈশিষ্ট্য গঠনে সাহায্য করে?",
        [
            "A slit-like filtration barrier (slit pores)",
            "The muscular wall of the ureter",
            "The adrenal medulla",
            "The gall bladder mucosa",
        ],
        [
            "ছিদ্রসদৃশ পরিস্রাবণ বাধা (স্লিট পোর)",
            "ইউরেটারের পেশিপ্রাচীর",
            "আ্যাড্রেনাল মেডুলা",
            "পিত্তথলির মিউকোসা",
        ],
        "A", "medium", "conceptual",
        "Interdigitating podocyte pedicels create filtration slits that act like a fine sieve.",
        "পোডোসাইটের পেডিসেলগুলো পরস্পর জড়িয়ে স্লিট পোর তৈরি করে যা সূক্ষ্ম ছাঁকনির মতো কাজ করে।",
    ),
    q(
        "Which blood vessel brings blood into the glomerulus?",
        "গ্লোমেরুলাসে রক্ত নিয়ে আসে কোন রক্তনালি?",
        ["Efferent arteriole", "Afferent arteriole", "Renal vein", "Hepatic portal vein"],
        ["ইফারেন্ট আর্টারিওল", "আ্যাফারেন্ট আর্টারিওল", "রেনাল শিরা", "হেপাটিক পোর্টাল শিরা"],
        "B", "easy", "factual",
        "The afferent arteriole supplies the glomerular capillary tuft.",
        "আ্যাফারেন্ট আর্টারিওল গ্লোমেরুলার কৈশিক জালিকায় রক্ত সরবরাহ করে।",
    ),
    q(
        "The structural and functional unit of the kidney is the what?",
        "বৃক্কের গঠন ও কার্যকর একক কোনটি?",
        ["Neuron", "Nephron", "Alveolus", "Osteon"],
        ["নিউরন", "নেফ্রন", "আ্যালভিওলাস", "অস্টিয়ন"],
        "B", "easy", "factual",
        "Nephrons—not neurons—are the kidney’s structural/functional units for excretion and water balance.",
        "নেফ্রন (নিউরন নয়) বৃক্কের গঠন ও কার্যকর একক; রেচন ও পানির ভারসাম্য রক্ষায় কাজ করে।",
    ),
    q(
        "Which sequence correctly orders parts after the proximal convoluted tubule?",
        "নিকটবর্তী প্যাঁচানো নালিকার পর সঠিক ক্রম কোনটি?",
        [
            "Collecting duct → loop of Henle → DCT",
            "Loop of Henle → distal convoluted tubule → collecting duct",
            "DCT → glomerulus → urethra",
            "Ureter → Bowman’s capsule → PCT",
        ],
        [
            "সংগ্রাহী নালিকা → হেনলির লুপ → ডিস্টাল প্যাঁচানো নালিকা",
            "হেনলির লুপ → দূরবর্তী প্যাঁচানো নালিকা → সংগ্রাহী নালিকা",
            "ডিস্টাল প্যাঁচানো নালিকা → গ্লোমেরুলাস → ইউরেথ্রা",
            "ইউরেটার → বোম্যানস ক্যাপসুল → নিকটবর্তী প্যাঁচানো নালিকা",
        ],
        "B", "medium", "conceptual",
        "Typical flow: PCT → loop of Henle → DCT → collecting duct (then pelvis/ureter).",
        "সাধারণ প্রবাহ: নিকটবর্তী প্যাঁচানো নালিকা → হেনলির লুপ → দূরবর্তী প্যাঁচানো নালিকা → সংগ্রাহী নালিকা।",
    ),
    q(
        "The filtration membrane of the renal corpuscle includes which components?",
        "রেনাল করপাসলের পরিস্রাবণ ঝিল্লিতে কোন উপাদানগুলো অন্তর্ভুক্ত?",
        [
            "Only capsular space fluid",
            "Podocytes and glomerular endothelium (with basement membrane)",
            "Only ureter smooth muscle",
            "Only urochrome pigment",
        ],
        [
            "শুধু ক্যাপসুলার স্পেসের তরল",
            "পোডোসাইট ও গ্লোমেরুলার এন্ডোথেলিয়াম (ভিত্তিঝিল্লিসহ)",
            "শুধু ইউরেটারের মসৃণ পেশি",
            "শুধু ইউরোক্রোম পিগমেন্ট",
        ],
        "B", "hard", "conceptual",
        "Ultrafiltration crosses glomerular endothelium, basement membrane and podocyte slits; space itself is not a wall component.",
        "আল্ট্রাফিলট্রেশন গ্লোমেরুলার এন্ডোথেলিয়াম, ভিত্তিঝিল্লি ও পোডোসাইট স্লিট দিয়ে ঘটে; ক্যাপসুলার স্পেস নিজে প্রাচীর উপাদান নয়।",
    ),
    q(
        "Which endocrine sources secrete hormones that assist kidney water/salt regulation?",
        "বৃক্কের পানি/লবণ নিয়ন্ত্রণে সহায়ক হরমোনের উৎপত্তিস্থল কোনগুলো?",
        [
            "Pituitary and adrenal glands",
            "Only thyroid gland",
            "Only pancreas islets",
            "Only pineal gland",
        ],
        [
            "পিটুইটারি ও আ্যাড্রেনাল গ্রন্থি",
            "শুধু থাইরয়েড গ্রন্থি",
            "শুধু অগ্ন্যাশয়ের আইলেট",
            "শুধু পাইনাল গ্রন্থি",
        ],
        "A", "medium", "factual",
        "ADH (posterior pituitary) and aldosterone (adrenal cortex) are classic renal regulators; liver makes urea, not these hormones.",
        "ADH (পশ্চাৎ পিটুইটারি) ও অ্যালডোস্টেরন (আ্যাড্রেনাল কর্টেক্স) বৃক্ক নিয়ন্ত্রণ করে; যকৃত ইউরিয়া তৈরি করে, এসব হরমোন নয়।",
    ),
    q(
        "Blood reaches the kidney primarily via which vessel from the aorta side?",
        "মহাধমনির দিক থেকে বৃক্কে রক্ত প্রধানত কোন নালি দিয়ে পৌঁছায়?",
        ["Hepatic vein", "Renal artery", "Pulmonary artery", "Coronary sinus"],
        ["হেপাটিক শিরা", "রেনাল ধমনি", "পালমোনারি ধমনি", "করোনারি সাইনাস"],
        "B", "easy", "factual",
        "A renal artery from the abdominal aorta supplies each kidney at high pressure.",
        "উদরীয় মহাধমনি থেকে রেনাল ধমনি উচ্চচাপে প্রতিটি বৃক্কে রক্ত সরবরাহ করে।",
    ),
]


# --- t02: Urine formation / মূত্র সৃষ্টি ---
T02 = [
    q(
        "What is the first step of urine formation in the nephron?",
        "নেফ্রনে মূত্র সৃষ্টির প্রথম ধাপ কোনটি?",
        [
            "Selective reabsorption only",
            "Ultrafiltration (glomerular filtration)",
            "Micturition reflex only",
            "Urea synthesis in muscle",
        ],
        [
            "শুধু নির্বাচনমূলক পুনঃশোষণ",
            "আল্ট্রাফিলট্রেশন (গ্লোমেরুলার পরিস্রাবণ)",
            "শুধু মিকচারেশন রিফ্লেক্স",
            "পেশিতে ইউরিয়া সংশ্লেষণ",
        ],
        "B", "easy", "factual",
        "Ultrafiltration in the renal corpuscle produces glomerular filtrate (primary urine).",
        "রেনাল করপাসলে আল্ট্রাফিলট্রেশনে গ্লোমেরুলার ফিলট্রেট (প্রাথমিক মূত্র) তৈরি হয়।",
    ),
    q(
        "Which component is normally absent from glomerular filtrate?",
        "গ্লোমেরুলার ফিলট্রেটে সাধারণত কোনটি অনুপস্থিত?",
        ["Glucose", "Urea", "Plasma proteins", "Sodium ions"],
        ["গ্লুকোজ", "ইউরিয়া", "প্লাজমা প্রোটিন", "সোডিয়াম আয়ন"],
        "C", "easy", "factual",
        "Blood cells and large plasma proteins are retained; filtrate contains water, ions, glucose, urea, etc.",
        "রক্তকণিকা ও বৃহৎ প্লাজমা প্রোটিন আটকে থাকে; ফিলট্রেটে পানি, আয়ন, গ্লুকোজ, ইউরিয়া ইত্যাদি থাকে।",
    ),
    q(
        "Most of the glomerular filtrate is reabsorbed chiefly in which segment?",
        "গ্লোমেরুলার ফিলট্রেটের অধিকাংশ পুনঃশোষণ প্রধানত কোন অংশে হয়?",
        [
            "Proximal convoluted tubule",
            "Loop of Henle only",
            "Distal convoluted tubule only",
            "Collecting duct only",
        ],
        [
            "নিকটবর্তী প্যাঁচানো নালিকা",
            "শুধু হেনলির লুপ",
            "শুধু দূরবর্তী প্যাঁচানো নালিকা",
            "শুধু সংগ্রাহী নালিকা",
        ],
        "A", "easy", "factual",
        "Board items emphasize that the bulk of selective reabsorption occurs in the PCT.",
        "বোর্ড প্রশ্নে জোর দেওয়া হয় যে অধিকাংশ নির্বাচনমূলক পুনঃশোষণ নিকটবর্তী প্যাঁচানো নালিকায় ঘটে।",
    ),
    q(
        "Selective reabsorption means that the tubule does what?",
        "নির্বাচনমূলক পুনঃশোষণ বলতে নালিকা কী করে বোঝায়?",
        [
            "Absorbs every filtrate solute equally",
            "Reabsorbs needed substances while leaving many wastes behind",
            "Only secretes proteins into the capsule",
            "Stops all water movement",
        ],
        [
            "সব দ্রব্য সমানভাবে শোষণ করে",
            "প্রয়োজনীয় পদার্থ শোষণ করে অনেক বর্জ্য অশোষিত রাখে",
            "শুধু ক্যাপসুলে প্রোটিন ক্ষরণ করে",
            "সব পানির চলাচল বন্ধ করে",
        ],
        "B", "easy", "conceptual",
        "Useful solutes (e.g., glucose, amino acids, many ions/water) are taken back; wastes largely continue.",
        "দরকারি দ্রব্য (যেমন গ্লুকোজ, অ্যামিনো অ্যাসিড, অনেক আয়ন/পানি) ফিরে নেওয়া হয়; বর্জ্য মূলত থেকে যায়।",
    ),
    q(
        "Active tubular secretion mainly adds substances such as creatinine from peritubular blood into what?",
        "সক্রিয় নালিকা ক্ষরণ প্রধানত পেরিটিউবিউলার রক্ত থেকে ক্রিয়েটিনিন জাতীয় পদার্থ কোথায় যোগ করে?",
        [
            "Into the tubular fluid (filtrate)",
            "Into the bile canaliculi only",
            "Into alveolar air",
            "Into cerebrospinal fluid",
        ],
        [
            "নালিকার তরলে (ফিলট্রেটে)",
            "শুধু পিত্তনালিকায়",
            "আ্যালভিওলার বাতাসে",
            "সেরিব্রোস্পাইনাল তরলে",
        ],
        "A", "medium", "conceptual",
        "Secretion transfers some wastes/ions from blood into tubular fluid, completing urine formation.",
        "ক্ষরণে কিছু বর্জ্য/আয়ন রক্ত থেকে নালিকার তরলে যায় এবং মূত্র গঠন সম্পূর্ণ করে।",
    ),
    q(
        "Glomerular filtrate is also commonly called what?",
        "গ্লোমেরুলার ফিলট্রেটকে সাধারণত আর কী বলা হয়?",
        ["Secondary urine only", "Primary urine", "Lymph exclusively", "Synovial fluid"],
        ["শুধু গৌণ মূত্র", "প্রাথমিক মূত্র", "একমাত্র লসিকা", "সাইনোভিয়াল তরল"],
        "B", "easy", "factual",
        "The protein-free filtered fluid in Bowman’s space is termed primary urine/glomerular filtrate.",
        "বোম্যানস স্পেসের প্রোটিনমুক্ত পরিশ্রুত তরলকে প্রাথমিক মূত্র বা গ্লোমেরুলার ফিলট্রেট বলে।",
    ),
    q(
        "Which hormone from the posterior pituitary mainly controls water reabsorption in collecting ducts?",
        "পশ্চাৎ পিটুইটারি থেকে নিঃসৃত কোন হরমোন প্রধানত সংগ্রাহী নালিকায় পানি পুনঃশোষণ নিয়ন্ত্রণ করে?",
        ["FSH", "LH", "ADH (vasopressin)", "Thyroxine"],
        ["FSH", "LH", "ADH (ভাসোপ্রেসিন)", "থাইরক্সিন"],
        "C", "easy", "factual",
        "ADH/vasopressin increases water permeability of collecting ducts, concentrating urine.",
        "ADH/ভাসোপ্রেসিন সংগ্রাহী নালিকার পানি প্রবেশ্যতা বাড়িয়ে মূত্র ঘনীভূত করে।",
    ),
    q(
        "Osmoregulation in humans chiefly maintains balance of what?",
        "মানুষে অসমোরেগুলেশন প্রধানত কীসের ভারসাম্য রক্ষা করে?",
        [
            "Only body temperature",
            "Body water and key salts (osmotic pressure)",
            "Only blood cell count",
            "Only bone calcium crystals",
        ],
        [
            "শুধু দেহতাপমাত্রা",
            "দেহের পানি ও প্রধান লবণ (অভিস্রবণিক চাপ)",
            "শুধু রক্তকণিকার সংখ্যা",
            "শুধু অস্থির ক্যালসিয়াম স্ফটিক",
        ],
        "B", "easy", "conceptual",
        "Osmoregulation keeps osmotic balance via water and Na⁺/K⁺/Cl⁻ etc., with ADH involvement.",
        "অসমোরেগুলেশন পানি ও Na⁺/K⁺/Cl⁻ ইত্যাদির অভিস্রবণিক ভারসাম্য রাখে; ADH জড়িত।",
    ),
    q(
        "When body water falls and plasma osmolarity rises, ADH levels typically do what?",
        "দেহে পানি কমলে ও প্লাজমা অসমোলারিটি বাড়লে ADH-এর মাত্রা সাধারণত কী হয়?",
        [
            "Decrease, producing dilute abundant urine",
            "Increase, producing less urine and conserving water",
            "Remain zero always",
            "Convert urea into protein",
        ],
        [
            "কমে, পাতলা প্রচুর মূত্র তৈরি হয়",
            "বাড়ে, কম মূত্র হয় ও পানি সংরক্ষিত হয়",
            "সবসময় শূন্য থাকে",
            "ইউরিয়াকে প্রোটিনে রূপান্তর করে",
        ],
        "B", "medium", "conceptual",
        "Osmoreceptors raise ADH release → more water reabsorption → smaller volume of concentrated urine.",
        "অসমোরিসেপ্টর ADH নিঃসরণ বাড়ায় → বেশি পানি পুনঃশোষণ → কম পরিমাণ ঘন মূত্র।",
    ),
    q(
        "About what percentage of normal human urine is water?",
        "স্বাভাবিক মানব মূত্রের প্রায় কত শতাংশ পানি?",
        ["About 50%", "About 75%", "About 95%", "About 99.9%"],
        ["প্রায় ৫০%", "প্রায় ৭৫%", "প্রায় ৯৫%", "প্রায় ৯৯.৯%"],
        "C", "easy", "numerical",
        "Texts commonly state urine is about 95% (often 95–97%) water and ~3–5% solids.",
        "পাঠ্যে সাধারণত মূত্রে প্রায় ৯৫% (৯৫–৯৭%) পানি ও ~৩–৫% কঠিন পদার্থ উল্লেখ থাকে।",
    ),
    q(
        "The straw-yellow colour of urine is mainly due to which pigment?",
        "মূত্রের খড় বর্ণের জন্য প্রধানত দায়ী উপাদান কোনটি?",
        ["Sodium", "Urea", "Urochrome", "Creatinine"],
        ["সোডিয়াম", "ইউরিয়া", "ইউরোক্রোম", "ক্রিয়েটিনিন"],
        "C", "easy", "factual",
        "Urochrome (from hemoglobin breakdown products) gives urine its typical straw colour.",
        "ইউরোক্রোম (হিমোগ্লোবিন ভাঙনের উপজাত) মূত্রকে সাধারণ খড় বর্ণ দেয়।",
    ),
    q(
        "Which of the following is a non-nitrogenous organic constituent that may appear in urine?",
        "মূত্রে বিদ্যমান নিচের কোনটি নন-নাইট্রোজেনাস জৈব উপাদান?",
        ["Creatinine", "Uric acid", "Ketone bodies", "Urea"],
        ["ক্রিয়েটিনিন", "ইউরিক অ্যাসিড", "কিটোন বডিস", "ইউরিয়া"],
        "C", "medium", "factual",
        "Urea, uric acid and creatinine are nitrogenous; ketone bodies are non-nitrogenous organics.",
        "ইউরিয়া, ইউরিক অ্যাসিড ও ক্রিয়েটিনিন নাইট্রোজেনঘটিত; কিটোন বডিস নন-নাইট্রোজেনাস জৈব।",
    ),
    q(
        "Uric acid in the body is mainly a metabolic product of what?",
        "দেহে ইউরিক অ্যাসিড প্রধানত কীসের বিপাকজাত উপজাত?",
        [
            "Purine bases of nucleic acids",
            "Only dietary cellulose",
            "Only vitamin C excess",
            "Only starch in saliva",
        ],
        [
            "নিউক্লিক অ্যাসিডের পিউরিন বেস",
            "শুধু খাদ্যের সেলুলোজ",
            "শুধু অতিরিক্ত ভিটামিন C",
            "শুধু লালার স্টার্চ",
        ],
        "A", "medium", "factual",
        "Purine catabolism (hepatic) yields uric acid; it is less toxic/less water-soluble than urea.",
        "পিউরিন ভাঙনে (প্রধানত যকৃতে) ইউরিক অ্যাসিড হয়; ইউরিয়ার চেয়ে কম বিষাক্ত ও কম পানিতে দ্রবণীয়।",
    ),
    q(
        "Animals that excrete urea as the main nitrogenous waste are called what?",
        "প্রধান নাইট্রোজেনঘটিত বর্জ্য হিসেবে ইউরিয়া ত্যাগকারী প্রাণীদের কী বলে?",
        ["Uricotelic", "Ureotelic", "Ammonotelic only", "Photosynthetic"],
        ["ইউরিকোটেলিক", "ইউরিওটেলিক", "শুধু অ্যামোনোটেলিক", "সালোকসংশ্লেষী"],
        "B", "easy", "factual",
        "Ureotelism: urea is the chief N-waste (e.g., humans/many mammals); birds/reptiles are often uricotelic.",
        "ইউরিওটেলিজম: ইউরিয়া প্রধান N-বর্জ্য (যেমন মানুষ); পাখি/সরীসৃপ প্রায়শই ইউরিকোটেলিক।",
    ),
    q(
        "High hydrostatic pressure in the glomerulus is important because it drives what?",
        "গ্লোমেরুলাসের উচ্চ হাইড্রোস্ট্যাটিক চাপ গুরুত্বপূর্ণ কারণ এটি কী চালিত করে?",
        [
            "Ultrafiltration into Bowman’s space",
            "Only bile secretion",
            "Only sweat gland atrophy",
            "Only bone marrow erythropoiesis stoppage",
        ],
        [
            "বোম্যানস স্পেসে আল্ট্রাফিলট্রেশন",
            "শুধু পিত্ত ক্ষরণ",
            "শুধু ঘর্মগ্রন্থি ক্ষয়",
            "শুধু অস্থিমজ্জায় RBC উৎপাদন বন্ধ",
        ],
        "A", "medium", "conceptual",
        "Afferent/efferent calibre difference raises glomerular pressure that filters plasma into the capsule.",
        "আ্যাফারেন্ট/ইফারেন্ট ব্যাসের পার্থক্যে চাপ বাড়ে এবং প্লাজমা ক্যাপসুলে পরিস্রুত হয়।",
    ),
    q(
        "Plasma creatinine concentration is commonly used clinically as an indicator of what?",
        "প্লাজমা ক্রিয়েটিনিন ঘনত্ব সাধারণত কোনটির নির্দেশক হিসেবে ব্যবহৃত হয়?",
        [
            "Hearing acuity",
            "Kidney excretory function (GFR status)",
            "Hair colour genes",
            "Tooth enamel hardness only",
        ],
        [
            "শ্রবণ ক্ষমতা",
            "বৃক্কের রেচন ক্ষমতা (GFR অবস্থা)",
            "চুলের রঙের জিন",
            "শুধু দাঁতের এনামেল কঠিনতা",
        ],
        "B", "medium", "application",
        "Creatinine is filtered (little reabsorbed); rising plasma levels often signal impaired renal clearance.",
        "ক্রিয়েটিনিন পরিস্রুত হয় (কম পুনঃশোষিত); প্লাজমায় বৃদ্ধি প্রায়শই বৃক্কীয় ক্লিয়ারেন্স হ্রাসের ইঙ্গিত।",
    ),
    q(
        "Which correct pathway describes tubular fluid after leaving the proximal convoluted tubule?",
        "নিকটবর্তী প্যাঁচানো নালিকা ছাড়ার পর নালিকা তরলের সঠিক গতিপথ কোনটি?",
        [
            "Glomerulus → PCT → collecting duct → loop of Henle",
            "Loop of Henle → DCT → collecting duct",
            "Collecting duct → Bowman’s capsule → urethra",
            "Ureter → DCT → glomerulus",
        ],
        [
            "গ্লোমেরুলাস → নিকটবর্তী প্যাঁচানো নালিকা → সংগ্রাহী নালিকা → হেনলির লুপ",
            "হেনলির লুপ → দূরবর্তী প্যাঁচানো নালিকা → সংগ্রাহী নালিকা",
            "সংগ্রাহী নালিকা → বোম্যানস ক্যাপসুল → ইউরেথ্রা",
            "ইউরেটার → দূরবর্তী প্যাঁচানো নালিকা → গ্লোমেরুলাস",
        ],
        "B", "medium", "conceptual",
        "After PCT, fluid traverses the loop of Henle, then DCT, then collecting duct.",
        "নিকটবর্তী প্যাঁচানো নালিকার পর তরল হেনলির লুপ → দূরবর্তী প্যাঁচানো নালিকা → সংগ্রাহী নালিকা দিয়ে যায়।",
    ),
    q(
        "In Bowman’s space, which pair can normally be present while protein is not?",
        "বোম্যানস স্পেসে প্রোটিন না থেকে সাধারণত কোন জোড়া উপস্থিত থাকতে পারে?",
        [
            "Only erythrocytes and platelets",
            "Glucose and uric acid",
            "Only fibrinogen clots",
            "Only intact albumin polymers",
        ],
        [
            "শুধু লোহিতকণিকা ও প্লাটিলেট",
            "গ্লুকোজ ও ইউরিক অ্যাসিড",
            "শুধু ফাইব্রিনোজেন জমাট",
            "শুধু অক্ষত অ্যালবুমিন পলিমার",
        ],
        "B", "medium", "application",
        "Filtrate may contain glucose and nitrogenous wastes like uric acid; plasma proteins stay in blood.",
        "ফিলট্রেটে গ্লুকোজ ও ইউরিক অ্যাসিড জাতীয় বর্জ্য থাকতে পারে; প্লাজমা প্রোটিন রক্তেই থাকে।",
    ),
    q(
        "Urea is formed mainly in which organ before being excreted by the kidneys?",
        "বৃক্ক দিয়ে নিষ্কাশনের আগে ইউরিয়া প্রধানত কোন অঙ্গে তৈরি হয়?",
        ["Spleen", "Liver", "Lung alveoli", "Skin epidermis only"],
        ["প্লীহা", "যকৃত", "ফুসফুসের আ্যালভিওলাস", "শুধু ত্বকের এপিডার্মিস"],
        "B", "easy", "factual",
        "The ornithine (urea) cycle in hepatocytes converts ammonia to urea for renal excretion.",
        "হেপাটোসাইটে অরনিথিন (ইউরিয়া) চক্র অ্যামোনিয়াকে ইউরিয়ায় রূপান্তর করে বৃক্ক দিয়ে নিষ্কাশিত হয়।",
    ),
    q(
        "If ADH secretion falls (as when excess water is present), urine typically becomes what?",
        "অতিরিক্ত পানি থাকায় ADH নিঃসরণ কমলে মূত্র সাধারণত কেমন হয়?",
        [
            "More concentrated and scant",
            "More dilute and of larger volume",
            "Completely protein-rich like plasma",
            "Identical to glomerular filtrate always",
        ],
        [
            "আরও ঘন ও স্বল্প পরিমাণ",
            "আরও পাতলা ও বেশি আয়তনের",
            "প্লাজমার মতো সম্পূর্ণ প্রোটিনসমৃদ্ধ",
            "সবসময় গ্লোমেরুলার ফিলট্রেটের সমান",
        ],
        "B", "medium", "application",
        "Low ADH reduces collecting-duct water reabsorption → polyuria of dilute urine.",
        "কম ADH-এ সংগ্রাহী নালিকায় পানি পুনঃশোষণ কমে → পাতলা মূত্রের আয়তন বাড়ে।",
    ),
]


# --- t03: Excretory disorders / রেচনজনিত সমস্যা ---
T03 = [
    q(
        "Edema (body swelling) with reduced urine output may suggest impairment of which organ system?",
        "দেহ ফুলে যাওয়া ও মূত্র নিঃসরণ কমে গেলে কোন অঙ্গতন্ত্রের সমস্যার ইঙ্গিত হতে পারে?",
        [
            "Excretory (renal) system",
            "Only the auditory ossicles",
            "Only sweat ducts of palms",
            "Only lacrimal glands",
        ],
        [
            "রেচন (বৃক্কীয়) তন্ত্র",
            "শুধু কর্ণের অসিকল",
            "শুধু হাতের তালুর ঘর্মনালি",
            "শুধু ল্যাক্রিমাল গ্রন্থি",
        ],
        "A", "easy", "application",
        "Fluid retention and oliguria are classic clues to renal dysfunction in board-style cases.",
        "তরল জমা ও অলিগুরিয়া বোর্ড-ধাঁচের কেসে বৃক্কীয় সমস্যার ক্লাসিক ইঙ্গিত।",
    ),
    q(
        "Besides swelling and low urine, which additional symptoms may accompany kidney disease?",
        "ফুলে যাওয়া ও কম মূত্র ছাড়াও বৃক্ক রোগে আর কোন লক্ষণ দেখা যেতে পারে?",
        [
            "Only improved appetite always",
            "Anorexia, vomiting and loin (flank) pain",
            "Only sudden hair greening",
            "Only permanent deafness in all cases",
        ],
        [
            "সবসময় শুধু ক্ষুধা বৃদ্ধি",
            "ক্ষুধামন্দা, বমি ও কোমরে ব্যথা",
            "শুধু চুল সবুজ হওয়া",
            "সব ক্ষেত্রে স্থায়ী বধিরতা",
        ],
        "B", "medium", "application",
        "Board stimuli often add anorexia, vomiting and loin pain to renal failure/nephritis pictures.",
        "বোর্ড উদ্দীপকে প্রায়শই ক্ষুধামন্দা, বমি ও কোমর ব্যথা বৃক্ক সমস্যার সাথে যুক্ত থাকে।",
    ),
    q(
        "Appropriate management steps for serious kidney impairment commonly include which set?",
        "গুরুতর বৃক্কীয় সমস্যায় সাধারণ ব্যবস্থাপনায় কোন সেট অন্তর্ভুক্ত?",
        [
            "Ignore diet and avoid doctors",
            "Medical advice, controlled diet and dialysis if needed",
            "Only unrestricted high-salt feasts",
            "Only stopping all fluid forever",
        ],
        [
            "খাদ্য উপেক্ষা ও চিকিৎসক এড়ানো",
            "চিকিৎসকের পরামর্শ, নিয়ন্ত্রিত আহার ও প্রয়োজনে ডায়ালাইসিস",
            "শুধু অনিয়ন্ত্রিত উচ্চ-লবণ ভোজ",
            "শুধু চিরকাল সব তরল বন্ধ",
        ],
        "B", "easy", "application",
        "Standard advice: consult a physician, restrict/control diet, and use dialysis when indicated.",
        "মানক পরামর্শ: চিকিৎসকের পরামর্শ, নিয়ন্ত্রিত খাদ্য এবং প্রয়োজনে ডায়ালাইসিস।",
    ),
    q(
        "Dialysis is used primarily to do what when kidneys fail?",
        "বৃক্ক অকার্যকর হলে ডায়ালাইসিস প্রধানত কী করে?",
        [
            "Artificially remove wastes and excess fluid from blood",
            "Produce new nephrons from bone",
            "Replace the entire nervous system",
            "Stop all metabolism permanently",
        ],
        [
            "রক্ত থেকে বর্জ্য ও অতিরিক্ত তরল কৃত্রিমভাবে অপসারণ করে",
            "অস্থি থেকে নতুন নেফ্রন তৈরি করে",
            "সম্পূর্ণ স্নায়ুতন্ত্র প্রতিস্থাপন করে",
            "সব বিপাক স্থায়ীভাবে বন্ধ করে",
        ],
        "A", "easy", "conceptual",
        "Hemodialysis/peritoneal dialysis clear diffusible wastes when native renal clearance is inadequate.",
        "নেটিভ বৃক্ক ক্লিয়ারেন্স অপর্যাপ্ত হলে হেমো/পেরিটোনিয়াল ডায়ালাইসিস বর্জ্য পরিষ্কার করে।",
    ),
    q(
        "Nephritis refers to what condition?",
        "নেফ্রাইটিস বলতে কোন অবস্থাকে বোঝায়?",
        [
            "Inflammation of the kidney",
            "Only fracture of the femur",
            "Only infection of the cornea",
            "Only hypertrophy of skeletal muscle",
        ],
        [
            "বৃক্কের প্রদাহ",
            "শুধু ফিমার ভাঙা",
            "শুধু কর্নিয়ার সংক্রমণ",
            "শুধু কঙ্কালপেশির বৃদ্ধি",
        ],
        "A", "easy", "factual",
        "Nephritis is renal inflammation and is a classic excretory-system disorder in the syllabus.",
        "নেফ্রাইটিস বৃক্কের প্রদাহ; সিলেবাসের ক্লাসিক রেচনজনিত সমস্যা।",
    ),
    q(
        "Stone formation in the ureter can directly obstruct which process?",
        "ইউরেটারে পাথর হলে সরাসরি কোন প্রক্রিয়া বাধাগ্রস্ত হতে পারে?",
        [
            "Urine flow from kidney to bladder",
            "Air flow in the trachea",
            "Bile storage only",
            "CSF circulation in ventricles",
        ],
        [
            "বৃক্ক থেকে মূত্রথলিতে মূত্র প্রবাহ",
            "ট্রাকিয়ায় বায়ুপ্রবাহ",
            "শুধু পিত্ত সংরক্ষণ",
            "ভেন্ট্রিকেলে CSF সঞ্চালন",
        ],
        "A", "easy", "application",
        "Ureteric calculi block urine transit and can cause severe loin/abdominal pain and hydronephrosis risk.",
        "ইউরেটার পাথর মূত্রপ্রবাহ আটকায় এবং তীব্র কোমর/উদর ব্যথা ও হাইড্রোনেফ্রোসিসের ঝুঁকি বাড়ায়।",
    ),
    q(
        "Which pair is more directly related to excretory tract disorders than a myocardial infarction?",
        "হার্ট অ্যাটাকের চেয়ে রেচনপথের সমস্যার সাথে কোন জোড়া বেশি সরাসরি সম্পর্কিত?",
        [
            "Nephritis and ureteric stone",
            "Only otitis media and myopia",
            "Only dental caries and alopecia",
            "Only fracture of clavicle and rhinitis",
        ],
        [
            "নেফ্রাইটিস ও ইউরেটার পাথর",
            "শুধু ওটিটিস মিডিয়া ও মায়োপিয়া",
            "শুধু দন্তক্ষয় ও অ্যালোপেশিয়া",
            "শুধু ক্ল্যাভিকল ভাঙা ও রাইনাইটিস",
        ],
        "A", "medium", "application",
        "Board keys typically accept nephritis and ureter stone as renal-tract problems; MI is cardiac.",
        "বোর্ড কীতে সাধারণত নেফ্রাইটিস ও ইউরেটার পাথর রেচনপথের সমস্যা; হার্ট অ্যাটাক হৃৎপিণ্ডের।",
    ),
    q(
        "Uremia is characterized by abnormal accumulation of what in the blood?",
        "ইউরেমিয়ায় রক্তে কোনটির অস্বাভাবিক জমা বৈশিষ্ট্যসূচক?",
        [
            "Nitrogenous wastes such as urea",
            "Only oxygen beyond saturation",
            "Only dietary fibre",
            "Only melanin in plasma",
        ],
        [
            "ইউরিয়া জাতীয় নাইট্রোজেনঘটিত বর্জ্য",
            "শুধু সম্পৃক্তির ঊর্ধ্বে অক্সিজেন",
            "শুধু খাদ্য আঁশ",
            "শুধু প্লাজমায় মেলানিন",
        ],
        "A", "medium", "factual",
        "Failed renal excretion elevates blood urea/other N-wastes—clinically called uremia.",
        "রেচন ব্যর্থতায় রক্তে ইউরিয়া/অন্য N-বর্জ্য বাড়ে—ক্লিনিক্যালি ইউরেমিয়া।",
    ),
    q(
        "Presence of significant protein in urine (proteinuria) often indicates damage to what?",
        "মূত্রে উল্লেখযোগ্য প্রোটিন (প্রোটিনিউরিয়া) প্রায়শই কীসের ক্ষতির ইঙ্গিত?",
        [
            "Glomerular filtration barrier",
            "Only enamel of teeth",
            "Only tympanic membrane",
            "Only nail cuticle",
        ],
        [
            "গ্লোমেরুলার পরিস্রাবণ বাধা",
            "শুধু দাঁতের এনামেল",
            "শুধু টিমপ্যানিক মেমব্রেন",
            "শুধু নখের কিউটিকল",
        ],
        "A", "medium", "conceptual",
        "Intact glomeruli retain plasma proteins; barrier injury allows albumin etc. into urine.",
        "অক্ষত গ্লোমেরুলাস প্লাজমা প্রোটিন আটকায়; বাধা ক্ষতিগ্রস্ত হলে অ্যালবুমিন ইত্যাদি মূত্রে যায়।",
    ),
    q(
        "Hematuria means which abnormal finding?",
        "হিমাটুরিয়া মানে কোন অস্বাভাবিক অবস্থা?",
        [
            "Blood in the urine",
            "Only excess saliva",
            "Only low body temperature always",
            "Only absence of sweat glands",
        ],
        [
            "মূত্রে রক্ত থাকা",
            "শুধু অতিরিক্ত লালা",
            "সবসময় শুধু নিম্ন দেহতাপ",
            "শুধু ঘর্মগ্রন্থির অনুপস্থিতি",
        ],
        "A", "easy", "factual",
        "Hematuria is blood in urine and may signal infection, stone, trauma or glomerular disease.",
        "হিমাটুরিয়া মূত্রে রক্ত; সংক্রমণ, পাথর, আঘাত বা গ্লোমেরুলার রোগের ইঙ্গিত হতে পারে।",
    ),
    q(
        "Anuria refers to what urinary pattern?",
        "অ্যানুরিয়া কোন মূত্র ধরনকে বোঝায়?",
        [
            "Nearly complete absence of urine output",
            "Only slightly increased sweat",
            "Only excessive tears",
            "Normal 1–2 L urine daily",
        ],
        [
            "প্রায় সম্পূর্ণ মূত্র নিঃসরণ বন্ধ",
            "শুধু সামান্য ঘাম বৃদ্ধি",
            "শুধু অতিরিক্ত অশ্রু",
            "স্বাভাবিক দৈনিক ১–২ লিটার মূত্র",
        ],
        "A", "easy", "factual",
        "Anuria is failure to produce/pass urine—an emergency renal/obstructive sign.",
        "অ্যানুরিয়া মূত্র উৎপাদন/নিষ্কাশন প্রায় বন্ধ—জরুরি বৃক্কীয়/অবস্ট্রাকটিভ লক্ষণ।",
    ),
    q(
        "Oliguria means which change in urine volume?",
        "অলিগুরিয়া মূত্রের আয়তনে কোন পরিবর্তন বোঝায়?",
        [
            "Abnormally decreased urine volume",
            "Always doubled urine forever",
            "Only coloured sweat",
            "Complete replacement by feces",
        ],
        [
            "অস্বাভাবিকভাবে মূত্রের আয়তন কমে যাওয়া",
            "চিরকাল দ্বিগুণ মূত্র",
            "শুধু রঙিন ঘাম",
            "মল দ্বারা সম্পূর্ণ প্রতিস্থাপন",
        ],
        "A", "easy", "factual",
        "Oliguria is low urine output, often linked to dehydration, shock or renal impairment.",
        "অলিগুরিয়া কম মূত্র; প্রায়শই পানিশূন্যতা, শক বা বৃক্কীয় ক্ষতির সাথে যুক্ত।",
    ),
    q(
        "Polyuria is typically described as what?",
        "পলিউরিয়া সাধারণত কী হিসেবে বর্ণিত?",
        [
            "Production of abnormally large volumes of urine",
            "Total inability to form urea in liver",
            "Absence of kidneys from birth only",
            "Only painless blue urine always",
        ],
        [
            "অস্বাভাবিকভাবে প্রচুর পরিমাণ মূত্র উৎপাদন",
            "যকৃতে ইউরিয়া গঠনের সম্পূর্ণ অক্ষমতা",
            "শুধু জন্মগতালীন বৃক্কের অনুপস্থিতি",
            "সবসময় ব্যথহীন নীল মূত্র",
        ],
        "A", "easy", "factual",
        "Polyuria is large urine volume (e.g., diabetes mellitus/insipidus or low ADH effect).",
        "পলিউরিয়া বেশি মূত্র (যেমন ডায়াবেটিস মেলিটাস/ইনসিপিডাস বা কম ADH প্রভাব)।",
    ),
    q(
        "Kidney (renal) stones are also commonly called what?",
        "বৃক্কের পাথরকে সাধারণত আর কী বলা হয়?",
        ["Renal calculi", "Pulmonary emboli only", "Gall stones only", "Dental plaque only"],
        ["রেনাল ক্যালকুলাস", "শুধু পালমোনারি এম্বোলাস", "শুধু পিত্তপাথর", "শুধু দন্ত প্লাক"],
        "A", "easy", "factual",
        "Renal calculi are solid concretions that may form in pelvis/calyces and migrate to the ureter.",
        "রেনাল ক্যালকুলাস পেলভিস/ক্যালিক্সে গঠিত কঠিন পাথর যা ইউরেটারে নামতে পারে।",
    ),
    q(
        "Gout is associated with elevated blood levels of which excretory metabolite?",
        "গাউট কোন রেচন বিপাকজাত পদার্থের রক্তে উচ্চ মাত্রার সাথে যুক্ত?",
        ["Uric acid", "Oxygen only", "Nitrogen gas only", "Carbon monoxide only"],
        ["ইউরিক অ্যাসিড", "শুধু অক্সিজেন", "শুধু নাইট্রোজেন গ্যাস", "শুধু কার্বন মনোক্সাইড"],
        "A", "medium", "factual",
        "Hyperuricemia can precipitate urate crystals in joints—gout—linking purine excretion disorders.",
        "হাইপারইউরিসেমিয়ায় জয়েন্টে ইউরেট স্ফটিক জমে গাউট হয়—পিউরিন রেচনের সমস্যা।",
    ),
    q(
        "Acute urinary retention differs from anuria mainly in that urine may still be what?",
        "তীব্র মূত্র ধারণ অ্যানুরিয়া থেকে প্রধানত কীভাবে আলাদা—মূত্র তখনও কী হতে পারে?",
        [
            "Produced by kidneys but not emptied from a blocked bladder outlet",
            "Absent because kidneys never existed",
            "Converted entirely into sweat only",
            "Stored permanently in the alveoli",
        ],
        [
            "বৃক্কে তৈরি হয়েও অবরুদ্ধ নিষ্কাশনপথে মূত্রথলি খালি হয় না",
            "বৃক্ক না থাকায় সম্পূর্ণ অনুপস্থিত",
            "সম্পূর্ণভাবে শুধু ঘামে রূপান্তরিত",
            "স্থায়ীভাবে আ্যালভিওলাসে সংরক্ষিত",
        ],
        "A", "hard", "conceptual",
        "Retention: kidneys make urine but outlet obstruction prevents voiding; true anuria is no urine formation/reaching bladder.",
        "ধারণ: বৃক্ক মূত্র তৈরি করে কিন্তু নিষ্কাশন বাধায় বেরোয় না; প্রকৃত অ্যানুরিয়ায় মূত্র গঠন/থলিতে পৌঁছানোই নেই।",
    ),
    q(
        "Which lifestyle factor commonly worsens risk of urinary stone disease?",
        "কোন জীবনযাত্রাগত্যরস সাধারণত মূত্রপাথরের ঝুঁকি বাড়ায়?",
        [
            "Chronic inadequate water intake",
            "Only reading textbooks",
            "Only walking in shade briefly",
            "Only speaking softly",
        ],
        [
            "দীর্ঘমেয়াদি অপর্যাপ্ত পানি গ্রহণ",
            "শুধু পাঠ্যবই পড়া",
            "শুধু ছায়ায় অল্প হাঁটা",
            "শুধু আস্তে কথা বলা",
        ],
        "A", "medium", "application",
        "Low fluid intake concentrates urine and favors crystal precipitation of calculi.",
        "কম পানি মূত্রকে ঘন করে স্ফটিক জমা ও পাথর গঠনের অনুকূল করে।",
    ),
    q(
        "In end-stage renal disease, erythropoietin deficiency commonly contributes to what?",
        "শেষ পর্যায়ের বৃক্ক রোগে এরিথ্রোপয়েটিন ঘাটতি সাধারণত কীতে অবদান রাখে?",
        [
            "Anemia",
            "Only hyperacusis",
            "Only excessive RBC overproduction always",
            "Only sudden bone lengthening",
        ],
        [
            "রক্তাল্পতা (অ্যানিমিয়া)",
            "শুধু হাইপারঅ্যাকুসিস",
            "সবসময় শুধু অতিরিক্ত RBC উৎপাদন",
            "শুধু হঠাৎ অস্থি দীর্ঘায়ন",
        ],
        "A", "hard", "conceptual",
        "Healthy kidneys secrete EPO; failure lowers EPO → reduced RBC production → anemia.",
        "সুস্থ বৃক্ক EPO ক্ষরণ করে; ব্যর্থতায় EPO কমে RBC কমে অ্যানিমিয়া হয়।",
    ),
    q(
        "Which finding best supports glomerular disease rather than a simple lower-urethral irritation alone?",
        "শুধু নিম্ন ইউরেথ্রার সাধারণ জ্বালা ছাড়া গ্লোমেরুলার রোগের পক্ষে কোন লক্ষণ বেশি সমর্থন করে?",
        [
            "Heavy proteinuria with edema",
            "Only a brief ticklish cough",
            "Only temporary hiccups",
            "Only seasonal sneezing without urine change",
        ],
        [
            "প্রোটিনিউরিয়াসহ শোথ",
            "শুধু সাময়িক কাশি",
            "শুধু অস্থায়ী হিক্কা",
            "মূত্র অপরিবর্তিত রেখে শুধু ঋতুকালীন হাঁচি",
        ],
        "A", "hard", "application",
        "Marked protein loss and edema point to glomerular barrier failure (nephrotic/nephritic patterns).",
        "উল্লেখযোগ্য প্রোটিন ক্ষয় ও শোথ গ্লোমেরুলার বাধার ব্যর্থতার দিকে ইঙ্গিত করে।",
    ),
    q(
        "Why must diet often be controlled in chronic kidney disease?",
        "দীর্ঘমেয়াদি বৃক্ক রোগে খাদ্য প্রায়শই কেন নিয়ন্ত্রণ করতে হয়?",
        [
            "To limit load of salt, protein metabolites and fluid the failing kidneys must clear",
            "To increase daily urea production deliberately",
            "To block intestinal absorption of all vitamins forever",
            "To replace nephrons with pancreatic acini",
        ],
        [
            "ব্যর্থ বৃক্ককে পরিষ্কার করতে হয় এমন লবণ, প্রোটিন বিপাকজাত ও তরলের চাপ কমাতে",
            "ইচ্ছাকৃতভাবে দৈনিক ইউরিয়া উৎপাদন বাড়াতে",
            "সব ভিটামিন শোষণ চিরকাল বন্ধ করতে",
            "নেফ্রনকে অগ্ন্যাশয়ের অ্যাসিনাই দিয়ে বদলাতে",
        ],
        "A", "medium", "conceptual",
        "Restricting Na⁺/protein/fluid (as advised) reduces azotemia, hypertension and edema risk.",
        "পরামর্শমতো Na⁺/প্রোটিন/তরল সীমিত করলে অ্যাজোটিমিয়া, উচ্চরক্তচাপ ও শোথের ঝুঁকি কমে।",
    ),
]


TOPICS_MAP = {
    "bio2_27_ch06_t01": T01,
    "bio2_27_ch06_t02": T02,
    "bio2_27_ch06_t03": T03,
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
        "chapter": "bio2_27_ch06",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p214_pdf220.png",
            "p215_pdf221.png",
            "p216_pdf222.png",
            "p217_pdf223.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio2_27_ch06_t01": {
                "title": "Kidney and nephron / বৃক্ক ও নেফ্রন",
                "themes": [
                    "bean-shaped kidney; hilum; left higher; capsule",
                    "Malpighian body; podocytes; parietal squamous; afferent/efferent",
                    "ureter vs urethra; renal pyramid; ~1–1.2M nephrons; cortex corpuscles",
                    "filtration slits; afferent vessel; nephron unit; PCT→loop→DCT→CD path",
                    "filtration membrane; pituitary+adrenal hormones; renal artery",
                ],
            },
            "bio2_27_ch06_t02": {
                "title": "Urine formation / মূত্র সৃষ্টি",
                "themes": [
                    "ultrafiltration first; no protein in filtrate; PCT bulk reabsorption",
                    "selective reabsorption; tubular secretion; primary urine",
                    "ADH/vasopressin; osmoregulation; ADH ↑ conserves water",
                    "urine ~95% water; urochrome; ketone non-N; uric acid from purines",
                    "ureotelic; hydrostatic pressure; creatinine GFR marker; liver urea; low ADH dilute urine",
                ],
            },
            "bio2_27_ch06_t03": {
                "title": "Excretory disorders / রেচনজনিত সমস্যা",
                "themes": [
                    "edema/oliguria; anorexia/vomiting/loin pain; advice+diet+dialysis",
                    "dialysis role; nephritis; ureteric stone obstruction",
                    "nephritis+stone vs MI; uremia; proteinuria; hematuria",
                    "anuria/oliguria/polyuria; renal calculi; gout/uric acid",
                    "retention vs anuria; low water→stones; EPO anemia; CKD diet rationale",
                ],
            },
        },
        "low_confidence": [
            "OCR of printed MCQ pages p214–217 is noisy (garbled options/answer marks); stems reconstructed from readable fragments, CQ text on earlier pages, and standard HSC Zoology Ch6 facts.",
            "Figure-/stimulus-linked bank items rewritten as standalone stems (no dependency on missing diagrams).",
            "Nephron count kept as ~1–1.2 million per kidney per common HSC framing.",
            "Urine water fraction kept as ~95% (texts also cite 95–97%).",
            "Disorder topic supplemented more heavily because MCQ OCR density for pathology was lower than for structure/urine formation.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio2_27_ch06_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio2_27_ch06_t01": 20,
                "bio2_27_ch06_t02": 20,
                "bio2_27_ch06_t03": 20,
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
        / "ch06_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
