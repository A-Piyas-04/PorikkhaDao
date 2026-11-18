#!/usr/bin/env python3
"""Seed Biology 2nd Paper Ch2 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio2_27_ch02_t01..t03 (Hydra; Grasshopper; Bony fish).
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
    "biology p2 ch02; curated bilingual"
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


# --- t01: Hydra / হাইড্রা ---
T01 = [
    q(
        "Which locomotion of Hydra is comparatively the fastest?",
        "নিচের কোনটি হাইড্রার তুলনামূলক দ্রুত চলন?",
        ["Looping", "Gliding", "Walking", "Somersaulting"],
        ["লুপিং", "গ্লাইডিং", "হাঁটা", "সমারসল্টিং"],
        "D", "easy", "factual",
        "Somersaulting is Hydra’s relatively rapid locomotion; looping covers long distance more slowly.",
        "সমারসল্টিং হাইড্রার তুলনামূলক দ্রুত চলন; লুপিং দীর্ঘ দূরত্বে ব্যবহৃত হয়।",
    ),
    q(
        "Where are cnidocytes most abundant in Hydra?",
        "Hydra-এর কোন অংশে নিডোসাইট কোষ সবচেয়ে বেশি থাকে?",
        ["Body column", "Tentacles", "Basal disc", "Body wall generally"],
        ["দেহকাণ্ড", "কর্ষিকা", "পাদচাকতি", "দেহপ্রাচীর সাধারণত"],
        "B", "easy", "factual",
        "Cnidocytes (stinging cells) are densest on the tentacles for prey capture and defence.",
        "শিকার ধরা ও আত্মরক্ষায় কর্ষিকায় নিডোসাইটের ঘনত্ব সর্বাধিক।",
    ),
    q(
        "Which cells make Hydra effectively ‘immortal’ through continuous renewal?",
        "কোন কোষের জন্য Hydra অমর প্রাণী বলে বিবেচিত?",
        ["Cnidocytes", "Musculoepithelial cells", "Germ cells", "Interstitial cells"],
        ["নিডোসাইট কোষ", "পেশি আবরণী কোষ", "জনন কোষ", "ইন্টারস্টিশিয়াল কোষ"],
        "D", "easy", "factual",
        "Totipotent interstitial cells continually replace other cell types, enabling lifelong regeneration.",
        "টটিপোটেন্ট ইন্টারস্টিশিয়াল কোষ অন্য কোষের পুনর্নবীকরণ করে বলে হাইড্রা অমরসদৃশ।",
    ),
    q(
        "Which Hydra cells are totipotent?",
        "হাইড্রার দেহের টটিপোটেন্ট কোষ কোনটি?",
        ["Sensory cells", "Gland cells", "Cnidocytes", "Interstitial cells"],
        ["সংবেদী কোষ", "গ্রন্থি কোষ", "নিডোসাইট", "ইন্টারস্টিশিয়াল কোষ"],
        "D", "easy", "factual",
        "Interstitial cells can differentiate into nematocytes, germ cells, and other types.",
        "ইন্টারস্টিশিয়াল কোষ নিমাটোসাইট, জননকোষসহ নানা কোষে রূপান্তরিত হতে পারে।",
    ),
    q(
        "Where are one-use nematocyst-bearing cells least abundant in Hydra?",
        "হাইড্রায় একবার ব্যবহার উপযোগী কোষ কোথায় সবচেয়ে কম থাকে?",
        ["Tentacles", "Hypostome", "Basal disc", "Body column"],
        ["কর্ষিকা", "হাইপোস্টোম", "পাদ-চাকতি", "দেহকাণ্ড"],
        "C", "medium", "factual",
        "Cnidocytes are scarcest on the pedal (basal) disc and densest on tentacles.",
        "পাদ-চাকতিতে নিডোসাইট সবচেয়ে কম; কর্ষিকায় সবচেয়ে বেশি।",
    ),
    q(
        "Which locomotion lets Hydra cover a long distance?",
        "কোন ধরনের চলন পদ্ধতিতে হাইড্রা লম্বা দূরত্ব অতিক্রম করে?",
        ["Looping", "Somersaulting", "Gliding", "Crawling"],
        ["লুপিং", "সমারসল্টিং", "গ্লাইডিং", "হামাগুড়ি"],
        "A", "easy", "factual",
        "Looping (special locomotion) covers longer distances; somersaulting is faster but shorter steps.",
        "লুপিং (বিশেষ চলন) দীর্ঘ দূরত্ব অতিক্রমে ব্যবহৃত হয়।",
    ),
    q(
        "Which Hydra locomotion is called leech-like movement?",
        "Hydra-এর কোন ধরনের চলনকে জোঁক চলন বলে?",
        ["Somersaulting", "Gliding", "Looping", "Walking"],
        ["সমারসল্টিং", "গ্লাইডিং", "লুপিং", "হাঁটা"],
        "D", "medium", "factual",
        "Walking (pedal locomotion) resembles leech movement with successive attachment of foot and tentacles.",
        "হাঁটা চলন জোঁকের মতো পাদচাকতি ও কর্ষিকার পর্যায়ক্রমে আটকানোর মাধ্যমে হয়।",
    ),
    q(
        "Intracellular digestion in Hydra mainly occurs in which cells?",
        "Hydra-এ অন্তঃকোষীয় পরিপাক ঘটে কোন কোষে?",
        ["Flagellated nutritive cells", "Pseudopodial nutritive cells", "Enzyme-secreting gland cells", "Mucus-secreting gland cells"],
        ["ফ্লাজেলাযুক্ত পুষ্টিকোষ", "ক্ষণপদযুক্ত পুষ্টিকোষ", "এনজাইম ক্ষরণকারী গ্রন্থি কোষ", "মিউকাস ক্ষরণকারী গ্রন্থি কোষ"],
        "B", "medium", "factual",
        "Gastrodermal amoeboid (pseudopodial) cells engulf food particles for intracellular digestion.",
        "গ্যাস্ট্রোডার্মিসের ক্ষণপদযুক্ত পুষ্টিকোষে খাদ্যকণা গ্রাস করে অন্তঃকোষীয় পরিপাক হয়।",
    ),
    q(
        "Why is the coelenteron called a gastrovascular cavity?",
        "সিলেন্টেরনকে কেন গ্যাস্ট্রোভাস্কুলার গহ্বর বলা হয়?",
        ["It stores only undigested waste", "It performs both digestion and distribution of nutrients", "It is filled with coelomic fluid", "It is lined only by epidermis"],
        ["এতে শুধু অপাচ্য বর্জ্য জমে", "এতে একসাথে পরিপাক ও পুষ্টি সংবহন ঘটে", "এটি সিলোমিক তরলে পূর্ণ", "এটি শুধু এপিডার্মিস দ্বারা আবৃত"],
        "B", "easy", "conceptual",
        "Extracellular digestion and transport of materials both occur in the coelenteron, hence gastrovascular.",
        "সিলেন্টেরনে বহিঃকোষীয় পরিপাক ও পদার্থ পরিবহন—উভয়ই হয় বলে একে গ্যাস্ট্রোভাস্কুলার বলা হয়।",
    ),
    q(
        "Which cells are found only in the outer layer (epidermis) of Hydra?",
        "Hydra-এর কোন কোষটি কেবলমাত্র বহিঃস্তরে বিদ্যমান?",
        ["Cnidoblast cells", "Nerve cells", "Gland cells", "Pseudopodial cells"],
        ["নিডোব্লাস্ট কোষ", "স্নায়ু কোষ", "গ্রন্থিকোষ", "ক্ষণপদীয় কোষ"],
        "A", "medium", "factual",
        "Cnidoblasts/cnidocytes occur in the epidermis; glandular and pseudopodial nutritive cells are gastrodermal.",
        "নিডোব্লাস্ট এপিডার্মিসে থাকে; গ্রন্থি ও ক্ষণপদীয় পুষ্টিকোষ গ্যাস্ট্রোডার্মিসে।",
    ),
    q(
        "Which nematocyst type contains phenol among Hydra’s stinging capsules?",
        "হাইড্রার কোন নেমাটোসিস্টে ফেনল থাকে?",
        ["Volvent", "Streptoline glutinant", "Penetrant", "Stereoline glutinant"],
        ["ভলভেন্ট", "স্ট্রেপটোলিন গ্লুটিন্যান্ট", "পেনিট্র্যান্ট", "স্টেরিওলিন গ্লুটিন্যান্ট"],
        "C", "hard", "factual",
        "Penetrant (stenotele) nematocysts contain hypnotoxin including phenolic components that immobilize prey.",
        "পেনিট্র্যান্ট (স্টেনোটিল) নেমাটোসিস্টে ফেনলসহ হিপনোটক্সিন থাকে যা শিকারকে অবশ করে।",
    ),
    q(
        "Which statement fits a volvent nematocyst?",
        "ভলভেন্ট নেমাটোসিস্টের ক্ষেত্রে প্রযোজ্য কোনটি?",
        ["Thread tip open with barbs only", "Closed tip, sticky secretion, and coiled thread that wraps prey", "Filled only with coelomic fluid", "Found only on the basal disc"],
        ["শুধু কাঁটাযুক্ত খোলা প্রান্ত", "শীর্ষ বন্ধ, আঠালো রস ও প্যাঁচানো সূত্রক যা শিকার প্যাঁচায়", "শুধু সিলোমিক তরলে পূর্ণ", "শুধু পাদচাকতিতে থাকে"],
        "B", "medium", "factual",
        "Volvents have a closed tip and a coiled thread that wraps and helps hold prey; they may secrete adhesive fluid.",
        "ভলভেন্টের শীর্ষ বন্ধ ও প্যাঁচানো সূত্রক শিকারকে প্যাঁচিয়ে ধরে; আঠালো রসও ক্ষরিত হতে পারে।",
    ),
    q(
        "Which feature is characteristic of a penetrant nematocyst?",
        "পেনিট্র্যান্ট নেমাটোসিস্টের বৈশিষ্ট্য কোনটি?",
        ["Thread armed with spines/barbs", "Secretes only sticky mucus", "Always has a closed tip", "Has a broad butt without toxin"],
        ["সূত্রক কাঁটাযুক্ত", "শুধু আঠালো মিউকাস ক্ষরণ করে", "সর্বদা শীর্ষ বন্ধ", "টক্সিনহীন প্রশস্ত গোড়া"],
        "A", "medium", "factual",
        "Penetrants have a barbed thread that pierces prey and injects hypnotoxin.",
        "পেনিট্র্যান্টের কাঁটাযুক্ত সূত্রক শিকার ভেদ করে হিপনোটক্সিন প্রবেশ করায়।",
    ),
    q(
        "Which cells form the gonads of Hydra?",
        "কোন কোষ Hydra-এর জননাঙ্গ সৃষ্টি করে?",
        ["Flagellated cells", "Musculoepithelial cells", "Pseudopodial cells", "Interstitial cells"],
        ["ফ্লাজেলীয় কোষ", "পেশি আবরণী কোষ", "ক্ষণপদীয় কোষ", "ইন্টারস্টিশিয়াল কোষ"],
        "D", "medium", "factual",
        "Interstitial cells aggregate and differentiate to form testes and ovaries.",
        "ইন্টারস্টিশিয়াল কোষ পুঞ্জীভূত হয়ে শুক্রাশয় ও ডিম্বাশয় গঠন করে।",
    ),
    q(
        "Which of the following is a gastrodermal cell of Hydra?",
        "Hydra-এর গ্যাস্ট্রোডার্মিসের কোষ কোনটি?",
        ["Cnidocyte", "Germ cell of epidermis", "Nutritive cell", "Sensory cell of epidermis only"],
        ["নিডোসাইট", "এপিডার্মিসের জনন কোষ", "পুষ্টি কোষ", "শুধু এপিডার্মিসের সংবেদী কোষ"],
        "C", "easy", "factual",
        "Nutritive (and gland) cells line the gastrodermis; cnidocytes are epidermal.",
        "পুষ্টিকোষ (ও গ্রন্থিকোষ) গ্যাস্ট্রোডার্মিসে; নিডোসাইট এপিডার্মিসে।",
    ),
    q(
        "What is commonly called the ‘blind sac’ in Hydra’s body plan?",
        "'ব্লাইন্ড স্যাক' বলা হয় কোনটিকে?",
        ["Hypostome", "Coelenteron", "Mesenteron of insects", "Mesoglea"],
        ["হাইপোস্টোম", "সিলেন্টেরন", "পতঙ্গের মেসেন্টেরন", "মেসোগ্লিয়া"],
        "B", "medium", "factual",
        "The coelenteron is a blind sac with a single opening (mouth) serving as anus as well.",
        "সিলেন্টেরন একমুখী ব্লাইন্ড স্যাক; মুখই খাদ্যগ্রহণ ও বর্জ্য নিষ্কাশনের পথ।",
    ),
    q(
        "Nitrogenous wastes of Hydra mainly meet which need of symbiotic algae?",
        "হাইড্রার নাইট্রোজেনঘটিত বর্জ্য থেকে শৈবালের কোন চাহিদা পূরণ হয়?",
        ["Lipid", "Carbohydrate", "Protein building / nitrogen", "Only mineral salts without N"],
        ["লিপিড", "শর্করা", "প্রোটিন গঠন / নাইট্রোজেন", "নাইট্রোজেনবিহীন শুধু খনিজ লবণ"],
        "C", "medium", "conceptual",
        "Symbiotic zoochlorellae use Hydra’s nitrogenous wastes as a nitrogen source for organic synthesis.",
        "সহজীবী শৈবাল (জুক্লোরেলা) হাইড্রার নাইট্রোজেনঘটিত বর্জ্য নাইট্রোজেন উৎস হিসেবে ব্যবহার করে।",
    ),
    q(
        "Which set is correct for Hydra?",
        "হাইড্রার ক্ষেত্রে কোনটি সঠিক?",
        ["Radial symmetry and coelenteron present; choanocytes absent", "Choanocytes present; coelenteron absent", "Bilateral symmetry only", "True coelom filled with coelomic fluid"],
        ["অরীয় প্রতিসাম্য ও সিলেন্টেরন আছে; কোয়ানোসাইট নেই", "কোয়ানোসাইট আছে; সিলেন্টেরন নেই", "শুধু দ্বিপার্শ্বীয় প্রতিসাম্য", "সিলোমিক তরলপূর্ণ সত্য সিলোম"],
        "A", "medium", "conceptual",
        "Hydra is radially symmetrical with a coelenteron; choanocytes characterize Porifera, not Cnidaria.",
        "হাইড্রা অরীয় প্রতিসম ও সিলেন্টেরনযুক্ত; কোয়ানোসাইট পরিফেরার বৈশিষ্ট্য।",
    ),
    q(
        "Which cells of Hydra are called reserve cells?",
        "হাইড্রার দেহের কোন কোষকে সংরক্ষিত কোষ বলে?",
        ["Sensory cells", "Gland cells", "Nerve cells", "Interstitial cells"],
        ["সংবেদী কোষ", "গ্রন্থি কোষ", "স্নায়ু কোষ", "ইন্টারস্টিশিয়াল কোষ"],
        "D", "easy", "factual",
        "Interstitial cells act as reserve/stem cells for regeneration and differentiation.",
        "ইন্টারস্টিশিয়াল কোষ সংরক্ষিত/স্টেম কোষ হিসেবে পুনরুৎপাদন ও বিভেদনে কাজ করে।",
    ),
    q(
        "Digestion in Hydra involves which gastrodermal cells?",
        "হাইড্রার পরিপাকে অংশ নেয় কোন কোষগুলো?",
        ["Only cnidocytes", "Flagellated, pseudopodial, and gland cells", "Only epidermal nerve cells", "Only mesogleal cells"],
        ["শুধু নিডোসাইট", "ফ্লাজেলীয়, ক্ষণপদীয় ও গ্রন্থি কোষ", "শুধু এপিডার্মিসের স্নায়ু কোষ", "শুধু মেসোগ্লিয়ার কোষ"],
        "B", "medium", "conceptual",
        "Flagellated and gland cells aid extracellular digestion; pseudopodial cells complete intracellular digestion.",
        "ফ্লাজেলীয় ও গ্রন্থিকোষ বহিঃকোষীয় এবং ক্ষণপদীয় কোষ অন্তঃকোষীয় পরিপাকে অংশ নেয়।",
    ),
]


# --- t02: Grasshopper / ঘাসফড়িং ---
T02 = [
    q(
        "Which of the following is NOT a mouthpart of the grasshopper?",
        "ঘাসফড়িংয়ের মুখোপাঙ্গের অংশ নয় কোনটি?",
        ["Mandible", "Maxilla", "Labium", "Antenna"],
        ["ম্যান্ডিবল", "ম্যাক্সিলা", "ল্যাবিয়াম", "অ্যান্টেনা"],
        "D", "easy", "factual",
        "Antennae are sensory cephalic appendages, not mouthparts; mouthparts include labrum, mandible, maxilla, labium, hypopharynx.",
        "অ্যান্টেনা সংবেদী উপাঙ্গ; মুখোপাঙ্গ নয়। মুখোপাঙ্গে ল্যাব্রাম, ম্যান্ডিবল, ম্যাক্সিলা, ল্যাবিয়াম, হাইপোফ্যারিংক্স থাকে।",
    ),
    q(
        "The egg-laying organ of the grasshopper is the—",
        "ঘাসফড়িং এর ডিম পাড়ার অঙ্গ হলো—",
        ["Supra-anal plate", "Anal cerci", "Subgenital plate", "Ovipositor"],
        ["সুপ্রা-অ্যানাল প্লেট", "অ্যানাল সারসি", "সাবজেনিটাল প্লেট", "ওভিপজিটর"],
        "D", "easy", "factual",
        "The female ovipositor deposits eggs in soil; it is a key female character.",
        "স্ত্রী ঘাসফড়িংয়ের ওভিপজিটর মাটিতে ডিম পাড়ায়; এটি স্ত্রী বৈশিষ্ট্য।",
    ),
    q(
        "Which part of the grasshopper compound eye receives light?",
        "ঘাসফড়িং এর পুঞ্জাক্ষির কোন অংশটি আলো গ্রহণ করে?",
        ["Cornea", "Rhabdom", "Corneagen cells", "Musculoepithelial cells"],
        ["কর্ণিয়া", "র্যাবডোম", "কর্নিয়াজেন কোষ", "পেশি আবরণী কোষ"],
        "B", "medium", "factual",
        "The rhabdom of each ommatidium is the light-sensitive photoreceptive region.",
        "প্রতিটি ওমাটিডিয়ামের র্যাবডোম আলোক সংবেদী অংশ যা আলো গ্রহণ করে।",
    ),
    q(
        "Incomplete metamorphosis is seen in which animal?",
        "নিচের কোন প্রাণীতে অসম্পূর্ণ রূপান্তর দেখা যায়?",
        ["Mosquito", "Housefly", "Grasshopper", "Butterfly"],
        ["মশা", "মাছি", "ঘাসফড়িং", "প্রজাপতি"],
        "C", "easy", "factual",
        "Grasshoppers show hemimetabolous (incomplete) metamorphosis: egg → nymph → adult.",
        "ঘাসফড়িংয়ে অসম্পূর্ণ রূপান্তর: ডিম → নিম্ফ → পূর্ণাঙ্গ।",
    ),
    q(
        "Why is the grasshopper heart called neurogenic?",
        "ঘাসফড়িং এর হৃদ্যন্ত্রকে নিউরোজেনিক হার্ট বলার প্রধান কারণ কী?",
        ["Cardiac muscle has its own pacemaker", "Impulse originates in nearby ganglia, not in heart wall muscle", "Blood is always oxygenated in the heart", "Heart has four chambers like mammals"],
        ["হৃৎপেশিতে নিজস্ব পেসমেকার আছে", "হৃৎবিভব হৃৎপ্রাচীর নয়, কাছের গ্যাংগ্লিয়নে তৈরি হয়", "হৃদ্যন্ত্রে সর্বদা অক্সিজেনযুক্ত রক্ত থাকে", "স্তন্যপায়ীর মতো চার প্রকোষ্ঠ"],
        "B", "medium", "conceptual",
        "Insects lack typical myocardial pacemakers; cardiac rhythm is driven by nearby ganglia (neurogenic heart).",
        "পতঙ্গের হৃৎপ্রাচীরে পেসমেকার নেই; হৃৎবিভব নিকটস্থ গ্যাংগ্লিয়ন থেকে আসে বলে নিউরোজেনিক।",
    ),
    q(
        "Where is the intima found in the grasshopper?",
        "ঘাসফড়িং এর দেহে ইন্টিমা কোথায় থাকে?",
        ["Only in spiracles", "In the trachea", "Only in Malpighian tubules", "Only in the crop"],
        ["শুধু স্পাইরাকলে", "ট্রাকিয়ায়", "শুধু মালপিজিয়ান নালিকায়", "শুধু ক্রুপে"],
        "B", "medium", "factual",
        "The cuticular intima lines the tracheal tubes; finer tracheoles may lack a continuous thick intima in some texts, but trachea characteristically has intima.",
        "ট্রাকিয়ার অন্তঃপ্রাচীরে কিউটিকুলার ইন্টিমা থাকে।",
    ),
    q(
        "Which is a sclerite of the grasshopper head capsule?",
        "কোনটি ঘাসফড়িংয়ের মাথার স্ক্লেরাইট?",
        ["Epicranium", "Sternum", "Tergum of abdomen", "Labium"],
        ["এপিক্রেনিয়াম", "স্টারনাম", "উদরের টারগাম", "ল্যাবিয়াম"],
        "A", "easy", "factual",
        "The head capsule (epicranium) is the main cephalic sclerite; sternum/tergum are trunk plates; labium is a mouthpart.",
        "মস্তক ক্যাপসুলের অপর নাম এপিক্রেনিয়াম; এটি মাথার প্রধান স্ক্লেরাইট।",
    ),
    q(
        "The excretory organ of the grasshopper is the—",
        "ঘাসফড়িং-এর রেচন অঙ্গ কোনটি?",
        ["Nephridia", "Flame cells", "Malpighian tubules", "Green glands"],
        ["নেফ্রিডিয়া", "শিখা কোষ", "মালপিজিয়ান নালিকা", "সবুজ গ্রন্থি"],
        "C", "easy", "factual",
        "Malpighian tubules collect metabolic wastes from haemolymph and empty into the gut.",
        "মালপিজিয়ান নালিকা হিমোলিম্ফ থেকে বর্জ্য সংগ্রহ করে পৌষ্টিক নালিতে উন্মুক্ত হয়।",
    ),
    q(
        "Correct sequence of grasshopper tracheal system branches is—",
        "ঘাসফড়িং এর ট্রাকিয়াল তন্ত্রের সঠিক অনুক্রম কোনটি?",
        ["Spiracle → trachea → tracheole cell → tracheole", "Trachea → spiracle → tracheole → tracheole cell", "Spiracle → tracheole → trachea → tracheole cell", "Tracheole cell → spiracle → trachea → tracheole"],
        ["শ্বাসরন্ধ্র → ট্রাকিয়া → ট্রাকিওল কোষ → ট্রাকিওল", "ট্রাকিয়া → শ্বাসরন্ধ্র → ট্রাকিওল → ট্রাকিওল কোষ", "শ্বাসরন্ধ্র → ট্রাকিওল → ট্রাকিয়া → ট্রাকিওল কোষ", "ট্রাকিওল কোষ → শ্বাসরন্ধ্র → ট্রাকিয়া → ট্রাকিওল"],
        "A", "medium", "factual",
        "Air enters via spiracles into tracheae, then via tracheole cells into fine tracheoles supplying tissues.",
        "বাতাস শ্বাসরন্ধ্র দিয়ে ট্রাকিয়ায়, অতঃপর ট্রাকিওল কোষ হয়ে সূক্ষ্ম ট্রাকিওলে যায়।",
    ),
    q(
        "How many pairs of spiracles does a grasshopper typically have?",
        "ঘাসফড়িং এ সাধারণত কত জোড়া স্পাইরাকল থাকে?",
        ["Two pairs", "Five pairs", "Eight pairs", "Ten pairs"],
        ["দুই জোড়া", "পাঁচ জোড়া", "আট জোড়া", "দশ জোড়া"],
        "D", "medium", "factual",
        "Grasshoppers typically have 10 pairs of spiracles (2 thoracic + 8 abdominal).",
        "ঘাসফড়িংয়ে সাধারণত ১০ জোড়া স্পাইরাকল থাকে (২ বক্ষীয় + ৮ উদরীয়)।",
    ),
    q(
        "Into how many body regions is a grasshopper divided?",
        "ঘাসফড়িং এর দেহ কয়টি অঞ্চলে বিভক্ত?",
        ["Two", "Three", "Four", "Five"],
        ["দুই", "তিন", "চার", "পাঁচ"],
        "B", "easy", "factual",
        "Tagmata are head, thorax, and abdomen—three regions.",
        "দেহ তিন অঞ্চলে বিভক্ত: মস্তক, বক্ষ ও উদর।",
    ),
    q(
        "The structural unit of the compound eye is the—",
        "পুঞ্জাক্ষির একক কোনটি?",
        ["Ommatidium", "Rhabdom alone", "Only the cornea", "Spiracle"],
        ["ওমাটিডিয়াম", "শুধু র্যাবডোম", "শুধু কর্নিয়া", "স্পাইরাকল"],
        "A", "easy", "factual",
        "Each ommatidium is a complete visual unit of the compound eye.",
        "পুঞ্জাক্ষির প্রতিটি একক ওমাটিডিয়াম।",
    ),
    q(
        "Correct order of parts in a grasshopper leg is—",
        "ঘাসফড়িং এর পায়ের গঠনের সঠিক ক্রম হলো—",
        ["Coxa → trochanter → femur → tibia → tarsus", "Femur → coxa → tibia → trochanter → tarsus", "Tarsus → tibia → femur → coxa → trochanter", "Trochanter → tarsus → coxa → femur → tibia"],
        ["কক্সা → ট্রোক্যান্টার → ফিমার → টিবিয়া → টার্সাস", "ফিমার → কক্সা → টিবিয়া → ট্রোক্যান্টার → টার্সাস", "টার্সাস → টিবিয়া → ফিমার → কক্সা → ট্রোক্যান্টার", "ট্রোক্যান্টার → টার্সাস → কক্সা → ফিমার → টিবিয়া"],
        "A", "medium", "factual",
        "From base to tip: coxa, trochanter, femur, tibia, tarsus (with claws).",
        "গোড়া থেকে অগ্রভাগ: কক্সা, ট্রোক্যান্টার, ফিমার, টিবিয়া, টার্সাস।",
    ),
    q(
        "Which structure immediately follows the coxa in an insect leg?",
        "পতঙ্গের পায়ের কক্সা-পরবর্তী অংশ কোনটি?",
        ["Femur", "Trochanter", "Tarsus", "Tibia"],
        ["ফিমার", "ট্রোক্যান্টার", "টার্সাস", "টিবিয়া"],
        "B", "easy", "factual",
        "After coxa comes the trochanter, then femur.",
        "কক্সার পর ট্রোক্যান্টার, তারপর ফিমার।",
    ),
    q(
        "Which is a female-specific character of the grasshopper?",
        "নিচের কোন বৈশিষ্ট্য স্ত্রী ঘাসফড়িং এ দেখা যায়?",
        ["Ovipositor", "Only supra-anal plate without ovipositor", "Aedeagus", "Only anal cerci as egg layer"],
        ["ওভিপজিটর", "ওভিপজিটর ছাড়া শুধু সুপ্রা-অ্যানাল প্লেট", "ইডিয়াগাস", "শুধু অ্যানাল সারসি দিয়ে ডিম পাড়া"],
        "A", "easy", "factual",
        "The ovipositor is the female egg-laying apparatus; males lack it.",
        "ওভিপজিটর স্ত্রী ঘাসফড়িংয়ের ডিম পাড়ার অঙ্গ; পুরুষে থাকে না।",
    ),
    q(
        "What is the blood of the grasshopper called?",
        "ঘাসফড়িং এর রক্তের নাম কী?",
        ["Haemocyte", "Haemocoel", "Haemolymph", "Haemocyanin alone"],
        ["হিমোসাইট", "হিমোসিল", "হিমোলিম্ফ", "শুধু হিমোসায়ানিন"],
        "C", "easy", "factual",
        "Insect circulating fluid is haemolymph within the haemocoel; haemocytes are blood cells.",
        "পতঙ্গের রক্ত হিমোলিম্ফ; হিমোসাইট হলো রক্তকোষ, হিমোসিল হলো গহ্বর।",
    ),
    q(
        "Which part belongs to the proctodeum of the grasshopper gut?",
        "ঘাসফড়িংয়ের প্রোক্টোডিয়ামের অংশ কোনটি?",
        ["Gizzard", "Crop", "Mesenteron", "Ileum"],
        ["গিজার্ড", "ক্রুপ", "মেসেন্টেরন", "ইলিয়াম"],
        "D", "medium", "factual",
        "Proctodeum (hindgut) includes ileum, colon, and rectum; crop and gizzard are stomodeal; mesenteron is midgut.",
        "প্রোক্টোডিয়ামে ইলিয়াম, কোলন, রেকটাম; ক্রুপ-গিজার্ড স্টোমোডিয়াম, মেসেন্টেরন মধ্যান্ত্র।",
    ),
    q(
        "How many times does a grasshopper nymph typically moult to become adult?",
        "ঘাসফড়িং নিম্ফ থেকে পূর্ণাঙ্গ হতে সাধারণত কয়বার খোলস ত্যাগ করে?",
        ["Once", "Three times", "Four times", "Five times"],
        ["একবার", "তিনবার", "চারবার", "পাঁচবার"],
        "D", "medium", "factual",
        "In standard HSC treatment, the nymph moults five times before the adult stage.",
        "এইচএসসি পাঠ্য অনুযায়ী নিম্ফ সাধারণত পাঁচবার নির্মোচন করে পূর্ণাঙ্গ হয়।",
    ),
    q(
        "Which statement is applicable to the grasshopper?",
        "ঘাসফড়িং এর ক্ষেত্রে কোনটি প্রযোজ্য?",
        ["Excretory organ is nephridium", "True coelom is absent as haemocoel dominates", "Mouthparts are mandibulate", "Life cycle always has a true larval stage like butterfly"],
        ["রেচন অঙ্গ নেফ্রিডিয়াম", "সত্য সিলোম অনুপস্থিত বলে হিমোসিল প্রধান", "মুখোপাঙ্গ ম্যান্ডিবুলেট প্রকৃতির", "প্রজাপতির মতো সর্বদা লার্ভা দশা থাকে"],
        "C", "medium", "conceptual",
        "Grasshoppers have mandibulate mouthparts and incomplete metamorphosis (nymph, not a holometabolous larva).",
        "ঘাসফড়িংয়ের মুখোপাঙ্গ ম্যান্ডিবুলেট; রূপান্তর অসম্পূর্ণ (নিম্ফ), সম্পূর্ণ রূপান্তরের লার্ভা নয়।",
    ),
    q(
        "Which part of the ommatidium mainly helps in refraction of light?",
        "ওমাটিডিয়ামের কোন অংশ আলো প্রতিসরণে সাহায্য করে?",
        ["Only retinular cells", "Crystalline cone cells", "Only iris pigment sheath", "Spiracle plate"],
        ["শুধু রেটিনুলার কোষ", "ক্রিস্টালাইন কোণ কোষ", "শুধু আইরিশ রঞ্জক আবরণী", "স্পাইরাকল প্লেট"],
        "B", "hard", "factual",
        "Cornea and crystalline cone form the dioptric apparatus that refracts light onto the rhabdom.",
        "কর্নিয়া ও ক্রিস্টালাইন কোণ আলো প্রতিসরিত করে র্যাবডোমে ফেলে।",
    ),
]


# --- t03: Bony fish / অস্থিময় মাছ ---
T03 = [
    q(
        "In which organ of fish is the pneumatic duct present?",
        "মাছের কোন অঙ্গে নিউম্যাটিক নালি বিদ্যমান?",
        ["Gill", "Heart", "Liver", "Swim bladder"],
        ["ফুলকা", "হৃৎপিণ্ড", "যকৃত", "সন্তরণ থলি / পটকা"],
        "D", "easy", "factual",
        "In physostomous carp such as rohu, a pneumatic duct links the swim (air) bladder to the gut.",
        "রুইয়ের মতো ফাইসোস্টোম মাছে নিউম্যাটিক নালি পটকা ও অন্ত্রের সংযোগ করে।",
    ),
    q(
        "Which river is called the ‘fish mine’ of Bangladesh?",
        "‘মৎস্য খনি’ নামে অভিহিত কোনটি?",
        ["Buriganga", "Shitalakshya", "Halda", "Karnaphuli"],
        ["বুড়িগঙ্গা", "শীতলক্ষ্যা", "হালদা", "কর্ণফুলি"],
        "C", "easy", "factual",
        "The Halda River is renowned as a natural breeding ground and is often called the fish mine.",
        "হালদা নদী প্রাকৃতিক প্রজনন ক্ষেত্র হিসেবে ‘মৎস্য খনি’ নামে পরিচিত।",
    ),
    q(
        "Age range of dhani fry (spawn stage) is—",
        "ধানী পোনার বয়সসীমা হলো—",
        ["72 hours to 8 days", "72 hours to 16 days", "72 hours to 20 days", "72 hours to 30 days"],
        ["৭২ ঘণ্টা বয়স থেকে ৮ দিন", "৭২ ঘণ্টা বয়স থেকে ১৬ দিন", "৭২ ঘণ্টা বয়স থেকে ২০ দিন", "৭২ ঘণ্টা বয়স থেকে ৩০ দিন"],
        "B", "medium", "factual",
        "In HSC fishery notes, dhani fry are aged from about 72 hours to 16 days.",
        "পাঠ্য অনুযায়ী ধানী পোনা প্রায় ৭২ ঘণ্টা থেকে ১৬ দিন বয়স পর্যন্ত।",
    ),
    q(
        "Which fin lies just behind the operculum of rohu?",
        "কোনটি রুইমাছের কানকুয়ার পিছনের পাখনা?",
        ["Pelvic fin", "Pectoral fin", "Dorsal fin", "Anal fin"],
        ["শ্রোণি পাখনা", "বক্ষ পাখনা", "পৃষ্ঠ পাখনা", "পায়ু পাখনা"],
        "B", "easy", "factual",
        "Pectoral fins are paired fins situated immediately behind the operculum (gill cover).",
        "কানকুয়ার ঠিক পিছনে যুগ্ম বক্ষ পাখনা অবস্থিত।",
    ),
    q(
        "The principal locomotor organ of rohu is the—",
        "রুই মাছের প্রধান চলনাঙ্গ কোনটি?",
        ["Pectoral fin", "Pelvic fin", "Anal fin", "Caudal fin"],
        ["বক্ষ পাখনা", "শ্রোণি পাখনা", "পায়ু পাখনা", "পুচ্ছ পাখনা"],
        "D", "easy", "factual",
        "The caudal (tail) fin provides the main propulsive thrust in swimming.",
        "পুচ্ছ (লেজ) পাখনা সাঁতারে প্রধান চালিকা শক্তি দেয়।",
    ),
    q(
        "Which of the following is a paired fin of rohu?",
        "নিচের কোনটি রুইমাছের যুগ্ম পাখনা?",
        ["Dorsal fin", "Anal fin", "Pectoral fin", "Caudal fin"],
        ["পৃষ্ঠ-পাখনা", "পায়ু-পাখনা", "বক্ষ-পাখনা", "পুচ্ছ-পাখনা"],
        "C", "easy", "factual",
        "Paired fins are pectoral and pelvic; dorsal, anal, and caudal are unpaired.",
        "যুগ্ম পাখনা: বক্ষ ও শ্রোণি; বিজোড়: পৃষ্ঠ, পায়ু ও পুচ্ছ।",
    ),
    q(
        "What type of blood circulation occurs in rohu?",
        "রুই মাছের রক্ত সংবহন কোন ধরনের?",
        ["Double circuit", "Pulmonary only", "Single circuit", "Portal only"],
        ["দ্বিচক্রীয়", "শুধু পালমোনারি", "এক চক্রীয়", "শুধু পোর্টাল"],
        "C", "easy", "factual",
        "Fish have single-circuit circulation: heart → gills → body → heart.",
        "মাছে একচক্রীয় সংবহন: হৃৎপিণ্ড → ফুলকা → দেহ → হৃৎপিণ্ড।",
    ),
    q(
        "Correct path of blood through the rohu heart toward the gills is—",
        "রুই মাছের হৃৎপিণ্ডে রক্তপ্রবাহের সঠিক পথ কোনটি?",
        ["Ventricle → atrium → sinus venosus → gills", "Sinus venosus → atrium → ventricle → bulbus/conus arteriosus → gills", "Atrium → sinus venosus → ventricle → gills", "Bulbus → sinus venosus → atrium → ventricle"],
        ["ভেন্ট্রিকল → অ্যাট্রিয়াম → সাইনাস ভেনোসাস → ফুলকা", "সাইনাস ভেনোসাস → অ্যাট্রিয়াম → ভেন্ট্রিকল → বাল্বাস/কোনাস আর্টারিওসাস → ফুলকা", "অ্যাট্রিয়াম → সাইনাস ভেনোসাস → ভেন্ট্রিকল → ফুলকা", "বাল্বাস → সাইনাস ভেনোসাস → অ্যাট্রিয়াম → ভেন্ট্রিকল"],
        "B", "medium", "factual",
        "Venous blood enters sinus venosus, then atrium, ventricle, and exits via bulbus/conus arteriosus to the gills.",
        "শিরা রক্ত সাইনাস ভেনোসাস → অলিন্দ → নিলয় → বাল্বাস/কোনাস হয়ে ফুলকায় যায়।",
    ),
    q(
        "How many pairs of gill slits are in the pharyngeal region of rohu?",
        "রুই মাছের গলবিলীয় অঞ্চলে কত জোড়া ফুলকা ছিদ্র থাকে?",
        ["Three pairs", "Four pairs", "Five pairs", "Six pairs"],
        ["৩ জোড়া", "৪ জোড়া", "৫ জোড়া", "৬ জোড়া"],
        "B", "easy", "factual",
        "Rohu has four pairs of gills/gill slits on each side of the pharynx.",
        "রুইয়ের গলবিলের প্রতি পাশে চার জোড়া ফুলকা/ফুলকা ছিদ্র থাকে।",
    ),
    q(
        "Number of gill arches on each side of the rohu pharynx is—",
        "রুই মাছের গলবিলের প্রতি পাশে ফুলকা আর্চের সংখ্যা কত?",
        ["Three", "Four", "Five", "Six"],
        ["৩", "৪", "৫", "৬"],
        "B", "easy", "factual",
        "There are four gill arches bearing gills on each side.",
        "প্রতি পাশে চারটি ফুলকা আর্চ থাকে।",
    ),
    q(
        "Which artery supplies blood to the pelvic fins of rohu?",
        "রুই মাছের শ্রোণি পাখনায় রক্ত সংবহন করে কোন ধমনি?",
        ["Renal artery", "Caudal artery", "Iliac artery", "Subclavian artery"],
        ["রেনাল ধমনি", "কডাল ধমনি", "ইলিয়াক ধমনি", "সাবক্ল্যাভিয়ান ধমনি"],
        "C", "medium", "factual",
        "Iliac arteries supply the pelvic fins; subclavian supply pectorals; caudal goes to the tail.",
        "ইলিয়াক ধমনি শ্রোণি পাখনায়, সাবক্ল্যাভিয়ান বক্ষে, কডাল লেজে রক্ত নেয়।",
    ),
    q(
        "Which artery carries blood to the tail of rohu?",
        "রুইমাছের কোন ধমনি লেজে রক্ত পরিবহণ করে?",
        ["Renal artery", "Caudal artery", "Iliac artery", "Subclavian artery"],
        ["রেনাল ধমনি", "কডাল ধমনি", "ইলিয়াক ধমনি", "সাবক্ল্যাভিয়ান ধমনি"],
        "B", "easy", "factual",
        "The caudal artery runs into the tail region.",
        "কডাল ধমনি লেজ অঞ্চলে রক্ত পরিবহণ করে।",
    ),
    q(
        "Rete mirabile of rohu is associated with which organ?",
        "রেটিয়া মিরাবিলিয়া রুই মাছের কোন অঙ্গে দেখা যায়?",
        ["Liver", "Kidney", "Swim bladder", "Stomach only"],
        ["যকৃত", "বৃক্ক", "পটকা / সন্তরণ থলি", "শুধু পাকস্থলি"],
        "C", "medium", "factual",
        "The rete mirabile is a capillary network in the swim bladder wall that secretes gases.",
        "রেটিয়া মিরাবিলিয়া পটকার প্রাচীরের কৈশিক জাল যা গ্যাস নিঃসরণে সাহায্য করে।",
    ),
    q(
        "Which gas is generally NOT secreted by the rete mirabile?",
        "রেটিয়া মিরাবিলিয়া কর্তৃক কোন গ্যাস সাধারণত নিঃসৃত হয় না?",
        ["Hydrogen (H₂)", "Oxygen (O₂)", "Nitrogen (N₂)", "Carbon dioxide (CO₂)"],
        ["হাইড্রোজেন (H₂)", "অক্সিজেন (O₂)", "নাইট্রোজেন (N₂)", "কার্বন ডাইঅক্সাইড (CO₂)"],
        "A", "hard", "factual",
        "Swim-bladder gas is mainly O₂, N₂, and CO₂; hydrogen is not a typical rete secretion.",
        "পটকার গ্যাসে প্রধানত O₂, N₂, CO₂ থাকে; H₂ সাধারণত নিঃসৃত হয় না।",
    ),
    q(
        "What type of scales does rohu have?",
        "রুই মাছের আঁইশ কী ধরনের?",
        ["Placoid", "Cycloid", "Ctenoid only", "Ganoid only"],
        ["প্ল্যাকয়েড", "সাইক্লয়েড", "শুধু কটিনয়েড", "শুধু গ্যানয়েড"],
        "B", "easy", "factual",
        "Carps such as Labeo rohita bear cycloid scales.",
        "রুই (Labeo rohita) সাইক্লয়েড আঁইশযুক্ত কার্প জাতীয় মাছ।",
    ),
    q(
        "Sensory organs detecting water currents in rohu are mainly located in the—",
        "রুই মাছের ক্ষেত্রে পানির তরঙ্গ সংবেদী অঙ্গ প্রধানত থাকে—",
        ["Only in the swim bladder", "Only in the liver", "Along the lateral line", "Only in the branchiostegal membrane"],
        ["শুধু পটকায়", "শুধু যকৃতে", "পার্শ্বরেখায়", "শুধু ব্রাঞ্কিওস্টেগাল পর্দায়"],
        "C", "medium", "factual",
        "Neuromasts of the lateral-line system sense water movement and vibrations.",
        "পার্শ্বরেখার নিউরোমাস্ট কোষ পানির তরঙ্গ ও কম্পন সংবেদন করে।",
    ),
    q(
        "Which statement about carp (major carp) is correct?",
        "কার্প জাতীয় মাছ সম্পর্কে কোনটি সঠিক?",
        ["Marine fish without air bladder", "Freshwater fish lacking head scales but possessing an air bladder", "Always lack fins", "Four-chambered heart like mammals"],
        ["পটকাবিহীন সামুদ্রিক মাছ", "মাথায় আঁইশহীন কিন্তু পটকাযুক্ত মিঠাপানির মাছ", "সর্বদা পাখনাহীন", "স্তন্যপায়ীর মতো চার প্রকোষ্ঠ হৃৎপিণ্ড"],
        "B", "medium", "conceptual",
        "Carps are freshwater physostomous fishes without scales on the head but with a swim bladder; major carps include Rui, Catla, Mrigal.",
        "কার্প মিঠাপানির মাছ—মাথায় আঁইশ নেই কিন্তু পটকা আছে; মেজর কার্প: রুই, কাতলা, মৃগেল।",
    ),
    q(
        "Unpaired fins of rohu include—",
        "রুইমাছের বিজোড় পাখনা কোনগুলো?",
        ["Pectoral and pelvic only", "Dorsal, anal, and caudal", "Only pectoral", "Only pelvic"],
        ["শুধু বক্ষ ও শ্রোণি", "পৃষ্ঠ, পায়ু ও পুচ্ছ", "শুধু বক্ষ", "শুধু শ্রোণি"],
        "B", "easy", "factual",
        "Unpaired (median) fins are dorsal, anal, and caudal.",
        "বিজোড় পাখনা: পৃষ্ঠ, পায়ু ও পুচ্ছ পাখনা।",
    ),
    q(
        "The heart of rohu is also called a venous heart because—",
        "রুই মাছের হৃৎপিণ্ডকে ভেনাস হার্ট বলার কারণ—",
        ["It pumps only oxygenated blood", "It receives and pumps mainly deoxygenated (venous) blood to the gills", "It has four atria", "It lacks sinus venosus"],
        ["শুধু অক্সিজেনযুক্ত রক্ত পাম্প করে", "এতে প্রধানত অক্সিজেনবিহীন শিরা রক্ত এসে ফুলকায় যায়", "এতে চারটি অলিন্দ আছে", "সাইনাস ভেনোসাস নেই"],
        "B", "medium", "conceptual",
        "Only CO₂-rich venous blood passes through the fish heart before gill oxygenation.",
        "হৃৎপিণ্ড দিয়ে কেবল CO₂-সমৃদ্ধ শিরা রক্ত যায়; অক্সিজেনেশন ফুলকায় হয়।",
    ),
    q(
        "Which is a paired fin among the following?",
        "মাছের জোড়া পাখনা কোনটি?",
        ["Dorsal fin", "Caudal fin", "Anal fin", "Pelvic fin"],
        ["পৃষ্ঠ পাখনা", "পুচ্ছ পাখনা", "পায়ু পাখনা", "শ্রোণি পাখনা"],
        "D", "easy", "factual",
        "Pelvic (and pectoral) fins are paired; dorsal, anal, and caudal are unpaired.",
        "শ্রোণি ও বক্ষ যুগ্ম; পৃষ্ঠ, পায়ু, পুচ্ছ বিজোড়।",
    ),
]


TOPICS_MAP = {
    "bio2_27_ch02_t01": T01,
    "bio2_27_ch02_t02": T02,
    "bio2_27_ch02_t03": T03,
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
        "chapter": "bio2_27_ch02",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p088_pdf094.png",
            "p089_pdf095.png",
            "p090_pdf096.png",
            "p091_pdf097.png",
            "p092_pdf098.png",
            "p093_pdf099.png",
            "p094_pdf100.png",
            "p095_pdf101.png",
            "p096_pdf102.png",
            "p097_pdf103.png",
            "p098_pdf104.png",
            "p099_pdf105.png",
            "p100_pdf106.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio2_27_ch02_t01": {
                "title": "Hydra / হাইড্রা",
                "themes": [
                    "locomotion: somersaulting fastest; looping long distance; walking leech-like",
                    "cnidocytes densest on tentacles, scarcest on basal disc",
                    "interstitial cells: totipotent, reserve, immortality, gonad formation",
                    "nematocysts: penetrant/phenol/barbs; volvent wraps prey",
                    "coelenteron gastrovascular / blind sac; intracellular digestion in pseudopodial cells",
                    "cnidoblasts epidermal only; nutritive cells gastrodermal",
                    "radial symmetry + coelenteron; no choanocytes; symbiotic algae use N-wastes",
                ],
            },
            "bio2_27_ch02_t02": {
                "title": "Grasshopper / ঘাসফড়িং",
                "themes": [
                    "antenna not mouthpart; mandibulate mouthparts; ovipositor female",
                    "incomplete metamorphosis; five nymphal moults",
                    "neurogenic heart; haemolymph; 10 pairs spiracles",
                    "trachea intima; spiracle→trachea→tracheole cell→tracheole",
                    "Malpighian tubules; compound eye ommatidium/rhabdom/crystalline cone",
                    "leg coxa→trochanter→femur→tibia→tarsus; three tagmata",
                    "epicranium head capsule; proctodeum includes ileum",
                ],
            },
            "bio2_27_ch02_t03": {
                "title": "Bony fish / অস্থিময় মাছ",
                "themes": [
                    "pneumatic duct in swim bladder; rete mirabile gases (not H₂)",
                    "Halda fish mine; dhani fry 72h–16 days; major carp characters",
                    "pectoral behind operculum; caudal main locomotor; paired vs unpaired fins",
                    "single-circuit venous heart: SV→atrium→ventricle→bulbus→gills",
                    "four pairs gills/arches; cycloid scales; lateral line sense",
                    "iliac→pelvic; caudal→tail; venous heart carries deoxygenated blood",
                ],
            },
        },
        "low_confidence": [
            "OCR of printed pages p088–100 is noisy (garbled options/answer marks); many stems reconstructed from readable fragments and standard HSC Zoology Ch2 facts.",
            "Figure-only and stimulus-linked bank items rewritten as standalone stems (no dependency on missing diagrams).",
            "Grasshopper heart chamber count and some multi-statement i/ii/iii keys were noisy in OCR and replaced with clearer factual stems.",
            "Dhani-fry age band taken from readable board-style item (72h–16 days); fingerling ranges vary by source.",
            "Nematocyst chemistry (phenol in penetrant) and rete gas exclusion (H₂) follow common HSC keys where OCR answer marks were ambiguous.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio2_27_ch02_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio2_27_ch02_t01": 20,
                "bio2_27_ch02_t02": 20,
                "bio2_27_ch02_t03": 20,
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
        / "ch02_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
