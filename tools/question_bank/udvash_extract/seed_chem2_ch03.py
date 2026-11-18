#!/usr/bin/env python3
"""Seed Chemistry 2nd Paper Ch3 (Quantitative Chemistry) bilingual MCQs.

Curated from Udvash HSC Question Bank 2026 printed pages 235–247 (PDF 241–253).
Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: chem2_27_ch03_t01..t04.
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
    "chemistry p2 ch03; curated bilingual"
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
# t01 — Mole concept and stoichiometry
# ---------------------------------------------------------------------------
T01 = [
    q(
        "Mass of Na2CO3 in 1 millimole is:",
        "এক মিলিমোল Na2CO3-এ কত গ্রাম থাকে?",
        ["106 g", "10.6 g", "1.06 g", "0.106 g"],
        ["106 গ্রাম", "10.6 গ্রাম", "1.06 গ্রাম", "0.106 গ্রাম"],
        "D", "easy", "numerical",
        "M(Na2CO3)=106 g mol−1; 1 mmol = 106×10−3 g = 0.106 g.",
        "M(Na2CO3)=১০৬ g mol−1; ১ মিলিমোল = ১০৬×১০−৩ g = ০.১০৬ g।",
        bank_n=1,
    ),
    q(
        "How many molecules are present in 6.0 g of water?",
        "৬.০ গ্রাম পানিতে কতটি অণু বিদ্যমান?",
        ["2.01 × 10^22", "3.01 × 10^22", "2.01 × 10^23", "3.02 × 10^23"],
        ["2.01 × 10^22", "3.01 × 10^22", "2.01 × 10^23", "3.02 × 10^23"],
        "C", "easy", "numerical",
        "n = 6/18 = 1/3 mol; molecules = (1/3)×6.023×10^23 ≈ 2.01×10^23.",
        "n = ৬/১৮ = ১/৩ mol; অণু সংখ্যা ≈ ২.০১×১০^২৩।",
        bank_n=5,
    ),
    q(
        "At SATP, the volume of 2 mol O2 gas is approximately:",
        "SATP-তে ২ মোল O2 গ্যাসের আয়তন প্রায় কত?",
        ["22.789 L", "24.789 L", "45.578 L", "49.578 L"],
        ["22.789 L", "24.789 L", "45.578 L", "49.578 L"],
        "D", "easy", "numerical",
        "SATP molar volume ≈ 24.789 L; 2 mol → 49.578 L.",
        "SATP-তে ১ মোল ≈ ২৪.৭৮৯ L; ২ মোল → ৪৯.৫৭৮ L।",
        bank_n=59,
    ),
    q(
        "Number of oxygen atoms in 1.80 × 10^−3 g of glucose (C6H12O6) is about:",
        "১.৮০ × ১০^−৩ g গ্লুকোজ অণুতে অক্সিজেন পরমাণুর সংখ্যা প্রায়:",
        ["6.02 × 10^18", "3.61 × 10^19", "3.61 × 10^29", "6.02 × 10^29"],
        ["6.02 × 10^18", "3.61 × 10^19", "3.61 × 10^29", "6.02 × 10^29"],
        "B", "medium", "numerical",
        "n = 10^−5 mol; O atoms = 6 × 6.023×10^23 × 10^−5 ≈ 3.61×10^19.",
        "n = ১০^−৫ mol; O পরমাণু ≈ ৩.৬১×১০^১৯।",
        bank_n=71,
    ),
    q(
        "At STP, 3.2 g of a gas occupies 2.24 L. The gas may be:",
        "STP-তে ৩.২ g গ্যাস ২.২৪ L আয়তন দখল করলে গ্যাসটি হতে পারে:",
        ["H2", "CO2", "N2", "O2"],
        ["H2", "CO2", "N2", "O2"],
        "D", "medium", "numerical",
        "M = (3.2 × 22.4)/2.24 = 32 g mol−1 → O2.",
        "M = (৩.২ × ২২.৪)/২.২৪ = ৩২ → O2।",
        bank_n=110,
    ),
    q(
        "Number of oxygen atoms in 0.5 mol of CO2 is:",
        "অর্ধ মোল CO2 গ্যাসে অক্সিজেন পরমাণুর সংখ্যা কত?",
        ["1 atom", "2 atoms", "3.01 × 10^23", "6.023 × 10^23"],
        ["১টি", "২টি", "3.01 × 10^23", "6.023 × 10^23"],
        "D", "easy", "numerical",
        "0.5 mol CO2 contains 1 mol O atoms → NA = 6.023×10^23.",
        "০.৫ mol CO2-এ ১ mol O পরমাণু → ৬.০২৩×১০^২৩।",
        bank_n=117,
    ),
    q(
        "Approximate mass of one oxygen atom is:",
        "একটি অক্সিজেন পরমাণুর ভর প্রায় কত?",
        ["2.66 × 10^−23 g", "3.76 × 10^−23 g", "1.33 × 10^−23 g", "1.88 × 10^−24 g"],
        ["2.66 × 10^−23 g", "3.76 × 10^−23 g", "1.33 × 10^−23 g", "1.88 × 10^−24 g"],
        "A", "medium", "numerical",
        "m = 16 / NA ≈ 2.66 × 10^−23 g.",
        "m = ১৬ / NA ≈ ২.৬৬ × ১০^−২৩ g।",
        bank_n=125,
    ),
    q(
        "At STP, number of hydrogen atoms in 9 g of water is:",
        "প্রমাণ অবস্থায় ৯ g পানিতে হাইড্রোজেন পরমাণুর সংখ্যা কত?",
        ["6.023 × 10^23", "3.0115 × 10^23", "6.023 × 10^21", "12.046 × 10^23"],
        ["6.023 × 10^23", "3.0115 × 10^23", "6.023 × 10^21", "12.046 × 10^23"],
        "A", "easy", "numerical",
        "9 g H2O = 0.5 mol; H atoms = 0.5 × 2 × NA = NA.",
        "৯ g পানি = ০.৫ mol; H পরমাণু = NA।",
        bank_n=139,
    ),
    q(
        "Number of hydrogen atoms in 1.8 kg of water is:",
        "১.৮ kg পানিতে হাইড্রোজেন পরমাণুর সংখ্যা কত?",
        ["6.023 × 10^23", "12.046 × 10^23", "6.023 × 10^25", "12.046 × 10^25"],
        ["6.023 × 10^23", "12.046 × 10^23", "6.023 × 10^25", "12.046 × 10^25"],
        "D", "medium", "numerical",
        "1.8 kg = 100 mol H2O; H atoms = 200 × NA = 12.046 × 10^25.",
        "১.৮ kg = ১০০ mol; H পরমাণু = ১২.০৪৬ × ১০^২৫।",
        bank_n=152,
    ),
    q(
        "Mass of Na2CO3 in 500 mL of 0.05 M solution is:",
        "৫০০ mL ০.০৫ M Na2CO3 দ্রবণে কত গ্রাম Na2CO3 থাকে?",
        ["2.65 g", "5.30 g", "6.30 g", "10.60 g"],
        ["2.65 g", "5.30 g", "6.30 g", "10.60 g"],
        "A", "easy", "numerical",
        "w = S×V×M/1000 = 0.05×500×106/1000 = 2.65 g.",
        "w = ০.০৫×৫০০×১০৬/১০০০ = ২.৬৫ g।",
        bank_n=58,
    ),
    q(
        "At STP, volume of CO2 from reaction of 2 mol CaCO3 with excess HCl is:",
        "STP-তে ২ mol CaCO3 ও অতিরিক্ত HCl বিক্রিয়ায় উৎপন্ন CO2-এর আয়তন কত?",
        ["11.2 L", "22.4 L", "33.6 L", "44.8 L"],
        ["11.2 L", "22.4 L", "33.6 L", "44.8 L"],
        "D", "easy", "numerical",
        "CaCO3 → CO2 (1:1); 2 mol CO2 at STP = 44.8 L.",
        "১:১ অনুপাতে ২ mol CO2 → STP-তে ৪৪.৮ L।",
        bank_n=92,
    ),
    q(
        "Mass of Na2CO3 needed to prepare 100 mL of demimolar solution is:",
        "১০০ mL সেমিমোলার দ্রবণ তৈরিতে কত গ্রাম Na2CO3 লাগে?",
        ["0.53 g", "1.06 g", "5.30 g", "10.60 g"],
        ["0.53 g", "1.06 g", "5.30 g", "10.60 g"],
        "C", "easy", "numerical",
        "Demimolar = 0.5 M; w = 0.5×100×106/1000 = 5.3 g.",
        "সেমিমোলার = ০.৫ M; w = ৫.৩ g।",
        bank_n=119,
    ),
    q(
        "Mass of Na2CO3 in 500 mL of decimolar solution is:",
        "৫০০ mL ডেসিমোলার Na2CO3 দ্রবণে কত গ্রাম থাকে?",
        ["2.65 g", "5.30 g", "6.30 g", "10.60 g"],
        ["2.65 g", "5.30 g", "6.30 g", "10.60 g"],
        "B", "easy", "numerical",
        "Decimolar = 0.1 M; w = 0.1×500×106/1000 = 5.30 g.",
        "ডেসিমোলার = ০.১ M; w = ৫.৩০ g।",
        bank_n=122,
    ),
    q(
        "12.0 g limestone gives 2.24 L CO2 at SATP. Approximate % purity of CaCO3 is:",
        "১২.০ g চুনাপাথর থেকে SATP-তে ২.২৪ L CO2 পাওয়া গেলে CaCO3-এর শতকরা পরিমাণ প্রায়:",
        ["85.33%", "43.26%", "75.30%", "73.50%"],
        ["৮৫.৩৩%", "৪৩.২৬%", "৭৫.৩০%", "৭৩.৫০%"],
        "C", "hard", "numerical",
        "SATP: 24.789 L CO2 from 100 g CaCO3; 2.24 L ← ~9.04 g; purity ≈ 75.3%.",
        "SATP অনুপাতে বিশুদ্ধ CaCO3 ≈ ৯.০৪ g → শতকরা ≈ ৭৫.৩%।",
        bank_n=46,
    ),
    q(
        "Mass of CaCO3 that thermally decomposes to give 22 g CO2 is:",
        "তাপীয় বিয়োজনে ২২ g CO2 দিতে কত গ্রাম CaCO3 লাগে?",
        ["11 g", "22 g", "44 g", "50 g"],
        ["11 g", "22 g", "44 g", "50 g"],
        "D", "medium", "numerical",
        "CaCO3 → CO2; 100 g → 44 g CO2, so 22 g CO2 needs 50 g CaCO3.",
        "১০০ g CaCO3 → ৪৪ g CO2; ২২ g CO2-এর জন্য ৫০ g।",
        bank_n=88,
    ),
    q(
        "In 2NH4Cl + CaO → 2NH3 + CaCl2 + H2O, mass of NH4Cl needed for 44.8 L NH3 at STP is:",
        "STP-তে ৪৪.৮ L NH3 প্রস্তুত করতে কত গ্রাম NH4Cl লাগে?",
        ["53.5 g", "107 g", "14 g", "7 g"],
        ["৫৩.৫ g", "১০৭ g", "১৪ g", "৭ g"],
        "B", "medium", "numerical",
        "2 mol NH3 = 44.8 L needs 2 mol NH4Cl = 107 g.",
        "৪৪.৮ L = ২ mol NH3 → ২ mol NH4Cl = ১০৭ g।",
        bank_n=56,
    ),
    q(
        "Mole fraction of water in 10% (w/w) aqueous Na2CO3 is approximately:",
        "১০% (w/w) Na2CO3 জলীয় দ্রবণে পানির মোল ভগ্নাংশ প্রায়:",
        ["0.0185", "0.98", "0.9815", "0.9833"],
        ["০.০১৮৫", "০.৯৮", "০.৯৮১৫", "০.৯৮৩৩"],
        "C", "hard", "numerical",
        "100 g solution: 10 g Na2CO3 + 90 g H2O → χ(H2O) ≈ 0.9815.",
        "১০০ g-এ ৯০ g পানি → χ(H2O) ≈ ০.৯৮১৫।",
        bank_n=76,
    ),
    q(
        "Which quantity is independent of temperature?",
        "দ্রবণের কোন এককটি তাপমাত্রার উপর নির্ভরশীল নয়?",
        ["molality", "molarity", "normality", "ppm (volume-based)"],
        ["মোলালিটি", "মোলারিটি", "নরমালিটি", "পিপিএম (আয়তনভিত্তিক)"],
        "A", "easy", "conceptual",
        "Molality uses mass of solvent, so it does not change with T.",
        "মোলালিটি দ্রাবকের ভরভিত্তিক; তাপমাত্রায় পরিবর্তন হয় না।",
        bank_n=70,
    ),
    q(
        "Unit of molarity is:",
        "দ্রবণের মোলারিটির একক হচ্ছে:",
        ["g/L", "mol/L", "mol/kg", "N/V"],
        ["g/L", "mol/L", "mol/kg", "N/V"],
        "B", "easy", "factual",
        "Molarity = moles of solute per litre of solution.",
        "মোলারিটি = প্রতি লিটার দ্রবণে দ্রবের মোল সংখ্যা।",
        bank_n=126,
    ),
    q(
        "One mole of any substance contains Avogadro’s number of—",
        "যেকোনো পদার্থের এক মোলে অ্যাভোগাড্রো সংখ্যক থাকে—",
        ["only molecules", "particles of the specified entity (atoms/molecules/ions)", "only atoms", "only electrons"],
        ["শুধু অণু", "নির্দিষ্ট এককের কণা (পরমাণু/অণু/আয়ন)", "শুধু পরমাণু", "শুধু ইলেকট্রন"],
        "B", "easy", "conceptual",
        "1 mol means NA entities of whatever is specified.",
        "১ মোল মানে নির্দিষ্ট সত্তার NA সংখ্যক কণা।",
        filler=True,
    ),
]

# ---------------------------------------------------------------------------
# t02 — Concentration of solutions
# ---------------------------------------------------------------------------
T02 = [
    q(
        "Molarity of water containing 877.5 ppm NaCl is approximately:",
        "৮৭৭.৫ ppm NaCl বিশিষ্ট পানির মোলারিটি প্রায়:",
        ["0.01 M", "0.05 M", "0.015 M", "0.025 M"],
        ["০.০১ M", "০.০৫ M", "০.০১৫ M", "০.০২৫ M"],
        "C", "medium", "numerical",
        "877.5 mg/L ÷ 58.5 g mol−1 ≈ 0.015 mol L−1.",
        "৮৭৭.৫ mg/L ÷ ৫৮.৫ ≈ ০.০১৫ M।",
        bank_n=2,
    ),
    q(
        "2.5% Na2CO3 solution in ppm is:",
        "২.৫% Na2CO3 দ্রবণের ঘনমাত্রা ppm এককে কত?",
        ["250", "2500", "25000", "250000"],
        ["২৫০", "২৫০০", "২৫০০০", "২৫০০০০"],
        "C", "easy", "numerical",
        "2.5% (w/v) ≈ 25 g/L = 25000 mg/L = 25000 ppm.",
        "২.৫% ≈ ২৫ g/L = ২৫০০০ ppm।",
        bank_n=7,
    ),
    q(
        "Concentration of demimolar caustic soda in ppm is:",
        "সেমিমোলার কস্টিক সোডা দ্রবণের ঘনমাত্রা ppm এককে কত?",
        ["200", "1000", "2000", "20000"],
        ["২০০", "১০০০", "২০০০", "২০০০০"],
        "D", "medium", "numerical",
        "0.5 M NaOH = 20 g/L = 20000 mg/L = 20000 ppm.",
        "০.৫ M NaOH = ২০ g/L = ২০০০০ ppm।",
        bank_n=17,
    ),
    q(
        "Which represents the same amount of solute as 100 mL of 0.3 M Na2CO3?",
        "১০০ mL ০.৩ M Na2CO3 দ্রবণের সমপরিমাণ দ্রব কোনটি বোঝায়?",
        ["10 mL of 0.3 M Na2CO3", "1000 mL of 0.003 M Na2CO3", "30 mL of 1 M Na2CO3", "100 mL of 3 M Na2CO3"],
        ["১০ mL ০.৩ M", "১০০০ mL ০.০০৩ M", "৩০ mL ১ M", "১০০ mL ৩ M"],
        "C", "medium", "numerical",
        "Moles = 0.03; also given by 30 mL of 1 M.",
        "মোল সংখ্যা = ০.০৩ = ৩০ mL × ১ M।",
        bank_n=21,
    ),
    q(
        "Mixing 5 mL of 0.002 M HCl with 5 mL of 0.001 M HCl gives ppm concentration of:",
        "৫ mL ০.০০২ M ও ৫ mL ০.০০১ M HCl মিশ্রণের ঘনমাত্রা ppm-এ:",
        ["32.75", "41.25", "54.75", "63.25"],
        ["৩২.৭৫", "৪১.২৫", "৫৪.৭৫", "৬৩.২৫"],
        "C", "hard", "numerical",
        "Final S = 0.0015 M; ppm = 0.0015×36.5×1000 = 54.75.",
        "মিশ্রণ S = ০.০০১৫ M → ৫৪.৭৫ ppm।",
        bank_n=22,
    ),
    q(
        "Molarity of 500 ppm H2SO4 solution is about:",
        "৫০০ ppm H2SO4 দ্রবণের মোলার ঘনমাত্রা প্রায়:",
        ["0.00205 M", "0.0051 M", "0.00801 M", "0.0102 M"],
        ["০.০০২০৫ M", "০.০০৫১ M", "০.০০৮০১ M", "০.০১০২ M"],
        "B", "medium", "numerical",
        "500 mg/L = 0.5 g/L; M = 0.5/98 ≈ 0.0051 M.",
        "০.৫ g/L ÷ ৯৮ ≈ ০.০০৫১ M।",
        bank_n=30,
    ),
    q(
        "From 250 mL of demimolar solution, volume of molar solution obtainable is:",
        "২৫০ mL সেমিমোলার দ্রবণ থেকে কত আয়তনের মোলার দ্রবণ পাওয়া যায়?",
        ["125 mL", "250 mL", "400 mL", "525 mL"],
        ["১২৫ mL", "২৫০ mL", "৪০০ mL", "৫২৫ mL"],
        "A", "easy", "numerical",
        "S1V1 = S2V2 → 0.5×250 = 1×V2 → V2 = 125 mL.",
        "০.৫×২৫০ = ১×V → V = ১২৫ mL।",
        bank_n=35,
    ),
    q(
        "If atmospheric CO2 is 0.036% (v/v), its value in ppm is:",
        "বাতাসে CO2 ০.০৩৬% হলে ppm এককে মান কত?",
        ["36", "360", "3600", "36 × 10^6"],
        ["৩৬", "৩৬০", "৩৬০০", "৩৬ × ১০^৬"],
        "B", "easy", "numerical",
        "ppm = % × 10^4 = 0.036 × 10^4 = 360.",
        "ppm = % × ১০^৪ = ৩৬০।",
        bank_n=43,
    ),
    q(
        "In 0.5 mol L−1 H2SO4, concentration of H+ in ppm is:",
        "০.৫ mol L−1 H2SO4 দ্রবণে H+-এর ঘনমাত্রা কত ppm?",
        ["10000", "1000", "100", "10"],
        ["১০০০০", "১০০০", "১০০", "১০"],
        "B", "medium", "numerical",
        "[H+] = 1.0 M = 1 g L−1 = 1000 mg L−1 = 1000 ppm.",
        "[H+] = ১.০ M → ১০০০ ppm।",
        bank_n=55,
    ),
    q(
        "ppm concentration of 0.025 M Na2CO3 is:",
        "০.০২৫ M Na2CO3 দ্রবণের ppm ঘনমাত্রা কত?",
        ["2.50 × 10^2", "2.65 × 10^3", "2.50 × 10^3", "2.65 × 10^2"],
        ["2.50 × 10^2", "2.65 × 10^3", "2.50 × 10^3", "2.65 × 10^2"],
        "B", "medium", "numerical",
        "0.025×106×1000 = 2650 ppm = 2.65×10^3.",
        "০.০২৫×১০৬×১০০০ = ২৬৫০ ppm।",
        bank_n=73,
    ),
    q(
        "ppm concentration of 0.15 M NaOH is:",
        "০.১৫ M NaOH দ্রবণের ppm ঘনমাত্রা কত?",
        ["4000", "5000", "6000", "7000"],
        ["৪০০০", "৫০০০", "৬০০০", "৭০০০"],
        "C", "easy", "numerical",
        "0.15×40×1000 = 6000 ppm.",
        "০.১৫×৪০×১০০০ = ৬০০০ ppm।",
        bank_n=79,
    ),
    q(
        "Molarity of 5% (w/v) Na2CO3 solution is about:",
        "৫% Na2CO3 দ্রবণের ঘনমাত্রা প্রায় কত মোলার?",
        ["0.047 M", "0.47 M", "0.74 M", "0.94 M"],
        ["০.০৪৭ M", "০.৪৭ M", "০.৭৪ M", "০.৯৪ M"],
        "B", "easy", "numerical",
        "50 g/L ÷ 106 ≈ 0.47 M.",
        "৫০ g/L ÷ ১০৬ ≈ ০.৪৭ M।",
        bank_n=86,
    ),
    q(
        "50 mL solution containing 4.9 g H2SO4 has concentration—\n(i) 1 M\n(ii) 98000 ppm\n(iii) 9.8 × 10^4 μg/mL\nWhich is correct?",
        "৫০ mL-এ ৪.৯ g H2SO4 থাকলে ঘনমাত্রা—\n(i) ১ M\n(ii) ৯৮০০০ ppm\n(iii) ৯.৮ × ১০^৪ μg/mL\nকোনটি সঠিক?",
        ["i and ii only", "ii and iii only", "i and iii only", "i, ii and iii"],
        ["কেবল i ও ii", "কেবল ii ও iii", "কেবল i ও iii", "i, ii ও iii"],
        "D", "medium", "numerical",
        "All three expressions equal 1 M / 98 g L−1.",
        "তিনটি প্রকাশই সমতুল্য।",
        bank_n=90,
    ),
    q(
        "Molarity of 12% (w/v) Na2CO3 is about:",
        "১২% (w/v) Na2CO3 দ্রবণের মোলারিটি প্রায়:",
        ["1.13 M", "1.31 M", "0.11 M", "1.20 M"],
        ["১.১৩ M", "১.৩১ M", "০.১১ M", "১.২০ M"],
        "A", "easy", "numerical",
        "120 g/L ÷ 106 ≈ 1.13 M.",
        "১২০ g/L ÷ ১০৬ ≈ ১.১৩ M।",
        bank_n=102,
    ),
    q(
        "Molarity of 20% (w/v) NaOH is about:",
        "২০% NaOH দ্রবণের মোলারিটি প্রায় কত?",
        ["5 M", "4 M", "3 M", "2 M"],
        ["৫ M", "৪ M", "৩ M", "২ M"],
        "A", "easy", "numerical",
        "200 g/L ÷ 40 = 5 M.",
        "২০০ g/L ÷ ৪০ = ৫ M।",
        bank_n=105,
    ),
    q(
        "Regarding ppm, which is correct?\n(i) 1 ppm = 1 g/m^3\n(ii) 1 ppm = 1 mg/L\n(iii) 1 ppm = 1 μg/L",
        "ppm সম্পর্কে কোনটি সঠিক?\n(i) ১ ppm = ১ g/m^3\n(ii) ১ ppm = ১ mg/L\n(iii) ১ ppm = ১ μg/L",
        ["i only", "i and ii", "ii and iii", "i, ii and iii"],
        ["কেবল i", "i ও ii", "ii ও iii", "i, ii ও iii"],
        "B", "medium", "factual",
        "For dilute aqueous solutions, 1 ppm ≈ 1 mg/L ≈ 1 g/m^3; not 1 μg/L.",
        "১ ppm ≈ ১ mg/L ≈ ১ g/m^3; μg/L নয়।",
        bank_n=106,
    ),
    q(
        "Percent (w/v) concentration of 0.98 M Na2CO3 is about:",
        "০.৯৮ M Na2CO3 দ্রবণের শতকরা ঘনমাত্রা প্রায়:",
        ["9.80%", "10.39%", "13.52%", "15.42%"],
        ["৯.৮০%", "১০.৩৯%", "১৩.৫২%", "১৫.৪২%"],
        "B", "medium", "numerical",
        "% = SM/10 = 0.98×106/10 ≈ 10.39.",
        "% = ০.৯৮×১০৬/১০ ≈ ১০.৩৯।",
        bank_n=133,
    ),
    q(
        "To convert 50 mL of 0.5 M NaOH into a decimolar solution, volume of water to add is:",
        "৫০ mL ০.৫ M NaOH-কে ডেসিমোলারে পরিণত করতে কত mL পানি যোগ করতে হবে?",
        ["250 mL", "200 mL", "150 mL", "100 mL"],
        ["২৫০ mL", "২০০ mL", "১৫০ mL", "১০০ mL"],
        "B", "medium", "numerical",
        "0.5×50 = 0.1×V → V = 250 mL total; water added = 200 mL.",
        "মোট আয়তন ২৫০ mL; যোগ্য পানি ২০০ mL।",
        bank_n=140,
    ),
    q(
        "Which concentration unit depends on temperature?",
        "কোনটি তাপমাত্রার উপর নির্ভরশীল?",
        ["molality", "mole fraction", "mass percent (w/w)", "molarity"],
        ["মোলালিটি", "মোল ভগ্নাংশ", "শতকরা ভর (w/w)", "মোলারিটি"],
        "D", "easy", "conceptual",
        "Molarity uses solution volume, which varies with temperature.",
        "মোলারিটি আয়তনভিত্তিক; তাপমাত্রায় পরিবর্তন হয়।",
        bank_n=155,
    ),
    q(
        "A demimolar solution means concentration of:",
        "সেমিমোলার দ্রবণ মানে ঘনমাত্রা:",
        ["0.1 M", "0.2 M", "0.5 M", "0.01 M"],
        ["০.১ M", "০.২ M", "০.৫ M", "০.০১ M"],
        "C", "easy", "factual",
        "Semi-/demi-molar = 0.5 mol L−1.",
        "সেমিমোলার = ০.৫ mol L−1।",
        bank_n=42,
    ),
]

# ---------------------------------------------------------------------------
# t03 — Titration and volumetric analysis
# ---------------------------------------------------------------------------
T03 = [
    q(
        "For the reaction Na2CO3 + 2HCl → 2NaCl + CO2 + H2O:\n(i) it is a neutralization\n(ii) phenolphthalein can be used\n(iii) at complete end point pH < 7\nWhich is correct?",
        "Na2CO3 + 2HCl বিক্রিয়াটি—\n(i) প্রশমন বিক্রিয়া\n(ii) ফেনলফথ্যালিন ব্যবহারযোগ্য\n(iii) পূর্ণ সমাপ্তি বিন্দুতে pH < ৭\nকোনটি সঠিক?",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "B", "medium", "conceptual",
        "Full titration to CO2/H2CO3 end point is acidic (pH < 7); phenolphthalein marks only half-neutralization.",
        "পূর্ণ প্রশমনে pH < ৭; ফেনলফথ্যালিন অর্ধ-প্রশমন নির্দেশ করে।",
        bank_n=3,
    ),
    q(
        "Suitable indicators for HCl–NaOH titration include—\n(i) methyl orange\n(ii) methyl red\n(iii) phenolphthalein",
        "HCl ও NaOH টাইট্রেশনে ব্যবহারযোগ্য নির্দেশক—\n(i) মিথাইল অরেঞ্জ\n(ii) মিথাইল রেড\n(iii) ফেনলফথ্যালিন",
        ["i only", "i and ii", "ii and iii", "i, ii and iii"],
        ["কেবল i", "i ও ii", "ii ও iii", "i, ii ও iii"],
        "D", "easy", "factual",
        "Strong acid–strong base: any common indicator works.",
        "তীব্র এসিড–তীব্র ক্ষারে সাধারণ নির্দেশকগুলোই চলে।",
        bank_n=8,
    ),
    q(
        "Which is a primary standard substance?",
        "কোনটি প্রাইমারি স্ট্যান্ডার্ড পদার্থ?",
        ["KMnO4", "Na2S2O3", "NaOH", "Na2C2O4"],
        ["KMnO4", "Na2S2O3", "NaOH", "Na2C2O4"],
        "D", "easy", "factual",
        "Sodium oxalate is a classical primary standard; KMnO4/NaOH/Na2S2O3 are secondary.",
        "সোডিয়াম অক্সালেট প্রাইমারি স্ট্যান্ডার্ড; অন্যগুলো সেকেন্ডারি।",
        bank_n=28,
    ),
    q(
        "Colour of methyl orange in acidic medium is:",
        "অম্লীয় মাধ্যমে মিথাইল অরেঞ্জের বর্ণ কী?",
        ["yellow", "blue", "pink", "red"],
        ["হলুদ", "নীল", "গোলাপি", "লাল"],
        "D", "easy", "factual",
        "Methyl orange is red in acid and yellow in base.",
        "মিথাইল অরেঞ্জ অম্লে লাল, ক্ষারে হলুদ।",
        bank_n=16,
    ),
    q(
        "In redox titration, KMnO4 solution—\n(i) is a primary standard\n(ii) acts as a self-indicator\n(iii) cannot be standardized using HCl medium\nWhich is correct?",
        "রিডক্স টাইট্রেশনে KMnO4 দ্রবণ—\n(i) প্রাইমারি স্ট্যান্ডার্ড\n(ii) স্বনির্দেশক\n(iii) HCl মাধ্যমে প্রমাণীকরণ যায় না\nকোনটি সঠিক?",
        ["i and ii", "ii and iii", "i and iii", "i, ii and iii"],
        ["i ও ii", "ii ও iii", "i ও iii", "i, ii ও iii"],
        "B", "medium", "conceptual",
        "KMnO4 is secondary but self-indicating; HCl interferes by being oxidized.",
        "KMnO4 সেকেন্ডারি কিন্তু স্বনির্দেশক; HCl মাধ্যম অনুপযোগী।",
        bank_n=18,
    ),
    q(
        "pH transition range of phenolphthalein is:",
        "ফেনলফথ্যালিনের বর্ণ পরিবর্তনের pH পরিসর কত?",
        ["3.0–4.0", "4.8–6.1", "8.2–10.0", "6.2–8.0"],
        ["৩.০–৪.০", "৪.৮–৬.১", "৮.২–১০.০", "৬.২–৮.০"],
        "C", "easy", "factual",
        "Phenolphthalein changes around pH 8.2–10.0.",
        "ফেনলফথ্যালিনের পরিসর প্রায় ৮.২–১০.০।",
        bank_n=25,
    ),
    q(
        "Which is a standard (primary-standard) solution among these?",
        "নিচের কোনটি প্রমাণ দ্রবণ?",
        ["approx. 1% NaOH", "approx. KMnO4 of unknown titre", "0.01 M K2Cr2O7", "approx. 2.0 M Na2CO3 without weighing"],
        ["প্রায় ১% NaOH", "অজানা টাইটারের KMnO4", "০.০১ M K2Cr2O7", "ওজন ছাড়া প্রায় ২.০ M Na2CO3"],
        "C", "medium", "factual",
        "K2Cr2O7 primary standard allows accurately known 0.01 M solution.",
        "K2Cr2O7 প্রাইমারি স্ট্যান্ডার্ড → সঠিক ০.০১ M প্রমাণ দ্রবণ।",
        bank_n=29,
    ),
    q(
        "Best indicator for weak acid–strong base titration is:",
        "মৃদু এসিড ও সবল ক্ষার টাইট্রেশনে উপযোগী নির্দেশক কোনটি?",
        ["bromophenol blue", "methyl red", "phenolphthalein", "methyl orange"],
        ["ব্রোমোফেনল ব্লু", "মিথাইল রেড", "ফেনলফথ্যালিন", "মিথাইল অরেঞ্জ"],
        "C", "easy", "factual",
        "End point is alkaline; phenolphthalein is suitable.",
        "সমাপ্তি বিন্দু ক্ষারীয় → ফেনলফথ্যালিন উপযুক্ত।",
        bank_n=36,
    ),
    q(
        "Suitable indicator for strong acid–weak base titration is:",
        "তীব্র এসিড ও মৃদু ক্ষার টাইট্রেশনে উপযুক্ত নির্দেশক কোনটি?",
        ["phenol red", "thymol blue", "phenolphthalein", "methyl orange"],
        ["ফেনল রেড", "থাইমল ব্লু", "ফেনলফথ্যালিন", "মিথাইল অরেঞ্জ"],
        "D", "easy", "factual",
        "End point is acidic; methyl orange fits.",
        "সমাপ্তি বিন্দু অম্লীয় → মিথাইল অরেঞ্জ।",
        bank_n=49,
    ),
    q(
        "Which indicator has pH range about 8–10?",
        "কোন নির্দেশকের pH সীমা প্রায় ৮–১০?",
        ["phenolphthalein", "methyl red", "methyl orange", "thymol blue (acid range)"],
        ["ফেনলফথ্যালিন", "মিথাইল রেড", "মিথাইল অরেঞ্জ", "থাইমল ব্লু (অম্লীয় সীমা)"],
        "A", "easy", "factual",
        "Phenolphthalein transitions near pH 8–10.",
        "ফেনলফথ্যালিনের পরিসর ~৮–১০।",
        bank_n=53,
    ),
    q(
        "pH transition range of methyl orange is:",
        "মিথাইল অরেঞ্জের বর্ণ পরিবর্তনের pH সীমা কোনটি?",
        ["3.1–4.4", "4.2–6.3", "5.0–8.0", "8.2–10.0"],
        ["৩.১–৪.৪", "৪.২–৬.৩", "৫.০–৮.০", "৮.২–১০.০"],
        "A", "easy", "factual",
        "Methyl orange changes roughly in the 3.1–4.4 region.",
        "মিথাইল অরেঞ্জ প্রায় ৩.১–৪.৪ পরিসরে বর্ণ বদলায়।",
        bank_n=60,
    ),
    q(
        "Suitable indicator for H2C2O4–NaOH titration is:",
        "H2C2O4 + NaOH বিক্রিয়ায় উপযুক্ত নির্দেশক কোনটি?",
        ["methyl red", "methyl orange", "thymol blue", "phenolphthalein"],
        ["মিথাইল রেড", "মিথাইল অরেঞ্জ", "থাইমল ব্লু", "ফেনলফথ্যালিন"],
        "D", "easy", "factual",
        "Weak acid–strong base → phenolphthalein.",
        "মৃদু এসিড–তীব্র ক্ষার → ফেনলফথ্যালিন।",
        bank_n=68,
    ),
    q(
        "Which can be stored accurately for a long time as a standard?",
        "কোন দ্রবণ দীর্ঘদিন সঠিকভাবে সংরক্ষণ করা যায়?",
        ["HCl", "NaOH", "K2Cr2O7", "H2SO4 (approximate)"],
        ["HCl", "NaOH", "K2Cr2O7", "আনুমানিক H2SO4"],
        "C", "easy", "factual",
        "K2Cr2O7 is a primary standard and stable in solution.",
        "K2Cr2O7 প্রাইমারি স্ট্যান্ডার্ড ও স্থিতিশীল।",
        bank_n=89,
    ),
    q(
        "In titration, the unknown solution being analysed is called the:",
        "টাইট্রেশনে অজানা দ্রবণকে বলা হয়:",
        ["titrant", "titrate (analyte)", "titre", "trimer"],
        ["টাইট্যান্ট", "টাইট্রেট (অ্যানালাইট)", "টাইটার", "ট্রাইমার"],
        "B", "easy", "factual",
        "Analyte/titrate is the solution of unknown concentration.",
        "অজানা ঘনমাত্রার দ্রবণই টাইট্রেট/অ্যানালাইট।",
        bank_n=91,
    ),
    q(
        "Which is a secondary standard substance?",
        "কোনটি সেকেন্ডারি স্ট্যান্ডার্ড পদার্থ?",
        ["sodium oxalate", "potassium dichromate", "caustic soda (NaOH)", "oxalic acid dihydrate"],
        ["সোডিয়াম অক্সালেট", "পটাশিয়াম ডাইক্রোমেট", "কস্টিক সোডা (NaOH)", "অক্সালিক এসিড ডাইহাইড্রেট"],
        "C", "easy", "factual",
        "NaOH absorbs CO2/moisture → secondary standard.",
        "NaOH CO2/আর্দ্রতা শোষণ করে → সেকেন্ডারি স্ট্যান্ডার্ড।",
        bank_n=95,
    ),
    q(
        "In HBr solution, phenolphthalein appears:",
        "HBr দ্রবণে ফেনলফথ্যালিন কী বর্ণ ধারণ করে?",
        ["red", "yellow", "pink", "colourless"],
        ["লাল", "হলুদ", "গোলাপি", "বর্ণহীন"],
        "D", "easy", "factual",
        "In acid, phenolphthalein is colourless.",
        "অম্লীয় মাধ্যমে ফেনলফথ্যালিন বর্ণহীন।",
        bank_n=118,
    ),
    q(
        "Basicity of oxalic acid is:",
        "অক্সালিক এসিডের ক্ষারকত্ব কত?",
        ["1", "2", "3", "4"],
        ["১", "২", "৩", "৪"],
        "B", "easy", "factual",
        "H2C2O4 is diprotic → basicity 2.",
        "H2C2O4 দ্বিপ্রোটিক → ক্ষারকত্ব ২।",
        bank_n=154,
    ),
    q(
        "Which compound cannot be used to prepare a primary standard solution directly?",
        "কোন যৌগ দিয়ে সরাসরি প্রাইমারি প্রমাণ দ্রবণ তৈরি করা যায় না?",
        ["KMnO4", "Na2CO3", "K2Cr2O7", "H2C2O4·2H2O"],
        ["KMnO4", "Na2CO3", "K2Cr2O7", "H2C2O4·2H2O"],
        "A", "easy", "factual",
        "KMnO4 is impure/unstable as weighed primary standard.",
        "KMnO4 প্রাইমারি স্ট্যান্ডার্ড নয়।",
        bank_n=159,
    ),
    q(
        "Volume of 0.2 M Na2CO3 needed to neutralize 10 mL of 0.1 M HCl is:",
        "১০ mL ০.১ M HCl প্রশমিত করতে ০.২ M Na2CO3-এর কত mL লাগে?",
        ["0.5 mL", "2.5 mL", "5 mL", "10 mL"],
        ["০.৫ mL", "২.৫ mL", "৫ mL", "১০ mL"],
        "B", "medium", "numerical",
        "e1V1S1 = e2V2S2 → 1×10×0.1 = 2×V×0.2 → V = 2.5 mL.",
        "১×১০×০.১ = ২×V×০.২ → V = ২.৫ mL।",
        bank_n=161,
    ),
    q(
        "An indicator present in a titration—\n(i) marks the end point\n(ii) alters the stoichiometry of the reaction\n(iii) changes its own colour\nWhich is correct?",
        "নির্দেশক বিক্রিয়ায় উপস্থিত থেকে—\n(i) শেষ বিন্দু নির্দেশ করে\n(ii) বিক্রিয়ার সমতা পরিবর্তন করে\n(iii) নিজের বর্ণ পরিবর্তন করে\nকোনটি সঠিক?",
        ["iii only", "i and ii", "i and iii", "i, ii and iii"],
        ["কেবল iii", "i ও ii", "i ও iii", "i, ii ও iii"],
        "C", "easy", "conceptual",
        "Indicators signal end point by colour change without changing stoichiometry.",
        "নির্দেশক বর্ণ পরিবর্তন করে শেষ বিন্দু দেখায়; সমতায় প্রভাব ফেলে না।",
        bank_n=164,
    ),
]

# ---------------------------------------------------------------------------
# t04 — Chemical calculations
# ---------------------------------------------------------------------------
T04 = [
    q(
        "Oxidation number of S in Na2S2O3 is:",
        "Na2S2O3 যৌগে S-এর জারণ সংখ্যা কত?",
        ["+2", "+2.5", "+4", "+5"],
        ["+2", "+2.5", "+4", "+5"],
        "B", "medium", "numerical",
        "2(+1) + 2x + 3(−2) = 0 → x = +2.5 (average).",
        "২(+১)+২x+৩(−২)=০ → x = +২.৫।",
        bank_n=6,
    ),
    q(
        "Oxidation number of S in S2O3^2− is:",
        "S2O3^2− আয়নে সালফারের জারণ সংখ্যা কোনটি?",
        ["+2.0", "+2.5", "+4.0", "+6.0"],
        ["+2.0", "+2.5", "+4.0", "+6.0"],
        "A", "medium", "numerical",
        "Printed explanation: 2x + 3(−2) = −2 → x = +2.",
        "মুদ্রিত ব্যাখ্যা: ২x + ৩(−২) = −২ → x = +২।",
        bank_n=50,
    ),
    q(
        "Oxidation number of carbon in magnesium carbide Mg2C is:",
        "ম্যাগনেসিয়াম কার্বাইডে কার্বনের জারণ মান কত?",
        ["−4", "−1", "+1", "+4"],
        ["−৪", "−১", "+১", "+৪"],
        "A", "medium", "numerical",
        "For Mg2C (methanide-type): 2(+2)+x=0 → x=−4.",
        "২(+২)+x=০ → x=−৪।",
        bank_n=51,
    ),
    q(
        "Equivalent mass of oxygen is:",
        "অক্সিজেনের তুল্য ভর কত?",
        ["64", "32", "16", "8"],
        ["৬৪", "৩২", "১৬", "৮"],
        "D", "easy", "factual",
        "Equivalent mass of O = 16/2 = 8.",
        "O-এর তুল্য ভর = ১৬/২ = ৮।",
        bank_n=52,
    ),
    q(
        "Volume of 0.1 M KMnO4 needed for 50 mL of 0.2 M Na2C2O4 (acid medium) is:",
        "৫০ mL ০.২ M Na2C2O4-এর জন্য ০.১ M KMnO4-এর আয়তন কত?",
        ["20 mL", "40 mL", "50 mL", "80 mL"],
        ["২০ mL", "৪০ mL", "৫০ mL", "৮০ mL"],
        "B", "hard", "numerical",
        "n-factors: C2O4^2− = 2, MnO4− = 5; 2×50×0.2 = 5×V×0.1 → V = 40 mL.",
        "২×৫০×০.২ = ৫×V×০.১ → V = ৪০ mL।",
        bank_n=54,
    ),
    q(
        "In balanced acidic KMnO4–FeC2O4 reaction, moles of oxidant : reductant are:",
        "অম্লীয় KMnO4 + FeC2O4 সমতাকৃত সমীকরণে জারক ও বিজারকের মোল সংখ্যা যথাক্রমে:",
        ["2 and 3", "2 and 6", "3 and 5", "3 and 6"],
        ["২ ও ৩", "২ ও ৬", "৩ ও ৫", "৩ ও ৬"],
        "C", "hard", "numerical",
        "Printed key: 6 KMnO4 : 10 FeC2O4 → ratio 3 : 5.",
        "৬ : ১০ = ৩ : ৫।",
        bank_n=32,
    ),
    q(
        "Molar ratio of oxidant to reductant in Cr2O7^2− + Fe^2+ + H+ → is:",
        "Cr2O7^2− + Fe^2+ + H+ বিক্রিয়ায় জারক ও বিজারকের মোল অনুপাত কত?",
        ["6 : 1", "1 : 6", "1 : 3", "1 : 7"],
        ["৬ : ১", "১ : ৬", "১ : ৩", "১ : ৭"],
        "B", "medium", "numerical",
        "1 Cr2O7^2− accepts 6 e− and oxidizes 6 Fe^2+ → 1 : 6.",
        "১ Cr2O7^2− ≡ ৬ Fe^2+ → ১ : ৬।",
        bank_n=44,
    ),
    q(
        "How many electrons does MnO4− accept in acidic medium?",
        "অম্লীয় মাধ্যমে MnO4− কয়টি ইলেকট্রন গ্রহণ করে?",
        ["2", "3", "4", "5"],
        ["২", "৩", "৪", "৫"],
        "D", "easy", "factual",
        "MnO4− + 8H+ + 5e− → Mn^2+ + 4H2O.",
        "MnO4− + ৮H+ + ৫e− → Mn^2+ + ৪H2O।",
        bank_n=145,
    ),
    q(
        "In alkaline medium, KMnO4 accepts how many electrons?",
        "ক্ষারীয় দ্রবণে KMnO4 কয়টি ইলেকট্রন গ্রহণ করে?",
        ["1", "3", "5", "7"],
        ["১", "৩", "৫", "৭"],
        "B", "medium", "factual",
        "In alkali, MnO4− → MnO2 (gain of 3e−).",
        "ক্ষারে MnO4− → MnO2 (৩e− গ্রহণ)।",
        bank_n=74,
    ),
    q(
        "Oxidation number of Mn in KMnO4 is:",
        "KMnO4-এ Mn-এর জারণ সংখ্যা কত?",
        ["+4", "+5", "+6", "+7"],
        ["+৪", "+৫", "+৬", "+৭"],
        "D", "easy", "numerical",
        "+1 + x + 4(−2) = 0 → x = +7.",
        "+১ + x + ৪(−২) = ০ → x = +৭।",
        bank_n=157,
    ),
    q(
        "Oxidation number of Cl in HClO4 is:",
        "HClO4-এ ক্লোরিনের জারণ সংখ্যা কত?",
        ["+1", "+3", "+5", "+7"],
        ["+১", "+৩", "+৫", "+৭"],
        "D", "easy", "numerical",
        "+1 + x + 4(−2) = 0 → x = +7.",
        "+১ + x − ৮ = ০ → x = +৭।",
        bank_n=103,
    ),
    q(
        "Which compound shows the highest oxidation state of chlorine?",
        "কোন যৌগে ক্লোরিনের জারণ মান সর্বোচ্চ?",
        ["HClO", "HClO2", "HClO3", "HClO4"],
        ["HClO", "HClO2", "HClO3", "HClO4"],
        "D", "easy", "factual",
        "Perchloric acid has Cl at +7.",
        "পারক্লোরিক অ্যাসিডে Cl = +৭।",
        bank_n=134,
    ),
    q(
        "1 mol acidic KMnO4 can oxidize how many moles of FeSO4?",
        "অম্লীয় মাধ্যমে ১ মোল KMnO4 কত মোল ফেরাস সালফেটকে জারিত করতে পারে?",
        ["10", "6", "5", "2.5"],
        ["১০", "৬", "৫", "২.৫"],
        "C", "easy", "numerical",
        "MnO4− ≡ 5 Fe^2+.",
        "১ MnO4− ≡ ৫ Fe^2+।",
        bank_n=135,
    ),
    q(
        "30 mL of 0.1 M FeSO4 requires what molarity of KMnO4 if 30 mL of it is used?",
        "৩০ mL ০.১ M FeSO4 টাইট্রেট করতে সমআয়তন KMnO4-এর ঘনমাত্রা কত?",
        ["0.01 M", "0.02 M", "0.03 M", "0.06 M"],
        ["০.০১ M", "০.০২ M", "০.০৩ M", "০.০৬ M"],
        "B", "hard", "numerical",
        "1 KMnO4 ≡ 5 FeSO4 → S(KMnO4) = (30×0.1)/(5×30) = 0.02 M.",
        "S = (৩০×০.১)/(৫×৩০) = ০.০২ M।",
        bank_n=113,
    ),
    q(
        "Mass of K2Cr2O7 needed to oxidize 10 g FeSO4 (acid) is about:",
        "১০ g FeSO4 জারিত করতে কত গ্রাম K2Cr2O7 লাগে?",
        ["3.22 g", "3.87 g", "4.12 g", "4.44 g"],
        ["৩.২২ g", "৩.৮৭ g", "৪.১২ g", "৪.৪৪ g"],
        "A", "hard", "numerical",
        "6 FeSO4 ≡ 1 K2Cr2O7 → 10 g needs ≈ 3.22 g dichromate.",
        "৬ FeSO4 ≡ ১ K2Cr2O7 → ≈ ৩.২২ g।",
        bank_n=123,
    ),
    q(
        "In 2Na2S2O3 + I2 → Na2S4O6 + 2NaI, number of electrons transferred is:",
        "2Na2S2O3 + I2 বিক্রিয়ায় কতটি ইলেকট্রন আদান-প্রদান হয়?",
        ["2", "3", "4", "6"],
        ["২", "৩", "৪", "৬"],
        "A", "medium", "numerical",
        "I2 + 2e− → 2I−; two electrons are exchanged.",
        "I2 + ২e− → ২I−; ইলেকট্রন সংখ্যা ২।",
        bank_n=143,
    ),
    q(
        "Equal volumes of 0.1 M NaOH and 0.1 M H2SO4 on mixing give a solution that is:",
        "সমআয়তন ০.১ M NaOH ও ০.১ M H2SO4 মিশ্রণের প্রকৃতি কী?",
        ["neutral", "amphiprotic", "acidic", "basic"],
        ["নিরপেক্ষ", "উভধর্মী", "অম্লীয়", "ক্ষারীয়"],
        "C", "medium", "numerical",
        "H2SO4 supplies twice the H+ of NaOH OH− → excess acid.",
        "H2SO4 দ্বিপ্রোটিক → অম্লীয় অবশেষ।",
        bank_n=132,
    ),
    q(
        "After diluting a 250 mL solution of 24.5 g H2SO4 by adding another 250 mL water, molarity becomes:",
        "২৪.৫ g H2SO4 বিশিষ্ট ২৫০ mL দ্রবণে আরও ২৫০ mL পানি যোগ করলে মোলার ঘনমাত্রা কত হবে?",
        ["0.1 M", "0.25 M", "0.5 M", "1 M"],
        ["০.১ M", "০.২৫ M", "০.৫ M", "১ M"],
        "C", "medium", "numerical",
        "Initial M = 24.5/(98×0.25)=1.0; double volume → 0.5 M.",
        "প্রাথমিক ১.০ M; আয়তন দ্বিগুণ → ০.৫ M।",
        bank_n=162,
    ),
    q(
        "ppm of 0.05 M H2SO4 (solute basis) is:",
        "০.০৫ M H2SO4 দ্রবণের ঘনমাত্রা ppm এককে কত?",
        ["2450 ppm", "245000 ppm", "4900 ppm", "490000 ppm"],
        ["২৪৫০ ppm", "২৪৫০০০ ppm", "৪৯০০ ppm", "৪৯০০০০ ppm"],
        "C", "medium", "numerical",
        "0.05×98×1000 = 4900 ppm.",
        "০.০৫×৯৮×১০০০ = ৪৯০০ ppm।",
        bank_n=146,
    ),
    q(
        "Which is a redox reaction?",
        "কোনটি জারণ-বিজারণ বিক্রিয়া?",
        [
            "HCl + NaOH → NaCl + H2O",
            "Na2SO4 + BaCl2 → BaSO4 + 2NaCl",
            "Zn + H2SO4 → ZnSO4 + H2",
            "AlCl3 + 3H2O → Al(OH)3 + 3HCl",
        ],
        [
            "HCl + NaOH → NaCl + H2O",
            "Na2SO4 + BaCl2 → BaSO4 + 2NaCl",
            "Zn + H2SO4 → ZnSO4 + H2",
            "AlCl3 + 3H2O → Al(OH)3 + 3HCl",
        ],
        "C", "easy", "conceptual",
        "Zn is oxidized and H+ reduced — a redox reaction.",
        "Zn জারিত ও H+ বিজারিত → রিডক্স।",
        bank_n=144,
    ),
]


def main() -> int:
    TOPICS.mkdir(parents=True, exist_ok=True)
    PARSED.mkdir(parents=True, exist_ok=True)

    topics = {
        "chem2_27_ch03_t01": T01,
        "chem2_27_ch03_t02": T02,
        "chem2_27_ch03_t03": T03,
        "chem2_27_ch03_t04": T04,
    }

    mappings = {}
    counts = {}
    for tid, items in topics.items():
        mappings[tid] = write_topic(tid, items)
        counts[tid] = 20
    counts["total"] = 80

    pdf_pages = [f"p{p:03d}_pdf{p+6}.png" for p in range(235, 248)]

    def bank_nums(mid: list) -> list:
        return sorted({n for n in mid if isinstance(n, int)})

    summary = {
        "chapter": "chem2_27_ch03",
        "title_en": "Quantitative Chemistry",
        "title_bn": "পরিমাণগত রসায়ন",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": pdf_pages,
        "skipped_faulty": {
            "figure_stimuli": "Vessel/figure-linked stems (e.g. unlabeled beaker pairs) rewritten as standalone numerical/conceptual items or skipped",
            "Q97": "Printed note admits no correct volume among options; skipped",
            "redox_overlap": "Some pure electrochemistry-only items left for ch04 when not needed to fill quantitative topics",
        },
        "pdf_mapping": {
            "chem2_27_ch03_t01": {
                "title": "Mole concept and stoichiometry / মোল ধারণা ও বিক্রিয়ার পরিমাণগত হিসাব",
                "main_bank": bank_nums(mappings["chem2_27_ch03_t01"]),
                "cq_or_reconstructed_fillers": sum(
                    1 for x in mappings["chem2_27_ch03_t01"] if x == "filler"
                ),
            },
            "chem2_27_ch03_t02": {
                "title": "Concentration of solutions / দ্রবণের ঘনমাত্রা",
                "main_bank": bank_nums(mappings["chem2_27_ch03_t02"]),
                "cq_or_reconstructed_fillers": sum(
                    1 for x in mappings["chem2_27_ch03_t02"] if x == "filler"
                ),
            },
            "chem2_27_ch03_t03": {
                "title": "Titration and volumetric analysis / টাইট্রেশন ও আয়তনিক বিশ্লেষণ",
                "main_bank": bank_nums(mappings["chem2_27_ch03_t03"]),
                "cq_or_reconstructed_fillers": sum(
                    1 for x in mappings["chem2_27_ch03_t03"] if x == "filler"
                ),
            },
            "chem2_27_ch03_t04": {
                "title": "Chemical calculations / রাসায়নিক গণনা",
                "main_bank": bank_nums(mappings["chem2_27_ch03_t04"]),
                "cq_or_reconstructed_fillers": sum(
                    1 for x in mappings["chem2_27_ch03_t04"] if x == "filler"
                ),
            },
        },
        "low_confidence": [
            "OCR on p235–p247 is noisy; stems reconstructed from explanations + chemical consistency.",
            "Oxidation-number average for S2O3^2− follows printed explanation (+2).",
            "Figure-dependent titration stimulus items converted to equation-only stems.",
        ],
        "counts": counts,
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {
                "chem2_27_ch03_t01": 20,
                "chem2_27_ch03_t02": 20,
                "chem2_27_ch03_t03": 20,
                "chem2_27_ch03_t04": 20,
            },
        },
    }

    out = PARSED / "ch03_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
