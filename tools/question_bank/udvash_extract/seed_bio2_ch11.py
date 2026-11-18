#!/usr/bin/env python3
"""Seed Biology 2nd Paper Ch11 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio2_27_ch11_t01..t03 (Mendelian inheritance; Genes and chromosomes; Evolution).
OCR ch11 covers printed pages ~337–343 (CQ + board MCQs); items reconstructed from
readable themes and standard HSC Zoology Ch11 facts.
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
    "biology p2 ch11; curated bilingual"
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


# --- t01: Mendelian inheritance / মেন্ডেলীয় বংশগতি ---
T01 = [
    q(
        "Who is regarded as the father of genetics?",
        "বংশগতিবিদ্যার জনক কে?",
        [
            "Gregor Johann Mendel",
            "Charles Robert Darwin",
            "Jean-Baptiste de Lamarck",
            "August Weismann",
        ],
        [
            "গ্রেগর জোহান মেন্ডেল",
            "চার্লস রবার্ট ডারউইন",
            "জ্যাঁ ব্যাপটিস্ট দ্য ল্যামার্ক",
            "আউগুস্ট ভাইজম্যান",
        ],
        "A", "easy", "factual",
        "Mendel’s pea experiments founded classical Mendelian genetics.",
        "মেন্ডেলের মটর গাছের পরীক্ষা ক্লাসিক্যাল বংশগতির ভিত্তি।",
    ),
    q(
        "Who first popularized the word Genetics for the science of heredity?",
        "বংশগতি বিজ্ঞানের জন্য Genetics শব্দ সর্বপ্রথম কে প্রচলন করেন?",
        [
            "William Bateson",
            "Gregor Mendel",
            "Hugo de Vries",
            "Thomas Morgan",
        ],
        [
            "উইলিয়াম বেটসন",
            "গ্রেগর মেন্ডেল",
            "হিউগো ডে ভ্রিস",
            "থমাস মরগান",
        ],
        "A", "easy", "factual",
        "William Bateson coined and promoted the term Genetics.",
        "উইলিয়াম বেটসন Genetics শব্দটি প্রচলন করেন।",
    ),
    q(
        "In a typical monohybrid cross with complete dominance, what is the F2 phenotypic ratio?",
        "পূর্ণ প্রকটতাসহ সাধারণ মনোহাইব্রিড ক্রসে F2 ফিনোটাইপিক অনুপাত কী?",
        [
            "3 : 1",
            "1 : 2 : 1",
            "9 : 3 : 3 : 1",
            "1 : 1",
        ],
        [
            "৩ : ১",
            "১ : ২ : ১",
            "৯ : ৩ : ৩ : ১",
            "১ : ১",
        ],
        "A", "easy", "factual",
        "Segregation with complete dominance yields about three dominant to one recessive phenotype.",
        "পূর্ণ প্রকটতায় প্রায় তিন ভাগ প্রকট ও এক ভাগ প্রচ্ছন্ন ফিনোটাইপ পাওয়া যায়।",
    ),
    q(
        "Mendel’s dihybrid cross with independent assortment typically gives which F2 phenotypic ratio?",
        "স্বাধীন সঞ্চারণসহ মেন্ডেলের ডাইহাইব্রিড ক্রসে সাধারণত কোন F2 ফিনোটাইপিক অনুপাত পাওয়া যায়?",
        [
            "9 : 3 : 3 : 1",
            "3 : 1",
            "1 : 2 : 1",
            "13 : 3",
        ],
        [
            "৯ : ৩ : ৩ : ১",
            "৩ : ১",
            "১ : ২ : ১",
            "১৩ : ৩",
        ],
        "A", "easy", "factual",
        "Independent assortment of two gene pairs produces the classic 9:3:3:1 ratio.",
        "দুই জোড়া জিনের স্বাধীন সঞ্চারণে ক্লাসিক ৯:৩:৩:১ অনুপাত হয়।",
    ),
    q(
        "How many distinct genotypes appear in the F2 of Mendel’s classic dihybrid cross?",
        "মেন্ডেলের ক্লাসিক ডাইহাইব্রিড ক্রসের F2-তে কত ধরনের জিনোটাইপ পাওয়া যায়?",
        [
            "9",
            "4",
            "16",
            "3",
        ],
        [
            "৯",
            "৪",
            "১৬",
            "৩",
        ],
        "A", "medium", "factual",
        "Among 16 equally likely zygotes there are nine different genotype classes.",
        "১৬টি সমসম্ভাব্য জাইগোটের মধ্যে নয়টি ভিন্ন জিনোটাইপ শ্রেণি থাকে।",
    ),
    q(
        "Incomplete dominance is best described by which outcome in F1?",
        "অসম্পূর্ণ প্রকটতায় F1-এ কোন ফল সবচেয়ে ভালোভাবে দেখা যায়?",
        [
            "An intermediate phenotype between the two parental extremes",
            "Only the dominant parental phenotype appears fully",
            "Both parental phenotypes appear fully side by side on every individual",
            "All F1 offspring die before birth",
        ],
        [
            "দুই পিতৃমাতৃ চরম বৈশিষ্ট্যের মাঝামাঝি একটি ফিনোটাইপ",
            "শুধু প্রকট পিতৃমাতৃ ফিনোটাইপ পূর্ণভাবে প্রকাশ",
            "প্রতিটি ব্যক্তিতে দুই পিতৃমাতৃ ফিনোটাইপই পূর্ণভাবে পাশাপাশি",
            "সব F1 সন্তান জন্মের আগেই মারা যায়",
        ],
        "A", "easy", "conceptual",
        "Heterozygotes show a blended intermediate trait, as in pink Mirabilis flowers.",
        "হেটারোজাইগোটে মাঝামাঝি বৈশিষ্ট্য প্রকাশ পায়, যেমন সন্ধ্যামালতীর গোলাপি ফুল।",
    ),
    q(
        "A red-flowered plant crossed with a white-flowered plant yields all pink F1 flowers. Which inheritance pattern is shown?",
        "লাল ফুলবিশিষ্ট উদ্ভিদের সাথে সাদা ফুলবিশিষ্ট উদ্ভিদের ক্রসে সব F1 গোলাপি হলে কোন বংশগতি দেখা যায়?",
        [
            "Incomplete dominance",
            "Complete dominance",
            "Dominant epistasis only",
            "Sex-linked inheritance only",
        ],
        [
            "অসম্পূর্ণ প্রকটতা",
            "পূর্ণ প্রকটতা",
            "শুধু প্রকট এপিস্ট্যাসিস",
            "শুধু সেক্স-লিংকড বংশগতি",
        ],
        "A", "easy", "application",
        "Pink F1 between red and white parents is the textbook incomplete-dominance result.",
        "লাল ও সাদার মাঝে গোলাপি F1 অসম্পূর্ণ প্রকটতার ক্লাসিক উদাহরণ।",
    ),
    q(
        "Under incomplete dominance, what is the usual F2 phenotypic ratio?",
        "অসম্পূর্ণ প্রকটতায় সাধারণ F2 ফিনোটাইপিক অনুপাত কী?",
        [
            "1 : 2 : 1",
            "3 : 1",
            "9 : 3 : 3 : 1",
            "13 : 3",
        ],
        [
            "১ : ২ : ১",
            "৩ : ১",
            "৯ : ৩ : ৩ : ১",
            "১৩ : ৩",
        ],
        "A", "medium", "factual",
        "Genotypic and phenotypic ratios both become 1:2:1 when dominance is incomplete.",
        "অসম্পূর্ণ প্রকটতায় জিনোটাইপিক ও ফিনোটাইপিক অনুপাতই ১:২:১ হয়।",
    ),
    q(
        "Codominance means which of the following in a heterozygote?",
        "সমপ্রকটতা হেটারোজাইগোটে কী বোঝায়?",
        [
            "Both alleles express their traits fully and simultaneously",
            "Neither allele is ever transcribed",
            "Only a diluted blend appears and neither allele product is detectable",
            "One allele permanently deletes the other from the chromosome",
        ],
        [
            "উভয় অ্যালিলের বৈশিষ্ট্যই পূর্ণ ও একসাথে প্রকাশিত হয়",
            "কোনো অ্যালিলই কখনো ট্রান্সক্রাইব হয় না",
            "শুধু লঘু মিশ্রণ দেখা যায় এবং কোনো অ্যালিল-উৎপাদই শনাক্ত হয় না",
            "এক অ্যালিল স্থায়ীভাবে অন্যটিকে ক্রোমোজোম থেকে মুছে ফেলে",
        ],
        "A", "easy", "conceptual",
        "In codominance both allele products appear distinctly in the heterozygote.",
        "সমপ্রকটতায় হেটারোজাইগোটে দুই অ্যালিলের প্রভাবই স্পষ্ট থাকে।",
    ),
    q(
        "Human AB blood group is a classic example of which Mendelian exception?",
        "মানুষের AB রক্ত গ্রুপ মেন্ডেলীয় কোন ব্যতিক্রমের ক্লাসিক উদাহরণ?",
        [
            "Codominance",
            "Incomplete dominance",
            "Complete dominance of O over A and B",
            "Lethal epistasis only",
        ],
        [
            "সমপ্রকটতা",
            "অসম্পূর্ণ প্রকটতা",
            "O-এর A ও B-এর উপর পূর্ণ প্রকটতা",
            "শুধু লিথাল এপিস্ট্যাসিস",
        ],
        "A", "easy", "factual",
        "IA and IB are codominant, so AB expresses both A and B antigens.",
        "IA ও IB সমপ্রকট, তাই AB গ্রুপে A ও B উভয় অ্যান্টিজেন থাকে।",
    ),
    q(
        "Black and white Andalusian fowl produce checkered (black-and-white) F1 offspring. What pattern is this?",
        "কালো ও সাদা আন্দালুসিয়ান মোরগ-মুরগির ক্রসে চেকযুক্ত F1 হলে কোন ধরনের বংশগতি?",
        [
            "Codominance",
            "Incomplete dominance only",
            "Sex-linked recessive inheritance",
            "Polygenic skin-color blending only",
        ],
        [
            "সমপ্রকটতা",
            "শুধু অসম্পূর্ণ প্রকটতা",
            "সেক্স-লিংকড প্রচ্ছন্ন বংশগতি",
            "শুধু পলিজেনিক ত্বকবর্ণ মিশ্রণ",
        ],
        "A", "medium", "application",
        "Checkered plumage shows both black and white alleles expressed together.",
        "চেকযুক্ত পালকে কালো ও সাদা অ্যালিল একসাথে প্রকাশ পায়।",
    ),
    q(
        "Which gene interaction commonly changes the dihybrid ratio to 13 : 3?",
        "কোন জিন ক্রিয়ার ফলে ডাইহাইব্রিড অনুপাত প্রায়ই ১৩ : ৩ হয়ে যায়?",
        [
            "Dominant epistasis",
            "Complementary gene action only",
            "Simple incomplete dominance",
            "Y-linked inheritance only",
        ],
        [
            "প্রকট এপিস্ট্যাসিস",
            "শুধু পরিপূরক জিন ক্রিয়া",
            "সরল অসম্পূর্ণ প্রকটতা",
            "শুধু Y-লিংকড বংশগতি",
        ],
        "A", "medium", "factual",
        "Dominant epistasis masks another locus and yields a 13:3 phenotypic split.",
        "প্রকট এপিস্ট্যাসিস অন্য লোকাসকে আড়াল করে ১৩:৩ অনুপাত দেয়।",
    ),
    q(
        "Complementary gene action in a dihybrid cross typically yields which F2 phenotypic ratio?",
        "ডাইহাইব্রিড ক্রসে পরিপূরক জিন ক্রিয়ায় সাধারণত কোন F2 ফিনোটাইপিক অনুপাত হয়?",
        [
            "9 : 7",
            "3 : 1",
            "1 : 2 : 1",
            "2 : 1",
        ],
        [
            "৯ : ৭",
            "৩ : ১",
            "১ : ২ : ১",
            "২ : ১",
        ],
        "A", "medium", "factual",
        "Both dominant alleles are needed for one phenotype, giving 9 colored : 7 white-type classes.",
        "এক ফিনোটাইপের জন্য উভয় প্রকট অ্যালিল লাগে বলে ৯:৭ অনুপাত হয়।",
    ),
    q(
        "Crossing white Leghorn (IICC) with white Wyandotte (iicc) often illustrates which interaction that can give 13 : 3 in F2?",
        "সাদা লেগহর্ন (IICC) ও সাদা ওয়াইনডট (iicc) ক্রস কোন জিন ক্রিয়ার উদাহরণ যা F2-তে ১৩ : ৩ দিতে পারে?",
        [
            "Dominant epistasis (inhibitor gene)",
            "Simple Mendelian complete dominance only",
            "Mitochondrial maternal inheritance only",
            "Holandric Y-linked transmission only",
        ],
        [
            "প্রকট এপিস্ট্যাসিস (ইনহিবিটর জিন)",
            "শুধু সরল মেন্ডেলীয় পূর্ণ প্রকটতা",
            "শুধু মাইটোকন্ড্রিয়াল মাতৃক বংশগতি",
            "শুধু হোল্যান্ড্রিক Y-লিংকড সঞ্চারণ",
        ],
        "A", "hard", "application",
        "An inhibitor (I) epistatically blocks color, producing mostly white and few colored F2 birds.",
        "ইনহিবিটর (I) বর্ণকে এপিস্ট্যাটিকভাবে আটকে বেশিরভাগ সাদা ও কম রঙিন F2 দেয়।",
    ),
    q(
        "For a recessive lethal allele that kills homozygotes, what live F2 phenotypic ratio is often observed among survivors?",
        "হোমোজাইগোটে মৃত্যু ঘটানো প্রচ্ছন্ন লিথাল অ্যালিলে জীবিতদের মধ্যে কোন ফিনোটাইপিক অনুপাত প্রায়ই দেখা যায়?",
        [
            "2 : 1",
            "3 : 1",
            "9 : 3 : 3 : 1",
            "1 : 1 : 1 : 1",
        ],
        [
            "২ : ১",
            "৩ : ১",
            "৯ : ৩ : ৩ : ১",
            "১ : ১ : ১ : ১",
        ],
        "A", "medium", "conceptual",
        "Lethal homozygous class is missing, leaving about two heterozygotes to one wild-type homozygote.",
        "লিথাল হোমোজাইগাস শ্রেণি অনুপস্থিত থাকে বলে প্রায় ২:১ অনুপাত থাকে।",
    ),
    q(
        "A back cross in Mendelian genetics typically means crossing F1 with which parent?",
        "মেন্ডেলীয় বংশগতিতে ব্যাক ক্রস সাধারণত F1-কে কার সাথে ক্রস করানো?",
        [
            "One of the parental (P) genotypes, often the recessive parent in a test cross",
            "Only an unrelated wild species from another genus",
            "Only F2 individuals among themselves without any parent",
            "Only somatic tissue culture cells without gametes",
        ],
        [
            "কোনো একটি পিতৃমাতৃ (P) জিনোটাইপের সাথে, টেস্ট ক্রসে প্রায়ই প্রচ্ছন্ন পিতামাতা",
            "শুধু অন্য গণের অসম্পর্কিত বন্য প্রজাতির সাথে",
            "শুধু F2 ব্যক্তিদের নিজেদের মধ্যে, কোনো পিতামাতা ছাড়া",
            "শুধু গ্যামেটবিহীন সোমাটিক টিস্যু কালচার কোষের সাথে",
        ],
        "A", "medium", "factual",
        "Back cross returns F1 to a P type; test cross specifically uses the recessive parent.",
        "ব্যাক ক্রসে F1-কে P-এর সাথে ফেরানো হয়; টেস্ট ক্রসে প্রচ্ছন্ন পিতামাতা ব্যবহার হয়।",
    ),
    q(
        "What does phenotype mean?",
        "ফিনোটাইপ বলতে কী বোঝায়?",
        [
            "The observable external or measurable traits of an organism",
            "Only the exact DNA sequence of every allele",
            "Only the number of chromosomes in the sperm",
            "Only the geological age of a fossil bed",
        ],
        [
            "জীবের পর্যবেক্ষণযোগ্য বাহ্যিক বা পরিমাপযোগ্য বৈশিষ্ট্য",
            "শুধু প্রতিটি অ্যালিলের সঠিক DNA সিকোয়েন্স",
            "শুধু শুক্রাণুর ক্রোমোজোম সংখ্যা",
            "শুধু জীবাশ্ম স্তরের ভূতাত্ত্বিক বয়স",
        ],
        "A", "easy", "factual",
        "Phenotype is the expressed appearance; genotype is the allelic constitution.",
        "ফিনোটাইপ প্রকাশিত রূপ; জিনোটাইপ অ্যালিলিক গঠন।",
    ),
    q(
        "If both parents have blood group A and can produce a group-O child, what is the chance of an O child?",
        "উভয় পিতামাতার রক্ত গ্রুপ A হলে এবং তারা O গ্রুপের সন্তান দিতে পারলে O সন্তানের সম্ভাবনা কত?",
        [
            "25%",
            "50%",
            "75%",
            "100%",
        ],
        [
            "২৫%",
            "৫০%",
            "৭৫%",
            "১০০%",
        ],
        "A", "medium", "numerical",
        "Heterozygous IA i × IA i yields ii (group O) in one of four combinations.",
        "হেটারোজাইগাস IA i × IA i ক্রসে চারটির একটিতে ii (O গ্রুপ) হয়।",
    ),
    q(
        "Which blood group is called the universal donor?",
        "কোন রক্ত গ্রুপকে সার্বজনীন দাতা বলা হয়?",
        [
            "O negative (O−)",
            "AB positive (AB+)",
            "A positive (A+)",
            "B positive (B+)",
        ],
        [
            "O নেগেটিভ (O−)",
            "AB পজিটিভ (AB+)",
            "A পজিটিভ (A+)",
            "B পজিটিভ (B+)",
        ],
        "A", "easy", "factual",
        "O− red cells lack A, B and RhD antigens, so they are safest as universal donor cells.",
        "O− লোহিত কণিকায় A, B ও RhD অ্যান্টিজেন নেই বলে সার্বজনীন দাতা।",
    ),
    q(
        "Skin-color variation between a dark-skinned and a light-skinned parent producing intermediate mulatto children is mainly which type of inheritance?",
        "গাঢ় ও হালকা ত্বকের পিতামাতার মাঝামাঝি মিউল্যাটো সন্তান মূলত কোন ধরনের বংশগতি?",
        [
            "Polygenic (multifactorial) inheritance",
            "Single-gene complete dominance only",
            "Strict Y-linked inheritance only",
            "Mitochondrial lethal inheritance only",
        ],
        [
            "পলিজেনিক (বহুজিনীয়) বংশগতি",
            "শুধু একজিনীয় পূর্ণ প্রকটতা",
            "শুধু কঠোর Y-লিংকড বংশগতি",
            "শুধু মাইটোকন্ড্রিয়াল লিথাল বংশগতি",
        ],
        "A", "medium", "conceptual",
        "Human skin color is controlled by several additive loci, a polygenic pattern.",
        "মানুষের ত্বকবর্ণ একাধিক যোগাত্মক লোকাস দ্বারা নিয়ন্ত্রিত পলিজেনিক বৈশিষ্ট্য।",
    ),
]


# --- t02: Genes and chromosomes / জিন ও ক্রোমোজোম ---
T02 = [
    q(
        "How many autosomes are present in a typical human somatic cell?",
        "মানবদেহের সাধারণ সোমাটিক কোষে কতটি অটোসোম থাকে?",
        [
            "44 (22 pairs)",
            "23 only",
            "46 sex chromosomes",
            "2 autosomes only",
        ],
        [
            "৪৪টি (২২ জোড়া)",
            "শুধু ২৩টি",
            "৪৬টি সেক্স ক্রোমোজোম",
            "শুধু ২টি অটোসোম",
        ],
        "A", "easy", "factual",
        "Humans have 22 pairs of autosomes plus one pair of sex chromosomes (46 total).",
        "মানুষে ২২ জোড়া অটোসোম ও এক জোড়া সেক্স ক্রোমোজোম (মোট ৪৬)।",
    ),
    q(
        "Sex-linked inheritance refers to transmission of traits controlled by genes on which chromosomes?",
        "সেক্স-লিংকড ইনহেরিট্যান্স কোন ক্রোমোজোমে অবস্থিত জিন দ্বারা নিয়ন্ত্রিত বৈশিষ্ট্যের সঞ্চারণ?",
        [
            "Sex chromosomes (X and/or Y)",
            "Only mitochondrial DNA outside the nucleus",
            "Only chromosome 1 autosome genes",
            "Only plastid genomes in plants transferred to humans",
        ],
        [
            "সেক্স ক্রোমোজোম (X এবং/অথবা Y)",
            "শুধু নিউক্লিয়াসের বাইরের মাইটোকন্ড্রিয়াল DNA",
            "শুধু ১ নম্বর অটোসোমের জিন",
            "শুধু উদ্ভিদের প্লাস্টিড জিনোম যা মানুষে স্থানান্তরিত",
        ],
        "A", "easy", "factual",
        "Sex-linked traits follow the inheritance pattern of X or Y chromosomes.",
        "সেক্স-লিংকড বৈশিষ্ট্য X বা Y ক্রোমোজোমের সঞ্চারণ অনুসরণ করে।",
    ),
    q(
        "Why is the father said to determine the sex of a human child?",
        "মানুষের সন্তানের লিঙ্গ নির্ধারণে পিতাকে দায়ী বলা হয় কেন?",
        [
            "Sperm are of two types (X-bearing and Y-bearing) while eggs are all X-bearing",
            "Eggs are of two types while all sperm carry only Y",
            "Only maternal mitochondria decide chromosomal sex",
            "Autosome number alone switches XX into XY after birth",
        ],
        [
            "শুক্রাণু দুই ধরনের (X-বাহী ও Y-বাহী) আর ডিম্বাণু সব X-বাহী",
            "ডিম্বাণু দুই ধরনের আর সব শুক্রাণু শুধু Y বহন করে",
            "শুধু মাতৃক মাইটোকন্ড্রিয়া ক্রোমোজোমীয় লিঙ্গ ঠিক করে",
            "শুধু অটোসোম সংখ্যা জন্মের পর XX-কে XY করে দেয়",
        ],
        "A", "easy", "conceptual",
        "Fertilization by X sperm yields XX (female); by Y sperm yields XY (male).",
        "X-শুক্রাণুতে XX (কন্যা) এবং Y-শুক্রাণুতে XY (পুত্র) হয়।",
    ),
    q(
        "Red–green colour blindness in humans is typically which kind of trait?",
        "মানুষের লাল-সবুজ বর্ণান্ধতা সাধারণত কোন ধরনের বৈশিষ্ট্য?",
        [
            "X-linked recessive",
            "Y-linked dominant only",
            "Autosomal lethal only",
            "Mitochondrial maternal only",
        ],
        [
            "X-লিংকড প্রচ্ছন্ন",
            "শুধু Y-লিংকড প্রকট",
            "শুধু অটোসোমাল লিথাল",
            "শুধু মাইটোকন্ড্রিয়াল মাতৃক",
        ],
        "A", "easy", "factual",
        "Colour-vision genes on the X chromosome make red–green colour blindness X-linked recessive.",
        "X ক্রোমোজোমের বর্ণ-দর্শন জিনের জন্য লাল-সবুজ বর্ণান্ধতা X-লিংকড প্রচ্ছন্ন।",
    ),
    q(
        "In which parental combination are all sons colour-blind?",
        "কোন পিতামাতার মিলনে সব পুত্র সন্তান বর্ণান্ধ হয়?",
        [
            "Colour-blind mother and normal father",
            "Normal homozygous mother and colour-blind father",
            "Carrier mother and normal father only",
            "Normal mother and normal father only",
        ],
        [
            "বর্ণান্ধ মা ও স্বাভাবিক পিতা",
            "স্বাভাবিক হোমোজাইগাস মা ও বর্ণান্ধ পিতা",
            "শুধু বাহক মা ও স্বাভাবিক পিতা",
            "শুধু স্বাভাবিক মা ও স্বাভাবিক পিতা",
        ],
        "A", "medium", "application",
        "A colour-blind mother (XcXc) passes Xc to every son, so all sons are colour-blind.",
        "বর্ণান্ধ মা (XcXc) প্রতি পুত্রকে Xc দেন, তাই সব পুত্র বর্ণান্ধ।",
    ),
    q(
        "A colour-blind daughter must have which parental situation?",
        "বর্ণান্ধ কন্যার ক্ষেত্রে পিতামাতার কোন অবস্থা থাকে?",
        [
            "Colour-blind father and at least carrier (or colour-blind) mother",
            "Only a colour-blind father with a homozygous normal mother",
            "Only a normal father with a homozygous normal mother",
            "Only Y-chromosome transfer from the mother",
        ],
        [
            "বর্ণান্ধ পিতা এবং অন্তত বাহক (বা বর্ণান্ধ) মা",
            "শুধু বর্ণান্ধ পিতা ও হোমোজাইগাস স্বাভাবিক মা",
            "শুধু স্বাভাবিক পিতা ও হোমোজাইগাস স্বাভাবিক মা",
            "শুধু মায়ের থেকে Y ক্রোমোজোম স্থানান্তর",
        ],
        "A", "hard", "application",
        "Daughters need Xc from father and Xc from mother to be colour-blind.",
        "কন্যা বর্ণান্ধ হতে পিতা ও মা উভয়ের থেকে Xc পেতে হয়।",
    ),
    q(
        "Classic haemophilia (haemophilia A) is mainly due to deficiency of which clotting factor?",
        "ক্লাসিক হিমোফিলিয়া (হিমোফিলিয়া A) মূলত কোন রক্তজমাট ফ্যাক্টরের অভাবে হয়?",
        [
            "Factor VIII",
            "Factor VII",
            "Factor XI",
            "Factor XIII",
        ],
        [
            "ফ্যাক্টর VIII",
            "ফ্যাক্টর VII",
            "ফ্যাক্টর XI",
            "ফ্যাক্টর XIII",
        ],
        "A", "medium", "factual",
        "Haemophilia A is an X-linked disorder from Factor VIII deficiency.",
        "হিমোফিলিয়া A হলো ফ্যাক্টর VIII অভাবজনিত X-লিংকড রোগ।",
    ),
    q(
        "A normal woman whose father was colour-blind marries a normal man. What is her genotype for the colour-vision locus?",
        "যার পিতা বর্ণান্ধ ছিলেন এমন স্বাভাবিক নারী স্বাভাবিক পুরুষকে বিয়ে করলে বর্ণদর্শন লোকাসে তার জিনোটাইপ কী?",
        [
            "Heterozygous carrier (XC Xc)",
            "Homozygous colour-blind (Xc Xc)",
            "XY male genotype",
            "Homozygous normal with no carrier risk (only if father were normal)",
        ],
        [
            "হেটারোজাইগাস বাহক (XC Xc)",
            "হোমোজাইগাস বর্ণান্ধ (Xc Xc)",
            "XY পুরুষ জিনোটাইপ",
            "বাহক ঝুঁকিহীন হোমোজাইগাস স্বাভাবিক (শুধু পিতা স্বাভাবিক হলে)",
        ],
        "A", "medium", "application",
        "She received Xc from her colour-blind father but appears normal, so she is a carrier.",
        "বর্ণান্ধ পিতা থেকে Xc পেয়েও স্বাভাবিক দেখালে তিনি বাহক।",
    ),
    q(
        "For that carrier woman and normal husband, what is expected among their sons regarding colour blindness?",
        "ঐ বাহক নারী ও স্বাভাবিক স্বামীর পুত্রদের মধ্যে বর্ণান্ধতা সম্পর্কে কী প্রত্যাশিত?",
        [
            "About 50% of sons colour-blind and 50% normal",
            "100% of sons colour-blind",
            "0% of sons can be colour-blind",
            "100% of daughters colour-blind",
        ],
        [
            "প্রায় ৫০% পুত্র বর্ণান্ধ ও ৫০% স্বাভাবিক",
            "১০০% পুত্র বর্ণান্ধ",
            "০% পুত্র বর্ণান্ধ হতে পারে না",
            "১০০% কন্যা বর্ণান্ধ",
        ],
        "A", "medium", "application",
        "Sons get either XC or Xc from the carrier mother; half are expected colour-blind.",
        "পুত্ররা বাহক মা থেকে XC বা Xc পায়; অর্ধেক বর্ণান্ধ হওয়ার সম্ভাবনা।",
    ),
    q(
        "Rh factor classification of blood is based on presence or absence of which kind of antigens on RBC membranes?",
        "Rh ব্লাডগ্রুপ শ্রেণিবিন্যাস লোহিত কণিকার ঝিল্লিতে কোন ধরনের অ্যান্টিজেনের উপস্থিতি-অনুপস্থিতির উপর নির্ভর করে?",
        [
            "Rhesus (Rh) antigens such as the C, D, E series",
            "Only ABO sugar antigens with no Rh molecules",
            "Only platelet collagen receptors",
            "Only nuclear histone proteins",
        ],
        [
            "রিসাস (Rh) অ্যান্টিজেন যেমন C, D, E সিরিজ",
            "শুধু ABO শর্করা অ্যান্টিজেন, কোনো Rh অণু নেই",
            "শুধু প্লাটিলেট কোলাজেন রিসেপ্টর",
            "শুধু নিউক্লিয়ার হিস্টোন প্রোটিন",
        ],
        "A", "medium", "factual",
        "Rh typing reflects Mendelian Rh antigens (notably D) on erythrocytes.",
        "Rh টাইপিং লোহিত কণিকার মেন্ডেলীয় Rh অ্যান্টিজেন (বিশেষত D) নির্দেশ করে।",
    ),
    q(
        "Which genotype set corresponds to Rh-positive blood among the options often cited in HSC texts?",
        "এইচএসসি পাঠ্যে উল্লিখিত কোন জিনোটাইপ সেট Rh-পজিটিভ রক্তের সাথে মিলে?",
        [
            "CDE (dominant Rh antigen set)",
            "cde only as the sole positive marker",
            "Absence of all C, D and E antigens",
            "Only mitochondrial Rh genes without nuclear alleles",
        ],
        [
            "CDE (প্রকট Rh অ্যান্টিজেন সেট)",
            "শুধু cde-ই একমাত্র পজিটিভ চিহ্নক",
            "সব C, D ও E অ্যান্টিজেনের অনুপস্থিতি",
            "শুধু নিউক্লিয়ার অ্যালিলবিহীন মাইটোকন্ড্রিয়াল Rh জিন",
        ],
        "A", "hard", "factual",
        "HSC texts treat C, D, E as Mendelian dominant Rh antigens marking Rh+ blood.",
        "পাঠ্যে C, D, E-কে Rh+ নির্দেশক মেন্ডেলীয় প্রকট অ্যান্টিজেন বলা হয়।",
    ),
    q(
        "Which blood group person is the universal recipient?",
        "কোন রক্ত গ্রুপের ব্যক্তি সার্বজনীন গ্রহীতা?",
        [
            "AB",
            "O",
            "A only",
            "B only",
        ],
        [
            "AB",
            "O",
            "শুধু A",
            "শুধু B",
        ],
        "A", "easy", "factual",
        "Group AB plasma lacks anti-A and anti-B, so AB can receive A, B, AB or O red cells (Rh matching aside).",
        "AB প্লাজমায় অ্যান্টি-A ও অ্যান্টি-B নেই বলে AB বিভিন্ন গ্রুপের রক্ত নিতে পারে।",
    ),
    q(
        "A person of blood group B can safely receive red cells from which groups (ignoring Rh for this item)?",
        "B রক্ত গ্রুপের ব্যক্তি কোন গ্রুপগুলো থেকে লোহিত কণিকা নিতে পারেন (এই প্রশ্নে Rh বাদ দিয়ে)?",
        [
            "B and O",
            "A and AB only",
            "AB and A only",
            "Only AB",
        ],
        [
            "B এবং O",
            "শুধু A এবং AB",
            "শুধু AB এবং A",
            "শুধু AB",
        ],
        "A", "medium", "application",
        "Anti-A in group B plasma rejects A/AB cells; B and O are compatible donors.",
        "B প্লাজমার অ্যান্টি-A A/AB প্রত্যাখ্যান করে; B ও O সামঞ্জস্যপূর্ণ দাতা।",
    ),
    q(
        "Which statement about AB blood is correct?",
        "AB রক্ত সম্পর্কে কোন উক্তি সঠিক?",
        [
            "Genotype IA IB; antigens A and B present; no anti-A or anti-B antibodies in plasma",
            "Genotype ii; no antigens; both anti-A and anti-B present",
            "Genotype IA IA only; only antigen B present",
            "Genotype IB IB only; only antigen A present",
        ],
        [
            "জিনোটাইপ IA IB; A ও B অ্যান্টিজেন আছে; প্লাজমায় অ্যান্টি-A বা অ্যান্টি-B নেই",
            "জিনোটাইপ ii; অ্যান্টিজেন নেই; অ্যান্টি-A ও অ্যান্টি-B দুটোই আছে",
            "শুধু জিনোটাইপ IA IA; শুধু B অ্যান্টিজেন আছে",
            "শুধু জিনোটাইপ IB IB; শুধু A অ্যান্টিজেন আছে",
        ],
        "A", "medium", "conceptual",
        "AB is IA IB with both antigens and neither anti-A nor anti-B.",
        "AB হলো IA IB—উভয় অ্যান্টিজেন আছে, অ্যান্টি-A/B নেই।",
    ),
    q(
        "Which blood group lacks A and B antibodies in plasma?",
        "কোন রক্ত গ্রুপের প্লাজমায় A ও B অ্যান্টিবডি থাকে না?",
        [
            "AB",
            "O",
            "A",
            "B",
        ],
        [
            "AB",
            "O",
            "A",
            "B",
        ],
        "A", "easy", "factual",
        "AB individuals do not make anti-A or anti-B; group O has both antibodies.",
        "AB-তে অ্যান্টি-A/B তৈরি হয় না; O-তে উভয় অ্যান্টিবডি থাকে।",
    ),
    q(
        "If the father is blood group A and the mother is AB, which child blood groups are possible?",
        "পিতার রক্ত গ্রুপ A এবং মায়ের AB হলে সন্তানের কোন গ্রুপ সম্ভব?",
        [
            "A, B and AB (not O)",
            "Only O",
            "Only O and B",
            "Only O and A",
        ],
        [
            "A, B এবং AB (O নয়)",
            "শুধু O",
            "শুধু O এবং B",
            "শুধু O এবং A",
        ],
        "A", "hard", "application",
        "Mother contributes IA or IB; father IA or i; combinations give A, B or AB, never ii (O).",
        "মা IA বা IB এবং পিতা IA বা i দিলে A, B বা AB হয়; ii (O) হয় না।",
    ),
    q(
        "Congenital ichthyosis in HSC genetics discussions is associated with which gene effect?",
        "এইচএসসি জিনতত্ত্ব আলোচনায় কনজেনিটাল ইকথিওসিস কোন জিন প্রভাবের সাথে যুক্ত?",
        [
            "Recessive lethal gene action affecting skin (fish-scale like cracking)",
            "Y-linked dominant feather colour only",
            "Simple incomplete dominance of flower colour only",
            "Mitochondrial deafness only",
        ],
        [
            "ত্বককে প্রভাবিত করা প্রচ্ছন্ন লিথাল জিন ক্রিয়া (মাছের আঁইশের মতো ফাটা)",
            "শুধু Y-লিংকড প্রকট পালকবর্ণ",
            "শুধু ফুলের রঙের সরল অসম্পূর্ণ প্রকটতা",
            "শুধু মাইটোকন্ড্রিয়াল বধিরতা",
        ],
        "A", "hard", "factual",
        "Texts link congenital ichthyosis to recessive lethal genes with severe skin scaling.",
        "পাঠ্যে কনজেনিটাল ইকথিওসিসকে তীব্র ত্বক আঁইশসহ প্রচ্ছন্ন লিথাল জিনের সাথে যুক্ত করা হয়।",
    ),
    q(
        "Two mute-deaf parents with complementary genotypes (e.g., DDee × ddEE) typically have what kind of children in F1?",
        "পরিপূরক জিনোটাইপবিশিষ্ট দুই মূক-বধির পিতামাতার (যেমন DDee × ddEE) F1 সন্তান সাধারণত কেমন হয়?",
        [
            "100% normal speech and hearing (DdEe)",
            "100% mute and deaf",
            "50% mute-deaf and 50% normal",
            "75% mute-deaf and 25% normal",
        ],
        [
            "১০০% স্বাভাবিক বাক্-শ্রবণক্ষম (DdEe)",
            "১০০% মূক ও বধির",
            "৫০% মূক-বধির ও ৫০% স্বাভাবিক",
            "৭৫% মূক-বধির ও ২৫% স্বাভাবিক",
        ],
        "A", "hard", "application",
        "Complementary dominant alleles restore normal hearing/speech in all F1 double heterozygotes.",
        "পরিপূরক প্রকট অ্যালিল সব F1 ডাবল হেটারোজাইগোটে স্বাভাবিক বাক্-শ্রবণ ফেরায়।",
    ),
    q(
        "Which option correctly lists a homozygous dominant genotype?",
        "কোন বিকল্প হোমোজাইগাস প্রকট জিনোটাইপ সঠিকভাবে নির্দেশ করে?",
        [
            "TT (two dominant alleles)",
            "Tt (one dominant and one recessive allele)",
            "tt (two recessive alleles)",
            "TY (a sex-chromosome pair, not a tall/short locus pair)",
        ],
        [
            "TT (দুটি প্রকট অ্যালিল)",
            "Tt (একটি প্রকট ও একটি প্রচ্ছন্ন অ্যালিল)",
            "tt (দুটি প্রচ্ছন্ন অ্যালিল)",
            "TY (সেক্স-ক্রোমোজোম জোড়া, লম্বা/বেটে লোকাস জোড়া নয়)",
        ],
        "A", "easy", "factual",
        "TT is homozygous dominant; Tt is heterozygous; tt is homozygous recessive.",
        "TT হোমোজাইগাস প্রকট; Tt হেটারোজাইগাস; tt হোমোজাইগাস প্রচ্ছন্ন।",
    ),
    q(
        "Which of the following is an exception to Mendel’s second law (independent assortment) when genes do not assort freely?",
        "জিন স্বাধীনভাবে সঞ্চারিত না হলে মেন্ডেলের দ্বিতীয় সূত্রের (স্বাধীন সঞ্চারণ) কোন ব্যতিক্রম ঘটে?",
        [
            "Gene linkage / linked genes on the same chromosome",
            "Simple monohybrid complete dominance alone",
            "Counting only phenotypic ratios of 3:1",
            "Presence of autosomes without sex chromosomes",
        ],
        [
            "জিন সংযোগ / একই ক্রোমোজোমে লিংকড জিন",
            "শুধু সরল মনোহাইব্রিড পূর্ণ প্রকটতা",
            "শুধু ৩:১ ফিনোটাইপিক অনুপাত গণনা",
            "সেক্স ক্রোমোজোম ছাড়া শুধু অটোসোমের উপস্থিতি",
        ],
        "A", "medium", "conceptual",
        "Linked genes travel together and violate free independent assortment.",
        "লিংকড জিন একসাথে সঞ্চারিত হয়ে স্বাধীন সঞ্চারণ ভঙ্গ করে।",
    ),
]


# --- t03: Evolution / বিবর্তন ---
T03 = [
    q(
        "Darwin’s greatest contribution is most associated with which field?",
        "ডারউইনের সবচেয়ে বড় অবদান কোন ক্ষেত্রের সাথে যুক্ত?",
        [
            "Evolution by natural selection",
            "Discovery of antibiotics",
            "Invention of the microscope",
            "Formulation of Mendel’s laws of heredity",
        ],
        [
            "প্রাকৃতিক নির্বাচনের মাধ্যমে বিবর্তন",
            "অ্যান্টিবায়োটিক আবিষ্কার",
            "অণুবীক্ষণ যন্ত্র উদ্ভাবন",
            "মেন্ডেলের বংশগতি সূত্র প্রণয়ন",
        ],
        "A", "easy", "factual",
        "Darwin explained origin of species mainly through natural selection.",
        "ডারউইন প্রাকৃতিক নির্বাচনের মাধ্যমে প্রজাতির উৎপত্তি ব্যাখ্যা করেন।",
    ),
    q(
        "Natural selection theory is also known as which -ism?",
        "প্রাকৃতিক নির্বাচন তত্ত্বকে অন্য কোন নামে ডাকা হয়?",
        [
            "Darwinism",
            "Lamarckism",
            "Mendelism only",
            "Weismannism only",
        ],
        [
            "ডারউইনিজম",
            "ল্যামার্কিজম",
            "শুধু মেন্ডেলিজম",
            "শুধু ভাইজম্যানিজম",
        ],
        "A", "easy", "factual",
        "Darwinism centres on natural selection and survival of the fittest.",
        "ডারউইনিজমের কেন্দ্রে প্রাকৃতিক নির্বাচন ও যোগ্যতমের উদ্বর্তন।",
    ),
    q(
        "Survival of the fittest means which of the following under Darwinism?",
        "ডারউইনবাদে Survival of the fittest বলতে কী বোঝায়?",
        [
            "Organisms with favourable variations survive struggle and leave more offspring",
            "Every acquired muscle enlargement is always inherited unchanged",
            "All species remain forever without any selection",
            "Only the largest fossils are preserved in museums",
        ],
        [
            "অনুকূল প্রকরণযুক্ত জীব জীবনসংগ্রামে টিকে বেশি সন্তান রাখে",
            "অর্জিত প্রতিটি পেশি বৃদ্ধিই সবসময় অপরিবর্তিতভাবে উত্তরাধিকারসূত্রে যায়",
            "সব প্রজাতি কোনো নির্বাচন ছাড়াই চিরকাল একই থাকে",
            "শুধু সবচেয়ে বড় জীবাশ্ম জাদুঘরে সংরক্ষিত হয়",
        ],
        "A", "easy", "conceptual",
        "Favourable variants win the struggle for existence and are selected naturally.",
        "অনুকূল প্রকরণ জীবনসংগ্রামে জয়ী হয়ে প্রাকৃতিকভাবে নির্বাচিত হয়।",
    ),
    q(
        "What is the central idea of Lamarckism regarding acquired characters?",
        "অর্জিত বৈশিষ্ট্য সম্পর্কে ল্যামার্কিজমের মূল ধারণা কী?",
        [
            "Characters acquired during life are inherited by offspring",
            "Only random DNA mutations create all new species overnight",
            "Natural selection alone, with no role for use and disuse",
            "Germplasm is isolated and somatic changes never matter in his view of use-inheritance",
        ],
        [
            "জীবদ্দশায় অর্জিত বৈশিষ্ট্য বংশধরে সঞ্চারিত হয়",
            "শুধু এলোমেলো DNA পরিব্যক্তি এক রাতে সব নতুন প্রজাতি তৈরি করে",
            "শুধু প্রাকৃতিক নির্বাচন, ব্যবহার-অব্যবহারের কোনো ভূমিকা নেই",
            "জার্মপ্লাজম বিচ্ছিন্ন এবং তার ব্যবহার-উত্তরাধিকার মতে সোমাটিক পরিবর্তনের কোনো গুরুত্ব নেই",
        ],
        "A", "easy", "conceptual",
        "Lamarck argued that use/disuse and acquired traits are passed to descendants.",
        "ল্যামার্ক মতে ব্যবহার/অব্যবহার ও অর্জিত বৈশিষ্ট্য বংশধরে যায়।",
    ),
    q(
        "Who proposed the mutation theory of evolution?",
        "বিবর্তনের পরিব্যক্তি মতবাদ কে দেন?",
        [
            "Hugo de Vries",
            "Charles Darwin",
            "Jean-Baptiste Lamarck",
            "August Weismann",
        ],
        [
            "হিউগো ডে ভ্রিস",
            "চার্লস ডারউইন",
            "জ্যাঁ ব্যাপটিস্ট ল্যামার্ক",
            "আউগুস্ট ভাইজম্যান",
        ],
        "A", "easy", "factual",
        "De Vries proposed that sudden mutations drive evolutionary change.",
        "ডে ভ্রিস হঠাৎ পরিব্যক্তিকে বিবর্তনের চালিকা বলে প্রস্তাব করেন।",
    ),
    q(
        "Who proposed the germplasm theory?",
        "জার্মপ্লাজম মতবাদ কে প্রবর্তন করেন?",
        [
            "August Weismann",
            "Ernst Haeckel",
            "Gregor Mendel",
            "Aristotle",
        ],
        [
            "আউগুস্ট ভাইজম্যান",
            "আর্নেস্ট হেকেল",
            "গ্রেগর মেন্ডেল",
            "অ্যারিস্টটল",
        ],
        "A", "easy", "factual",
        "Weismann’s germplasm theory separates hereditary germ line from soma.",
        "ভাইজম্যানের জার্মপ্লাজম মতবাদ বংশগতি রেখাকে সোমা থেকে আলাদা করে।",
    ),
    q(
        "Ontogeny recapitulates phylogeny is the slogan of which theory, and who is its main proponent?",
        "Ontogeny recapitulates phylogeny কোন মতবাদের স্লোগান এবং এর প্রধান প্রবক্তা কে?",
        [
            "Recapitulation theory; Ernst Haeckel",
            "Natural selection; Lamarck",
            "Germplasm theory; Darwin",
            "Mutation theory; Mendel",
        ],
        [
            "পুনরাবৃত্তি মতবাদ; আর্নেস্ট হেকেল",
            "প্রাকৃতিক নির্বাচন; ল্যামার্ক",
            "জার্মপ্লাজম মতবাদ; ডারউইন",
            "পরিব্যক্তি মতবাদ; মেন্ডেল",
        ],
        "A", "medium", "factual",
        "Haeckel’s recapitulation theory claims individual development repeats ancestral history.",
        "হেকেলের পুনরাবৃত্তি মতবাদ বলে ব্যক্তিজনি জাতিজনির পুনরাবৃত্তি করে।",
    ),
    q(
        "Homologous organs are best defined as organs that share which property?",
        "সমসংস্থ অঙ্গ কোন বৈশিষ্ট্য ভাগ করে?",
        [
            "Similar origin and basic structural plan, even if functions differ",
            "Identical function only, regardless of origin",
            "No anatomical relation at all",
            "Only temporary larval organs that vanish in adults of every phylum",
        ],
        [
            "একই উৎপত্তি ও মৌলিক গঠন পরিকল্পনা, কাজ ভিন্ন হলেও",
            "শুধু একই কাজ, উৎপত্তি যাই হোক",
            "কোনো শারীরবৃত্তীয় সম্পর্ক নেই",
            "শুধু সব পর্বের প্রাপ্তবয়স্কতে অদৃশ্য হওয়া অস্থায়ী লার্ভা অঙ্গ",
        ],
        "A", "easy", "conceptual",
        "Forelimbs of cat, whale flipper and bat wing are homologous despite different uses.",
        "বিড়ালের অগ্রপদ, তিমির ফ্লিপার ও বাদুরের ডানা কাজ ভিন্ন হলেও সমসংস্থ।",
    ),
    q(
        "Which of the following is an analogous organ pair/example?",
        "নিচের কোনটি সমবৃত্তীয় অঙ্গের উদাহরণ?",
        [
            "Wings of a bird and wings of a butterfly",
            "Forelimb of a cat and flipper of a whale",
            "Arm of a human and wing of a bat (homologous pair)",
            "Vertebral column of fish and human only as identical genes",
        ],
        [
            "পাখির ডানা ও প্রজাপতির ডানা",
            "বিড়ালের অগ্রপদ ও তিমির ফ্লিপার",
            "মানুষের বাহু ও বাদুরের ডানা (সমসংস্থ জোড়া)",
            "শুধু মাছ ও মানুষের কশেরুকাদণ্ড একই জিন হিসেবে",
        ],
        "A", "medium", "application",
        "Analogous organs perform similar functions but have different evolutionary origins.",
        "সমবৃত্তীয় অঙ্গের কাজ একই কিন্তু বিবর্তনীয় উৎপত্তি ভিন্ন।",
    ),
    q(
        "What is a living fossil?",
        "জীবন্ত জীবাশ্ম বলতে কী বোঝায়?",
        [
            "An ancient lineage that survives nearly unchanged while related groups went extinct",
            "Any recently extinct species known only from DNA in labs",
            "A mineral cast that never belonged to a living organism",
            "Only artificial plastic museum models",
        ],
        [
            "প্রাচীন বংশধারা যা প্রায় অপরিবর্তিত টিকে আছে অথচ সমগোত্রীয় দল বিলুপ্ত",
            "শুধু ল্যাবে DNA থেকে জানা যেকোনো সদ্য বিলুপ্ত প্রজাতি",
            "কখনো জীবিত জীবের অংশ নয় এমন খনিজ ছাঁচ",
            "শুধু কৃত্রিম প্লাস্টিক জাদুঘর মডেল",
        ],
        "A", "easy", "conceptual",
        "Living fossils bridge past and present as nearly unchanged survivors of old stocks.",
        "জীবন্ত জীবাশ্ম প্রাচীন গোষ্ঠীর প্রায় অপরিবর্তিত জীবিত নিদর্শন।",
    ),
    q(
        "Platypus (Ornithorhynchus) is called a living fossil mainly because it shows features of which transition?",
        "প্লাটিপাসকে (Ornithorhynchus) জীবন্ত জীবাশ্ম বলা হয় মূলত কোন উত্তরণের বৈশিষ্ট্য দেখানোর জন্য?",
        [
            "Reptile-like and mammal-like traits together",
            "Only pure fish scales with no mammalian traits",
            "Only insect wings with bird beaks",
            "Only flowering-plant wood anatomy",
        ],
        [
            "সরিসৃপসদৃশ ও স্তন্যপায়ীসদৃশ বৈশিষ্ট্য একসাথে",
            "শুধু বিশুদ্ধ মাছের আঁইশ, কোনো স্তন্যপায়ী বৈশিষ্ট্য নেই",
            "শুধু পতঙ্গের ডানা ও পাখির চঞ্চু",
            "শুধু সপুষ্পক উদ্ভিদের কাঠগঠন",
        ],
        "A", "medium", "factual",
        "Egg-laying and reptile-like urogenital traits plus hair and mammary glands mark the link.",
        "ডিমপাড়া ও সরিসৃপসদৃশ রেচন-জননসহ লোম ও স্তনগ্রন্থি সংযোগ নির্দেশ করে।",
    ),
    q(
        "Which of the following is often cited as a living fossil fish?",
        "নিচের কোনটিকে প্রায়ই জীবন্ত জীবাশ্ম মাছ হিসেবে উল্লেখ করা হয়?",
        [
            "Latimeria (coelacanth)",
            "Eohippus",
            "Archaeopteryx only as a modern aquarium fish",
            "Mesohippus",
        ],
        [
            "Latimeria (সিলাক্যান্থ)",
            "Eohippus (বৈজ্ঞানিক নাম)",
            "শুধু আধুনিক অ্যাকুয়ারিয়াম মাছ হিসেবে Archaeopteryx",
            "Mesohippus (বৈজ্ঞানিক নাম)",
        ],
        "A", "medium", "factual",
        "Latimeria is a classic living-fossil lobe-finned fish; Limulus and Sphenodon are other living fossils.",
        "Latimeria ক্লাসিক জীবন্ত জীবাশ্ম; Limulus ও Sphenodon-ও জীবন্ত জীবাশ্ম।",
    ),
    q(
        "Which fossil is the classic connecting link between reptiles and birds?",
        "সরিসৃপ ও পাখির মধ্যে ক্লাসিক সংযোগকারী জীবাশ্ম কোনটি?",
        [
            "Archaeopteryx",
            "Eohippus",
            "Mesohippus",
            "Pliohippus",
        ],
        [
            "Archaeopteryx (বৈজ্ঞানিক নাম)",
            "Eohippus (বৈজ্ঞানিক নাম)",
            "Mesohippus (বৈজ্ঞানিক নাম)",
            "Pliohippus (বৈজ্ঞানিক নাম)",
        ],
        "A", "easy", "factual",
        "Archaeopteryx combines reptilian and avian characters as a connecting fossil.",
        "Archaeopteryx সরিসৃপ ও পাখির বৈশিষ্ট্য মিলিয়ে সংযোগকারী জীবাশ্ম।",
    ),
    q(
        "Which is a reptilian character of Archaeopteryx among the following?",
        "নিচের কোনটি Archaeopteryx-এর সরিসৃপীয় বৈশিষ্ট্য?",
        [
            "Teeth present in the jaws",
            "Constant body temperature like modern birds only",
            "Complete absence of a long vertebral tail",
            "Presence of a furcula with no other reptile traits",
        ],
        [
            "চোয়ালে দাঁত বিদ্যমান",
            "শুধু আধুনিক পাখির মতো স্থির দেহতাপমাত্রা",
            "দীর্ঘ কশেরুকাযুক্ত লেজের সম্পূর্ণ অনুপস্থিতি",
            "অন্য কোনো সরিসৃপ বৈশিষ্ট্য ছাড়া শুধু ফারকুলার উপস্থিতি",
        ],
        "A", "medium", "factual",
        "Toothed jaws and a long bony tail are key reptilian features of Archaeopteryx.",
        "দাঁতযুক্ত চোয়াল ও দীর্ঘ অস্থিময় লেজ Archaeopteryx-এর মূল সরিসৃপ বৈশিষ্ট্য।",
    ),
    q(
        "Study of fossils is called which science?",
        "জীবাশ্ম সম্পর্কিত আলোচনাকে কোন বিজ্ঞান বলে?",
        [
            "Palaeontology",
            "Ornithology",
            "Entomology",
            "Ethology",
        ],
        [
            "প্যালিওন্টোলজি",
            "অর্নিথোলজি",
            "এনটোমোলজি",
            "ইথোলজি",
        ],
        "A", "easy", "factual",
        "Palaeontology is the scientific study of fossils.",
        "প্যালিওন্টোলজি হলো জীবাশ্মের বৈজ্ঞানিক অধ্যয়ন।",
    ),
    q(
        "Which geological era is called the Age of Reptiles?",
        "কোন ভূতাত্ত্বিক যুগকে সরিসৃপের যুগ বলা হয়?",
        [
            "Mesozoic",
            "Cenozoic",
            "Palaeozoic",
            "Archaeozoic",
        ],
        [
            "মেসোজয়িক",
            "সিনোজয়িক",
            "প্যালিওজয়িক",
            "আর্কিওজয়িক",
        ],
        "A", "easy", "factual",
        "Mesozoic (Triassic–Jurassic–Cretaceous) is the Age of Reptiles.",
        "মেসোজয়িক (ট্রায়াসিক–জুরাসিক–ক্রিটেসিয়াস) সরিসৃপের যুগ।",
    ),
    q(
        "Which era is called the Age of Mammals?",
        "কোন যুগকে স্তন্যপায়ীর যুগ বলা হয়?",
        [
            "Cenozoic",
            "Mesozoic",
            "Palaeozoic",
            "Proterozoic",
        ],
        [
            "সিনোজয়িক",
            "মেসোজয়িক",
            "প্যালিওজয়িক",
            "প্রোটেরোজয়িক",
        ],
        "A", "easy", "factual",
        "Cenozoic is dominated by mammalian diversification—the Age of Mammals.",
        "সিনোজয়িকে স্তন্যপায়ীর ব্যাপক বিকাশ—স্তন্যপায়ীর যুগ।",
    ),
    q(
        "Which of the following is a vestigial (rudimentary) organ in humans?",
        "মানুষের নিচের কোনটি নিষ্ক্রিয় (অবশিষ্টাংশ) অঙ্গ?",
        [
            "Muscles of the external ear (pinna muscles)",
            "Diaphragm used in breathing",
            "Functional eyeball muscles required for vision",
            "Active cardiac muscle of the heart wall",
        ],
        [
            "কানের বাইরের পেশি (পিনা পেশি)",
            "শ্বাসকাজে ব্যবহৃত ডায়াফ্রাম",
            "দর্শনের জন্য প্রয়োজনীয় কার্যকর চক্ষুপেশি",
            "হৃৎপিণ্ড প্রাচীরের সক্রিয় হৃদপেশি",
        ],
        "A", "medium", "factual",
        "Ear muscles, wisdom teeth and similar remnants are classic human vestigial organs.",
        "কানের পেশি, আক্কেল দাঁত ইত্যাদি মানুষের ক্লাসিক নিষ্ক্রিয় অঙ্গ।",
    ),
    q(
        "Evolution of closely related groups into different forms in different environments is called what?",
        "নিকট সম্পর্কিত জীবগোষ্ঠীর ভিন্ন পরিবেশে ভিন্ন রূপ ধারণকে কী বলে?",
        [
            "Divergent evolution",
            "Convergent evolution",
            "Parallel evolution only as identical twins",
            "Macro-mutation of a single cell overnight only",
        ],
        [
            "অপসারী বিবর্তন",
            "অভিসারী বিবর্তন",
            "শুধু অভিন্ন যমজ হিসেবে সমান্তরাল বিবর্তন",
            "শুধু এক কোষের একরাতের ম্যাক্রো-পরিব্যক্তি",
        ],
        "A", "medium", "conceptual",
        "Divergent evolution splits related lineages into dissimilar adaptive forms.",
        "অপসারী বিবর্তনে সম্পর্কিত বংশধারা ভিন্ন অভিযোজিত রূপে বিভক্ত হয়।",
    ),
    q(
        "Archaeopteryx is evidence for the evolutionary origin of which vertebrate class?",
        "Archaeopteryx কোন শ্রেণির বিবর্তনীয় উৎপত্তির প্রমাণ?",
        [
            "Aves (birds) from reptilian ancestors",
            "Osteichthyes only from amphibians overnight",
            "Amphibia only from mammals",
            "Reptilia only from modern whales",
        ],
        [
            "সরিসৃপ পূর্বপুরুষ থেকে Aves (পাখি)",
            "শুধু একরাতে উভচর থেকে Osteichthyes",
            "শুধু স্তন্যপায়ী থেকে Amphibia",
            "শুধু আধুনিক তিমি থেকে Reptilia",
        ],
        "A", "medium", "application",
        "Mixed reptile–bird characters in Archaeopteryx support avian origin from reptiles.",
        "Archaeopteryx-এর মিশ্র সরিসৃপ–পাখি বৈশিষ্ট্য পাখির সরিসৃপ উৎসের সমর্থন দেয়।",
    ),
]


TOPICS_MAP = {
    "bio2_27_ch11_t01": T01,
    "bio2_27_ch11_t02": T02,
    "bio2_27_ch11_t03": T03,
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
        "chapter": "bio2_27_ch11",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p337_pdf343.png",
            "p338_pdf344.png",
            "p339_pdf345.png",
            "p340_pdf346.png",
            "p341_pdf347.png",
            "p342_pdf348.png",
            "p343_pdf349.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio2_27_ch11_t01": {
                "title": "Mendelian inheritance / মেন্ডেলীয় বংশগতি",
                "themes": [
                    "Mendel as father of genetics; Bateson coined Genetics",
                    "monohybrid 3:1; dihybrid 9:3:3:1; F2 genotype classes",
                    "incomplete dominance (Mirabilis pink); F2 1:2:1; codominance",
                    "AB blood; Andalusian checkered plumage; epistasis 13:3; complementary 9:7",
                    "Leghorn×Wyandotte inhibitor; lethal 2:1; back/test cross; phenotype",
                    "A×A → O 25%; universal donor O−; polygenic skin colour",
                ],
            },
            "bio2_27_ch11_t02": {
                "title": "Genes and chromosomes / জিন ও ক্রোমোজোম",
                "themes": [
                    "44 autosomes; sex-linked inheritance; paternal sex determination",
                    "X-linked colour blindness; all sons colour-blind if mother affected",
                    "colour-blind daughter requires carrier/affected mother + affected father",
                    "haemophilia A / Factor VIII; carrier woman genotypes and 50% sons",
                    "Rh antigens C/D/E; universal recipient AB; B receives B/O",
                    "AB genotype IAIB; A×AB children; ichthyosis lethal; complementary mute-deaf",
                    "homozygous TT; linkage as exception to independent assortment",
                ],
            },
            "bio2_27_ch11_t03": {
                "title": "Evolution / বিবর্তন",
                "themes": [
                    "Darwinism / natural selection; survival of the fittest",
                    "Lamarck inheritance of acquired characters; de Vries mutation; Weismann germplasm",
                    "Haeckel recapitulation; homologous vs analogous organs",
                    "living fossils; platypus; Latimeria; Archaeopteryx connecting link",
                    "palaeontology; Mesozoic Age of Reptiles; Cenozoic Age of Mammals",
                    "vestigial ear muscles; divergent evolution; avian origin evidence",
                ],
            },
        },
        "low_confidence": [
            "OCR of printed pages p337–343 mixes CQ answers and board MCQs with noisy glyphs; stems authored/reconstructed as standalone bilingual items from readable themes and standard HSC Zoology Ch11 facts.",
            "Figure-/stimulus-linked pedigree and Punnett items rewritten without requiring the original diagram.",
            "Some answer keys (e.g. exact epistasis labeling 13:3 vs double-recessive variants; Rh genotype letter sets) follow common Bangladesh HSC textbook phrasing aligned with OCR options.",
            "Bank supplemented to exactly 20 items per syllabus topic where printed MCQ density alone was insufficient after deduplication.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio2_27_ch11_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio2_27_ch11_t01": 20,
                "bio2_27_ch11_t02": 20,
                "bio2_27_ch11_t03": 20,
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
        / "ch11_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
