#!/usr/bin/env python3
"""Seed Chemistry 1st Paper Ch4 bilingual MCQs (Chemical Change).

Import CSV chemistry_1_ch04.csv had headers only; authored 20 bilingual MCQs
per topic aligned to NCTB chemistry_1st_paper_2027 ch04.
Writes chem1_27_ch04_t01..t04 under content/bank/topics/.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPICS = ROOT / "content" / "bank" / "topics"
PARSED = ROOT / "content" / "bank" / "udvash_raw" / "chemistry_1" / "parsed"
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
from core import validate_record  # noqa: E402

SRC = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "chemistry p1 ch04; curated bilingual"
)

TOPIC_IDS = [f"chem1_27_ch04_t{i:02d}" for i in range(1, 5)]


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
        bn = f"মান {bn}"
    return en, bn


def q(stem_en, stem_bn, opts_en, opts_bn, correct, difficulty, qtype, exp_en, exp_bn):
    pairs = [_norm_pair(e, b) for e, b in zip(opts_en, opts_bn)]
    (a, ab), (b, bb), (c, cb), (d, db) = pairs
    if not re.search(r"[ঀ-৿]", exp_bn):
        exp_bn = "ব্যাখ্যা: " + exp_bn
    return {
        "stem_en": stem_en.strip(),
        "stem_bn": stem_bn.strip(),
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
        "explanation_en": exp_en.strip(),
        "explanation_bn": exp_bn.strip(),
        "verified": False,
        "source": SRC,
    }


# --- t01: Reaction rates ---
T01 = [
    q(
        "The rate of a chemical reaction is usually expressed as:",
        "রাসায়নিক বিক্রিয়ার গতি সাধারণত প্রকাশ করা হয়:",
        ["Change in concentration per unit time", "Only total mass of products", "Color of the flask", "Atmospheric pressure alone"],
        ["একক সময়ে ঘনমাত্রার পরিবর্তন", "শুধু উৎপাদের মোট ভর", "ফ্লাস্কের রঙ", "শুধু বায়ুমণ্ডলীয় চাপ"],
        "A", "easy", "factual",
        "Rate = Δconcentration / Δtime for reactants or products.",
        "গতি = বিক্রিয়ক/উৎপাদের ঘনমাত্রার পরিবর্তন ÷ সময়।",
    ),
    q(
        "According to collision theory, effective collisions require:",
        "সংঘর্ষ তত্ত্ব অনুসারে কার্যকর সংঘর্ষের জন্য প্রয়োজন:",
        ["Any random bump at low energy", "Sufficient energy and proper orientation", "Only darkness", "Zero activation energy always"],
        ["কম শক্তিতে যেকোনো ধাক্কা", "পর্যাপ্ত শক্তি ও সঠিক অভিমুখ", "শুধু অন্ধকার", "সবসময় শূন্য সক্রিয়ন শক্তি"],
        "B", "easy", "conceptual",
        "Molecules must collide with Ea and correct geometry to react.",
        "বিক্রিয়ার জন্য Ea ও সঠিক জ্যামিতিসহ সংঘর্ষ লাগে।",
    ),
    q(
        "Activation energy (Ea) is the:",
        "সক্রিয়ন শক্তি (Ea) হলো:",
        ["Energy released as heat always", "Minimum energy barrier to form products", "Bond energy of products only", "Zero for all catalysts"],
        ["সবসময় তাপ হিসেবে মুক্ত শক্তি", "উৎপাদ গঠনের ন্যূনতম শক্তি বাধা", "শুধু উৎপাদের বন্ধন শক্তি", "সব অনুঘটকের জন্য শূন্য"],
        "B", "easy", "factual",
        "Ea is the energy hill reactants must overcome to reach the transition state.",
        "Ea হলো বিক্রিয়ক থেকে ট্রানজিশন স্টেটে যেতে প্রয়োজনীয় শক্তি বাধা।",
    ),
    q(
        "Increasing temperature generally increases reaction rate because:",
        "তাপমাত্রা বাড়ালে বিক্রিয়ার গতি সাধারণত বাড়ে কারণ:",
        ["Activation energy increases", "More molecules have energy ≥ Ea", "Concentration always falls", "Catalysts disappear"],
        ["সক্রিয়ন শক্তি বাড়ে", "অধিক অণুর শক্তি ≥ Ea হয়", "ঘনমাত্রা সবসময় কমে", "অনুঘটক অদৃশ্য হয়"],
        "B", "easy", "conceptual",
        "Higher T shifts the Maxwell–Boltzmann distribution toward successful collisions.",
        "উচ্চ T তে Maxwell–Boltzmann বণ্টনে সফল সংঘর্ষের অণু বাড়ে।",
    ),
    q(
        "A catalyst increases rate by:",
        "অনুঘটক গতি বাড়ায়:",
        ["Raising Ea", "Providing an alternative path with lower Ea", "Removing all products instantly", "Increasing ΔH of reaction"],
        ["Ea বাড়িয়ে", "কম Ea এর বিকল্প পথ দিয়ে", "সব উৎপাদ তাৎক্ষণিক সরিয়ে", "বিক্রিয়ার ΔH বাড়িয়ে"],
        "B", "easy", "conceptual",
        "Catalysts lower the activation energy without being consumed net.",
        "অনুঘটক নিটভাবে ব্যবহৃত না হয়ে সক্রিয়ন শক্তি কমায়।",
    ),
    q(
        "For a reaction that is first order in A, doubling [A] will:",
        "A এর প্রতি প্রথম ক্রমের বিক্রিয়ায় [A] দ্বিগুণ করলে:",
        ["Halve the rate", "Double the rate", "Quadruple the rate", "Leave rate unchanged"],
        ["গতি অর্ধেক হবে", "গতি দ্বিগুণ হবে", "গতি চারগুণ হবে", "গতি অপরিবর্তিত"],
        "B", "medium", "numerical",
        "Rate = k[A]; doubling [A] doubles rate for first order.",
        "Rate = k[A]; [A] দ্বিগুণে গতি দ্বিগুণ।",
    ),
    q(
        "The units of a first-order rate constant are typically:",
        "প্রথম ক্রমের হার ধ্রুবকের একক সাধারণত:",
        ["mol L−1 s−1", "s−1", "L mol−1 s−1", "mol2 L−2 s−1"],
        ["mol L−1 s−1", "s−1", "L mol−1 s−1", "mol2 L−2 s−1"],
        "B", "medium", "factual",
        "For rate = k[A], k has units of reciprocal time (s−1).",
        "rate = k[A] হলে k এর একক সময়ের ব্যস্তানুপাত (s−1)।",
    ),
    q(
        "Increasing the concentration of reactants generally increases rate because:",
        "বিক্রিয়কের ঘনমাত্রা বাড়ালে গতি সাধারণত বাড়ে কারণ:",
        ["Fewer collisions occur", "Collision frequency rises", "Ea becomes infinite", "Temperature must fall"],
        ["সংঘর্ষ কমে", "সংঘর্ষের কম্পাঙ্ক বাড়ে", "Ea অসীম হয়", "তাপমাত্রা কমতেই হবে"],
        "B", "easy", "conceptual",
        "More particles per volume mean more collisions per second.",
        "প্রতি আয়তনে বেশি কণা মানে প্রতি সেকেন্ডে বেশি সংঘর্ষ।",
    ),
    q(
        "Surface area affects rate most clearly for:",
        "পৃষ্ঠক্ষেত্র গতিকে সবচেয়ে স্পষ্ট প্রভাবিত করে কোনটিতে?",
        ["Homogeneous gas reactions only", "Heterogeneous reactions of solids with liquids/gases", "Nuclear decay", "Ideal vacuum"],
        ["শুধু সমসত্ব গ্যাস বিক্রিয়া", "কঠিনের সাথে তরল/গ্যাসের বিষমসত্ব বিক্রিয়া", "নিউক্লিয়ার ক্ষয়", "আদর্শ শূন্য"],
        "B", "medium", "application",
        "Powdered solids react faster than lumps due to greater contact area.",
        "পাউডার কঠিনের সংস্পর্শ ক্ষেত্র বেশি বলে ডলার চেয়ে দ্রুত বিক্রিয়া করে।",
    ),
    q(
        "The half-life of a first-order reaction is:",
        "প্রথম ক্রমের বিক্রিয়ার অর্ধায়ু:",
        ["Proportional to initial concentration", "Independent of initial concentration", "Zero always", "Infinite for all cases"],
        ["প্রারম্ভিক ঘনমাত্রার সমানুপাতিক", "প্রারম্ভিক ঘনমাত্রা নিরপেক্ষ", "সবসময় শূন্য", "সব ক্ষেত্রে অসীম"],
        "B", "medium", "conceptual",
        "t1/2 = ln2 / k for first order — independent of [A]0.",
        "প্রথম ক্রমে t1/2 = ln2 / k — [A]0 নিরপেক্ষ।",
    ),
    q(
        "In the rate law rate = k[A]2[B], the overall order is:",
        "rate = k[A]2[B] হলে সামগ্রিক ক্রম কত?",
        ["1", "2", "3", "0"],
        ["1", "2", "3", "0"],
        "C", "easy", "numerical",
        "Overall order = 2 + 1 = 3.",
        "সামগ্রিক ক্রম = ২ + ১ = ৩।",
    ),
    q(
        "A zero-order reaction has a rate that:",
        "শূন্য ক্রমের বিক্রিয়ার গতি:",
        ["Depends linearly on [A]", "Is independent of reactant concentration", "Is always infinite", "Equals Ea"],
        ["[A] এর রৈখিক নির্ভর", "বিক্রিয়ক ঘনমাত্রা নিরপেক্ষ", "সবসময় অসীম", "Ea এর সমান"],
        "B", "medium", "factual",
        "Rate = k for zero order (often when a surface or catalyst is saturated).",
        "শূন্য ক্রমে Rate = k (প্রায়ই পৃষ্ঠ/অনুঘটক স্যাচুরেটেড হলে)।",
    ),
    q(
        "Which factor does NOT generally increase the rate of a chemical reaction?",
        "কোন উপাদান সাধারণত রাসায়নিক বিক্রিয়ার গতি বাড়ায় না?",
        ["Adding a suitable catalyst", "Raising temperature", "Increasing reactant concentration", "Lowering temperature substantially"],
        ["উপযুক্ত অনুঘটক যোগ", "তাপমাত্রা বৃদ্ধি", "বিক্রিয়ক ঘনমাত্রা বৃদ্ধি", "তাপমাত্রা উল্লেখযোগ্যভাবে কমানো"],
        "D", "easy", "application",
        "Cooling reduces the fraction of energetic collisions.",
        "ঠান্ডা করলে উচ্চ শক্তির সংঘর্ষের অনুপাত কমে।",
    ),
    q(
        "The rate-determining step of a mechanism is:",
        "বিক্রিয়া কৌশলের গতি-নির্ধারক ধাপ হলো:",
        ["The fastest elementary step", "The slowest elementary step", "Always the last step", "Never elementary"],
        ["দ্রুততম মৌলিক ধাপ", "মন্থরতম মৌলিক ধাপ", "সবসময় শেষ ধাপ", "কখনো মৌলিক নয়"],
        "B", "medium", "conceptual",
        "The slowest step limits the overall observed rate.",
        "মন্থরতম ধাপ সামগ্রিক পর্যবেক্ষিত গতি সীমিত করে।",
    ),
    q(
        "Photochemical reactions are initiated by:",
        "আলোকরাসায়নিক বিক্রিয়া শুরু হয়:",
        ["Only mechanical stirring", "Absorption of light (photons)", "Only gravity", "Removing all energy"],
        ["শুধু যান্ত্রিক নাড়াচাড়া", "আলো (ফোটন) শোষণ", "শুধু মাধ্যাকর্ষণ", "সব শক্তি অপসারণ"],
        "B", "easy", "factual",
        "Photons excite molecules to reactive states (e.g., H2 + Cl2).",
        "ফোটন অণুকে সক্রিয় অবস্থায় উত্তেজিত করে (যেমন H2 + Cl2)।",
    ),
    q(
        "An inhibitor is a substance that:",
        "ইনহিবিটর এমন পদার্থ যা:",
        ["Always increases rate", "Slows or stops a reaction", "Is identical to a reactant", "Raises nuclear charge"],
        ["সবসময় গতি বাড়ায়", "বিক্রিয়া মন্থর বা বন্ধ করে", "বিক্রিয়কের অভিন্ন", "নিউক্লিয়ার চার্জ বাড়ায়"],
        "B", "easy", "factual",
        "Inhibitors reduce rate, often by blocking active sites or scavenging radicals.",
        "ইনহিবিটর সক্রিয় স্থান অবরোধ বা র্যাডিক্যাল ধরে গতি কমায়।",
    ),
    q(
        "If a reaction is second order overall and first order in each of A and B, the rate law is:",
        "সামগ্রিক দ্বিতীয় ক্রম ও A ও B প্রত্যেকের প্রতি প্রথম ক্রম হলে rate law:",
        ["rate = k[A]2", "rate = k[A][B]", "rate = k", "rate = k[A]2[B]"],
        ["rate = k[A]2", "rate = k[A][B]", "rate = k", "rate = k[A]2[B]"],
        "B", "medium", "application",
        "Orders add to 2 when each reactant is first order.",
        "প্রতিটি বিক্রিয়ক প্রথম ক্রম হলে মোট ক্রম ২; rate = k[A][B]।",
    ),
    q(
        "Arrhenius equation relates rate constant k to:",
        "আরেনিয়াস সমীকরণ হার ধ্রুবক k কে সম্পর্কিত করে:",
        ["Only pressure and volume", "Temperature and activation energy", "Only pH", "Optical rotation"],
        ["শুধু চাপ ও আয়তন", "তাপমাত্রা ও সক্রিয়ন শক্তি", "শুধু pH", "আলোক ঘূর্ণন"],
        "B", "medium", "factual",
        "k = A e^(−Ea/RT) links k with T and Ea.",
        "k = A e^(−Ea/RT) k কে T ও Ea এর সাথে যুক্ত করে।",
    ),
    q(
        "Homogeneous catalysis means the catalyst is:",
        "সমসত্ব অনুঘটন মানে অনুঘটক:",
        ["In a different phase from reactants", "In the same phase as reactants", "Always a solid metal", "Never recoverable"],
        ["বিক্রিয়ক থেকে ভিন্ন দশায়", "বিক্রিয়কের একই দশায়", "সবসময় কঠিন ধাতু", "কখনো পুনরুদ্ধারযোগ্য নয়"],
        "B", "easy", "conceptual",
        "Example: acid catalysis of ester hydrolysis in aqueous solution.",
        "উদাহরণ: জলীয় দ্রবণে এস্টার জলবিশ্লেষণের অম্ল অনুঘটন।",
    ),
    q(
        "Why does grinding a marble chip increase its reaction rate with acid?",
        "মার্বেল চিপ গুঁড়ো করলে অম্লের সাথে বিক্রিয়ার গতি বাড়ে কেন?",
        ["Ea of the reaction increases", "Contact surface area with acid increases", "Acid concentration must decrease", "CO2 cannot escape"],
        ["বিক্রিয়ার Ea বাড়ে", "অম্লের সাথে সংস্পর্শ পৃষ্ঠক্ষেত্র বাড়ে", "অম্লের ঘনমাত্রা কমতেই হবে", "CO2 বেরোতে পারে না"],
        "B", "easy", "application",
        "Greater surface area allows more frequent collisions at the solid–liquid interface.",
        "বেশি পৃষ্ঠক্ষেত্রে কঠিন–তরল ইন্টারফেসে সংঘর্ষ বাড়ে।",
    ),
]

# --- t02: Chemical equilibrium ---
T02 = [
    q(
        "Chemical equilibrium is reached when:",
        "রাসায়নিক সাম্যাবস্থা অর্জিত হয় যখন:",
        ["All reactants are consumed", "Forward and reverse rates become equal", "Temperature becomes absolute zero", "No molecules remain"],
        ["সব বিক্রিয়ক শেষ হয়", "অগ্র ও বিপরীত গতি সমান হয়", "তাপমাত্রা পরম শূন্য হয়", "কোনো অণু থাকে না"],
        "B", "easy", "conceptual",
        "At equilibrium, macroscopic concentrations stay constant while both reactions continue.",
        "সাম্যে ম্যাক্রো ঘনমাত্রা স্থির; উভয় বিক্রিয়া চলতে থাকে।",
    ),
    q(
        "For aA + bB ⇌ cC + dD, Kc equals:",
        "aA + bB ⇌ cC + dD এর জন্য Kc সমান:",
        ["[A]a[B]b / [C]c[D]d", "[C]c[D]d / [A]a[B]b", "[A]+[B]+[C]+[D]", "k_forward only"],
        ["[A]a[B]b / [C]c[D]d", "[C]c[D]d / [A]a[B]b", "[A]+[B]+[C]+[D]", "শুধু k_forward"],
        "B", "easy", "factual",
        "Kc is products over reactants with stoichiometric exponents.",
        "Kc = উৎপাদ/বিক্রিয়ক; স্টয়কিওমেট্রিক সূচকসহ।",
    ),
    q(
        "A large value of Kc (>1) indicates:",
        "Kc এর বড় মান (>1) নির্দেশ করে:",
        ["Reactants are heavily favored", "Products are favored at equilibrium", "No reaction occurs", "Equilibrium is impossible"],
        ["বিক্রিয়ক বেশি অনুকূল", "সাম্যে উৎপাদ অনুকূল", "কোনো বিক্রিয়া হয় না", "সাম্য অসম্ভব"],
        "B", "easy", "conceptual",
        "Large K means product concentrations dominate at equilibrium.",
        "বড় K মানে সাম্যে উৎপাদের ঘনমাত্রা প্রাধান্য পায়।",
    ),
    q(
        "Le Chatelier’s principle states that if a system at equilibrium is disturbed:",
        "ল্য শাতেলিয়ের নীতি অনুসারে সাম্যে ব্যাঘাত ঘটলে:",
        ["Nothing changes", "The system shifts to counteract the disturbance", "K always becomes zero", "All catalysts fail"],
        ["কিছুই বদলায় না", "ব্যাঘাত প্রশমনে তন্ত্র সরে যায়", "K সবসময় শূন্য হয়", "সব অনুঘটক ব্যর্থ"],
        "B", "easy", "conceptual",
        "The equilibrium position shifts to relieve the applied stress.",
        "প্রয়োগকৃত চাপ কমাতে সাম্য অবস্থান সরে যায়।",
    ),
    q(
        "Adding more reactant to a gaseous equilibrium typically:",
        "গ্যাসীয় সাম্যে অতিরিক্ত বিক্রিয়ক যোগ করলে সাধারণত:",
        ["Shifts equilibrium toward products", "Shifts toward reactants only always", "Stops the reverse reaction forever", "Changes Kc at constant T"],
        ["সাম্য উৎপাদের দিকে সরে", "সবসময় শুধু বিক্রিয়কের দিকে সরে", "বিপরীত বিক্রিয়া চিরকাল বন্ধ", "ধ্রুব T তে Kc বদলায়"],
        "A", "easy", "application",
        "Extra reactant drives the forward reaction until a new balance is reached; Kc unchanged at fixed T.",
        "অতিরিক্ত বিক্রিয়ক অগ্র বিক্রিয়া চালায়; ধ্রুব T তে Kc অপরিবর্তিত।",
    ),
    q(
        "For an exothermic equilibrium, increasing temperature:",
        "তাপোৎপাদী সাম্যে তাপমাত্রা বাড়ালে:",
        ["Favors products", "Favors reactants (shifts reverse)", "Leaves composition unchanged always", "Makes K infinite"],
        ["উৎপাদ অনুকূল করে", "বিক্রিয়ক অনুকূল করে (বিপরীত দিকে সরে)", "গঠন সবসময় অপরিবর্তিত", "K অসীম করে"],
        "B", "medium", "conceptual",
        "Heat is like a product; adding heat shifts exothermic equilibria left and lowers K.",
        "তাপ উৎপাদের মতো; তাপোৎপাদী সাম্যে তাপ যোগে বাম দিকে সরে K কমে।",
    ),
    q(
        "Increasing pressure on N2 + 3H2 ⇌ 2NH3 (all gases) favors:",
        "N2 + 3H2 ⇌ 2NH3 (সব গ্যাস) এ চাপ বাড়ালে অনুকূল হয়:",
        ["Reactants (more moles)", "Ammonia (fewer moles)", "No shift", "Only solid NH3 instantly"],
        ["বিক্রিয়ক (বেশি মোল)", "অ্যামোনিয়া (কম মোল)", "কোনো সরণ নেই", "শুধু তাৎক্ষণিক কঠিন NH3"],
        "B", "medium", "application",
        "Higher P favors the side with fewer gas moles (2 vs 4).",
        "উচ্চ P কম গ্যাস মোলের দিক অনুকূল করে (২ বনাম ৪)।",
    ),
    q(
        "A catalyst affects equilibrium by:",
        "অনুঘটক সাম্যকে প্রভাবিত করে:",
        ["Changing Kc", "Speeding attainment of equilibrium without changing K", "Destroying products", "Removing temperature dependence"],
        ["Kc পরিবর্তন করে", "K অপরিবর্তিত রেখে সাম্য দ্রুত আনে", "উৎপাদ ধ্বংস করে", "তাপমাত্রা নির্ভরতা সরিয়ে"],
        "B", "medium", "conceptual",
        "Catalysts accelerate forward and reverse rates equally; K unchanged.",
        "অনুঘটক অগ্র ও বিপরীত গতি সমানভাবে বাড়ায়; K অপরিবর্তিত।",
    ),
    q(
        "Kp and Kc are related by:",
        "Kp ও Kc সম্পর্কিত:",
        ["Kp = Kc always", "Kp = Kc(RT)Δn", "Kp = Kc / T only", "Kp = 0 if Kc > 1"],
        ["Kp = Kc সবসময়", "Kp = Kc(RT)Δn", "Kp = Kc / T শুধু", "Kc > 1 হলে Kp = 0"],
        "B", "hard", "factual",
        "Δn = change in moles of gas (products − reactants).",
        "Δn = গ্যাস মোলের পরিবর্তন (উৎপাদ − বিক্রিয়ক)।",
    ),
    q(
        "Homogeneous equilibrium means:",
        "সমসত্ব সাম্যাবস্থা মানে:",
        ["All species in different phases", "All species in the same phase", "Only solids present", "No reverse reaction"],
        ["সব প্রজাতি ভিন্ন দশায়", "সব প্রজাতি একই দশায়", "শুধু কঠিন উপস্থিত", "বিপরীত বিক্রিয়া নেই"],
        "B", "easy", "factual",
        "Example: all gases in the Haber process mixture.",
        "উদাহরণ: হেবার প্রক্রিয়ার মিশ্রণে সব গ্যাস।",
    ),
    q(
        "In heterogeneous equilibria, concentrations of pure solids/liquids:",
        "বিষমসত্ব সাম্যে বিশুদ্ধ কঠিন/তরলের ঘনমাত্রা:",
        ["Appear raised to high powers in K", "Are omitted from the K expression (activity ≈ 1)", "Must equal zero", "Equal the gas constant"],
        ["K তে উচ্চ ঘাতে থাকে", "K প্রকাশে বাদ (অ্যাক্টিভিটি ≈ 1)", "শূন্য হতেই হবে", "গ্যাস ধ্রুবকের সমান"],
        "B", "medium", "conceptual",
        "Pure condensed phases have unit activity and drop out of K.",
        "বিশুদ্ধ ঘনীভূত দশার অ্যাক্টিভিটি ১; K থেকে বাদ যায়।",
    ),
    q(
        "If Q < K for a reaction, the system will:",
        "কোনো বিক্রিয়ায় Q < K হলে তন্ত্র:",
        ["Shift toward reactants", "Shift toward products", "Already at equilibrium", "Stop completely"],
        ["বিক্রিয়কের দিকে সরে", "উৎপাদের দিকে সরে", "ইতিমধ্যে সাম্যে", "সম্পূর্ণ বন্ধ"],
        "B", "medium", "application",
        "Reaction quotient below K means forward reaction is needed to reach equilibrium.",
        "Q < K মানে সাম্যে পৌঁছাতে অগ্র বিক্রিয়া প্রয়োজন।",
    ),
    q(
        "Dynamic equilibrium means:",
        "গতিশীল সাম্যাবস্থা মানে:",
        ["Reactions have permanently stopped", "Forward and reverse continue at equal rates", "Only products form", "Energy is created"],
        ["বিক্রিয়া স্থায়ীভাবে থেমেছে", "অগ্র ও বিপরীত সমান গতিতে চলে", "শুধু উৎপাদ গঠিত হয়", "শক্তি সৃষ্টি হয়"],
        "B", "easy", "conceptual",
        "Molecular exchange continues; net change is zero.",
        "আণবিক বিনিময় চলে; নিট পরিবর্তন শূন্য।",
    ),
    q(
        "Removing a product from an equilibrium mixture typically:",
        "সাম্য মিশ্রণ থেকে উৎপাদ সরালে সাধারণত:",
        ["Shifts equilibrium toward more product formation", "Shifts only toward reactants", "Increases K at fixed T", "Freezes the system"],
        ["আরও উৎপাদ গঠনের দিকে সরে", "শুধু বিক্রিয়কের দিকে সরে", "ধ্রুব T তে K বাড়ায়", "তন্ত্র স্থির করে"],
        "A", "easy", "application",
        "Product removal drives the forward reaction (Le Chatelier).",
        "উৎপাদ অপসারণ অগ্র বিক্রিয়া চালায় (ল্য শাতেলিয়ে)।",
    ),
    q(
        "The equilibrium constant K depends primarily on:",
        "সাম্য ধ্রুবক K প্রধানত নির্ভর করে:",
        ["Catalyst amount", "Temperature", "How fast equilibrium is reached", "Container color"],
        ["অনুঘটকের পরিমাণ", "তাপমাত্রা", "সাম্য কত দ্রুত আসে", "পাত্রের রঙ"],
        "B", "easy", "factual",
        "K is a function of temperature for a given reaction.",
        "প্রদত্ত বিক্রিয়ার জন্য K তাপমাত্রার ফাংশন।",
    ),
    q(
        "For 2SO2 + O2 ⇌ 2SO3, adding an inert gas at constant volume:",
        "2SO2 + O2 ⇌ 2SO3 এ ধ্রুব আয়তনে নিষ্ক্রিয় গ্যাস যোগ করলে:",
        ["Changes partial pressures and shifts equilibrium strongly", "Does not change partial pressures of reactants/products; no shift", "Always doubles K", "Converts SO3 to solid"],
        ["আংশিক চাপ বদলে সাম্য জোরে সরে", "বিক্রিয়ক/উৎপাদের আংশিক চাপ অপরিবর্তিত; সরণ নেই", "সবসময় K দ্বিগুণ", "SO3 কে কঠিন করে"],
        "B", "hard", "conceptual",
        "At constant V, inert gas raises total P but not partial pressures of reacting gases.",
        "ধ্রুব V তে নিষ্ক্রিয় গ্যাস মোট P বাড়ায় কিন্তু বিক্রিয়ক গ্যাসের আংশিক চাপ নয়।",
    ),
    q(
        "The Haber process for ammonia uses high pressure because:",
        "অ্যামোনিয়ার হেবার প্রক্রিয়ায় উচ্চ চাপ ব্যবহার হয় কারণ:",
        ["It favors the side with more gas moles", "It favors NH3 (fewer gas moles)", "It makes the reaction endothermic", "Catalysts require vacuum"],
        ["বেশি গ্যাস মোলের দিক অনুকূল", "NH3 অনুকূল (কম গ্যাস মোল)", "বিক্রিয়া তাপহারী করে", "অনুঘটকের শূন্য প্রয়োজন"],
        "B", "medium", "application",
        "Industrial synthesis exploits Le Chatelier with high P toward NH3.",
        "শিল্প সংশ্লেষণে উচ্চ P দিয়ে NH3 এর দিকে ল্য শাতেলিয়ে প্রয়োগ।",
    ),
    q(
        "If K = 1 for a reaction at a given T:",
        "প্রদত্ত T তে কোনো বিক্রিয়ার K = 1 হলে:",
        ["Only reactants exist", "Products and reactants are comparably significant at equilibrium", "Reaction cannot occur", "ΔG° must be largely negative always"],
        ["শুধু বিক্রিয়ক থাকে", "সাম্যে উৎপাদ ও বিক্রিয়ক তুলনামূলকভাবে গুরুত্বপূর্ণ", "বিক্রিয়া অসম্ভব", "ΔG° সবসময় অনেক ঋণাত্মক"],
        "B", "medium", "conceptual",
        "K ≈ 1 means neither side strongly dominates.",
        "K ≈ 1 মানে কোনো দিকই জোরালোভাবে প্রাধান্য পায় না।",
    ),
    q(
        "Writing the equilibrium expression for CaCO3(s) ⇌ CaO(s) + CO2(g), Kp is essentially:",
        "CaCO3(s) ⇌ CaO(s) + CO2(g) এর সাম্য প্রকাশে Kp মূলত:",
        ["P_CO2", "1 / P_CO2", "[CaCO3]/[CaO]", "P_CaO × P_CO2"],
        ["P_CO2", "1 / P_CO2", "[CaCO3]/[CaO]", "P_CaO × P_CO2"],
        "A", "hard", "application",
        "Solids omit from K; Kp = P_CO2 for this decomposition.",
        "কঠিন K থেকে বাদ; এই বিয়োজনে Kp = P_CO2।",
    ),
    q(
        "A closed system is required to maintain chemical equilibrium because:",
        "রাসায়নিক সাম্য বজায় রাখতে বদ্ধ তন্ত্র প্রয়োজন কারণ:",
        ["Matter can freely leave forever", "Reactants and products must remain available to both directions", "Open flasks increase K automatically", "Light must be excluded always"],
        ["পদার্থ চিরকাল অবাধে বেরোতে পারে", "উভয় দিকের জন্য বিক্রিয়ক ও উৎপাদ উপলব্ধ থাকতে হবে", "মুক্ত ফ্লাস্ক স্বয়ংক্রিয়ভাবে K বাড়ায়", "সবসময় আলো বাদ দিতে হবে"],
        "B", "easy", "conceptual",
        "If matter escapes, concentrations change and true equilibrium cannot persist.",
        "পদার্থ বেরোলে ঘনমাত্রা বদলায়; প্রকৃত সাম্য টেকে না।",
    ),
]

# --- t03: Acids, bases and pH ---
T03 = [
    q(
        "According to Arrhenius, an acid produces in water:",
        "আরেনিয়াস অনুসারে অম্ল পানিতে উৎপন্ন করে:",
        ["OH− ions", "H+ (H3O+) ions", "Only electrons", "Noble gases"],
        ["OH− আয়ন", "H+ (H3O+) আয়ন", "শুধু ইলেকট্রন", "নিষ্ক্রিয় গ্যাস"],
        "B", "easy", "factual",
        "Arrhenius acids increase [H+] in aqueous solution.",
        "আরেনিয়াস অম্ল জলীয় দ্রবণে [H+] বাড়ায়।",
    ),
    q(
        "According to Arrhenius, a base produces in water:",
        "আরেনিয়াস অনুসারে ক্ষার পানিতে উৎপন্ন করে:",
        ["H+ ions", "OH− ions", "Only CO2", "Protons only"],
        ["H+ আয়ন", "OH− আয়ন", "শুধু CO2", "শুধু প্রোটন"],
        "B", "easy", "factual",
        "Arrhenius bases increase [OH−] in water.",
        "আরেনিয়াস ক্ষার পানিতে [OH−] বাড়ায়।",
    ),
    q(
        "In the Brønsted–Lowry definition, an acid is a:",
        "ব্রনস্টেড–লাউরি সংজ্ঞায় অম্ল হলো:",
        ["Proton acceptor", "Proton donor", "Electron pair donor only", "Oxide former only"],
        ["প্রোটন গ্রহীতা", "প্রোটন দাতা", "শুধু ইলেকট্রন জোড়া দাতা", "শুধু অক্সাইড গঠনকারী"],
        "B", "easy", "factual",
        "Brønsted acids donate H+; bases accept H+.",
        "ব্রনস্টেড অম্ল H+ দান করে; ক্ষার H+ গ্রহণ করে।",
    ),
    q(
        "A conjugate base is formed when an acid:",
        "অম্ল থেকে কনজুগেট ক্ষার গঠিত হয় যখন অম্ল:",
        ["Gains a proton", "Loses a proton", "Gains an electron pair only", "Becomes a metal"],
        ["প্রোটন গ্রহণ করে", "প্রোটন হারায়", "শুধু ইলেকট্রন জোড়া নেয়", "ধাতু হয়"],
        "B", "easy", "conceptual",
        "HA ⇌ H+ + A−; A− is the conjugate base of HA.",
        "HA ⇌ H+ + A−; A− হলো HA এর কনজুগেট ক্ষার।",
    ),
    q(
        "pH is defined as:",
        "pH এর সংজ্ঞা:",
        ["log[H+]", "−log[H+]", "log[OH−]", "[H+] × [OH−]"],
        ["log[H+]", "−log[H+]", "log[OH−]", "[H+] × [OH−]"],
        "B", "easy", "factual",
        "pH = −log10[H3O+] (approx. −log[H+]).",
        "pH = −log10[H3O+] (প্রায় −log[H+])।",
    ),
    q(
        "A solution with pH = 3 is:",
        "pH = ৩ এর দ্রবণ:",
        ["Neutral", "Basic", "Acidic", "Pure water only"],
        ["নিরপেক্ষ", "ক্ষারীয়", "অম্লীয়", "শুধু বিশুদ্ধ পানি"],
        "C", "easy", "application",
        "pH < 7 indicates acidity at 25 °C.",
        "২৫ °C তে pH < ৭ অম্লীয় নির্দেশ করে।",
    ),
    q(
        "At 25 °C, pure water has pH approximately:",
        "২৫ °C তে বিশুদ্ধ পানির pH প্রায়:",
        ["0", "7", "14", "1"],
        ["0", "7", "14", "1"],
        "B", "easy", "factual",
        "Kw = 1×10−14; [H+] = 1×10−7 → pH 7.",
        "Kw = 1×10−14; [H+] = 1×10−7 → pH ৭।",
    ),
    q(
        "The ionic product of water Kw equals:",
        "পানির আয়নিক গুণফল Kw সমান:",
        ["[H+] / [OH−]", "[H+][OH−]", "[H+] + [OH−]", "pH × pOH"],
        ["[H+] / [OH−]", "[H+][OH−]", "[H+] + [OH−]", "pH × pOH"],
        "B", "easy", "factual",
        "Kw = [H+][OH−] ≈ 1.0×10−14 at 25 °C.",
        "২৫ °C তে Kw = [H+][OH−] ≈ 1.0×10−14।",
    ),
    q(
        "For aqueous solutions at 25 °C, pH + pOH equals:",
        "২৫ °C তে জলীয় দ্রবণে pH + pOH সমান:",
        ["1", "7", "14", "0"],
        ["1", "7", "14", "0"],
        "C", "easy", "numerical",
        "Because Kw = 10−14, pH + pOH = 14.",
        "Kw = 10−14 বলে pH + pOH = ১৪।",
    ),
    q(
        "A strong acid is one that:",
        "সবল অম্ল এমন যা:",
        ["Partially ionizes in water", "Completely ionizes in water", "Never reacts with bases", "Has pH > 10 always"],
        ["পানিতে আংশিক আয়নিত হয়", "পানিতে সম্পূর্ণ আয়নিত হয়", "ক্ষারের সাথে কখনো বিক্রিয়া করে না", "সবসময় pH > ১০"],
        "B", "easy", "conceptual",
        "HCl, HNO3, H2SO4 (first proton) are typical strong acids.",
        "HCl, HNO3, H2SO4 (প্রথম প্রোটন) সাধারণ সবল অম্ল।",
    ),
    q(
        "Which is a weak acid?",
        "কোনটি দুর্বল অম্ল?",
        ["HCl", "HNO3", "CH3COOH", "HClO4"],
        ["HCl", "HNO3", "CH3COOH", "HClO4"],
        "C", "easy", "application",
        "Acetic acid only partially dissociates in water.",
        "অ্যাসিটিক অম্ল পানিতে শুধু আংশিক বিয়োজিত হয়।",
    ),
    q(
        "Neutralization of a strong acid with a strong base produces:",
        "সবল অম্ল ও সবল ক্ষারের প্রশমন উৎপন্ন করে:",
        ["Only a gas", "Salt and water", "Only alcohol", "Ozone"],
        ["শুধু গ্যাস", "লবণ ও পানি", "শুধু অ্যালকোহল", "ওজোন"],
        "B", "easy", "factual",
        "H+ + OH− → H2O; the accompanying ions form a salt.",
        "H+ + OH− → H2O; সহগামী আয়ন লবণ গঠন করে।",
    ),
    q(
        "A buffer solution resists changes in:",
        "বাফার দ্রবণ প্রতিরোধ করে কোনটির পরিবর্তন?",
        ["Volume only", "pH on addition of small amounts of acid or base", "Temperature only", "Color permanently"],
        ["শুধু আয়তন", "অল্প অম্ল/ক্ষার যোগে pH", "শুধু তাপমাত্রা", "স্থায়ীভাবে রঙ"],
        "B", "medium", "conceptual",
        "Typical buffers: weak acid + its salt (conjugate base).",
        "সাধারণ বাফার: দুর্বল অম্ল + তার লবণ (কনজুগেট ক্ষার)।",
    ),
    q(
        "Lewis acid is defined as an:",
        "লুইস অম্লের সংজ্ঞা:",
        ["Electron pair donor", "Electron pair acceptor", "Proton donor only", "OH− producer only"],
        ["ইলেকট্রন জোড়া দাতা", "ইলেকট্রন জোড়া গ্রহীতা", "শুধু প্রোটন দাতা", "শুধু OH− উৎপাদক"],
        "B", "medium", "factual",
        "BF3 and AlCl3 are classic Lewis acids.",
        "BF3 ও AlCl3 ক্লাসিক লুইস অম্ল।",
    ),
    q(
        "The pH of 0.01 M HCl (strong acid, ideal) is approximately:",
        "০.০১ M HCl (সবল অম্ল, আদর্শ) এর pH প্রায়:",
        ["1", "2", "12", "7"],
        ["1", "2", "12", "7"],
        "B", "medium", "numerical",
        "[H+] = 0.01 = 10−2 → pH = 2.",
        "[H+] = ০.০১ = 10−2 → pH = ২।",
    ),
    q(
        "Hydrolysis of CH3COONa in water makes the solution:",
        "পানিতে CH3COONa এর জলবিশ্লেষণ দ্রবণকে করে:",
        ["Acidic", "Basic (alkaline)", "Neutral always like NaCl", "Strongly oxidizing"],
        ["অম্লীয়", "ক্ষারীয়", "NaCl এর মতো সবসময় নিরপেক্ষ", "সবল জারক"],
        "B", "medium", "application",
        "Acetate ion is the conjugate base of a weak acid and accepts H+ from water.",
        "অ্যাসিটেট দুর্বল অম্লের কনজুগেট ক্ষার; পানি থেকে H+ নেয়।",
    ),
    q(
        "Which indicator is commonly used near the end point of strong acid–strong base titration?",
        "সবল অম্ল–সবল ক্ষার টাইট্রেশনের শেষ বিন্দুর কাছে সাধারণত কোন সূচক?",
        ["Only starch", "Phenolphthalein or methyl orange (suitable range)", "Only litmus paper in nonaqueous media", "None exist"],
        ["শুধু স্টার্চ", "ফেনলফথ্যালিন বা মিথাইল অরেঞ্জ (উপযুক্ত পরিসর)", "শুধু অজলীয় মাধ্যমে লিটমাস", "কোনোটি নেই"],
        "B", "medium", "application",
        "Both work near neutral; choice depends on exact transition pH.",
        "উভয়ই নিরপেক্ষের কাছে কাজ করে; স্থানান্তর pH অনুসারে বাছাই।",
    ),
    q(
        "Amphoteric substances can:",
        "উভধর্মী পদার্থ পারে:",
        ["Only act as acids", "Act as either acid or base depending on partner", "Never donate protons", "Only form salts with metals"],
        ["শুধু অম্ল হিসেবে কাজ", "সঙ্গীর উপর নির্ভর করে অম্ল বা ক্ষার হিসেবে কাজ", "কখনো প্রোটন দান করে না", "শুধু ধাতুর সাথে লবণ গঠন"],
        "B", "medium", "conceptual",
        "Water and Al(OH)3 are common amphiprotic/amphoteric examples.",
        "পানি ও Al(OH)3 সাধারণ উভধর্মী উদাহরণ।",
    ),
    q(
        "Ka is the:",
        "Ka হলো:",
        ["Base dissociation constant", "Acid dissociation constant", "Solubility product only", "Rate constant of catalysis"],
        ["ক্ষার বিয়োজন ধ্রুবক", "অম্ল বিয়োজন ধ্রুবক", "শুধু দ্রবণীয়তা গুণফল", "অনুঘটনের হার ধ্রুবক"],
        "B", "easy", "factual",
        "Larger Ka means a stronger acid.",
        "বড় Ka মানে সবলতর অম্ল।",
    ),
    q(
        "For a weak acid HA, increasing dilution generally:",
        "দুর্বল অম্ল HA এর তরলীকরণ বাড়ালে সাধারণত:",
        ["Decreases degree of dissociation", "Increases degree of dissociation", "Makes Ka temperature-independent forever", "Converts HA to a strong base"],
        ["বিয়োজন মাত্রা কমায়", "বিয়োজন মাত্রা বাড়ায়", "Ka কে চিরকাল তাপমাত্রা-নিরপেক্ষ করে", "HA কে সবল ক্ষার করে"],
        "B", "hard", "conceptual",
        "Ostwald’s dilution law: α increases as concentration falls for weak electrolytes.",
        "অস্টওয়াল্ড তরলীকরণ সূত্র: দুর্বল তড়িৎবিশ্লেষ্যে ঘনমাত্রা কমলে α বাড়ে।",
    ),
]

# --- t04: Energy changes in reactions ---
T04 = [
    q(
        "An exothermic reaction:",
        "তাপোৎপাদী বিক্রিয়া:",
        ["Absorbs heat from surroundings", "Releases heat to surroundings", "Has ΔH always positive", "Never occurs"],
        ["পরিবেশ থেকে তাপ শোষণ করে", "পরিবেশে তাপ মুক্ত করে", "ΔH সবসময় ধনাত্মক", "কখনো ঘটে না"],
        "B", "easy", "factual",
        "Exothermic processes have negative ΔH (heat released).",
        "তাপোৎপাদী প্রক্রিয়ায় ΔH ঋণাত্মক (তাপ মুক্ত)।",
    ),
    q(
        "An endothermic reaction:",
        "তাপহারী বিক্রিয়া:",
        ["Releases heat", "Absorbs heat from surroundings", "Always spontaneous at all T", "Has ΔH = 0"],
        ["তাপ মুক্ত করে", "পরিবেশ থেকে তাপ শোষণ করে", "সব T তে সবসময় স্বতঃস্ফূর্ত", "ΔH = ০"],
        "B", "easy", "factual",
        "Endothermic processes have positive ΔH.",
        "তাপহারী প্রক্রিয়ায় ΔH ধনাত্মক।",
    ),
    q(
        "Enthalpy change ΔH is approximately the heat exchanged at:",
        "এনথ্যালপি পরিবর্তন ΔH প্রায় কোন অবস্থায় বিনিময়িত তাপ?",
        ["Constant volume only", "Constant pressure", "Absolute zero only", "Infinite pressure"],
        ["শুধু ধ্রুব আয়তন", "ধ্রুব চাপ", "শুধু পরম শূন্য", "অসীম চাপ"],
        "B", "easy", "factual",
        "qp = ΔH for processes at constant pressure.",
        "ধ্রুব চাপে qp = ΔH।",
    ),
    q(
        "In a thermochemical equation, the ΔH value refers to:",
        "তাপরাসায়নিক সমীকরণে ΔH মান নির্দেশ করে:",
        ["Any random amount of substance", "The molar amounts as written in the balanced equation", "Only catalysts", "Nuclear binding alone"],
        ["পদার্থের যেকোনো এলোমেলো পরিমাণ", "সমতুল্য সমীকরণে লিখিত মোল পরিমাণ", "শুধু অনুঘটক", "শুধু নিউক্লিয়ার বন্ধন"],
        "B", "easy", "conceptual",
        "Scaling the equation scales ΔH proportionally.",
        "সমীকরণ গুণ করলে ΔH সমানুপাতিকভাবে গুণ হয়।",
    ),
    q(
        "Hess’s law states that the overall enthalpy change:",
        "হেসের সূত্র অনুসারে সামগ্রিক এনথ্যালপি পরিবর্তন:",
        ["Depends on the path taken", "Is path-independent; equals the sum of stepwise ΔH", "Is always zero", "Equals only bond energies of products"],
        ["পথের উপর নির্ভর করে", "পথ-নিরপেক্ষ; ধাপগুলোর ΔH এর যোগফল", "সবসময় শূন্য", "শুধু উৎপাদের বন্ধন শক্তির সমান"],
        "B", "medium", "conceptual",
        "Enthalpy is a state function; Hess cycles combine known ΔH values.",
        "এনথ্যালপি অবস্থা ফাংশন; হেস চক্রে পরিচিত ΔH যোগ করা যায়।",
    ),
    q(
        "Bond enthalpy is the energy required to:",
        "বন্ধন এনথ্যালপি হলো কোনটির জন্য প্রয়োজনীয় শক্তি?",
        ["Form a bond in a solid crystal only", "Break one mole of a particular bond in gaseous molecules", "Melt ice", "Ionize metals in solution"],
        ["শুধু কঠিন স্ফটিকে বন্ধন গঠন", "গ্যাসীয় অণুতে নির্দিষ্ট বন্ধনের এক মোল ভাঙা", "বরফ গলানো", "দ্রবণে ধাতু আয়নিত করা"],
        "B", "medium", "factual",
        "Average bond enthalpies estimate ΔH for gas-phase reactions.",
        "গড় বন্ধন এনথ্যালপি গ্যাস দশার বিক্রিয়ার ΔH আনুমান করে।",
    ),
    q(
        "If bonds broken require more energy than bonds formed release, the reaction is:",
        "ভাঙা বন্ধনের শক্তি গঠিত বন্ধনের মুক্ত শক্তির চেয়ে বেশি হলে বিক্রিয়া:",
        ["Exothermic", "Endothermic", "At equilibrium always", "Impossible"],
        ["তাপোৎপাদী", "তাপহারী", "সবসময় সাম্যে", "অসম্ভব"],
        "B", "medium", "conceptual",
        "Net energy absorption → positive ΔH (endothermic).",
        "নিট শক্তি শোষণ → ধনাত্মক ΔH (তাপহারী)।",
    ),
    q(
        "Standard enthalpy of formation ΔHf° of an element in its standard state is:",
        "মৌলের মানক অবস্থায় গঠন এনথ্যালপি ΔHf°:",
        ["Always largely positive", "Zero by definition", "Equal to its boiling point", "Equal to Ea"],
        ["সবসময় অনেক ধনাত্মক", "সংজ্ঞা অনুসারে শূন্য", "স্ফুটনাঙ্কের সমান", "Ea এর সমান"],
        "B", "easy", "factual",
        "ΔHf° = 0 for elements in standard states (e.g., O2(g), C(graphite)).",
        "মানক অবস্থার মৌলের ΔHf° = ০ (যেমন O2(g), C(গ্রাফাইট))।",
    ),
    q(
        "Combustion of fuels is typically:",
        "জ্বালানির দহন সাধারণত:",
        ["Endothermic", "Exothermic", "Without enthalpy change", "A nuclear process only"],
        ["তাপহারী", "তাপোৎপাদী", "এনথ্যালপি পরিবর্তনহীন", "শুধু নিউক্লিয়ার প্রক্রিয়া"],
        "B", "easy", "application",
        "Burning releases heat used for heating and engines.",
        "দহনে তাপ মুক্ত হয় যা উত্তাপ ও ইঞ্জিনে ব্যবহৃত।",
    ),
    q(
        "Calorimetry measures:",
        "ক্যালোরিমেট্রি পরিমাপ করে:",
        ["Only color changes", "Heat exchanged in chemical/physical processes", "Nuclear spin only", "pH exclusively"],
        ["শুধু রঙ পরিবর্তন", "রাসায়নিক/ভৌত প্রক্রিয়ায় বিনিময়িত তাপ", "শুধু নিউক্লিয়ার স্পিন", "কেবল pH"],
        "B", "easy", "factual",
        "A calorimeter tracks temperature change to find heat q.",
        "ক্যালোরিমিটার তাপমাত্রা পরিবর্তন থেকে তাপ q নির্ধারণ করে।",
    ),
    q(
        "Internal energy change ΔU relates to heat at constant volume by:",
        "ধ্রুব আয়তনে অভ্যন্তরীণ শক্তি পরিবর্তন ΔU তাপের সাথে:",
        ["ΔU = qp", "ΔU = qv", "ΔU = T only", "ΔU = pH"],
        ["ΔU = qp", "ΔU = qv", "ΔU = শুধু T", "ΔU = pH"],
        "B", "medium", "factual",
        "At constant volume, qv = ΔU.",
        "ধ্রুব আয়তনে qv = ΔU।",
    ),
    q(
        "The relationship ΔH = ΔU + Δn_g RT applies approximately to:",
        "ΔH = ΔU + Δn_g RT সম্পর্ক প্রায় প্রযোজ্য:",
        ["Only solid–solid reactions with no gas", "Ideal-gas mole changes in reactions at constant T", "Only photochemical explosions", "pH buffers"],
        ["গ্যাসহীন শুধু কঠিন–কঠিন বিক্রিয়া", "ধ্রুব T তে বিক্রিয়ায় আদর্শ গ্যাস মোল পরিবর্তন", "শুধু আলোকরাসায়নিক বিস্ফোরণ", "pH বাফার"],
        "B", "hard", "conceptual",
        "Δn_g is the change in moles of gas in the balanced equation.",
        "Δn_g হলো সমতুল্য সমীকরণে গ্যাস মোলের পরিবর্তন।",
    ),
    q(
        "Spontaneous processes at constant T and P are favored by:",
        "ধ্রুব T ও P তে স্বতঃস্ফূর্ত প্রক্রিয়া অনুকূল হয়:",
        ["Positive ΔG", "Negative ΔG", "ΔG undefined", "Only when ΔH is largely positive and ΔS negative"],
        ["ধনাত্মক ΔG", "ঋণাত্মক ΔG", "ΔG অনির্ধারিত", "শুধু ΔH অনেক ধনাত্মক ও ΔS ঋণাত্মক হলে"],
        "B", "medium", "conceptual",
        "Gibbs free energy: ΔG < 0 indicates spontaneity under standard criteria.",
        "গিবস মুক্ত শক্তি: ΔG < ০ স্বতঃস্ফূর্ততার নির্দেশক।",
    ),
    q(
        "ΔG = ΔH − TΔS implies that an endothermic reaction can be spontaneous if:",
        "ΔG = ΔH − TΔS অনুসারে তাপহারী বিক্রিয়া স্বতঃস্ফূর্ত হতে পারে যদি:",
        ["ΔS is negative and T is low always", "ΔS is sufficiently positive and T is high enough", "ΔH is more positive forever", "Entropy is zero"],
        ["ΔS ঋণাত্মক ও T সবসময় কম", "ΔS যথেষ্ট ধনাত্মক ও T যথেষ্ট উচ্চ", "ΔH চিরকাল আরও ধনাত্মক", "এনট্রপি শূন্য"],
        "B", "hard", "conceptual",
        "−TΔS can outweigh positive ΔH at high temperature.",
        "উচ্চ তাপমাত্রায় −TΔS ধনাত্মক ΔH কে ছাড়িয়ে যেতে পারে।",
    ),
    q(
        "Entropy (S) is a measure of:",
        "এনট্রপি (S) পরিমাপ করে:",
        ["Only temperature", "Disorder or dispersal of energy/matter", "Only bond strength", "Nuclear charge"],
        ["শুধু তাপমাত্রা", "বিশৃঙ্খলা বা শক্তি/পদার্থের বিস্তার", "শুধু বন্ধন শক্তি", "নিউক্লিয়ার চার্জ"],
        "B", "easy", "conceptual",
        "Gases typically have higher entropy than liquids or solids.",
        "গ্যাসের এনট্রপি সাধারণত তরল বা কঠিনের চেয়ে বেশি।",
    ),
    q(
        "Photosynthesis is overall:",
        "সালোকসংশ্লেষণ সামগ্রিকভাবে:",
        ["Strongly exothermic like combustion", "Endothermic, storing solar energy in chemical bonds", "Without energy change", "A neutralization only"],
        ["দহনের মতো সবল তাপোৎপাদী", "তাপহারী; সৌরশক্তি রাসায়নিক বন্ধনে সঞ্চিত", "শক্তি পরিবর্তনহীন", "শুধু প্রশমন"],
        "B", "medium", "application",
        "CO2 + H2O → sugars + O2 requires input of light energy.",
        "CO2 + H2O → শর্করা + O2 এ আলোক শক্তির ইনপুট লাগে।",
    ),
    q(
        "The heat of neutralization of strong acid and strong base (per mole H2O) is approximately:",
        "সবল অম্ল ও সবল ক্ষারের প্রশমন তাপ (প্রতি মোল H2O) প্রায়:",
        ["Highly endothermic +57 kJ", "About −57 kJ mol−1 (exothermic)", "Zero", "Equal to bond energy of N2"],
        ["অত্যন্ত তাপহারী +৫৭ kJ", "প্রায় −৫৭ kJ mol−1 (তাপোৎপাদী)", "শূন্য", "N2 এর বন্ধন শক্তির সমান"],
        "B", "medium", "factual",
        "H+ + OH− → H2O releases about 57 kJ mol−1.",
        "H+ + OH− → H2O প্রায় ৫৭ kJ mol−1 তাপ মুক্ত করে।",
    ),
    q(
        "A reaction coordinate diagram for an exothermic reaction shows products:",
        "তাপোৎপাদী বিক্রিয়ার প্রতিক্রিয়া-সমন্বয় চিত্রে উৎপাদ:",
        ["Higher in enthalpy than reactants", "Lower in enthalpy than reactants", "At identical enthalpy always", "Without an activation barrier ever"],
        ["বিক্রিয়কের চেয়ে উচ্চ এনথ্যালপিতে", "বিক্রিয়কের চেয়ে নিম্ন এনথ্যালপিতে", "সবসময় অভিন্ন এনথ্যালপিতে", "কখনো সক্রিয়ন বাধা ছাড়া"],
        "B", "easy", "conceptual",
        "Products lie below reactants; the difference is −ΔH released as heat.",
        "উৎপাদ বিক্রিয়কের নিচে; পার্থক্য −ΔH তাপ হিসেবে মুক্ত।",
    ),
    q(
        "Standard enthalpy of combustion ΔHc° is the enthalpy change when:",
        "দহন এনথ্যালপি ΔHc° হলো কোনটির এনথ্যালপি পরিবর্তন?",
        ["One mole of substance burns completely in oxygen under standard conditions", "A substance melts", "An element forms from ions", "Water freezes"],
        ["মানক অবস্থায় এক মোল পদার্থ অক্সিজেনে সম্পূর্ণ দহন", "পদার্থ গলে", "আয়ন থেকে মৌল গঠন", "পানি জমে"],
        "A", "easy", "factual",
        "ΔHc° values are typically negative (exothermic combustion).",
        "ΔHc° সাধারণত ঋণাত্মক (তাপোৎপাদী দহন)।",
    ),
    q(
        "If a reaction has ΔH < 0 and ΔS > 0, it is:",
        "ΔH < ০ ও ΔS > ০ হলে বিক্রিয়া:",
        ["Non-spontaneous at all temperatures", "Spontaneous at all temperatures (ΔG < 0)", "Spontaneous only at very low T", "Forbidden by Hess’s law"],
        ["সব তাপমাত্রায় অস্বতঃস্ফূর্ত", "সব তাপমাত্রায় স্বতঃস্ফূর্ত (ΔG < ০)", "শুধু খুব কম T তে স্বতঃস্ফূর্ত", "হেসের সূত্রে নিষিদ্ধ"],
        "B", "hard", "application",
        "Both enthalpy and entropy terms favor negative ΔG at any T.",
        "এনথ্যালপি ও এনট্রপি উভয়ই যেকোনো T তে ঋণাত্মক ΔG অনুকূল করে।",
    ),
]

TOPICS_MAP = {
    "chem1_27_ch04_t01": T01,
    "chem1_27_ch04_t02": T02,
    "chem1_27_ch04_t03": T03,
    "chem1_27_ch04_t04": T04,
}


def write_topic(topic_id: str, items: list[dict]) -> dict:
    assert len(items) == 20, f"{topic_id} has {len(items)}"
    clean = []
    for item in items:
        row = {k: v for k, v in item.items() if not k.startswith("_")}
        row["verified"] = False
        row["source"] = SRC
        err = validate_record(row)
        if err:
            raise SystemExit(f"{topic_id}: {err}\n{row['stem_en'][:120]}")
        clean.append(row)
    path = TOPICS / f"{topic_id}.jsonl"
    path.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in clean) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {path.name}: {len(clean)}")
    return {"path": str(path.relative_to(ROOT)).replace("\\", "/"), "count": len(clean)}


def main() -> int:
    for tid, rows in TOPICS_MAP.items():
        assert len(rows) == 20, f"{tid} has {len(rows)}"

    counts = {}
    paths = {}
    for tid, rows in TOPICS_MAP.items():
        info = write_topic(tid, rows)
        counts[tid] = info["count"]
        paths[tid] = info["path"]

    all_stems = []
    for tid in TOPIC_IDS:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "chem1_27_ch04",
        "title_en": "Chemical Change",
        "title_bn": "রাসায়নিক পরিবর্তন",
        "source": SRC,
        "pdf_pages": [],
        "note": (
            "Import CSV chemistry_1_ch04.csv had headers only; authored 20 bilingual MCQs "
            "per topic aligned to NCTB chemistry_1st_paper_2027 ch04 (Chemical Change)."
        ),
        "counts": {**counts, "total": sum(counts.values())},
        "paths": paths,
        "pdf_mapping": {
            "chem1_27_ch04_t01": {
                "title": "Reaction rates / বিক্রিয়ার গতি",
                "themes": [
                    "rate definition; collision theory; Ea; temperature; catalyst",
                    "order rate laws half-life Arrhenius surface area",
                    "inhibitor photochemical RDS homogeneous catalysis",
                ],
            },
            "chem1_27_ch04_t02": {
                "title": "Chemical equilibrium / রাসায়নিক সাম্যাবস্থা",
                "themes": [
                    "dynamic equilibrium Kc Kp Q; Le Chatelier",
                    "T P concentration catalyst; Haber; heterogeneous K",
                    "Kp=Kc(RT)Δn; inert gas constant V; CaCO3 Kp",
                ],
            },
            "chem1_27_ch04_t03": {
                "title": "Acids, bases and pH / অম্ল, ক্ষার ও pH",
                "themes": [
                    "Arrhenius Bronsted Lewis; conjugate pairs; Ka",
                    "pH pOH Kw strong weak acids buffers hydrolysis",
                    "neutralization indicators amphoteric Ostwald dilution",
                ],
            },
            "chem1_27_ch04_t04": {
                "title": "Energy changes in reactions / বিক্রিয়ায় শক্তির পরিবর্তন",
                "themes": [
                    "exo endo ΔH Hess bond enthalpy ΔHf ΔHc calorimetry",
                    "ΔU ΔH ΔnRT; ΔG ΔH−TΔS entropy photosynthesis",
                    "neutralization heat reaction profiles spontaneity",
                ],
            },
        },
        "low_confidence": [
            "No usable OCR for Chemistry 1st paper Udvash PDF ch04; syllabus-authored MCQs.",
            "Import CSV content/bank/import/chemistry_1_ch04.csv had headers only.",
            "Neutralization heat ~57 kJ mol−1 and ideal pH calculations follow common board values.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (chem1_27_ch04_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {tid: 20 for tid in TOPIC_IDS},
        },
        "chem1_ch04_completion": {
            "topics_expected": 4,
            "topics_at_20": 4,
            "note": "chem1_27_ch04_t01..t04 complete at 20/topic (chapter total 80).",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch04_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
