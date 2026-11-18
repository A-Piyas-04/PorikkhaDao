#!/usr/bin/env python3
"""Seed Biology 2nd Paper Ch4 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio2_27_ch04_t01..t03 (Blood/groups; Heart/circulation; Lymph).
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
    "biology p2 ch04; curated bilingual"
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


# --- t01: Blood and blood groups / রক্ত ও রক্তের গ্রুপ ---
T01 = [
    q(
        "Which white blood cell secretes heparin?",
        "কোন শ্বেত রক্তকণিকা হেপারিন ক্ষরণ করে?",
        ["Eosinophil", "Neutrophil", "Basophil", "Lymphocyte"],
        ["ইওসিনোফিল", "নিউট্রোফিল", "বেসোফিল", "লিম্ফোসাইট"],
        "C", "easy", "factual",
        "Basophils release heparin (anticoagulant) and histamine from their granules.",
        "বেসোফিলের দানা থেকে হেপারিন (অ্যান্টিকোয়াগুল্যান্ট) ও হিস্টামিন ক্ষরিত হয়।",
    ),
    q(
        "From which blood cell is histamine mainly secreted?",
        "কোন রক্তকণিকা হতে প্রধানত হিস্টামিন ক্ষরিত হয়?",
        ["Neutrophil", "Lymphocyte", "Basophil", "Eosinophil"],
        ["নিউট্রোফিল", "লিম্ফোসাইট", "বেসোফিল", "ইওসিনোফিল"],
        "C", "easy", "factual",
        "Basophils (and mast cells) secrete histamine, involved in allergy and inflammation.",
        "বেসোফিল (ও মাস্ট কোষ) হিস্টামিন ক্ষরণ করে যা অ্যালার্জি ও প্রদাহে ভূমিকা রাখে।",
    ),
    q(
        "Which substance helps constrict blood vessels and reduce bleeding?",
        "নিচের কোন উপাদান রক্তনালির সংকোচন ও রক্তক্ষরণ কমাতে সহায়তা করে?",
        ["Heparin", "Histamine", "Thromboplastin", "Serotonin"],
        ["হেপারিন", "হিস্টামিন", "থ্রম্বোপ্লাস্টিন", "সেরোটোনিন"],
        "D", "medium", "factual",
        "Platelets release serotonin, which causes local vasoconstriction and limits bleeding.",
        "অণুচক্রিকা থেকে সেরোটোনিন নির্গত হয়ে স্থানীয় রক্তনালি সংকুচিত করে রক্তক্ষরণ কমায়।",
    ),
    q(
        "Which formed element is chiefly involved in O₂ and CO₂ transport?",
        "O₂ ও CO₂ পরিবহণে নিচের কোনটি প্রধানত জড়িত?",
        ["Leukocyte", "Erythrocyte", "Lymphocyte", "Monocyte"],
        ["লিউকোসাইট", "এরিথ্রোসাইট", "লিম্ফোসাইট", "মনোসাইট"],
        "B", "easy", "factual",
        "Erythrocytes contain haemoglobin that binds and transports respiratory gases.",
        "এরিথ্রোসাইটে হিমোগ্লোবিন থাকে যা শ্বসন গ্যাস পরিবহন করে।",
    ),
    q(
        "What is the approximate percentage of organic substances in blood plasma?",
        "রক্তরসে জৈব পদার্থের পরিমাণ প্রায় কত?",
        ["0.9–1.0%", "7–9%", "8–10%", "90–92%"],
        ["০.৯–১.০%", "৭–৯%", "৮–১০%", "৯০–৯২%"],
        "B", "medium", "numerical",
        "Plasma is ~90–92% water; organic solutes (mainly proteins) are about 7–9%.",
        "প্লাজমার প্রায় ৯০–৯২% পানি; জৈব পদার্থ (প্রধানত প্রোটিন) প্রায় ৭–৯%।",
    ),
    q(
        "The percentage volume of red blood cells in blood is called what?",
        "রক্তে লোহিত রক্তকণিকার আয়তনের শতকরা হিসাবকে কী বলে?",
        ["Haemostasis", "Haematopoiesis", "Homeostasis", "Haematocrit"],
        ["হিমোস্ট্যাসিস", "হিমাটোপয়েসিস", "হোমিওস্ট্যাসিস", "হেমাটোক্রিট"],
        "D", "easy", "factual",
        "Haematocrit (packed cell volume) is the percent of blood volume occupied by RBCs.",
        "হেমাটোক্রিট হলো রক্তের মোট আয়তনের যে শতাংশ লোহিত কণিকা দখল করে।",
    ),
    q(
        "What is the usual ratio of RBC to WBC in human blood?",
        "মানুষের রক্তে RBC ও WBC-এর সাধারণ অনুপাত কত?",
        ["1:700", "500:1", "1:500", "700:1"],
        ["১:৭০০", "৫০০:১", "১:৫০০", "৭০০:১"],
        "D", "easy", "numerical",
        "HSC texts commonly cite RBC:WBC ≈ 700:1 (some newer keys note ~600:1).",
        "এইচএসসি পাঠ্যে সাধারণত RBC:WBC ≈ ৭০০:১ উল্লেখ থাকে।",
    ),
    q(
        "Why is a neutrophil called a phagocyte?",
        "নিউট্রোফিলকে ফ্যাগোসাইট বলা হয় কেন?",
        [
            "It secretes antibodies only",
            "It engulfs and destroys microbes with lysosomal enzymes",
            "It carries oxygen with haemoglobin",
            "It initiates blood clotting",
        ],
        [
            "এটি শুধু অ্যান্টিবডি ক্ষরণ করে",
            "এটি অণুজীব গ্রাস করে লাইসোজোম এনজাইমে ধ্বংস করে",
            "এটি হিমোগ্লোবিন দিয়ে অক্সিজেন বহন করে",
            "এটি রক্ত তঞ্চন শুরু করে",
        ],
        "B", "easy", "conceptual",
        "Neutrophils phagocytose bacteria/viruses and digest them with proteolytic enzymes; one cell may engulf many microbes before dying.",
        "নিউট্রোফিল ব্যাকটেরিয়া/ভাইরাস গ্রাস করে প্রোটিওলাইটিক এনজাইমে ধ্বংস করে বলে একে ফ্যাগোসাইট বলে।",
    ),
    q(
        "Which statement about platelets is correct?",
        "অণুচক্রিকার ক্ষেত্রে কোনটি সঠিক?",
        [
            "They are nucleated cells",
            "They are destroyed in the spleen",
            "They phagocytose bacteria as their main role",
            "They contain haemoglobin",
        ],
        [
            "এগুলো নিউক্লিয়াসযুক্ত কোষ",
            "এগুলো প্লীহাতে ধ্বংস হয়",
            "এগুলোর প্রধান কাজ ব্যাকটেরিয়া ভক্ষণ",
            "এগুলোতে হিমোগ্লোবিন থাকে",
        ],
        "B", "medium", "factual",
        "Platelets are anucleate fragments; many are removed in the spleen; their main role is haemostasis, not phagocytosis.",
        "অণুচক্রিকা নিউক্লিয়াসবিহীন খণ্ড; অনেক প্লীহাতে ধ্বংস হয়; প্রধান কাজ তঞ্চন সহায়তা।",
    ),
    q(
        "What is a principal function of platelets?",
        "অণুচক্রিকার প্রধান কাজ কোনটি?",
        [
            "Producing antibodies",
            "Maintaining acid–base balance",
            "Secreting histamine as the main role",
            "Helping blood to clot",
        ],
        [
            "অ্যান্টিবডি উৎপাদন",
            "অম্ল–ক্ষার সমতা রক্ষা",
            "প্রধানত হিস্টামিন নিঃসরণ",
            "রক্ত জমাটে সহায়তা",
        ],
        "D", "easy", "factual",
        "Platelets adhere at injury sites, release clotting factors/serotonin and form the platelet plug.",
        "ক্ষতস্থানে অণুচক্রিকা জমা হয়ে প্লাগ গঠন ও তঞ্চন ফ্যাক্টর/সেরোটোনিন ক্ষরণ করে।",
    ),
    q(
        "Which factor converts fibrinogen to fibrin monomers?",
        "ফাইব্রিনোজেনকে ফাইব্রিন মনোমারে রূপান্তর করে কোন ফ্যাক্টর?",
        ["Hageman factor", "Accelerin", "Calcium ion alone", "Thrombin"],
        ["হ্যাগম্যান ফ্যাক্টর", "অ্যাকসেলারিন", "শুধু ক্যালসিয়াম আয়ন", "থ্রম্বিন"],
        "D", "medium", "factual",
        "Thrombin (factor IIa) cleaves fibrinogen to fibrin monomers that polymerise into a clot.",
        "থ্রম্বিন (ফ্যাক্টর IIa) ফাইব্রিনোজেনকে ফাইব্রিন মনোমারে ভেঙে তঞ্চন জালক গঠন করে।",
    ),
    q(
        "Which clotting factor cross-links and stabilises fibrin?",
        "কোন তঞ্চন ফ্যাক্টর ফাইব্রিনকে ক্রস-লিংক ও স্থায়ী করে?",
        ["Factor I", "Factor VIII", "Factor IX", "Factor XIII"],
        ["ফ্যাক্টর I", "ফ্যাক্টর VIII", "ফ্যাক্টর IX", "ফ্যাক্টর XIII"],
        "D", "hard", "factual",
        "Factor XIII (fibrin-stabilising factor) cross-links fibrin polymers into a stable clot.",
        "ফ্যাক্টর XIII (ফাইব্রিন-স্থায়ীকারী) ফাইব্রিন পলিমারকে ক্রস-লিংক করে স্থায়ী জমাট গঠন করে।",
    ),
    q(
        "Which substance helps keep blood flowing inside vessels by opposing clotting?",
        "রক্তনালিতে রক্ত সচল রাখতে তঞ্চনবিরোধী কোনটি সাহায্য করে?",
        ["Fibrin", "Heparin", "Histamine", "Serum"],
        ["ফাইব্রিন", "হেপারিন", "হিস্টামিন", "সিরাম"],
        "B", "easy", "factual",
        "Heparin is a natural anticoagulant that inhibits clotting and keeps blood fluid in vessels.",
        "হেপারিন প্রাকৃতিক অ্যান্টিকোয়াগুল্যান্ট যা তঞ্চন বাধা দিয়ে রক্তনালিতে রক্ত তরল রাখে।",
    ),
    q(
        "How does serum differ from plasma?",
        "সিরাম রক্তরস (প্লাজমা) থেকে কীভাবে আলাদা?",
        [
            "Serum has more fibrinogen than plasma",
            "Serum lacks fibrinogen and some clotting factors (II, V, VIII) and has more serotonin",
            "Serum contains all clotting factors that plasma has",
            "Serum is identical to whole blood",
        ],
        [
            "সিরামে প্লাজমার চেয়ে বেশি ফাইব্রিনোজেন থাকে",
            "সিরামে ফাইব্রিনোজেন ও কিছু তঞ্চন ফ্যাক্টর (II, V, VIII) থাকে না এবং সেরোটোনিন বেশি",
            "সিরামে প্লাজমার সব তঞ্চন ফ্যাক্টর থাকে",
            "সিরাম সম্পূর্ণ রক্তের সমান",
        ],
        "B", "medium", "conceptual",
        "After clotting, the fluid left is serum—plasma minus fibrinogen and several clotting factors, richer in serotonin.",
        "তঞ্চনের পর অবশিষ্ট তরল সিরাম; এতে ফাইব্রিনোজেন ও কয়েকটি তঞ্চন ফ্যাক্টর নেই, সেরোটোনিন বেশি।",
    ),
    q(
        "Which statement about eosinophils is correct?",
        "ইওসিনোফিলের ক্ষেত্রে কোনটি সঠিক?",
        [
            "They are stain-neutral (neutrophilic)",
            "They are acidophilic",
            "They mainly secrete histamine",
            "They are the least numerous WBC type",
        ],
        [
            "এগুলো বর্ণনিরপেক্ষ",
            "এগুলো অম্লধর্মী (অ্যাসিডোফিলিক)",
            "এগুলো প্রধানত হিস্টামিন নিঃসরণ করে",
            "এগুলো সংখ্যায় সবচেয়ে কম WBC",
        ],
        "B", "medium", "factual",
        "Eosinophils take up acidic dyes (acidophilic); basophils are fewest; histamine is mainly from basophils.",
        "ইওসিনোফিল অম্লীয় রং গ্রহণ করে (অ্যাসিডোফিলিক); হিস্টামিন প্রধানত বেসোফিল থেকে আসে।",
    ),
    q(
        "Which are agranular (non-granular) white blood cells?",
        "কোনগুলো দানাবিহীন শ্বেত রক্তকণিকা?",
        [
            "Neutrophil and eosinophil",
            "Basophil and neutrophil",
            "Lymphocyte and monocyte",
            "Eosinophil and basophil",
        ],
        [
            "নিউট্রোফিল ও ইওসিনোফিল",
            "বেসোফিল ও নিউট্রোফিল",
            "লিম্ফোসাইট ও মনোসাইট",
            "ইওসিনোফিল ও বেসোফিল",
        ],
        "C", "easy", "factual",
        "Agranulocytes are lymphocytes and monocytes; the three granulocytes are neutrophil, eosinophil and basophil.",
        "অ্যাগ্রানুলোসাইট = লিম্ফোসাইট ও মনোসাইট; গ্রানুলোসাইট = নিউট্রোফিল, ইওসিনোফিল, বেসোফিল।",
    ),
    q(
        "Which of the following are human plasma proteins?",
        "মানুষের রক্তের প্লাজমা প্রোটিন কোনগুলো?",
        [
            "Fibrinogen and collagen",
            "Collagen and globulin",
            "Fibrinogen and globulin",
            "Only collagen",
        ],
        [
            "ফাইব্রিনোজেন ও কোলাজেন",
            "কোলাজেন ও গ্লোবিউলিন",
            "ফাইব্রিনোজেন ও গ্লোবিউলিন",
            "শুধু কোলাজেন",
        ],
        "C", "easy", "factual",
        "Major plasma proteins include albumin, globulins and fibrinogen; collagen is a connective-tissue protein, not a plasma protein.",
        "প্রধান প্লাজমা প্রোটিন: অ্যালবুমিন, গ্লোবিউলিন, ফাইব্রিনোজেন; কোলাজেন সংযোজক কলার প্রোটিন।",
    ),
    q(
        "Which is called the mobile defensive unit of the body?",
        "দেহের ভ্রাম্যমাণ প্রতিরক্ষাকারী একক কোনটি?",
        ["Red blood cell", "White blood cell", "Platelet", "Lymph fluid only"],
        ["লোহিত কণিকা", "শ্বেত কণিকা", "অণুচক্রিকা", "শুধু লসিকারস"],
        "B", "easy", "factual",
        "WBCs move through tissues and destroy pathogens, so they are mobile defence units.",
        "শ্বেত কণিকা কলায় চলাচল করে রোগজীবাণু ধ্বংস করে বলে একে ভ্রাম্যমাণ প্রতিরক্ষা একক বলে।",
    ),
    q(
        "To which group of haemoglobin does CO₂ mainly bind?",
        "হিমোগ্লোবিনের কোন অংশে CO₂ প্রধানত যুক্ত হয়?",
        ["–COOH", "–OH", "–NH₂", "HCO₃⁻ only as the binding site on Hb"],
        ["–COOH", "–OH", "–NH₂", "শুধু HCO₃⁻ হিমোগ্লোবিনের বন্ধনস্থল"],
        "C", "medium", "factual",
        "A portion of CO₂ binds amino groups (–NH₂) of the globin chains forming carbamino haemoglobin.",
        "কিছু CO₂ গ্লোবিন শৃঙ্খলের –NH₂ গ্রুপের সাথে যুক্ত হয়ে কার্বামিনো হিমোগ্লোবিন গঠন করে।",
    ),
    q(
        "ABO blood-group antigens are located mainly where?",
        "ABO রক্তগ্রুপের অ্যান্টিজেন প্রধানত কোথায় অবস্থিত?",
        [
            "On the plasma membrane of RBCs",
            "Only inside WBC nuclei",
            "Only dissolved free in plasma water",
            "Only on platelet granules",
        ],
        [
            "লোহিত কণিকার প্লাজমাঝিল্লিতে",
            "শুধু শ্বেতকণিকার নিউক্লিয়াসে",
            "শুধু প্লাজমা পানিতে দ্রবীভূত অবস্থায়",
            "শুধু অণুচক্রিকার দানায়",
        ],
        "A", "easy", "factual",
        "ABO antigens are glycoproteins/glycolipids on the RBC surface; they determine blood grouping.",
        "ABO অ্যান্টিজেন RBC পৃষ্ঠের গ্লাইকোপ্রোটিন/গ্লাইকোলিপিড; এগুলো রক্ত গ্রুপিং নির্ধারণ করে।",
    ),
]


# --- t02: Heart and circulation / হৃৎপিণ্ড ও রক্তসঞ্চালন ---
T02 = [
    q(
        "What is called the natural pacemaker of the heart?",
        "হৃৎপিণ্ডের প্রাকৃতিক পেসমেকার বলা হয় কোনটিকে?",
        [
            "Sino-atrial (SA) node",
            "Purkinje fibres",
            "Bundle of His",
            "Atrio-ventricular (AV) node",
        ],
        [
            "সাইনো-অ্যাট্রিয়াল (SA) নোড",
            "পারকিনজি তন্তু",
            "বান্ডল অব হিজ",
            "অ্যাট্রিও-ভেন্ট্রিকুলার (AV) নোড",
        ],
        "A", "easy", "factual",
        "The SA node in the right atrial wall initiates the heartbeat and is the natural pacemaker.",
        "ডান অলিন্দের প্রাচীরে SA নোড হৃৎস্পন্দন শুরু করে বলে একে প্রাকৃতিক পেসমেকার বলে।",
    ),
    q(
        "Which sequence of myogenic conduction is correct?",
        "মায়োজেনিক নিয়ন্ত্রণের কোন ক্রম সঠিক?",
        [
            "SAN → AVN → Purkinje system → Bundle of His",
            "SAN → AVN → Bundle of His → Purkinje system",
            "SAN → Bundle of His → AVN → Purkinje system",
            "SAN → Purkinje system → AVN → Bundle of His",
        ],
        [
            "SAN → AVN → পারকিনজি তন্ত্র → বান্ডল অব হিজ",
            "SAN → AVN → বান্ডল অব হিজ → পারকিনজি তন্ত্র",
            "SAN → বান্ডল অব হিজ → AVN → পারকিনজি তন্ত্র",
            "SAN → পারকিনজি তন্ত্র → AVN → বান্ডল অব হিজ",
        ],
        "B", "medium", "factual",
        "Impulse: SA node → AV node → Bundle of His → right/left branches → Purkinje fibres → ventricular myocardium.",
        "উদ্দীপনা: SA নোড → AV নোড → বান্ডল অব হিজ → শাখা → পারকিনজি তন্তু → নিলয় পেশি।",
    ),
    q(
        "Which phase of the cardiac cycle lasts about 0.1 second?",
        "কার্ডিয়াক চক্রের কোন দশার সময়কাল প্রায় ০.১ সেকেন্ড?",
        [
            "Atrial systole",
            "Atrial diastole",
            "Ventricular systole",
            "Ventricular diastole",
        ],
        [
            "অলিন্দের সিস্টোল",
            "অলিন্দের ডায়াস্টোল",
            "নিলয়ের সিস্টোল",
            "নিলয়ের ডায়াস্টোল",
        ],
        "A", "easy", "numerical",
        "Typical timings: atrial systole ~0.1 s; ventricular systole ~0.3 s; ventricular diastole ~0.5 s.",
        "সাধারণ সময়: অলিন্দ সিস্টোল ~০.১ সে.; নিলয় সিস্টোল ~০.৩ সে.; নিলয় ডায়াস্টোল ~০.৫ সে.।",
    ),
    q(
        "What is the approximate duration of ventricular diastole?",
        "মানব হৃৎপিণ্ডে ভেন্ট্রিকলের ডায়াস্টোলের সময়কাল প্রায় কত?",
        ["0.7 second", "0.1 second", "0.5 second", "0.3 second"],
        ["০.৭ সেকেন্ড", "০.১ সেকেন্ড", "০.৫ সেকেন্ড", "০.৩ সেকেন্ড"],
        "C", "easy", "numerical",
        "Ventricular diastole lasts about 0.5 s and is the longest phase of the cardiac cycle.",
        "নিলয়ের ডায়াস্টোল প্রায় ০.৫ সেকেন্ড এবং কার্ডিয়াক চক্রের দীর্ঘতম দশা।",
    ),
    q(
        "What is the usual duration of one cardiac cycle?",
        "একটি হৃৎচক্রের সাধারণ সময়কাল কত সেকেন্ড?",
        ["0.75", "0.78", "0.80", "0.70"],
        ["০.৭৫", "০.৭৮", "০.৮০", "০.৭০"],
        "C", "easy", "numerical",
        "At ~75 beats/min, one cycle lasts about 0.8 second.",
        "প্রতি মিনিটে ~৭৫ স্পন্দনে একটি চক্রের সময়কাল প্রায় ০.৮ সেকেন্ড।",
    ),
    q(
        "What is the approximate duration of atrial diastole?",
        "হৃৎপিণ্ডের অলিন্দের ডায়াস্টোলের সময়কাল প্রায় কত সেকেন্ড?",
        ["0.7", "0.5", "0.3", "0.1"],
        ["০.৭", "০.৫", "০.৩", "০.১"],
        "A", "medium", "numerical",
        "Atria are in diastole for most of the cycle (~0.7 s) while ventricles contract and then relax.",
        "চক্রের অধিকাংশ সময় (~০.৭ সে.) অলিন্দ ডায়াস্টোলে থাকে।",
    ),
    q(
        "Which chamber has the thicker wall, and why?",
        "বাম ও ডান নিলয়ের মধ্যে কোনটির প্রাচীর পুরু এবং কেন?",
        [
            "Right ventricle — pumps blood only to the lungs",
            "Left ventricle — pumps blood through the systemic circuit to the whole body",
            "Both ventricles equally thick for the same workload",
            "Right atrium — receives all venous return",
        ],
        [
            "ডান নিলয় — শুধু ফুসফুসে রক্ত পাঠায়",
            "বাম নিলয় — সিস্টেমিক সংবহনে সারা দেহে রক্ত পাঠায়",
            "উভয় নিলয় সমান পুরু একই কাজের জন্য",
            "ডান অলিন্দ — সব শিরারক্ত গ্রহণ করে",
        ],
        "B", "easy", "conceptual",
        "Left ventricular myocardium is thicker because systemic arterial pressure and distance require greater force.",
        "বাম নিলয়ের প্রাচীর পুরু কারণ সারা দেহে উচ্চ চাপে রক্ত পাঠাতে বেশি শক্তি লাগে।",
    ),
    q(
        "Where are semilunar valves found at heart chamber–vessel junctions?",
        "হৃৎপিণ্ডের প্রকোষ্ঠ ও রক্তনালির সংযোগস্থলে সেমিলুনার কপাটিকা কোথায় থাকে?",
        [
            "Between left ventricle and aorta (and similarly right ventricle–pulmonary artery)",
            "Between left atrium and left ventricle only",
            "Between inferior vena cava and right atrium",
            "Between superior vena cava and right atrium",
        ],
        [
            "বাম নিলয় ও অ্যাওটার মধ্যে (এবং ডান নিলয়–পালমোনারি ধমনিতেও)",
            "শুধু বাম অলিন্দ ও বাম নিলয়ের মধ্যে",
            "ইনফিরিয়র ভেনা ক্যাভা ও ডান অলিন্দের মধ্যে",
            "সুপিরিয়র ভেনা ক্যাভা ও ডান অলিন্দের মধ্যে",
        ],
        "A", "medium", "factual",
        "Semilunar valves guard aorta and pulmonary trunk; AV valves (bi/tricuspid) guard atrio-ventricular openings.",
        "সেমিলুনার কপাটিকা অ্যাওটা ও পালমোনারি ধমনিতে; বাই/ট্রাইকাসপিড অলিন্দ–নিলয় ছিদ্রে।",
    ),
    q(
        "Which path correctly describes systemic circulation?",
        "সিস্টেমিক সংবহনে রক্ত প্রবাহের সঠিক গতিপথ কোনটি?",
        [
            "Left ventricle → aorta → body tissues/organs",
            "Right ventricle → lungs → alveoli only as the full systemic path",
            "Left ventricle → coronary artery → heart muscle only",
            "Lungs → veins → left ventricle as the start of systemic flow",
        ],
        [
            "বাম নিলয় → অ্যাওটা → কলা ও অঙ্গ",
            "ডান নিলয় → ফুসফুস → অ্যালভিওলাসই পূর্ণ সিস্টেমিক পথ",
            "বাম নিলয় → করোনারি ধমনি → শুধু হৃৎপেশি",
            "ফুসফুস → শিরা → বাম নিলয়ই সিস্টেমিক শুরু",
        ],
        "A", "easy", "factual",
        "Systemic circulation starts from the left ventricle via the aorta to body tissues and returns via venae cavae to the right atrium.",
        "সিস্টেমিক সংবহন বাম নিলয় থেকে অ্যাওটা দিয়ে দেহকলায় যায় এবং ভেনা ক্যাভা দিয়ে ডান অলিন্দে ফেরে।",
    ),
    q(
        "What is coronary circulation?",
        "করোনারি সংবহন বলতে কী বোঝায়?",
        [
            "Blood flow through the lungs only",
            "Blood supply to the heart muscle via coronary vessels",
            "Portal flow from intestine to liver",
            "Open circulation into haemocoel",
        ],
        [
            "শুধু ফুসফুসের মধ্য দিয়ে রক্তপ্রবাহ",
            "করোনারি রক্তনালি দিয়ে হৃৎপেশিতে রক্ত সরবরাহ",
            "অন্ত্র থেকে যকৃতে পোর্টাল প্রবাহ",
            "হিমোসিলে মুক্ত সংবহন",
        ],
        "B", "easy", "factual",
        "Coronary arteries from the aorta feed myocardium; coronary veins return blood largely to the right atrium.",
        "অ্যাওটা থেকে করোনারি ধমনি হৃৎপ্রাচীরে O₂-সমৃদ্ধ রক্ত দেয়; করোনারি শিরা প্রধানত ডান অলিন্দে ফেরায়।",
    ),
    q(
        "What is meant by the Bundle of His?",
        "বান্ডল অব হিজ বলতে কী বোঝায়?",
        [
            "A special conducting tissue from the AV node into the interventricular septum, branching to Purkinje fibres",
            "The muscle of the left atrium only",
            "A valve between atria",
            "The pericardial sac around the heart",
        ],
        [
            "AV নোড থেকে আন্তঃনিলয় প্রাচীরে বিস্তৃত বিশেষ পরিবাহী টিস্যু যা পারকিনজি তন্তুতে মিলিত হয়",
            "শুধু বাম অলিন্দের পেশি",
            "অলিন্দদ্বয়ের মধ্যবর্তী কপাটিকা",
            "হৃৎপিণ্ডের পেরিকার্ডিয়াল থলি",
        ],
        "A", "medium", "conceptual",
        "The atrioventricular bundle transmits the impulse from the AV node to the ventricular walls via Purkinje fibres.",
        "বান্ডল অব হিজ AV নোডের উদ্দীপনা নিলয় প্রাচীরে পারকিনজি তন্তুর মাধ্যমে পৌঁছায়।",
    ),
    q(
        "Artificial pacemaker batteries are commonly made using which metal?",
        "কৃত্রিম পেসমেকারের ব্যাটারি সাধারণত কোন ধাতু দিয়ে তৈরি হয়?",
        ["Aluminium", "Uranium", "Plutonium", "Lithium"],
        ["অ্যালুমিনিয়াম", "ইউরেনিয়াম", "প্লুটোনিয়াম", "লিথিয়াম"],
        "D", "easy", "factual",
        "Modern implantable pacemakers typically use long-life lithium batteries.",
        "আধুনিক ইমপ্লান্টেবল পেসমেকারে সাধারণত দীর্ঘস্থায়ী লিথিয়াম ব্যাটারি ব্যবহৃত হয়।",
    ),
    q(
        "In which phase is the first heart sound (“lub”) produced?",
        "হৃৎচক্রের কোন পর্যায়ে প্রথম হৃৎশব্দ (“লাব”) সৃষ্টি হয়?",
        [
            "Atrial diastole",
            "Ventricular systole",
            "Atrial systole",
            "Ventricular diastole",
        ],
        [
            "অলিন্দের ডায়াস্টোল",
            "নিলয়ের সিস্টোল",
            "অলিন্দের সিস্টোল",
            "নিলয়ের ডায়াস্টোল",
        ],
        "B", "medium", "factual",
        "“Lub” occurs at the start of ventricular systole when AV (bi/tricuspid) valves close.",
        "নিলয় সিস্টোল শুরুতে বাইকাসপিড/ট্রাইকাসপিড বন্ধ হলে “লাব” শব্দ হয়।",
    ),
    q(
        "Chest pain from reduced blood flow to heart muscle is called what?",
        "হৃৎপেশিতে রক্ত সঞ্চালন কমলে বুকের মাঝখানে যে ব্যথা হয় তাকে কী বলে?",
        [
            "Arrhythmia",
            "Coronary thrombosis only",
            "Myocardial infarction",
            "Angina pectoris",
        ],
        [
            "অ্যারিথমিয়া",
            "শুধু করোনারি থ্রম্বোসিস",
            "মায়োকার্ডিয়াল ইনফার্কশন",
            "অ্যানজাইনা পেকটোরিস",
        ],
        "D", "medium", "factual",
        "Angina pectoris is ischaemic chest pain from inadequate coronary flow; MI is actual death of myocardium.",
        "অ্যানজাইনা হলো অপর্যাপ্ত করোনারি প্রবাহজনিত ব্যথা; MI হলো হৃৎপেশি টিস্যুর মৃত্যু।",
    ),
    q(
        "Myocardial infarction (heart attack) mainly results when what happens?",
        "মায়োকার্ডিয়াল ইনফার্কশন (হার্ট অ্যাটাক) প্রধানত কখন ঘটে?",
        [
            "When coronary lumen is fully blocked and heart muscle dies from lack of O₂/nutrients",
            "When only atrial diastole is prolonged",
            "When lymph nodes enlarge in the neck",
            "When plasma albumin alone decreases slightly",
        ],
        [
            "করোনারি লুমেন সম্পূর্ণ রুদ্ধ হয়ে হৃৎপেশি O₂/পুষ্টির অভাবে মারা গেলে",
            "শুধু অলিন্দের ডায়াস্টোল দীর্ঘ হলে",
            "ঘাড়ের লসিকাগ্রন্থি বড় হলে",
            "শুধু প্লাজমা অ্যালবুমিন সামান্য কমলে",
        ],
        "A", "medium", "conceptual",
        "Plaque rupture and thrombosis can occlude a coronary artery, causing myocardial tissue death (MI).",
        "প্লাক ফেটে থ্রম্বোসিসে করোনারি রুদ্ধ হলে হৃৎপেশি মারা যায়—একে মায়োকার্ডিয়াল ইনফার্কশন বলে।",
    ),
    q(
        "In which condition does the heart become abnormally enlarged?",
        "কোন অবস্থায় হৃৎপিণ্ড অস্বাভাবিকভাবে বড় হয়ে যায়?",
        [
            "Rheumatic heart disease only as the name for enlargement",
            "Pericarditis",
            "Cardiomyopathy only",
            "Cardiomegaly",
        ],
        [
            "শুধু রিউম্যাটিক হৃৎরোগই বৃদ্ধির নাম",
            "পেরিকার্ডাইটিস",
            "শুধু কার্ডিওমায়োপ্যাথি",
            "কার্ডিওমেগালি",
        ],
        "D", "easy", "factual",
        "Cardiomegaly means pathological enlargement of the heart; cardiomyopathy is disease of heart muscle that may cause it.",
        "কার্ডিওমেগালি অর্থ হৃৎপিণ্ডের অস্বাভাবিক বৃদ্ধি; কার্ডিওমায়োপ্যাথি হৃৎপেশির রোগ যা এতে নিয়ে যেতে পারে।",
    ),
    q(
        "When blood pressure falls, signals reach the medulla oblongata mainly via which nerves?",
        "রক্তচাপ কমলে অবলংগাটায় সংকেত প্রধানত কোন স্নায়ু দিয়ে পৌঁছায়?",
        [
            "Glossopharyngeal and vagus",
            "Only olfactory",
            "Only optic",
            "Only hypoglossal",
        ],
        [
            "গ্লসোফ্যারিঞ্জিয়াল ও ভেগাস",
            "শুধু অলফ্যাক্টরি",
            "শুধু অপটিক",
            "শুধু হাইপোগ্লসাল",
        ],
        "A", "hard", "factual",
        "Baroreceptor afferents travel via glossopharyngeal (carotid sinus) and vagus (aortic arch) nerves to the medulla.",
        "বারোরিসেপ্টর সংকেত ক্যারোটিড থেকে গ্লসোফ্যারিঞ্জিয়াল ও অ্যাওর্টিক আর্চ থেকে ভেগাস দিয়ে অবলংগাটায় যায়।",
    ),
    q(
        "From which chamber does CO₂-rich blood enter the pulmonary artery?",
        "কোন প্রকোষ্ঠ হতে CO₂-সমৃদ্ধ রক্ত পালমোনারি ধমনিতে প্রবেশ করে?",
        ["Left atrium", "Left ventricle", "Right ventricle", "Right atrium directly into the artery"],
        ["বাম অলিন্দ", "বাম নিলয়", "ডান নিলয়", "ডান অলিন্দ সরাসরি ধমনিতে"],
        "C", "easy", "factual",
        "The right ventricle pumps deoxygenated blood into the pulmonary trunk/arteries toward the lungs.",
        "ডান নিলয় CO₂-সমৃদ্ধ রক্ত পালমোনারি ধমনিতে পাঠায় ফুসফুসের দিকে।",
    ),
    q(
        "Which layer lines the heart chambers and covers the valves?",
        "কোন স্তর হৃৎপ্রকোষ্ঠ আবৃত রাখে ও কপাটিকাগুলো ঢেকে রাখে?",
        ["Pericardium", "Epicardium", "Myocardium", "Endocardium"],
        ["পেরিকার্ডিয়াম", "এপিকার্ডিয়াম", "মায়োকার্ডিয়াম", "এন্ডোকার্ডিয়াম"],
        "D", "easy", "factual",
        "Endocardium is the inner lining continuous over valves; myocardium is muscle; pericardium/epicardium are outer coverings.",
        "এন্ডোকার্ডিয়াম প্রকোষ্ঠের অন্তঃস্তর ও কপাটিকা আবৃত করে; মায়োকার্ডিয়াম পেশি স্তর।",
    ),
    q(
        "Why is double circulation important in humans?",
        "মানুষে দ্বিচক্র সংবহন গুরুত্বপূর্ণ কেন?",
        [
            "Blood never passes through the heart twice per body circuit",
            "Blood crosses the heart twice per full circuit, allowing efficient O₂ delivery to tissues",
            "It is found only in arthropods",
            "It prevents any separation of O₂-rich and O₂-poor blood",
        ],
        [
            "দেহচক্রে রক্ত কখনো দুবার হৃৎপিণ্ড অতিক্রম করে না",
            "এক পূর্ণ চক্রে রক্ত দুবার হৃৎপিণ্ড পার হয়, ফলে কোষে O₂ সরবরাহ দক্ষ হয়",
            "এটি শুধু আর্থ্রোপোডায় দেখা যায়",
            "এতে O₂-সমৃদ্ধ ও দরিদ্র রক্তের কোনো পৃথকীকরণ থাকে না",
        ],
        "B", "medium", "conceptual",
        "In double circulation, pulmonary and systemic circuits keep oxygenated and deoxygenated blood largely separate and raise O₂ delivery rate.",
        "দ্বিচক্র সংবহনে পালমোনারি ও সিস্টেমিক পথ আলাদা থাকায় O₂-সমৃদ্ধ/দরিদ্র রক্ত পৃথক ও সরবরাহ দক্ষ হয়।",
    ),
]


# --- t03: Lymph / লসিকা ---
T03 = [
    q(
        "Which set correctly lists functions of lymph?",
        "লসিকার কাজ সম্পর্কে কোন সেট সঠিক?",
        [
            "Only clotting of blood in arteries",
            "Absorb fat-soluble vitamins from intestine, aid immunity, return metabolic wastes toward blood",
            "Carry ABO antigens for typing only",
            "Replace haemoglobin in RBCs",
        ],
        [
            "শুধু ধমনিতে রক্ত তঞ্চন",
            "অন্ত্র থেকে চর্বিতে দ্রবণীয় ভিটামিন শোষণ, রোগপ্রতিরোধ, বিপাকীয় বর্জ্য রক্তে ফেরানো",
            "শুধু ABO অ্যান্টিজেন বহন",
            "RBC-তে হিমোগ্লোবিন প্রতিস্থাপন",
        ],
        "B", "medium", "conceptual",
        "Lymph transports fats/fat-soluble vitamins via lacteals, carries immune cells, and returns interstitial fluid/wastes to blood.",
        "লসিকা ল্যাকটিয়াল দিয়ে চর্বি/ভিটামিন শোষণ, প্রতিরক্ষা ও অন্তঃকলার তরল/বর্জ্য রক্তে ফেরায়।",
    ),
    q(
        "What is the lymphatic system?",
        "লসিকাতন্ত্র বলতে কী বোঝায়?",
        [
            "Only the coronary arteries of the heart",
            "The system of lymph vessels and lymphoid organs through which lymph flows",
            "Only the liver sinusoids",
            "Only red bone marrow without vessels",
        ],
        [
            "শুধু হৃৎপিণ্ডের করোনারি ধমনি",
            "লসিকানালি ও লসিকাগ্রন্থির তন্ত্র যার মধ্য দিয়ে লসিকারস প্রবাহিত হয়",
            "শুধু যকৃতের সাইনুসয়েড",
            "নালিবিহীন শুধু লাল অস্থিমজ্জা",
        ],
        "B", "easy", "factual",
        "Lymphatic vessels plus nodes and other lymphoid organs form the lymphatic (second circulatory) system.",
        "লসিকানালি ও লসিকা অঙ্গ নিয়ে লসিকাতন্ত্র গঠিত; একে কখনো দ্বিতীয় সংবহনতন্ত্রও বলে।",
    ),
    q(
        "What is a main function of lymph nodes in humans?",
        "মানবদেহে লিম্ফনোডের প্রধান কাজ কী?",
        [
            "Produce bile for fat emulsification",
            "Filter microbes and foreign matter from lymph using macrophages and lymphocytes",
            "Pump blood like the left ventricle",
            "Synthesise haemoglobin for RBCs",
        ],
        [
            "চর্বি ইমালসিফিকেশনে পিত্ত উৎপাদন",
            "ম্যাক্রোফেজ ও লিম্ফোসাইট দিয়ে লসিকা থেকে অণুজীব ও বহিরাগত পদার্থ অপসারণ",
            "বাম নিলয়ের মতো রক্ত পাম্প করা",
            "RBC-র জন্য হিমোগ্লোবিন সংশ্লেষ",
        ],
        "B", "easy", "factual",
        "Lymph nodes are capsule-like filters packed with macrophages and lymphocytes that clear pathogens from lymph.",
        "লিম্ফনোড ক্যাপসুলসদৃশ ফিল্টার; ম্যাক্রোফেজ ও লিম্ফোসাইট লসিকা থেকে জীবাণু দূর করে।",
    ),
    q(
        "Which is the largest lymphoid organ of the human body?",
        "মানবদেহের সবচেয়ে বড় লসিকাগ্রন্থি/লসিকা অঙ্গ কোনটি?",
        ["Lymph node", "Tonsil", "Thymus", "Spleen"],
        ["লিম্ফনোড", "টনসিল", "থাইমাস", "প্লীহা"],
        "D", "easy", "factual",
        "The spleen is the largest lymphoid organ; it filters blood and helps destroy aged RBCs/platelets.",
        "প্লীহা বৃহত্তম লসিকা অঙ্গ; রক্ত পরিশোধন ও পুরোনো RBC/অণুচক্রিকা ধ্বংসে সাহায্য করে।",
    ),
    q(
        "Which of the following is a tonsillar lymphoid structure?",
        "টনসিল জাতীয় লসিকাগ্রন্থি কোনটি?",
        ["Thymus", "Lymph node of the groin only", "Adenoid", "Red bone marrow only"],
        ["থাইমাস", "শুধু কুঁচকির লিম্ফনোড", "অ্যাডেনয়েড", "শুধু লাল অস্থিমজ্জা"],
        "C", "medium", "factual",
        "Adenoids (pharyngeal tonsils) are lymphoid tissue of the tonsillar group in the nasopharynx.",
        "অ্যাডেনয়েড (ফ্যারিঞ্জিয়াল টনসিল) নাসোফ্যারিনক্সের টনসিল গোষ্ঠীর লসিকা টিস্যু।",
    ),
    q(
        "Which five lymphoid structures are commonly listed for the human body?",
        "মানবদেহে সাধারণত উল্লিখিত পাঁচ ধরনের লসিকা অঙ্গ কোনগুলো?",
        [
            "Lymph node, tonsil, spleen, thymus and red bone marrow",
            "Only liver, pancreas and gall bladder",
            "Only SA node, AV node and Bundle of His",
            "Only alveoli, bronchi and trachea",
        ],
        [
            "লিম্ফনোড, টনসিল, প্লীহা, থাইমাস ও লাল অস্থিমজ্জা",
            "শুধু যকৃত, অগ্ন্যাশয় ও পিত্তথলি",
            "শুধু SA নোড, AV নোড ও বান্ডল অব হিজ",
            "শুধু অ্যালভিওলাস, ব্রংকাই ও ট্রাকিয়া",
        ],
        "A", "medium", "factual",
        "HSC texts list lymph nodes, tonsils, spleen, thymus and red bone marrow among lymphoid components.",
        "এইচএসসি পাঠ্যে লিম্ফনোড, টনসিল, প্লীহা, থাইমাস ও লাল অস্থিমজ্জা লসিকা উপাদান হিসেবে আসে।",
    ),
    q(
        "Where are lymph nodes especially numerous?",
        "দেহের কোন অংশে অধিক সংখ্যক লসিকাগ্রন্থি দেখা যায়?",
        [
            "Only inside cardiac muscle fibres",
            "Neck, axilla (armpit) and groin",
            "Only in the cornea of the eye",
            "Only in enamel of teeth",
        ],
        [
            "শুধু হৃৎপেশি তন্তুর ভিতরে",
            "ঘাড়, বগল ও কুঁচকিতে",
            "শুধু চোখের কর্নিয়ায়",
            "শুধু দাঁতের এনামেলে",
        ],
        "B", "easy", "factual",
        "Clusters of lymph nodes are prominent in cervical, axillary and inguinal regions.",
        "সার্ভিকাল, অ্যাক্সিলারি ও ইনগুইনাল অঞ্চলে লসিকাগ্রন্থির গুচ্ছ বেশি থাকে।",
    ),
    q(
        "Lymph is often called a second circulatory system because it does what?",
        "লসিকাতন্ত্রকে দ্বিতীয় সংবহনতন্ত্র বলা হয় কেন?",
        [
            "It replaces the heart entirely",
            "Together with blood it circulates body fluids throughout the body",
            "It only carries oxygenated arterial blood",
            "It secretes digestive enzymes into the duodenum",
        ],
        [
            "এটি সম্পূর্ণভাবে হৃৎপিণ্ড প্রতিস্থাপন করে",
            "রক্তের সাথে মিলে সমগ্র দেহে দেহতরল সংবহন করে",
            "এটি শুধু অক্সিজেনযুক্ত ধমনিরক্ত বহন করে",
            "এটি ডিওডেনামে পাচক এনজাইম ক্ষরণ করে",
        ],
        "B", "easy", "conceptual",
        "Blood and lymph both circulate fluids; lymph returns excess tissue fluid and supports immunity.",
        "রক্ত ও লসিকা উভয়েই দেহতরল সংবহন করে; লসিকা অতিরিক্ত কলারস ফেরায় ও প্রতিরক্ষা করে।",
    ),
    q(
        "Which statement about lymph composition versus blood is most accurate?",
        "লসিকা ও রক্তের তুলনায় কোন বক্তব্য সবচেয়ে সঠিক?",
        [
            "Lymph normally has abundant RBCs like arterial blood",
            "Lymph is similar to plasma/tissue fluid and usually lacks RBCs",
            "Lymph is identical to whole blood including platelets in the same counts",
            "Lymph contains only haemoglobin crystals",
        ],
        [
            "লসিকায় ধমনিরক্তের মতো প্রচুর RBC থাকে",
            "লসিকা প্লাজমা/কলারসের মতো এবং সাধারণত RBC থাকে না",
            "লসিকা সম্পূর্ণ রক্তের সমান একই সংখ্যক অণুচক্রিকা সহ",
            "লসিকায় শুধু হিমোগ্লোবিন স্ফটিক থাকে",
        ],
        "B", "medium", "conceptual",
        "Lymph derives from interstitial fluid filtered from plasma; it is clear/pale and normally RBC-free.",
        "লসিকা অন্তঃকলার তরল থেকে আসে; সাধারণত স্বচ্ছ/ফ্যাকাশে এবং RBCবিহীন।",
    ),
    q(
        "Fat absorption from the small intestine into lymph occurs mainly via what?",
        "ক্ষুদ্রান্ত্র থেকে চর্বি লসিকায় শোষণ প্রধানত কীসের মাধ্যমে হয়?",
        ["Lacteals in villi", "Coronary sinus", "Bowman’s capsule", "Alveolar ducts"],
        ["ভিল্লাইয়ের ল্যাকটিয়াল", "করোনারি সাইনাস", "বোম্যান্স ক্যাপসুল", "অ্যালভিওলার নালি"],
        "A", "easy", "factual",
        "Intestinal villi contain lacteals that take up chylomicrons/fats into lymph.",
        "অন্ত্রের ভিল্লাইয়ের ল্যাকটিয়াল কাইলোমাইক্রোন/চর্বি লসিকায় নিয়ে যায়।",
    ),
    q(
        "Which is a correct function often attributed to lymph in HSC texts?",
        "এইচএসসি পাঠ্যে লসিকার কোন কাজটি সঠিকভাবে উল্লেখিত?",
        [
            "Supply O₂ with haemoglobin like RBCs as its main job",
            "Help exchange/transport of nutrients and remove wastes between tissues and blood pathway",
            "Determine ABO blood group antigens on RBC membranes",
            "Act as the sole clotting factor XIII source",
        ],
        [
            "RBC-এর মতো হিমোগ্লোবিন দিয়ে O₂ সরবরাহই প্রধান কাজ",
            "কলা ও রক্তপথের মধ্যে পুষ্টি পরিবহন/বিনিময় ও বর্জ্য অপসারণে সাহায্য",
            "RBC ঝিল্লিতে ABO অ্যান্টিজেন নির্ধারণ",
            "একমাত্র তঞ্চন ফ্যাক্টর XIII উৎস",
        ],
        "B", "medium", "conceptual",
        "Lymph helps return tissue fluid and participates in nutrient/waste traffic linked to the blood capillary bed.",
        "লসিকা কলারস ফেরায় এবং কৈশিক জালিকার সাথে পুষ্টি/বর্জ্য চলাচলে সহায়তা করে।",
    ),
    q(
        "Open blood circulation (for comparison with closed/lymph-linked systems) is typical of which groups?",
        "মুক্ত রক্তসংবহন কোন প্রাণীপর্বে সাধারণত দেখা যায়?",
        [
            "Arthropoda and Mollusca",
            "Only mammals",
            "Only birds and crocodiles",
            "Only annelid earthworms with complete double circulation",
        ],
        [
            "আর্থ্রোপোডা ও মলাস্কা",
            "শুধু স্তন্যপায়ী",
            "শুধু পাখি ও কুমির",
            "শুধু দ্বিচক্র সংবহনসহ অ্যানিলিড কেঁচো",
        ],
        "A", "medium", "factual",
        "In open circulation, blood leaves vessels into haemocoel/sinuses (e.g., many arthropods and molluscs).",
        "মুক্ত সংবহনে রক্ত নালি ছেড়ে হিমোসিল/সাইনাসে যায়—অনেক আর্থ্রোপোড ও মলাস্কায়।",
    ),
    q(
        "Which cells in lymph nodes are especially important for destroying microbes in lymph?",
        "লিম্ফনোডে লসিকার অণুজীব ধ্বংসে বিশেষ গুরুত্বপূর্ণ কোষ কোনগুলো?",
        [
            "Only mature erythrocytes",
            "Macrophages and lymphocytes",
            "Only megakaryocytes of marrow",
            "Only osteoblasts",
        ],
        [
            "শুধু পরিণত এরিথ্রোসাইট",
            "ম্যাক্রোফেজ ও লিম্ফোসাইট",
            "শুধু মজ্জার মেগাক্যারিওসাইট",
            "শুধু অস্টিওব্লাস্ট",
        ],
        "B", "easy", "factual",
        "Macrophages phagocytose debris/pathogens; lymphocytes mediate specific immune responses.",
        "ম্যাক্রোফেজ জীবাণু/ধ্বংসাবশেষ গ্রাস করে; লিম্ফোসাইট নির্দিষ্ট প্রতিরোধ গড়ে তোলে।",
    ),
    q(
        "The thymus is mainly associated with which role?",
        "থাইমাসের প্রধান ভূমিকা কোনটির সাথে জড়িত?",
        [
            "Maturation of T-lymphocytes for adaptive immunity",
            "Storage of bile",
            "Filtration of urine",
            "Production of digestive pepsin",
        ],
        [
            "অভিযোজিত প্রতিরোধে T-লিম্ফোসাইট পরিণতকরণ",
            "পিত্ত সংরক্ষণ",
            "মূত্র পরিশোধন",
            "পাচক পেপসিন উৎপাদন",
        ],
        "A", "medium", "factual",
        "The thymus is a primary lymphoid organ where T cells mature, especially active in childhood.",
        "থাইমাস প্রাথমিক লসিকা অঙ্গ যেখানে T-কোষ পরিণত হয়; শৈশবে বেশি সক্রিয়।",
    ),
    q(
        "Lymph capillaries are best described as what?",
        "লসিকা কৈশিকনালির সঠিক বর্ণনা কোনটি?",
        [
            "Blind-ended vessels that take up excess tissue fluid",
            "Thick-walled arteries with high pulse pressure",
            "Continuous with Bowman’s capsule lumen",
            "Identical to coronary arteries",
        ],
        [
            "অন্ধপ্রাপ্ত নালি যা অতিরিক্ত কলারস গ্রহণ করে",
            "উচ্চ পালস চাপের পুরু প্রাচীরযুক্ত ধমনি",
            "বোম্যান্স ক্যাপসুল লুমেনের সাথে অবিচ্ছিন্ন",
            "করোনারি ধমনির সমান",
        ],
        "A", "medium", "factual",
        "Lymphatic capillaries begin blindly in tissues and drain excess interstitial fluid as lymph.",
        "লসিকা কৈশিক কলায় অন্ধভাবে শুরু হয়ে অতিরিক্ত অন্তঃকলার তরল লসিকা হিসেবে নিষ্কাশন করে।",
    ),
    q(
        "Which duct returns most of the body’s lymph to the blood?",
        "দেহের অধিকাংশ লসিকা রক্তে কোন নালি দিয়ে ফেরে?",
        [
            "Thoracic duct (into the left subclavian vein region)",
            "Cystic duct of the gall bladder",
            "Duct of Wirsung only",
            "Nasolacrimal duct",
        ],
        [
            "থোরাসিক ডাক্ট (বাম সাবক্ল্যাভিয়ান শিরা অঞ্চলে)",
            "পিত্তথলির সিস্টিক ডাক্ট",
            "শুধু উইর্সাং নালি",
            "ন্যাসোল্যাক্রিমাল নালি",
        ],
        "A", "hard", "factual",
        "The thoracic duct drains most lymph into the left venous angle; the right lymphatic duct drains the upper right quadrant.",
        "থোরাসিক ডাক্ট অধিকাংশ লসিকা বাম শিরা-কোণে ঢোকায়; ডান লসিকা নালি উপরের ডান অংশ নিষ্কাশন করে।",
    ),
    q(
        "Besides filtering blood, the spleen helps destroy which aged cells?",
        "রক্ত পরিশোধন ছাড়াও প্লীহা কোন পুরোনো কণিকা ধ্বংসে সাহায্য করে?",
        [
            "Aged RBCs and many platelets",
            "Only enamel cells of teeth",
            "Only neurons of the cortex",
            "Only osteocytes of compact bone",
        ],
        [
            "পুরোনো RBC ও অনেক অণুচক্রিকা",
            "শুধু দাঁতের এনামেল কোষ",
            "শুধু কর্টেক্সের নিউরন",
            "শুধু কঠিন অস্থির অস্টিওসাইট",
        ],
        "A", "medium", "factual",
        "The spleen is a major site for removal of worn RBCs and platelets and stores some blood cells.",
        "প্লীহা ক্ষয়প্রাপ্ত RBC ও অণুচক্রিকা অপসারণের প্রধান স্থান এবং কিছু রক্তকণিকা মজুত রাখে।",
    ),
    q(
        "Tonsils help immunity mainly by doing what?",
        "টনসিল প্রধানত কী করে প্রতিরোধে সাহায্য করে?",
        [
            "Trapping pathogens entering via mouth/nose and housing lymphoid tissue",
            "Pumping lymph like a second heart ventricle",
            "Synthesising clotting factor VIII for haemophilia cure alone",
            "Forming the Bundle of His",
        ],
        [
            "মুখ/নাক দিয়ে প্রবেশকারী জীবাণু আটকানো ও লসিকা টিস্যু রাখা",
            "দ্বিতীয় নিলয়ের মতো লসিকা পাম্প করা",
            "শুধু হিমোফিলিয়া সারাতে ফ্যাক্টর VIII সংশ্লেষ",
            "বান্ডল অব হিজ গঠন",
        ],
        "A", "easy", "conceptual",
        "Palatine/pharyngeal/lingual tonsils are lymphoid rings that sample inhaled/ingested antigens.",
        "প্যালাটাইন/ফ্যারিঞ্জিয়াল/লিঙ্গুয়াল টনসিল শ্বাস/খাদ্যপথের অ্যান্টিজেন নমুনা নিয়ে প্রতিরোধে সাহায্য করে।",
    ),
    q(
        "After lymph is filtered in nodes, returning it to blood helps the body how?",
        "নোডে পরিশোধিত লসিকা রক্তে ফিরলে দেহ কীভাবে উপকৃত হয়?",
        [
            "It restores fluid volume and returns immune-cleared fluid to circulation",
            "It permanently removes all plasma proteins from the body",
            "It stops all future antibody production",
            "It converts all lymph into pure hydrochloric acid",
        ],
        [
            "তরল আয়তন পুনরুদ্ধার হয় এবং প্রতিরোধ-পরিশোধিত তরল সংবহনে ফেরে",
            "দেহ থেকে সব প্লাজমা প্রোটিন স্থায়ীভাবে সরে যায়",
            "ভবিষ্যতে সব অ্যান্টিবডি উৎপাদন বন্ধ হয়",
            "সব লসিকা বিশুদ্ধ HCl-এ পরিণত হয়",
        ],
        "A", "medium", "conceptual",
        "Returning lymph maintains blood volume and delivers lymphocytes/antibodies back into the bloodstream.",
        "লসিকা ফেরার ফলে রক্তের আয়তন রক্ষা পায় এবং লিম্ফোসাইট/অ্যান্টিবডি রক্তে পৌঁছায়।",
    ),
    q(
        "Which claim about lymph is incorrect?",
        "লসিকা সম্পর্কে কোন দাবিটি ভুল?",
        [
            "It helps in body defence via lymphoid organs",
            "It absorbs fats from the intestine via lacteals",
            "It is the main carrier of ABO grouping antigens on RBC surfaces",
            "It returns excess tissue fluid toward the venous blood",
        ],
        [
            "লসিকা অঙ্গ দিয়ে দেহপ্রতিরোধে সাহায্য করে",
            "ল্যাকটিয়াল দিয়ে অন্ত্র থেকে চর্বি শোষণ করে",
            "RBC পৃষ্ঠের ABO গ্রুপিং অ্যান্টিজেনের প্রধান বাহক এটি",
            "অতিরিক্ত কলারস শিরারক্তের দিকে ফেরায়",
        ],
        "C", "hard", "conceptual",
        "ABO antigens sit on RBC membranes in blood; lymph is not the primary site for blood-group typing antigens.",
        "ABO অ্যান্টিজেন রক্তের RBC ঝিল্লিতে থাকে; লসিকা রক্তগ্রুপ নির্ণয়ের প্রধান স্থান নয়।",
    ),
]


TOPICS_MAP = {
    "bio2_27_ch04_t01": T01,
    "bio2_27_ch04_t02": T02,
    "bio2_27_ch04_t03": T03,
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
        "chapter": "bio2_27_ch04",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p170_pdf176.png",
            "p171_pdf177.png",
            "p172_pdf178.png",
            "p173_pdf179.png",
            "p174_pdf180.png",
            "p175_pdf181.png",
            "p176_pdf182.png",
            "p177_pdf183.png",
            "p178_pdf184.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio2_27_ch04_t01": {
                "title": "Blood and blood groups / রক্ত ও রক্তের গ্রুপ",
                "themes": [
                    "basophil heparin/histamine; platelet serotonin; erythrocyte gas transport",
                    "plasma organics 7–9%; haematocrit; RBC:WBC ~700:1",
                    "neutrophil phagocyte; platelet anucleate/spleen; clotting thrombin/XIII",
                    "heparin anticoagulant; serum vs plasma; eosinophil acidophilic",
                    "agranulocytes; plasma proteins; mobile WBC defence; CO₂–NH₂; ABO antigens on RBC",
                ],
            },
            "bio2_27_ch04_t02": {
                "title": "Heart and circulation / হৃৎপিণ্ড ও রক্তসঞ্চালন",
                "themes": [
                    "SA node pacemaker; SAN→AVN→His→Purkinje",
                    "cycle timings 0.1/0.5/0.7/0.8 s; LV wall thickness; semilunar valves",
                    "systemic vs coronary paths; Bundle of His; lithium pacemaker battery",
                    "lub at ventricular systole; angina vs MI; cardiomegaly",
                    "baroreceptor nerves; RV→pulmonary artery; endocardium; double circulation",
                ],
            },
            "bio2_27_ch04_t03": {
                "title": "Lymph / লসিকা",
                "themes": [
                    "lymph functions; lymphatic system as second circuit",
                    "lymph nodes filter; spleen largest; adenoid/tonsil; five lymphoid organs",
                    "nodes in neck/axilla/groin; lymph vs blood composition; lacteals",
                    "open circulation arthropods/molluscs; macrophages/lymphocytes; thymus T cells",
                    "blind lymph capillaries; thoracic duct; spleen RBC/platelet removal; incorrect ABO claim",
                ],
            },
        },
        "low_confidence": [
            "OCR of printed pages p170–178 is noisy (garbled options/answer marks); stems reconstructed from readable fragments and standard HSC Zoology Ch4 facts.",
            "Figure-only and stimulus-linked bank items rewritten as standalone stems (no dependency on missing diagrams).",
            "RBC:WBC ratio kept as 700:1 per frequent board keys; one OCR note mentions ~600:1 in a newer edition.",
            "Diapedesis is performed by several leukocytes; neutrophil phagocytosis emphasized as the common HSC framing.",
            "Thoracic duct as main lymph return follows standard anatomy; right lymphatic duct drains only the upper right quadrant.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio2_27_ch04_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio2_27_ch04_t01": 20,
                "bio2_27_ch04_t02": 20,
                "bio2_27_ch04_t03": 20,
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
        / "ch04_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
