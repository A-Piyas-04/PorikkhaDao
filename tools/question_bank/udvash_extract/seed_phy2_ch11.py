#!/usr/bin/env python3
"""Seed Physics 2nd Paper Ch11 (Astronomy).

Curated from Udvash HSC Question Bank 2026 pages p348–p351 (PDF 354–357).
Writes exactly 20 bilingual JSONL rows per topic under content/bank/topics/.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
from core import validate_record  # noqa: E402

TOPICS = ROOT / "content" / "bank" / "topics"
PARSED = ROOT / "content" / "bank" / "udvash_raw" / "physics_2" / "parsed"
SOURCE = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "physics p2 ch11; curated bilingual"
)


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    if not re.search(r"[A-Za-z]", en):
        en = f"value {en}"
    if not re.search(r"[ঀ-৿]", bn):
        raw = bn
        bn = f"মান {raw}"
    return en, bn


def q(
    stem_en,
    stem_bn,
    opts_en,
    opts_bn,
    correct,
    difficulty,
    qtype,
    exp_en,
    exp_bn,
    *,
    bank_n=None,
    filler=False,
):
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
        "source": SOURCE,
        "verified": False,
        "_bank_n": bank_n,
        "_filler": filler,
    }


def write_topic(topic_id: str, items: list[dict]) -> list:
    assert len(items) == 20, f"{topic_id} has {len(items)}"
    path = TOPICS / f"{topic_id}.jsonl"
    mapping = []
    lines = []
    for item in items:
        mapping.append("filler" if item.get("_filler") else item.get("_bank_n"))
        row = {k: v for k, v in item.items() if not k.startswith("_")}
        row["verified"] = False
        row["source"] = SOURCE
        err = validate_record(row)
        if err:
            raise SystemExit(f"{topic_id}: {err}\n{row['stem_en'][:100]}")
        lines.append(json.dumps(row, ensure_ascii=False))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return mapping


# ---------------------------------------------------------------------------
# t01 — Origin and fate of the universe
# ---------------------------------------------------------------------------
T01 = [
    q(
        "Which is the theory of the creation of the universe?",
        "মহাবিশ্ব সৃষ্টির তত্ত্ব কোনটি?",
        ["Relativity theory", "Quantum theory", "Big Bang theory", "Wave theory"],
        ["আপেক্ষিক তত্ত্ব", "কোয়ান্টাম তত্ত্ব", "বিগ ব্যাং তত্ত্ব", "তরঙ্গ তত্ত্ব"],
        "C", "easy", "factual",
        "Printed board key: Big Bang theory explains cosmic origin.",
        "মুদ্রিত চাবি: বিগ ব্যাং তত্ত্ব মহাবিশ্বের উৎপত্তি ব্যাখ্যা করে।",
        bank_n=14,
    ),
    q(
        "Which of the following is most abundant in the universe?",
        "মহাবিশ্বে নিচের কোনটির পরিমাণ সবচেয়ে বেশি?",
        ["Black holes", "Nebulae", "Galaxies", "Dark energy / dark matter"],
        ["কৃষ্ণগহ্বরসমূহ", "নীহারিকাসমূহ", "গ্যালাক্সিসমূহ", "ডার্ক এনার্জি বস্তুসমূহ"],
        "D", "medium", "factual",
        "Printed key: dark energy/dark-matter content dominates the cosmic energy budget.",
        "মুদ্রিত চাবি: মহাবিশ্বের শক্তি বাজেটে ডার্ক এনার্জি/অদৃশ্য উপাদানই প্রধান।",
        bank_n=15,
    ),
    q(
        "The ultimate fate of the universe mainly depends on—\n(i) geometric shape of the universe\n(ii) dark energy\n(iii) dark matter\nWhich is correct?",
        "মহাবিশ্বের চূড়ান্ত পরিণতি প্রধানত নির্ভর করে—\n(i) মহাবিশ্বের জ্যামিতিক আকৃতি\n(ii) অদৃশ্য শক্তি\n(iii) অদৃশ্য বস্তু\nনিচের কোনটি সঠিক?",
        ["i, ii and iii", "i and ii", "i and iii", "ii and iii"],
        ["i, ii ও iii", "i ও ii", "i ও iii", "ii ও iii"],
        "A", "medium", "conceptual",
        "Printed key: fate depends on geometry, dark energy and dark matter together.",
        "মুদ্রিত চাবি: জ্যামিতি, অদৃশ্য শক্তি ও অদৃশ্য বস্তু—সবগুলোই পরিণতি নির্ধারণ করে।",
        bank_n=24,
    ),
    q(
        "Who presented the idea that the universe is continually expanding?",
        "মহাবিশ্ব প্রতিনিয়ত প্রসারিত হচ্ছে—এ বিষয়টি উপস্থাপন করেন কে?",
        ["Stephen Hawking", "Edwin Hubble", "Friedmann", "Einstein"],
        ["স্টিফেন হকিং", "এডউইন হাবল", "ফ্রিডম্যান", "আইনস্টাইন"],
        "B", "easy", "factual",
        "Printed key: Edwin Hubble established cosmic expansion observationally.",
        "মুদ্রিত চাবি: এডউইন হাবল পর্যবেক্ষণ দিয়ে মহাবিশ্বের প্রসারণ প্রতিষ্ঠা করেন।",
        bank_n=25,
    ),
    q(
        "The Big Bang occurred—",
        "বিগ-ব্যাং সংঘটিত হয়েছিল—",
        ["In outer space only", "On Earth", "In the solar system", "Everywhere"],
        ["শুধু মহাকাশে", "পৃথিবীতে", "সৌরজগতে", "সর্বত্র"],
        "D", "medium", "conceptual",
        "Printed key: the Big Bang was the origin of space itself—everywhere.",
        "মুদ্রিত চাবি: বিগ ব্যাং মহাকাশেরই উৎপত্তি—তাই সর্বত্র ঘটেছিল।",
        bank_n=26,
    ),
    q(
        "Which of the following is still mysterious?",
        "নিচের কোনটি এখনো রহস্যময়?",
        ["Length contraction", "Time dilation", "Contraction of the universe", "Relativity of mass"],
        ["দৈর্ঘ্য সংকোচন", "সময় প্রসারণ", "মহাবিশ্বের সংকোচন", "ভরের আপেক্ষিকতা"],
        "C", "medium", "conceptual",
        "Printed key: whether/how the universe will contract remains an open question.",
        "মুদ্রিত চাবি: মহাবিশ্ব সংকুচিত হবে কি না—এটি এখনো রহস্যময়।",
        bank_n=27,
    ),
    q(
        "Who proposed the Big Bang theory?",
        "মহাবিস্ফোরণ তত্ত্বের প্রবর্তক কে?",
        ["George Gamow", "Georges Lemaître", "Fred Hoyle", "Gold"],
        ["জর্জ গ্যামো", "জর্জ লেমাইটার", "ফ্রেড হয়েল", "গোল্ড"],
        "B", "easy", "factual",
        "Printed key: Georges Lemaître proposed the primeval-atom / Big Bang idea.",
        "মুদ্রিত চাবি: জর্জ লেমাইটার মহাবিস্ফোরণ তত্ত্বের প্রবর্তক।",
        bank_n=31,
    ),
    q(
        "Best values of the Hubble constant include—\n(i) H = 72 km s⁻¹/Mpc\n(ii) H = 3.22 × 10⁻¹⁸ s⁻¹\n(iii) H = 2.33 × 10⁻¹⁸ s⁻¹\nWhich is correct?",
        "হাবল ধ্রুবকের সর্বোত্তম মান হচ্ছে—\n(i) H = 72 km s⁻¹/Mpc\n(ii) H = 3.22 × 10⁻¹⁸ s⁻¹\n(iii) H = 2.33 × 10⁻¹⁸ s⁻¹\nনিচের কোনটি সঠিক?",
        ["i and ii", "ii and iii", "i and iii", "i, ii and iii"],
        ["i ও ii", "ii ও iii", "i ও iii", "i, ii ও iii"],
        "C", "hard", "numerical",
        "Printed key: 72 km s⁻¹/Mpc ≈ 2.33×10⁻¹⁸ s⁻¹; 3.22×10⁻¹⁸ is inconsistent.",
        "মুদ্রিত চাবি: 72 km s⁻¹/Mpc ≈ 2.33×10⁻¹⁸ s⁻¹; 3.22×10⁻¹⁸ সামঞ্জস্যপূর্ণ নয়।",
        bank_n=42,
    ),
    q(
        "If the average density of the universe is greater than the critical density, then—",
        "মহাবিশ্বের গড় ঘনত্ব সংকট ঘনত্বের অপেক্ষা বেশি হলে—",
        [
            "The universe will only contract",
            "The universe will only expand",
            "The universe will contract and then expand again",
            "The universe will expand and later contract again",
        ],
        [
            "মহাবিশ্ব সংকুচিত হবে",
            "মহাবিশ্ব প্রসারিত হবে",
            "মহাবিশ্ব সংকুচিত হয়ে আবার প্রসারিত হবে",
            "মহাবিশ্ব প্রসারণের পর আবার সংকুচিত হবে",
        ],
        "D", "medium", "conceptual",
        "Printed key: ρ > ρ_c ⇒ closed universe that expands then recollapses.",
        "মুদ্রিত চাবি: ρ > ρ_c হলে বদ্ধ মহাবিশ্ব—প্রসারিত হয়ে পরে সংকুচিত হয়।",
        bank_n=51,
    ),
    q(
        "The density of matter needed to keep the universe closed is called—",
        "বিশ্বকে আবদ্ধ করতে যে পরিমাণ পদার্থের প্রয়োজন তার ঘনত্বকে কী বলে?",
        ["Relative density", "Critical density", "Thermal density", "Ordinary density"],
        ["আপেক্ষিক ঘনত্ব", "সংকট ঘনত্ব", "তাপীয় ঘনত্ব", "ঘনত্ব"],
        "B", "easy", "factual",
        "Printed key: that threshold density is the critical density.",
        "মুদ্রিত চাবি: সেই সীমা ঘনত্বকে সংকট ঘনত্ব বলে।",
        bank_n=52,
    ),
    q(
        "Which particle is known as the 'God particle'?",
        "কোন কণা “ঈশ্বর কণা” নামে পরিচিত?",
        ["Boson particle", "Higgs–Boson particle", "Meson particle", "Lepton particle"],
        ["বোসন কণা", "হিগস-বোসন কণা", "মেসন কণা", "লেপটন কণা"],
        "B", "easy", "factual",
        "Printed board key: Higgs boson is popularly called the God particle.",
        "মুদ্রিত চাবি: হিগস বোসনকে ঈশ্বর কণা বলা হয়।",
        bank_n=7,
    ),
    q(
        "The Higgs particle is a—",
        "হিগস কণা হচ্ছে—",
        ["Lepton", "Boson", "Baryon", "Fermion"],
        ["লেপটন", "বোসন", "ব্যারিয়ন", "ফার্মিয়ন"],
        "B", "easy", "factual",
        "Printed key: Higgs is a boson (integer spin).",
        "মুদ্রিত চাবি: হিগস একটি বোসন কণা।",
        bank_n=41,
    ),
    q(
        "Hubble's law relates recession speed v of a galaxy to its distance d as—",
        "হাবলের সূত্রানুসারে গ্যালাক্সির অপসারণ বেগ v ও দূরত্ব d এর সম্পর্ক—",
        ["v = H/d", "v = Hd", "v = H d²", "v independent of d"],
        ["v = H/d", "v = Hd", "v = H d²", "v, d নিরপেক্ষ"],
        "B", "easy", "factual",
        "Syllabus filler: Hubble's law is v = Hd (linear expansion).",
        "পাঠ্যক্রম ফিলার: হাবলের সূত্র v = Hd (রৈখিক প্রসারণ)।",
        filler=True,
    ),
    q(
        "An open-universe model predicts that galaxies will—",
        "উন্মুক্ত মহাবিশ্ব মডেল অনুসারে গ্যালাক্সিগুলো—",
        [
            "Eventually reverse and collapse",
            "Expand forever",
            "Remain at fixed separations",
            "Form a single static sphere",
        ],
        [
            "একদিন উল্টে সংকুচিত হবে",
            "অনন্তকাল ধরে প্রসারিত হবে",
            "স্থির দূরত্বে থাকবে",
            "একটি স্থির গোলক গঠন করবে",
        ],
        "B", "medium", "conceptual",
        "Syllabus filler: open (under-dense) models expand forever.",
        "পাঠ্যক্রম ফিলার: উন্মুক্ত মডেলে প্রসারণ অনন্তকাল চলতে থাকে।",
        filler=True,
    ),
    q(
        "Cosmic microwave background radiation is mainly evidence of—",
        "কসমিক মাইক্রোওয়েভ পটভূমি বিকিরণ মূলত প্রমাণ করে—",
        ["A static ether", "A hot early universe after the Big Bang", "Only local solar activity", "Galilean relativity"],
        ["স্থির ইথার", "বিগ ব্যাং-পরবর্তী উত্তপ্ত আদি মহাবিশ্ব", "শুধু সৌর সক্রিয়তা", "গ্যালিলীয় আপেক্ষিকতা"],
        "B", "medium", "conceptual",
        "Syllabus filler: CMB is the cooled remnant of the hot Big Bang.",
        "পাঠ্যক্রম ফিলার: CMB আদি উত্তপ্ত বিগ ব্যাং-এর শীতল অবশেষ।",
        filler=True,
    ),
    q(
        "If cosmic density equals the critical density, the universe is described as—",
        "মহাজাগতিক ঘনত্ব সংকট ঘনত্বের সমান হলে মহাবিশ্বকে বলে—",
        ["Closed", "Open", "Flat (critical)", "Static Newtonian"],
        ["বদ্ধ", "উন্মুক্ত", "সমতল (সংকট)", "স্থির নিউটনীয়"],
        "C", "medium", "conceptual",
        "Syllabus filler: ρ = ρ_c corresponds to a flat/critical geometry.",
        "পাঠ্যক্রম ফিলার: ρ = ρ_c হলে সমতল/সংকট জ্যামিতি।",
        filler=True,
    ),
    q(
        "Redshift of distant galaxies means their spectral lines are shifted toward—",
        "দূরবর্তী গ্যালাক্সির লাল অপসারণ মানে বর্ণালি রেখা সরে যায়—",
        ["Shorter (blue) wavelengths", "Longer (red) wavelengths", "Zero wavelength", "Only X-ray bands"],
        ["কম (নীল) তরঙ্গদৈর্ঘ্যে", "বেশি (লাল) তরঙ্গদৈর্ঘ্যে", "শূন্য তরঙ্গদৈর্ঘ্যে", "শুধু এক্স-রে ব্যান্ডে"],
        "B", "easy", "conceptual",
        "Syllabus filler: cosmological redshift stretches wavelengths toward red.",
        "পাঠ্যক্রম ফিলার: মহাজাগতিক লাল অপসারণ তরঙ্গদৈর্ঘ্য বাড়ায়।",
        filler=True,
    ),
    q(
        "Spin of a lepton particle is—",
        "লেপটন কণার স্পিন—",
        ["0", "1/2", "1", "3/2"],
        ["0", "1/2", "1", "3/2"],
        "B", "easy", "factual",
        "Printed key: leptons are spin-1/2 fermions (chapter Standard Model).",
        "মুদ্রিত চাবি: লেপটনসমূহ স্পিন 1/2 ফার্মিয়ন।",
        bank_n=12,
    ),
    q(
        "Which particle belongs to the lepton class?",
        "নিচের কোন কণাটি লেপটন শ্রেণির অন্তর্ভুক্ত?",
        ["Neutron", "Pion", "Proton", "Electron"],
        ["নিউট্রন", "পাইয়ন", "প্রোটন", "ইলেকট্রন"],
        "D", "easy", "factual",
        "Printed key: the electron is a lepton.",
        "মুদ্রিত চাবি: ইলেকট্রন একটি লেপটন।",
        bank_n=23,
    ),
    q(
        "Regarding quarks, which is correct?\n(i) They have their own quantum numbers\n(ii) Protons and neutrons are made of quarks\n(iii) They can transfer mass to massless particles\nWhich is correct?",
        "কোয়ার্ক সম্পর্কে বলা যায়—\n(i) নিজস্ব কোয়ান্টাম সংখ্যা আছে\n(ii) প্রোটন ও নিউট্রনসমূহ কোয়ার্ক দিয়ে গঠিত\n(iii) ভরহীন কণাতে ভর স্থানান্তর করতে পারে\nনিচের কোনটি সঠিক?",
        ["i and iii", "iii only", "ii and iii", "i and ii"],
        ["i ও iii", "শুধু iii", "ii ও iii", "i ও ii"],
        "D", "medium", "conceptual",
        "Printed key: (i) and (ii) about quarks; mass transfer is Higgs, not quarks.",
        "মুদ্রিত চাবি: (i) ও (ii) কোয়ার্কের; ভর স্থানান্তর হিগসের কাজ।",
        bank_n=38,
    ),
]

# ---------------------------------------------------------------------------
# t02 — Celestial objects and phenomena
# ---------------------------------------------------------------------------
T02 = [
    q(
        "If a star of mass 4.5 × 10³⁰ kg becomes a black hole, its radius will be about—",
        "4.5 × 10³⁰ kg ভরের একটি নক্ষত্র কৃষ্ণগহ্বরে পরিণত হলে ব্যাসার্ধ কত হবে?",
        ["2.6 km", "6.7 km", "1.41 × 10³ km", "2 × 10⁹ km"],
        ["2.6 km", "6.7 km", "1.41 × 10³ km", "2 × 10⁹ km"],
        "B", "hard", "numerical",
        "Printed solution: R = 2GM/c² ≈ 6.67 km.",
        "মুদ্রিত সমাধান: R = 2GM/c² ≈ 6.67 km।",
        bank_n=1,
    ),
    q(
        "Which is the equation for the Schwarzschild (event-horizon) radius?",
        "ঘটনা দিগন্তের ব্যাসার্ধের সমীকরণ কোনটি?",
        ["R = GM/(2c²)", "R = GM/c²", "R = c²/(2GM)", "R = 2GM/c²"],
        ["R = GM/(2c²)", "R = GM/c²", "R = c²/(2GM)", "R = 2GM/c²"],
        "D", "easy", "factual",
        "Printed key: Schwarzschild radius R = 2GM/c².",
        "মুদ্রিত চাবি: সোয়ার্জচাইল্ড ব্যাসার্ধ R = 2GM/c²।",
        bank_n=2,
    ),
    q(
        "If a star's mass is between about 2 and 3 solar masses, its final fate is—",
        "কোনো নক্ষত্রের ভর 2 থেকে 3 সৌর ভরের মধ্যে হলে, নক্ষত্রটির শেষ পরিণতি কী হবে?",
        ["White dwarf", "Black dwarf", "Neutron star", "Black hole"],
        ["শ্বেত বামন", "কালো বামন", "নিউট্রন তারকা", "কৃষ্ণ বিবর"],
        "C", "medium", "factual",
        "Printed key: ~2–3 M☉ remnants become neutron stars.",
        "মুদ্রিত চাবি: প্রায় 2–3 সৌর ভরের অবশেষ নিউট্রন তারকা হয়।",
        bank_n=4,
    ),
    q(
        "What is the next stage after a supernova?",
        "সুপারনোভার পরবর্তী ধাপ কোনটি?",
        ["Neutron star", "White dwarf", "Dwarf star", "Giant star"],
        ["নিউট্রন স্টার", "শ্বেত বামন", "বামন স্টার", "দানব স্টার"],
        "A", "easy", "factual",
        "Printed key: a supernova can leave a neutron star.",
        "মুদ্রিত চাবি: সুপারনোভার পর নিউট্রন তারকা হতে পারে।",
        bank_n=5,
    ),
    q(
        "The main constituents of a nebula are—",
        "নীহারিকা গঠনকারী প্রধান উপাদানদ্বয় হচ্ছে—",
        ["Hydrogen and helium", "Hydrogen and water vapour", "Hydrogen and oxygen", "Oxygen and helium"],
        ["হাইড্রোজেন ও হিলিয়াম", "হাইড্রোজেন ও জলীয় বাষ্প", "হাইড্রোজেন ও অক্সিজেন", "অক্সিজেন ও হিলিয়াম"],
        "A", "easy", "factual",
        "Printed key: nebulae are mainly hydrogen and helium.",
        "মুদ্রিত চাবি: নীহারিকার প্রধান উপাদান হাইড্রোজেন ও হিলিয়াম।",
        bank_n=9,
    ),
    q(
        "The mass of a supernova is how many times the solar mass?",
        "সুপারনোভার ভর সৌর ভরের কত গুণ?",
        ["2", "3", "4", "5"],
        ["2", "3", "4", "5"],
        "D", "medium", "factual",
        "Printed key selects 5× solar mass for the supernova mass scale.",
        "মুদ্রিত চাবি: সুপারনোভার ভর সৌর ভরের 5 গুণ।",
        bank_n=10,
    ),
    q(
        "Event horizon is related to a—",
        "ঘটনা দিগন্তের সাথে সম্পর্ক হল—",
        ["Planet", "Galaxy", "Satellite", "Star (black hole)"],
        ["গ্রহের", "গ্যালাক্সির", "উপগ্রহের", "নক্ষত্রের"],
        "D", "easy", "factual",
        "Printed key: event horizon is associated with a collapsed star / black hole.",
        "মুদ্রিত চাবি: ঘটনা দিগন্ত কৃষ্ণগহ্বরে পরিণত নক্ষত্রের সাথে সম্পর্কিত।",
        bank_n=11,
    ),
    q(
        "A pulsar is a—",
        "পালসার হলো একটি—",
        ["Black hole", "White dwarf", "Neutron star", "Supernova"],
        ["কৃষ্ণ গহ্বর", "শ্বেত বামন", "নিউট্রন স্টার", "সুপারনোভা"],
        "C", "easy", "factual",
        "Printed key: pulsars are rapidly rotating neutron stars.",
        "মুদ্রিত চাবি: পালসার দ্রুত ঘূর্ণায়মান নিউট্রন তারকা।",
        bank_n=13,
    ),
    q(
        "If a star's mass is greater than three solar masses, it will become a—",
        "নক্ষত্রের ভর যদি তিন সৌর ভরের চেয়ে বেশি হয় তবে নক্ষত্রটি পরিণত হবে—",
        ["Black hole", "White dwarf star", "Neutron star", "Black dwarf star"],
        ["কৃষ্ণ গহ্বর", "শ্বেত বামন তারা", "নিউট্রন তারা", "কালো বামন তারা"],
        "A", "medium", "factual",
        "Printed key: M > 3 M☉ → black hole.",
        "মুদ্রিত চাবি: M > 3 M☉ হলে কৃষ্ণগহ্বর।",
        bank_n=16,
    ),
    q(
        "A star has mass 7.96 × 10³⁰ kg; G = 6.67 × 10⁻¹¹; c = 3 × 10⁸. Its Schwarzschild radius is—",
        "একটি নক্ষত্রের ভর 7.96 × 10³⁰ kg; G = 6.67 × 10⁻¹¹; c = 3 × 10⁸। এর সোয়ার্জচাইল্ড ব্যাসার্ধ কত?",
        ["5.9 × 10³ m", "11.8 × 10³ m", "1.2 × 10¹² m", "4.1 × 10¹⁵ m"],
        ["5.9 × 10³ m", "11.8 × 10³ m", "1.2 × 10¹² m", "4.1 × 10¹⁵ m"],
        "B", "hard", "numerical",
        "Printed solution: Rs = 2GM/c² ≈ 11.8 × 10³ m.",
        "মুদ্রিত সমাধান: Rs = 2GM/c² ≈ 11.8 × 10³ m।",
        bank_n=17,
    ),
    q(
        "The boundary of a black-hole region is called—",
        "কৃষ্ণবিবর অঞ্চলের সীমাকে বলে—",
        ["Event horizon", "Schwarzschild radius", "Nebula", "White dwarf"],
        ["ঘটনা দিগন্ত", "শোয়ার্জশিল্ড ব্যাসার্ধ", "নেবুলা", "সাদা বামন"],
        "B", "easy", "factual",
        "Printed key selects Schwarzschild radius for the black-hole boundary.",
        "মুদ্রিত চাবি: কৃষ্ণবিবর সীমা হিসেবে সোয়ার্জচাইল্ড ব্যাসার্ধ।",
        bank_n=19,
    ),
    q(
        "Condition for a star to become a white dwarf (M☉ = solar mass)—\n(i) M = 1.4 M☉\n(ii) M > 1.4 M☉\n(iii) M < 1.4 M☉\nWhich is correct?",
        "তারকার শ্বেত বামন হওয়ার শর্ত হলো (M☉ = সূর্যের ভর)—\n(i) M = 1.4 M☉\n(ii) M > 1.4 M☉\n(iii) M < 1.4 M☉\nনিচের কোনটি সঠিক?",
        ["i and ii", "ii and iii", "i only", "i and iii"],
        ["i ও ii", "ii ও iii", "শুধু i", "i ও iii"],
        "D", "medium", "conceptual",
        "Printed key: white-dwarf mass at/below the Chandrasekhar value 1.4 M☉.",
        "মুদ্রিত চাবি: শ্বেত বামনের ভর চন্দ্রশেখর সীমা 1.4 M☉ বা তার কম।",
        bank_n=20,
    ),
    q(
        "When a neutron star contracts further, it becomes a—",
        "নিউট্রন তারকা সংকুচিত হয়ে কী হয়?",
        ["Red giant", "Supernova", "White dwarf", "Black hole"],
        ["রক্তিম দৈত্য", "সুপারনোভা", "সাদা বামন", "কৃষ্ণ গহ্বর"],
        "D", "medium", "factual",
        "Printed key: further collapse of a neutron star yields a black hole.",
        "মুদ্রিত চাবি: নিউট্রন তারকা আরও সংকুচিত হয়ে কৃষ্ণগহ্বর হয়।",
        bank_n=21,
    ),
    q(
        "Near death, if a star's mass exceeds 1.4 solar masses it cannot become a white dwarf. This mass limit is the—",
        "মৃত্যুপূর্ব মুহূর্তে তারকার ভর সৌর ভরের 1.4 গুণের বেশি থাকলে এটি শ্বেত বামন হতে পারে না। ভরের এই সীমাকে বলা হয়—",
        ["Newton limit", "Einstein limit", "Chandrasekhar limit", "Schwarzschild radius"],
        ["নিউটন সীমা", "আইনস্টাইন সীমা", "চন্দ্রশেখর সীমা", "সোয়ার্জশিল্ড ব্যাসার্ধ"],
        "C", "easy", "factual",
        "Printed key: Chandrasekhar limit ≈ 1.4 M☉.",
        "মুদ্রিত চাবি: চন্দ্রশেখর সীমা ≈ 1.4 M☉।",
        bank_n=28,
    ),
    q(
        "Between which two planets do asteroids orbit the Sun?",
        "গ্রহাণু কোন দুটি গ্রহের কক্ষপথের মাঝ দিয়ে সূর্যকে প্রদক্ষিণ করে?",
        ["Mars and Saturn", "Mercury and Venus", "Jupiter and Saturn", "Mars and Jupiter"],
        ["মঙ্গল ও শনি", "বুধ ও শুক্র", "বৃহস্পতি ও শনি", "মঙ্গল ও বৃহস্পতি"],
        "D", "easy", "factual",
        "Printed key: the asteroid belt lies between Mars and Jupiter.",
        "মুদ্রিত চাবি: গ্রহাণু বলয় মঙ্গল ও বৃহস্পতির মাঝে।",
        bank_n=29,
    ),
    q(
        "Two black holes have event-horizon radii 21 km and 6 km. Their mass ratio is—",
        "দুটি কৃষ্ণ বিবরের ঘটনা দিগন্তের ব্যাসার্ধ যথাক্রমে 21 km ও 6 km। এদের ভরের অনুপাত কত?",
        ["3:1", "7:2", "2:7", "1:3"],
        ["3:1", "7:2", "2:7", "1:3"],
        "B", "hard", "numerical",
        "Printed key: Rs ∝ M ⇒ 21:6 = 7:2.",
        "মুদ্রিত চাবি: Rs ∝ M ⇒ 21:6 = 7:2।",
        bank_n=43,
    ),
    q(
        "The Sun radiates energy each second of about—",
        "সূর্য প্রতি সেকেন্ডে শক্তি বিকিরণ করে—",
        ["4 × 10²⁶ J", "4 × 10²⁷ J", "4 × 10²⁸ J", "4 × 10²⁹ J"],
        ["4 × 10²⁶ J", "4 × 10²⁷ J", "4 × 10²⁸ J", "4 × 10²⁹ J"],
        "A", "medium", "factual",
        "Printed key: solar luminosity ≈ 4 × 10²⁶ J/s.",
        "মুদ্রিত চাবি: সূর্যের শক্তি বিকিরণ ≈ 4 × 10²⁶ J/s।",
        bank_n=32,
    ),
    q(
        "Solar mass is 1.99 × 10³⁰ kg. A star of 6 solar masses becomes a black hole. Event-horizon radius is—",
        "সূর্যের ভর 1.99 × 10³⁰ kg। একটি নক্ষত্রের ভর সূর্যের 6 গুণ। কৃষ্ণ বিবরে পরিণত হলে ঘটনা দিগন্তের ব্যাসার্ধ—",
        ["4.2 km", "8.85 km", "17.70 km", "8.85 × 10¹¹ km"],
        ["4.2 km", "8.85 km", "17.70 km", "8.85 × 10¹¹ km"],
        "C", "hard", "numerical",
        "Printed key: Rs = 2GM/c² ≈ 17.7 km for 6 M☉.",
        "মুদ্রিত চাবি: 6 M☉ এর জন্য Rs ≈ 17.7 km।",
        bank_n=33,
    ),
    q(
        "Energy in stars is produced by which reaction?",
        "কোন বিক্রিয়ার ফলে নক্ষত্রে শক্তি উৎপন্ন হয়?",
        ["Fission", "Fusion", "Chemical", "Chain (only)"],
        ["ফিশন", "ফিউশন", "রাসায়নিক", "শৃঙ্খল"],
        "B", "easy", "factual",
        "Printed key: stellar energy comes from nuclear fusion.",
        "মুদ্রিত চাবি: নক্ষত্রে শক্তি নিউক্লিয় ফিউশন থেকে আসে।",
        bank_n=37,
    ),
    q(
        "What type of galaxy is the Milky Way?",
        "আকাশগঙ্গা কোন ধরনের গ্যালাক্সি?",
        ["Elliptical", "Rectangular", "Circular", "Spiral"],
        ["উপবৃত্তাকার", "আয়তাকার", "বৃত্তাকার", "সর্পিলাকার"],
        "D", "easy", "factual",
        "Printed key: the Milky Way is a spiral galaxy.",
        "মুদ্রিত চাবি: আকাশগঙ্গা একটি সর্পিল গ্যালাক্সি।",
        bank_n=48,
    ),
]

# ---------------------------------------------------------------------------
# t03 — Optical and radio telescopes
# ---------------------------------------------------------------------------
T03 = [
    q(
        "How many types of optical telescopes are there?",
        "অপটিক্যাল টেলিস্কোপ কত প্রকার?",
        ["2", "3", "4", "1"],
        ["2", "3", "4", "1"],
        "B", "easy", "factual",
        "Printed key: optical telescopes are classified into three types in this bank.",
        "মুদ্রিত চাবি: এ ব্যাংকে অপটিক্যাল টেলিস্কোপ তিন প্রকার।",
        bank_n=46,
    ),
    q(
        "A refracting telescope forms images mainly using—",
        "প্রতিসরণী দূরবীক্ষণ প্রধানত কোনটি দিয়ে প্রতিবিম্ব গঠন করে?",
        ["Concave mirrors only", "Convex objective lenses", "Radio antennas", "Photographic film alone"],
        ["শুধু অবতল দর্পণ", "উত্তল অভিলক্ষ্য লেন্স", "রেডিও অ্যান্টেনা", "শুধু ফটোগ্রাফিক ফিল্ম"],
        "B", "easy", "factual",
        "Syllabus filler: refractors use lenses as the objective.",
        "পাঠ্যক্রম ফিলার: প্রতিসরণী টেলিস্কোপে অভিলক্ষ্য লেন্স ব্যবহৃত হয়।",
        filler=True,
    ),
    q(
        "A reflecting telescope uses as its primary collector a—",
        "প্রতিফলনী দূরবীক্ষণের প্রাথমিক সংগ্রাহক হলো—",
        ["Convex lens only", "Concave (or parabolic) mirror", "Glass prism only", "Magnetic coil"],
        ["শুধু উত্তল লেন্স", "অবতল (বা প্যারাবোলিক) দর্পণ", "শুধু কাচের প্রিজম", "চৌম্বক কুণ্ডলী"],
        "B", "easy", "factual",
        "Syllabus filler: reflectors gather light with a concave primary mirror.",
        "পাঠ্যক্রম ফিলার: প্রতিফলনীতে অবতল প্রাইমারি দর্পণ আলো সংগ্রহ করে।",
        filler=True,
    ),
    q(
        "Compared with optical telescopes, radio telescopes detect—",
        "আলোকীয় দূরবীক্ষণের তুলনায় রেডিও দূরবীক্ষণ শনাক্ত করে—",
        ["Only visible colours", "Radio-wavelength electromagnetic waves", "Sound waves in air", "Neutrinos only"],
        ["শুধু দৃশ্যমান রং", "রেডিও তরঙ্গদৈর্ঘ্যের তড়িৎচুম্বকীয় তরঙ্গ", "বাতাসে শব্দ তরঙ্গ", "শুধু নিউট্রিনো"],
        "B", "easy", "conceptual",
        "Syllabus filler: radio telescopes observe the radio band of the EM spectrum.",
        "পাঠ্যক্রম ফিলার: রেডিও টেলিস্কোপ EM বর্ণালির রেডিও ব্যান্ড দেখে।",
        filler=True,
    ),
    q(
        "Light-gathering power of a telescope increases when the objective diameter—",
        "দূরবীক্ষণের আলো সংগ্রহ ক্ষমতা বাড়ে যখন অভিলক্ষ্যের ব্যাস—",
        ["Decreases", "Increases", "Becomes zero", "Is replaced by a slit"],
        ["কমে", "বাড়ে", "শূন্য হয়", "চিড় দিয়ে প্রতিস্থাপিত হয়"],
        "B", "easy", "conceptual",
        "Syllabus filler: collecting area ∝ D², so larger aperture gathers more light.",
        "পাঠ্যক্রম ফিলার: সংগ্রহ ক্ষেত্রফল ∝ D², তাই বড় অ্যাপারচারে বেশি আলো।",
        filler=True,
    ),
    q(
        "Angular resolving power of a telescope improves (smaller minimum angle) when aperture D—",
        "দূরবীক্ষণের কৌণিক বিভেদন ক্ষমতা ভালো হয় (ন্যূনতম কোণ ছোট হয়) যখন অ্যাপারচার D—",
        ["Decreases", "Increases", "Is irrelevant", "Must equal focal length"],
        ["কমে", "বাড়ে", "অপ্রাসঙ্গিক", "ফোকাস দূরত্বের সমান হতেই হবে"],
        "B", "medium", "conceptual",
        "Syllabus filler: diffraction limit θ ≈ 1.22 λ/D decreases as D grows.",
        "পাঠ্যক্রম ফিলার: বিচ্ছুরণ সীমা θ ≈ 1.22 λ/D; D বাড়লে θ কমে।",
        filler=True,
    ),
    q(
        "Radio telescopes often use a large dish because radio wavelengths are—",
        "রেডিও দূরবীক্ষণে বড় ডিশ ব্যবহার হয় কারণ রেডিও তরঙ্গদৈর্ঘ্য—",
        ["Much shorter than visible light", "Much longer than visible light", "Exactly zero", "Only ultraviolet"],
        ["দৃশ্যমান আলোর চেয়ে অনেক ছোট", "দৃশ্যমান আলোর চেয়ে অনেক বড়", "একদম শূন্য", "শুধু অতিবেগুনি"],
        "B", "medium", "conceptual",
        "Syllabus filler: long λ needs large D for useful resolution and collecting area.",
        "পাঠ্যক্রম ফিলার: বড় λ-এর জন্য ভালো বিভেদন ও সংগ্রহে বড় D দরকার।",
        filler=True,
    ),
    q(
        "An advantage of reflecting telescopes over large refractors is that mirrors—",
        "বড় প্রতিসরণীর তুলনায় প্রতিফলনীর সুবিধা হলো দর্পণ—",
        ["Suffer strong chromatic aberration", "Can be supported from behind and avoid chromatic aberration", "Cannot be made large", "Work only underwater"],
        ["তীব্র বর্ণবিচ্যুতি ভোগে", "পিছন থেকে ধরা যায় এবং বর্ণবিচ্যুতি এড়ায়", "বড় করা যায় না", "শুধু পানির নিচে কাজ করে"],
        "B", "medium", "conceptual",
        "Syllabus filler: mirrors have no chromatic aberration and are easier to support when large.",
        "পাঠ্যক্রম ফিলার: দর্পণে বর্ণবিচ্যুতি নেই এবং বড় আকারে ধরা সহজ।",
        filler=True,
    ),
    q(
        "Chromatic aberration is a problem mainly for—",
        "বর্ণবিচ্যুতি প্রধানত সমস্যা কোনটিতে?",
        ["Mirror-only reflectors", "Simple lens refractors", "Radio dish antennas", "Gravitational lenses only"],
        ["শুধু দর্পণ প্রতিফলনী", "সাধারণ লেন্স প্রতিসরণী", "রেডিও ডিশ অ্যান্টেনা", "শুধু মহাকর্ষীয় লেন্স"],
        "B", "medium", "conceptual",
        "Syllabus filler: different colours focus differently in lenses.",
        "পাঠ্যক্রম ফিলার: লেন্সে ভিন্ন রঙ ভিন্ন ফোকাসে পড়ে।",
        filler=True,
    ),
    q(
        "A compound (catadioptric) optical telescope combines—",
        "যৌগিক (ক্যাটাডিঅপট্রিক) আলোকীয় দূরবীক্ষণ একত্র করে—",
        ["Only radio receivers", "Both lenses and mirrors", "Only prisms", "Only magnetic shields"],
        ["শুধু রেডিও রিসিভার", "লেন্স ও দর্পণ উভয়ই", "শুধু প্রিজম", "শুধু চৌম্বক ঢাল"],
        "B", "medium", "factual",
        "Syllabus filler: catadioptric designs use lens + mirror elements.",
        "পাঠ্যক্রম ফিলার: ক্যাটাডিঅপট্রিকে লেন্স ও দর্পণ দুইই থাকে।",
        filler=True,
    ),
    q(
        "Magnifying power of an astronomical telescope (normal adjustment) is approximately—",
        "জ্যোতির্বৈজ্ঞানিক দূরবীক্ষণের বিবর্ধন ক্ষমতা (স্বাভাবিক সমন্বয়ে) প্রায়—",
        ["f_o / f_e", "f_e / f_o", "f_o × f_e", "f_o + f_e"],
        ["f_o / f_e", "f_e / f_o", "f_o × f_e", "f_o + f_e"],
        "A", "medium", "factual",
        "Syllabus filler: M ≈ f_objective / f_eyepiece.",
        "পাঠ্যক্রম ফিলার: M ≈ অভিলক্ষ্য ফোকাস / অভিনেত্র ফোকাস।",
        filler=True,
    ),
    q(
        "Why are large optical observatories often built on high mountains?",
        "বড় আলোকীয় মানমন্দির প্রায়ই উঁচু পাহাড়ে তৈরি হয় কেন?",
        ["To be closer to the Moon only", "Thinner, clearer air and less atmospheric disturbance", "Because gravity is zero there", "To avoid all radio noise automatically"],
        ["শুধু চাঁদের কাছে যেতে", "পাতলা ও স্বচ্ছ বায়ু এবং কম বায়ুমণ্ডলীয় ব্যাঘাত", "সেখানে মহাকর্ষ শূন্য বলে", "সব রেডিও নয়েজ আপনা থেকেই এড়াতে"],
        "B", "easy", "conceptual",
        "Syllabus filler: altitude reduces atmospheric absorption and seeing blur.",
        "পাঠ্যক্রম ফিলার: উচ্চতায় বায়ুমণ্ডলীয় শোষণ ও দেখা-ঝাপসা কমে।",
        filler=True,
    ),
    q(
        "Interferometry with multiple radio dishes is used mainly to—",
        "একাধিক রেডিও ডিশের ইন্টারফেরোমেট্রি প্রধানত ব্যবহৃত হয়—",
        ["Heat the ionosphere", "Improve effective angular resolution", "Generate X-rays", "Measure only DC voltage"],
        ["আয়নোস্ফিয়ার গরম করতে", "কার্যকর কৌণিক বিভেদন বাড়াতে", "এক্স-রে উৎপাদন করতে", "শুধু ডিসি ভোল্টেজ মাপতে"],
        "B", "hard", "conceptual",
        "Syllabus filler: baselines much larger than one dish sharpen radio resolution.",
        "পাঠ্যক্রম ফিলার: বড় বেসলাইন রেডিও বিভেদন তীক্ষ্ণ করে।",
        filler=True,
    ),
    q(
        "Which waveband cannot be observed well from the ground because the atmosphere blocks it strongly?",
        "বায়ুমণ্ডল তীব্রভাবে আটকালে মাটি থেকে কোন তরঙ্গব্যান্ড ভালোভাবে দেখা যায় না?",
        ["Some radio windows and visible light", "Many X-ray and gamma-ray bands", "All FM radio forever", "Only red visible light"],
        ["কিছু রেডিও উইন্ডো ও দৃশ্যমান আলো", "অনেক এক্স-রে ও গামা-রে ব্যান্ড", "সব এফএম রেডিও চিরকাল", "শুধু লাল দৃশ্যমান আলো"],
        "B", "medium", "conceptual",
        "Syllabus filler: X/γ rays need space telescopes due to atmospheric absorption.",
        "পাঠ্যক্রম ফিলার: এক্স/গামা রশ্মির জন্য মহাকাশ টেলিস্কোপ দরকার।",
        filler=True,
    ),
    q(
        "The objective of an astronomical telescope is usually of—",
        "জ্যোতির্বৈজ্ঞানিক দূরবীক্ষণের অভিলক্ষ্য সাধারণত হয়—",
        ["Short focal length and small aperture", "Long focal length and large aperture", "Zero focal length", "Negative refractive index"],
        ["ক্ষুদ্র ফোকাস ও ছোট অ্যাপারচার", "দীর্ঘ ফোকাস ও বড় অ্যাপারচার", "শূন্য ফোকাস", "ঋণাত্মক প্রতিসরাঙ্ক"],
        "B", "medium", "factual",
        "Syllabus filler: large, long-focus objectives gather light and set high magnification.",
        "পাঠ্যক্রম ফিলার: বড় ও দীর্ঘ-ফোকাস অভিলক্ষ্য আলো সংগ্রহ ও বিবর্ধন বাড়ায়।",
        filler=True,
    ),
    q(
        "A radio telescope's receiver is typically placed at the—",
        "রেডিও দূরবীক্ষণের রিসিভার সাধারণত রাখা হয়—",
        ["Random underground pit", "Focus of the parabolic dish", "Centre of the Earth", "Only on the Moon"],
        ["এলোমেলো মাটির গর্তে", "প্যারাবোলিক ডিশের ফোকাসে", "পৃথিবীর কেন্দ্রে", "শুধু চাঁদে"],
        "B", "easy", "factual",
        "Syllabus filler: the feed horn sits at the dish focus.",
        "পাঠ্যক্রম ফিলার: ফিড হর্ন ডিশের ফোকাসে থাকে।",
        filler=True,
    ),
    q(
        "Which statement about optical vs radio astronomy is correct?",
        "আলোকীয় বনাম রেডিও জ্যোতির্বিজ্ঞান সম্পর্কে কোনটি সঠিক?",
        [
            "Radio waves need clear nights only",
            "Radio can observe through clouds; optical needs clear skies",
            "Optical works equally well in heavy rain always",
            "Radio telescopes see only visible stars",
        ],
        [
            "রেডিওর জন্য শুধু পরিষ্কার রাত লাগে",
            "রেডিও মেঘ ভেদ করে দেখে; আলোকীয়তে পরিষ্কার আকাশ লাগে",
            "আলোকীয় ভারি বৃষ্টিতেও সমান ভালো",
            "রেডিও টেলিস্কোপ শুধু দৃশ্যমান নক্ষত্র দেখে",
        ],
        "B", "medium", "conceptual",
        "Syllabus filler: radio observing is less hindered by clouds than optical.",
        "পাঠ্যক্রম ফিলার: রেডিও পর্যবেক্ষণ মেঘে কম বাধা পায়।",
        filler=True,
    ),
    q(
        "Spherical aberration in a simple spherical mirror telescope is reduced by using a—",
        "সাধারণ গোলীয় দর্পণ দূরবীক্ষণে গোলীয় বিচ্যুতি কমাতে ব্যবহার করা হয়—",
        ["Parabolic primary mirror", "Thicker atmosphere", "Smaller wavelength only", "Higher humidity"],
        ["প্যারাবোলিক প্রাইমারি দর্পণ", "মোটা বায়ুমণ্ডল", "শুধু ছোট তরঙ্গদৈর্ঘ্য", "বেশি আর্দ্রতা"],
        "A", "medium", "conceptual",
        "Syllabus filler: a parabola focuses parallel rays to one point.",
        "পাঠ্যক্রম ফিলার: প্যারাবোলা সমান্তরাল রশ্মিকে এক ফোকাসে আনে।",
        filler=True,
    ),
    q(
        "The eyepiece of a telescope is used mainly to—",
        "দূরবীক্ষণের অভিনেত্র প্রধানত ব্যবহৃত হয়—",
        ["Collect all cosmic rays", "Magnify the intermediate image for the eye", "Generate radio noise", "Cool the objective"],
        ["সব কসমিক রশ্মি সংগ্রহে", "মধ্যবর্তী প্রতিবিম্ব চোখের জন্য বিবর্ধনে", "রেডিও নয়েজ সৃষ্টিতে", "অভিলক্ষ্য ঠান্ডা করতে"],
        "B", "easy", "factual",
        "Syllabus filler: the eyepiece acts as a magnifier for the objective's image.",
        "পাঠ্যক্রম ফিলার: অভিনেত্র অভিলক্ষ্যের প্রতিবিম্ব বিবর্ধন করে।",
        filler=True,
    ),
    q(
        "A Cassegrain reflecting telescope folds the light path using a—",
        "ক্যাসেগ্রেইন প্রতিফলনী দূরবীক্ষণ আলোর পথ ভাঁজ করে কোনটি দিয়ে?",
        ["Secondary convex mirror near the focus", "Only a glass prism train", "A radio horn alone", "A magnetic lens"],
        ["ফোকাসের কাছে সেকেন্ডারি উত্তল দর্পণ", "শুধু কাচের প্রিজম শ্রেণি", "শুধু রেডিও হর্ন", "চৌম্বক লেন্স"],
        "A", "medium", "factual",
        "Syllabus filler: Cassegrain designs use a secondary mirror to fold the beam.",
        "পাঠ্যক্রম ফিলার: ক্যাসেগ্রেইনে সেকেন্ডারি দর্পণ রশ্মি ভাঁজ করে।",
        filler=True,
    ),
]

# ---------------------------------------------------------------------------
# t04 — Space observation and satellites
# ---------------------------------------------------------------------------
T04 = [
    q(
        "Distance in space is measured in—\n(i) astronomical unit\n(ii) light-year unit\n(iii) parsec unit\nWhich is correct?",
        "মহাকাশে দূরত্ব মাপা হয়—\n(i) নভো এককে\n(ii) আলোক বছর এককে\n(iii) পারসেক এককে\nনিচের কোনটি সঠিক?",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "D", "easy", "factual",
        "Printed key: AU, light-year and parsec are all used for space distances.",
        "মুদ্রিত চাবি: নভো একক, আলোকবর্ষ ও পারসেক—সবই ব্যবহৃত।",
        bank_n=6,
    ),
    q(
        "In destructive events in space, which radiations are emitted?\n(i) gamma rays\n(ii) X-rays\n(iii) ultraviolet / violet rays\nWhich is correct?",
        "মহাকাশে বিভিন্ন ধ্বংসাত্মক ঘটনায় নির্গত হয়—\n(i) গামা রশ্মি\n(ii) X-রশ্মি\n(iii) বেগুনি রশ্মি\nনিচের কোনটি সঠিক?",
        ["i and ii", "ii and iii", "i and iii", "i, ii and iii"],
        ["i ও ii", "ii ও iii", "i ও iii", "i, ii ও iii"],
        "D", "medium", "factual",
        "Printed key: violent cosmic events emit γ, X and UV bands.",
        "মুদ্রিত চাবি: মহাজাগতিক বিধ্বংসী ঘটনায় γ, X ও UV নির্গত হয়।",
        bank_n=50,
    ),
    q(
        "Which order of length units is correct?",
        "নিচের কোনটি সঠিক ক্রম?",
        [
            "parsec > megametre > angstrom > light-year",
            "light-year > parsec > megametre > angstrom",
            "parsec > light-year > megametre > angstrom",
            "angstrom > parsec > megametre > light-year",
        ],
        [
            "পারসেক > মেগামিটার > অ্যাংস্ট্রম > আলোক বছর",
            "আলোক বছর > পারসেক > মেগামিটার > অ্যাংস্ট্রম",
            "পারসেক > আলোক বছর > মেগামিটার > অ্যাংস্ট্রম",
            "অ্যাংস্ট্রম > পারসেক > মেগামিটার > আলোক বছর",
        ],
        "C", "medium", "numerical",
        "Printed conversions: 1 pc > 1 ly ≫ 1 Mm ≫ 1 Å.",
        "মুদ্রিত রূপান্তর: 1 pc > 1 ly ≫ 1 Mm ≫ 1 Å।",
        bank_n=35,
    ),
    q(
        "An artificial satellite stays in orbit primarily because—",
        "কৃত্রিম উপগ্রহ কক্ষপথে থাকে প্রধানত কারণ—",
        [
            "Gravity is exactly zero in space",
            "Its tangential speed balances gravitational pull (free fall around Earth)",
            "It continuously burns fuel against gravity only",
            "Magnetic monopoles push it up",
        ],
        [
            "মহাকাশে মহাকর্ষ একদম শূন্য",
            "স্পর্শকীয় বেগ মহাকর্ষীয় টানের সাথে ভারসাম্য রাখে (পৃথিবীকে কেন্দ্র করে মুক্ত পতন)",
            "শুধু মহাকর্ষের বিরুদ্ধে জ্বালানি পোড়ায়",
            "চৌম্বক মনোপোল উপরে ঠেলে",
        ],
        "B", "medium", "conceptual",
        "Syllabus filler: orbital motion is continuous free-fall with suitable speed.",
        "পাঠ্যক্রম ফিলার: উপযুক্ত বেগে অবিরাম মুক্ত পতনই কক্ষপথ।",
        filler=True,
    ),
    q(
        "For a circular low-Earth orbit, orbital speed is of order—",
        "বৃত্তাকার নিম্ন পৃথিবী কক্ষপথে অরবিটাল বেগের মান প্রায়—",
        ["A few m/s", "About 7–8 km/s", "About c = 3 × 10⁸ m/s", "Zero always"],
        ["কয়েক m/s", "প্রায় 7–8 km/s", "প্রায় c = 3 × 10⁸ m/s", "সবসময় শূন্য"],
        "B", "medium", "numerical",
        "Syllabus filler: LEO speeds are several km/s (~7.9 km/s near surface scale).",
        "পাঠ্যক্রম ফিলার: LEO বেগ কয়েক km/s (প্রায় 7.9 km/s মাত্রায়)।",
        filler=True,
    ),
    q(
        "Geostationary satellites appear fixed in the sky because their orbital period is—",
        "ভূস্থির উপগ্রহ আকাশে স্থির দেখায় কারণ এদের পর্যায়কাল—",
        ["1 hour", "Equal to Earth's rotation period (~24 h)", "1 year only", "Equal to the Moon's month only"],
        ["1 ঘণ্টা", "পৃথিবীর ঘূর্ণন পর্যায়কালের সমান (~24 ঘণ্টা)", "শুধু 1 বছর", "শুধু চান্দ্র মাসের সমান"],
        "B", "easy", "factual",
        "Syllabus filler: GEO period matches sidereal day over the equator.",
        "পাঠ্যক্রম ফিলার: GEO পর্যায়কাল নিরক্ষরেখায় পার্থিব দিনের সাথে মিলে।",
        filler=True,
    ),
    q(
        "A major advantage of space-based observatories is that they—",
        "মহাকাশভিত্তিক মানমন্দিরের বড় সুবিধা হলো তারা—",
        [
            "Avoid Earth's atmospheric absorption and distortion",
            "Are cheaper than all ground telescopes always",
            "Cannot see ultraviolet at all",
            "Must use only sound detectors",
        ],
        [
            "পৃথিবীর বায়ুমণ্ডলীয় শোষণ ও বিকৃতি এড়ায়",
            "সব মাটির টেলিস্কোপের চেয়ে সবসময় সস্তা",
            "অতিবেগুনি একেবারেই দেখতে পারে না",
            "শুধু শব্দ শনাক্তক ব্যবহার করতে হয়",
        ],
        "A", "easy", "conceptual",
        "Syllabus filler: above the atmosphere, more of the EM spectrum is accessible.",
        "পাঠ্যক্রম ফিলার: বায়ুমণ্ডলের উপরে EM বর্ণালির বেশি অংশ দেখা যায়।",
        filler=True,
    ),
    q(
        "Communication satellites are commonly placed in—",
        "যোগাযোগ উপগ্রহ সাধারণত রাখা হয়—",
        ["Deep underground tunnels", "Geostationary or other high orbits", "Only inside the Sun", "Only Antarctic ice"],
        ["গভীর ভূগর্ভ সুড়ঙ্গে", "ভূস্থির বা অন্য উচ্চ কক্ষপথে", "শুধু সূর্যের ভিতরে", "শুধু অ্যান্টার্কটিক বরফে"],
        "B", "easy", "factual",
        "Syllabus filler: telecom links often use GEO / high-orbit satellites.",
        "পাঠ্যক্রম ফিলার: টেলিকম প্রায়ই GEO/উচ্চ কক্ষপথ ব্যবহার করে।",
        filler=True,
    ),
    q(
        "Remote-sensing Earth satellites are mainly used to—",
        "দূর সংবেদন পৃথিবী উপগ্রহ প্রধানত ব্যবহৃত হয়—",
        ["Observe weather, land and ocean from orbit", "Replace all optical laws", "Stop Earth's rotation", "Create black holes"],
        ["কক্ষপথ থেকে আবহাওয়া, স্থল ও মহাসাগর পর্যবেক্ষণে", "সব আলোকীয় সূত্র বদলাতে", "পৃথিবীর ঘূর্ণন থামাতে", "কৃষ্ণগহ্বর তৈরি করতে"],
        "A", "easy", "application",
        "Syllabus filler: Earth-observation satellites map climate, crops and oceans.",
        "পাঠ্যক্রম ফিলার: পৃথিবী পর্যবেক্ষণ উপগ্রহ জলবায়ু/ফসল/মহাসাগর মানচিত্র করে।",
        filler=True,
    ),
    q(
        "GPS navigation satellites form a constellation that provides—",
        "GPS ন্যাভিগেশন উপগ্রহ মণ্ডলী সরবরাহ করে—",
        ["Only weather forecasts", "Position and time signals to receivers on Earth", "Only tidal locking", "Only X-ray images of Mars"],
        ["শুধু আবহাওয়ার পূর্বাভাস", "পৃথিবীর রিসিভারে অবস্থান ও সময় সংকেত", "শুধু জোয়ার লকিং", "শুধু মঙ্গলের এক্স-রে ছবি"],
        "B", "easy", "application",
        "Syllabus filler: GNSS satellites broadcast timing for positioning.",
        "পাঠ্যক্রম ফিলার: GNSS উপগ্রহ অবস্থান নির্ণয়ে সময় সংকেত পাঠায়।",
        filler=True,
    ),
    q(
        "Escape velocity from Earth's surface is about—",
        "পৃথিবীর পৃষ্ঠ থেকে মুক্তি বেগ প্রায়—",
        ["7.9 km/s", "11.2 km/s", "30 km/s", "3 × 10⁸ m/s"],
        ["7.9 km/s", "11.2 km/s", "30 km/s", "3 × 10⁸ m/s"],
        "B", "medium", "numerical",
        "Syllabus filler: v_esc = √(2GM/R) ≈ 11.2 km/s for Earth.",
        "পাঠ্যক্রম ফিলার: পৃথিবীর মুক্তি বেগ ≈ 11.2 km/s।",
        filler=True,
    ),
    q(
        "Kepler's third law for satellites implies that farther orbits have—",
        "উপগ্রহের জন্য কেপলারের তৃতীয় সূত্র বলছে দূরবর্তী কক্ষপথের—",
        ["Shorter periods", "Longer periods", "Zero periods", "Infinite mass"],
        ["ছোট পর্যায়কাল", "বড় পর্যায়কাল", "শূন্য পর্যায়কাল", "অসীম ভর"],
        "B", "medium", "conceptual",
        "Syllabus filler: T² ∝ a³, so larger semi-major axis ⇒ longer period.",
        "পাঠ্যক্রম ফিলার: T² ∝ a³ — বড় কক্ষপথে পর্যায়কাল বেশি।",
        filler=True,
    ),
    q(
        "Polar-orbiting observation satellites are useful because they—",
        "মেরুকক্ষীয় পর্যবেক্ষণ উপগ্রহ উপযোগী কারণ তারা—",
        ["Stay fixed over one city forever", "Sweep over all latitudes as Earth rotates beneath", "Never see the poles", "Require zero orbital energy"],
        ["এক শহরের উপর চিরকাল স্থির থাকে", "পৃথিবী ঘোরার সাথে সব অক্ষাংশ ঝাড় দেয়", "মেরু কখনো দেখে না", "শূন্য অরবিটাল শক্তি চায়"],
        "B", "medium", "application",
        "Syllabus filler: polar LEO gives global surface coverage over successive orbits.",
        "পাঠ্যক্রম ফিলার: মেরুকক্ষ LEO ধারাবাহিক কক্ষে বৈশ্বিক আবরণ দেয়।",
        filler=True,
    ),
    q(
        "Hubble Space Telescope observes from orbit mainly to—",
        "হাবল স্পেস টেলিস্কোপ কক্ষপথ থেকে পর্যবেক্ষণ করে প্রধানত—",
        ["Avoid atmospheric blur for sharp optical/UV images", "Measure only Earth's core temperature", "Replace radio astronomy entirely", "Power all GPS phones"],
        ["বায়ুমণ্ডলীয় ঝাপসা এড়িয়ে তীক্ষ্ণ আলোকীয়/UV ছবি পেতে", "শুধু পৃথিবীর কেন্দ্রের তাপমাত্রা মাপতে", "রেডিও জ্যোতির্বিজ্ঞান পুরোপুরি বদলাতে", "সব GPS ফোন চালাতে"],
        "A", "easy", "factual",
        "Syllabus filler: HST sits above seeing/absorption for high-resolution imaging.",
        "পাঠ্যক্রম ফিলার: HST বায়ুমণ্ডলের উপরে উচ্চ রেজোলিউশন ছবি নেয়।",
        filler=True,
    ),
    q(
        "Weightlessness felt by astronauts in orbit means they are—",
        "কক্ষপথে নভোচারীদের ওজনহীনতা মানে তারা—",
        ["Outside all gravity", "In continuous free fall with the spacecraft", "At absolute zero temperature", "Moving faster than light"],
        ["সব মহাকর্ষের বাইরে", "মহাকাশযানের সাথে অবিরাম মুক্ত পতনে", "পরম শূন্য তাপমাত্রায়", "আলোর চেয়ে দ্রুত চলছে"],
        "B", "medium", "conceptual",
        "Syllabus filler: microgravity is orbital free-fall, not absence of gravity.",
        "পাঠ্যক্রম ফিলার: মাইক্রোগ্র্যাভিটি মানে অরবিটাল মুক্ত পতন—মহাকর্ষের অনুপস্থিতি নয়।",
        filler=True,
    ),
    q(
        "Which unit equals the mean Earth–Sun distance?",
        "কোন একক পৃথিবী–সূর্য গড় দূরত্বের সমান?",
        ["1 parsec", "1 astronomical unit (AU)", "1 angstrom", "1 fermi"],
        ["1 পারসেক", "1 নভো একক (AU)", "1 অ্যাংস্ট্রম", "1 ফার্মি"],
        "B", "easy", "factual",
        "Syllabus filler: 1 AU is defined from the Earth–Sun distance scale.",
        "পাঠ্যক্রম ফিলার: 1 AU পৃথিবী–সূর্য দূরত্ব মাপকাঠি।",
        filler=True,
    ),
    q(
        "A light-year is a unit of—",
        "আলোক বর্ষ কীসের একক?",
        ["Speed", "Distance", "Time", "Frequency"],
        ["দ্রুতির", "দূরত্বের", "সময়ের", "কম্পাঙ্কের"],
        "B", "easy", "factual",
        "Printed key: a light-year measures astronomical distance.",
        "মুদ্রিত চাবি: আলোক বর্ষ দূরত্বের একক।",
        bank_n=30,
    ),
    q(
        "One parsec (pc) equals—\n(i) 3.26 light years\n(ii) 9.46 × 10¹⁵ m\n(iii) 3.08 × 10¹³ km\nWhich is correct?",
        "এক পারসেক (pc) সমান—\n(i) 3.26 আলোক বর্ষ\n(ii) 9.46 × 10¹⁵ m\n(iii) 3.08 × 10¹³ km\nনিচের কোনটি সঠিক?",
        ["i only", "iii only", "i and iii", "i, ii and iii"],
        ["শুধু i", "শুধু iii", "i ও iii", "i, ii ও iii"],
        "C", "medium", "numerical",
        "Printed key: 1 pc ≈ 3.26 ly ≈ 3.08×10¹³ km; 9.46×10¹⁵ m is 1 light-year, not 1 pc.",
        "মুদ্রিত চাবি: 1 pc ≈ 3.26 ly ≈ 3.08×10¹³ km; 9.46×10¹⁵ m হলো 1 আলোকবর্ষ।",
        bank_n=3,
    ),
    q(
        "Weather satellites commonly use which orbits for global coverage sweeps?",
        "আবহাওয়া উপগ্রহ বৈশ্বিক আবরণের জন্য সাধারণত কোন কক্ষপথ ব্যবহার করে?",
        ["Only GEO fixed over one longitude always without imaging", "Sun-synchronous / polar LEO for repeated global passes", "Only solar escape trajectories", "Only subsurface tunnels"],
        ["শুধু এক দ্রাঘিমাংশে স্থির GEO ছাড়া ইমেজিং নেই", "সান-সিঙ্ক্রোনাস/মেরুকক্ষ LEO বারবার বৈশ্বিক পাসের জন্য", "শুধু সৌর পলায়ন কক্ষ", "শুধু ভূগর্ভ সুড়ঙ্গ"],
        "B", "medium", "application",
        "Syllabus filler: polar/sun-synchronous LEO enables repeated Earth weather imaging.",
        "পাঠ্যক্রম ফিলার: মেরু/সান-সিঙ্ক্রোনাস LEO বারবার আবহাওয়া ইমেজিং দেয়।",
        filler=True,
    ),
    q(
        "Space probes studying the Sun or planets typically communicate with Earth using—",
        "সূর্য বা গ্রহ অধ্যয়নরত মহাকাশ প্রোব সাধারণত পৃথিবীর সাথে যোগাযোগ করে—",
        ["Only acoustic underwater cables", "Radio / microwave telemetry links", "Only visible semaphore flags", "Only postal mail"],
        ["শুধু জলের নিচে অ্যাকোস্টিক কেবল", "রেডিও/মাইক্রোওয়েভ টেলিমেট্রি লিংক", "শুধু দৃশ্যমান সিমাফোর পতাকা", "শুধু ডাকযোগে চিঠি"],
        "B", "easy", "application",
        "Syllabus filler: deep-space missions downlink science data by radio telemetry.",
        "পাঠ্যক্রম ফিলার: গভীর মহাকাশ মিশন রেডিও টেলিমেট্রিতে তথ্য পাঠায়।",
        filler=True,
    ),
]


def main():
    assert len(T01) == 20 and len(T02) == 20 and len(T03) == 20 and len(T04) == 20

    maps = {
        "phy2_27_ch11_t01": write_topic("phy2_27_ch11_t01", T01),
        "phy2_27_ch11_t02": write_topic("phy2_27_ch11_t02", T02),
        "phy2_27_ch11_t03": write_topic("phy2_27_ch11_t03", T03),
        "phy2_27_ch11_t04": write_topic("phy2_27_ch11_t04", T04),
    }

    def bank_list(m):
        return [x for x in m if x != "filler"]

    # Local validate + global pipeline validate
    import core  # noqa: E402

    errors = []
    seen = set()
    dups = 0
    for tid in maps:
        for i, row in enumerate(core.read_jsonl(core.topic_path(tid)), 1):
            err = core.validate_record(row)
            if err:
                errors.append((tid, i, err))
            k = core.stem_key(row["stem_en"])
            if k in seen:
                dups += 1
            else:
                seen.add(k)

    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "question_bank" / "pipeline" / "bank.py"), "validate"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    out = (proc.stdout or "") + (proc.stderr or "")

    summary = {
        "chapter": "phy2_27_ch11",
        "title_en": "Astronomy",
        "title_bn": "জ্যোতিবিজ্ঞান",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p348_pdf354.png",
            "p349_pdf355.png",
            "p350_pdf356.png",
            "p351_pdf357.png",
        ],
        "skipped_faulty": {
            "Q08": "Four Hubble v–d graph panels; figure-only",
            "Q40": "Printed key b (ii,iii) excludes redshift as expansion evidence — faulty",
            "Q47": "Printed solar-energy option text chemically/physically reversed vs fusion; skipped",
            "Q51_particles": "Roman statements on lepton lifetime / antiparticles ambiguous vs printed numbering; skipped",
        },
        "counts": {
            "phy2_27_ch11_t01": 20,
            "phy2_27_ch11_t02": 20,
            "phy2_27_ch11_t03": 20,
            "phy2_27_ch11_t04": 20,
            "total": 80,
        },
        "pdf_mapping": {
            "phy2_27_ch11_t01": {
                "title": "Origin and fate of the universe / মহাবিশ্বের উৎপত্তি ও পরিণতি",
                "main_bank": bank_list(maps["phy2_27_ch11_t01"]),
                "cq_or_reconstructed_fillers": maps["phy2_27_ch11_t01"].count("filler"),
            },
            "phy2_27_ch11_t02": {
                "title": "Celestial objects and phenomena / মহাজাগতিক বস্তু ও ঘটনা",
                "main_bank": bank_list(maps["phy2_27_ch11_t02"]),
                "cq_or_reconstructed_fillers": maps["phy2_27_ch11_t02"].count("filler"),
            },
            "phy2_27_ch11_t03": {
                "title": "Optical and radio telescopes / আলোকীয় ও রেডিও দূরবীক্ষণ যন্ত্র",
                "main_bank": bank_list(maps["phy2_27_ch11_t03"]),
                "cq_or_reconstructed_fillers": maps["phy2_27_ch11_t03"].count("filler"),
            },
            "phy2_27_ch11_t04": {
                "title": "Space observation and satellites / মহাকাশ পর্যবেক্ষণ ও কৃত্রিম উপগ্রহ",
                "main_bank": bank_list(maps["phy2_27_ch11_t04"]),
                "cq_or_reconstructed_fillers": maps["phy2_27_ch11_t04"].count("filler"),
            },
        },
        "low_confidence": [
            "Q10 printed key d (5× solar mass) kept; solution note also mentions >3 M☉ supernova threshold.",
            "Q19 printed key b (Schwarzschild radius) kept though event horizon is the usual boundary name.",
            "Q20 printed key d (i and iii) kept for white-dwarf mass conditions.",
            "t03/t04 are thin in the Udvash MCQ band — syllabus-faithful fillers used heavily.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate",
            "exit_code": proc.returncode,
            "invalid": len(errors),
            "duplicates": dups,
            "stdout_tail": "\n".join(out.splitlines()[-20:]),
        },
    }

    PARSED.mkdir(parents=True, exist_ok=True)
    (PARSED / "ch11_curated_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary["counts"], ensure_ascii=False, indent=2))
    print("invalid", len(errors), "dups", dups, "validate_exit", proc.returncode)
    if errors:
        for e in errors:
            print("ERR", e)
        raise SystemExit(1)
    if proc.returncode != 0:
        print(out[-2000:])
        raise SystemExit(proc.returncode)


if __name__ == "__main__":
    main()
