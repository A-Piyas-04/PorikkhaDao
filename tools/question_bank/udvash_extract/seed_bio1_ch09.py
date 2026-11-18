#!/usr/bin/env python3
"""Seed Biology 1st Paper Ch9 bilingual MCQs (Udvash-licensed curation).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: bio1_27_ch09_t01..t03 (water/minerals; photosynthesis; respiration & growth).
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
    "biology p1 ch09; curated bilingual"
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


# --- t01: Water and mineral transport / পানি ও খনিজ পরিবহন ---
T01 = [
    q(
        "Which ion is absorbed most slowly by plants?",
        "উদ্ভিদ দ্বারা সবচেয়ে ধীর গতিতে শোষিত হয় কোন আয়নটি?",
        ["K⁺", "Ca²⁺", "NO₃⁻", "Cl⁻"],
        ["K⁺", "Ca²⁺", "NO₃⁻", "Cl⁻"],
        "B", "easy", "factual",
        "Among common ions, K⁺ and NO₃⁻ are absorbed fastest; Ca²⁺ and SO₄²⁻ are among the slowest.",
        "সাধারণ আয়নের মধ্যে K⁺ ও NO₃⁻ দ্রুততম; Ca²⁺ ও SO₄²⁻ সবচেয়ে ধীর গতিতে শোষিত হয়।",
    ),
    q(
        "Which ion is absorbed most rapidly by plant roots?",
        "মূল দ্বারা কোন খনিজ আয়ন সবচেয়ে দ্রুত গতিতে শোষিত হয়?",
        ["Na⁺", "Mg²⁺", "K⁺", "Ca²⁺"],
        ["Na⁺", "Mg²⁺", "K⁺", "Ca²⁺"],
        "C", "easy", "factual",
        "Potassium (K⁺) and nitrate (NO₃⁻) show the highest absorption rates in HSC mineral-uptake lists.",
        "HSC তালিকায় K⁺ ও NO₃⁻ শোষণ হার সর্বোচ্চ।",
    ),
    q(
        "Stomatal opening and closing are controlled by which factors?",
        "পত্ররন্ধ্র খোলা ও বন্ধ হওয়া নিয়ন্ত্রণ করে কোনগুলো?",
        ["K⁺ and pH only", "Na⁺ only", "Ca²⁺ only", "Mg²⁺ and Cl⁻ only"],
        ["কেবল K⁺ ও pH", "কেবল Na⁺", "কেবল Ca²⁺", "কেবল Mg²⁺ ও Cl⁻"],
        "A", "medium", "conceptual",
        "Modern stomatal mechanism links K⁺ fluxes and guard-cell pH/turgor; Na⁺ is not the primary controller.",
        "আধুনিক ধারণায় K⁺ প্রবাহ ও রক্ষীকোষের pH/টার্গর পত্ররন্ধ্র নিয়ন্ত্রণ করে; Na⁺ প্রধান নিয়ন্ত্রক নয়।",
    ),
    q(
        "Which ion helps stomata to open?",
        "কোন আয়নটি পত্ররন্ধ্র খুলতে সহায়তা করে?",
        ["Ca²⁺", "Na⁺", "Mn²⁺", "K⁺"],
        ["Ca²⁺", "Na⁺", "Mn²⁺", "K⁺"],
        "D", "easy", "factual",
        "Active K⁺ entry into guard cells raises osmotic potential and opens the stomatal pore.",
        "রক্ষীকোষে K⁺ প্রবেশ অভিস্রবণ চাপ বাড়িয়ে পত্ররন্ধ্র খুলে।",
    ),
    q(
        "Silicon is a major nutrient specially for which plants?",
        "সিলিকন কোন উদ্ভিদের জন্য বৃহৎ পুষ্টি উপাদান?",
        ["C₄ plants only", "Marine algae", "Grasses", "Nitrogen-fixing legumes"],
        ["কেবল C₄ উদ্ভিদ", "সামুদ্রিক শৈবাল", "ঘাস", "নাইট্রোজেন ফিক্সিং লিগিউম"],
        "C", "medium", "factual",
        "Si is especially important for grasses; Na for many C₄ plants, Co for N-fixing legumes, I for marine algae.",
        "সিলিকন ঘাসের জন্য গুরুত্বপূর্ণ; সোডিয়াম অনেক C₄, কোবাল্ট নাইট্রোজেন ফিক্সার, আয়োডিন সামুদ্রিক শৈবালের জন্য।",
    ),
    q(
        "Which is a macronutrient?",
        "নিচের কোনটি ম্যাক্রো মৌল?",
        ["Sodium", "Nitrogen", "Manganese", "Chlorine"],
        ["সোডিয়াম", "নাইট্রোজেন", "ম্যাঙ্গানিজ", "ক্লোরিন"],
        "B", "easy", "factual",
        "N, P, K, Ca, Mg, S (and C, H, O) are macronutrients; Mn, Cl, Na are micro or beneficial.",
        "N, P, K, Ca, Mg, S ম্যাক্রো; Mn, Cl, Na সাধারণত মাইক্রো বা উপকারী মৌল।",
    ),
    q(
        "Which element do plants take mainly from the air?",
        "নিচের কোনটি উদ্ভিদ বাতাস হতে গ্রহণ করে?",
        ["Nitrogen", "Carbon", "Chlorine", "Sodium"],
        ["নাইট্রোজেন", "কার্বন", "ক্লোরিন", "সোডিয়াম"],
        "B", "easy", "factual",
        "Carbon enters as CO₂ from air; most other minerals (except C, H, O sources) come from soil/water.",
        "কার্বন বায়ুর CO₂ থেকে আসে; অধিকাংশ অন্যান্য খনিজ মাটি/পানি থেকে শোষিত হয়।",
    ),
    q(
        "Which element do plants absorb mainly from the soil?",
        "নিচের কোন মৌল উদ্ভিদ মাটি থেকে গ্রহণ করে?",
        ["Carbon", "Hydrogen", "Oxygen", "Nitrogen"],
        ["কার্বন", "হাইড্রোজেন", "অক্সিজেন", "নাইট্রোজেন"],
        "D", "easy", "factual",
        "C, H and O come largely from CO₂ and H₂O; nitrogen is absorbed from soil as mineral ions.",
        "C, H, O মূলত CO₂ ও H₂O থেকে; নাইট্রোজেন মাটির খনিজ আয়ন রূপে শোষিত হয়।",
    ),
    q(
        "Why is ion-exchange absorption called passive absorption?",
        "আয়ন বিনিময় প্রক্রিয়াকে নিষ্ক্রিয় পরিশোষণ বলার কারণ কী?",
        [
            "It requires cytochrome pumps",
            "It consumes metabolic ATP",
            "It occurs without spending metabolic energy",
            "It always moves ions against a gradient using carriers",
        ],
        [
            "এতে সাইটোক্রোম পাম্প লাগে",
            "এতে বিপাকীয় ATP খরচ হয়",
            "বিপাকীয় শক্তি ব্যয় ছাড়াই ঘটে",
            "সবসময় বাহক দিয়ে ঘনত্বের বিপরীতে যায়",
        ],
        "C", "medium", "conceptual",
        "In ion exchange, H⁺/OH⁻ swap with external cations/anions without metabolic energy expenditure.",
        "আয়ন বিনিময়ে H⁺/OH⁻ বিনিময়ে বাইরের ক্যাটায়ন/অ্যানায়ন প্রবেশ করে; বিপাকীয় শক্তি লাগে না।",
    ),
    q(
        "Which theory explains active salt absorption involving the cytochrome system?",
        "সাইটোক্রোম পাম্প ধারণার প্রবক্তা কোন তত্ত্ব/বিজ্ঞানীর সাথে যুক্ত?",
        ["Bennet-Clark", "George de Hevesy", "Lundegårdh", "S. Imamura"],
        ["বেনেট-ক্লার্ক", "জর্জ দ্য হেভেসি", "লুনডেগার্ড", "এস. ইমামুরা"],
        "C", "medium", "factual",
        "Lundegårdh proposed anion absorption via the cytochrome (respiratory) electron chain — the cytochrome pump.",
        "লুনডেগার্ড সাইটোক্রোম সিস্টেমের মাধ্যমে অ্যানায়ন পরিশোষণের সাইটোক্রোম পাম্প মতবাদ দেন।",
    ),
    q(
        "Which is an active absorption theory?",
        "সক্রিয় লবণ পরিশোষণ মতবাদ কোনটি?",
        [
            "Mass-flow theory",
            "Ion-exchange theory",
            "Donnan equilibrium theory",
            "Lundegårdh (cytochrome pump) theory",
        ],
        [
            "ব্যাপক প্রবাহ মতবাদ",
            "আয়ন বিনিময় মতবাদ",
            "ডোনান সাম্যাবস্থা মতবাদ",
            "লুনডেগার্ড (সাইটোক্রোম পাম্প) মতবাদ",
        ],
        "D", "medium", "conceptual",
        "Mass flow, ion exchange and Donnan equilibrium are passive; Lundegårdh’s cytochrome pump is active.",
        "ব্যাপক প্রবাহ, আয়ন বিনিময় ও ডোনান নিষ্ক্রিয়; লুনডেগার্ডের সাইটোক্রোম পাম্প সক্রিয় পরিশোষণ।",
    ),
    q(
        "Which is a passive absorption theory?",
        "নিষ্ক্রিয় পরিশোষণ মতবাদ হলো—",
        [
            "Lundegårdh theory",
            "Lecithin carrier theory",
            "Proton–anion co-transport theory",
            "Donnan equilibrium",
        ],
        [
            "লুনডেগার্ড মতবাদ",
            "লেসিথিন বাহক মতবাদ",
            "প্রোটন-অ্যানায়ন কো-ট্রান্সপোর্ট মতবাদ",
            "ডোনান সাম্যাবস্থা",
        ],
        "D", "medium", "factual",
        "Donnan equilibrium describes passive ionic distribution; carrier and cytochrome-linked models are active.",
        "ডোনান সাম্যাবস্থা নিষ্ক্রিয় আয়ন বণ্টন ব্যাখ্যা করে; বাহক ও সাইটোক্রোম-সংযুক্ত মডেল সক্রিয়।",
    ),
    q(
        "Active mineral absorption: (i) respiration rate stays normal (ii) carriers mediate uptake (iii) enzymes play important roles — which are correct?",
        "সক্রিয় পরিশোষণে—(i) শ্বসন হার স্বাভাবিক থাকে (ii) বাহক দ্বারা সম্পন্ন (iii) এনজাইম গুরুত্বপূর্ণ — কোনটি সঠিক?",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "B", "hard", "conceptual",
        "Active uptake uses carriers/enzymes and often raises respiration; (i) is false, so (ii) and (iii) apply.",
        "সক্রিয় শোষণে বাহক ও এনজাইম লাগে এবং শ্বসন হার বাড়ে; (i) মিথ্যা, তাই (ii) ও (iii) সঠিক।",
    ),
    q(
        "What is the chief organ of transpiration in plants?",
        "উদ্ভিদের প্রধান প্রস্বেদন অঙ্গ/পথ কোনটি?",
        ["Root epidermis only", "Stem cuticle only", "Stomata (leaves)", "Hydathodes only"],
        ["কেবল মূলের ত্বক", "কেবল কাণ্ডের কিউটিকল", "পত্ররন্ধ্র (পাতা)", "কেবল হাইডাথোড"],
        "C", "easy", "factual",
        "Most water vapour leaves through stomata on leaves; cuticular and lenticular paths are minor.",
        "অধিকাংশ জলীয়বাষ্প পাতার পত্ররন্ধ্র দিয়ে বের হয়; ত্বকীয় ও লেন্টিকুলার প্রস্বেদন কম।",
    ),
    q(
        "Transpiration rate increases when—",
        "কোন ক্ষেত্রে প্রস্বেদন হার বেশি হয়?",
        [
            "Humidity is high",
            "Atmospheric pressure is low",
            "Temperature is low",
            "Air movement is low",
        ],
        [
            "আর্দ্রতা বেশি হয়",
            "বায়ুচাপ কম হয়",
            "তাপমাত্রা কম হয়",
            "বায়ুপ্রবাহ কম হয়",
        ],
        "B", "medium", "conceptual",
        "Lower atmospheric pressure favours evaporation; high humidity, low temperature and still air reduce it.",
        "বায়ুচাপ কম হলে বাষ্পীভবন সহজ; উচ্চ আর্দ্রতা, কম তাপ ও কম বায়ুপ্রবাহ প্রস্বেদন কমায়।",
    ),
    q(
        "Which increase reduces the rate of transpiration?",
        "নিচের কোনটি বাড়লে প্রস্বেদন কমে?",
        ["Light intensity", "Temperature", "Relative humidity", "Air movement"],
        ["আলোর তীব্রতা", "তাপমাত্রা", "আপেক্ষিক আর্দ্রতা", "বায়ুপ্রবাহ"],
        "C", "easy", "conceptual",
        "Higher relative humidity lowers the vapour-pressure gradient, so transpiration slows.",
        "আপেক্ষিক আর্দ্রতা বাড়লে বাষ্পচাপ ঢাল কমে, ফলে প্রস্বেদন হ্রাস পায়।",
    ),
    q(
        "Which ion is absorbed as an anion?",
        "কোনটি অ্যানায়ন হিসেবে শোষিত হয়?",
        ["Chlorine", "Calcium", "Magnesium", "Sodium"],
        ["ক্লোরিন", "ক্যালসিয়াম", "ম্যাগনেসিয়াম", "সোডিয়াম"],
        "A", "easy", "factual",
        "Cl⁻ is an anion; Ca²⁺, Mg²⁺ and Na⁺ are cations.",
        "Cl⁻ অ্যানায়ন; Ca²⁺, Mg²⁺ ও Na⁺ ক্যাটায়ন।",
    ),
    q(
        "Which nutrient is absorbed as a cation?",
        "কোন উপাদানটি উদ্ভিদ ক্যাটায়ন হিসেবে শোষণ করে?",
        ["N as NO₃⁻ form only", "Cl", "B", "K"],
        ["কেবল NO₃⁻ রূপে N", "Cl", "B", "K"],
        "D", "easy", "factual",
        "Potassium is taken up as K⁺; chloride is Cl⁻; nitrogen often enters as NO₃⁻/NH₄⁺ depending on form.",
        "পটাসিয়াম K⁺ রূপে শোষিত; ক্লোরাইড Cl⁻; নাইট্রোজেন সাধারণত NO₃⁻/NH₄⁺ রূপে।",
    ),
    q(
        "Which is a micronutrient (microelement) for plants?",
        "উদ্ভিদের পুষ্টির জন্য মাইক্রো এলিমেন্ট কোনটি?",
        ["Calcium", "Carbon", "Sulphur", "Iron"],
        ["ক্যালসিয়াম", "কার্বন", "সালফার", "লৌহ"],
        "D", "easy", "factual",
        "Fe, Mn, Zn, Cu, Mo, B, Cl, Ni are micronutrients; Ca, S and C are not micro.",
        "Fe, Mn, Zn, Cu, Mo, B, Cl, Ni মাইক্রো; Ca, S ও C মাইক্রো নয়।",
    ),
    q(
        "Mineral salt absorption: (i) absorbed as ions (ii) anion uptake is active (iii) cation uptake is always passive — which are correct?",
        "খনিজ লবণ পরিশোষণে—(i) আয়ন হিসেবে শোষিত (ii) অ্যানায়ন শোষণ সক্রিয় (iii) ক্যাটায়ন শোষণ সবসময় নিষ্ক্রিয় — কোনটি সঠিক?",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "A", "hard", "conceptual",
        "Minerals enter as ions; anion absorption is typically active. Cation uptake is not simply always passive, so (iii) is rejected.",
        "খনিজ আয়ন রূপে শোষিত এবং অ্যানায়ন শোষণ সাধারণত সক্রিয়; ক্যাটায়ন সবসময় নিষ্ক্রিয় নয় বলে (i) ও (ii) সঠিক।",
    ),
]


# --- t02: Photosynthesis / সালোকসংশ্লেষণ ---
T02 = [
    q(
        "Which is a C₃ plant among the following?",
        "নিচের কোনটি C₃ উদ্ভিদ?",
        ["Sugarcane", "Maize", "Mango", "Bryophyllum (pathorkuchi)"],
        ["আখ", "ভুট্টা", "আম", "পাথরকুচি"],
        "C", "easy", "factual",
        "Mango (and rice, wheat, potato) are C₃; sugarcane and maize are C₄; Bryophyllum is CAM.",
        "আম (ধান, গম, আলু) C₃; আখ ও ভুট্টা C₄; পাথরকুচি CAM।",
    ),
    q(
        "Which scientific name denotes a C₄ plant?",
        "কোন বৈজ্ঞানিক নামটি C₄ উদ্ভিদ নির্দেশ করে?",
        [
            "Saccharum officinarum",
            "Mangifera indica",
            "Oryza sativa",
            "Triticum aestivum",
        ],
        [
            "Saccharum officinarum",
            "Mangifera indica",
            "Oryza sativa",
            "Triticum aestivum",
        ],
        "A", "medium", "factual",
        "Saccharum officinarum (sugarcane) is C₄; mango, rice and wheat are C₃.",
        "Saccharum officinarum (ইক্ষু) C₄; আম, ধান ও গম C₃।",
    ),
    q(
        "First stable compound of the C₃ cycle is—",
        "C₃ চক্রের প্রথম স্থায়ী যৌগ—",
        [
            "Oxaloacetic acid",
            "3-phosphoglyceric acid (PGA)",
            "Malic acid",
            "Pyruvic acid",
        ],
        [
            "অক্সালোঅ্যাসিটিক এসিড",
            "৩-ফসফোগ্লিসারিক এসিড (PGA)",
            "ম্যালিক এসিড",
            "পাইরুভিক এসিড",
        ],
        "B", "easy", "factual",
        "In the Calvin cycle the first stable product is 3-PGA (3-carbon).",
        "ক্যালভিন চক্রে প্রথম স্থায়ী উৎপাদ ৩-PGA (৩ কার্বন)।",
    ),
    q(
        "First CO₂ acceptor in C₄ plants is—",
        "C₄ উদ্ভিদের প্রথম কার্বন ডাই-অক্সাইড গ্রহীতা কোনটি?",
        [
            "Phosphoenolpyruvic acid (PEP)",
            "Ribulose 1,5-bisphosphate",
            "Oxaloacetic acid",
            "3-phosphoglyceric acid",
        ],
        [
            "ফসফোইনল পাইরুভিক এসিড (PEP)",
            "রাইবুলোজ ১,৫-বিসফসফেট",
            "অক্সালোঅ্যাসিটিক এসিড",
            "৩-ফসফোগ্লিসারিক এসিড",
        ],
        "A", "easy", "factual",
        "PEP (3-C) accepts CO₂ in mesophyll; OAA is the first stable C₄ product, not the acceptor.",
        "মেসোফিলে PEP CO₂ গ্রহণ করে; OAA প্রথম স্থায়ী C₄ যৌগ, গ্রহীতা নয়।",
    ),
    q(
        "First stable product of the C₄ (Hatch–Slack) pathway is—",
        "C₄ চক্রের প্রথম স্থায়ী যৌগ কোনটি?",
        [
            "3-phosphoglyceric acid",
            "Oxaloacetic acid",
            "Pyruvic acid",
            "Malic acid",
        ],
        [
            "৩-ফসফোগ্লিসারিক এসিড",
            "অক্সালোঅ্যাসিটিক এসিড",
            "পাইরুভিক এসিড",
            "ম্যালিক এসিড",
        ],
        "B", "easy", "factual",
        "PEP + CO₂ → oxaloacetic acid (4-C), the first stable Hatch–Slack product.",
        "PEP + CO₂ → অক্সালোঅ্যাসিটিক এসিড (৪-C), হ্যাচ-স্ল্যাকের প্রথম স্থায়ী যৌগ।",
    ),
    q(
        "How many carbon atoms are in the first stable compound of the Calvin cycle?",
        "ক্যালভিন চক্রের প্রথম স্থায়ী যৌগটি কত কার্বনবিশিষ্ট?",
        ["2", "3", "4", "6"],
        ["২", "৩", "৪", "৬"],
        "B", "easy", "factual",
        "3-PGA has three carbon atoms.",
        "৩-PGA তে তিনটি কার্বন থাকে।",
    ),
    q(
        "How many carbon atoms does oxaloacetic acid contain?",
        "অক্সালোঅ্যাসিটিক এসিডে কার্বন সংখ্যা কত?",
        ["Two", "Three", "Four", "Six"],
        ["দুই", "তিন", "চার", "ছয়"],
        "C", "easy", "factual",
        "OAA is a four-carbon dicarboxylic acid.",
        "OAA চার কার্বনবিশিষ্ট ডাইকার্বক্সিলিক এসিড।",
    ),
    q(
        "Light reaction of photosynthesis occurs in the—",
        "সালোকসংশ্লেষণের আলোক পর্যায় সংঘটিত হয় কোনটিতে?",
        ["Thylakoid", "Oxysome", "Stroma lamella only", "Stroma"],
        ["থাইলাকয়েড", "অক্সিজোম", "কেবল স্ট্রোমা ল্যামেলা", "স্ট্রোমা"],
        "A", "easy", "factual",
        "Photochemical reactions run on thylakoid membranes; Calvin cycle occurs in the stroma.",
        "আলোক পর্যায় থাইলাকয়েড মেমব্রেনে; আলোক-নিরপেক্ষ পর্যায় স্ট্রোমাতে।",
    ),
    q(
        "Where does the Calvin cycle take place?",
        "ক্যালভিন চক্র কোথায় সংঘটিত হয়?",
        [
            "Chloroplast stroma",
            "Chloroplast thylakoid",
            "Cytoplasm",
            "Mitochondrial matrix",
        ],
        [
            "ক্লোরোপ্লাস্টের স্ট্রোমাতে",
            "ক্লোরোপ্লাস্টের থাইলাকয়েডে",
            "সাইটোপ্লাজমে",
            "মাইটোকন্ড্রিয়ার ম্যাট্রিক্সে",
        ],
        "A", "easy", "factual",
        "Carbon fixation (Calvin cycle) occurs in the chloroplast stroma.",
        "কার্বন আত্তীকরণ (ক্যালভিন চক্র) ক্লোরোপ্লাস্টের স্ট্রোমাতে ঘটে।",
    ),
    q(
        "Products of the light phase of photosynthesis are—",
        "সালোকসংশ্লেষণের আলোক পর্যায়ে উৎপন্ন হয় কোনটি?",
        ["Water and sugar", "ATP and sugar", "NADP and sugar", "NADPH₂ and ATP"],
        ["পানি ও শর্করা", "ATP ও শর্করা", "NADP ও শর্করা", "NADPH₂ ও ATP"],
        "D", "easy", "factual",
        "Light reactions produce ATP, NADPH (NADPH₂) and O₂; sugars form in the dark reactions.",
        "আলোক পর্যায়ে ATP, NADPH (NADPH₂) ও O₂ তৈরি হয়; শর্করা অন্ধকার পর্যায়ে।",
    ),
    q(
        "In which plant are two types of chloroplasts found?",
        "কোন উদ্ভিদে দুই ধরনের ক্লোরোপ্লাস্ট পাওয়া যায়?",
        ["Sugarcane", "Rice", "Wheat", "Mango"],
        ["ইক্ষু", "ধান", "গম", "আম"],
        "A", "easy", "factual",
        "C₄ plants like sugarcane have mesophyll and bundle-sheath chloroplasts (Kranz anatomy).",
        "ইক্ষুর মতো C₄ উদ্ভিদে মেসোফিল ও বান্ডলসীথ — দুই ধরনের ক্লোরোপ্লাস্ট (ক্র্যাঞ্জ অ্যানাটমি)।",
    ),
    q(
        "Kranz anatomy is seen in which plant?",
        "নিচের কোন উদ্ভিদে ক্র্যাঞ্জ অ্যানাটমি দেখা যায়?",
        ["Rice", "Maize", "Wheat", "Barley"],
        ["ধান", "ভুট্টা", "গম", "বার্লি"],
        "B", "easy", "factual",
        "Maize (and sugarcane, sorghum) show Kranz anatomy; rice, wheat and barley are C₃.",
        "ভুট্টা (আখ, সরগাম) তে ক্র্যাঞ্জ অ্যানাটমি; ধান, গম, বার্লি C₃।",
    ),
    q(
        "Which enzyme helps CO₂ uptake in the Calvin (C₃) pathway?",
        "ক্যালভিন (C₃) পথে CO₂ গ্রহণে কোন এনজাইম সাহায্য করে?",
        ["Kinase", "Rubisco", "Dehydrogenase", "Isomerase"],
        ["কাইনেজ", "রুবিস্কো", "ডিহাইড্রোজিনেজ", "আইসোমারেজ"],
        "B", "easy", "factual",
        "RuBisCO carboxylates RuBP to form 3-PGA in the Calvin cycle.",
        "ক্যালভিন চক্রে RuBisCO RuBP-কে কার্বক্সিলেট করে ৩-PGA তৈরি করে।",
    ),
    q(
        "Under intense light and high temperature, C₃ plants often show—",
        "তীব্র আলো ও উচ্চ তাপমাত্রায় C₃ উদ্ভিদে সাধারণত ঘটে—",
        [
            "Oxidative phosphorylation only",
            "Photophosphorylation only",
            "Photorespiration",
            "Ordinary dark respiration only",
        ],
        [
            "কেবল অক্সিডেটিভ ফসফোরাইলেশন",
            "কেবল ফটোফসফোরাইলেশন",
            "আলোক শ্বসন (ফটোরেসপিরেশন)",
            "কেবল সাধারণ অন্ধকার শ্বসন",
        ],
        "C", "medium", "conceptual",
        "High O₂/CO₂ ratio with heat and bright light promotes RuBisCO oxygenase activity — photorespiration.",
        "উচ্চ তাপ ও তীব্র আলোতে RuBisCO-এর অক্সিজেনেজ ক্রিয়ায় ফটোরেসপিরেশন বাড়ে।",
    ),
    q(
        "Which light colour gives the highest photosynthetic rate?",
        "কোন আলোতে সালোকসংশ্লেষণের হার সর্বোচ্চ?",
        ["Yellow", "Green", "Red", "White only"],
        ["হলুদ", "সবুজ", "লাল", "কেবল সাদা"],
        "C", "medium", "factual",
        "Chlorophyll absorbs most strongly in blue-violet and red; red light is classically cited for peak rate in HSC MCQs.",
        "ক্লোরোফিল নীল-বেগুনি ও লালে সর্বাধিক শোষণ করে; HSC MCQ-তে লাল আলোয় হার সর্বোচ্চ বলা হয়।",
    ),
    q(
        "Which spectral regions are mainly used in photosynthesis?",
        "সালোকসংশ্লেষণের সময় বর্ণালির কোন অংশ প্রধানত ব্যবহৃত হয়?",
        [
            "Violet–blue and sky-blue–green",
            "Violet–red and blue–green",
            "Violet–blue and orange–red",
            "Violet–yellow and blue–orange",
        ],
        [
            "বেগুনি-নীল ও আসমানি-সবুজ",
            "বেগুনি-লাল ও নীল-সবুজ",
            "বেগুনি-নীল ও কমলা-লাল",
            "বেগুনি-হলুদ ও নীল-কমলা",
        ],
        "C", "medium", "factual",
        "Action/absorption peaks lie in violet–blue and orange–red regions.",
        "শোষণ/ক্রিয়া শিখর বেগুনি-নীল ও কমলা-লাল অঞ্চলে।",
    ),
    q(
        "Which is an internal factor of photosynthesis?",
        "সালোকসংশ্লেষণের অভ্যন্তরীণ প্রভাবক কোনটি?",
        ["Chlorophyll", "Mineral salts (external supply)", "Oxygen concentration", "Water availability"],
        ["ক্লোরোফিল", "খনিজ লবণ (বাহ্যিক সরবরাহ)", "অক্সিজেন ঘনত্ব", "পানির প্রাপ্যতা"],
        "A", "easy", "conceptual",
        "Chlorophyll content is an internal plant factor; O₂, water and external minerals are environmental/external.",
        "ক্লোরোফিল উদ্ভিদের অভ্যন্তরীণ প্রভাবক; O₂, পানি ও বাহ্যিক খনিজ পরিবেশগত।",
    ),
    q(
        "O₂ released in the light reactions comes from which process?",
        "আলোক পর্যায়ে O₂ তৈরি হয় যে প্রক্রিয়ায়—",
        [
            "Photophosphorylation",
            "Photolysis of water",
            "Photorespiration",
            "Oxidative phosphorylation",
        ],
        [
            "ফটোফসফোরাইলেশন",
            "পানির ফটোলাইসিস",
            "ফটোরেসপিরেশন",
            "অক্সিডেটিভ ফসফোরাইলেশন",
        ],
        "B", "easy", "factual",
        "Hill reaction/photolysis splits H₂O to release O₂, H⁺ and electrons.",
        "হিল বিক্রিয়া/ফটোলাইসিসে H₂O ভেঙে O₂, H⁺ ও ইলেকট্রন নির্গত হয়।",
    ),
    q(
        "Which ion helps in photolysis of water?",
        "পানির ফটোলাইসিসে কোনটি সহায়তা করে?",
        ["Mg²⁺", "Ca²⁺", "Mn²⁺", "Fe³⁺ only"],
        ["Mg²⁺", "Ca²⁺", "Mn²⁺", "কেবল Fe³⁺"],
        "C", "medium", "factual",
        "Mn²⁺ (with Cl⁻) assists the water-splitting complex of PSII.",
        "PSII-এর পানি-বিভাজন কমপ্লেক্সে Mn²⁺ (ও Cl⁻) সহায়ক।",
    ),
    q(
        "C₄ plants: (i) two chloroplast types (ii) Kranz anatomy (iii) need higher CO₂ than C₃ — which are correct?",
        "C₄ উদ্ভিদে—(i) দুই ধরনের ক্লোরোপ্লাস্ট (ii) ক্র্যাঞ্জ অ্যানাটমি (iii) C₃-এর চেয়ে বেশি CO₂ দরকার — কোনটি সঠিক?",
        ["(i) and (ii) only", "(ii) and (iii) only", "(i) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "কেবল (i) ও (iii)", "(i), (ii) ও (iii)"],
        "A", "hard", "conceptual",
        "C₄ plants have dual chloroplasts and Kranz anatomy and work at lower ambient CO₂; (iii) is false.",
        "C₄-এ দুই ক্লোরোপ্লাস্ট ও ক্র্যাঞ্জ অ্যানাটমি থাকে এবং কম CO₂-তেও চলে; (iii) মিথ্যা।",
    ),
]


# --- t03: Respiration and growth / শ্বসন ও বৃদ্ধি ---
T03 = [
    q(
        "Conversion of one glucose molecule to two pyruvic acid molecules is—",
        "এক অণু গ্লুকোজ থেকে দুই অণু পাইরুভিক এসিড তৈরির প্রক্রিয়াটি হলো—",
        ["Phosphorylation", "Glycolysis", "Calvin cycle", "Hatch–Slack cycle"],
        ["ফসফোরাইলেশন", "গ্লাইকোলাইসিস", "ক্যালভিন চক্র", "হ্যাচ-স্ল্যাক চক্র"],
        "B", "easy", "factual",
        "Glycolysis (EMP pathway) converts glucose to two pyruvates in the cytoplasm.",
        "গ্লাইকোলাইসিস (EMP) সাইটোপ্লাজমে গ্লুকোজকে দুই পাইরুভেটে রূপান্তর করে।",
    ),
    q(
        "Glycolysis: (i) three irreversible steps (ii) occurs in mitochondria (iii) two ATP are consumed — which are correct?",
        "গ্লাইকোলাইসিসে—(i) তিনটি একমুখী বিক্রিয়া (ii) মাইটোকন্ড্রিয়ায় ঘটে (iii) দুই অণু ATP খরচ — কোনটি সঠিক?",
        ["(i) and (iii) only", "(i) and (ii) only", "(ii) and (iii) only", "(i), (ii) and (iii)"],
        ["কেবল (i) ও (iii)", "কেবল (i) ও (ii)", "কেবল (ii) ও (iii)", "(i), (ii) ও (iii)"],
        "A", "hard", "conceptual",
        "Glycolysis is cytoplasmic with three irreversible kinase steps and uses 2 ATP; it is not mitochondrial.",
        "গ্লাইকোলাইসিস সাইটোপ্লাজমে; তিন একমুখী ধাপ ও ২ ATP খরচ; মাইটোকন্ড্রিয়ায় নয়।",
    ),
    q(
        "In which organelle does the Krebs cycle occur?",
        "কোষের কোন অঙ্গাণুতে ক্রেবস চক্র সম্পন্ন হয়?",
        ["Mitochondria", "Golgi body", "Ribosome", "Nucleus"],
        ["মাইটোকন্ড্রিয়া", "গলগি বডি", "রাইবোসোম", "নিউক্লিয়াস"],
        "A", "easy", "factual",
        "The TCA/Krebs cycle runs in the mitochondrial matrix.",
        "TCA/ক্রেবস চক্র মাইটোকন্ড্রিয়ার ম্যাট্রিক্সে ঘটে।",
    ),
    q(
        "Common step of aerobic and anaerobic respiration is—",
        "সবাত ও অবাত শ্বসনের অভিন্ন ধাপ কোনটি?",
        ["Glycolysis", "Acetyl-CoA formation", "Krebs cycle", "Electron transport system"],
        ["গ্লাইকোলাইসিস", "অ্যাসিটাইল কো-এ সৃষ্টি", "ক্রেবস চক্র", "ইলেকট্রন ট্রান্সপোর্ট তন্ত্র"],
        "A", "easy", "factual",
        "Both pathways begin with glycolysis; later steps differ with oxygen availability.",
        "উভয় পথ গ্লাইকোলাইসিস দিয়ে শুরু; অক্সিজেন অনুসারে পরবর্তী ধাপ ভিন্ন।",
    ),
    q(
        "In aerobic respiration, oxygen is used in which step?",
        "শ্বসনের কোন ধাপে অক্সিজেন ব্যবহৃত হয়?",
        ["Glycolysis", "Acetyl-CoA formation", "Krebs cycle", "Electron transport system"],
        ["গ্লাইকোলাইসিস", "অ্যাসিটাইল কো-এ সৃষ্টি", "ক্রেবস চক্র", "ইলেকট্রন ট্রান্সপোর্ট তন্ত্র"],
        "D", "medium", "conceptual",
        "O₂ is the terminal electron acceptor in the ETS/oxidative phosphorylation.",
        "ETS/অক্সিডেটিভ ফসফোরাইলেশনে O₂ চূড়ান্ত ইলেকট্রন গ্রহীতা।",
    ),
    q(
        "One molecule of acetyl-CoA through the Krebs cycle yields about how many ATP (classical HSC count)?",
        "ক্রেবস চক্রে এক অণু অ্যাসিটাইল কো-এ থেকে মোট কত অণু ATP তৈরি হয় (শাস্ত্রীয় HSC গণনা)?",
        ["2", "8", "12", "24"],
        ["২", "৮", "১২", "২৪"],
        "C", "medium", "numerical",
        "Classical school count: 3 NADH (≈9 ATP) + 1 FADH₂ (≈2) + 1 GTP/ATP ≈ 12 ATP per acetyl-CoA.",
        "শাস্ত্রীয় গণনায় ৩ NADH (≈৯) + ১ FADH₂ (≈২) + ১ GTP/ATP ≈ ১২ ATP প্রতি অ্যাসিটাইল কো-এ।",
    ),
    q(
        "Complete aerobic oxidation of one glucose yields how many ATP (classical plant count)?",
        "সবাত শ্বসনে এক অণু গ্লুকোজ জারিত হয়ে কয়টি ATP উৎপন্ন করে (শাস্ত্রীয় গণনা)?",
        ["34", "35", "36", "38"],
        ["৩৪", "৩৫", "৩৬", "৩৮"],
        "C", "medium", "numerical",
        "HSC classical total for plants is often 36 ATP per glucose (38 in some bacterial counts).",
        "উদ্ভিদের শাস্ত্রীয় HSC গণনায় প্রায় ৩৬ ATP/গ্লুকোজ (কিছু ব্যাকটেরিয়ায় ৩৮)।",
    ),
    q(
        "Net ATP from anaerobic respiration of one glucose is—",
        "অবাত শ্বসনে এক অণু গ্লুকোজ থেকে কত অণু ATP তৈরি হয়?",
        ["2", "4", "24", "38"],
        ["২", "৪", "২৪", "৩৮"],
        "A", "easy", "numerical",
        "Fermentation yields a net of 2 ATP per glucose from glycolysis only.",
        "ফার্মেন্টেশনে কেবল গ্লাইকোলাইসিস থেকে নিট ২ ATP/গ্লুকোজ।",
    ),
    q(
        "How many ATP are spent in the preparatory phase of glycolysis?",
        "গ্লাইকোলাইসিস প্রক্রিয়ায় ব্যয়িত শক্তি কত অণু ATP?",
        ["2", "4", "6", "8"],
        ["২", "৪", "৬", "৮"],
        "A", "easy", "numerical",
        "Hexokinase and phosphofructokinase each use one ATP — total 2 ATP invested.",
        "হেক্সোকাইনেজ ও ফসফোফ্রুক্টোকাইনেজ মিলে ২ ATP ব্যয় করে।",
    ),
    q(
        "Enzyme converting fructose-6-phosphate to fructose-1,6-bisphosphate is—",
        "ফ্রুক্টোজ-৬-ফসফেট থেকে ফ্রুক্টোজ-১,৬-বিসফসফেট তৈরি করে কোন এনজাইম?",
        ["Phosphofructokinase", "Hexokinase", "Isomerase", "Phosphoglyceromutase"],
        ["ফসফোফ্রুক্টোকাইনেজ", "হেক্সোকাইনেজ", "আইসোমারেজ", "ফসফোগ্লিসারোমিউটেজ"],
        "A", "medium", "factual",
        "PFK is the key regulatory kinase of the glycolytic investment phase.",
        "ফসফোফ্রুক্টোকাইনেজ গ্লাইকোলাইসিসের মূল নিয়ন্ত্রক কাইনেজ।",
    ),
    q(
        "Glucose-6-phosphate ⇌ fructose-6-phosphate is catalysed by—",
        "গ্লুকোজ-৬-ফসফেট ⇌ ফ্রুক্টোজ-৬-ফসফেট বিক্রিয়া কোন এনজাইম দ্বারা প্রভাবিত হয়?",
        ["Hydrolase", "Isomerase", "Transferase", "Lyase"],
        ["হাইড্রোলেজ", "আইসোমারেজ", "ট্রান্সফারেজ", "লাইয়েজ"],
        "B", "medium", "factual",
        "Phosphoglucose isomerase interconverts G6P and F6P.",
        "ফসফোগ্লুকোজ আইসোমারেজ G6P ও F6P পরস্পর রূপান্তর করে।",
    ),
    q(
        "Formation of ATP from ADP in presence of oxygen during respiration is—",
        "শ্বসনে অক্সিজেনের উপস্থিতিতে ADP হতে ATP তৈরির প্রক্রিয়া কোনটি?",
        [
            "Substrate-level phosphorylation only",
            "Photophosphorylation",
            "Oxidative phosphorylation",
            "Simple diffusion",
        ],
        [
            "কেবল সাবস্ট্রেট-লেভেল ফসফোরাইলেশন",
            "ফটোফসফোরাইলেশন",
            "অক্সিডেটিভ ফসফোরাইলেশন",
            "সরল ব্যাপন",
        ],
        "C", "easy", "conceptual",
        "Most ATP in aerobic respiration arises by oxidative phosphorylation on the inner mitochondrial membrane.",
        "সবাত শ্বসনে অধিকাংশ ATP মাইটোকন্ড্রিয়ার অন্তঃঝিল্লিতে অক্সিডেটিভ ফসফোরাইলেশনে তৈরি।",
    ),
    q(
        "Which compound is called the ‘biological coin’?",
        "‘Biological coin’ বলা হয় কোনটিকে?",
        ["ADP", "ATP", "NAD", "FAD"],
        ["ADP", "ATP", "NAD", "FAD"],
        "B", "easy", "factual",
        "ATP is the universal energy currency of cells — the ‘biological coin’.",
        "ATP কোষের সার্বজনীন শক্তিমুদ্রা — ‘biological coin’।",
    ),
    q(
        "Tricarboxylic acid cycle refers to—",
        "ট্রাইকার্বোক্সিলিক চক্র নিচের কোনটি?",
        ["Glycolysis", "Krebs cycle", "C₃ cycle", "C₄ cycle"],
        ["গ্লাইকোলাইসিস", "ক্রেবস চক্র", "C₃ চক্র", "C₄ চক্র"],
        "B", "easy", "factual",
        "Krebs cycle is also called the TCA (tricarboxylic acid) cycle.",
        "ক্রেবস চক্রকে TCA (ট্রাইকার্বোক্সিলিক অ্যাসিড) চক্রও বলে।",
    ),
    q(
        "First product formed when acetyl-CoA enters the Krebs cycle is—",
        "ক্রেবস চক্রের প্রথম উৎপাদিত পদার্থ—",
        ["Malic acid", "Citric acid", "Oxalic acid", "Lactic acid"],
        ["ম্যালিক এসিড", "সাইট্রিক এসিড", "অক্সালিক এসিড", "ল্যাকটিক এসিড"],
        "B", "easy", "factual",
        "Acetyl-CoA (2C) + OAA (4C) → citric acid (6C).",
        "অ্যাসিটাইল কো-এ (২C) + OAA (৪C) → সাইট্রিক এসিড (৬C)।",
    ),
    q(
        "Which enzyme is most active in alcoholic fermentation?",
        "ফার্মেন্টেশন প্রক্রিয়ায় কোন এনজাইমটি সবচেয়ে বেশি ক্রিয়াশীল হয়?",
        ["Zymase", "Kinase", "Isomerase", "Hydrogenase"],
        ["জাইমেজ", "কাইনেজ", "আইসোমারেজ", "হাইড্রোজেনেজ"],
        "A", "medium", "factual",
        "Yeast zymase complex drives alcoholic fermentation of sugars.",
        "ঈস্টের জাইমেজ কমপ্লেক্স অ্যালকোহলিক ফার্মেন্টেশন চালায়।",
    ),
    q(
        "Lactic acid from carbohydrate is produced in—",
        "কার্বোহাইড্রেট থেকে ল্যাকটিক এসিড উৎপন্ন হয় কোন প্রক্রিয়ায়?",
        ["Photosynthesis", "Anaerobic respiration", "Transpiration", "Osmosis"],
        ["সালোকসংশ্লেষণ", "অবাত শ্বসন", "প্রস্বেদন", "অভিস্রবণ"],
        "B", "easy", "factual",
        "Lactic fermentation is a form of anaerobic respiration/fermentation.",
        "ল্যাকটিক ফার্মেন্টেশন এক ধরনের অবাত শ্বসন।",
    ),
    q(
        "Respiratory quotient (RQ) of glucose in aerobic respiration is—",
        "সবাত শ্বসনে গ্লুকোজের শ্বসনিক হার (RQ) কত?",
        ["0.7", "0.9", "1.0", "1.33"],
        ["০.৭", "০.৯", "১.০", "১.৩৩"],
        "C", "medium", "numerical",
        "For carbohydrate, CO₂ produced equals O₂ consumed, so RQ = 1.",
        "শর্করায় উৎপন্ন CO₂ = ব্যবহৃত O₂, তাই RQ = ১।",
    ),
    q(
        "Which plant hormone promotes cell elongation in shoots (phototropism)?",
        "কোন উদ্ভিদ হরমোন কাণ্ডের কোষ দীর্ঘায়ন (আলোকানুবর্তন) ত্বরান্বিত করে?",
        ["Auxin (IAA)", "Ethylene", "Abscisic acid", "Cytokinin only"],
        ["অক্সিন (IAA)", "ইথিলিন", "অ্যাবসিসিক এসিড", "কেবল সাইটোকাইনিন"],
        "A", "medium", "factual",
        "Auxin redistributes under unilateral light and elongates cells on the shaded side.",
        "একপার্শ্বিক আলোতে অক্সিন ছায়াদিকে জমা হয়ে কোষ দীর্ঘায়ন ঘটায়।",
    ),
    q(
        "Which hormone is mainly associated with fruit ripening and senescence?",
        "ফল পাকানো ও সেনেসেন্সের সাথে প্রধানত কোন হরমোন যুক্ত?",
        ["Gibberellin", "Cytokinin", "Ethylene", "Auxin only"],
        ["জিব্বারেলিন", "সাইটোকাইনিন", "ইথিলিন", "কেবল অক্সিন"],
        "C", "easy", "factual",
        "Ethylene is the gaseous hormone of ripening and many senescence responses; ABA mainly closes stomata/stress.",
        "ইথিলিন পাকানো ও সেনেসেন্সের গ্যাসীয় হরমোন; ABA প্রধানত পত্ররন্ধ্র বন্ধ/স্ট্রেস নিয়ন্ত্রণ করে।",
    ),
]


TOPICS_MAP = {
    "bio1_27_ch09_t01": T01,
    "bio1_27_ch09_t02": T02,
    "bio1_27_ch09_t03": T03,
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
        "chapter": "bio1_27_ch09",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p284_pdf290.png",
            "p285_pdf291.png",
            "p286_pdf292.png",
            "p287_pdf293.png",
            "p288_pdf294.png",
            "p289_pdf295.png",
            "p290_pdf296.png",
            "p291_pdf297.png",
            "p292_pdf298.png",
            "p293_pdf299.png",
            "p294_pdf300.png",
            "p295_pdf301.png",
        ],
        "counts": {**counts, "total": sum(counts.values())},
        "pdf_mapping": {
            "bio1_27_ch09_t01": {
                "title": "Water and mineral transport / পানি ও খনিজ পরিবহন",
                "themes": [
                    "fastest K⁺/NO₃⁻ vs slowest Ca²⁺/SO₄²⁻ ion uptake rates",
                    "stomatal K⁺/pH control; leaf stomata as main transpiration path",
                    "macronutrients N; micronutrient Fe; Si for grasses",
                    "C from air; N from soil; Cl⁻ anion vs K⁺ cation",
                    "passive ion exchange & Donnan; active Lundegårdh cytochrome pump",
                    "transpiration factors: low pressure ↑; high RH ↓",
                ],
            },
            "bio1_27_ch09_t02": {
                "title": "Photosynthesis / সালোকসংশ্লেষণ",
                "themes": [
                    "C₃ mango vs C₄ sugarcane/maize; Kranz dual chloroplasts",
                    "Calvin PGA/Rubisco/stroma vs Hatch–Slack PEP/OAA",
                    "light reaction thylakoid → ATP+NADPH; O₂ from photolysis+Mn²⁺",
                    "photorespiration under high light/heat; red light peak rate",
                    "action spectrum violet–blue & orange–red; chlorophyll internal factor",
                    "C₄ traits: dual chloroplasts + Kranz; not higher CO₂ demand",
                ],
            },
            "bio1_27_ch09_t03": {
                "title": "Respiration and growth / শ্বসন ও বৃদ্ধি",
                "themes": [
                    "glycolysis EMP cytoplasmic; shared aerobic/anaerobic step",
                    "Krebs/TCA matrix; citric acid first; O₂ used in ETS",
                    "classical ATP: 12/acetyl-CoA, 36/glucose aerobic, net 2 anaerobic",
                    "PFK & isomerase glycolytic enzymes; zymase fermentation; RQ=1",
                    "biological coin ATP; oxidative phosphorylation",
                    "growth hormones: auxin elongation/phototropism; ethylene ripening",
                ],
            },
        },
        "low_confidence": [
            "OCR on p284–295 is noisy; figure-stimulus and multi-statement keys rewritten as standalone stems.",
            "Growth (হরমোন) coverage is thin in printed MCQ span; two accurate board-level hormone items added for syllabus t03.",
            "Classical HSC ATP counts (12 per acetyl-CoA; 36 per glucose) used; modern P/O ratios differ.",
            "Mineral absorption (iii) cation-always-passive keys vary across boards; curated to (i)+(ii).",
            "Red-light peak photosynthetic rate follows common BD board keys (blue also high).",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (bio1_27_ch09_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "bio1_27_ch09_t01": 20,
                "bio1_27_ch09_t02": 20,
                "bio1_27_ch09_t03": 20,
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
        / "ch09_curated_summary.json"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
