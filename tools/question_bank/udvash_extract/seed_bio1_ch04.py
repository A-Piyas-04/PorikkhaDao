#!/usr/bin/env python3
"""Seed Biology 1st Paper Ch4 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio1_27_ch04_t01..t03 (viruses; bacteria; microbial roles and disease).
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
    "biology p1 ch04; curated bilingual"
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


# --- t01: Viruses / ভাইরাস ---
T01 = [
    q(
        "Which of the following is a single-stranded DNA virus?",
        "একক সূত্রক DNA ভাইরাস কোনটি?",
        ["Vaccinia", "Ebola", "Coliphage (ΦX174 type)", "Influenza"],
        ["ভ্যাকসিনিয়া", "ইবোলা", "কলিফাজ (ΦX174 ধরনের)", "ইনফ্লুয়েঞ্জা"],
        "C", "medium", "factual",
        "ΦX174-type coliphages carry ssDNA; vaccinia is dsDNA, while Ebola and influenza are RNA viruses.",
        "ΦX174 ধরনের কলিফাজে ssDNA থাকে; ভ্যাকসিনিয়া dsDNA, আর ইবোলা ও ইনফ্লুয়েঞ্জা RNA ভাইরাস।",
    ),
    q(
        "A virion is best described as:",
        "ভিরিয়ন হলো ভাইরাসের—",
        [
            "A non-infectious particle",
            "An infectious complete virus particle",
            "Only the protein coat",
            "Only the nucleic acid",
        ],
        [
            "সংক্রমণ ক্ষমতাবিহীন কণা",
            "সংক্রমণক্ষম পূর্ণাঙ্গ ভাইরাস কণা",
            "কেবল প্রোটিন আবরণ",
            "কেবল নিউক্লিক এসিড",
        ],
        "B", "easy", "factual",
        "A virion is the complete, extracellular infectious form of a virus.",
        "ভিরিয়ন হলো ভাইরাসের পূর্ণাঙ্গ, বহিঃকোষীয় সংক্রমণক্ষম রূপ।",
    ),
    q(
        "Which is commonly cited as an emerging virus?",
        "ইমার্জিং ভাইরাস কোনটি?",
        ["T2 phage", "Zika virus", "TMV", "TIV"],
        ["T₂ ফাজ", "জিকা ভাইরাস", "TMV (টোব্যাকো মোজাইক)", "TIV (টিপুলিড ইরিডিসেন্ট)"],
        "B", "easy", "factual",
        "Zika (with Ebola, Nipah, novel coronaviruses, etc.) is treated as an emerging virus in HSC texts.",
        "HSC পাঠে জিকা (ইবোলা, নিপা, নভেল করোনা ইত্যাদির সঙ্গে) ইমার্জিং ভাইরাস হিসেবে ধরা হয়।",
    ),
    q(
        "Which statement best fits viruses?",
        "ভাইরাসের ক্ষেত্রে কোনটি প্রযোজ্য?",
        ["Ultramicroscopic", "Prokaryotic cells", "Unicellular organisms", "Ordinary microscopic"],
        ["অতি আণুবীক্ষণিক", "আদিকোষী", "এককোষী", "সাধারণ আণুবীক্ষণিক"],
        "A", "easy", "conceptual",
        "Viruses are ultramicroscopic (electron-microscope scale), acellular obligate parasites—not prokaryotic cells.",
        "ভাইরাস অতি-আণুবীক্ষণিক (ইলেকট্রন অণুবীক্ষণিক মাপের), অকোষীয় বাধ্যতামূলক পরজীবী—আদিকোষী নয়।",
    ),
    q(
        "Which of the following is an RNA virus?",
        "কোনটি RNA ভাইরাস?",
        ["T2 phage", "Hepatitis B", "Variola", "TMV"],
        ["T₂ ফাজ", "হেপাটাইটিস-বি", "ভ্যারিওলা", "TMV (টোব্যাকো মোজাইক)"],
        "D", "easy", "factual",
        "Tobacco mosaic virus (TMV) has RNA; T2, hepatitis B and variola are DNA viruses.",
        "টোব্যাকো মোজাইক ভাইরাসে (TMV) RNA থাকে; T₂, হেপাটাইটিস-বি ও ভ্যারিওলা DNA ভাইরাস।",
    ),
    q(
        "Which of the following is a DNA virus?",
        "কোনটি DNA ভাইরাস?",
        ["Rabies", "Influenza", "Vaccinia", "Ebola"],
        ["রেবিস", "ইনফ্লুয়েঞ্জা", "ভ্যাকসিনিয়া", "ইবোলা"],
        "C", "easy", "factual",
        "Vaccinia is a dsDNA poxvirus; rabies, influenza and Ebola are RNA viruses.",
        "ভ্যাকসিনিয়া একটি dsDNA পক্সভাইরাস; রেবিস, ইনফ্লুয়েঞ্জা ও ইবোলা RNA ভাইরাস।",
    ),
    q(
        "Which virus has a rod-like (helical) shape?",
        "নিচের কোনটি দণ্ডাকার ভাইরাস?",
        ["T2 phage", "TMV", "HIV", "Vaccinia"],
        ["T₂ ফাজ", "TMV (টোব্যাকো মোজাইক)", "HIV (এইচআইভি)", "ভ্যাকসিনিয়া"],
        "B", "easy", "factual",
        "TMV is the classic rod-shaped (helical) plant virus; HIV is roughly spherical and T2 is tadpole-shaped.",
        "TMV ক্লাসিক দণ্ডাকৃতির (হেলিকাল) উদ্ভিদ ভাইরাস; HIV প্রায় গোলাকার এবং T₂ ব্যাঙাচি আকৃতির।",
    ),
    q(
        "Which of the following is a roughly spherical virus?",
        "নিচের কোনটি গোলাকার ভাইরাস?",
        ["TMV", "HIV", "T2 phage", "Ebola"],
        ["TMV (টোব্যাকো মোজাইক)", "HIV (এইচআইভি)", "T₂ ফাজ", "ইবোলা"],
        "B", "easy", "factual",
        "HIV is often described as spherical/icosahedral-enveloped; TMV is rod-like and Ebola is filamentous.",
        "HIV প্রায়শই গোলাকার/আইকোসাহেড্রাল-আবৃত হিসেবে বর্ণিত; TMV দণ্ডাকার ও ইবোলা সুতাকার।",
    ),
    q(
        "Which virus contains double-stranded RNA?",
        "কোন ভাইরাসে দ্বি-সূত্রক RNA থাকে?",
        ["HIV", "Reovirus", "Polio", "Rabies"],
        ["HIV (এইচআইভি)", "রিওভাইরাস", "পোলিও", "রেবিস"],
        "B", "medium", "factual",
        "Reoviruses are classic dsRNA viruses; HIV, polio and rabies are ssRNA viruses.",
        "রিওভাইরাস ক্লাসিক dsRNA ভাইরাস; HIV, পোলিও ও রেবিস ssRNA ভাইরাস।",
    ),
    q(
        "Which of the following can be crystallized?",
        "কোনটিকে কেলাসিত করা যায়?",
        ["Archaebacteria", "Malaria parasite", "Virus", "Cyanobacteria"],
        ["আর্কিব্যাকটেরিয়া", "ম্যালেরিয়া পরজীবী", "ভাইরাস", "সায়ানোব্যাকটেরিয়া"],
        "C", "easy", "factual",
        "Viruses (e.g., TMV) can form crystals because they are particulate macromolecular assemblies.",
        "ভাইরাস (যেমন TMV) কণিকাধর্মী ম্যাক্রোমলিকুলার সমাহার হওয়ায় কেলাসিত করা যায়।",
    ),
    q(
        "Who first crystallized TMV from tobacco leaves?",
        "কোন বিজ্ঞানী TMV-কে তামাক পাতা থেকে কেলাসন প্রক্রিয়ায় পৃথক করেন?",
        ["Adolf Mayer", "Ivanovsky", "W. M. Stanley", "Beijerinck"],
        ["আ্যাডলফ মায়ার", "আইভানোভস্কি", "ডব্লিউ. এম. স্টানলি", "বাইজারিনক"],
        "C", "medium", "factual",
        "W. M. Stanley crystallized TMV (1935); Mayer and Ivanovsky earlier established the infectious filtrate concept.",
        "ডব্লিউ. এম. স্টানলি TMV কেলাসিত করেন (১৯৩৫); মায়ার ও আইভানোভস্কি আগে সংক্রামক ফিলট্রেট ধারণা প্রতিষ্ঠা করেন।",
    ),
    q(
        "About how many genes are present in T2 phage DNA?",
        "T₂ ভাইরাসের DNA-তে মোট প্রায় কতটি জিন থাকে?",
        ["80", "90", "120", "150"],
        ["৮০টি", "৯০টি", "১২০টি", "১৫০টি"],
        "D", "medium", "factual",
        "HSC sources commonly state that T2 phage DNA carries about 150 genes.",
        "HSC উৎসে সাধারণত বলা হয় T₂ ফাজের DNA-তে প্রায় ১৫০টি জিন থাকে।",
    ),
    q(
        "Which statement about viruses is NOT correct?",
        "ভাইরাসের ক্ষেত্রে কোনটি সঠিক নয়?",
        [
            "A given virus particle contains both DNA and RNA together",
            "There is no somatic growth as in cellular organisms",
            "They do not respond to environmental stimuli like free-living cells",
            "They can be crystallized",
        ],
        [
            "একই কণায় DNA ও RNA উভয়ই একসাথে থাকে",
            "কোষীয় জীবের মতো দৈহিক বৃদ্ধি নেই",
            "মুক্তজীবী কোষের মতো পরিবেশের উদ্দীপনায় সাড়া দেয় না",
            "কেলাসিত করা যায়",
        ],
        "A", "medium", "conceptual",
        "A virus genome is either DNA or RNA, never both nucleic acids in the same particle.",
        "একটি ভাইরাস জিনোম হয় DNA নয়তো RNA—একই কণায় দুই নিউক্লিক এসিড একসাথে থাকে না।",
    ),
    q(
        "Hepatitis B virus nucleic acid type is:",
        "হেপাটাইটিস-বি ভাইরাসের নিউক্লিক এসিডের ধরন:",
        ["ssRNA", "dsDNA (partially)", "dsRNA", "ssDNA only like ΦX174"],
        ["একসূত্রক RNA (ssRNA)", "আংশিক দ্বিসূত্রক DNA", "দ্বিসূত্রক RNA (dsRNA)", "কেবল ΦX174-এর মতো একসূত্রক DNA"],
        "B", "medium", "factual",
        "HBV is a DNA virus (partially double-stranded circular DNA) in HSC classification.",
        "HSC শ্রেণিতে HBV একটি DNA ভাইরাস (আংশিক দ্বিসূত্রক বৃত্তাকার DNA)।",
    ),
    q(
        "The natural vector of papaya ringspot virus (PRSV) is mainly:",
        "PRSV-এর প্রকৃত বাহক প্রধানত কোনটি?",
        ["Anopheles mosquito", "Aedes mosquito", "Aphid", "Plasmodium"],
        ["অ্যানোফিলিস মশা", "এডিস মশা", "অ্যাফিড (জাবপোকা)", "প্লাজমোডিয়াম"],
        "C", "medium", "factual",
        "PRSV is typically aphid-transmitted; mosquitoes and Plasmodium are unrelated vectors here.",
        "PRSV সাধারণত অ্যাফিড/জাবপোকাবাহিত; মশা ও প্লাজমোডিয়াম এখানে প্রাসঙ্গিক বাহক নয়।",
    ),
    q(
        "In the lysogenic cycle, phage DNA integrated into the bacterial chromosome is called a:",
        "লাইসোজেনিক চক্রে ব্যাকটেরিয়ার ক্রোমোজোমে সংযুক্ত ফাজ DNA-কে কী বলে?",
        ["Virion", "Prophage", "Viroid", "Prion"],
        ["ভিরিয়ন", "প্রোফাজ", "ভিরয়েড", "প্রিয়ন"],
        "B", "medium", "factual",
        "Integrated temperate-phage DNA is a prophage until induction triggers the lytic path.",
        "সংযুক্ত টেম্পারেট-ফাজ DNA প্রোফাজ; ইনডাকশনের পর লাইটিক পথে যেতে পারে।",
    ),
    q(
        "Kaposi sarcoma is associated with which viral group?",
        "কোন ভাইরাস দিয়ে ক্যাপোসি সারকোমা রোগ হয়?",
        ["Ebola virus", "Herpes simplex only", "Retrovirus (e.g., HIV-related)", "Encephalitis virus"],
        ["ইবোলা ভাইরাস", "কেবল হার্পিস সিমপ্লেক্স", "রিট্রোভাইরাস (যেমন HIV-সম্পর্কিত)", "এনসেফালাইটিস ভাইরাস"],
        "C", "hard", "factual",
        "HSC keys link Kaposi sarcoma with retrovirus/HIV context (HHV-8 co-factor clinically).",
        "HSC কীতে ক্যাপোসি সারকোমা রিট্রোভাইরাস/HIV প্রেক্ষাপটে যুক্ত (ক্লিনিক্যালি HHV-8 সহ-কারক)।",
    ),
    q(
        "Which is a DNA virus among the following plant/animal examples?",
        "নিচের কোনটি DNA ভাইরাস?",
        ["T2 phage", "TMV", "Flavi virus", "COVID-19 (SARS-CoV-2)"],
        ["T₂ ফাজ", "TMV (টোব্যাকো মোজাইক)", "ফ্লাভি ভাইরাস", "কোভিড-১৯ (SARS-CoV-2)"],
        "A", "easy", "factual",
        "T2 bacteriophage has dsDNA; TMV, flaviviruses and SARS-CoV-2 are RNA viruses.",
        "T₂ ব্যাকটেরিওফাজে dsDNA থাকে; TMV, ফ্লাভিভাইরাস ও SARS-CoV-2 RNA ভাইরাস।",
    ),
    q(
        "A non-infectious protein coat–nucleic acid assembly without full infectivity packaging context is often called:",
        "সংক্রমণ ক্ষমতাবিহীন নিউক্লিক এসিড–প্রোটিন আবরণ সমষ্টিকে প্রায়শই কী বলে?",
        ["Virion", "Nucleocapsid", "Plasmid", "Mesosome"],
        ["ভিরিয়ন", "নিউক্লিওক্যাপসিড", "প্লাজমিড", "মেসোসোম"],
        "B", "medium", "conceptual",
        "HSC notes contrast infectious virion with nucleocapsid as the core coat–genome assembly.",
        "HSC নোটে সংক্রমণক্ষম ভিরিয়নের বিপরীতে নিউক্লিওক্যাপসিডকে কোর আবরণ–জিনোম সমষ্টি হিসেবে দেখানো হয়।",
    ),
    q(
        "Which feature is typical of a bacteriophage such as T2?",
        "T₂-এর মতো ব্যাকটেরিওফাজের বৈশিষ্ট্য কোনটি?",
        [
            "Acellular and ultramicroscopic with DNA in the head",
            "Always eukaryotic with 80S ribosomes",
            "Photosynthetic thylakoids present",
            "Binary fission as free-living cells",
        ],
        [
            "অকোষীয় ও অতি-আণুবীক্ষণিক; মাথায় DNA থাকে",
            "সর্বদা সুকেন্দ্রিক ও ৮০S রাইবোজোমযুক্ত",
            "সালোকসংশ্লেষী থাইলাকয়েড থাকে",
            "মুক্তজীবী কোষ হিসেবে দ্বিবিভাজন করে",
        ],
        "A", "medium", "conceptual",
        "T2 is an ultramicroscopic acellular phage whose dsDNA is packaged in the head.",
        "T₂ অতি-আণুবীক্ষণিক অকোষীয় ফাজ; এর dsDNA মাথায় প্যাকেজড থাকে।",
    ),
]


# --- t02: Bacteria / ব্যাকটেরিয়া ---
T02 = [
    q(
        "Rod-shaped bacteria are called:",
        "দণ্ডাকার ব্যাকটেরিয়াকে কী বলে?",
        ["Coccus", "Spirillum", "Vibrio", "Bacillus"],
        ["কক্কাস", "স্পাইরিলাম", "ভিব্রিও", "ব্যাসিলাস"],
        "D", "easy", "factual",
        "Bacilli are rod-shaped; cocci spherical, spirilla spiral, vibrios comma-shaped.",
        "ব্যাসিলাস দণ্ডাকার; কক্কাস গোলাকার, স্পাইরিলাম প্যাঁচানো, ভিব্রিও কমাকার।",
    ),
    q(
        "The main function of bacterial pili is to:",
        "ব্যাকটেরিয়াতে পিলির প্রধান কাজ কোনটি?",
        [
            "Help in cell division",
            "Participate mainly in swimming motility",
            "Attach to the host/surface",
            "Protect against all adverse conditions like endospores",
        ],
        [
            "কোষ বিভাজনে সাহায্য করা",
            "প্রধানত সাঁতার চলনে অংশগ্রহণ করা",
            "পোষক/পৃষ্ঠের সাথে যুক্ত হওয়া",
            "এন্ডোস্পোরের মতো সব প্রতিকূলতা থেকে রক্ষা করা",
        ],
        "C", "easy", "factual",
        "Pili (fimbriae) mainly mediate adhesion; flagella handle motility and endospores handle survival.",
        "পিলি (ফিমব্রিয়া) প্রধানত আনুগত্য/সংযুক্তি করে; ফ্ল্যাজেলা চলন ও এন্ডোস্পোর টিকে থাকায় সাহায্য করে।",
    ),
    q(
        "Which bacterium forms nodules on roots of legumes?",
        "কোনটি ডালজাতীয় উদ্ভিদের মূলে নডিউল তৈরি করে?",
        ["Nitrosomonas", "Pseudomonas", "Rhizobium", "Streptococcus"],
        ["নাইট্রোসোমোনাস", "সিউডোমোনাস", "রাইজোবিয়াম", "স্ট্রেপ্টোকক্কাস"],
        "C", "easy", "factual",
        "Rhizobium forms symbiotic root nodules and fixes atmospheric nitrogen.",
        "রাইজোবিয়াম সিমবায়োটিক মূলনডিউল গঠন করে এবং বায়বীয় নাইট্রোজেন সংবন্ধন করে।",
    ),
    q(
        "Which of the following is a free-living nitrogen-fixing bacterium (among the options)?",
        "নিচের কোনটি নাইট্রোজেন সংবন্ধনকারী ব্যাকটেরিয়া?",
        ["Clostridium", "Nitrosomonas", "Nitrococcus", "Nitrobacter"],
        ["ক্লস্ট্রিডিয়াম", "নাইট্রোসোমোনাস", "নাইট্রোকক্কাস", "নাইট্রোব্যাকটার"],
        "A", "medium", "factual",
        "Clostridium (and Azotobacter, etc.) fix N₂; Nitrosomonas/Nitrobacter are nitrifiers, not N₂-fixers.",
        "ক্লস্ট্রিডিয়াম (ও অ্যাজোটোব্যাকটার ইত্যাদি) N₂ সংবন্ধন করে; নাইট্রোসোমোনাস/নাইট্রোব্যাকটার নাইট্রিফায়ার।",
    ),
    q(
        "Which Bacillus species is associated with denitrification that can reduce soil fertility?",
        "মাটির উর্বরতা বিপন্নকারী ডিনাইট্রিফাইং ব্যাকটেরিয়া কোনটি?",
        [
            "Bacillus subtilis",
            "Bacillus polymyxa",
            "Bacillus megaterium",
            "Bacillus denitrificans",
        ],
        [
            "Bacillus subtilis (ব্যাসিলাস সাবটিলিস)",
            "Bacillus polymyxa (ব্যাসিলাস পলিমিক্সা)",
            "Bacillus megaterium (ব্যাসিলাস মেগাটেরিয়াম)",
            "Bacillus denitrificans (ব্যাসিলাস ডিনাইট্রিফিক্যান্স)",
        ],
        "D", "medium", "factual",
        "Bacillus denitrificans converts nitrate to N₂ gas, lowering plant-available nitrogen.",
        "Bacillus denitrificans নাইট্রেটকে N₂ গ্যাসে রূপান্তর করে উদ্ভিদের ব্যবহারযোগ্য নাইট্রোজেন কমায়।",
    ),
    q(
        "Diplococcus pneumoniae cells are typically:",
        "Diplococcus pneumoniae-এর আকৃতি কেমন?",
        ["Spiral", "Comma-shaped", "Rod-shaped", "Spherical"],
        ["প্যাঁচানো", "কমাকার", "দণ্ডাকার", "গোলাকার"],
        "D", "easy", "factual",
        "Pneumococci are spherical diplococci (pairs of cocci).",
        "নিউমোকক্কাই গোলাকার ডিপ্লোকক্কাস (জোড়ায় জোড়ায় কক্কাস)।",
    ),
    q(
        "Comma-shaped bacteria are called:",
        "কমা আকৃতির ব্যাকটেরিয়া কোনটি?",
        ["Vibrio", "Pseudomonas", "Spirillum", "Sarcina"],
        ["ভিব্রিও", "সিউডোমোনাস", "স্পাইরিলাম", "সারসিনা"],
        "A", "easy", "factual",
        "Vibrio (e.g., V. cholerae) is comma-shaped; spirilla are helical and sarcina packet cocci.",
        "ভিব্রিও (যেমন V. cholerae) কমাকার; স্পাইরিলাম হেলিকাল এবং সারসিনা প্যাকেট কক্কাস।",
    ),
    q(
        "Which bacterium is used in processing tea, coffee and tobacco (among common HSC examples)?",
        "চা, কফি ও তামাক প্রক্রিয়াজাতকরণে নিচের কোন ব্যাকটেরিয়া ব্যবহৃত হয়?",
        [
            "Bacillus thuringiensis",
            "Bacillus megaterium",
            "Bordetella pertussis",
            "Bacillus lactis",
        ],
        [
            "Bacillus thuringiensis (বিটি)",
            "Bacillus megaterium (ব্যাসিলাস মেগাটেরিয়াম)",
            "Bordetella pertussis (হুপিং কাশির জীবাণু)",
            "Bacillus lactis (ব্যাসিলাস ল্যাকটিস)",
        ],
        "B", "medium", "factual",
        "HSC texts cite Bacillus megaterium in curing/processing of tea, coffee and tobacco.",
        "HSC পাঠে চা–কফি–তামাক প্রক্রিয়াজাতকরণে Bacillus megaterium উল্লেখ করা হয়।",
    ),
    q(
        "A plasmid carrying antibiotic-resistance genes is called an:",
        "যে প্লাজমিডে অ্যান্টিবায়োটিক প্রতিরোধী জিন থাকে, তাকে বলে—",
        ["F-plasmid", "R-plasmid", "Col plasmid", "Degradative plasmid"],
        ["F-প্লাজমিড", "R-প্লাজমিড", "কল প্লাজমিড", "ডিগ্রেডেটিভ প্লাজমিড"],
        "B", "easy", "factual",
        "R-plasmids (resistance plasmids) encode antibiotic resistance; F is fertility, Col makes colicin.",
        "R-প্লাজমিড অ্যান্টিবায়োটিক রেজিস্ট্যান্স কোড করে; F ফার্টিলিটি, Col কলিসিন তৈরি করে।",
    ),
    q(
        "Bacterial plasma membrane infolding that aids respiration/division is the:",
        "ব্যাকটেরিয়া কোষের প্লাজমা ঝিল্লির ভিতরের ভাঁজ যা শ্বসন/বিভাজনে সাহায্য করে তা হলো—",
        ["Ribosome", "Mesosome", "Chromosome", "Volutin"],
        ["রাইবোজোম", "মেসোসোম", "ক্রোমোজোম", "ভলিউটিন"],
        "B", "easy", "factual",
        "Mesosomes are membrane invaginations linked in textbooks to respiration and septum formation.",
        "মেসোসোম ঝিল্লির অন্তর্ভাঁজ; পাঠ্যে শ্বসন ও সেপ্টাম গঠনের সঙ্গে যুক্ত করা হয়।",
    ),
    q(
        "Which set of bacterial features is correct?",
        "ব্যাকটেরিয়ার বৈশিষ্ট্য হলো— (i) এরা সুকেন্দ্রিক (ii) রাইবোজোম 70S মানের (iii) বংশবৃদ্ধির প্রধান প্রক্রিয়া দ্বিবিভাজন। কোনটি সঠিক?",
        ["(i) and (ii)", "(i) and (iii)", "(ii) and (iii)", "(i), (ii) and (iii)"],
        ["(i) ও (ii)", "(i) ও (iii)", "(ii) ও (iii)", "(i), (ii) ও (iii)"],
        "C", "medium", "conceptual",
        "Bacteria are prokaryotic (not eukaryotic), have 70S ribosomes, and mainly reproduce by binary fission.",
        "ব্যাকটেরিয়া আদিকেন্দ্রিক (সুকেন্দ্রিক নয়), ৭০S রাইবোজোমযুক্ত এবং প্রধানত দ্বিবিভাজনে বংশবৃদ্ধি করে।",
    ),
    q(
        "The fastest/main asexual reproduction method of bacteria is:",
        "ব্যাকটেরিয়ার প্রজননের প্রধান ও দ্রুততর উপায় হলো—",
        ["Budding", "Binary fission", "Gonidia formation", "Transformation"],
        ["মুকুলোদ্গম", "দ্বিবিভাজন", "গনিডিয়া গঠন", "ট্রান্সফরমেশন"],
        "B", "easy", "factual",
        "Binary fission is the primary rapid asexual division; transformation is genetic uptake, not growth.",
        "দ্বিবিভাজন প্রধান দ্রুত অযৌন বিভাজন; ট্রান্সফরমেশন জিন গ্রহণ প্রক্রিয়া, বৃদ্ধি নয়।",
    ),
    q(
        "Which bacterium is associated with vitamin production in HSC examples?",
        "কোন ব্যাকটেরিয়াটি ভিটামিন উৎপন্ন করে?",
        ["Escherichia sp.", "Agrobacterium sp.", "Clostridium sp.", "Rhizobium sp."],
        ["এশেরিচিয়া প্রজাতি", "অ্যাগ্রোব্যাকটেরিয়াম প্রজাতি", "ক্লস্ট্রিডিয়াম প্রজাতি", "রাইজোবিয়াম প্রজাতি"],
        "A", "medium", "factual",
        "Escherichia (gut flora / industrial strains) is cited for vitamin (e.g., K/B-group) production.",
        "Escherichia (অন্ত্রীয়/শিল্প স্ট্রেন) ভিটামিন (যেমন K/B-গ্রুপ) উৎপাদনের উদাহরণ হিসেবে আসে।",
    ),
    q(
        "Xanthomonas oryzae, the rice bacterial blight pathogen, is:",
        "ধানের ব্যাকটেরিয়াল ব্লাইটের জীবাণু Xanthomonas oryzae সম্পর্কে সঠিক—",
        [
            "Gram-positive and spore-forming",
            "Gram-negative and non-spore-forming",
            "An RNA virus",
            "A fungal oomycete",
        ],
        [
            "গ্রাম পজেটিভ ও স্পোর গঠনকারী",
            "গ্রাম নেগেটিভ ও স্পোর গঠন করে না",
            "একটি RNA ভাইরাস",
            "একটি ছত্রাকীয় উমাইসিট",
        ],
        "B", "medium", "factual",
        "X. oryzae is a Gram-negative non-spore-forming bacterial plant pathogen.",
        "X. oryzae গ্রাম নেগেটিভ, স্পোরহীন ব্যাকটেরিয়াল উদ্ভিদ প্যাথোজেন।",
    ),
    q(
        "Which disease is bacterial among the following?",
        "কোনটি ব্যাকটেরিয়াজনিত রোগ?",
        ["Jaundice (viral hepatitis context)", "Measles", "Rabies", "Typhoid"],
        ["জন্ডিস (ভাইরাল হেপাটাইটিস প্রেক্ষাপট)", "হাম", "জলাতঙ্ক", "টাইফয়েড"],
        "D", "easy", "factual",
        "Typhoid is caused by Salmonella Typhi; measles, rabies and typical viral hepatitis jaundice are viral.",
        "টাইফয়েড Salmonella Typhi ঘটিত; হাম, জলাতঙ্ক ও সাধারণ ভাইরাল হেপাটাইটিস জন্ডিস ভাইরাসঘটিত।",
    ),
    q(
        "Which of the following is a bacterial disease?",
        "কোনটি ব্যাকটেরিয়াজনিত রোগ?",
        ["Jaundice", "Cholera", "Dengue", "Polio"],
        ["জন্ডিস", "কলেরা", "ডেঙ্গু", "পোলিও"],
        "B", "easy", "factual",
        "Cholera is caused by Vibrio cholerae; dengue, polio and viral jaundice are viral.",
        "কলেরা Vibrio cholerae ঘটিত; ডেঙ্গু, পোলিও ও ভাইরাল জন্ডিস ভাইরাসঘটিত।",
    ),
    q(
        "Which pathogen of the listed diseases is prokaryotic?",
        "নিচের কোন রোগের জীবাণু আদিকোষী?",
        ["Malaria", "Pneumonia (Pneumococcus)", "Influenza", "Rabies"],
        ["ম্যালেরিয়া", "নিউমোনিয়া (নিউমোকক্কাস)", "ইনফ্লুয়েঞ্জা", "জলাতঙ্ক"],
        "B", "medium", "conceptual",
        "Pneumococcus is a prokaryotic bacterium; malaria is eukaryotic Plasmodium; influenza/rabies are viruses.",
        "নিউমোকক্কাস আদিকোষী ব্যাকটেরিয়া; ম্যালেরিয়া সুকেন্দ্রিক প্লাজমোডিয়াম; ইনফ্লুয়েঞ্জা/জলাতঙ্ক ভাইরাস।",
    ),
    q(
        "Which bacterial features may include: (i) gonidia (ii) endospore (iii) conjugation?",
        "ব্যাকটেরিয়ার ক্ষেত্রে প্রযোজ্য হতে পারে— (i) গনিডিয়া (ii) এন্ডোস্পোর (iii) কনজুগেশন। কোনটি সঠিক?",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "D", "hard", "conceptual",
        "Some bacteria form gonidia/endospores and can transfer DNA by conjugation—all three appear in HSC notes.",
        "কিছু ব্যাকটেরিয়া গনিডিয়া/এন্ডোস্পোর গঠন করে এবং কনজুগেশনে DNA স্থানান্তর করে—তিনটিই HSC নোটে আসে।",
    ),
    q(
        "Bacterial plasmids used in gene engineering typically:",
        "জিন প্রকৌশলে ব্যবহৃত ব্যাকটেরিয়াল প্লাজমিড সাধারণত—",
        [
            "Have few genes and can replicate independently",
            "Are 80S ribosomes",
            "Are eukaryotic nuclei",
            "Are viral capsids only",
        ],
        [
            "স্বল্প সংখ্যক জিন থাকে ও স্বতন্ত্রভাবে বিভাজন/রেপ্লিকেশন করতে পারে",
            "৮০S রাইবোজোম",
            "সুকেন্দ্রিক নিউক্লিয়াস",
            "কেবল ভাইরাল ক্যাপসিড",
        ],
        "A", "medium", "conceptual",
        "Plasmids are small extrachromosomal DNA molecules with autonomous replication—key cloning vectors.",
        "প্লাজমিড ক্ষুদ্র এক্সট্রাক্রোমোজোমাল DNA যা স্বায়ত্তশাসিত রেপ্লিকেশন করে—মূল ক্লোনিং ভেক্টর।",
    ),
    q(
        "Bacteria attach to host cells primarily using:",
        "ব্যাকটেরিয়া পোষক কোষের সাথে প্রধানত কী দ্বারা আবদ্ধ হয়?",
        ["Pili", "Flagella", "Capsid", "Mesosome"],
        ["পিলি", "ফ্ল্যাজেলা", "ক্যাপসিড", "মেসোসোম"],
        "A", "easy", "factual",
        "Adhesive pili/fimbriae bind hosts; flagella are for motility and capsids belong to viruses.",
        "আনুগত্যকারী পিলি/ফিমব্রিয়া পোষক বাঁধে; ফ্ল্যাজেলা চলনের জন্য এবং ক্যাপসিড ভাইরাসের।",
    ),
]


# --- t03: Microbial roles and disease / অণুজীবের ভূমিকা ও রোগ ---
T03 = [
    q(
        "Signet-ring stage of the malaria parasite appears during:",
        "ম্যালেরিয়া পরজীবীর জীবনচক্রের কোন ধাপে সিগনেট রিং দেখা যায়?",
        [
            "Hepatic schizogony",
            "Erythrocytic schizogony",
            "Gametogony",
            "Sporogony",
        ],
        [
            "হেপাটিক সাইজোগনি",
            "এরিথ্রোসাইটিক সাইজোগনি",
            "গ্যামিটোগনি",
            "স্পোরোগনি",
        ],
        "B", "medium", "factual",
        "The signet-ring trophozoite is an early erythrocytic-schizogony stage inside RBCs.",
        "সিগনেট-রিং ট্রফোজয়েট RBC-র ভিতরে এরিথ্রোসাইটিক সাইজোগনির প্রাথমিক দশা।",
    ),
    q(
        "Which is a diploid stage of Plasmodium vivax?",
        "Plasmodium vivax-এর ডিপ্লয়েড দশা কোনটি?",
        ["Trophozoite", "Cryptozoite", "Merozoite", "Oocyst"],
        ["ট্রফোজয়েট", "ক্রিপ্টোজয়েট", "মেরোজয়েট", "উওসিস্ট"],
        "D", "medium", "factual",
        "Zygote, ookinete and oocyst are diploid (2n); trophozoite/merozoite stages are haploid.",
        "জাইগোট, উওকিনেট ও উওসিস্ট ডিপ্লয়েড (2n); ট্রফোজয়েট/মেরোজয়েট হ্যাপ্লয়েড।",
    ),
    q(
        "Malaria fever is mainly triggered by which factor?",
        "কোন উপাদানের কারণে ম্যালেরিয়া জ্বর আসে?",
        ["Hemozoin", "Pyrogen", "Schaffner's granules", "Hemolysin"],
        ["হিমোজয়েন", "পাইরোজেন", "সাফনার্স কণা", "হিমোলাইসিন"],
        "B", "easy", "factual",
        "Pyrogen released at RBC rupture induces the characteristic fever paroxysms.",
        "RBC ফেটে পাইরোজেন ক্ষরণে বৈশিষ্ট্যমূলক ম্যালেরিয়া জ্বরের প্যারোক্সিজম হয়।",
    ),
    q(
        "Which disease is viral among the following?",
        "ভাইরাস জনিত রোগ কোনটি?",
        ["Malaria", "Dengue", "Typhoid", "Pneumonia (bacterial)"],
        ["ম্যালেরিয়া", "ডেঙ্গুজ্বর", "টাইফয়েড", "নিউমোনিয়া (ব্যাকটেরিয়াল)"],
        "B", "easy", "factual",
        "Dengue is flavivirus-borne; malaria is Plasmodium; typhoid and classic pneumococcal pneumonia are bacterial.",
        "ডেঙ্গু ফ্লাভিভাইরাসঘটিত; ম্যালেরিয়া প্লাজমোডিয়াম; টাইফয়েড ও ক্লাসিক নিউমোকক্কাল নিউমোনিয়া ব্যাকটেরিয়াল।",
    ),
    q(
        "Which infective stage of Plasmodium enters humans via mosquito bite?",
        "ম্যালেরিয়া জীবাণুর কোন দশা মানবদেহে সংক্রমণ ঘটায়?",
        ["Merozoite", "Cryptozoite", "Sporozoite", "Schizont"],
        ["মেরোজয়েট", "ক্রিপ্টোজয়েট", "স্পোরোজয়েট", "সাইজন্ট"],
        "C", "easy", "factual",
        "Infective sporozoites from Anopheles salivary glands enter human blood during the bite.",
        "অ্যানোফিলিসের লালাগ্রন্থির সংক্রামক স্পোরোজয়েট কামড়ে মানব রক্তে প্রবেশ করে।",
    ),
    q(
        "Anemia in malaria patients is mainly due to destruction of:",
        "ম্যালেরিয়ায় আক্রান্ত মানুষের রক্তস্বল্পতার প্রধান কারণ কী?",
        ["Platelets only", "Neutrophils only", "Erythrocytes (RBCs)", "Monocytes only"],
        ["কেবল প্লাটিলেট", "কেবল নিউট্রোফিল", "এরিথ্রোসাইট (RBC)", "কেবল মনোসাইট"],
        "C", "easy", "factual",
        "Erythrocytic schizogony ruptures RBCs, causing anemia.",
        "এরিথ্রোসাইটিক সাইজোগনিতে RBC ফেটে রক্তস্বল্পতা হয়।",
    ),
    q(
        "Which plant is the classical source of quinine used against malaria?",
        "ম্যালেরিয়া রোগের প্রধান ওষুধ কুইনাইনের উৎস কোন উদ্ভিদ?",
        ["Neem", "Cinchona", "Tulsi", "Arjun"],
        ["নিম", "সিনকোনা", "তুলসী", "অর্জুন"],
        "B", "easy", "factual",
        "Quinine is obtained from Cinchona bark.",
        "কুইনাইন সিনকোনা গাছের বাকল থেকে পাওয়া যায়।",
    ),
    q(
        "Which virus is associated with pandemic-scale disease among the options?",
        "প্যানডেমিক রোগের জন্য দায়ী কোনটি?",
        ["Ebola (typically epidemic/outbreak)", "Nipah (outbreak)", "COVID-19 (SARS-CoV-2)", "Hepatitis B (endemic chronic)"],
        ["ইবোলা (সাধারণত এপিডেমিক/প্রাদুর্ভাব)", "নিপা (প্রাদুর্ভাব)", "কোভিড-১৯ (SARS-CoV-2)", "হেপাটাইটিস-বি (এন্ডেমিক দীর্ঘমেয়াদি)"],
        "C", "medium", "factual",
        "HSC keys treat COVID-19 as pandemic; MERS more endemic/epidemic, Ebola/Nipah as outbreaks.",
        "HSC কীতে COVID-19 প্যানডেমিক; MERS বেশি এন্ডেমিক/এপিডেমিক, ইবোলা/নিপা প্রাদুর্ভাবধর্মী।",
    ),
    q(
        "Quartan malaria is caused by:",
        "কোয়ারটান ম্যালেরিয়ার পরজীবী কোনটি?",
        ["Plasmodium vivax", "Plasmodium malariae", "Plasmodium ovale", "Plasmodium falciparum"],
        [
            "Plasmodium vivax (পি. ভাইভ্যাক্স)",
            "Plasmodium malariae (পি. ম্যালেরিয়াই)",
            "Plasmodium ovale (পি. ওভেল)",
            "Plasmodium falciparum (পি. ফ্যালসিপ্যারাম)",
        ],
        "B", "medium", "factual",
        "P. malariae causes quartan (72-hour) malaria; P. vivax/ovale tertian; P. falciparum malignant tertian.",
        "পি. ম্যালেরিয়াই কোয়ারটান (৭২ ঘণ্টা) ম্যালেরিয়া করে; vivax/ovale টার্শিয়ান; falciparum ম্যালিগন্যান্ট টার্শিয়ান।",
    ),
    q(
        "Benign tertian malaria is typically caused by:",
        "বিনাইন টার্শিয়ান ম্যালেরিয়া রোগ সংক্রমিত হয় নিচের কোনটি দ্বারা?",
        [
            "Plasmodium vivax",
            "Plasmodium malariae",
            "Plasmodium ovale only exclusive worldwide",
            "Plasmodium falciparum",
        ],
        [
            "Plasmodium vivax (পি. ভাইভ্যাক্স)",
            "Plasmodium malariae (পি. ম্যালেরিয়াই)",
            "কেবল বিশ্বব্যাপী একমাত্র পি. ওভেল",
            "Plasmodium falciparum (পি. ফ্যালসিপ্যারাম)",
        ],
        "A", "medium", "factual",
        "P. vivax causes classic benign tertian malaria (P. ovale also tertian but less emphasized locally).",
        "P. vivax ক্লাসিক বিনাইন টার্শিয়ান ম্যালেরিয়া করে (P. ovale-ও টার্শিয়ান তবে স্থানীয় পাঠে কম জোর)।",
    ),
    q(
        "Hemozoin is formed mainly in which Plasmodium stage?",
        "কোন ধাপে হিমোজয়েন তৈরি হয়?",
        ["Schizont only exclusive", "Cryptozoite", "Amoeboid trophozoite", "Extracellular sporozoite"],
        ["কেবল সাইজন্ট", "ক্রিপ্টোজয়েট", "অ্যামিবয়েড ট্রফোজয়েট", "বহিঃকোষীয় স্পোরোজয়েট"],
        "C", "medium", "factual",
        "During the amoeboid trophozoite stage in RBCs, digested hemoglobin yields hemozoin pigment.",
        "RBC-র অ্যামিবয়েড ট্রফোজয়েট দশায় হিমোগ্লোবিন হজমে হিমোজয়েন রঞ্জক তৈরি হয়।",
    ),
    q(
        "Which Plasmodium stage is found in the mosquito salivary gland?",
        "মশকীর লালাগ্রন্থিতে ম্যালেরিয়া জীবাণুর কোন দশা পাওয়া যায়?",
        ["Sporozoite", "Trophozoite", "Cryptozoite", "Merozoite"],
        ["স্পোরোজয়েট", "ট্রফোজয়েট", "ক্রিপ্টোজয়েট", "মেরোজয়েট"],
        "A", "easy", "factual",
        "Spindle-shaped sporozoites accumulate in Anopheles salivary glands before transmission.",
        "সংক্রমণের আগে অ্যানোফিলিসের লালাগ্রন্থিতে মাকু আকৃতির স্পোরোজয়েট জমা হয়।",
    ),
    q(
        "Exflagellation of Plasmodium occurs in the:",
        "এক্সফ্ল্যাজেলেশন কোথায় ঘটে?",
        ["Liver", "Human RBC cytoplasm only", "Human saliva", "Mosquito midgut"],
        ["যকৃতে", "কেবল মানব RBC সাইটোপ্লাজমে", "মানব লালারসে", "মশকীর মধ্যান্ত্রে"],
        "D", "medium", "factual",
        "Male gametocyte exflagellation occurs in the mosquito midgut during gametogony.",
        "গ্যামিটোগনির সময় মশকীর মধ্যান্ত্রে পুং গ্যামেটোসাইটের এক্সফ্ল্যাজেলেশন ঘটে।",
    ),
    q(
        "The motile elongated zygote of Plasmodium is called an:",
        "ম্যালেরিয়া জীবাণুর যৌন জননে সচল ও লম্বাকৃতি জাইগোটের নাম কী?",
        ["Sporozoite", "Oocyst", "Ookinete", "Merozoite"],
        ["স্পোরোজয়েট", "উওসিস্ট", "উওকিনেট", "মেরোজয়েট"],
        "C", "medium", "factual",
        "The zygote transforms into a motile ookinete that penetrates the midgut wall.",
        "জাইগোট সচল উওকিনেটে পরিণত হয়ে মধ্যান্ত্র প্রাচীর ভেদ করে।",
    ),
    q(
        "Cryptozoites of Plasmodium obtain nutrients mainly from:",
        "ক্রিপ্টোজয়েট কোথা হতে খাদ্য সংগ্রহ করে?",
        ["RBC", "WBC", "Liver cells", "Salivary glands"],
        ["লোহিত রক্তকণিকা (RBC)", "শ্বেত রক্তকণিকা (WBC)", "যকৃত কোষ", "লালাগ্রন্থি"],
        "C", "medium", "factual",
        "Cryptozoites develop in hepatocytes during pre-erythrocytic (hepatic) schizogony.",
        "প্রি-এরিথ্রোসাইটিক (হেপাটিক) সাইজোগনিতে ক্রিপ্টোজয়েট হেপাটোসাইটে বিকশিত হয়।",
    ),
    q(
        "Which statement about rice bacterial blight is correct?",
        "ধান গাছের ব্লাইট রোগের ক্ষেত্রে প্রযোজ্য— (i) আক্রান্ত জীবাণু গ্রাম পজেটিভ ব্যাকটেরিয়া (ii) পাতায় ভেজা, অর্ধস্বচ্ছ ও লম্বা দাগ সৃষ্টি হয় (iii) আক্রান্ত গাছের অধিকাংশ ধান চিটায় পরিণত হয়। কোনটি সঠিক?",
        ["(i) and (ii)", "(ii) and (iii)", "(i) and (iii)", "(i), (ii) and (iii)"],
        ["(i) ও (ii)", "(ii) ও (iii)", "(i) ও (iii)", "(i), (ii) ও (iii)"],
        "B", "hard", "application",
        "X. oryzae is Gram-negative (so i is false); wet translucent long leaf lesions and chita grains match (ii)–(iii).",
        "X. oryzae গ্রাম নেগেটিভ (তাই i ভুল); ভেজা অর্ধস্বচ্ছ লম্বা পাতাদাগ ও চিটা ধান (ii)–(iii) মিলে যায়।",
    ),
    q(
        "Drinking raw date-palm sap is classically linked in Bangladesh to which virus?",
        "কাঁচা খেজুরের রস পানের পর অসুস্থতার সঙ্গে শ্রেণিকভাবে কোন ভাইরাস যুক্ত?",
        ["SARS virus", "Zika virus", "MERS virus", "Nipah virus"],
        ["SARS ভাইরাস", "জিকা ভাইরাস", "MERS ভাইরাস", "নিপা ভাইরাস"],
        "D", "medium", "application",
        "Nipah outbreaks in Bangladesh are associated with raw date-palm sap contaminated by bats.",
        "বাংলাদেশে নিপা প্রাদুর্ভাব বাদুড়দূষিত কাঁচা খেজুর রসের সঙ্গে যুক্ত।",
    ),
    q(
        "For dengue-like illness (high fever, joint/muscle pain, rash, red eyes), which is true?",
        "ডেঙ্গু-সদৃশ অসুস্থতায় (উচ্চ জ্বর, জয়েন্ট/পেশি ব্যথা, র্যাশ, লাল চোখ) কোনটি সত্য?",
        [
            "Caused by Plasmodium in Anopheles only",
            "Caused by a flavivirus, often Aedes-borne",
            "Caused by Vibrio cholerae",
            "Caused by Bacillus anthracis",
        ],
        [
            "কেবল অ্যানোফিলিসের প্লাজমোডিয়াম ঘটিত",
            "ফ্লাভিভাইরাস ঘটিত; প্রায়শই এডিসবাহিত",
            "Vibrio cholerae ঘটিত",
            "Bacillus anthracis ঘটিত",
        ],
        "B", "medium", "application",
        "Dengue is an Aedes-transmitted flavivirus disease; avoid aspirin—use paracetamol and source reduction.",
        "ডেঙ্গু এডিসবাহিত ফ্লাভিভাইরাস রোগ; অ্যাসপিরিন এড়িয়ে প্যারাসিটামল ও পানিজমা নিয়ন্ত্রণ করুন।",
    ),
    q(
        "Which multi-nucleate stage appears in erythrocytic schizogony of Plasmodium?",
        "ম্যালেরিয়া জীবাণুর বহু নিউক্লিয়াসযুক্ত দশা কোনটি?",
        ["Sporozoite", "Trophozoite (early ring)", "Schizont", "Merozoite"],
        ["স্পোরোজয়েট", "ট্রফোজয়েট (প্রাথমিক রিং)", "সাইজন্ট", "মেরোজয়েট"],
        "C", "easy", "factual",
        "Nuclear divisions produce a multinucleate schizont that later releases merozoites.",
        "নিউক্লিয়ার বিভাজনে বহুনিউক্লিয়াসযুক্ত সাইজন্ট তৈরি হয়, যা পরে মেরোজয়েট মুক্ত করে।",
    ),
    q(
        "Which set correctly lists diploid Plasmodium stages?",
        "ম্যালেরিয়া পরজীবীর ডিপ্লয়েড পর্যায় হলো— (i) ট্রফোজয়েট (ii) উওকিনেট (iii) উওসিস্ট। কোনটি সঠিক?",
        ["(i) and (ii)", "(i) and (iii)", "(ii) and (iii)", "(i), (ii) and (iii)"],
        ["(i) ও (ii)", "(i) ও (iii)", "(ii) ও (iii)", "(i), (ii) ও (iii)"],
        "C", "hard", "conceptual",
        "Ookinete and oocyst are diploid; trophozoites are haploid erythrocytic stages.",
        "উওকিনেট ও উওসিস্ট ডিপ্লয়েড; ট্রফোজয়েট হ্যাপ্লয়েড এরিথ্রোসাইটিক দশা।",
    ),
]


TOPICS_MAP = {
    "bio1_27_ch04_t01": T01,
    "bio1_27_ch04_t02": T02,
    "bio1_27_ch04_t03": T03,
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
        "chapter": "bio1_27_ch04",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p141_pdf147.png",
            "p142_pdf148.png",
            "p143_pdf149.png",
            "p144_pdf150.png",
            "p145_pdf151.png",
            "p146_pdf152.png",
            "p147_pdf153.png",
            "p148_pdf154.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio1_27_ch04_t01": {
                "title": "Viruses / ভাইরাস",
                "themes": [
                    "ssDNA coliphage; virion vs nucleocapsid",
                    "emerging viruses (Zika); ultramicroscopic nature",
                    "RNA vs DNA viruses (TMV, vaccinia, HBV, T2)",
                    "shapes: rod TMV, spherical HIV, dsRNA reo",
                    "crystallization / Stanley; T2 ~150 genes",
                    "no DNA+RNA together; PRSV aphid vector",
                    "prophage / lysogeny; Kaposi–retrovirus key",
                    "T2 head DNA / phage features",
                ],
            },
            "bio1_27_ch04_t02": {
                "title": "Bacteria / ব্যাকটেরিয়া",
                "themes": [
                    "bacillus / vibrio / coccus shapes",
                    "pili adhesion; mesosome; binary fission",
                    "Rhizobium nodules; Clostridium N2 fixation",
                    "Bacillus denitrificans; B. megaterium processing",
                    "R-plasmid; gene-engineering plasmids",
                    "70S ribosome / prokaryotic traits",
                    "X. oryzae Gram-negative blight",
                    "typhoid / cholera / pneumococcus prokaryote",
                ],
            },
            "bio1_27_ch04_t03": {
                "title": "Microbial roles and disease / অণুজীবের ভূমিকা ও রোগ",
                "themes": [
                    "signet ring / erythrocytic schizogony",
                    "diploid oocyst–ookinete; haploid trophozoite",
                    "pyrogen fever; RBC anemia; sporozoite infection",
                    "cinchona–quinine; vivax tertian / malariae quartan",
                    "hemozoin; salivary sporozoite; exflagellation",
                    "cryptozoite in liver; rice blight i/ii/iii",
                    "Nipah–date sap; dengue flavivirus/Aedes",
                    "schizont multinucleate; COVID pandemic key",
                ],
            },
        },
        "low_confidence": [
            "Diagram-linked bank items (phage anatomy, Plasmodium cycle figures) rewritten as standalone bilingual stems.",
            "OCR noisy across p141–p148; answers cross-checked against printed explanation snippets and standard HSC keys.",
            "Kaposi sarcoma key follows board/Udvash 'retrovirus' framing rather than clinical HHV-8 nuance.",
            "Pandemic vs epidemic distinctions (COVID vs Ebola/Nipah/MERS) follow HSC bank explanations.",
            "Rice blight Gram-positive distractor retained as false stem clause matching board keys.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio1_27_ch04_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio1_27_ch04_t01": 20,
                "bio1_27_ch04_t02": 20,
                "bio1_27_ch04_t03": 20,
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
        / "ch04_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
