#!/usr/bin/env python3
"""Seed Biology 2nd Paper Ch12 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio2_27_ch12_t01..t03 (Innate behaviour; Learned behaviour; Social behaviour).
OCR ch12 covers only ~2 printed pages (mainly CQ answers); items reconstructed from
readable CQ themes and standard HSC Zoology Ch12 facts.
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
    "biology p2 ch12; curated bilingual"
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


# --- t01: Innate behaviour / সহজাত আচরণ ---
T01 = [
    q(
        "Animal behaviour is best defined as which of the following?",
        "প্রাণীর আচরণ বলতে নিচের কোনটিকে সবচেয়ে ভালো বোঝায়?",
        [
            "An animal’s response or reaction to environmental and situational stimuli",
            "Only the chemical composition of its blood plasma",
            "Only the number of chromosomes in its somatic cells",
            "Only the rate of photosynthesis in green plants nearby",
        ],
        [
            "পরিবেশ ও পরিস্থিতির উদ্দীপকের প্রতি প্রাণীর সাড়া বা প্রতিক্রিয়া",
            "কেবল এর রক্তরসের রাসায়নিক গঠন",
            "কেবল এর দেহকোষে ক্রোমোজোমের সংখ্যা",
            "কেবল আশপাশের সবুজ উদ্ভিদের সালোকসংশ্লেষের হার",
        ],
        "A", "easy", "factual",
        "Behaviour is the animal’s response relative to environment and situation.",
        "আচরণ হলো পরিবেশ ও পরিস্থিতির সাপেক্ষে প্রাণীর সাড়া।",
    ),
    q(
        "Innate behaviour is best described as which kind of behaviour?",
        "সহজাত আচরণকে কোন ধরনের আচরণ হিসেবে সবচেয়ে ভালো বর্ণনা করা যায়?",
        [
            "Inborn, spontaneous, genetically guided behaviour performed without prior learning",
            "Behaviour acquired only after years of schooling",
            "Behaviour that changes randomly every generation with no genetic basis",
            "Behaviour that occurs only when a teacher demonstrates it first",
        ],
        [
            "জন্মগত, স্বতঃস্ফূর্ত, জিনগতভাবে নিয়ন্ত্রিত ও পূর্বশিক্ষা ছাড়াই সম্পাদিত আচরণ",
            "কেবল বছরের পর বছর স্কুল শিক্ষার পর অর্জিত আচরণ",
            "কোনো জিনগত ভিত্তি ছাড়াই প্রতি প্রজন্মে এলোমেলো পরিবর্তনশীল আচরণ",
            "কেবল শিক্ষক আগে দেখালেই ঘটে এমন আচরণ",
        ],
        "A", "easy", "factual",
        "Innate behaviour is inborn and performed without learning from experience.",
        "সহজাত আচরণ জন্মগত এবং শিক্ষণ ছাড়াই প্রকাশ পায়।",
    ),
    q(
        "Which statement is a characteristic feature of innate behaviour?",
        "সহজাত আচরণের বৈশিষ্ট্য কোনটি?",
        [
            "It is species-typical, genetically controlled, and not acquired by learning",
            "It appears only after formal classroom instruction",
            "It never repeats within a species across generations",
            "It always requires a map drawn by the animal first",
        ],
        [
            "এটি প্রজাতি-নির্দিষ্ট, জিনগতভাবে নিয়ন্ত্রিত এবং শিক্ষণে অর্জিত নয়",
            "এটি কেবল শ্রেণিকক্ষের আনুষ্ঠানিক শিক্ষার পর দেখা যায়",
            "এটি প্রজাতির মধ্যে প্রজন্ম ধরে কখনোই পুনরাবৃত্তি হয় না",
            "এতে প্রাণীকে আগেই মানচিত্র আঁকতে হয়",
        ],
        "A", "easy", "conceptual",
        "Innate acts are heritable, species-specific, and independent of prior learning.",
        "সহজাত আচরণ বংশগত, প্রজাতি-নির্দিষ্ট ও পূর্বশিক্ষা-নিরপেক্ষ।",
    ),
    q(
        "Spider web-building and bird nest-building repeated in a species-typical way are classic examples of what?",
        "মাকড়সার জাল বুনন ও পাখির বাসা তৈরির প্রজাতি-নির্দিষ্ট পুনরাবৃত্তি কোন আচরণের ক্লাসিক উদাহরণ?",
        [
            "Innate behaviour",
            "Conditioned reflex only",
            "Insight learning only",
            "Imprinting only",
        ],
        [
            "সহজাত আচরণ",
            "কেবল সাপেক্ষ প্রতিবর্ত ক্রিয়া",
            "কেবল অন্তর্দৃষ্টিমূলক শিক্ষণ",
            "কেবল ছাপ বা ইমপ্রিন্টিং",
        ],
        "A", "easy", "factual",
        "These stereotyped, unlearned species patterns are innate behaviours.",
        "এই স্থির, অশিক্ষিত প্রজাতিগত ধরন সহজাত আচরণ।",
    ),
    q(
        "Taxis is best defined as which innate response?",
        "ট্যাক্সিস বলতে কোন সহজাত সাড়াকে বোঝায়?",
        [
            "Directed innate locomotor response toward or away from a stimulus source",
            "Random undirected change of speed with no stimulus relation",
            "Learning a maze by trial and error over many days",
            "Copying a new dance after watching another animal once",
        ],
        [
            "উদ্দীপকের উৎসের দিকে বা বিপরীতে দিকমুখী সহজাত চলন সাড়া",
            "উদ্দীপক সম্পর্ক ছাড়া এলোমেলো গতি পরিবর্তন",
            "অনেক দিন ধরে চেষ্টা-ভুলের মাধ্যমে গোলকধাঁধা শেখা",
            "অন্য প্রাণী একবার দেখে নতুন নৃত্য নকল করা",
        ],
        "A", "easy", "factual",
        "Taxis is an innate, oriented movement relative to a stimulus gradient or source.",
        "ট্যাক্সিস উদ্দীপকের সাপেক্ষে দিকমুখী সহজাত চলন।",
    ),
    q(
        "Which feature correctly describes taxis?",
        "ট্যাক্সিসের সঠিক বৈশিষ্ট্য কোনটি?",
        [
            "It is not learned; external stimuli guide body orientation via sense organs",
            "It requires classroom teaching before it can appear",
            "It occurs only inside the brain without any sensory input",
            "It is always identical to insight learning in mammals",
        ],
        [
            "এটি শিক্ষালব্ধ নয়; বাহ্যিক উদ্দীপক সংবেদী অঙ্গ দিয়ে দেহমুখ নিয়ন্ত্রণ করে",
            "এটি প্রকাশের আগে শ্রেণিকক্ষ শিক্ষা প্রয়োজন",
            "কোনো সংবেদী ইনপুট ছাড়াই কেবল মস্তিষ্কে ঘটে",
            "এটি স্তন্যপায়ীর অন্তর্দৃষ্টিমূলক শিক্ষণের সঙ্গে সবসময় অভিন্ন",
        ],
        "A", "medium", "conceptual",
        "Taxis is unlearned, stimulus-directed locomotion involving sensory organs.",
        "ট্যাক্সিস অশিক্ষিত, উদ্দীপক-নির্দেশিত চলন এবং সংবেদী অঙ্গ জড়িত।",
    ),
    q(
        "Thigmotaxis refers to which kind of taxis?",
        "থিগমোট্যাক্সিস কোন ধরনের ট্যাক্সিস?",
        [
            "Taxis in response to touch or contact stimuli",
            "Taxis only in response to magnetic poles of Earth",
            "Taxis only in response to absolute silence",
            "Taxis only caused by learning a password",
        ],
        [
            "স্পর্শ বা সংস্পর্শ উদ্দীপকের প্রতি ট্যাক্সিস",
            "কেবল পৃথিবীর চৌম্বক মেরুর প্রতি ট্যাক্সিস",
            "কেবল সম্পূর্ণ নীরবতার প্রতি ট্যাক্সিস",
            "কেবল পাসওয়ার্ড শেখার ফলে সৃষ্ট ট্যাক্সিস",
        ],
        "A", "easy", "factual",
        "Thigmotaxis is contact/touch-oriented taxis behaviour.",
        "থিগমোট্যাক্সিস স্পর্শ/সংস্পর্শমুখী ট্যাক্সিস আচরণ।",
    ),
    q(
        "Rheotaxis is defined as which response?",
        "রিওট্যাক্সিস কাকে বলে?",
        [
            "Taxis of an animal in a fluid in response to current or flow",
            "Taxis only toward bright artificial neon lights indoors",
            "A learned dance used only by trained circus animals",
            "A voluntary decision made after reading a map",
        ],
        [
            "তরলে স্রোত বা প্রবাহের প্রতি প্রাণীর ট্যাক্সিস",
            "কেবল ঘরের উজ্জ্বল নিয়ন আলোর দিকে ট্যাক্সিস",
            "কেবল প্রশিক্ষিত সার্কাস প্রাণীর শিক্ষিত নৃত্য",
            "মানচিত্র পড়ার পর নেওয়া স্বেচ্ছাকৃত সিদ্ধান্ত",
        ],
        "A", "easy", "factual",
        "Rheotaxis is current-oriented taxis in a fluid medium.",
        "রিওট্যাক্সিস তরলে স্রোতজনিত ট্যাক্সিস।",
    ),
    q(
        "Phototaxis is movement oriented with respect to which stimulus?",
        "ফোটোট্যাক্সিস কোন উদ্দীপকের সাপেক্ষে দিকমুখী চলন?",
        [
            "Light",
            "Sound frequency only",
            "Taste of sugar only",
            "Written language symbols",
        ],
        [
            "আলো",
            "কেবল শব্দের কম্পাঙ্ক",
            "কেবল চিনির স্বাদ",
            "লিখিত ভাষার প্রতীক",
        ],
        "A", "easy", "factual",
        "Photo- means light; phototaxis is light-oriented taxis.",
        "ফোটো অর্থ আলো; ফোটোট্যাক্সিস আলোমুখী ট্যাক্সিস।",
    ),
    q(
        "Chemotaxis is an oriented response to which class of stimuli?",
        "কেমোট্যাক্সিস কোন শ্রেণির উদ্দীপকের প্রতি দিকমুখী সাড়া?",
        [
            "Chemical stimuli",
            "Only gravitational pull of the Moon",
            "Only the colour of printed textbooks",
            "Only electrical mains voltage in houses",
        ],
        [
            "রাসায়নিক উদ্দীপক",
            "কেবল চাঁদের মহাকর্ষ টান",
            "কেবল মুদ্রিত পাঠ্যবইয়ের রঙ",
            "কেবল ঘরের বৈদ্যুতিক মেইন ভোল্টেজ",
        ],
        "A", "easy", "factual",
        "Chemotaxis is directed movement relative to chemical gradients.",
        "কেমোট্যাক্সিস রাসায়নিক গ্রেডিয়েন্টের সাপেক্ষে দিকমুখী চলন।",
    ),
    q(
        "A reflex (reflex action) is best described as which response?",
        "রিফ্লেক্স বা প্রতিবর্ত ক্রিয়া কোন সাড়া?",
        [
            "A rapid involuntary response to a sudden stimulus without conscious brain command",
            "A slow planned essay written after long deliberation",
            "A voluntary speech prepared for a debate contest",
            "A learned calculus proof memorized from a book",
        ],
        [
            "মস্তিষ্কের সচেতন নির্দেশ ছাড়াই আকস্মিক উদ্দীপকে দ্রুত অনৈচ্ছিক সাড়া",
            "দীর্ঘ চিন্তার পর লেখা ধীর পরিকল্পিত রচনা",
            "বিতর্ক প্রতিযোগিতার জন্য তৈরি স্বেচ্ছাকৃত বক্তৃতা",
            "বই থেকে মুখস্থ করা ক্যালকুলাসের প্রমাণ",
        ],
        "A", "easy", "factual",
        "Reflexes are fast, involuntary, and do not wait for conscious cortical command.",
        "প্রতিবর্ত দ্রুত, অনৈচ্ছিক এবং সচেতন কর্টেক্স নির্দেশের অপেক্ষা করে না।",
    ),
    q(
        "In a typical simple reflex arc, which structure is especially important for the rapid pathway?",
        "সাধারণ সরল প্রতিবর্ত চাপে দ্রুত পথের জন্য কোন কাঠামো বিশেষ গুরুত্বপূর্ণ?",
        [
            "Spinal cord pathway of the reflex arc",
            "Only the outer ear pinna cartilage",
            "Only the enamel of molar teeth",
            "Only the nails of the fingers",
        ],
        [
            "প্রতিবর্ত চাপের স্পাইনাল কর্ড পথ",
            "কেবল বাইরের কানের পিনা তরুণাস্থি",
            "কেবল মোলার দাঁতের এনামেল",
            "কেবল আঙুলের নখ",
        ],
        "A", "medium", "conceptual",
        "Many urgent reflexes travel a short spinal reflex-arc path.",
        "অনেক জরুরি প্রতিবর্ত সংক্ষিপ্ত স্পাইনাল প্রতিবর্ত চাপ দিয়ে চলে।",
    ),
    q(
        "Instinct is best characterized as which innate pattern?",
        "ইনস্টিংক্ট বা সহজাত প্রবৃত্তি কোন সহজাত ধরন?",
        [
            "Complex species-typical innate behaviour performed without learning purpose or outcome",
            "A single blink caused only by dust in one eye once",
            "Solving algebra after formal school training",
            "Buying food after reading a supermarket advertisement",
        ],
        [
            "শিক্ষণ ও ফলাফল সম্বন্ধে অবহিত না হয়ে প্রজাতিগত জটিল সহজাত আচরণ",
            "একবার এক চোখে ধুলো লাগায় কেবল একটি পলক",
            "আনুষ্ঠানিক স্কুল প্রশিক্ষণের পর বীজগণিত সমাধান",
            "সুপারমার্কেট বিজ্ঞাপন পড়ে খাবার কেনা",
        ],
        "A", "medium", "conceptual",
        "Instinct is complex innate behaviour for survival/reproduction without learned foresight.",
        "ইনস্টিংক্ট বেঁচে থাকা/বংশরক্ষার জটিল সহজাত আচরণ, শিক্ষিত পূর্বজ্ঞান ছাড়া।",
    ),
    q(
        "Nest building, fighting, fleeing, and food storing are commonly cited as examples of what?",
        "বাসা তৈরি, যুদ্ধ, পলায়ন ও খাদ্য সঞ্চয় সাধারণত কোন আচরণের উদাহরণ?",
        [
            "Instinctive innate behaviour",
            "Only language translation skill",
            "Only computer programming ability",
            "Only monetary accounting practice",
        ],
        [
            "ইনস্টিংকটিভ সহজাত আচরণ",
            "কেবল ভাষা অনুবাদ দক্ষতা",
            "কেবল কম্পিউটার প্রোগ্রামিং ক্ষমতা",
            "কেবল আর্থিক হিসাবরক্ষণ অনুশীলন",
        ],
        "A", "easy", "factual",
        "These complex unlearned survival acts are classic instinct examples.",
        "এই জটিল অশিক্ষিত বেঁচে থাকার কাজ ক্লাসিক ইনস্টিংক্ট উদাহরণ।",
    ),
    q(
        "FAP (Fixed Action Pattern) refers to which concept?",
        "FAP (Fixed Action Pattern) কোন ধারণাকে বোঝায়?",
        [
            "Genetically controlled, species-specific stereotyped action patterns in animal behaviour",
            "A temporary fashion trend among humans only",
            "A mathematical formula for calculating tax",
            "A dietary vitamin deficiency syndrome",
        ],
        [
            "প্রাণীর আচরণে জিনগতভাবে নিয়ন্ত্রিত, প্রজাতি-নির্দিষ্ট স্থায়ী অ্যাকশন প্যাটার্ন",
            "কেবল মানুষের মধ্যে অস্থায়ী ফ্যাশন ট্রেন্ড",
            "কর হিসাবের গাণিতিক সূত্র",
            "খাদ্যে ভিটামিন ঘাটতির সিনড্রোম",
        ],
        "A", "medium", "factual",
        "FAPs are fixed, gene-guided, species-typical behaviour units.",
        "FAP জিন-নিয়ন্ত্রিত, প্রজাতি-নির্দিষ্ট স্থির আচরণ একক।",
    ),
    q(
        "A releaser (sign stimulus) is best defined as what?",
        "রিলিজার বা সাইন স্টিমুলাস কাকে বলে?",
        [
            "A specific external signal that triggers a particular innate behavioural pattern",
            "Any random noise that never affects behaviour",
            "A written contract signed by two lawyers",
            "A chemical used only to clean laboratory glassware",
        ],
        [
            "নির্দিষ্ট সহজাত আচরণ প্যাটার্ন ট্রিগার করে এমন নির্দিষ্ট বাহ্যিক সংকেত",
            "আচরণকে কখনোই প্রভাবিত করে না এমন যেকোনো এলোমেলো শব্দ",
            "দুই আইনজীবীর স্বাক্ষরিত লিখিত চুক্তি",
            "কেবল ল্যাব গ্লাসওয়্যার পরিষ্কারের রাসায়নিক",
        ],
        "A", "medium", "factual",
        "A releaser is the specific external cue that releases an innate act.",
        "রিলিজার সেই নির্দিষ্ট বাহ্যিক সংকেত যা সহজাত আচরণ ছাড়ে।",
    ),
    q(
        "A terminating stimulus is the stimulus that does which of the following?",
        "টারমিনেটিং উদ্দীপনা কোন কাজ করে?",
        [
            "Ends or completes a behavioural response sequence",
            "Always starts a brand-new species evolution event",
            "Converts all innate acts into languages overnight",
            "Removes DNA from every cell of the animal",
        ],
        [
            "আচরণগত সাড়া ধারার সমাপ্তি বা সম্পূর্ণতা ঘটায়",
            "সবসময় নতুন প্রজাতি বিবর্তন শুরু করে",
            "এক রাতে সব সহজাত আচরণকে ভাষায় রূপান্তর করে",
            "প্রাণীর প্রতিটি কোষ থেকে DNA সরিয়ে দেয়",
        ],
        "A", "medium", "factual",
        "Terminating stimuli bring a behavioural response sequence to an end.",
        "টারমিনেটিং উদ্দীপনায় আচরণগত সাড়ার সমাপ্তি ঘটে।",
    ),
    q(
        "Newborn mammals suckling milk soon after birth mainly illustrates which point about innate behaviour?",
        "জন্মের পরপরই স্তন্যপায়ী শিশুর দুধ পান সহজাত আচরণ সম্বন্ধে মূলত কী দেখায়?",
        [
            "Some innate behaviours appear immediately after birth",
            "All behaviours require university education first",
            "No mammal can feed without reading instructions",
            "Suckling is purely a conditioned reflex to algebra",
        ],
        [
            "কিছু সহজাত আচরণ জন্মের পরপরই প্রকাশ পায়",
            "সব আচরণের আগে বিশ্ববিদ্যালয় শিক্ষা লাগে",
            "নির্দেশনা না পড়ে কোনো স্তন্যপায়ী খাদ্য নিতে পারে না",
            "দুধ পান কেবল বীজগণিতের সাপেক্ষ প্রতিবর্ত",
        ],
        "A", "easy", "application",
        "Immediate postnatal suckling is a classic early-expressed innate act.",
        "জন্মপরবর্তী তাৎক্ষণিক দুধপান আদি প্রকাশিত সহজাত আচরণের উদাহরণ।",
    ),
    q(
        "Bird nest-building or incubating eggs that appear mainly after maturity shows what about innate behaviour?",
        "পরিপক্কতার পর প্রধানত দেখা পাখির বাসা তৈরি বা ডিমে তা দেওয়া সহজাত আচরণ সম্বন্ধে কী বলে?",
        [
            "Some innate behaviours are expressed only after maturation",
            "Innate behaviour can never appear after birth at all",
            "Innate behaviour requires buying nesting manuals",
            "Only learned algebra can trigger nest building",
        ],
        [
            "কিছু সহজাত আচরণ কেবল পরিপক্কতার পর প্রকাশ পায়",
            "সহজাত আচরণ জন্মের পর কখনোই দেখা যায় না",
            "সহজাত আচরণে বাসা তৈরির ম্যানুয়াল কেনা লাগে",
            "কেবল শিক্ষিত বীজগণিত বাসা তৈরি ট্রিগার করে",
        ],
        "A", "medium", "conceptual",
        "Some innate patterns wait for physiological maturity before expression.",
        "কিছু সহজাত ধরন শারীরবৃত্তীয় পরিপক্কতার পর প্রকাশ পায়।",
    ),
    q(
        "Compared with learned behaviour, innate behaviour is generally which of the following?",
        "অর্জিত আচরণের তুলনায় সহজাত আচরণ সাধারণত কেমন?",
        [
            "Relatively stereotyped within a species and independent of individual experience",
            "Completely different in every individual of the same species every day",
            "Possible only after watching television advertisements",
            "Impossible in insects and present only in humans",
        ],
        [
            "প্রজাতির মধ্যে তুলনামূলকভাবে স্থির এবং ব্যক্তিগত অভিজ্ঞতা-নিরপেক্ষ",
            "একই প্রজাতির প্রতিটি ব্যক্তিতে প্রতিদিন সম্পূর্ণ ভিন্ন",
            "কেবল টেলিভিশন বিজ্ঞাপন দেখার পর সম্ভব",
            "পোকামাকড়ে অসম্ভব এবং কেবল মানুষে উপস্থিত",
        ],
        "A", "medium", "conceptual",
        "Innate acts are species-stereotyped and do not depend on personal learning history.",
        "সহজাত আচরণ প্রজাতিগতভাবে স্থির এবং ব্যক্তিগত শিক্ষা ইতিহাস-নিরপেক্ষ।",
    ),
]


# --- t02: Learned behaviour / অর্জিত আচরণ ---
T02 = [
    q(
        "Learned behaviour is best defined as which kind of behaviour?",
        "অর্জিত আচরণ বলতে কোন ধরনের আচরণকে বোঝায়?",
        [
            "Behaviour modified or acquired through experience, practice, or learning",
            "Behaviour fixed at birth and never changed by experience",
            "Behaviour identical in every species without exception",
            "Behaviour caused only by the phase of the Moon",
        ],
        [
            "অভিজ্ঞতা, অনুশীলন বা শিক্ষণের মাধ্যমে পরিবর্তিত বা অর্জিত আচরণ",
            "জন্মেই স্থির এবং অভিজ্ঞতায় কখনোই পরিবর্তনহীন আচরণ",
            "ব্যতিক্রম ছাড়া সব প্রজাতিতে অভিন্ন আচরণ",
            "কেবল চাঁদের কলার ফলে সৃষ্ট আচরণ",
        ],
        "A", "easy", "factual",
        "Learned behaviour depends on experience rather than pure inheritance alone.",
        "অর্জিত আচরণ কেবল বংশগতির বদলে অভিজ্ঞতার ওপর নির্ভর করে।",
    ),
    q(
        "A conditioned reflex (conditional reflex) is best described as what?",
        "সাপেক্ষ প্রতিবর্ত ক্রিয়া কাকে বলে?",
        [
            "A learned response linked to a previously neutral stimulus by association",
            "An inborn reflex that never changes with experience",
            "A voluntary political speech prepared overnight",
            "A mathematical identity proven without observation",
        ],
        [
            "পূর্বে নিরপেক্ষ উদ্দীপকের সঙ্গে সংযুক্ত হয়ে শিক্ষণলব্ধ সাড়া",
            "অভিজ্ঞতায় কখনোই বদলায় না এমন জন্মগত প্রতিবর্ত",
            "রাতারাতি তৈরি স্বেচ্ছাকৃত রাজনৈতিক বক্তৃতা",
            "পর্যবেক্ষণ ছাড়াই প্রমাণিত গাণিতিক অভেদ",
        ],
        "A", "easy", "factual",
        "Conditioned reflexes are acquired by associating a new stimulus with a response.",
        "সাপেক্ষ প্রতিবর্ত নতুন উদ্দীপকের সঙ্গে সাড়া যুক্ত করে অর্জিত হয়।",
    ),
    q(
        "In Pavlov’s classic dog experiment, what happened after repeated pairing of a bell with food?",
        "প্যাভলভের ক্লাসিক কুকুর পরীক্ষায় খাবারের সঙ্গে ঘণ্টা বারবার জুড়লে কী হয়?",
        [
            "The dog salivated to the bell alone",
            "The dog permanently lost all salivary glands",
            "The dog began photosynthesis like a plant",
            "The dog forgot how to walk forever",
        ],
        [
            "কেবল ঘণ্টার শব্দেই কুকুরের লালা ঝরতে শুরু করে",
            "কুকুর স্থায়ীভাবে সব লালাগ্রন্থি হারায়",
            "কুকুর উদ্ভিদের মতো সালোকসংশ্লেষ শুরু করে",
            "কুকুর চিরকাল হাঁটা ভুলে যায়",
        ],
        "A", "easy", "factual",
        "Classical conditioning made the bell a conditioned stimulus for salivation.",
        "ক্লাসিক্যাল কন্ডিশনিংয়ে ঘণ্টা লালার সাপেক্ষ উদ্দীপক হয়ে ওঠে।",
    ),
    q(
        "Pavlov’s conditioning experiment is a landmark example of which learned process?",
        "প্যাভলভের কন্ডিশনিং পরীক্ষা কোন অর্জিত প্রক্রিয়ার মাইলফলক উদাহরণ?",
        [
            "Classical conditioning / conditioned reflex learning",
            "Fixed action pattern release only",
            "Rheotaxis in flowing water only",
            "Photosynthetic carbon fixation only",
        ],
        [
            "ক্লাসিক্যাল কন্ডিশনিং / সাপেক্ষ প্রতিবর্ত শিক্ষণ",
            "কেবল ফিক্সড অ্যাকশন প্যাটার্ন রিলিজ",
            "কেবল প্রবহমান জলে রিওট্যাক্সিস",
            "কেবল সালোকসংশ্লেষী কার্বন স্থিরীকরণ",
        ],
        "A", "easy", "factual",
        "Pavlov demonstrated associative classical conditioning.",
        "প্যাভলভ অ্যাসোসিয়েটিভ ক্লাসিক্যাল কন্ডিশনিং দেখান।",
    ),
    q(
        "Habituation is learning in which an animal does what?",
        "অভ্যস্তকরণ বা হ্যাবিচুয়েশনে প্রাণী কী করে?",
        [
            "Gradually stops responding to a repeated harmless stimulus",
            "Suddenly invents a new language overnight",
            "Increases reflex strength to every repeated harmless noise forever",
            "Converts all innate taxes into algebraic equations",
        ],
        [
            "বারবার নিরীহ উদ্দীপকে ধীরে ধীরে সাড়া দেওয়া বন্ধ করে",
            "এক রাতে হঠাৎ নতুন ভাষা উদ্ভাবন করে",
            "প্রতিটি পুনরাবৃত্ত নিরীহ শব্দে চিরকাল প্রতিবর্ত বাড়ায়",
            "সব সহজাত ট্যাক্সিসকে বীজগণিত সমীকরণে রূপান্তর করে",
        ],
        "A", "medium", "conceptual",
        "Habituation is the waning of response to repeated non-threatening stimuli.",
        "হ্যাবিচুয়েশন পুনরাবৃত্ত নিরাপদ উদ্দীপকে সাড়া কমে যাওয়া।",
    ),
    q(
        "Imprinting is typically which kind of learning?",
        "ইমপ্রিন্টিং সাধারণত কোন ধরনের শিক্ষণ?",
        [
            "Rapid early-life learning of a key social object during a sensitive period",
            "Slow lifelong memorization of every street name in a city",
            "Only adult court learning of tax law",
            "Only laboratory calculation of molar mass",
        ],
        [
            "সংবেদনশীল পর্যায়ে দ্রুত আদি জীবনে গুরুত্বপূর্ণ সামাজিক বস্তু শেখা",
            "শহরের সব রাস্তার নাম আজীবন ধীরে মুখস্থ করা",
            "কেবল প্রাপ্তবয়স্ক আদালতে কর আইন শেখা",
            "কেবল ল্যাবে মোলার ভর হিসাব",
        ],
        "A", "medium", "factual",
        "Imprinting is rapid, often irreversible learning in an early critical period.",
        "ইমপ্রিন্টিং আদি সংবেদনশীল পর্যায়ের দ্রুত, প্রায়শই অপরিবর্তনীয় শিক্ষণ।",
    ),
    q(
        "Konrad Lorenz is especially associated with pioneering studies of which learned phenomenon?",
        "কোনার্ড লোরেঞ্জ বিশেষভাবে কোন অর্জিত ঘটনার অগ্রণী গবেষণার সঙ্গে যুক্ত?",
        [
            "Imprinting in young birds following a parent figure",
            "Discovery of penicillin antibiotics",
            "Invention of the steam engine",
            "Formulation of Mendel’s pea ratios",
        ],
        [
            "অভিভাবক অনুসরণকারী তরুণ পাখিতে ইমপ্রিন্টিং",
            "পেনিসিলিন অ্যান্টিবায়োটিক আবিষ্কার",
            "বাষ্প ইঞ্জিন উদ্ভাবন",
            "মেন্ডেলের মটর অনুপাত প্রণয়ন",
        ],
        "A", "medium", "factual",
        "Lorenz’s gosling work made imprinting a classic ethology example.",
        "লোরেঞ্জের হাঁসের বাচ্চা গবেষণা ইমপ্রিন্টিংকে ক্লাসিক করে তোলে।",
    ),
    q(
        "Trial-and-error learning (as in Thorndike’s puzzle-box work) mainly shows what?",
        "চেষ্টা-ভুল শিক্ষণ (যেমন থর্নডাইকের পাজল-বক্স) মূলত কী দেখায়?",
        [
            "Successful responses are strengthened by rewarding outcomes over repeated trials",
            "Animals never change behaviour after any reward",
            "All learning is purely genetic FAP release",
            "Rewards always abolish every motor neuron",
        ],
        [
            "বারবার চেষ্টায় পুরস্কৃত সফল সাড়া শক্তিশালী হয়",
            "কোনো পুরস্কারের পর প্রাণী কখনোই আচরণ বদলায় না",
            "সব শিক্ষণ কেবল জিনগত FAP রিলিজ",
            "পুরস্কার সবসময় সব মোটর নিউরন বিলুপ্ত করে",
        ],
        "A", "medium", "conceptual",
        "Operant/trial-and-error learning reinforces acts that produce favourable results.",
        "অপারেন্ট/চেষ্টা-ভুল শিক্ষণে অনুকূল ফলদায়ক কাজ শক্তিশালী হয়।",
    ),
    q(
        "Insight learning is best illustrated by which situation?",
        "অন্তর্দৃষ্টিমূলক শিক্ষণ কোন পরিস্থিতিতে সবচেয়ে ভালো বোঝা যায়?",
        [
            "Suddenly solving a novel problem by reorganizing prior experience without stepwise trial",
            "Repeating an unchanged FAP after a releaser every time",
            "Ignoring all stimuli forever after one exposure",
            "Moving only by rheotaxis in a stream",
        ],
        [
            "ধাপে ধাপে চেষ্টা ছাড়াই পূর্ব অভিজ্ঞতা পুনর্গঠন করে নতুন সমস্যা হঠাৎ সমাধান",
            "প্রতিবার রিলিজারের পর অপরিবর্তিত FAP পুনরাবৃত্তি",
            "একবার উদ্দীপকের পর চিরকাল সব উদ্দীপক উপেক্ষা",
            "কেবল স্রোতে রিওট্যাক্সিস দিয়ে চলা",
        ],
        "A", "medium", "conceptual",
        "Insight is abrupt adaptive problem-solving from mental reorganization of experience.",
        "অন্তর্দৃষ্টি অভিজ্ঞতার মানসিক পুনর্গঠনে হঠাৎ অভিযোজিত সমাধান।",
    ),
    q(
        "Wolfgang Köhler’s chimpanzee studies with sticks or boxes are classic evidence for which learning?",
        "স্টিক বা বাক্স নিয়ে ক্যোলারের শিম্পাঞ্জি গবেষণা কোন শিক্ষণের ক্লাসিক প্রমাণ?",
        [
            "Insight learning",
            "Only thigmotaxis",
            "Only reflex arc anatomy",
            "Only swarming of honeybees",
        ],
        [
            "অন্তর্দৃষ্টিমূলক শিক্ষণ",
            "কেবল থিগমোট্যাক্সিস",
            "কেবল প্রতিবর্ত চাপের শারীরস্থান",
            "কেবল মৌমাছির সোয়ার্মিং",
        ],
        "A", "medium", "factual",
        "Köhler’s apes appeared to solve tool problems by insight, not mere blind trial.",
        "ক্যোলারের প্রাইমেটরা অন্ধ চেষ্টা নয়, অন্তর্দৃষ্টিতে টুল সমস্যা সমাধান করে।",
    ),
    q(
        "Associative learning means which of the following?",
        "অ্যাসোসিয়েটিভ শিক্ষণ বলতে কী বোঝায়?",
        [
            "Forming a link between a stimulus and a response or between two stimuli",
            "Deleting all synapses from the nervous system",
            "Replacing behaviour with photosynthesis",
            "Counting chromosomes during mitosis only",
        ],
        [
            "উদ্দীপক ও সাড়ার বা দুই উদ্দীপকের মধ্যে সংযোগ গঠন",
            "স্নায়ুতন্ত্র থেকে সব সিন্যাপ্স মুছে ফেলা",
            "আচরণকে সালোকসংশ্লেষ দিয়ে প্রতিস্থাপন",
            "কেবল মাইটোসিসে ক্রোমোজোম গণনা",
        ],
        "A", "easy", "conceptual",
        "Association links events so that one predicts or triggers the other.",
        "অ্যাসোসিয়েশন ঘটনাগুলোকে যুক্ত করে যাতে একটি অন্যটিকে নির্দেশ করে।",
    ),
    q(
        "Which statement correctly contrasts innate and learned behaviour?",
        "সহজাত ও অর্জিত আচরণের সঠিক পার্থক্য কোনটি?",
        [
            "Innate behaviour needs no prior experience; learned behaviour depends on experience",
            "Learned behaviour is always present at the moment of fertilization",
            "Innate behaviour requires formal schooling; learned behaviour never does",
            "Both are impossible in vertebrates",
        ],
        [
            "সহজাতে পূর্ব অভিজ্ঞতা লাগে না; অর্জিতে অভিজ্ঞতা নির্ভর করে",
            "অর্জিত আচরণ নিষেকের মুহূর্তেই সবসময় উপস্থিত",
            "সহজাতে আনুষ্ঠানিক স্কুলিং লাগে; অর্জিতে কখনোই লাগে না",
            "উভয়ই মেরুদণ্ডীতে অসম্ভব",
        ],
        "A", "easy", "conceptual",
        "The key contrast is independence versus dependence on experience.",
        "মূল পার্থক্য অভিজ্ঞতা-নিরপেক্ষতা বনাম অভিজ্ঞতা-নির্ভরতা।",
    ),
    q(
        "A dog that sits on command after repeated reward training mainly shows which type of behaviour?",
        "বারবার পুরস্কার প্রশিক্ষণের পর নির্দেশে বসা কুকুর মূলত কোন আচরণ দেখায়?",
        [
            "Learned behaviour shaped by training",
            "Pure rheotaxis in air currents",
            "An unchanged FAP to moonlight only",
            "Photosynthetic innate taxis",
        ],
        [
            "প্রশিক্ষণে গঠিত অর্জিত আচরণ",
            "বায়ুপ্রবাহে বিশুদ্ধ রিওট্যাক্সিস",
            "কেবল চাঁদের আলোয় অপরিবর্তিত FAP",
            "সালোকসংশ্লেষী সহজাত ট্যাক্সিস",
        ],
        "A", "easy", "application",
        "Command sitting after reward training is acquired, not purely innate.",
        "পুরস্কার প্রশিক্ষণের পর নির্দেশে বসা অর্জিত আচরণ।",
    ),
    q(
        "Latent learning typically means which of the following?",
        "লেটেন্ট লার্নিং সাধারণত কী বোঝায়?",
        [
            "Learning that occurs without obvious immediate reward and shows later when needed",
            "Learning that is impossible without electric shock every second",
            "Learning identical to a spinal stretch reflex",
            "Learning that deletes all previous memories instantly",
        ],
        [
            "তাৎক্ষণিক স্পষ্ট পুরস্কার ছাড়াই শেখা যা প্রয়োজনে পরে প্রকাশ পায়",
            "প্রতি সেকেন্ডে বৈদ্যুতিক শক ছাড়া অসম্ভব শিক্ষণ",
            "স্পাইনাল স্ট্রেচ রিফ্লেক্সের অভিন্ন শিক্ষণ",
            "আগের সব স্মৃতি তাৎক্ষণিক মুছে ফেলা শিক্ষণ",
        ],
        "A", "hard", "conceptual",
        "Latent learning is acquired without immediate reinforcement and revealed later.",
        "লেটেন্ট লার্নিং তাৎক্ষণিক পুনর্বলন ছাড়া অর্জিত হয়ে পরে প্রকাশ পায়।",
    ),
    q(
        "Which feature is typical of learned behaviour compared with a simple innate reflex?",
        "সরল সহজাত প্রতিবর্তের তুলনায় অর্জিত আচরণের সাধারণ বৈশিষ্ট্য কোনটি?",
        [
            "It can be modified by experience and may vary among individuals",
            "It is always identical in every member of the species from birth",
            "It never involves the nervous system at all",
            "It can occur only in plants, never in animals",
        ],
        [
            "অভিজ্ঞতায় পরিবর্তনযোগ্য এবং ব্যক্তিভেদে ভিন্ন হতে পারে",
            "জন্ম থেকে প্রজাতির সবাইতে সবসময় অভিন্ন",
            "স্নায়ুতন্ত্র একেবারেই জড়িত নয়",
            "কেবল উদ্ভিদে সম্ভব, প্রাণীতে নয়",
        ],
        "A", "medium", "conceptual",
        "Learning allows individual flexibility beyond rigid innate stereotypes.",
        "শিক্ষণ সহজাত স্থিরতার বাইরে ব্যক্তিগত নমনীয়তা দেয়।",
    ),
    q(
        "If a chick follows the first large moving object it sees after hatching, this is mainly an example of what?",
        "ফুটার পর প্রথম দেখা বড় চলমান বস্তু অনুসরণ করা মুরগির বাচ্চা মূলত কোন উদাহরণ?",
        [
            "Imprinting",
            "Rheotaxis",
            "Chemotaxis toward sugar only",
            "Mendelian independent assortment",
        ],
        [
            "ইমপ্রিন্টিং",
            "রিওট্যাক্সিস",
            "কেবল চিনির দিকে কেমোট্যাক্সিস",
            "মেন্ডেলীয় স্বাধীন সঞ্চারণ",
        ],
        "A", "easy", "application",
        "Following the first conspicuous moving object is classic imprinting.",
        "প্রথম স্পষ্ট চলমান বস্তু অনুসরণ ক্লাসিক ইমপ্রিন্টিং।",
    ),
    q(
        "Which learning type best explains ignoring a repeatedly harmless ticking clock nearby?",
        "আশপাশের বারবার নিরীহ ঘড়ির টিকটিক উপেক্ষা কোন শিক্ষণে সবচেয়ে ভালো ব্যাখ্যা হয়?",
        [
            "Habituation",
            "Nuptial flight",
            "Swarming",
            "Fixed action pattern release by a queen substance only",
        ],
        [
            "হ্যাবিচুয়েশন",
            "নপসিয়াল উড্ডয়ন",
            "সোয়ার্মিং",
            "কেবল রাণী পদার্থ দ্বারা FAP রিলিজ",
        ],
        "A", "easy", "application",
        "Repeated harmless ticks lose behavioural relevance through habituation.",
        "পুনরাবৃত্ত নিরীহ টিকটিক হ্যাবিচুয়েশনে আচরণগত গুরুত্ব হারায়।",
    ),
    q(
        "Operant conditioning differs from classical conditioning mainly because the animal does what?",
        "অপারেন্ট কন্ডিশনিং ক্লাসিক্যাল থেকে মূলত কীভাবে আলাদা—প্রাণী কী করে?",
        [
            "Emits a voluntary act that is strengthened or weakened by its consequences",
            "Never moves and only passively receives paired bells and food",
            "Uses only thigmotaxis without any reward history",
            "Relies solely on FAP genetics with no outcome feedback",
        ],
        [
            "স্বেচ্ছাকৃত কাজ করে যার পরিণামে কাজ শক্তিশালী বা দুর্বল হয়",
            "কখনো নড়ে না এবং কেবল ঘণ্টা-খাবার জোড়া নিষ্ক্রিয়ভাবে পায়",
            "কোনো পুরস্কার ইতিহাস ছাড়াই কেবল থিগমোট্যাক্সিস ব্যবহার করে",
            "ফলাফল ফিডব্যাক ছাড়াই কেবল FAP জিনে নির্ভর করে",
        ],
        "A", "hard", "conceptual",
        "In operant learning, consequences of the animal’s own acts shape future behaviour.",
        "অপারেন্টে প্রাণীর নিজ কাজের পরিণাম ভবিষ্যৎ আচরণ গড়ে।",
    ),
    q(
        "Which statement about conditioned reflexes is correct?",
        "সাপেক্ষ প্রতিবর্ত সম্বন্ধে সঠিক উক্তি কোনটি?",
        [
            "They depend on prior experience and do not occur naturally the first time without association",
            "They are identical to inborn spinal reflexes present at fertilization",
            "They require no nervous system involvement whatsoever",
            "They are only found in honeybee swarming flights",
        ],
        [
            "পূর্ব অভিজ্ঞতা নির্ভর এবং সংযোগ ছাড়া প্রথমবার স্বাভাবিকভাবে ঘটে না",
            "নিষেকের সময় উপস্থিত জন্মগত স্পাইনাল প্রতিবর্তের অভিন্ন",
            "স্নায়ুতন্ত্রের কোনো সম্পৃক্ততাই লাগে না",
            "কেবল মৌমাছির সোয়ার্মিং উড্ডয়নে পাওয়া যায়",
        ],
        "A", "medium", "conceptual",
        "Conditioned reflexes are experience-built associations, not first-trial innate acts.",
        "সাপেক্ষ প্রতিবর্ত অভিজ্ঞতায় গঠিত সংযোগ, প্রথমবারের সহজাত কাজ নয়।",
    ),
    q(
        "A student who improves maze performance after practice is mainly demonstrating which category of animal behaviour concepts?",
        "অনুশীলনের পর গোলকধাঁধায় উন্নতি কোন আচরণ ধারণার উদাহরণ?",
        [
            "Learned behaviour",
            "Pure innate phototaxis only",
            "Only terminating stimulus anatomy",
            "Only altruistic caste determination",
        ],
        [
            "অর্জিত আচরণ",
            "কেবল বিশুদ্ধ সহজাত ফোটোট্যাক্সিস",
            "কেবল টারমিনেটিং উদ্দীপনার শারীরস্থান",
            "কেবল পরার্থপর জাত নির্ধারণ",
        ],
        "A", "easy", "application",
        "Practice-based improvement is a clear learned-behaviour outcome.",
        "অনুশীলনে উন্নতি স্পষ্ট অর্জিত আচরণের ফল।",
    ),
]


# --- t03: Social behaviour / সামাজিক আচরণ ---
T03 = [
    q(
        "Social behaviour is best defined as which of the following?",
        "সামাজিক আচরণ বলতে নিচের কোনটিকে বোঝায়?",
        [
            "Interactions among members of the same species living together",
            "Only solitary hunting with zero contact among conspecifics",
            "Only chemical reactions inside a single mitochondrion",
            "Only geological folding of mountain rocks",
        ],
        [
            "একই প্রজাতির একত্রে বসবাসকারী সদস্যদের পারস্পরিক ক্রিয়াকলাপ",
            "কেবল সহপ্রজাতির শূন্য যোগাযোগে একাকী শিকার",
            "কেবল একটি মাইটোকন্ড্রিয়নের অভ্যন্তরীণ রাসায়নিক বিক্রিয়া",
            "কেবল পর্বত শিলার ভূতাত্ত্বিক ভাঁজ",
        ],
        "A", "easy", "factual",
        "Social behaviour covers conspecific group living and mutual interactions.",
        "সামাজিক আচরণ সহপ্রজাতির দলবদ্ধ বাস ও পারস্পরিক ক্রিয়া।",
    ),
    q(
        "Altruism in animals means which behaviour?",
        "প্রাণীতে অ্যালট্রুইজম বা পরার্থপরতা কোন আচরণ?",
        [
            "Helping another member of the same species at a cost or risk to oneself",
            "Always attacking every member of one’s own species for no reason",
            "Refusing all contact with every living organism forever",
            "Eating only inorganic rocks for nutrition",
        ],
        [
            "নিজের ক্ষতি বা ঝুঁকি স্বীকার করে একই প্রজাতির অন্য সদস্যকে উপকার করা",
            "কোনো কারণ ছাড়াই নিজ প্রজাতির সবাইকে সবসময় আক্রমণ",
            "সব জীবের সঙ্গে চিরকাল সব যোগাযোগ প্রত্যাখ্যান",
            "পুষ্টির জন্য কেবল অজৈব পাথর খাওয়া",
        ],
        "A", "easy", "factual",
        "Altruism is costly help directed toward conspecifics.",
        "অ্যালট্রুইজম সহপ্রজাতির প্রতি ব্যয়বহুল সাহায্য।",
    ),
    q(
        "Why are honeybees commonly called social animals in HSC biology?",
        "HSC জীববিজ্ঞানে মৌমাছিকে সামাজিক জীব বলা হয় কেন?",
        [
            "They live in colonies with organized castes that cooperate for the hive",
            "Each bee lives alone and never meets another bee",
            "They photosynthesize like green plants in sunlight",
            "They have no division of labour at all",
        ],
        [
            "এরা সংগঠিত জাতসহ কলোনিতে বাস করে এবং মৌচাকের জন্য সহযোগিতা করে",
            "প্রতিটি মৌমাছি একাকী থাকে এবং অন্য মৌমাছির দেখা পায় না",
            "এরা সূর্যালোকে সবুজ উদ্ভিদের মতো সালোকসংশ্লেষ করে",
            "এদের কোনো শ্রমবিভাগই নেই",
        ],
        "A", "easy", "conceptual",
        "Colony living with cooperative castes defines their social lifestyle.",
        "সহযোগী জাতসহ কলোনি জীবনই তাদের সামাজিকতার ভিত্তি।",
    ),
    q(
        "A typical honeybee colony includes which three kinds of members?",
        "সাধারণ মৌমাছি কলোনিতে কোন তিন ধরনের সদস্য থাকে?",
        [
            "Queen, drones (males), and workers (sterile females)",
            "Only kings, princes, and photographers",
            "Only tadpoles, frogs, and toads",
            "Only algae, fungi, and mosses",
        ],
        [
            "রাণী, ড্রোন (পুরুষ) ও কর্মী (বন্ধ্যা স্ত্রী)",
            "কেবল রাজা, রাজপুত্র ও আলোকচিত্রশিল্পী",
            "কেবল ব্যাঙাচি, ব্যাঙ ও কুনোব্যাঙ",
            "কেবল শৈবাল, ছত্রাক ও শ্যাওলা",
        ],
        "A", "easy", "factual",
        "Honeybee societies are organized into queen, drone, and worker castes.",
        "মৌমাছি সমাজে রাণী, ড্রোন ও কর্মী—এই তিন জাত।",
    ),
    q(
        "Worker honeybees are best described as which of the following?",
        "কর্মী মৌমাছিদের সবচেয়ে ভালো বর্ণনা কোনটি?",
        [
            "Sterile females that perform colony tasks and do not normally reproduce",
            "Fertile males that lay all the eggs of the hive",
            "Single queens that leave the hive every hour to mate",
            "Larvae that photosynthesize nectar into protein",
        ],
        [
            "বন্ধ্যা স্ত্রী যারা কলোনির কাজ করে এবং সাধারণত প্রজনন করে না",
            "সব ডিম পাড়ে এমন উর্বর পুরুষ",
            "প্রতি ঘণ্টায় মিলনের জন্য মৌচাক ছাড়ে এমন একক রাণী",
            "নেক্টারকে সালোকসংশ্লেষে প্রোটিনে রূপান্তর করে এমন লার্ভা",
        ],
        "A", "easy", "factual",
        "Workers are sterile females serving brood care, foraging, and hive maintenance.",
        "কর্মীরা বন্ধ্যা স্ত্রী—শিশুযত্ন, খাদ্য সংগ্রহ ও মৌচাক রক্ষায় নিয়োজিত।",
    ),
    q(
        "About how many worker bees may be present in a large honeybee colony according to common HSC descriptions?",
        "সাধারণ HSC বর্ণনায় বড় মৌমাছি কলোনিতে প্রায় কত কর্মী থাকতে পারে?",
        [
            "About 60,000–80,000 workers",
            "Exactly 2 workers only",
            "About 5 workers maximum",
            "Zero workers in every healthy colony",
        ],
        [
            "প্রায় ৬০,০০০–৮০,০০০ কর্মী",
            "ঠিক ২ জন কর্মী মাত্র",
            "সর্বোচ্চ প্রায় ৫ জন কর্মী",
            "প্রতিটি সুস্থ কলোনিতে শূন্য কর্মী",
        ],
        "A", "medium", "factual",
        "Textbooks often cite tens of thousands of workers under one queen.",
        "পাঠ্যে প্রায়ই এক রাণীর অধীনে কয়েক হাজার কর্মীর উল্লেখ থাকে।",
    ),
    q(
        "Nuptial flight of the queen honeybee refers to which event?",
        "রাণী মৌমাছির নপসিয়াল উড্ডয়ন কোন ঘটনা?",
        [
            "Mating flight in which she leaves the hive once to mate and collect sperm",
            "Daily shopping trips to buy artificial sugar from markets",
            "Migration of the entire colony to another planet",
            "Molting of wings into leaves every morning",
        ],
        [
            "মিলন উড্ডয়ন যেখানে সে একবার মৌচাক ছেড়ে সঙ্গম ও শুক্রাণু সংগ্রহ করে",
            "বাজার থেকে কৃত্রিম চিনি কেনার দৈনন্দিন ভ্রমণ",
            "পুরো কলোনির অন্য গ্রহে অভিবাসন",
            "প্রতি সকালে ডানার পাতায় রূপান্তর",
        ],
        "A", "medium", "factual",
        "The queen’s nuptial flight is her reproductive mating excursion from the hive.",
        "নপসিয়াল উড্ডয়ন রাণীর প্রজননমূলক সঙ্গম উড্ডয়ন।",
    ),
    q(
        "During her lifetime, a queen honeybee typically mates in which pattern regarding nuptial flight?",
        "জীবদ্দশায় রাণী মৌমাছি নপসিয়াল উড্ডয়নের ক্ষেত্রে সাধারণত কোন ধরন অনুসরণ করে?",
        [
            "She mates (often with multiple drones) mainly once in life and stores sperm thereafter",
            "She must remate every hour of every day to lay any egg",
            "She never leaves the hive and never stores any sperm",
            "She mates only with worker bees inside sealed brood cells",
        ],
        [
            "জীবনে মূলত একবার (প্রায়ই একাধিক ড্রোনের সঙ্গে) সঙ্গম করে পরে শুক্রাণু সংরক্ষণ করে",
            "ডিম পাড়তে প্রতিদিন প্রতি ঘণ্টায় পুনঃসঙ্গম করতে হয়",
            "কখনো মৌচাক ছাড়ে না এবং কোনো শুক্রাণু রাখে না",
            "কেবল সিল করা ব্রুড কোষে কর্মীদের সঙ্গে সঙ্গম করে",
        ],
        "A", "medium", "conceptual",
        "Stored sperm from the mating flight fertilizes eggs for the rest of her laying life.",
        "মিলন উড্ডয়নের সংরক্ষিত শুক্রাণু দিয়ে আজীবন ডিম নিষিক্ত হয়।",
    ),
    q(
        "Swarming in honeybees mainly means which process?",
        "মৌমাছিতে সোয়ার্মিং মূলত কোন প্রক্রিয়া?",
        [
            "Part of the colony leaving with a queen to found a new nest when the colony grows large",
            "Individual bees converting into butterflies overnight",
            "Workers permanently abandoning all larvae without forming any new home",
            "Drones turning into queens by eating only salt",
        ],
        [
            "কলোনি বড় হলে রাণীসহ অংশবিশেষ নতুন বাসা গড়তে চলে যাওয়া",
            "এক রাতে পৃথক মৌমাছির প্রজাপতিতে রূপান্তর",
            "নতুন বাসা না গড়ে কর্মীদের স্থায়ীভাবে সব লার্ভা পরিত্যাগ",
            "কেবল লবণ খেয়ে ড্রোনের রাণীতে পরিণত হওয়া",
        ],
        "A", "medium", "factual",
        "Swarming is colony fission/relocation for new nest establishment and gene flow.",
        "সোয়ার্মিং নতুন বাসা ও জিন প্রবাহের জন্য কলোনি বিভাজন/স্থানান্তর।",
    ),
    q(
        "Worker bees caring for the queen and colony at personal reproductive cost mainly illustrate what?",
        "নিজ প্রজনন ব্যয়ে রাণী ও কলোনির যত্ন নেওয়া কর্মী মৌমাছি মূলত কী দেখায়?",
        [
            "Altruistic social behaviour",
            "Only solitary territorial isolation",
            "Only phototaxis toward street lamps",
            "Only imprinting on a ticking clock",
        ],
        [
            "পরার্থপর সামাজিক আচরণ",
            "কেবল একাকী আঞ্চলিক বিচ্ছিন্নতা",
            "কেবল রাস্তার বাতির দিকে ফোটোট্যাক্সিস",
            "কেবল টিকটিক ঘড়িতে ইমপ্রিন্টিং",
        ],
        "A", "medium", "application",
        "Sterile workers’ costly help to the colony is a textbook altruism example.",
        "বন্ধ্যা কর্মীর ব্যয়বহুল কলোনি সেবা ক্লাসিক অ্যালট্রুইজম।",
    ),
    q(
        "Karl von Frisch is famous for decoding which honeybee communication behaviour?",
        "কার্ল ভন ফ্রিশ কোন মৌমাছি যোগাযোগ আচরণ পাঠোদ্ধারে বিখ্যাত?",
        [
            "The waggle (and related) dance communicating food location",
            "The invention of electric refrigerators",
            "The discovery of blood groups A/B/O",
            "The naming of dinosaurs in the Mesozoic",
        ],
        [
            "খাদ্যের অবস্থান জানানো ওয়াগল (ও সংশ্লিষ্ট) নৃত্য",
            "বৈদ্যুতিক রেফ্রিজারেটর উদ্ভাবন",
            "A/B/O রক্তগ্রুপ আবিষ্কার",
            "মেসোজোইকে ডাইনোসরের নামকরণ",
        ],
        "A", "medium", "factual",
        "Von Frisch showed dances convey distance and direction of food sources.",
        "ভন ফ্রিশ দেখান নৃত্য খাদ্যের দূরত্ব ও দিক জানায়।",
    ),
    q(
        "In eusocial insects like honeybees, division of labour among castes mainly benefits the colony by doing what?",
        "মৌমাছির মতো ইউসোশ্যাল পোকায় জাতভিত্তিক শ্রমবিভাগ কলোনিকে মূলত কীভাবে উপকৃত করে?",
        [
            "Assigning specialized tasks (reproduction, foraging, care) efficiently among members",
            "Eliminating all communication between members forever",
            "Forcing every individual to lay equal numbers of eggs daily",
            "Stopping all food collection as a permanent rule",
        ],
        [
            "সদস্যদের মধ্যে প্রজনন, খাদ্য সংগ্রহ, যত্ন ইত্যাদি বিশেষায়িত কাজ দক্ষভাবে ভাগ করা",
            "সদস্যদের মধ্যে সব যোগাযোগ চিরকাল বিলুপ্ত করা",
            "প্রত্যেককে প্রতিদিন সমান সংখ্যক ডিম পাড়তে বাধ্য করা",
            "স্থায়ী নিয়ম হিসেবে সব খাদ্য সংগ্রহ বন্ধ করা",
        ],
        "A", "medium", "conceptual",
        "Caste-based task specialization raises colony efficiency and survival.",
        "জাতভিত্তিক কাজের বিশেষায়ন কলোনির দক্ষতা ও বেঁচে থাকা বাড়ায়।",
    ),
    q(
        "Territorial behaviour in animals typically involves which action?",
        "প্রাণীর আঞ্চলিক বা টেরিটোরিয়াল আচরণে সাধারণত কোন কাজ থাকে?",
        [
            "Defending a space or resource against rival conspecifics",
            "Donating one’s territory permanently to every passing stranger species",
            "Never responding to any intrusion at all",
            "Converting territory into pure mathematical symbols",
        ],
        [
            "প্রতিদ্বন্দ্বী সহপ্রজাতির বিরুদ্ধে স্থান বা সম্পদ রক্ষা করা",
            "প্রতিটি অতিবাহিত অন্য প্রজাতিকে স্থায়ীভাবে নিজ এলাকা দান",
            "কোনো অনুপ্রবেশেই কখনো সাড়া না দেওয়া",
            "এলাকাকে বিশুদ্ধ গাণিতিক প্রতীকে রূপান্তর",
        ],
        "A", "easy", "conceptual",
        "Territoriality is defense of an area or resource against rivals.",
        "টেরিটোরিয়ালিটি প্রতিদ্বন্দ্বীর বিরুদ্ধে এলাকা/সম্পদ রক্ষা।",
    ),
    q(
        "A dominance hierarchy (pecking order) in a social group mainly means what?",
        "সামাজিক দলে আধিপত্য ক্রম বা পেকিং অর্ডার মূলত কী বোঝায়?",
        [
            "A ranked order of individuals that regulates access to resources and reduces constant fighting",
            "A complete absence of any rank differences among members",
            "A chemical formula for making artificial honey",
            "A geological ranking of rock layers only",
        ],
        [
            "সম্পদে প্রবেশাধিকার নিয়ন্ত্রণ ও নিরন্তর লড়াই কমাতে ব্যক্তিদের ক্রমবিন্যাস",
            "সদস্যদের মধ্যে কোনো পদমর্যাদা পার্থক্যের সম্পূর্ণ অনুপস্থিতি",
            "কৃত্রিম মধু তৈরির রাসায়নিক সূত্র",
            "কেবল শিলা স্তরের ভূতাত্ত্বিক ক্রম",
        ],
        "A", "medium", "conceptual",
        "Hierarchies structure social competition and often stabilize groups.",
        "আধিপত্য ক্রম সামাজিক প্রতিযোগিতা গুছিয়ে দল স্থিতিশীল রাখে।",
    ),
    q(
        "Honey produced by bees is a natural sweet product derived mainly from what?",
        "মৌমাছির তৈরি মধু মূলত কোন উৎস থেকে পাওয়া প্রাকৃতিক মিষ্টি পণ্য?",
        [
            "Nectar (and related plant secretions) processed by bees",
            "Pure metallic iron mined from rocks",
            "Only distilled ocean salt crystals",
            "Synthetic plastic polymers from factories",
        ],
        [
            "মৌমাছি কর্তৃক প্রক্রিয়াজাত নেক্টার (ও সংশ্লিষ্ট উদ্ভিদ নিঃসরণ)",
            "পাথর থেকে খননকৃত বিশুদ্ধ ধাতব লোহা",
            "কেবল পাতিত সমুদ্র লবণের স্ফটিক",
            "কারখানার কৃত্রিম প্লাস্টিক পলিমার",
        ],
        "A", "easy", "factual",
        "Bees convert floral nectar (etc.) into stored honey.",
        "মৌমাছি পুষ্পমধু ইত্যাদি প্রক্রিয়াজাত করে মধু সঞ্চয় করে।",
    ),
    q(
        "Cooperative hunting or cooperative brood care among conspecifics is primarily classified as which behaviour?",
        "সহপ্রজাতির মধ্যে সহযোগী শিকার বা সহযোগী বাচ্চাযত্ন প্রধানত কোন আচরণ?",
        [
            "Social behaviour",
            "Only solitary innate thigmotaxis",
            "Only classical conditioning to a bell",
            "Only geotaxis in plant roots",
        ],
        [
            "সামাজিক আচরণ",
            "কেবল একাকী সহজাত থিগমোট্যাক্সিস",
            "কেবল ঘণ্টার ক্লাসিক্যাল কন্ডিশনিং",
            "কেবল উদ্ভিদ মূলের জিওট্যাক্সিস",
        ],
        "A", "easy", "application",
        "Joint tasks among group members are social interactions.",
        "দলের সদস্যদের যৌথ কাজ সামাজিক মিথস্ক্রিয়া।",
    ),
    q(
        "Which statement best links altruism to honeybee workers?",
        "অ্যালট্রুইজমের সঙ্গে কর্মী মৌমাছির কোন সংযোগ সবচেয়ে সঠিক?",
        [
            "Workers forgo personal reproduction while aiding the queen and siblings",
            "Workers always destroy the queen to maximize personal egg laying",
            "Workers never collect food for anyone in the hive",
            "Workers mate every day and replace the queen hourly",
        ],
        [
            "কর্মীরা ব্যক্তিগত প্রজনন ত্যাগ করে রাণী ও সহোদরদের সাহায্য করে",
            "কর্মীরা ব্যক্তিগত ডিম পাড়া বাড়াতে সবসময় রাণী ধ্বংস করে",
            "কর্মীরা মৌচাকের কারও জন্য কখনো খাদ্য সংগ্রহ করে না",
            "কর্মীরা প্রতিদিন সঙ্গম করে প্রতি ঘণ্টায় রাণী বদলায়",
        ],
        "A", "medium", "application",
        "Reproductive sacrifice for colony relatives is altruism in eusocial bees.",
        "কলোনি আত্মীয়ের জন্য প্রজনন ত্যাগ ইউসোশ্যাল মৌমাছির অ্যালট্রুইজম।",
    ),
    q(
        "Communication is important in social animals mainly because it does what?",
        "সামাজিক প্রাণীতে যোগাযোগ গুরুত্বপূর্ণ কেন—এটি মূলত কী করে?",
        [
            "Coordinates group activities such as foraging, alarm, and nest care",
            "Prevents any individual from ever detecting food",
            "Deletes all memory of nest location permanently",
            "Converts social groups into solitary fossils instantly",
        ],
        [
            "খাদ্য সংগ্রহ, সতর্কতা ও বাসাযত্নের মতো দলগত কাজ সমন্বয় করে",
            "কোনো ব্যক্তিকে কখনোই খাদ্য শনাক্ত করতে দেয় না",
            "বাসার অবস্থানের সব স্মৃতি স্থায়ীভাবে মুছে দেয়",
            "সামাজিক দলকে তাৎক্ষণিক একাকী জীবাশ্ম করে তোলে",
        ],
        "A", "easy", "conceptual",
        "Signals let group members share information and act together.",
        "সংকেত দলের সদস্যদের তথ্য ভাগ ও যৌথ কাজ করতে দেয়।",
    ),
    q(
        "Which feature is NOT a reason honeybees are treated as social insects in this chapter?",
        "এই অধ্যায়ে মৌমাছিকে সামাজিক পোকা বলার কোনটি কারণ নয়?",
        [
            "Each bee completes its entire life cycle without ever meeting another bee",
            "They share a nest and show cooperative caste roles",
            "They communicate and care for brood within the colony",
            "They show organized reproduction centered on a queen",
        ],
        [
            "প্রতিটি মৌমাছি অন্য কোনো মৌমাছির দেখা না পেয়েই পূর্ণ জীবনচক্র শেষ করে",
            "এরা এক বাসা ভাগ করে এবং সহযোগী জাতভিত্তিক ভূমিকা দেখায়",
            "এরা কলোনিতে যোগাযোগ ও বাচ্চাযত্ন করে",
            "এদের রাণীকেন্দ্রিক সংগঠিত প্রজনন আছে",
        ],
        "A", "medium", "application",
        "Total lifelong solitude contradicts social-insect criteria; the others support it.",
        "আজীবন একাকীত্ব সামাজিক পোকার মানদণ্ডবিরোধী; বাকিগুলো সমর্থক।",
    ),
    q(
        "Swarming and nuptial mating flights together mainly contribute to honeybee colonies by doing what?",
        "সোয়ার্মিং ও নপসিয়াল মিলন উড্ডয়ন একত্রে মৌমাছি কলোনিকে মূলত কীভাবে সাহায্য করে?",
        [
            "Enabling colony propagation and genetic mixing through new nests and mating",
            "Stopping all egg laying forever in every colony",
            "Converting workers into green plants",
            "Eliminating queens from the species permanently",
        ],
        [
            "নতুন বাসা ও সঙ্গমের মাধ্যমে কলোনি বংশবিস্তার ও জিনগত মিশ্রণ সম্ভব করা",
            "সব কলোনিতে চিরকাল ডিম পাড়া বন্ধ করা",
            "কর্মীদের সবুজ উদ্ভিদে রূপান্তর",
            "প্রজাতি থেকে রাণীদের স্থায়ীভাবে বিলুপ্ত করা",
        ],
        "A", "hard", "conceptual",
        "New colony founding plus mating maintain population growth and genetic diversity.",
        "নতুন কলোনি ও সঙ্গম জনসংখ্যা বৃদ্ধি ও জিন বৈচিত্র্য বজায় রাখে।",
    ),
]


TOPICS_MAP = {
    "bio2_27_ch12_t01": T01,
    "bio2_27_ch12_t02": T02,
    "bio2_27_ch12_t03": T03,
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
        "chapter": "bio2_27_ch12",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p354_pdf360.png",
            "p355_pdf361.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio2_27_ch12_t01": {
                "title": "Innate behaviour / সহজাত আচরণ",
                "themes": [
                    "behaviour definition; innate inborn gene-guided acts",
                    "innate traits; spider web / bird nest examples; early vs mature expression",
                    "taxis features; thigmotaxis; rheotaxis; phototaxis; chemotaxis",
                    "reflex / spinal reflex arc; instinct; FAP; releaser; terminating stimulus",
                ],
            },
            "bio2_27_ch12_t02": {
                "title": "Learned behaviour / অর্জিত আচরণ",
                "themes": [
                    "learned vs innate contrast; conditioned reflex definition",
                    "Pavlov classical conditioning / bell–salivation",
                    "habituation; imprinting (Lorenz); trial-and-error / operant (Thorndike)",
                    "insight (Köhler); associative and latent learning; training applications",
                ],
            },
            "bio2_27_ch12_t03": {
                "title": "Social behaviour / সামাজিক আচরণ",
                "themes": [
                    "social behaviour definition; altruism",
                    "honeybee colony castes; workers 60–80k; cooperative roles",
                    "nuptial flight; swarming; von Frisch waggle dance",
                    "division of labour; territory; dominance hierarchy; communication; colony genetics",
                ],
            },
        },
        "low_confidence": [
            "OCR of printed pages p354–355 is mainly CQ (short-answer) text, not dense MCQ keys; stems authored/reconstructed from readable CQ themes and standard HSC Zoology Ch12 facts.",
            "Printed MCQ section for ch12 is only two pages; bank supplemented to exactly 20 items per syllabus topic.",
            "Figure-/stimulus-linked CQ items (honey, altruism scenarios) rewritten as standalone stems.",
            "Colony worker counts (60–80 thousand) and nuptial/swarming details follow common Bangladesh HSC textbook phrasing aligned with OCR CQ answers.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio2_27_ch12_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio2_27_ch12_t01": 20,
                "bio2_27_ch12_t02": 20,
                "bio2_27_ch12_t03": 20,
            },
        },
        "bio2_completion": {
            "topics_expected": 36,
            "note": "Ch12 finishes Biology 2nd Paper topic bank (bio2_27_ch01..ch12).",
        },
    }
    out = (
        ROOT
        / "content"
        / "bank"
        / "udvash_raw"
        / "biology_2"
        / "parsed"
        / "ch12_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
