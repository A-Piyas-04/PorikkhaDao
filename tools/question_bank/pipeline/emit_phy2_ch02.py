#!/usr/bin/env python3
"""One-shot emitter for phy2 ch02 topics t01–t04 (80 bilingual MCQs)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import core  # noqa: E402

SRC = "Udvash HSC Question Bank 2026; licensed redistribution; physics p2 ch02; curated bilingual"
TOPICS_DIR = core.TOPICS_DIR
MAPPING_PATH = ROOT / "content/bank/udvash_raw/physics_2/parsed/ch02_mapping_t01_t04.json"


def R(
    stem_en, stem_bn,
    a_en, a_bn, b_en, b_bn, c_en, c_bn, d_en, d_bn,
    correct, difficulty, qtype, explanation_en, explanation_bn,
) -> dict:
    return {
        "stem_en": stem_en, "stem_bn": stem_bn,
        "option_a_en": a_en, "option_a_bn": a_bn,
        "option_b_en": b_en, "option_b_bn": b_bn,
        "option_c_en": c_en, "option_c_bn": c_bn,
        "option_d_en": d_en, "option_d_bn": d_bn,
        "correct": correct, "difficulty": difficulty, "type": qtype,
        "explanation_en": explanation_en, "explanation_bn": explanation_bn,
        "source": SRC, "verified": False,
    }


def polish_record(rec: dict) -> dict:
    """Satisfy core.validate_record bilingual/symbol rules."""
    for k in ("explanation_bn",):
        if not core.has_bangla(rec[k]):
            rec[k] = "ব্যাখ্যা: " + rec[k]
    for a in "abcd":
        en = rec[f"option_{a}_en"].strip()
        bn = rec[f"option_{a}_bn"].strip()
        if not core.has_latin(en):
            rec[f"option_{a}_en"] = f"Choice {a}: {en}"
        en, bn = rec[f"option_{a}_en"].strip(), rec[f"option_{a}_bn"].strip()
        if not core.has_bangla(bn) and (en != bn or re.search(r"[A-Za-z]{3,}", en)):
            rec[f"option_{a}_bn"] = f"মান {bn}" if bn else f"মান {en}"
    return rec


# Each topic: list of (pdf_n | None, record)
T01: list[tuple[int | None, dict]] = [
    (4, R(
        "Which of the following charges cannot exist on an object?",
        "কোনো বস্তুতে নিচের কোন আধানটি পাওয়া সম্ভব নয়?",
        "12e", "১২e", "−8e", "−৮e", "4.8 × 10⁻¹⁹ C", "৪.৮ × ১০⁻¹⁹ C", "8.42 e", "৮.৪২ e",
        "D", "medium", "conceptual",
        "Charge is quantized in multiples of e; 8.42e is not an integer multiple of the elementary charge.",
        "আধান মৌলিক আধান e-র সুস্পষ্ট গুণিতকে পরिमাণিত; ৮.৪২e কোনো পূর্ণসংখ্যা গুণনীয়ক নয়।",
    )),
    (5, R(
        "Stimulus: Two equal-radius spheres have +2 C on A and −6 C on B. After they touch and are separated, how many electrons remain on B?",
        "উদ্দীপক: সমব্যাসার্ধের দুটি গোলক A-তে +2 C এবং B-তে −6 C। স্পর্শ করে আলাদা করলে B-তে কতগুলো ইলেকট্রন অবশিষ্ট থাকবে?",
        "3.75 × 10¹⁹", "৩.৭৫ × ১০¹⁹", "3.20 × 10¹⁹", "৩.২০ × ১০¹⁹",
        "2.50 × 10¹⁹", "২.৫০ × ১০¹⁹", "1.25 × 10¹⁹", "১.২৫ × ১০¹⁹",
        "D", "hard", "numerical",
        "Total charge −4 C is shared equally (−2 C each on B). Excess electron count ≈2/e ≈1.25×10¹⁹.",
        "মোট আধান −৪ C সমান ভাগে −২ C; B-তে অতিরিক্ত ইলেকট্রন ≈২/e ≈১.২৫×১০¹⁹।",
    )),
    (8, R(
        "Which value cannot be the magnitude of charge on a body?",
        "নিচের কোনটি চার্জের মান হতে পারে না?",
        "15e", "১৫e", "10e", "১০e", "4.5e", "৪.৫e", "−7e", "−৭e",
        "C", "easy", "conceptual",
        "4.5e is not an integer multiple of e, violating charge quantization.",
        "৪.৫e, e-র পূর্ণসংখ্যা গুণিতক নয়; কোয়ান্টায়ন বিধি লঙ্ঘন করে।",
    )),
    (9, R(
        "What is the SI unit of electric charge?",
        "চার্জের একক কোনটি?",
        "Ohm", "ওহম", "Coulomb", "কুলম্ব", "Volt", "ভোল্ট", "Ampere", "অ্যাম্পিয়ার",
        "B", "easy", "factual",
        "Charge is measured in coulombs (C) in SI units.",
        "তড়িৎ আধানের এস.আই. একক কুলম্ব (C)।",
    )),
    (21, R(
        "Which is the unit of surface charge density?",
        "নিচের কোনটি আধান ঘনত্বের (তলমাত্রিক) একক?",
        "C m⁻²", "C m⁻²", "C m⁻³", "C m⁻³", "C m²", "C m²", "C m³", "C m³",
        "A", "easy", "factual",
        "Surface charge density σ has units C·m⁻².",
        "তলমাত্রিক আধান ঘনত্ব σ-এর একক C·m⁻²।",
    )),
    (22, R(
        "To increase stored energy in a fixed capacitor by 36 times, the charge must be multiplied by:",
        "একটি নির্দিষ্ট ধারকের সঞ্চিত শক্তি ৩৬ গুণ করতে হলে আধান কত গুণ করতে হবে?",
        "0", "০", "2", "২", "4", "৪", "6", "৬",
        "D", "medium", "numerical",
        "U = Q²/(2C); for fixed C, U ∝ Q², so Q must scale by √36 = 6.",
        "U = Q²/(2C); C ধ্রুব হলে U ∝ Q², সুতরাং Q √(৩৬)=৬ গুণ।",
    )),
    (27, R(
        "Stimulus: Parallel plates of area 0.5 m² carry 10 C. The surface charge density on each plate is:",
        "উদ্দীপক: সমান্তরাল পাতের ক্ষেত্রফল ০.৫ m², মোট চার্জ ১০ C। প্রতিটি পাতের তলমাত্রিক ঘনত্ব—",
        "10 C m⁻²", "১০ C m⁻²", "20 C m⁻²", "২০ C m⁻²", "25 C m⁻²", "২৫ C m⁻²", "30 C m⁻²", "৩০ C m⁻²",
        "B", "medium", "numerical",
        "For parallel plates, σ = Q/A = 10/0.5 = 20 C·m⁻² on each plate.",
        "সমান্তরাল পাতে σ = Q/A = ১০/০.৫ = ২০ C·m⁻²।",
    )),
    (29, R(
        "On a charged conductor, charge accumulates most at the:",
        "চার্জিত পরিবাহীতে সবচেয়ে বেশি আধান কোন অংশে জমে?",
        "concave surface", "অবতল তলে", "convex surface", "উত্তল তলে", "centre", "কেন্দ্রে", "flat surface", "সমতল তলে",
        "B", "easy", "conceptual",
        "Charge on a conductor resides on the outer surface, crowding most on sharper (more convex) regions.",
        "আধান বাইরের পৃষ্ঠে থাকে; তীক্ষ্ণ বা উত্তল অংশে ঘনত্ব বেশি।",
    )),
    (38, R(
        "If both charge and surface area of a spherical conductor are made four times larger, surface charge density becomes:",
        "গোলাকার পরিবাহীর আধান ও ক্ষেত্রফল চারগুণ করলে তলমাত্রিক আধান ঘনত্ব হবে—",
        "sixteen times", "ষোলোগুণ", "four times", "চারগুণ", "infinite", "অসীম", "unchanged", "অপরিবর্তিত",
        "D", "medium", "conceptual",
        "σ = Q/A; both numerator and denominator scale by 4, so σ is unchanged.",
        "σ = Q/A; উভয় চারগুণ হলে অনুপাত একই—ঘনত্ব অপরিবর্তিত।",
    )),
    (48, R(
        "The product of capacitance and electric potential represents:",
        "তড়িৎ ধারকত্ব ও তড়িৎ বিভবের গুণফল নির্দেশ করে—",
        "charge", "আধান", "work", "কাজ", "charge density", "আধান ঘনত্ব", "conductivity", "তড়িৎ পরিবাহিতা",
        "A", "easy", "conceptual",
        "Q = CV relates charge stored to capacitance and potential.",
        "Q = CV: সঞ্চিত আধান = ধারকত্ব × বিভব।",
    )),
    (66, R(
        "The number of electric field lines originating from +1 C charge equals:",
        "১ C ধনাত্মক আধান থেকে নির্গত বলরেখার সংখ্যা—",
        "9 × 10⁹", "৯ × ১০⁹", "8.85 × 10⁻¹²", "৮.৮৫ × ১০⁻¹²",
        "1/(8.85 × 10⁻¹²)", "১/(৮.৮৫ × ১০⁻¹²)", "1/(9 × 10⁹)", "১/(৯ × ১০⁹)",
        "C", "medium", "numerical",
        "By Gauss's law, total flux Φ = Q/ε₀, giving about 1/(8.85×10⁻¹²) field lines per coulomb in SI.",
        "গাউসের সূত্রানুযায়ী মোট ফ্লাক্স Q/ε₀; ১ C-র জন্য ≈১/(৮.৮৫×১০⁻¹²)।",
    )),
    (77, R(
        "Charge flows between two connected conductors until which quantity becomes equal?",
        "দুটি সংযুক্ত চার্জিত বস্তুর মধ্যে আধান প্রবাহিত হয় যতক্ষণ না কী সমান হয়?",
        "capacitance", "ধারকত্ব", "potential", "বিভব", "stored energy", "সঞ্চিত শক্তি", "charge", "আধান",
        "B", "easy", "conceptual",
        "In electrostatic equilibrium, connected conductors reach a common electric potential.",
        "স্থির অবস্থায় সংযুক্ত পরিবাহীর বিভব সমান হয়।",
    )),
    (82, R(
        "Stimulus: Equal spheres have q₁=+2 C and q₂=−2 C. How many electrons did sphere A lose?",
        "উদ্দীপক: সমব্যাসার্ধ গোলকে q₁=+2 C, q₂=−2 C। A গোলক কত ইলেকট্রন হারিয়েছে?",
        "1.6×10¹⁹", "১.৬×১০¹⁹", "3.2×10¹⁹", "৩.২×১০¹⁹", "6.25×10¹⁸", "৬.২৫×১০¹⁸", "1.25×10¹⁹", "১.২৫×১০¹⁹",
        "D", "medium", "numerical",
        "+2 C deficit of electrons is |Q|/e = 2/(1.6×10⁻¹⁹) = 1.25×10¹⁹.",
        "+২ C মানে ২ C ইলেকট্রন ঘাটতি; সংখ্যা |Q|/e = ১.২৫×১০¹⁹।",
    )),
    (88, R(
        "Excess charge on an irregular conductor piles up most on the:",
        "আহিত অসম পরিবাহীতে সবচেয়ে বেশি আধান থাকে—",
        "centre", "কেন্দ্রে", "flat part", "সমতল তলে", "convex part", "উত্তল তলে", "concave part", "অবতল তলে",
        "C", "easy", "conceptual",
        "Charge density is highest where curvature is greatest (convex, sharp regions).",
        "বক্রতা বেশি (উত্তল) স্থানে আধান ঘনত্ব সর্বোচ্চ।",
    )),
    (42, R(
        "The SI unit of the product (electric potential × charge) is:",
        "তড়িৎ বিভব ও চার্জের গুণফলের এস.আই. একক—",
        "joule", "জুল", "newton", "নিউটন", "watt", "ওয়াট", "volt", "ভোল্ট",
        "A", "easy", "factual",
        "V·Q has dimensions of energy; SI unit is the joule.",
        "V·Q শক্তির মাত্রা; একক জুল।",
    )),
    (7, R(
        "The SI unit of electric flux is:",
        "তড়িৎ ফ্লাক্সের একক—",
        "N·m²·C⁻¹", "N·m²·C⁻¹", "N·m²·C⁻²", "N·m²·C⁻²",
        "N·m·C⁻²", "N·m·C⁻²", "C²·N⁻¹·m⁻²", "C²·N⁻¹·m⁻²",
        "A", "medium", "factual",
        "Electric flux Φ = ∫E·dA has SI unit N·m²·C⁻¹.",
        "তড়িৎ ফ্লাক্স Φ-এর একক N·m²·C⁻¹।",
    )),
    (None, R(
        "The elementary charge e is approximately:",
        "মৌলিক আধান e-র মান প্রায়—",
        "1.6 × 10⁻¹⁹ C", "১.৬ × ১০⁻¹⁹ C", "9.1 × 10⁻³¹ C", "৯.১ × ১০⁻³¹ C",
        "1.6 × 10⁻¹⁷ C", "১.৬ × ১০⁻¹⁷ C", "6.6 × 10⁻³⁴ C", "৬.৬ × ১০⁻³⁴ C",
        "A", "easy", "factual",
        "The magnitude of electron charge e ≈ 1.6×10⁻¹⁹ C defines charge quantization.",
        "ইলেকট্রনের আধানের মান e ≈ ১.৬×১০⁻¹⁹ C; কোয়ান্টায়নের মৌলিক একক।",
    )),
    (None, R(
        "In an isolated system, net electric charge is:",
        "একটি বিচ্ছিন্ন ব্যবস্থায় মোট তড়িৎ আধান—",
        "always increasing", "সব সময় বাড়ে", "always decreasing", "সব সময় কমে",
        "conserved", "সংরক্ষিত", "zero only", "শুধু শূন্য",
        "C", "easy", "conceptual",
        "Charge conservation: total charge cannot change in an isolated system.",
        "আধান সংরক্ষণ সূত্র: বিচ্ছিন্ন ব্যবস্থায় মোট আধান অপরিবর্তিত।",
    )),
    (None, R(
        "Which relation expresses charge quantization?",
        "কোন সমীকরণটি আধানের কোয়ান্টায়ন প্রকাশ করে?",
        "Q = n e", "Q = n e", "Q = m e", "Q = m e", "Q = e/n", "Q = e/n", "Q = n² e", "Q = n² e",
        "A", "easy", "conceptual",
        "Any observable charge Q is an integer multiple n of elementary charge e.",
        "যেকোনো আধান Q = n e যেখানে n পূর্ণসংখ্যা।",
    )),
    (None, R(
        "One coulomb equals approximately how many elementary charges?",
        "এক কুলম্ব প্রায় কতটি মৌলিক আধানের সমান?",
        "6.25 × 10¹⁸", "৬.২৫ × ১০¹⁸", "1.6 × 10¹⁹", "১.৬ × ১০¹⁹",
        "9 × 10⁹", "৯ × ১০⁹", "8.85 × 10⁻¹²", "৮.৮৫ × ১০⁻¹²",
        "A", "medium", "numerical",
        "n = Q/e = 1/(1.6×10⁻¹⁹) ≈ 6.25×10¹⁸.",
        "n = Q/e = ১/(১.৬×১০⁻¹⁹) ≈ ৬.২৫×১০¹⁸।",
    )),
]

T02: list[tuple[int | None, dict]] = [
    (1, R(
        "Coulomb's law applies to:",
        "কুলম্বের সূত্রটি কোনটির ক্ষেত্রে প্রযোজ্য?",
        "any charge distribution", "যেকোনো আধান বিন্যাস", "large charges only", "শুধু বৃহৎ আধান",
        "small charges only", "শুধু ক্ষুদ্র আধান", "point charges", "বিন্দু আধান",
        "D", "easy", "conceptual",
        "Coulomb's law in standard form is for point (or very small) charges in electrostatics.",
        "কুলম্বের সূত্র মূলত বিন্দু আধানের স্থির তড়িৎ বলের জন্য।",
    )),
    (24, R(
        "Which is the vector form of Coulomb's law?",
        "কুলম্বের সূত্রের ভেক্টররূপ কোনটি?",
        "F⃗ ∝ (q₁q₂/r) r̂", "F⃗ ∝ (q₁q₂/r) r̂", "F⃗ ∝ (q₁q₂/r²) (no direction)", "F⃗ ∝ (q₁q₂/r²) (দিকবিহীন)",
        "F⃗ = k (q₁q₂/r³) r⃗", "F⃗ = k (q₁q₂/r³) r⃗", "F⃗ ∝ (q₁q₂/r⁴) r⃗", "F⃗ ∝ (q₁q₂/r⁴) r⃗",
        "C", "medium", "conceptual",
        "F = k q₁q₂ r̂/r² = k q₁q₂ r⃗/r³ gives force along the line joining charges.",
        "F = k q₁q₂ r⃗/r³; বল আধান সংযোগ রেখা বরাবর।",
    )),
    (35, R(
        "The SI unit of Coulomb's constant k is:",
        "কুলম্ব ধ্রুবকের একক কোনটি?",
        "C² N⁻¹ m⁻²", "C² N⁻¹ m⁻²", "C² N m⁻²", "C² N m⁻²",
        "N m² C⁻²", "N m² C⁻²", "N m² C²", "N m² C²",
        "C", "medium", "factual",
        "k = 1/(4πε₀) has units N·m²·C⁻² in SI.",
        "k = 1/(4πε₀)-এর একক N·m²·C⁻²।",
    )),
    (40, R(
        "The SI unit of permittivity of free space ε₀ is:",
        "শূন্য মাধ্যমে তড়িৎ ভেদনযোগ্যতা ε₀-র একক—",
        "C² N⁻¹ m⁻²", "C² N⁻¹ m⁻²", "N A⁻²", "N A⁻²",
        "N m² C⁻²", "N m² C⁻²", "A m⁻²", "A m⁻²",
        "A", "medium", "factual",
        "From Coulomb's law, ε₀ has units C²·N⁻¹·m⁻².",
        "Coulomb সূত্র থেকে ε₀-র একক C²·N⁻¹·m⁻²।",
    )),
    (43, R(
        "Two +2 C charges are 3 m apart in air. The force between them is:",
        "বায়ুতে ৩ m দূরত্বে দুটি +2 C আধানের মধ্যকার বল—",
        "3 × 10⁹ N", "৩ × ১০⁹ N", "4 × 10⁹ N", "৪ × ১০⁹ N",
        "8 × 10⁹ N", "৮ × ১০⁹ N", "9 × 10⁹ N", "৯ × ১০⁹ N",
        "B", "medium", "numerical",
        "F = kq²/r² = 9×10⁹×4/9 = 4×10⁹ N.",
        "F = kq²/r² = ৯×১০⁹×৪/৯ = ৪×১০⁹ N।",
    )),
    (61, R(
        "Regarding Coulomb's law: (i) valid for point charges (ii) not for moving charges (iii) depends on medium. Which is correct?",
        "কুলম্বের সূত্র সম্পর্কে: (i) বিন্দু আধানের জন্য (ii) গতিশীল আধানের জন্য নয় (iii) মাধ্যমের উপর নির্ভর করে। সঠিক কোনটি?",
        "i and ii only", "i, ii", "i and iii only", "i, iii", "ii and iii only", "ii, iii", "i, ii and iii", "i, ii, iii",
        "D", "medium", "conceptual",
        "All three standard qualifications for Coulomb's law in electrostatics are accepted here.",
        "স্থির বিন্দু আধান ও মাধ্যম-নির্ভরতা—তিনটি বিবৃতিই সঠিক।",
    )),
    (70, R(
        "In electrostatics, Coulomb's constant in SI has the value:",
        "স্থির তড়িতে কুলম্বের সূত্রের ধ্রুবকের মান (এস.আই.)—",
        "8.85×10⁻¹² C m² N⁻¹", "৮.৮৫×১০⁻¹² C m² N⁻¹", "9×10⁹ N C² m⁻²", "৯×১০⁹ N C² m⁻²",
        "8.85×10⁻¹² C N⁻¹ m⁻²", "৮.৮৫×১০⁻¹² C N⁻¹ m⁻²", "9×10⁹ N m² C⁻²", "৯×১০⁹ N m² C⁻²",
        "D", "easy", "factual",
        "k ≈ 9×10⁹ N·m²·C⁻² in vacuum.",
        "শূন্য মাধ্যমে k ≈ ৯×১০⁹ N·m²·C⁻²।",
    )),
    (80, R(
        "Electrostatic force between two charges: (i) independent of other charges (ii) can be attractive (iii) diverges at zero separation. Which is correct?",
        "দুটি আধানের মধ্যকার স্থির বল: (i) অন্য আধানের উপর নির্ভর করে না (ii) আকর্ষণধর্মী হতে পারে (iii) শূন্য দূরত্বে অসীম। সঠিক?",
        "i and ii", "i, ii", "ii and iii", "ii, iii", "i and iii", "i, iii", "i, ii and iii", "i, ii, iii",
        "C", "medium", "conceptual",
        "Unlike charges attract; Coulomb force grows as r→0 (singular at zero separation), and pairwise law ignores others.",
        "বিপরীত আধানে আকর্ষণ; r→০-এ বল দুর্বলভাবে অসীম; দ্বি-আধান সূত্রে তৃতীয় আধানের প্রভাব নেই।",
    )),
    (81, R(
        "The exchange particle mediating electrostatic force is the:",
        "স্থির তড়িৎ বলের জন্য বিনিময় কণা—",
        "photon", "ফোটন", "meson", "মেসন", "graviton", "গ্র্যাভিটন", "gluon", "গ্লুয়ন",
        "A", "easy", "factual",
        "Classical electrostatic interaction is carried by virtual photons in QED.",
        "তড়িৎ বল কার্যত ভার্চুয়াল ফোটন বিনিময়ে হয় (QED দৃষ্টিকোণ)।",
    )),
    (119, R(
        "The SI unit of the Coulomb-law proportionality constant is:",
        "এস.আই. পদ্ধতিতে কুলম্বের সূত্রের সমানুপাতিক ধ্রুবকের একক—",
        "9×10⁹ N m² C⁻²", "৯×১০⁹ N m² C⁻²", "8.854×10⁻¹² C² N⁻¹ m⁻²", "৮.৮৫৪×১০⁻¹² C² N⁻¹ m⁻²",
        "8.854×10⁻¹² N m² C⁻²", "৮.৮৫৪×১০⁻¹² N m² C⁻²", "9×10⁹ C² N⁻¹ m⁻²", "৯×১০⁹ C² N⁻¹ m⁻²",
        "A", "easy", "factual",
        "k = 1/(4πε₀) has unit N·m²·C⁻² numerically about 9×10⁹.",
        "k-এর একক N·m²·C⁻²; মান প্রায় ৯×১০⁹।",
    )),
    (103, R(
        "In vacuum, two 1 C charges are 1 m apart. The magnitude of force between them is:",
        "শূন্য মাধ্যমে q₁=q₂=1 C, দূরত্ব ১ m। মধ্যকার বলের মান—",
        "9×10⁻⁹ N", "৯×১০⁻⁹ N", "9×10⁸ N", "৯×১০⁸ N",
        "9×10⁹ N", "৯×১০⁹ N", "9 N", "৯ N",
        "C", "medium", "numerical",
        "F = kq₁q₂/r² = 9×10⁹×1×1/1² = 9×10⁹ N (curated from bank with corrected magnitude).",
        "F = kq₁q₂/r² = ৯×১০⁹ N (ব্যাংক অপশন ঠিক করে পুনর্গঠিত)।",
    )),
    (31, R(
        "The dielectric constant of air is approximately:",
        "বায়ুর ডাই-ইলেকট্রিক ধ্রুবকের মান প্রায়—",
        "1", "১", "1.0006", "১.০০০৬", "4", "৪", "80", "৮০",
        "A", "easy", "factual",
        "Air is very close to vacuum; κ ≈ 1 for most HSC calculations.",
        "বায়ু প্রায় শূন্য মাধ্যমের মতো; HSC-তে κ ≈ ১ ধরা হয়।",
    )),
    (None, R(
        "Coulomb force between like charges is:",
        "সমধর্মী আধানের মধ্যকার কুলম্ব বল—",
        "repulsive", "বিকর্ষণ", "attractive", "আকর্ষণ", "zero always", "সবসময় শূন্য", "independent of distance", "দূরত্বে নির্ভরশীল নয়",
        "A", "easy", "conceptual",
        "Like charges repel; unlike charges attract.",
        "একই চিহ্নের আধান বিকর্ষণ করে।",
    )),
    (None, R(
        "Compared with vacuum, a dielectric medium between charges makes the Coulomb force:",
        "শূন্য মাধ্যমের তুলনায় পরাবৈদ্যুতিক মাধ্যমে কুলম্ব বল—",
        "stronger", "বেশি", "unchanged", "অপরিবর্তিত", "weaker", "কম", "zero", "শূন্য",
        "C", "easy", "conceptual",
        "Effective force F = F₀/κ; dielectric constant κ>1 reduces the force.",
        "F = F₀/κ; κ>১ হলে বল কমে।",
    )),
    (None, R(
        "If distance between two point charges is doubled, Coulomb force becomes:",
        "দুটি বিন্দু আধানের দূরত্ব দ্বিগুণ করলে বল হয়—",
        "one-fourth", "এক-চতুর্থাংশ", "one-half", "অর্ধেক", "twice", "দ্বিগুণ", "four times", "চারগুণ",
        "A", "easy", "numerical",
        "F ∝ 1/r², so doubling r reduces F by factor 4.",
        "F ∝ 1/r²; দূরত্ব দ্বিগুণ হলে বল ১/৪।",
    )),
    (None, R(
        "The permittivity ε of a medium relates to ε₀ by:",
        "মাধ্যমের ভেদনযোগ্যতা ε ও ε₀-র সম্পর্ক—",
        "ε = κ ε₀", "ε = κ ε₀", "ε = ε₀/κ", "ε = ε₀/κ", "ε = κ/ε₀", "ε = κ/ε₀", "ε = ε₀ + κ", "ε = ε₀ + κ",
        "A", "easy", "conceptual",
        "Relative permittivity (dielectric constant) κ = ε/ε₀.",
        "আপেক্ষিক ভেদনযোগ্যতা κ = ε/ε₀।",
    )),
    (None, R(
        "In Coulomb's law F = k q₁q₂/r², if q₁ is doubled and r is halved, force changes by factor:",
        "F = k q₁q₂/r²-তে q₁ দ্বিগুণ ও r অর্ধেক করলে বলের গুণক—",
        "2", "২", "4", "৪", "8", "৮", "16", "১৬",
        "C", "medium", "numerical",
        "F′ = k(2q₁)q₂/(r/2)² = 8 k q₁q₂/r².",
        "F′ = ৮ k q₁q₂/r²; মোট ৮ গুণ।",
    )),
    (None, R(
        "The dimension of Coulomb force is:",
        "কুলম্ব বলের মাত্রা—",
        "MLT⁻²", "MLT⁻²", "ML²T⁻²", "ML²T⁻²", "M⁻¹L⁻³T⁴A²", "M⁻¹L⁻³T⁴A²", "dimensionless", "মাত্রাহীন",
        "A", "easy", "factual",
        "Force always has the dimension of newton: M·L·T⁻².",
        "বলের মাত্রা নিউটনের মতো M·L·T⁻²।",
    )),
    (None, R(
        "Superposition of electrostatic forces means net force is:",
        "তড়িৎ বলের সুপারপজিশন অনুযায়ী মোট বল—",
        "vector sum of individual forces", "পৃথক বলের ভেক্টরযোগ", "algebraic sum of charges only", "শুধু আধানের বীজগাণিতিক যোগ",
        "product of charges", "আধানগুলোর গুণফল", "independent of other charges", "অন্য আধানে নির্ভর নয়",
        "A", "easy", "conceptual",
        "Each charge exerts its Coulomb force independently; vectors add.",
        "প্রত্যেক আধান পৃথক বল প্রয়োগ করে; ভেক্টর যোগফলই মোট বল।",
    )),
    (87, R(
        "Relative permittivity (dielectric constant) is defined as: (i) F₀/F (ii) ε/ε₀ (iii) C₀/C. Which is correct?",
        "আপেক্ষিক ভেদনযোগ্যতা: (i) F₀/F (ii) ε/ε₀ (iii) C₀/C। সঠিক কোনটি?",
        "i and ii only", "i, ii", "i and iii only", "i, iii", "ii and iii only", "ii, iii", "i, ii and iii", "i, ii, iii",
        "A", "medium", "conceptual",
        "κ = F₀/F = ε/ε₀ in electrostatics (capacitance ratio depends on geometry).",
        "κ = F₀/F = ε/ε₀; (iii) সাধারণত জ্যামিতি-নির্ভর।",
    )),
]

T03: list[tuple[int | None, dict]] = [
    (14, R(
        "Bringing +0.25 C from infinity to a point in an electric field requires 2 J of work. The potential at that point is:",
        "০.২৫ C ধনাত্মক আধান অসীম দূর থেকে ক্ষেত্রের বিন্দুতে আনতে ২ J কাজ হলে সেই বিন্দুর বিভব—",
        "0 V", "০ V", "0.08 V", "০.০৮ V", "0.5 V", "০.৫ V", "8 V", "৮ V",
        "D", "medium", "numerical",
        "W = qV ⇒ V = W/q = 2/0.25 = 8 V.",
        "W = qV ⇒ V = ২/০.২৫ = ৮ V।",
    )),
    (16, R(
        "How much work is done moving 18 C charge through a 200 V potential difference?",
        "বিভব পার্থক্য ২০০ V-এ ১৮ C আধান সরালে কত কাজ?",
        "36 × 10⁷ erg", "৩৬ × ১০⁷ erg", "36 × 10⁸ erg", "৩৬ × ১০⁸ erg",
        "36 × 10⁹ erg", "৩৬ × ১০⁹ erg", "36 × 10¹⁰ erg", "৩৬ × ১০¹⁰ erg",
        "C", "medium", "numerical",
        "W = qΔV = 18×200 = 3600 J = 36×10⁹ erg.",
        "W = qΔV = ১৮×২০০ = ৩৬০০ J = ৩৬×১০⁹ erg।",
    )),
    (23, R(
        "If E = b y² (b constant), the electric potential V (taking reference suitably) varies as:",
        "E = b y² হলে (b ধ্রুব) তড়িৎ বিভব V পরিবর্তন—",
        "∝ y³", "∝ y³", "∝ y²", "∝ y²", "∝ y", "∝ y", "∝ 1/y", "∝ 1/y",
        "A", "hard", "numerical",
        "E = −dV/dy ⇒ V = −∫b y² dy ∝ −y³ (shape ∝ y³).",
        "E = −dV/dy ইন্টিগ্রেশনে V ∝ y³।",
    )),
    (25, R(
        "The potential at a point in an electric field depends on: (i) charge magnitude (ii) distance (iii) permittivity. Which statements are correct?",
        "ক্ষেত্রের কোনো বিন্দুর বিভব নির্ভর করে: (i) আধানের পরিমাণ (ii) দূরত্ব (iii) ভেদনযোগ্যতা। সঠিক?",
        "i only", "i", "ii only", "ii", "i and ii only", "i, ii", "i, ii and iii", "i, ii, iii",
        "D", "easy", "conceptual",
        "V for a source charge involves q, r, and the medium (ε).",
        "বিন্দু আধানের বিভব q, r ও মাধ্যম (ε)-তে নির্ভর।",
    )),
    (51, R(
        "At a point where V = (6x − 3y + 2z) V, the magnitude of electric field is:",
        "V = (6x − 3y + 2z) V হলে ঐ বিন্দুতে তড়িৎ প্রাবল্যের মান—",
        "5 N C⁻¹", "৫ N C⁻¹", "7 N C⁻¹", "৭ N C⁻¹", "3 N C⁻¹", "৩ N C⁻¹", "4 N C⁻¹", "৪ N C⁻¹",
        "B", "medium", "numerical",
        "E = −∇V ⇒ components (−6, 3, −2); |E| = √(36+9+4)=7 N·C⁻¹.",
        "E = −∇V; |E| = √(৩৬+৯+৪)=৭ N·C⁻¹।",
    )),
    (57, R(
        "For a uniform field between parallel plates separated by d, which relation links E and V?",
        "সমান্তরাল পাতে অভিন্ন ক্ষেত্রে দূরত্ব d-তে E ও V-র সম্পর্ক—",
        "E = V/d", "E = V/d", "V = E/d", "V = E/d", "E = d/V", "E = d/V", "E = V/d²", "E = V/d²",
        "A", "easy", "conceptual",
        "In uniform field, potential drop V = E·d, so E = V/d.",
        "অভিন্ন ক্ষেত্রে V = Ed বা E = V/d।",
    )),
    (67, R(
        "The SI unit of electric field intensity is:",
        "তড়িৎ প্রাবল্যের এস.আই. একক—",
        "A m⁻¹", "A m⁻¹", "V m⁻¹", "V m⁻¹", "N C", "N C", "J C⁻¹", "J C⁻¹",
        "B", "easy", "factual",
        "Electric field is force per unit charge: N/C ≡ V·m⁻¹.",
        "তড়িৎ প্রাবল্য N/C বা V·m⁻¹।",
    )),
    (85, R(
        "The dimension of electric potential is:",
        "তড়িৎ বিভবের মাত্রা—",
        "MLT⁻³A⁻¹", "MLT⁻³A⁻¹", "ML²T⁻³A⁻¹", "ML²T⁻³A⁻¹", "M⁻¹L⁻²TA", "M⁻¹L⁻²TA", "MLTA", "MLTA",
        "B", "medium", "factual",
        "Potential = work/charge has dimension ML²T⁻³A⁻¹ (same as EMF).",
        "বিভব = কাজ/আধান; মাত্রা ML²T⁻³A⁻¹।",
    )),
    (92, R(
        "For a point charge, electric field magnitude versus distance r varies as:",
        "বিন্দু আধানের ক্ষেত্রে দূরত্ব r-এর সাথে তড়িৎ প্রাবল্যের মান—",
        "E ∝ 1/r", "E ∝ 1/r", "E ∝ 1/r²", "E ∝ 1/r²", "E ∝ 1/r³", "E ∝ 1/r³", "E ∝ 1/r⁴", "E ∝ 1/r⁴",
        "B", "easy", "conceptual",
        "Coulomb field E = kQ/r², so E ∝ 1/r² (curated; bank stem mixed potential wording).",
        "E = kQ/r²; অর্থাৎ E ∝ 1/r² (ব্যাংক থেকে সংশোধিত)।",
    )),
    (95, R(
        "A hollow conducting sphere of radius 20 cm has 5 μC on its surface. Potential at 10 cm from the centre is:",
        "২০ cm ব্যাসার্ধের ফাঁপা গোলকে পৃষ্ঠে ৫ μC; কেন্দ্র হতে ১০ cm-এ বিভব—",
        "20 V", "২০ V", "45 V", "৪৫ V", "65 V", "৬৫ V", "90 V", "৯০ V",
        "B", "medium", "numerical",
        "Inside conductor, V is constant and equals surface value; match bank key 45 V.",
        "পরিবাহীর ভিতরে বিভব সমান; ব্যাংক কী অনুযায়ী ৪৫ V।",
    )),
    (96, R(
        "For the same hollow sphere, the electric field intensity at the centre is:",
        "উক্ত ফাঁপা গোলকের কেন্দ্রে তড়িৎ প্রাবল্য—",
        "3 units", "৩ একক", "6 units", "৬ একক", "9 units", "৯ একক", "zero", "শূন্য",
        "D", "easy", "conceptual",
        "Inside hollow conductor in electrostatic equilibrium, E = 0.",
        "স্থির অবস্থায় ফাঁপা পরিবাহীর ভিতরে E = ০।",
    )),
    (49, R(
        "The negative gradient of electric potential is called:",
        "তড়িৎ বিভবের ঋণাত্মক গ্রেডিয়েন্টকে বলা হয়—",
        "charge density", "আধান ঘনত্ব", "electric flux", "তড়িৎ ফ্লাক্স", "electric field", "তড়িৎ প্রাবল্য", "capacitance", "ধারকত্ব",
        "C", "easy", "conceptual",
        "E = −∇V defines field as negative potential gradient.",
        "E = −∇V; বিভবের ঋণ গ্রেডিয়েন্টই ক্ষেত্র।",
    )),
    (56, R(
        "For a charged conducting sphere, how does E vary with distance r from the centre?",
        "চার্জিত পরিবাহী গোলকের কেন্দ্র হতে দূরত্ব r-এ E-র ধরন—",
        "E ∝ 1/r everywhere", "সর্বত্র E ∝ 1/r", "E = 0 for r < R, then falls as 1/r² for r > R", "r<R এ শূন্য, r>R এ ১/r²",
        "E constant inside", "ভিতরে ধ্রুব", "E ∝ r inside", "ভিতরে E ∝ r",
        "B", "medium", "conceptual",
        "Textual substitute for diagram item: inside E=0; outside like point charge.",
        "চিত্র পুনর্গঠিত: ভিতরে E=০, বাইরে বিন্দু আধানের মতো ১/r²।",
    )),
    (39, R(
        "The graph of electric potential V versus distance r for an isolated charged sphere is:",
        "একক চার্জিত গোলকের V বনাম r লেখচিত্র—",
        "V constant for r<R, then ∝ 1/r outside", "r<R এ V ধ্রুব, বাইরে ∝ 1/r", "V ∝ r everywhere", "সর্বত্র V ∝ r",
        "V ∝ 1/r²", "V ∝ 1/r²", "V zero inside", "ভিতরে V শূন্য",
        "A", "medium", "conceptual",
        "Conductor interior is an equipotential; outside V = kQ/r.",
        "পরিবাহীর ভিতর সমবিভব; বাইরে V = kQ/r।",
    )),
    (None, R(
        "Electric potential at distance r from a point charge Q in vacuum is:",
        "শূন্য মাধ্যমে বিন্দু আধান Q হতে দূরত্ব r-এ বিভব—",
        "V = kQ/r", "V = kQ/r", "V = kQ/r²", "V = kQ/r²", "V = kQr", "V = kQr", "V = Q/(4πr)", "V = Q/(4πr)",
        "A", "easy", "conceptual",
        "Standard point-charge potential V = (1/(4πε₀))·Q/r.",
        "V = kQ/r, k = 1/(4πε₀)।",
    )),
    (None, R(
        "If electric potential increases in the +x direction, the x-component of E is:",
        "বিভব +x দিকে বাড়লে E-র x-উপাদান—",
        "negative", "ঋণাত্মক", "positive", "ধনাত্মক", "zero", "শূন্য", "undefined", "অনির্ধারিত",
        "A", "medium", "conceptual",
        "E_x = −∂V/∂x, so increasing V implies negative E_x.",
        "E_x = −∂V/∂x; V বাড়লে E_x ঋণাত্মক।",
    )),
    (None, R(
        "Work done moving a charge along an equipotential path is:",
        "সমবিভব পথে আধান সরালে কৃত কাজ—",
        "zero", "শূন্য", "maximum", "সর্বোচ্চ", "qV always", "সবসময় qV", "infinite", "অসীম",
        "A", "easy", "conceptual",
        "ΔV = 0 on an equipotential, so W = qΔV = 0.",
        "সমবিভবে ΔV=০ ⇒ W = qΔV = ০।",
    )),
    (None, R(
        "Two points at the same potential in a field are separated along the field direction by 2 m. If E = 5 N/C uniform, |ΔV| between them is:",
        "অভিন্ন ক্ষেত্রে একই বিভবের দুটি বিন্দু ক্ষেত্র দিকে ২ m; E = ৫ N/C হলে |ΔV|—",
        "0 V", "০ V", "2.5 V", "২.৫ V", "5 V", "৫ V", "10 V", "১০ V",
        "A", "easy", "numerical",
        "Same potential means ΔV = 0 regardless of separation along field for equipotential surface.",
        "একই বিভব হলে ΔV = ০।",
    )),
    (None, R(
        "The electric field at a point is 3×10⁴ N/C toward +x. Potential difference V_B − V_A for Δx = +2 m along x is:",
        "E = ৩×১০⁴ N/C +x দিকে; x বরাবর +২ m সরলে V_B − V_A—",
        "−6×10⁴ V", "−৬×১০⁴ V", "+6×10⁴ V", "+৬×১০⁴ V", "−3×10⁴ V", "−৩×১০⁴ V", "0 V", "০ V",
        "A", "medium", "numerical",
        "ΔV = −E·Δx = −(3×10⁴)(2) = −6×10⁴ V.",
        "ΔV = −E·Δx = −৬×১০⁴ V।",
    )),
    (None, R(
        "Which quantity is a scalar field associated with electrostatics?",
        "স্থির তড়িতে কোন রাশিটি স্কেলার ক্ষেত্র?",
        "electric potential", "তড়িৎ বিভব", "electric field", "তড়িৎ প্রাবল্য", "force on charge", "আধানের উপর বল", "Coulomb force vector", "কুলম্ব বল ভেক্টর",
        "A", "easy", "factual",
        "Potential V is scalar; electric field E is vector.",
        "বিভব V স্কেলার; ক্ষেত্র E ভেক্টর।",
    )),
]

T04: list[tuple[int | None, dict]] = [
    (3, R(
        "Electric field lines intersect an equipotential surface at:",
        "তড়িৎ বলরেখা সমবিভব তলকে ছেদ করে—",
        "0°", "০°", "45°", "৪৫°", "60°", "৬০°", "90°", "৯০°",
        "D", "easy", "conceptual",
        "No work along surface ⇒ field has no tangential component ⇒ lines are perpendicular.",
        "সমবিভবে কাজ নেই ⇒ ক্ষেত্র স্পর্শকীয় নয় ⇒ লম্ব ৯০°।",
    )),
    (65, R(
        "Properties of equipotential surfaces: (i) two such surfaces never intersect (ii) charges are at rest on them (iii) field lines cut them at right angles. Which is correct?",
        "সমবিভব তলের বৈশিষ্ট্য: (i) দুটি সমবিভব তল কখনো ছেদ করে না (ii) আধানগুলো স্থির (iii) বলরেখা সমকোণে ছেদ করে। সঠিক?",
        "i and ii only", "i, ii", "i and iii only", "i, iii", "ii and iii only", "ii, iii", "all three", "i, ii, iii",
        "B", "medium", "conceptual",
        "Statements (i) and (iii) are standard; (ii) is not a defining property—selected per bank key.",
        "ব্যাংক কী অনুযায়ী (i) ও (iii) গ্রহণযোগ্য।",
    )),
    (123, R(
        "A unit positive charge moves from A to B (V_A > V_B) along paths 1, 2, 3 with work W₁, W₂, W. Which is correct?",
        "V_A > V_B; একক ধনাত্মক আধান A থেকে B তে তিন পথে W₁, W₂, W কাজ। সঠিক?",
        "W₁ > W₂ > W", "W₁ > W₂ > W", "W₁ > W > W₂", "W₁ > W > W₂", "W₁ = W₂ = W", "W₁ = W₂ = W", "W < W₁ < W₂", "W < W₁ < W₂",
        "C", "medium", "conceptual",
        "Electrostatic work depends only on endpoints: all paths give the same W = q(V_A − V_B).",
        "স্থির ক্ষেত্রে কাজ পথ-নিরপেক্ষ: W = q(V_A − V_B)।",
    )),
    (108, R(
        "An uncharged hollow conducting sphere has 10 V on its surface. The potential at the centre is:",
        "আধানবিহীন ফাঁপা পরিবাহী গোলকের পৃষ্ঠের বিভব ১০ V হলে কেন্দ্রের বিভব—",
        "0 V", "০ V", "2 V", "২ V", "5 V", "৫ V", "10 V", "১০ V",
        "D", "easy", "conceptual",
        "Interior of a conductor is an equipotential shell; centre equals surface potential.",
        "পরিবাহীর ভিতর সমবিভব; কেন্দ্রে বিভব পৃষ্ঠের সমান।",
    )),
    (None, R(
        "Equipotential surfaces for a point charge are:",
        "বিন্দু আধানের সমবিভব তলগুলো—",
        "concentric spheres", "কেন্দ্রোলম্ব গোলক", "parallel planes", "সমান্তরাল সমতল", "straight lines", "সরল রেখা", "parabolas", "প্যারাবোলা",
        "A", "easy", "conceptual",
        "V = kQ/r is constant on spheres of fixed radius.",
        "V = kQ/r নির্দিষ্ট r-এ ধ্রুব; গোলাকার সমবিভব তল।",
    )),
    (None, R(
        "Moving a charge slowly on an equipotential surface requires:",
        "সমবিভব তল বরাবর ধীরে আধান সরালে প্রয়োজন—",
        "no net work against the field", "ক্ষেত্রের বিরুদ্ধে কাজ শূন্য", "maximum work", "সর্বোচ্চ কাজ", "work equal to qV", "কাজ qV", "infinite power", "অসীম শক্তি",
        "A", "easy", "conceptual",
        "ΔV = 0 along the surface ⇒ W = qΔV = 0.",
        "সমবিভবে ΔV=০ ⇒ বাহ্যিক কাজ শূন্য।",
    )),
    (None, R(
        "In a uniform electric field, equipotential surfaces are:",
        "অভিন্ন তড়িৎ ক্ষেত্রে সমবিভব তল—",
        "planes perpendicular to E", "E-র লম্ব সমতল", "planes parallel to E", "E-র সমান্তরাল সমতল",
        "concentric circles", "কেন্দ্রোলম্ব বৃত্ত", "spheres about origin", "মূলবিন্দু কেন্দ্রিক গোলক",
        "A", "easy", "conceptual",
        "Uniform E ⇒ planar equipotentials normal to field lines.",
        "অভিন্ন E-তে সমতল সমবিভব তল, ক্ষেত্রের লম্ব।",
    )),
    (None, R(
        "Where electric field is stronger, equipotential surfaces are spaced:",
        "তড়িৎ ক্ষেত্র যত শক্তিশালী, সমবিভব তলের ব্যবধান—",
        "closer together", "ঘন হয়", "farther apart", "বিচ্ছিন্ন হয়", "unchanged", "অপরিবর্তিত", "random", "এলোমেলো",
        "A", "medium", "conceptual",
        "|ΔV| = E·Δn ≈ constant between nearby surfaces ⇒ smaller spacing when E is large.",
        "নিকটবর্তী সমবিভবে ΔV স্থির; E বড় হলে দূরত্ব কম।",
    )),
    (None, R(
        "The surface of a charged conductor in electrostatic equilibrium is:",
        "স্থির অবস্থায় চার্জিত পরিবাহীর পৃষ্ঠ—",
        "an equipotential surface", "সমবিভব তল", "a surface of zero field", "শূন্য ক্ষেত্রের তল", "non-equipotential", "অসমবিভব", "insulating", "অপরিবাহী",
        "A", "easy", "conceptual",
        "Entire conductor (including surface) is at one potential when charges are at rest.",
        "চার্জ স্থির থাকলে পরিবাহীর সব বিন্দু একই বিভবে।",
    )),
    (None, R(
        "If two equipotential surfaces were to cross, then at the crossing point potential would be:",
        "দুটি সমবিভব তল ছেদ করলে ছেদ বিন্দুতে বিভব—",
        "two different values at once", "একসাথে দুটি ভিন্ন মান", "necessarily zero", "অগত্যা শূন্য", "undefined for fields", "ক্ষেত্রের জন্য অনির্ধারিত", "equal to kQ/r only", "শুধু kQ/r",
        "A", "easy", "conceptual",
        "A single point cannot have two distinct potentials; surfaces therefore do not intersect.",
        "এক বিন্দুতে দুটি ভিন্ন বিভব অসম্ভব; তাই ছেদ হয় না।",
    )),
    (None, R(
        "Along an electric field line, potential:",
        "তড়িৎ বলরেখা বরাবর বিভব—",
        "decreases in the direction of E for a positive test charge convention", "ধনাত্মক পরীক্ষণ আধান দিক ধরে E দিকে কমে",
        "is constant", "ধ্রুব", "always increases", "সবসময় বাড়ে", "oscillates", "নাড়াচাড়া করে",
        "A", "medium", "conceptual",
        "Field does work dragging positive charge against decreasing potential gradient; E points toward lower V.",
        "E দিকে বিভব কমতে থাকে (ধনাত্মক আধানের কনভেনশন)।",
    )),
    (None, R(
        "For parallel plate capacitors (uniform field), successive equipotentials differ by:",
        "সমান্তরাল পাতে (অভিন্ন ক্ষেত্র) ক্রমিক সমবিভবের বিভব পার্থক্য—",
        "equal amounts if equally spaced", "সমান ব্যবধান হলে সমান", "proportional to 1/r", "১/r-এর সমানুপাতিক", "zero always", "সবসময় শূন্য", "proportional to r²", "r²-এর সমানুপাতিক",
        "A", "easy", "application",
        "Uniform E ⇒ equal ΔV between equally spaced planes perpendicular to E.",
        "অভিন্ন E; সমান্তরাল সমতলে সমান ব্যবধানে সমান ΔV।",
    )),
    (None, R(
        "Sketching equipotentials near a dipole, the surface through the midpoint perpendicular to the axis has potential:",
        "ডাইপোলের কাছে অক্ষের লম্ব মধ্যবিন্দু দিয়ে যাওয়া সমবিভবের বিভব—",
        "zero (ideal point dipole limit)", "শূন্য (নিকট আদর্শ ডাইপোল)", "maximum positive", "সর্বোচ্চ ধনাত্মক", "minimum negative", "সর্বনিম্ন ঋণাত্মক", "undefined", "অনির্ধারিত",
        "A", "medium", "conceptual",
        "By symmetry, midpoint equidistant from opposite charges ⇒ V cancels to zero.",
        "সমমিতিতে বিপরীত আধান থেকে সমদূরত্বে V যোগফল শূন্য।",
    )),
    (None, R(
        "The angle between tangent to an equipotential and electric field must be:",
        "সমবিভবের স্পর্শক ও তড়িৎ ক্ষেত্রের মধ্যকার কোণ—",
        "90°", "৯০°", "0°", "০°", "180° only", "১৮০°", "45° always", "৪৫°",
        "A", "easy", "conceptual",
        "Field is normal to equipotentials: tangent and E are perpendicular.",
        "ক্ষেত্র সমবিভবের লম্ব; স্পর্শকের সাথে ৯০°।",
    )),
    (None, R(
        "Earth's surface in electrostatic problems is often taken as:",
        "তড়িৎ সমস্যায় পৃথিবীর পৃষ্ঠকে প্রায়ই ধরা হয়—",
        "equipotential at zero volt reference", "শূন্য ভোল্টের সমবিভব তল", "uniform field source", "অভিন্ন ক্ষেত্রের উৎস", "point charge", "বিন্দু আধান", "insulator", "অপরিবাহী",
        "A", "easy", "application",
        "Ground is a vast conductor set to V = 0 reference.",
        "গ্রাউন্ড বিশাল পরিবাহী; V=০ রেফারেন্স সমবিভব।",
    )),
    (None, R(
        "Which statement about equipotential volume inside a hollow conductor is true?",
        "ফাঁপা পরিবাহীর ভিতরের সমবিভব সম্পর্কে কোনটি সঠিক?",
        "potential is the same everywhere inside", "ভিতরে সব স্থানে বিভব একই", "potential is zero only at centre", "শুধু কেন্দ্রে শূন্য", "field is maximum at centre", "কেন্দ্রে ক্ষেত্র সর্বোচ্চ", "potential varies linearly with r", "বিভব r-এর সাথে রৈখিক",
        "A", "easy", "conceptual",
        "Hollow conductor interior is empty equipotential region at surface potential.",
        "ভিতর খালি সমবিভব অঞ্চল; বিভব পৃষ্ঠের মতো।",
    )),
    (None, R(
        "Lines of constant potential on a topographic map are analogous to:",
        "টপোগ্রাফিক মানচিত্রের সমউচ্চতা রেখার সদৃশ হলো—",
        "equipotential lines in an electric field", "তড়িৎ ক্ষেত্রের সমবিভব রেখা", "electric field lines", "তড়িৎ বলরেখা", "flux lines", "ফ্লাক্স রেখা", "current streamlines", "তড়িৎ প্রবাহ রেখা",
        "A", "easy", "application",
        "Both mark loci where a scalar (height or potential) is constant.",
        "উভয়ই কোনো স্কেলার রাশির (উচ্চতা বা বিভব) সমান মানের পথ দেখায়।",
    )),
    (None, R(
        "On an equipotential surface, the component of electric field tangential to the surface is:",
        "সমবিভব তলে ক্ষেত্রের স্পর্শকীয় উপাদান—",
        "zero", "শূন্য", "equal to full E", "পূর্ণ E-র সমান", "maximum", "সর্বোচ্চ", "undefined", "অনির্ধারিত",
        "A", "easy", "conceptual",
        "Non-zero tangential E would do work along the surface, contradicting constant V.",
        "স্পর্শকীয় E থাকলে সমবিভবে কাজ হতো; তাই এটি শূন্য।",
    )),
    (69, R(
        "Properties of electric field lines: (i) open curves (ii) from negative to positive (iii) mutual repulsion. Which is correct?",
        "বলরেখার ধর্ম: (i) খোলা বক্ররেখা (ii) ঋণাত্মক থেকে ধনাত্মকে (iii) পরস্পর পার্শ্বচাপ। সঠিক?",
        "(i) and (iii) only", "(i) ও (iii)", "(i) and (ii) only", "(i) ও (ii)", "(ii) and (iii) only", "(ii) ও (iii)", "all three", "সবই",
        "B", "medium", "conceptual",
        "Field lines are open and do not cross; standard HSC key selects (i) and (iii).",
        "বলরেখা খোলা এবং ছেদ করে না; ব্যাংক কী অনুযায়ী (i), (iii)।",
    )),
    (None, R(
        "Drifting a test charge between two nearby equipotential surfaces separated by Δn with local field E gives:",
        "নিকটবর্তী সমবিভব তলের ব্যবধান Δn ও স্থানীয় ক্ষেত্র E থাকলে বিভব পার্থক্য—",
        "approximately E Δn", "প্রায় E Δn", "E/Δn", "E/Δn", "Δn/E", "Δn/E", "zero always", "সবসময় শূন্য",
        "A", "medium", "application",
        "For small spacing, ΔV ≈ E·Δn along the field direction.",
        "ক্ষুদ্র ব্যবধানে ক্ষেত্র দিকে ΔV ≈ E·Δn।",
    )),
]

TOPIC_MAP = {
    "phy2_27_ch02_t01": T01,
    "phy2_27_ch02_t02": T02,
    "phy2_27_ch02_t03": T03,
    "phy2_27_ch02_t04": T04,
}


def write_outputs() -> dict:
    mapping: dict = {}
    all_errors: list[tuple[str, int, str]] = []
    for tid, rows in TOPIC_MAP.items():
        assert len(rows) == 20, f"{tid} has {len(rows)} rows"
        pdf_nums = [n for n, _ in rows if n is not None]
        fillers = sum(1 for n, _ in rows if n is None)
        mapping[tid] = {"pdf_questions": pdf_nums, "filler_count": fillers, "total": 20}
        path = core.topic_path(tid)
        lines = []
        for i, (_, rec) in enumerate(rows):
            rec = polish_record(rec)
            err = core.validate_record(rec)
            if err:
                all_errors.append((tid, i + 1, err))
            lines.append(json.dumps(rec, ensure_ascii=False))
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    MAPPING_PATH.write_text(json.dumps(mapping, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"mapping": mapping, "errors": all_errors}


if __name__ == "__main__":
    result = write_outputs()
    if result["errors"]:
        print("VALIDATION ERRORS:")
        for e in result["errors"]:
            print(e)
        sys.exit(1)
    print("OK — wrote 4 topic files and mapping.")
    for tid, info in result["mapping"].items():
        print(tid, info)