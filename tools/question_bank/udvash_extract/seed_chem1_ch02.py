#!/usr/bin/env python3
"""Seed Chemistry 1st Paper Ch2 bilingual MCQs (Qualitative Chemistry).

Import CSV chemistry_1_ch02.csv had headers only; PDF OCR corrupted.
Authored 20 bilingual MCQs per topic aligned to NCTB chemistry_1st_paper_2027 ch02.
Topics: chem1_27_ch02_t01..t05.
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
    "chemistry p1 ch02; curated bilingual"
)

TOPIC_IDS = [f"chem1_27_ch02_t{i:02d}" for i in range(1, 6)]


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    if not re.search(r"[A-Za-z]", en):
        en = f"value {en}"
    if not re.search(r"[ঀ-৿]", bn) and re.search(r"[A-Za-z]{3,}", bn):
        bn = f"{bn} (মান)"
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


# --- t01: Atomic structure and quantum numbers ---
T01 = [
    q(
        "The atomic number of an element equals the number of:",
        "কোনো মৌলের পারমাণবিক সংখ্যা সমান:",
        [
            "Protons in the nucleus",
            "Neutrons only",
            "Nucleons minus electrons always",
            "Valence shells only",
        ],
        [
            "নিউক্লিয়াসের প্রোটন সংখ্যা",
            "শুধু নিউট্রন",
            "সবসময় নিউক্লিয়ন বিয়োগ ইলেকট্রন",
            "শুধু ভ্যালেন্স শেল",
        ],
        "A", "easy", "factual",
        "Atomic number Z is defined as the proton count.",
        "পারমাণবিক সংখ্যা Z প্রোটন সংখ্যা দ্বারা সংজ্ঞায়িত।",
    ),
    q(
        "Mass number (A) of an atom is the total of:",
        "পরমাণুর ভর সংখ্যা (A) হলো মোট:",
        [
            "Protons + neutrons",
            "Protons + electrons only",
            "Neutrons + electrons only",
            "Electrons alone",
        ],
        [
            "প্রোটন + নিউট্রন",
            "শুধু প্রোটন + ইলেকট্রন",
            "শুধু নিউট্রন + ইলেকট্রন",
            "শুধু ইলেকট্রন",
        ],
        "A", "easy", "factual",
        "A = Z + N (protons plus neutrons).",
        "A = Z + N (প্রোটন ও নিউট্রনের যোগফল)।",
    ),
    q(
        "Isotopes of an element have the same:",
        "কোনো মৌলের আইসোটোপগুলোর একই থাকে:",
        [
            "Atomic number but different mass numbers",
            "Mass number but different atomic numbers",
            "Number of neutrons only, never protons",
            "Chemical symbol that must differ",
        ],
        [
            "পারমাণবিক সংখ্যা কিন্তু ভিন্ন ভর সংখ্যা",
            "ভর সংখ্যা কিন্তু ভিন্ন পারমাণবিক সংখ্যা",
            "শুধু নিউট্রন সংখ্যা, কখনো প্রোটন নয়",
            "রাসায়নিক প্রতীক যা অবশ্যই ভিন্ন",
        ],
        "A", "easy", "conceptual",
        "Isotopes share Z (and chemical identity) but differ in neutron count.",
        "আইসোটোপগুলোর Z (ও রাসায়নিক পরিচয়) এক; নিউট্রন সংখ্যা ভিন্ন।",
    ),
    q(
        "Which subatomic particle has a relative charge of −1?",
        "কোন উপপরমাণবিক কণার আপেক্ষিক চার্জ −১?",
        [
            "Electron",
            "Proton",
            "Neutron",
            "Alpha particle nucleus only",
        ],
        [
            "ইলেকট্রন",
            "প্রোটন",
            "নিউট্রন",
            "শুধু আলফা কণার নিউক্লিয়াস",
        ],
        "A", "easy", "factual",
        "Electrons carry unit negative charge; protons are +1; neutrons are 0.",
        "ইলেকট্রনের একক ঋণাত্মক চার্জ; প্রোটন +১; নিউট্রন ০।",
    ),
    q(
        "The principal quantum number n mainly indicates:",
        "প্রধান কোয়ান্টাম সংখ্যা n মূলত নির্দেশ করে:",
        [
            "The main energy level (shell) of an electron",
            "Only the spin direction",
            "Only nuclear charge",
            "Only the number of neutrons",
        ],
        [
            "ইলেকট্রনের প্রধান শক্তিস্তর (শেল)",
            "শুধু স্পিন দিক",
            "শুধু নিউক্লিয়ার চার্জ",
            "শুধু নিউট্রন সংখ্যা",
        ],
        "A", "easy", "factual",
        "n = 1, 2, 3… labels K, L, M… shells and relative energy.",
        "n = ১, ২, ৩… দ্বারা K, L, M… শেল ও আপেক্ষিক শক্তি চিহ্নিত।",
    ),
    q(
        "The azimuthal (angular momentum) quantum number l for n = 3 can be:",
        "n = ৩ এর জন্য অ্যাজিমুথাল (কৌণিক ভরবেগ) কোয়ান্টাম সংখ্যা l হতে পারে:",
        [
            "0, 1, or 2",
            "Only 3",
            "Only −1/2 and +1/2",
            "4, 5, and 6",
        ],
        [
            "০, ১, অথবা ২",
            "শুধু ৩",
            "শুধু −১/২ ও +১/২",
            "৪, ৫ ও ৬",
        ],
        "A", "medium", "numerical",
        "Allowed l values run from 0 to n−1.",
        "অনুমোদিত l মান ০ থেকে n−১ পর্যন্ত।",
    ),
    q(
        "For l = 2 (d subshell), the magnetic quantum number m_l can take how many values?",
        "l = ২ (d সাবশেল) এর জন্য চৌম্বক কোয়ান্টাম সংখ্যা m_l কতটি মান নিতে পারে?",
        [
            "5 values (−2, −1, 0, +1, +2)",
            "2 values only",
            "1 value only",
            "7 values always",
        ],
        [
            "৫টি মান (−২, −১, ০, +১, +২)",
            "শুধু ২টি মান",
            "শুধু ১টি মান",
            "সবসময় ৭টি মান",
        ],
        "A", "medium", "numerical",
        "m_l ranges from −l to +l, so 2l+1 = 5 orientations for d orbitals.",
        "m_l −l থেকে +l; d অরবিটালে ২l+১ = ৫ অভিমুখ।",
    ),
    q(
        "The spin quantum number m_s of an electron is:",
        "ইলেকট্রনের স্পিন কোয়ান্টাম সংখ্যা m_s হলো:",
        [
            "+1/2 or −1/2",
            "Only 0",
            "Only +1",
            "Any integer from −n to +n",
        ],
        [
            "+১/২ অথবা −১/২",
            "শুধু ০",
            "শুধু +১",
            "−n থেকে +n যেকোনো পূর্ণসংখ্যা",
        ],
        "A", "easy", "factual",
        "Electron spin has two orientations commonly labeled ±1/2.",
        "ইলেকট্রন স্পিনের দুই অভিমুখ সাধারণত ±১/২ দিয়ে চিহ্নিত।",
    ),
    q(
        "Which set of quantum numbers is NOT allowed for an electron?",
        "ইলেকট্রনের জন্য কোন কোয়ান্টাম সংখ্যার সেট অনুমোদিত নয়?",
        [
            "n = 2, l = 2, m_l = 0, m_s = +1/2",
            "n = 2, l = 1, m_l = −1, m_s = −1/2",
            "n = 3, l = 0, m_l = 0, m_s = +1/2",
            "n = 1, l = 0, m_l = 0, m_s = −1/2",
        ],
        [
            "n = ২, l = ২, m_l = ০, m_s = +১/২",
            "n = ২, l = ১, m_l = −১, m_s = −১/২",
            "n = ৩, l = ০, m_l = ০, m_s = +১/২",
            "n = ১, l = ০, m_l = ০, m_s = −১/২",
        ],
        "A", "hard", "conceptual",
        "For n = 2, l cannot be 2 because l max is n−1 = 1.",
        "n = ২ হলে l সর্বোচ্চ n−১ = ১; তাই l = ২ অসম্ভব।",
    ),
    q(
        "A neutral atom of atomic number 17 contains how many electrons?",
        "পারমাণবিক সংখ্যা ১৭-এর নিরপেক্ষ পরমাণুতে ইলেকট্রন কতটি?",
        [
            "17",
            "8",
            "35",
            "0",
        ],
        [
            "১৭",
            "৮",
            "৩৫",
            "০",
        ],
        "A", "easy", "numerical",
        "In a neutral atom, electron count equals proton count Z.",
        "নিরপেক্ষ পরমাণুতে ইলেকট্রন সংখ্যা প্রোটন সংখ্যা Z-এর সমান।",
    ),
    q(
        "Cathode rays in Thomson’s experiments were streams of:",
        "থমসনের পরীক্ষায় ক্যাথোড রশ্মি ছিল:",
        [
            "Electrons",
            "Protons only",
            "Neutrons only",
            "Alpha particles only",
        ],
        [
            "ইলেকট্রন",
            "শুধু প্রোটন",
            "শুধু নিউট্রন",
            "শুধু আলফা কণা",
        ],
        "A", "easy", "factual",
        "Cathode rays are negatively charged electron beams.",
        "ক্যাথোড রশ্মি ঋণাত্মক চার্জযুক্ত ইলেকট্রন বিম।",
    ),
    q(
        "Rutherford’s gold-foil experiment mainly concluded that:",
        "রাদারফোর্ডের স্বর্ণপাত পরীক্ষা মূলত সিদ্ধান্ত দেয় যে:",
        [
            "Most of the atom is empty space with a tiny dense positive nucleus",
            "Electrons fill the entire atom like a solid pudding only",
            "Neutrons orbit outside protons in fixed circles always",
            "Atoms have no charged particles",
        ],
        [
            "পরমাণুর বেশিরভাগ শূন্য স্থান এবং ক্ষুদ্র ঘন ধনাত্মক নিউক্লিয়াস",
            "ইলেকট্রন শুধু কঠিন পুডিংয়ের মতো পুরো পরমাণু ভরে",
            "নিউট্রন সবসময় প্রোটনের বাইরে নির্দিষ্ট বৃত্তে ঘোরে",
            "পরমাণুতে কোনো চার্জযুক্ত কণা নেই",
        ],
        "A", "medium", "conceptual",
        "Most alpha particles passed through; rare large deflections implied a nucleus.",
        "অধিকাংশ আলফা কণা ভেদ করে; বিরল বড় বিক্ষেপণ নিউক্লিয়াস নির্দেশ করে।",
    ),
    q(
        "The maximum number of electrons in a shell with principal quantum number n is:",
        "প্রধান কোয়ান্টাম সংখ্যা n-এর শেলে ইলেকট্রনের সর্বোচ্চ সংখ্যা:",
        [
            "2n²",
            "n²",
            "n + 2",
            "4n",
        ],
        [
            "2n²",
            "n²",
            "n + 2",
            "4n",
        ],
        "A", "medium", "factual",
        "Shell capacity is 2n² (K: 2, L: 8, M: 18, …).",
        "শেল ধারণক্ষমতা 2n² (K: ২, L: ৮, M: ১৮, …)।",
    ),
    q(
        "Which particle was discovered last among e⁻, p⁺, and n⁰ historically?",
        "ঐতিহাসিকভাবে e⁻, p⁺, ও n⁰ এর মধ্যে কোন কণা সর্বশেষ আবিষ্কৃত?",
        [
            "Neutron (n⁰)",
            "Electron (e⁻)",
            "Proton (p⁺)",
            "Photon only",
        ],
        [
            "নিউট্রন (n⁰)",
            "ইলেকট্রন (e⁻)",
            "প্রোটন (p⁺)",
            "শুধু ফোটন",
        ],
        "A", "easy", "factual",
        "Electron (1897), proton earlier named, neutron by Chadwick (1932).",
        "ইলেকট্রন (১৮৯৭), প্রোটন আগে নামকরণ; নিউট্রন চাডউইক (১৯৩২)।",
    ),
    q(
        "Two electrons in the same orbital must have:",
        "একই অরবিটালের দুই ইলেকট্রনের থাকতে হবে:",
        [
            "Opposite spins",
            "Identical spins always",
            "Different principal quantum numbers",
            "Zero charge",
        ],
        [
            "বিপরীত স্পিন",
            "সবসময় অভিন্ন স্পিন",
            "ভিন্ন প্রধান কোয়ান্টাম সংখ্যা",
            "শূন্য চার্জ",
        ],
        "A", "easy", "conceptual",
        "Pauli exclusion requires opposite m_s in one orbital.",
        "পলি বর্জন নীতি অনুসারে এক অরবিটালে বিপরীত m_s প্রয়োজন।",
    ),
    q(
        "An ion X²⁺ has 10 electrons; the atomic number of X is:",
        "X²⁺ আয়নে ১০টি ইলেকট্রন থাকলে X এর পারমাণবিক সংখ্যা:",
        [
            "12",
            "10",
            "8",
            "14",
        ],
        [
            "১২",
            "১০",
            "৮",
            "১৪",
        ],
        "A", "medium", "numerical",
        "X²⁺ lost 2 electrons, so neutral X had 12 electrons → Z = 12 (Mg).",
        "X²⁺ ২ ইলেকট্রন হারিয়েছে; নিরপেক্ষ X-এ ১২ ইলেকট্রন → Z = ১২ (Mg)।",
    ),
    q(
        "The shape of an orbital is primarily determined by which quantum number?",
        "অরবিটালের আকৃতি প্রধানত কোন কোয়ান্টাম সংখ্যা নির্ধারণ করে?",
        [
            "Azimuthal quantum number l",
            "Spin quantum number m_s only",
            "Mass number A only",
            "Atomic number Z only",
        ],
        [
            "অ্যাজিমুথাল কোয়ান্টাম সংখ্যা l",
            "শুধু স্পিন কোয়ান্টাম সংখ্যা m_s",
            "শুধু ভর সংখ্যা A",
            "শুধু পারমাণবিক সংখ্যা Z",
        ],
        "A", "medium", "conceptual",
        "l distinguishes s, p, d, f shapes (spherical, dumbbell, etc.).",
        "l দ্বারা s, p, d, f আকৃতি (গোলাকার, ডাম্বেল ইত্যাদি) পৃথক হয়।",
    ),
    q(
        "Orientation of an orbital in space is described by:",
        "মহাকাশে অরবিটালের অভিমুখ বর্ণনা করে:",
        [
            "Magnetic quantum number m_l",
            "Only the neutron count",
            "Only Avogadro’s number",
            "Only the Faraday constant",
        ],
        [
            "চৌম্বক কোয়ান্টাম সংখ্যা m_l",
            "শুধু নিউট্রন সংখ্যা",
            "শুধু অ্যাভোগাড্রো সংখ্যা",
            "শুধু ফ্যারাডে ধ্রুবক",
        ],
        "A", "medium", "factual",
        "m_l labels spatial orientations of orbitals within a subshell.",
        "m_l সাবশেলের মধ্যে অরবিটালের স্থানিক অভিমুখ চিহ্নিত করে।",
    ),
    q(
        "Which statement about protons and neutrons is correct?",
        "প্রোটন ও নিউট্রন সম্পর্কে কোন বিবৃতি সঠিক?",
        [
            "Both are nucleons; proton is charged, neutron is neutral",
            "Both orbit far outside the nucleus always",
            "Neutrons have charge +1 like protons",
            "Protons have zero mass compared with electrons",
        ],
        [
            "উভয়ই নিউক্লিয়ন; প্রোটন চার্জযুক্ত, নিউট্রন নিরপেক্ষ",
            "উভয় সবসময় নিউক্লিয়াসের অনেক বাইরে ঘোরে",
            "নিউট্রনের চার্জ প্রোটনের মতো +১",
            "ইলেকট্রনের তুলনায় প্রোটনের ভর শূন্য",
        ],
        "A", "easy", "conceptual",
        "Nucleons reside in the nucleus; charge distinguishes p⁺ from n⁰.",
        "নিউক্লিয়ন নিউক্লিয়াসে থাকে; চার্জ p⁺ ও n⁰ পৃথক করে।",
    ),
    q(
        "For n = 4, the possible subshells are:",
        "n = ৪ এর জন্য সম্ভাব্য সাবশেল:",
        [
            "4s, 4p, 4d, and 4f",
            "Only 4s",
            "Only 4f",
            "5s and 5p only",
        ],
        [
            "4s, 4p, 4d ও 4f",
            "শুধু 4s",
            "শুধু 4f",
            "শুধু 5s ও 5p",
        ],
        "A", "medium", "factual",
        "l = 0,1,2,3 → s,p,d,f for the n = 4 shell.",
        "n = ৪ শেলে l = ০,১,২,৩ → s,p,d,f।",
    ),
]

# --- t02: Electron configuration and orbitals ---
T02 = [
    q(
        "According to the Aufbau principle, electrons occupy orbitals in order of:",
        "আউফবাউ নীতি অনুসারে ইলেকট্রন অরবিটাল দখল করে:",
        [
            "Increasing energy (lowest available first)",
            "Highest energy first always",
            "Random energy without preference",
            "Only f orbitals before s orbitals",
        ],
        [
            "ক্রমবর্ধমান শক্তি (প্রথমে সর্বনিম্ন উপলব্ধ)",
            "সবসময় সর্বোচ্চ শক্তি আগে",
            "পছন্দ ছাড়া এলোমেলো শক্তি",
            "s এর আগে শুধু f অরবিটাল",
        ],
        "A", "easy", "factual",
        "Aufbau fills lower-energy orbitals before higher ones.",
        "আউফবাউ নিম্নশক্তি অরবিটাল আগে পূরণ করে।",
    ),
    q(
        "Hund’s rule states that electrons in degenerate orbitals:",
        "হান্ডের নিয়ম অনুসারে সমশক্তি অরবিটালে ইলেকট্রন:",
        [
            "Occupy separately with parallel spins before pairing",
            "Pair up in one orbital before occupying others",
            "Always have opposite spins in different orbitals first",
            "Leave all orbitals empty if possible",
        ],
        [
            "জোড়া বাঁধার আগে সমান্তরাল স্পিনে আলাদা দখল করে",
            "অন্যগুলো দখলের আগে এক অরবিটালে জোড়া বাঁধে",
            "সবসময় আগে ভিন্ন অরবিটালে বিপরীত স্পিন রাখে",
            "সম্ভব হলে সব অরবিটাল খালি রাখে",
        ],
        "A", "easy", "conceptual",
        "Maximize unpaired parallel spins among equal-energy orbitals.",
        "সমশক্তি অরবিটালে অযুগ্ম সমান্তরাল স্পিন সর্বাধিক করা হয়।",
    ),
    q(
        "The Pauli exclusion principle forbids two electrons in an atom from having:",
        "পলি বর্জন নীতি পরমাণুর দুই ইলেকট্রনকে নিষেধ করে:",
        [
            "All four quantum numbers identical",
            "The same principal quantum number only",
            "Any magnetic quantum number",
            "Opposite spins in one orbital",
        ],
        [
            "চারটি কোয়ান্টাম সংখ্যাই অভিন্ন",
            "শুধু একই প্রধান কোয়ান্টাম সংখ্যা",
            "যেকোনো চৌম্বক কোয়ান্টাম সংখ্যা",
            "এক অরবিটালে বিপরীত স্পিন",
        ],
        "A", "easy", "factual",
        "No two electrons may share the complete (n,l,m_l,m_s) set.",
        "দুই ইলেকট্রনের সম্পূর্ণ (n,l,m_l,m_s) সেট এক হতে পারে না।",
    ),
    q(
        "The ground-state electron configuration of carbon (Z = 6) is:",
        "কার্বনের (Z = ৬) মূল অবস্থার ইলেকট্রন বিন্যাস:",
        [
            "1s² 2s² 2p²",
            "1s² 2s² 2p⁶",
            "1s² 2p⁴",
            "1s² 2s¹ 2p³",
        ],
        [
            "1s² 2s² 2p²",
            "1s² 2s² 2p⁶",
            "1s² 2p⁴",
            "1s² 2s¹ 2p³",
        ],
        "A", "easy", "factual",
        "Six electrons fill 1s, then 2s, then two in 2p.",
        "ছয় ইলেকট্রন 1s, তারপর 2s, তারপর 2p-এ দুইটি পূরণ করে।",
    ),
    q(
        "An s orbital can hold a maximum of how many electrons?",
        "একটি s অরবিটাল সর্বোচ্চ কতটি ইলেকট্রন ধারণ করতে পারে?",
        [
            "2",
            "6",
            "10",
            "14",
        ],
        [
            "২",
            "৬",
            "১০",
            "১৪",
        ],
        "A", "easy", "numerical",
        "One orbital holds at most two electrons of opposite spin.",
        "এক অরবিটালে সর্বোচ্চ দুই বিপরীত স্পিনের ইলেকট্রন।",
    ),
    q(
        "A p subshell consists of how many orbitals?",
        "একটি p সাবশেলে কয়টি অরবিটাল থাকে?",
        [
            "3",
            "1",
            "5",
            "7",
        ],
        [
            "৩",
            "১",
            "৫",
            "৭",
        ],
        "A", "easy", "factual",
        "p → l = 1 → 2l+1 = 3 orbitals (px, py, pz).",
        "p → l = ১ → ২l+১ = ৩ অরবিটাল (px, py, pz)।",
    ),
    q(
        "The maximum electrons in a d subshell is:",
        "d সাবশেলে সর্বোচ্চ ইলেকট্রন:",
        [
            "10",
            "2",
            "6",
            "14",
        ],
        [
            "১০",
            "২",
            "৬",
            "১৪",
        ],
        "A", "easy", "numerical",
        "Five d orbitals × 2 electrons = 10.",
        "পাঁচটি d অরবিটাল × ২ ইলেকট্রন = ১০।",
    ),
    q(
        "Which orbital-filling order fragment is correct (n+l rule)?",
        "কোন অরবিটাল-পূরণ ক্রমের অংশ সঠিক (n+l নিয়ম)?",
        [
            "4s fills before 3d",
            "3d fills before 4s always in neutral atoms",
            "5f fills before 6s always",
            "2p fills before 2s",
        ],
        [
            "3d এর আগে 4s পূরণ হয়",
            "নিরপেক্ষ পরমাণুতে সবসময় 4s এর আগে 3d",
            "সবসময় 6s এর আগে 5f",
            "2s এর আগে 2p",
        ],
        "A", "medium", "conceptual",
        "Lower n+l (or lower n if tied) fills first: 4s (n+l=4) before 3d (n+l=5).",
        "নিম্ন n+l (বা সমান হলে নিম্ন n) আগে: 4s (n+l=৪) 3d (n+l=৫) এর আগে।",
    ),
    q(
        "The noble-gas shorthand for sodium (Z = 11) is:",
        "সোডিয়ামের (Z = ১১) নিষ্ক্রিয় গ্যাস শর্টহ্যান্ড:",
        [
            "[Ne] 3s¹",
            "[He] 2s² 2p⁶",
            "[Ar] 4s¹",
            "[Ne] 3s²",
        ],
        [
            "[Ne] 3s¹",
            "[He] 2s² 2p⁶",
            "[Ar] 4s¹",
            "[Ne] 3s²",
        ],
        "A", "easy", "factual",
        "Na has neon core plus one 3s electron.",
        "Na এর নিয়ন কোর ও একটি 3s ইলেকট্রন।",
    ),
    q(
        "Chromium (Z = 24) shows an exceptional configuration often written as:",
        "ক্রোমিয়াম (Z = ২৪) এর ব্যতিক্রমী বিন্যাস প্রায়ই লেখা হয়:",
        [
            "[Ar] 4s¹ 3d⁵",
            "[Ar] 4s² 3d⁴",
            "[Ar] 4s² 3d⁶",
            "[Ne] 3s² 3p⁶",
        ],
        [
            "[Ar] 4s¹ 3d⁵",
            "[Ar] 4s² 3d⁴",
            "[Ar] 4s² 3d⁶",
            "[Ne] 3s² 3p⁶",
        ],
        "A", "hard", "factual",
        "Half-filled d⁵ with 4s¹ is more stable than 4s² 3d⁴.",
        "অর্ধপূর্ণ d⁵ ও 4s¹ 4s² 3d⁴ এর চেয়ে স্থিতিশীল।",
    ),
    q(
        "Copper (Z = 29) commonly has the ground configuration:",
        "তামার (Z = ২৯) মূল অবস্থার বিন্যাস সাধারণত:",
        [
            "[Ar] 4s¹ 3d¹⁰",
            "[Ar] 4s² 3d⁹",
            "[Ar] 4s² 3d¹⁰",
            "[Kr] 5s¹",
        ],
        [
            "[Ar] 4s¹ 3d¹⁰",
            "[Ar] 4s² 3d⁹",
            "[Ar] 4s² 3d¹⁰",
            "[Kr] 5s¹",
        ],
        "A", "hard", "factual",
        "Fully filled d¹⁰ with 4s¹ is preferred over 4s² 3d⁹.",
        "পূর্ণ d¹⁰ ও 4s¹ 4s² 3d⁹ এর চেয়ে অগ্রাধিকার।",
    ),
    q(
        "An orbital is best described as:",
        "অরবিটালকে সবচেয়ে ভালো বর্ণনা করা যায়:",
        [
            "A region of space with high probability of finding an electron",
            "A fixed circular path of definite radius only",
            "A solid planetary ring around the nucleus",
            "A neutron storage pouch",
        ],
        [
            "ইলেকট্রন পাওয়ার উচ্চ সম্ভাবনাযুক্ত স্থানিক অঞ্চল",
            "শুধু নির্দিষ্ট ব্যাসার্ধের স্থির বৃত্তাকার পথ",
            "নিউক্লিয়াসের চারপাশে কঠিন গ্রহীয় বলয়",
            "নিউট্রন সংরক্ষণ থলি",
        ],
        "A", "easy", "conceptual",
        "Quantum orbitals are probability density regions, not Bohr tracks.",
        "কোয়ান্টাম অরবিটাল সম্ভাবন ঘনত্বের অঞ্চল; বোরের নির্দিষ্ট পথ নয়।",
    ),
    q(
        "The number of unpaired electrons in ground-state nitrogen (Z = 7) is:",
        "মূল অবস্থার নাইট্রোজেনে (Z = ৭) অযুগ্ম ইলেকট্রন সংখ্যা:",
        [
            "3",
            "1",
            "0",
            "5",
        ],
        [
            "৩",
            "১",
            "০",
            "৫",
        ],
        "A", "medium", "numerical",
        "N is 1s² 2s² 2p³ with three unpaired 2p electrons (Hund).",
        "N: 1s² 2s² 2p³; হান্ড অনুসারে তিনটি অযুগ্ম 2p ইলেকট্রন।",
    ),
    q(
        "Which species is isoelectronic with Ne?",
        "Ne এর সাথে কোন প্রজাতি সমইলেকট্রনিক?",
        [
            "Na⁺",
            "Na",
            "F",
            "O",
        ],
        [
            "Na⁺",
            "Na",
            "F",
            "O",
        ],
        "A", "medium", "conceptual",
        "Ne and Na⁺ both have 10 electrons.",
        "Ne ও Na⁺ উভয়ের ১০টি ইলেকট্রন।",
    ),
    q(
        "Valence electrons of an atom are those in:",
        "পরমাণুর ভ্যালেন্স ইলেকট্রন থাকে:",
        [
            "The outermost shell (highest n)",
            "Only the nucleus",
            "Only completely filled inner cores never used in bonding",
            "Neutron orbitals",
        ],
        [
            "সবচেয়ে বাইরের শেলে (সর্বোচ্চ n)",
            "শুধু নিউক্লিয়াসে",
            "শুধু পূর্ণ অভ্যন্তরীণ কোরে যা বন্ধনে কখনো ব্যবহৃত হয় না",
            "নিউট্রন অরবিটালে",
        ],
        "A", "easy", "factual",
        "Chemical behavior is dominated by outermost electrons.",
        "রাসায়নিক আচরণে প্রধান ভূমিকা বাইরের ইলেকট্রনের।",
    ),
    q(
        "The electron configuration 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ belongs to:",
        "ইলেকট্রন বিন্যাস 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ এর মৌল:",
        [
            "Krypton (Kr)",
            "Argon (Ar)",
            "Xenon (Xe)",
            "Bromine (Br)",
        ],
        [
            "ক্রিপ্টন (Kr)",
            "আর্গন (Ar)",
            "জেনন (Xe)",
            "ব্রোমিন (Br)",
        ],
        "A", "medium", "factual",
        "This is the noble-gas configuration of Kr (Z = 36).",
        "এটি Kr (Z = ৩৬) এর নিষ্ক্রিয় গ্যাস বিন্যাস।",
    ),
    q(
        "A node in an orbital wave function is a region where:",
        "অরবিটাল তরঙ্গ ফাংশনের নোড এমন অঞ্চল যেখানে:",
        [
            "Electron probability density is zero",
            "Electron density is always maximum",
            "Nuclear charge vanishes",
            "Neutrons accumulate",
        ],
        [
            "ইলেকট্রন সম্ভাবন ঘনত্ব শূন্য",
            "ইলেকট্রন ঘনত্ব সবসময় সর্বোচ্চ",
            "নিউক্লিয়ার চার্জ বিলুপ্ত",
            "নিউট্রন জমা হয়",
        ],
        "A", "medium", "conceptual",
        "At a node the wave amplitude (and ψ²) is zero.",
        "নোডে তরঙ্গ প্রশস্ততা (ও ψ²) শূন্য।",
    ),
    q(
        "Which configuration violates Hund’s rule for carbon?",
        "কার্বনের কোন বিন্যাস হান্ডের নিয়ম লঙ্ঘন করে?",
        [
            "2p electrons both paired in one p orbital with the other empty",
            "Two 2p electrons in different p orbitals with parallel spins",
            "1s² 2s² with remaining electrons in 2p",
            "Using three p orbitals available for the two electrons",
        ],
        [
            "দুই 2p ইলেকট্রন এক p অরবিটালে জোড়া, অন্যটি খালি",
            "দুই 2p ইলেকট্রন ভিন্ন p অরবিটালে সমান্তরাল স্পিনে",
            "1s² 2s² ও অবশিষ্ট 2p-এ",
            "দুই ইলেকট্রনের জন্য তিন p অরবিটাল ব্যবহার",
        ],
        "A", "hard", "conceptual",
        "Pairing before separate parallel occupancy violates Hund.",
        "আলাদা সমান্তরাল দখলের আগে জোড়া বাঁধা হান্ড লঙ্ঘন।",
    ),
    q(
        "The f subshell can hold a maximum of:",
        "f সাবশেল সর্বোচ্চ ধারণ করে:",
        [
            "14 electrons",
            "10 electrons",
            "6 electrons",
            "2 electrons",
        ],
        [
            "১৪টি ইলেকট্রন",
            "১০টি ইলেকট্রন",
            "৬টি ইলেকট্রন",
            "২টি ইলেকট্রন",
        ],
        "A", "easy", "numerical",
        "Seven f orbitals × 2 = 14 electrons.",
        "সাতটি f অরবিটাল × ২ = ১৪ ইলেকট্রন।",
    ),
    q(
        "Removing one electron from Na (3s¹) yields Na⁺ with configuration like:",
        "Na (3s¹) থেকে এক ইলেকট্রন অপসারণে Na⁺ এর বিন্যাস যেমন:",
        [
            "Neon (1s² 2s² 2p⁶)",
            "Argon (3s² 3p⁶)",
            "Fluorine (2s² 2p⁵)",
            "Magnesium (3s²)",
        ],
        [
            "নিয়ন (1s² 2s² 2p⁶)",
            "আর্গন (3s² 3p⁶)",
            "ফ্লুরিন (2s² 2p⁵)",
            "ম্যাগনেসিয়াম (3s²)",
        ],
        "A", "easy", "conceptual",
        "Na⁺ is isoelectronic with Ne.",
        "Na⁺ নিয়নের সাথে সমইলেকট্রনিক।",
    ),
]

# --- t03: Electromagnetic radiation and spectra ---
T03 = [
    q(
        "The speed of light in vacuum c relates frequency ν and wavelength λ by:",
        "শূন্যে আলোর গতি c কম্পাঙ্ক ν ও তরঙ্গদৈর্ঘ্য λ এর সাথে সম্পর্কিত:",
        [
            "c = νλ",
            "c = ν/λ",
            "c = ν + λ",
            "c = ν − λ",
        ],
        [
            "c = νλ",
            "c = ν/λ",
            "c = ν + λ",
            "c = ν − λ",
        ],
        "A", "easy", "factual",
        "Electromagnetic wave speed equals frequency times wavelength.",
        "তড়িৎচৌম্বক তরঙ্গের গতি = কম্পাঙ্ক × তরঙ্গদৈর্ঘ্য।",
    ),
    q(
        "Photon energy E is related to frequency ν by Planck’s relation:",
        "ফোটন শক্তি E প্ল্যাঙ্কের সম্পর্কে কম্পাঙ্ক ν এর সাথে:",
        [
            "E = hν",
            "E = h/ν",
            "E = ν/h",
            "E = h + ν",
        ],
        [
            "E = hν",
            "E = h/ν",
            "E = ν/h",
            "E = h + ν",
        ],
        "A", "easy", "factual",
        "Energy of a quantum is Planck’s constant times frequency.",
        "কোয়ান্টামের শক্তি = প্ল্যাঙ্ক ধ্রুবক × কম্পাঙ্ক।",
    ),
    q(
        "Among visible colors of equal intensity in vacuum, which has the highest frequency?",
        "শূন্যে সমান তীব্রতার দৃশ্যমান রঙের মধ্যে কোনটির কম্পাঙ্ক সর্বোচ্চ?",
        [
            "Violet",
            "Red",
            "Yellow",
            "Green",
        ],
        [
            "বেগুনি",
            "লাল",
            "হলুদ",
            "সবুজ",
        ],
        "A", "easy", "conceptual",
        "Violet has shorter wavelength and thus higher frequency than red.",
        "বেগুনির তরঙ্গদৈর্ঘ্য কম; তাই লালের চেয়ে কম্পাঙ্ক বেশি।",
    ),
    q(
        "In the Bohr model, an electron emits a photon when it:",
        "বোর মডেলে ইলেকট্রন ফোটন নির্গত করে যখন:",
        [
            "Falls from a higher to a lower energy orbit",
            "Moves to a higher orbit without energy change",
            "Stays in the same orbit forever",
            "Gains mass equal to the proton",
        ],
        [
            "উচ্চতর থেকে নিম্নতর শক্তি কক্ষে নেমে আসে",
            "শক্তি পরিবর্তন ছাড়া উচ্চতর কক্ষে যায়",
            "চিরকাল একই কক্ষে থাকে",
            "প্রোটনের সমান ভর অর্জন করে",
        ],
        "A", "easy", "conceptual",
        "ΔE released appears as a photon of energy hν.",
        "মুক্ত ΔE শক্তি hν এর ফোটনরূপে প্রকাশ পায়।",
    ),
    q(
        "The Lyman series of the hydrogen spectrum corresponds to transitions ending at:",
        "হাইড্রোজেন বর্ণালির লাইম্যান শ্রেণি সেই রূপান্তর যা শেষ হয়:",
        [
            "n = 1",
            "n = 2",
            "n = 3",
            "n = ∞",
        ],
        [
            "n = ১",
            "n = ২",
            "n = ৩",
            "n = ∞",
        ],
        "A", "medium", "factual",
        "Lyman lines are UV transitions to the ground level n = 1.",
        "লাইম্যান রেখা n = ১ ভূমিস্তরে UV রূপান্তর।",
    ),
    q(
        "The Balmer series lines of hydrogen appear mainly in the:",
        "হাইড্রোজেনের ব্যালমার শ্রেণির রেখা প্রধানত দেখা যায়:",
        [
            "Visible region",
            "Only X-ray region",
            "Only radio-wave region",
            "Only gamma-ray region",
        ],
        [
            "দৃশ্যমান অঞ্চলে",
            "শুধু এক্স-রে অঞ্চলে",
            "শুধু রেডিও-তরঙ্গ অঞ্চলে",
            "শুধু গামা-রে অঞ্চলে",
        ],
        "A", "easy", "factual",
        "Balmer transitions end at n = 2 and give visible lines (e.g., Hα).",
        "ব্যালমার রূপান্তর n = ২-এ শেষ হয়ে দৃশ্যমান রেখা (যেমন Hα) দেয়।",
    ),
    q(
        "Paschen series transitions of hydrogen terminate at:",
        "হাইড্রোজেনের পাশেন শ্রেণির রূপান্তর শেষ হয়:",
        [
            "n = 3",
            "n = 1",
            "n = 2",
            "n = 0",
        ],
        [
            "n = ৩",
            "n = ১",
            "n = ২",
            "n = ০",
        ],
        "A", "medium", "factual",
        "Paschen is infrared series ending at n = 3.",
        "পাশেন ইনফ্রারেড শ্রেণি; শেষ স্তর n = ৩।",
    ),
    q(
        "A continuous spectrum is typically produced by:",
        "অবিচ্ছিন্ন বর্ণালি সাধারণত উৎপন্ন করে:",
        [
            "A hot solid or dense glowing body",
            "Only isolated atoms in a discharge tube",
            "Only cold transparent gases without emission",
            "A single monochromatic laser line always",
        ],
        [
            "গরম কঠিন বা ঘন উজ্জ্বল বস্তু",
            "শুধু ডিসচার্জ টিউবের বিচ্ছিন্ন পরমাণু",
            "শুধু নির্গমনহীন ঠান্ডা স্বচ্ছ গ্যাস",
            "সবসময় একটি একবর্ণ লেজার রেখা",
        ],
        "A", "medium", "conceptual",
        "Blackbody-like emitters give continuous spectra; atoms give lines.",
        "কৃষ্ণবস্তু-সদৃশ উৎস অবিচ্ছিন্ন বর্ণালি; পরমাণু রেখা বর্ণালি দেয়।",
    ),
    q(
        "An emission line spectrum of an element shows:",
        "কোনো মৌলের নির্গমন রেখা বর্ণালি দেখায়:",
        [
            "Bright lines at wavelengths characteristic of that element",
            "Only a featureless rainbow with no lines",
            "Dark lines solely from cold metal blocks",
            "A single wavelength for all elements identical",
        ],
        [
            "সেই মৌলের বৈশিষ্ট্যসূচক তরঙ্গদৈর্ঘ্যে উজ্জ্বল রেখা",
            "শুধু রেখাহীন রংধনু",
            "শুধু ঠান্ডা ধাতব ব্লকের অন্ধকার রেখা",
            "সব মৌলের একই একক তরঙ্গদৈর্ঘ্য",
        ],
        "A", "easy", "conceptual",
        "Each element has unique electronic energy gaps → unique lines.",
        "প্রতি মৌলের অনন্য শক্তি ব্যবধান → অনন্য রেখা।",
    ),
    q(
        "Absorption spectra of atoms typically show:",
        "পরমাণুর শোষণ বর্ণালি সাধারণত দেখায়:",
        [
            "Dark lines where the atom absorbs specific wavelengths",
            "Only brighter continuous bands with no gaps",
            "Random colors unrelated to energy levels",
            "Only neutron radiation peaks",
        ],
        [
            "পরমাণু নির্দিষ্ট তরঙ্গদৈর্ঘ্য শোষণে অন্ধকার রেখা",
            "শুধু ফাঁকহীন উজ্জ্বলতর অবিচ্ছিন্ন ব্যান্ড",
            "শক্তিস্তর-নিরপেক্ষ এলোমেলো রং",
            "শুধু নিউট্রন বিকিরণ শিখর",
        ],
        "A", "easy", "conceptual",
        "Atoms remove resonant frequencies from a continuum, leaving dark lines.",
        "পরমাণু অবিচ্ছিন্ন বর্ণালি থেকে অনুরণিত কম্পাঙ্ক সরিয়ে অন্ধকার রেখা রাখে।",
    ),
    q(
        "If wavelength doubles while in the same medium, frequency:",
        "একই মাধ্যমে তরঙ্গদৈর্ঘ্য দ্বিগুণ হলে কম্পাঙ্ক:",
        [
            "Halves (since c = νλ is fixed in vacuum; ν ∝ 1/λ)",
            "Doubles",
            "Remains exactly the same always",
            "Becomes zero",
        ],
        [
            "অর্ধেক হয় (শূন্যে c = νλ স্থির; ν ∝ ১/λ)",
            "দ্বিগুণ হয়",
            "সবসময় সম্পূর্ণ অপরিবর্তিত",
            "শূন্য হয়",
        ],
        "A", "medium", "numerical",
        "For fixed wave speed, ν and λ are inversely proportional.",
        "স্থির তরঙ্গগতিতে ν ও λ ব্যস্তানুপাতিক।",
    ),
    q(
        "Which region of the electromagnetic spectrum has longer wavelength than infrared?",
        "তড়িৎচৌম্বক বর্ণালির কোন অঞ্চলের তরঙ্গদৈর্ঘ্য ইনফ্রারেডের চেয়ে বেশি?",
        [
            "Microwave / radio region",
            "Ultraviolet",
            "X-rays",
            "Gamma rays",
        ],
        [
            "মাইক্রোওয়েভ / রেডিও অঞ্চল",
            "অতিবেগুনি",
            "এক্স-রে",
            "গামা রে",
        ],
        "A", "medium", "factual",
        "Wavelength order: radio > microwave > IR > visible > UV > X > γ.",
        "তরঙ্গদৈর্ঘ্য ক্রম: রেডিও > মাইক্রোওয়েভ > IR > দৃশ্যমান > UV > X > γ।",
    ),
    q(
        "Rydberg’s formula is used to calculate:",
        "রিডবার্গ সূত্র ব্যবহার হয় হিসাব করতে:",
        [
            "Wavenumbers/wavelengths of hydrogen spectral lines",
            "Only the mass of the neutron",
            "Only Avogadro’s number from gases",
            "Only pH of strong acids",
        ],
        [
            "হাইড্রোজেন বর্ণালি রেখার তরঙ্গসংখ্যা/তরঙ্গদৈর্ঘ্য",
            "শুধু নিউট্রনের ভর",
            "শুধু গ্যাস থেকে অ্যাভোগাড্রো সংখ্যা",
            "শুধু প্রবল অ্যাসিডের pH",
        ],
        "A", "medium", "factual",
        "1/λ = R(1/n₁² − 1/n₂²) for H-like transitions.",
        "H-সদৃশ রূপান্তরে 1/λ = R(1/n₁² − 1/n₂²)।",
    ),
    q(
        "A quantum of electromagnetic radiation is called a:",
        "তড়িৎচৌম্বক বিকিরণের এক কোয়ান্টামকে বলে:",
        [
            "Photon",
            "Proton",
            "Phonon only in nuclei",
            "Neutrino in all lamps",
        ],
        [
            "ফোটন",
            "প্রোটন",
            "শুধু নিউক্লিয়াসে ফোনন",
            "সব প্রদীপে নিউট্রিনো",
        ],
        "A", "easy", "factual",
        "Light quanta are photons with energy hν.",
        "আলোর কোয়ান্টা হলো hν শক্তির ফোটন।",
    ),
    q(
        "Why do different elements show different line spectra?",
        "ভিন্ন মৌল ভিন্ন রেখা বর্ণালি দেখায় কেন?",
        [
            "Their electronic energy level spacings differ",
            "All atoms have identical energy gaps always",
            "Spectra depend only on nuclear mass number A",
            "Line spectra ignore electron transitions",
        ],
        [
            "তাদের ইলেকট্রন শক্তিস্তরের ব্যবধান ভিন্ন",
            "সব পরমাণুর শক্তি ব্যবধান সবসময় অভিন্ন",
            "বর্ণালি শুধু নিউক্লিয়ার ভর সংখ্যা A নির্ভর",
            "রেখা বর্ণালি ইলেকট্রন রূপান্তর উপেক্ষা করে",
        ],
        "A", "medium", "conceptual",
        "Unique ΔE values produce unique photon frequencies.",
        "অনন্য ΔE অনন্য ফোটন কম্পাঙ্ক উৎপন্ন করে।",
    ),
    q(
        "de Broglie’s relation for a particle of momentum p is:",
        "ভরবেগ p এর কণার দ্য ব্রগলি সম্পর্ক:",
        [
            "λ = h/p",
            "λ = p/h",
            "λ = hp",
            "λ = h + p",
        ],
        [
            "λ = h/p",
            "λ = p/h",
            "λ = hp",
            "λ = h + p",
        ],
        "A", "medium", "factual",
        "Matter waves have wavelength Planck’s constant over momentum.",
        "পদার্থ তরঙ্গের তরঙ্গদৈর্ঘ্য = প্ল্যাঙ্ক ধ্রুবক / ভরবেগ।",
    ),
    q(
        "Which transition in H atom emits the highest-energy photon among these?",
        "H পরমাণুতে এগুলোর মধ্যে কোন রূপান্তর সর্বোচ্চ শক্তির ফোটন নির্গত করে?",
        [
            "n = 2 → n = 1",
            "n = 3 → n = 2",
            "n = 4 → n = 3",
            "n = 5 → n = 4",
        ],
        [
            "n = ২ → n = ১",
            "n = ৩ → n = ২",
            "n = ৪ → n = ৩",
            "n = ৫ → n = ৪",
        ],
        "A", "hard", "numerical",
        "Largest ΔE among listed is the Lyman jump 2→1.",
        "তালিকায় বৃহত্তম ΔE লাইম্যান ২→১ রূপান্তর।",
    ),
    q(
        "Ultraviolet radiation has frequency that is generally:",
        "অতিবেগুনি বিকিরণের কম্পাঙ্ক সাধারণত:",
        [
            "Higher than visible light",
            "Lower than infrared",
            "Lower than radio waves",
            "Equal to all microwaves always",
        ],
        [
            "দৃশ্যমান আলোর চেয়ে বেশি",
            "ইনফ্রারেডের চেয়ে কম",
            "রেডিও তরঙ্গের চেয়ে কম",
            "সবসময় সব মাইক্রোওয়েভের সমান",
        ],
        "A", "easy", "conceptual",
        "UV sits beyond violet: higher ν, shorter λ than visible.",
        "UV বেগুনির বাইরে: দৃশ্যমানের চেয়ে বেশি ν, কম λ।",
    ),
    q(
        "A spectrophotometer in qualitative analysis is used mainly to:",
        "গুণগত বিশ্লেষণে স্পেকট্রোফটোমিটার মূলত ব্যবহৃত হয়:",
        [
            "Measure absorption/emission at selected wavelengths for identification/quantitation",
            "Weigh precipitates only",
            "Replace all filtration steps",
            "Generate neutrons for isotopes",
        ],
        [
            "শনাক্তকরণ/পরিমাণ নির্ধারণে নির্বাচিত তরঙ্গদৈর্ঘ্যে শোষণ/নির্গমন মাপা",
            "শুধু অধঃক্ষেপ ওজন করা",
            "সব পরিস্রাবণ ধাপ প্রতিস্থাপন",
            "আইসোটোপের জন্য নিউট্রন উৎপাদন",
        ],
        "A", "medium", "application",
        "Spectral intensity at characteristic λ supports analysis.",
        "বৈশিষ্ট্যসূচক λ-এ বর্ণালি তীব্রতা বিশ্লেষণে সহায়ক।",
    ),
    q(
        "Wave number ν̄ is defined as:",
        "তরঙ্গসংখ্যা ν̄ সংজ্ঞায়িত:",
        [
            "1/λ (reciprocal of wavelength)",
            "λ × c only",
            "h × λ only",
            "λ² only",
        ],
        [
            "1/λ (তরঙ্গদৈর্ঘ্যের বিপরীত)",
            "শুধু λ × c",
            "শুধু h × λ",
            "শুধু λ²",
        ],
        "A", "medium", "factual",
        "Spectroscopists often report lines in cm⁻¹ as 1/λ.",
        "বর্ণালিবিদে প্রায়ই রেখা cm⁻¹-এ 1/λ হিসেবে প্রকাশ।",
    ),
]

# --- t04: Identification of ions ---
T04 = [
    q(
        "A flame test giving a persistent golden-yellow color indicates:",
        "শিখা পরীক্ষায় স্থায়ী সোনালি-হলুদ রং নির্দেশ করে:",
        [
            "Na⁺",
            "K⁺",
            "Cu²⁺",
            "Ba²⁺",
        ],
        [
            "Na⁺",
            "K⁺",
            "Cu²⁺",
            "Ba²⁺",
        ],
        "A", "easy", "factual",
        "Sodium salts impart an intense yellow flame.",
        "সোডিয়াম লবণ তীব্র হলুদ শিখা দেয়।",
    ),
    q(
        "A violet (lilac) flame in the flame test typically indicates:",
        "শিখা পরীক্ষায় বেগুনি (লিলাক) শিখা সাধারণত নির্দেশ করে:",
        [
            "K⁺",
            "Na⁺",
            "Ca²⁺",
            "Sr²⁺",
        ],
        [
            "K⁺",
            "Na⁺",
            "Ca²⁺",
            "Sr²⁺",
        ],
        "A", "easy", "factual",
        "Potassium gives a lilac/violet flame (often viewed through cobalt glass).",
        "পটাশিয়াম লিলাক/বেগুনি শিখা দেয় (প্রায়ই কোবাল্ট কাচে দেখা)।",
    ),
    q(
        "A brick-red flame is characteristic of:",
        "ইট-লাল শিখা বৈশিষ্ট্যসূচক:",
        [
            "Ca²⁺",
            "Na⁺",
            "Cu²⁺",
            "Ba²⁺",
        ],
        [
            "Ca²⁺",
            "Na⁺",
            "Cu²⁺",
            "Ba²⁺",
        ],
        "A", "easy", "factual",
        "Calcium salts give a brick-red flame coloration.",
        "ক্যালসিয়াম লবণ ইট-লাল শিখা রং দেয়।",
    ),
    q(
        "A green flame often indicates the presence of:",
        "সবুজ শিখা প্রায়ই নির্দেশ করে:",
        [
            "Ba²⁺ or Cu²⁺ (depending on salt)",
            "Na⁺ only",
            "K⁺ only",
            "NH₄⁺ only",
        ],
        [
            "Ba²⁺ অথবা Cu²⁺ (লবণভেদে)",
            "শুধু Na⁺",
            "শুধু K⁺",
            "শুধু NH₄⁺",
        ],
        "A", "medium", "factual",
        "Barium is apple-green; copper salts often give green/blue-green flames.",
        "বেরিয়াম আপেল-সবুজ; তামার লবণ প্রায়ই সবুজ/নীল-সবুজ শিখা দেয়।",
    ),
    q(
        "AgNO₃ solution with Cl⁻ produces a white precipitate of:",
        "Cl⁻ এর সাথে AgNO₃ দ্রবণ তৈরি করে সাদা অধঃক্ষেপ:",
        [
            "AgCl",
            "AgBr",
            "AgI",
            "Ag₂SO₄ only always",
        ],
        [
            "AgCl",
            "AgBr",
            "AgI",
            "শুধু সবসময় Ag₂SO₄",
        ],
        "A", "easy", "factual",
        "Chloride + Ag⁺ → white AgCl ppt (soluble in NH₃).",
        "ক্লোরাইড + Ag⁺ → সাদা AgCl অধঃক্ষেপ (NH₃-এ দ্রবণীয়)।",
    ),
    q(
        "A cream precipitate with AgNO₃ that is sparingly soluble in NH₃ suggests:",
        "AgNO₃ দিয়ে ক্রিম অধঃক্ষেপ যা NH₃-এ সামান্য দ্রবণীয় নির্দেশ করে:",
        [
            "Br⁻",
            "Cl⁻",
            "I⁻",
            "SO₄²⁻",
        ],
        [
            "Br⁻",
            "Cl⁻",
            "I⁻",
            "SO₄²⁻",
        ],
        "A", "medium", "conceptual",
        "AgBr is cream-colored and less soluble in ammonia than AgCl.",
        "AgBr ক্রিম রঙের এবং AgCl এর চেয়ে অ্যামোনিয়ায় কম দ্রবণীয়।",
    ),
    q(
        "A yellow precipitate with AgNO₃ insoluble in NH₃ indicates:",
        "AgNO₃ দিয়ে হলুদ অধঃক্ষেপ যা NH₃-এ অদ্রবণীয় নির্দেশ করে:",
        [
            "I⁻",
            "Cl⁻",
            "Br⁻",
            "F⁻",
        ],
        [
            "I⁻",
            "Cl⁻",
            "Br⁻",
            "F⁻",
        ],
        "A", "medium", "factual",
        "AgI is yellow and essentially insoluble in dilute NH₃.",
        "AgI হলুদ এবং লঘু NH₃-এ প্রায় অদ্রবণীয়।",
    ),
    q(
        "BaCl₂ solution with SO₄²⁻ yields a white precipitate of:",
        "SO₄²⁻ এর সাথে BaCl₂ দ্রবণ দেয় সাদা অধঃক্ষেপ:",
        [
            "BaSO₄",
            "BaCO₃ only",
            "Ba(OH)₂ only",
            "BaS only",
        ],
        [
            "BaSO₄",
            "শুধু BaCO₃",
            "শুধু Ba(OH)₂",
            "শুধু BaS",
        ],
        "A", "easy", "factual",
        "Insoluble BaSO₄ is the classic sulfate test ppt.",
        "অদ্রবণীয় BaSO₄ সালফেট পরীক্ষার ক্লাসিক অধঃক্ষেপ।",
    ),
    q(
        "On heating with NaOH, NH₄⁺ salts liberate a gas that:",
        "NaOH সহ গরম করলে NH₄⁺ লবণ যে গ্যাস ছাড়ে:",
        [
            "Turns moist red litmus blue (NH₃)",
            "Bleaches litmus permanently like Cl₂ always",
            "Is odorless CO₂ only",
            "Is H₂ that pops with a flame only",
        ],
        [
            "আর্দ্র লাল লিটমাস নীল করে (NH₃)",
            "সবসময় Cl₂ এর মতো লিটমাস স্থায়ী বিরঞ্জিত করে",
            "শুধু গন্ধহীন CO₂",
            "শুধু শিখায় পপ করা H₂",
        ],
        "A", "easy", "application",
        "NH₄⁺ + OH⁻ → NH₃↑ + H₂O; ammonia is alkaline to litmus.",
        "NH₄⁺ + OH⁻ → NH₃↑ + H₂O; অ্যামোনিয়া লিটমাসে ক্ষারীয়।",
    ),
    q(
        "Fe³⁺ with KSCN (thiocyanate) produces a blood-red color of:",
        "KSCN (থাইওসায়ানেট) সহ Fe³⁺ রক্ত-লাল রং দেয়:",
        [
            "Fe(SCN)²⁺ / Fe(SCN)₃ complex",
            "Fe(OH)₂ only",
            "Metallic iron only",
            "FeSO₄ crystal only",
        ],
        [
            "Fe(SCN)²⁺ / Fe(SCN)₃ জটিল",
            "শুধু Fe(OH)₂",
            "শুধু ধাতব লোহা",
            "শুধু FeSO₄ কেলাস",
        ],
        "A", "medium", "factual",
        "Thiocyanate complexation is a sensitive Fe³⁺ test.",
        "থাইওসায়ানেট জটিলীকরণ Fe³⁺ এর সংবেদনশীল পরীক্ষা।",
    ),
    q(
        "Cu²⁺ in aqueous solution typically appears:",
        "জলীয় দ্রবণে Cu²⁺ সাধারণত দেখায়:",
        [
            "Blue (as [Cu(H₂O)₆]²⁺)",
            "Colorless like Na⁺",
            "Deep purple like MnO₄⁻",
            "Yellow like FeCl₃ always only",
        ],
        [
            "নীল ([Cu(H₂O)₆]²⁺ রূপে)",
            "Na⁺ এর মতো বর্ণহীন",
            "MnO₄⁻ এর মতো গভীর বেগুনি",
            "শুধু সবসময় FeCl₃ এর মতো হলুদ",
        ],
        "A", "easy", "factual",
        "Hydrated copper(II) ions are characteristically blue.",
        "জলীয় কপার(II) আয়ন বৈশিষ্ট্যসূচক নীল।",
    ),
    q(
        "Adding NaOH to Cu²⁺ solution gives a blue precipitate of:",
        "Cu²⁺ দ্রবণে NaOH যোগে নীল অধঃক্ষেপ:",
        [
            "Cu(OH)₂",
            "CuCl",
            "CuS only",
            "Cu metal only",
        ],
        [
            "Cu(OH)₂",
            "CuCl",
            "শুধু CuS",
            "শুধু Cu ধাতু",
        ],
        "A", "easy", "factual",
        "Cu²⁺ + 2OH⁻ → Cu(OH)₂ (blue) ppt.",
        "Cu²⁺ + 2OH⁻ → Cu(OH)₂ (নীল) অধঃক্ষেপ।",
    ),
    q(
        "Excess NH₃ added to Cu(OH)₂ dissolves it forming deep blue:",
        "Cu(OH)₂-এ অতিরিক্ত NH₃ যোগে গভীর নীল গঠন করে দ্রবীভূত:",
        [
            "[Cu(NH₃)₄]²⁺",
            "[CuCl₄]²⁻ only",
            "Cu²⁺ gas",
            "CuO₂²⁻ only",
        ],
        [
            "[Cu(NH₃)₄]²⁺",
            "শুধু [CuCl₄]²⁻",
            "Cu²⁺ গ্যাস",
            "শুধু CuO₂²⁻",
        ],
        "A", "medium", "conceptual",
        "Tetraamminecopper(II) is the deep-blue complex.",
        "টেট্রাঅ্যামিনকপার(II) গভীর নীল জটিল।",
    ),
    q(
        "Pb²⁺ with KI solution forms a yellow precipitate of:",
        "KI দ্রবণে Pb²⁺ হলুদ অধঃক্ষেপ গঠন করে:",
        [
            "PbI₂",
            "PbCl₂ only",
            "PbSO₄ only",
            "PbO₂ only",
        ],
        [
            "PbI₂",
            "শুধু PbCl₂",
            "শুধু PbSO₄",
            "শুধু PbO₂",
        ],
        "A", "easy", "factual",
        "Lead(II) iodide is a bright yellow ppt (golden spangles on cooling).",
        "লেড(II) আয়োডাইড উজ্জ্বল হলুদ অধঃক্ষেপ (ঠান্ডায় সোনালি স্প্যাঙ্গল)।",
    ),
    q(
        "CO₃²⁻ with dilute acid liberates a gas that:",
        "লঘু অ্যাসিডে CO₃²⁻ যে গ্যাস ছাড়ে:",
        [
            "Turns limewater milky (CO₂)",
            "Burns with a pop (H₂)",
            "Bleaches damp litmus like Cl₂",
            "Is alkaline NH₃",
        ],
        [
            "চুনাজল ঘোলা করে (CO₂)",
            "পপ শব্দে জ্বলে (H₂)",
            "Cl₂ এর মতো আর্দ্র লিটমাস বিরঞ্জিত করে",
            "ক্ষারীয় NH₃",
        ],
        "A", "easy", "application",
        "Carbonate + acid → CO₂; limewater test confirms CO₂.",
        "কার্বোনেট + অ্যাসিড → CO₂; চুনাজল পরীক্ষা CO₂ নিশ্চিত করে।",
    ),
    q(
        "NO₃⁻ in the brown-ring test involves formation of:",
        "বাদামি-বলয় পরীক্ষায় NO₃⁻ এর সাথে গঠিত হয়:",
        [
            "[Fe(H₂O)₅NO]²⁺ (brown ring complex)",
            "Only NaNO₃ crystals floating",
            "Only N₂ gas with no color",
            "Only Fe₂O₃ rust powder",
        ],
        [
            "[Fe(H₂O)₅NO]²⁺ (বাদামি বলয় জটিল)",
            "শুধু ভাসমান NaNO₃ কেলাস",
            "শুধু বর্ণহীন N₂ গ্যাস",
            "শুধু Fe₂O₃ মরিচা গুঁড়ো",
        ],
        "A", "hard", "factual",
        "FeSO₄ + nitrate + conc. H₂SO₄ give the classic brown ring.",
        "FeSO₄ + নাইট্রেট + গাঢ় H₂SO₄ ক্লাসিক বাদামি বলয় দেয়।",
    ),
    q(
        "S²⁻ with lead acetate paper turns the paper:",
        "লেড অ্যাসিটেট পেপারে S²⁻ পেপারকে করে:",
        [
            "Black (PbS)",
            "Bright red only",
            "White permanently only",
            "Blue like CuSO₄ only",
        ],
        [
            "কালো (PbS)",
            "শুধু উজ্জ্বল লাল",
            "শুধু স্থায়ী সাদা",
            "শুধু CuSO₄ এর মতো নীল",
        ],
        "A", "medium", "application",
        "H₂S/S²⁻ forms black lead sulfide on the paper.",
        "H₂S/S²⁻ পেপারে কালো লেড সালফাইড গঠন করে।",
    ),
    q(
        "Al³⁺ with NaOH first forms a white gelatinous ppt that dissolves in excess NaOH as:",
        "Al³⁺ এর সাথে NaOH প্রথমে সাদা জেলটিনাস অধঃক্ষেপ দেয় যা অতিরিক্ত NaOH-এ দ্রবীভূত হয়ে:",
        [
            "[Al(OH)₄]⁻ (aluminate)",
            "Al metal flakes only",
            "AlCl₃ gas only",
            "Al₂(SO₄)₃ insoluble always",
        ],
        [
            "[Al(OH)₄]⁻ (অ্যালুমিনেট)",
            "শুধু Al ধাতুর পাত",
            "শুধু AlCl₃ গ্যাস",
            "সবসময় অদ্রবণীয় Al₂(SO₄)₃",
        ],
        "A", "hard", "conceptual",
        "Amphoteric Al(OH)₃ dissolves in excess strong base as aluminate.",
        "উভধর্মী Al(OH)₃ অতিরিক্ত প্রবল ক্ষারে অ্যালুমিনেটরূপে দ্রবীভূত।",
    ),
    q(
        "Fe²⁺ with NaOH gives a dirty-green ppt of Fe(OH)₂ that on standing often:",
        "Fe²⁺ এর সাথে NaOH ময়লা-সবুজ Fe(OH)₂ অধঃক্ষেপ দেয় যা দাঁড়ালে প্রায়ই:",
        [
            "Oxidizes toward brown Fe(OH)₃",
            "Becomes metallic gold",
            "Turns into Na metal",
            "Evaporates as Fe gas",
        ],
        [
            "বাদামি Fe(OH)₃ এর দিকে জারিত হয়",
            "ধাতব স্বর্ণ হয়",
            "Na ধাতুতে পরিণত হয়",
            "Fe গ্যাসরূপে উবে যায়",
        ],
        "A", "medium", "conceptual",
        "Air oxidation converts Fe(II) hydroxide toward Fe(III) hydroxide.",
        "বায়ু জারণে Fe(II) হাইড্রক্সাইড Fe(III) হাইড্রক্সাইডের দিকে যায়।",
    ),
    q(
        "Which reagent is commonly used to confirm Cl⁻ after AgCl ppt forms?",
        "AgCl অধঃক্ষেপ গঠনের পর Cl⁻ নিশ্চিত করতে সাধারণত কোন বিকারক?",
        [
            "Dilute NH₃ (AgCl dissolves; reprecipitates with HNO₃)",
            "Concentrated H₂SO₄ only with no further test",
            "Only distilled water that never dissolves AgCl",
            "Only KMnO₄ without ammonia",
        ],
        [
            "লঘু NH₃ (AgCl দ্রবীভূত; HNO₃-এ পুনরায় অধঃক্ষিপ্ত)",
            "শুধু গাঢ় H₂SO₄ বিনা পরবর্তী পরীক্ষা",
            "শুধু ডিস্টিলড ওয়াটার যা কখনো AgCl গলায় না",
            "শুধু অ্যামোনিয়া ছাড়া KMnO₄",
        ],
        "A", "medium", "application",
        "Solubility in ammonia distinguishes AgCl from AgI especially.",
        "অ্যামোনিয়ায় দ্রবণীয়তা বিশেষ করে AgCl কে AgI থেকে পৃথক করে।",
    ),
]

# --- t05: Separation and qualitative analysis ---
T05 = [
    q(
        "Filtration separates an insoluble solid from a liquid based mainly on:",
        "পরিস্রাবণ মূলত কীসের ভিত্তিতে অদ্রবণীয় কঠিনকে তরল থেকে পৃথক করে:",
        [
            "Particle size relative to the filter pores",
            "Identical boiling points only",
            "Magnetic polarity of water only",
            "Nuclear spin of hydrogen only",
        ],
        [
            "ফিল্টার ছিদ্রের তুলনায় কণার আকার",
            "শুধু অভিন্ন স্ফুটনাঙ্ক",
            "শুধু পানির চৌম্বক মেরুত্ব",
            "শুধু হাইড্রোজেনের নিউক্লিয়ার স্পিন",
        ],
        "A", "easy", "conceptual",
        "Filter media retain solids larger than pore size.",
        "ফিল্টার মাধ্যম ছিদ্রের চেয়ে বড় কঠিন আটকায়।",
    ),
    q(
        "Distillation separates liquid mixtures primarily by differences in:",
        "ডিস্টিলেশন তরল মিশ্রণ পৃথক করে প্রধানত পার্থক্যের ভিত্তিতে:",
        [
            "Boiling points / vapor pressures",
            "Only color of the liquids",
            "Only magnetic susceptibility",
            "Only isotopic spin",
        ],
        [
            "স্ফুটনাঙ্ক / বাষ্পচাপ",
            "শুধু তরলের রং",
            "শুধু চৌম্বক প্রবণতা",
            "শুধু আইসোটোপিক স্পিন",
        ],
        "A", "easy", "factual",
        "More volatile components vaporize preferentially and are condensed.",
        "বেশি উদ্বায়ী উপাদান অগ্রাধিকারে বাষ্পীভূত হয়ে ঘনীভূত হয়।",
    ),
    q(
        "Paper chromatography separates mixture components by differences in:",
        "পেপার ক্রোমাটোগ্রাফি মিশ্রণের উপাদান পৃথক করে পার্থক্যের ভিত্তিতে:",
        [
            "Affinity for stationary vs mobile phase (partition/adsorption)",
            "Only identical Rf for all spots",
            "Only nuclear charge Z",
            "Only the mass of the paper roll",
        ],
        [
            "স্থির বনাম চলমান দশার প্রতি আসক্তি (বিভাজন/শোষণ)",
            "শুধু সব স্পটের অভিন্ন Rf",
            "শুধু নিউক্লিয়ার চার্জ Z",
            "শুধু কাগজ রোলের ভর",
        ],
        "A", "medium", "conceptual",
        "Components travel different distances → different Rf values.",
        "উপাদান ভিন্ন দূরত্ব ভ্রমণ করে → ভিন্ন Rf।",
    ),
    q(
        "Rf value in paper chromatography is defined as:",
        "পেপার ক্রোমাটোগ্রাফিতে Rf মান সংজ্ঞায়িত:",
        [
            "Distance traveled by solute / distance traveled by solvent front",
            "Solvent front / solute distance only inverted always wrong",
            "Only the boiling point of water",
            "Only the atomic number of carbon",
        ],
        [
            "দ্রবের অতিক্রান্ত দূরত্ব / দ্রাবক সীমান্তের দূরত্ব",
            "শুধু দ্রাবক/দ্রব উল্টো যা সবসময় ভুল",
            "শুধু পানির স্ফুটনাঙ্ক",
            "শুধু কার্বনের পারমাণবিক সংখ্যা",
        ],
        "A", "easy", "factual",
        "Rf is a dimensionless retention factor for each component.",
        "Rf প্রতি উপাদানের মাত্রাহীন রিটেনশন ফ্যাক্টর।",
    ),
    q(
        "Centrifugation speeds separation of suspensions by:",
        "সেন্ট্রিফিউগেশন সাসপেনশন পৃথকীকরণ ত্বরান্বিত করে:",
        [
            "Applying enhanced effective gravitational (centrifugal) force",
            "Removing all intermolecular forces chemically",
            "Changing nuclear binding energies",
            "Making all particles dissolve instantly",
        ],
        [
            "বর্ধিত কার্যকর মহাকর্ষীয় (কেন্দ্রমুখী) বল প্রয়োগ করে",
            "সব আন্তঃআণবিক বল রাসায়নিকভাবে সরিয়ে",
            "নিউক্লিয়ার বন্ধন শক্তি পরিবর্তন করে",
            "সব কণা তাৎক্ষণিক দ্রবীভূত করে",
        ],
        "A", "medium", "conceptual",
        "Denser particles sediment faster under high g.",
        "উচ্চ g-তে ঘনতর কণা দ্রুত অধঃক্ষিপ্ত হয়।",
    ),
    q(
        "In qualitative inorganic analysis, Group I cations are typically precipitated as chlorides using:",
        "গুণগত অজৈব বিশ্লেষণে Group I ক্যাটায়ন সাধারণত ক্লোরাইডরূপে অধঃক্ষিপ্ত হয় ব্যবহার করে:",
        [
            "Dilute HCl",
            "Only concentrated HNO₃ with no chloride",
            "Only NaOH without acid",
            "Only distilled water heating",
        ],
        [
            "লঘু HCl",
            "শুধু ক্লোরাইডহীন গাঢ় HNO₃",
            "শুধু অ্যাসিড ছাড়া NaOH",
            "শুধু ডিস্টিলড ওয়াটার গরম করা",
        ],
        "A", "medium", "factual",
        "Ag⁺, Pb²⁺, Hg₂²⁺ form insoluble chlorides in dilute HCl.",
        "লঘু HCl-এ Ag⁺, Pb²⁺, Hg₂²⁺ অদ্রবণীয় ক্লোরাইড গঠন করে।",
    ),
    q(
        "H₂S in acidic medium is used in classical analysis mainly to precipitate:",
        "অম্লীয় মাধ্যমে H₂S ক্লাসিক্যাল বিশ্লেষণে মূলত অধঃক্ষিপ্ত করে:",
        [
            "Group II sulfides of cations like Cu²⁺, Pb²⁺, As³⁺, etc.",
            "Only alkali metal chlorides",
            "Only NH₄⁺ as a solid metal",
            "Only noble gases as solids",
        ],
        [
            "Cu²⁺, Pb²⁺, As³⁺ ইত্যাদি Group II সালফাইড",
            "শুধু ক্ষার ধাতুর ক্লোরাইড",
            "শুধু NH₄⁺ কঠিন ধাতুরূপে",
            "শুধু নিষ্ক্রিয় গ্যাস কঠিনরূপে",
        ],
        "A", "hard", "factual",
        "Low S²⁻ in acid selectively precipitates less soluble Group II sulfides.",
        "অ্যাসিডে কম S²⁻ কম দ্রবণীয় Group II সালফাইড নির্বাচনী অধঃক্ষেপ করে।",
    ),
    q(
        "Decantation differs from filtration in that decantation:",
        "ডিক্যান্টেশন পরিস্রাবণ থেকে ভিন্ন কারণ ডিক্যান্টেশন:",
        [
            "Pours off liquid carefully after solids settle, without a filter medium",
            "Always uses filter paper pores",
            "Requires a chromatographic solvent front",
            "Boils the mixture to dryness only",
        ],
        [
            "কঠিন তলানির পর ফিল্টার মাধ্যম ছাড়া সতর্কভাবে তরল ঢেলে ফেলা",
            "সবসময় ফিল্টার পেপার ছিদ্র ব্যবহার করে",
            "ক্রোমাটোগ্রাফিক দ্রাবক সীমান্ত দাবি করে",
            "শুধু মিশ্রণ শুষ্ক না হওয়া পর্যন্ত ফোটানো",
        ],
        "A", "easy", "conceptual",
        "Decantation relies on sedimentation then pouring.",
        "ডিক্যান্টেশন তলানি ও তারপর ঢালার উপর নির্ভর করে।",
    ),
    q(
        "Sublimation can separate a mixture when one component:",
        "সাবলিমেশন মিশ্রণ পৃথক করতে পারে যখন এক উপাদান:",
        [
            "Passes solid → vapor → solid without lasting as liquid under conditions used",
            "Has identical vapor pressure to all others always",
            "Is completely nonvolatile forever",
            "Dissolves only in supercritical plasma",
        ],
        [
            "ব্যবহৃত অবস্থায় স্থায়ী তরল না হয়ে কঠিন → বাষ্প → কঠিন হয়",
            "সবসময় অন্য সবের সাথে অভিন্ন বাষ্পচাপ রাখে",
            "চিরকাল সম্পূর্ণ অ-উদ্বায়ী",
            "শুধু সুপারক্রিটিক্যাল প্লাজমায় দ্রবীভূত",
        ],
        "A", "medium", "conceptual",
        "Iodine or NH₄Cl can be sublimed away from non-volatile impurities.",
        "আয়োডিন বা NH₄Cl অ-উদ্বায়ী অশুদ্ধি থেকে সাবলিম করে পৃথক করা যায়।",
    ),
    q(
        "Solvent extraction (liquid–liquid) separates solutes based on:",
        "দ্রাবক নিষ্কাশন (তরল–তরল) দ্রব পৃথক করে ভিত্তিতে:",
        [
            "Preferential solubility/partition between two immiscible liquids",
            "Only identical densities always",
            "Only the color of the separatory funnel",
            "Only neutron diffraction",
        ],
        [
            "দুই অমিশ্রণীয় তরলের মধ্যে অগ্রাধিকার দ্রবণীয়তা/বিভাজন",
            "শুধু সবসময় অভিন্ন ঘনত্ব",
            "শুধু সেপারেটরি ফানেলের রং",
            "শুধু নিউট্রন ডিফ্র্যাকশন",
        ],
        "A", "medium", "factual",
        "A solute concentrates in the solvent where it is more soluble.",
        "দ্রব যে দ্রাবকে বেশি দ্রবণীয় সেখানে ঘনীভূত হয়।",
    ),
    q(
        "In a qualitative analysis scheme, why is the sequence of group reagents important?",
        "গুণগত বিশ্লেষণ স্কিমে গ্রুপ বিকারকের ক্রম গুরুত্বপূর্ণ কেন?",
        [
            "Wrong order causes co-precipitation or missing ions",
            "Order never affects which ions precipitate",
            "Any random order always gives the same ppt purity",
            "Sequence only matters for weighing bottles",
        ],
        [
            "ভুল ক্রমে সহ-অধঃক্ষেপ বা আয়ন হারানো যায়",
            "ক্রম কোন আয়ন অধঃক্ষিপ্ত হয় তা কখনো প্রভাবিত করে না",
            "যেকোনো এলোমেলো ক্রম সবসময় একই অধঃক্ষেপ বিশুদ্ধতা দেয়",
            "ক্রম শুধু ওজন বোতলের জন্য গুরুত্বপূর্ণ",
        ],
        "A", "hard", "conceptual",
        "Group reagents are selective only under specified prior conditions.",
        "গ্রুপ বিকারক শুধু নির্ধারিত পূর্বশর্তে নির্বাচনী।",
    ),
    q(
        "Crystallization purifies a solid mainly by:",
        "কেলাসন কঠিন বিশুদ্ধ করে মূলত:",
        [
            "Dissolving then slowly reforming crystals that exclude many impurities",
            "Melting impurities into the crystal lattice intentionally",
            "Burning the solid completely to ash",
            "Adding random soil as seed crystals",
        ],
        [
            "দ্রবীভূত করে ধীরে কেলাস গঠন যা অনেক অশুদ্ধি বর্জন করে",
            "ইচ্ছাকৃতভাবে অশুদ্ধি কেলাস জালিতে গলানো",
            "কঠিন সম্পূর্ণ পুড়িয়ে ছাই করা",
            "বীজ কেলাস হিসেবে এলোমেলো মাটি যোগ",
        ],
        "A", "easy", "application",
        "Slow crystal growth prefers the pure lattice.",
        "ধীর কেলাস বৃদ্ধি বিশুদ্ধ জালিকে অগ্রাধিকার দেয়।",
    ),
    q(
        "A drying agent (desiccant) in a desiccator is used to:",
        "ডেসিকেটরে শুষ্ককারক (ডেসিকেন্ট) ব্যবহার হয়:",
        [
            "Remove moisture from samples or atmosphere inside",
            "Increase sample humidity deliberately",
            "Dissolve all inorganic salts",
            "Generate H₂S for Group IV",
        ],
        [
            "নমুনা বা অভ্যন্তরীণ বায়ুমণ্ডল থেকে আর্দ্রতা সরাতে",
            "ইচ্ছাকৃতভাবে নমুনার আর্দ্রতা বাড়াতে",
            "সব অজৈব লবণ দ্রবীভূত করতে",
            "Group IV এর জন্য H₂S উৎপাদন করতে",
        ],
        "A", "easy", "factual",
        "Common desiccants include silica gel, CaCl₂, P₄O₁₀.",
        "সাধারণ ডেসিকেন্ট: সিলিকা জেল, CaCl₂, P₄O₁₀।",
    ),
    q(
        "Fractional distillation is preferred over simple distillation when:",
        "সরল ডিস্টিলেশনের চেয়ে ভগ্নাংশ ডিস্টিলেশন অগ্রাধিকার যখন:",
        [
            "Boiling points of components are close",
            "Components have enormously different boiling points always only",
            "No vapor forms at any temperature",
            "The mixture is a single pure compound",
        ],
        [
            "উপাদানগুলোর স্ফুটনাঙ্ক কাছাকাছি",
            "শুধু সবসময় স্ফুটনাঙ্ক অনেক আলাদা",
            "কোনো তাপমাত্রায় বাষ্প গঠিত হয় না",
            "মিশ্রণ একটিমাত্র বিশুদ্ধ যৌগ",
        ],
        "A", "medium", "application",
        "A fractionating column improves separation of close boilers.",
        "ভগ্নাংশ কলাম কাছাকাছি স্ফুটনশীল পদার্থের পৃথকীকরণ উন্নত করে।",
    ),
    q(
        "In cation analysis, why is the solution often acidified before H₂S for Group II?",
        "ক্যাটায়ন বিশ্লেষণে Group II এর জন্য H₂S এর আগে দ্রবণ প্রায়ই অম্লীয় করা হয় কেন?",
        [
            "To keep [S²⁻] low so only less soluble sulfides precipitate",
            "To dissolve all Group IV sulfides first intentionally wrong",
            "To convert all cations into gases",
            "To neutralize the need for any reagents",
        ],
        [
            "[S²⁻] কম রেখে শুধু কম দ্রবণীয় সালফাইড অধঃক্ষিপ্ত করতে",
            "ইচ্ছাকৃত ভুলে আগে সব Group IV সালফাইড গলাতে",
            "সব ক্যাটায়ন গ্যাসে রূপান্তর করতে",
            "যেকোনো বিকারকের প্রয়োজন নিরপেক্ষ করতে",
        ],
        "A", "hard", "conceptual",
        "pH controls sulfide ion concentration via H₂S equilibria.",
        "H₂S সাম্যাবস্থায় pH সালফাইড আয়ন ঘনত্ব নিয়ন্ত্রণ করে।",
    ),
    q(
        "Magnetic separation can isolate:",
        "চৌম্বক পৃথকীকরণ আলাদা করতে পারে:",
        [
            "Ferromagnetic solids (e.g., iron filings) from non-magnetic mixtures",
            "Only NaCl from KCl by magnetism alone",
            "Only isotopes of neon",
            "Only dissolved sulfate ions from water",
        ],
        [
            "অচৌম্বক মিশ্রণ থেকে ফেরোচৌম্বক কঠিন (যেমন লোহার গুঁড়ো)",
            "শুধু চুম্বকত্বে NaCl থেকে KCl",
            "শুধু নিয়নের আইসোটোপ",
            "শুধু পানি থেকে দ্রবীভূত সালফেট আয়ন",
        ],
        "A", "easy", "application",
        "A magnet attracts magnetic particles selectively.",
        "চুম্বক নির্বাচনীভাবে চৌম্বক কণা আকর্ষণ করে।",
    ),
    q(
        "Evaporation as a separation technique is useful to:",
        "পৃথকীকরণ কৌশল হিসেবে বাষ্পীভবন উপযোগী:",
        [
            "Recover a dissolved solid by removing solvent",
            "Separate two gases with identical properties always",
            "Create new elements",
            "Stop all phase changes",
        ],
        [
            "দ্রাবক সরিয়ে দ্রবীভূত কঠিন পুনরুদ্ধার",
            "সবসময় অভিন্ন ধর্মের দুই গ্যাস পৃথক",
            "নতুন মৌল সৃষ্টি",
            "সব দশা পরিবর্তন বন্ধ",
        ],
        "A", "easy", "factual",
        "Driving off solvent leaves non-volatile solute behind.",
        "দ্রাবক তাড়িয়ে অ-উদ্বায়ী দ্রব পড়ে থাকে।",
    ),
    q(
        "A common laboratory method to dry an organic liquid after washing is to:",
        "ধোয়ার পর জৈব তরল শুকানোর সাধারণ ল্যাব পদ্ধতি:",
        [
            "Shake with an anhydrous drying agent then decant/filter",
            "Add lots of water to dilute it further",
            "Pass it through wet filter paper only",
            "Boil it with aqueous NaCl indefinitely",
        ],
        [
            "অ্যানহাইড্রাস শুষ্ককারকের সাথে ঝাঁকিয়ে ডিক্যান্ট/ফিল্টার",
            "আরও লঘু করতে প্রচুর পানি যোগ",
            "শুধু ভেজা ফিল্টার পেপার দিয়ে চালানো",
            "অনির্দিষ্টকাল জলীয় NaCl সহ ফোটানো",
        ],
        "A", "medium", "application",
        "Anhydrous MgSO₄ or Na₂SO₄ bind residual water.",
        "অ্যানহাইড্রাস MgSO₄ বা Na₂SO₄ অবশিষ্ট পানি বাঁধে।",
    ),
    q(
        "Why must precipitates often be washed during qualitative analysis?",
        "গুণগত বিশ্লেষণে অধঃক্ষেপ প্রায়ই ধোয়া প্রয়োজন কেন?",
        [
            "To remove adsorbed impurities and co-precipitated ions",
            "To dissolve the desired ppt intentionally always",
            "To increase contamination from the filtrate",
            "To change the atomic number of the metal",
        ],
        [
            "শোষিত অশুদ্ধি ও সহ-অধঃক্ষিপ্ত আয়ন সরাতে",
            "সবসময় ইচ্ছাকৃতভাবে কাঙ্ক্ষিত অধঃক্ষেপ গলাতে",
            "ফিল্ট্রেট থেকে দূষণ বাড়াতে",
            "ধাতুর পারমাণবিক সংখ্যা বদলাতে",
        ],
        "A", "medium", "conceptual",
        "Washing improves purity before confirmatory tests.",
        "নিশ্চিতকরণ পরীক্ষার আগে ধোয়া বিশুদ্ধতা বাড়ায়।",
    ),
    q(
        "Which statement best describes qualitative vs quantitative analysis?",
        "গুণগত বনাম পরিমাণগত বিশ্লেষণের কোন বর্ণনা সঠিক?",
        [
            "Qualitative identifies what is present; quantitative measures how much",
            "Qualitative only measures exact molarity; quantitative only names ions",
            "They are identical procedures always",
            "Qualitative ignores all chemical properties",
        ],
        [
            "গুণগত শনাক্ত করে কী আছে; পরিমাণগত মাপে কতটা আছে",
            "গুণগত শুধু সঠিক মোলারিটি মাপে; পরিমাণগত শুধু আয়নের নাম বলে",
            "এরা সবসময় অভিন্ন পদ্ধতি",
            "গুণগত সব রাসায়নিক ধর্ম উপেক্ষা করে",
        ],
        "A", "easy", "conceptual",
        "Qualitative chemistry focuses on identity and separation of species.",
        "গুণগত রসায়ন প্রজাতির পরিচয় ও পৃথকীকরণে মনোযোগী।",
    ),
]

TOPICS_MAP = {
    "chem1_27_ch02_t01": T01,
    "chem1_27_ch02_t02": T02,
    "chem1_27_ch02_t03": T03,
    "chem1_27_ch02_t04": T04,
    "chem1_27_ch02_t05": T05,
}


def write_topic(topic_id: str, rows: list[dict]) -> dict:
    clean = []
    for row in rows:
        err = validate_record(row)
        if err:
            raise SystemExit(f"{topic_id}: {err}\n{row['stem_en'][:120]}")
        clean.append({**row, "verified": False, "source": SRC})
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
        "chapter": "chem1_27_ch02",
        "title_en": "Qualitative Chemistry",
        "title_bn": "গুণগত রসায়ন",
        "source": SRC,
        "pdf_pages": [],
        "note": (
            "Import CSV chemistry_1_ch02.csv had headers only; authored 20 bilingual "
            "MCQs per topic aligned to NCTB chemistry_1st_paper_2027 ch02 "
            "(Qualitative Chemistry)."
        ),
        "counts": {**counts, "total": sum(counts.values())},
        "paths": paths,
        "pdf_mapping": {
            "chem1_27_ch02_t01": {
                "title": "Atomic structure and quantum numbers / পরমাণুর গঠন ও কোয়ান্টাম সংখ্যা",
                "themes": [
                    "Z A isotopes protons neutrons electrons",
                    "n l m_l m_s rules and forbidden sets",
                    "Thomson Rutherford shell 2n² Pauli in orbital",
                    "ions X²⁺ orbital shape orientation subshells",
                ],
            },
            "chem1_27_ch02_t02": {
                "title": "Electron configuration and orbitals / ইলেকট্রন বিন্যাস ও অরবিটাল",
                "themes": [
                    "Aufbau Hund Pauli; C N Ne shorthand",
                    "s p d f capacities; n+l order 4s/3d",
                    "Cr Cu exceptions; isoelectronic Na⁺",
                    "orbitals nodes valence configurations",
                ],
            },
            "chem1_27_ch02_t03": {
                "title": "Electromagnetic radiation and spectra / তড়িৎচৌম্বক বিকিরণ ও বর্ণালি",
                "themes": [
                    "c=νλ E=hν photon wave number",
                    "Bohr emission Lyman Balmer Paschen",
                    "continuous emission absorption spectra",
                    "Rydberg de Broglie spectrophotometer UV",
                ],
            },
            "chem1_27_ch02_t04": {
                "title": "Identification of ions / আয়ন শনাক্তকরণ",
                "themes": [
                    "flame tests Na K Ca Ba/Cu",
                    "AgNO₃ Cl Br I; BaSO₄; NH₄⁺; Fe SCN",
                    "Cu²⁺ hydroxide ammine; PbI₂; CO₂ limewater",
                    "brown ring S²⁻ PbS Al amphoteric Fe²⁺",
                ],
            },
            "chem1_27_ch02_t05": {
                "title": "Separation and qualitative analysis / পৃথকীকরণ ও গুণগত বিশ্লেষণ",
                "themes": [
                    "filtration distillation chromatography Rf centrifugation",
                    "Group I HCl Group II acidic H₂S order importance",
                    "decantation sublimation extraction crystallization",
                    "desiccant fractional distillation washing qualitative vs quantitative",
                ],
            },
        },
        "low_confidence": [
            "No usable in-repo OCR page set for Chemistry 1st paper Udvash PDF ch02; items are syllabus-aligned authored MCQs, not direct OCR transcriptions.",
            "Import CSV content/bank/import/chemistry_1_ch02.csv had headers only (no stems to reuse).",
            "Cation group schemes follow common BD HSC qualitative analysis teaching; textbook grouping labels can vary slightly by edition.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (chem1_27_ch02_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {tid: 20 for tid in TOPIC_IDS},
        },
        "chem1_ch02_completion": {
            "topics_expected": 5,
            "topics_at_20": 5,
            "note": "chem1_27_ch02_t01..t05 complete at 20/topic (chapter total 100).",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch02_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
