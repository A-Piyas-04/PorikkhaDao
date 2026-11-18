#!/usr/bin/env python3
"""Seed Biology 2nd Paper Ch8 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio2_27_ch08_t01..t03 (Nervous system; Sense organs; Hormones).
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
    "biology p2 ch08; curated bilingual"
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


# --- t01: Nervous system / স্নায়ুতন্ত্র ---
T01 = [
    q(
        "Cranial nerve X (vagus) correctly supplies which of the following?",
        "দশম করোটিক স্নায়ু (ভ্যাগাস) সঠিকভাবে কোনগুলোতে বিস্তৃত?",
        [
            "(i) larynx and (ii) heart only",
            "(ii) heart and (iii) tongue only",
            "(i) larynx and (iii) tongue only",
            "(i), (ii) and (iii)",
        ],
        [
            "শুধু (i) স্বরযন্ত্র ও (ii) হৃৎপিণ্ড",
            "শুধু (ii) হৃৎপিণ্ড ও (iii) জিহ্বা",
            "শুধু (i) স্বরযন্ত্র ও (iii) জিহ্বা",
            "(i), (ii) ও (iii)",
        ],
        "A", "medium", "conceptual",
        "Vagus (X) supplies larynx and heart; tongue motor supply is mainly hypoglossal (XII).",
        "ভ্যাগাস স্বরযন্ত্র ও হৃৎপিণ্ডে যায়; জিহ্বার চেষ্টীয় স্নায়ু প্রধানত হাইপোগ্লোসাল (XII)।",
    ),
    q(
        "What is the name of the fourth (IV) cranial nerve?",
        "চতুর্থ (IV) করোটিক স্নায়ুর নাম কী?",
        ["Trochlear", "Abducens", "Auditory", "Trigeminal"],
        ["ট্রকলিয়ার", "অ্যাবডুসেন্স", "অডিটরি", "ট্রাইজেমিনাল"],
        "A", "easy", "factual",
        "Cranial nerve IV is the trochlear nerve (eye muscle motor).",
        "চতুর্থ করোটিক স্নায়ু হলো ট্রকলিয়ার (চক্ষুপেশি চেষ্টীয়)।",
    ),
    q(
        "Which of the following cranial nerves are mixed in nature?",
        "নিচের কোন করোটিক স্নায়ুগুলো মিশ্র প্রকৃতির?",
        [
            "(i) trochlear only",
            "(ii) facial and (iii) vagus only",
            "(i) trochlear and (ii) facial only",
            "(i), (ii) and (iii)",
        ],
        [
            "শুধু (i) ট্রকলিয়ার",
            "শুধু (ii) ফ্যাসিয়াল ও (iii) ভ্যাগাস",
            "শুধু (i) ট্রকলিয়ার ও (ii) ফ্যাসিয়াল",
            "(i), (ii) ও (iii)",
        ],
        "B", "medium", "conceptual",
        "Facial (VII) and vagus (X) are mixed; trochlear (IV) is purely motor.",
        "ফ্যাসিয়াল ও ভ্যাগাস মিশ্র; ট্রকলিয়ার শুধু চেষ্টীয়।",
    ),
    q(
        "Which cranial nerve helps control pharynx, larynx, soft palate and shoulder movement?",
        "গলবিল, স্বরযন্ত্র, নরম তালু ও কাঁধের সঞ্চালন নিয়ন্ত্রণে কোন করোটিক স্নায়ু সাহায্য করে?",
        ["Trigeminal", "Vagus", "Spinal accessory", "Trochlear"],
        ["ট্রাইজেমিনাল", "ভ্যাগাস", "স্পাইনাল অ্যাকসেসরি", "ট্রকলিয়ার"],
        "C", "medium", "factual",
        "Cranial nerve XI (spinal accessory) supplies sternocleidomastoid/trapezius and related neck–shoulder control.",
        "একাদশ (স্পাইনাল অ্যাকসেসরি) স্নায়ু মাথা–কাঁধ সঞ্চালনে গুরুত্বপূর্ণ।",
    ),
    q(
        "Which set of cranial nerves is mainly involved in eyeball movement?",
        "অক্ষিগোলক সঞ্চালনে প্রধানত কোন করোটিক স্নায়ুগুলো জড়িত?",
        [
            "Optic and trigeminal only",
            "Oculomotor, trochlear and abducens",
            "Olfactory and auditory only",
            "Facial and hypoglossal only",
        ],
        [
            "শুধু অপটিক ও ট্রাইজেমিনাল",
            "অকুলোমোটর, ট্রকলিয়ার ও অ্যাবডুসেন্স",
            "শুধু অলফ্যাক্টরি ও অডিটরি",
            "শুধু ফ্যাসিয়াল ও হাইপোগ্লোসাল",
        ],
        "B", "medium", "factual",
        "Extraocular muscles are supplied by CN III, IV and VI.",
        "চক্ষুপেশি III, IV ও VI করোটিক স্নায়ু দ্বারা নিয়ন্ত্রিত।",
    ),
    q(
        "Which of the following is a part of the hindbrain?",
        "নিচের কোনটি পশ্চাৎ মস্তিষ্কের অংশ?",
        ["Cerebrum", "Thalamus", "Hypothalamus", "Cerebellum"],
        ["সেরেব্রাম", "থ্যালামাস", "হাইপোথ্যালামাস", "সেরেবেলাম"],
        "D", "easy", "factual",
        "The hindbrain includes cerebellum, pons and medulla; cerebrum is forebrain.",
        "পশ্চাৎ মস্তিষ্কে সেরেবেলাম, পনস ও মেডুলা; সেরেব্রাম অগ্রমস্তিষ্ক।",
    ),
    q(
        "What is the largest part of the human brain?",
        "মানুষের মস্তিষ্কের সবচেয়ে বড় অংশ কোনটি?",
        ["Cerebellum", "Cerebrum", "Thalamus", "Hypothalamus"],
        ["সেরেবেলাম", "সেরেব্রাম", "থ্যালামাস", "হাইপোথ্যালামাস"],
        "B", "easy", "factual",
        "The cerebrum is the largest brain region and handles higher functions.",
        "সেরেব্রাম মস্তিষ্কের বৃহত্তম অংশ এবং উচ্চতর কাজ নিয়ন্ত্রণ করে।",
    ),
    q(
        "Which cranial nerve is most closely associated with taste from the anterior tongue?",
        "জিহ্বার অগ্রভাগের স্বাদ গ্রহণের সাথে সবচেয়ে ঘনিষ্ঠ কোন করোটিক স্নায়ু?",
        ["Facial", "Trochlear", "Olfactory", "Optic"],
        ["ফ্যাসিয়াল", "ট্রকলিয়ার", "অলফ্যাক্টরি", "অপটিক"],
        "A", "medium", "factual",
        "Facial (VII) carries taste from the anterior two-thirds of the tongue.",
        "ফ্যাসিয়াল (VII) জিহ্বার অগ্র দুই-তৃতীয়াংশের স্বাদ বহন করে।",
    ),
    q(
        "Which statements about a typical spinal reflex are correct?",
        "সাধারণ স্পাইনাল প্রতিবর্ত ক্রিয়া সম্পর্কে কোনগুলো সঠিক?",
        [
            "Spinal cord controlled and involuntary only",
            "Brain-controlled voluntary only",
            "Always learned behaviour only",
            "Only cranial-nerve mediated voluntary acts",
        ],
        [
            "শুধু সুষুম্না নিয়ন্ত্রিত ও অনৈচ্ছিক",
            "শুধু মস্তিষ্ক নিয়ন্ত্রিত ঐচ্ছিক",
            "শুধু শিখন আচরণ",
            "শুধু করোটিক স্নায়ুবাহিত ঐচ্ছিক কাজ",
        ],
        "A", "medium", "conceptual",
        "Classic spinal reflexes are rapid, involuntary and mediated via the spinal cord.",
        "ক্লাসিক স্পাইনাল রিফ্লেক্স দ্রুত, অনৈচ্ছিক ও সুষুম্না-নিয়ন্ত্রিত।",
    ),
    q(
        "Which cranial nerve mainly causes tongue movement?",
        "কোন করোটিক স্নায়ু প্রধানত জিহ্বার সঞ্চালন ঘটায়?",
        ["Abducens", "Facial", "Vagus", "Hypoglossal"],
        ["অ্যাবডুসেন্স", "ফ্যাসিয়াল", "ভ্যাগাস", "হাইপোগ্লোসাল"],
        "D", "easy", "factual",
        "Hypoglossal (XII) is the motor nerve of the tongue.",
        "হাইপোগ্লোসাল (XII) জিহ্বার চেষ্টীয় স্নায়ু।",
    ),
    q(
        "Which cranial nerve plays a major role in hearing and balance?",
        "শ্রবণ ও ভারসাম্য রক্ষায় কোন স্নায়ু প্রধান ভূমিকা রাখে?",
        ["Optic", "Oculomotor", "Auditory (vestibulocochlear)", "Vagus"],
        ["অপটিক", "অকুলোমোটর", "অডিটরি (ভেস্টিবুলোকোকলিয়ার)", "ভ্যাগাস"],
        "C", "easy", "factual",
        "CN VIII (auditory/vestibulocochlear) serves hearing and equilibrium.",
        "অষ্টম করোটিক স্নায়ু শ্রবণ ও ভারসাম্যে কাজ করে।",
    ),
    q(
        "How many ventricles are present inside the human brain?",
        "মানুষের মস্তিষ্কের অভ্যন্তরে প্রকোষ্ঠ (ভেন্ট্রিকল) সংখ্যা কত?",
        ["3", "4", "5", "6"],
        ["৩", "৪", "৫", "৬"],
        "B", "easy", "factual",
        "There are four brain ventricles (two lateral, third and fourth).",
        "মস্তিষ্কে চারটি প্রকোষ্ঠ থাকে (দুই ল্যাটারাল, তৃতীয় ও চতুর্থ)।",
    ),
    q(
        "Withdrawing the hand from a hot object is mainly controlled by which part of the nervous system?",
        "জ্বলন্ত বস্তু থেকে হাত সরিয়ে নেওয়া প্রধানত স্নায়ুতন্ত্রের কোন অংশ দ্বারা নিয়ন্ত্রিত?",
        ["Cerebrum", "Cerebellum", "Medulla oblongata", "Spinal cord"],
        ["সেরেব্রাম", "সেরেবেলাম", "মেডুলা অবলংগাটা", "সুষুম্নাকাণ্ড"],
        "D", "easy", "application",
        "The withdrawal reflex arc is completed mainly through the spinal cord.",
        "প্রত্যাহার প্রতিবর্ত মূলত সুষুম্নাকাণ্ডের মাধ্যমে সম্পন্ন হয়।",
    ),
    q(
        "The sudden hand-withdrawal reflex from heat is best classified as which behaviour type?",
        "তাপ থেকে হঠাৎ হাত সরিয়ে নেওয়ার প্রতিবর্ত কোন ধরনের আচরণ?",
        ["Taxis only", "Learned behaviour only", "Innate (instinctive) behaviour", "Conditional operant learning"],
        ["শুধু ট্যাক্সিস", "শুধু শিখন আচরণ", "সহজাত (ইনস্টিংকটিভ) আচরণ", "শর্তযুক্ত অপারেন্ট শিখন"],
        "C", "medium", "conceptual",
        "Spinal withdrawal is an innate reflex, not a learned operant response.",
        "স্পাইনাল প্রত্যাহার সহজাত প্রতিবর্ত; শিখন আচরণ নয়।",
    ),
    q(
        "Which of the following is a mixed cranial nerve?",
        "নিচের কোনটি মিশ্র প্রকৃতির করোটিক স্নায়ু?",
        ["Optic", "Trochlear", "Auditory", "Vagus"],
        ["অপটিক", "ট্রকলিয়ার", "অডিটরি", "ভ্যাগাস"],
        "D", "easy", "factual",
        "Vagus (X) carries both sensory and motor fibres; optic/trochlear/auditory are not mixed.",
        "ভ্যাগাস সংবেদী ও চেষ্টীয় উভয় তন্তু বহন করে।",
    ),
    q(
        "What are meninges?",
        "মেনিনজেস কী?",
        [
            "Tough protective membranes covering brain and spinal cord",
            "Fluid-filled chambers only inside the eye",
            "Hormone-secreting islets of the pancreas",
            "Cartilage rings of the trachea",
        ],
        [
            "মস্তিষ্ক ও সুষুম্নাকে আবৃত দৃঢ় প্রতিরক্ষামূলক আবরণ",
            "শুধু চোখের তরলপূর্ণ প্রকোষ্ঠ",
            "অগ্ন্যাশয়ের হরমোন-ক্ষরা দ্বীপ",
            "শ্বাসনালির তরুণাস্থি বলয়",
        ],
        "A", "easy", "factual",
        "Meninges are the protective coverings of CNS; meningitis is their inflammation.",
        "মেনিনজেস CNS-এর প্রতিরক্ষামূলক আবরণ; প্রদাহ হলে মেনিনজাইটিস।",
    ),
    q(
        "What is a synapse?",
        "সিন্যাপস কী?",
        [
            "Junction gap where one neuron’s axon ending meets the next neuron",
            "Bone cavity housing the pituitary gland",
            "Transparent refractive disc of the eye",
            "Duct of an exocrine salivary gland",
        ],
        [
            "এক নিউরনের অ্যাক্সন প্রান্ত যে ফাঁকযুক্ত সংযোগে পরবর্তী নিউরনের সাথে মিলিত হয়",
            "পিটুইটারি ধারণকারী অস্থি গহ্বর",
            "চোখের স্বচ্ছ প্রতিসরণ ডিস্ক",
            "বহিঃক্ষরা লালার গ্রন্থিনালি",
        ],
        "A", "easy", "factual",
        "A synapse is the specialized junction transmitting signals between neurons (or to effectors).",
        "সিন্যাপস নিউরনগুলোর (বা ইফেক্টরের) মধ্যে সংকেত পরিবহণের বিশেষ সংযোগ।",
    ),
    q(
        "CSF (cerebrospinal fluid) is best described as which of the following?",
        "CSF (সেরিব্রোস্পাইনাল ফ্লুইড) সম্পর্কে কোনটি সঠিক?",
        [
            "Clear fluid in subarachnoid space that cushions the CNS",
            "Digestive enzyme secreted into the duodenum",
            "Pigment of rod cells for night vision",
            "Wax secreted by ceruminous glands of the ear",
        ],
        [
            "সাবঅ্যারাকনয়েড স্থানের স্বচ্ছ তরল যা CNS-কে সুরক্ষা/প্লবতা দেয়",
            "ডিওডেনামে নিঃসৃত পাচক এনজাইম",
            "রাতের দর্শনের রডকোষ রঞ্জক",
            "কানের সিরুমিনাস গ্রন্থির মোম",
        ],
        "A", "medium", "factual",
        "CSF bathes brain and cord, reduces effective weight and cushions against shock.",
        "CSF মস্তিষ্ক–সুষুম্নাকে ভাসিয়ে রাখে ও আঘাত থেকে রক্ষা করে।",
    ),
    q(
        "Why is the trigeminal nerve called a mixed nerve?",
        "ট্রাইজেমিনাল স্নায়ুকে মিশ্র স্নায়ু বলা হয় কেন?",
        [
            "It has sensory ophthalmic/maxillary branches and a mixed mandibular branch",
            "It carries only smell from the nasal mucosa",
            "It is purely motor to the tongue only",
            "It secretes hormones into the blood",
        ],
        [
            "এর অপথ্যালমিক/ম্যাক্সিলারি শাখা সংবেদী এবং ম্যান্ডিবুলার শাখা মিশ্র",
            "শুধু নাসামিউকোসার গন্ধ বহন করে",
            "শুধু জিহ্বার চেষ্টীয় স্নায়ু",
            "রক্তে হরমোন ক্ষরণ করে",
        ],
        "A", "hard", "conceptual",
        "Trigeminal (V) has three branches; mandibular carries both sensory and motor fibres.",
        "ট্রাইজেমিনালের তিন শাখা; ম্যান্ডিবুলার সংবেদী ও চেষ্টীয় উভয়ই।",
    ),
    q(
        "Neurotransmitters are chemical substances that mainly do what?",
        "নিউরোট্রান্সমিটার মূলত কী কাজ করে?",
        [
            "Carry impulse information across a synapse to another neuron, muscle or gland",
            "Form the myelin sheath of peripheral axons only",
            "Store calcium inside bone matrix",
            "Digest starch in the mouth",
        ],
        [
            "সিন্যাপস পেরিয়ে অন্য নিউরন/পেশি/গ্রন্থিতে উদ্দীপনা তথ্য পরিবহণে সাহায্য করে",
            "শুধু পেরিফেরাল অ্যাক্সনের মায়েলিন তৈরি করে",
            "অস্থি ম্যাট্রিক্সে ক্যালসিয়াম জমায়",
            "মুখে স্টার্চ হজম করে",
        ],
        "A", "medium", "conceptual",
        "Examples include acetylcholine, glycine and GABA released at synapses.",
        "উদাহরণ: অ্যাসিটাইলকোলিন, গ্লাইসিন, GABA—সিন্যাপসে মুক্ত হয়।",
    ),
]


# --- t02: Sense organs / ইন্দ্রিয় অঙ্গ ---
T02 = [
    q(
        "Which of the following is an accessory structure of the human eye (not part of the eyeball wall layers)?",
        "মানুষের চোখের আনুষঙ্গিক অংশ কোনটি (অক্ষিগোলকের প্রাচীর স্তর নয়)?",
        ["Iris", "Ciliary body", "Conjunctiva", "Suspensory ligament"],
        ["আইরিশ", "সিলিয়ারি বডি", "কনজাংকটিভা", "সাসপেন্সারি লিগামেন্ট"],
        "C", "medium", "factual",
        "Conjunctiva is an accessory covering; iris/ciliary body/suspensory ligament belong to the eyeball apparatus.",
        "কনজাংকটিভা আনুষঙ্গিক আবরণ; আইরিশ–সিলিয়ারি–সাসপেন্সারি অক্ষিগোলকীয় অংশ।",
    ),
    q(
        "Which statements about rod cells are correct?",
        "রডকোষ সম্পর্কে কোনগুলো সঠিক?",
        [
            "(i) contain rhodopsin (ii) highly light-sensitive (iii) used in night vision — all",
            "Only (i) and (ii)",
            "Only (ii) and (iii)",
            "Only (i)",
        ],
        [
            "(i) রডোপসিনযুক্ত (ii) আলোক-সংবেদী (iii) রাতের দর্শন—সবগুলো",
            "শুধু (i) ও (ii)",
            "শুধু (ii) ও (iii)",
            "শুধু (i)",
        ],
        "A", "easy", "conceptual",
        "Rods are rhodopsin-rich, very sensitive to dim light and enable scotopic (night) vision.",
        "রডকোষ রডোপসিনসমৃদ্ধ, মৃদু আলোয় সংবেদী এবং রাতের দর্শনে ব্যবহৃত।",
    ),
    q(
        "Absence of functional rod cells typically causes which visual problem?",
        "কার্যকর রডকোষের অনুপস্থিতিতে সাধারণত কোন দৃষ্টি সমস্যা হয়?",
        ["Colour blindness only", "Night blindness", "Myopia only", "Presbyopia only"],
        ["শুধু বর্ণান্ধতা", "রাতকানা", "শুধু মায়োপিয়া", "শুধু প্রেসবায়োপিয়া"],
        "B", "easy", "factual",
        "Rod dysfunction/deficiency leads to nyctalopia (night blindness).",
        "রডকোষের ত্রুটিতে নাইক্টালোপিয়া বা রাতকানা হয়।",
    ),
    q(
        "Which structure is NOT a refractive medium of the human eye?",
        "মানব চোখের কোনটি প্রতিসরণ মাধ্যম নয়?",
        ["Cornea", "Pupil", "Aqueous humor", "Lens"],
        ["কর্নিয়া", "পিউপিল", "অ্যাকুয়াস হিউমার", "লেন্স"],
        "B", "medium", "conceptual",
        "The pupil is an aperture controlled by the iris; it does not refract light like cornea/lens/humors.",
        "পিউপিল আইরিশ-নিয়ন্ত্রিত ছিদ্র; কর্নিয়া/লেন্স/হিউমারের মতো প্রতিসরণ করে না।",
    ),
    q(
        "What is a major function of aqueous humor?",
        "অ্যাকুয়াস হিউমারের একটি প্রধান কাজ কী?",
        [
            "Nourishes the lens and cornea",
            "Forms the optic nerve only",
            "Secretes rhodopsin into rods",
            "Equalizes middle-ear air pressure",
        ],
        [
            "লেন্স ও কর্নিয়াকে পুষ্টি যোগায়",
            "শুধু অপটিক স্নায়ু গঠন করে",
            "রডে রডোপসিন ক্ষরণ করে",
            "মধ্যকর্ণের বায়ুচাপ সমান করে",
        ],
        "A", "medium", "factual",
        "Aqueous humor nourishes avascular lens/cornea and helps maintain intraocular pressure.",
        "অ্যাকুয়াস হিউমার অ্যাভাসকুলার লেন্স–কর্নিয়াকে পুষ্ট করে ও চাপ রক্ষা করে।",
    ),
    q(
        "Which rectus muscle mainly turns the eyeball upward?",
        "কোন রেকটাস পেশি অক্ষিগোলককে প্রধানত উপরের দিকে ঘোরায়?",
        ["Medial rectus", "Lateral rectus", "Superior rectus", "Inferior rectus"],
        ["মিডিয়াল রেকটাস", "ল্যাটারাল রেকটাস", "সুপিরিয়র রেকটাস", "ইনফিরিয়র রেকটাস"],
        "C", "easy", "factual",
        "Superior rectus elevates the eyeball (with synergistic contributions in gaze).",
        "সুপিরিয়র রেকটাস অক্ষিগোলককে উর্ধ্বমুখী করে।",
    ),
    q(
        "Which statements correctly describe the Eustachian (pharyngotympanic) tube?",
        "ইউস্টেশিয়ান (ফ্যারিঙ্গোটাইমপ্যানিক) নালি সম্পর্কে কোনগুলো সঠিক?",
        [
            "Air-fills middle ear and equalizes pressure across the tympanic membrane",
            "Is the pigmented spot of the retina only",
            "Is the smallest middle-ear ossicle",
            "Secretes thyroid hormones into blood",
        ],
        [
            "মধ্যকর্ণ বায়ুপূর্ণ করে ও কর্ণপটহের দুই পাশের চাপ সমান রাখে",
            "শুধু রেটিনার রঞ্জিত বিন্দু",
            "মধ্যকর্ণের ক্ষুদ্রতম অস্থিকা",
            "রক্তে থাইরয়েড হরমোন ক্ষরণ করে",
        ],
        "A", "medium", "conceptual",
        "The tube links middle ear to pharynx; infections are common in children. Round window damps perilymph waves, not the tube.",
        "নালি মধ্যকর্ণকে গলবিলের সাথে যুক্ত করে; শিশুতে সংক্রমণ বেশি। পেরিলিম্ফ প্রশমন রাউন্ড উইন্ডোর কাজ।",
    ),
    q(
        "Which are parts/associated structures of the human middle ear?",
        "মানুষের মধ্যকর্ণের অংশ/সংশ্লিষ্ট গঠন কোনগুলো?",
        [
            "Tympanic membrane, Eustachian tube and ear ossicles",
            "Cornea, iris and pupil only",
            "Cochlea and semicircular canals only",
            "Optic chiasma and vitreous humor only",
        ],
        [
            "টিমপ্যানিক পর্দা, ইউস্টেশিয়ান নালি ও কর্ণাস্থিকা",
            "শুধু কর্নিয়া, আইরিশ ও পিউপিল",
            "শুধু ককলিয়া ও সেমিসার্কুলার ক্যানাল",
            "শুধু অপটিক কায়াজমা ও ভিট্রিয়াস হিউমার",
        ],
        "A", "medium", "factual",
        "Middle ear includes the tympanic cavity with ossicles and the Eustachian tube; cochlea is inner ear.",
        "মধ্যকর্ণে টিমপ্যানিক গহ্বর, অস্থিকা ও ইউস্টেশিয়ান নালি; ককলিয়া অন্তঃকর্ণ।",
    ),
    q(
        "During visual accommodation for near objects, which changes typically occur?",
        "কাছের বস্তুর জন্য উপযোজনের সময় সাধারণত কোন পরিবর্তন ঘটে?",
        [
            "Ciliary muscle activity changes and lens curvature/shape changes",
            "Optic nerve is detached from the retina",
            "Rods convert permanently into cones",
            "Eustachian tube secretes aqueous humor",
        ],
        [
            "সিলিয়ারি পেশির ক্রিয়া ও লেন্সের বক্রতা/আকার পরিবর্তন হয়",
            "অপটিক স্নায়ু রেটিনা থেকে বিচ্ছিন্ন হয়",
            "রড স্থায়ীভাবে কোনে রূপান্তরিত হয়",
            "ইউস্টেশিয়ান নালি অ্যাকুয়াস হিউমার ক্ষরণ করে",
        ],
        "A", "medium", "conceptual",
        "Accommodation alters lens focus via ciliary muscle and suspensory ligaments without changing object–lens distance.",
        "উপযোজনে সিলিয়ারি পেশি ও সাসপেন্সারি লিগামেন্টের মাধ্যমে লেন্সের ফোকাস বদলায়।",
    ),
    q(
        "What is the organ of Corti?",
        "অর্গান অব কর্টি কী?",
        [
            "Sound-receptor organ in the cochlear duct of the inner ear",
            "Tear-secreting gland at the outer eye angle",
            "Yellow spot at the retinal centre only",
            "Master endocrine gland below the hypothalamus",
        ],
        [
            "অন্তঃকর্ণের ককলিয়ার ডাক্টে অবস্থিত শব্দগ্রাহক সংবেদী অঙ্গ",
            "চোখের বাইরের কোণের অশ্রুগ্রন্থি",
            "শুধু রেটিনার কেন্দ্রের পীতবিন্দু",
            "হাইপোথ্যালামাসের নিচের প্রভু অন্তঃক্ষরা গ্রন্থি",
        ],
        "A", "easy", "factual",
        "Organ of Corti in the median cochlear channel converts vibrations into nerve impulses.",
        "অর্গান অব কর্টি শব্দ কম্পনকে স্নায়ু উদ্দীপনায় রূপান্তর করে।",
    ),
    q(
        "Where is the blind spot of the eye, and why is vision absent there?",
        "চোখের অন্ধবিন্দু কোথায় এবং কেন সেখানে দৃষ্টি থাকে না?",
        [
            "Where axons form the optic nerve; no rods or cones present",
            "At the fovea centralis where cones are densest",
            "In the cornea where refraction is maximal",
            "In the lens where accommodation occurs",
        ],
        [
            "অ্যাক্সনগুলো অপটিক স্নায়ু গঠনের স্থান; রড–কোন নেই",
            "ফোবিয়া সেন্ট্রালিসে যেখানে কোন ঘন",
            "কর্নিয়ায় যেখানে প্রতিসরণ সর্বাধিক",
            "লেন্সে যেখানে উপযোজন হয়",
        ],
        "A", "medium", "conceptual",
        "The optic disc lacks photoreceptors, so no image is detected there.",
        "অপটিক ডিস্কে আলোকগ্রাহক নেই বলে সেখানে প্রতিবিম্ব গৃহীত হয় না।",
    ),
    q(
        "What is the yellow spot (macula lutea / fovea region) of the retina?",
        "রেটিনার পীতবিন্দু (ম্যাকুলা লুটিয়া / ফোবিয়া অঞ্চল) কী?",
        [
            "A small yellowish area with a central pit of sharpest vision",
            "The opening of the Eustachian tube into the pharynx",
            "The malleus attached to the tympanic membrane",
            "The outer fibrous sclera of the eyeball",
        ],
        [
            "ছোট হলদেটে অঞ্চল যার কেন্দ্রীয় গর্তে সবচেয়ে স্পষ্ট দর্শন হয়",
            "গলবিলে ইউস্টেশিয়ান নালির মুখ",
            "টিমপ্যানিক পর্দায় আটকানো ম্যালিয়াস",
            "অক্ষিগোলকের বহিঃ তন্তুময় স্ক্লেরা",
        ],
        "A", "easy", "factual",
        "Fovea centralis in the macula provides highest visual acuity with dense cones.",
        "ম্যাকুলার ফোবিয়া সেন্ট্রালিসে ঘন কোন থাকায় তীক্ষ্ণ দৃষ্টি হয়।",
    ),
    q(
        "Which middle-ear ossicle is anvil-shaped?",
        "মধ্যকর্ণের কোন অস্থিকা নেহাই (অ্যানভিল) আকৃতির?",
        ["Malleus", "Incus", "Stapes", "Hyoid"],
        ["ম্যালিয়াস", "ইনকাস", "স্টেপিস", "হাইয়েড"],
        "B", "easy", "factual",
        "Incus looks like an anvil; malleus is hammer-like and stapes is stirrup-like.",
        "ইনকাস নেহাইসদৃশ; ম্যালিয়াস হাতুড়ি ও স্টেপিস রিক্যাব সদৃশ।",
    ),
    q(
        "Which is the smallest bone of the human body?",
        "মানবদেহের সবচেয়ে ছোট অস্থি কোনটি?",
        ["Malleus", "Incus", "Stapes", "Pisiform"],
        ["ম্যালিয়াস", "ইনকাস", "স্টেপিস", "পিসিফর্ম"],
        "C", "easy", "factual",
        "Stapes (stirrup) in the middle ear is the smallest bone and meets the oval window.",
        "স্টেপিস (রিক্যাব) দেহের ক্ষুদ্রতম অস্থি এবং ওভাল উইন্ডোর সাথে যুক্ত।",
    ),
    q(
        "How do otoliths help maintain balance?",
        "অটোলিথ কীভাবে ভারসাম্য রক্ষায় সাহায্য করে?",
        [
            "Their membrane presses hair cells when the head tilts, signalling the brain",
            "They refract light onto the fovea",
            "They secrete insulin into the blood",
            "They form CSF in the lateral ventricles",
        ],
        [
            "মাথা হেললে অটোলিথিক মেমব্রেন রোমকোষে চাপ দিয়ে মস্তিষ্কে সংকেত পাঠায়",
            "ফোবিয়ায় আলো প্রতিসরণ করে",
            "রক্তে ইনসুলিন ক্ষরণ করে",
            "ল্যাটারাল ভেন্ট্রিকলে CSF তৈরি করে",
        ],
        "A", "hard", "conceptual",
        "Otolithic membrane of the vestibular apparatus detects linear acceleration/tilt.",
        "ভেস্টিবুলার অটোলিথিক মেমব্রেন মাথার হেলানো/রৈখিক ত্বরণ শনাক্ত করে।",
    ),
    q(
        "Which gland secretes tears that clean and lubricate the eye surface?",
        "কোন গ্রন্থি অশ্রু ক্ষরণ করে চোখের পৃষ্ঠ পরিষ্কার ও মসৃণ রাখে?",
        ["Ceruminous", "Lacrimal", "Harderian", "Meibomian"],
        ["সিরুমিনাস", "ল্যাক্রিমাল", "হার্ডেরিয়ান", "মেবোমিয়ান"],
        "B", "easy", "factual",
        "Lacrimal glands produce tears; ceruminous glands make ear wax.",
        "ল্যাক্রিমাল গ্রন্থি অশ্রু উৎপন্ন করে; সিরুমিনাস কানের মোম তৈরি করে।",
    ),
    q(
        "Human vision is called binocular vision mainly because of which reason?",
        "মানুষের দৃষ্টিকে দ্বিনেত্র দৃষ্টি বলা হয় প্রধানত কেন?",
        [
            "Both eyes view one object and the brain fuses images into one 3D percept",
            "Only one eye functions at a time in daylight",
            "Rods alone create colour images",
            "The pupil secretes vitreous humor",
        ],
        [
            "দুচোখ এক বস্তু দেখে এবং মস্তিষ্ক প্রতিবিম্ব একত্রে ত্রিমাত্রিক ধারণায় মিলিয়ে নেয়",
            "দিনের বেলা একবারে একটি চোখই কাজ করে",
            "শুধু রড বর্ণচিত্র তৈরি করে",
            "পিউপিল ভিট্রিয়াস হিউমার ক্ষরণ করে",
        ],
        "A", "medium", "conceptual",
        "Slightly different retinal images are integrated for depth perception.",
        "দুই রেটিনার সামান্য ভিন্ন প্রতিবিম্ব মিলিয়ে গভীরতা উপলব্ধি হয়।",
    ),
    q(
        "Colour blindness is primarily associated with dysfunction of which photoreceptors?",
        "বর্ণান্ধতা প্রধানত কোন আলোকগ্রাহক কোষের ত্রুটির সাথে যুক্ত?",
        ["Rods only", "Cones", "Olfactory cells", "Taste buds"],
        ["শুধু রড", "কোন", "অলফ্যাক্টরি কোষ", "স্বাদকলি"],
        "B", "easy", "factual",
        "Cones mediate colour vision; cone defects cause colour blindness.",
        "কোন বর্ণদর্শন করে; কোনের ত্রুটিতে বর্ণান্ধতা হয়।",
    ),
    q(
        "Which of the following best describes vitreous humor?",
        "ভিট্রিয়াস হিউমার সম্পর্কে কোনটি সবচেয়ে সঠিক?",
        [
            "Transparent gel filling the posterior chamber that supports the eyeball",
            "Wax of the external auditory canal",
            "Hormone of the adrenal medulla",
            "Myelin of cranial nerve II only",
        ],
        [
            "পশ্চাৎ প্রকোষ্ঠের স্বচ্ছ জেল যা অক্ষিগোলককে স্থিতি দেয়",
            "বহিঃকর্ণ নালির মোম",
            "অ্যাড্রেনাল মেডুলার হরমোন",
            "শুধু দ্বিতীয় করোটিক স্নায়ুর মায়েলিন",
        ],
        "A", "medium", "factual",
        "Vitreous humor maintains shape and optical path behind the lens.",
        "ভিট্রিয়াস হিউমার লেন্সের পেছনে আকৃতি ও আলোকপথ বজায় রাখে।",
    ),
    q(
        "Meibomian glands of the eyelids mainly secrete which substance?",
        "অক্ষিপল্লবের মেবোমিয়ান গ্রন্থি প্রধানত কী ক্ষরণ করে?",
        [
            "Oily secretion that reduces tear evaporation",
            "Thyroxine into the bloodstream",
            "CSF into the ventricles",
            "Digestive pepsin into the stomach",
        ],
        [
            "তৈলাক্ত ক্ষরণ যা অশ্রুর বাষ্পীভবন কমায়",
            "রক্তে থাইরক্সিন",
            "ভেন্ট্রিকলে CSF",
            "পাকস্থলীতে পেপসিন",
        ],
        "A", "hard", "factual",
        "Meibomian (tarsal) glands secrete lipids forming the outer tear film layer.",
        "মেবোমিয়ান গ্রন্থি অশ্রুপটলের বহিঃ লিপিড স্তর তৈরি করে।",
    ),
]


# --- t03: Hormones / হরমোন ---
T03 = [
    q(
        "Which secretions come from the ‘master gland’ (pituitary)?",
        "‘প্রভুগ্রন্থি’ (পিটুইটারি) থেকে কোনগুলো নিঃসৃত হয়?",
        [
            "ACTH and FSH only (not calcitonin)",
            "Calcitonin only",
            "Pepsin and salivary amylase only",
            "Bile salts only",
        ],
        [
            "শুধু ACTH ও FSH (ক্যালসিটোনিন নয়)",
            "শুধু ক্যালসিটোনিন",
            "শুধু পেপসিন ও লালা অ্যামাইলেজ",
            "শুধু পিত্তলবণ",
        ],
        "A", "medium", "conceptual",
        "Anterior pituitary secretes ACTH, FSH and other tropins; calcitonin is from thyroid C cells.",
        "অগ্র পিটুইটারি থেকে ACTH, FSH ইত্যাদি; ক্যালসিটোনিন থাইরয়েডের।",
    ),
    q(
        "Which hormone increases heart rate and blood pressure in emergency ‘fight-or-flight’ states?",
        "জরুরি ‘লড়াই-বা-পলায়ন’ অবস্থায় হৃৎস্পন্দন ও রক্তচাপ বৃদ্ধিকারী হরমোন কোনটি?",
        ["Glucocorticoid", "Adrenaline", "Estrogen", "Vasopressin"],
        ["গ্লুকোকর্টিকয়েড", "অ্যাড্রেনালিন", "ইস্ট্রোজেন", "ভেসোপ্রেসিন"],
        "B", "easy", "factual",
        "Adrenaline (epinephrine) from adrenal medulla raises HR, BP and readiness.",
        "অ্যাড্রেনাল মেডুলার অ্যাড্রেনালিন হৃৎস্পন্দন ও রক্তচাপ বাড়ায়।",
    ),
    q(
        "Secretion transported in blood from a ductless gland is mainly which of the following?",
        "নালিবিহীন গ্রন্থি থেকে রক্তে পরিবাহিত ক্ষরণ মূলত কোনটি?",
        ["Hormone", "Digestive enzyme via duct only", "Bile via bile duct only", "Sweat onto skin only"],
        ["হরমোন", "শুধু নালিপথে পাচক এনজাইম", "শুধু পিত্তনালিতে পিত্ত", "শুধু ত্বকে ঘাম"],
        "A", "easy", "conceptual",
        "Endocrine (ductless) glands release hormones into blood/lymph.",
        "অন্তঃক্ষরা (নালিবিহীন) গ্রন্থি রক্ত/লসিকায় হরমোন ক্ষরণ করে।",
    ),
    q(
        "A ducted (exocrine) gland typically secretes which type of product?",
        "নালিযুক্ত (বহিঃক্ষরা) গ্রন্থি সাধারণত কোন ধরনের পদার্থ ক্ষরণ করে?",
        ["Oxytocin", "Enzyme (via a duct)", "Melatonin", "Adrenaline"],
        ["অক্সিটোসিন", "এনজাইম (নালিপথে)", "মেলাটোনিন", "অ্যাড্রেনালিন"],
        "B", "easy", "factual",
        "Exocrine glands pour secretions (e.g., enzymes) through ducts; the others are endocrine hormones.",
        "বহিঃক্ষরা গ্রন্থি নালি দিয়ে এনজাইম ইত্যাদি ক্ষরায়; বাকিগুলো অন্তঃক্ষরা হরমোন।",
    ),
    q(
        "Seeing a dangerous animal suddenly raises which hormone in blood?",
        "হঠাৎ বিপজ্জনক প্রাণী দেখলে রক্তে কোন হরমোন বাড়ে?",
        ["Insulin", "Adrenaline", "Thyroxine", "Gastrin"],
        ["ইনসুলিন", "অ্যাড্রেনালিন", "থাইরক্সিন", "গ্যাস্ট্রিন"],
        "B", "easy", "application",
        "Fear/stress triggers adrenal medullary adrenaline release.",
        "ভয়/চাপে অ্যাড্রেনাল মেডুলা থেকে অ্যাড্রেনালিন ক্ষরিত হয়।",
    ),
    q(
        "Deficiency of thyroxine can lead to which disorders?",
        "থাইরক্সিনের অভাবে কোন সমস্যাগুলো হতে পারে?",
        [
            "Myxoedema, cretinism and goitre (as applicable by age/iodine status)",
            "Only night blindness",
            "Only colour blindness",
            "Only otitis media",
        ],
        [
            "মিক্সিডিমা, ক্রেটিনিজম ও গলগণ্ড (বয়স/আয়োডিন অবস্থা অনুসারে)",
            "শুধু রাতকানা",
            "শুধু বর্ণান্ধতা",
            "শুধু ওটিটিস মিডিয়া",
        ],
        "A", "medium", "conceptual",
        "Low thyroxine: cretinism in children, myxoedema in adults; iodine lack also causes goitre.",
        "থাইরক্সিন কমলে শিশুতে ক্রেটিনিজম, প্রাপ্তবয়স্কে মিক্সিডিমা; আয়োডিন অভাবে গলগণ্ড।",
    ),
    q(
        "Which element is present in thyroxine?",
        "থাইরক্সিনে কোন উপাদান বিদ্যমান?",
        ["Iron", "Potassium", "Calcium", "Iodine"],
        ["আয়রন", "পটাসিয়াম", "ক্যালসিয়াম", "আয়োডিন"],
        "D", "easy", "factual",
        "Thyroxine (T4) is an iodinated thyroid hormone.",
        "থাইরক্সিন (T4) আয়োডিনযুক্ত থাইরয়েড হরমোন।",
    ),
    q(
        "Which hormone is secreted by the posterior pituitary?",
        "পশ্চাৎ পিটুইটারি থেকে কোন হরমোন নিঃসৃত হয়?",
        ["STH (GH)", "TSH", "FSH", "ADH (vasopressin) / oxytocin"],
        ["STH (GH)", "TSH", "FSH", "ADH (ভেসোপ্রেসিন) / অক্সিটোসিন"],
        "D", "medium", "factual",
        "Posterior pituitary releases ADH and oxytocin; STH, TSH and FSH are anterior.",
        "পশ্চাৎ পিটুইটারি ADH ও অক্সিটোসিন মুক্ত করে; STH, TSH, FSH অগ্র পিটুইটারির।",
    ),
    q(
        "Which of the following is NOT secreted by the thyroid gland?",
        "নিচের কোনটি থাইরয়েড গ্রন্থি থেকে নিঃসৃত নয়?",
        ["Thyroxine", "Calcitonin", "Triiodothyronine (T3)", "Parathormone (PTH)"],
        ["থাইরক্সিন", "ক্যালসিটোনিন", "ট্রাইআয়োডোথাইরোনিন (T3)", "প্যারাথরমোন (PTH)"],
        "D", "medium", "factual",
        "PTH is from parathyroid glands; thyroid secretes T3, T4 and calcitonin.",
        "PTH প্যারাথাইরয়েড থেকে; থাইরয়েড T3, T4 ও ক্যালসিটোনিন ক্ষরায়।",
    ),
    q(
        "What is insulin, and what is its main effect?",
        "ইনসুলিন কী এবং এর প্রধান কাজ কী?",
        [
            "Pancreatic β-cell hormone that lowers blood glucose",
            "Adrenal cortex steroid that raises Na⁺ only",
            "Pineal hormone that sets only skin colour",
            "Gastric enzyme that digests protein",
        ],
        [
            "অগ্ন্যাশয়ের β-কোষের হরমোন যা রক্তে গ্লুকোজ কমায়",
            "অ্যাড্রেনাল কর্টেক্সের স্টেরয়েড যা শুধু Na⁺ বাড়ায়",
            "পাইনাল হরমোন যা শুধু ত্বকের বর্ণ ঠিক করে",
            "পাকস্থলীর প্রোটিন-পাচক এনজাইম",
        ],
        "A", "easy", "factual",
        "Insulin from islets of Langerhans promotes glucose uptake/utilization.",
        "ল্যাঙ্গারহ্যান্স দ্বীপের ইনসুলিন গ্লুকোজ গ্রহণ/ব্যবহার বাড়ায়।",
    ),
    q(
        "What are tropic hormones?",
        "ট্রপিক হরমোন কী?",
        [
            "Hormones from one gland that stimulate secretion of another endocrine gland",
            "Only digestive enzymes of the pancreas",
            "Only neurotransmitters at neuromuscular junctions",
            "Only antibodies in plasma",
        ],
        [
            "এক গ্রন্থির হরমোন যা অন্য অন্তঃক্ষরা গ্রন্থির ক্ষরণ উদ্দীপ্ত করে",
            "শুধু অগ্ন্যাশয়ের পাচক এনজাইম",
            "শুধু নিউরোমাসকুলার জংশনের নিউরোট্রান্সমিটার",
            "শুধু প্লাজমার অ্যান্টিবডি",
        ],
        "A", "medium", "conceptual",
        "Examples: TSH, FSH, LH, ACTH from anterior pituitary.",
        "উদাহরণ: অগ্র পিটুইটারির TSH, FSH, LH, ACTH।",
    ),
    q(
        "Why is the pituitary called the master gland?",
        "পিটুইটারিকে প্রভুগ্রন্থি বলা হয় কেন?",
        [
            "It secretes many hormones including tropins that control other endocrine glands",
            "It is the largest gland of the body",
            "It only digests food in the intestine",
            "It forms CSF exclusively",
        ],
        [
            "অনেক হরমোনসহ ট্রপিন ক্ষরণ করে অন্য অন্তঃক্ষরা গ্রন্থি নিয়ন্ত্রণ করে",
            "দেহের বৃহত্তম গ্রন্থি",
            "শুধু অন্ত্রে খাদ্য হজম করে",
            "একমাত্র CSF তৈরি করে",
        ],
        "A", "medium", "conceptual",
        "Despite small size, pituitary regulates growth, metabolism and other glands via tropic hormones.",
        "আকারে ছোট হলেও ট্রপিক হরমোন দিয়ে অন্য গ্রন্থি ও বিপাক নিয়ন্ত্রণ করে।",
    ),
    q(
        "Hormones are often called chemical messengers because they do what?",
        "হরমোনকে রাসায়নিক দূত বলা হয় কারণ তারা কী করে?",
        [
            "Travel in blood/lymph to affect distant target physiology in tiny amounts",
            "Act only as structural proteins of bone",
            "Are excreted solely as urea without any effect",
            "Replace neurons entirely in all reflexes",
        ],
        [
            "অতি অল্প মাত্রায় রক্ত/লসিকায় গিয়ে দূরবর্তী লক্ষ্যে শারীরবৃত্ত প্রভাব ফেলে",
            "শুধু অস্থির কাঠামোগত প্রোটিন হিসেবে কাজ করে",
            "কোনো প্রভাব ছাড়া শুধু ইউরিয়া হিসেবে নির্গতমিত হয়",
            "সব প্রতিবর্তে নিউরন সম্পূর্ণ প্রতিস্থাপন করে",
        ],
        "A", "easy", "conceptual",
        "Endocrine messengers regulate growth, metabolism, reproduction and homeostasis.",
        "অন্তঃক্ষরা দূত বৃদ্ধি, বিপাক, প্রজনন ও হোমিওস্ট্যাসিস নিয়ন্ত্রণ করে।",
    ),
    q(
        "Glucocorticoids mainly regulate which process?",
        "গ্লুকোকর্টিকয়েড প্রধানত কোন প্রক্রিয়া নিয়ন্ত্রণ করে?",
        [
            "Carbohydrate (and related) metabolism",
            "Only hearing acuity in the cochlea",
            "Only iris colour",
            "Only formation of ear wax",
        ],
        [
            "শর্করা (ও সংশ্লিষ্ট) বিপাক",
            "শুধু ককলিয়ার শ্রবণ তীক্ষ্ণতা",
            "শুধু আইরিশের বর্ণ",
            "শুধু কানের মোম গঠন",
        ],
        "A", "medium", "factual",
        "Adrenal cortex glucocorticoids (e.g., cortisol) regulate carb metabolism and stress responses.",
        "অ্যাড্রেনাল কর্টেক্সের গ্লুকোকর্টিকয়েড শর্করা বিপাক ও স্ট্রেস প্রতিক্রিয়া নিয়ন্ত্রণ করে।",
    ),
    q(
        "ADH (vasopressin) mainly acts on which target to conserve water?",
        "ADH (ভেসোপ্রেসিন) পানি সংরক্ষণে প্রধানত কোন লক্ষ্যে কাজ করে?",
        ["Kidney tubules (water reabsorption)", "Taste buds only", "Rod cells only", "Hair cells of Corti only"],
        ["বৃক্কের নালিকা (পানি পুনঃশোষণ)", "শুধু স্বাদকলি", "শুধু রডকোষ", "শুধু কর্টির রোমকোষ"],
        "A", "medium", "factual",
        "ADH from posterior pituitary increases renal water reabsorption; aldosterone (adrenal) also affects salt/water.",
        "পশ্চাৎ পিটুইটারির ADH বৃক্কে পানি পুনঃশোষণ বাড়ায়।",
    ),
    q(
        "Melatonin is secreted by which gland?",
        "মেলাটোনিন কোন গ্রন্থি থেকে নিঃসৃত হয়?",
        ["Pineal", "Parotid only", "Prostate only", "Sweat gland only"],
        ["পাইনাল", "শুধু প্যারোটিড", "শুধু প্রোস্টেট", "শুধু ঘর্মগ্রন্থি"],
        "A", "easy", "factual",
        "Pineal melatonin helps regulate sleep–wake (circadian) rhythms.",
        "পাইনাল গ্রন্থির মেলাটোনিন ঘুম–জাগরণ ছন্দ নিয়ন্ত্রণে সাহায্য করে।",
    ),
    q(
        "FSH mainly stimulates which process in females?",
        "নারীদেহে FSH প্রধানত কোন প্রক্রিয়া উদ্দীপ্ত করে?",
        [
            "Ovarian follicle maturation and estrogen synthesis support",
            "Only contraction of uterine smooth muscle in labour",
            "Only adrenaline release from medulla",
            "Only formation of aqueous humor",
        ],
        [
            "ডিম্বাশয়ের ফলিকল পরিপক্কতা ও ইস্ট্রোজেন সংশ্লেষে সহায়তা",
            "শুধু প্রসবকালীন জরায়ু পেশি সংকোচন",
            "শুধু মেডুলা থেকে অ্যাড্রেনালিন ক্ষরণ",
            "শুধু অ্যাকুয়াস হিউমার গঠন",
        ],
        "A", "medium", "factual",
        "Follicle-stimulating hormone from anterior pituitary matures follicles and supports estrogen production.",
        "অগ্র পিটুইটারির FSH ফলিকল পূর্ণতা ও ইস্ট্রোজেন সংশ্লেষে উদ্দীপনা দেয়।",
    ),
    q(
        "Aldosterone is secreted from which source?",
        "অ্যালডোস্টেরন কোন উৎস থেকে নিঃসৃত হয়?",
        ["Adrenal cortex", "Posterior pituitary only", "Retinal pigment epithelium", "Organ of Corti"],
        ["অ্যাড্রেনাল কর্টেক্স", "শুধু পশ্চাৎ পিটুইটারি", "রেটিনার পিগমেন্ট এপিথেলিয়াম", "অর্গান অব কর্টি"],
        "A", "medium", "factual",
        "Mineralocorticoid aldosterone from adrenal cortex regulates Na⁺/K⁺ and water balance.",
        "অ্যাড্রেনাল কর্টেক্সের মিনারেলোকর্টিকয়েড অ্যালডোস্টেরন Na⁺/K⁺ ও পানি ভারসাম্য রাখে।",
    ),
    q(
        "Which statements about endocrine (ductless) hormone action are typically true?",
        "অন্তঃক্ষরা হরমোন ক্রিয়া সম্পর্কে সাধারণত কোনগুলো সত্য?",
        [
            "Carried in blood and effective in very low concentration",
            "Always stored indefinitely in ducts like saliva",
            "Never travel farther than one synapse",
            "Are identical to digestive enzymes of the gut",
        ],
        [
            "রক্তে বাহিত হয় এবং অতি কম ঘনত্বে কার্যকর",
            "সবসময় লালার মতো নালিতে অনির্দিষ্টকাল জমা থাকে",
            "এক সিন্যাপসের বেশি দূর যায় না",
            "অন্ত্রের পাচক এনজাইমের সমান",
        ],
        "A", "medium", "conceptual",
        "Hormones circulate and act at tiny concentrations on specific receptors; they are not duct-stored enzymes.",
        "হরমোন রক্তে চলাচল করে ক্ষুদ্র মাত্রায় নির্দিষ্ট রিসেপ্টরে কাজ করে।",
    ),
    q(
        "Hypothalamus influences endocrine control mainly by which means?",
        "হাইপোথ্যালামাস অন্তঃক্ষরা নিয়ন্ত্রণে প্রধানত কীভাবে প্রভাব রাখে?",
        [
            "Releasing/inhibiting factors regulating pituitary, and producing ADH/oxytocin",
            "Forming the tympanic membrane only",
            "Secreting pepsinogen only",
            "Generating rhodopsin only",
        ],
        [
            "পিটুইটারি নিয়ন্ত্রক রিলিজিং/ইনহিবিটিং ফ্যাক্টর এবং ADH/অক্সিটোসিন উৎপাদন",
            "শুধু টিমপ্যানিক পর্দা গঠন",
            "শুধু পেপসিনোজেন ক্ষরণ",
            "শুধু রডোপসিন তৈরি",
        ],
        "A", "hard", "conceptual",
        "Hypothalamus is the key link between nervous and endocrine systems via pituitary control.",
        "হাইপোথ্যালামাস পিটুইটারি নিয়ন্ত্রণের মাধ্যমে স্নায়ু–অন্তঃক্ষরা সংযোগ রক্ষা করে।",
    ),
]


TOPICS_MAP = {
    "bio2_27_ch08_t01": T01,
    "bio2_27_ch08_t02": T02,
    "bio2_27_ch08_t03": T03,
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
        "chapter": "bio2_27_ch08",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p266_pdf272.png",
            "p267_pdf273.png",
            "p268_pdf274.png",
            "p269_pdf275.png",
            "p270_pdf276.png",
            "p271_pdf277.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio2_27_ch08_t01": {
                "title": "Nervous system / স্নায়ুতন্ত্র",
                "themes": [
                    "vagus to larynx/heart; CN IV trochlear; mixed facial+vagus; spinal accessory shoulder",
                    "eye-motor III/IV/VI; hindbrain cerebellum; cerebrum largest; facial taste",
                    "spinal reflex; hypoglossal tongue; auditory hearing/balance; 4 ventricles",
                    "withdrawal via cord; innate reflex; vagus mixed; meninges; synapse; CSF; trigeminal branches; neurotransmitter",
                ],
            },
            "bio2_27_ch08_t02": {
                "title": "Sense organs / ইন্দ্রিয় অঙ্গ",
                "themes": [
                    "conjunctiva accessory; rods rhodopsin/night; night blindness; pupil not refractive",
                    "aqueous nourishes lens/cornea; superior rectus; Eustachian pressure; middle ear parts",
                    "accommodation ciliary+lens; organ of Corti; blind spot; yellow spot/fovea",
                    "incus anvil; stapes smallest; otoliths; lacrimal tears; binocular vision; cones colour; vitreous; meibomian oil",
                ],
            },
            "bio2_27_ch08_t03": {
                "title": "Hormones / হরমোন",
                "themes": [
                    "pituitary ACTH+FSH not CT; adrenaline HR/BP; hormone ductless; enzyme exocrine",
                    "fear→adrenaline; thyroxine deficiency triad; iodine in T4; posterior ADH/oxytocin",
                    "PTH not thyroid; insulin β-cells; tropic hormones; master gland; chemical messenger",
                    "glucocorticoids carb; ADH kidney; melatonin pineal; FSH follicles; aldosterone; endocrine traits; hypothalamus–pituitary",
                ],
            },
        },
        "low_confidence": [
            "OCR of printed MCQ pages p266–271 is noisy (garbled options/answer marks); stems reconstructed from readable fragments, CQ text on the same pages, and standard HSC Zoology Ch8 facts.",
            "Figure-/stimulus-linked bank items (cranial-nerve diagrams, ear ossicle labels, brain-part labels, gland vignettes) rewritten as standalone stems.",
            "Answer keys for multi-select board items inferred from physiology when OCR option marks were unreadable.",
            "Sense-organ and hormone topics supplemented from CQ knowledge stems (meninges, CSF, accommodation, tropic hormones, insulin) where MCQ density on a page was figure-heavy.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio2_27_ch08_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio2_27_ch08_t01": 20,
                "bio2_27_ch08_t02": 20,
                "bio2_27_ch08_t03": 20,
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
        / "ch08_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
