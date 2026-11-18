#!/usr/bin/env python3
"""Seed Biology 2nd Paper Ch5 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio2_27_ch05_t01..t03 (Respiratory organs; Breathing/gas exchange; Cellular respiration).
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
    "biology p2 ch05; curated bilingual"
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


# --- t01: Respiratory organs / শ্বাসযন্ত্র ---
T01 = [
    q(
        "How many vocal cords are present in the human larynx?",
        "মানুষের স্বরযন্ত্রে ভোকাল কর্ডের সংখ্যা কত?",
        ["2", "4", "6", "8"],
        ["২", "৪", "৬", "৮"],
        "A", "easy", "numerical",
        "HSC texts commonly cite one pair (2) of vocal cords in the larynx that vibrate to produce sound.",
        "এইচএসসি পাঠ্যে সাধারণত স্বরযন্ত্রে এক জোড়া (২টি) ভোকাল কর্ড উল্লেখ থাকে যা কম্পিত হয়ে শব্দ সৃষ্টি করে।",
    ),
    q(
        "Which sinus lies between the two eyes in humans?",
        "মানুষের দুচোখের মধ্যবর্তী সাইনাসের নাম কী?",
        ["Maxillary", "Frontal", "Sphenoid", "Ethmoid"],
        ["ম্যাক্সিলারি", "ফ্রন্টাল", "স্ফেনয়েড", "এথময়েড"],
        "D", "medium", "factual",
        "The ethmoid sinus (ethmoidal air cells) lies in the ethmoid bone between the orbits.",
        "এথময়েড সাইনাস দুই অক্ষিকোটরের মধ্যবর্তী এথময়েড অস্থিতে অবস্থিত।",
    ),
    q(
        "How many lobes does the left human lung have?",
        "বাম ফুসফুসে কতটি লোব থাকে?",
        ["2", "3", "4", "5"],
        ["২টি", "৩টি", "৪টি", "৫টি"],
        "A", "easy", "numerical",
        "The left lung has two lobes (superior and inferior); the right lung has three.",
        "বাম ফুসফুসে দুটি লোব (ঊর্ধ্ব ও অধঃ); ডান ফুসফুসে তিনটি লোব থাকে।",
    ),
    q(
        "In which organ are bronchioles found?",
        "নিচের কোন অঙ্গে ব্রঙ্কিওল বিদ্যমান?",
        ["Lung", "Heart", "Liver", "Femur"],
        ["ফুসফুস", "হৃৎপিণ্ড", "যকৃত", "ফিমার"],
        "A", "easy", "factual",
        "Bronchioles are the finer airway branches inside the lungs leading to alveolar ducts.",
        "ব্রঙ্কিওল ফুসফুসের অভ্যন্তরের সূক্ষ্ম শ্বাসনালি যা আ্যালভিওলার নালির দিকে যায়।",
    ),
    q(
        "The phrenic artery mainly supplies blood to which structure?",
        "ফ্রেনিক ধমনি মানুষের কোন অংশে রক্ত সরবরাহ করে?",
        ["Intercostal muscles", "Diaphragm", "Shoulder", "Thoracic vertebrae"],
        ["ইন্টারকোস্টাল পেশি", "ডায়াফ্রাম", "কাঁধ", "বক্ষ অস্থিচক্র"],
        "B", "medium", "factual",
        "Phrenic arteries (and the phrenic nerves) serve the diaphragm, the primary muscle of inspiration.",
        "ফ্রেনিক ধমনি (ও ফ্রেনিক স্নায়ু) প্রধান শ্বাসপেশি ডায়াফ্রামকে রক্ত সরবরাহ/নিয়ন্ত্রণ করে।",
    ),
    q(
        "Adam’s apple refers to which laryngeal cartilage?",
        "Adam’s Apple বলা হয় কোন তরুণাস্থিকে?",
        ["Cricoid", "Corniculate", "Thyroid", "Arytenoid"],
        ["ক্রিকয়েড", "কর্নিকুলেট", "থাইরয়েড", "অ্যারিটিনয়েড"],
        "C", "easy", "factual",
        "The laryngeal prominence of the thyroid cartilage is commonly called Adam’s apple.",
        "থাইরয়েড তরুণাস্থির অগ্রভাগের উদ্গত অংশকে সাধারণত Adam’s apple বলে।",
    ),
    q(
        "What are the two branches formed by bifurcation of the trachea called?",
        "মানবদেহে ট্রাকিয়ার দ্বিবিভাজনে সৃষ্ট শাখা দুটিকে কী বলে?",
        ["Terminal bronchioles", "Primary bronchi", "Secondary bronchi", "Tertiary bronchi"],
        ["প্রান্তীয় ব্রঙ্কিওল", "প্রাইমারি ব্রঙ্কাস", "সেকেন্ডারি ব্রঙ্কাস", "টার্সিয়ারি ব্রঙ্কাস"],
        "B", "easy", "factual",
        "The trachea divides into right and left primary (main) bronchi that enter the lungs.",
        "ট্রাকিয়া ডান ও বাম প্রাইমারি (মেইন) ব্রঙ্কাসে বিভক্ত হয়ে ফুসফুসে প্রবেশ করে।",
    ),
    q(
        "Where is pulmonary surfactant secreted?",
        "সারফ্যাকট্যান্ট কোথায় ক্ষরিত হয়?",
        ["In alveoli", "In sinuses", "In bronchioles", "In the trachea"],
        ["আ্যালভিওলাসে", "সাইনাসে", "ব্রঙ্কিওলে", "ট্রাকিয়াতে"],
        "A", "easy", "factual",
        "Type II (septal) alveolar cells secrete phospholipid surfactant that coats the alveolar lining.",
        "টাইপ-২ (সেপ্টাল) আ্যালভিওলার কোষ ফসফোলিপিড সারফ্যাকট্যান্ট ক্ষরণ করে আ্যালভিওলাস আবৃত করে।",
    ),
    q(
        "At about how many weeks of fetal age does surfactant secretion first begin?",
        "কত সপ্তাহ বয়স্ক মানবভ্রূণে সর্বপ্রথম সারফ্যাকট্যান্ট ক্ষরণ শুরু হয়?",
        ["20", "23", "28", "32"],
        ["২০", "২৩", "২৮", "৩২"],
        "B", "medium", "numerical",
        "Board items commonly place the onset of fetal surfactant secretion at about 23 weeks.",
        "বোর্ড প্রশ্নে সাধারণত প্রায় ২৩ সপ্তাহ বয়স্ক ভ্রূণে সারফ্যাকট্যান্ট ক্ষরণ শুরুর উল্লেখ থাকে।",
    ),
    q(
        "Which is NOT a function of surfactant?",
        "নিচের কোনটি সারফ্যাকট্যান্ট এর কাজ নয়?",
        [
            "Prevents alveolar collapse",
            "Facilitates alveolar gas exchange",
            "Acts in a detergent-like way on alveolar fluid",
            "Reduces alveolar working efficiency",
        ],
        [
            "আ্যালভিওলাসের চুপসে যাওয়া রোধ করে",
            "আ্যালভিওলাসে গ্যাসীয় বিনিময় সহজ করে",
            "ডিটারজেন্টের ন্যায় কাজ করে",
            "আ্যালভিওলাসের কর্মক্ষমতা হ্রাস করে",
        ],
        "D", "easy", "conceptual",
        "Surfactant lowers surface tension, prevents collapse, and aids gas exchange; it does not reduce efficiency.",
        "সারফ্যাকট্যান্ট পৃষ্ঠটান কমিয়ে চুপসে যাওয়া রোধ ও গ্যাস বিনিময় সহজ করে; কর্মক্ষমতা হ্রাস করে না।",
    ),
    q(
        "Which statements about the alveolar wall are correct?",
        "আ্যালভিওলাসের প্রাচীর সম্পর্কে কোনগুলো সঠিক?",
        [
            "Only collagen fibres form the wall",
            "It is lined by squamous epithelium and has septal cells that secrete surfactant",
            "It lacks epithelial cells",
            "It is made only of cartilage rings",
        ],
        [
            "শুধু কোলাজেন তন্তু দিয়ে গঠিত",
            "স্কোয়ামাস এপিথেলিয়ামে আবৃত এবং সারফ্যাকট্যান্ট ক্ষরক সেপ্টাল কোষ সমৃদ্ধ",
            "এতে এপিথেলিয়াল কোষ নেই",
            "শুধু তরুণাস্থি বলয় দিয়ে গঠিত",
        ],
        "B", "medium", "conceptual",
        "Alveoli have thin squamous epithelium; type II septal cells secrete surfactant for gas exchange support.",
        "আ্যালভিওলাস পাতলা স্কোয়ামাস এপিথেলিয়াম ও টাইপ-২ সেপ্টাল কোষসমৃদ্ধ যা সারফ্যাকট্যান্ট ক্ষরণ করে।",
    ),
    q(
        "The two layers of the pleural membrane of the lung are called what?",
        "ফুসফুসের দ্বিস্তরী প্লিউরাল পর্দার অংশ কোনগুলো?",
        [
            "Vestibule and parietal",
            "Visceral and lobule",
            "Bronchiole and lobule",
            "Visceral and parietal",
        ],
        [
            "ভেস্টিবিউল ও প্যারাইটাল",
            "ভিসেরাল ও লোবিউল",
            "ব্রঙ্কিওল ও লোবিউল",
            "ভিসেরাল ও প্যারাইটাল",
        ],
        "D", "easy", "factual",
        "Pleura has a visceral layer on the lung surface and a parietal layer lining the thoracic wall.",
        "প্লিউরার ভিসেরাল স্তর ফুসফুস গায়ে এবং প্যারাইটাল স্তর বক্ষপ্রাচীরে থাকে।",
    ),
    q(
        "Where are trabeculae found among the following?",
        "ট্র্যাবেকুলী কোথায় পাওয়া যায়?",
        ["Liver only", "Blood only", "Lungs", "Bone marrow only"],
        ["শুধু যকৃতে", "শুধু রক্তে", "ফুসফুসে", "শুধু অস্থিমজ্জায়"],
        "C", "medium", "factual",
        "Lung parenchyma is supported by connective-tissue trabeculae (also seen in other organs, but among these options the lung is correct for the bank item).",
        "ফুসফুসীয় প্যারেনকাইমা সংযোজক কলার ট্র্যাবেকুলা দ্বারা দৃঢ় থাকে; প্রদত্ত অপশনে ফুসফুসই সঠিক।",
    ),
    q(
        "In which part of the respiratory tract are olfactory cells located?",
        "শ্বসনতন্ত্রের কোন অংশে অলফ্যাক্টরী কোষ থাকে?",
        ["Vestibule", "Nasal cavity", "Posterior naris only", "Nasopharynx"],
        ["ভেস্টিবিউল", "নাসাগহ্বর", "শুধু পশ্চাৎ নাসারন্ধ্র", "নাসাগলবিল"],
        "B", "easy", "factual",
        "Olfactory receptor cells lie in the olfactory epithelium of the upper nasal cavity.",
        "অলফ্যাক্টরী কোষ নাসাগহ্বরের ঊর্ধ্বাংশের অলফ্যাক্টরী এপিথেলিয়ামে অবস্থিত।",
    ),
    q(
        "Inflammation of which sinus commonly causes cheek and tooth pain?",
        "কোন সাইনাসের প্রদাহের কারণে মানুষের গালে ও দাঁতে ব্যথা হয়?",
        ["Frontal", "Maxillary", "Ethmoid", "Sphenoid"],
        ["ফ্রন্টাল", "ম্যাক্সিলারি", "এথময়েড", "স্ফেনয়েড"],
        "B", "medium", "factual",
        "Maxillary sinuses lie beside the upper jaw; their inflammation often refers pain to cheek and teeth.",
        "ম্যাক্সিলারি সাইনাস উপরের চোয়ালের পাশে; প্রদাহে গাল ও দাঁতে ব্যথা হয়।",
    ),
    q(
        "What is the main protective role of the epiglottis during swallowing?",
        "গলাধঃকরণের সময় এপিগ্লটিসের প্রধান কাজ কী?",
        [
            "It vibrates to produce voice",
            "It closes the laryngeal opening so food does not enter the airway",
            "It secretes surfactant",
            "It exchanges O₂ and CO₂",
        ],
        [
            "এটি কম্পিত হয়ে স্বর সৃষ্টি করে",
            "স্বরযন্ত্রের মুখ বন্ধ করে খাদ্য শ্বাসনালিতে না ঢোকে",
            "এটি সারফ্যাকট্যান্ট ক্ষরণ করে",
            "এটি O₂ ও CO₂ বিনিময় করে",
        ],
        "B", "easy", "conceptual",
        "During swallowing the epiglottis covers the glottis, directing food toward the oesophagus.",
        "গলাধঃকরণে এপিগ্লটিস গ্লটিস ঢেকে খাদ্যকে অন্ননালির দিকে পরিচালিত করে।",
    ),
    q(
        "Which laryngeal cartilages are correctly listed together?",
        "স্বরযন্ত্রের তরুণাস্থি হিসেবে কোনগুলো একসাথে সঠিক?",
        [
            "Thyroid only",
            "Cricoid and hyoid only",
            "Thyroid, cricoid and arytenoid",
            "Only tracheal C-rings",
        ],
        [
            "শুধু থাইরয়েড",
            "শুধু ক্রিকয়েড ও হায়েড",
            "থাইরয়েড, ক্রিকয়েড ও অ্যারিটিনয়েড",
            "শুধু ট্রাকিয়ার C-বলয়",
        ],
        "C", "medium", "factual",
        "Major laryngeal cartilages include thyroid, cricoid and arytenoid (plus smaller ones).",
        "স্বরযন্ত্রের প্রধান তরুণাস্থি: থাইরয়েড, ক্রিকয়েড ও অ্যারিটিনয়েড।",
    ),
    q(
        "Which structure actually enters each lung after tracheal bifurcation?",
        "নিচের কোন অংশটি ফুসফুসে প্রবেশ করে?",
        ["Vestibule", "Larynx", "Trachea as a single tube", "Bronchus"],
        ["ভেস্টিবিউল", "ল্যারিংক্স", "একটি নল হিসেবে ট্রাকিয়া", "ব্রঙ্কাস"],
        "D", "easy", "factual",
        "The trachea ends outside the lung parenchyma; primary bronchi enter the lung hilum.",
        "ট্রাকিয়া ফুসফুসের বাইরে দ্বিবিভক্ত হয়; প্রাইমারি ব্রঙ্কাস ফুসফুসের হিলামে প্রবেশ করে।",
    ),
    q(
        "Air-filled cavities beside the nasal cavity in the facial skull are called what?",
        "মাথার খুলির মুখমণ্ডলীয় অংশে নাসাগহ্বরের দুপাশের বায়ুপূর্ণ গহ্বরগুলোকে কী বলে?",
        ["Alveoli", "Sinuses (paranasal)", "Bronchioles", "Pleural sacs"],
        ["আ্যালভিওলাস", "সাইনাস (প্যারান্যাসাল)", "ব্রঙ্কিওল", "প্লিউরাল থলি"],
        "B", "easy", "factual",
        "Four pairs of paranasal sinuses (maxillary, frontal, ethmoid, sphenoid) open into the nasal cavity.",
        "চার জোড়া প্যারান্যাসাল সাইনাস (ম্যাক্সিলারি, ফ্রন্টাল, এথময়েড, স্ফেনয়েড) নাসাগহ্বরে খোলে।",
    ),
    q(
        "Infection travelling via the Eustachian tube to the middle ear causes which condition?",
        "ইউস্টেশিয়ান নালি পথে জীবাণু মধ্যকর্ণে যে প্রদাহ সৃষ্টি করে তাকে কী বলে?",
        ["Sinusitis", "Otitis media", "Ischaemia", "Emphysema"],
        ["সাইনুসাইটিস", "ওটিটিস মিডিয়া", "ইস্কেমিয়া", "এমফাইসেমা"],
        "B", "easy", "factual",
        "Otitis media is inflammation of the middle ear, often via the Eustachian (auditory) tube from the pharynx.",
        "ওটিটিস মিডিয়া মধ্যকর্ণের প্রদাহ; প্রায়শই গলবিল থেকে ইউস্টেশিয়ান নালি দিয়ে সংক্রমণ ছড়ায়।",
    ),
]


# --- t02: Breathing and gas exchange / শ্বাসক্রিয়া ও গ্যাস বিনিময় ---
T02 = [
    q(
        "Where does gaseous exchange mainly occur in the respiratory system?",
        "শ্বসনতন্ত্রের কোন অংশে প্রধানত গ্যাসীয় বিনিময় ঘটে?",
        [
            "Trachea–bronchus",
            "Alveolus–capillary network",
            "Bronchus–bronchiole",
            "Larynx–capillary network",
        ],
        [
            "ট্রাকিয়া–ব্রঙ্কাস",
            "আ্যালভিওলাস–কৈশিক জালিকা",
            "ব্রঙ্কাস–ব্রঙ্কিওল",
            "ল্যারিংক্স–কৈশিক জালিকা",
        ],
        "B", "easy", "factual",
        "O₂ and CO₂ diffuse across the thin alveolar–capillary (respiratory) membrane.",
        "পাতলা আ্যালভিওলার–কৈশিক ঝিল্লি দিয়ে O₂ ও CO₂ ব্যাপন হয়।",
    ),
    q(
        "During inspiration, what is the approximate PO₂ in alveolar air?",
        "প্রশ্বাসের সময় আ্যালভিওলাসে O₂ এর চাপ প্রায় কত?",
        ["40 mm Hg", "100 mm Hg", "104 mm Hg", "120 mm Hg"],
        ["৪০ mm Hg", "১০০ mm Hg", "১০৪ mm Hg", "১২০ mm Hg"],
        "C", "medium", "numerical",
        "HSC keys commonly give alveolar PO₂ ≈ 104 mm Hg (arterial blood ≈ 100 mm Hg).",
        "এইচএসসি কী-তে সাধারণত আ্যালভিওলার PO₂ ≈ ১০৪ mm Hg উল্লেখ থাকে।",
    ),
    q(
        "Where does the chloride shift occur?",
        "ক্লোরাইড শিফটিং কোথায় হয়?",
        [
            "Between RBCs and plasma",
            "Between WBCs and plasma",
            "Between platelets and plasma",
            "Between body cells and capillaries only",
        ],
        [
            "লোহিত রক্তকণিকা ও প্লাজমার মধ্যে",
            "শ্বেত রক্তকণিকা ও প্লাজমার মধ্যে",
            "অণুচক্রিকা ও প্লাজমার মধ্যে",
            "শুধু দেহকোষ ও কৈশিক জালিকায়",
        ],
        "A", "medium", "factual",
        "As HCO₃⁻ leaves RBCs, Cl⁻ enters from plasma (chloride/Hamburger shift) to maintain electroneutrality.",
        "RBC থেকে HCO₃⁻ বের হলে প্লাজমা থেকে Cl⁻ প্রবেশ করে তড়িৎ-নিরপেক্ষতা রক্ষায় (ক্লোরাইড শিফট)।",
    ),
    q(
        "Which nerve mainly initiates the cough reflex?",
        "কোন স্নায়ু কাশি প্রতিবর্ত ক্রিয়ার উদ্ভব ঘটায়?",
        ["Vagus", "Glossopharyngeal", "Olfactory", "Oculomotor"],
        ["ভেগাস", "গ্লসোফ্যারিঞ্জিয়াল", "অলফ্যাক্টরি", "অকুলোমোটর"],
        "A", "medium", "factual",
        "Afferent fibres of the vagus from the airway mucosa trigger the cough reflex.",
        "শ্বাসনালির মিউকোসা থেকে ভেগাসের অ্যাফারেন্ট তন্তু কাশি প্রতিবর্ত উদ্দীপিত করে।",
    ),
    q(
        "Rupture of alveoli due to smoking is called what?",
        "ধূমপানের কারণে আ্যালভিওলাস ফেটে যাওয়াকে কী বলে?",
        ["Bronchitis", "Emphysema", "Pleurisy", "Fibrosis"],
        ["ব্রঙ্কাইটিস", "এমফাইসেমা", "প্লিউরিসি", "ফাইব্রোসিস"],
        "B", "easy", "factual",
        "Emphysema involves destruction/enlargement of alveolar walls, commonly linked to smoking.",
        "এমফাইসেমায় আ্যালভিওলার প্রাচীর ক্ষতিগ্রস্ত/বড় হয়ে ফাঁকা স্থান তৈরি হয়; ধূমপান প্রধান কারণ।",
    ),
    q(
        "Which factors increase the breathing rate?",
        "শ্বসন হার বৃদ্ধির কারণ কোনগুলো?",
        [
            "Only suppression of the apneustic centre",
            "Decreased O₂ and increased CO₂ concentration",
            "Only decreased CO₂",
            "Only increased O₂",
        ],
        [
            "শুধু অ্যাপনিউস্টিক কেন্দ্রের প্রশমন",
            "O₂ এর ঘনত্ব কমে যাওয়া ও CO₂ এর ঘনত্ব বৃদ্ধি",
            "শুধু CO₂ কমে যাওয়া",
            "শুধু O₂ বৃদ্ধি",
        ],
        "B", "medium", "conceptual",
        "Chemoreceptors respond strongly to raised CO₂ (and low O₂), increasing ventilation rate.",
        "কেমোরিসেপ্টর উচ্চ CO₂ (ও নিম্ন O₂) অনুধাবন করে শ্বসনহার বাড়ায়।",
    ),
    q(
        "During inspiration, which events occur?",
        "প্রশ্বাস ক্রিয়ার সময় কোনগুলো ঘটে?",
        [
            "Diaphragm moves upward only",
            "Diaphragm descends, intercostals contract, ribs elevate",
            "Intercostals relax and chest volume falls",
            "Only the sternum moves downward",
        ],
        [
            "শুধু ডায়াফ্রাম উপরের দিকে যায়",
            "ডায়াফ্রাম নিম্নগামী হয়, ইন্টারকোস্টাল সংকুচিত হয়, পাঁজর উত্তোলিত হয়",
            "ইন্টারকোস্টাল শিথিল ও বক্ষআয়তন কমে",
            "শুধু স্টার্নাম নিচের দিকে যায়",
        ],
        "B", "easy", "conceptual",
        "Inspiration enlarges the thorax: diaphragm contracts downward and external intercostals raise the ribs.",
        "প্রশ্বাসে বক্ষআয়তন বাড়ে: ডায়াফ্রাম নিচে সংকুচিত হয় ও বাহ্য ইন্টারকোস্টাল পাঁজর তোলে।",
    ),
    q(
        "Respiratory centres in the brain are located in which parts?",
        "শ্বাসকেন্দ্র মস্তিষ্কের যে অংশে থাকে—",
        [
            "Pons and medulla oblongata",
            "Cerebellum only",
            "Cerebrum only",
            "Midbrain only",
        ],
        [
            "পনস ও মেডুলা অবলংগাটা",
            "শুধু সেরেবেলাম",
            "শুধু সেরেব্রাম",
            "শুধু মধ্যমস্তিষ্ক",
        ],
        "A", "easy", "factual",
        "Medullary respiratory groups and pontine centres (pneumotaxic/apneustic) regulate breathing rhythm.",
        "মেডুলার শ্বসন গ্রুপ ও পনসের নিউমোট্যাক্সিক/অ্যাপনিউস্টিক কেন্দ্র শ্বাসরিতি নিয়ন্ত্রণ করে।",
    ),
    q(
        "Which nerves assist breathing movements?",
        "শ্বাসক্রিয়ায় সহায়তাকারী স্নায়ু কোনগুলো?",
        [
            "Only olfactory",
            "Vagus, phrenic and intercostal",
            "Only oculomotor",
            "Only facial",
        ],
        [
            "শুধু অলফ্যাক্টরি",
            "ভেগাস, ফ্রেনিক ও ইন্টারকোস্টাল",
            "শুধু অকুলোমোটর",
            "শুধু ফ্যাসিয়াল",
        ],
        "B", "medium", "factual",
        "Phrenic nerves drive the diaphragm; intercostal nerves supply intercostal muscles; vagus carries airway afferents.",
        "ফ্রেনিক ডায়াফ্রাম, ইন্টারকোস্টাল স্নায়ু পাঁজরের পেশি, ভেগাস শ্বাসনালির সংবেদী তন্তু বহন করে।",
    ),
    q(
        "External respiration is best described as which kind of process?",
        "বহিঃশ্বসন কোন ধরনের প্রক্রিয়া?",
        [
            "A biochemical process inside cells producing ATP",
            "A physical process of pulmonary ventilation and lung gas exchange",
            "Only glycolysis in the cytoplasm",
            "Only the Krebs cycle in mitochondria",
        ],
        [
            "কোষে ATP উৎপাদনকারী জৈবরাসায়নিক প্রক্রিয়া",
            "শ্বাসগ্রহণ-ত্যাগ ও ফুসফুসে গ্যাস বিনিময়ের ভৌত প্রক্রিয়া",
            "শুধু সাইটোপ্লাজমে গ্লাইকোলাইসিস",
            "শুধু মাইটোকন্ড্রিয়ায় ক্রেবস চক্র",
        ],
        "B", "easy", "conceptual",
        "External respiration covers breathing and alveolar gas exchange; cellular oxidation is internal respiration.",
        "বহিঃশ্বসন শ্বাসক্রিয়া ও আ্যালভিওলার গ্যাস বিনিময়; কোষীয় জারণ অন্তঃশ্বসন।",
    ),
    q(
        "Haemoglobin has been nicknamed which of the following?",
        "হিমোগ্লোবিনকে কোন নামে ডাকা হয়?",
        [
            "Robin Hood particle",
            "Adam’s apple",
            "Bundle of His",
            "Pacemaker particle",
        ],
        [
            "রবিন হুড পার্টিকেল",
            "অ্যাডামস অ্যাপল",
            "বান্ডেল অব হিজ",
            "পেসমেকার পার্টিকেল",
        ],
        "A", "easy", "factual",
        "Because Hb ‘takes’ O₂ from alveolar air and delivers it to tissues, it is poetically called a Robin Hood particle.",
        "Hb আ্যালভিওলাই থেকে O₂ নিয়ে কলায় পৌঁছায় বলে একে রবিন হুড পার্টিকেল বলা হয়।",
    ),
    q(
        "Which disease is an infection of the lower airways (bronchi)?",
        "কোনটি নিম্ন শ্বাসনালির (ব্রঙ্কাস) সংক্রমণ?",
        ["Sinusitis", "Otitis media", "Bronchitis", "Laryngitis"],
        ["সাইনুসাইটিস", "ওটাইটিস মিডিয়া", "ব্রঙ্কাইটিস", "ল্যারিঞ্জাইটিস"],
        "C", "easy", "factual",
        "Bronchitis is inflammation/infection of the bronchi; laryngitis affects the larynx, sinusitis the sinuses.",
        "ব্রঙ্কাইটিস ব্রঙ্কাসের প্রদাহ/সংক্রমণ; ল্যারিঞ্জাইটিস স্বরযন্ত্রে, সাইনুসাইটিস সাইনাসে।",
    ),
    q(
        "Surfactant secreted by type II cells helps by doing which of the following?",
        "টাইপ-২ কোষ থেকে ক্ষরিত সারফ্যাকট্যান্ট কীভাবে সাহায্য করে?",
        [
            "Only by raising surface tension",
            "Lowering surface tension, easing gas exchange and preventing collapse",
            "Blocking all O₂ diffusion",
            "Converting Hb to myoglobin",
        ],
        [
            "শুধু পৃষ্ঠটান বাড়িয়ে",
            "পৃষ্ঠটান কমিয়ে গ্যাস বিনিময় সহজ ও চুপসে যাওয়া রোধ করে",
            "সব O₂ ব্যাপন বন্ধ করে",
            "Hb কে মায়োগ্লোবিনে রূপান্তর করে",
        ],
        "B", "easy", "conceptual",
        "Phospholipid surfactant acts detergent-like: lowers surface tension, stabilises alveoli, aids exchange.",
        "ফসফোলিপিড সারফ্যাকট্যান্ট ডিটারজেন্টের মতো পৃষ্ঠটান কমিয়ে আ্যালভিওলাস স্থিতিশীল ও বিনিময় সহজ করে।",
    ),
    q(
        "Fluid between the two pleural layers is called what?",
        "প্লিউরার দুই স্তরের মধ্যবর্তী তরলের নাম কী?",
        ["Plasma fluid", "Pericardial fluid", "Cerebral fluid", "Pleural fluid"],
        ["প্লাজমা ফ্লুইড", "পেরিকার্ডিয়াল ফ্লুইড", "সেরিব্রাল ফ্লুইড", "প্লিউরাল ফ্লুইড"],
        "D", "easy", "factual",
        "A thin film of pleural fluid lubricates movement of visceral against parietal pleura.",
        "পাতলা প্লিউরাল তরল ভিসেরাল ও প্যারাইটাল প্লিউরার ঘর্ষণ কমায়।",
    ),
    q(
        "Thickening of alveolar walls that impairs breathing after smoking is associated with which condition?",
        "ধূমপানের ফলে ফুসফুসের বায়ুথলির প্রাচীর পুরু হয়ে শ্বাসপ্রশ্বাসে ব্যাঘাত কোন রোগে?",
        ["Bronchitis", "Emphysema", "Pleurisy", "Fibrosis"],
        ["ব্রঙ্কাইটিস", "এমফাইসেমা", "প্লিউরিসি", "ফাইব্রোসিস"],
        "D", "medium", "factual",
        "Pulmonary fibrosis features scarring/thickening that reduces compliance and gas exchange.",
        "পালমোনারি ফাইব্রোসিসে দাগ/প্রাচীর পুরু হয়ে সম্প্রসারণ ও গ্যাস বিনিময় কমে।",
    ),
    q(
        "Most oxygen in blood is transported in which form?",
        "রক্তে অধিকাংশ অক্সিজেন কোন আকারে পরিবাহিত হয়?",
        [
            "Dissolved only in plasma",
            "Bound to haemoglobin as oxyhaemoglobin",
            "As bicarbonate ion only",
            "As carbamino compound only",
        ],
        [
            "শুধু প্লাজমায় দ্রবীভূত",
            "হিমোগ্লোবিনের সাথে অক্সিহিমোগ্লোবিন রূপে",
            "শুধু বাইকার্বোনেট আয়ন রূপে",
            "শুধু কার্বামিনো যৌগ রূপে",
        ],
        "B", "easy", "factual",
        "About 97% of O₂ is carried as HbO₂; a small fraction dissolves in plasma.",
        "প্রায় ৯৭% O₂ অক্সিহিমোগ্লোবিন রূপে; সামান্য অংশ প্লাজমায় দ্রবীভূত থাকে।",
    ),
    q(
        "What is meant by artificial respiration?",
        "কৃত্রিম শ্বাস-প্রশ্বাস বলতে কী বোঝায়?",
        [
            "Cellular ATP synthesis in mitochondria",
            "Mechanically or manually maintaining ventilation when natural breathing fails",
            "Only measuring tidal volume",
            "Only surfactant replacement therapy",
        ],
        [
            "মাইটোকন্ড্রিয়ায় কোষীয় ATP সংশ্লেষণ",
            "স্বাভাবিক শ্বাস বন্ধ/বন্ধপ্রায় হলে যান্ত্রিক বা কায়িক উপায়ে শ্বাস চালু রাখা",
            "শুধু টাইডাল ভলিউম পরিমাপ",
            "শুধু সারফ্যাকট্যান্ট প্রতিস্থাপন চিকিৎসা",
        ],
        "B", "easy", "conceptual",
        "Artificial respiration restores airflow (mouth-to-mouth, bag-mask, ventilator) in emergencies like drowning or CO poisoning.",
        "ডোবা, CO বিষক্রিয়া ইত্যাদিতে মুখ-মুখ/ব্যাগ-মাস্ক/ভেন্টিলেটর দিয়ে বায়ুপ্রবাহ ফেরানোই কৃত্রিম শ্বাস।",
    ),
    q(
        "Most CO₂ in blood is transported mainly as what?",
        "রক্তে অধিকাংশ CO₂ প্রধানত কোন আকারে পরিবাহিত হয়?",
        [
            "Dissolved gas only",
            "Bicarbonate ions",
            "Carbamino haemoglobin only",
            "Carbon monoxide",
        ],
        [
            "শুধু দ্রবীভূত গ্যাস",
            "বাইকার্বোনেট আয়ন",
            "শুধু কার্বামিনো হিমোগ্লোবিন",
            "কার্বন মনোক্সাইড",
        ],
        "B", "medium", "factual",
        "Roughly 70% of CO₂ travels as HCO₃⁻ after carbonic anhydrase action in RBCs; rest as dissolved/carbamino forms.",
        "প্রায় ৭০% CO₂ RBC-তে কার্বনিক অ্যানহাইড্রেজের মাধ্যমে HCO₃⁻ রূপে পরিবাহিত হয়।",
    ),
    q(
        "Gas exchange across the alveolar membrane occurs by which process?",
        "আ্যালভিওলার ঝিল্লি দিয়ে গ্যাস বিনিময় কোন প্রক্রিয়ায় হয়?",
        ["Active transport only", "Osmosis", "Diffusion down partial-pressure gradients", "Phagocytosis"],
        ["শুধু সক্রিয় পরিবহন", "অসমোসিস", "আংশিক চাপের ঢালে ব্যাপন", "ফ্যাগোসাইটোসিস"],
        "C", "easy", "conceptual",
        "O₂ and CO₂ move passively from higher to lower partial pressure across the respiratory membrane.",
        "O₂ ও CO₂ উচ্চ থেকে নিম্ন আংশিক চাপের দিকে প্যাসিভ ব্যাপনে আদান-প্রদান হয়।",
    ),
    q(
        "Which statement about respiratory pigments is correct?",
        "শ্বাসরঞ্জক সম্পর্কে কোনটি সঠিক?",
        [
            "Hb has no iron",
            "Hb is made of iron and protein, and its reaction with O₂ is reversible",
            "Hb binds O₂ irreversibly only",
            "Hb is found only in plasma, never in RBCs",
        ],
        [
            "Hb-এ আয়রন নেই",
            "Hb আয়রন ও প্রোটিনের সমন্বয়ে গঠিত এবং O₂ এর সাথে বিক্রিয়া উভমুখী",
            "Hb শুধু অপরিবর্তনীয়ভাবে O₂ বাঁধে",
            "Hb শুধু প্লাজমায় থাকে, RBC-তে নয়",
        ],
        "B", "medium", "conceptual",
        "Haemoglobin (haem Fe²⁺ + globin) binds O₂ reversibly for loading in lungs and unloading in tissues.",
        "হিমোগ্লোবিন (হিম Fe²⁺ + গ্লোবিন) O₂ কে উভমুখীভাবে বাঁধে—ফুসফুসে গ্রহণ, কলায় মুক্তি।",
    ),
]


# --- t03: Cellular respiration / কোষীয় শ্বসন ---
T03 = [
    q(
        "Internal (cellular) respiration is best defined as what?",
        "অন্তঃশ্বসন বলতে কী বোঝায়?",
        [
            "Only movement of the diaphragm",
            "Biochemical oxidation of food in cells with enzyme action producing energy, plus related gas exchange with blood",
            "Only air entering the nose",
            "Only coughing",
        ],
        [
            "শুধু ডায়াফ্রামের চলাচল",
            "দেহকোষে খাদ্যের এনজাইমনির্ভর জৈবরাসায়নিক জারণে শক্তি উৎপাদন ও রক্তের সাথে সংশ্লিষ্ট গ্যাস বিনিময়",
            "শুধু নাকে বায়ু প্রবেশ",
            "শুধু কাশি",
        ],
        "B", "easy", "conceptual",
        "Internal respiration is the cellular/biochemical use of O₂ to oxidise nutrients and release energy (with CO₂ as a by-product).",
        "অন্তঃশ্বসন কোষে O₂ দিয়ে খাদ্য জারণে শক্তি উৎপাদন; উপজাত CO₂ রক্তে ফেরে।",
    ),
    q(
        "Where does the Krebs (TCA) cycle occur in eukaryotic cells?",
        "ইউক্যারিওটিক কোষে ক্রেবস চক্র কোথায় সম্পন্ন হয়?",
        ["Cytoplasm", "Mitochondrial matrix", "Nucleus", "Golgi apparatus"],
        ["সাইটোপ্লাজম", "মাইটোকন্ড্রিয়াল ম্যাট্রিক্স", "নিউক্লিয়াস", "গলজি বডি"],
        "B", "easy", "factual",
        "After pyruvate enters mitochondria, the Krebs cycle runs in the mitochondrial matrix.",
        "পাইরুভেট মাইটোকন্ড্রিয়ায় প্রবেশের পর ক্রেবস চক্র ম্যাট্রিক্সে চলে।",
    ),
    q(
        "Glycolysis takes place in which cellular compartment?",
        "গ্লাইকোলাইসিস কোষের কোন অংশে ঘটে?",
        ["Mitochondrial matrix", "Cytoplasm", "Thylakoid", "Lysosome"],
        ["মাইটোকন্ড্রিয়াল ম্যাট্রিক্স", "সাইটোপ্লাজম", "থাইলাকয়েড", "লাইসোজোম"],
        "B", "easy", "factual",
        "Glycolysis is the anaerobic cytoplasmic pathway that converts glucose to pyruvate.",
        "গ্লাইকোলাইসিস সাইটোপ্লাজমে গ্লুকোজকে পাইরুভেটে রূপান্তর করে (অক্সিজেন ছাড়াই চলে)।",
    ),
    q(
        "Which equation correctly summarises aerobic respiration of glucose?",
        "গ্লুকোজের অ্যারোবিক শ্বসনের সঠিক সারাংশ সমীকরণ কোনটি?",
        [
            "C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂",
            "C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + Energy",
            "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂",
            "C₆H₁₂O₆ + 6CO₂ → 6O₂ + Energy",
        ],
        [
            "C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂",
            "C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + Energy",
            "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂",
            "C₆H₁₂O₆ + 6CO₂ → 6O₂ + Energy",
        ],
        "B", "easy", "factual",
        "Complete aerobic oxidation uses O₂ and yields CO₂, H₂O and usable energy (ATP/heat).",
        "সম্পূর্ণ অ্যারোবিক জারণে O₂ ব্যবহৃত হয়ে CO₂, H₂O ও শক্তি (ATP) উৎপন্ন হয়।",
    ),
    q(
        "Which statement about cellular respiration is incorrect?",
        "কোষীয় শ্বসন সম্পর্কে কোনটি ভুল?",
        [
            "Enzymes play a major role",
            "A major sub-stage is the Krebs cycle",
            "It occurs inside cells",
            "No energy is produced",
        ],
        [
            "এনজাইমের ভূমিকা আছে",
            "প্রধান উপপর্যায় ক্রেবস চক্র",
            "কোষের অভ্যন্তরে সংঘটিত হয়",
            "শক্তি উৎপন্ন হয় না",
        ],
        "D", "easy", "conceptual",
        "Cellular respiration’s purpose is energy release; claiming no energy is produced is false.",
        "কোষীয় শ্বসনের উদ্দেশ্যই শক্তি উৎপাদন; ‘শক্তি উৎপন্ন হয় না’ দাবিটি ভুল।",
    ),
    q(
        "Aerobic respiration differs from anaerobic respiration mainly because it requires what?",
        "অ্যারোবিক শ্বসন অ্যানঅ্যারোবিক শ্বসন থেকে প্রধানত কীতে আলাদা?",
        [
            "No enzymes",
            "Molecular oxygen as the final electron acceptor",
            "Occurrence only in the nucleus",
            "Production of only alcohol in all animal cells",
        ],
        [
            "কোনো এনজাইম নেই",
            "চূড়ান্ত ইলেকট্রন গ্রহীতা হিসেবে আণবিক অক্সিজেন",
            "শুধু নিউক্লিয়াসে ঘটে",
            "সব প্রাণীকোষে শুধু অ্যালকোহল উৎপাদন",
        ],
        "B", "easy", "conceptual",
        "In aerobic respiration O₂ accepts electrons at the end of the ETC; anaerobic pathways do not use O₂.",
        "অ্যারোবিক শ্বসনে ETC-এর শেষে O₂ ইলেকট্রন গ্রহণ করে; অ্যানঅ্যারোবিকে O₂ লাগে না।",
    ),
    q(
        "Most ATP from aerobic respiration of glucose is generated where?",
        "গ্লুকোজের অ্যারোবিক শ্বসনে অধিকাংশ ATP কোথায় উৎপন্ন হয়?",
        [
            "Only in glycolysis",
            "Oxidative phosphorylation via the electron transport chain",
            "Only in the nucleus",
            "Only during fermentation",
        ],
        [
            "শুধু গ্লাইকোলাইসিসে",
            "ইলেকট্রন পরিবহন শৃঙ্খলের মাধ্যমে অক্সিডেটিভ ফসফোরাইলেশনে",
            "শুধু নিউক্লিয়াসে",
            "শুধু ফার্মেন্টেশনে",
        ],
        "B", "medium", "conceptual",
        "NADH/FADH₂ from earlier stages drive the ETC; chemiosmotic ATP synthase yields most ATP.",
        "পূর্ববর্তী ধাপের NADH/FADH₂ ETC চালায়; কেমিঅসমোটিক ATP সিন্থেস থেকেই বেশিরভাগ ATP।",
    ),
    q(
        "In the link reaction, pyruvate is converted mainly into what?",
        "লিঙ্ক বিক্রিয়ায় পাইরুভেট প্রধানত কীতে রূপান্তরিত হয়?",
        ["Lactate only", "Acetyl-CoA", "Glucose-6-phosphate", "Urea"],
        ["শুধু ল্যাকটেট", "অ্যাসিটাইল-CoA", "গ্লুকোজ-৬-ফসফেট", "ইউরিয়া"],
        "B", "medium", "factual",
        "Oxidative decarboxylation of pyruvate forms acetyl-CoA that enters the Krebs cycle.",
        "পাইরুভেটের অক্সিডেটিভ ডিকার্বক্সিলেশনে অ্যাসিটাইল-CoA তৈরি হয়ে ক্রেবস চক্রে প্রবেশ করে।",
    ),
    q(
        "In animal muscle under anaerobic conditions, glycolysis ends mainly with what product?",
        "অ্যানঅ্যারোবিক অবস্থায় প্রাণীর পেশিতে গ্লাইকোলাইসিসের প্রধান শেষ পণ্য কী?",
        ["Ethanol", "Lactic acid (lactate)", "Acetyl-CoA", "Uric acid"],
        ["ইথানল", "ল্যাকটিক অ্যাসিড (ল্যাকটেট)", "অ্যাসিটাইল-CoA", "ইউরিক অ্যাসিড"],
        "B", "easy", "factual",
        "Homolactic fermentation regenerates NAD⁺ by reducing pyruvate to lactate in muscle.",
        "পেশিতে পাইরুভেট ল্যাকটেটে পরিণত হয়ে NAD⁺ পুনরুদ্ধার করে (ল্যাকটিক অ্যাসিড ফার্মেন্টেশন)।",
    ),
    q(
        "Which reduced coenzymes formed during respiration donate electrons to the ETC?",
        "শ্বসনে উৎপন্ন কোন বিজারিত কোএনজাইমগুলো ETC-তে ইলেকট্রন দান করে?",
        ["ATP and AMP only", "NADH and FADH₂", "NADP⁺ only", "CoA and biotin only"],
        ["শুধু ATP ও AMP", "NADH ও FADH₂", "শুধু NADP⁺", "শুধু CoA ও বায়োটিন"],
        "B", "medium", "factual",
        "NADH and FADH₂ carry high-energy electrons to complexes of the mitochondrial ETC.",
        "NADH ও FADH₂ উচ্চশক্তি ইলেকট্রন মাইটোকন্ড্রিয়াল ETC কমপ্লেক্সে পৌঁছায়।",
    ),
    q(
        "The main end products of complete aerobic respiration of glucose are what?",
        "গ্লুকোজের সম্পূর্ণ অ্যারোবিক শ্বসনের প্রধান শেষ পণ্য কী কী?",
        ["Ammonia and urea", "CO₂ and H₂O (plus ATP/energy)", "Only lactic acid", "Only ethanol"],
        ["অ্যামোনিয়া ও ইউরিয়া", "CO₂ ও H₂O (এবং ATP/শক্তি)", "শুধু ল্যাকটিক অ্যাসিড", "শুধু ইথানল"],
        "B", "easy", "factual",
        "Complete oxidation yields carbon dioxide and water together with captured chemical energy.",
        "সম্পূর্ণ জারণে কার্বন ডাইঅক্সাইড ও পানিসহ রাসায়নিক শক্তি (ATP) পাওয়া যায়।",
    ),
    q(
        "Why are enzymes essential in cellular respiration?",
        "কোষীয় শ্বসনে এনজাইম কেন অপরিহার্য?",
        [
            "They replace oxygen entirely",
            "They catalyse stepwise oxidation so energy is released in controlled amounts",
            "They prevent any ATP formation",
            "They only digest food in the stomach",
        ],
        [
            "এগুলো সম্পূর্ণভাবে অক্সিজেন প্রতিস্থাপন করে",
            "ধাপে ধাপে জারণ অনুঘটন করে নিয়ন্ত্রিত পরিমাণে শক্তি মুক্ত করে",
            "ATP গঠনই বন্ধ করে",
            "শুধু পাকস্থলীতে খাদ্য হজম করে",
        ],
        "B", "medium", "conceptual",
        "Respiratory enzymes lower activation energy and channel released energy into ATP rather than waste heat alone.",
        "শ্বসন এনজাইম সক্রিয়ন শক্তি কমিয়ে ধাপে ধাপে শক্তি ATP-তে আবদ্ধ করতে সাহায্য করে।",
    ),
    q(
        "Net gain of ATP molecules from glycolysis of one glucose (classical HSC count) is about what?",
        "এক অণু গ্লুকোজের গ্লাইকোলাইসিসে নীট ATP লাভ (ধ্রুপদী এইচএসসি গণনা) প্রায় কত?",
        ["0", "2", "18", "38"],
        ["০", "২", "১৮", "৩৮"],
        "B", "easy", "numerical",
        "Glycolysis uses 2 ATP and produces 4 ATP, for a net of 2 ATP per glucose.",
        "গ্লাইকোলাইসিসে ২ ATP খরচ ও ৪ ATP উৎপাদনে নীট ২ ATP পাওয়া যায়।",
    ),
    q(
        "Complete aerobic oxidation of one glucose is often taught in HSC as yielding about how many ATP?",
        "এক অণু গ্লুকোজের সম্পূর্ণ অ্যারোবিক জারণে এইচএসসিতে সাধারণত কত ATP উল্লেখ থাকে?",
        ["2", "8", "18", "38"],
        ["২", "৮", "১৮", "৩৮"],
        "D", "medium", "numerical",
        "Classical board texts often total ~38 ATP (some modern counts ~30–32); HSC keys commonly use 38.",
        "ধ্রুপদী পাঠ্য/কী-তে প্রায় ৩৮ ATP; আধুনিক গণনায় কখনো ~৩০–৩২ বলা হয়।",
    ),
    q(
        "The electron transport chain of aerobic respiration is located where?",
        "অ্যারোবিক শ্বসনের ইলেকট্রন পরিবহন শৃঙ্খল কোথায় অবস্থিত?",
        [
            "Outer mitochondrial membrane only",
            "Inner mitochondrial membrane",
            "Nuclear envelope",
            "Rough ER lumen",
        ],
        [
            "শুধু বহিঃ মাইটোকন্ড্রিয়াল ঝিল্লি",
            "অন্তঃ মাইটোকন্ড্রিয়াল ঝিল্লি",
            "নিউক্লিয়ার এনভেলপ",
            "রাফ ER লুমেন",
        ],
        "B", "medium", "factual",
        "ETC complexes and ATP synthase are embedded in the inner mitochondrial membrane (cristae).",
        "ETC কমপ্লেক্স ও ATP সিন্থেস অন্তঃ মাইটোকন্ড্রিয়াল ঝিল্লি/ক্রিস্টায় থাকে।",
    ),
    q(
        "What is the final electron acceptor in the mitochondrial ETC?",
        "মাইটোকন্ড্রিয়াল ETC-এর চূড়ান্ত ইলেকট্রন গ্রহীতা কী?",
        ["NAD⁺", "Oxygen", "Pyruvate", "Glucose"],
        ["NAD⁺", "অক্সিজেন", "পাইরুভেট", "গ্লুকোজ"],
        "B", "easy", "factual",
        "Molecular oxygen accepts electrons (with protons) to form water at the end of the chain.",
        "শৃঙ্খলের শেষে আণবিক অক্সিজেন ইলেকট্রন ও প্রোটন নিয়ে পানি গঠন করে।",
    ),
    q(
        "Which comparison between external and internal respiration is correct?",
        "বহিঃশ্বসন ও অন্তঃশ্বসনের কোন তুলনা সঠিক?",
        [
            "Both occur only inside mitochondria",
            "External is mainly physical (ventilation/exchange); internal is biochemical energy release in cells",
            "Internal never involves enzymes",
            "External always produces 38 ATP",
        ],
        [
            "দুটোই শুধু মাইটোকন্ড্রিয়ায় ঘটে",
            "বহিঃশ্বসন প্রধানত ভৌত (বায়ুচলাচল/বিনিময়); অন্তঃশ্বসন কোষে জৈবরাসায়নিক শক্তি মুক্তি",
            "অন্তঃশ্বসনে কখনো এনজাইম লাগে না",
            "বহিঃশ্বসনে সবসময় ৩৮ ATP হয়",
        ],
        "B", "medium", "conceptual",
        "Breathing/alveolar exchange is external; enzymatic oxidation of food in cells is internal respiration.",
        "শ্বাস ও আ্যালভিওলার বিনিময় বহিঃশ্বসন; কোষে এনজাইমনির্ভর খাদ্যজারণ অন্তঃশ্বসন।",
    ),
    q(
        "Substrate-level phosphorylation during respiration means what?",
        "শ্বসনে সাবস্ট্রেট-লেভেল ফসফোরাইলেশন বলতে কী বোঝায়?",
        [
            "ATP made only by sunlight",
            "Direct enzymatic transfer of a phosphate to ADP from a metabolic intermediate",
            "ATP made only when O₂ is absent forever",
            "Breaking of peptide bonds only",
        ],
        [
            "শুধু সূর্যালোকে ATP তৈরি",
            "বিপাকীয় মধ্যবর্তী থেকে সরাসরি এনজাইম দিয়ে ADP-তে ফসফেট স্থানান্তর",
            "চিরকাল O₂ না থাকলেই কেবল ATP",
            "শুধু পেপটাইড বন্ধন ভাঙা",
        ],
        "B", "hard", "conceptual",
        "In glycolysis and the Krebs cycle, some ATP forms directly from high-energy substrate phosphates.",
        "গ্লাইকোলাইসিস ও ক্রেবস চক্রে উচ্চশক্তি সাবস্ট্রেট থেকে সরাসরি কিছু ATP তৈরি হয়।",
    ),
    q(
        "Respiratory quotient (RQ) is defined as the ratio of what?",
        "রেসপিরেটরি কোয়েশেন্ট (RQ) কীসের অনুপাত?",
        [
            "O₂ consumed / CO₂ produced",
            "CO₂ produced / O₂ consumed",
            "ATP / ADP only",
            "Inspiration volume / expiration volume only",
        ],
        [
            "গৃহীত O₂ / উৎপন্ন CO₂",
            "উৎপন্ন CO₂ / গৃহীত O₂",
            "শুধু ATP / ADP",
            "শুধু প্রশ্বাস আয়তন / নিঃশ্বাস আয়তন",
        ],
        "B", "hard", "numerical",
        "RQ = volume of CO₂ evolved ÷ volume of O₂ absorbed; for carbohydrate RQ ≈ 1.",
        "RQ = নির্গত CO₂ আয়তন ÷ গৃহীত O₂ আয়তন; কার্বোহাইড্রেটে RQ ≈ ১।",
    ),
    q(
        "Fermentation differs from aerobic respiration mainly in that it does what?",
        "ফার্মেন্টেশন অ্যারোবিক শ্বসন থেকে প্রধানত কীভাবে আলাদা?",
        [
            "Uses the full Krebs cycle and ETC with O₂",
            "Regenerates NAD⁺ without using O₂ as final acceptor and yields far less ATP",
            "Occurs only in the mitochondrial cristae",
            "Always produces 38 ATP per glucose",
        ],
        [
            "O₂সহ পূর্ণ ক্রেবস চক্র ও ETC ব্যবহার করে",
            "O₂ ছাড়াই NAD⁺ পুনরুদ্ধার করে এবং অনেক কম ATP দেয়",
            "শুধু মাইটোকন্ড্রিয়াল ক্রিস্টায় ঘটে",
            "প্রতি গ্লুকোজে সবসময় ৩৮ ATP দেয়",
        ],
        "B", "medium", "conceptual",
        "Fermentation is anaerobic cytoplasmic NAD⁺ regeneration (lactate/ethanol) with low net ATP (~2).",
        "ফার্মেন্টেশন অ্যানঅ্যারোবিক সাইটোপ্লাজমিক NAD⁺ পুনরুদ্ধার; নীট ATP খুব কম (~২)।",
    ),
]


TOPICS_MAP = {
    "bio2_27_ch05_t01": T01,
    "bio2_27_ch05_t02": T02,
    "bio2_27_ch05_t03": T03,
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
        "chapter": "bio2_27_ch05",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p195_pdf201.png",
            "p196_pdf202.png",
            "p197_pdf203.png",
            "p198_pdf204.png",
            "p199_pdf205.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio2_27_ch05_t01": {
                "title": "Respiratory organs / শ্বাসযন্ত্র",
                "themes": [
                    "vocal cords; ethmoid/maxillary sinuses; left lung 2 lobes",
                    "bronchioles; phrenic artery; Adam’s apple = thyroid cartilage",
                    "primary bronchi; surfactant site/onset 23 wk; alveolar wall cells",
                    "pleura visceral/parietal; trabeculae; olfactory cells; epiglottis",
                    "laryngeal cartilages; bronchus enters lung; paranasal sinuses; otitis media",
                ],
            },
            "bio2_27_ch05_t02": {
                "title": "Breathing and gas exchange / শ্বাসক্রিয়া ও গ্যাস বিনিময়",
                "themes": [
                    "alveolus–capillary exchange; alveolar PO₂ ≈ 104 mm Hg",
                    "chloride shift; vagus cough reflex; emphysema vs fibrosis",
                    "↑CO₂/↓O₂ raise rate; inspiration mechanics; pons + medulla",
                    "phrenic/intercostal/vagus; external vs internal; Robin Hood Hb",
                    "bronchitis; surfactant roles; pleural fluid; O₂/CO₂ transport; diffusion; artificial respiration",
                ],
            },
            "bio2_27_ch05_t03": {
                "title": "Cellular respiration / কোষীয় শ্বসন",
                "themes": [
                    "internal respiration definition; Krebs matrix; glycolysis cytoplasm",
                    "aerobic equation; energy claim; O₂ as final acceptor",
                    "ETC ATP; acetyl-CoA link; lactate fermentation; NADH/FADH₂",
                    "end products; enzymes; net 2 / classical 38 ATP; inner membrane ETC",
                    "RQ; substrate-level phosphorylation; external vs internal; fermentation",
                ],
            },
        },
        "low_confidence": [
            "OCR of printed MCQ pages p195–199 is noisy (garbled options/answer marks); stems reconstructed from readable fragments, CQ text on earlier pages, and standard HSC Zoology Ch5 facts.",
            "Figure-/stimulus-linked bank items rewritten as standalone stems (no dependency on missing diagrams).",
            "Vocal cord count kept as 2 (one pair) per frequent board framing; some texts also discuss true/false pairs.",
            "Complete glucose oxidation ATP kept as classical HSC 38; modern estimates often ~30–32.",
            "Cellular-respiration topic supplemented more heavily because OCR MCQ density for biochemistry was lower than for organs/breathing.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio2_27_ch05_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio2_27_ch05_t01": 20,
                "bio2_27_ch05_t02": 20,
                "bio2_27_ch05_t03": 20,
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
        / "ch05_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
