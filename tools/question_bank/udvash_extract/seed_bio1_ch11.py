#!/usr/bin/env python3
"""Seed Biology 1st Paper Ch11 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio1_27_ch11_t01..t03 (genetic engineering; tissue culture; applications).
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
    "biology p1 ch11; curated bilingual"
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


# --- t01: Genetic engineering / জেনেটিক ইঞ্জিনিয়ারিং ---
T01 = [
    q(
        "Which enzyme is commonly called a molecular scissors?",
        "কোনটি আণবিক কাঁচি নামে পরিচিত?",
        [
            "Ligase enzyme",
            "Lipase enzyme",
            "Restriction enzyme",
            "Enolase enzyme",
        ],
        [
            "লাইগেজ এনজাইম",
            "লাইপেজ এনজাইম",
            "রেস্ট্রিকশন এনজাইম",
            "এনোলেজ এনজাইম",
        ],
        "C", "easy", "factual",
        "Restriction endonucleases cut DNA at specific recognition sites, so they are called molecular scissors.",
        "রেস্ট্রিকশন এন্ডোনিউক্লিয়েজ DNA-এর সুনির্দিষ্ট স্বীকৃতি স্থানে কাটে বলে এদের আণবিক কাঁচি বলা হয়।",
    ),
    q(
        "Making many exact copies of a gene is called—",
        "একটি জিনের বহু সংখ্যক হুবহু কপি তৈরি করাই হলো—",
        [
            "Genome sequencing",
            "Gene cloning",
            "Gene engineering only",
            "Gene expression",
        ],
        [
            "জিনোম সিকোয়েন্সিং",
            "জিন ক্লোনিং",
            "কেবল জিন প্রকৌশল",
            "জিন প্রকাশ",
        ],
        "B", "easy", "factual",
        "Gene cloning produces numerous identical copies of a selected gene, often via vectors in host cells.",
        "জিন ক্লোনিং-এ নির্বাচিত জিনের অসংখ্য অভিন্ন কপি তৈরি করা হয়, সাধারণত বাহক ও পোষক কোষ ব্যবহার করে।",
    ),
    q(
        "Which enzyme cuts a plasmid at a specific site in recombinant DNA technology?",
        "রিকম্বিনেন্ট DNA প্রযুক্তিতে কোন এনজাইম দ্বারা প্লাজমিডের নির্দিষ্ট অংশ কাটা হয়?",
        ["Lipase", "Ligase", "Restriction enzyme", "Primase"],
        ["লাইপেজ", "লাইগেজ", "রেস্ট্রিকশন এনজাইম", "প্রাইমেজ"],
        "C", "easy", "factual",
        "Restriction enzymes open the plasmid (and cut donor DNA) at matching restriction sites.",
        "রেস্ট্রিকশন এনজাইম একই স্বীকৃতি স্থানে প্লাজমিড ও দাতা DNA কেটে যোগের সুযোগ তৈরি করে।",
    ),
    q(
        "Which enzyme joins cut DNA fragments to form recombinant DNA?",
        "কর্তিত DNA খণ্ডগুলো যুক্ত করে রিকম্বিনেন্ট DNA তৈরি করতে কোন এনজাইম ব্যবহৃত হয়?",
        ["Helicase", "DNA ligase", "Reverse transcriptase", "Topoisomerase"],
        ["হেলিকেজ", "DNA লাইগেজ", "রিভার্স ট্রান্সক্রিপ্টেজ", "টোপোআইসোমারেজ"],
        "B", "easy", "factual",
        "DNA ligase seals nicks and covalently joins sticky or blunt ends of DNA fragments.",
        "DNA লাইগেজ কর্তিত প্রান্তগুলোকে সমযোজী বন্ধনে যুক্ত করে রিকম্বিনেন্ট DNA গঠন করে।",
    ),
    q(
        "In recombinant DNA technology, gene vectors typically have which features?",
        "রিকম্বিনেন্ট DNA প্রযুক্তিতে জিনের বাহকের বৈশিষ্ট্য কোনগুলো?",
        [
            "Self-replicating; double-stranded; circular",
            "Single-stranded only; linear only",
            "Unable to replicate in host cells",
            "Always RNA viruses only",
        ],
        [
            "স্বপ্রজননক্ষম; দ্বিসূত্রক; গোলাকার",
            "কেবল একসূত্রক; কেবল রৈখিক",
            "পোষক কোষে অনুলিপন অক্ষম",
            "সবসময় কেবল RNA ভাইরাস",
        ],
        "A", "medium", "conceptual",
        "Common plasmid vectors are circular, double-stranded DNA that can replicate independently in the host.",
        "সাধারণ প্লাজমিড বাহক বৃত্তাকার দ্বিসূত্রক DNA এবং পোষক কোষে স্বতন্ত্রভাবে অনুলিপন করতে পারে।",
    ),
    q(
        "Which organism commonly contains plasmids used as cloning vectors?",
        "ক্লোনিং বাহক হিসেবে ব্যবহৃত প্লাজমিড কোনটিতে সাধারণত পাওয়া যায়?",
        ["Pneumococcus only", "TMV only", "E. coli", "Vibrio cholerae only"],
        [
            "কেবল নিউমোকক্কাস",
            "কেবল TMV",
            "E. coli",
            "কেবল Vibrio cholerae",
        ],
        "C", "easy", "factual",
        "E. coli plasmids (e.g., modified pBR-type vectors) are widely used to carry desired DNA inserts.",
        "E. coli-এর প্লাজমিড (যেমন পরিবর্তিত pBR ধরনের বাহক) কাঙ্ক্ষিত DNA বহনের জন্য ব্যাপক ব্যবহৃত।",
    ),
    q(
        "Why are plasmids called vectors in genetic engineering?",
        "জেনেটিক ইঞ্জিনিয়ারিং-এ প্লাজমিডকে ভেক্টর বলা হয় কেন?",
        [
            "Because they digest proteins only",
            "Because they can be modified to carry and transfer desired DNA into a host",
            "Because they form the nuclear membrane",
            "Because they are always single-stranded RNA",
        ],
        [
            "কেবল প্রোটিন হজম করে বলে",
            "কাঙ্ক্ষিত DNA বহন ও পোষকে স্থানান্তরের জন্য পরিবর্তনযোগ্য বাহক হিসেবে কাজ করে বলে",
            "নিউক্লিয়ার মেমব্রেন গঠন করে বলে",
            "সবসময় একসূত্রক RNA বলে",
        ],
        "B", "medium", "conceptual",
        "A vector carries foreign DNA into a host; bacterial plasmids are modified for this carrier role.",
        "ভেক্টর বিদেশি DNA পোষক কোষে নিয়ে যায়; ব্যাকটেরিয়াল প্লাজমিডকে এ উদ্দেশ্যে পরিবর্তন করে ব্যবহার করা হয়।",
    ),
    q(
        "Which process introduces recombinant plasmid DNA into a competent bacterial host cell?",
        "রিকম্বিনেন্ট প্লাজমিড DNA দক্ষ ব্যাকটেরিয়া পোষক কোষে কোন প্রক্রিয়ায় প্রবেশ করানো হয়?",
        ["Fermentation", "Transformation", "Photosynthesis", "Transpiration"],
        ["ফার্মেন্টেশন", "ট্রান্সফরমেশন", "সালোকসংশ্লেষণ", "প্রস্বেদন"],
        "B", "medium", "factual",
        "In bacteria, uptake of naked recombinant DNA (often heat-shock/chemical competence) is called transformation.",
        "ব্যাকটেরিয়ায় নগ্ন রিকম্বিনেন্ট DNA গ্রহণকে ট্রান্সফরমেশন বলে।",
    ),
    q(
        "Restriction enzymes cut DNA at which kind of site?",
        "রেস্ট্রিকশন এনজাইম DNA-এর কোন ধরনের স্থানে কাটে?",
        [
            "Any random nucleotide only",
            "A specific restriction/recognition sequence",
            "Only RNA primers",
            "Only peptide bonds",
        ],
        [
            "কেবল যেকোনো এলোমেলো নিউক্লিওটাইড",
            "সুনির্দিষ্ট রেস্ট্রিকশন/স্বীকৃতি সিকোয়েন্স",
            "কেবল RNA প্রাইমার",
            "কেবল পেপটাইড বন্ধন",
        ],
        "B", "easy", "conceptual",
        "Each restriction endonuclease recognizes a short specific DNA sequence (restriction site) and cleaves there.",
        "প্রতিটি রেস্ট্রিকশন এন্ডোনিউক্লিয়েজ নির্দিষ্ট ছোট DNA সিকোয়েন্স (রেস্ট্রিকশন সাইট) চিনে সেখানে কাটে।",
    ),
    q(
        "Which technology can change an organism’s genotype by inserting foreign genes?",
        "কোন প্রযুক্তি প্রয়োগ করে জীবের জিনোটাইপে বিদেশি জিন সংযোজনের মাধ্যমে পরিবর্তন ঘটানো যায়?",
        [
            "Tissue culture alone",
            "Genome sequencing alone",
            "Gene cloning description only",
            "Recombinant DNA technology",
        ],
        [
            "কেবল টিস্যু কালচার",
            "কেবল জিনোম সিকোয়েন্সিং",
            "কেবল জিন ক্লোনিং-এর বর্ণনা",
            "রিকম্বিনেন্ট DNA প্রযুক্তি",
        ],
        "D", "medium", "conceptual",
        "Recombinant DNA technology combines DNA from different sources and can alter genotype when expressed in the host.",
        "রিকম্বিনেন্ট DNA প্রযুক্তিতে ভিন্ন উৎসের DNA যুক্ত করে পোষকে প্রকাশ করলে জিনোটাইপ পরিবর্তন সম্ভব।",
    ),
    q(
        "What does PCR (Polymerase Chain Reaction) mainly achieve?",
        "PCR (পলিমারেজ চেইন রিঅ্যাকশন) মূলত কী অর্জন করে?",
        [
            "Cutting chromosomes into chromatids only",
            "Amplifying many copies of a DNA segment in vitro",
            "Forming callus from explants",
            "Measuring stomatal density",
        ],
        [
            "কেবল ক্রোমোসোমকে ক্রোমাটিডে ভাঙা",
            "ইন ভিট্রোতে একটি DNA অংশের বহু কপি তৈরি",
            "এক্সপ্লান্ট থেকে ক্যালাস গঠন",
            "পত্ররন্ধ্রের ঘনত্ব মাপা",
        ],
        "B", "medium", "conceptual",
        "PCR thermally denatures DNA, anneals primers, and uses polymerase to amplify the target fragment rapidly.",
        "PCR-এ তাপ দিয়ে DNA বিযুক্ত, প্রাইমার অ্যানিল ও পলিমারেজ দিয়ে লক্ষ্য খণ্ড দ্রুত বহুগুণিত হয়।",
    ),
    q(
        "In a typical PCR cycle, double-stranded DNA is first separated at about what temperature?",
        "সাধারণ PCR চক্রে দ্বিসূত্রক DNA প্রথমে প্রায় কত তাপমাত্রায় পৃথক করা হয়?",
        ["About 37°C", "About 55°C", "About 72°C", "About 90–95°C"],
        ["প্রায় ৩৭°সে.", "প্রায় ৫৫°সে.", "প্রায় ৭২°সে.", "প্রায় ৯০–৯৫°সে."],
        "D", "medium", "factual",
        "Denaturation of dsDNA in PCR is usually done near 90–95°C before primer annealing and extension.",
        "PCR-এ দ্বিসূত্রক DNA সাধারণত প্রায় ৯০–৯৫°সে. তাপমাত্রায় একসূত্রক করা হয়।",
    ),
    q(
        "Which statements about recombinant DNA technology are correct?",
        "রিকম্বিনেন্ট DNA প্রযুক্তি সম্পর্কে কোনগুলো সঠিক?",
        [
            "Needs a plasmid/vector; can change genotype; does not mainly mass-produce plantlets like tissue culture",
            "Needs no DNA-cutting enzyme",
            "Only increases plantlet number without gene transfer",
            "Works only on mitochondrial RNA",
        ],
        [
            "প্লাজমিড/বাহক দরকার; জিনোটাইপ পরিবর্তন সম্ভব; মূলত টিস্যু কালচারের মতো অণুচারা উৎপাদন নয়",
            "DNA কাটার এনজাইমের প্রয়োজন নেই",
            "জিন স্থানান্তর ছাড়াই কেবল চারা সংখ্যা বাড়ায়",
            "কেবল মাইটোকন্ড্রিয়াল RNA-তে কাজ করে",
        ],
        "A", "hard", "conceptual",
        "rDNA typically uses vectors and restriction/ligation steps to alter genetic makeup; rapid clonal plantlets are a tissue-culture advantage.",
        "rDNA-তে বাহক ও রেস্ট্রিকশন/লাইগেশন দিয়ে জিনগত পরিবর্তন হয়; স্বল্প সময়ে অধিক চারা টিস্যু কালচারের সুবিধা।",
    ),
    q(
        "Which microorganism is most widely used as a host in recombinant DNA work?",
        "রিকম্বিনেন্ট DNA প্রযুক্তিতে কোন অণুজীব পোষক হিসেবে সবচেয়ে ব্যাপক ব্যবহৃত?",
        ["Azotobacter", "Pseudomonas", "Clostridium", "E. coli"],
        ["Azotobacter", "Pseudomonas", "Clostridium", "E. coli"],
        "D", "easy", "factual",
        "E. coli is the standard laboratory host for many cloning and expression experiments.",
        "অনেক ক্লোনিং ও প্রোটিন প্রকাশ পরীক্ষায় E. coli আদর্শ ল্যাবরেটরি পোষক।",
    ),
    q(
        "Which of the following is NOT a restriction enzyme?",
        "নিচের কোনটি রেস্ট্রিকশন এনজাইম নয়?",
        ["EcoRI", "BamHI", "HindIII", "Amylase"],
        ["EcoRI", "BamHI", "HindIII", "অ্যামাইলেজ"],
        "D", "medium", "factual",
        "EcoRI, BamHI and HindIII are restriction endonucleases; amylase digests starch, not DNA at restriction sites.",
        "EcoRI, BamHI ও HindIII রেস্ট্রিকশন এনজাইম; অ্যামাইলেজ স্টার্চ ভাঙে, DNA রেস্ট্রিকশন সাইট কাটে না।",
    ),
    q(
        "Desired gene presence in a recombinant construct can be checked by—",
        "রিকম্বিনেন্ট কনস্ট্রাক্টে কাঙ্ক্ষিত জিন আছে কি না শনাক্ত করা যায়—",
        [
            "PCR; restriction digestion; genetic probe methods",
            "Only measuring leaf area",
            "Only counting stomata",
            "Only soil pH testing",
        ],
        [
            "PCR; রেস্ট্রিকশন ডাইজেশন; জেনেটিক প্রোব পদ্ধতি",
            "কেবল পাতার ক্ষেত্রফল মাপা",
            "কেবল পত্ররন্ধ্র গণনা",
            "কেবল মাটির pH পরীক্ষা",
        ],
        "A", "hard", "application",
        "Insert verification commonly uses PCR, restriction mapping, and hybridization with labeled probes.",
        "ইনসার্ট যাচাইয়ে সাধারণত PCR, রেস্ট্রিকশন ম্যাপিং ও লেবেলযুক্ত প্রোব হাইব্রিডাইজেশন ব্যবহার হয়।",
    ),
    q(
        "A key feature of a useful plasmid vector is that it is—",
        "একটি উপযোগী প্লাজমিড বাহকের গুরুত্বপূর্ণ বৈশিষ্ট্য হলো এটি—",
        [
            "Unable to replicate",
            "Capable of replication (self-replicating) in the host",
            "Always found only in plant nuclei",
            "Always four-stranded DNA",
        ],
        [
            "অনুলিপনে অক্ষম",
            "পোষক কোষে অনুলিপনক্ষম (স্বপ্রজননক্ষম)",
            "সবসময় কেবল উদ্ভিদ নিউক্লিয়াসে থাকে",
            "সবসময় চারসূত্রক DNA",
        ],
        "B", "easy", "conceptual",
        "Vectors must replicate so the inserted gene is maintained and multiplied with the plasmid.",
        "বাহককে অনুলিপনক্ষম হতে হয় যাতে সন্নিবিষ্ট জিন প্লাজমিডসহ বজায় ও বহুগুণিত হয়।",
    ),
    q(
        "In recombinant DNA construction, bacteria may be used as—",
        "রিকম্বিনেন্ট DNA নির্মাণে ব্যাকটেরিয়া ব্যবহার করা যায়—",
        [
            "Vector source/host and as a source of restriction enzymes",
            "Only as a carbon dioxide fixer",
            "Only to produce callus",
            "Only as a light microscope lens",
        ],
        [
            "বাহক/পোষক এবং রেস্ট্রিকশন এনজাইমের উৎস হিসেবে",
            "কেবল কার্বন ডাইঅক্সাইড স্থিতিকারী হিসেবে",
            "কেবল ক্যালাস তৈরি করতে",
            "কেবল অণুবীক্ষণ যন্ত্রের লেন্স হিসেবে",
        ],
        "A", "medium", "application",
        "Bacteria supply plasmids/hosts and many restriction enzymes used to cut DNA.",
        "ব্যাকটেরিয়া প্লাজমিড/পোষক সরবরাহ করে এবং অনেক রেস্ট্রিকশন এনজাইমের উৎস।",
    ),
    q(
        "Sticky ends produced by the same restriction enzyme on vector and insert allow—",
        "একই রেস্ট্রিকশন এনজাইমে বাহক ও ইনসার্টে তৈরি স্টিকি এন্ড কী সম্ভব করে?",
        [
            "Complementary base pairing before ligation",
            "Immediate protein folding only",
            "Formation of starch grains",
            "Loss of all genes permanently",
        ],
        [
            "লাইগেশনের আগে সম্পূরক ক্ষারক জোড় বাঁধা",
            "কেবল তাৎক্ষণিক প্রোটিন ভাঁজ",
            "স্টার্চ দানা গঠন",
            "সব জিন স্থায়ীভাবে হারানো",
        ],
        "A", "medium", "conceptual",
        "Compatible sticky ends anneal by complementary base pairing, helping ligase join insert and vector.",
        "সুসংগত স্টিকি এন্ড সম্পূরক ক্ষারক জোড়ে অস্থায়ীভাবে মিলে লাইগেজকে যুক্ত করতে সহায়তা করে।",
    ),
    q(
        "Genetic engineering broadly means—",
        "জেনেটিক ইঞ্জিনিয়ারিং বলতে ব্যাপক অর্থে কী বোঝায়?",
        [
            "Only counting chromosomes under a microscope",
            "Deliberate manipulation of genes/DNA to obtain desired traits or products",
            "Only watering plants daily",
            "Only measuring body temperature",
        ],
        [
            "কেবল অণুবীক্ষণে ক্রোমোসোম গণনা",
            "কাঙ্ক্ষিত বৈশিষ্ট্য বা পণ্য পেতে জিন/DNA-এর সচেতন পরিবর্তন",
            "কেবল প্রতিদিন গাছে পানি দেওয়া",
            "কেবল শরীরের তাপমাত্রা মাপা",
        ],
        "B", "easy", "conceptual",
        "Genetic engineering uses molecular tools to alter genetic material for useful products or traits.",
        "জেনেটিক ইঞ্জিনিয়ারিং-এ আণবিক পদ্ধতিতে জিনগত উপাদান পরিবর্তন করে উপযোগী পণ্য বা বৈশিষ্ট্য পাওয়া যায়।",
    ),
]

# --- t02: Tissue culture / টিস্যু কালচার ---
T02 = [
    q(
        "Who is regarded as the father of tissue culture?",
        "টিস্যু কালচারের জনক কে?",
        [
            "Karl Nageli",
            "Dr. S. J. Singer",
            "Stephen Hales",
            "Gottlieb Haberlandt",
        ],
        [
            "Karl Nageli",
            "Dr. S. J. Singer",
            "Stephen Hales",
            "Gottlieb Haberlandt",
        ],
        "D", "easy", "factual",
        "Gottlieb Haberlandt pioneered the idea of culturing plant cells/tissues in vitro.",
        "Gottlieb Haberlandt উদ্ভিদ কোষ/টিস্যু ইন ভিট্রো কালচারের ধারণার পথিকৃৎ বলে স্বীকৃত।",
    ),
    q(
        "The excised plant part taken from a mother plant for tissue culture is called—",
        "টিস্যু কালচারের উদ্দেশ্যে মাতৃ উদ্ভিদ হতে পৃথকীকৃত অংশের নাম কী?",
        ["Meristem only", "Plantlet only", "Explant", "Callus only"],
        ["কেবল মেরিস্টেম", "কেবল অণুচারা", "এক্সপ্লান্ট", "কেবল ক্যালাস"],
        "C", "easy", "factual",
        "An explant is any living plant piece excised and placed on/in culture medium.",
        "এক্সপ্লান্ট হলো মাতৃ উদ্ভিদ থেকে কেটে কালচার মিডিয়ামে নেওয়া জীবন্ত অংশ।",
    ),
    q(
        "The unorganized cell mass formed in tissue culture is called—",
        "টিস্যু কালচারে সৃষ্ট অসংগঠিত কোষপিণ্ডকে কী বলে?",
        ["Callus", "Medium", "Vector", "Cybrid"],
        ["ক্যালাস", "মিডিয়াম", "ভেক্টর", "সাইব্রিড"],
        "A", "easy", "factual",
        "Callus is a mass of undifferentiated cells proliferating on culture medium.",
        "ক্যালাস হলো কালচার মিডিয়ামে সৃষ্ট অভেদিত কোষের পিণ্ড।",
    ),
    q(
        "Explant is primarily associated with which process?",
        "এক্সপ্লান্ট প্রধানত কোন প্রক্রিয়ার সাথে সম্পর্কযুক্ত?",
        [
            "Tissue culture",
            "Genetic engineering only",
            "Gene cloning only",
            "Genome sequencing only",
        ],
        [
            "টিস্যু কালচার",
            "কেবল জেনেটিক ইঞ্জিনিয়ারিং",
            "কেবল জিন ক্লোনিং",
            "কেবল জিনোম সিকোয়েন্সিং",
        ],
        "A", "easy", "factual",
        "Tissue culture begins with placing an explant on a sterile nutrient medium.",
        "টিস্যু কালচার শুরু হয় জীবাণুমুক্ত পুষ্টি মাধ্যমে এক্সপ্লান্ট স্থাপন দিয়ে।",
    ),
    q(
        "Which culture method is best for producing the most pathogen-free plantlets?",
        "কোনটির মাধ্যমে সর্বাপেক্ষা জীবাণুমুক্ত চারা উৎপাদন সম্ভব?",
        [
            "Stem culture only",
            "Pollen culture only",
            "Protoplast culture only",
            "Meristem culture",
        ],
        [
            "কেবল কাণ্ড কালচার",
            "কেবল পরাগরেণু কালচার",
            "কেবল প্রোটোপ্লাস্ট কালচার",
            "মেরিস্টেম কালচার",
        ],
        "D", "medium", "conceptual",
        "Apical meristems are often virus-free; meristem culture yields disease-free plantlets.",
        "অগ্রভাজক মেরিস্টেম সাধারণত ভাইরাসমুক্ত; মেরিস্টেম কালচারে রোগমুক্ত চারা পাওয়া যায়।",
    ),
    q(
        "Haploid plants can be produced through—",
        "হ্যাপ্লয়েড উদ্ভিদ উৎপাদন করা যায় কোনটির মাধ্যমে?",
        [
            "Meristem culture only",
            "Callus culture only",
            "Anther/pollen culture",
            "Axillary bud culture only",
        ],
        [
            "কেবল মেরিস্টেম কালচার",
            "কেবল ক্যালাস কালচার",
            "পরাগধানী/পরাগরেণু কালচার",
            "কেবল কক্ষ মুকুল কালচার",
        ],
        "C", "medium", "factual",
        "Culturing anthers or pollen grains can regenerate haploid plants useful in breeding.",
        "পরাগধানী বা পরাগরেণু কালচার করে হ্যাপ্লয়েড উদ্ভিদ পাওয়া যায়, যা প্রজননে উপযোগী।",
    ),
    q(
        "Which component helps solidify the tissue culture medium?",
        "কোনটি আবাদ মাধ্যমকে জমাট বাঁধতে সহায়তা করে?",
        ["Vitamin", "Hormone", "Agar", "Sucrose only as gelling agent"],
        ["ভিটামিন", "হরমোন", "অ্যাগার", "কেবল জেলিং এজেন্ট হিসেবে সুক্রোজ"],
        "C", "easy", "factual",
        "Agar is the usual gelling agent that solidifies plant tissue culture media.",
        "উদ্ভিদ টিস্যু কালচার মিডিয়াম জমাট করতে সাধারণত অ্যাগার ব্যবহার করা হয়।",
    ),
    q(
        "Tissue culture media for plants commonly require—",
        "উদ্ভিদের টিস্যু কালচার মিডিয়ামে সাধারণত কী থাকা প্রয়োজন?",
        [
            "Only pure protein powder",
            "Macro/micro nutrients, vitamins, sucrose, and phytohormones",
            "Only maltose without minerals",
            "Only distilled water",
        ],
        [
            "কেবল বিশুদ্ধ প্রোটিন গুঁড়ো",
            "ম্যাক্রো/মাইক্রো পুষ্টি, ভিটামিন, সুক্রোজ ও ফাইটোহরমোন",
            "খনিজ ছাড়া কেবল ম্যালটোজ",
            "কেবল ডিস্টিলড পানি",
        ],
        "B", "medium", "conceptual",
        "Standard media supply minerals, vitamins, a carbon source (often 2–4% sucrose), and growth regulators.",
        "আদর্শ মিডিয়ামে খনিজ, ভিটামিন, কার্বন উৎস (প্রায় ২–৪% সুক্রোজ) ও বৃদ্ধি নিয়ন্ত্রক থাকে।",
    ),
    q(
        "A major advantage of tissue culture technology is—",
        "টিস্যু কালচার প্রযুক্তির একটি প্রধান সুবিধা কী?",
        [
            "Producing many genetically uniform plantlets in a short time and small space",
            "Always creating new unrelated species overnight",
            "Eliminating the need for any nutrients",
            "Working only in open non-sterile soil beds",
        ],
        [
            "স্বল্প সময়ে ও অল্প স্থানে সমগুণসম্পন্ন অসংখ্য অণুচারা পাওয়া",
            "সবসময় এক রাতে নতুন অসম্পর্কিত প্রজাতি তৈরি",
            "কোনো পুষ্টির প্রয়োজন না থাকা",
            "কেবল খোলা অজীবাণুমুক্ত মাটিতে কাজ করা",
        ],
        "A", "easy", "conceptual",
        "Micropropagation rapidly yields large numbers of clonal, often disease-managed plantlets under aseptic conditions.",
        "মাইক্রোপ্রোপাগেশনে জীবাণুমুক্ত অবস্থায় দ্রুত প্রচুর ক্লোনাল চারা পাওয়া যায়।",
    ),
    q(
        "Which statements correctly list benefits of tissue culture?",
        "টিস্যু কালচারের সুবিধা সম্পর্কে কোনটি সঠিক?",
        [
            "Disease-free plantlets; maternal-trait fidelity; many plantlets in little time/space",
            "Only increases soil salinity",
            "Only destroys all phytohormones",
            "Only prevents photosynthesis forever",
        ],
        [
            "রোগমুক্ত চারা; মাতৃগুণসম্পন্নতা; স্বল্প সময় ও স্থানে অধিক চারা",
            "কেবল মাটির লবণাক্ততা বাড়ায়",
            "কেবল সব ফাইটোহরমোন নষ্ট করে",
            "কেবল সালোকসংশ্লেষণ চিরতরে বন্ধ করে",
        ],
        "A", "medium", "conceptual",
        "Tissue culture can give pathogen-cleaned, true-to-type plantlets at high density and year-round.",
        "টিস্যু কালচারে রোগমুক্ত, মাতৃসদৃশ চারা ঘন ও বছরজুড়ে উৎপাদন সম্ভব।",
    ),
    q(
        "In a typical tissue-culture sequence, the explant is first placed on—",
        "সাধারণ টিস্যু কালচার ধাপে এক্সপ্লান্ট প্রথমে কোথায় রাখা হয়?",
        [
            "A sterile nutrient medium",
            "Only dry desert sand",
            "Only concentrated acid",
            "Only liquid nitrogen permanently",
        ],
        [
            "জীবাণুমুক্ত পুষ্টি মাধ্যমে",
            "কেবল শুষ্ক মরুবালুতে",
            "কেবল ঘন অ্যাসিডে",
            "কেবল স্থায়ীভাবে তরল নাইট্রোজেনে",
        ],
        "A", "easy", "factual",
        "Aseptic inoculation of the explant onto/into nutrient medium starts in vitro culture.",
        "জীবাণুমুক্তভাবে এক্সপ্লান্ট পুষ্টি মাধ্যমে স্থাপন করে ইন ভিট্রো কালচার শুরু হয়।",
    ),
    q(
        "Pomato is an example of a plant produced mainly by—",
        "পোম্যাটো মূলত কোন পদ্ধতিতে সৃষ্ট উদ্ভিদের উদাহরণ?",
        [
            "Only conventional seed sowing",
            "Protoplast fusion (cybrid/hybrid tissue approaches), not ordinary rDNA crop insertion alone",
            "Only grafting tomato onto potato roots in the field",
            "Only genome sequencing of wheat",
        ],
        [
            "কেবল প্রচলিত বীজ বপন",
            "প্রোটোপ্লাস্ট ফিউশন (সাইব্রিড/সংকর টিস্যু পদ্ধতি), কেবল সাধারণ rDNA শস্য সন্নিবেশ নয়",
            "কেবল মাঠে আলুর মূলে টমেটো কলম",
            "কেবল গমের জিনোম সিকোয়েন্সিং",
        ],
        "B", "hard", "conceptual",
        "Pomato arises from potato–tomato protoplast fusion; texts distinguish it from typical recombinant DNA crops like Bt brinjal.",
        "পোম্যাটো আলু–টমেটো প্রোটোপ্লাস্ট ফিউশনের ফল; Bt বেগুনের মতো সাধারণ rDNA ফসল থেকে আলাদা।",
    ),
    q(
        "A plant formed by fusion of cytoplasms without nuclear fusion is called a—",
        "নিউক্লিয়াসের মিলন ছাড়া কেবল সাইটোপ্লাজম মিলনে সৃষ্ট উদ্ভিদকে কী বলে?",
        ["True sexual hybrid only", "Cybrid", "Vector", "Primer"],
        ["কেবল প্রকৃত যৌন সংকর", "সাইব্রিড", "ভেক্টর", "প্রাইমার"],
        "B", "medium", "factual",
        "Cybrids result when protoplast fusion combines cytoplasms without complete nuclear fusion.",
        "প্রোটোপ্লাস্ট ফিউশনে নিউক্লিয়াস মিলন ছাড়া সাইটোপ্লাজম মিললে সাইব্রিড গঠিত হয়।",
    ),
    q(
        "Which materials are essential for a tissue-culture setup described in HSC texts?",
        "HSC পাঠ্য অনুসারে টিস্যু কালচার সেটআপে প্রয়োজনীয় উপকরণ কোনগুলো?",
        [
            "Glass vessels, culture medium, and phytohormones",
            "Only a soil tiller",
            "Only a fishing net",
            "Only a barometer",
        ],
        [
            "কাচপাত্র, কালচার মিডিয়াম ও ফাইটোহরমোন",
            "কেবল মাটি চাষের যন্ত্র",
            "কেবল মাছ ধরার জাল",
            "কেবল ব্যারোমিটার",
        ],
        "A", "easy", "factual",
        "In vitro culture needs sterile containers, nutrient medium, and growth regulators among other controls.",
        "ইন ভিট্রো কালচারে জীবাণুমুক্ত পাত্র, পুষ্টি মাধ্যম ও বৃদ্ধি নিয়ন্ত্রক প্রয়োজন।",
    ),
    q(
        "Tissue culture is especially useful when a plant—",
        "টিস্যু কালচার বিশেষ উপযোগী যখন কোনো উদ্ভিদের—",
        [
            "Seeds are absent or vegetative propagation is difficult",
            "Always has unlimited natural seed set with no disease",
            "Cannot photosynthesize at all and needs no carbon source",
            "Lives only as free DNA in air",
        ],
        [
            "বীজ হয় না বা অঙ্গজ বংশবৃদ্ধি সহজ নয়",
            "সবসময় রোগহীন অসীম প্রাকৃতিক বীজ উৎপাদন করে",
            "সালোকসংশ্লেষণই করে না এবং কার্বন উৎস লাগে না",
            "কেবল বাতাসে মুক্ত DNA হিসেবে থাকে",
        ],
        "A", "medium", "application",
        "Species that set little seed or are hard to propagate vegetatively can still be multiplied via tissue culture.",
        "যেসব উদ্ভিদের বীজ কম হয় বা অঙ্গজ বংশবৃদ্ধি কঠিন, টিস্যু কালচারে তাদের চারা বাড়ানো যায়।",
    ),
    q(
        "Somaclonal variation refers to—",
        "সোমাক্লোনাল ভ্যারিয়েশন বলতে কী বোঝায়?",
        [
            "Genetic/phenotypic variation arising among plants regenerated from tissue culture",
            "Only seasonal rainfall change",
            "Only moon-phase effects on tides",
            "Only change in soil color",
        ],
        [
            "টিস্যু কালচার থেকে পুনরুজ্জীবিত উদ্ভিদের মধ্যে জিনগত/ফিনোটাইপিক ভিন্নতা",
            "কেবল ঋতুভিত্তিক বৃষ্টির পরিবর্তন",
            "কেবল জোয়ার-ভাটায় চাঁদের প্রভাব",
            "কেবল মাটির রঙের পরিবর্তন",
        ],
        "A", "hard", "conceptual",
        "Cells cultured in vitro may accumulate variation; regenerants can show somaclonal differences useful or undesirable in breeding.",
        "ইন ভিট্রো কোষে ভিন্নতা জমতে পারে; পুনরুজ্জীবিত গাছে সোমাক্লোনাল পার্থক্য দেখা যায়।",
    ),
    q(
        "Micropropagation mainly aims to—",
        "মাইক্রোপ্রোপাগেশনের মূল লক্ষ্য কী?",
        [
            "Rapid clonal multiplication of plants under aseptic culture",
            "Only sequence an entire animal genome",
            "Only extract crude oil",
            "Only measure wind speed",
        ],
        [
            "জীবাণুমুক্ত কালচারে উদ্ভিদের দ্রুত ক্লোনাল বংশবৃদ্ধি",
            "কেবল সম্পূর্ণ প্রাণী জিনোম সিকোয়েন্স করা",
            "কেবল অশোধিত তেল নিষ্কাশন",
            "কেবল বায়ুবেগ মাপা",
        ],
        "A", "easy", "conceptual",
        "Micropropagation is large-scale clonal plant production using tissue-culture methods.",
        "মাইক্রোপ্রোপাগেশন হলো টিস্যু কালচার পদ্ধতিতে বড় পরিসরে ক্লোনাল উদ্ভিদ উৎপাদন।",
    ),
    q(
        "Which advantage pair correctly describes tissue culture but NOT recombinant DNA crop insertion?",
        "কোন সুবিধাজোড়া টিস্যু কালচারের বৈশিষ্ট্য, সাধারণ রিকম্বিনেন্ট DNA শস্য সন্নিবেশের নয়?",
        [
            "Many true-to-type plantlets quickly without necessarily inserting a foreign gene",
            "Always inserting Bt toxin genes into every crop",
            "Always producing human insulin in bacteria",
            "Always reading DNA fingerprint bands",
        ],
        [
            "বিদেশি জিন সন্নিবেশ ছাড়াই দ্রুত সমগুণসম্পন্ন অনেক চারা",
            "সব ফসলে সবসময় Bt টক্সিন জিন ঢোকানো",
            "ব্যাকটেরিয়ায় সবসময় মানব ইনসুলিন তৈরি",
            "সবসময় DNA ফিঙ্গারপ্রিন্ট ব্যান্ড পড়া",
        ],
        "A", "hard", "conceptual",
        "Tissue culture multiplies existing genotypes; rDNA insertion deliberately adds new genetic material.",
        "টিস্যু কালচার বিদ্যমান জিনোটাইপ বাড়ায়; rDNA সন্নিবেশ ইচ্ছাকৃত নতুন জিনগত উপাদান যোগ করে।",
    ),
    q(
        "Pollen culture is especially linked to producing—",
        "পরাগরেণু কালচার বিশেষভাবে কোনটির সাথে যুক্ত?",
        [
            "Homozygous lines via haploid pathway",
            "Only starch-filled endosperm in mango",
            "Only nitrogen fixation nodules",
            "Only viral envelopes",
        ],
        [
            "হ্যাপ্লয়েড পথ দিয়ে হোমোজাইগাস লাইন",
            "কেবল আমের স্টার্চপূর্ণ এন্ডোস্পার্ম",
            "কেবল নাইট্রোজেন স্থিতিকরণ নডিউল",
            "কেবল ভাইরাস আবরণ",
        ],
        "A", "medium", "application",
        "Haploids from pollen culture can be doubled to obtain homozygous breeding lines quickly.",
        "পরাগরেণু কালচারের হ্যাপ্লয়েড দ্বিগুণ করে দ্রুত হোমোজাইগাস প্রজনন লাইন পাওয়া যায়।",
    ),
    q(
        "Protoplast culture is useful for—",
        "প্রোটোপ্লাস্ট কালচার উপযোগী—",
        [
            "Cybrid/hybrid formation and some transformation work",
            "Only measuring rainfall",
            "Only counting nest eggs",
            "Only polishing glassware",
        ],
        [
            "সাইব্রিড/সংকর গঠন ও কিছু ট্রান্সফরমেশন কাজে",
            "কেবল বৃষ্টিপাত মাপা",
            "কেবল পাখির ডিম গণনা",
            "কেবল কাচপাত্র পালিশ",
        ],
        "A", "medium", "application",
        "Wall-less protoplasts enable fusion and certain DNA uptake experiments before regeneration.",
        "প্রাচীরহীন প্রোটোপ্লাস্ট ফিউশন ও কিছু DNA গ্রহণ পরীক্ষা করে পরে উদ্ভিদ পুনরুজ্জীবন সম্ভব।",
    ),
]

# --- t03: Biotechnology applications / জীবপ্রযুক্তির প্রয়োগ ---
T03 = [
    q(
        "Bt brinjal is produced using crystal protein gene from which organism?",
        "Bt বেগুন উৎপাদনে কোন অণুজীবের ক্রিস্টাল প্রোটিন জিন ব্যবহার করা হয়?",
        [
            "Bacillus dysenteriae",
            "Bacillus thuringiensis",
            "Bacillus anthracis",
            "Bacillus denitrificans",
        ],
        [
            "Bacillus dysenteriae",
            "Bacillus thuringiensis",
            "Bacillus anthracis",
            "Bacillus denitrificans",
        ],
        "B", "easy", "factual",
        "The cry gene from soil bacterium Bacillus thuringiensis confers insect resistance in Bt brinjal.",
        "মৃত্তিকা ব্যাকটেরিয়া Bacillus thuringiensis-এর cry জিন Bt বেগুনকে কীটপতঙ্গ প্রতিরোধী করে।",
    ),
    q(
        "Which was the first GM food crop approved by the Government of Bangladesh?",
        "বাংলাদেশ সরকার অনুমোদিত প্রথম GM খাদ্য ফসল কোনটি?",
        ["Bt cotton", "Bt brinjal", "Bt wheat", "Bt potato"],
        ["Bt তুলা", "Bt বেগুন", "Bt গম", "Bt আলু"],
        "B", "easy", "factual",
        "Bt brinjal was Bangladesh’s first approved genetically modified food crop.",
        "বাংলাদেশে সরকারিভাবে অনুমোদিত প্রথম GM খাদ্য ফসল Bt বেগুন।",
    ),
    q(
        "Golden rice (super rice type discussed in texts) is enriched in which vitamin?",
        "গোল্ডেন রাইস (পাঠ্যে আলোচিত সুপার রাইস ধরন) কোন ভিটামিনে সমৃদ্ধ?",
        ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"],
        ["ভিটামিন A", "ভিটামিন B", "ভিটামিন C", "ভিটামিন D"],
        "A", "easy", "factual",
        "Golden rice accumulates beta-carotene, a precursor of vitamin A, in the endosperm.",
        "গোল্ডেন রাইসের এন্ডোস্পার্মে বিটা-ক্যারোটিন জমে, যা ভিটামিন A-এর পূর্ববর্তী।",
    ),
    q(
        "Genes used to develop golden/super rice pathways are classically sourced from plants such as—",
        "গোল্ডেন/সুপার রাইস পথে ব্যবহৃত জিন শাস্ত্রীয়ভাবে কোন উদ্ভিদ উৎস থেকে আসে?",
        [
            "Daffodil (and related carotenoid pathway donors)",
            "Only sunflower seed oil bottles",
            "Only pancreatic beta cells",
            "Only fibroblast cell lines of humans",
        ],
        [
            "ড্যাফোডিল (ও সম্পর্কিত ক্যারোটিনয়েড পথ দাতা)",
            "কেবল সূর্যমুখী তেলের বোতল",
            "কেবল অগ্ন্যাশয়ের বিটা কোষ",
            "কেবল মানুষের ফাইব্রোব্লাস্ট কোষলাইন",
        ],
        "A", "medium", "factual",
        "Classic golden rice used daffodil (and later other) carotenoid biosynthesis genes transferred into rice.",
        "ক্লাসিক গোল্ডেন রাইসে ড্যাফোডিলসহ ক্যারোটিনয়েড জিন ধানের জিনোমে স্থানান্তর করা হয়।",
    ),
    q(
        "Human insulin produced by genetic engineering is chemically a—",
        "জেনেটিক ইঞ্জিনিয়ারিং-এ উৎপাদিত মানব ইনসুলিন রাসায়নিকভাবে কী?",
        ["Protein", "Vitamin", "Lipid", "Carbohydrate"],
        ["প্রোটিন", "ভিটামিন", "লিপিড", "কার্বোহাইড্রেট"],
        "A", "easy", "factual",
        "Insulin is a small protein (peptide hormone) made of amino acids.",
        "ইনসুলিন অ্যামিনো অ্যাসিড দিয়ে গঠিত ক্ষুদ্র প্রোটিন (পেপটাইড হরমোন)।",
    ),
    q(
        "Commercial recombinant insulin production mainly uses—",
        "বাণিজ্যিক রিকম্বিনেন্ট ইনসুলিন উৎপাদনে প্রধানত কোন প্রক্রিয়া ব্যবহৃত হয়?",
        [
            "Genome sequencing only",
            "Micropropagation only",
            "Hybridization of flowers only",
            "Genetic engineering",
        ],
        [
            "কেবল জিনোম সিকোয়েন্সিং",
            "কেবল মাইক্রোপ্রোপাগেশন",
            "কেবল পুষ্প সংকরায়ন",
            "জেনেটিক ইঞ্জিনিয়ারিং",
        ],
        "D", "easy", "application",
        "Human insulin genes are expressed in microbial hosts via genetic engineering for large-scale production.",
        "মানব ইনসুলিন জিন অণুজীব পোষকে জেনেটিক ইঞ্জিনিয়ারিং দিয়ে প্রকাশ করে বড় পরিসরে উৎপাদন হয়।",
    ),
    q(
        "Interferon is important because it can—",
        "ইন্টারফেরনের গুরুত্ব কী?",
        [
            "Inhibit viral multiplication and help against some cancers/viral diseases",
            "Only digest cellulose in the gut",
            "Only form plant cell walls",
            "Only fix atmospheric nitrogen",
        ],
        [
            "ভাইরাস বংশবৃদ্ধি বাধা দেয় এবং কিছু ক্যান্সার/ভাইরাস রোগে সহায়তা করে",
            "কেবল অন্ত্রে সেলুলোজ হজম করে",
            "কেবল উদ্ভিদ কোষপ্রাচীর গঠন করে",
            "কেবল বায়ুমণ্ডলীয় নাইট্রোজেন স্থিত করে",
        ],
        "A", "medium", "conceptual",
        "Interferons are proteins that interfere with viral replication and are used in therapies for certain viral and cancer conditions.",
        "ইন্টারফেরন প্রোটিন ভাইরাস অনুলিপনে বাধা দেয় এবং কিছু ভাইরাস ও ক্যান্সার চিকিৎসায় ব্যবহৃত হয়।",
    ),
    q(
        "Interferon is secreted mainly as a response from—",
        "ইন্টারফেরন প্রধানত কোন ধরনের সাড়া হিসেবে নিঃসৃত হয়?",
        [
            "Only mast cells in all cases",
            "Only uninfected resting bacteria",
            "Only healthy plant xylem",
            "Virus-infected (and related immune-response) cells",
        ],
        [
            "সব ক্ষেত্রে কেবল মাস্ট কোষ",
            "কেবল অসংক্রমিত নিষ্ক্রিয় ব্যাকটেরিয়া",
            "কেবল সুস্থ উদ্ভিদ জাইলেম",
            "ভাইরাস-আক্রান্ত (ও সংশ্লিষ্ট ইমিউন সাড়া) কোষ",
        ],
        "D", "medium", "factual",
        "Virus-infected cells release interferons that alert neighboring cells and modulate immunity.",
        "ভাইরাস-আক্রান্ত কোষ ইন্টারফেরন নিঃসৃত করে প্রতিবেশী কোষ ও ইমিউন প্রতিক্রিয়া প্রভাবিত করে।",
    ),
    q(
        "Which protein helps the human body resist cancer and viral spread as discussed in this chapter?",
        "এ অধ্যায়ে আলোচিত কোন প্রোটিন মানুষের শরীরে ক্যান্সার ও ভাইরাস বিস্তার রোধে সহায়ক?",
        ["Insulin", "Globulin only", "Interferon", "Somatostatin only"],
        ["ইনসুলিন", "কেবল গ্লোবিউলিন", "ইন্টারফেরন", "কেবল সোমাটোস্ট্যাটিন"],
        "C", "easy", "factual",
        "Texts highlight interferon for antiviral and anticancer therapeutic roles.",
        "পাঠ্যে ইন্টারফেরনকে অ্যান্টিভাইরাল ও অ্যান্টিক্যান্সার ভূমিকায় গুরুত্ব দেওয়া হয়।",
    ),
    q(
        "DNA fingerprinting can help identify—",
        "DNA ফিঙ্গারপ্রিন্ট এর মাধ্যমে শনাক্ত করা যায়—",
        [
            "Criminals; disputed parentage; close kinship relations",
            "Only the age of a rock",
            "Only the boiling point of water",
            "Only the color of chlorophyll",
        ],
        [
            "অপরাধী; বিতর্কিত পিতৃত্ব/মাতৃত্ব; নিকট আত্মীয়তার সম্পর্ক",
            "কেবল শিলার বয়স",
            "কেবল পানির স্ফুটনাঙ্ক",
            "কেবল ক্লোরোফিলের রঙ",
        ],
        "A", "easy", "application",
        "Individual-specific DNA patterns support forensics, paternity tests, and relatedness studies.",
        "ব্যক্তি-নির্দিষ্ট DNA প্যাটার্ন ফরেনসিক, পিতৃত্ব পরীক্ষা ও আত্মীয়তা নির্ধারণে কাজে লাগে।",
    ),
    q(
        "Genome sequencing applications include—",
        "জিনোম সিকোয়েন্সিং-এর প্রয়োগের মধ্যে আছে—",
        [
            "Criminal identification; cancer research; improving plant traits",
            "Only making yogurt",
            "Only counting leaf veins",
            "Only measuring humidity",
        ],
        [
            "অপরাধী শনাক্তকরণ; ক্যান্সার গবেষণা; উদ্ভিদের মান উন্নয়ন",
            "কেবল দই তৈরি",
            "কেবল পাতার শিরা গণনা",
            "কেবল আর্দ্রতা মাপা",
        ],
        "A", "medium", "application",
        "Sequence data aids forensics, disease research including cancer, and crop improvement strategies.",
        "সিকোয়েন্স তথ্য ফরেনসিক, ক্যান্সারসহ রোগ গবেষণা ও ফসল উন্নয়নে সহায়ক।",
    ),
    q(
        "A practical use of genome sequence information in society is—",
        "সমাজে জিনোম সিকোয়েন্স তথ্যের একটি ব্যবহারিক প্রয়োগ হলো—",
        [
            "Determining kinship/identity relationships",
            "Only producing callus on agar",
            "Only manufacturing wooden chairs",
            "Only forecasting tides without data",
        ],
        [
            "স্বজন/পরিচয় সম্পর্ক নির্ধারণ",
            "কেবল অ্যাগারে ক্যালাস তৈরি",
            "কেবল কাঠের চেয়ার তৈরি",
            "কেবল তথ্য ছাড়া জোয়ার পূর্বাভাস",
        ],
        "A", "medium", "application",
        "Sequence comparison supports relatedness and identity questions beyond simple morphology.",
        "সিকোয়েন্স তুলনা দিয়ে আত্মীয়তা ও পরিচয় সংক্রান্ত প্রশ্নের উত্তর পাওয়া যায়।",
    ),
    q(
        "GM crops are best described as crops whose—",
        "GM ফসল বলতে বোঝায় এমন ফসল যাদের—",
        [
            "Traits are improved by genetic modification (e.g., pest resistance)",
            "Seeds were never selected by humans",
            "DNA was removed entirely",
            "Cells lack any cytoplasm",
        ],
        [
            "জেনেটিক পরিবর্তনে বৈশিষ্ট্য উন্নত (যেমন বালাই প্রতিরোধ)",
            "মানুষ কখনো নির্বাচন করেনি",
            "DNA সম্পূর্ণ সরিয়ে ফেলা হয়েছে",
            "কোষে কোনো সাইটোপ্লাজম নেই",
        ],
        "A", "easy", "conceptual",
        "Genetically modified crops carry intentionally altered DNA for useful agricultural traits.",
        "জেনেটিক্যালি মডিফাইড ফসলে কাঙ্ক্ষিত কৃষি বৈশিষ্ট্যের জন্য DNA ইচ্ছাকৃত পরিবর্তন করা হয়।",
    ),
    q(
        "Why is a biosafety protocol important when releasing a new crop variety?",
        "নতুন শস্য ভ্যারাইটি অবমুক্তকরণে জীবনিরাপত্তা প্রোটোকল কেন জরুরি?",
        [
            "To assess and reduce health and environmental risks to humans and animals",
            "Only to increase advertisement costs",
            "Only to rename the crop every day",
            "Only to ban all farming forever",
        ],
        [
            "মানুষ ও প্রাণীর স্বাস্থ্য ও পরিবেশ ঝুঁকি মূল্যায়ন ও হ্রাস করতে",
            "কেবল বিজ্ঞাপন খরচ বাড়াতে",
            "কেবল প্রতিদিন ফসলের নাম বদলাতে",
            "কেবল চিরতরে সব চাষ নিষিদ্ধ করতে",
        ],
        "A", "medium", "conceptual",
        "Biosafety rules check whether new varieties (especially GM) pose immune/health or ecological risks before release.",
        "জীবনিরাপত্তা নীতিমালা নতুন (বিশেষত GM) জাত অবমুক্তির আগে স্বাস্থ্য ও পরিবেশ ঝুঁকি যাচাই করে।",
    ),
    q(
        "Which is an example of ancient/traditional biotechnology?",
        "প্রাচীন/প্রথাগত জীবপ্রযুক্তির উদাহরণ কোনটি?",
        [
            "Gene engineering of today only",
            "Making curd/yogurt by microbial fermentation",
            "Modern tissue culture labs only",
            "Only PCR machines",
        ],
        [
            "কেবল আজকের জিন প্রকৌশল",
            "অণুজীব ফার্মেন্টেশনে দই তৈরি",
            "কেবল আধুনিক টিস্যু কালচার ল্যাব",
            "কেবল PCR যন্ত্র",
        ],
        "B", "easy", "factual",
        "Fermented foods like curd are classic traditional biotech uses of microbes.",
        "দইয়ের মতো ফার্মেন্টেড খাদ্য অণুজীবের প্রাচীন জীবপ্রযুক্তি ব্যবহারের উদাহরণ।",
    ),
    q(
        "Recombinant DNA technology is used to produce all of the following EXCEPT—",
        "রিকম্বিনেন্ট DNA প্রযুক্তি দিয়ে নিচের কোনটি সাধারণত উৎপাদিত হয় না বলে পাঠ্যে আলাদা করা হয়?",
        [
            "Super/golden rice type GM traits",
            "Bt brinjal",
            "Pomato via protoplast fusion alone",
            "Many pharmaceutical proteins in microbes",
        ],
        [
            "সুপার/গোল্ডেন রাইস ধরনের GM বৈশিষ্ট্য",
            "Bt বেগুন",
            "কেবল প্রোটোপ্লাস্ট ফিউশনে পোম্যাটো",
            "অণুজীবে অনেক ঔষধি প্রোটিন",
        ],
        "C", "hard", "conceptual",
        "Board notes stress pomato from tissue/protoplast fusion, whereas Bt brinjal and golden rice involve recombinant DNA approaches.",
        "বোর্ড নোটে পোম্যাটো টিস্যু/প্রোটোপ্লাস্ট ফিউশনের; Bt বেগুন ও গোল্ডেন রাইস রিকম্বিনেন্ট DNA পথের।",
    ),
    q(
        "Which statements correctly describe applications of the illustrated rDNA pathway in crops/medicine?",
        "রিকম্বিনেন্ট DNA পথের প্রয়োগ সম্পর্কে কোনটি সঠিক?",
        [
            "Disease-resistant varieties; transgenic lines; insulin production",
            "Only measuring leaf thickness",
            "Only counting petals",
            "Only painting flower pots",
        ],
        [
            "রোগপ্রতিরোধী জাত; ট্রান্সজেনিক লাইন; ইনসুলিন উৎপাদন",
            "কেবল পাতার পুরুত্ব মাপা",
            "কেবল পাপড়ি গণনা",
            "কেবল ফুলদানি রং করা",
        ],
        "A", "medium", "application",
        "The same molecular toolkit supports transgenic pest/disease resistance and microbial production of insulin.",
        "একই আণবিক টুলকিট ট্রান্সজেনিক রোগ/পোকা প্রতিরোধ ও অণুজীবে ইনসুলিন উৎপাদনে ব্যবহৃত।",
    ),
    q(
        "Tissue-culture plantlets help agriculture by enabling—",
        "টিস্যু কালচারের চারা কৃষিতে সহায়তা করে—",
        [
            "Disease-free planting material; year-round production; controlled variation use",
            "Only permanent drought creation",
            "Only removal of all soil minerals",
            "Only stopping pollination forever",
        ],
        [
            "রোগমুক্ত রোপণ উপাদান; বছরজুড়ে উৎপাদন; নিয়ন্ত্রিত ভ্যারিয়েশন ব্যবহার",
            "কেবল স্থায়ী খরা সৃষ্টি",
            "কেবল সব মৃত্তিকা খনিজ অপসারণ",
            "কেবল চিরতরে পরাগায়ন বন্ধ",
        ],
        "A", "medium", "application",
        "Aseptic culture supplies clean planting stock anytime and can exploit somaclonal variation selectively.",
        "জীবাণুমুক্ত কালচার যেকোনো সময় পরিষ্কার চারা দেয় এবং সোমাক্লোনাল ভ্যারিয়েশন নির্বাচনী কাজে লাগে।",
    ),
    q(
        "Gene therapy is an application area linked with—",
        "জিন থেরাপি কোন ক্ষেত্রের প্রয়োগের সাথে যুক্ত?",
        [
            "Using genetic knowledge/tools to treat genetic disorders",
            "Only building concrete roads",
            "Only weaving cotton cloth",
            "Only boiling drinking water",
        ],
        [
            "জিনগত জ্ঞান/টুল দিয়ে জিনগত রোগের চিকিৎসা",
            "কেবল কংক্রিট রাস্তা নির্মাণ",
            "কেবল সুতির কাপড় বোনা",
            "কেবল পানীয় জল ফোটানো",
        ],
        "A", "medium", "conceptual",
        "Genome/sequence knowledge and gene tools underpin experimental gene therapy approaches.",
        "জিনোম/সিকোয়েন্স জ্ঞান ও জিন টুল পরীক্ষামূলক জিন থেরাপির ভিত্তি।",
    ),
    q(
        "Which pair correctly matches product and biotech route?",
        "কোন জোড়া সঠিকভাবে পণ্য ও জীবপ্রযুক্তি পথ মেলানো?",
        [
            "Bt brinjal — recombinant DNA; disease-free banana plantlets — tissue culture",
            "Bt brinjal — only yogurt fermentation; interferon — only grafting",
            "Golden rice — only agar solidification; callus — only DNA ligase",
            "Insulin — only meristem tip culture of rice",
        ],
        [
            "Bt বেগুন — রিকম্বিনেন্ট DNA; রোগমুক্ত কলা চারা — টিস্যু কালচার",
            "Bt বেগুন — কেবল দই ফার্মেন্টেশন; ইন্টারফেরন — কেবল কলম",
            "গোল্ডেন রাইস — কেবল অ্যাগার জমাট; ক্যালাস — কেবল DNA লাইগেজ",
            "ইনসুলিন — কেবল ধানের মেরিস্টেম টিপ কালচার",
        ],
        "A", "hard", "application",
        "Bt traits come from gene transfer; clean planting material for bananas often comes from tissue culture/micropropagation.",
        "Bt বৈশিষ্ট্য জিন স্থানান্তরের; কলার পরিষ্কার চারা প্রায়ই টিস্যু কালচার/মাইক্রোপ্রোপাগেশনের।",
    ),
]


def main() -> int:
    bundles = {
        "bio1_27_ch11_t01": T01,
        "bio1_27_ch11_t02": T02,
        "bio1_27_ch11_t03": T03,
    }
    TOPICS.mkdir(parents=True, exist_ok=True)
    counts: dict[str, int] = {}
    all_stems: dict[str, str] = {}
    invalid = 0
    duplicates = 0

    for tid, rows in bundles.items():
        if len(rows) != 20:
            raise SystemExit(f"{tid}: expected 20, got {len(rows)}")
        path = TOPICS / f"{tid}.jsonl"
        lines: list[str] = []
        for i, rec in enumerate(rows, 1):
            err = validate_record(rec)
            if err:
                invalid += 1
                print(f"INVALID {tid}#{i}: {err}")
            key = rec["stem_en"].strip().lower()
            if key in all_stems:
                duplicates += 1
                print(f"DUPLICATE stem with {all_stems[key]}: {tid}#{i}")
            else:
                all_stems[key] = tid
            lines.append(json.dumps(rec, ensure_ascii=False))
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        counts[tid] = len(rows)
        print(f"Wrote {path} ({len(rows)})")

    summary = {
        "chapter": "bio1_27_ch11",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p335_pdf341.png",
            "p336_pdf342.png",
            "p337_pdf343.png",
            "p338_pdf344.png",
            "p339_pdf345.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio1_27_ch11_t01": {
                "title": "Genetic engineering / জেনেটিক ইঞ্জিনিয়ারিং",
                "themes": [
                    "restriction enzymes as molecular scissors; EcoRI/BamHI/HindIII",
                    "plasmid vectors: circular dsDNA, self-replicating; E. coli host",
                    "ligase joining; sticky ends; transformation into competent cells",
                    "gene cloning vs genome sequencing; PCR denaturation ~90–95°C",
                    "rDNA changes genotype; insert checks via PCR/RE/probe",
                    "bacteria as vector/host and restriction-enzyme source",
                ],
            },
            "bio1_27_ch11_t02": {
                "title": "Tissue culture / টিস্যু কালচার",
                "themes": [
                    "Haberlandt as father; explant → medium → callus/plantlets",
                    "meristem culture for pathogen-free plantlets; anther/pollen haploids",
                    "agar gelling; minerals, vitamins, sucrose, phytohormones",
                    "micropropagation: clonal, fast, small space, year-round",
                    "pomato/cybrid via protoplast fusion; somaclonal variation",
                    "advantages when seed/vegetative propagation is difficult",
                ],
            },
            "bio1_27_ch11_t03": {
                "title": "Biotechnology applications / জীবপ্রযুক্তির প্রয়োগ",
                "themes": [
                    "Bt brinjal from B. thuringiensis; first BD-approved GM food",
                    "golden/super rice vitamin A; daffodil carotenoid genes",
                    "recombinant insulin protein; interferon antiviral/anticancer",
                    "DNA fingerprint & genome sequencing (forensics, kinship, cancer)",
                    "GM crops + biosafety protocol; yogurt as ancient biotech",
                    "match routes: rDNA crops/drugs vs tissue-culture planting stock",
                ],
            },
        },
        "low_confidence": [
            "OCR on p335–339 is noisy; figure-stimulus items rewritten as standalone stems.",
            "Short printed MCQ span (~5 pages); accurate HSC-level authored items supplement OCR reconstructions.",
            "Pomato classified as protoplast-fusion/cybrid path per Udvash notes (not typical rDNA crop list).",
            "Tissue-culture medium ingredient MCQs vary by board key; stem uses the full nutrient package.",
            "Biosafety item emphasizes health/environment risk assessment before variety release.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio1_27_ch11_* checked via validate_record)",
            "invalid": invalid,
            "duplicates": duplicates,
            "per_topic": counts,
        },
    }
    out = (
        ROOT
        / "content"
        / "bank"
        / "udvash_raw"
        / "biology_1"
        / "parsed"
        / "ch11_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    # Patch validate counts after run
    summary["validate"]["invalid"] = invalid
    summary["validate"]["duplicates"] = duplicates
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    if invalid or duplicates:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
