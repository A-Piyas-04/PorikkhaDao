#!/usr/bin/env python3
"""Seed Chemistry 1st Paper Ch3 bilingual MCQs (Periodic Properties and Chemical Bonding).

Import CSV chemistry_1_ch03.csv had headers only; authored 20 bilingual MCQs
per topic aligned to NCTB chemistry_1st_paper_2027 ch03.
Writes chem1_27_ch03_t01..t05 under content/bank/topics/.
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
    "chemistry p1 ch03; curated bilingual"
)

TOPIC_IDS = [f"chem1_27_ch03_t{i:02d}" for i in range(1, 6)]


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


# --- t01: Periodic table and electron configuration ---
T01 = [
    q(
        "Who proposed the modern periodic law based on atomic number?",
        "পারমাণবিক সংখ্যার উপর ভিত্তি করে আধুনিক পর্যায় সূত্র কে প্রস্তাব করেন?",
        ["Mendeleev", "Moseley", "Dalton", "Newlands"],
        ["মেন্ডেলিভ", "মোজলি", "ডালটন", "নিউল্যান্ডস"],
        "B", "easy", "factual",
        "Moseley showed that atomic number, not atomic mass, orders the periodic table.",
        "মোজলি দেখান যে পর্যায় সারণির ক্রম পারমাণবিক ভর নয়, পারমাণবিক সংখ্যা দ্বারা নির্ধারিত।",
    ),
    q(
        "Modern periodic law states that properties of elements are periodic functions of:",
        "আধুনিক পর্যায় সূত্র অনুসারে মৌলের ধর্ম কোনটির পর্যায়বৃত্ত ফাংশন?",
        ["Atomic mass", "Atomic number", "Neutron number", "Mass number only"],
        ["পারমাণবিক ভর", "পারমাণবিক সংখ্যা", "নিউট্রন সংখ্যা", "শুধু ভর সংখ্যা"],
        "B", "easy", "factual",
        "Periodic properties depend on atomic number (Z).",
        "পর্যায়বৃত্ত ধর্ম পারমাণবিক সংখ্যা (Z) এর উপর নির্ভর করে।",
    ),
    q(
        "Elements in the same group of the periodic table have the same:",
        "পর্যায় সারণির একই গ্রুপের মৌলগুলোর কোনটি একই থাকে?",
        ["Number of electron shells", "Number of valence electrons", "Atomic mass", "Number of neutrons"],
        ["ইলেকট্রন শেলের সংখ্যা", "যোজনী ইলেকট্রনের সংখ্যা", "পারমাণবিক ভর", "নিউট্রনের সংখ্যা"],
        "B", "easy", "conceptual",
        "Group members share the same valence electron count, giving similar chemistry.",
        "একই গ্রুপের মৌলে যোজনী ইলেকট্রন সংখ্যা সমান, তাই ধর্ম অনুরূপ।",
    ),
    q(
        "Across a period from left to right, the number of valence electrons:",
        "বাম থেকে ডানে পর্যায় বরাবর যোজনী ইলেকট্রনের সংখ্যা:",
        ["Decreases", "Increases", "Remains constant", "Becomes zero"],
        ["কমে", "বাড়ে", "অপরিবর্তিত থাকে", "শূন্য হয়"],
        "B", "easy", "conceptual",
        "Each successive element adds one proton and usually one valence electron.",
        "পরবর্তী মৌলে সাধারণত এক প্রোটন ও এক যোজনী ইলেকট্রন যোগ হয়।",
    ),
    q(
        "s-block elements have their outermost electrons in which orbitals?",
        "s-ব্লক মৌলের বহিস্থ ইলেকট্রন কোন অরবিটালে থাকে?",
        ["p orbitals", "d orbitals", "s orbitals", "f orbitals"],
        ["p অরবিটাল", "d অরবিটাল", "s অরবিটাল", "f অরবিটাল"],
        "C", "easy", "factual",
        "Groups 1 and 2 (alkali and alkaline earth) are s-block elements.",
        "গ্রুপ ১ ও ২ (ক্ষার ও মৃৎক্ষার) s-ব্লক মৌল।",
    ),
    q(
        "Transition metals belong mainly to which block?",
        "ট্রানজিশন ধাতু প্রধানত কোন ব্লকের?",
        ["s-block", "p-block", "d-block", "Only noble gases"],
        ["s-ব্লক", "p-ব্লক", "d-ব্লক", "শুধু নিষ্ক্রিয় গ্যাস"],
        "C", "easy", "factual",
        "d-block elements with incomplete d subshells are typical transition metals.",
        "অসম্পূর্ণ d সাবশেলযুক্ত d-ব্লক মৌলই সাধারণ ট্রানজিশন ধাতু।",
    ),
    q(
        "The electron configuration of sodium (Z=11) is:",
        "সোডিয়ামের (Z=11) ইলেকট্রন বিন্যাস কোনটি?",
        ["1s2 2s2 2p6 3s1", "1s2 2s2 2p6 3s2", "1s2 2s2 2p5", "1s2 2s2 2p6 3p1"],
        ["1s2 2s2 2p6 3s1", "1s2 2s2 2p6 3s2", "1s2 2s2 2p5", "1s2 2s2 2p6 3p1"],
        "A", "easy", "factual",
        "Na has 11 electrons ending in 3s1.",
        "Na-এর ১১টি ইলেকট্রন; শেষ কনফিগারেশন 3s1।",
    ),
    q(
        "According to the Aufbau principle, electrons fill orbitals in order of:",
        "অফবাউ নীতি অনুসারে ইলেকট্রন অরবিটাল ভরে কোন ক্রমে?",
        ["Decreasing energy", "Increasing energy", "Random order", "Only by spin"],
        ["শক্তি হ্রাসের ক্রমে", "শক্তি বৃদ্ধির ক্রমে", "এলোমেলোভাবে", "শুধু স্পিন অনুসারে"],
        "B", "easy", "factual",
        "Aufbau fills lower-energy orbitals before higher ones.",
        "অফবাউতে কম শক্তির অরবিটাল আগে ভরে।",
    ),
    q(
        "Pauli exclusion principle states that no two electrons in an atom can have:",
        "পাউলি বর্জন নীতি অনুসারে পরমাণুর দুই ইলেকট্রনের কোনটি একই হতে পারে না?",
        ["The same mass", "The same set of four quantum numbers", "Opposite spins only", "Different shells"],
        ["একই ভর", "চারটি কোয়ান্টাম সংখ্যার একই সেট", "শুধু বিপরীত স্পিন", "ভিন্ন শেল"],
        "B", "medium", "conceptual",
        "Each electron must have a unique combination of n, l, ml, and ms.",
        "প্রতিটি ইলেকট্রনের n, l, ml ও ms এর সমন্বয় অনন্য হতে হবে।",
    ),
    q(
        "Hund's rule says that electrons in degenerate orbitals prefer to:",
        "হুন্ডের নিয়ম অনুসারে degenerate অরবিটালে ইলেকট্রন অগ্রাধিকার দেয়:",
        ["Pair up first with opposite spins", "Occupy singly with parallel spins", "Leave orbitals empty", "Jump to higher shells"],
        ["প্রথমে বিপরীত স্পিনে জোড়া বাঁধতে", "সমান্তরাল স্পিনে এককভাবে থাকতে", "অরবিটাল খালি রাখতে", "উচ্চ শেলে যেতে"],
        "B", "medium", "conceptual",
        "Degenerate orbitals get one electron each with parallel spins before pairing.",
        "Degenerate অরবিটালে জোড়া বাঁধার আগে সমান্তরাল স্পিনে একক ইলেকট্রন থাকে।",
    ),
    q(
        "Noble gases generally have which outer shell configuration?",
        "নিষ্ক্রিয় গ্যাসের বহিঃস্থ শেল সাধারণত কেমন?",
        ["ns1", "ns2 np4", "ns2 np6 (except He)", "nd10 only"],
        ["ns1", "ns2 np4", "ns2 np6 (He ছাড়া)", "শুধু nd10"],
        "C", "easy", "factual",
        "Stable octets (ns2 np6) explain noble-gas inertness; He is 1s2.",
        "স্থিতিশীল অক্টেট (ns2 np6) নিষ্ক্রিয়তার কারণ; He হলো 1s2।",
    ),
    q(
        "In the long-form periodic table, a period corresponds to:",
        "দীর্ঘ পর্যায় সারণিতে একটি পর্যায় নির্দেশ করে:",
        ["Same valence electrons", "Filling of a principal energy level", "Same atomic mass", "Only metals"],
        ["একই যোজনী ইলেকট্রন", "একটি প্রধান শক্তিস্তর ভরাট", "একই পারমাণবিক ভর", "শুধু ধাতু"],
        "B", "medium", "conceptual",
        "Each period starts as a new principal shell begins to fill.",
        "প্রতিটি পর্যায় নতুন প্রধান শেল ভরাটের সাথে শুরু হয়।",
    ),
    q(
        "Lanthanides and actinides are placed in which block?",
        "ল্যান্থানাইড ও অ্যাক্টিনাইড কোন ব্লকে রাখা হয়?",
        ["s-block", "p-block", "d-block", "f-block"],
        ["s-ব্লক", "p-ব্লক", "d-ব্লক", "f-ব্লক"],
        "D", "easy", "factual",
        "Inner transition elements occupy the f-block.",
        "অন্তঃট্রানজিশন মৌল f-ব্লকে থাকে।",
    ),
    q(
        "The maximum number of electrons in the n=2 shell is:",
        "n=2 শেলে সর্বোচ্চ কতটি ইলেকট্রন থাকতে পারে?",
        ["2", "8", "18", "32"],
        ["2", "8", "18", "32"],
        "B", "easy", "numerical",
        "2n^2 for n=2 gives 8 electrons.",
        "n=2 এর জন্য 2n^2 = ৮টি ইলেকট্রন।",
    ),
    q(
        "Which quantum number describes the shape of an orbital?",
        "অরবিটালের আকৃতি কোন কোয়ান্টাম সংখ্যা নির্দেশ করে?",
        ["Principal (n)", "Azimuthal (l)", "Magnetic (ml)", "Spin (ms)"],
        ["প্রধান (n)", "অজিমুথাল (l)", "চৌম্বক (ml)", "স্পিন (ms)"],
        "B", "medium", "factual",
        "Azimuthal quantum number l defines orbital shape (s, p, d, f).",
        "অজিমুথাল কোয়ান্টাম সংখ্যা l অরবিটালের আকৃতি নির্ধারণ করে।",
    ),
    q(
        "An element with atomic number 17 belongs to which group (IUPAC)?",
        "পারমাণবিক সংখ্যা ১৭ এর মৌল IUPAC অনুসারে কোন গ্রুপে?",
        ["Group 1", "Group 2", "Group 17", "Group 18"],
        ["গ্রুপ ১", "গ্রুপ ২", "গ্রুপ ১৭", "গ্রুপ ১৮"],
        "C", "medium", "application",
        "Cl (Z=17) has configuration ending in ns2 np5 — a halogen in group 17.",
        "Cl (Z=17) এর কনফিগারেশন ns2 np5 — গ্রুপ ১৭ এর হ্যালোজেন।",
    ),
    q(
        "Isoelectronic species have the same:",
        "আইসোইলেকট্রনিক প্রজাতির কোনটি একই?",
        ["Atomic number", "Number of electrons", "Number of protons", "Mass number"],
        ["পারমাণবিক সংখ্যা", "ইলেকট্রন সংখ্যা", "প্রোটন সংখ্যা", "ভর সংখ্যা"],
        "B", "easy", "conceptual",
        "Isoelectronic means equal electron counts (e.g., Na+, Ne, F−).",
        "আইসোইলেকট্রনিক মানে সমান ইলেকট্রন সংখ্যা (যেমন Na+, Ne, F−)।",
    ),
    q(
        "The ground-state configuration of Cr (Z=24) is exceptional because:",
        "Cr (Z=24) এর ভূমি অবস্থার কনফিগারেশন ব্যতিক্রমী কারণ:",
        ["It has a half-filled 3d and 4s preference", "It has no d electrons", "It is a noble gas", "It fills 4p before 3d"],
        ["অর্ধপূর্ণ 3d ও 4s এর স্থিতিশীলতা", "এর কোনো d ইলেকট্রন নেই", "এটি নিষ্ক্রিয় গ্যাস", "3d এর আগে 4p ভরে"],
        "A", "hard", "conceptual",
        "Cr is [Ar] 4s1 3d5 due to extra stability of half-filled d subshell.",
        "অর্ধপূর্ণ d সাবশেলের স্থিতিশীলতার জন্য Cr হলো [Ar] 4s1 3d5।",
    ),
    q(
        "Halogens are located in which block of the periodic table?",
        "হ্যালোজেন পর্যায় সারণির কোন ব্লকে?",
        ["s-block", "p-block", "d-block", "f-block"],
        ["s-ব্লক", "p-ব্লক", "d-ব্লক", "f-ব্লক"],
        "B", "easy", "factual",
        "Halogens are group 17 p-block elements with ns2 np5 configuration.",
        "হ্যালোজেন গ্রুপ ১৭ এর p-ব্লক মৌল; কনফিগারেশন ns2 np5।",
    ),
    q(
        "Valence electrons of an atom are those in the:",
        "পরমাণুর যোজনী ইলেকট্রন কোনটিতে থাকে?",
        ["Innermost shell only", "Outermost shell", "Nucleus", "Only d orbitals always"],
        ["শুধু অন্তঃস্থ শেল", "বহিঃস্থ শেল", "নিউক্লিয়াস", "সবসময় শুধু d অরবিটাল"],
        "B", "easy", "factual",
        "Chemical bonding involves outermost (valence) electrons.",
        "রাসায়নিক বন্ধনে বহিঃস্থ (যোজনী) ইলেকট্রন অংশ নেয়।",
    ),
]

# --- t02: Periodic trends ---
T02 = [
    q(
        "Across a period, atomic radius generally:",
        "পর্যায় বরাবর পারমাণবিক ব্যাসার্ধ সাধারণত:",
        ["Increases", "Decreases", "Remains constant", "Becomes infinite"],
        ["বাড়ে", "কমে", "অপরিবর্তিত থাকে", "অসীম হয়"],
        "B", "easy", "conceptual",
        "Increasing nuclear charge pulls electrons closer across a period.",
        "পর্যায় বরাবর নিউক্লিয়ার চার্জ বৃদ্ধিতে ইলেকট্রন কাছে টানা হয়।",
    ),
    q(
        "Down a group, atomic radius generally:",
        "গ্রুপ নিচে পারমাণবিক ব্যাসার্ধ সাধারণত:",
        ["Decreases", "Increases", "Stays the same", "Oscillates randomly"],
        ["কমে", "বাড়ে", "একই থাকে", "এলোমেলো দোদুল্যমান"],
        "B", "easy", "conceptual",
        "New electron shells are added down a group, increasing size.",
        "গ্রুপ নিচে নতুন ইলেকট্রন শেল যোগ হয়ে আকার বাড়ে।",
    ),
    q(
        "Ionization energy is the energy required to:",
        "আয়নীকরণ শক্তি হলো কোনটির জন্য প্রয়োজনীয় শক্তি?",
        ["Add an electron to a neutral atom", "Remove an electron from a gaseous atom", "Break a covalent bond only", "Melt a solid metal"],
        ["নিরপেক্ষ পরমাণুতে ইলেকট্রন যোগ", "গ্যাসীয় পরমাণু থেকে ইলেকট্রন অপসারণ", "শুধু সমযোজী বন্ধন ভাঙা", "কঠিন ধাতু গলানো"],
        "B", "easy", "factual",
        "First ionization energy removes the outermost electron from a gaseous atom.",
        "প্রথম আয়নীকরণ শক্তি গ্যাসীয় পরমাণুর বহিঃস্থ ইলেকট্রন অপসারণ করে।",
    ),
    q(
        "Across a period, first ionization energy generally:",
        "পর্যায় বরাবর প্রথম আয়নীকরণ শক্তি সাধারণত:",
        ["Decreases", "Increases", "Is zero", "Depends only on mass"],
        ["কমে", "বাড়ে", "শূন্য", "শুধু ভরের উপর নির্ভর"],
        "B", "easy", "conceptual",
        "Smaller atoms with higher effective nuclear charge hold electrons more tightly.",
        "উচ্চ কার্যকর নিউক্লিয়ার চার্জযুক্ত ছোট পরমাণু ইলেকট্রন শক্তভাবে ধরে।",
    ),
    q(
        "Electron affinity is related to the energy change when an atom:",
        "ইলেকট্রন আসক্তি কোন প্রক্রিয়ার শক্তি পরিবর্তনের সাথে সম্পর্কিত?",
        ["Loses a proton", "Gains an electron", "Emits a neutron", "Forms a cation only"],
        ["প্রোটন হারায়", "ইলেকট্রন গ্রহণ করে", "নিউট্রন নির্গত করে", "শুধু ধনাত্মক আয়ন গঠন করে"],
        "B", "easy", "factual",
        "Electron affinity concerns adding an electron to a gaseous atom/ion.",
        "ইলেকট্রন আসক্তি গ্যাসীয় পরমাণু/আয়নে ইলেকট্রন যোগের সাথে জড়িত।",
    ),
    q(
        "Which element typically has the highest electronegativity?",
        "কোন মৌলের তড়িৎঋণাত্মকতা সাধারণত সর্বোচ্চ?",
        ["Francium", "Fluorine", "Cesium", "Sodium"],
        ["ফ্রান্সিয়াম", "ফ্লুরিন", "সিজিয়াম", "সোডিয়াম"],
        "B", "easy", "factual",
        "Fluorine is the most electronegative element on the Pauling scale.",
        "পলিং স্কেলে ফ্লুরিন সবচেয়ে তড়িৎঋণাত্মক মৌল।",
    ),
    q(
        "Metallic character across a period generally:",
        "পর্যায় বরাবর ধাতব ধর্ম সাধারণত:",
        ["Increases", "Decreases", "Remains maximum always", "Is undefined"],
        ["বাড়ে", "কমে", "সবসময় সর্বোচ্চ থাকে", "অনির্ধারিত"],
        "B", "easy", "conceptual",
        "Left-side metals give way to non-metals on the right of a period.",
        "পর্যায়ের বামে ধাতু, ডানে অধাতু — ধাতব ধর্ম কমে।",
    ),
    q(
        "Which ion is larger: Na+ or Na?",
        "Na+ ও Na এর মধ্যে কোনটি বড়?",
        ["Na+", "Na", "They are equal", "Neither exists"],
        ["Na+", "Na", "এরা সমান", "কোনোটিই নেই"],
        "B", "medium", "conceptual",
        "Removing an electron shrinks the atom; Na is larger than Na+.",
        "ইলেকট্রন অপসারণে আকার ছোট হয়; Na, Na+ এর চেয়ে বড়।",
    ),
    q(
        "Among O2−, F−, Na+, and Mg2+ (isoelectronic), the smallest ion is:",
        "O2−, F−, Na+, Mg2+ (আইসোইলেকট্রনিক) এর মধ্যে ক্ষুদ্রতম কোনটি?",
        ["O2−", "F−", "Na+", "Mg2+"],
        ["O2−", "F−", "Na+", "Mg2+"],
        "D", "hard", "application",
        "Same electrons, highest nuclear charge (Mg2+) gives smallest radius.",
        "একই ইলেকট্রন সংখ্যায় সর্বোচ্চ নিউক্লিয়ার চার্জ (Mg2+) ক্ষুদ্রতম ব্যাসার্ধ দেয়।",
    ),
    q(
        "Second ionization energy is always higher than the first because:",
        "দ্বিতীয় আয়নীকরণ শক্তি প্রথমটির চেয়ে বেশি কারণ:",
        ["The atom gains mass", "Removing an electron from a cation is harder", "Orbitals disappear", "Temperature falls"],
        ["পরমাণুর ভর বাড়ে", "ধনাত্মক আয়ন থেকে ইলেকট্রন সরানো কঠিনতর", "অরবিটাল অদৃশ্য হয়", "তাপমাত্রা কমে"],
        "B", "medium", "conceptual",
        "A positive ion attracts remaining electrons more strongly.",
        "ধনাত্মক আয়ন অবশিষ্ট ইলেকট্রনকে আরও শক্তভাবে আকর্ষণ করে।",
    ),
    q(
        "Alkali metals have low ionization energies mainly because:",
        "ক্ষার ধাতুর আয়নীকরণ শক্তি কম প্রধানত কারণ:",
        ["They have full octets", "Valence electron is loosely held in a large atom", "They are gases", "They have no electrons"],
        ["এদের পূর্ণ অক্টেট আছে", "বড় পরমাণুতে যোজনী ইলেকট্রন শিথিলভাবে আবদ্ধ", "এরা গ্যাস", "এদের ইলেকট্রন নেই"],
        "B", "medium", "conceptual",
        "Large size and single ns1 electron make removal easy.",
        "বড় আকার ও একক ns1 ইলেকট্রন অপসারণ সহজ করে।",
    ),
    q(
        "Electronegativity down a group generally:",
        "গ্রুপ নিচে তড়িৎঋণাত্মকতা সাধারণত:",
        ["Increases", "Decreases", "Becomes infinite", "Equals atomic mass"],
        ["বাড়ে", "কমে", "অসীম হয়", "পারমাণবিক ভরের সমান"],
        "B", "easy", "conceptual",
        "Larger atoms attract bonding electrons less strongly.",
        "বড় পরমাণু বন্ধন ইলেকট্রন কম শক্তভাবে আকর্ষণ করে।",
    ),
    q(
        "Which property decreases down group 17 (halogens)?",
        "গ্রুপ ১৭ (হ্যালোজেন) নিচে কোন ধর্ম কমে?",
        ["Atomic radius", "Electronegativity", "Boiling point of F2 only always", "Number of electron shells"],
        ["পারমাণবিক ব্যাসার্ধ", "তড়িৎঋণাত্মকতা", "শুধু F2 এর স্ফুটনাঙ্ক সবসময়", "ইলেকট্রন শেলের সংখ্যা"],
        "B", "medium", "application",
        "Electronegativity falls down the halogen group as atoms enlarge.",
        "হ্যালোজেন গ্রুপে আকার বাড়লে তড়িৎঋণাত্মকতা কমে।",
    ),
    q(
        "Effective nuclear charge (Zeff) across a period generally:",
        "পর্যায় বরাবর কার্যকর নিউক্লিয়ার চার্জ (Zeff) সাধারণত:",
        ["Decreases", "Increases", "Is constant for all elements", "Is zero"],
        ["কমে", "বাড়ে", "সব মৌলে ধ্রুবক", "শূন্য"],
        "B", "medium", "conceptual",
        "Added protons outweigh added shielding within a period.",
        "পর্যায়ে প্রোটন বৃদ্ধি শিল্ডিংয়ের চেয়ে বেশি প্রভাব ফেলে।",
    ),
    q(
        "Which is a typical non-metallic property?",
        "কোনটি সাধারণ অধাতব ধর্ম?",
        ["High electrical conductivity", "Tendency to form cations", "High electronegativity and anion formation", "Malleability"],
        ["উচ্চ তড়িৎ পরিবাহিতা", "ধনাত্মক আয়ন গঠনের প্রবণতা", "উচ্চ তড়িৎঋণাত্মকতা ও ঋণাত্মক আয়ন গঠন", "নমনীয়তা"],
        "C", "easy", "conceptual",
        "Non-metals attract electrons and often form anions.",
        "অধাতু ইলেকট্রন আকর্ষণ করে ও প্রায়ই ঋণাত্মক আয়ন গঠন করে।",
    ),
    q(
        "The element with the largest atomic radius among Li, Be, B, and C is:",
        "Li, Be, B, C এর মধ্যে বৃহত্তম পারমাণবিক ব্যাসার্ধ কোনটির?",
        ["Li", "Be", "B", "C"],
        ["Li", "Be", "B", "C"],
        "A", "medium", "application",
        "In period 2, Li is leftmost and largest.",
        "পর্যায় ২ এ Li সবচেয়ে বামে ও বৃহত্তম।",
    ),
    q(
        "Why is the first ionization energy of Be higher than that of B?",
        "Be এর প্রথম আয়নীকরণ শক্তি B এর চেয়ে বেশি কেন?",
        ["Be has more protons than B", "Be has a stable filled 2s2 subshell", "B is a noble gas", "Be has no electrons"],
        ["Be তে B এর চেয়ে বেশি প্রোটন", "Be এর স্থিতিশীল পূর্ণ 2s2 সাবশেল", "B নিষ্ক্রিয় গ্যাস", "Be তে ইলেকট্রন নেই"],
        "B", "hard", "conceptual",
        "Removing an electron from filled 2s2 (Be) is harder than from 2p1 (B).",
        "পূর্ণ 2s2 (Be) থেকে ইলেকট্রন সরানো 2p1 (B) এর চেয়ে কঠিন।",
    ),
    q(
        "Oxidizing power of halogens down the group generally:",
        "গ্রুপ নিচে হ্যালোজেনের জারক ক্ষমতা সাধারণত:",
        ["Increases", "Decreases", "Remains identical", "Becomes catalytic only"],
        ["বাড়ে", "কমে", "অভিন্ন থাকে", "শুধু অনুঘটক হয়"],
        "B", "medium", "conceptual",
        "F2 is the strongest oxidizer; oxidizing power falls down the group.",
        "F2 সবচেয়ে শক্তিশালী জারক; গ্রুপ নিচে জারক ক্ষমতা কমে।",
    ),
    q(
        "Cations are smaller than their parent atoms because:",
        "ধনাত্মক আয়ন মূল পরমাণুর চেয়ে ছোট কারণ:",
        ["Proton number decreases", "Electron–electron repulsion decreases and Zeff rises", "Neutrons are lost", "Orbitals expand"],
        ["প্রোটন সংখ্যা কমে", "ইলেকট্রন–ইলেকট্রন বিকর্ষণ কমে ও Zeff বাড়ে", "নিউট্রন হারায়", "অরবিটাল প্রসারিত হয়"],
        "B", "medium", "conceptual",
        "Fewer electrons mean less repulsion and stronger nuclear pull per electron.",
        "কম ইলেকট্রনে বিকর্ষণ কম ও প্রতি ইলেকট্রনে নিউক্লিয়ার আকর্ষণ বাড়ে।",
    ),
    q(
        "Which trend correctly describes reactivity of alkali metals down the group?",
        "গ্রুপ নিচে ক্ষার ধাতুর সক্রিয়তা কোনটি সঠিকভাবে বর্ণনা করে?",
        ["Decreases", "Increases", "Is zero for all", "Depends only on color"],
        ["কমে", "বাড়ে", "সবগুলোর শূন্য", "শুধু রঙের উপর নির্ভর"],
        "B", "easy", "conceptual",
        "Larger atoms lose the valence electron more readily down the group.",
        "গ্রুপ নিচে বড় পরমাণু যোজনী ইলেকট্রন সহজে হারায়।",
    ),
]

# --- t03: Ionic and covalent bonding ---
T03 = [
    q(
        "An ionic bond is mainly formed by:",
        "আয়নিক বন্ধন প্রধানত গঠিত হয়:",
        ["Sharing of electrons equally", "Transfer of electrons between atoms", "Nuclear fusion", "Hydrogen bonding only"],
        ["ইলেকট্রনের সমান ভাগাভাগি", "পরমাণুর মধ্যে ইলেকট্রন স্থানান্তর", "নিউক্লিয়ার ফিউশন", "শুধু হাইড্রোজেন বন্ধন"],
        "B", "easy", "factual",
        "Ionic bonds arise from electron transfer creating cations and anions.",
        "ইলেকট্রন স্থানান্তরে ধনাত্মক ও ঋণাত্মক আয়ন তৈরি হয়ে আয়নিক বন্ধন হয়।",
    ),
    q(
        "A covalent bond involves:",
        "সমযোজী বন্ধনে জড়িত:",
        ["Complete electron transfer only", "Sharing of electron pairs", "Only metallic lattices", "Proton exchange"],
        ["শুধু সম্পূর্ণ ইলেকট্রন স্থানান্তর", "ইলেকট্রন জোড়ার ভাগাভাগি", "শুধু ধাতব জালক", "প্রোটন বিনিময়"],
        "B", "easy", "factual",
        "Covalent bonding shares one or more electron pairs between atoms.",
        "সমযোজী বন্ধনে পরমাণুর মধ্যে এক বা একাধিক ইলেকট্রন জোড়া ভাগাভাগি হয়।",
    ),
    q(
        "Which compound is typically ionic?",
        "কোন যৌগ সাধারণত আয়নিক?",
        ["CH4", "H2O", "NaCl", "Cl2"],
        ["CH4", "H2O", "NaCl", "Cl2"],
        "C", "easy", "application",
        "NaCl forms from Na+ and Cl− via electron transfer.",
        "Na+ ও Cl− এর ইলেকট্রন স্থানান্তরে NaCl আয়নিক।",
    ),
    q(
        "Which molecule is a classic example of a nonpolar covalent bond?",
        "কোন অণু অপোলার সমযোজী বন্ধনের ক্লাসিক উদাহরণ?",
        ["HCl", "NaF", "Cl2", "HF"],
        ["HCl", "NaF", "Cl2", "HF"],
        "C", "easy", "application",
        "Identical atoms share electrons equally in Cl2.",
        "Cl2 তে অভিন্ন পরমাণু সমানভাবে ইলেকট্রন ভাগ করে।",
    ),
    q(
        "Electronegativity difference is large in which type of bond?",
        "কোন ধরনের বন্ধনে তড়িৎঋণাত্মকতার পার্থক্য বড়?",
        ["Nonpolar covalent", "Metallic only", "Ionic", "van der Waals only"],
        ["অপোলার সমযোজী", "শুধু ধাতব", "আয়নিক", "শুধু ভ্যান ডার ওয়ালস"],
        "C", "easy", "conceptual",
        "Large ΔEN favors electron transfer and ionic character.",
        "বড় ΔEN ইলেকট্রন স্থানান্তর ও আয়নিক চরিত্র সহায়তা করে।",
    ),
    q(
        "A polar covalent bond forms when:",
        "পোলার সমযোজী বন্ধন গঠিত হয় যখন:",
        ["Atoms have identical electronegativity", "Electrons are shared unequally", "Only metals bond", "Ions completely separate in vacuum always"],
        ["পরমাণুর তড়িৎঋণাত্মকতা অভিন্ন", "ইলেকট্রন অসমভাবে ভাগাভাগি হয়", "শুধু ধাতু বন্ধন করে", "শূন্যে আয়ন সবসময় সম্পূর্ণ পৃথক"],
        "B", "easy", "conceptual",
        "Unequal sharing creates partial charges (δ+ and δ−).",
        "অসম ভাগাভাগিতে আংশিক চার্জ (δ+ ও δ−) সৃষ্টি হয়।",
    ),
    q(
        "Lattice energy of an ionic crystal is the energy released when:",
        "আয়নিক স্ফটিকের জালক শক্তি হলো কোন প্রক্রিয়ায় মুক্ত শক্তি?",
        ["Gaseous ions form a solid crystal lattice", "The crystal melts", "Electrons are shared", "Molecules sublime only"],
        ["গ্যাসীয় আয়ন থেকে কঠিন স্ফটিক জালক গঠন", "স্ফটিক গলে", "ইলেকট্রন ভাগাভাগি হয়", "শুধু অণু সাবলাইম হয়"],
        "A", "medium", "factual",
        "Lattice energy measures stability of the ionic lattice from gaseous ions.",
        "গ্যাসীয় আয়ন থেকে জালক গঠনের স্থিতিশীলতা জালক শক্তি নির্দেশ করে।",
    ),
    q(
        "According to the octet rule, atoms tend to achieve:",
        "অক্টেট নিয়ম অনুসারে পরমাণু অর্জন করতে চায়:",
        ["Two valence electrons always", "Eight electrons in the outer shell (often)", "Zero electrons", "Sixteen protons"],
        ["সবসময় দুই যোজনী ইলেকট্রন", "বহিঃস্থ শেলে প্রায়ই আট ইলেকট্রন", "শূন্য ইলেকট্রন", "ষোলো প্রোটন"],
        "B", "easy", "factual",
        "Many main-group atoms seek a noble-gas-like octet.",
        "অনেক মূল-গ্রুপ পরমাণু নিষ্ক্রিয় গ্যাসের মতো অক্টেট চায়।",
    ),
    q(
        "A coordinate (dative) covalent bond is formed when:",
        "সমন্বয় (ডেটিভ) সমযোজী বন্ধন গঠিত হয় যখন:",
        ["Both atoms contribute one electron each always", "One atom donates both electrons of the shared pair", "Protons are shared", "Only ionic transfer occurs"],
        ["সবসময় উভয় পরমাণু একটি করে ইলেকট্রন দেয়", "এক পরমাণু ভাগাভাগি জোড়ার দুই ইলেকট্রন দান করে", "প্রোটন ভাগাভাগি হয়", "শুধু আয়নিক স্থানান্তর হয়"],
        "B", "medium", "conceptual",
        "In NH4+ or BF3·NH3, one atom supplies the entire bonding pair.",
        "NH4+ বা BF3·NH3 তে এক পরমাণু পুরো বন্ধন জোড়া সরবরাহ করে।",
    ),
    q(
        "Which species contains a coordinate bond?",
        "কোন প্রজাতিতে সমন্বয় বন্ধন আছে?",
        ["H2", "Cl2", "NH4+", "NaCl lattice ion pair only"],
        ["H2", "Cl2", "NH4+", "শুধু NaCl জালকের আয়ন জোড়া"],
        "C", "medium", "application",
        "In NH4+, the H+ accepts a lone pair from NH3 (coordinate bond).",
        "NH4+ এ H+ NH3 এর একাকী জোড়া গ্রহণ করে (সমন্বয় বন্ধন)।",
    ),
    q(
        "Metallic bonding is characterized by:",
        "ধাতব বন্ধনের বৈশিষ্ট্য:",
        ["Fixed shared pairs between two atoms only", "A sea of delocalized electrons around metal cations", "Only hydrogen bridges", "Complete insulation"],
        ["শুধু দুই পরমাণুর স্থির ভাগাভাগি জোড়া", "ধাতব ধনাত্মক আয়নের চারপাশে বিমুক্ত ইলেকট্রনের সমুদ্র", "শুধু হাইড্রোজেন সেতু", "সম্পূর্ণ অন্তরকতা"],
        "B", "easy", "conceptual",
        "Delocalized electrons explain metal conductivity and malleability.",
        "বিমুক্ত ইলেকট্রন ধাতুর পরিবাহিতা ও নমনীয়তা ব্যাখ্যা করে।",
    ),
    q(
        "Which statement about ionic compounds is generally true?",
        "আয়নিক যৌগ সম্পর্কে কোন বিবৃতি সাধারণত সত্য?",
        ["They are soft gases at room temperature always", "They conduct electricity when molten or aqueous", "They never dissolve in water", "They have only London forces"],
        ["কক্ষতাপমাত্রায় সবসময় নরম গ্যাস", "গলিত বা জলীয় অবস্থায় তড়িৎ পরিবহন করে", "কখনো পানিতে দ্রবীভূত হয় না", "শুধু লন্ডন বল থাকে"],
        "B", "easy", "conceptual",
        "Mobile ions in melt or solution carry current; solid lattices usually do not.",
        "গলিত/দ্রবণে চলমান আয়ন তড়িৎ বহন করে; কঠিন জালকে সাধারণত করে না।",
    ),
    q(
        "A double covalent bond shares how many electron pairs?",
        "দ্বিবন্ধন সমযোজী বন্ধনে কত জোড়া ইলেকট্রন ভাগাভাগি হয়?",
        ["One", "Two", "Three", "Four"],
        ["এক", "দুই", "তিন", "চার"],
        "B", "easy", "factual",
        "A double bond shares two pairs (four electrons), as in O2 or C=C.",
        "দ্বিবন্ধনে দুই জোড়া (চার ইলেকট্রন) ভাগ হয়, যেমন O2 বা C=C।",
    ),
    q(
        "Which molecule has a triple bond?",
        "কোন অণুতে ত্রিবন্ধন আছে?",
        ["H2O", "NH3", "N2", "CH4"],
        ["H2O", "NH3", "N2", "CH4"],
        "C", "easy", "application",
        "N2 has a triple covalent bond (one σ and two π).",
        "N2 তে ত্রিবন্ধন আছে (এক σ ও দুই π)।",
    ),
    q(
        "Fajans' rules help predict when a bond has more:",
        "ফাজানসের নিয়ম কোনটির অধিক উপস্থিতি অনুমানে সাহায্য করে?",
        ["Pure ionic character always", "Covalent character in ionic compounds", "Nuclear binding energy", "Only metallic luster"],
        ["সবসময় বিশুদ্ধ আয়নিক চরিত্র", "আয়নিক যৌগে সমযোজী চরিত্র", "নিউক্লিয়ার বন্ধন শক্তি", "শুধু ধাতব ঔজ্জ্বল্য"],
        "B", "hard", "conceptual",
        "Small highly charged cations polarize anions, increasing covalent character.",
        "ছোট উচ্চ চার্জযুক্ত ধনাত্মক আয়ন ঋণাত্মক আয়নকে পোলারাইজ করে সমযোজী চরিত্র বাড়ায়।",
    ),
    q(
        "Which bond is most polar?",
        "কোন বন্ধন সবচেয়ে পোলার?",
        ["H−H", "C−H", "H−F", "Cl−Cl"],
        ["H−H", "C−H", "H−F", "Cl−Cl"],
        "C", "medium", "application",
        "H−F has the largest electronegativity difference among the options.",
        "বিকল্পগুলোর মধ্যে H−F এ তড়িৎঋণাত্মকতার পার্থক্য সবচেয়ে বেশি।",
    ),
    q(
        "Lewis structures represent:",
        "লুইস গঠন প্রকাশ করে:",
        ["Nuclear protons only", "Valence electrons as dots and bonding pairs", "Only crystal packing", "Neutron orbits"],
        ["শুধু নিউক্লিয়ার প্রোটন", "যোজনী ইলেকট্রন বিন্দু ও বন্ধন জোড়া হিসেবে", "শুধু স্ফটিক প্যাকিং", "নিউট্রন কক্ষপথ"],
        "B", "easy", "factual",
        "Lewis diagrams show valence electrons and shared pairs.",
        "লুইস চিত্র যোজনী ইলেকট্রন ও ভাগাভাগি জোড়া দেখায়।",
    ),
    q(
        "Resonance structures are used when:",
        "অনুনাদ গঠন ব্যবহার হয় যখন:",
        ["A molecule has no electrons", "One Lewis structure cannot fully describe bonding", "Only ionic salts form", "Temperature is absolute zero"],
        ["অণুতে ইলেকট্রন নেই", "এক লুইস গঠন বন্ধন পুরোপুরি বর্ণনা করতে পারে না", "শুধু আয়নিক লবণ গঠিত হয়", "তাপমাত্রা পরম শূন্য"],
        "B", "medium", "conceptual",
        "Actual structure is a hybrid of contributing resonance forms (e.g., O3, benzene).",
        "প্রকৃত গঠন অনুনাদ রূপগুলোর সংকর (যেমন O3, বেনজিন)।",
    ),
    q(
        "Which compound shows predominantly covalent bonding?",
        "কোন যৌগে প্রধানত সমযোজী বন্ধন দেখা যায়?",
        ["MgO", "KBr", "CO2", "CaF2"],
        ["MgO", "KBr", "CO2", "CaF2"],
        "C", "easy", "application",
        "CO2 has polar covalent C=O bonds, not a simple ionic lattice.",
        "CO2 তে পোলার সমযোজী C=O বন্ধন; সরল আয়নিক জালক নয়।",
    ),
    q(
        "Born–Haber cycle is used to determine:",
        "বোর্ন–হ্যাবার চক্র ব্যবহার হয় নির্ধারণ করতে:",
        ["pH of acids", "Lattice energy of ionic compounds", "Hybridization of CH4 only", "Optical activity"],
        ["অম্লের pH", "আয়নিক যৌগের জালক শক্তি", "শুধু CH4 এর সংকরায়ন", "আলোক সক্রিয়তা"],
        "B", "hard", "factual",
        "Born–Haber relates formation enthalpy steps to lattice energy.",
        "বোর্ন–হ্যাবার গঠন এনথ্যালপির ধাপগুলোকে জালক শক্তির সাথে যুক্ত করে।",
    ),
]

# --- t04: Molecular shape and hybridization ---
T04 = [
    q(
        "VSEPR theory predicts molecular shape based on:",
        "VSEPR তত্ত্ব অণুর আকৃতি পূর্বানুমান করে কোনটির ভিত্তিতে?",
        ["Nuclear mass only", "Repulsion between electron pairs around the central atom", "Color of the compound", "Only bond lengths in metals"],
        ["শুধু নিউক্লিয়ার ভর", "কেন্দ্রীয় পরমাণুর চারপাশে ইলেকট্রন জোড়ার বিকর্ষণ", "যৌগের রঙ", "শুধু ধাতুর বন্ধন দৈর্ঘ্য"],
        "B", "easy", "conceptual",
        "Electron pairs arrange to minimize repulsion, setting geometry.",
        "ইলেকট্রন জোড়া বিকর্ষণ কমাতে সাজায় — এতে জ্যামিতি নির্ধারিত হয়।",
    ),
    q(
        "The shape of BeCl2 (gas phase) is:",
        "BeCl2 (গ্যাস দশা) এর আকৃতি কোনটি?",
        ["Bent", "Linear", "Trigonal planar", "Tetrahedral"],
        ["বাঁকা", "রৈখিক", "ত্রিকোণীয় সমতল", "চতুস্তলকীয়"],
        "B", "easy", "factual",
        "Two bonding pairs and no lone pairs give linear geometry (180°).",
        "দুই বন্ধন জোড়া ও কোনো একাকী জোড়া নেই — রৈখিক (১৮০°)।",
    ),
    q(
        "BF3 has which molecular geometry?",
        "BF3 এর আণবিক জ্যামিতি কোনটি?",
        ["Tetrahedral", "Trigonal planar", "Pyramidal", "Octahedral"],
        ["চতুস্তলকীয়", "ত্রিকোণীয় সমতল", "পিরামিডাল", "অষ্টতলকীয়"],
        "B", "easy", "factual",
        "Three bonding pairs, no lone pairs → trigonal planar (120°).",
        "তিন বন্ধন জোড়া, একাকী জোড়া নেই → ত্রিকোণীয় সমতল (১২০°)।",
    ),
    q(
        "The bond angle in CH4 is approximately:",
        "CH4 এর বন্ধন কোণ প্রায় কত?",
        ["90°", "109.5°", "120°", "180°"],
        ["৯০°", "১০৯.৫°", "১২০°", "১৮০°"],
        "B", "easy", "numerical",
        "Tetrahedral methane has H−C−H angles of about 109.5°.",
        "চতুস্তলকীয় মিথেনের H−C−H কোণ প্রায় ১০৯.৫°।",
    ),
    q(
        "NH3 has a trigonal pyramidal shape because:",
        "NH3 এর আকৃতি ত্রিকোণীয় পিরামিডাল কারণ:",
        ["It has four bonding pairs", "It has three bonding pairs and one lone pair", "It is linear", "It has no electrons"],
        ["এর চার বন্ধন জোড়া আছে", "এর তিন বন্ধন জোড়া ও এক একাকী জোড়া আছে", "এটি রৈখিক", "এতে ইলেকট্রন নেই"],
        "B", "medium", "conceptual",
        "The lone pair compresses H−N−H angles below 109.5° (~107°).",
        "একাকী জোড়া H−N−H কোণ ১০৯.৫° এর নিচে (~১০৭°) চাপে।",
    ),
    q(
        "The shape of H2O is:",
        "H2O এর আকৃতি কোনটি?",
        ["Linear", "Tetrahedral", "Bent (angular)", "Trigonal planar"],
        ["রৈখিক", "চতুস্তলকীয়", "বাঁকা (কৌণিক)", "ত্রিকোণীয় সমতল"],
        "C", "easy", "factual",
        "Two bonding and two lone pairs give a bent molecular shape.",
        "দুই বন্ধন ও দুই একাকী জোড়া বাঁকা আণবিক আকৃতি দেয়।",
    ),
    q(
        "Hybridization of carbon in CH4 is:",
        "CH4 এ কার্বনের সংকরায়ন কোনটি?",
        ["sp", "sp2", "sp3", "sp3d"],
        ["sp", "sp2", "sp3", "sp3d"],
        "C", "easy", "factual",
        "Four equivalent C−H bonds arise from sp3 hybrid orbitals.",
        "চারটি সমতুল্য C−H বন্ধন sp3 সংকর অরবিটাল থেকে আসে।",
    ),
    q(
        "Hybridization of carbon in ethene (C2H4) is:",
        "ইথিন (C2H4) এ কার্বনের সংকরায়ন কোনটি?",
        ["sp", "sp2", "sp3", "dsp2"],
        ["sp", "sp2", "sp3", "dsp2"],
        "B", "medium", "factual",
        "Each carbon in ethene is trigonal planar sp2 with a π bond.",
        "ইথিনের প্রতিটি কার্বন ত্রিকোণীয় সমতল sp2 ও একটি π বন্ধনযুক্ত।",
    ),
    q(
        "Hybridization of carbon in ethyne (C2H2) is:",
        "ইথাইন (C2H2) এ কার্বনের সংকরায়ন কোনটি?",
        ["sp", "sp2", "sp3", "sp3d2"],
        ["sp", "sp2", "sp3", "sp3d2"],
        "A", "medium", "factual",
        "Linear ethyne carbons are sp hybridized with two π bonds.",
        "রৈখিক ইথাইনের কার্বন sp সংকরিত; দুইটি π বন্ধন আছে।",
    ),
    q(
        "The number of hybrid orbitals equals:",
        "সংকর অরবিটালের সংখ্যা সমান:",
        ["Atomic number", "Number of atomic orbitals mixed", "Mass number", "Neutron count"],
        ["পারমাণবিক সংখ্যা", "মিশ্রিত পারমাণবিক অরবিটালের সংখ্যা", "ভর সংখ্যা", "নিউট্রন সংখ্যা"],
        "B", "easy", "conceptual",
        "n atomic orbitals combine to form n hybrid orbitals.",
        "nটি পারমাণবিক অরবিটাল মিলে nটি সংকর অরবিটাল গঠন করে।",
    ),
    q(
        "PCl5 has which geometry around phosphorus?",
        "PCl5 এ ফসফরাসের চারপাশের জ্যামিতি কোনটি?",
        ["Tetrahedral", "Trigonal bipyramidal", "Octahedral", "Linear"],
        ["চতুস্তলকীয়", "ত্রিকোণীয় দ্বিপিরামিডাল", "অষ্টতলকীয়", "রৈখিক"],
        "B", "medium", "factual",
        "Five bonding pairs give trigonal bipyramidal geometry (sp3d).",
        "পাঁচ বন্ধন জোড়া ত্রিকোণীয় দ্বিপিরামিডাল জ্যামিতি দেয় (sp3d)।",
    ),
    q(
        "SF6 has which molecular geometry?",
        "SF6 এর আণবিক জ্যামিতি কোনটি?",
        ["Tetrahedral", "Square planar", "Octahedral", "Trigonal planar"],
        ["চতুস্তলকীয়", "বর্গীয় সমতল", "অষ্টতলকীয়", "ত্রিকোণীয় সমতল"],
        "C", "medium", "factual",
        "Six bonding pairs → octahedral (sp3d2).",
        "ছয় বন্ধন জোড়া → অষ্টতলকীয় (sp3d2)।",
    ),
    q(
        "Lone pairs affect bond angles because they:",
        "একাকী জোড়া বন্ধন কোণ প্রভাবিত করে কারণ তারা:",
        ["Attract bonding pairs more weakly than bonding pairs do", "Repel more strongly than bonding pairs", "Have no charge", "Increase nuclear mass"],
        ["বন্ধন জোড়ার চেয়ে দুর্বল আকর্ষণ করে", "বন্ধন জোড়ার চেয়ে শক্তিশালী বিকর্ষণ করে", "কোনো চার্জ নেই", "নিউক্লিয়ার ভর বাড়ায়"],
        "B", "medium", "conceptual",
        "Lone-pair–bond-pair repulsion > bond-pair–bond-pair repulsion.",
        "একাকী–বন্ধন জোড়া বিকর্ষণ > বন্ধন–বন্ধন জোড়া বিকর্ষণ।",
    ),
    q(
        "The ideal bond angle in a trigonal planar molecule is:",
        "ত্রিকোণীয় সমতল অণুর আদর্শ বন্ধন কোণ কত?",
        ["90°", "109.5°", "120°", "180°"],
        ["৯০°", "১০৯.৫°", "১২০°", "১৮০°"],
        "C", "easy", "numerical",
        "Three equivalent pairs at 120° define trigonal planar geometry.",
        "তিন সমতুল্য জোড়া ১২০° কোণে ত্রিকোণীয় সমতল গঠন করে।",
    ),
    q(
        "Which molecule is linear?",
        "কোন অণু রৈখিক?",
        ["H2O", "SO2", "CO2", "NH3"],
        ["H2O", "SO2", "CO2", "NH3"],
        "C", "easy", "application",
        "CO2 has two double bonds and no lone pairs on carbon → linear.",
        "CO2 তে কার্বনে দুই দ্বিবন্ধন ও একাকী জোড়া নেই → রৈখিক।",
    ),
    q(
        "σ bonds are formed by:",
        "σ বন্ধন গঠিত হয়:",
        ["Sideways overlap of p orbitals only", "End-on (axial) overlap of orbitals", "Only London forces", "Proton tunneling"],
        ["শুধু p অরবিটালের পার্শ্বিক অধিক্রমণ", "অরবিটালের অক্ষীয় (প্রান্তিক) অধিক্রমণ", "শুধু লন্ডন বল", "প্রোটন টানেলিং"],
        "B", "medium", "conceptual",
        "Head-on overlap produces a σ bond along the internuclear axis.",
        "মুখোমুখি অধিক্রমণে আন্তঃনিউক্লিয়ার অক্ষ বরাবর σ বন্ধন হয়।",
    ),
    q(
        "A π bond is formed by:",
        "π বন্ধন গঠিত হয়:",
        ["End-on s–s overlap only", "Sideways overlap of parallel p orbitals", "Only ionic attraction", "Neutron pairing"],
        ["শুধু অক্ষীয় s–s অধিক্রমণ", "সমান্তরাল p অরবিটালের পার্শ্বিক অধিক্রমণ", "শুধু আয়নিক আকর্ষণ", "নিউট্রন জোড়া"],
        "B", "medium", "conceptual",
        "Lateral p–p overlap above and below the axis forms a π bond.",
        "অক্ষের উপর ও নিচে পার্শ্বিক p–p অধিক্রমণে π বন্ধন হয়।",
    ),
    q(
        "In a double bond there are:",
        "দ্বিবন্ধনে থাকে:",
        ["Two σ bonds", "One σ and one π bond", "Two π bonds only", "Three σ bonds"],
        ["দুই σ বন্ধন", "এক σ ও এক π বন্ধন", "শুধু দুই π বন্ধন", "তিন σ বন্ধন"],
        "B", "easy", "factual",
        "A typical double bond = one σ + one π.",
        "সাধারণ দ্বিবন্ধন = এক σ + এক π।",
    ),
    q(
        "The hybridization of boron in BF3 is:",
        "BF3 এ বোরনের সংকরায়ন কোনটি?",
        ["sp", "sp2", "sp3", "sp3d"],
        ["sp", "sp2", "sp3", "sp3d"],
        "B", "medium", "application",
        "Three equivalent B−F bonds in a plane require sp2 hybrids.",
        "সমতলে তিন সমতুল্য B−F বন্ধনের জন্য sp2 সংকর প্রয়োজন।",
    ),
    q(
        "Why is the H−O−H angle in water less than 109.5°?",
        "পানিতে H−O−H কোণ ১০৯.৫° এর কম কেন?",
        ["Oxygen has no lone pairs", "Two lone pairs increase repulsion and compress the angle", "Hydrogen is larger than oxygen", "It is linear by VSEPR"],
        ["অক্সিজেনে একাকী জোড়া নেই", "দুই একাকী জোড়ার বিকর্ষণ কোণ চেপে দেয়", "হাইড্রোজেন অক্সিজেনের চেয়ে বড়", "VSEPR অনুসারে এটি রৈখিক"],
        "B", "medium", "conceptual",
        "Two lone pairs on oxygen reduce the bond angle to about 104.5°.",
        "অক্সিজেনের দুই একাকী জোড়া বন্ধন কোণ প্রায় ১০৪.৫° করে।",
    ),
]

# --- t05: Intermolecular forces ---
T05 = [
    q(
        "Intermolecular forces act:",
        "আন্তঃআণবিক বল ক্রিয়া করে:",
        ["Inside the nucleus only", "Between molecules", "Only between protons", "Only in vacuum with no matter"],
        ["শুধু নিউক্লিয়াসের ভিতরে", "অণুর মধ্যে", "শুধু প্রোটনের মধ্যে", "শুধু শূন্যে পদার্থ ছাড়া"],
        "B", "easy", "factual",
        "Intermolecular forces are attractions between separate molecules.",
        "আন্তঃআণবিক বল পৃথক অণুগুলোর মধ্যে আকর্ষণ।",
    ),
    q(
        "London dispersion forces are present in:",
        "লন্ডন বিচ্ছুরণ বল উপস্থিত থাকে:",
        ["Only ionic crystals", "All atoms and molecules", "Only metals", "Only aqueous acids"],
        ["শুধু আয়নিক স্ফটিকে", "সব পরমাণু ও অণুতে", "শুধু ধাতুতে", "শুধু জলীয় অম্লে"],
        "B", "easy", "conceptual",
        "Instantaneous dipoles create weak London forces even in nonpolar species.",
        "তাৎক্ষণিক দ্বিমেরু অপোলার প্রজাতিতেও দুর্বল লন্ডন বল সৃষ্টি করে।",
    ),
    q(
        "Dipole–dipole attractions occur between:",
        "দ্বিমেরু–দ্বিমেরু আকর্ষণ ঘটে:",
        ["Nonpolar molecules only", "Polar molecules", "Noble gas atoms only", "Neutrons"],
        ["শুধু অপোলার অণুতে", "পোলার অণুতে", "শুধু নিষ্ক্রিয় গ্যাস পরমাণুতে", "নিউট্রনে"],
        "B", "easy", "factual",
        "Permanent dipoles attract opposite ends of neighboring polar molecules.",
        "স্থায়ী দ্বিমেরু প্রতিবেশী পোলার অণুর বিপরীত প্রান্ত আকর্ষণ করে।",
    ),
    q(
        "Hydrogen bonding is a special strong attraction when H is bonded to:",
        "হাইড্রোজেন বন্ধন বিশেষ শক্তিশালী আকর্ষণ যখন H যুক্ত থাকে:",
        ["C, Si, or Ge", "N, O, or F", "Na, K, or Cs", "He, Ne, or Ar"],
        ["C, Si বা Ge", "N, O বা F", "Na, K বা Cs", "He, Ne বা Ar"],
        "B", "easy", "factual",
        "Highly electronegative N, O, F enable strong H-bonding.",
        "উচ্চ তড়িৎঋণাত্মক N, O, F শক্তিশালী H-বন্ধন সম্ভব করে।",
    ),
    q(
        "Ice floats on water mainly because of:",
        "বরফ পানিতে ভাসে প্রধানত কারণ:",
        ["Metallic bonding in ice", "Open hydrogen-bonded structure lowering density", "Higher molecular mass of ice", "Absence of any forces"],
        ["বরফে ধাতব বন্ধন", "উন্মুক্ত হাইড্রোজেন-বন্ধন গঠনে ঘনত্ব কম", "বরফের আণবিক ভর বেশি", "কোনো বলের অনুপস্থিতি"],
        "B", "medium", "conceptual",
        "H-bonded hexagonal lattice of ice is less dense than liquid water.",
        "বরফের H-বন্ধনযুক্ত ষড়ভুজ জালক তরল পানির চেয়ে কম ঘন।",
    ),
    q(
        "Which has the highest boiling point among H2O, H2S, H2Se, and H2Te (anomalous)?",
        "H2O, H2S, H2Se, H2Te এর মধ্যে কোনটির স্ফুটনাঙ্ক সর্বোচ্চ (ব্যতিক্রমী)?",
        ["H2S", "H2Se", "H2Te", "H2O"],
        ["H2S", "H2Se", "H2Te", "H2O"],
        "D", "medium", "application",
        "Strong hydrogen bonding raises water’s boiling point anomalously.",
        "শক্তিশালী হাইড্রোজেন বন্ধন পানির স্ফুটনাঙ্ক ব্যতিক্রমীভাবে বাড়ায়।",
    ),
    q(
        "Among F2, Cl2, Br2, and I2, London forces are strongest in:",
        "F2, Cl2, Br2, I2 এর মধ্যে লন্ডন বল সবচেয়ে শক্তিশালী কোনটিতে?",
        ["F2", "Cl2", "Br2", "I2"],
        ["F2", "Cl2", "Br2", "I2"],
        "D", "medium", "application",
        "Larger, more polarizable electron clouds give stronger dispersion forces.",
        "বড়, অধিক পোলারাইজেবল ইলেকট্রন মেঘ শক্তিশালী বিচ্ছুরণ বল দেয়।",
    ),
    q(
        "van der Waals forces broadly include:",
        "ভ্যান ডার ওয়ালস বল ব্যাপকভাবে অন্তর্ভুক্ত করে:",
        ["Only covalent bonds", "Dispersion, dipole–dipole, and related weak attractions", "Only ionic lattice energy", "Nuclear forces"],
        ["শুধু সমযোজী বন্ধন", "বিচ্ছুরণ, দ্বিমেরু–দ্বিমেরু ও সংশ্লিষ্ট দুর্বল আকর্ষণ", "শুধু আয়নিক জালক শক্তি", "নিউক্লিয়ার বল"],
        "B", "easy", "conceptual",
        "van der Waals is an umbrella term for weak intermolecular attractions.",
        "ভ্যান ডার ওয়ালস দুর্বল আন্তঃআণবিক আকর্ষণের ছাতা শব্দ।",
    ),
    q(
        "Which property increases with stronger intermolecular forces?",
        "শক্তিশালী আন্তঃআণবিক বলে কোন ধর্ম বাড়ে?",
        ["Vapor pressure at fixed T (generally)", "Boiling point", "Rate of evaporation always unboundedly", "Ideal gas deviation becoming zero"],
        ["নির্দিষ্ট T তে বাষ্প চাপ (সাধারণত)", "স্ফুটনাঙ্ক", "বাষ্পীভবন হার সবসময় সীমাহীনভাবে", "আদর্শ গ্যাস বিচ্যুতি শূন্য হওয়া"],
        "B", "easy", "conceptual",
        "Stronger attractions require more energy to separate molecules into vapor.",
        "শক্তিশালী আকর্ষণে অণু বাষ্পে আলাদা করতে বেশি শক্তি লাগে।",
    ),
    q(
        "Dry ice (solid CO2) sublimes easily partly because:",
        "ড্রাই আইস (কঠিন CO2) সহজে সাবলাইম হয় আংশিক কারণ:",
        ["It has metallic bonds", "Only weak London forces hold the nonpolar molecules", "It has strong H-bonds like ice", "It is ionic"],
        ["এতে ধাতব বন্ধন আছে", "অপোলার অণু শুধু দুর্বল লন্ডন বলে আবদ্ধ", "বরফের মতো শক্তিশালী H-বন্ধন আছে", "এটি আয়নিক"],
        "B", "medium", "conceptual",
        "Nonpolar CO2 is held by dispersion forces, so it sublimes at low T.",
        "অপোলার CO2 বিচ্ছুরণ বলে আবদ্ধ; কম তাপমাত্রায় সাবলাইম হয়।",
    ),
    q(
        "Which liquid shows significant hydrogen bonding?",
        "কোন তরলে উল্লেখযোগ্য হাইড্রোজেন বন্ধন দেখা যায়?",
        ["CCl4", "Hexane", "Ethanol (C2H5OH)", "Liquid argon"],
        ["CCl4", "হেক্সেন", "ইথানল (C2H5OH)", "তরল আর্গন"],
        "C", "easy", "application",
        "The −OH group in ethanol forms intermolecular H-bonds.",
        "ইথানলের −OH গ্রুপ আন্তঃআণবিক H-বন্ধন গঠন করে।",
    ),
    q(
        "Ion–dipole forces are important in:",
        "আয়ন–দ্বিমেরু বল গুরুত্বপূর্ণ কোনটিতে?",
        ["Dissolving ionic salts in water", "Bonding inside NaCl crystal lattice only", "Nuclear fission", "Forming diamond"],
        ["পানিতে আয়নিক লবণ দ্রবীভূত করা", "শুধু NaCl স্ফটিক জালকের অভ্যন্তরীণ বন্ধন", "নিউক্লিয়ার ফিশন", "হীরা গঠন"],
        "A", "medium", "application",
        "Water dipoles solvate Na+ and Cl− via ion–dipole attractions.",
        "পানির দ্বিমেরু আয়ন–দ্বিমেরু আকর্ষণে Na+ ও Cl− কে সলভেট করে।",
    ),
    q(
        "Compared with covalent bonds, intermolecular forces are generally:",
        "সমযোজী বন্ধনের তুলনায় আন্তঃআণবিক বল সাধারণত:",
        ["Much stronger", "Much weaker", "Identical in strength", "Nuclear in origin"],
        ["অনেক শক্তিশালী", "অনেক দুর্বল", "শক্তিতে অভিন্ন", "নিউক্লিয়ার উৎসের"],
        "B", "easy", "conceptual",
        "Breaking intermolecular forces changes phase; covalent bonds break in chemical reactions.",
        "আন্তঃআণবিক বল ভাঙলে দশা বদলায়; সমযোজী বন্ধন রাসায়নিক বিক্রিয়ায় ভাঙে।",
    ),
    q(
        "Why does HF have a higher boiling point than HCl?",
        "HF এর স্ফুটনাঙ্ক HCl এর চেয়ে বেশি কেন?",
        ["HF has weaker forces", "HF forms strong hydrogen bonds", "HF is heavier than HCl", "HF is nonpolar"],
        ["HF এর বল দুর্বল", "HF শক্তিশালী হাইড্রোজেন বন্ধন গঠন করে", "HF, HCl এর চেয়ে ভারী", "HF অপোলার"],
        "B", "medium", "conceptual",
        "H-bonding in HF outweighs the larger dispersion forces in HCl.",
        "HF এর H-বন্ধন HCl এর বৃহত্তর বিচ্ছুরণ বলকে ছাড়িয়ে যায়।",
    ),
    q(
        "Surface tension of water is relatively high mainly due to:",
        "পানির পৃষ্ঠটান তুলনামূলকভাবে বেশি প্রধানত কারণ:",
        ["London forces only in air", "Strong hydrogen bonding among surface molecules", "Absence of polarity", "Metallic cohesion"],
        ["শুধু বাতাসে লন্ডন বল", "পৃষ্ঠের অণুগুলোর মধ্যে শক্তিশালী হাইড্রোজেন বন্ধন", "পোলারিটির অনুপস্থিতি", "ধাতব সংহতি"],
        "B", "medium", "conceptual",
        "H-bonded surface molecules resist expansion of surface area.",
        "H-বন্ধনযুক্ত পৃষ্ঠ অণু পৃষ্ঠক্ষেত্র বৃদ্ধির বিরুদ্ধে প্রতিরোধ করে।",
    ),
    q(
        "Which interaction is strongest among the following?",
        "নিচের কোন আন্তঃক্রিয়া সবচেয়ে শক্তিশালী?",
        ["London force between CH4 molecules", "Dipole–dipole in HCl gas", "Hydrogen bond in liquid HF", "Dispersion in He"],
        ["CH4 অণুর মধ্যে লন্ডন বল", "HCl গ্যাসে দ্বিমেরু–দ্বিমেরু", "তরল HF এ হাইড্রোজেন বন্ধন", "He তে বিচ্ছুরণ"],
        "C", "medium", "application",
        "Hydrogen bonds are stronger than typical dipole–dipole or London forces.",
        "হাইড্রোজেন বন্ধন সাধারণ দ্বিমেরু–দ্বিমেরু বা লন্ডন বলের চেয়ে শক্তিশালী।",
    ),
    q(
        "Capillary rise of water in a glass tube is aided by:",
        "কাচ নলে পানির কৈশিক উত্থান সহায়তা পায়:",
        ["Repulsion from glass only", "Adhesive forces and hydrogen bonding with glass", "Only gravity increasing upward", "Absence of cohesion"],
        ["শুধু কাচ থেকে বিকর্ষণ", "আসঞ্জন বল ও কাচের সাথে হাইড্রোজেন বন্ধন", "শুধু মাধ্যাকর্ষণ উপরের দিকে বাড়া", "সংহতির অনুপস্থিতি"],
        "B", "hard", "application",
        "Adhesion to polar glass plus cohesion in water drives capillary action.",
        "পোলার কাচে আসঞ্জন ও পানির সংহতি কৈশিক ক্রিয়া চালায়।",
    ),
    q(
        "Glycerol is viscous largely because of:",
        "গ্লিসারল সান্দ্র প্রধানত কারণ:",
        ["No polar groups", "Extensive intermolecular hydrogen bonding via three −OH groups", "Being a noble gas", "Only instantaneous dipoles"],
        ["কোনো পোলার গ্রুপ নেই", "তিন −OH গ্রুপের বিস্তৃত আন্তঃআণবিক হাইড্রোজেন বন্ধন", "নিষ্ক্রিয় গ্যাস হওয়া", "শুধু তাৎক্ষণিক দ্বিমেরু"],
        "B", "medium", "application",
        "Multiple −OH groups create a strong H-bonded network, raising viscosity.",
        "একাধিক −OH শক্তিশালী H-বন্ধন নেটওয়ার্ক গঠন করে সান্দ্রতা বাড়ায়।",
    ),
    q(
        "Which statement is correct?",
        "কোন বিবৃতি সঠিক?",
        ["Boiling breaks covalent bonds inside H2O molecules", "Boiling overcomes intermolecular forces between H2O molecules", "Melting ice creates new NaCl bonds", "Gases have the strongest intermolecular forces"],
        ["স্ফুটনে H2O অণুর ভিতরের সমযোজী বন্ধন ভাঙে", "স্ফুটনে H2O অণুর মধ্যেকার আন্তঃআণবিক বল অতিক্রম হয়", "বরফ গললে নতুন NaCl বন্ধন হয়", "গ্যাসে আন্তঃআণবিক বল সবচেয়ে শক্তিশালী"],
        "B", "easy", "conceptual",
        "Phase changes rearrange molecules; covalent O−H bonds remain intact.",
        "দশা পরিবর্তনে অণু পুনর্বিন্যস্ত হয়; সমযোজী O−H বন্ধন অটুট থাকে।",
    ),
    q(
        "Induced dipole forces are especially important for:",
        "প্ররোচিত দ্বিমেরু বল বিশেষ গুরুত্বপূর্ণ কোনটির জন্য?",
        ["Dissolving nonpolar gases like O2 in water to a small extent", "Forming diamond networks", "Ionic lattice Madelung energy only", "Nuclear binding"],
        ["পানিতে O2 এর মতো অপোলার গ্যাসের সামান্য দ্রবণীয়তা", "হীরার জালক গঠন", "শুধু আয়নিক জালকের Madelung শক্তি", "নিউক্লিয়ার বন্ধন"],
        "A", "hard", "conceptual",
        "Water’s dipole can induce a temporary dipole in O2, enabling slight solubility.",
        "পানির দ্বিমেরু O2 তে অস্থায়ী দ্বিমেরু প্ররোচিত করে সামান্য দ্রবণীয়তা দেয়।",
    ),
]

TOPICS_MAP = {
    "chem1_27_ch03_t01": T01,
    "chem1_27_ch03_t02": T02,
    "chem1_27_ch03_t03": T03,
    "chem1_27_ch03_t04": T04,
    "chem1_27_ch03_t05": T05,
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
        "chapter": "chem1_27_ch03",
        "title_en": "Periodic Properties and Chemical Bonding",
        "title_bn": "মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন",
        "source": SRC,
        "pdf_pages": [],
        "note": (
            "Import CSV chemistry_1_ch03.csv had headers only; authored 20 bilingual MCQs "
            "per topic aligned to NCTB chemistry_1st_paper_2027 ch03 "
            "(Periodic Properties and Chemical Bonding)."
        ),
        "counts": {**counts, "total": sum(counts.values())},
        "paths": paths,
        "pdf_mapping": {
            "chem1_27_ch03_t01": {
                "title": "Periodic table and electron configuration / পর্যায় সারণি ও ইলেকট্রন বিন্যাস",
                "themes": [
                    "modern periodic law; Moseley; groups periods blocks",
                    "Aufbau Pauli Hund; valence electrons; noble gases",
                    "Na Cr configs; quantum numbers; isoelectronic; halogens",
                ],
            },
            "chem1_27_ch03_t02": {
                "title": "Periodic trends / পর্যায়বৃত্ত ধর্মের পরিবর্তন",
                "themes": [
                    "atomic ionic radius; ionization energy; electron affinity",
                    "electronegativity; metallic character; Zeff",
                    "isoelectronic size; Be vs B IE; halogen oxidizing power",
                ],
            },
            "chem1_27_ch03_t03": {
                "title": "Ionic and covalent bonding / আয়নিক ও সমযোজী বন্ধন",
                "themes": [
                    "ionic vs covalent vs metallic; polarity; lattice energy",
                    "octet; coordinate bond; Lewis resonance; Fajans",
                    "Born–Haber; double triple bonds; conductivity of ionics",
                ],
            },
            "chem1_27_ch03_t04": {
                "title": "Molecular shape and hybridization / অণুর আকৃতি ও সংকরায়ন",
                "themes": [
                    "VSEPR shapes BeCl2 BF3 CH4 NH3 H2O CO2",
                    "sp sp2 sp3 sp3d sp3d2; bond angles; lone-pair effect",
                    "sigma pi bonds; PCl5 SF6 hybridization",
                ],
            },
            "chem1_27_ch03_t05": {
                "title": "Intermolecular forces / আন্তঃআণবিক বল",
                "themes": [
                    "London dipole–dipole H-bonding van der Waals",
                    "boiling points ice ethanol HF viscosity surface tension",
                    "ion–dipole capillary; phase change vs covalent bonds",
                ],
            },
        },
        "low_confidence": [
            "No usable OCR page set for Chemistry 1st paper Udvash PDF ch03; items are syllabus-aligned authored MCQs.",
            "Import CSV content/bank/import/chemistry_1_ch03.csv had headers only (no stems to reuse).",
            "Some advanced items (Fajans, Born–Haber, Cr configuration) follow common HSC board emphasis.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (chem1_27_ch03_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {tid: 20 for tid in TOPIC_IDS},
        },
        "chem1_ch03_completion": {
            "topics_expected": 5,
            "topics_at_20": 5,
            "note": "chem1_27_ch03_t01..t05 complete at 20/topic (chapter total 100).",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch03_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
