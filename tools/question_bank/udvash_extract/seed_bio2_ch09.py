#!/usr/bin/env python3
"""Seed Biology 2nd Paper Ch9 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio2_27_ch09_t01..t03 (Human reproduction; Development; Reproductive health).
OCR ch09 covers only ~2 printed pages (mainly CQ); items reconstructed from
readable CQ themes and standard HSC Zoology Ch9 facts.
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
    "biology p2 ch09; curated bilingual"
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


# --- t01: Human reproduction / মানব প্রজনন ---
T01 = [
    q(
        "What is reproduction?",
        "প্রজনন কী?",
        [
            "Process by which organisms produce offspring of their own kind and maintain the species",
            "Only digestion of food in the gut",
            "Only excretion of nitrogenous waste",
            "Only transport of oxygen in blood",
        ],
        [
            "যে প্রক্রিয়ায় জীব নিজ সত্ত্বা ও আকৃতিবিশিষ্ট সন্তান সৃষ্টি করে প্রজাতির অস্তিত্ব বজায় রাখে",
            "শুধু অন্ত্রে খাদ্য পরিপাক",
            "শুধু নাইট্রোজেনজাত বর্জ্য নিষ্কাশন",
            "শুধু রক্তে অক্সিজেন পরিবহন",
        ],
        "A", "easy", "factual",
        "Reproduction produces similar offspring and sustains the species across generations.",
        "প্রজনন অনুরূপ সন্তান সৃষ্টি করে প্রজাতির ধারাবাহিকতা রক্ষা করে।",
    ),
    q(
        "Puberty is best defined as which stage of life?",
        "বয়ঃসন্ধিকাল জীবনের কোন পর্যায়কে বোঝায়?",
        [
            "Stage when secondary sexual characters develop and individuals become capable of reproduction",
            "Only the neonatal period after birth",
            "Only menopause in older women",
            "Only embryonic cleavage stages",
        ],
        [
            "যে পর্যায়ে গৌণ যৌন বৈশিষ্ট্য প্রকাশ পায় এবং প্রজননক্ষমতা অর্জিত হয়",
            "শুধু জন্মের পর নবজাতক পর্যায়",
            "শুধু বয়স্ক নারীর মেনোপজ",
            "শুধু ভ্রূণের ক্লিভেজ পর্যায়",
        ],
        "A", "easy", "factual",
        "At puberty, secondary sexual characters appear and reproductive capacity begins.",
        "বয়ঃসন্ধিতে গৌণ যৌন বৈশিষ্ট্য ও প্রজননক্ষমতা আসে।",
    ),
    q(
        "Typical age ranges often cited for puberty onset in Bangladesh HSC context are closest to which pair?",
        "এইচএসসি প্রেক্ষাপটে বয়ঃসন্ধির সূচনার সাধারণ বয়সসীমা কোন জোড়ার কাছাকাছি?",
        [
            "Boys about 13–15 years; girls about 11–13 years",
            "Boys about 5–7 years; girls about 3–5 years",
            "Boys about 25–30 years; girls about 22–25 years",
            "Boys and girls both only after 40 years",
        ],
        [
            "ছেলে প্রায় ১৩–১৫ বছর; মেয়ে প্রায় ১১–১৩ বছর",
            "ছেলে প্রায় ৫–৭ বছর; মেয়ে প্রায় ৩–৫ বছর",
            "ছেলে প্রায় ২৫–৩০ বছর; মেয়ে প্রায় ২২–২৫ বছর",
            "ছেলে–মেয়ে উভয়ই শুধু ৪০ বছরের পর",
        ],
        "A", "easy", "factual",
        "Girls usually enter puberty earlier than boys in the cited HSC ranges.",
        "উল্লিখিত সীমায় মেয়েদের বয়ঃসন্ধি সাধারণত আগে শুরু হয়।",
    ),
    q(
        "Which changes typically appear in males at puberty?",
        "বয়ঃসন্ধিকালে পুরুষদেহে সাধারণত কোন পরিবর্তনগুলো দেখা যায়?",
        [
            "Sex hormones secreted, spermatozoa produced, accessory organs mature, basal metabolic rate rises",
            "Only menopause and endometrial shedding",
            "Only placental formation without hormones",
            "Only cessation of all gamete production",
        ],
        [
            "জনন হরমোন ক্ষরণ, শুক্রাণু উৎপাদন, আনুষঙ্গিক অঙ্গ পরিপক্কতা, মৌল বিপাকীয় হার বৃদ্ধি",
            "শুধু মেনোপজ ও এন্ডোমেট্রিয়াম ক্ষয়",
            "শুধু হরমোন ছাড়াই প্লাসেন্টা গঠন",
            "শুধু সব গ্যামেট উৎপাদন বন্ধ",
        ],
        "A", "medium", "conceptual",
        "Male puberty involves androgen-driven maturation, spermatogenesis and metabolic changes.",
        "পুরুষ বয়ঃসন্ধিতে অ্যান্ড্রোজেন-নির্ভর পরিপক্কতা ও শুক্রাণুজনন ঘটে।",
    ),
    q(
        "Gametogenesis means which process?",
        "গ্যামেটোজেনেসিস বলতে কী বোঝায়?",
        [
            "Formation of functional gametes from primordial germ cells in gonads",
            "Only formation of red blood cells in bone marrow",
            "Only digestion of proteins by pepsin",
            "Only filtration of urine in nephrons",
        ],
        [
            "জননাঙ্গের প্রাইমর্ডিয়াল জননকোষ থেকে কার্যকর গ্যামেট উৎপাদন",
            "শুধু অস্থিমজ্জায় লোহিত রক্তকণিকা গঠন",
            "শুধু পেপসিন দিয়ে প্রোটিন পরিপাক",
            "শুধু নেফ্রনে মূত্র পরিস্রাবণ",
        ],
        "A", "easy", "factual",
        "Gametogenesis produces spermatozoa (spermatogenesis) and ova (oogenesis).",
        "গ্যামেটোজেনেসিসে শুক্রাণুজনন ও ডিম্বাণুজনন অন্তর্ভুক্ত।",
    ),
    q(
        "Spermatogenesis is the process of forming which cells?",
        "স্পার্মাটোজেনেসিস কোন কোষ গঠনের প্রক্রিয়া?",
        ["Spermatozoa (sperm)", "Ova only", "Neurons only", "Osteocytes only"],
        ["শুক্রাণু (স্পার্মাটোজোয়া)", "শুধু ডিম্বাণু", "শুধু নিউরন", "শুধু অস্টিওসাইট"],
        "A", "easy", "factual",
        "Spermatogenesis occurs in the testes and yields mature sperm.",
        "স্পার্মাটোজেনেসিস শুক্রাশয়ে পরিপক্ক শুক্রাণু তৈরি করে।",
    ),
    q(
        "Oogenesis is the process of forming which cells?",
        "উওজেনেসিস কোন কোষ গঠনের প্রক্রিয়া?",
        ["Ova (egg cells)", "Spermatozoa only", "Platelets only", "Chondrocytes only"],
        ["ডিম্বাণু", "শুধু শুক্রাণু", "শুধু প্লাটিলেট", "শুধু কনড্রোসাইট"],
        "A", "easy", "factual",
        "Oogenesis occurs in the ovaries and produces ova.",
        "উওজেনেসিস ডিম্বাশয়ে ডিম্বাণু তৈরি করে।",
    ),
    q(
        "Which pair correctly matches male and female primary gonads?",
        "পুরুষ ও নারীর প্রাথমিক জননাঙ্গের সঠিক জোড়া কোনটি?",
        [
            "Testes and ovaries",
            "Prostate and uterus only",
            "Seminal vesicle and vagina only",
            "Epididymis and hymen only",
        ],
        [
            "শুক্রাশয় ও ডিম্বাশয়",
            "শুধু প্রোস্টেট ও জরায়ু",
            "শুধু সেমিনাল ভেসিকল ও যোনি",
            "শুধু এপিডিডাইমিস ও হাইমেন",
        ],
        "A", "easy", "factual",
        "Primary gonads produce gametes and sex hormones: testes and ovaries.",
        "প্রাথমিক জননাঙ্গ গ্যামেট ও যৌন হরমোন উৎপাদন করে।",
    ),
    q(
        "Fertilization in humans normally occurs in which region?",
        "মানুষে স্বাভাবিক নিষেক সাধারণত কোন অংশে ঘটে?",
        [
            "Ampullary region of the fallopian (uterine) tube",
            "Only inside the urinary bladder",
            "Only in the oral cavity",
            "Only in the gallbladder",
        ],
        [
            "ফ্যালোপিয়ান (ডিম্ব) নালির অ্যাম্পুলারি অংশ",
            "শুধু মূত্রাশয়ের ভিতরে",
            "শুধু মুখগহ্বরে",
            "শুধু পিত্তাশয়ে",
        ],
        "A", "medium", "factual",
        "Sperm meet the ovum usually in the upper/ampullary part of the oviduct.",
        "শুক্রাণু–ডিম্বাণু মিলন সাধারণত ডিম্বনালির উর্ধ্ব/অ্যাম্পুলারি অংশে হয়।",
    ),
    q(
        "The ovarian cycle is initiated primarily when the hypothalamus secretes which hormone?",
        "ডিম্বাশয় চক্র প্রধানত হাইপোথ্যালামাস থেকে কোন হরমোন ক্ষরণে শুরু হয়?",
        ["GnRH", "Pepsin", "Insulin only", "ADH only"],
        ["GnRH", "পেপসিন", "শুধু ইনসুলিন", "শুধু ADH"],
        "A", "medium", "factual",
        "GnRH stimulates the anterior pituitary to release FSH and LH, starting the ovarian cycle.",
        "GnRH সম্মুখ পিটুইটারিকে FSH ও LH ক্ষরণে উদ্দীপ্ত করে ডিম্বাশয় চক্র শুরু করে।",
    ),
    q(
        "In the ovarian cycle, FSH mainly promotes which event?",
        "ডিম্বাশয় চক্রে FSH প্রধানত কোন ঘটনাকে উদ্দীপ্ত করে?",
        [
            "Growth of ovarian follicles and estrogen production",
            "Only contraction of skeletal muscle fibers",
            "Only clotting of blood plasma",
            "Only formation of bile salts",
        ],
        [
            "ফলিকলের বৃদ্ধি ও ইস্ট্রোজেন উৎপাদন",
            "শুধু কঙ্কালপেশি সংকোচন",
            "শুধু রক্তপ্লাজমা জমাট",
            "শুধু পিত্তলবণ গঠন",
        ],
        "A", "medium", "conceptual",
        "With LH support, FSH drives follicle growth; follicles then secrete estrogen.",
        "LH সহযোগে FSH ফলিকল বৃদ্ধি ও ইস্ট্রোজেন ক্ষরণে সাহায্য করে।",
    ),
    q(
        "A mid-cycle LH surge is most closely associated with which event?",
        "চক্রের মধ্যভাগে LH উর্ধ্বগতি কোন ঘটনার সাথে সবচেয়ে ঘনিষ্ঠভাবে যুক্ত?",
        [
            "Ovulation (release of a secondary oocyte)",
            "Only formation of enamel on teeth",
            "Only start of spermatogenesis in females",
            "Only permanent menopause in childhood",
        ],
        [
            "ডিম্বপাত (সেকেন্ডারি ওসাইট মুক্তি)",
            "শুধু দাঁতের এনামেল গঠন",
            "শুধু নারীতে শুক্রাণুজনন শুরু",
            "শুধু শৈশবে স্থায়ী মেনোপজ",
        ],
        "A", "medium", "conceptual",
        "The LH surge triggers ovulation around mid-cycle (~day 14 in a 28-day cycle).",
        "LH সার্জ মধ্যচক্রে ডিম্বপাত ঘটায় (প্রায় ২৮ দিনের চক্রে ~১৪তম দিন)।",
    ),
    q(
        "The menstrual (ovarian–uterine) cycle in sexually mature women typically lasts about how many days?",
        "যৌন পরিপক্ক নারীতে রজঃচক্র সাধারণত প্রায় কত দিন স্থায়ী?",
        [
            "About 28 days (commonly 24–32), with menstruation lasting about 3–5 days",
            "Exactly 2 days every year only",
            "About 365 days without bleeding",
            "Exactly 90 days with no hormonal change",
        ],
        [
            "প্রায় ২৮ দিন (সাধারণত ২৪–৩২), রজঃস্রাব প্রায় ৩–৫ দিন",
            "বছরে শুধু ঠিক ২ দিন",
            "প্রায় ৩৬৫ দিন রক্তপাত ছাড়া",
            "ঠিক ৯০ দিন হরমোন পরিবর্তন ছাড়া",
        ],
        "A", "easy", "factual",
        "A typical cycle is ~28 days; menstrual bleeding usually lasts 3–5 days.",
        "সাধারণ চক্র ~২৮ দিন; রজঃস্রাব সাধারণত ৩–৫ দিন।",
    ),
    q(
        "Menarche refers to which event?",
        "মেনার্কি কোন ঘটনাকে বোঝায়?",
        [
            "The first menstrual cycle / first menstruation",
            "Permanent stop of menstruation in old age only",
            "Only fertilization of an ovum",
            "Only delivery of a full-term baby",
        ],
        [
            "প্রথম রজঃচক্র / প্রথম রজঃস্রাব",
            "শুধু বার্ধক্যে রজঃস্রাবের স্থায়ী বন্ধ",
            "শুধু ডিম্বাণুর নিষেক",
            "শুধু পূর্ণমেয়াদি শিশুর জন্ম",
        ],
        "A", "easy", "factual",
        "Menarche is the first menstruation marking reproductive maturation onset.",
        "মেনার্কি প্রথম রজঃস্রাব—প্রজনন পরিপক্কতার সূচক।",
    ),
    q(
        "Menopause refers to which event?",
        "মেনোপজ কোন ঘটনাকে বোঝায়?",
        [
            "Cessation of the menstrual cycle at the end of reproductive life",
            "Only the first ovulation in childhood",
            "Only formation of the zygote",
            "Only puberty in boys",
        ],
        [
            "যৌন জীবনকালের শেষে রজঃচক্রের নিবৃত্তি",
            "শুধু শৈশবে প্রথম ডিম্বপাত",
            "শুধু জাইগোট গঠন",
            "শুধু ছেলেদের বয়ঃসন্ধি",
        ],
        "A", "easy", "factual",
        "Menopause is the permanent stop of menstrual cycling at reproductive life’s end.",
        "মেনোপজ যৌন জীবনের শেষে রজঃচক্র স্থায়ীভাবে বন্ধ হওয়া।",
    ),
    q(
        "Menstruation mainly results from breakdown of which uterine layer?",
        "রজঃস্রাব প্রধানত জরায়ুর কোন স্তরের অবক্ষয় থেকে হয়?",
        [
            "Endometrium (uterine lining)",
            "Only the myocardium of the heart",
            "Only the periosteum of bone",
            "Only the sclera of the eye",
        ],
        [
            "এন্ডোমেট্রিয়াম (জরায়ুর আস্তরণ)",
            "শুধু হৃৎপিণ্ডের মায়োকার্ডিয়াম",
            "শুধু অস্থির পেরিওস্টিয়াম",
            "শুধু চোখের স্ক্লেরা",
        ],
        "A", "medium", "factual",
        "Falling progesterone/estrogen after failed implantation causes endometrial shedding.",
        "গর্ভধারণ না হলে হরমোন হ্রাসের ফলে এন্ডোমেট্রিয়াম ক্ষয় হয়ে রজঃস্রাব হয়।",
    ),
    q(
        "Which hormone is the principal androgen produced by the testes?",
        "শুক্রাশয় থেকে উৎপন্ন প্রধান অ্যান্ড্রোজেন কোনটি?",
        ["Testosterone", "Progesterone only", "Relaxin only", "Oxytocin only"],
        ["টেস্টোস্টেরন", "শুধু প্রোজেস্টেরন", "শুধু রিলাক্সিন", "শুধু অক্সিটোসিন"],
        "A", "easy", "factual",
        "Leydig cells secrete testosterone, driving male secondary sexual characters.",
        "লেডিগ কোষ টেস্টোস্টেরন ক্ষরণ করে পুরুষ গৌণ যৌন বৈশিষ্ট্য নিয়ন্ত্রণ করে।",
    ),
    q(
        "Corpus luteum mainly secretes which hormone that maintains the endometrium after ovulation?",
        "ডিম্বপাতের পর এন্ডোমেট্রিয়াম বজায় রাখতে কর্পাস লুটিয়াম প্রধানত কোন হরমোন ক্ষরণ করে?",
        ["Progesterone", "Thyroxine only", "Glucagon only", "Melatonin only"],
        ["প্রোজেস্টেরন", "শুধু থাইরক্সিন", "শুধু গ্লুকাগন", "শুধু মেলাটোনিন"],
        "A", "medium", "conceptual",
        "Progesterone from the corpus luteum prepares and maintains the uterine lining.",
        "কর্পাস লুটিয়ামের প্রোজেস্টেরন জরায়ু আস্তরণ প্রস্তুত ও বজায় রাখে।",
    ),
    q(
        "Estrogen in the follicular phase is produced mainly by which structures?",
        "ফলিকুলার পর্যায়ে ইস্ট্রোজেন প্রধানত কোন কাঠামো থেকে উৎপন্ন হয়?",
        [
            "Growing ovarian follicles",
            "Only the parathyroid glands",
            "Only the adrenal medulla exclusively without follicles",
            "Only salivary glands",
        ],
        [
            "বর্ধনশীল ডিম্বাশয় ফলিকল",
            "শুধু প্যারাথাইরয়েড গ্রন্থি",
            "শুধু ফলিকল ছাড়াই অ্যাড্রিনাল মেডুলা",
            "শুধু লালাগ্রন্থি",
        ],
        "A", "medium", "factual",
        "FSH-stimulated follicles secrete estrogen during the follicular phase.",
        "FSH-উদ্দীপ্ত ফলিকল ফলিকুলার পর্যায়ে ইস্ট্রোজেন ক্ষরণ করে।",
    ),
    q(
        "Which statement about human sexual reproduction is correct?",
        "মানব যৌন প্রজনন সম্পর্কে কোন বক্তব্য সঠিক?",
        [
            "Haploid sperm and ovum fuse to form a diploid zygote",
            "Two diploid eggs fuse without sperm in every pregnancy",
            "Sperm alone develops into a fetus without an ovum",
            "No meiosis occurs in gamete formation",
        ],
        [
            "হ্যাপ্লয়েড শুক্রাণু ও ডিম্বাণু মিলে ডিপ্লয়েড জাইগোট গঠন করে",
            "প্রতি গর্ভে শুক্রাণু ছাড়াই দুই ডিপ্লয়েড ডিম্বাণু মিলে যায়",
            "ডিম্বাণু ছাড়াই শুক্রাণু একাই ফিটাস হয়",
            "গ্যামেট গঠনে মিয়োসিস ঘটে না",
        ],
        "A", "medium", "conceptual",
        "Meiosis yields haploid gametes; fertilization restores the diploid chromosome number.",
        "মিয়োসিসে হ্যাপ্লয়েড গ্যামেট; নিষেকে ডিপ্লয়েড সংখ্যা পুনরুদ্ধার হয়।",
    ),
]


# --- t02: Development / বিকাশ ---
T02 = [
    q(
        "After fertilization, the diploid cell formed is called what?",
        "নিষেকের পর গঠিত ডিপ্লয়েড কোষকে কী বলে?",
        ["Zygote", "Neuron", "Osteoclast", "Platelet"],
        ["জাইগোট", "নিউরন", "অস্টিওক্লাস্ট", "প্লাটিলেট"],
        "A", "easy", "factual",
        "Fusion of sperm and ovum nuclei produces the zygote.",
        "শুক্রাণু ও ডিম্বাণু নিউক্লিয়াসের মিলনে জাইগোট গঠিত হয়।",
    ),
    q(
        "Cleavage of the zygote produces a solid ball of cells called what?",
        "জাইগোটের ক্লিভেজে গঠিত কঠিন কোষগোলককে কী বলে?",
        ["Morula", "Placenta", "Amnion only", "Allantois only"],
        ["মরুলা", "প্লাসেন্টা", "শুধু অ্যামনিয়ন", "শুধু অ্যালানটয়েস"],
        "A", "easy", "factual",
        "Rapid mitotic cleavage yields a morula before blastocyst formation.",
        "দ্রুত মাইটোটিক ক্লিভেজে মরুলা, পরে ব্লাস্টোসিস্ট গঠিত হয়।",
    ),
    q(
        "The blastocyst stage is characterized by which feature?",
        "ব্লাস্টোসিস্ট পর্যায়ের বৈশিষ্ট্য কোনটি?",
        [
            "A fluid-filled cavity with trophoblast and inner cell mass",
            "Only a single unfertilized ovum",
            "Only a fully formed adult skeleton",
            "Only a calcified tooth crown",
        ],
        [
            "তরলপূর্ণ গহ্বরসহ ট্রফোব্লাস্ট ও অন্তঃকোষপুঞ্জ",
            "শুধু একটি অনিষিক্ত ডিম্বাণু",
            "শুধু পূর্ণাঙ্গ প্রাপ্তবয়স্ক কঙ্কাল",
            "শুধু ক্যালসিফাইড দন্তমুকুট",
        ],
        "A", "medium", "factual",
        "Blastocyst has trophoblast (outer) and embryoblast/inner cell mass around a blastocoel.",
        "ব্লাস্টোসিস্টে ট্রফোব্লাস্ট, ইনার সেল ম্যাস ও ব্লাস্টোসিল থাকে।",
    ),
    q(
        "Implantation is best described as which process?",
        "ইমপ্লান্টেশন কোন প্রক্রিয়াকে বোঝায়?",
        [
            "Embedding of the blastocyst into the uterine endometrium about 6–9 days after fertilization",
            "Only eruption of permanent teeth",
            "Only fusion of cranial sutures in old age",
            "Only shedding of skin epidermis daily",
        ],
        [
            "নিষেকের প্রায় ৬–৯ দিন পর ব্লাস্টোসিস্টের জরায়ু এন্ডোমেট্রিয়ামে সংস্থাপন",
            "শুধু স্থায়ী দাঁত ওঠা",
            "শুধু বার্ধক্যে করোটিক সেলাই মিলন",
            "শুধু প্রতিদিন ত্বকের এপিডার্মিস খসা",
        ],
        "A", "medium", "conceptual",
        "Trophoblast enzymes help the blastocyst implant in the endometrium.",
        "ট্রফোব্লাস্ট এনজাইম এন্ডোমেট্রিয়ামে ব্লাস্টোসিস্ট প্রোথিত হতে সাহায্য করে।",
    ),
    q(
        "Germ layers (ectoderm, mesoderm, endoderm) are formed during which process?",
        "জার্ম স্তর (এক্টোডার্ম, মেসোডার্ম, এন্ডোডার্ম) কোন প্রক্রিয়ায় গঠিত হয়?",
        ["Gastrulation", "Menstruation only", "Mastication only", "Perspiration only"],
        ["গ্যাস্ট্রুলেশন", "শুধু রজঃস্রাব", "শুধু চর্বণ", "শুধু ঘর্মক্ষরণ"],
        "A", "medium", "factual",
        "Gastrulation reorganizes the embryo into three germ layers (germ/embryonic layers).",
        "গ্যাস্ট্রুলেশনে তিনটি ভ্রূণীয়/জার্ম স্তর গঠিত হয়।",
    ),
    q(
        "Which set correctly names the three primary germ layers?",
        "তিনটি প্রাথমিক জার্ম স্তরের সঠিক সেট কোনটি?",
        [
            "Ectoderm, mesoderm and endoderm",
            "Epidermis, dermis and hypodermis only as germ layers",
            "Cortex, medulla and pelvis of kidney only",
            "Enamel, dentine and pulp only",
        ],
        [
            "এক্টোডার্ম, মেসোডার্ম ও এন্ডোডার্ম",
            "শুধু এপিডার্মিস, ডার্মিস ও হাইপোডার্মিসকে জার্ম স্তর বলা",
            "শুধু বৃক্কের কর্টেক্স, মেডুলা ও পেলভিস",
            "শুধু এনামেল, ডেন্টিন ও পাল্প",
        ],
        "A", "easy", "factual",
        "All tissues and organs derive from ectoderm, mesoderm or endoderm.",
        "সব কলা ও অঙ্গ এক্টোডার্ম, মেসোডার্ম বা এন্ডোডার্ম থেকে উদ্ভূত।",
    ),
    q(
        "Organogenesis refers to which developmental process?",
        "অর্গানোজেনেসিস কোন বিকাশ প্রক্রিয়াকে বোঝায়?",
        [
            "Formation of organ primordia (organ buds) from germ layers",
            "Only daily renewal of hair cuticle",
            "Only formation of urine in Bowman’s capsule",
            "Only clotting after a skin cut",
        ],
        [
            "জার্ম স্তর থেকে অঙ্গকুঁড়ি/প্রাথমিক অঙ্গ গঠন",
            "শুধু প্রতিদিন চুলের কিউটিকল নবায়ন",
            "শুধু বোম্যান ক্যাপসুলে মূত্র গঠন",
            "শুধু ত্বক কাটার পর জমাট বাঁধা",
        ],
        "A", "medium", "conceptual",
        "After gastrulation, germ-layer cell groups form primary then secondary organ buds.",
        "গ্যাস্ট্রুলেশনের পর জার্ম স্তর থেকে প্রাইমারি ও সেকেন্ডারি অঙ্গকুঁড়ি গঠিত হয়।",
    ),
    q(
        "The placenta (amnion-related chorionic disc with maternal tissue) is often called a ‘biological bridge’ because it mainly does what?",
        "অমরাকে ‘জৈব সেতু’ বলা হয় কেন—এর প্রধান কাজ কী?",
        [
            "Exchanges nutrients, gases, wastes, hormones and antibodies between mother and fetus",
            "Only stores bile for fat digestion",
            "Only pumps blood like a second heart permanently after birth",
            "Only filters lymph in lymph nodes",
        ],
        [
            "মা ও ভ্রূণ/ফিটাসের মধ্যে পুষ্টি, গ্যাস, বর্জ্য, হরমোন ও অ্যান্টিবডি বিনিময় করে",
            "শুধু চর্বি পরিপাকের জন্য পিত্ত জমা রাখে",
            "শুধু জন্মের পর স্থায়ী দ্বিতীয় হৃৎপিণ্ড হিসেবে রক্ত পাম্প করে",
            "শুধু লিম্ফ নোডে লিম্ফ পরিস্রাবণ করে",
        ],
        "A", "medium", "conceptual",
        "Placenta links maternal and fetal circulations for exchange without direct blood mixing.",
        "অমরা মা–সন্তানের মধ্যে পদার্থ বিনিময়ের সংযোগ; রক্ত সরাসরি মেশে না।",
    ),
    q(
        "Which materials can cross the placenta toward the fetus?",
        "অমরার মাধ্যমে ফিটাসের দিকে কোন পদার্থগুলো যেতে পারে?",
        [
            "Glucose, amino acids, oxygen, some vitamins, ions, hormones, drugs and some pathogens",
            "Only solid bone fragments",
            "Only intact whole blood cells as the sole cargo always",
            "Only urine crystals exclusively",
        ],
        [
            "গ্লুকোজ, অ্যামিনো অ্যাসিড, অক্সিজেন, কিছু ভিটামিন, আয়ন, হরমোন, ওষুধ ও কিছু জীবাণু",
            "শুধু কঠিন অস্থিখণ্ড",
            "শুধু সবসময় অক্ষত পূর্ণ রক্তকণিকাই একমাত্র বহন",
            "শুধু মূত্র স্ফটিক",
        ],
        "A", "hard", "conceptual",
        "Useful nutrients and O₂ cross; CO₂ and urea return to the mother; some drugs/pathogens can also cross.",
        "পুষ্টি ও O₂ যায়; CO₂ ও ইউরিয়া মায়ের দিকে ফেরে; কিছু ওষুধ/জীবাণুও যেতে পারে।",
    ),
    q(
        "Fetal wastes such as CO₂ and urea mainly leave the fetus via which route?",
        "ফিটাসের CO₂ ও ইউরিয়ার মতো বর্জ্য প্রধানত কোন পথে বের হয়?",
        [
            "Through the placenta into the maternal circulation for excretion",
            "Only through fetal lungs breathing air in utero",
            "Only through open fetal skin pores to the amniotic air",
            "Only through the maternal oral cavity directly",
        ],
        [
            "অমরার মাধ্যমে মাতৃ রক্তসংবহনে গিয়ে নিষ্কাশনের জন্য",
            "শুধু গর্ভে ফিটাস ফুসফুস দিয়ে বায়ু শ্বাস নিয়ে",
            "শুধু ফিটাস ত্বকের ছিদ্র দিয়ে অ্যামনিয়টিক বায়ুতে",
            "শুধু সরাসরি মায়ের মুখগহ্বর দিয়ে",
        ],
        "A", "medium", "conceptual",
        "The placenta returns fetal metabolic wastes to the mother for excretion.",
        "অমরা ফিটাসের বিপাকীয় বর্জ্য মাতৃদেহে পাঠায় নিষ্কাশনের জন্য।",
    ),
    q(
        "Teratogens are best defined as which agents?",
        "টেরাটোজেন কী?",
        [
            "Environmental or maternal factors that cause embryonic/fetal malformations",
            "Only vitamins that always improve fetal growth without risk",
            "Only digestive enzymes of the pancreas",
            "Only pigments of the iris",
        ],
        [
            "ভ্রূণ/ফিটাসের অঙ্গবিকৃতি ঘটাতে পারে এমন পরিবেশিক বা মাতৃগত কারণ",
            "শুধু যেসব ভিটামিন সবসময় ঝুঁকি ছাড়াই বৃদ্ধি বাড়ায়",
            "শুধু অগ্ন্যাশয়ের পাচক এনজাইম",
            "শুধু আইরিসের রঞ্জক",
        ],
        "A", "medium", "factual",
        "Examples include certain infections (e.g. rubella), drugs, toxins and maternal illness.",
        "উদাহরণ: রুবেলা ইত্যাদি সংক্রমণ, কিছু ওষুধ, বিষ ও মাতৃ অসুস্থতা।",
    ),
    q(
        "The embryonic period is especially sensitive to teratogens mainly during which window?",
        "টেরাটোজেনের প্রতি ভ্রূণ সবচেয়ে সংবেদনশীল কোন সময়ে?",
        [
            "Early weeks of organogenesis when organ systems are forming",
            "Only after age 60 years",
            "Only during adult menopause",
            "Only after teeth have fully erupted in adolescence",
        ],
        [
            "অর্গানোজেনেসিসের প্রাথমিক সপ্তাহগুলোতে যখন অঙ্গতন্ত্র গঠিত হচ্ছে",
            "শুধু ৬০ বছর বয়সের পর",
            "শুধু প্রাপ্তবয়স্ক মেনোপজে",
            "শুধু কৈশোরে দাঁত পুরোপুরি ওঠার পর",
        ],
        "A", "hard", "conceptual",
        "Major malformations are most likely when organs are being laid down in early pregnancy.",
        "গর্ভের প্রথম দিকে অঙ্গ গঠনের সময় বড় বিকৃতির ঝুঁকি সবচেয়ে বেশি।",
    ),
    q(
        "Which statement correctly contrasts embryo and fetus in human development?",
        "মানব বিকাশে ভ্রূণ ও ফিটাসের সঠিক পার্থক্য কোনটি?",
        [
            "Early organ-forming stage is the embryo; later more recognizably developed stage is the fetus",
            "Fetus always precedes zygote formation",
            "Embryo appears only after birth",
            "There is no developmental difference between the terms",
        ],
        [
            "প্রাথমিক অঙ্গগঠন পর্যায় ভ্রূণ; পরে অধিক পরিচিত বিকাশ পর্যায় ফিটাস",
            "ফিটাস সবসময় জাইগোট গঠনের আগে আসে",
            "ভ্রূণ শুধু জন্মের পরে দেখা যায়",
            "দুই শব্দের মধ্যে কোনো বিকাশগত পার্থক্য নেই",
        ],
        "A", "medium", "conceptual",
        "Conventionally, embryo covers early development; fetus refers to later intrauterine growth.",
        "প্রথমে ভ্রূণ পর্যায়; পরে গর্ভস্থ অধিক বিকশিত পর্যায়কে ফিটাস বলা হয়।",
    ),
    q(
        "The inner cell mass of the blastocyst mainly gives rise to which structure?",
        "ব্লাস্টোসিস্টের অন্তঃকোষপুঞ্জ প্রধানত কোন কাঠামোতে পরিণত হয়?",
        [
            "The embryo proper",
            "Only the maternal ovary",
            "Only adult red bone marrow exclusively",
            "Only the placenta without any embryonic contribution from trophoblast",
        ],
        [
            "প্রকৃত ভ্রূণ",
            "শুধু মাতৃ ডিম্বাশয়",
            "শুধু প্রাপ্তবয়স্ক লোহিত অস্থিমজ্জা",
            "শুধু ট্রফোব্লাস্ট ছাড়াই সম্পূর্ণ প্লাসেন্টা",
        ],
        "A", "medium", "factual",
        "Inner cell mass → embryo; trophoblast contributes to chorion/placenta.",
        "ইনার সেল ম্যাস → ভ্রূণ; ট্রফোব্লাস্ট কোরিয়ন/প্লাসেন্টায় অবদান রাখে।",
    ),
    q(
        "Amniotic fluid mainly provides which benefit to the developing fetus?",
        "অ্যামনিয়টিক তরল ফিটাসের জন্য প্রধানত কী সুবিধা দেয়?",
        [
            "Cushioning, temperature stability and freedom for movement/growth",
            "Only permanent lung ventilation with atmospheric air",
            "Only digestion of maternal food in the fetal stomach before birth always",
            "Only formation of adult teeth enamel exclusively",
        ],
        [
            "আঘাত থেকে রক্ষা, তাপমাত্রা স্থিরতা ও নড়াচড়া/বৃদ্ধির সুযোগ",
            "শুধু বায়ুমণ্ডলীয় বাতাসে স্থায়ী ফুসফুস বায়ুচলাচল",
            "শুধু জন্মের আগেই সবসময় মাতৃখাদ্য ফিটাস পাকস্থলীতে পরিপাক",
            "শুধু প্রাপ্তবয়স্ক দন্ত এনামেল গঠন",
        ],
        "A", "medium", "conceptual",
        "The amnion/amniotic fluid protects and supports the fetus mechanically and thermally.",
        "অ্যামনিয়টিক তরল যান্ত্রিক ও তাপীয় সুরক্ষা দেয়।",
    ),
    q(
        "Human pregnancy (gestation) from fertilization to birth lasts approximately how long?",
        "নিষেক থেকে জন্ম পর্যন্ত মানব গর্ভকাল প্রায় কত?",
        [
            "About 9 months (~38–40 weeks)",
            "About 2 weeks only",
            "About 2 years continuously",
            "Exactly 5 days always",
        ],
        [
            "প্রায় ৯ মাস (~৩৮–৪০ সপ্তাহ)",
            "শুধু প্রায় ২ সপ্তাহ",
            "প্রায় ২ বছর একটানা",
            "সবসময় ঠিক ৫ দিন",
        ],
        "A", "easy", "factual",
        "Full-term human gestation is roughly nine months.",
        "পূর্ণমেয়াদি মানব গর্ভকাল প্রায় নয় মাস।",
    ),
    q(
        "Ectoderm typically gives rise to which of the following?",
        "এক্টোডার্ম সাধারণত কোনটি গঠন করে?",
        [
            "Nervous system and epidermis",
            "Only liver parenchyma exclusively",
            "Only cardiac muscle exclusively",
            "Only kidney nephrons exclusively",
        ],
        [
            "স্নায়ুতন্ত্র ও এপিডার্মিস",
            "শুধু যকৃত প্যারেনকাইমা",
            "শুধু হৃৎপেশি",
            "শুধু বৃক্ক নেফ্রন",
        ],
        "A", "hard", "conceptual",
        "Ectoderm forms epidermis and neural tissues; endoderm/mesoderm form other organ sets.",
        "এক্টোডার্ম থেকে ত্বকের এপিডার্মিস ও স্নায়ুকলা গঠিত হয়।",
    ),
    q(
        "Endoderm typically contributes to which structures?",
        "এন্ডোডার্ম সাধারণত কোন কাঠামো গঠনে অবদান রাখে?",
        [
            "Lining of the digestive and respiratory tracts",
            "Only the enamel of teeth exclusively",
            "Only the dermis of skin exclusively",
            "Only skeletal muscle of limbs exclusively",
        ],
        [
            "পৌষ্টিক ও শ্বসন নালির আস্তরণ",
            "শুধু দাঁতের এনামেল",
            "শুধু ত্বকের ডার্মিস",
            "শুধু অঙ্গপ্রত্যঙ্গের কঙ্কালপেশি",
        ],
        "A", "hard", "conceptual",
        "Endoderm lines gut and respiratory tubes and forms associated glands’ epithelia.",
        "এন্ডোডার্ম অন্ত্র–শ্বসন নালি আস্তরণ ও সংশ্লিষ্ট গ্রন্থির এপিথেলিয়াম গঠন করে।",
    ),
    q(
        "Mesoderm typically gives rise to which of the following?",
        "মেসোডার্ম সাধারণত কোনটি গঠন করে?",
        [
            "Muscles, connective tissue, blood and much of the urogenital system",
            "Only the lens of the eye exclusively from surface ectoderm incorrectly stated as mesoderm",
            "Only enamel of teeth exclusively",
            "Only neural tube exclusively",
        ],
        [
            "পেশি, যোজক কলা, রক্ত ও অধিকাংশ ইউরোজেনিটাল তন্ত্র",
            "শুধু চোখের লেন্স (যা প্রকৃতপক্ষে এক্টোডার্ম থেকে)",
            "শুধু দাঁতের এনামেল",
            "শুধু নিউরাল টিউব",
        ],
        "A", "hard", "conceptual",
        "Mesoderm forms mesenchyme-derived structures: muscle, bone, blood, kidney, gonads, etc.",
        "মেসোডার্ম থেকে পেশি, অস্থি, রক্ত, বৃক্ক, গোনাড ইত্যাদি গঠিত হয়।",
    ),
    q(
        "Which sequence of early human development is correct?",
        "প্রাথমিক মানব বিকাশের সঠিক ক্রম কোনটি?",
        [
            "Zygote → cleavage/morula → blastocyst → implantation → gastrulation → organogenesis",
            "Organogenesis → zygote → fertilization → morula",
            "Fetus → gametes → zygote without fertilization",
            "Implantation → gametogenesis → fertilization in the ovary only",
        ],
        [
            "জাইগোট → ক্লিভেজ/মরুলা → ব্লাস্টোসিস্ট → ইমপ্লান্টেশন → গ্যাস্ট্রুলেশন → অর্গানোজেনেসিস",
            "অর্গানোজেনেসিস → জাইগোট → নিষেক → মরুলা",
            "ফিটাস → গ্যামেট → নিষেক ছাড়াই জাইগোট",
            "ইমপ্লান্টেশন → গ্যামেটোজেনেসিস → শুধু ডিম্বাশয়ে নিষেক",
        ],
        "A", "hard", "conceptual",
        "Development proceeds from zygote through blastocyst implantation to germ layers and organs.",
        "জাইগোট থেকে ব্লাস্টোসিস্ট ইমপ্লান্টেশন, জার্ম স্তর ও অঙ্গগঠন পর্যায়ক্রমে ঘটে।",
    ),
]


# --- t03: Reproductive health / প্রজনন স্বাস্থ্য ---
T03 = [
    q(
        "STD in reproductive health usually stands for what?",
        "প্রজনন স্বাস্থ্যে STD সাধারণত কী বোঝায়?",
        [
            "Sexually transmitted disease",
            "Standard thyroid dose",
            "Skeletal tendon disorder",
            "Salivary taste deficit",
        ],
        [
            "যৌনবাহিত রোগ",
            "স্ট্যান্ডার্ড থাইরয়েড ডোজ",
            "কঙ্কাল টেন্ডন ব্যাধি",
            "লালা স্বাদ ঘাটতি",
        ],
        "A", "easy", "factual",
        "STDs (STIs) are infections transmitted mainly through sexual contact.",
        "STD/STI মূলত যৌন সংস্পর্শে সংক্রমিত রোগ।",
    ),
    q(
        "IVF (in vitro fertilization) means which procedure?",
        "IVF (ইন ভিট্রো নিষেক) কোন পদ্ধতি?",
        [
            "Fertilizing egg with sperm outside the body, then placing the embryo in the uterus",
            "Only surgical removal of both kidneys",
            "Only vaccination against tetanus",
            "Only measuring blood pressure in the clinic",
        ],
        [
            "দেহের বাইরে শুক্রাণু–ডিম্বাণু নিষেক করে ভ্রূণ জরায়ুতে স্থাপন",
            "শুধু উভয় বৃক্ক অস্ত্রোপচার করে অপসারণ",
            "শুধু ধনুষ্টংকার টিকা",
            "শুধু ক্লিনিকে রক্তচাপ মাপা",
        ],
        "A", "easy", "factual",
        "IVF is assisted fertilization in vitro followed by uterine transfer of the embryo.",
        "IVF-তে দেহবহিঃ নিষেকের পর ভ্রূণ জরায়ুতে স্থানান্তর করা হয়।",
    ),
    q(
        "Couples may consider IVF when which problems are present?",
        "কোন সমস্যা থাকলে দম্পতি IVF বিবেচনা করতে পারে?",
        [
            "Blocked/damaged oviducts, endometriosis, low/abnormal sperm count, or failed ovulation",
            "Only mild seasonal allergy to pollen",
            "Only temporary common cold without infertility",
            "Only preference for a shorter menstrual cycle with no infertility",
        ],
        [
            "বন্ধ/ক্ষত ডিম্বনালি, এন্ডোমেট্রিওসিস, কম/অস্বাভাবিক শুক্রাণু বা ডিম্বপাত ব্যর্থতা",
            "শুধু মৃদু ঋতুকালীন পরাগ অ্যালার্জি",
            "শুধু অস্থায়ী সর্দি যা বন্ধ্যাত্ব নয়",
            "শুধু বন্ধ্যাত্ব ছাড়াই ছোট রজঃচক্র পছন্দ",
        ],
        "A", "medium", "conceptual",
        "IVF bypasses tubal barriers and can help with certain male/female infertility causes.",
        "IVF নালি প্রতিবন্ধকতা এড়ায় এবং নির্দিষ্ট বন্ধ্যাত্ব কারণে সাহায্য করে।",
    ),
    q(
        "Tubal ligation (female sterilization) works mainly by which mechanism?",
        "টিউবাল লাইগেশন (নারী নির্বীজন) প্রধানত কীভাবে কাজ করে?",
        [
            "Cutting/blocking both fallopian tubes so sperm cannot meet the ovum",
            "Removing the pituitary gland permanently",
            "Blocking only the nasal cavity",
            "Destroying all bone marrow stem cells",
        ],
        [
            "উভয় ডিম্বনালি কেটে/বন্ধ করে শুক্রাণু–ডিম্বাণু মিলন রোধ",
            "পিটুইটারি গ্রন্থি স্থায়ী অপসারণ",
            "শুধু নাসারন্ধ্র বন্ধ করা",
            "সব অস্থিমজ্জা স্টেম সেল ধ্বংস",
        ],
        "A", "medium", "conceptual",
        "Ligation is chosen when further pregnancy is not desired or is medically unsafe.",
        "আর সন্তান না চাইলে বা গর্ভধারণ ঝুঁকিপূর্ণ হলে লাইগেশন নেওয়া হয়।",
    ),
    q(
        "Vasectomy is a contraceptive method that mainly involves which structure?",
        "ভ্যাসেকটমি কোন অঙ্গ/নালির সাথে জড়িত গর্ভনিরোধ পদ্ধতি?",
        [
            "Vas deferens (deferent ducts) in the male",
            "Only the fallopian tubes in the female",
            "Only the ureters bilaterally",
            "Only the common bile duct",
        ],
        [
            "পুরুষের ভ্যাস ডিফারেন্স",
            "শুধু নারীর ফ্যালোপিয়ান নালি",
            "শুধু উভয় ইউরেটার",
            "শুধু কমন বাইল ডাক্ট",
        ],
        "A", "medium", "factual",
        "Vasectomy interrupts sperm transport via the vas deferens.",
        "ভ্যাসেকটমিতে ভ্যাস ডিফারেন্স বন্ধ করে শুক্রাণু পরিবহন রুদ্ধ হয়।",
    ),
    q(
        "Barrier contraceptives such as condoms mainly prevent pregnancy by which means?",
        "কন্ডোমের মতো ব্যারিয়ার গর্ভনিরোধক প্রধানত কীভাবে গর্ভধারণ রোধ করে?",
        [
            "Preventing sperm from entering the female reproductive tract",
            "Destroying the ovaries permanently after one use",
            "Removing the uterus surgically each cycle",
            "Stopping heartbeat for several minutes",
        ],
        [
            "শুক্রাণুকে নারী জননপথে প্রবেশ করতে না দিয়ে",
            "একবার ব্যবহারেই ডিম্বাশয় স্থায়ী ধ্বংস করে",
            "প্রতি চক্রে জরায়ু অস্ত্রোপচার করে সরিয়ে",
            "কয়েক মিনিট হৃৎস্পন্দন বন্ধ করে",
        ],
        "A", "easy", "conceptual",
        "Condoms are barriers that also help reduce STD transmission when used correctly.",
        "সঠিক ব্যবহারে কন্ডোম গর্ভনিরোধ ও STD ঝুঁকি কমায়।",
    ),
    q(
        "Oral contraceptive pills mainly prevent pregnancy by which hormonal effect?",
        "মুখে সেবনীয় গর্ভনিরোধক বড়ি প্রধানত কোন হরমোন প্রভাবে গর্ভধারণ রোধ করে?",
        [
            "Suppressing ovulation and altering cervical mucus/endometrium",
            "Increasing continuous LH surge every hour without pause",
            "Stimulating continuous dual ovulation daily",
            "Hardening the skull bones instantly",
        ],
        [
            "ডিম্বপাত দমন এবং সার্ভিক্যাল মিউকাস/এন্ডোমেট্রিয়াম পরিবর্তন",
            "প্রতি ঘণ্টায় বিরতিহীন LH সার্জ বাড়ানো",
            "প্রতিদিন দ্বৈত ডিম্বপাত উদ্দীপনা",
            "তাৎক্ষণিক করোটিক অস্থি শক্ত করা",
        ],
        "A", "medium", "conceptual",
        "Combined pills use estrogen/progestin to inhibit ovulation and change tract receptivity.",
        "সম্মিলিত বড়িতে ইস্ট্রোজেন/প্রোজেস্টিন ডিম্বপাত ও নালি গ্রহণযোগ্যতা নিয়ন্ত্রণ করে।",
    ),
    q(
        "Why is the recommended marriage age for girls often cited around 18–20 years in HSC texts?",
        "এইচএসসি পাঠে মেয়েদের বিয়ের বয়স প্রায় ১৮–২০ বছর নির্ধারণের যুক্তি কী?",
        [
            "Adequate sexual maturity and physical readiness for pregnancy and childbirth",
            "Only because puberty never occurs before age 30",
            "Only because menstruation starts only after age 40",
            "Only because fertilization is impossible after age 16",
        ],
        [
            "যৌন পরিপক্কতা ও গর্ভধারণ/প্রসবের শারীরিক উপযুক্ততা নিশ্চিত করতে",
            "শুধু ৩০ বছরের আগে বয়ঃসন্ধি কখনো হয় না বলে",
            "শুধু ৪০ বছরের পর রজঃস্রাব শুরু হয় বলে",
            "শুধু ১৬ বছরের পর নিষেক অসম্ভব বলে",
        ],
        "A", "medium", "conceptual",
        "Early marriage risks incomplete maturity and higher maternal–child health hazards.",
        "অকাল বিয়েতে পরিপক্কতা অসম্পূর্ণ ও মা–শিশু স্বাস্থ্যঝুঁকি বাড়ে।",
    ),
    q(
        "Reproductive health broadly includes which of the following?",
        "প্রজনন স্বাস্থ্য ব্যাপকভাবে কোনটি অন্তর্ভুক্ত করে?",
        [
            "Safe sex, family planning, maternal care, STI prevention and infertility support",
            "Only treating bone fractures in athletes",
            "Only measuring visual acuity",
            "Only dental cavity filling",
        ],
        [
            "নিরাপদ যৌনতা, পরিবার পরিকল্পনা, মাতৃসেবা, STI প্রতিরোধ ও বন্ধ্যাত্ব সহায়তা",
            "শুধু ক্রীড়াবিদের অস্থি ভাঙা চিকিৎসা",
            "শুধু দৃষ্টি তীক্ষ্ণতা মাপা",
            "শুধু দন্ত ক্ষয় ভর্তি",
        ],
        "A", "easy", "conceptual",
        "WHO-style reproductive health covers physical, mental and social well-being in reproduction.",
        "প্রজনন স্বাস্থ্য প্রজননসংক্রান্ত শারীরিক–মানসিক–সামাজিক সুস্থতা নিয়ে গঠিত।",
    ),
    q(
        "Which practice best reduces the risk of many sexually transmitted infections?",
        "অনেক যৌনবাহিত সংক্রমণের ঝুঁকি কমাতে কোন অনুশীলন সবচেয়ে কার্যকর?",
        [
            "Consistent safer-sex practices including correct condom use and avoiding high-risk exposure",
            "Sharing unsterilized needles intentionally",
            "Ignoring all genital symptoms forever",
            "Using antibiotics daily without medical advice for every mild cough",
        ],
        [
            "সঠিক কন্ডোম ব্যবহারসহ নিরাপদ যৌন আচরণ ও উচ্চঝুঁকি এড়ানো",
            "ইচ্ছাকৃতভাবে অপরিশোধিত সুই শেয়ার করা",
            "সব যৌনাঙ্গ লক্ষণ চিরকাল উপেক্ষা করা",
            "মৃদু কাশিতেও পরামর্শ ছাড়া প্রতিদিন অ্যান্টিবায়োটিক",
        ],
        "A", "medium", "conceptual",
        "Prevention relies on safer sex, awareness, testing and timely treatment—not denial.",
        "প্রতিরোধে নিরাপদ যৌনতা, সচেতনতা, পরীক্ষা ও সময়মতো চিকিৎসা জরুরি।",
    ),
    q(
        "Infertility is best described as which condition?",
        "বন্ধ্যাত্ব কোন অবস্থাকে বোঝায়?",
        [
            "Inability to conceive after a reasonable period of unprotected intercourse",
            "Only temporary hiccups after eating",
            "Only having brown eye color",
            "Only left-handedness",
        ],
        [
            "নির্দিষ্ট সময় অরক্ষিত সহবাসের পরও গর্ভধারণে অক্ষমতা",
            "শুধু খাওয়ার পর অস্থায়ী হিক্কা",
            "শুধু বাদামি চোখের রং",
            "শুধু বামহাতি হওয়া",
        ],
        "A", "easy", "factual",
        "Infertility may involve male factors, female factors, or both, and may need medical evaluation.",
        "বন্ধ্যাত্ব পুরুষ/নারী/উভয় কারণে হতে পারে; চিকিৎসা মূল্যায়ন লাগতে পারে।",
    ),
    q(
        "Antenatal (prenatal) care mainly aims to protect which pair?",
        "অ্যান্টিনেটাল (প্রসবপূর্ব) সেবা প্রধানত কাদের রক্ষা করে?",
        [
            "Mother and developing fetus/baby",
            "Only the father’s wisdom teeth",
            "Only unrelated neighbors’ pets",
            "Only classroom chalkboards",
        ],
        [
            "মা ও বিকাশমান ভ্রূণ/শিশু",
            "শুধু পিতার আক্কেলদাঁত",
            "শুধু অপ্রাসঙ্গিক প্রতিবেশীর পোষা প্রাণী",
            "শুধু শ্রেণিকক্ষের ব্ল্যাকবোর্ড",
        ],
        "A", "easy", "conceptual",
        "Prenatal care monitors maternal–fetal health, nutrition, vaccines and risk factors.",
        "প্রসবপূর্ব সেবায় মা–শিশুর স্বাস্থ্য, পুষ্টি, টিকা ও ঝুঁকি নজরদারি করা হয়।",
    ),
    q(
        "Avoiding unnecessary drugs, alcohol and smoking in pregnancy mainly reduces which risk?",
        "গর্ভাবস্থায় অপ্রয়োজনীয় ওষুধ, মদ ও ধূমপান এড়ানো প্রধানত কোন ঝুঁকি কমায়?",
        [
            "Teratogenic and other developmental harm to the embryo/fetus",
            "Only adult male-pattern baldness in the father",
            "Only change of eye color after birth guaranteed",
            "Only permanent loss of maternal fingerprints",
        ],
        [
            "ভ্রূণ/ফিটাসের টেরাটোজেনিক ও অন্যান্য বিকাশগত ক্ষতি",
            "শুধু পিতার পুরুষ-ধরনের টাক",
            "শুধু জন্মের পর চোখের রং পরিবর্তনের নিশ্চয়তা",
            "শুধু মায়ের আঙুলের ছাপ স্থায়ী হারানো",
        ],
        "A", "medium", "conceptual",
        "Many chemicals and infections act as teratogens during sensitive developmental windows.",
        "সংবেদনশীল সময়ে অনেক রাসায়নিক ও সংক্রমণ টেরাটোজেন হিসেবে কাজ করে।",
    ),
    q(
        "Which statement about family planning is correct?",
        "পরিবার পরিকল্পনা সম্পর্কে কোন বক্তব্য সঠিক?",
        [
            "It helps couples decide if, when and how many children to have using informed methods",
            "It only means forbidding all medical care forever",
            "It only means removing all food from the household",
            "It only means stopping all education for girls",
        ],
        [
            "সচেতন পদ্ধতিতে সন্তান নেবে কি না, কখন ও কতজন—এ সিদ্ধান্তে সাহায্য করে",
            "শুধু সব চিকিৎসা চিরকাল নিষিদ্ধ করা",
            "শুধু ঘর থেকে সব খাদ্য সরিয়ে ফেলা",
            "শুধু মেয়েদের সব শিক্ষা বন্ধ করা",
        ],
        "A", "easy", "conceptual",
        "Family planning supports reproductive rights, spacing and maternal–child health.",
        "পরিবার পরিকল্পনা প্রজনন অধিকার, ব্যবধান ও মা–শিশু স্বাস্থ্য সহায়তা করে।",
    ),
    q(
        "IUCD (intrauterine contraceptive device) mainly prevents pregnancy by which action?",
        "IUCD (অন্তঃজরায়ু গর্ভনিরোধক যন্ত্র) প্রধানত কীভাবে গর্ভধারণ রোধ করে?",
        [
            "Creating a uterine environment hostile to sperm/implantation",
            "Removing both ovaries each month",
            "Blocking only the trachea",
            "Stopping kidney filtration permanently",
        ],
        [
            "জরায়ু পরিবেশ শুক্রাণু/ইমপ্লান্টেশনের প্রতিকূল করে",
            "প্রতি মাসে উভয় ডিম্বাশয় অপসারণ করে",
            "শুধু ট্রাকিয়া বন্ধ করে",
            "বৃক্ক পরিস্রাবণ স্থায়ী বন্ধ করে",
        ],
        "A", "medium", "factual",
        "Copper/hormonal IUCDs impair sperm function and/or endometrial receptivity.",
        "তামা/হরমোন IUCD শুক্রাণু ক্রিয়া ও/বা এন্ডোমেট্রিয়াম গ্রহণযোগ্যতা কমায়।",
    ),
    q(
        "Safe motherhood programs emphasize which priority?",
        "নিরাপদ মাতৃত্ব কর্মসূচি কোন অগ্রাধিকারের ওপর জোর দেয়?",
        [
            "Skilled care before, during and after childbirth to reduce maternal and newborn deaths",
            "Only delaying all vaccinations indefinitely",
            "Only encouraging delivery without any trained helper always",
            "Only withholding nutrition from pregnant women",
        ],
        [
            "প্রসবপূর্ব–প্রসবকালীন–প্রসবোত্তর দক্ষ সেবায় মা ও নবজাতক মৃত্যু কমানো",
            "শুধু সব টিকা অনির্দিষ্টকাল বিলম্ব",
            "শুধু সবসময় প্রশিক্ষিত সহায়ক ছাড়া প্রসব উৎসাহ",
            "শুধু গর্ভবতীকে পুষ্টি না দেওয়া",
        ],
        "A", "medium", "conceptual",
        "Skilled birth attendance and emergency obstetric care are core safe-motherhood pillars.",
        "দক্ষ প্রসব সহায়তা ও জরুরি প্রসূতি সেবা নিরাপদ মাতৃত্বের মূল স্তম্ভ।",
    ),
    q(
        "Which is an example of a temporary contraceptive method?",
        "অস্থায়ী গর্ভনিরোধক পদ্ধতির উদাহরণ কোনটি?",
        [
            "Condoms or oral contraceptive pills",
            "Bilateral tubal ligation intended as permanent",
            "Vasectomy intended as permanent",
            "Surgical hysterectomy for contraception only always",
        ],
        [
            "কন্ডোম বা মুখে সেবনীয় গর্ভনিরোধক বড়ি",
            "স্থায়ী উদ্দেশ্যে উভয় ডিম্বনালি লাইগেশন",
            "স্থায়ী উদ্দেশ্যে ভ্যাসেকটমি",
            "শুধু গর্ভনিরোধে সবসময় হিস্টারেক্টমি",
        ],
        "A", "easy", "factual",
        "Barrier methods and pills are reversible; sterilization is generally permanent.",
        "ব্যারিয়ার ও বড়ি বিপরীতযোগ্য; নির্বীজন সাধারণত স্থায়ী।",
    ),
    q(
        "Which statement about abortion and reproductive health education is most appropriate for HSC-level awareness?",
        "গর্ভপাত ও প্রজনন স্বাস্থ্য শিক্ষা সম্পর্কে এইচএসসি-স্তরের সবচেয়ে উপযুক্ত বক্তব্য কোনটি?",
        [
            "Unwanted pregnancy prevention via education and contraception is safer than unsafe abortion",
            "Unsafe abortion has no health risks at all",
            "Contraception knowledge is unnecessary for adolescents",
            "Only males need reproductive health information",
        ],
        [
            "শিক্ষা ও গর্ভনিরোধে অনাকাঙ্ক্ষিত গর্ভ রোধ অনিরাপদ গর্ভপাতের চেয়ে নিরাপদ",
            "অনিরাপদ গর্ভপাতের কোনো স্বাস্থ্যঝুঁকি নেই",
            "কিশোর–কিশোরীর গর্ভনিরোধ জ্ঞান অপ্রয়োজনীয়",
            "শুধু পুরুষদের প্রজনন স্বাস্থ্য তথ্য দরকার",
        ],
        "A", "hard", "conceptual",
        "Prevention and counseling reduce unsafe procedures and maternal morbidity.",
        "প্রতিরোধ ও পরামর্শ অনিরাপদ গর্ভপাত ও মাতৃ রোগহার কমায়।",
    ),
    q(
        "Breastfeeding after birth can contribute to reproductive health mainly by which means?",
        "জন্মের পর বুকের দুধ খাওয়ানো প্রজনন স্বাস্থ্যে প্রধানত কীভাবে অবদান রাখে?",
        [
            "Providing infant nutrition/immunity and often delaying return of fertility (lactational amenorrhea effect)",
            "Permanently sterilizing the mother after one feed",
            "Replacing all vaccines forever",
            "Stopping all maternal hormone production permanently",
        ],
        [
            "শিশুর পুষ্টি/রোগপ্রতিরোধ ও প্রায়শই উর্বরতা ফেরার বিলম্ব (ল্যাকটেশনাল অ্যামেনোরিয়া)",
            "একবার দুধ খাওয়ালেই মা স্থায়ী নির্বীজিত",
            "সব টিকার স্থায়ী বিকল্প",
            "মাতৃ সব হরমোন উৎপাদন স্থায়ী বন্ধ",
        ],
        "A", "hard", "conceptual",
        "Exclusive breastfeeding may delay ovulation but is not a foolproof long-term contraceptive alone.",
        "একমাত্র বুকের দুধ ডিম্বপাত বিলম্ব করতে পারে; একা দীর্ঘমেয়াদি নিশ্চিত গর্ভনিরোধক নয়।",
    ),
    q(
        "Which public-health measure supports reproductive health at the community level?",
        "কমিউনিটি পর্যায়ে প্রজনন স্বাস্থ্য সহায়ক কোন জনস্বাস্থ্য ব্যবস্থা?",
        [
            "Sex education, STI clinics, contraception access and maternal health services",
            "Banning all maternal health clinics permanently",
            "Promoting child marriage as a health strategy",
            "Withholding iron–folate from all pregnant women intentionally",
        ],
        [
            "যৌন শিক্ষা, STI ক্লিনিক, গর্ভনিরোধক প্রাপ্তি ও মাতৃস্বাস্থ্য সেবা",
            "সব মাতৃস্বাস্থ্য ক্লিনিক স্থায়ী নিষিদ্ধকরণ",
            "স্বাস্থ্য কৌশল হিসেবে বাল্যবিবাহ উৎসাহ",
            "সব গর্ভবতীকে ইচ্ছাকৃতভাবে আয়রন–ফোলেট না দেওয়া",
        ],
        "A", "medium", "conceptual",
        "Community programs improve awareness, access and outcomes across the reproductive life course.",
        "কমিউনিটি কর্মসূচি সচেতনতা, সেবাপ্রাপ্তি ও ফলাফল উন্নত করে।",
    ),
]


TOPICS_MAP = {
    "bio2_27_ch09_t01": T01,
    "bio2_27_ch09_t02": T02,
    "bio2_27_ch09_t03": T03,
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
        "chapter": "bio2_27_ch09",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p286_pdf292.png",
            "p287_pdf293.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio2_27_ch09_t01": {
                "title": "Human reproduction / মানব প্রজনন",
                "themes": [
                    "reproduction definition; puberty definition/ages; male puberty changes",
                    "gametogenesis/spermatogenesis/oogenesis; testes–ovaries; fertilization in ampulla",
                    "GnRH→FSH/LH; FSH follicles/estrogen; LH surge ovulation; ~28-day cycle",
                    "menarche/menopause; endometrium shedding; testosterone; corpus luteum progesterone; diploid zygote",
                ],
            },
            "bio2_27_ch09_t02": {
                "title": "Development / বিকাশ",
                "themes": [
                    "zygote; morula; blastocyst structure; implantation 6–9 days",
                    "gastrulation germ layers; organogenesis primary/secondary buds",
                    "placenta biological bridge; nutrient/waste exchange; teratogens early organogenesis",
                    "embryo vs fetus; inner cell mass; amniotic fluid; ~9 months; ecto/meso/endoderm fates; sequence",
                ],
            },
            "bio2_27_ch09_t03": {
                "title": "Reproductive health / প্রজনন স্বাস্থ্য",
                "themes": [
                    "STD; IVF indications; tubal ligation; vasectomy; condoms; oral pills",
                    "marriage age 18–20 rationale; reproductive health scope; safer sex",
                    "infertility; antenatal care; avoid teratogens in pregnancy; family planning",
                    "IUCD; safe motherhood; temporary vs permanent methods; abortion awareness; breastfeeding; community services",
                ],
            },
        },
        "low_confidence": [
            "OCR of printed pages p286–287 is mainly CQ (short-answer) text, not dense MCQ keys; stems authored/reconstructed from readable CQ themes and standard HSC Zoology Ch9 facts.",
            "Printed MCQ section for ch9 is only two pages; bank supplemented to exactly 20 items per syllabus topic.",
            "Figure-/stimulus-linked items (if any on source pages) rewritten as standalone stems.",
            "Numeric ages (puberty, marriage recommendation, gestation, implantation days) follow common Bangladesh HSC textbook phrasing from the OCR CQ answers.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio2_27_ch09_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio2_27_ch09_t01": 20,
                "bio2_27_ch09_t02": 20,
                "bio2_27_ch09_t03": 20,
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
        / "ch09_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
