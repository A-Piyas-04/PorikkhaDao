#!/usr/bin/env python3
"""Seed Biology 2nd Paper Ch7 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio2_27_ch07_t01..t03 (Skeleton/joints; Muscles; Movement).
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
    "biology p2 ch07; curated bilingual"
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


# --- t01: Skeleton and joints / কঙ্কাল ও অস্থিসন্ধি ---
T01 = [
    q(
        "On which regional vertebra is the odontoid (dens) process present?",
        "ওডোন্টয়েড (ডেন্স) প্রসেস কোন অঞ্চলের কশেরুকায় বিদ্যমান?",
        ["Cervical", "Thoracic", "Lumbar", "Caudal"],
        ["গ্রীবাদেশীয়", "বক্ষদেশীয়", "কটিদেশীয়", "পুচ্ছদেশীয়"],
        "A", "easy", "factual",
        "The odontoid process is on the axis (2nd cervical vertebra).",
        "ওডোন্টয়েড প্রসেস অক্ষ কশেরুকায় (২য় সার্ভাইকাল) থাকে।",
    ),
    q(
        "In an adult human, which three bones form each hip (innominate) bone?",
        "প্রাপ্তবয়স্ক মানুষে প্রতিটি হিপবোন কোন তিনটি অস্থি নিয়ে গঠিত?",
        [
            "Pisiform, pubis and scapula",
            "Ischium, lunate and pubis",
            "Lunate, hamate and ischium",
            "Pubis, ischium and ilium",
        ],
        [
            "পিসিফর্ম, পিউবিস ও স্ক্যাপুলা",
            "ইস্চিয়াম, লুনেট ও পিউবিস",
            "লুনেট, হ্যামেট ও ইস্চিয়াম",
            "পিউবিস, ইস্চিয়াম ও ইলিয়াম",
        ],
        "D", "easy", "factual",
        "Each adult hip bone is fused ilium + ischium + pubis.",
        "প্রাপ্তবয়স্ক প্রতিটি হিপবোন ইলিয়াম, ইস্চিয়াম ও পিউবিসের সংযুক্ত রূপ।",
    ),
    q(
        "How many lumbar vertebrae does a human normally have?",
        "মানুষের সাধারণত লাম্বার কশেরুকা সংখ্যা কত?",
        ["4", "5", "7", "12"],
        ["৪", "৫", "৭", "১২"],
        "B", "easy", "factual",
        "There are five lumbar vertebrae in the human vertebral column.",
        "মানব মেরুদণ্ডে পাঁচটি কটিদেশীয় (লাম্বার) কশেরুকা থাকে।",
    ),
    q(
        "In which skull bone is the foramen magnum located?",
        "ফোরামেন ম্যাগনাম কোন অস্থিতে বিদ্যমান?",
        ["Frontal bone", "Parietal bone", "Occipital bone", "Temporal bone"],
        ["ফ্রন্টাল অস্থি", "প্যারাইটাল অস্থি", "অক্সিপিটাল অস্থি", "টেম্পোরাল অস্থি"],
        "C", "easy", "factual",
        "The large occipital opening (foramen magnum) transmits the spinal cord.",
        "অক্সিপিটাল অস্থির ফোরামেন ম্যাগনাম দিয়ে স্পাইনাল কর্ড যায়।",
    ),
    q(
        "Which statements about hyaline cartilage are correct? (i) largely fibre-free (ii) matrix translucent (iii) example: trachea",
        "হায়ালিন তরুণাস্থি সম্পর্কে কোনগুলো সঠিক? (i) প্রায় তন্তুবিহীন (ii) ম্যাট্রিক্স স্বচ্ছ/অর্ধস্বচ্ছ (iii) উদাহরণ: ট্রাকিয়া",
        ["(i) and (ii) only", "(i) and (iii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["শুধু (i) ও (ii)", "শুধু (i) ও (iii)", "শুধু (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "medium", "conceptual",
        "Hyaline cartilage is typically nearly fibre-free, glassy matrix, and lines trachea rings.",
        "হায়ালিন তরুণাস্থি প্রায় তন্তুবিহীন, স্বচ্ছ ম্যাট্রিক্সযুক্ত এবং শ্বাসনালিতে থাকে।",
    ),
    q(
        "Where does the head of the femur articulate?",
        "ফিমারের মস্তক কোথায় আটকানো থাকে?",
        ["Glenoid cavity", "Obturator foramen", "Vertebral foramen", "Acetabulum"],
        ["গ্লিনয়েড গহ্বর", "অবটুরেটর ফোরামেন", "ভার্টিব্রাল ফোরামেন", "অ্যাসিটাবুলাম"],
        "D", "easy", "factual",
        "The femoral head fits the acetabulum of the hip bone (ball-and-socket).",
        "ফিমারের মস্তক হিপবোনের অ্যাসিটাবুলামে বসে (বল-সকেট সন্ধি)।",
    ),
    q(
        "Which hormone is secreted by bone cells?",
        "অস্থির কোষ থেকে কোন হরমোন ক্ষরিত হয়?",
        ["Noradrenaline", "Osteocalcin", "Mineralocorticoid", "Oxytocin"],
        ["নরঅ্যাড্রেনালিন", "অস্টিওক্যালসিন", "মিনারেলোকর্টিকয়েড", "অক্সিটোসিন"],
        "B", "medium", "factual",
        "Osteoblasts secrete osteocalcin, a bone-derived hormone.",
        "অস্টিওব্লাস্ট অস্টিওক্যালসিন নামক অস্থি-উৎস হরমোন ক্ষরণ করে।",
    ),
    q(
        "Which of the following is a fibrous joint?",
        "নিচের কোনটি তন্তুময় অস্থিসন্ধি?",
        ["Shoulder joint", "Pubic symphysis", "Gomphosis", "Ankle joint"],
        ["কাঁধের সন্ধি", "পিউবিক সিমফাইসিস", "গম্ফোসিস", "গোড়ালি সন্ধি"],
        "C", "medium", "factual",
        "Gomphosis (tooth in socket) is a classic fibrous joint; pubic symphysis is cartilaginous.",
        "গম্ফোসিস (দাঁতের সকেট) তন্তুময় সন্ধি; পিউবিক সিমফাইসিস তরুণাস্থিময়।",
    ),
    q(
        "Which cartilage type has abundant CaCO₃ deposited in its matrix?",
        "কোন তরুণাস্থির ম্যাট্রিক্সে প্রচুর CaCO₃ জমা থাকে?",
        ["Hyaline (clear)", "Yellow elastic", "White fibrous", "Calcified"],
        ["স্বচ্ছ (হায়ালিন)", "পীত তন্তুময়", "শ্বেত তন্তুময়", "চুনময় (ক্যালসিফাইড)"],
        "D", "easy", "factual",
        "Calcified cartilage is stiffened by calcium salts such as CaCO₃.",
        "চুনময় তরুণাস্থির ম্যাট্রিক্সে ক্যালসিয়াম লবণ (যেমন CaCO₃) জমে।",
    ),
    q(
        "Which features correctly describe a typical thoracic vertebra?",
        "আদর্শ থোরাসিক কশেরুকার কোন বৈশিষ্ট্যগুলো সঠিক?",
        [
            "Medium heart-shaped centrum and long slender spinous process",
            "Largest triangular vertebral foramen only",
            "No costal facets for ribs",
            "Fused into a single sacral bone",
        ],
        [
            "মাঝারি হৃদয়াকৃতি সেন্ট্রাম ও লম্বা সরু স্পাইনাস প্রসেস",
            "শুধু বৃহত্তম ত্রিকোণাকার ভার্টিব্রাল ফোরামেন",
            "পাঁজরের জন্য কোনো কস্টাল ফ্যাসেট নেই",
            "একটিমাত্র স্যাক্রাল অস্থিতে একীভূত",
        ],
        "A", "medium", "conceptual",
        "Typical thoracic vertebrae have a heart-shaped centrum and a long downward spinous process.",
        "আদর্শ থোরাসিক কশেরুকায় হৃদয়াকৃতি সেন্ট্রাম ও লম্বা নিম্নমুখী স্পাইনাস প্রসেস থাকে।",
    ),
    q(
        "In which of these bones is a well-developed Haversian system typically present?",
        "নিচের কোন অস্থিতে সাধারণত সুগঠিত হ্যাভারসিয়ান তন্ত্র থাকে?",
        ["Parietal", "Occipital", "Femur", "Ethmoid"],
        ["প্যারাইটাল", "অক্সিপিটাল", "ফিমার", "এথময়েড"],
        "C", "medium", "factual",
        "Compact bone of long bones such as the femur shows osteons (Haversian systems).",
        "ফিমারের মতো দীর্ঘ অস্থির নিরেট অংশে হ্যাভারসিয়ান তন্ত্র (অস্টিয়ন) থাকে।",
    ),
    q(
        "What type of cartilage is present in the trachea?",
        "শ্বাসনালিতে কোন ধরনের তরুণাস্থি থাকে?",
        ["Hyaline (clear)", "Elastic", "White fibrous", "Calcified"],
        ["স্বচ্ছ (হায়ালিন)", "স্থিতিস্থাপক", "শ্বেত তন্তুময়", "চুনময়"],
        "A", "easy", "factual",
        "Tracheal C-rings are hyaline cartilage.",
        "শ্বাসনালির সি-আকৃতির বলয় হায়ালিন তরুণাস্থির।",
    ),
    q(
        "Which bone is NOT a carpal bone of the wrist?",
        "নিচের কোনটি কব্জির কারপাল অস্থি নয়?",
        ["Scaphoid", "Trapezium", "Trapezoid", "Calcaneus"],
        ["স্ক্যাফয়েড", "ট্রাপেজিয়াম", "ট্রাপেজয়েড", "ক্যালকেনিয়াস"],
        "D", "easy", "factual",
        "Calcaneus is a tarsal (heel) bone, not a carpal.",
        "ক্যালকেনিয়াস গোড়ালির টারসাল অস্থি, কারপাল নয়।",
    ),
    q(
        "Which cell is commonly described in HSC texts as the mature/“dead” bone cell in lacunae?",
        "এইচএসসি পাঠ্যে ল্যাকুনায় অবস্থিত পরিণত/“মৃত” অস্থি কোষ কোনটি?",
        ["Osteoblast", "Osteocyte", "Chondrocyte", "Osteoclast"],
        ["অস্টিওব্লাস্ট", "অস্টিওসাইট", "কন্ড্রোসাইট", "অস্টিওক্লাস্ট"],
        "B", "medium", "factual",
        "Osteocytes are osteoblasts trapped in lacunae; texts often call them mature/dead bone cells.",
        "অস্টিওসাইট ল্যাকুনায় আবদ্ধ পরিণত অস্থি কোষ; পাঠ্যে প্রায়ই মৃত অস্থি কোষ বলা হয়।",
    ),
    q(
        "Where is the cuboid bone found?",
        "কিউবয়েড অস্থি কোন অংশে দেখা যায়?",
        ["Wrist", "Ankle/foot", "Skull vault", "Rib cage"],
        ["কব্জি", "গোড়ালি/পা", "করোটিকা খিলান", "বক্ষপিঞ্জর"],
        "B", "easy", "factual",
        "Cuboid is a tarsal bone of the lateral foot.",
        "কিউবয়েড পায়ের পার্শ্বীয় টারসাল অস্থি।",
    ),
    q(
        "How many bones form each half of the bony pelvic (hip) girdle in the adult?",
        "প্রাপ্তবয়স্ক মানুষে শ্রোণি-অস্থিচক্রের প্রতি অর্ধাংশে কতটি প্রধান অস্থি থাকে?",
        ["1 fused hip bone (from 3)", "8 separate bones", "5 sacral pieces only", "12 costal bones"],
        ["১টি সংযুক্ত হিপবোন (৩টির মিলন)", "৮টি পৃথক অস্থি", "শুধু ৫টি স্যাক্রাল খণ্ড", "১২টি পাঁজর অস্থি"],
        "A", "medium", "conceptual",
        "Each side of the pelvic girdle is one innominate bone fused from ilium, ischium and pubis.",
        "শ্রোণিচক্রের প্রতি পাশে ইলিয়াম–ইস্চিয়াম–পিউবিস মিলে একটি হিপবোন।",
    ),
    q(
        "Which vertebral region normally contains seven vertebrae?",
        "মেরুদণ্ডের কোন অংশে সাধারণত ৭টি কশেরুকা থাকে?",
        ["Cervical", "Thoracic", "Lumbar", "Sacral"],
        ["সার্ভাইকাল", "থোরাসিক", "লাম্বার", "স্যাক্রাল"],
        "A", "easy", "factual",
        "Humans have seven cervical vertebrae.",
        "মানুষের গ্রীবাদেশে সাতটি সার্ভাইকাল কশেরুকা থাকে।",
    ),
    q(
        "The patella belongs to which part of the skeleton?",
        "প্যাটেলা অস্থি কোন অংশের?",
        ["Vertebral column", "Skull", "Forelimb", "Hindlimb"],
        ["মেরুদণ্ড", "করোটি", "অগ্রপদ", "পশ্চাৎপদ"],
        "D", "easy", "factual",
        "The kneecap (patella) is a sesamoid bone of the hindlimb.",
        "হাঁটুর প্যাটেলা পশ্চাৎপদের সিসাময়েড অস্থি।",
    ),
    q(
        "How many bones form the human cranium (braincase)?",
        "মানুষের করোটিকার অস্থি সংখ্যা কত?",
        ["8", "14", "22", "29"],
        ["৮", "১৪", "২২", "২৯"],
        "A", "easy", "factual",
        "The cranium has 8 bones; facial skeleton adds more to make the full skull.",
        "করোটিকায় ৮টি অস্থি; মুখাবয়বের অস্থি মিলিয়ে পূর্ণ করোটি হয়।",
    ),
    q(
        "Which of the following is a bone of the pelvic girdle?",
        "নিচের কোনটি শ্রোণিচক্রের অস্থি?",
        ["Maxilla", "Scapula", "Pubis", "Clavicle"],
        ["ম্যাক্সিলা", "স্ক্যাপুলা", "পিউবিস", "ক্ল্যাভিকল"],
        "C", "easy", "factual",
        "Pubis is one of the three bones of the hip; scapula/clavicle are pectoral.",
        "পিউবিস হিপবোনের অংশ; স্ক্যাপুলা/ক্ল্যাভিকল অংসচক্রের।",
    ),
]


# --- t02: Muscles / পেশি ---
T02 = [
    q(
        "Which muscle group plays the main role in straightening (extending) the knee joint?",
        "হাঁটুর জয়েন্ট সোজা (এক্সটেনশন) করতে প্রধান ভূমিকা কোন পেশি পালন করে?",
        ["Soleus", "Gastrocnemius", "Quadriceps", "Gluteus"],
        ["সোলিয়াস", "গ্যাস্ট্রোকনেমিয়াস", "কোয়াড্রিসেপস", "গ্লুটিয়াস"],
        "C", "easy", "factual",
        "Quadriceps femoris is the primary knee extensor.",
        "কোয়াড্রিসেপস ফিমোরিস হাঁটু এক্সটেনশনের প্রধান পেশি।",
    ),
    q(
        "What is a main function of smooth muscle?",
        "মসৃণ পেশির প্রধান কাজ কোনটি?",
        [
            "Controls movement of materials in various ducts and hollow organs",
            "Keeps cardiac rhythm via intercalated discs alone",
            "Moves skeletal limbs under voluntary control",
            "Forms a rigid outer skeletal frame",
        ],
        [
            "বিভিন্ন নালি ও ফাঁপা অঙ্গে বস্তুর চলাচল নিয়ন্ত্রণ করে",
            "শুধু ইন্টারক্যালেটেড ডিস্ক দিয়ে হৃদ্ছন্দ রাখে",
            "ইচ্ছাকৃতভাবে অঙ্গ-প্রত্যঙ্গ চালায়",
            "দৃঢ় বহিঃকঙ্কাল গঠন করে",
        ],
        "A", "easy", "conceptual",
        "Visceral smooth muscle regulates peristalsis and vessel/duct tone.",
        "ভিসেরাল মসৃণ পেশি পেরিস্টালসিস ও নালি/বাহিকার টোন নিয়ন্ত্রণ করে।",
    ),
    q(
        "What is a tendon?",
        "টেনডন বলতে কী বোঝায়?",
        [
            "Dense white fibrous cord attaching muscle to bone",
            "Elastic sheet joining two bones at a joint only",
            "Fluid-filled synovial sac inside bone marrow",
            "Cartilage pad between vertebral bodies",
        ],
        [
            "পেশিকে অস্থির সাথে যুক্ত করা শ্বেত তন্তুময় দৃঢ় রজ্জু",
            "শুধু সন্ধিতে দুই অস্থি যুক্ত করা স্থিতিস্থাপক পর্দা",
            "অস্থিমজ্জার ভেতর তরলপূর্ণ সাইনোভিয়াল থলি",
            "কশেরুকা দেহের মধ্যবর্তী তরুণাস্থি প্যাড",
        ],
        "A", "easy", "factual",
        "Tendons are tough white fibrous cords connecting muscle to bone.",
        "টেনডন পেশি ও অস্থি সংযোগকারী মজবুত শ্বেত তন্তুময় রজ্জু।",
    ),
    q(
        "How do tendons and ligaments mainly differ?",
        "টেনডন ও লিগামেন্টের প্রধান পার্থক্য কী?",
        [
            "Tendon joins muscle to bone; ligament joins bone to bone",
            "Tendon joins bone to bone; ligament joins muscle to muscle",
            "Both only connect cartilage to nerve",
            "Ligament always contains Haversian canals",
        ],
        [
            "টেনডন পেশি–অস্থি; লিগামেন্ট অস্থি–অস্থি যুক্ত করে",
            "টেনডন অস্থি–অস্থি; লিগামেন্ট পেশি–পেশি যুক্ত করে",
            "উভয়ই শুধু তরুণাস্থি ও স্নায়ু যুক্ত করে",
            "লিগামেন্টে সবসময় হ্যাভারসিয়ান নালি থাকে",
        ],
        "A", "easy", "conceptual",
        "Classic HSC contrast: tendon = muscle–bone; ligament = bone–bone (more elastic).",
        "টেনডন = পেশি–অস্থি; লিগামেন্ট = অস্থি–অস্থি (অধিক স্থিতিস্থাপক)।",
    ),
    q(
        "Which features apply to typical skeletal (striated) muscle fibres?",
        "আদর্শ অমসৃণ/কঙ্কাল পেশি তন্তুর কোন বৈশিষ্ট্যগুলো প্রযোজ্য?",
        [
            "Myofibrils present and transverse striations present",
            "Spindle-shaped and no myofibrils",
            "Intercalated discs throughout every fibre",
            "Always involuntary and non-striated",
        ],
        [
            "মায়োফাইব্রিল ও অনুপ্রস্থ রেখা থাকে",
            "মাকু আকৃতির এবং মায়োফাইব্রিল নেই",
            "প্রতিটি তন্তুতে ইন্টারক্যালেটেড ডিস্ক",
            "সবসময় অনৈচ্ছিক ও রেখাবিহীন",
        ],
        "A", "medium", "conceptual",
        "Skeletal fibres are multinucleate, myofibril-rich and cross-striated; voluntary.",
        "কঙ্কাল পেশি বহুকেন্দ্রিক, মায়োফাইব্রিলযুক্ত ও অনুপ্রস্থ রেখাযুক্ত; ঐচ্ছিক।",
    ),
    q(
        "Smooth muscle fibres are typically described as which shape?",
        "মসৃণ পেশি তন্তু সাধারণত কোন আকৃতির?",
        ["Spindle (fusiform)", "Long cylindrical branched", "Cube-shaped epithelial", "Star-shaped neuron-like"],
        ["মাকু (ফিউজিফর্ম)", "লম্বা নলাকার শাখাযুক্ত", "ঘনকাকার এপিথেলিয়াল", "তারকাকৃতি নিউরনসদৃশ"],
        "A", "easy", "factual",
        "Visceral smooth muscle cells are spindle-shaped and uninucleate.",
        "ভিসেরাল মসৃণ পেশি কোষ মাকু আকৃতির ও এককেন্দ্রিক।",
    ),
    q(
        "Intercalated discs are a special feature of which muscle type?",
        "ইন্টারক্যালেটেড ডিস্ক কোন পেশির বিশেষ বৈশিষ্ট্য?",
        ["Smooth muscle", "Skeletal muscle", "Cardiac muscle", "All connective tissues"],
        ["মসৃণ পেশি", "কঙ্কাল পেশি", "হৃৎপেশি", "সব সংযোজক কলা"],
        "C", "easy", "factual",
        "Cardiac muscle fibres join at intercalated discs for coordinated contraction.",
        "হৃৎপেশি তন্তু ইন্টারক্যালেটেড ডিস্কে যুক্ত হয়ে সমন্বিত সংকোচন করে।",
    ),
    q(
        "Hamstring muscles mainly help to do what at the knee?",
        "হ্যামস্ট্রিং পেশিগুলো হাঁটুতে প্রধানত কী করতে সাহায্য করে?",
        [
            "Flex (bend) the knee and bring femur closer toward the tibia posteriorly",
            "Only extend the knee like quadriceps",
            "Abduct the arm at the shoulder",
            "Rotate the atlas on the axis alone",
        ],
        [
            "হাঁটু ভাঁজ (ফ্লেক্স) করে ফিমার ও টিবিয়াকে পেছন দিকে নিকটবর্তী করে",
            "শুধু কোয়াড্রিসেপসের মতো হাঁটু সোজা করে",
            "কাঁধে বাহু অ্যাবডাক্ট করে",
            "শুধু অ্যাটলাসকে অক্ষের ওপর ঘোরায়",
        ],
        "A", "medium", "conceptual",
        "Hamstrings (semimembranosus, semitendinosus, biceps femoris) are knee flexors.",
        "হ্যামস্ট্রিং (সেমিমেমব্রেনোসাস ইত্যাদি) হাঁটু ফ্লেক্সর পেশি।",
    ),
    q(
        "Where is the deltoid ridge (tuberosity) located?",
        "ডেল্টয়েড রিজ কোথায় বিদ্যমান?",
        ["Radius", "Femur", "Tibia", "Humerus"],
        ["রেডিয়াস", "ফিমার", "টিবিয়া", "হিউমেরাস"],
        "D", "easy", "factual",
        "The deltoid tuberosity/ridge is on the shaft of the humerus for deltoid insertion.",
        "হিউমেরাসের শ্যাফটে ডেল্টয়েড রিজ/টিউবারোসিটি থাকে।",
    ),
    q(
        "Which muscle action raises a body part upward?",
        "দেহের কোনো অংশকে উপরে তুলতে সাহায্য করে কোন পেশি ক্রিয়া?",
        ["Abductor", "Levator", "Depressor", "Rotator"],
        ["অ্যাবডাক্টর", "লিভেটর", "ডিপ্রেসর", "রোটেটর"],
        "B", "easy", "factual",
        "Levator muscles elevate; depressors lower; abductors move away from midline.",
        "লিভেটর উত্তোলন করে; ডিপ্রেসর নামিয়ে আনে; অ্যাবডাক্টর মধ্যরেখা থেকে দূরে নেয়।",
    ),
    q(
        "A muscle that moves a limb toward the midline is called what?",
        "অঙ্গকে মধ্যরেখার দিকে আনে এমন পেশিকে কী বলে?",
        ["Adductor", "Abductor", "Levator", "Depressor"],
        ["অ্যাডাক্টর", "অ্যাবডাক্টর", "লিভেটর", "ডিপ্রেসর"],
        "A", "easy", "factual",
        "Adductors pull toward the midline; abductors move away.",
        "অ্যাডাক্টর মধ্যরেখার দিকে টানে; অ্যাবডাক্টর দূরে সরায়।",
    ),
    q(
        "Which protein filaments are the thick filaments of the sarcomere?",
        "সারকোময়ারের মোটা তন্তু কোন প্রোটিন দিয়ে গঠিত?",
        ["Myosin", "Actin only", "Collagen of tendon only", "Keratin of skin only"],
        ["মায়োসিন", "শুধু অ্যাক্টিন", "শুধু টেনডনের কোলাজেন", "শুধু ত্বকের কেরাটিন"],
        "A", "easy", "factual",
        "Thick filaments are myosin; thin filaments are mainly actin.",
        "মোটা তন্তু মায়োসিন; পাতলা তন্তু প্রধানত অ্যাক্টিন।",
    ),
    q(
        "What is the cytoplasm of a muscle fibre called?",
        "পেশি তন্তুর সাইটোপ্লাজমকে কী বলে?",
        ["Sarcoplasm", "Neuroplasm only", "Osteoid", "Chondrin matrix"],
        ["সারকোপ্লাজম", "শুধু নিউরোপ্লাজম", "অস্টিওয়েড", "কন্ড্রিন ম্যাট্রিক্স"],
        "A", "easy", "factual",
        "Sarcoplasm contains myofibrils, mitochondria and glycogen stores.",
        "সারকোপ্লাজমে মায়োফাইব্রিল, মাইটোকন্ড্রিয়া ও গ্লাইকোজেন থাকে।",
    ),
    q(
        "What is the plasma membrane of a muscle fibre called?",
        "পেশি তন্তুর প্লাজমা ঝিল্লিকে কী বলে?",
        ["Sarcolemma", "Periosteum", "Neurilemma only of bone", "Pleura"],
        ["সারকোলেমা", "পেরিঅস্টিয়াম", "শুধু অস্থির নিউরিলেমা", "প্লুরা"],
        "A", "easy", "factual",
        "Sarcolemma is the cell membrane of a muscle fibre; sarcoplasm is its cytoplasm.",
        "সারকোলেমা পেশি তন্তুর কোষঝিল্লি; সারকোপ্লাজম এর সাইটোপ্লাজম।",
    ),
    q(
        "Compared with skeletal muscle, cardiac muscle fibres are typically—",
        "কঙ্কাল পেশির তুলনায় হৃৎপেশি তন্তু সাধারণত—",
        [
            "Shorter, branched, and joined by intercalated discs",
            "Long, unbranched, and multinucleate like skeletal fibres only",
            "Spindle-shaped without any striations",
            "Absent from the heart wall",
        ],
        [
            "খাটো, শাখাযুক্ত এবং ইন্টারক্যালেটেড ডিস্কযুক্ত",
            "শুধু কঙ্কালের মতো লম্বা, শাখাবিহীন ও বহুকেন্দ্রিক",
            "মাকু আকৃতির ও সম্পূর্ণ রেখাবিহীন",
            "হৃৎপ্রাচীরে অনুপস্থিত",
        ],
        "A", "medium", "conceptual",
        "Cardiac fibres are branched, mostly uninucleate, striated, with intercalated discs.",
        "হৃৎপেশি শাখাযুক্ত, প্রায় এককেন্দ্রিক, রেখাযুক্ত ও ইন্টারক্যালেটেড ডিস্কযুক্ত।",
    ),
    q(
        "In muscle terminology, the relatively fixed attachment end is called what?",
        "পেশি পরিভাষায় অপেক্ষাকৃত স্থির সংযোগ প্রান্তকে কী বলে?",
        ["Origin", "Insertion only as the fixed end", "Sarcomere mid-line only", "Haversian canal"],
        ["উৎস (অরিজিন)", "শুধু ইনসারশনকে স্থির প্রান্ত বলা", "শুধু সারকোময়ার মধ্যরেখা", "হ্যাভারসিয়ান নালি"],
        "A", "easy", "factual",
        "Origin is usually proximal/fixed; insertion is the more movable attachment.",
        "অরিজিন সাধারণত স্থির/নিকটবর্তী; ইনসারশন অধিক চলনশীল প্রান্ত।",
    ),
    q(
        "Which control pattern correctly matches muscle types?",
        "পেশির প্রকারের সাথে কোন নিয়ন্ত্রণ বিন্যাস মিলে?",
        [
            "Skeletal = voluntary; cardiac and smooth = involuntary",
            "All three muscle types are always voluntary",
            "Only smooth muscle is voluntary; skeletal is involuntary",
            "Cardiac muscle is under conscious minute-by-minute will",
        ],
        [
            "কঙ্কাল = ঐচ্ছিক; হৃৎ ও মসৃণ = অনৈচ্ছিক",
            "তিন প্রকার পেশিই সবসময় ঐচ্ছিক",
            "শুধু মসৃণ ঐচ্ছিক; কঙ্কাল অনৈচ্ছিক",
            "হৃৎপেশি মুহূর্তে মুহূর্তে সচেতন ইচ্ছায় চলে",
        ],
        "A", "easy", "conceptual",
        "Skeletal muscle is under will; heart and visceral smooth muscle are involuntary.",
        "কঙ্কাল পেশি ইচ্ছাধীন; হৃৎ ও ভিসেরাল মসৃণ পেশি অনৈচ্ছিক।",
    ),
    q(
        "What is the contractile unit of a myofibril between two Z-lines?",
        "দুই জেড-রেখার মধ্যবর্তী মায়োফাইব্রিলের সংকোচন একক কী?",
        ["Sarcomere", "Osteon", "Nephron", "Alveolus"],
        ["সারকোময়ার", "অস্টিয়ন", "নেফ্রন", "অ্যালভিওলাস"],
        "A", "easy", "factual",
        "The sarcomere is the basic contractile unit of striated muscle.",
        "সারকোময়ার রেখাযুক্ত পেশির মৌলিক সংকোচন একক।",
    ),
    q(
        "Gastrocnemius and soleus mainly act on which region?",
        "গ্যাস্ট্রোকনেমিয়াস ও সোলিয়াস প্রধানত কোন অঞ্চলে কাজ করে?",
        [
            "Calf — plantarflex the ankle / help push off in walking",
            "Only extend the fingers",
            "Only rotate the eyeball",
            "Only elevate the mandible for chewing",
        ],
        [
            "পিণ্ডালি — গোড়ালি প্লান্টারফ্লেক্স / হাঁটায় ধাক্কা দিতে সাহায্য",
            "শুধু আঙুল এক্সটেনড করে",
            "শুধু অক্ষিগোলক ঘোরায়",
            "শুধু চর্বণে নিম্নচোয়াল তোলে",
        ],
        "A", "medium", "factual",
        "These posterior leg muscles plantarflex the foot and are key in stance/push-off.",
        "এই পশ্চাৎ পা পেশি পদ প্লান্টারফ্লেক্স করে এবং হাঁটায় গুরুত্বপূর্ণ।",
    ),
    q(
        "Which statement about skeletal muscle nuclei is standard in HSC texts?",
        "কঙ্কাল পেশির নিউক্লিয়াস সম্পর্কে এইচএসসি পাঠ্যের আদর্শ বক্তব্য কোনটি?",
        [
            "Fibres are multinucleate with peripheral nuclei",
            "Each fibre has exactly one central nucleus only like smooth muscle",
            "Nuclei are absent from all skeletal fibres",
            "Nuclei are replaced by osteocytes",
        ],
        [
            "তন্তু বহুকেন্দ্রিক এবং নিউক্লিয়াস প্রান্তীয়",
            "প্রতি তন্তুতে মসৃণ পেশির মতো মাত্র এক কেন্দ্রীয় নিউক্লিয়াস",
            "সব কঙ্কাল তন্তুতে নিউক্লিয়াস নেই",
            "নিউক্লিয়াস অস্টিওসাইট দিয়ে প্রতিস্থাপিত",
        ],
        "A", "medium", "factual",
        "Long skeletal fibres form by fusion and keep many nuclei just under the sarcolemma.",
        "কঙ্কাল তন্তু সংযুক্তিতে তৈরি হয় এবং সারকোলেমার নিচে বহু নিউক্লিয়াস রাখে।",
    ),
]


# --- t03: Movement / চলন ---
T03 = [
    q(
        "Why is the joint between the skull and the first cervical vertebra called a first-class lever?",
        "করোটি ও প্রথম কশেরুকার সন্ধিকে প্রথম শ্রেণির লিভার বলা হয় কেন?",
        [
            "Fulcrum lies between the load (head weight) and the effort (neck muscles)",
            "Load always lies between fulcrum and effort only",
            "Effort always lies between fulcrum and load only",
            "There is no fulcrum in this joint",
        ],
        [
            "পিভট ভার (মাথার ওজন) ও প্রচেষ্টার (ঘাড়ের পেশি) মাঝখানে থাকে",
            "ভার সবসময় পিভট ও প্রচেষ্টার মাঝে থাকে",
            "প্রচেষ্টা সবসময় পিভট ও ভারের মাঝে থাকে",
            "এ সন্ধিতে কোনো পিভট নেই",
        ],
        "A", "medium", "conceptual",
        "At the atlanto-occipital joint the fulcrum is between load and muscular effort (1st class).",
        "অ্যাটলান্টো-অক্সিপিটাল সন্ধিতে পিভট ভার ও পেশি প্রচেষ্টার মাঝে (১ম শ্রেণি)।",
    ),
    q(
        "In a third-class lever example at the human elbow, the elbow joint acts as what?",
        "মানুষের কনুই সন্ধির তৃতীয় শ্রেণির লিভার উদাহরণে কনুই সন্ধি কী হিসেবে কাজ করে?",
        ["Fulcrum (pivot)", "Effort only", "Load only", "Ligament only"],
        ["পিভট (ফুলক্রাম)", "শুধু প্রচেষ্টা", "শুধু ভার", "শুধু লিগামেন্ট"],
        "A", "medium", "conceptual",
        "Elbow is the fulcrum; biceps provides effort between fulcrum and hand load (3rd class).",
        "কনুই পিভট; বাইসেপস প্রচেষ্টা পিভট ও হাতের ভারের মাঝে (৩য় শ্রেণি)।",
    ),
    q(
        "What is the glenoid cavity’s skeletal region?",
        "গ্লিনয়েড গহ্বর কোন কঙ্কাল অঞ্চলে থাকে?",
        ["Forelimb / pectoral girdle", "Hindlimb only", "Vertebral centrum", "Pelvic girdle acetabulum"],
        ["অগ্রপদ / অংসচক্র", "শুধু পশ্চাৎপদ", "কশেরুকা সেন্ট্রাম", "শ্রোণিচক্রের অ্যাসিটাবুলাম"],
        "A", "easy", "factual",
        "Glenoid cavity is on the scapula of the pectoral girdle for the humerus.",
        "গ্লিনয়েড গহ্বর অংসচক্রের স্ক্যাপুলায়; হিউমেরাস এখানে বসে।",
    ),
    q(
        "A bone break that does not pierce the skin is called what?",
        "চামড়া ভেদ না করে যে অস্থিভঙ্গ হয় তাকে কী বলে?",
        ["Closed (simple) fracture", "Compound fracture", "Greenstick only in adults always", "Dislocation without break"],
        ["বদ্ধ (সরল) অস্থিভঙ্গ", "যৌগিক অস্থিভঙ্গ", "প্রাপ্তবয়স্কে সবসময় গ্রিনিস্টিক", "ভাঙা ছাড়া সন্ধিচ্যুতি"],
        "A", "easy", "factual",
        "Closed/simple fracture: bone ends do not communicate with the exterior.",
        "বদ্ধ/সরল অস্থিভঙ্গে ভাঙা প্রান্ত ত্বক ভেদ করে বাইরে আসে না।",
    ),
    q(
        "Which first-aid ideas apply to managing a closed fracture?",
        "বদ্ধ অস্থিভঙ্গের প্রাথমিক ব্যবস্থাপনায় কোন ধারণাগুলো প্রযোজ্য?",
        [
            "Immobilize/support the site and identify severity and exact location",
            "Force the limb through full painful range immediately",
            "Ignore swelling and walk on the limb at once",
            "Remove all immobilization before medical care",
        ],
        [
            "স্থান স্থির/সাপোর্ট করা এবং মাত্রা ও সঠিক স্থান চিহ্নিত করা",
            "অঙ্গকে সঙ্গে সঙ্গে পূর্ণ বেদনাদায়ক চলাচলে বাধ্য করা",
            "ফোলা উপেক্ষা করে সঙ্গে সঙ্গে হাঁটা",
            "চিকিৎসার আগে সব স্থিরকরণ খুলে ফেলা",
        ],
        "A", "medium", "application",
        "Stabilize, locate and assess; avoid moving broken ends; seek proper care.",
        "স্থির রাখা, স্থান ও মাত্রা নির্ণয়; ভাঙা প্রান্ত না নাড়ানো; যথাযথ চিকিৎসা।",
    ),
    q(
        "Standing on the toes (raising the heel) is commonly cited as which lever class?",
        "পায়ের আঙুলে ভর দিয়ে গোড়ালি তোলা সাধারণত কোন শ্রেণির লিভার?",
        ["Second-class lever", "First-class only", "Third-class only", "Not a lever system"],
        ["দ্বিতীয় শ্রেণির লিভার", "শুধু প্রথম শ্রেণি", "শুধু তৃতীয় শ্রেণি", "লিভার তন্ত্র নয়"],
        "A", "medium", "conceptual",
        "Ball of foot = fulcrum, body weight = load, calf effort = behind—classic 2nd class.",
        "পদতলের অগ্রভাগ পিভট, দেহভার মাঝে, গোড়ালির পেশি প্রচেষ্টা—২য় শ্রেণি।",
    ),
    q(
        "What is the key difference between locomotion and mere movement in animals?",
        "প্রাণীতে চলন ও সাধারণ অঙ্গচালনার মূল পার্থক্য কী?",
        [
            "Locomotion displaces the whole body from place to place; movement may be local",
            "Movement always relocates the entire organism; locomotion never does",
            "Locomotion occurs only in plants",
            "They are identical terms with no distinction",
        ],
        [
            "চলনে সমগ্র দেহ স্থানান্তরিত হয়; অঙ্গচালনা স্থানীয় হতে পারে",
            "অঙ্গচালনায় সবসময় পুরো জীব সরে; চলনে কখনো সরে না",
            "চলন শুধু উদ্ভিদে ঘটে",
            "দুটি শব্দ অভিন্ন; কোনো পার্থক্য নেই",
        ],
        "A", "easy", "conceptual",
        "HSC framing: locomotion = whole-body displacement; movement = change of position of parts.",
        "চলন = সমগ্র দেহের স্থানান্তর; অঙ্গচালনা = অংশের অবস্থান পরিবর্তন।",
    ),
    q(
        "Which pair of muscles act as antagonists at the elbow during flexion–extension?",
        "কনুইয়ের ফ্লেক্সন–এক্সটেনশনে কোন পেশি জোড়া প্রধানত বিরোধী (অ্যান্টাগনিস্ট) কাজ করে?",
        ["Biceps and triceps", "Masseter and temporalis only", "Both gastrocnemii alone", "Only intercostals"],
        ["বাইসেপস ও ট্রাইসেপস", "শুধু ম্যাসেটার ও টেম্পোরালিস", "শুধু দুই গ্যাস্ট্রোকনেমিয়াস", "শুধু ইন্টারকস্টাল"],
        "A", "easy", "conceptual",
        "Biceps flexes; triceps extends—classic antagonistic pair for elbow movement.",
        "বাইসেপস ফ্লেক্স করে; ট্রাইসেপস এক্সটেনড করে—বিরোধী জোড়া।",
    ),
    q(
        "During skeletal muscle contraction, sliding-filament theory says which filaments slide?",
        "স্লাইডিং-ফিলামেন্ট তত্ত্ব অনুসারে কঙ্কাল পেশি সংকোচনে কোন তন্তুগুলো একে অপরের ওপর পিছলে?",
        [
            "Actin thin filaments slide over myosin thick filaments",
            "DNA strands slide over lipid bilayers",
            "Collagen fibres slide out of bone only",
            "Nerve axons slide into the sarcoplasm forever",
        ],
        [
            "অ্যাক্টিন পাতলা তন্তু মায়োসিন মোটা তন্তুর ওপর পিছলে",
            "ডিএনএ সূত্র লিপিড দ্বিস্তরের ওপর পিছলে",
            "শুধু কোলাজেন অস্থি থেকে বেরিয়ে পিছলে",
            "স্নায়ু অ্যাক্সন চিরকাল সারকোপ্লাজমে পিছলে ঢোকে",
        ],
        "A", "medium", "conceptual",
        "Cross-bridges pull thin actin past thick myosin, shortening sarcomeres.",
        "ক্রসব্রিজ অ্যাক্টিনকে মায়োসিনের ওপর টেনে সারকোময়ার ছোট করে।",
    ),
    q(
        "Which joint type allows the freest multi-axial movement, as in the shoulder?",
        "কাঁধের মতো সর্বাধিক বহুঅক্ষীয় চলন কোন ধরনের সন্ধিতে হয়?",
        ["Ball-and-socket synovial", "Suture fibrous", "Gomphosis", "Synchondrosis only"],
        ["বল-অ্যান্ড-সকেট সাইনোভিয়াল", "সুচার তন্তুময়", "গম্ফোসিস", "শুধু সিনকন্ড্রোসিস"],
        "A", "easy", "factual",
        "Shoulder and hip are ball-and-socket synovial joints with wide ROM.",
        "কাঁধ ও হিপ বল-সকেট সাইনোভিয়াল সন্ধি; চলনের পরিসর বড়।",
    ),
    q(
        "Elbow and knee are mainly examples of which synovial joint?",
        "কনুই ও হাঁটু প্রধানত কোন সাইনোভিয়াল সন্ধির উদাহরণ?",
        ["Hinge joint", "Pivot only", "Saddle only", "Plane gliding only"],
        ["হিঞ্জ সন্ধি", "শুধু পিভট", "শুধু স্যাডল", "শুধু প্লেন গ্লাইডিং"],
        "A", "easy", "factual",
        "Hinge joints mainly allow flexion and extension in one plane.",
        "হিঞ্জ সন্ধি প্রধানত এক তলে ফ্লেক্সন–এক্সটেনশন দেয়।",
    ),
    q(
        "Rotation of the head “no” movement mainly involves which joint arrangement?",
        "মাথা “না” বলে ঘোরানো প্রধানত কোন সন্ধি বিন্যাসে হয়?",
        ["Pivot joint between atlas and axis (odontoid)", "Suture of parietal bones", "Pubic symphysis", "Distal tibiofibular only"],
        ["অ্যাটলাস–অক্ষের পিভট সন্ধি (ওডোন্টয়েড)", "প্যারাইটাল সুচার", "পিউবিক সিমফাইসিস", "শুধু দূরবর্তী টিবিওফিবুলার"],
        "A", "medium", "factual",
        "The dens of axis forms a pivot with the atlas for head rotation.",
        "অক্ষের ডেন্স অ্যাটলাসের সাথে পিভট গঠন করে মাথা ঘোরাতে সাহায্য করে।",
    ),
    q(
        "Abduction of a limb means moving it in which direction relative to the midline?",
        "অঙ্গের অ্যাবডাকশন মানে মধ্যরেখার তুলনায় কোন দিকে সরানো?",
        ["Away from the midline", "Toward the midline only", "Only rotation on its long axis", "Only elevation without lateral shift"],
        ["মধ্যরেখা থেকে দূরে", "শুধু মধ্যরেখার দিকে", "শুধু দীর্ঘ অক্ষে ঘূর্ণন", "শুধু উত্তোলন; পার্শ্ব সরণ নয়"],
        "A", "easy", "factual",
        "Abduction = away from midline; adduction = toward midline.",
        "অ্যাবডাকশন = মধ্যরেখা থেকে দূরে; অ্যাডাকশন = মধ্যরেখার দিকে।",
    ),
    q(
        "What immediate energy molecule powers myosin cross-bridge cycling in muscle?",
        "পেশিতে মায়োসিন ক্রসব্রিজ চক্রের তাৎক্ষণিক শক্তি কোন অণু দেয়?",
        ["ATP", "DNA", "Urea", "Glycogen stored outside the cell only"],
        ["এটিপি", "ডিএনএ", "ইউরিয়া", "শুধু কোষের বাইরের গ্লাইকোজেন"],
        "A", "easy", "factual",
        "ATP hydrolysis fuels attachment–power stroke–detachment cycles.",
        "এটিপি ভাঙন ক্রসব্রিজ সংযোগ–পাওয়ার স্ট্রোক–বিচ্ছিন্নকরণ চালায়।",
    ),
    q(
        "How do tendons contribute to movement?",
        "চলনে টেনডন কীভাবে অবদান রাখে?",
        [
            "They transmit contractile force from muscle to bone across a joint",
            "They secrete osteocalcin into the bloodstream only",
            "They form the synovial fluid of every joint",
            "They replace the need for any muscle contraction",
        ],
        [
            "সন্ধি পেরিয়ে পেশির সংকোচন বল অস্থিতে পৌঁছায়",
            "শুধু রক্তে অস্টিওক্যালসিন ক্ষরণ করে",
            "সব সন্ধির সাইনোভিয়াল তরল গঠন করে",
            "পেশি সংকোচনের প্রয়োজনই ফুরিয়ে দেয়",
        ],
        "A", "easy", "conceptual",
        "Muscle shortens → tendon pulls bone → joint angle changes (movement).",
        "পেশি ছোট হলে টেনডন অস্থি টানে → সন্ধির কোণ বদলে চলন হয়।",
    ),
    q(
        "What is a primary mechanical role of ligaments during movement?",
        "চলনের সময় লিগামেন্টের প্রাথমিক যান্ত্রিক ভূমিকা কী?",
        [
            "Stabilize joints and limit excessive/unwanted motion between bones",
            "Generate the main contractile force like actin–myosin",
            "Produce red blood cells in marrow",
            "Store bile for digestion",
        ],
        [
            "সন্ধি স্থিতিশীল রাখা এবং অস্থির অতিরিক্ত/অবাঞ্ছিত চলন সীমিত করা",
            "অ্যাক্টিন–মায়োসিনের মতো প্রধান সংকোচন বল তৈরি করা",
            "মজ্জায় লোহিত কণিকা উৎপাদন করা",
            "পাচনের জন্য পিত্ত সঞ্চয় করা",
        ],
        "A", "easy", "conceptual",
        "Ligaments bind bones and restrain joint ranges to protect structures.",
        "লিগামেন্ট অস্থি বাঁধে ও সন্ধির পরিসর সীমায় রেখে সুরক্ষা দেয়।",
    ),
    q(
        "The human thoracic cage participates in which movement essential to breathing?",
        "মানব বক্ষপিঞ্জর শ্বসনের কোন অপরিহার্য চলনে অংশ নেয়?",
        [
            "Rhythmic expansion and relaxation that change thoracic volume",
            "Only permanent rigid fixation with zero motion",
            "Only rotation of the femur in the acetabulum",
            "Only blinking of eyelids",
        ],
        [
            "ছন্দময় প্রসারণ ও শিথিলন যা বক্ষ আয়তন বদলায়",
            "শুধু স্থায়ী দৃঢ় স্থিরতা; কোনো চলন নেই",
            "শুধু অ্যাসিটাবুলামে ফিমার ঘোরানো",
            "শুধু অক্ষিপল্লবের পলক ফেলা",
        ],
        "A", "medium", "application",
        "Ribs, sternum and thoracic vertebrae move to alter volume for inspiration/expiration.",
        "পাঁজর–স্টার্নাম–থোরাসিক কশেরুকা নড়ে আয়তন বদলে নিশ্বাস–প্রশ্বাস হয়।",
    ),
    q(
        "Which statement correctly matches a muscle action name?",
        "পেশি ক্রিয়ার নামের সাথে কোন বর্ণনা মিলে?",
        [
            "Depressor lowers a part; rotator turns a part around an axis",
            "Levator always lowers; depressor always elevates",
            "Abductor always adducts toward midline",
            "Flexor always extends a hinge joint",
        ],
        [
            "ডিপ্রেসর নামিয়ে আনে; রোটেটর অক্ষ ঘুরিয়ে দেয়",
            "লিভেটর সবসময় নামিয়ে; ডিপ্রেসর সবসময় তোলে",
            "অ্যাবডাক্টর সবসময় মধ্যরেখার দিকে আনে",
            "ফ্লেক্সর সবসময় হিঞ্জ সন্ধি সোজা করে",
        ],
        "A", "easy", "factual",
        "Standard action vocabulary: levator↑, depressor↓, rotator, abductor/adductor, flexor/extensor.",
        "লিভেটর↑, ডিপ্রেসর↓, রোটেটর, অ্যাবডাক্টর/অ্যাডাক্টর, ফ্লেক্সর/এক্সটেনসর।",
    ),
    q(
        "In adults, why is the vertebral count often stated as 26 rather than 33 separate movable pieces?",
        "পূর্ণবয়স্ক মানুষে কশেরুকা প্রায়শই ৩৩টির বদলে ২৬টি বলা হয় কেন?",
        [
            "Sacral and coccygeal vertebrae fuse into fewer bones",
            "All cervical vertebrae disappear after puberty",
            "Thoracic vertebrae are absorbed into the sternum",
            "Lumbar vertebrae migrate into the skull",
        ],
        [
            "স্যাক্রাল ও কক্সিজিয়াল কশেরুকা একীভূত হয়ে কম সংখ্যক অস্থি হয়",
            "বয়ঃসন্ধির পর সব সার্ভাইকাল কশেরুকা অদৃশ্য হয়",
            "থোরাসিক কশেরুকা স্টার্নামে শোষিত হয়",
            "লাম্বার কশেরুকা করোটিতে সরে যায়",
        ],
        "A", "medium", "conceptual",
        "33 segments in fetus/child; adult: 7C+12T+5L+1 sacrum+1 coccyx = 26.",
        "শিশুতে ৩৩ খণ্ড; প্রাপ্তবয়স্কে ৭+১২+৫+১ স্যাক্রাম+১ কক্সিক্স = ২৬।",
    ),
    q(
        "Which features identify a cervical vertebra such as the atlas/axis group in figures?",
        "চিত্রে অ্যাটলাস/অক্ষ শ্রেণির সার্ভাইকাল কশেরুকা চেনার বৈশিষ্ট্য কোনটি?",
        [
            "Transverse foramina present; axis also has an odontoid process",
            "Long slender spinous process only like mid-thoracic",
            "Largest kidney-shaped centrum of lumbar type only",
            "Complete fusion into the hip bone",
        ],
        [
            "ট্রান্সভার্স ফোরামেন থাকে; অক্ষে ওডোন্টয়েড প্রসেসও থাকে",
            "শুধু মধ্য-থোরাসিকের মতো লম্বা সরু স্পাইনাস",
            "শুধু লাম্বার ধরনের বৃহত্তম কিডনি আকৃতি সেন্ট্রাম",
            "সম্পূর্ণ হিপবোনে একীভূত",
        ],
        "A", "hard", "application",
        "Cervicals have transverse foramina; C2 uniquely bears the dens (odontoid).",
        "সার্ভাইকালে ট্রান্সভার্স ফোরামেন; সি২-এ ডেন্স (ওডোন্টয়েড) থাকে।",
    ),
]


TOPICS_MAP = {
    "bio2_27_ch07_t01": T01,
    "bio2_27_ch07_t02": T02,
    "bio2_27_ch07_t03": T03,
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
        "chapter": "bio2_27_ch07",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p242_pdf248.png",
            "p243_pdf249.png",
            "p244_pdf250.png",
            "p245_pdf251.png",
            "p246_pdf252.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio2_27_ch07_t01": {
                "title": "Skeleton and joints / কঙ্কাল ও অস্থিসন্ধি",
                "themes": [
                    "odontoid on cervical; hip = ilium+ischium+pubis; lumbar 5; foramen magnum occipital",
                    "hyaline traits; femur→acetabulum; osteocalcin; fibrous gomphosis; calcified CaCO₃",
                    "thoracic vertebra traits; Haversian in femur; tracheal hyaline; calcaneus not carpal",
                    "osteocyte; cuboid tarsal; pelvic girdle half; cervical 7; patella hindlimb; cranium 8; pubis pelvic",
                ],
            },
            "bio2_27_ch07_t02": {
                "title": "Muscles / পেশি",
                "themes": [
                    "quadriceps knee extension; smooth muscle ducts; tendon; tendon vs ligament",
                    "skeletal myofibrils+striations; spindle smooth; intercalated discs cardiac; hamstrings flex",
                    "deltoid ridge humerus; levator; adductor; myosin thick filaments; sarcoplasm",
                    "sarcolemma; cardiac branched; origin vs insertion; voluntary/involuntary; sarcomere; calf muscles; multinucleate fibres",
                ],
            },
            "bio2_27_ch07_t03": {
                "title": "Movement / চলন",
                "themes": [
                    "1st-class skull–atlas lever; 3rd-class elbow fulcrum; glenoid pectoral; closed fracture + first aid",
                    "2nd-class toe-raise; locomotion vs movement; biceps–triceps antagonists; sliding filament ATP",
                    "ball-socket; hinge; atlas–axis pivot; abduction; tendon force; ligament limit; thoracic breathing motion",
                    "action vocabulary; adult 26 vertebrae fusion; cervical ID transverse foramen + dens",
                ],
            },
        },
        "low_confidence": [
            "OCR of printed MCQ pages p242–246 is noisy (garbled options/answer marks); stems reconstructed from readable fragments, CQ text on earlier pages, and standard HSC Zoology Ch7 facts.",
            "Figure-/stimulus-linked bank items (cartilage diagrams, muscle P/Q labels, fracture vignettes) rewritten as standalone stems.",
            "Pelvic girdle bone-count stem framed as one fused hip bone per side (from three primordia) to avoid ambiguous board option OCR.",
            "Movement topic supplemented with levers, joint types, and sliding-filament items because dedicated locomotion MCQ OCR density was lower.",
            "Cartilage-heavy OCR stems kept mainly under t01 (skeleton/joints); t02 focused on muscle structure, types, and actions.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio2_27_ch07_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio2_27_ch07_t01": 20,
                "bio2_27_ch07_t02": 20,
                "bio2_27_ch07_t03": 20,
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
        / "ch07_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
