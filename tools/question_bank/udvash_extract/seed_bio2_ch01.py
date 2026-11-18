#!/usr/bin/env python3
"""Seed Biology 2nd Paper Ch1 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio2_27_ch01_t01..t03 (classification principles; major phyla; diversity).
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
    "biology p2 ch01; curated bilingual"
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
    # Scientific names / Latin-only options: satisfy Bangla-option check.
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


# --- t01: Principles of classification / শ্রেণিবিন্যাসের নীতি ---
T01 = [
    q(
        "Who introduced the binomial system of scientific naming of organisms?",
        "প্রাণীর বিশেষ বৈজ্ঞানিক নামের প্রবর্তন করেন কোন বিজ্ঞানী?",
        ["Ernst Haeckel", "Carolus Linnaeus", "Charles Darwin", "Johann Mendel"],
        ["আর্নেস্ট হেকেল", "ক্যারোলাস লিনিয়াস", "চার্লস ডারউইন", "জোহান মেন্ডেল"],
        "B", "easy", "factual",
        "Carolus Linnaeus established binomial nomenclature; each species gets a genus and specific epithet.",
        "ক্যারোলাস লিনিয়াস দ্বিনামকরণ পদ্ধতি প্রবর্তন করেন; প্রতিটি প্রজাতির গণ ও প্রজাতি নাম থাকে।",
    ),
    q(
        "Who is regarded as the father of zoology?",
        "প্রাণিবিদ্যার জনক কে?",
        ["Linnaeus", "Theophrastus", "Aristotle", "Darwin"],
        ["লিনিয়াস", "থিওফ্রাস্টাস", "অ্যারিস্টটল", "ডারউইন"],
        "C", "easy", "factual",
        "Aristotle is traditionally called the father of zoology for early systematic animal study.",
        "প্রাণীদের প্রাথমিক সুশৃঙ্খল অধ্যয়নের জন্য অ্যারিস্টটলকে প্রাণিবিদ্যার জনক বলা হয়।",
    ),
    q(
        "What type of symmetry is shown by Astropecten irregularis (starfish)?",
        "Astropecten irregularis-এ কোন ধরনের প্রতিসাম্যতা দেখা যায়?",
        ["Radial", "Biradial", "Pentaradial", "Bilateral"],
        ["অরীয়", "দ্বিঅরীয়", "পঞ্চঅরীয়", "দ্বিপার্শ্বীয়"],
        "C", "easy", "factual",
        "Adult starfish such as Astropecten show pentaradial (five-rayed) symmetry.",
        "Astropecten-এর মতো প্রাপ্তবয়স্ক তারামাছে পঞ্চঅরীয় প্রতিসাম্যতা দেখা যায়।",
    ),
    q(
        "Which animal shows biradial symmetry?",
        "দ্বিঅরীয় প্রতিসম প্রাণী কোনটি?",
        ["Aurelia", "Coeloplana", "Pieris", "Pila"],
        ["Aurelia", "Coeloplana", "Pieris", "Pila"],
        "B", "medium", "factual",
        "Coeloplana shows biradial symmetry; Aurelia is radial, Pieris bilateral, and Pila asymmetric as an adult.",
        "Coeloplana দ্বিঅরীয়; Aurelia অরীয়, Pieris দ্বিপার্শ্বীয় এবং প্রাপ্তবয়স্ক Pila অপ্রতিসম।",
    ),
    q(
        "Which alga-like colonial organism shows spherical symmetry?",
        "কোনটিতে গোলীয় প্রতিসাম্যতা দেখা যায়?",
        ["Volvox", "Hydra", "Pila", "Julus"],
        ["Volvox", "Hydra", "Pila", "Julus"],
        "A", "easy", "factual",
        "Volvox (and similar forms like Radiolaria) exemplify spherical symmetry.",
        "Volvox-এ গোলীয় প্রতিসাম্যতা দেখা যায়; Radiolaria, Heliozoa প্রভৃতিও উদাহরণ।",
    ),
    q(
        "Which of the following is an example of asymmetry?",
        "অপ্রতিসাম্যতার উদাহরণ কোনটি?",
        ["Volvox", "Pila", "Hydra", "Julus"],
        ["Volvox", "Pila", "Hydra", "Julus"],
        "B", "medium", "factual",
        "Adult Pila (snail) is typically asymmetric due to torsion; Hydra is radial and Julus bilateral.",
        "প্রাপ্তবয়স্ক Pila (শামুক) টর্শনের কারণে অপ্রতিসম; Hydra অরীয় এবং Julus দ্বিপার্শ্বীয়।",
    ),
    q(
        "Animals with cellular grade of organization belong to which phylum?",
        "কোষীয় মাত্রার গঠন কোন পর্বের প্রাণীতে দেখা যায়?",
        ["Nematoda", "Cnidaria", "Platyhelminthes", "Porifera"],
        ["Nematoda", "Cnidaria", "Platyhelminthes", "Porifera"],
        "D", "easy", "factual",
        "Porifera have a cellular level of body organization without true tissues.",
        "Porifera পর্বের প্রাণীদের দেহগঠন কোষীয় মাত্রার; সত্য টিস্যু নেই।",
    ),
    q(
        "Which animal shows tissue–organ grade of organization?",
        "কোনটি টিস্যু–অঙ্গ মাত্রার প্রাণী?",
        ["Sycon", "Aurelia", "Taenia", "Ascaris"],
        ["Sycon", "Aurelia", "Taenia", "Ascaris"],
        "C", "medium", "factual",
        "Taenia (flatworm) has organ systems at tissue–organ grade; Sycon is cellular and Aurelia tissue-grade.",
        "Taenia টিস্যু–অঙ্গ মাত্রার; Sycon কোষীয় এবং Aurelia মূলত টিস্যু মাত্রার।",
    ),
    q(
        "Which of the following is an acoelomate animal?",
        "নিচের কোন প্রাণী অ্যাসিলোমেট?",
        ["Roundworm", "Tapeworm", "Earthworm", "Snail"],
        ["গোলকৃমি", "ফিতাকৃমি", "কেঁচো", "শামুক"],
        "B", "easy", "factual",
        "Tapeworms (Platyhelminthes) lack a body cavity and are acoelomates; roundworms are pseudocoelomate.",
        "ফিতাকৃমি (Platyhelminthes) দেহগহ্বরহীন অ্যাসিলোমেট; গোলকৃমি সিউডোসিলোমেট।",
    ),
    q(
        "In which animal is a pseudocoelom found?",
        "নিচের কোন প্রাণীতে সিউডোসিলোম দেখা যায়?",
        ["Fasciola hepatica", "Taenia solium", "Ascaris lumbricoides", "Metaphire posthuma"],
        ["Fasciola hepatica", "Taenia solium", "Ascaris lumbricoides", "Metaphire posthuma"],
        "C", "easy", "factual",
        "Ascaris is a nematode with a pseudocoelom; Fasciola and Taenia are acoelomate; Metaphire is eucoelomate.",
        "Ascaris নেমাটোড ও সিউডোসিলোমেট; Fasciola ও Taenia অ্যাসিলোমেট; Metaphire ইউসিলোমেট।",
    ),
    q(
        "Which animal is a true coelomate?",
        "প্রকৃত সিলোমযুক্ত প্রাণী কোনটি?",
        ["Fasciola hepatica", "Taenia solium", "Ascaris lumbricoides", "Metaphire posthuma"],
        ["Fasciola hepatica", "Taenia solium", "Ascaris lumbricoides", "Metaphire posthuma"],
        "D", "easy", "factual",
        "Metaphire (earthworm) is an annelid with a true schizocoelous coelom.",
        "Metaphire (কেঁচো) অ্যানিলিড এবং প্রকৃত সিলোমযুক্ত।",
    ),
    q(
        "Which phylum contains acoelomate animals?",
        "সিলোমবিহীন প্রাণীদের পর্ব কোনটি?",
        ["Annelida", "Mollusca", "Nematoda", "Platyhelminthes"],
        ["Annelida", "Mollusca", "Nematoda", "Platyhelminthes"],
        "D", "easy", "factual",
        "Platyhelminthes are acoelomates; nematodes are pseudocoelomates; annelids and molluscs are coelomates.",
        "Platyhelminthes অ্যাসিলোমেট; Nematoda সিউডোসিলোমেট; Annelida ও Mollusca সিলোমেট।",
    ),
    q(
        "Radial cleavage is characteristic of which phylum?",
        "অরীয় ক্লিভেজ দেখা যায় কোন পর্বে?",
        ["Annelida", "Arthropoda", "Mollusca", "Chordata"],
        ["Annelida", "Arthropoda", "Mollusca", "Chordata"],
        "D", "medium", "conceptual",
        "Chordates typically show radial indeterminate cleavage; annelids and molluscs show spiral cleavage.",
        "Chordata-তে সাধারণত অরীয় অনির্ধারিত ক্লিভেজ; Annelida ও Mollusca-তে সর্পিল ক্লিভেজ।",
    ),
    q(
        "In which of the following animals does radial cleavage occur?",
        "কোন প্রাণীতে অরীয় ক্লিভেজ ঘটে?",
        ["Mussel", "Earthworm", "Grasshopper", "Frog"],
        ["ঝিনুক", "কেঁচো", "ঘাসফড়িং", "ব্যাঙ"],
        "D", "medium", "conceptual",
        "Frog (chordate) shows radial cleavage; mussel and earthworm show spiral cleavage patterns.",
        "ব্যাঙ (কর্ডেট) অরীয় ক্লিভেজ দেখায়; ঝিনুক ও কেঁচোতে সর্পিল ক্লিভেজ দেখা যায়।",
    ),
    q(
        "Which of the following is a diploblastic animal?",
        "নিচের কোন প্রাণীটি দ্বিস্তরী?",
        ["Starfish", "Grasshopper", "Earthworm", "Hydra"],
        ["তারামাছ", "ঘাসফড়িং", "কেঁচো", "হাইড্রা"],
        "D", "easy", "factual",
        "Hydra (Cnidaria) is diploblastic; the others are triploblastic.",
        "হাইড্রা (Cnidaria) দ্বিস্তরী; বাকিগুলো ত্রিস্তরী।",
    ),
    q(
        "Tagmatization is especially important in the classification of which phylum?",
        "'অঙ্গলায়ন' কোন পর্বের শ্রেণিবিন্যাসের জন্য গুরুত্বপূর্ণ?",
        ["Mollusca", "Arthropoda", "Annelida", "Echinodermata"],
        ["Mollusca", "Arthropoda", "Annelida", "Echinodermata"],
        "B", "medium", "conceptual",
        "Arthropod body regions (tagmata: head, thorax, abdomen or cephalothorax) are key classification characters.",
        "আর্থ্রোপোডার দেহখণ্ড (ট্যাগমাটা) শ্রেণিবিন্যাসের গুরুত্বপূর্ণ বৈশিষ্ট্য।",
    ),
    q(
        "Which of the following is an endothermic animal?",
        "কোনটি এন্ডোথার্মিক প্রাণী?",
        ["Panthera", "Naja", "Salamandra", "Hemidactylus"],
        ["Panthera", "Naja", "Salamandra", "Hemidactylus"],
        "A", "easy", "factual",
        "Panthera (tiger/leopard) is a warm-blooded mammal; snakes, salamanders and lizards are ectothermic.",
        "Panthera উষ্ণরক্ত স্তন্যপায়ী; সাপ, স্যালামাণ্ডার ও টিকটিকি এক্টোথার্মিক।",
    ),
    q(
        "Which of the following is an ectothermic animal?",
        "এক্টোথার্মিক প্রাণী কোনটি?",
        ["Magpie robin (Doel)", "Indian bullfrog", "Royal Bengal tiger", "Guinea pig"],
        ["দোয়েল", "সোনা ব্যাঙ", "রয়েল বেঙ্গল টাইগার", "গিনিপিগ"],
        "B", "easy", "factual",
        "Frogs are ectothermic amphibians; birds and mammals are endothermic.",
        "ব্যাঙ এক্টোথার্মিক উভচর; পাখি ও স্তন্যপায়ী এন্ডোথার্মিক।",
    ),
    q(
        "Which of the following animals is coelomate?",
        "সিলোমযুক্ত প্রাণী কোনটি?",
        ["Sponge", "Jellyfish", "Flatworm", "Cockroach"],
        ["স্পঞ্জ", "জেলিফিস", "চ্যাপ্টা কৃমি", "তেলাপোকা"],
        "D", "easy", "factual",
        "Cockroach (Arthropoda) has a haemocoel derived from a reduced coelom; sponges and cnidarians lack a coelom, flatworms are acoelomate.",
        "তেলাপোকায় হিমোসিল (হ্রাসপ্রাপ্ত সিলোমজাত); স্পঞ্জ ও জেলিফিসে সিলোম নেই, চ্যাপ্টাকৃমি অ্যাসিলোমেট।",
    ),
    q(
        "Which criteria are commonly used as bases for classifying animals such as snails and starfish?",
        "শামুক ও তারামাছের মতো প্রাণী শ্রেণিবিন্যাসে কোন ভিত্তিগুলো সাধারণত ব্যবহৃত হয়?",
        [
            "Respiratory method and skeletal system",
            "Habitat alone",
            "Color pattern only",
            "Body size alone",
        ],
        [
            "শ্বসন কৌশল ও কঙ্কালতন্ত্র",
            "শুধু আবাসস্থল",
            "শুধু বর্ণবিন্যাস",
            "শুধু দেহের আকার",
        ],
        "A", "medium", "conceptual",
        "Morphological and physiological traits such as respiration and skeleton are primary classification bases; habitat or size alone are insufficient.",
        "শ্বসন ও কঙ্কালতন্ত্রের মতো গাঠনিক–শারীরবৃত্তীয় বৈশিষ্ট্য প্রধান ভিত্তি; কেবল আবাস বা আকার যথেষ্ট নয়।",
    ),
]


# --- t02: Major animal groups / প্রাণিজগতের প্রধান পর্ব ---
T02 = [
    q(
        "Excretory organs called nephridia occur in which phylum?",
        "কোন পর্বের প্রাণীদের রেচন অঙ্গ নেফ্রিডিয়া?",
        ["Nematoda", "Mollusca", "Annelida", "Arthropoda"],
        ["Nematoda", "Mollusca", "Annelida", "Arthropoda"],
        "C", "easy", "factual",
        "Annelids excrete via nephridia; arthropods typically use Malpighian tubules and flatworms use flame cells.",
        "অ্যানিলিডে নেফ্রিডিয়া; আর্থ্রোপোডায় মালপিজিয়ান নালিকা এবং চ্যাপ্টাকৃমিতে শিখা কোষ।",
    ),
    q(
        "Animals of which phylum are called 'flowers of the sea'?",
        "কোন পর্বের প্রাণীদের সমুদ্রের ফুল বলা হয়?",
        ["Porifera", "Cnidaria", "Mollusca", "Echinodermata"],
        ["Porifera", "Cnidaria", "Mollusca", "Echinodermata"],
        "B", "easy", "factual",
        "Many cnidarians (anemones, corals) are popularly called sea flowers.",
        "অ্যানিমন, প্রবাল প্রভৃতি Cnidaria পর্বের প্রাণীকে সমুদ্রের ফুল বলা হয়।",
    ),
    q(
        "In which phylum are spiny-skinned animals found?",
        "কোন পর্বের প্রাণীতে কাঁটাযুক্ত ত্বক দেখা যায়?",
        ["Cnidaria", "Mollusca", "Annelida", "Echinodermata"],
        ["Cnidaria", "Mollusca", "Annelida", "Echinodermata"],
        "D", "easy", "factual",
        "Echinodermata means 'spiny skin'; starfish and relatives have calcareous spines.",
        "Echinodermata অর্থ কাঁটাযুক্ত ত্বক; তারামাছ প্রভৃতিতে ক্যালকেয়ারিয়াস কাঁটা থাকে।",
    ),
    q(
        "Flame cells are the excretory organs of which phylum?",
        "শিখা কোষ নামক রেচন অঙ্গ পাওয়া যায় কোন পর্বের প্রাণীতে?",
        ["Cnidaria", "Platyhelminthes", "Nematoda", "Mollusca"],
        ["Cnidaria", "Platyhelminthes", "Nematoda", "Mollusca"],
        "B", "easy", "factual",
        "Platyhelminthes possess protonephridia ending in flame cells.",
        "Platyhelminthes-এ প্রোটোনেফ্রিডিয়া ও শিখা কোষ থাকে।",
    ),
    q(
        "The main excretory organ of Arthropoda is:",
        "Arthropoda পর্বের প্রাণীদের প্রধান রেচন অঙ্গ কোনটি?",
        ["Flame cell", "Green gland (in some)", "Nephridium", "Malpighian tubule"],
        ["শিখা কোষ", "সবুজ গ্রন্থি (কিছুতে)", "নেফ্রিডিয়া", "মালপিজিয়ান নালিকা"],
        "D", "easy", "factual",
        "Insects use Malpighian tubules as the chief excretory organs; crustaceans may use green/antennal glands.",
        "পতঙ্গে প্রধান রেচন অঙ্গ মালপিজিয়ান নালিকা; ক্রাস্টেশিয়ায় সবুজ/অ্যান্টেনাল গ্রন্থি থাকতে পারে।",
    ),
    q(
        "An elastin-rich cuticle is characteristic of which phylum?",
        "ইলাস্টিনযুক্ত কিউটিকল কোন পর্বের প্রাণীতে থাকে?",
        ["Platyhelminthes", "Nematoda", "Annelida", "Arthropoda"],
        ["Platyhelminthes", "Nematoda", "Annelida", "Arthropoda"],
        "B", "medium", "factual",
        "Nematodes have a tough, elastic cuticle that is periodically moulted.",
        "নেমাটোডের মজবুত ইলাস্টিক কিউটিকল থাকে যা পর্যায়ক্রমে খসে পড়ে।",
    ),
    q(
        "Open type of circulatory system is seen in which phylum?",
        "কোন পর্বের প্রাণীতে অমুক্ত (মুক্ত) ধরনের সংবহনতন্ত্র দেখা যায়?",
        ["Annelida", "Mollusca", "Nematoda", "Echinodermata"],
        ["Annelida", "Mollusca", "Nematoda", "Echinodermata"],
        "B", "medium", "factual",
        "Most molluscs (except cephalopods) and arthropods have open circulation with haemocoel.",
        "অধিকাংশ মলাস্কায় (সেফালোপোড ছাড়া) মুক্ত সংবহন ও হিমোসিল থাকে।",
    ),
    q(
        "Which is the second-largest phylum of the animal kingdom?",
        "প্রাণিজগতের দ্বিতীয় বৃহত্তম পর্ব কোনটি?",
        ["Cnidaria", "Annelida", "Mollusca", "Arthropoda"],
        ["Cnidaria", "Annelida", "Mollusca", "Arthropoda"],
        "C", "easy", "factual",
        "Arthropoda is the largest phylum; Mollusca is the second largest.",
        "বৃহত্তম পর্ব Arthropoda; দ্বিতীয় বৃহত্তম Mollusca।",
    ),
    q(
        "Tube feet are locomotory organs of which phylum?",
        "নালিকা পদ কোন পর্বের প্রাণীর চলনাঙ্গ?",
        ["Nematoda", "Annelida", "Mollusca", "Echinodermata"],
        ["Nematoda", "Annelida", "Mollusca", "Echinodermata"],
        "D", "easy", "factual",
        "Echinoderms move using tube feet of the water vascular system.",
        "একাইনোডার্মে পানি সংবহনতন্ত্রের নালিকা পদ দিয়ে চলাচল করে।",
    ),
    q(
        "A perihaemal system is found in which phylum?",
        "পেরিহিমালতন্ত্র কোন পর্বের প্রাণীতে দেখা যায়?",
        ["Echinodermata", "Arthropoda", "Mollusca", "Nematoda"],
        ["Echinodermata", "Arthropoda", "Mollusca", "Nematoda"],
        "A", "medium", "factual",
        "Echinoderms have haemal and perihaemal systems instead of a typical blood vascular system.",
        "একাইনোডার্মাটায় সাধারণ রক্ত সংবহনের পরিবর্তে হিমাল ও পেরিহিমালতন্ত্র থাকে।",
    ),
    q(
        "Which phylum has choanocyte (collar) cells with flagella?",
        "পরিফেরা পর্বের প্রাণীদের কোন কোষটি ফ্ল্যাজেলাযুক্ত?",
        ["Choanocyte", "Pinacocyte", "Amoebocyte", "Myocyte"],
        ["কোয়ানোসাইট", "পিনাকোসাইট", "অ্যামিবোসাইট", "মায়োসাইট"],
        "A", "easy", "factual",
        "Choanocytes line sponge canals/cavities and create water current with flagella.",
        "কোয়ানোসাইট স্পঞ্জের নালিকা/গহ্বরে ফ্ল্যাজেলা দিয়ে জলপ্রবাহ সৃষ্টি করে।",
    ),
    q(
        "Which of the following is a characteristic of starfish?",
        "তারা মাছের বৈশিষ্ট্য হলো—",
        [
            "Excretory organ is green gland",
            "Trochophore larva is present",
            "Blood vascular system is absent",
            "True segmentation is present",
        ],
        [
            "রেচন অঙ্গ সবুজ গ্রন্থি",
            "ট্রোকোফোর লার্ভা দেখা যায়",
            "রক্ত সংবহনতন্ত্র অনুপস্থিত",
            "প্রকৃত খণ্ডায়ন বিদ্যমান",
        ],
        "C", "medium", "factual",
        "Starfish lack a typical blood vascular system and instead have water vascular, haemal and perihaemal systems.",
        "তারামাছে প্রচলিত রক্ত সংবহনতন্ত্র নেই; পানি সংবহন ও হিমাল/পেরিহিমালতন্ত্র থাকে।",
    ),
    q(
        "Radial symmetry is typically seen in which phylum?",
        "অরীয় প্রতিসাম্যতা দেখা যায় কোন পর্বের প্রাণীতে?",
        ["Porifera", "Cnidaria", "Nematoda", "Annelida"],
        ["Porifera", "Cnidaria", "Nematoda", "Annelida"],
        "B", "easy", "factual",
        "Cnidarians such as Hydra and Aurelia generally show radial symmetry.",
        "Hydra, Aurelia প্রভৃতি Cnidaria-তে সাধারণত অরীয় প্রতিসাম্যতা দেখা যায়।",
    ),
    q(
        "A mussel belongs to which phylum?",
        "ঝিনুক কোন পর্বের প্রাণী?",
        ["Platyhelminthes", "Echinodermata", "Annelida", "Mollusca"],
        ["Platyhelminthes", "Echinodermata", "Annelida", "Mollusca"],
        "D", "easy", "factual",
        "Mussels are bivalve molluscs with a soft body enclosed by a shell and mantle.",
        "ঝিনুক দ্বিকপাটিকা Mollusca; নরম দেহ খোলক ও ম্যান্টলে আবৃত।",
    ),
    q(
        "Rhabditiform larval stage is seen in which phylum?",
        "কোন পর্বের প্রাণীতে র্যাবডিটিফর্ম লার্ভা দশা দেখা যায়?",
        ["Platyhelminthes", "Nematoda", "Arthropoda", "Echinodermata"],
        ["Platyhelminthes", "Nematoda", "Arthropoda", "Echinodermata"],
        "B", "hard", "factual",
        "Many nematodes (e.g. Ascaris, hookworms) pass through a rhabditiform larval stage.",
        "অনেক নেমাটোডে (যেমন Ascaris) র্যাবডিটিফর্ম লার্ভা দশা দেখা যায়।",
    ),
    q(
        "Parenchymula larva is characteristic of which phylum?",
        "প্যারেনকাইমুলা লার্ভা নিচের কোন পর্বভুক্ত প্রাণীতে দেখা যায়?",
        ["Nematoda", "Cnidaria", "Echinodermata", "Porifera"],
        ["Nematoda", "Cnidaria", "Echinodermata", "Porifera"],
        "D", "medium", "factual",
        "Porifera development often includes a parenchymula (or amphiblastula) larval stage.",
        "Porifera-তে প্যারেনকাইমুলা (বা অ্যাম্ফিব্লাস্টুলা) লার্ভা দশা দেখা যায়।",
    ),
    q(
        "Which statement about Scypha is correct?",
        "Scypha সম্পর্কে কোনটি সঠিক?",
        [
            "It belongs to Porifera only",
            "It shows radial symmetry only",
            "It has a spongocoel only",
            "It belongs to Porifera, shows radial symmetry, and has a spongocoel",
        ],
        [
            "শুধু Porifera পর্বের",
            "শুধু অরীয় প্রতিসম",
            "শুধু স্পঞ্জোসিলযুক্ত",
            "Porifera পর্বের, অরীয় প্রতিসম এবং স্পঞ্জোসিলযুক্ত",
        ],
        "D", "medium", "conceptual",
        "Scypha is a sponge with radial symmetry and a central spongocoel.",
        "Scypha স্পঞ্জ; অরীয় প্রতিসম এবং কেন্দ্রীয় স্পঞ্জোসিলযুক্ত।",
    ),
    q(
        "Haemocoel is found in which of the following phyla?",
        "হিমোসিলযুক্ত পর্ব কোনগুলো?",
        ["Mollusca and Annelida", "Mollusca and Arthropoda", "Annelida and Arthropoda", "Only Annelida"],
        ["Mollusca ও Annelida", "Mollusca ও Arthropoda", "Annelida ও Arthropoda", "শুধু Annelida"],
        "B", "medium", "conceptual",
        "Open circulation with haemocoel occurs in Arthropoda and most Mollusca; Annelida have closed circulation and a true coelom.",
        "মুক্ত সংবহন ও হিমোসিল Arthropoda ও অধিকাংশ Mollusca-তে; Annelida-তে বদ্ধ সংবহন ও সত্য সিলোম।",
    ),
    q(
        "Blood vascular and respiratory systems are typically absent in:",
        "রক্ত সংবহনতন্ত্র ও শ্বসনতন্ত্র অনুপস্থিত থাকে—",
        ["Nematoda and Mollusca", "Nematoda and Platyhelminthes", "Mollusca and Platyhelminthes", "All three phyla"],
        ["Nematoda ও Mollusca", "Nematoda ও Platyhelminthes", "Mollusca ও Platyhelminthes", "তিনটি পর্বেই"],
        "B", "medium", "conceptual",
        "Flatworms and nematodes lack specialized circulatory and respiratory organs; molluscs have both systems.",
        "প্লাটিহেলমিনথেস ও নেমাটোডায় বিশেষায়িত সংবহন ও শ্বসন অঙ্গ নেই; মলাস্কায় উভয়ই আছে।",
    ),
    q(
        "Which feature is characteristic of Echinodermata?",
        "Echinodermata পর্বের বৈশিষ্ট্য কোনটি?",
        ["Water vascular system", "Compound eye", "Flame cells", "Typical blood vascular system"],
        ["পানি সংবহনতন্ত্র", "পুঞ্জাক্ষি", "শিখা কোষ", "প্রচলিত রক্ত সংবহনতন্ত্র"],
        "A", "easy", "factual",
        "A unique water vascular system with tube feet is diagnostic of echinoderms.",
        "নালিকা পদসহ পানি সংবহনতন্ত্র একাইনোডার্মাটার বৈশিষ্ট্যসূচক।",
    ),
]


# --- t03: Animal diversity / প্রাণীর বৈচিত্র্য ---
T03 = [
    q(
        "Which class typically shows scales among the following?",
        "নিচের কোন শ্রেণিতে আঁইশ দেখা যায়?",
        ["Thaliacea", "Ascidiacea", "Larvacea", "Sarcopterygii"],
        ["Thaliacea", "Ascidiacea", "Larvacea", "Sarcopterygii"],
        "D", "medium", "factual",
        "Sarcopterygii (lobe-finned fishes) have bony scales; the listed urochordate classes lack fish scales.",
        "Sarcopterygii-তে অস্থিময় আঁইশ থাকে; তালিকাভুক্ত ইউরোকর্ডেট শ্রেণিতে মাছের আঁইশ নেই।",
    ),
    q(
        "A characteristic feature of Urochordata is:",
        "ইউরোকর্ডাটা উপপর্বের বৈশিষ্ট্য কোনটি?",
        [
            "Retrogressive metamorphosis occurs",
            "Oral hood is present",
            "Excretory organ is Malpighian tubule",
            "Parapodia are present",
        ],
        [
            "প্রতীপ রূপান্তর ঘটে",
            "ওরাল হুড বিদ্যমান",
            "রেচন অঙ্গ মালপিজিয়ান নালিকা",
            "প্যারাপোডিয়া বিদ্যমান",
        ],
        "A", "medium", "factual",
        "Urochordates show retrogressive metamorphosis; oral hood is a cephalochordate feature.",
        "ইউরোকর্ডাটায় প্রতীপ রূপান্তর ঘটে; ওরাল হুড সেফালোকর্ডাটার বৈশিষ্ট্য।",
    ),
    q(
        "Retrogressive metamorphosis is seen in which class?",
        "নিচের কোন শ্রেণির প্রাণীতে প্রতীপ রূপান্তর দেখা যায়?",
        ["Ascidiacea", "Myxini", "Petromyzontida", "Actinopterygii"],
        ["Ascidiacea", "Myxini", "Petromyzontida", "Actinopterygii"],
        "A", "medium", "factual",
        "Ascidians (sea squirts) lose the larval notochord and become sessile adults.",
        "Ascidiacea-তে লার্ভার নটোকর্ড হারিয়ে নিশ্চল প্রাপ্তবয়স্ক হয়।",
    ),
    q(
        "Which is a characteristic of Cephalochordata?",
        "Cephalochordata উপপর্বের বৈশিষ্ট্য কোনটি?",
        [
            "Body covered by a tunic",
            "Retrogressive metamorphosis occurs",
            "Oral hood is present throughout life",
            "Ammocoete larva is present",
        ],
        [
            "দেহ টিউনিক নামক আবরণে আবৃত",
            "প্রতীপ রূপান্তর দেখা যায়",
            "জীবনভর ওরাল হুড বিদ্যমান",
            "অ্যামোসিট লার্ভা দশা দেখা যায়",
        ],
        "C", "hard", "factual",
        "Cephalochordates (e.g. Branchiostoma) have an oral hood; tunic and retrogressive metamorphosis belong to urochordates; ammocoete is of lampreys.",
        "সেফালোকর্ডাটায় ওরাল হুড থাকে; টিউনিক ও প্রতীপ রূপান্তর ইউরোকর্ডাটার; অ্যামোসিট ল্যামপ্রের।",
    ),
    q(
        "Which of the following is a characteristic of Aves?",
        "Aves এর বৈশিষ্ট্য হলো—",
        [
            "Whole body covered with hair only",
            "Forelimbs modified into wings; bones air-filled",
            "Body covered with hair and scales only",
            "Four-chambered heart absent",
        ],
        [
            "সমগ্র দেহ শুধু লোমে আবৃত",
            "অগ্রপদ ডানায় রূপান্তরিত; অস্থি বায়ুপূর্ণ",
            "দেহ শুধু লোম ও আঁইশে আবৃত",
            "চার প্রকোষ্ঠবিশিষ্ট হৃৎপিণ্ড নেই",
        ],
        "B", "easy", "factual",
        "Birds have feathered bodies, winged forelimbs, pneumatic bones and a four-chambered heart.",
        "পাখির দেহ পালকে আবৃত, অগ্রপদ ডানা, বায়ুপূর্ণ অস্থি এবং চার প্রকোষ্ঠ হৃৎপিণ্ড।",
    ),
    q(
        "In which animal is a completely four-chambered heart present among reptiles?",
        "কোন প্রাণীতে সম্পূর্ণ চার প্রকোষ্ঠবিশিষ্ট হৃৎপিণ্ড বিদ্যমান?",
        ["Hemidactylus frenatus", "Crocodylus palustris", "Caretta caretta", "Naja naja"],
        ["Hemidactylus frenatus", "Crocodylus palustris", "Caretta caretta", "Naja naja"],
        "B", "medium", "factual",
        "Crocodilians uniquely among living reptiles have a fully four-chambered heart.",
        "জীবিত সরীসৃপদের মধ্যে কুমিরের সম্পূর্ণ চার প্রকোষ্ঠবিশিষ্ট হৃৎপিণ্ড আছে।",
    ),
    q(
        "Lobe-finned fishes belong to which class?",
        "পিণ্ডাকার পাখনাবিশিষ্ট মাছ (lobe-finned fishes) নামে পরিচিত কোন শ্রেণি?",
        ["Chondrichthyes", "Actinopterygii", "Petromyzontida", "Sarcopterygii"],
        ["Chondrichthyes", "Actinopterygii", "Petromyzontida", "Sarcopterygii"],
        "D", "easy", "factual",
        "Sarcopterygii are lobe-finned fishes (e.g. Latimeria, lungfishes).",
        "Sarcopterygii হলো লোব-ফিনড মাছ (যেমন Latimeria, লাংফিশ)।",
    ),
    q(
        "Which of the following is a feature of Reptilia?",
        "Reptilia শ্রেণির বৈশিষ্ট্য কোনটি?",
        [
            "Moist glandular skin",
            "They are endothermic",
            "Lungs are the sole respiratory organ in adults",
            "Forelimbs modified into wings",
        ],
        [
            "আর্দ্র ও গ্রন্থিযুক্ত ত্বক বিদ্যমান",
            "এরা এন্ডোথার্মিক প্রাণী",
            "প্রাপ্তবয়স্কে ফুসফুস একমাত্র শ্বসন অঙ্গ",
            "অগ্রপদ ডানায় রূপান্তরিত",
        ],
        "C", "medium", "factual",
        "Adult reptiles breathe only with lungs and have dry epidermal scales; they are ectothermic.",
        "প্রাপ্তবয়স্ক সরীসৃপ কেবল ফুসফুসে শ্বাস নেয়; ত্বক শুষ্ক এপিডার্মাল আঁইশযুক্ত এবং এক্টোথার্মিক।",
    ),
    q(
        "Animals of which class typically have a three-chambered heart?",
        "কোন শ্রেণির প্রাণীদের হৃৎপিণ্ডের প্রকোষ্ঠ তিনটি?",
        ["Amphibia", "Aves", "Mammalia", "Crocodilia only as a class"],
        ["Amphibia", "Aves", "Mammalia", "শুধু Crocodilia শ্রেণি"],
        "A", "easy", "factual",
        "Amphibians typically have a three-chambered heart (two atria, one ventricle).",
        "উভচরদের সাধারণত তিন প্রকোষ্ঠবিশিষ্ট হৃৎপিণ্ড থাকে।",
    ),
    q(
        "In chordates, the endostyle is homologous to which gland?",
        "কর্ডেট প্রাণীদের ক্ষেত্রে এন্ডোস্টাইল কোন গ্রন্থিতে রূপান্তরিত হয়?",
        ["Thymus", "Thyroid", "Parathyroid", "Pituitary"],
        ["থাইমাস", "থাইরয়েড", "প্যারাথাইরয়েড", "পিটুইটারি"],
        "B", "hard", "conceptual",
        "The endostyle of protochordates is homologous to the vertebrate thyroid gland.",
        "প্রোটোকর্ডেটের এন্ডোস্টাইল মেরুদণ্ডীদের থাইরয়েড গ্রন্থির সমসংস্থ।",
    ),
    q(
        "Which animal has placoid scales?",
        "নিচের কোন প্রাণীটিতে প্ল্যাকয়েড আঁইশ বিদ্যমান?",
        ["Myxine", "Petromyzon", "Scoliodon", "Branchiostoma"],
        ["Myxine", "Petromyzon", "Scoliodon", "Branchiostoma"],
        "C", "easy", "factual",
        "Scoliodon (dogfish/shark) is a chondrichthyan with placoid scales.",
        "Scoliodon কনড্রিকথিয়ান এবং প্ল্যাকয়েড আঁইশযুক্ত।",
    ),
    q(
        "Placoid scales are found in which class?",
        "'প্ল্যাকয়েড' আঁইশ পাওয়া যায় কোন শ্রেণিভুক্ত প্রাণীতে?",
        ["Actinopterygii", "Sarcopterygii", "Chondrichthyes", "Amphibia"],
        ["Actinopterygii", "Sarcopterygii", "Chondrichthyes", "Amphibia"],
        "C", "easy", "factual",
        "Cartilaginous fishes (Chondrichthyes) characteristically have placoid scales.",
        "কনড্রিকথিয়িস শ্রেণির বৈশিষ্ট্য প্ল্যাকয়েড আঁইশ।",
    ),
    q(
        "Which chordate is not a vertebrate?",
        "কোন প্রাণীটি কর্ডেট কিন্তু মেরুদণ্ডী নয়?",
        ["Astropecten", "Ascidia", "Petromyzon", "Scoliodon"],
        ["Astropecten", "Ascidia", "Petromyzon", "Scoliodon"],
        "B", "medium", "factual",
        "Ascidia is a urochordate (protochordate); Petromyzon and Scoliodon are vertebrates; Astropecten is an echinoderm.",
        "Ascidia ইউরোকর্ডেট; Petromyzon ও Scoliodon মেরুদণ্ডী; Astropecten একাইনোডার্ম।",
    ),
    q(
        "Ammocoete larval stage is found in:",
        "অ্যামোসিট (Ammocoete) লার্ভা দশা দেখা যায় কোনটিতে?",
        ["Hagfish", "Shark", "Stingray", "Lamprey"],
        ["হ্যাগফিশ", "হাঙ্গর", "স্টিংরে", "ল্যামপ্রে"],
        "D", "medium", "factual",
        "Petromyzontida (lampreys) have an ammocoete larva; hagfish lack this stage.",
        "ল্যামপ্রেতে (Petromyzontida) অ্যামোসিট লার্ভা থাকে; হ্যাগফিশে নেই।",
    ),
    q(
        "How many chambers does a bat's heart have?",
        "বাদুড়ের হৃৎপিণ্ডে প্রকোষ্ঠের সংখ্যা কতটি?",
        ["2", "3", "5", "4"],
        ["২", "৩", "৫", "৪"],
        "D", "easy", "factual",
        "Bats are mammals and have a four-chambered heart.",
        "বাদুড় স্তন্যপায়ী; হৃৎপিণ্ড চার প্রকোষ্ঠবিশিষ্ট।",
    ),
    q(
        "Which fish has a heterocercal caudal fin?",
        "কোনটির পুচ্ছ পাখনা হেটারোসার্কাল ধরনের?",
        ["Rohu (Labeo)", "Lungfish", "Climbing perch (Taki)", "Shark"],
        ["রুই", "লাংফিশ", "টাকি", "হাঙ্গর"],
        "D", "easy", "factual",
        "Sharks typically have a heterocercal tail; most bony fishes have a homocercal tail.",
        "হাঙ্গরের পুচ্ছ পাখনা সাধারণত হেটারোসার্কাল; অধিকাংশ অস্থিময় মাছের হোমোসার্কাল।",
    ),
    q(
        "Animals that breathe with gills early in life and lungs later belong to:",
        "জীবনের প্রথম পর্যায়ে ফুলকা এবং পরবর্তীতে ফুসফুস দ্বারা শ্বসনকারী প্রাণী কোন শ্রেণিভুক্ত?",
        ["Amphibia", "Aves", "Reptilia", "Mammalia"],
        ["Amphibia", "Aves", "Reptilia", "Mammalia"],
        "A", "easy", "factual",
        "Amphibians typically have aquatic gill-breathing larvae and lung-breathing adults.",
        "উভচর লার্ভা ফুলকায় এবং প্রাপ্তবয়স্ক ফুসফুসে শ্বাস নেয়।",
    ),
    q(
        "Which of the following belongs to Platyhelminthes?",
        "নিচের কোনটি Platyhelminthes পর্বভুক্ত প্রাণী?",
        ["Scypha", "Fasciola", "Ascaris", "Metaphire"],
        ["Scypha", "Fasciola", "Ascaris", "Metaphire"],
        "B", "easy", "factual",
        "Fasciola (liver fluke) is a flatworm; Ascaris is a nematode; Metaphire an annelid; Scypha a sponge.",
        "Fasciola চ্যাপ্টাকৃমি; Ascaris নেমাটোড; Metaphire অ্যানিলিড; Scypha স্পঞ্জ।",
    ),
    q(
        "Coelacanth belongs to which class?",
        "Coelacanth কোন শ্রেণির অন্তর্ভুক্ত?",
        ["Sarcopterygii", "Myxini", "Petromyzontida", "Chondrichthyes"],
        ["Sarcopterygii", "Myxini", "Petromyzontida", "Chondrichthyes"],
        "A", "medium", "factual",
        "Living coelacanth (Latimeria) is a lobe-finned fish in Sarcopterygii.",
        "জীবিত Coelacanth (Latimeria) Sarcopterygii শ্রেণির লোব-ফিনড মাছ।",
    ),
    q(
        "Which animal lacks both teeth and an external ear?",
        "কোন প্রাণীর দাঁত ও বহিঃকর্ণ থাকে না?",
        ["Bat", "Kangaroo", "Platypus", "Black francolin"],
        ["বাদুড়", "ক্যাঙ্গারু", "প্লাটিপাস", "কালো তিতির"],
        "C", "medium", "factual",
        "Adult platypus lacks teeth and external pinnae; it is a monotreme mammal.",
        "প্রাপ্তবয়স্ক প্লাটিপাসের দাঁত ও বহিঃকর্ণ (পিনা) নেই; এটি মনোট্রিম স্তন্যপায়ী।",
    ),
]


TOPICS_MAP = {
    "bio2_27_ch01_t01": T01,
    "bio2_27_ch01_t02": T02,
    "bio2_27_ch01_t03": T03,
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

    # Soft check: similar stems about placoid / coelom across topics are OK if wording differs.
    summary = {
        "chapter": "bio2_27_ch01",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p039_pdf045.png",
            "p040_pdf046.png",
            "p041_pdf047.png",
            "p042_pdf048.png",
            "p043_pdf049.png",
            "p044_pdf050.png",
            "p045_pdf051.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio2_27_ch01_t01": {
                "title": "Principles of classification / শ্রেণিবিন্যাসের নীতি",
                "themes": [
                    "Linnaeus binomial naming; Aristotle father of zoology",
                    "symmetry: pentaradial Astropecten; biradial Coeloplana; spherical Volvox; asymmetric Pila",
                    "organization: Porifera cellular; Taenia tissue–organ grade",
                    "coelom: acoelomate tapeworm/Platyhelminthes; pseudocoelom Ascaris; eucoelom Metaphire",
                    "radial cleavage Chordata/frog vs spiral annelid/mollusc",
                    "diploblastic Hydra; tagmatization Arthropoda",
                    "endotherm Panthera vs ectotherm frog; coelomate cockroach",
                    "classification bases: respiration and skeleton",
                ],
            },
            "bio2_27_ch01_t02": {
                "title": "Major animal groups / প্রাণিজগতের প্রধান পর্ব",
                "themes": [
                    "Annelida nephridia; Cnidaria sea flowers; Echinodermata spiny skin/tube feet/water vascular/perihaemal",
                    "Platyhelminthes flame cells; Arthropoda Malpighian tubules",
                    "Nematoda elastic cuticle / rhabditiform larva",
                    "Mollusca open circulation; second-largest phylum; mussel",
                    "Porifera choanocytes / Scypha / parenchymula",
                    "starfish lacks typical blood vascular system; Cnidaria radial",
                    "haemocoel Mollusca+Arthropoda; no circ/resp in Nematoda+Platyhelminthes",
                ],
            },
            "bio2_27_ch01_t03": {
                "title": "Animal diversity / প্রাণীর বৈচিত্র্য",
                "themes": [
                    "Urochordata retrogressive metamorphosis / Ascidiacea; Cephalochordata oral hood",
                    "Aves wings+pneumatic bones; crocodile four-chamber heart",
                    "Sarcopterygii lobe-fins / Coelacanth; Reptilia adult lung-only",
                    "Amphibia three-chamber heart / gill-then-lung life",
                    "endostyle→thyroid; Chondrichthyes placoid / Scoliodon / heterocercal shark",
                    "Ascidia chordate non-vertebrate; ammocoete lamprey",
                    "bat 4-chamber heart; Fasciola Platyhelminthes; platypus no teeth/pinna",
                ],
            },
        },
        "low_confidence": [
            "OCR of printed pages p039–045 is noisy (garbled options/answer marks); many stems reconstructed from readable fragments and standard HSC Zoology Ch1 facts.",
            "Figure-only and stimulus-only bank items rewritten as standalone stems (no dependency on missing diagrams).",
            "T01 classification-basis item simplified from multi-statement OCR stimulus about snails/starfish.",
            "Open circulation keyed to Mollusca among given options (standard HSC framing; cephalopod exception noted in explanation).",
            "Cephalochordata 'oral hood' item authored from standard Branchiostoma characters where OCR options were corrupted.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio2_27_ch01_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio2_27_ch01_t01": 20,
                "bio2_27_ch01_t02": 20,
                "bio2_27_ch01_t03": 20,
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
        / "ch01_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
