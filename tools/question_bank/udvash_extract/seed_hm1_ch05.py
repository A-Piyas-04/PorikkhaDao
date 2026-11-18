#!/usr/bin/env python3
"""Seed Higher Mathematics 1st Paper Ch5 (Permutations and Combinations).

Curated from Udvash HSC Question Bank 2026 printed pp. 180–183 (PDF 186–189).
Writes exactly 20 bilingual JSONL rows per syllabus topic under content/bank/topics/.
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
PARSED = ROOT / "content" / "bank" / "udvash_raw" / "higher_mathematics_1" / "parsed"
SOURCE = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "higher_mathematics p1 ch05; curated bilingual"
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
# hm1_27_ch05_t01 — Counting and factorials / গণনার নীতি ও ফ্যাক্টরিয়াল
# =============================================================================
T01 = [
    q(
        "The value of 0! is:",
        "0! এর মান:",
        ["-infinity", "0", "1", "infinity"],
        ["-অসীম", "0", "1", "অসীম"],
        "C", "easy", "factual",
        "By definition, 0! = 1.",
        "সংজ্ঞা অনুসারে 0! = 1।",
    ),
    q(
        "The value of 5! is:",
        "5! এর মান:",
        ["60", "100", "120", "150"],
        ["60", "100", "120", "150"],
        "C", "easy", "numerical",
        "5! = 5 × 4 × 3 × 2 × 1 = 120.",
        "5! = 5 × 4 × 3 × 2 × 1 = 120।",
    ),
    q(
        "n! / (n - 1)! equals:",
        "n! / (n - 1)! এর মান:",
        ["n - 1", "n", "n + 1", "1"],
        ["n - 1", "n", "n + 1", "1"],
        "B", "easy", "conceptual",
        "n! = n × (n - 1)!, so n! / (n - 1)! = n.",
        "n! = n × (n - 1)! ⇒ ভাগফল n।",
    ),
    q(
        "7! / 5! equals:",
        "7! / 5! এর মান:",
        ["12", "30", "42", "56"],
        ["12", "30", "42", "56"],
        "C", "easy", "numerical",
        "7! / 5! = 7 × 6 = 42.",
        "7! / 5! = 7 × 6 = 42।",
    ),
    q(
        "8! / 6! equals:",
        "8! / 6! এর মান:",
        ["48", "56", "64", "72"],
        ["48", "56", "64", "72"],
        "B", "easy", "numerical",
        "8! / 6! = 8 × 7 = 56.",
        "8! / 6! = 8 × 7 = 56।",
    ),
    q(
        "You forgot the last three digits of a phone number. How many trials guarantee "
        "you dial the correct ending at least once?",
        "মোবাইলের শেষ তিনটি ডিজিট ভুলে গেলে কত প্রকারে চেষ্টা করলে অন্তত একবার সংযোগ পাবে?",
        ["10^2", "9^3", "3^10", "10^3"],
        ["10^2", "9^3", "3^10", "10^3"],
        "D", "easy", "application",
        "Each of 3 digits has 10 choices, so 10 × 10 × 10 = 10^3.",
        "প্রতিটি অঙ্কে 10টি করে পছন্দ ⇒ 10^3।",
    ),
    q(
        "In how many ways can 7 distinct rings be worn on 4 fingers (each ring on one finger)?",
        "৭টি আংটি ৪টি আঙুলে কত উপায়ে পরানো যাবে?",
        ["16384", "16383", "2401", "2400"],
        ["16384", "16383", "2401", "2400"],
        "A", "medium", "application",
        "Each ring has 4 independent choices, so 4^7 = 16384.",
        "প্রতি আংটিতে 4টি পছন্দ ⇒ 4^7 = 16384।",
    ),
    q(
        "The number of positive divisors of 277200 is:",
        "277200 সংখ্যাটির ধনাত্মক উৎপাদকের সংখ্যা:",
        ["25", "187", "180", "90"],
        ["25", "187", "180", "90"],
        "C", "medium", "numerical",
        "277200 = 2^4 × 3^2 × 5^2 × 7 × 11; divisors = 5 × 3 × 3 × 2 × 2 = 180.",
        "277200 = 2^4 × 3^2 × 5^2 × 7 × 11; উৎপাদক সংখ্যা = 180।",
    ),
    q(
        "A student has 6 friends. In how many ways can the student invite one or more of them?",
        "একজন ছাত্রের 6 জন বন্ধু আছে। সে কত রকমে এক বা একাধিক বন্ধুকে নিমন্ত্রণ করতে পারে?",
        ["48", "56", "63", "64"],
        ["48", "56", "63", "64"],
        "C", "medium", "application",
        "Each friend is invited or not: 2^6 = 64, excluding the empty invite gives 64 - 1 = 63.",
        "2^6 - 1 = 63।",
    ),
    q(
        "How many meaningful 3-digit numbers can be formed using the digits 0, 1, 2 "
        "each at most once?",
        "0, 1, 2 অঙ্কগুলোর প্রত্যেকটি প্রতি সংখ্যায় একবার মাত্র ব্যবহার করে কতগুলি "
        "অর্থপূর্ণ তিন অঙ্কের সংখ্যা গঠন করা যায়?",
        ["2", "3", "4", "6"],
        ["2", "3", "4", "6"],
        "C", "medium", "numerical",
        "Total arrangements 3! = 6; exclude those with leading 0 (2! = 2) ⇒ 6 - 2 = 4.",
        "3! - 2! = 4।",
    ),
    q(
        "How many even numbers can be formed by rearranging the digits of 2017 "
        "(using all digits)?",
        "2017 সংখ্যাটির পুনর্বিন্যাসের মধ্যে কয়টি জোড় সংখ্যা?",
        ["9", "10", "11", "12"],
        ["9", "10", "11", "12"],
        "B", "hard", "numerical",
        "Even endings: 0 or 2. Ending 0: 3! = 6. Ending 2 with nonzero lead: 2 × 2! = 4. Total 10.",
        "0 দিয়ে শেষ: 3! = 6; 2 দিয়ে শেষ ও অগ্র অঙ্ক অশূন্য: 4; মোট 10।",
    ),
    q(
        "Four distinct books can be arranged on a shelf in how many ways?",
        "চারটি ভিন্ন বইকে তাকে কতভাবে সাজানো যায়?",
        ["12", "16", "24", "48"],
        ["12", "16", "24", "48"],
        "C", "easy", "factual",
        "Arrangements of 4 distinct objects = 4! = 24.",
        "4! = 24।",
    ),
    q(
        "A multiple-choice test has 5 questions, each with 2 answers (true/false). "
        "How many complete answer sheets are possible?",
        "৫টি প্রশ্নবিশিষ্ট সত্য/মিথ্যা পরীক্ষায় কতগুলি সম্পূর্ণ উত্তরপত্র সম্ভব?",
        ["10", "16", "25", "32"],
        ["10", "16", "25", "32"],
        "D", "easy", "application",
        "Each question has 2 choices ⇒ 2^5 = 32.",
        "প্রতি প্রশ্নে 2টি পছন্দ ⇒ 2^5 = 32।",
    ),
    q(
        "From city A to B there are 3 roads and from B to C there are 4 roads. "
        "In how many ways can one go from A to C via B?",
        "A থেকে B তে 3টি এবং B থেকে C তে 4টি রাস্তা থাকলে A থেকে C তে B হয়ে যাওয়ার উপায় সংখ্যা:",
        ["7", "12", "14", "24"],
        ["7", "12", "14", "24"],
        "B", "easy", "application",
        "By the multiplication principle: 3 × 4 = 12.",
        "গুণন নীতি: 3 × 4 = 12।",
    ),
    q(
        "How many 3-digit numbers can be formed with distinct nonzero digits?",
        "ভিন্ন অশূন্য অঙ্ক দিয়ে কতগুলি তিন অঙ্কের সংখ্যা গঠন করা যায়?",
        ["504", "648", "720", "729"],
        ["504", "648", "720", "729"],
        "A", "medium", "numerical",
        "Digits 1–9, all different: 9 × 8 × 7 = 504.",
        "9 × 8 × 7 = 504।",
    ),
    q(
        "The value of n × (n - 1) × (n - 2) when written with factorials is:",
        "n × (n - 1) × (n - 2) কে ফ্যাক্টরিয়ালে লিখলে:",
        ["n! / (n - 3)!", "n! / (n - 2)!", "(n - 3)!", "n! / 3!"],
        ["n! / (n - 3)!", "n! / (n - 2)!", "(n - 3)!", "n! / 3!"],
        "A", "medium", "conceptual",
        "n! / (n - 3)! = n(n - 1)(n - 2).",
        "n! / (n - 3)! = n(n - 1)(n - 2)।",
    ),
    q(
        "If 10! = 10 × 9 × k!, then k equals:",
        "10! = 10 × 9 × k! হলে k এর মান:",
        ["7", "8", "9", "10"],
        ["7", "8", "9", "10"],
        "B", "easy", "numerical",
        "10! = 10 × 9 × 8!, so k = 8.",
        "10! = 10 × 9 × 8! ⇒ k = 8।",
    ),
    q(
        "A code uses 2 English letters followed by 2 digits (0–9), repetition allowed. "
        "How many codes are possible?",
        "2টি ইংরেজি অক্ষর ও তারপর 2টি অঙ্ক (0–9), পুনরাবৃত্তি চললে মোট কোড সংখ্যা:",
        ["26 × 26 × 10 × 10", "26 × 25 × 10 × 9", "26^2 × 9^2", "52 × 10^2"],
        ["26 × 26 × 10 × 10", "26 × 25 × 10 × 9", "26^2 × 9^2", "52 × 10^2"],
        "A", "medium", "application",
        "Letters: 26 × 26; digits: 10 × 10 ⇒ 26^2 × 10^2.",
        "অক্ষর 26×26, অঙ্ক 10×10।",
    ),
    q(
        "How many ways can 5 people stand in a queue?",
        "5 জন ব্যক্তি এক সারিতে কতভাবে দাঁড়াতে পারে?",
        ["20", "60", "120", "240"],
        ["20", "60", "120", "240"],
        "C", "easy", "factual",
        "Linear arrangements of 5 distinct people = 5! = 120.",
        "5! = 120।",
    ),
    q(
        "Evaluate 4! + 3! + 2! + 1! + 0!:",
        "4! + 3! + 2! + 1! + 0! এর মান:",
        ["33", "34", "35", "36"],
        ["33", "34", "35", "36"],
        "B", "easy", "numerical",
        "24 + 6 + 2 + 1 + 1 = 34.",
        "24 + 6 + 2 + 1 + 1 = 34।",
    ),
]


# =============================================================================
# hm1_27_ch05_t02 — Permutations / বিন্যাস
# =============================================================================
T02 = [
    q(
        "In how many ways can the letters of ABSCISSA be rearranged (excluding the original word)?",
        "ABSCISSA শব্দটির অক্ষরগুলোকে কতভাবে পুনর্বিন্যাস করা যায়?",
        ["719", "3359", "3360", "20159"],
        ["719", "3359", "3360", "20159"],
        "B", "medium", "numerical",
        "8! / (3! × 2!) - 1 = 3360 - 1 = 3359 (S×3, A×2).",
        "8!/(3!×2!) - 1 = 3359।",
    ),
    q(
        "Taking all letters of AMERICA together, how many rearrangements are there "
        "(excluding the original word)?",
        "AMERICA শব্দটির সবগুলি অক্ষর একত্রে নিয়ে কত প্রকারে পুনর্বিন্যাস করা যায়?",
        ["2519", "2520", "5039", "5040"],
        ["2519", "2520", "5039", "5040"],
        "A", "medium", "numerical",
        "7! / 2! - 1 = 2520 - 1 = 2519 (A appears twice).",
        "7!/2! - 1 = 2519।",
    ),
    q(
        "Keeping the vowels of COMBINATION fixed in position, the number of rearrangements is:",
        "COMBINATION শব্দটির স্বরবর্ণের অবস্থান পরিবর্তন না করে পুনর্বিন্যাস সংখ্যা:",
        ["720", "719", "360", "359"],
        ["720", "719", "360", "359"],
        "D", "hard", "numerical",
        "Consonant slots rearrange in 6!/2! = 360 ways; excluding the original ⇒ 359.",
        "ব্যঞ্জনবর্ণের বিন্যাস 6!/2! = 360; পুনর্বিন্যাস 359।",
    ),
    q(
        "How many distinct words can be formed using all letters of BANANA?",
        "BANANA শব্দটির সবগুলো বর্ণ ব্যবহার করে কতগুলো শব্দ গঠন করা যায়?",
        ["720", "120", "60", "6"],
        ["720", "120", "60", "6"],
        "C", "easy", "numerical",
        "6! / (3! × 2!) = 60 (A×3, N×2).",
        "6!/(3!×2!) = 60।",
    ),
    q(
        "How many permutations can be formed using all letters of SESIP?",
        "SESIP শব্দটির সবগুলো অক্ষর ব্যবহার করে কতগুলো বিন্যাস সংখ্যা পাওয়া যায়?",
        ["24", "60", "120", "240"],
        ["24", "60", "120", "240"],
        "B", "easy", "numerical",
        "5! / 2! = 60 (S appears twice).",
        "5!/2! = 60।",
    ),
    q(
        "In how many ways can the letters of Destination be arranged?",
        "Destination শব্দটির বর্ণগুলোকে কত প্রকারে সাজানো যায়?",
        ["11! / 3!", "11! / (2! × 2! × 2!)", "8! / (2! × 2! × 2!)", "8! / 3!"],
        ["11! / 3!", "11! / (2! × 2! × 2!)", "8! / (2! × 2! × 2!)", "8! / 3!"],
        "B", "medium", "numerical",
        "11 letters with t, i, n each twice ⇒ 11! / (2! × 2! × 2!).",
        "t, i, n দুইবার ⇒ 11!/(2!×2!×2!)।",
    ),
    q(
        "In how many ways can 6 boys sit on a bench that has 4 seats?",
        "6 জন বালক 4 আসনের একটি বেঞ্চে কতভাবে বসতে পারে?",
        ["6!", "4!", "6C4", "6P4"],
        ["6!", "4!", "6C4", "6P4"],
        "D", "medium", "conceptual",
        "Choose and arrange 4 of 6: 4! × 6C4 = 6P4.",
        "4! × 6C4 = 6P4।",
    ),
    q(
        "The number of distinct signals from 8 different flags taking 5 at a time is:",
        "8টি ভিন্ন রঙের পতাকা হতে 5টি পতাকা নিয়ে ভিন্ন সিগনাল গঠনের উপায় সংখ্যা:",
        ["8P5", "5!", "8!", "8C5"],
        ["8P5", "5!", "8!", "8C5"],
        "A", "easy", "conceptual",
        "Order matters for signals ⇒ 8P5.",
        "ক্রম গুরুত্বপূর্ণ ⇒ 8P5।",
    ),
    q(
        "Using digits 3, 4, 5, 6, 7 each once, how many 5-digit numbers have 4 in the "
        "2nd place and 6 in the 4th place?",
        "3,4,5,6,7 দ্বারা পাঁচ অঙ্কের কতগুলো সংখ্যায় 4 ও 6 যথাক্রমে দ্বিতীয় ও চতুর্থ স্থানে বসবে?",
        ["120", "60", "12", "6"],
        ["120", "60", "12", "6"],
        "D", "medium", "numerical",
        "After fixing positions of 4 and 6, the remaining 3 digits permute in 3! = 6 ways.",
        "বাকি 3 অঙ্কের বিন্যাস 3! = 6।",
    ),
    q(
        "The value of nP1 is:",
        "nP1 এর মান:",
        ["n - 1", "n", "n + 1", "1"],
        ["n - 1", "n", "n + 1", "1"],
        "B", "easy", "factual",
        "nP1 = n.",
        "nP1 = n।",
    ),
    q(
        "Arranging the letters of 'algebra' with all vowels together gives how many ways?",
        "algebra শব্দটির স্বরবর্ণগুলোকে একত্রে নিয়ে কত প্রকারে বিন্যাস করা যায়?",
        ["2520", "720", "360", "120"],
        ["2520", "720", "360", "120"],
        "C", "hard", "numerical",
        "Treat vowels (a,e,a) as one block: 5! × (3!/2!) = 360.",
        "স্বরবর্ণ এক খণ্ড: 5! × (3!/2!) = 360।",
    ),
    q(
        "Which are true? (i) nPn = n!  (ii) nCr = nC(n-r)  (iii) nPr = nCr × r!",
        "কোনটি সঠিক? (i) nPn = n!  (ii) nCr = nC(n-r)  (iii) nPr = nCr × r!",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "D", "easy", "conceptual",
        "All three standard identities hold.",
        "তিনটি পরিচয়ই সত্য।",
    ),
    q(
        "Keeping vowels fixed, the number of rearrangements of DIFFERENT is:",
        "স্বরবর্ণগুলোর স্থান পরিবর্তন না করে DIFFERENT শব্দটির পুনর্বিন্যাস সংখ্যা:",
        ["720", "719", "360", "359"],
        ["720", "719", "360", "359"],
        "D", "hard", "numerical",
        "Consonant arrangements 6!/2! = 360; rearrangements excluding original ⇒ 359.",
        "6!/2! - 1 = 359।",
    ),
    q(
        "How many distinct arrangements of MATURITY are there?",
        "MATURITY শব্দটির সব অক্ষর ব্যবহার করে কত প্রকারে সাজানো যায়?",
        ["2520", "20160", "5040", "40320"],
        ["2520", "20160", "5040", "40320"],
        "B", "medium", "numerical",
        "8 letters with T twice ⇒ 8!/2! = 20160.",
        "T দুইবার ⇒ 8!/2! = 20160।",
    ),
    q(
        "How many arrangements of INTERNET are possible?",
        "INTERNET শব্দটির অক্ষর কতভাবে সাজানো যায়?",
        ["25200", "151200", "5040", "2520"],
        ["25200", "151200", "5040", "2520"],
        "C", "medium", "numerical",
        "8 letters with N, E, T each twice ⇒ 8! / (2! × 2! × 2!) = 5040.",
        "8!/(2!×2!×2!) = 5040।",
    ),
    q(
        "The number of arrangements of EQUATION is:",
        "EQUATION শব্দটির বিন্যাস সংখ্যা:",
        ["40320", "720", "5040", "40230"],
        ["40320", "720", "5040", "40230"],
        "A", "easy", "numerical",
        "8 distinct letters ⇒ 8! = 40320.",
        "8টি ভিন্ন অক্ষর ⇒ 8! = 40320।",
    ),
    q(
        "How many distinct words can be formed with all letters of MONDAY?",
        "MONDAY শব্দটির বর্ণগুলি নিয়ে কতগুলো ভিন্ন শব্দ গঠন করা যায়?",
        ["120", "720", "600", "119"],
        ["120", "720", "600", "119"],
        "B", "easy", "numerical",
        "6 distinct letters ⇒ 6! = 720.",
        "6! = 720।",
    ),
    q(
        "The number of arrangements of COLLEGE is:",
        "College শব্দটির বিন্যাস সংখ্যা:",
        ["1260", "2520", "5040", "40320"],
        ["1260", "2520", "5040", "40320"],
        "A", "medium", "numerical",
        "7 letters with L×2, E×2 ⇒ 7! / (2! × 2!) = 1260.",
        "7!/(2!×2!) = 1260।",
    ),
    q(
        "Keeping vowels of TRIANGLE fixed, how many rearrangements are there?",
        "TRIANGLE শব্দটির বর্ণগুলোকে স্বরবর্ণের অবস্থান পরিবর্তন না করে কত রকমে পুনরায় সাজানো যায়?",
        ["120", "119", "24", "720"],
        ["120", "119", "24", "720"],
        "B", "hard", "numerical",
        "5 consonants rearrange in 5! = 120 ways; rearrangements ⇒ 120 - 1 = 119.",
        "5! - 1 = 119।",
    ),
    q(
        "If nPr = 240 and nCr = 120, then r equals:",
        "nPr = 240 এবং nCr = 120 হলে r = ?",
        ["5", "2", "1", "3"],
        ["5", "2", "1", "3"],
        "B", "medium", "numerical",
        "nPr = nCr × r! ⇒ 240 = 120 × r! ⇒ r! = 2 ⇒ r = 2.",
        "r! = 2 ⇒ r = 2।",
    ),
]


# =============================================================================
# hm1_27_ch05_t03 — Combinations / সমাবেশ
# =============================================================================
T03 = [
    q(
        "How many triangles can be formed from line segments of lengths 2, 3, 5 and 7 cm?",
        "2, 3, 5 এবং 7 সেমি দৈর্ঘ্যবিশিষ্ট সরলরেখা দ্বারা কতগুলি ত্রিভুজ গঠন করা যায়?",
        ["1", "2", "3", "4"],
        ["1", "2", "3", "4"],
        "A", "medium", "application",
        "Of 4C3 = 4 triples, only (3, 5, 7) satisfies the triangle inequality.",
        "কেবল (3, 5, 7) ত্রিভুজ অসমতা মেনে চলে।",
    ),
    q(
        "If nC10 = nC6, then n equals:",
        "nC10 = nC6 হলে n এর মান:",
        ["4", "6", "10", "16"],
        ["4", "6", "10", "16"],
        "D", "easy", "conceptual",
        "nCx = nCy ⇒ x + y = n ⇒ 10 + 6 = 16.",
        "10 + 6 = n ⇒ n = 16।",
    ),
    q(
        "How many diagonals does a 6-sided polygon have?",
        "6 বাহুবিশিষ্ট একটি বহুভুজের কতটি কর্ণ আছে?",
        ["2", "6", "9", "12"],
        ["2", "6", "9", "12"],
        "C", "easy", "numerical",
        "Diagonals = 6C2 - 6 = 15 - 6 = 9.",
        "6C2 - 6 = 9।",
    ),
    q(
        "If nC5 = nC7, then n equals:",
        "nC5 = nC7 হলে n এর মান:",
        ["2", "7", "12", "35"],
        ["2", "7", "12", "35"],
        "C", "easy", "conceptual",
        "5 + 7 = n ⇒ n = 12.",
        "5 + 7 = 12।",
    ),
    q(
        "The number of diagonals of a 10-sided planar figure is:",
        "10 বাহুবিশিষ্ট সমতলিক ক্ষেত্রের কর্ণের সংখ্যা:",
        ["35", "45", "80", "90"],
        ["35", "45", "80", "90"],
        "A", "easy", "numerical",
        "10C2 - 10 = 45 - 10 = 35.",
        "10C2 - 10 = 35।",
    ),
    q(
        "The complementary combination of nCr is:",
        "nCr এর সম্পূরক সমাবেশ:",
        ["nC(n-r)", "nCr-1", "n+1Cr", "nPr"],
        ["nC(n-r)", "nCr-1", "n+1Cr", "nPr"],
        "A", "easy", "factual",
        "nCr = nC(n-r); the complement selects the remaining n - r items.",
        "সম্পূরক = nC(n-r)।",
    ),
    q(
        "For the word DOMAIN, which are true? "
        "(i) rearrangements = 719  "
        "(ii) permutations with vowels fixed = 6  "
        "(iii) number of combinations of all letters = 6!",
        "DOMAIN শব্দটির ক্ষেত্রে কোনটি সঠিক? "
        "(i) পুনর্বিন্যাস সংখ্যা 719  "
        "(ii) স্বরবর্ণের অবস্থান অপরিবর্তিত রেখে বিন্যাস = 6  "
        "(iii) সমাবেশ সংখ্যা = 6!",
        ["i and ii", "ii and iii", "i and iii", "i, ii and iii"],
        ["i ও ii", "ii ও iii", "i ও iii", "i, ii ও iii"],
        "A", "hard", "conceptual",
        "(i) 6! - 1 = 719. (ii) 3! = 6 for consonants. (iii) 6C6 = 1, not 6!. So i and ii.",
        "(iii) মিথ্যা; i ও ii সত্য।",
    ),
    q(
        "The value of 12C0 is:",
        "12C0 এর মান:",
        ["0", "1", "12", "144"],
        ["0", "1", "12", "144"],
        "B", "easy", "factual",
        "nC0 = 1 for every n.",
        "nC0 = 1।",
    ),
    q(
        "Which are true for permutations and combinations? "
        "(i) nCr = nC(n-r)  "
        "(ii) nCr + nC(r-1) = (n+1)Cr  "
        "(iii) r! × nCr = nPr",
        "বিন্যাস ও সমাবেশের ক্ষেত্রে কোনটি সঠিক? "
        "(i) nCr = nC(n-r)  "
        "(ii) nCr + nC(r-1) = (n+1)Cr  "
        "(iii) r! × nCr = nPr",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "D", "medium", "conceptual",
        "All three identities are standard and true.",
        "তিনটিই সত্য।",
    ),
    q(
        "How many combinations can be formed taking any two letters from the word GOOD?",
        "GOOD শব্দটির যে কোন দুইটি বর্ণ নিয়ে কয়টি সমাবেশ গঠন করা যায়?",
        ["3", "4", "5", "6"],
        ["3", "4", "5", "6"],
        "B", "medium", "numerical",
        "Distinct pairs: {G,O}, {G,D}, {O,D}, {O,O} ⇒ 3C2 + 1 = 4.",
        "3C2 + 1 = 4।",
    ),
    q(
        "The number of diagonals of a heptagon (7 sides) is:",
        "7 বাহুবিশিষ্ট একটি বহুভুজের কর্ণের সংখ্যা:",
        ["14", "21", "35", "42"],
        ["14", "21", "35", "42"],
        "A", "easy", "numerical",
        "7C2 - 7 = 21 - 7 = 14.",
        "7C2 - 7 = 14।",
    ),
    q(
        "In how many ways can 6 students be divided into two groups of 3?",
        "6 জন শিক্ষার্থীকে সমান সংখ্যক শিক্ষার্থীর দুইটি দলে কত রকমে বিভক্ত করা যায়?",
        ["10", "20", "60", "120"],
        ["10", "20", "60", "120"],
        "B", "medium", "numerical",
        "Choose 3 of 6 for one group: 6C3 = 20 (groups labeled as in the printed key).",
        "6C3 = 20।",
    ),
    q(
        "The number of diagonals of a 16-sided polygon is:",
        "16 ভুজবিশিষ্ট একটি সমতলিক ক্ষেত্রের কর্ণের সংখ্যা:",
        ["240", "224", "120", "104"],
        ["240", "224", "120", "104"],
        "D", "medium", "numerical",
        "16C2 - 16 = 120 - 16 = 104.",
        "16C2 - 16 = 104।",
    ),
    q(
        "The number of diagonals of a 12-sided polygon is:",
        "12 বাহুবিশিষ্ট বহুভুজের কর্ণের সংখ্যা:",
        ["220", "54", "66", "12"],
        ["220", "54", "66", "12"],
        "B", "easy", "numerical",
        "12C2 - 12 = 66 - 12 = 54.",
        "12C2 - 12 = 54।",
    ),
    q(
        "If nC2 = 496, then n equals:",
        "nC2 = 496 হলে n এর মান:",
        ["16", "24", "31", "32"],
        ["16", "24", "31", "32"],
        "D", "medium", "numerical",
        "n(n - 1)/2 = 496 ⇒ n(n - 1) = 992 ⇒ n = 32.",
        "n(n - 1) = 992 ⇒ n = 32।",
    ),
    q(
        "If 2nCr = 2nC(r+2), then r equals:",
        "2nCr = 2nC(r+2) হলে r এর মান:",
        ["n + 1", "n - 1", "n + 2", "n - 2"],
        ["n + 1", "n - 1", "n + 2", "n - 2"],
        "B", "hard", "conceptual",
        "r + (r + 2) = 2n ⇒ 2r + 2 = 2n ⇒ r = n - 1.",
        "2r + 2 = 2n ⇒ r = n - 1।",
    ),
    q(
        "The greatest value of 12Cr is:",
        "12Cr এর বৃহত্তম মান:",
        ["924", "925", "792", "495"],
        ["924", "925", "792", "495"],
        "A", "medium", "numerical",
        "For even n = 12, max is 12C6 = 924.",
        "12C6 = 924।",
    ),
    q(
        "If r = n, then nCr equals:",
        "r = n হলে nCr = ?",
        ["0", "1", "n", "r!"],
        ["0", "1", "n", "r!"],
        "B", "easy", "factual",
        "nCn = 1.",
        "nCn = 1।",
    ),
    q(
        "How many triangles can be formed from segments of lengths 1, 2, 3, 4?",
        "1, 2, 3, 4 দৈর্ঘ্যবিশিষ্ট সরলরেখা দ্বারা কয়টি ত্রিভুজ গঠন করা যাবে?",
        ["4", "3", "2", "1"],
        ["4", "3", "2", "1"],
        "D", "medium", "application",
        "Only (2, 3, 4) satisfies the triangle inequality.",
        "কেবল (2, 3, 4) সম্ভব।",
    ),
    q(
        "If nC6 + nC5 = 210, then n equals:",
        "nC6 + nC5 = 210 হলে n এর মান:",
        ["7", "8", "9", "10"],
        ["7", "8", "9", "10"],
        "C", "hard", "numerical",
        "nC6 + nC5 = (n+1)C6 = 210 = 10C6 ⇒ n + 1 = 10 ⇒ n = 9.",
        "(n+1)C6 = 210 ⇒ n = 9।",
    ),
]


def write_topic(topic_id: str, rows: list[dict]) -> dict:
    if len(rows) != 20:
        raise SystemExit(f"{topic_id}: expected 20 rows, got {len(rows)}")
    clean = []
    for i, r in enumerate(rows, 1):
        err = validate_record(r)
        if err:
            raise SystemExit(f"{topic_id}#{i}: {err}\n{json.dumps(r, ensure_ascii=False)[:400]}")
        clean.append(r)
    stems = [r["stem_en"] for r in clean]
    if len(set(map(str.casefold, stems))) != 20:
        raise SystemExit(f"{topic_id}: duplicate stems")
    path = TOPICS / f"{topic_id}.jsonl"
    path.write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in clean) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {path.name}: {len(clean)}")
    return {"path": str(path.relative_to(ROOT)).replace("\\", "/"), "count": len(clean)}


def main() -> None:
    # Remove near-duplicate combination identity that appears twice with same stem family
    assert len(T01) == 20 and len(T02) == 20 and len(T03) == 20
    counts = {}
    counts["hm1_27_ch05_t01"] = write_topic("hm1_27_ch05_t01", T01)["count"]
    counts["hm1_27_ch05_t02"] = write_topic("hm1_27_ch05_t02", T02)["count"]
    counts["hm1_27_ch05_t03"] = write_topic("hm1_27_ch05_t03", T03)["count"]

    all_stems = []
    for tid in counts:
        for line in (TOPICS / f"{tid}.jsonl").read_text(encoding="utf-8").splitlines():
            all_stems.append(json.loads(line)["stem_en"].casefold())
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stems across topics")

    summary = {
        "chapter": "hm1_27_ch05",
        "title_en": "Permutations and Combinations",
        "title_bn": "বিন্যাস ও সমাবেশ",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [f"p{str(i).zfill(3)}_pdf{str(i+6).zfill(3)}.png" for i in range(180, 184)],
        "topics": {
            "hm1_27_ch05_t01": {
                "title_en": "Counting and factorials",
                "title_bn": "গণনার নীতি ও ফ্যাক্টরিয়াল",
                "udvash_types": ["factorials", "multiplication principle", "digit codes"],
                "count": 20,
            },
            "hm1_27_ch05_t02": {
                "title_en": "Permutations",
                "title_bn": "বিন্যাস",
                "udvash_types": ["T-02", "T-03", "word rearrangements", "nPr"],
                "count": 20,
            },
            "hm1_27_ch05_t03": {
                "title_en": "Combinations",
                "title_bn": "সমাবেশ",
                "udvash_types": ["T-05", "T-08", "nCr identities", "diagonals", "triangles"],
                "count": 20,
            },
        },
        "counts": {**counts, "total": sum(counts.values())},
        "skipped_faulty": {
            "Q01_triangles_printed": "Printed options 2/3/4/24 but true count is 1; curated with option 1",
            "Q12_equal_parts": "60 items into 4 equal unlabeled groups OCR options garbled; skipped",
            "Q26_cube_colors": "Printed multi-select C6/6!/P6 contradicts rotation-aware key 30; skipped",
            "Q28_2n_split": "OCR options unreadable; skipped",
            "Q36_derangement": "Printed key 12 for !4 letters; true !4=9; skipped rather than keep wrong key",
            "Q41_necklace": "Fraction options OCR garbled; skipped",
            "Q42_maturity_claims": "Printed (ii) 5040 contradicts 7!/2!=2520; skipped multi-claim item",
            "Q45_sum_ocr": "Stem °C+°C+70 unreadable; skipped",
            "Q48_nC12": "If nC12=nC8 then n=20 but printed 20C2 options mismatched; skipped",
            "Q53_examinee": "Stem/working mismatch (1+5C1+5C2=16 vs 'any 4 letters'); skipped",
        },
        "low_confidence": [
            "ABSCISSA/AMERICA/COMBINATION/DIFFERENT/TRIANGLE use board-style পুনর্বিন্যাস = total - 1.",
            "6 students into two groups of 3 kept as 6C3=20 per printed উত্তরমালা (groups treated distinguishable).",
            "Inline math stored as plain text (nCr, nPr, n!, ^) for JSONL.",
            "Sparse OCR on pp. 182–183; several items authored as accurate HSC-level supplements.",
        ],
        "validate": {
            "seed_command": "python tools/question_bank/udvash_extract/seed_hm1_ch05.py",
            "bank_command": "python tools/question_bank/pipeline/bank.py validate",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": counts,
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch05_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
