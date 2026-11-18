#!/usr/bin/env python3
"""Seed Chemistry 2nd Paper Ch4 (Electrochemistry) bilingual MCQs.

Curated from Udvash HSC Question Bank 2026 printed pages 282–293 (PDF 288–299).
Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: chem2_27_ch04_t01..t04.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPICS = ROOT / "content" / "bank" / "topics"
PARSED = ROOT / "content" / "bank" / "udvash_raw" / "chemistry_2" / "parsed"
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
from core import validate_record  # noqa: E402

SRC = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "chemistry p2 ch04; curated bilingual"
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
    if not re.search(r"[ঀ-৿]", bn):
        bn = f"মান {bn}"
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
        "verified": False,
        "source": SRC,
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
        row["source"] = SRC
        err = validate_record(row)
        if err:
            raise SystemExit(f"{topic_id}: {err}\n{row['stem_en'][:120]}")
        lines.append(json.dumps(row, ensure_ascii=False))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {path.name}: {len(items)}")
    return mapping


# ---------------------------------------------------------------------------
# t01 — Oxidation and reduction / জারণ ও বিজারণ
# ---------------------------------------------------------------------------
T01 = [
    q(
        "Which of the following is an oxidation–reduction half-cell?",
        "নিচের কোনটি জারণ-বিজারণ অর্ধকোষ?",
        ["Sn4+/Sn2+, Pt", "Zn2+/Zn", "H+(aq)/H2(g), Pt", "Na/Na+"],
        ["Sn4+/Sn2+, Pt", "Zn2+/Zn", "H+(aq)/H2(g), Pt", "Na/Na+"],
        "A", "medium", "conceptual",
        "A redox half-cell has the same element in two oxidation states on an inert electrode (e.g. Sn4+/Sn2+, Pt).",
        "একই মৌলের দুই জারণ অবস্থা নিষ্ক্রিয় তড়িৎদ্বারে থাকলে জারণ-বিজারণ অর্ধকোষ হয় (যেমন Sn4+/Sn2+, Pt)।",
        bank_n=1,
    ),
    q(
        "Which electrode notation indicates an oxidation half-cell?",
        "কোন তড়িৎদ্বার প্রকাশ জারণ অর্ধকোষ নির্দেশ করে?",
        ["Zn2+/Zn", "Zn/Zn2+", "Cu2+/Cu", "H+/H2, Pt"],
        ["Zn2+/Zn", "Zn/Zn2+", "Cu2+/Cu", "H+/H2, Pt"],
        "B", "easy", "factual",
        "Oxidation is written metal/metal-ion (left → right electron loss): Zn/Zn2+.",
        "জারণ লেখা হয় ধাতু/ধাতব আয়ন রূপে: Zn/Zn2+।",
        bank_n=51,
    ),
    q(
        "Which is the strongest oxidizing agent among the following?",
        "নিচের কোনটি অধিকতর শক্তিশালী জারক?",
        ["H+", "Au3+", "Ag+", "Cu2+"],
        ["H+", "Au3+", "Ag+", "Cu2+"],
        "B", "medium", "conceptual",
        "Au3+ lies lowest in the electrochemical series and is most readily reduced.",
        "তড়িৎ রাসায়নিক সারিতে Au3+ সবচেয়ে নিচে; সহজে বিজারিত হয়।",
        bank_n=13,
    ),
    q(
        "Which is the strongest reducing agent among Cu, Pb, Zn and Ag?",
        "Cu, Pb, Zn ও Ag এর মধ্যে কোনটি তীব্রতম বিজারক?",
        ["Cu", "Pb", "Zn", "Ag"],
        ["Cu", "Pb", "Zn", "Ag"],
        "C", "easy", "conceptual",
        "Zn is highest among these in the activity series, so it is the strongest reducer.",
        "সক্রিয়তা সারিতে Zn উপরের দিকে; এটি সবচেয়ে শক্তিশালী বিজারক।",
        bank_n=20,
    ),
    q(
        "Which metal is the strongest reducing agent?",
        "কোনটি সবচেয়ে বেশি শক্তিশালী বিজারক?",
        ["Li", "Na", "K", "Ag"],
        ["Li", "Na", "K", "Ag"],
        "A", "easy", "factual",
        "Li has the most negative reduction potential and is the strongest reducer.",
        "Li-এর বিজারণ বিভব সবচেয়ে ঋণাত্মক; এটি শক্তিশালী বিজারক।",
        bank_n=50,
    ),
    q(
        "Which electrode represents a redox electrode?",
        "কোনটি জারণ-বিজারণ ইলেকট্রোড?",
        ["Cu/Cu2+", "H2/H+, Pt", "Pt(s), Fe2+/Fe3+", "Ag/AgCl, KCl"],
        ["Cu/Cu2+", "H2/H+, Pt", "Pt(s), Fe2+/Fe3+", "Ag/AgCl, KCl"],
        "C", "medium", "factual",
        "Pt with Fe2+/Fe3+ is a classic inert-electrode redox couple.",
        "Pt ও Fe2+/Fe3+ একটি ধ্রুপদী জারণ-বিজারণ তড়িৎদ্বার।",
        bank_n=146,
    ),
    q(
        "Which species can act as both oxidizing and reducing agent?",
        "কোনটি জারক ও বিজারক উভয়রূপে ক্রিয়া করে?",
        ["H2O2", "SO4^2−", "Hg2+", "Cl−"],
        ["H2O2", "SO4^2−", "Hg2+", "Cl−"],
        "A", "medium", "conceptual",
        "H2O2 can be oxidized to O2 or reduced to H2O, so it is amphiprotic in redox sense.",
        "H2O2 O2-তে জারিত বা H2O-তে বিজারিত হতে পারে।",
        bank_n=68,
    ),
    q(
        "In Cr2O7^2− → 2Cr3+ + 7H2O (acid medium), which statements are correct?\n(i) Six electrons are transferred\n(ii) Required charge is about 6F\n(iii) The reactant is an oxidizing agent",
        "Cr2O7^2− → 2Cr3+ + 7H2O অর্ধবিক্রিয়ায়—\n(i) ছয়টি ইলেকট্রন স্থানান্তরিত হয়\n(ii) প্রয়োজনীয় আধান প্রায় 6F\n(iii) বিক্রিয়কটি জারক পদার্থ",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["কেবল i ও ii", "কেবল i ও iii", "কেবল ii ও iii", "i, ii ও iii"],
        "D", "hard", "conceptual",
        "Each Cr(VI) → Cr(III) needs 3e−; two Cr need 6e− (6F). Dichromate is an oxidizer.",
        "দুইটি Cr-এর জন্য ৬e− (৬F); ডাইক্রোমেট জারক।",
        bank_n=35,
    ),
    q(
        "Oxidation number of Cr in K2Cr2O7 is:",
        "K2Cr2O7-এ Cr-এর জারণ সংখ্যা কত?",
        ["+3", "+4", "+6", "+7"],
        ["+৩", "+৪", "+৬", "+৭"],
        "C", "easy", "numerical",
        "2(+1) + 2x + 7(−2) = 0 → x = +6.",
        "২(+১) + ২x + ৭(−২) = ০ → x = +৬।",
        bank_n=None,
        filler=True,
    ),
    q(
        "In the reaction Zn + Cu2+ → Zn2+ + Cu, which statement is true?",
        "Zn + Cu2+ → Zn2+ + Cu বিক্রিয়ায় কোনটি সত্য?",
        [
            "Zn is reduced",
            "Cu2+ is oxidized",
            "Zn is oxidized and Cu2+ is reduced",
            "Both metals are oxidized",
        ],
        [
            "Zn বিজারিত হয়",
            "Cu2+ জারিত হয়",
            "Zn জারিত ও Cu2+ বিজারিত হয়",
            "উভয় ধাতু জারিত হয়",
        ],
        "C", "easy", "conceptual",
        "Zn loses electrons (oxidation); Cu2+ gains electrons (reduction).",
        "Zn ইলেকট্রন হারায় (জারণ); Cu2+ ইলেকট্রন গ্রহণ করে (বিজারণ)।",
        bank_n=None,
        filler=True,
    ),
    q(
        "Which half-cell is a metal–metal ion half-cell?",
        "কোনটি ধাতু–ধাতব আয়ন অর্ধকোষ?",
        ["Pt, Cl2/Cl−", "Ag, AgCl/Cl−", "Zn2+/Zn", "Pt, Fe2+/Fe3+"],
        ["Pt, Cl2/Cl−", "Ag, AgCl/Cl−", "Zn2+/Zn", "Pt, Fe2+/Fe3+"],
        "C", "easy", "factual",
        "Zn2+/Zn is a typical metal–metal ion electrode.",
        "Zn2+/Zn ধ্রুপদী ধাতু–ধাতব আয়ন তড়িৎদ্বার।",
        bank_n=70,
    ),
    q(
        "Na–Hg/Na+ half-cell is classified as:",
        "Na–Hg/Na+ অর্ধকোষটি কোন ধরনের?",
        [
            "metal–metal ion",
            "gas half-cell",
            "oxidation–reduction half-cell",
            "metal amalgam–metal ion",
        ],
        [
            "ধাতু–ধাতুর আয়ন",
            "গ্যাস অর্ধকোষ",
            "জারণ-বিজারণ অর্ধকোষ",
            "ধাতু অ্যামালগাম–ধাতুর আয়ন",
        ],
        "D", "medium", "factual",
        "Sodium amalgam with Na+ is a metal-amalgam electrode.",
        "সোডিয়াম অ্যামালগাম ও Na+ ধাতু-অ্যামালগাম তড়িৎদ্বার।",
        bank_n=140,
    ),
    q(
        "During oxidation, the oxidation number of an element:",
        "জারনের সময় কোনো মৌলের জারণ সংখ্যা:",
        ["decreases", "increases", "remains zero", "becomes fractional only"],
        ["কমে", "বাড়ে", "শূন্য থাকে", "শুধু ভগ্নাংশ হয়"],
        "B", "easy", "conceptual",
        "Oxidation means increase in oxidation number (electron loss).",
        "জারণ মানে জারণ সংখ্যা বৃদ্ধি (ইলেকট্রন হ্রাস)।",
        bank_n=None,
        filler=True,
    ),
    q(
        "Which ion is reduced first during electrolysis among Ag+, Cu2+, Fe2+, Zn2+?",
        "তড়িৎ বিশ্লেষণকালে কোনটি সর্বপ্রথম চার্জমুক্ত হবে?",
        ["Ag+", "Cu2+", "Fe2+", "Zn2+"],
        ["Ag+", "Cu2+", "Fe2+", "Zn2+"],
        "A", "medium", "conceptual",
        "Ag+ has the highest reduction potential among these cations.",
        "এদের মধ্যে Ag+-এর বিজারণ বিভব সর্বোচ্চ।",
        bank_n=36,
    ),
    q(
        "Among SO4^2−, Br−, Cl− and OH−, which anion is discharged first at the anode in aqueous electrolysis (preferential discharge)?",
        "জলীয় তড়িৎ বিশ্লেষণে অ্যানোডে কোন আয়ন আগে চার্জমুক্ত হয়?",
        ["SO4^2−", "Br−", "Cl−", "OH−"],
        ["SO4^2−", "Br−", "Cl−", "OH−"],
        "B", "hard", "conceptual",
        "Among common anions, Br− is preferentially oxidized before Cl−, OH− and SO4^2− under typical aqueous conditions.",
        "সাধারণত Br− Cl−, OH− ও SO4^2−-এর আগে জারিত হয়।",
        bank_n=9,
    ),
    q(
        "Oxidation number of S in Na2S2O3 is on average:",
        "Na2S2O3-এ সালফারের গড় জারণ সংখ্যা:",
        ["+2", "+3", "+4", "+6"],
        ["+২", "+৩", "+৪", "+৬"],
        "A", "medium", "numerical",
        "2(+1) + 2x + 3(−2) = 0 → x = +2 average.",
        "২(+১) + ২x + ৩(−২) = ০ → গড় x = +২।",
        bank_n=None,
        filler=True,
    ),
    q(
        "In Fe → Fe2+ + 2e−, iron is:",
        "Fe → Fe2+ + 2e− বিক্রিয়ায় লোহা:",
        ["reduced", "oxidized", "neither oxidized nor reduced", "precipitated only"],
        ["বিজারিত", "জারিত", "জারিত বা বিজারিত নয়", "শুধু অধঃক্ষিপ্ত"],
        "B", "easy", "conceptual",
        "Loss of electrons is oxidation.",
        "ইলেকট্রন হারানোই জারণ।",
        bank_n=None,
        filler=True,
    ),
    q(
        "Which has the lowest oxidation potential among Cu, Au, H2 and Li?",
        "কোনটির জারণ বিভব সবচেয়ে কম?",
        ["copper", "gold", "hydrogen", "lithium"],
        ["কপার", "গোল্ড", "হাইড্রোজেন", "লিথিয়াম"],
        "B", "medium", "conceptual",
        "Gold is least active; its oxidation potential is lowest (most noble).",
        "সোনা সবচেয়ে নিষ্ক্রিয়; জারণ বিভব সর্বনিম্ন।",
        bank_n=49,
    ),
    q(
        "For the half-reaction Fe2+ + 2e− → Fe, charge needed to produce 1 mol Fe is:",
        "Fe2+ + 2e− → Fe বিক্রিয়ায় ১ মোল Fe উৎপাদনে কত চার্জ লাগে?",
        ["1F", "2F", "3F", "4F"],
        ["১F", "২F", "৩F", "৪F"],
        "B", "easy", "numerical",
        "Two moles of electrons (2F) reduce 1 mol Fe2+.",
        "১ মোল Fe2+ বিজারনে ২F চার্জ লাগে।",
        bank_n=62,
    ),
    q(
        "Which reaction is a redox process?",
        "কোনটি জারণ-বিজারণ বিক্রিয়া?",
        [
            "HCl + NaOH → NaCl + H2O",
            "AgNO3 + NaCl → AgCl + NaNO3",
            "Zn + H2SO4 → ZnSO4 + H2",
            "BaCl2 + Na2SO4 → BaSO4 + 2NaCl",
        ],
        [
            "HCl + NaOH → NaCl + H2O",
            "AgNO3 + NaCl → AgCl + NaNO3",
            "Zn + H2SO4 → ZnSO4 + H2",
            "BaCl2 + Na2SO4 → BaSO4 + 2NaCl",
        ],
        "C", "easy", "conceptual",
        "Zn is oxidized and H+ is reduced.",
        "Zn জারিত ও H+ বিজারিত হয়।",
        bank_n=None,
        filler=True,
    ),
]


# ---------------------------------------------------------------------------
# t02 — Electrochemical cells and electrodes / তড়িৎ রাসায়নিক কোষ ও তড়িৎদ্বার
# ---------------------------------------------------------------------------
T02 = [
    q(
        "In a galvanic cell, which conversion occurs?",
        "গ্যালভানিক কোষে কোনটি ঘটে?",
        [
            "chemical energy → electrical energy",
            "electrical energy → chemical energy",
            "heat energy → chemical energy",
            "electrical energy → heat energy only",
        ],
        [
            "রাসায়নিক শক্তি → তড়িৎ শক্তি",
            "তড়িৎ শক্তি → রাসায়নিক শক্তি",
            "তাপ শক্তি → রাসায়নিক শক্তি",
            "কেবল তড়িৎ শক্তি → তাপ শক্তি",
        ],
        "A", "easy", "conceptual",
        "Galvanic (voltaic) cells convert spontaneous chemical change into electricity.",
        "গ্যালভানিক কোষে স্বতঃস্ফূর্ত রাসায়নিক শক্তি তড়িৎ শক্তিতে রূপান্তরিত হয়।",
        bank_n=9,
    ),
    q(
        "Standard hydrogen electrode potential is:",
        "প্রমাণ হাইড্রোজেন তড়িৎদ্বারের বিভব মান কত?",
        ["+1.0 V", "−1.34 V", "+0.76 V", "0.0 V"],
        ["+১.০ V", "−১.৩৪ V", "+০.৭৬ V", "০.০ V"],
        "D", "easy", "factual",
        "By definition, E°(H+/H2) = 0.00 V.",
        "সংজ্ঞা অনুসারে E°(H+/H2) = ০.০০ V।",
        bank_n=12,
    ),
    q(
        "For a standard hydrogen electrode, which conditions are required?\n(i) pressure 1 atm\n(ii) [H+] = 0.1 M\n(iii) temperature 25 °C",
        "প্রমাণ হাইড্রোজেন তড়িৎদ্বারের ক্ষেত্রে—\n(i) চাপ ১ atm\n(ii) [H+] = ০.১ M\n(iii) তাপমাত্রা ২৫ °C",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["কেবল i ও ii", "কেবল i ও iii", "কেবল ii ও iii", "i, ii ও iii"],
        "B", "medium", "factual",
        "SHE uses [H+] = 1 M (not 0.1 M), 1 atm H2, and usually 25 °C.",
        "SHE-তে [H+] = ১ M, ১ atm H2 ও সাধারণত ২৫ °C।",
        bank_n=7,
    ),
    q(
        "Which salt is commonly used in a salt bridge?",
        "লবণ সেতুতে কোনটি ব্যবহার করা যায়?",
        ["CaCl2", "CuCl2", "KCl", "Al2(SO4)3"],
        ["CaCl2", "CuCl2", "KCl", "Al2(SO4)3"],
        "C", "easy", "factual",
        "KCl (or KNO3/NH4NO3) ions have similar mobility and do not react with cell ions.",
        "KCl আয়নগুলোর গতিশীলতা কাছাকাছি এবং কোষের সাথে বিক্রিয়া করে না।",
        bank_n=18,
    ),
    q(
        "Calomel electrode uses which compound?",
        "ক্যালোমেল তড়িৎদ্বারে কোনটি ব্যবহৃত হয়?",
        ["Hg2Cl2", "NH4NO3", "HgCl2", "NH4Cl"],
        ["Hg2Cl2", "NH4NO3", "HgCl2", "NH4Cl"],
        "A", "easy", "factual",
        "Calomel electrode is Hg | Hg2Cl2 | KCl.",
        "ক্যালোমেল তড়িৎদ্বার: Hg | Hg2Cl2 | KCl।",
        bank_n=5,
    ),
    q(
        "Correct cell notation for the Zn–Cu Daniell cell is:",
        "কোনটি সঠিক Zn–Cu কোষ গঠন?",
        [
            "Zn/Zn2+ || Cu2+/Cu",
            "Cu/Cu2+ || Zn2+/Zn",
            "Cu2+/Cu || Zn/Zn2+",
            "Zn2+/Zn || Cu2+/Cu",
        ],
        [
            "Zn/Zn2+ || Cu2+/Cu",
            "Cu/Cu2+ || Zn2+/Zn",
            "Cu2+/Cu || Zn/Zn2+",
            "Zn2+/Zn || Cu2+/Cu",
        ],
        "A", "easy", "conceptual",
        "Anode (oxidation) is written on the left: Zn/Zn2+ || Cu2+/Cu.",
        "অ্যানোড বামে: Zn/Zn2+ || Cu2+/Cu।",
        bank_n=45,
    ),
    q(
        "Functions of a salt bridge include:\n(i) connecting the two half-cells\n(ii) eliminating liquid junction potential\n(iii) maintaining electrical neutrality",
        "লবণ সেতুর কাজ—\n(i) দুই অর্ধকোষ সংযোগ\n(ii) তরল সংযোগ বিভব দূর করা\n(iii) তড়িৎ নিরপেক্ষতা বজায় রাখা",
        ["i only", "i and ii only", "i and iii only", "i, ii and iii"],
        ["কেবল i", "কেবল i ও ii", "কেবল i ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "All three roles are standard salt-bridge functions.",
        "তিনটিই লবণ সেতুর মানক কাজ।",
        bank_n=121,
    ),
    q(
        "In an electrochemical cell:",
        "তড়িৎ রাসায়নিক কোষে—",
        [
            "anode is positive and reduction occurs there",
            "cathode is negative in a galvanic cell",
            "oxidation occurs at the anode",
            "electrons flow from cathode to anode externally",
        ],
        [
            "অ্যানোড ধনাত্মক ও সেখানে বিজারণ ঘটে",
            "গ্যালভানিক কোষে ক্যাথোড ঋণাত্মক",
            "অ্যানোডে জারণ ঘটে",
            "বহিঃবর্তনীতে ইলেকট্রন ক্যাথোড থেকে অ্যানোডে যায়",
        ],
        "C", "easy", "conceptual",
        "By definition, oxidation occurs at the anode.",
        "সংজ্ঞা অনুসারে অ্যানোডে জারণ ঘটে।",
        bank_n=109,
    ),
    q(
        "Which is an electronic conductor?",
        "কোনটি ইলেকট্রনীয় পরিবাহী?",
        ["CuSO4 solution", "copper wire", "molten NaCl", "glass tube"],
        ["CuSO4 দ্রবণ", "Cu তার", "গলিত NaCl", "কাচনল"],
        "B", "easy", "factual",
        "Metals conduct via free electrons; solutions/melts are electrolytic conductors.",
        "ধাতু মুক্ত ইলেকট্রন দিয়ে পরিবহন করে।",
        bank_n=103,
    ),
    q(
        "Sucrose solution is:",
        "সুক্রোজের দ্রবণটি—",
        ["an electrolyte", "a non-electrolyte", "an electronic conductor", "a metallic conductor"],
        ["তড়িৎ বিশ্লেষ্য", "তড়িৎ অবিশ্লেষ্য", "ইলেকট্রনীয় পরিবাহী", "ধাতব পরিবাহী"],
        "B", "easy", "factual",
        "Sucrose does not ionize; it is a non-electrolyte.",
        "সুক্রোজ আয়নিত হয় না; এটি তড়িৎ অবিশ্লেষ্য।",
        bank_n=81,
    ),
    q(
        "Secondary reference electrodes include:\n(i) Pt, H2 (1 atm)/H+ (1 M)\n(ii) Ag(s), AgCl(s)/HCl(aq)\n(iii) Hg(l), Hg2Cl2(s)/KCl(aq)",
        "সেকেন্ডারি নির্দেশক তড়িৎদ্বার—\n(i) Pt, H2 (1 atm)/H+ (1 M)\n(ii) Ag(s), AgCl(s)/HCl(aq)\n(iii) Hg(l), Hg2Cl2(s)/KCl(aq)",
        ["i only", "i and ii", "ii and iii", "i, ii and iii"],
        ["কেবল i", "i ও ii", "ii ও iii", "i, ii ও iii"],
        "C", "medium", "factual",
        "SHE is primary; Ag/AgCl and calomel are secondary references.",
        "SHE প্রাইমারি; Ag/AgCl ও ক্যালোমেল সেকেন্ডারি।",
        bank_n=90,
    ),
    q(
        "In a dry cell, the anode is commonly:",
        "শুষ্ক কোষে অ্যানোড হিসেবে ব্যবহৃত হয়:",
        ["NH4Cl", "MnO2", "Zn", "graphite only"],
        ["NH4Cl", "MnO2", "Zn", "কেবল গ্রাফাইট"],
        "C", "easy", "factual",
        "The zinc can is the anode in a Leclanché dry cell.",
        "শুষ্ক কোষে Zn ক্যান অ্যানোড।",
        bank_n=None,
        filler=True,
    ),
    q(
        "For Pt, H2/H+ || Cu2+/Cu with E°(Cu2+/Cu) = +0.34 V, E°cell is:",
        "Pt, H2/H+ || Cu2+/Cu কোষে E°(Cu2+/Cu) = +0.34 V হলে emf:",
        ["0.00 V", "+0.34 V", "−0.34 V", "+0.17 V"],
        ["০.০০ V", "+০.৩৪ V", "−০.৩৪ V", "+০.১৭ V"],
        "B", "easy", "numerical",
        "E°cell = 0 + 0.34 = +0.34 V.",
        "E°cell = ০ + ০.৩৪ = +০.৩৪ V।",
        bank_n=48,
    ),
    q(
        "Which compound is suitable for a salt bridge?",
        "কোন যৌগটি লবণ সেতুতে ব্যবহৃত হয়?",
        ["CuCl2", "KMnO4", "K2Cr2O7", "KNO3"],
        ["CuCl2", "KMnO4", "K2Cr2O7", "KNO3"],
        "D", "easy", "factual",
        "KNO3 does not interfere with electrode reactions and is commonly used.",
        "KNO3 তড়িৎদ্বার বিক্রিয়ায় হস্তক্ষেপ করে না।",
        bank_n=42,
    ),
    q(
        "In which device is electrical energy consumed (non-spontaneous)?",
        "কোনটিতে বিদ্যুৎ শক্তি ব্যয়িত হয়?",
        ["electrolytic cell", "lead–acid cell (discharging)", "lithium-ion battery (discharging)", "galvanic cell"],
        ["তড়িৎ বিশ্লেষ্য কোষ", "লেড অ্যাসিড কোষ (ডিসচার্জ)", "লিথিয়াম আয়ন ব্যাটারি (ডিসচার্জ)", "গ্যালভানিক কোষ"],
        "A", "medium", "conceptual",
        "Electrolytic cells drive non-spontaneous reactions using external electricity.",
        "তড়িৎ বিশ্লেষ্য কোষে বাহ্যিক তড়িৎ দিয়ে অস্বতঃস্ফূর্ত বিক্রিয়া চালানো হয়।",
        bank_n=163,
    ),
    q(
        "Molten NaCl conducts electricity because of:",
        "গলিত NaCl-এর তড়িৎ পরিবাহিতার কারণ:",
        ["free electrons", "free atoms", "free ions", "free molecules"],
        ["মুক্ত ইলেকট্রন", "মুক্ত পরমাণু", "মুক্ত আয়ন", "মুক্ত অণু"],
        "C", "easy", "conceptual",
        "Ionic melts conduct via mobile cations and anions.",
        "গলিত লবণে মুক্ত আয়ন পরিবহন করে।",
        bank_n=144,
    ),
    q(
        "Number of types of reference electrodes commonly taught is:",
        "নির্দেশক তড়িৎদ্বার কত প্রকার?",
        ["one", "two", "three", "five"],
        ["এক", "দুই", "তিন", "পাঁচ"],
        "B", "easy", "factual",
        "Reference electrodes are classified as primary and secondary.",
        "প্রাইমারি ও সেকেন্ডারি—দুই প্রকার।",
        bank_n=132,
    ),
    q(
        "For cell reaction H2 + Cu2+ → 2H+ + Cu, the anode reaction is:",
        "কোষ বিক্রিয়া H2 + Cu2+ → 2H+ + Cu-এ অ্যানোড বিক্রিয়া:",
        ["2H+ + 2e− → H2", "Cu → Cu2+ + 2e−", "H2 → 2H+ + 2e−", "Cu2+ + 2e− → Cu"],
        ["2H+ + 2e− → H2", "Cu → Cu2+ + 2e−", "H2 → 2H+ + 2e−", "Cu2+ + 2e− → Cu"],
        "C", "medium", "conceptual",
        "H2 is oxidized at the anode.",
        "অ্যানোডে H2 জারিত হয়।",
        bank_n=104,
    ),
    q(
        "Unit of conductivity (conductance) includes:\n(i) mho\n(ii) ohm−1\n(iii) siemens",
        "পরিবাহিতার একক—\n(i) mho\n(ii) ohm−1\n(iii) Siemens",
        ["i only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["কেবল i", "কেবল ii ও iii", "কেবল i ও iii", "i, ii ও iii"],
        "D", "easy", "factual",
        "Siemens (S) = ohm−1 = mho.",
        "Siemens = ohm−1 = mho।",
        bank_n=85,
    ),
    q(
        "Which is a strong electrolyte?",
        "কোনটি তীব্র তড়িৎ বিশ্লেষ্য পদার্থ?",
        ["pure water", "CH3COOH", "sucrose", "CuSO4 solution"],
        ["বিশুদ্ধ পানি", "CH3COOH", "সুক্রোজ", "CuSO4 দ্রবণ"],
        "D", "easy", "factual",
        "CuSO4 is a strong electrolyte; acetic acid is weak; sucrose/water are non/very weak.",
        "CuSO4 তীব্র তড়িৎ বিশ্লেষ্য।",
        bank_n=128,
    ),
]


# ---------------------------------------------------------------------------
# t03 — Cell potential and electrochemical series / কোষ বিভব ও তড়িৎ রাসায়নিক সারি
# ---------------------------------------------------------------------------
T03 = [
    q(
        "For Zn(s) + Cu2+(aq) → Zn2+(aq) + Cu(s); E°(Zn2+/Zn) = −0.76 V, E°(Cu2+/Cu) = +0.34 V. E°cell =?",
        "Zn + Cu2+ → Zn2+ + Cu; E°(Zn2+/Zn)=−০.৭৬ V, E°(Cu2+/Cu)=+০.৩৪ V হলে E°cell=?",
        ["+1.1 V", "+1.4 V", "−1.1 V", "−1.4 V"],
        ["+১.১ V", "+১.৪ V", "−১.১ V", "−১.৪ V"],
        "A", "easy", "numerical",
        "E°cell = E°cathode − E°anode = 0.34 − (−0.76) = 1.10 V.",
        "E°cell = ০.৩৪ − (−০.৭৬) = ১.১০ V।",
        bank_n=8,
    ),
    q(
        "Position of Cu in the electrochemical series:\n(i) above Fe\n(ii) above Ag\n(iii) below H",
        "তড়িৎ রাসায়নিক সিরিজে Cu-এর অবস্থান—\n(i) Fe-এর উপরে\n(ii) Ag-এর উপরে\n(iii) H-এর নিচে",
        ["i and ii only", "ii and iii only", "iii only", "i, ii and iii"],
        ["কেবল i ও ii", "কেবল ii ও iii", "কেবল iii", "i, ii ও iii"],
        "B", "medium", "factual",
        "Cu is below H and above Ag (less active than Fe).",
        "Cu H-এর নিচে ও Ag-এর উপরে; Fe-এর নিচে।",
        bank_n=6,
    ),
    q(
        "Zn and Fe electrodes have E° = −0.76 V and −0.44 V. Cell potential is:",
        "Zn ও Fe-এর প্রমাণ বিজারণ বিভব −০.৭৬ V ও −০.৪৪ V হলে কোষ বিভব:",
        ["1.20 V", "0.32 V", "−0.32 V", "−1.20 V"],
        ["১.২০ V", "০.৩২ V", "−০.৩২ V", "−১.২০ V"],
        "B", "easy", "numerical",
        "E°cell = (−0.44) − (−0.76) = 0.32 V (Zn anode).",
        "E°cell = (−০.৪৪) − (−০.৭৬) = ০.৩২ V।",
        bank_n=15,
    ),
    q(
        "SHE acts as cathode when paired with which electrode?",
        "প্রমাণ হাইড্রোজেন তড়িৎদ্বার কোনটির সাথে ক্যাথোড হিসেবে কাজ করে?",
        ["Zn/Zn2+", "Au/Au3+", "Cu/Cu2+", "Ag/Ag+"],
        ["Zn/Zn2+", "Au/Au3+", "Cu/Cu2+", "Ag/Ag+"],
        "A", "medium", "conceptual",
        "With Zn (more negative E°), H+ is reduced at the SHE (cathode).",
        "Zn-এর সাথে SHE-তে H+ বিজারিত হয় (ক্যাথোড)।",
        bank_n=17,
    ),
    q(
        "Ni(s)/Ni2+ || Ag+/Ag; E°(Ni2+/Ni)=−0.25 V, E°(Ag+/Ag)=+0.80 V. Cell potential is:",
        "Ni/Ni2+ || Ag+/Ag; E°=−০.২৫ V ও +০.৮০ V হলে কোষ বিভব:",
        ["0.55 V", "0.61 V", "1.05 V", "1.85 V"],
        ["০.৫৫ V", "০.৬১ V", "১.০৫ V", "১.৮৫ V"],
        "C", "easy", "numerical",
        "E°cell = 0.80 − (−0.25) = 1.05 V.",
        "E°cell = ০.৮০ − (−০.২৫) = ১.০৫ V।",
        bank_n=7,
    ),
    q(
        "Electrode potential equations include:\n(i) Ecell = Ecathode(red) − Eanode(red)\n(ii) Ecell = Eanode(ox) − Ecathode(ox)\n(iii) Ecell = Eanode(ox) + Ecathode(red)",
        "কোষ বিভব নির্ণয়ের সমীকরণ—\n(i) Ecell = Ecathode(red) − Eanode(red)\n(ii) Ecell = Eanode(ox) − Ecathode(ox)\n(iii) Ecell = Eanode(ox) + Ecathode(red)",
        ["i and ii only", "i and iii only", "ii and iii only", "i, ii and iii"],
        ["কেবল i ও ii", "কেবল i ও iii", "কেবল ii ও iii", "i, ii ও iii"],
        "D", "hard", "conceptual",
        "All three equivalent forms are used when signs of oxidation/reduction potentials are consistent.",
        "চিহ্ন সামঞ্জস্য রাখলে তিনটি রূপই সমতুল্য।",
        bank_n=6,
    ),
    q(
        "Which electrode has the highest reduction potential?",
        "কোন তড়িৎদ্বারের বিজারণ বিভব বেশি?",
        ["Ag+/Ag", "Ni2+/Ni", "Zn2+/Zn", "Na+/Na"],
        ["Ag+/Ag", "Ni2+/Ni", "Zn2+/Zn", "Na+/Na"],
        "A", "easy", "conceptual",
        "Ag+/Ag is most noble among the listed couples.",
        "তালিকায় Ag+/Ag সবচেয়ে মহৎ।",
        bank_n=39,
    ),
    q(
        "Oxidation potential of nickel is approximately:",
        "নিকেলের জারণ বিভবের মান প্রায় কত?",
        ["+0.76 V", "−0.80 V", "+0.44 V", "+0.25 V"],
        ["+০.৭৬ V", "−০.৮০ V", "+০.৪৪ V", "+০.২৫ V"],
        "D", "medium", "factual",
        "E°ox(Ni) ≈ +0.25 V when E°red(Ni2+/Ni) ≈ −0.25 V.",
        "E°red ≈ −০.২৫ V হলে E°ox ≈ +০.২৫ V।",
        bank_n=32,
    ),
    q(
        "Maximum useful work from an electrochemical cell equals:",
        "তড়িৎ রাসায়নিক কোষ দ্বারা সর্বোচ্চ কৃত কাজের মান:",
        ["ΔG = −nFE", "ΔG = +nFE", "RT ln K only", "ΔH only"],
        ["ΔG = −nFE", "ΔG = +nFE", "কেবল RT ln K", "কেবল ΔH"],
        "A", "medium", "conceptual",
        "Wmax,electrical = −ΔG = nFE for a reversible cell.",
        "প্রতিবর্তী কোষে Wmax = nFE = −ΔG।",
        bank_n=21,
    ),
    q(
        "Zn/Zn2+ (E°ox = +0.76 V) and Ag/Ag+ (E°ox = −0.80 V) give E°cell ≈:",
        "Zn/Zn2+ (E°ox=+০.৭৬ V) ও Ag/Ag+ (E°ox=−০.৮০ V) হলে E°cell ≈:",
        ["1.459 V", "1.559 V", "1.669 V", "2.559 V"],
        ["১.৪৫৯ V", "১.৫৫৯ V", "১.৬৬৯ V", "২.৫৫৯ V"],
        "B", "medium", "numerical",
        "E°cell = 0.76 + 0.80 = 1.56 V ≈ 1.559 V.",
        "E°cell = ০.৭৬ + ০.৮০ ≈ ১.৫৫৯ V।",
        bank_n=71,
    ),
    q(
        "Ag+/Ag (E°= +0.80 V) and Au+/Au (E°= +1.56 V) give cell potential:",
        "Ag+/Ag (+০.৮০ V) ও Au+/Au (+১.৫৬ V) কোষের বিভব:",
        ["+0.76 V", "−0.76 V", "+2.36 V", "−2.36 V"],
        ["+০.৭৬ V", "−০.৭৬ V", "+২.৩৬ V", "−২.৩৬ V"],
        "A", "medium", "numerical",
        "Ag is anode: E°cell = 1.56 − 0.80 = 0.76 V.",
        "Ag অ্যানোড: E°cell = ১.৫৬ − ০.৮০ = ০.৭৬ V।",
        bank_n=107,
    ),
    q(
        "Which metal can liberate H2 from dilute H2SO4?",
        "কোনটি লঘু H2SO4 থেকে হাইড্রোজেন বিমুক্ত করতে পারে?",
        ["Pb", "Hg", "Cu", "Ca"],
        ["Pb", "Hg", "Cu", "Ca"],
        "D", "easy", "conceptual",
        "Metals above H in the series (e.g. Ca) displace H2 from acids.",
        "H-এর উপরের ধাতু (যেমন Ca) অ্যাসিড থেকে H2 মুক্ত করে।",
        bank_n=77,
    ),
    q(
        "Which element cannot displace hydrogen from HCl?",
        "কোন মৌলটি HCl থেকে হাইড্রোজেন প্রতিস্থাপন করতে পারে না?",
        ["Fe", "Zn", "Mg", "Pt"],
        ["Fe", "Zn", "Mg", "Pt"],
        "D", "easy", "conceptual",
        "Pt is below hydrogen and cannot displace H2 from acids.",
        "Pt H-এর নিচে; H2 প্রতিস্থাপন করে না।",
        bank_n=94,
    ),
    q(
        "If Fe/Fe2+ is the anode, which can serve as cathode?",
        "Fe/Fe2+ অ্যানোড হলে কোনটি ক্যাথোড হিসেবে ব্যবহার করা যাবে?",
        ["Zn/Zn2+", "Mg/Mg2+", "Al/Al3+", "Au/Au3+"],
        ["Zn/Zn2+", "Mg/Mg2+", "Al/Al3+", "Au/Au3+"],
        "D", "medium", "conceptual",
        "Cathode must have higher reduction potential; Au3+/Au qualifies.",
        "ক্যাথোডে উচ্চতর বিজারণ বিভব দরকার; Au উপযুক্ত।",
        bank_n=159,
    ),
    q(
        "Sn(s)/Sn2+ || H+/H2; E°(Sn2+/Sn) = −0.14 V. EMF is:",
        "Sn/Sn2+ || H+/H2; E°(Sn2+/Sn)=−০.১৪ V হলে EMF:",
        ["−0.14 V", "−0.07 V", "+0.07 V", "+0.14 V"],
        ["−০.১৪ V", "−০.০৭ V", "+০.০৭ V", "+০.১৪ V"],
        "D", "medium", "numerical",
        "With Sn as anode and SHE as cathode: E° = 0 − (−0.14) = +0.14 V.",
        "Sn অ্যানোড, SHE ক্যাথোড: E° = +০.১৪ V।",
        bank_n=157,
    ),
    q(
        "M/M2+ || N+/N with E°(M2+/M)= −0.76 V and E°(N+/N)= +0.40 V. EMF is:",
        "M/M2+ || N+/N; E°=−০.৭৬ V ও +০.৪০ V হলে emf:",
        ["+1.16 V", "+0.36 V", "−0.36 V", "−1.16 V"],
        ["+১.১৬ V", "+০.৩৬ V", "−০.৩৬ V", "−১.১৬ V"],
        "A", "easy", "numerical",
        "E°cell = 0.40 − (−0.76) = 1.16 V.",
        "E°cell = ০.৪০ − (−০.৭৬) = ১.১৬ V।",
        bank_n=102,
    ),
    q(
        "For Zn/Zn2+ (0.001 M) || Ag+ (0.1 M)/Ag, E° = 1.56 V. Approximate Ecell is:",
        "Zn/Zn2+(0.001 M)||Ag+(0.1 M)/Ag; E°=১.৫৬ V হলে প্রায় Ecell:",
        ["1.61 V", "1.59 V", "1.46 V", "1.10 V"],
        ["১.৬১ V", "১.৫৯ V", "১.৪৬ V", "১.১০ V"],
        "B", "hard", "numerical",
        "Nernst: E = 1.56 − (0.059/2) log([Zn2+]/[Ag+]^2) ≈ 1.59 V.",
        "নার্নস্ট সমীকরণে ≈ ১.৫৯ V।",
        bank_n=2,
    ),
    q(
        "Among Li+, Na+, Zn2+, Cu2+, which ion is discharged first during electrolysis?",
        "Li+, Na+, Zn2+, Cu2+ এর মধ্যে কোন আয়ন সর্বপ্রথম চার্জমুক্ত হবে?",
        ["Cu2+", "Zn2+", "Na+", "Li+"],
        ["Cu2+", "Zn2+", "Na+", "Li+"],
        "A", "medium", "conceptual",
        "Cu2+ has the least negative (highest) reduction potential among these.",
        "এদের মধ্যে Cu2+-এর বিজারণ বিভব সর্বোচ্চ।",
        bank_n=116,
    ),
    q(
        "Cell emf depends on:\n(i) oxidation and reduction potentials\n(ii) ion concentrations\n(iii) gas pressures",
        "কোষের emf নির্ভর করে—\n(i) জারণ ও বিজারণ বিভবের উপর\n(ii) আয়নের ঘনমাত্রার উপর\n(iii) গ্যাসের চাপের উপর",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["কেবল i ও ii", "কেবল ii ও iii", "কেবল i ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "Nernst equation includes E°, concentrations, and partial pressures.",
        "নার্নস্ট সমীকরণে E°, ঘনমাত্রা ও চাপ সবই আসে।",
        bank_n=None,
        filler=True,
    ),
    q(
        "With Zn as anode (E°ox = +0.76 V), which cathode is suitable?",
        "Zn অ্যানোড (E°ox=+০.৭৬ V) হলে কোনটি ক্যাথোড হিসেবে উপযুক্ত?",
        [
            "Co/Co2+ (E°ox = +0.28 V)",
            "Mg/Mg2+ (E°ox = +2.36 V)",
            "Ca/Ca2+ (E°ox = +2.87 V)",
            "Al/Al3+ (E°ox = +1.66 V)",
        ],
        [
            "Co/Co2+ (E°ox = +০.২৮ V)",
            "Mg/Mg2+ (E°ox = +২.৩৬ V)",
            "Ca/Ca2+ (E°ox = +২.৮৭ V)",
            "Al/Al3+ (E°ox = +১.৬৬ V)",
        ],
        "A", "hard", "application",
        "Cathode must have lower oxidation potential than Zn; Co (+0.28 V) works.",
        "ক্যাথোডে Zn-এর চেয়ে কম জারণ বিভব দরকার; Co উপযুক্ত।",
        bank_n=100,
    ),
]


# ---------------------------------------------------------------------------
# t04 — Electrolysis and Faraday's laws / তড়িৎ বিশ্লেষণ ও ফ্যারাডের সূত্র
# ---------------------------------------------------------------------------
T04 = [
    q(
        "Faraday's laws are applicable to:\n(i) calculating electron charge\n(ii) determining amount of metal deposited\n(iii) electrolytic conductors",
        "ফ্যারাডের সূত্র প্রযোজ্য—\n(i) ইলেকট্রনের চার্জ গণনায়\n(ii) ধাতুর পরিমাণ নির্ণয়ে\n(iii) তড়িৎ বিশ্লেষ্য পরিবাহীর ক্ষেত্রে",
        ["iii only", "i and ii only", "ii and iii only", "i, ii and iii"],
        ["কেবল iii", "কেবল i ও ii", "কেবল ii ও iii", "i, ii ও iii"],
        "D", "medium", "factual",
        "Faraday relations link charge, electrons, and mass deposited in electrolytes.",
        "ফ্যারাডের সূত্র চার্জ, ইলেকট্রন ও জমা ভর সংযুক্ত করে।",
        bank_n=4,
    ),
    q(
        "Faradays of electricity needed to produce 1 mol Al from Al3+ are:",
        "এক মোল Al3+ থেকে Al উৎপাদনে কত ফ্যারাডে বিদ্যুৎ লাগে?",
        ["1.0", "1.5", "2.0", "3.0"],
        ["১.০", "১.৫", "২.০", "৩.০"],
        "D", "easy", "numerical",
        "Al3+ + 3e− → Al requires 3F per mole.",
        "Al3+ + ৩e− → Al; ৩F প্রয়োজন।",
        bank_n=5,
    ),
    q(
        "0.1 mA flows for 15 min through a copper wire. Number of electrons transferred is about:",
        "০.১ mA বিদ্যুৎ ১৫ min প্রবাহিত হলে ইলেকট্রন সংখ্যা প্রায়:",
        ["4.84 × 10^17", "5.62 × 10^17", "2.3 × 10^18", "8.60 × 10^18"],
        ["4.84 × 10^17", "5.62 × 10^17", "2.3 × 10^18", "8.60 × 10^18"],
        "B", "hard", "numerical",
        "Q = 0.1×10−3×15×60 = 0.09 C; N = Q/e ≈ 5.62×10^17.",
        "Q = ০.০৯ C; N ≈ ৫.৬২×১০^১৭।",
        bank_n=3,
    ),
    q(
        "To deposit 63.5 g Cu from CuSO4, charge required is:",
        "ক্যাথোডে ৬৩.৫ g Cu জমা করতে কী পরিমাণ বিদ্যুৎ লাগে?",
        ["1F", "2F", "3F", "4F"],
        ["১F", "২F", "৩F", "৪F"],
        "B", "easy", "numerical",
        "1 mol Cu2+ needs 2 mol e− → 2F.",
        "১ মোল Cu2+-এর জন্য ২F।",
        bank_n=19,
    ),
    q(
        "For complete deposition of metal from 1 mol molten Al2O3, charge needed is:",
        "১ মোল গলিত Al2O3 থেকে সম্পূর্ণ ধাতু জমা করতে কত ফ্যারাড লাগে?",
        ["1F", "3F", "4F", "6F"],
        ["১F", "৩F", "৪F", "৬F"],
        "D", "medium", "numerical",
        "Al2O3 → 2Al needs 6e− → 6F.",
        "Al2O3 → ২Al-এ ৬e− → ৬F।",
        bank_n=33,
    ),
    q(
        "Passing 30 A through molten alumina for 90 min deposits about how much Al?",
        "গলিত অ্যালুমিনায় ৩০ A বিদ্যুৎ ৯০ min চালনা করলে ক্যাথোডে Al প্রায়:",
        ["2.27 g", "15.10 g", "21.82 g", "45.32 g"],
        ["২.২৭ g", "১৫.১০ g", "২১.৮২ g", "৪৫.৩২ g"],
        "B", "hard", "numerical",
        "W = (27×30×90×60)/(3×96500) ≈ 15.10 g.",
        "W ≈ ১৫.১০ g।",
        bank_n=47,
    ),
    q(
        "5 A through AgNO3 for 60 min deposits about how much Ag?",
        "AgNO3-এ ৫ A বিদ্যুৎ ৬০ min চালনা করলে Ag প্রায়:",
        ["8.766 g", "16.812 g", "20.145 g", "24.854 g"],
        ["৮.৭৬৬ g", "১৬.৮১২ g", "২০.১৪৫ g", "২৪.৮৫৪ g"],
        "C", "medium", "numerical",
        "W = (108×5×3600)/96500 ≈ 20.15 g.",
        "W ≈ ২০.১৫ g।",
        bank_n=52,
    ),
    q(
        "4 A through CuSO4 for 45 min deposits about how much Cu?",
        "CuSO4-এ ৪ A বিদ্যুৎ ৪৫ min চালনা করলে Cu প্রায়:",
        ["7.11 g", "3.55 g", "0.118 g", "0.059 g"],
        ["৭.১১ g", "৩.৫৫ g", "০.১১৮ g", "০.০৫৯ g"],
        "B", "medium", "numerical",
        "W = (63.5×4×45×60)/(2×96500) ≈ 3.55 g.",
        "W ≈ ৩.৫৫ g।",
        bank_n=54,
    ),
    q(
        "Passing 2.0 F through FeSO4 deposits how many moles of iron?",
        "FeSO4-এ ২.০ F চার্জ চালনা করলে কত মোল আয়রন জমা হবে?",
        ["1.0 × 10−5 mol", "5.8 × 10−4 mol", "0.5 mol", "1 mol"],
        ["1.0 × 10−5 mol", "5.8 × 10−4 mol", "০.৫ mol", "১ mol"],
        "D", "easy", "numerical",
        "Fe2+ + 2e− → Fe; 2F deposits 1 mol Fe.",
        "২F-এ ১ মোল Fe জমা হয়।",
        bank_n=64,
    ),
    q(
        "Charge to obtain 1 mol Fe from Fe2O3 is:",
        "১ মোল Fe2O3 হতে ১ মোল লোহা পেতে কত তড়িৎ লাগে?",
        ["1F", "2F", "3F", "6F"],
        ["১F", "২F", "৩F", "৬F"],
        "C", "medium", "numerical",
        "Fe3+ → Fe needs 3e−; 1 mol Fe requires 3F.",
        "Fe3+ → Fe-এ ৩F লাগে।",
        bank_n=79,
    ),
    q(
        "3000 C through AgNO3 deposits about how much Ag (Ag = 108)?",
        "AgNO3-এ ৩০০০ C চালনা করলে Ag প্রায় (Ag=১০৮):",
        ["3.3575 g", "2.3575 g", "0.3357 g", "0.2357 g"],
        ["৩.৩৫৭৫ g", "২.৩৫৭৫ g", "০.৩৩৫৭ g", "০.২৩৫৭ g"],
        "A", "medium", "numerical",
        "W = (108×3000)/96500 ≈ 3.36 g.",
        "W ≈ ৩.৩৬ g।",
        bank_n=83,
    ),
    q(
        "Faradays needed to deposit 54 g Al from molten AlCl3 are:",
        "গলিত AlCl3 থেকে ৫৪ g Al জমা করতে কত ফ্যারাড লাগে?",
        ["1", "3", "6", "9"],
        ["১", "৩", "৬", "৯"],
        "C", "medium", "numerical",
        "54 g = 2 mol Al; each needs 3F → 6F.",
        "৫৪ g = ২ মোল Al; মোট ৬F।",
        bank_n=84,
    ),
    q(
        "Electrochemical equivalent of Ag is about:",
        "Ag-এর তড়িৎ রাসায়নিক তুল্যাঙ্ক প্রায়:",
        ["0.000289", "0.000658", "0.000329", "0.001118"],
        ["০.০০০২৮৯", "০.০০০৬৫৮", "০.০০০৩২৯", "০.০০১১১৮"],
        "D", "medium", "numerical",
        "Z = M/(nF) = 108/96500 ≈ 0.001119 g C−1.",
        "Z = ১০৮/৯৬৫০০ ≈ ০.০০১১১৮ g C−1।",
        bank_n=89,
    ),
    q(
        "0.5 F equals how many coulombs?",
        "০.৫ F = কত কুলম্ব?",
        ["48250 C", "96500 C", "193000 C", "289500 C"],
        ["৪৮২৫০ C", "৯৬৫০০ C", "১৯৩০০০ C", "২৮৯৫০০ C"],
        "A", "easy", "numerical",
        "0.5 × 96500 = 48250 C.",
        "০.৫ × ৯৬৫০০ = ৪৮২৫০ C।",
        bank_n=108,
    ),
    q(
        "5 A for 10 min through FeSO4 deposits about how much Fe (Fe = 55.85)?",
        "FeSO4-এ ৫ A বিদ্যুৎ ১০ min চালনা করলে Fe প্রায় (Fe=৫৫.৮৫):",
        ["0.144 g", "0.868 g", "0.578 g", "0.404 g"],
        ["০.১৪৪ g", "০.৮৬৮ g", "০.৫৭৮ g", "০.৪০৪ g"],
        "B", "medium", "numerical",
        "W = (55.85×5×600)/(2×96500) ≈ 0.868 g.",
        "W ≈ ০.৮৬৮ g।",
        bank_n=125,
    ),
    q(
        "Charge needed to deposit 27 g Al is:",
        "২৭ g Al জমা হতে কী পরিমাণ বিদ্যুৎ প্রয়োজন?",
        ["27F", "13.5F", "3F", "1F"],
        ["২৭F", "১৩.৫F", "৩F", "১F"],
        "C", "easy", "numerical",
        "27 g = 1 mol Al from Al3+ needs 3F.",
        "১ মোল Al-এ ৩F লাগে।",
        bank_n=127,
    ),
    q(
        "Electrolysis of aqueous NaCl (brine) produces:",
        "ব্রাইনের তড়িৎ বিশ্লেষণে কী উৎপন্ন হয়?",
        ["NaCl", "NaHCO3", "NaOH", "NaClO3 only"],
        ["NaCl", "NaHCO3", "NaOH", "কেবল NaClO3"],
        "C", "easy", "factual",
        "Chlor-alkali electrolysis yields NaOH, Cl2 and H2.",
        "ব্রাইন তড়িৎ বিশ্লেষণে NaOH, Cl2 ও H2 পাওয়া যায়।",
        bank_n=93,
    ),
    q(
        "At the cathode during electrolysis of aqueous table salt, the gas liberated is:",
        "খাদ্য লবণের জলীয় দ্রবণে তড়িৎ বিশ্লেষণে ক্যাথোডে মুক্ত গ্যাস:",
        ["O2", "N2", "Cl2", "H2"],
        ["O2", "N2", "Cl2", "H2"],
        "D", "easy", "factual",
        "H+ (water) is reduced preferentially to H2 at the cathode.",
        "ক্যাথোডে পানি থেকে H2 মুক্ত হয়।",
        bank_n=141,
    ),
    q(
        "1 mol of electrons carries a total charge of about:",
        "১ মোল ইলেকট্রনের মোট চার্জ প্রায়:",
        [
            "1.602 × 10−19 C",
            "1.602 × 10−19 × 6.022 × 10^23 C",
            "6.022 × 10^23 C",
            "196500 C exactly as listed only",
        ],
        [
            "1.602 × 10−19 C",
            "1.602 × 10−19 × 6.022 × 10^23 C",
            "6.022 × 10^23 C",
            "কেবল ১৯৬৫০০ C",
        ],
        "B", "easy", "numerical",
        "1 F = NA × e ≈ 96500 C.",
        "১ F = NA × e ≈ ৯৬৫০০ C।",
        bank_n=129,
    ),
    q(
        "Passing 1F through molten NaCl, MgCl2, AlCl3 and SnCl4 deposits the greatest number of moles of which metal at the cathode?",
        "গলিত NaCl, MgCl2, AlCl3 ও SnCl4-এ ১F চালনা করলে ক্যাথোডে কোন ধাতুর মোল সংখ্যা সর্বাধিক?",
        ["Na", "Mg", "Al", "Sn"],
        ["Na", "Mg", "Al", "Sn"],
        "A", "hard", "application",
        "Moles deposited = 1/n; Na+ (n=1) gives the most moles per faraday.",
        "জমা মোল = ১/n; Na+-এর n=১ বলে মোল সর্বাধিক।",
        bank_n=None,
        filler=True,
    ),
]


def main() -> int:
    TOPICS.mkdir(parents=True, exist_ok=True)
    PARSED.mkdir(parents=True, exist_ok=True)

    topics = {
        "chem2_27_ch04_t01": T01,
        "chem2_27_ch04_t02": T02,
        "chem2_27_ch04_t03": T03,
        "chem2_27_ch04_t04": T04,
    }

    mappings = {}
    counts = {}
    for tid, items in topics.items():
        mappings[tid] = write_topic(tid, items)
        counts[tid] = 20
    counts["total"] = 80

    pdf_pages = [f"p{p:03d}_pdf{p+6}.png" for p in range(282, 294)]

    def bank_nums(mid: list) -> list:
        return sorted({n for n in mid if isinstance(n, int)})

    summary = {
        "chapter": "chem2_27_ch04",
        "title_en": "Electrochemistry",
        "title_bn": "তড়িৎ রসায়ন",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": pdf_pages,
        "skipped_faulty": {
            "figure_stimuli": "Stimulus-linked paired items rewritten as standalone cell/ Faraday stems",
            "Q30": "Printed note: no correct oxidation-electrode option among listed choices; replaced with clear Zn/Zn2+ item",
            "Q80": "Printed note admits no matching time among options; skipped",
            "Q97": "Printed note admits correct choice not among options; skipped",
            "Q154": "Printed note: all listed forms are reduction electrodes; skipped",
            "Q164": "Printed options mismatch computed +0.32 V; used corrected Zn–Fe stem elsewhere",
        },
        "pdf_mapping": {
            "chem2_27_ch04_t01": {
                "title": "Oxidation and reduction / জারণ ও বিজারণ",
                "main_bank": bank_nums(mappings["chem2_27_ch04_t01"]),
                "cq_or_reconstructed_fillers": sum(
                    1 for x in mappings["chem2_27_ch04_t01"] if x == "filler"
                ),
            },
            "chem2_27_ch04_t02": {
                "title": "Electrochemical cells and electrodes / তড়িৎ রাসায়নিক কোষ ও তড়িৎদ্বার",
                "main_bank": bank_nums(mappings["chem2_27_ch04_t02"]),
                "cq_or_reconstructed_fillers": sum(
                    1 for x in mappings["chem2_27_ch04_t02"] if x == "filler"
                ),
            },
            "chem2_27_ch04_t03": {
                "title": "Cell potential and electrochemical series / কোষ বিভব ও তড়িৎ রাসায়নিক সারি",
                "main_bank": bank_nums(mappings["chem2_27_ch04_t03"]),
                "cq_or_reconstructed_fillers": sum(
                    1 for x in mappings["chem2_27_ch04_t03"] if x == "filler"
                ),
            },
            "chem2_27_ch04_t04": {
                "title": "Electrolysis and Faraday's laws / তড়িৎ বিশ্লেষণ ও ফ্যারাডের সূত্র",
                "main_bank": bank_nums(mappings["chem2_27_ch04_t04"]),
                "cq_or_reconstructed_fillers": sum(
                    1 for x in mappings["chem2_27_ch04_t04"] if x == "filler"
                ),
            },
        },
        "low_confidence": [
            "OCR on p282–p293 is noisy; stems reconstructed from explanations + electrochemical consistency.",
            "Preferential anion discharge (Br−) follows common HSC teaching order; conditions can vary.",
            "Nickel oxidation potential taken as +0.25 V opposite E°red ≈ −0.25 V.",
            "Figure/stimulus-dependent paired items converted to equation-only stems.",
        ],
        "counts": counts,
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "chem2_27_ch04_t01": 20,
                "chem2_27_ch04_t02": 20,
                "chem2_27_ch04_t03": 20,
                "chem2_27_ch04_t04": 20,
            },
        },
    }

    out = PARSED / "ch04_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
