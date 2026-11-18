#!/usr/bin/env python3
"""Seed Higher Mathematics 2nd Paper Ch10 (Measures of Dispersion and Probability).

Curated from Udvash HSC Question Bank 2026 printed pp. 332–334 (PDF 338–340).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
OCR is sparse/noisy (~3 pages; mostly creative CQ + model-test mix); reconstructs
board-style items from readable stems/solutions and supplements with accurate
HSC-level authored MCQs to complete all three topics.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
from core import validate_record  # noqa: E402

TOPICS = ROOT / "content" / "bank" / "topics"
PARSED = ROOT / "content" / "bank" / "udvash_raw" / "higher_mathematics_2" / "parsed"
SOURCE = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "higher_mathematics p2 ch10; curated bilingual"
)


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    if not re.search(r"[A-Za-z]", en):
        en = f"value {en}"
    if not re.search(r"[ঀ-৿]", bn):
        if en.startswith("value ") or re.search(r"[A-Za-z]{3,}", en):
            bn = "মান " + bn.removeprefix("মান ").strip()
    return en, bn


def q(
    stem_en: str,
    stem_bn: str,
    opts_en: list[str],
    opts_bn: list[str],
    correct: str,
    difficulty: str,
    qtype: str,
    exp_en: str,
    exp_bn: str,
) -> dict:
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
        "source": SOURCE,
    }


# =============================================================================
# hm2_27_ch10_t01 — Measures of dispersion / বিস্তার পরিমাপ
# =============================================================================
T01 = [
    q(
        "The range of the data 2, 5, 8, 11, 14 is:",
        "2, 5, 8, 11, 14 তথ্যের পরিসর কত?",
        ["10", "11", "12", "14"],
        ["10", "11", "12", "14"],
        "C", "easy", "numerical",
        "Range = largest − smallest = 14 − 2 = 12.",
        "পরিসর = বৃহত্তম − ক্ষুদ্রতম = 14 − 2 = 12।",
    ),
    q(
        "Which is a measure of absolute dispersion?",
        "নিচের কোনটি পরম বিস্তার পরিমাপ?",
        ["Coefficient of variation", "Standard deviation", "Coefficient of range", "Correlation coefficient"],
        ["বিভেদাঙ্কের গুণাঙ্ক", "আদর্শ বিচ্যুতি", "পরিসরের গুণাঙ্ক", "সহসম্পর্ক গুণাঙ্ক"],
        "B", "easy", "factual",
        "Standard deviation is an absolute measure of dispersion; CV is relative.",
        "আদর্শ বিচ্যুতি পরম বিস্তার পরিমাপ; CV আপেক্ষিক।",
    ),
    q(
        "Mean deviation of 3, 6, 9 about the mean is:",
        "3, 6, 9 এর গড় সম্পর্কে গড় ব্যবধান কত?",
        ["0", "2", "3", "6"],
        ["0", "2", "3", "6"],
        "B", "easy", "numerical",
        "Mean = 6; MD = (|3−6|+|6−6|+|9−6|)/3 = 6/3 = 2.",
        "গড় = 6; MD = 6/3 = 2।",
    ),
    q(
        "For observations x₁,…,xₙ with mean x̄, variance σ² equals:",
        "x₁,…,xₙ পর্যবেক্ষণের গড় x̄ হলে বিভেদাঙ্ক σ² সমান—",
        ["(1/n) Σ(xᵢ − x̄)", "(1/n) Σ(xᵢ − x̄)²", "(1/n) Σ|xᵢ − x̄|", "Σ(xᵢ − x̄)²"],
        ["মান (1/n) Σ(xᵢ − x̄)", "মান (1/n) Σ(xᵢ − x̄)²", "মান (1/n) Σ|xᵢ − x̄|", "মান Σ(xᵢ − x̄)²"],
        "B", "easy", "factual",
        "By definition σ² = (1/n) Σ(xᵢ − x̄)².",
        "সংজ্ঞা অনুসারে σ² = (1/n) Σ(xᵢ − x̄)²।",
    ),
    q(
        "If variance of x₁,…,xₙ is 9, then standard deviation is:",
        "x₁,…,xₙ এর বিভেদাঙ্ক 9 হলে আদর্শ বিচ্যুতি কত?",
        ["3", "9", "81", "√3"],
        ["3", "9", "81", "√3"],
        "A", "easy", "numerical",
        "σ = √(variance) = √9 = 3.",
        "σ = √9 = 3।",
    ),
    q(
        "Quartile deviation (semi-interquartile range) is:",
        "চতুর্থক ব্যবধান (অর্ধ-আন্তঃচতুর্থক পরিসর) হল—",
        ["Q₃ − Q₁", "(Q₃ − Q₁)/2", "(Q₃ + Q₁)/2", "Q₃/Q₁"],
        ["Q₃ − Q₁", "(Q₃ − Q₁)/2", "(Q₃ + Q₁)/2", "Q₃/Q₁"],
        "B", "easy", "factual",
        "QD = (Q₃ − Q₁)/2.",
        "QD = (Q₃ − Q₁)/2।",
    ),
    q(
        "For data with Q₁ = 20 and Q₃ = 40, quartile deviation is:",
        "Q₁ = 20 ও Q₃ = 40 হলে চতুর্থক ব্যবধান কত?",
        ["10", "20", "30", "60"],
        ["10", "20", "30", "60"],
        "A", "easy", "numerical",
        "QD = (40 − 20)/2 = 10.",
        "QD = (40 − 20)/2 = 10।",
    ),
    q(
        "Coefficient of variation (CV) is:",
        "বিভেদাঙ্কের গুণাঙ্ক (CV) হল—",
        ["(σ/x̄)×100%", "(x̄/σ)×100%", "σ × x̄", "σ − x̄"],
        ["মান (σ/x̄)×100%", "মান (x̄/σ)×100%", "মান σ × x̄", "মান σ − x̄"],
        "A", "easy", "factual",
        "CV = (σ/x̄)×100% (relative dispersion).",
        "CV = (σ/x̄)×100% (আপেক্ষিক বিস্তার)।",
    ),
    q(
        "If mean = 50 and SD = 5, then CV is:",
        "গড় = 50 ও আদর্শ বিচ্যুতি = 5 হলে CV কত?",
        ["5%", "10%", "25%", "50%"],
        ["5%", "10%", "25%", "50%"],
        "B", "easy", "numerical",
        "CV = (5/50)×100% = 10%.",
        "CV = (5/50)×100% = 10%।",
    ),
    q(
        "For 2, 4, 6, 8, 10 the variance is:",
        "2, 4, 6, 8, 10 এর বিভেদাঙ্ক কত?",
        ["4", "6", "8", "10"],
        ["4", "6", "8", "10"],
        "C", "medium", "numerical",
        "Mean = 6; deviations −4,−2,0,2,4; Σ(x−x̄)² = 40; σ² = 40/5 = 8.",
        "গড়=6; বিচ্যুতির বর্গযোগ 40; σ²=40/5=8।",
    ),
    q(
        "Variance of first n natural numbers is:",
        "প্রথম n স্বাভাবিক সংখ্যার বিভেদাঙ্ক—",
        ["(n²−1)/12", "(n²+1)/12", "n(n+1)/2", "(n−1)/12"],
        ["মান (n²−1)/12", "মান (n²+1)/12", "মান n(n+1)/2", "মান (n−1)/12"],
        "A", "medium", "factual",
        "σ² = (n² − 1)/12 for 1,2,…,n.",
        "1,2,…,n এর জন্য σ² = (n² − 1)/12।",
    ),
    q(
        "If each observation is increased by 5, variance:",
        "প্রতিটি পর্যবেক্ষণ 5 বৃদ্ধি করলে বিভেদাঙ্ক—",
        ["increases by 5", "increases by 25", "remains unchanged", "becomes zero"],
        ["5 বৃদ্ধি পায়", "25 বৃদ্ধি পায়", "অপরিবর্তিত থাকে", "শূন্য হয়"],
        "C", "medium", "conceptual",
        "Adding a constant shifts mean but does not change deviations; variance unchanged.",
        "ধ্রুবক যোগে বিচ্যুতি অপরিবর্তিত; বিভেদাঙ্ক একই থাকে।",
    ),
    q(
        "If each observation is multiplied by 3, new variance is old variance times:",
        "প্রতিটি পর্যবেক্ষণ 3 দিয়ে গুণ করলে নতুন বিভেদাঙ্ক পুরোনোর কতগুণ?",
        ["3", "6", "9", "1/3"],
        ["3", "6", "9", "1/3"],
        "C", "medium", "conceptual",
        "Scaling by k multiplies variance by k²; here k=3 ⇒ factor 9.",
        "k গুণে বিভেদাঙ্ক k² গুণ হয়; k=3 ⇒ 9 গুণ।",
    ),
    q(
        "Which statement is true? (i) SD ≥ 0 (ii) variance = (SD)² (iii) range ≥ QD×2",
        "কোনটি সঠিক? (i) SD ≥ 0 (ii) বিভেদাঙ্ক = (SD)² (iii) পরিসর ≥ QD×2",
        ["i, ii only", "i, iii only", "ii, iii only", "i, ii and iii"],
        ["কেবল i, ii", "কেবল i, iii", "কেবল ii, iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "All three hold: SD is non-negative; variance is its square; Q₃−Q₁ ≤ range so 2·QD ≤ range.",
        "তিনটিই সত্য: SD ≥ 0; σ²=(SD)²; 2·QD ≤ পরিসর।",
    ),
    q(
        "Mean deviation is least when taken about the:",
        "গড় ব্যবধান সর্বনিম্ন হয় যখন নেওয়া হয়—",
        ["mean", "median", "mode", "mid-range"],
        ["গড়", "মধ্যমা", "প্রচুরক", "মধ্য-পরিসর"],
        "B", "medium", "factual",
        "Mean deviation is minimized about the median.",
        "গড় ব্যবধান মধ্যমার সাপেক্ষে সর্বনিম্ন হয়।",
    ),
    q(
        "For a frequency distribution, if Σf = 50, Σf|x−A| = 200 about A, mean deviation about A is:",
        "Σf = 50, A সম্পর্কে Σf|x−A| = 200 হলে গড় ব্যবধান কত?",
        ["2", "4", "5", "10"],
        ["2", "4", "5", "10"],
        "B", "medium", "numerical",
        "MD = Σf|x−A|/Σf = 200/50 = 4.",
        "MD = 200/50 = 4।",
    ),
    q(
        "Coefficient of quartile deviation is:",
        "চতুর্থক ব্যবধানের গুণাঙ্ক—",
        ["(Q₃−Q₁)/(Q₃+Q₁)", "(Q₃+Q₁)/(Q₃−Q₁)", "(Q₃−Q₁)/2", "Q₃/Q₁"],
        ["মান (Q₃−Q₁)/(Q₃+Q₁)", "মান (Q₃+Q₁)/(Q₃−Q₁)", "মান (Q₃−Q₁)/2", "মান Q₃/Q₁"],
        "A", "medium", "factual",
        "Coefficient of QD = (Q₃ − Q₁)/(Q₃ + Q₁).",
        "চতুর্থক ব্যবধানের গুণাঙ্ক = (Q₃ − Q₁)/(Q₃ + Q₁)।",
    ),
    q(
        "Two series have means 40 and 50, SDs 5 and 10. Which is more consistent?",
        "দুই সিরিজের গড় 40 ও 50, SD 5 ও 10। কোনটি অধিক সুসংগত?",
        ["first (CV=12.5%)", "second (CV=20%)", "both equal", "cannot compare"],
        ["প্রথম (CV=12.5%)", "দ্বিতীয় (CV=20%)", "উভয় সমান", "তুলনা করা যায় না"],
        "A", "hard", "application",
        "CV₁=5/40×100%=12.5%, CV₂=10/50×100%=20%; smaller CV ⇒ more consistent.",
        "CV₁=12.5%, CV₂=20%; ক্ষুদ্রতর CV ⇒ অধিক সুসংগত।",
    ),
    q(
        "If σ = 4 and mean = 20 for variable x, then for y = 2x + 3 the SD of y is:",
        "x এর σ = 4 ও গড় = 20; y = 2x + 3 হলে y এর আদর্শ বিচ্যুতি কত?",
        ["4", "5", "8", "11"],
        ["4", "5", "8", "11"],
        "C", "hard", "numerical",
        "SD(aX+b) = |a|·SD(X) = 2×4 = 8.",
        "SD(aX+b) = |a|·SD(X) = 8।",
    ),
    q(
        "For scores 10, 20, 30, 40, 50, mean deviation about the median is:",
        "10, 20, 30, 40, 50 এর মধ্যমা সম্পর্কে গড় ব্যবধান কত?",
        ["8", "10", "12", "15"],
        ["8", "10", "12", "15"],
        "C", "hard", "numerical",
        "Median = 30; MD = (|10−30|+|20−30|+0+|40−30|+|50−30|)/5 = 60/5 = 12.",
        "মধ্যমা=30; MD=60/5=12।",
    ),
]


# =============================================================================
# hm2_27_ch10_t02 — Probability rules / সম্ভাবনার সূত্র
# =============================================================================
T02 = [
    q(
        "Classical probability of an event A is:",
        "ঘটনা A এর চিরায়ত সম্ভাবনা—",
        ["n(A)/n(S)", "n(S)/n(A)", "n(A)×n(S)", "1 − n(A)"],
        ["মান n(A)/n(S)", "মান n(S)/n(A)", "মান n(A)×n(S)", "মান 1 − n(A)"],
        "A", "easy", "factual",
        "P(A) = number of favourable outcomes / total outcomes = n(A)/n(S).",
        "P(A) = অনুকূল ফলাফল / মোট ফলাফল = n(A)/n(S)।",
    ),
    q(
        "If P(A′) = 1/3, then P(A) equals:",
        "P(A′) = 1/3 হলে P(A) কত?",
        ["1/3", "2/3", "1", "0"],
        ["1/3", "2/3", "1", "0"],
        "B", "easy", "numerical",
        "P(A) + P(A′) = 1 ⇒ P(A) = 1 − 1/3 = 2/3.",
        "P(A) = 1 − 1/3 = 2/3।",
    ),
    q(
        "For mutually exclusive events A and B:",
        "বর্জনশীল ঘটনা A ও B এর জন্য—",
        ["P(A∪B)=P(A)+P(B)", "P(A∪B)=P(A)P(B)", "P(A∩B)=P(A)+P(B)", "P(A∪B)=1"],
        ["মান P(A∪B)=P(A)+P(B)", "মান P(A∪B)=P(A)P(B)", "মান P(A∩B)=P(A)+P(B)", "মান P(A∪B)=1"],
        "A", "easy", "factual",
        "Mutually exclusive ⇒ P(A∩B)=0 ⇒ P(A∪B)=P(A)+P(B).",
        "বর্জনশীল ⇒ P(A∪B)=P(A)+P(B)।",
    ),
    q(
        "A fair coin is tossed once. P(head) is:",
        "একটি নিরপেক্ষ মুদ্রা একবার নিক্ষেপে হেড পাওয়ার সম্ভাবনা—",
        ["0", "1/4", "1/2", "1"],
        ["0", "1/4", "1/2", "1"],
        "C", "easy", "numerical",
        "Two equally likely outcomes; P(H)=1/2.",
        "দুই সমসম্ভাব্য ফল; P(H)=1/2।",
    ),
    q(
        "A fair die is rolled. Probability of an even number is:",
        "নিরপেক্ষ ছক্কায় জোড় সংখ্যা পাওয়ার সম্ভাবনা—",
        ["1/6", "1/3", "1/2", "2/3"],
        ["1/6", "1/3", "1/2", "2/3"],
        "C", "easy", "numerical",
        "Even faces {2,4,6}; P=3/6=1/2.",
        "জোড় {2,4,6}; P=3/6=1/2।",
    ),
    q(
        "A coin and a die are tossed together. P(head and even) is:",
        "একটি মুদ্রা ও একটি ছক্কা একত্রে নিক্ষেপে হেড ও জোড় সংখ্যার সম্ভাবনা—",
        ["1/12", "1/6", "1/4", "1/2"],
        ["1/12", "1/6", "1/4", "1/2"],
        "C", "medium", "numerical",
        "Independent: P(H)=1/2, P(even)=1/2 ⇒ P=1/4. (Also 3 favourable of 12 outcomes.)",
        "স্বাধীন: (1/2)×(1/2)=1/4।",
    ),
    q(
        "If P(A)=1/2, P(B)=1/3 and A, B independent, then P(A∩B) is:",
        "P(A)=1/2, P(B)=1/3 এবং A, B স্বাধীন হলে P(A∩B) কত?",
        ["1/6", "5/6", "1/3", "2/3"],
        ["1/6", "5/6", "1/3", "2/3"],
        "A", "easy", "numerical",
        "Independence ⇒ P(A∩B)=P(A)P(B)=(1/2)(1/3)=1/6.",
        "স্বাধীনতায় P(A∩B)=P(A)P(B)=1/6।",
    ),
    q(
        "If P(A)=1/2, P(B)=1/3, P(A∩B)=1/6, then P(A∪B) is:",
        "P(A)=1/2, P(B)=1/3, P(A∩B)=1/6 হলে P(A∪B) কত?",
        ["1/6", "1/2", "2/3", "5/6"],
        ["1/6", "1/2", "2/3", "5/6"],
        "C", "easy", "numerical",
        "P(A∪B)=P(A)+P(B)−P(A∩B)=1/2+1/3−1/6=2/3.",
        "P(A∪B)=1/2+1/3−1/6=2/3।",
    ),
    q(
        "For any events A and B, P(A∪B) equals:",
        "যেকোনো ঘটনা A, B এর জন্য P(A∪B) সমান—",
        ["P(A)+P(B)", "P(A)+P(B)−P(A∩B)", "P(A)P(B)", "P(A)−P(B)"],
        ["মান P(A)+P(B)", "মান P(A)+P(B)−P(A∩B)", "মান P(A)P(B)", "মান P(A)−P(B)"],
        "B", "easy", "factual",
        "Addition theorem: P(A∪B)=P(A)+P(B)−P(A∩B).",
        "যোগসূত্র: P(A∪B)=P(A)+P(B)−P(A∩B)।",
    ),
    q(
        "Probability that a randomly chosen day of a week is Sunday is:",
        "সপ্তাহের দৈব একটি দিন রবিবার হওয়ার সম্ভাবনা—",
        ["1/7", "1/6", "1/5", "2/7"],
        ["1/7", "1/6", "1/5", "2/7"],
        "A", "easy", "numerical",
        "One Sunday among seven days ⇒ 1/7.",
        "৭ দিনে ১ রবিবার ⇒ 1/7।",
    ),
    q(
        "Two fair coins are tossed. P(exactly one head) is:",
        "দুই নিরপেক্ষ মুদ্রা নিক্ষেপে ঠিক এক হেড পাওয়ার সম্ভাবনা—",
        ["1/4", "1/2", "3/4", "1"],
        ["1/4", "1/2", "3/4", "1"],
        "B", "easy", "numerical",
        "Outcomes HH,HT,TH,TT; exactly one head: HT,TH ⇒ 2/4=1/2.",
        "ঠিক এক হেড: HT,TH ⇒ 1/2।",
    ),
    q(
        "Three fair dice are thrown. P(all show the same number) is:",
        "তিন নিরপেক্ষ ছক্কায় প্রতিটিতে একই সংখ্যা উঠার সম্ভাবনা—",
        ["1/36", "1/216", "1/6", "3/216"],
        ["1/36", "1/216", "1/6", "3/216"],
        "A", "medium", "numerical",
        "Favourable: (1,1,1)…(6,6,6) = 6; total 6³ = 216 ⇒ 6/216 = 1/36.",
        "অনুকূল ৬, মোট ২১৬ ⇒ 6/216 = 1/36।",
    ),
    q(
        "If A and B are independent with P(A)=2/5, P(B)=1/2, then P(A∪B) is:",
        "A, B স্বাধীন; P(A)=2/5, P(B)=1/2 হলে P(A∪B) কত?",
        ["1/5", "7/10", "9/10", "4/5"],
        ["1/5", "7/10", "9/10", "4/5"],
        "B", "medium", "numerical",
        "P(A∩B)=(2/5)(1/2)=1/5; P(A∪B)=2/5+1/2−1/5=7/10.",
        "P(A∪B)=2/5+1/2−1/5=7/10।",
    ),
    q(
        "Urn has 3 white and 2 black balls. One ball drawn at random. P(white) is:",
        "পাত্রে 3 সাদা ও 2 কালো বল। দৈব একটি বল তুললে সাদা হওয়ার সম্ভাবনা—",
        ["2/5", "3/5", "1/2", "3/2"],
        ["2/5", "3/5", "1/2", "3/2"],
        "B", "easy", "numerical",
        "P(W)=3/5.",
        "P(W)=3/5।",
    ),
    q(
        "Two urns: first 3W+2B, second 2W+5B. One ball from each. P(at least one white) is:",
        "দুই পাত্র: প্রথম 3W+2B, দ্বিতীয় 2W+5B। প্রত্যেক থেকে একটি করে; কমপক্ষে একটি সাদা—",
        ["2/7", "5/7", "3/7", "4/7"],
        ["2/7", "5/7", "3/7", "4/7"],
        "B", "hard", "application",
        "P(both black)=(2/5)(5/7)=2/7; P(at least one white)=1−2/7=5/7.",
        "P(কমপক্ষে এক সাদা)=1−P(উভয় কালো)=1−(2/5)(5/7)=5/7।",
    ),
    q(
        "P(A)=0.4, P(B)=0.5, P(A∪B)=0.7. Then P(A∩B) is:",
        "P(A)=0.4, P(B)=0.5, P(A∪B)=0.7 হলে P(A∩B) কত?",
        ["0.1", "0.2", "0.3", "0.9"],
        ["0.1", "0.2", "0.3", "0.9"],
        "B", "medium", "numerical",
        "P(A∩B)=P(A)+P(B)−P(A∪B)=0.4+0.5−0.7=0.2.",
        "P(A∩B)=0.4+0.5−0.7=0.2।",
    ),
    q(
        "Which is always true?",
        "নিচের কোনটি সর্বদা সত্য?",
        ["0 ≤ P(A) ≤ 1", "P(A) > 1", "P(A) < 0", "P(A∪A′)=0"],
        ["মান 0 ≤ P(A) ≤ 1", "মান P(A) > 1", "মান P(A) < 0", "মান P(A∪A′)=0"],
        "A", "easy", "conceptual",
        "Axioms of probability require 0 ≤ P(A) ≤ 1.",
        "সম্ভাবনার স্বতঃসিদ্ধ: 0 ≤ P(A) ≤ 1।",
    ),
    q(
        "A card is drawn from a pack of 52. P(ace of spades) is:",
        "৫২ তাসের এক তাস তুললে স্পেডের অ্যাস পাওয়ার সম্ভাবনা—",
        ["1/13", "1/4", "1/52", "4/52"],
        ["1/13", "1/4", "1/52", "4/52"],
        "C", "easy", "numerical",
        "Only one ace of spades ⇒ 1/52.",
        "একমাত্র স্পেড অ্যাস ⇒ 1/52।",
    ),
    q(
        "If A ⊂ B, then which holds?",
        "A ⊂ B হলে কোনটি সত্য?",
        ["P(A) ≥ P(B)", "P(A) ≤ P(B)", "P(A)=P(B) always", "P(A∪B)=0"],
        ["মান P(A) ≥ P(B)", "মান P(A) ≤ P(B)", "সর্বদা P(A)=P(B)", "মান P(A∪B)=0"],
        "B", "medium", "conceptual",
        "If A is subset of B, then P(A) ≤ P(B).",
        "A ⊂ B ⇒ P(A) ≤ P(B)।",
    ),
    q(
        "Two events with P(A)=0.3, P(B)=0.4, P(A∩B)=0.12. Are they independent?",
        "P(A)=0.3, P(B)=0.4, P(A∩B)=0.12 হলে ঘটনাদ্বয় স্বাধীন কি?",
        ["yes, since 0.3×0.4=0.12", "no, product differs", "yes, mutually exclusive", "cannot decide"],
        ["হ্যাঁ, কারণ 0.3×0.4=0.12", "না, গুণফল ভিন্ন", "হ্যাঁ, বর্জনশীল", "নির্ণয় অসম্ভব"],
        "A", "medium", "conceptual",
        "Independence test: P(A)P(B)=0.12=P(A∩B).",
        "P(A)P(B)=P(A∩B) ⇒ স্বাধীন।",
    ),
]


# =============================================================================
# hm2_27_ch10_t03 — Conditional probability / শর্তাধীন সম্ভাবনা
# =============================================================================
T03 = [
    q(
        "Conditional probability P(A|B) is defined as:",
        "শর্তাধীন সম্ভাবনা P(A|B) এর সংজ্ঞা—",
        ["P(A∩B)/P(B), P(B)>0", "P(A∪B)/P(B)", "P(A)/P(B)", "P(B)/P(A)"],
        ["মান P(A∩B)/P(B), P(B)>0", "মান P(A∪B)/P(B)", "মান P(A)/P(B)", "মান P(B)/P(A)"],
        "A", "easy", "factual",
        "By definition P(A|B)=P(A∩B)/P(B) when P(B)>0.",
        "সংজ্ঞা: P(A|B)=P(A∩B)/P(B), P(B)>0।",
    ),
    q(
        "If P(A∩B)=1/6 and P(B)=1/2, then P(A|B) is:",
        "P(A∩B)=1/6 ও P(B)=1/2 হলে P(A|B) কত?",
        ["1/12", "1/6", "1/3", "1/2"],
        ["1/12", "1/6", "1/3", "1/2"],
        "C", "easy", "numerical",
        "P(A|B)=(1/6)/(1/2)=1/3.",
        "P(A|B)=(1/6)/(1/2)=1/3।",
    ),
    q(
        "If A and B are independent, then P(A|B) equals:",
        "A ও B স্বাধীন হলে P(A|B) সমান—",
        ["P(A)", "P(B)", "P(A∩B)", "1"],
        ["মান P(A)", "মান P(B)", "মান P(A∩B)", "মান 1"],
        "A", "easy", "conceptual",
        "Independence ⇒ P(A|B)=P(A).",
        "স্বাধীনতায় P(A|B)=P(A)।",
    ),
    q(
        "P(A)=0.6, P(B)=0.5, P(A∩B)=0.3. Then P(A|B) is:",
        "P(A)=0.6, P(B)=0.5, P(A∩B)=0.3 হলে P(A|B) কত?",
        ["0.3", "0.5", "0.6", "0.8"],
        ["0.3", "0.5", "0.6", "0.8"],
        "C", "easy", "numerical",
        "P(A|B)=0.3/0.5=0.6.",
        "P(A|B)=0.3/0.5=0.6।",
    ),
    q(
        "A bag has 4 red and 6 blue balls. Two drawn without replacement. P(both red) is:",
        "থলে 4 লাল ও 6 নীল বল। বিনা প্রতিস্থাপনে দুইটি তুললে উভয় লাল—",
        ["2/15", "4/25", "6/45", "8/45"],
        ["2/15", "4/25", "6/45", "8/45"],
        "A", "medium", "numerical",
        "P=(4/10)×(3/9)=12/90=2/15.",
        "P=(4/10)(3/9)=2/15।",
    ),
    q(
        "From 5 boys and 3 girls, two chosen at random. P(both girls | at least one girl) is:",
        "5 ছেলে ও 3 মেয়ে থেকে দুইজন; কমপক্ষে এক মেয়ে জেনে উভয় মেয়ে হওয়ার সম্ভাবনা—",
        ["1/6", "3/13", "3/28", "1/7"],
        ["1/6", "3/13", "3/28", "1/7"],
        "A", "hard", "application",
        "P(both girls)=C(3,2)/C(8,2)=3/28; P(≥1 girl)=18/28; P(both|≥1)=(3/28)/(18/28)=1/6.",
        "P(উভয় মেয়ে | ≥1 মেয়ে)=(3/28)/(18/28)=1/6।",
    ),
    q(
        "A die is rolled. Given the number is odd, P(it is 5) is:",
        "ছক্কায় বিজোড় সংখ্যা জেনে তা 5 হওয়ার সম্ভাবনা—",
        ["1/6", "1/3", "1/2", "5/6"],
        ["1/6", "1/3", "1/2", "5/6"],
        "B", "easy", "numerical",
        "Odd = {1,3,5}; P(5|odd)=1/3.",
        "বিজোড় {1,3,5}; P(5|বিজোড়)=1/3।",
    ),
    q(
        "Multiplication rule: P(A∩B) equals:",
        "গুণসূত্র অনুসারে P(A∩B) সমান—",
        ["P(A)·P(B|A)", "P(A)+P(B|A)", "P(A)/P(B|A)", "P(B)−P(A)"],
        ["মান P(A)·P(B|A)", "মান P(A)+P(B|A)", "মান P(A)/P(B|A)", "মান P(B)−P(A)"],
        "A", "easy", "factual",
        "P(A∩B)=P(A)·P(B|A)=P(B)·P(A|B).",
        "P(A∩B)=P(A)·P(B|A)।",
    ),
    q(
        "Two cards drawn without replacement from 52. P(second is ace | first was ace) is:",
        "৫২ তাস থেকে বিনা প্রতিস্থাপনে দুই তাস; প্রথম অ্যাস জেনে দ্বিতীয় অ্যাস—",
        ["3/51", "4/51", "3/52", "4/52"],
        ["3/51", "4/51", "3/52", "4/52"],
        "A", "medium", "numerical",
        "After drawing one ace, 3 aces remain among 51 cards ⇒ 3/51.",
        "এক অ্যাস তোলার পর 51 এ 3 ⇒ 3/51।",
    ),
    q(
        "P(B|A)=0.4, P(A)=0.5. Then P(A∩B) is:",
        "P(B|A)=0.4, P(A)=0.5 হলে P(A∩B) কত?",
        ["0.1", "0.2", "0.4", "0.9"],
        ["0.1", "0.2", "0.4", "0.9"],
        "B", "easy", "numerical",
        "P(A∩B)=P(A)·P(B|A)=0.5×0.4=0.2.",
        "P(A∩B)=0.5×0.4=0.2।",
    ),
    q(
        "If P(A|B)=P(A), then A and B are:",
        "P(A|B)=P(A) হলে A ও B—",
        ["mutually exclusive", "independent", "exhaustive", "impossible"],
        ["বর্জনশীল", "স্বাধীন", "সম্পূর্ণ", "অসম্ভব"],
        "B", "easy", "conceptual",
        "P(A|B)=P(A) is equivalent to independence (when P(B)>0).",
        "P(A|B)=P(A) ⇒ স্বাধীনতা।",
    ),
    q(
        "Box: 5 good, 3 defective items. Two drawn without replacement. P(second defective | first good) is:",
        "বাক্সে 5 ভালো ও 3 ত্রুটিপূর্ণ। বিনা প্রতিস্থাপনে; প্রথম ভালো জেনে দ্বিতীয় ত্রুটিপূর্ণ—",
        ["3/7", "3/8", "5/8", "3/5"],
        ["3/7", "3/8", "5/8", "3/5"],
        "A", "medium", "numerical",
        "After one good removed: 7 left with 3 defective ⇒ 3/7.",
        "এক ভালো তোলার পর 7 এ 3 ত্রুটি ⇒ 3/7।",
    ),
    q(
        "Bayes-type: P(A)=0.4, P(B|A)=0.3, P(B|A′)=0.5. Then P(B) is:",
        "P(A)=0.4, P(B|A)=0.3, P(B|A′)=0.5 হলে P(B) কত?",
        ["0.32", "0.38", "0.42", "0.50"],
        ["0.32", "0.38", "0.42", "0.50"],
        "C", "hard", "application",
        "Total probability: P(B)=P(B|A)P(A)+P(B|A′)P(A′)=0.3·0.4+0.5·0.6=0.12+0.30=0.42.",
        "মোট সম্ভাবনা: P(B)=0.3·0.4+0.5·0.6=0.42।",
    ),
    q(
        "With P(A)=0.4, P(B|A)=0.3, P(B|A′)=0.5, P(A|B) is approximately:",
        "P(A)=0.4, P(B|A)=0.3, P(B|A′)=0.5 হলে P(A|B) প্রায়—",
        ["2/7", "3/7", "4/7", "5/7"],
        ["2/7", "3/7", "4/7", "5/7"],
        "A", "hard", "application",
        "P(A∩B)=0.12; P(B)=0.42; P(A|B)=0.12/0.42=2/7.",
        "P(A|B)=0.12/0.42=2/7।",
    ),
    q(
        "From groups of sizes 5, 12, 18, probability that two randomly selected students are from the same group is:",
        "শ্রেণি আকার 5, 12, 18; দৈব দুই শিক্ষার্থী একই শ্রেণি থেকে হওয়ার সম্ভাবনা—",
        ["229/595", "253/595", "301/595", "325/595"],
        ["229/595", "253/595", "301/595", "325/595"],
        "A", "hard", "numerical",
        "C(5,2)+C(12,2)+C(18,2)=10+66+153=229; C(35,2)=595 ⇒ 229/595.",
        "C(5,2)+C(12,2)+C(18,2)=229; C(35,2)=595 ⇒ 229/595।",
    ),
    q(
        "A family has two children. Given at least one is a boy, P(both boys) is (assume equal likelihood):",
        "দুই সন্তানের পরিবারে কমপক্ষে এক ছেলে জেনে উভয় ছেলে হওয়ার সম্ভাবনা (সমসম্ভাব্য)—",
        ["1/4", "1/3", "1/2", "2/3"],
        ["1/4", "1/3", "1/2", "2/3"],
        "B", "medium", "conceptual",
        "Sample space conditioned on ≥1 boy: {BB,BG,GB}; both boys ⇒ 1/3.",
        "শর্তাধীন নমুনা: {BB,BG,GB}; উভয় ছেলে ⇒ 1/3।",
    ),
    q(
        "P(A∪B)=0.7, P(A)=0.5, P(B)=0.4. Then P(A|B) is:",
        "P(A∪B)=0.7, P(A)=0.5, P(B)=0.4 হলে P(A|B) কত?",
        ["0.2", "0.4", "0.5", "0.8"],
        ["0.2", "0.4", "0.5", "0.8"],
        "C", "medium", "numerical",
        "P(A∩B)=0.5+0.4−0.7=0.2; P(A|B)=0.2/0.4=0.5.",
        "P(A∩B)=0.2; P(A|B)=0.5।",
    ),
    q(
        "Events A and B with P(A)=1/2, P(B)=1/3, P(A|B)=1/2. Then P(B|A) is:",
        "P(A)=1/2, P(B)=1/3, P(A|B)=1/2 হলে P(B|A) কত?",
        ["1/6", "1/3", "1/2", "2/3"],
        ["1/6", "1/3", "1/2", "2/3"],
        "B", "medium", "numerical",
        "P(A∩B)=P(A|B)P(B)=(1/2)(1/3)=1/6; P(B|A)=(1/6)/(1/2)=1/3.",
        "P(B|A)=(1/6)/(1/2)=1/3।",
    ),
    q(
        "Which equals P(A′|B)?",
        "P(A′|B) এর সমান কোনটি?",
        ["1 − P(A|B)", "1 − P(A∪B)", "P(A)/P(B)", "P(B|A′)"],
        ["মান 1 − P(A|B)", "মান 1 − P(A∪B)", "মান P(A)/P(B)", "মান P(B|A′)"],
        "A", "medium", "conceptual",
        "Given B, A and A′ partition ⇒ P(A′|B)=1−P(A|B).",
        "B প্রদত্তে A ও A′ বিভাজন ⇒ P(A′|B)=1−P(A|B)।",
    ),
    q(
        "Three examinees drawn successively from groups 5, 12, 18 (total 35) without replacement. "
        "P(all three from the group of 18) is:",
        "গোষ্ঠী 5, 12, 18 (মোট 35) থেকে পরপর তিনজন; তিনজনই 18-এর গোষ্ঠী থেকে—",
        ["18×17×16/(35×34×33)", "18/35", "18×17×16/(35×35×35)", "3/35"],
        ["মান 18×17×16/(35×34×33)", "মান 18/35", "মান 18×17×16/(35×35×35)", "মান 3/35"],
        "A", "hard", "application",
        "Ordered without replacement: (18/35)(17/34)(16/33).",
        "বিনা প্রতিস্থাপনে (18/35)(17/34)(16/33)।",
    ),
]


def write_topic(topic_id: str, rows: list[dict]) -> dict:
    clean = []
    for i, row in enumerate(rows, 1):
        err = validate_record(row)
        if err:
            raise SystemExit(f"{topic_id}#{i}: {err}")
        clean.append(row)
    path = TOPICS / f"{topic_id}.jsonl"
    path.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in clean) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {path.name}: {len(clean)}")
    return {"path": str(path.relative_to(ROOT)).replace("\\", "/"), "count": len(clean)}


def main() -> None:
    assert len(T01) == 20 and len(T02) == 20 and len(T03) == 20

    counts = {}
    counts["hm2_27_ch10_t01"] = write_topic("hm2_27_ch10_t01", T01)["count"]
    counts["hm2_27_ch10_t02"] = write_topic("hm2_27_ch10_t02", T02)["count"]
    counts["hm2_27_ch10_t03"] = write_topic("hm2_27_ch10_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm2_27_ch10",
        "title_en": "Measures of Dispersion and Probability",
        "title_bn": "বিস্তার পরিমাপ ও সম্ভাবনা",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{i}_pdf{i+6}.png" for i in range(332, 335)],
        "topics": {
            "hm2_27_ch10_t01": {
                "title_en": "Measures of dispersion",
                "title_bn": "বিস্তার পরিমাপ",
                "udvash_types": [
                    "range; mean deviation; quartile deviation QD=(Q3−Q1)/2",
                    "variance σ²=(1/n)Σ(x−x̄)²; SD=√variance; CV=(σ/x̄)×100%",
                    "effect of adding/scaling constants on variance",
                    "consistency via CV; MD minimized about median",
                ],
                "count": 20,
            },
            "hm2_27_ch10_t02": {
                "title_en": "Probability rules",
                "title_bn": "সম্ভাবনার সূত্র",
                "udvash_types": [
                    "classical P=n(A)/n(S); complement P(A′)=1−P(A)",
                    "addition: exclusive P(A∪B)=P(A)+P(B); general −P(A∩B)",
                    "independence P(A∩B)=P(A)P(B); coin/die/card/urn",
                    "at least one white from two urns; three dice same face",
                ],
                "count": 20,
            },
            "hm2_27_ch10_t03": {
                "title_en": "Conditional probability",
                "title_bn": "শর্তাধীন সম্ভাবনা",
                "udvash_types": [
                    "P(A|B)=P(A∩B)/P(B); multiplication rule",
                    "without replacement sequential draws; cards/balls",
                    "total probability and Bayes P(A|B)",
                    "same-group selection; successive examinees from frequency table",
                ],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "garbled_stems": "OCR on pp. 332–334 mostly creative CQ + model-test mix; reconstructed from readable probability/dispersion fragments",
            "figure_only_items": "Urn diagrams and frequency tables rewritten as self-contained text MCQs",
            "broken_option_glyphs": "Fraction glyphs often unreadable; replaced with closed-form HSC standards",
            "thin_mcq_span": "Printed chapter span is short (~3 pages); supplemented with accurate HSC dispersion/probability MCQs",
        },
        "low_confidence": [
            "OCR pages 332–334 noisy; creative-question answer keys used for theme cross-checks (variance, QD, independent events, urns).",
            "Model-test page 334 mixes algebra/geometry; only probability-adjacent stems reused.",
            "Inline math stored as plain text (σ², Q₁, P(A|B), C(n,r)) for JSONL.",
            "Heavy supplementation with board-accurate authored items to reach 20/topic.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm2_ch10.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
        "math2_progress": {
            "topics_complete": "30/30",
            "note": "Ch10 completes higher_mathematics 2nd paper (all 10 chapters / 30 topics / 600Q)",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch10_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()

