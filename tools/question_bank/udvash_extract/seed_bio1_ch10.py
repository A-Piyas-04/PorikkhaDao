#!/usr/bin/env python3
"""Seed Biology 1st Paper Ch10 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio1_27_ch10_t01..t03 (pollination/fertilization; seeds/fruits; asexual).
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
    "biology p1 ch10; curated bilingual"
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


# --- t01: Pollination and fertilization / পরাগায়ন ও নিষেক ---
T01 = [
    q(
        "What is meant by double fertilization in flowering plants?",
        "আবৃতবীজী উদ্ভিদে দ্বিনিষেক বলতে কী বোঝায়?",
        [
            "Fusion of only one male gamete with the egg",
            "Simultaneous fusion of one male gamete with the egg and the other with the secondary nucleus",
            "Fusion of pollen tube with the style only",
            "Fusion of two eggs with one male gamete",
        ],
        [
            "কেবল একটি পুংগ্যামিটের সাথে ডিম্বাণুর মিলন",
            "একই সময়ে একটি পুংগ্যামিট ডিম্বাণুর সাথে ও অপরটি সেকেন্ডারি নিউক্লিয়াসের সাথে মিলিত হওয়া",
            "কেবল পরাগনালিকার সাথে গর্ভদণ্ডের মিলন",
            "এক পুংগ্যামিটের সাথে দুই ডিম্বাণুর মিলন",
        ],
        "B", "easy", "conceptual",
        "Double fertilization is the simultaneous syngamy and triple fusion characteristic of angiosperms.",
        "দ্বিনিষেক হলো আবৃতবীজীর বৈশিষ্ট্য—একই সাথে সিনগ্যামি ও ত্রিমিলন।",
    ),
    q(
        "Triple fusion involves which three nuclei?",
        "ত্রিমিলনে কোন তিনটি নিউক্লিয়াসের মিলন ঘটে?",
        [
            "Egg + two synergids",
            "Two polar nuclei + one male nucleus",
            "Two male nuclei + one synergid",
            "Egg + antipodal + male nucleus",
        ],
        [
            "ডিম্বাণু + দুই সহকারি কোষ",
            "দুই মেরু নিউক্লিয়াস + একটি পুংনিউক্লিয়াস",
            "দুই পুংনিউক্লিয়াস + একটি সহকারি কোষ",
            "ডিম্বাণু + প্রতিপাদ কোষ + পুংনিউক্লিয়াস",
        ],
        "B", "medium", "factual",
        "In triple fusion one male gamete fuses with the secondary (two polar) nuclei to form triploid endosperm.",
        "ত্রিমিলনে একটি পুংগ্যামিট দুই মেরু নিউক্লিয়াস গঠিত সেকেন্ডারি নিউক্লিয়াসের সাথে মিলিত হয়ে ট্রিপ্লয়েড এন্ডোস্পার্ম তৈরি করে।",
    ),
    q(
        "Double fertilization is a special feature of which plant group?",
        "দ্বিনিষেক কোন উদ্ভিদ গোষ্ঠীর বিশেষ বৈশিষ্ট্য?",
        ["Gymnosperms only", "Algae only", "Angiosperms", "Bryophytes only"],
        ["কেবল নগ্নবীজী", "কেবল শৈবাল", "আবৃতবীজী", "কেবল ব্রায়োফাইট"],
        "C", "easy", "factual",
        "Double fertilization (syngamy + triple fusion) is characteristic of angiosperms (with rare exceptions noted in texts).",
        "দ্বিনিষেক (সিনগ্যামি + ত্রিমিলন) আবৃতবীজী উদ্ভিদের বিশেষ বৈশিষ্ট্য।",
    ),
    q(
        "What is the main purpose of emasculation in artificial hybridization?",
        "কৃত্রিম সংকরায়নে ইমাস্কুলেশনের প্রধান উদ্দেশ্য কী?",
        [
            "To increase self-pollination",
            "To remove stamens before maturity so self-pollination cannot occur",
            "To remove the ovary only",
            "To force the flower to become male",
        ],
        [
            "স্বপরাগায়ন বাড়ানো",
            "পরিপক্বতার আগে পুংকেশর সরিয়ে স্বপরাগায়ন রোধ করা",
            "কেবল গর্ভাশয় অপসারণ",
            "ফুলকে পুংলিঙ্গে পরিণত করা",
        ],
        "B", "easy", "conceptual",
        "Emasculation removes immature stamens from the intended female (bisexual) flower so only desired pollen can fertilize it.",
        "ইমাস্কুলেশনে মাতৃপুষ্প থেকে অপরিপক্ব পুংকেশর সরিয়ে স্বপরাগায়ন রোধ করা হয়।",
    ),
    q(
        "Which statements correctly describe emasculation?",
        "ইমাস্কুলেশনের বৈশিষ্ট্য সম্পর্কে কোনগুলো সঠিক?",
        [
            "Stamen removal; occurs mainly in bisexual flowers; prevents self-pollination",
            "Occurs only in unisexual male flowers",
            "Removes the stigma only",
            "Always done after fruit set",
        ],
        [
            "পুংকেশর অপসারণ; মূলত উভলিঙ্গ ফুলে; স্বপরাগায়ন রোধ",
            "কেবল একলিঙ্গ পুং ফুলে ঘটে",
            "কেবল গর্ভমুণ্ড অপসারণ",
            "সবসময় ফল ধরার পর করা হয়",
        ],
        "A", "medium", "conceptual",
        "Board keys emphasize stamen removal in bisexual flowers to stop unwanted self-pollination before bagging/crossing.",
        "বোর্ড কী অনুসারে উভলিঙ্গ ফুলে পুংকেশর অপসারণ করে স্বপরাগায়ন রোধ করাই ইমাস্কুলেশন।",
    ),
    q(
        "Entry of the pollen tube through the micropyle is called what?",
        "মাইক্রোপাইল দিয়ে পরাগনালিকা প্রবেশকে কী বলে?",
        ["Porogamy", "Mesogamy", "Chalazogamy", "Syngamy"],
        ["পোরোগ্যামি", "মেসোগ্যামি", "ক্যালাজোগ্যামি", "সিনগ্যামি"],
        "A", "easy", "factual",
        "Porogamy = via micropyle; mesogamy via integument; chalazogamy via chalaza; syngamy is gamete fusion.",
        "পোরোগ্যামি = মাইক্রোপাইল দিয়ে; মেসোগ্যামি = ডিম্বকত্বক; ক্যালাজোগ্যামি = ক্যালাজা; সিনগ্যামি = গ্যামিট মিলন।",
    ),
    q(
        "Entry of the pollen tube through the integument is called what?",
        "ডিম্বকত্বক ভেদ করে পরাগনালিকা প্রবেশকে কী বলে?",
        ["Porogamy", "Mesogamy", "Chalazogamy", "Apogamy"],
        ["পোরোগ্যামি", "মেসোগ্যামি", "ক্যালাজোগ্যামি", "অ্যাপোগ্যামি"],
        "B", "medium", "factual",
        "Mesogamy is pollen-tube entry through the integument rather than micropyle or chalaza.",
        "মেসোগ্যামি হলো ডিম্বকত্বক দিয়ে পরাগনালিকার প্রবেশ।",
    ),
    q(
        "How many nuclei are present in the egg apparatus?",
        "ডিম্বাণুযন্ত্র কতটি নিউক্লিয়াস বিশিষ্ট?",
        ["One", "Two", "Three", "Eight"],
        ["এক", "দুই", "তিন", "আট"],
        "C", "easy", "factual",
        "The egg apparatus has one egg cell and two synergids — three nuclei in total.",
        "ডিম্বাণুযন্ত্রে একটি ডিম্বাণু ও দুই সহকারি কোষ—মোট তিন নিউক্লিয়াস।",
    ),
    q(
        "In about what percentage of flowering plants is the embryo sac formed by the monosporic process?",
        "শতকরা প্রায় কতটি উদ্ভিদে মনোস্পোরিক প্রক্রিয়ায় ভ্রূণথলি গঠিত হয়?",
        ["20%", "50%", "75%", "80%"],
        ["২০%", "৫০%", "৭৫%", "৮০%"],
        "D", "medium", "factual",
        "HSC texts commonly state that about 80% of angiosperms form a monosporic (Polygonum-type) embryo sac.",
        "HSC পাঠ্যে প্রায় ৮০% আবৃতবীজীতে মনোস্পোরিক (পলিগনাম টাইপ) ভ্রূণথলি গঠিত হয়।",
    ),
    q(
        "If a pollen sac has 25 pollen mother cells, how many pollen grains form after meiosis?",
        "একটি পরাগথলিতে ২৫টি পরাগ মাতৃকোষ থাকলে মিয়োসিসের পর কতটি পরাগরেণু তৈরি হবে?",
        ["25", "50", "75", "100"],
        ["২৫", "৫০", "৭৫", "১০০"],
        "D", "medium", "numerical",
        "Each PMC undergoes meiosis to yield 4 pollen grains; 25 × 4 = 100.",
        "প্রতি পরাগ মাতৃকোষ থেকে মিয়োসিসে ৪টি পরাগরেণু হয়; ২৫ × ৪ = ১০০।",
    ),
    q(
        "Which layer of the anther wall nourishes developing pollen grains?",
        "পরাগধানীর কোন স্তর বিকাশমান পরাগরেণুকে পুষ্টি জোগায়?",
        ["Epidermis", "Endothecium", "Tapetum", "Middle layer only"],
        ["এপিডার্মিস", "এন্ডোথেসিয়াম", "ট্যাপেটাম", "কেবল মধ্যস্তর"],
        "C", "easy", "factual",
        "The tapetum is the innermost nutritive layer of the anther wall for pollen development.",
        "ট্যাপেটাম পরাগধানীর অন্তঃতম পুষ্টিকর স্তর যা পরাগরেণু বিকাশে সহায়তা করে।",
    ),
    q(
        "The outer hard layer of a pollen grain wall is called what?",
        "পরাগরেণুর প্রাচীরের বাইরের শক্ত স্তরকে কী বলে?",
        ["Intine", "Exine", "Tapetum", "Nucellus"],
        ["ইন্টাইন", "এক্সাইন", "ট্যাপেটাম", "নিউসেলাস"],
        "B", "easy", "factual",
        "Exine is the outer sporopollenin-rich wall; intine is the inner cellulose/pectin layer.",
        "এক্সাইন বাইরের স্পোরোপলেনিন সমৃদ্ধ স্তর; ইন্টাইন ভিতরের সেলুলোজ/পেকটিন স্তর।",
    ),
    q(
        "The thin area of the pollen wall through which the pollen tube emerges is called what?",
        "পরাগপ্রাচীরের যে পাতলা অংশ দিয়ে পরাগনালিকা বের হয় তাকে কী বলে?",
        ["Intine", "Exine", "Germ pore", "Tapetum"],
        ["ইন্টাইন", "এক্সাইন", "জার্মপোর", "ট্যাপেটাম"],
        "C", "easy", "factual",
        "The germ pore is a thin exine region where the pollen tube usually emerges.",
        "জার্মপোর এক্সাইনের পাতলা অংশ; এখান দিয়ে সাধারণত পরাগনালিকা বের হয়।",
    ),
    q(
        "Orthotropous (atropous) ovules are typically seen in which plant?",
        "উর্ধ্বমুখী (অর্থোট্রপস) ডিম্বক সাধারণত কোন উদ্ভিদে দেখা যায়?",
        ["Bean (Shim)", "Opium poppy", "Mustard", "Piper (Panimirich)"],
        ["শিম", "আফিম", "সরিষা", "পানিমরিচ"],
        "D", "medium", "factual",
        "Orthotropous ovules occur in Piper, etc.; bean often anatropous; opium amphitropous; mustard campylotropous.",
        "পানিমরিচ ইত্যাদিতে উর্ধ্বমুখী; শিমে অধোমুখী; আফিমে পার্শ্বমুখী; সরিষায় বক্রমুখী ডিম্বক দেখা যায়।",
    ),
    q(
        "Campylotropous ovules are characteristically found in which plant?",
        "বক্রমুখী ডিম্বক কোন উদ্ভিদের বৈশিষ্ট্য?",
        ["Mustard", "Piper", "Bean", "Opium only"],
        ["সরিষা", "পানিমরিচ", "শিম", "কেবল আফিম"],
        "A", "medium", "factual",
        "Mustard (Brassica) is a standard textbook example of campylotropous ovules.",
        "সরিষা (Brassica) বক্রমুখী ডিম্বকের মানক উদাহরণ।",
    ),
    q(
        "Which statements correctly state the significance of fertilization?",
        "নিষেকের তাৎপর্য সম্পর্কে কোনগুলো সঠিক?",
        [
            "Maintains chromosome balance; can create high-yielding/tolerant crops; enables new genetic combinations",
            "Prevents all fruit and seed formation",
            "Always reduces genetic diversity to zero",
            "Occurs without any nuclear fusion",
        ],
        [
            "ক্রোমোজোম ভারসাম্য রক্ষা; অধিক ফলনশীল/সহনশীল ফসল; নতুন জেনেটিক সংমিশ্রণ",
            "সব ফল ও বীজ গঠন বন্ধ করে",
            "সবসময় জেনেটিক বৈচিত্র্য শূন্য করে",
            "কোনো নিউক্লিয়াস মিলন ছাড়াই ঘটে",
        ],
        "A", "medium", "conceptual",
        "Fertilization restores diploidy, produces seeds/fruits, and generates genetic variation useful in crop improvement.",
        "নিষেক ডিপ্লয়েডি রক্ষা, ফল-বীজ সৃষ্টি ও জেনেটিক বৈচিত্র্য তৈরি করে—ফসল উন্নয়নে গুরুত্বপূর্ণ।",
    ),
    q(
        "The generative nucleus of pollen divides by mitosis to form what?",
        "পরাগরেণুর জনন নিউক্লিয়াস মাইটোসিসে বিভাজিত হয়ে কী গঠন করে?",
        [
            "Two male gametes (sperm cells)",
            "One egg and one synergid",
            "Four megaspores",
            "Only the vegetative tube nucleus",
        ],
        [
            "দুই পুংগ্যামিট (শুক্রাণু)",
            "এক ডিম্বাণু ও এক সহকারি কোষ",
            "চার মেগাস্পোর",
            "কেবল নালিকা নিউক্লিয়াস",
        ],
        "A", "easy", "factual",
        "The generative cell/nucleus divides mitotically into two male gametes used in double fertilization.",
        "জনন নিউক্লিয়াস মাইটোসিসে দুই পুংগ্যামিট তৈরি করে যা দ্বিনিষেকে ব্যবহৃত হয়।",
    ),
    q(
        "Transfer of pollen from anther to stigma of the same flower is called what?",
        "একই ফুলের পরাগধানী থেকে গর্ভমুণ্ডে পরাগ স্থানান্তরকে কী বলে?",
        ["Cross-pollination", "Self-pollination", "Double fertilization", "Apogamy"],
        ["পরপরাগায়ন", "স্বপরাগায়ন", "দ্বিনিষেক", "অ্যাপোগ্যামি"],
        "B", "easy", "factual",
        "Self-pollination (autogamy) is pollen transfer within the same flower; cross-pollination involves different flowers/plants.",
        "স্বপরাগায়ন একই ফুলের মধ্যে; পরপরাগায়ন ভিন্ন ফুল/উদ্ভিদের মধ্যে ঘটে।",
    ),
    q(
        "In artificial hybridization, covering the emasculated flower to exclude unwanted pollen is called what?",
        "কৃত্রিম সংকরায়নে অবাঞ্ছিত পরাগ রোধে ইমাস্কুলেটেড ফুল ঢেকে রাখাকে কী বলে?",
        ["Bagging", "Tagging only", "Layering", "Grafting"],
        ["ব্যাগিং", "কেবল ট্যাগিং", "লেয়ারিং", "গ্রাফটিং"],
        "A", "easy", "factual",
        "Bagging isolates the flower after emasculation until controlled pollination and labeling/tagging.",
        "ইমাস্কুলেশনের পর ব্যাগিং করে নিয়ন্ত্রিত পরাগায়ন ও লেবেলিং/ট্যাগিং পর্যন্ত ফুল আলাদা রাখা হয়।",
    ),
    q(
        "The first cell of the male gametophyte in angiosperms is which structure?",
        "আবৃতবীজীতে পুংগ্যামিটোফাইটের প্রথম কোষ কোনটি?",
        ["Egg cell", "Pollen grain", "Zygote", "Endosperm nucleus"],
        ["ডিম্বাণু", "পরাগরেণু", "জাইগোট", "এন্ডোস্পার্ম নিউক্লিয়াস"],
        "B", "medium", "conceptual",
        "The pollen grain is the first cell of the male gametophyte; it later forms tube and generative nuclei.",
        "পরাগরেণু পুংগ্যামিটোফাইটের প্রথম কোষ; পরে নালিকা ও জনন নিউক্লিয়াস গঠিত হয়।",
    ),
]


# --- t02: Seeds and fruits / বীজ ও ফল ---
T02 = [
    q(
        "After fertilization, the ovule develops into which structure?",
        "নিষেকের পর ডিম্বক কিসে পরিণত হয়?",
        ["Fruit", "Seed", "Flower", "Endosperm only"],
        ["ফল", "বীজ", "ফুল", "কেবল এন্ডোস্পার্ম"],
        "B", "easy", "factual",
        "Fertilized ovule → seed; ovary → fruit; secondary nucleus product → endosperm.",
        "নিষিক্ত ডিম্বক → বীজ; গর্ভাশয় → ফল; সেকেন্ডারি নিউক্লিয়াসের ফল → এন্ডোস্পার্ম।",
    ),
    q(
        "After fertilization, the ovary develops into which structure?",
        "নিষেকের পর গর্ভাশয় কিসে পরিণত হয়?",
        ["Seed", "Fruit", "Pollen grain", "Ovule"],
        ["বীজ", "ফল", "পরাগরেণু", "ডিম্বক"],
        "B", "easy", "factual",
        "The ovary wall and ovary as a whole mature into the fruit enclosing seeds.",
        "গর্ভাশয় পরিণত হয়ে ফল গঠন করে এবং এর ভিতরে বীজ থাকে।",
    ),
    q(
        "The triploid nutritive tissue formed after triple fusion is called what?",
        "ত্রিমিলনের পর গঠিত ট্রিপ্লয়েড পুষ্টিকর কলাটিকে কী বলে?",
        ["Pericarp", "Endosperm", "Testa", "Plumule"],
        ["পেলিকার্প", "এন্ডোস্পার্ম", "টেস্টা", "প্লুমিউল"],
        "B", "easy", "factual",
        "Triple fusion yields triploid endosperm that nourishes the developing embryo.",
        "ত্রিমিলনে ট্রিপ্লয়েড এন্ডোস্পার্ম তৈরি হয় যা ভ্রূণকে পুষ্টি জোগায়।",
    ),
    q(
        "Development of fruit without fertilization (often seedless) is called what?",
        "নিষেক ছাড়া ফল গঠনকে (প্রায়শই বীজহীন) কী বলে?",
        ["Parthenocarpy", "Porogamy", "Syngamy", "Chalazogamy"],
        ["পার্থেনোকার্পি", "পোরোগ্যামি", "সিনগ্যামি", "ক্যালাজোগ্যামি"],
        "A", "easy", "conceptual",
        "Parthenocarpy produces fruit without fertilization; auxin/gibberellin may induce it in horticulture.",
        "পার্থেনোকার্পিতে নিষেক ছাড়া ফল হয়; উদ্যানকৃষিতে অক্সিন/জিব্বারেলিন প্রয়োগে উদ্দীপিত করা যায়।",
    ),
    q(
        "Which plant hormone is commonly applied to induce parthenocarpy?",
        "পার্থেনোকার্পি প্ররোচিত করতে সাধারণত কোন হরমোন প্রয়োগ করা হয়?",
        ["Cytokinin only", "Abscisic acid only", "Auxin (or gibberellin)", "Ethylene only as the sole option"],
        ["কেবল সাইটোকাইনিন", "কেবল অ্যাবসিসিক অ্যাসিড", "অক্সিন (বা জিব্বারেলিন)", "কেবল ইথিলিনই একমাত্র বিকল্প"],
        "C", "medium", "factual",
        "Auxins (and often gibberellins) are classic inducers of parthenocarpic fruit set in HSC horticulture examples.",
        "HSC উদাহরণে অক্সিন (এবং প্রায়শই জিব্বারেলিন) পার্থেনোকার্পিক ফল গঠনে ব্যবহৃত হয়।",
    ),
    q(
        "The outer seed coat developed from the integument is called what?",
        "ডিম্বকত্বক থেকে গঠিত বীজের বাইরের আবরণকে কী বলে?",
        ["Endosperm", "Testa", "Cotyledon", "Hilum only"],
        ["এন্ডোস্পার্ম", "টেস্টা", "বীজপত্র", "কেবল হাইলাম"],
        "B", "easy", "factual",
        "The testa (seed coat) develops from ovule integuments; hilum is the scar of the funicle.",
        "টেস্টা ডিম্বকত্বক থেকে গঠিত বীজাবরণ; হাইলাম ডিম্বকমূলের সংযোগ দাগ।",
    ),
    q(
        "The scar on a seed marking the point of attachment of the funicle is called what?",
        "বীজে ডিম্বকমূলের সংযোগস্থল চিহ্নিত দাগকে কী বলে?",
        ["Micropyle", "Hilum", "Plumule", "Radicle"],
        ["মাইক্রোপাইল", "হাইলাম", "প্লুমিউল", "রেডিকেল"],
        "B", "easy", "factual",
        "Hilum is the funicular scar; micropyle is the small pore near it used in water entry during germination.",
        "হাইলাম ডিম্বকমূলের দাগ; মাইক্রোপাইল এর কাছের ছিদ্র যা অঙ্কুরোদগমে পানি প্রবেশে সাহায্য করে।",
    ),
    q(
        "In a dicot seed such as gram, the embryonic shoot tip is called what?",
        "ছোলার মতো দ্বিবীজপত্রী বীজে ভ্রূণীয় কাণ্ডপ্রান্তকে কী বলে?",
        ["Radicle", "Plumule", "Testa", "Endosperm"],
        ["রেডিকেল", "প্লুমিউল", "টেস্টা", "এন্ডোস্পার্ম"],
        "B", "easy", "factual",
        "Plumule → future shoot; radicle → future root; cotyledons store/absorb food.",
        "প্লুমিউল → ভবিষ্যৎ কাণ্ড; রেডিকেল → ভবিষ্যৎ মূল; বীজপত্র খাদ্য সঞ্চয়/শোষণ করে।",
    ),
    q(
        "Seeds that retain endosperm at maturity (e.g., castor, cereals) are called what?",
        "পরিপক্ব অবস্থায় এন্ডোস্পার্ম ধরে রাখে এমন বীজকে (যেমন রেড়ি, শস্য) কী বলে?",
        [
            "Non-albuminous (exalbuminous) seeds",
            "Albuminous (endospermic) seeds",
            "Apomictic seeds only",
            "Parthenocarpic fruits",
        ],
        [
            "অ্যালবুমিনবিহীন (এক্সঅ্যালবুমিনাস) বীজ",
            "অ্যালবুমিনাস (এন্ডোস্পার্মযুক্ত) বীজ",
            "কেবল অ্যাপোমিকটিক বীজ",
            "পার্থেনোকার্পিক ফল",
        ],
        "B", "medium", "conceptual",
        "Albuminous/endospermic seeds keep endosperm; non-albuminous seeds transfer food mainly into cotyledons.",
        "অ্যালবুমিনাস বীজে এন্ডোস্পার্ম থাকে; নন-অ্যালবুমিনাসে খাদ্য মূলত বীজপত্রে সঞ্চিত হয়।",
    ),
    q(
        "A fruit that develops from a single ovary of one flower is classified as what?",
        "একটি ফুলের একক গর্ভাশয় থেকে গঠিত ফলকে কী বলে?",
        ["Simple fruit", "Aggregate fruit", "Multiple (composite) fruit", "False fruit only"],
        ["সরল ফল", "পুঞ্জফল", "যৌগফল", "কেবল অপ্রকৃত ফল"],
        "A", "easy", "factual",
        "Simple fruit ← one ovary; aggregate ← many free carpels of one flower; multiple ← whole inflorescence.",
        "সরল ফল ← এক গর্ভাশয়; পুঞ্জফল ← এক ফুলের অনেক মুক্ত গর্ভপত্র; যৌগফল ← সমগ্র পুষ্পমঞ্জরি।",
    ),
    q(
        "A fruit formed from many free carpels of a single flower (e.g., custard apple) is called what?",
        "এক ফুলের অনেক মুক্ত গর্ভপত্র থেকে গঠিত ফলকে (যেমন আতা) কী বলে?",
        ["Simple fruit", "Aggregate fruit", "Caryopsis only", "Legume only"],
        ["সরল ফল", "পুঞ্জফল", "কেবল ক্যারিওপসিস", "কেবল লেগিউম"],
        "B", "medium", "factual",
        "Aggregate fruits arise from apocarpous gynoecia of one flower (e.g., Annona, strawberry receptacle with achenes).",
        "পুঞ্জফল এক ফুলের অ্যাপোকার্পাস গর্ভকেশর থেকে গঠিত (যেমন আতা)।",
    ),
    q(
        "Pineapple develops from an entire inflorescence and is therefore which fruit type?",
        "আনারস সমগ্র পুষ্পমঞ্জরি থেকে গঠিত বলে কোন ধরনের ফল?",
        ["Simple dry fruit", "Aggregate fruit", "Multiple (composite/sorosis) fruit", "Follicle"],
        ["সরল শুষ্ক ফল", "পুঞ্জফল", "যৌগফল (সোরোসিস)", "ফলিকল"],
        "C", "medium", "factual",
        "Multiple/composite fruits (sorosis in pineapple) form from a whole inflorescence.",
        "আনারসের যৌগফল (সোরোসিস) সমগ্র পুষ্পমঞ্জরি থেকে গঠিত হয়।",
    ),
    q(
        "In a cereal grain (caryopsis), the pericarp is fused with which layer?",
        "শস্যদানায় (ক্যারিওপসিস) পেলিকার্প কোন স্তরের সাথে মিশে থাকে?",
        ["Only the plumule", "The seed coat", "Only the radicle", "Only the hilum"],
        ["কেবল প্লুমিউল", "বীজাবরণ", "কেবল রেডিকেল", "কেবল হাইলাম"],
        "B", "medium", "conceptual",
        "In a caryopsis the fruit wall (pericarp) is fused with the seed coat, so grain = fruit + seed.",
        "ক্যারিওপসিসে পেলিকার্প বীজাবরণের সাথে মিশে থাকে—দানাটি ফল ও বীজ একসাথে।",
    ),
    q(
        "Monocot seeds typically have how many cotyledons?",
        "একবীজপত্রী বীজে সাধারণত কতটি বীজপত্র থাকে?",
        ["One", "Two", "Three", "None"],
        ["একটি", "দুটি", "তিনটি", "কোনোটিই নয়"],
        "A", "easy", "factual",
        "Monocots have one cotyledon (scutellum in grasses); dicots have two.",
        "একবীজপত্রীতে একটি বীজপত্র (ঘাসে স্কুটেলাম); দ্বিবীজপত্রীতে দুটি।",
    ),
    q(
        "Which part of the embryo grows downward to form the root system?",
        "ভ্রূণের কোন অংশ নিচের দিকে বৃদ্ধি পেয়ে মূলতন্ত্র গঠন করে?",
        ["Plumule", "Radicle", "Testa", "Pericarp"],
        ["প্লুমিউল", "রেডিকেল", "টেস্টা", "পেলিকার্প"],
        "B", "easy", "factual",
        "The radicle is the embryonic root; the plumule is the embryonic shoot.",
        "রেডিকেল ভ্রূণীয় মূল; প্লুমিউল ভ্রূণীয় কাণ্ডপ্রান্ত।",
    ),
    q(
        "False fruits develop with significant contribution from which extra-ovarian part?",
        "অপ্রকৃত ফল গঠনে গর্ভাশয়ের বাইরের কোন অংশের গুরুত্বপূর্ণ অবদান থাকে?",
        [
            "Only the egg cell",
            "Thalamus/receptacle or other floral parts",
            "Only the antipodals",
            "Only the tapetum",
        ],
        [
            "কেবল ডিম্বাণু",
            "থ্যালামাস/পুষ্পासन বা অন্য পুষ্পাংশ",
            "কেবল প্রতিপাদ কোষ",
            "কেবল ট্যাপেটাম",
        ],
        "B", "medium", "conceptual",
        "False (accessory) fruits such as apple involve fleshy thalamus; true fruits develop mainly from ovary.",
        "অপ্রকৃত ফলে (যেমন আপেল) মাংসল থ্যালামাসের অবদান থাকে; প্রকৃত ফল মূলত গর্ভাশয় থেকে।",
    ),
    q(
        "Which structure of the ovule usually becomes the micropyle of the seed?",
        "ডিম্বকের কোন অংশ সাধারণত বীজের মাইক্রোপাইলে পরিণত হয়?",
        [
            "The micropylar opening of the ovule",
            "The chalaza only",
            "The entire nucellus always disappears without a pore",
            "The anther tapetum",
        ],
        [
            "ডিম্বকের মাইক্রোপাইলার ছিদ্র",
            "কেবল ক্যালাজা",
            "সমগ্র নিউসেলাস সবসময় ছিদ্র ছাড়াই অদৃশ্য হয়",
            "পরাগধানীর ট্যাপেটাম",
        ],
        "A", "easy", "factual",
        "The ovule micropyle persists as the seed micropyle, important for water uptake at germination.",
        "ডিম্বকের মাইক্রোপাইল বীজেও থাকে এবং অঙ্কুরোদগমে পানি শোষণে গুরুত্বপূর্ণ।",
    ),
    q(
        "Nucellus remnant that persists around the embryo in some seeds (e.g., black pepper) is called what?",
        "কিছু বীজে (যেমন গোলমরিচ) ভ্রূণের চারপাশে অবশিষ্ট নিউসেলাসকে কী বলে?",
        ["Perisperm", "Pericarp", "Exine", "Coleoptile"],
        ["পেরিস্পার্ম", "পেলিকার্প", "এক্সাইন", "কলিওপটাইল"],
        "A", "hard", "factual",
        "Perisperm is persistent nucellus tissue storing food in some seeds; endosperm is from triple fusion.",
        "পেরিস্পার্ম অবশিষ্ট নিউসেলাস; এন্ডোস্পার্ম ত্রিমিলনজাত কলা।",
    ),
    q(
        "Which event must normally precede seed formation in sexual reproduction of angiosperms?",
        "আবৃতবীজীর যৌন প্রজননে বীজ গঠনের আগে সাধারণত কোন ঘটনা ঘটে?",
        [
            "Only vegetative budding",
            "Pollination followed by fertilization",
            "Only grafting",
            "Only leaf cutting",
        ],
        [
            "কেবল অঙ্গজ মুকুলোদ্গম",
            "পরাগায়ন ও তারপর নিষেক",
            "কেবল গ্রাফটিং",
            "কেবল পাতা কাটিং",
        ],
        "B", "easy", "conceptual",
        "Sexual seed set requires pollination and fertilization (except special apomictic/parthenocarpic cases).",
        "যৌন বীজ গঠনে সাধারণত পরাগায়ন ও নিষেক প্রয়োজন (অ্যাপোমিক্সিস/পার্থেনোকার্পি ব্যতিক্রম)।",
    ),
    q(
        "Which of the following is a dry dehiscent fruit that splits along two sutures?",
        "নিচের কোনটি দুই সেলাই বরাবর ফেটে যাওয়া শুষ্ক ডিহিসেন্ট ফল?",
        ["Caryopsis of rice", "Legume (pod) of pea", "Drupe of mango", "Berry of tomato"],
        ["ধানের ক্যারিওপসিস", "মটরের লেগিউম (শুঁটি)", "আমের ড্রুপ", "টমেটোর বেরি"],
        "B", "medium", "factual",
        "A legume is a dry fruit dehiscing along two sutures; caryopsis is indehiscent; mango/tomato are fleshy.",
        "লেগিউম দুই সেলাই দিয়ে ফাটে; ক্যারিওপসিস অডিহিসেন্ট; আম/টমেটো মাংসল ফল।",
    ),
]


# --- t03: Asexual reproduction / অযৌন প্রজনন ---
T03 = [
    q(
        "The terms 'stock' and 'scion' apply to which vegetative method?",
        "'স্টক' ও 'সায়ন' শব্দগুলি কোন অঙ্গজ পদ্ধতির ক্ষেত্রে প্রযোজ্য?",
        ["Cutting", "Budding only", "Grafting", "Layering only"],
        ["কাটিং", "কেবল বাডিং", "গ্রাফটিং", "কেবল লেয়ারিং"],
        "C", "easy", "factual",
        "In grafting, the scion (desired shoot) is joined to the stock (rooted plant); fruit/flower traits follow the scion.",
        "গ্রাফটিংয়ে সায়ন (উন্নত শাখা) স্টকের সাথে যুক্ত হয়; ফল-ফুলের গুণ সায়নের উপর নির্ভর করে।",
    ),
    q(
        "Why is grafting widely used in fruit and flower cultivation?",
        "ফল ও ফুল চাষে গ্রাফটিং ব্যাপকভাবে ব্যবহারের কারণ কী?",
        [
            "It always creates new species by meiosis",
            "It maintains improved cultivars by joining superior scion onto a suitable stock",
            "It removes the need for any roots",
            "It only works in algae",
        ],
        [
            "এটি সবসময় মিয়োসিসে নতুন প্রজাতি তৈরি করে",
            "উন্নত সায়নকে উপযুক্ত স্টকে জুড়ে উন্নত জাত বজায় রাখে",
            "এতে কোনো মূলের প্রয়োজন থাকে না",
            "এটি কেবল শৈবালে কাজ করে",
        ],
        "B", "medium", "conceptual",
        "Grafting clones desirable aerial traits of the scion while using stock for root vigor/disease resistance.",
        "গ্রাফটিং সায়নের কাঙ্ক্ষিত বৈশিষ্ট্য ক্লোন করে এবং স্টকের মূল শক্তি/রোগ প্রতিরোধ কাজে লাগায়।",
    ),
    q(
        "Vegetative propagation of potato (Solanum tuberosum) occurs mainly through which organ?",
        "গোল আলুর অঙ্গজ বংশবৃদ্ধি প্রধানত কোন অঙ্গের মাধ্যমে হয়?",
        ["Root", "Stem (tuber)", "Leaf", "Flower"],
        ["মূল", "কাণ্ড (কন্দ)", "পাতা", "ফুল"],
        "B", "easy", "factual",
        "Potato tuber is a modified stem with eyes (buds) used for vegetative propagation.",
        "আলুর কন্দ পরিবর্তিত কাণ্ড; চোখ (মুকুল) দিয়ে অঙ্গজ বংশবৃদ্ধি হয়।",
    ),
    q(
        "Which plant commonly propagates vegetatively by leaves?",
        "কোন উদ্ভিদ সাধারণত পাতা দিয়ে অঙ্গজ বংশবৃদ্ধি করে?",
        ["Bryophyllum (Pathorkuchi)", "Ginger", "Dahlia", "Potato"],
        ["পাথরকুচি", "আদা", "ডালিয়া", "আলু"],
        "A", "easy", "factual",
        "Bryophyllum produces plantlets on leaf margins; ginger uses rhizome; dahlia often root tubers; potato stem tuber.",
        "পাথরকুচি পাতার কিনারায় নতুন চারা গজায়; আদা রাইজোম; ডালিয়া মূলকন্দ; আলু কাণ্ডকন্দ।",
    ),
    q(
        "Dahlia, kakrol (teasle gourd) and pointed gourd (potol) commonly multiply by which organ?",
        "ডালিয়া, কাঁকরোল ও পটল সাধারণত কোন অঙ্গ দ্বারা বংশবৃদ্ধি করে?",
        ["Root", "Leaf only", "Flower only", "Pollen only"],
        ["মূল", "কেবল পাতা", "কেবল ফুল", "কেবল পরাগ"],
        "A", "medium", "factual",
        "Board keys list dahlia, kakrol and potol as root-propagated; olkocu (Amorphophallus) often by stem/corm.",
        "বোর্ড কীতে ডালিয়া, কাঁকরোল, পটল মূল দ্বারা; ওলকচু প্রায়শই কাণ্ড/কন্দ দ্বারা বংশবৃদ্ধি করে।",
    ),
    q(
        "Which plant multiplies by stem (not root) among the following?",
        "নিচের কোনটি মূল নয়, কাণ্ড দ্বারা বংশবিস্তার করে?",
        ["Dahlia", "Pointed gourd (potol)", "Olkochu (elephant foot yam)", "Kakrol"],
        ["ডালিয়া", "পটল", "ওলকচু", "কাঁকরোল"],
        "C", "medium", "factual",
        "Olkochu propagates by stem/corm; dahlia, potol and kakrol are cited as root propagators in HSC lists.",
        "ওলকচু কাণ্ড/কন্দ দ্বারা; ডালিয়া-পটল-কাঁকরোল HSC তালিকায় মূল দ্বারা।",
    ),
    q(
        "Ginger multiplies vegetatively mainly by which modified stem?",
        "আদা প্রধানত কোন পরিবর্তিত কাণ্ড দিয়ে অঙ্গজ বংশবৃদ্ধি করে?",
        ["Rhizome", "Bulbil only", "Phylloclade only", "Root tuber only"],
        ["রাইজোম", "কেবল বালবিল", "কেবল ফাইলোক্লেড", "কেবল মূলকন্দ"],
        "A", "easy", "factual",
        "Ginger rhizome is an underground stem used for vegetative planting.",
        "আদার রাইজোম ভূনিম্নস্থ কাণ্ড যা অঙ্গজ চাষে ব্যবহৃত হয়।",
    ),
    q(
        "Development of an embryo from the egg without fertilization is called what?",
        "নিষেক ছাড়া ডিম্বাণু থেকে ভ্রূণ সৃষ্টিকে কী বলে?",
        ["Parthenogenesis", "Syngamy", "Porogamy", "Triple fusion"],
        ["পার্থেনোজেনেসিস", "সিনগ্যামি", "পোরোগ্যামি", "ত্রিমিলন"],
        "A", "easy", "conceptual",
        "Parthenogenesis: unfertilized egg → embryo; may be haploid or diploid depending on type.",
        "পার্থেনোজেনেসিস: অনিষিক্ত ডিম্বাণু থেকে ভ্রূণ—হ্যাপ্লয়েড বা ডিপ্লয়েড প্রকারভেদে।",
    ),
    q(
        "Formation of an embryo from a somatic cell of the ovule (e.g., nucellus) is called what?",
        "ডিম্বকের দেহকোষ (যেমন নিউসেলাস) থেকে ভ্রূণ সৃষ্টিকে কী বলে?",
        ["Apospory", "Syngamy", "Emasculation", "Bagging"],
        ["অ্যাপোস্পোরি", "সিনগ্যামি", "ইমাস্কুলেশন", "ব্যাগিং"],
        "A", "medium", "factual",
        "Apospory produces an embryo sac/embryo pathway from somatic ovule cells (e.g., nucellus/integument).",
        "অ্যাপোস্পোরিতে নিউসেলাস/ডিম্বকত্বকের দেহকোষ থেকে ভ্রূণথলি/ভ্রূণ পথ তৈরি হয়।",
    ),
    q(
        "Embryo formation from a synergid or antipodal (not the egg) without fertilization is called what?",
        "নিষেক ছাড়া সহকারি বা প্রতিপাদ কোষ থেকে (ডিম্বাণু নয়) ভ্রূণ সৃষ্টিকে কী বলে?",
        ["Apogamy", "Porogamy", "Mesogamy", "Chalazogamy"],
        ["অ্যাপোগ্যামি", "পোরোগ্যামি", "মেসোগ্যামি", "ক্যালাজোগ্যামি"],
        "A", "medium", "factual",
        "Apogamy: embryo from embryo-sac cells other than the egg; porogamy/mesogamy/chalazogamy are pollen-tube entry modes.",
        "অ্যাপোগ্যামি: ডিম্বাণু ছাড়া ভ্রূণথলির অন্য কোষ থেকে ভ্রূণ; পোরো/মেসো/ক্যালাজোগ্যামি পরাগনালিকা প্রবেশপথ।",
    ),
    q(
        "Which process can produce a haploid plant from pollen/anther culture pathways in texts?",
        "পাঠ্য অনুসারে পরাগ/পরাগধানী পথ থেকে হ্যাপ্লয়েড উদ্ভিদ কোন প্রক্রিয়ায় পাওয়া যায়?",
        ["Androgenesis", "Porogamy", "Self-pollination only", "Layering"],
        ["অ্যান্ড্রোজেনেসিস", "পোরোগ্যামি", "কেবল স্বপরাগায়ন", "লেয়ারিং"],
        "A", "hard", "conceptual",
        "Androgenesis refers to embryo/plant development from male gametophytic cells (pollen/anther routes).",
        "অ্যান্ড্রোজেনেসিস পুংগ্যামিটোফাইটিক কোষ (পরাগ/অ্যানথার) থেকে ভ্রূণ/উদ্ভিদ গঠন।",
    ),
    q(
        "Which method is mainly used to create improved crop varieties by controlled crossing?",
        "নিয়ন্ত্রিত ক্রসিংয়ের মাধ্যমে উন্নত জাত সৃষ্টিতে প্রধানত কোন পদ্ধতি ব্যবহৃত হয়?",
        [
            "Parthenogenesis only",
            "Artificial hybridization (artificial breeding)",
            "Only natural selfing without selection",
            "Only leaf layering",
        ],
        [
            "কেবল পার্থেনোজেনেসিস",
            "কৃত্রিম সংকরায়ন (কৃত্রিম প্রজনন)",
            "কেবল নির্বাচনহীন প্রাকৃতিক স্বপরাগায়ন",
            "কেবল পাতা লেয়ারিং",
        ],
        "B", "easy", "conceptual",
        "Artificial hybridization combines chosen parental traits via emasculation, bagging, crossing and selection.",
        "কৃত্রিম সংকরায়নে ইমাস্কুলেশন, ব্যাগিং, ক্রসিং ও নির্বাচনের মাধ্যমে কাঙ্ক্ষিত গুণ একত্র করা হয়।",
    ),
    q(
        "In the hybridization sequence, removing stamens of the female parent flower is which step?",
        "সংকরায়ন ধাপে মাতৃপুষ্পের পুংকেশর অপসারণ কোন ধাপ?",
        ["Bagging", "Emasculation", "Labeling only", "Layering"],
        ["ব্যাগিং", "ইমাস্কুলেশন", "কেবল লেবেলিং", "লেয়ারিং"],
        "B", "easy", "factual",
        "Typical order: parent selection → emasculation → bagging → artificial pollination → tagging/labeling → selection.",
        "সাধারণ ধাপ: পিতামাতা নির্বাচন → ইমাস্কুলেশন → ব্যাগিং → কৃত্রিম পরাগায়ন → ট্যাগিং/লেবেলিং → নির্বাচন।",
    ),
    q(
        "Bending a stem to the soil so roots form while still attached to the parent is called what?",
        "মাতৃউদ্ভিদের সাথে যুক্ত অবস্থায় কাণ্ড মাটিতে নামিয়ে মূল গজানোকে কী বলে?",
        ["Layering", "Emasculation", "Triple fusion", "Porogamy"],
        ["লেয়ারিং", "ইমাস্কুলেশন", "ত্রিমিলন", "পোরোগ্যামি"],
        "A", "easy", "factual",
        "Layering induces adventitious roots on a stem still attached to the parent plant.",
        "লেয়ারিংয়ে মাতৃউদ্ভিদসংলগ্ন কাণ্ডে অস্থানিক মূল উৎপন্ন হয়।",
    ),
    q(
        "Separating a stem piece and planting it to form a new plant is called what?",
        "কাণ্ডের অংশ কেটে রোপণ করে নতুন উদ্ভিদ গঠনকে কী বলে?",
        ["Cutting", "Double fertilization", "Syngamy", "Chalazogamy"],
        ["কাটিং", "দ্বিনিষেক", "সিনগ্যামি", "ক্যালাজোগ্যামি"],
        "A", "easy", "factual",
        "Stem/root/leaf cuttings are common vegetative propagation techniques in horticulture.",
        "কাণ্ড/মূল/পাতার কাটিং উদ্যানকৃষিতে সাধারণ অঙ্গজ পদ্ধতি।",
    ),
    q(
        "Gootee (air layering) is mainly a form of which propagation method?",
        "গুটি কলম প্রধানত কোন বংশবৃদ্ধি পদ্ধতির রূপ?",
        ["Layering", "Sexual double fertilization", "Meiotic seed set only", "Emasculation"],
        ["লেয়ারিং", "যৌন দ্বিনিষেক", "কেবল মিয়োটিক বীজ গঠন", "ইমাস্কুলেশন"],
        "A", "medium", "factual",
        "Gootee is air layering: bark ringed, moist medium applied on the stem to induce roots before separation.",
        "গুটি কলম বায়ু লেয়ারিং—বাকল কেটে আর্দ্র মাধ্যম দিয়ে মূল গজিয়ে পরে আলাদা করা হয়।",
    ),
    q(
        "Which statement about asexual (vegetative) reproduction is correct?",
        "অযৌন (অঙ্গজ) প্রজনন সম্পর্কে কোনটি সঠিক?",
        [
            "Offspring are usually genetically identical to the parent",
            "It always requires double fertilization",
            "It always increases heterozygosity each generation",
            "It cannot be used in agriculture",
        ],
        [
            "বংশধর সাধারণত মাতৃউদ্ভিদের জিনগতভাবে অভিন্ন",
            "এতে সবসময় দ্বিনিষেক প্রয়োজন",
            "এতে প্রতি প্রজন্মে হেটেরোজাইগোসিটি বাড়ে",
            "কৃষিতে ব্যবহার করা যায় না",
        ],
        "A", "easy", "conceptual",
        "Vegetative clones preserve genotype; sexual reproduction reshuffles genes via meiosis and fertilization.",
        "অঙ্গজ ক্লোন জিনোটাইপ অক্ষুণ্ণ রাখে; যৌন প্রজনন মিয়োসিস-নিষেকে জিন পুনর্বিন্যাস করে।",
    ),
    q(
        "Haploid parthenogenesis is exemplified in HSC texts by which organism pair?",
        "HSC পাঠ্যে হ্যাপ্লয়েড পার্থেনোজেনেসিসের উদাহরণ কোন জোড়া?",
        [
            "Solanum nigrum and Orchis maculata",
            "Mango and coconut only",
            "Only Pinus and Cycas",
            "Only Spirogyra and Vaucheria",
        ],
        [
            "Solanum nigrum ও Orchis maculata",
            "কেবল আম ও নারকেল",
            "কেবল পাইন ও সাইকাস",
            "কেবল স্পাইরোগাইরা ও ভশেনিয়া",
        ],
        "A", "hard", "factual",
        "Texts cite Solanum nigrum, Orchis maculata for haploid and Parthenium/Taraxacum for diploid parthenogenesis.",
        "পাঠ্যে Solanum nigrum, Orchis maculata হ্যাপ্লয়েড এবং Parthenium/Taraxacum ডিপ্লয়েড পার্থেনোজেনেসিসের উদাহরণ।",
    ),
    q(
        "Budding (as vegetative grafting of a bud) joins a bud of the desired plant onto what?",
        "বাডিং (মুকুল কলম) এ কাঙ্ক্ষিত উদ্ভিদের মুকুল কীসের উপর যুক্ত করা হয়?",
        [
            "A suitable stock plant",
            "Only a pollen grain",
            "Only an embryo sac",
            "Only a fruit pericarp",
        ],
        [
            "উপযুক্ত স্টক উদ্ভিদের উপর",
            "কেবল একটি পরাগরেণুর উপর",
            "কেবল একটি ভ্রূণথলির উপর",
            "কেবল ফলের পেলিকার্পের উপর",
        ],
        "A", "medium", "factual",
        "In budding, a bud (scion tissue) is inserted into the stock; after union it grows into the desired shoot.",
        "বাডিংয়ে মুকুল স্টকে স্থাপন করা হয়; সংযোগের পর কাঙ্ক্ষিত শাখায় পরিণত হয়।",
    ),
    q(
        "Which plants among the following reproduce vegetatively by roots?",
        "নিচের কোনগুলো মূল দ্বারা অঙ্গজ জনন করে?",
        [
            "Dahlia and pointed gourd (potol)",
            "Only bryophyllum and ginger",
            "Only rice and wheat by flowers",
            "Only gymnosperms by cones",
        ],
        [
            "ডালিয়া ও পটল",
            "কেবল পাথরকুচি ও আদা",
            "কেবল ধান ও গম ফুল দ্বারা",
            "কেবল নগ্নবীজী শঙ্কু দ্বারা",
        ],
        "A", "medium", "factual",
        "Dahlia and potol are standard root-propagation examples; bryophyllum uses leaves and ginger rhizomes.",
        "ডালিয়া ও পটল মূল দ্বারা; পাথরকুচি পাতা এবং আদা রাইজোম ব্যবহার করে।",
    ),
]


TOPICS_MAP = {
    "bio1_27_ch10_t01": T01,
    "bio1_27_ch10_t02": T02,
    "bio1_27_ch10_t03": T03,
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
        "chapter": "bio1_27_ch10",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p309_pdf315.png",
            "p310_pdf316.png",
            "p311_pdf317.png",
            "p312_pdf318.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio1_27_ch10_t01": {
                "title": "Pollination and fertilization / পরাগায়ন ও নিষেক",
                "themes": [
                    "double fertilization & triple fusion (2 polar + 1 male)",
                    "emasculation + bagging in artificial hybridization",
                    "porogamy / mesogamy / chalazogamy pollen-tube entry",
                    "egg apparatus 3 nuclei; monosporic embryo sac ~80%",
                    "25 PMC → 100 pollen; tapetum / exine / germ pore",
                    "ovule types: Piper orthotropous; mustard campylotropous",
                ],
            },
            "bio1_27_ch10_t02": {
                "title": "Seeds and fruits / বীজ ও ফল",
                "themes": [
                    "ovule→seed; ovary→fruit; endosperm from triple fusion",
                    "parthenocarpy + auxin/GA induction",
                    "testa, hilum, micropyle, plumule, radicle",
                    "albuminous vs non-albuminous; monocot one cotyledon",
                    "simple / aggregate / multiple fruits; caryopsis fusion",
                    "false fruit thalamus; legume dehiscence; perisperm",
                ],
            },
            "bio1_27_ch10_t03": {
                "title": "Asexual reproduction / অযৌন প্রজনন",
                "themes": [
                    "grafting stock/scion; budding onto stock",
                    "potato stem tuber; bryophyllum leaf; ginger rhizome",
                    "dahlia/kakrol/potol by root; olkochu by stem",
                    "cutting, layering, gootee (air layering)",
                    "parthenogenesis, apospory, apogamy, androgenesis",
                    "artificial hybridization steps; clonal identity",
                ],
            },
        },
        "low_confidence": [
            "OCR on p309–312 is very noisy; many figure-stimulus items rewritten as standalone stems.",
            "Short printed MCQ span (~4 pages); accurate HSC-level authored items supplement OCR reconstructions.",
            "Monosporic embryo-sac percentage follows common BD board key (~80%).",
            "Root vs stem vegetative lists follow Udvash/board answer keys (dahlia/kakrol/potol root; olkochu stem).",
            "Perisperm and androgenesis items are syllabus-accurate but thin in the OCR pages.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio1_27_ch10_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio1_27_ch10_t01": 20,
                "bio1_27_ch10_t02": 20,
                "bio1_27_ch10_t03": 20,
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
        / "ch10_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
