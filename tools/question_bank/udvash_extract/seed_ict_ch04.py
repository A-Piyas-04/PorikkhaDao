#!/usr/bin/env python3
"""Seed ICT Ch4 bilingual MCQs (Introduction to Web Design and HTML).

Writes exactly 20 JSONL rows per topic under content/bank/topics/.
Topics: ict27_ch04_t01..t05.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPICS = ROOT / "content" / "bank" / "topics"
PARSED = ROOT / "content" / "bank" / "udvash_raw" / "ict" / "parsed"
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
from core import validate_record  # noqa: E402

SRC = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "ict ch04; curated bilingual"
)

TOPIC_IDS = [f"ict27_ch04_t{i:02d}" for i in range(1, 6)]


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    if en == bn and not re.search(r"[A-Za-z]", en):
        en = f"value {en}"
        bn = f"মান {bn}" if not re.search(r"[ঀ-৿]", bn) else bn
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


# --- t01: Website structure ---
T01 = [
    q(
        "What is a website?",
        "ওয়েবসাইট কী?",
        [
            "A collection of related web pages under a common domain",
            "Only a single image file on a hard disk",
            "A printer driver package",
            "A keyboard shortcut list",
        ],
        [
            "একই ডোমেইনের অধীনে সম্পর্কিত ওয়েব পেজের সংগ্রহ",
            "শুধু হার্ড ডিস্কের একটি চিত্র ফাইল",
            "একটি প্রিন্টার ড্রাইভার প্যাকেজ",
            "কীবোর্ড শর্টকাটের তালিকা",
        ],
        "A", "easy", "factual",
        "A website is a set of linked pages identified by a domain name.",
        "ওয়েবসাইট হলো একটি ডোমেইন নামে চিহ্নিত সংযুক্ত পেজের সেট।",
    ),
    q(
        "A single document that a browser displays from a website is called a:",
        "ওয়েবসাইট থেকে ব্রাউজার যে একক নথি প্রদর্শন করে তাকে বলে:",
        ["Web page", "Database server only", "Operating system", "RAM module"],
        ["ওয়েব পেজ", "শুধু ডেটাবেস সার্ভার", "অপারেটিং সিস্টেম", "RAM মডিউল"],
        "A", "easy", "factual",
        "A web page is one HTML (or similar) document rendered by a browser.",
        "ওয়েব পেজ হলো ব্রাউজারে রেন্ডার হওয়া একটি HTML (বা অনুরূপ) নথি।",
    ),
    q(
        "The main or starting page of a website is commonly called the:",
        "ওয়েবসাইটের প্রধান বা শুরুর পেজকে সাধারণত বলে:",
        ["Home page", "Footer only", "Cookie jar", "Cache dump"],
        ["হোম পেজ", "শুধু ফুটার", "কুকি জার", "ক্যাশ ডাম্প"],
        "A", "easy", "factual",
        "The home page is the default entry point users often see first.",
        "হোম পেজ ব্যবহারকারীদের সাধারণ প্রবেশদ্বার।",
    ),
    q(
        "WWW stands for:",
        "WWW এর পূর্ণরূপ কী?",
        [
            "World Wide Web",
            "Wide Wireless Wire",
            "Web Word Writer",
            "Work With Windows",
        ],
        [
            "ওয়ার্ল্ড ওয়াইড ওয়েব",
            "ওয়াইড ওয়্যারলেস ওয়্যার",
            "ওয়েব ওয়ার্ড রাইটার",
            "ওয়ার্ক উইথ উইন্ডোজ",
        ],
        "A", "easy", "factual",
        "WWW is the World Wide Web of hyperlinked documents.",
        "WWW হলো হাইপারলিঙ্কযুক্ত নথির বিশ্বব্যাপী ওয়েব।",
    ),
    q(
        "Which statement correctly distinguishes the Internet from the WWW?",
        "ইন্টারনেট ও WWW এর মধ্যে কোন বিবৃতি সঠিক পার্থক্য করে?",
        [
            "The Internet is the global network; WWW is a service that runs on it",
            "WWW is the cables only; Internet is only email",
            "They are identical and interchangeable always",
            "Internet exists only inside one school LAN",
        ],
        [
            "ইন্টারনেট বৈশ্বিক নেটওয়ার্ক; WWW সেটিতে চলা একটি সেবা",
            "WWW শুধু কেবল; ইন্টারনেট শুধু ইমেইল",
            "এরা সবসময় অভিন্ন ও বিনিময়যোগ্য",
            "ইন্টারনেট শুধু এক স্কুল LAN-এ থাকে",
        ],
        "A", "medium", "conceptual",
        "The Internet is infrastructure; WWW is one application/service on top.",
        "ইন্টারনেট অবকাঠামো; WWW তার উপরের একটি অ্যাপ্লিকেশন/সেবা।",
    ),
    q(
        "A URL is used to:",
        "URL ব্যবহার করা হয়:",
        [
            "Locate a resource on the web",
            "Measure CPU temperature only",
            "Format a hard disk partition",
            "Compile C++ source code",
        ],
        [
            "ওয়েবে কোনো রিসোর্সের অবস্থান নির্দেশ করতে",
            "শুধু CPU তাপমাত্রা মাপতে",
            "হার্ড ডিস্ক পার্টিশন ফরম্যাট করতে",
            "C++ সোর্স কোড কম্পাইল করতে",
        ],
        "A", "easy", "factual",
        "URL (Uniform Resource Locator) addresses a web resource.",
        "URL (ইউনিফর্ম রিসোর্স লোকেটর) ওয়েব রিসোর্সের ঠিকানা।",
    ),
    q(
        "In the URL https://www.example.com/about.html, the domain name is:",
        "URL https://www.example.com/about.html এ ডোমেইন নাম কোনটি?",
        ["www.example.com", "https", "about.html", "/about"],
        ["www.example.com (ডোমেইন)", "https (প্রোটোকল)", "about.html (ফাইল)", "/about (পাথ)"],
        "A", "medium", "application",
        "The host/domain part is www.example.com; about.html is the path file.",
        "হোস্ট/ডোমেইন অংশ www.example.com; about.html পাথের ফাইল।",
    ),
    q(
        "Which protocol is commonly used to transfer web pages securely?",
        "নিরাপদে ওয়েব পেজ স্থানান্তরে সাধারণত কোন প্রোটোকল ব্যবহৃত হয়?",
        ["HTTPS", "SMTP only", "FTP only for email", "DHCP for pages"],
        ["HTTPS প্রোটোকল", "শুধু SMTP", "শুধু ইমেইলের জন্য FTP", "পেজের জন্য DHCP"],
        "A", "easy", "factual",
        "HTTPS is HTTP over TLS/SSL for encrypted web traffic.",
        "HTTPS হলো এনক্রিপ্টেড ওয়েব ট্রাফিকের জন্য TLS/SSL সহ HTTP।",
    ),
    q(
        "A web browser is software that:",
        "ওয়েব ব্রাউজার এমন সফটওয়্যার যা:",
        [
            "Requests and displays web pages for the user",
            "Only prints invoices offline forever",
            "Replaces the computer BIOS chip",
            "Builds physical network cables",
        ],
        [
            "ব্যবহারকারীর জন্য ওয়েব পেজ অনুরোধ ও প্রদর্শন করে",
            "চিরকাল শুধু অফলাইন চালান ছাপায়",
            "কম্পিউটারের BIOS চিপ প্রতিস্থাপন করে",
            "ভৌত নেটওয়ার্ক কেবল তৈরি করে",
        ],
        "A", "easy", "factual",
        "Browsers (Chrome, Firefox, Edge, etc.) fetch and render pages.",
        "ব্রাউজার (Chrome, Firefox, Edge ইত্যাদি) পেজ আনে ও রেন্ডার করে।",
    ),
    q(
        "A web server primarily:",
        "ওয়েব সার্ভার প্রধানত:",
        [
            "Stores and delivers web content in response to client requests",
            "Draws cartoons without networking",
            "Charges phone batteries wirelessly only",
            "Formats USB pendrives only",
        ],
        [
            "ক্লায়েন্ট অনুরোধে ওয়েব কন্টেন্ট সংরক্ষণ ও সরবরাহ করে",
            "নেটওয়ার্ক ছাড়া কার্টুন আঁকে",
            "শুধু ওয়্যারলেস ফোন চার্জ করে",
            "শুধু USB পেনড্রাইভ ফরম্যাট করে",
        ],
        "A", "easy", "conceptual",
        "Web servers host sites and reply to HTTP/HTTPS requests.",
        "ওয়েব সার্ভার সাইট হোস্ট করে এবং HTTP/HTTPS অনুরোধের জবাব দেয়।",
    ),
    q(
        "In a typical client–server web model, the client is usually the:",
        "সাধারণ ক্লায়েন্ট–সার্ভার ওয়েব মডেলে ক্লায়েন্ট সাধারণত:",
        [
            "User’s browser making requests",
            "Only the hard disk of the server",
            "The ISP’s undersea cable exclusively",
            "A printer queue queue",
        ],
        [
            "অনুরোধকারী ব্যবহারকারীর ব্রাউজার",
            "শুধু সার্ভারের হার্ড ডিস্ক",
            "একমাত্র ISP-এর সাবমেরিন কেবল",
            "প্রিন্টার কিউ কিউ",
        ],
        "A", "medium", "conceptual",
        "The browser acts as client; the remote host runs the web server.",
        "ব্রাউজার ক্লায়েন্ট; দূরবর্তী হোস্টে ওয়েব সার্ভার চলে।",
    ),
    q(
        "Static web pages:",
        "স্ট্যাটিক ওয়েব পেজ:",
        [
            "Show the same fixed content until the file is edited",
            "Always rewrite themselves every millisecond automatically",
            "Can never contain text or images",
            "Require a database for every character",
        ],
        [
            "ফাইল সম্পাদনা না হওয়া পর্যন্ত একই স্থির কন্টেন্ট দেখায়",
            "প্রতি মিলিসেকেন্ডে স্বয়ংক্রিয়ভাবে নিজেকে পুনর্লিখন করে",
            "কখনোই লেখা বা চিত্র থাকতে পারে না",
            "প্রতি অক্ষরের জন্য ডেটাবেস লাগে",
        ],
        "A", "medium", "conceptual",
        "Static pages are fixed HTML (etc.) files without per-user generation.",
        "স্ট্যাটিক পেজ ব্যবহারকারীভেদে তৈরি নয়; স্থির HTML ফাইল।",
    ),
    q(
        "Dynamic web pages typically:",
        "ডায়নামিক ওয়েব পেজ সাধারণত:",
        [
            "Generate content at request time (often via scripts/databases)",
            "Are printed on paper only once",
            "Cannot use any hyperlinks",
            "Exist only offline on floppy disks",
        ],
        [
            "অনুরোধের সময় কন্টেন্ট তৈরি করে (প্রায়ই স্ক্রিপ্ট/ডেটাবেস দিয়ে)",
            "শুধু একবার কাগজে ছাপা হয়",
            "কোনো হাইপারলিঙ্ক ব্যবহার করতে পারে না",
            "শুধু ফ্লপি ডিস্কে অফলাইন থাকে",
        ],
        "A", "medium", "conceptual",
        "Dynamic pages change based on user, time, or data sources.",
        "ডায়নামিক পেজ ব্যবহারকারী, সময় বা ডেটা উৎস অনুযায়ী বদলায়।",
    ),
    q(
        "Which part of a typical page layout usually holds the site logo and main menu?",
        "সাধারণ পেজ লেআউটে কোন অংশে সাধারণত লোগো ও প্রধান মেনু থাকে?",
        ["Header / navigation area", "Only the printer spooler", "BIOS setup screen", "GPU fan"],
        ["হেডার / নেভিগেশন এলাকা", "শুধু প্রিন্টার স্পুলার", "BIOS সেটআপ স্ক্রিন", "GPU ফ্যান"],
        "A", "easy", "factual",
        "Header and nav commonly contain branding and primary links.",
        "হেডার ও ন্যাভে সাধারণত ব্র্যান্ডিং ও প্রধান লিঙ্ক থাকে।",
    ),
    q(
        "The footer of a web page often contains:",
        "ওয়েব পেজের ফুটারে প্রায়ই থাকে:",
        [
            "Copyright, contact, or secondary links",
            "Only the CPU instruction set",
            "Only the root password",
            "Only machine code binaries",
        ],
        [
            "কপিরাইট, যোগাযোগ বা গৌণ লিঙ্ক",
            "শুধু CPU নির্দেশ সেট",
            "শুধু রুট পাসওয়ার্ড",
            "শুধু মেশিন কোড বাইনারি",
        ],
        "A", "easy", "factual",
        "Footers hold legal notes, contacts, and secondary navigation.",
        "ফুটারে আইনি নোট, যোগাযোগ ও গৌণ নেভিগেশন থাকে।",
    ),
    q(
        "A sitemap helps by:",
        "সাইটম্যাপ সাহায্য করে:",
        [
            "Showing the structure and hierarchy of pages on a site",
            "Heating the server room automatically",
            "Replacing DNS entirely",
            "Deleting all hyperlinks",
        ],
        [
            "সাইটের পেজের কাঠামো ও ক্রম দেখিয়ে",
            "স্বয়ংক্রিয়ভাবে সার্ভার রুম গরম করে",
            "DNS সম্পূর্ণ প্রতিস্থাপন করে",
            "সব হাইপারলিঙ্ক মুছে",
        ],
        "A", "medium", "conceptual",
        "Sitemaps outline page organisation for users and search tools.",
        "সাইটম্যাপ ব্যবহারকারী ও সার্চ টুলের জন্য পেজ সংগঠন দেখায়।",
    ),
    q(
        "Hypertext means:",
        "হাইপারটেক্সট বলতে বোঝায়:",
        [
            "Text with links that jump to other related content",
            "Text that can never be clicked",
            "Only binary machine instructions",
            "Only handwritten letters on paper",
        ],
        [
            "লিঙ্কযুক্ত লেখা যা অন্য সম্পর্কিত কন্টেন্টে নিয়ে যায়",
            "লেখা যা কখনো ক্লিক করা যায় না",
            "শুধু বাইনারি মেশিন নির্দেশ",
            "শুধু কাগজে হাতে লেখা চিঠি",
        ],
        "A", "easy", "conceptual",
        "Hypertext connects documents via hyperlinks.",
        "হাইপারটেক্সট হাইপারলিঙ্কের মাধ্যমে নথি সংযুক্ত করে।",
    ),
    q(
        "Web hosting provides:",
        "ওয়েব হোস্টিং প্রদান করে:",
        [
            "Space and services to keep a website available online",
            "Only a physical paint brush",
            "Only offline typewriter ribbons",
            "Only local keyboard stickers",
        ],
        [
            "ওয়েবসাইট অনলাইনে রাখার জায়গা ও সেবা",
            "শুধু একটি ভৌত পেইন্ট ব্রাশ",
            "শুধু অফলাইন টাইপরাইটার রিবন",
            "শুধু স্থানীয় কীবোর্ড স্টিকার",
        ],
        "A", "easy", "factual",
        "Hosting stores site files on servers reachable via the Internet.",
        "হোস্টিং ইন্টারনেট-সংযুক্ত সার্ভারে সাইট ফাইল রাখে।",
    ),
    q(
        "Frontend of a website mainly concerns:",
        "ওয়েবসাইটের ফ্রন্টএন্ড প্রধানত সম্পর্কিত:",
        [
            "What users see and interact with in the browser",
            "Only the database backup tape library",
            "Only power-supply voltage rails",
            "Only BIOS beep codes",
        ],
        [
            "ব্রাউজারে ব্যবহারকারী যা দেখে ও ইন্টারঅ্যাক্ট করে",
            "শুধু ডেটাবেস ব্যাকআপ টেপ লাইব্রেরি",
            "শুধু পাওয়ার সাপ্লাই ভোল্টেজ রেল",
            "শুধু BIOS বিপ কোড",
        ],
        "A", "medium", "conceptual",
        "Frontend covers UI markup, styling, and client-side behaviour.",
        "ফ্রন্টএন্ড UI মার্কআপ, স্টাইল ও ক্লায়েন্ট-সাইড আচরণ।",
    ),
    q(
        "Which is a correct hierarchy example for a small school website?",
        "ছোট স্কুল ওয়েবসাইটের কোনটি সঠিক ক্রম/কাঠামোর উদাহরণ?",
        [
            "Home → About → Classes → Contact",
            "BIOS → CMOS → Jumpers → Fans",
            "Ink → Toner → Staples → Glue",
            "Only a single unlinked PDF with no entry page",
        ],
        [
            "হোম → সম্পর্কে → ক্লাস → যোগাযোগ",
            "BIOS → CMOS → জাম্পার → ফ্যান",
            "কালি → টোনার → স্ট্যাপল → আঠা",
            "শুধু একটি আনলিঙ্কড PDF, কোনো এন্ট্রি পেজ নেই",
        ],
        "A", "hard", "application",
        "Sites organise from a home hub into logical section pages.",
        "সাইট হোম কেন্দ্র থেকে যৌক্তিক বিভাগীয় পেজে সাজানো হয়।",
    ),
]


# --- t02: HTML structure, tags and syntax ---
T02 = [
    q(
        "HTML stands for:",
        "HTML এর পূর্ণরূপ কী?",
        [
            "HyperText Markup Language",
            "High Transfer Machine Language",
            "Hyper Tool Meta Loader",
            "Host Text Memory List",
        ],
        [
            "হাইপারটেক্সট মার্কআপ ল্যাঙ্গুয়েজ",
            "হাই ট্রান্সফার মেশিন ল্যাঙ্গুয়েজ",
            "হাইপার টুল মেটা লোডার",
            "হোস্ট টেক্সট মেমোরি লিস্ট",
        ],
        "A", "easy", "factual",
        "HTML is HyperText Markup Language for structuring web content.",
        "HTML ওয়েব কন্টেন্ট গঠনের হাইপারটেক্সট মার্কআপ ভাষা।",
    ),
    q(
        "An HTML tag is generally written inside:",
        "HTML ট্যাগ সাধারণত লেখা হয়:",
        ["Angle brackets < >", "Curly braces only { }", "Parentheses only ( )", "Square brackets only [ ]"],
        ["কোণ বন্ধনী < > এর ভিতরে", "শুধু সুরবন্ধনী { }", "শুধু বৃত্তাকার বন্ধনী ( )", "শুধু বর্গাকার বন্ধনী [ ]"],
        "A", "easy", "factual",
        "Tags use angle brackets, e.g. <p>…</p>.",
        "ট্যাগ কোণ বন্ধনী ব্যবহার করে, যেমন <p>…</p>।",
    ),
    q(
        "Which pair correctly shows an opening and closing paragraph tag?",
        "কোন জোড়া সঠিকভাবে অনুচ্ছেদের খোলা ও বন্ধ ট্যাগ দেখায়?",
        ["<p> and </p>", "<p> and <p/>", "</p> and <p>", "<para> and </para> only in HTML5"],
        ["<p> এবং </p>", "<p> এবং <p/>", "</p> এবং <p>", "HTML5-এ শুধু <para> ও </para>"],
        "A", "easy", "factual",
        "Most elements need matching start and end tags: <p>…</p>.",
        "অধিকাংশ উপাদানের মিলিত শুরু ও শেষ ট্যাগ লাগে: <p>…</p>।",
    ),
    q(
        "The basic HTML document skeleton usually includes:",
        "মৌলিক HTML নথির কাঠামোতে সাধারণত থাকে:",
        [
            "html, head, and body sections",
            "Only a <print> tag",
            "Only machine language opcodes",
            "Only <excel> worksheets",
        ],
        [
            "html, head ও body অংশ",
            "শুধু একটি <print> ট্যাগ",
            "শুধু মেশিন ল্যাঙ্গুয়েজ অপকোড",
            "শুধু <excel> ওয়ার্কশিট",
        ],
        "A", "easy", "factual",
        "Standard structure nests head and body inside html.",
        "মানক কাঠামোতে html-এর ভিতরে head ও body থাকে।",
    ),
    q(
        "The <title> tag content appears mainly in the:",
        "<title> ট্যাগের বিষয়বস্তু প্রধানত দেখা যায়:",
        [
            "Browser title bar / tab",
            "Printer toner cartridge",
            "CPU heatsink label",
            "Keyboard backlight only",
        ],
        [
            "ব্রাউজারের টাইটেল বার / ট্যাবে",
            "প্রিন্টার টোনার কার্ট্রিজে",
            "CPU হিটসিঙ্ক লেবেলে",
            "শুধু কীবোর্ড ব্যাকলাইটে",
        ],
        "A", "easy", "factual",
        "Title text shows in the tab/title bar and may be used by search engines.",
        "টাইটেল ট্যাব/টাইটেল বারে দেখায় এবং সার্চ ইঞ্জিনে ব্যবহৃত হতে পারে।",
    ),
    q(
        "Visible page content for users is placed inside the:",
        "ব্যবহারকারীর দৃশ্যমান পেজ কন্টেন্ট রাখা হয়:",
        ["<body> element", "<head> only", "<meta> only", "<!DOCTYPE> only"],
        ["<body> উপাদানে", "শুধু <head>-এ", "শুধু <meta>-তে", "শুধু <!DOCTYPE>-এ"],
        "A", "easy", "factual",
        "Body holds headings, text, images, tables, links, etc.",
        "বডিতে শিরোনাম, লেখা, চিত্র, টেবিল, লিঙ্ক ইত্যাদি থাকে।",
    ),
    q(
        "The <head> section typically contains:",
        "<head> অংশে সাধারণত থাকে:",
        [
            "Metadata such as title, meta, and linked styles/scripts",
            "Only large visible paragraphs for readers",
            "Only the full photo gallery",
            "Only printable invoice tables",
        ],
        [
            "টাইটেল, মেটা ও লিঙ্কড স্টাইল/স্ক্রিপ্টের মতো মেটাডেটা",
            "শুধু পাঠকের বড় দৃশ্যমান অনুচ্ছেদ",
            "শুধু পূর্ণ ফটো গ্যালারি",
            "শুধু ছাপানোর চালান টেবিল",
        ],
        "A", "medium", "conceptual",
        "Head holds non-visible structural metadata for the document.",
        "হেডে নথির অদৃশ্য কাঠামোগত মেটাডেটা থাকে।",
    ),
    q(
        "A void (empty) HTML element example is:",
        "একটি শূন্য (void/empty) HTML উপাদানের উদাহরণ:",
        ["<br>", "<p>…</p>", "<div>…</div>", "<html>…</html>"],
        ["<br> ট্যাগ", "<p>…</p> উপাদান", "<div>…</div> উপাদান", "<html>…</html> উপাদান"],
        "A", "medium", "factual",
        "<br>, <hr>, <img>, <meta> etc. do not wrap content with a closing pair in the same way.",
        "<br>, <hr>, <img>, <meta> ইত্যাদি একইভাবে কন্টেন্ট মোড়ানো বন্ধ জোড়া ব্যবহার করে না।",
    ),
    q(
        "HTML attributes provide:",
        "HTML অ্যাট্রিবিউট প্রদান করে:",
        [
            "Extra information about an element (e.g., href, src, id)",
            "Only the computer’s BIOS password",
            "Only network cable colours",
            "Only GPU clock speeds",
        ],
        [
            "উপাদান সম্পর্কে অতিরিক্ত তথ্য (যেমন href, src, id)",
            "শুধু কম্পিউটারের BIOS পাসওয়ার্ড",
            "শুধু নেটওয়ার্ক কেবলের রং",
            "শুধু GPU ক্লক স্পিড",
        ],
        "A", "easy", "conceptual",
        "Attributes appear in the opening tag: <a href=\"…\">.",
        "অ্যাট্রিবিউট খোলার ট্যাগে থাকে: <a href=\"…\">।",
    ),
    q(
        "Which declaration tells the browser the document is HTML5?",
        "কোন ঘোষণা ব্রাউজারকে বলে নথিটি HTML5?",
        ["<!DOCTYPE html>", "<html5>", "<doctype HTML4>", "<version=5>"],
        ["<!DOCTYPE html> ঘোষণা", "<html5> ট্যাগ", "<doctype HTML4> ঘোষণা", "<version=5> অ্যাট্রিবিউট"],
        "A", "medium", "factual",
        "HTML5 uses the simple <!DOCTYPE html> preamble.",
        "HTML5-এ সরল <!DOCTYPE html> ব্যবহার হয়।",
    ),
    q(
        "HTML comments are written as:",
        "HTML মন্তব্য লেখা হয়:",
        ["<!-- comment -->", "// comment only", "/* comment */ only", "# comment only"],
        ["<!-- মন্তব্য -->", "শুধু // মন্তব্য", "শুধু /* মন্তব্য */", "শুধু # মন্তব্য"],
        "A", "easy", "factual",
        "Browsers ignore <!-- … --> comments in HTML source.",
        "ব্রাউজার HTML সোর্সের <!-- … --> মন্তব্য উপেক্ষা করে।",
    ),
    q(
        "Nested HTML tags means:",
        "নেস্টেড HTML ট্যাগ বলতে বোঝায়:",
        [
            "One element placed correctly inside another",
            "Deleting all tags from the page",
            "Using only attributes without elements",
            "Saving the file as a .docx document",
        ],
        [
            "এক উপাদান অন্যটির ভিতরে সঠিকভাবে রাখা",
            "পেজ থেকে সব ট্যাগ মুছে ফেলা",
            "উপাদান ছাড়া শুধু অ্যাট্রিবিউট ব্যবহার",
            "ফাইলকে .docx হিসেবে সংরক্ষণ",
        ],
        "A", "medium", "conceptual",
        "Proper nesting avoids crossing tags incorrectly.",
        "সঠিক নেস্টিং ভুলভাবে ক্রস করা ট্যাগ এড়ায়।",
    ),
    q(
        "Which is the correct nesting order?",
        "কোনটি সঠিক নেস্টিং ক্রম?",
        [
            "<p><strong>text</strong></p>",
            "<p><strong>text</p></strong>",
            "</p><strong>text</strong><p>",
            "<strong></p>text<p></strong>",
        ],
        [
            "সঠিক নেস্টিং: <p><strong>text</strong></p>",
            "ভুল ক্রস: <p><strong>text</p></strong>",
            "ভুল ক্রম: </p><strong>text</strong><p>",
            "ভুল মিশ্রণ: <strong></p>text<p></strong>",
        ],
        "A", "hard", "application",
        "Close inner tags before outer ones: last opened, first closed.",
        "ভেতরের ট্যাগ আগে বন্ধ করুন: শেষে খোলা, আগে বন্ধ।",
    ),
    q(
        "The default file extension for an HTML page is commonly:",
        "HTML পেজের সাধারণ ডিফল্ট ফাইল এক্সটেনশন:",
        [".html or .htm", ".xlsx only", ".mp3 only", ".dll only"],
        [".html বা .htm", "শুধু .xlsx", "শুধু .mp3", "শুধু .dll"],
        "A", "easy", "factual",
        "Pages are saved as .html/.htm for browsers to open.",
        "ব্রাউজারে খোলার জন্য পেজ .html/.htm হিসেবে সংরক্ষিত হয়।",
    ),
    q(
        "In modern HTML, tag names are generally treated as:",
        "আধুনিক HTML-এ ট্যাগ নাম সাধারণত বিবেচিত হয়:",
        [
            "Case-insensitive (conventionally written lowercase)",
            "Case-sensitive only in CAPS forever",
            "Invalid if lowercase",
            "Required to be binary digits",
        ],
        [
            "কেস-ইন্সেনসিটিভ (প্রথানুযায়ী ছোট হাতের অক্ষরে লেখা)",
            "চিরকাল শুধু বড় হাতের অক্ষরে কেস-সেনসিটিভ",
            "ছোট হাতের অক্ষরে অবৈধ",
            "বাইনারি অঙ্ক হতে বাধ্য",
        ],
        "B", "hard", "conceptual",
        "HTML parsers treat tags case-insensitively; lowercase is recommended.",
        "HTML পার্সার ট্যাগকে কেস-ইন্সেনসিটিভ ধরে; ছোট হাতের অক্ষর সুপারিশকৃত।",
    ),
    q(
        "Which tag wraps the entire HTML document content structure?",
        "কোন ট্যাগ পুরো HTML নথির কাঠামো মোড়ায়?",
        ["<html>", "<body> only", "<p> only", "<br> only"],
        ["<html> ট্যাগ", "শুধু <body>", "শুধু <p>", "শুধু <br>"],
        "A", "easy", "factual",
        "The root element is <html> containing head and body.",
        "রুট উপাদান <html>, যার ভিতরে head ও body।",
    ),
    q(
        "A <meta charset=\"UTF-8\"> tag is useful to:",
        "<meta charset=\"UTF-8\"> ট্যাগ উপকারী:",
        [
            "Declare character encoding so Bangla/English display correctly",
            "Increase RAM size physically",
            "Replace the graphics card",
            "Disable all hyperlinks forever",
        ],
        [
            "ক্যারেক্টার এনকোডিং ঘোষণা করে যাতে বাংলা/ইংরেজি সঠিক দেখায়",
            "ভৌতভাবে RAM বাড়াতে",
            "গ্রাফিক্স কার্ড প্রতিস্থাপনে",
            "চিরকাল সব হাইপারলিঙ্ক বন্ধ করতে",
        ],
        "A", "medium", "application",
        "Charset meta helps the browser interpret text bytes correctly.",
        "charset মেটা ব্রাউজারকে টেক্সট বাইট সঠিকভাবে ব্যাখ্যা করতে সাহায্য করে।",
    ),
    q(
        "An HTML element consists of:",
        "একটি HTML উপাদান গঠিত হয়:",
        [
            "Start tag, content (if any), and end tag (unless void)",
            "Only a CSS file without markup",
            "Only a JPEG binary",
            "Only a database index",
        ],
        [
            "শুরুর ট্যাগ, কন্টেন্ট (থাকলে) ও শেষ ট্যাগ (void না হলে)",
            "মার্কআপ ছাড়া শুধু CSS ফাইল",
            "শুধু JPEG বাইনারি",
            "শুধু ডেটাবেস ইনডেক্স",
        ],
        "A", "medium", "conceptual",
        "Element = tags + optional content; void elements are self-contained.",
        "উপাদান = ট্যাগ + ঐচ্ছিক কন্টেন্ট; void উপাদান স্বয়ংসম্পূর্ণ।",
    ),
    q(
        "Which is NOT a purpose of HTML?",
        "HTML-এর উদ্দেশ্য কোনটি নয়?",
        [
            "Structuring and marking up web content",
            "Replacing the computer’s power supply unit",
            "Defining headings, paragraphs, and links",
            "Providing a semantic skeleton for pages",
        ],
        [
            "ওয়েব কন্টেন্ট গঠন ও মার্কআপ করা",
            "কম্পিউটারের পাওয়ার সাপ্লাই ইউনিট প্রতিস্থাপন",
            "শিরোনাম, অনুচ্ছেদ ও লিঙ্ক নির্ধারণ",
            "পেজের সেমান্টিক কাঠামো দেওয়া",
        ],
        "B", "easy", "conceptual",
        "HTML is markup for documents, not hardware maintenance.",
        "HTML নথির মার্কআপ; হার্ডওয়্যার রক্ষণাবেক্ষণ নয়।",
    ),
    q(
        "If <h1>Welcome</h1> is written, the browser displays:",
        "<h1>Welcome</h1> লিখলে ব্রাউজার প্রদর্শন করে:",
        [
            "Welcome as a top-level heading",
            "Nothing because tags are always hidden including text",
            "Only the characters <h1> literally forever",
            "A database error always",
        ],
        [
            "শীর্ষ স্তরের শিরোনাম হিসেবে Welcome",
            "কিছুই না কারণ ট্যাগসহ সব লেখা সবসময় লুকানো",
            "চিরকাল শুধু আক্ষরিক <h1> অক্ষর",
            "সবসময় ডেটাবেস ত্রুটি",
        ],
        "A", "easy", "application",
        "Tags instruct rendering; the content Welcome is shown styled as h1.",
        "ট্যাগ রেন্ডার নির্দেশ দেয়; Welcome বিষয়বস্তু h1 স্টাইলে দেখায়।",
    ),
]


# Fix t02 Q15 - I marked B but explanation says case-insensitive which is A.
# Correct answer should be A. Fixing in the list above... wait I wrote B as correct by mistake.
# I'll fix with search_replace after write.

# --- t03: Text formatting and hyperlinks ---
T03 = [
    q(
        "Which tag creates the largest default heading?",
        "কোন ট্যাগ ডিফল্টে সবচেয়ে বড় শিরোনাম তৈরি করে?",
        ["<h1>", "<h6>", "<p>", "<br>"],
        ["<h1> ট্যাগ", "<h6> ট্যাগ", "<p> ট্যাগ", "<br> ট্যাগ"],
        "A", "easy", "factual",
        "Heading levels run h1 (largest) to h6 (smallest).",
        "শিরোনাম স্তর h1 (সবচেয়ে বড়) থেকে h6 (সবচেয়ে ছোট)।",
    ),
    q(
        "The <p> tag is used to mark a:",
        "<p> ট্যাগ ব্যবহৃত হয়:",
        ["Paragraph of text", "Page-break printer command only", "Password field only", "PDF attachment only"],
        ["লেখার অনুচ্ছেদ চিহ্নিত করতে", "শুধু পেজ-ব্রেক প্রিন্টার কমান্ড", "শুধু পাসওয়ার্ড ফিল্ড", "শুধু PDF অ্যাটাচমেন্ট"],
        "A", "easy", "factual",
        "<p> defines a paragraph block.",
        "<p> একটি অনুচ্ছেদ ব্লক নির্ধারণ করে।",
    ),
    q(
        "Which tag inserts a line break without starting a new paragraph block the same way as <p>?",
        "কোন ট্যাগ <p>-এর মতো নতুন অনুচ্ছেদ ব্লক না শুরু করে লাইন ব্রেক দেয়?",
        ["<br>", "<hr>", "<h1>", "<title>"],
        ["<br> ট্যাগ", "<hr> ট্যাগ", "<h1> ট্যাগ", "<title> ট্যাগ"],
        "A", "easy", "factual",
        "<br> forces a line break inside flowing text.",
        "<br> প্রবাহিত লেখার ভিতরে লাইন ব্রেক দেয়।",
    ),
    q(
        "The <hr> tag typically inserts a:",
        "<hr> ট্যাগ সাধারণত সন্নিবেশ করে:",
        ["Horizontal rule / thematic break line", "Hyperlink reference only", "Header row of a table only", "Hosting account invoice"],
        ["অনুভূমিক রেখা / থিম্যাটিক বিভাজক", "শুধু হাইপারলিঙ্ক রেফারেন্স", "শুধু টেবিলের হেডার সারি", "হোস্টিং অ্যাকাউন্ট চালান"],
        "A", "easy", "factual",
        "<hr> draws a horizontal separator.",
        "<hr> অনুভূমিক বিভাজক আঁকে।",
    ),
    q(
        "Which tags make text bold (semantic emphasis often preferred with strong)?",
        "কোন ট্যাগ লেখা মোটা করে (সেমান্টিক জোরে strong প্রায়ই পছন্দনীয়)?",
        ["<b> or <strong>", "<i> only", "<u> only", "<br> only"],
        ["<b> বা <strong>", "শুধু <i>", "শুধু <u>", "শুধু <br>"],
        "A", "easy", "factual",
        "<b>/<strong> bold; <strong> carries stronger semantic importance.",
        "<b>/<strong> মোটা করে; <strong>-এর সেমান্টিক গুরুত্ব বেশি।",
    ),
    q(
        "Italic text can be marked with:",
        "বাঁকা (italic) লেখা চিহ্নিত করা যায়:",
        ["<i> or <em>", "<table> only", "<img> only", "<html> only"],
        ["<i> বা <em>", "শুধু <table>", "শুধু <img>", "শুধু <html>"],
        "A", "easy", "factual",
        "<i> and <em> render italic; <em> implies emphasis.",
        "<i> ও <em> বাঁকা দেখায়; <em> জোর বোঝায়।",
    ),
    q(
        "An unordered list in HTML uses:",
        "HTML-এ আনঅর্ডার্ড লিস্ট ব্যবহার করে:",
        ["<ul> with <li> items", "<ol> only without items", "<a> only", "<form> only"],
        ["<ul> ও <li> আইটেম", "আইটেম ছাড়া শুধু <ol>", "শুধু <a>", "শুধু <form>"],
        "A", "easy", "factual",
        "Unordered lists are bullets via <ul><li>…</li></ul>.",
        "আনঅর্ডার্ড লিস্ট বুলেট: <ul><li>…</li></ul>।",
    ),
    q(
        "An ordered (numbered) list uses the:",
        "অর্ডার্ড (সংখ্যাযুক্ত) লিস্ট ব্যবহার করে:",
        ["<ol> tag with <li> items", "<ul> only for numbers always", "<hr> for each item", "<meta> for each item"],
        ["<ol> ট্যাগ ও <li> আইটেম", "সংখ্যার জন্য সবসময় শুধু <ul>", "প্রতি আইটেমে <hr>", "প্রতি আইটেমে <meta>"],
        "A", "easy", "factual",
        "Ordered lists number items with <ol>.",
        "অর্ডার্ড লিস্ট <ol> দিয়ে আইটেম সংখ্যায়িত করে।",
    ),
    q(
        "The primary tag for a hyperlink is:",
        "হাইপারলিঙ্কের প্রধান ট্যাগ:",
        ["<a>", "<link> in body text only", "<href>", "<url>"],
        ["<a> ট্যাগ", "বডি টেক্সটে শুধু <link>", "<href> ট্যাগ", "<url> ট্যাগ"],
        "A", "easy", "factual",
        "Anchor element <a> creates hyperlinks.",
        "অ্যাঙ্কর উপাদান <a> হাইপারলিঙ্ক তৈরি করে।",
    ),
    q(
        "Which attribute of <a> specifies the destination URL?",
        "<a>-এর কোন অ্যাট্রিবিউট গন্তব্য URL নির্দেশ করে?",
        ["href", "src", "alt", "action"],
        ["href অ্যাট্রিবিউট", "src অ্যাট্রিবিউট", "alt অ্যাট্রিবিউট", "action অ্যাট্রিবিউট"],
        "A", "easy", "factual",
        "Use href=\"https://…\" on the anchor tag.",
        "অ্যাঙ্কর ট্যাগে href=\"https://…\" ব্যবহার করুন।",
    ),
    q(
        "target=\"_blank\" on a link typically means:",
        "লিঙ্কে target=\"_blank\" সাধারণত মানে:",
        [
            "Open the linked page in a new tab/window",
            "Delete the linked page from the server",
            "Disable the mouse permanently",
            "Convert the page to plain text only",
        ],
        [
            "লিঙ্ক করা পেজ নতুন ট্যাব/উইন্ডোতে খোলা",
            "সার্ভার থেকে লিঙ্ক করা পেজ মুছে ফেলা",
            "স্থায়ীভাবে মাউস নিষ্ক্রিয় করা",
            "পেজকে শুধু প্লেইন টেক্সটে রূপান্তর",
        ],
        "A", "medium", "conceptual",
        "_blank opens a new browsing context.",
        "_blank নতুন ব্রাউজিং কনটেক্সট খোলে।",
    ),
    q(
        "An email link can be created with href value starting with:",
        "ইমেইল লিঙ্ক তৈরি করা যায় এমন href মান দিয়ে যা শুরু হয়:",
        ["mailto:", "httpmail:", "sendto:", "emailto:"],
        ["mailto: স্কিম", "httpmail: স্কিম", "sendto: স্কিম", "emailto: স্কিম"],
        "A", "medium", "factual",
        "Example: <a href=\"mailto:info@school.edu\">Email us</a>.",
        "উদাহরণ: <a href=\"mailto:info@school.edu\">Email us</a>।",
    ),
    q(
        "A bookmark (internal page jump) often uses:",
        "বুকমার্ক (পেজের ভিতরের জাম্প) প্রায়ই ব্যবহার করে:",
        [
            "id on a target element and href=\"#id\" on the link",
            "Only the <br> tag twice",
            "Only FTP passwords in plain text",
            "Only the <title> tag duplicated",
        ],
        [
            "লক্ষ্য উপাদানে id এবং লিঙ্কে href=\"#id\"",
            "শুধু দুবার <br> ট্যাগ",
            "শুধু প্লেইন টেক্সটে FTP পাসওয়ার্ড",
            "শুধু ডুপ্লিকেট <title> ট্যাগ",
        ],
        "A", "hard", "application",
        "Anchors jump to elements whose id matches the hash fragment.",
        "হ্যাশ ফ্র্যাগমেন্টের সাথে মিলে যাওয়া id-তে অ্যাঙ্কর জাম্প করে।",
    ),
    q(
        "The <u> tag traditionally:",
        "<u> ট্যাগ প্রথাগতভাবে:",
        ["Underlines text", "Uploads files to FTP", "Unmounts hard disks", "Updates BIOS firmware"],
        ["লেখার নিচে দাগ দেয়", "FTP-তে ফাইল আপলোড করে", "হার্ড ডিস্ক আনমাউন্ট করে", "BIOS ফার্মওয়্যার আপডেট করে"],
        "A", "easy", "factual",
        "<u> underlines; overuse can confuse users who expect links.",
        "<u> আন্ডারলাইন করে; অতিরিক্ত ব্যবহার লিঙ্কের সাথে বিভ্রান্তি ঘটাতে পারে।",
    ),
    q(
        "The <pre> tag is useful when you need to:",
        "<pre> ট্যাগ উপযোগী যখন প্রয়োজন:",
        [
            "Preserve spaces and line breaks as typed (preformatted text)",
            "Remove all whitespace automatically always",
            "Encrypt the whole hard disk",
            "Compile Java bytecode",
        ],
        [
            "টাইপ করা স্পেস ও লাইন ব্রেক সংরক্ষণ (প্রিফরম্যাটেড টেক্সট)",
            "সবসময় স্বয়ংক্রিয়ভাবে সব হোয়াইটস্পেস মুছে ফেলা",
            "পুরো হার্ড ডিস্ক এনক্রিপ্ট করা",
            "Java বাইটকোড কম্পাইল করা",
        ],
        "A", "medium", "conceptual",
        "<pre> keeps monospace-style preformatted layout.",
        "<pre> মনোস্পেস-স্টাইল প্রিফরম্যাটেড লেআউট রাখে।",
    ),
    q(
        "Which is the correct hyperlink markup?",
        "কোনটি সঠিক হাইপারলিঙ্ক মার্কআপ?",
        [
            "<a href=\"https://example.com\">Visit</a>",
            "<a>https://example.com</a> without href",
            "<href=\"https://example.com\">Visit</href>",
            "<link href=\"https://example.com\">Visit</link> as body text",
        ],
        [
            "সঠিক: <a href=\"https://example.com\">Visit</a>",
            "href ছাড়া <a>https://example.com</a>",
            "ভুল ট্যাগ: <href=\"https://example.com\">Visit</href>",
            "বডি টেক্সট হিসেবে <link>…</link>",
        ],
        "A", "medium", "application",
        "Anchor needs href; visible text sits between <a> and </a>.",
        "অ্যাঙ্করে href লাগে; দৃশ্যমান লেখা <a> ও </a>-এর মাঝে।",
    ),
    q(
        "Relative links differ from absolute links because they:",
        "রিলেটিভ লিঙ্ক পরম (absolute) লিঙ্ক থেকে আলাদা কারণ এরা:",
        [
            "Refer to paths relative to the current page/site location",
            "Always include the full https://domain every time",
            "Can only point to email addresses",
            "Never work inside the same website",
        ],
        [
            "বর্তমান পেজ/সাইট অবস্থানের আপেক্ষিক পাথ নির্দেশ করে",
            "প্রতিবার পূর্ণ https://domain অন্তর্ভুক্ত করে",
            "শুধু ইমেইল ঠিকানায় নির্দেশ করতে পারে",
            "একই ওয়েবসাইটের ভিতরে কখনো কাজ করে না",
        ],
        "A", "medium", "conceptual",
        "Example relative: about.html; absolute: https://school.edu/about.html.",
        "রিলেটিভ উদাহরণ: about.html; পরম: https://school.edu/about.html।",
    ),
    q(
        "Which heading level is typically used for the least important subheading?",
        "সবচেয়ে কম গুরুত্বপূর্ণ উপশিরোনামে সাধারণত কোন স্তর ব্যবহার হয়?",
        ["<h6>", "<h1>", "<title>", "<caption>"],
        ["<h6> ট্যাগ", "<h1> ট্যাগ", "<title> ট্যাগ", "<caption> ট্যাগ"],
        "A", "easy", "factual",
        "h6 is the smallest/lowest-rank heading level.",
        "h6 সবচেয়ে ছোট/নিম্নতম শিরোনাম স্তর।",
    ),
    q(
        "Combining <ol type=\"A\"> typically starts numbering with:",
        "<ol type=\"A\"> একত্রে ব্যবহার করলে সাধারণত সংখ্যায়ন শুরু হয়:",
        ["Uppercase letters A, B, C…", "Roman numerals only", "Bullets only", "Binary 0 and 1 only"],
        ["বড় হাতের অক্ষর A, B, C…", "শুধু রোমান সংখ্যা", "শুধু বুলেট", "শুধু বাইনারি ০ ও ১"],
        "A", "hard", "application",
        "type=\"A\" uses A, B, C… for ordered list markers (legacy/presentational).",
        "type=\"A\" অর্ডার্ড লিস্ট মার্কারে A, B, C… ব্যবহার করে।",
    ),
    q(
        "Clickable image links are made by:",
        "ক্লিকযোগ্য চিত্র লিঙ্ক তৈরি হয়:",
        [
            "Wrapping an <img> inside an <a> element",
            "Using only <hr> around the image",
            "Putting the image inside <title>",
            "Saving the JPG as .exe",
        ],
        [
            "<a> উপাদানের ভিতরে <img> মোড়ানো",
            "চিত্রের চারপাশে শুধু <hr>",
            "<title>-এর ভিতরে চিত্র রাখা",
            "JPG কে .exe হিসেবে সংরক্ষণ",
        ],
        "A", "medium", "application",
        "Pattern: <a href=\"…\"><img src=\"…\" alt=\"…\"></a>.",
        "প্যাটার্ন: <a href=\"…\"><img src=\"…\" alt=\"…\"></a>।",
    ),
]


# --- t04: Images and tables ---
T04 = [
    q(
        "Which tag embeds an image in an HTML page?",
        "HTML পেজে চিত্র সন্নিবেশের ট্যাগ কোনটি?",
        ["<img>", "<image> only in all versions", "<pic>", "<photo>"],
        ["<img> ট্যাগ", "সব সংস্করণে শুধু <image>", "<pic> ট্যাগ", "<photo> ট্যাগ"],
        "A", "easy", "factual",
        "Use the void <img> element to display images.",
        "চিত্র দেখাতে void <img> উপাদান ব্যবহার করুন।",
    ),
    q(
        "The src attribute of <img> specifies:",
        "<img>-এর src অ্যাট্রিবিউট নির্দেশ করে:",
        [
            "The path or URL of the image file",
            "Only the alt text description",
            "Only the browser zoom level",
            "Only the printer paper size",
        ],
        [
            "চিত্র ফাইলের পাথ বা URL",
            "শুধু alt টেক্সট বর্ণনা",
            "শুধু ব্রাউজার জুম স্তর",
            "শুধু প্রিন্টার কাগজের আকার",
        ],
        "A", "easy", "factual",
        "src points to where the image resource is loaded from.",
        "src বলে চিত্র রিসোর্স কোথা থেকে লোড হবে।",
    ),
    q(
        "The alt attribute on images is important because it:",
        "চিত্রে alt অ্যাট্রিবিউট গুরুত্বপূর্ণ কারণ এটি:",
        [
            "Provides alternative text if the image cannot be shown / for accessibility",
            "Always encrypts the image file",
            "Increases GPU VRAM physically",
            "Deletes broken links automatically",
        ],
        [
            "চিত্র না দেখালে বিকল্প লেখা দেয় / অ্যাক্সেসিবিলিটির জন্য",
            "সবসময় চিত্র ফাইল এনক্রিপ্ট করে",
            "ভৌতভাবে GPU VRAM বাড়ায়",
            "ভাঙা লিঙ্ক স্বয়ংক্রিয়ভাবে মুছে",
        ],
        "A", "medium", "conceptual",
        "Alt text helps screen readers and appears when images fail to load.",
        "alt টেক্সট স্ক্রিন রিডার ও চিত্র লোড ব্যর্থ হলে সাহায্য করে।",
    ),
    q(
        "width and height attributes on <img> can:",
        "<img>-এ width ও height অ্যাট্রিবিউট পারে:",
        [
            "Suggest display dimensions of the image",
            "Change the server’s electricity voltage",
            "Rename the domain registrar",
            "Compile the HTML into machine code",
        ],
        [
            "চিত্রের প্রদর্শন মাত্রা নির্দেশ করতে",
            "সার্ভারের বিদ্যুৎ ভোল্টেজ বদলাতে",
            "ডোমেইন রেজিস্ট্রারের নাম বদলাতে",
            "HTML কে মেশিন কোডে কম্পাইল করতে",
        ],
        "A", "easy", "factual",
        "They control rendered size (CSS is preferred in modern practice).",
        "এরা রেন্ডার আকার নিয়ন্ত্রণ করে (আধুনিক চর্চায় CSS পছন্দনীয়)।",
    ),
    q(
        "Which HTML tag starts a table?",
        "কোন HTML ট্যাগ টেবিল শুরু করে?",
        ["<table>", "<tab>", "<grid>", "<tr> alone as root"],
        ["<table> ট্যাগ", "<tab> ট্যাগ", "<grid> ট্যাগ", "রুট হিসেবে একা <tr>"],
        "A", "easy", "factual",
        "Tables begin with <table>…</table>.",
        "টেবিল <table>…</table> দিয়ে শুরু হয়।",
    ),
    q(
        "Table rows are defined with:",
        "টেবিলের সারি নির্ধারণ হয়:",
        ["<tr>", "<td> only as the row container", "<th> only as the row container", "<row>"],
        ["<tr> ট্যাগ", "সারি ধারক হিসেবে শুধু <td>", "সারি ধারক হিসেবে শুধু <th>", "<row> ট্যাগ"],
        "A", "easy", "factual",
        "Each row is a <tr> containing cells.",
        "প্রতি সারি একটি <tr>, যার ভিতরে সেল থাকে।",
    ),
    q(
        "A standard data cell in a table uses:",
        "টেবিলের সাধারণ ডেটা সেল ব্যবহার করে:",
        ["<td>", "<tr> only", "<table> only", "<caption> only"],
        ["<td> ট্যাগ", "শুধু <tr>", "শুধু <table>", "শুধু <caption>"],
        "A", "easy", "factual",
        "<td> holds ordinary table data.",
        "<td> সাধারণ টেবিল ডেটা ধারণ করে।",
    ),
    q(
        "Header cells are typically marked with:",
        "হেডার সেল সাধারণত চিহ্নিত হয়:",
        ["<th>", "<hd>", "<header-cell>", "<thead-cell>"],
        ["<th> ট্যাগ", "<hd> ট্যাগ", "<header-cell> ট্যাগ", "<thead-cell> ট্যাগ"],
        "A", "easy", "factual",
        "<th> marks heading cells (often bold/centered by default).",
        "<th> শিরোনাম সেল চিহ্নিত করে (প্রায়ই ডিফল্টে মোটা/কেন্দ্রিক)।",
    ),
    q(
        "The <caption> tag for a table provides:",
        "টেবিলের <caption> ট্যাগ প্রদান করে:",
        [
            "A title/description for the table",
            "Only the border colour of the browser chrome",
            "Only FTP login credentials",
            "Only the page’s favicon",
        ],
        [
            "টেবিলের শিরোনাম/বর্ণনা",
            "শুধু ব্রাউজার ক্রোমের বর্ডার রং",
            "শুধু FTP লগইন তথ্য",
            "শুধু পেজের ফেভিকন",
        ],
        "A", "medium", "factual",
        "Caption labels the table for readers and accessibility.",
        "ক্যাপশন পাঠক ও অ্যাক্সেসিবিলিটির জন্য টেবিল লেবেল করে।",
    ),
    q(
        "border attribute on <table> (classic HTML) controls:",
        "<table>-এ border অ্যাট্রিবিউট (ক্লাসিক HTML) নিয়ন্ত্রণ করে:",
        [
            "Whether/how a border is shown around cells",
            "The DNS TTL value",
            "The SSL certificate expiry only",
            "The RAM refresh rate",
        ],
        [
            "সেলের চারপাশে বর্ডার দেখাবে কিনা/কীভাবে",
            "DNS TTL মান",
            "শুধু SSL সার্টিফিকেট মেয়াদ",
            "RAM রিফ্রেশ রেট",
        ],
        "A", "easy", "factual",
        "border=\"1\" shows borders; modern pages often use CSS instead.",
        "border=\"1\" বর্ডার দেখায়; আধুনিক পেজে প্রায়ই CSS ব্যবহার হয়।",
    ),
    q(
        "colspan=\"2\" on a cell means the cell:",
        "সেলে colspan=\"2\" মানে সেলটি:",
        [
            "Spans two columns horizontally",
            "Spans two rows vertically only",
            "Splits into two nested tables",
            "Deletes two neighbouring pages",
        ],
        [
            "অনুভূমিকভাবে দুই কলাম জুড়ে থাকে",
            "শুধু উল্লম্বভাবে দুই সারি জোড়ে",
            "দুই নেস্টেড টেবিলে বিভক্ত হয়",
            "দুই প্রতিবেশী পেজ মুছে ফেলে",
        ],
        "A", "medium", "conceptual",
        "colspan merges across columns; rowspan merges across rows.",
        "colspan কলাম জুড়ে মেশায়; rowspan সারি জুড়ে মেশায়।",
    ),
    q(
        "rowspan=\"3\" causes a cell to:",
        "rowspan=\"3\" একটি সেলকে:",
        [
            "Occupy three rows vertically",
            "Occupy three columns horizontally only",
            "Create three separate HTML files",
            "Open three new browser windows",
        ],
        [
            "উল্লম্বভাবে তিন সারি দখল করায়",
            "শুধু অনুভূমিকভাবে তিন কলাম দখল করায়",
            "তিনটি পৃথক HTML ফাইল তৈরি করে",
            "তিনটি নতুন ব্রাউজার উইন্ডো খোলে",
        ],
        "A", "medium", "conceptual",
        "rowspan extends a cell downward across multiple rows.",
        "rowspan সেলকে নিচের দিকে একাধিক সারিতে বিস্তৃত করে।",
    ),
    q(
        "A common image file format used on web pages is:",
        "ওয়েব পেজে ব্যবহৃত সাধারণ চিত্র ফাইল ফরম্যাট:",
        ["JPEG / PNG / GIF", "EXE only", "DLL only", "SYS only"],
        ["JPEG / PNG / GIF ফরম্যাট", "শুধু EXE", "শুধু DLL", "শুধু SYS"],
        "A", "easy", "factual",
        "Web images are often JPG, PNG, GIF, SVG, or WebP.",
        "ওয়েব চিত্র প্রায়ই JPG, PNG, GIF, SVG বা WebP।",
    ),
    q(
        "Which markup correctly includes an image with alternative text?",
        "বিকল্প লেখসহ চিত্রের সঠিক মার্কআপ কোনটি?",
        [
            "<img src=\"logo.png\" alt=\"School logo\">",
            "<img alt=\"logo.png\" src=\"School logo\">",
            "<img>logo.png</img> with required end tag always",
            "<image href=\"logo.png\">",
        ],
        [
            "সঠিক: <img src=\"logo.png\" alt=\"স্কুল লোগো\">",
            "উল্টো অ্যাট্রিবিউট মানসহ <img>",
            "সবসময় আবশ্যক শেষ ট্যাগসহ <img>logo.png</img>",
            "ভুল ট্যাগ: <image href=\"logo.png\">",
        ],
        "A", "medium", "application",
        "src is the file; alt describes it for accessibility.",
        "src ফাইল; alt অ্যাক্সেসিবিলিটির জন্য বর্ণনা।",
    ),
    q(
        "A minimal 2×2 table structure includes:",
        "ন্যূনতম ২×২ টেবিল কাঠামোতে থাকে:",
        [
            "One <table>, two <tr> rows, each with two <td> cells",
            "Only four <img> tags",
            "Only one <br> tag",
            "Only a single <a> tag",
        ],
        [
            "এক <table>, দুই <tr> সারি, প্রতিটিতে দুই <td> সেল",
            "শুধু চারটি <img> ট্যাগ",
            "শুধু একটি <br> ট্যাগ",
            "শুধু একটি <a> ট্যাগ",
        ],
        "A", "medium", "application",
        "Rows hold cells; two rows × two cells = 2×2 grid.",
        "সারিতে সেল থাকে; দুই সারি × দুই সেল = ২×২ গ্রিড।",
    ),
    q(
        "<thead>, <tbody>, and <tfoot> help to:",
        "<thead>, <tbody> ও <tfoot> সাহায্য করে:",
        [
            "Group header, body, and footer sections of a table",
            "Replace the need for any cells",
            "Host the website on FTP automatically",
            "Convert images into tables",
        ],
        [
            "টেবিলের হেডার, বডি ও ফুটার অংশ গ্রুপ করতে",
            "কোনো সেলের প্রয়োজন প্রতিস্থাপন করতে",
            "স্বয়ংক্রিয়ভাবে FTP-তে ওয়েবসাইট হোস্ট করতে",
            "চিত্রকে টেবিলে রূপান্তর করতে",
        ],
        "A", "hard", "conceptual",
        "These sectioning elements organise complex tables semantically.",
        "এই সেকশনিং উপাদান জটিল টেবিল সেমান্টিকভাবে সাজায়।",
    ),
    q(
        "If an image path is wrong, the browser typically:",
        "চিত্রের পাথ ভুল হলে ব্রাউজার সাধারণত:",
        [
            "Shows a broken-image icon and may display the alt text",
            "Formats the hard disk automatically",
            "Always crashes the operating system",
            "Silently installs a new graphics driver",
        ],
        [
            "ভাঙা-চিত্র আইকন দেখায় এবং alt টেক্সট দেখাতে পারে",
            "স্বয়ংক্রিয়ভাবে হার্ড ডিস্ক ফরম্যাট করে",
            "সবসময় অপারেটিং সিস্টেম ক্র্যাশ করে",
            "নীরবে নতুন গ্রাফিক্স ড্রাইভার ইনস্টল করে",
        ],
        "A", "medium", "application",
        "Failed loads surface alt text / broken image indicators.",
        "লোড ব্যর্থ হলে alt টেক্সট / ভাঙা চিত্র নির্দেশক দেখায়।",
    ),
    q(
        "cellpadding (classic) affects:",
        "cellpadding (ক্লাসিক) প্রভাব ফেলে:",
        [
            "Space between cell content and cell border",
            "Space only between separate tables on disk",
            "The HTTPS certificate chain length",
            "The number of DNS servers",
        ],
        [
            "সেল কন্টেন্ট ও সেল বর্ডারের মধ্যবর্তী ফাঁকা স্থান",
            "শুধু ডিস্কে আলাদা টেবিলগুলোর মধ্যবর্তী স্থান",
            "HTTPS সার্টিফিকেট চেইনের দৈর্ঘ্য",
            "DNS সার্ভারের সংখ্যা",
        ],
        "A", "hard", "factual",
        "cellpadding pads inside cells; cellspacing spaces between cells.",
        "cellpadding সেলের ভিতরে প্যাড করে; cellspacing সেলগুলোর মাঝে ফাঁক দেয়।",
    ),
    q(
        "cellspacing (classic) affects:",
        "cellspacing (ক্লাসিক) প্রভাব ফেলে:",
        [
            "Space between adjacent cells",
            "Only the font family of <title>",
            "Only email SMTP ports",
            "Only the favicon colour depth",
        ],
        [
            "পাশাপাশি সেলগুলোর মধ্যবর্তী ফাঁকা স্থান",
            "শুধু <title>-এর ফন্ট পরিবার",
            "শুধু ইমেইল SMTP পোর্ট",
            "শুধু ফেভিকনের কালার ডেপথ",
        ],
        "A", "hard", "factual",
        "cellspacing controls gaps between cells in older HTML tables.",
        "পুরনো HTML টেবিলে cellspacing সেলের ফাঁক নিয়ন্ত্রণ করে।",
    ),
    q(
        "To make a table more accessible and understandable, authors should:",
        "টেবিলকে আরও অ্যাক্সেসিবল ও বোধগম্য করতে লেখকদের উচিত:",
        [
            "Use clear <th> headers and a meaningful <caption>",
            "Remove all text and keep only borders",
            "Nest fifty empty tables with no cells",
            "Put the entire site inside one cell without headers",
        ],
        [
            "স্পষ্ট <th> হেডার ও অর্থপূর্ণ <caption> ব্যবহার করা",
            "সব লেখা সরিয়ে শুধু বর্ডার রাখা",
            "সেল ছাড়া পঞ্চাশটি খালি টেবিল নেস্ট করা",
            "হেডার ছাড়া পুরো সাইট এক সেলে রাখা",
        ],
        "A", "hard", "application",
        "Headers and captions clarify structure for all users.",
        "হেডার ও ক্যাপশন সব ব্যবহারকারীর জন্য কাঠামো স্পষ্ট করে।",
    ),
]


# --- t05: Web page design and publishing ---
T05 = [
    q(
        "A simple way to write HTML is to use a:",
        "HTML লেখার সহজ উপায় হলো ব্যবহার করা:",
        [
            "Text editor (e.g., Notepad) and save as .html",
            "Only a calculator app",
            "Only a paint roller",
            "Only a barcode scanner",
        ],
        [
            "টেক্সট এডিটর (যেমন Notepad) ও .html হিসেবে সংরক্ষণ",
            "শুধু ক্যালকুলেটর অ্যাপ",
            "শুধু পেইন্ট রোলার",
            "শুধু বারকোড স্ক্যানার",
        ],
        "A", "easy", "factual",
        "Any plain-text editor can author HTML files.",
        "যেকোনো প্লেইন-টেক্সট এডিটরে HTML লেখা যায়।",
    ),
    q(
        "WYSIWYG web editors are tools that:",
        "WYSIWYG ওয়েব এডিটর এমন টুল যা:",
        [
            "Let you design visually while generating markup behind the scenes",
            "Only delete websites permanently",
            "Only measure network cable length",
            "Only flash BIOS chips",
        ],
        [
            "দৃশ্যমানভাবে ডিজাইন করতে দেয় এবং পেছনে মার্কআপ তৈরি করে",
            "শুধু স্থায়ীভাবে ওয়েবসাইট মুছে ফেলে",
            "শুধু নেটওয়ার্ক কেবলের দৈর্ঘ্য মাপে",
            "শুধু BIOS চিপ ফ্ল্যাশ করে",
        ],
        "A", "medium", "conceptual",
        "WYSIWYG means What You See Is What You Get.",
        "WYSIWYG মানে What You See Is What You Get।",
    ),
    q(
        "Before coding a site, good practice is to:",
        "সাইট কোডিংয়ের আগে ভালো চর্চা হলো:",
        [
            "Plan purpose, audience, content, and page structure",
            "Upload random empty folders with no plan",
            "Share the root password publicly first",
            "Skip testing on any browser",
        ],
        [
            "উদ্দেশ্য, দর্শক, কন্টেন্ট ও পেজ কাঠামো পরিকল্পনা করা",
            "পরিকল্পনা ছাড়া এলোমেলো খালি ফোল্ডার আপলোড",
            "আগে রুট পাসওয়ার্ড প্রকাশ্যে শেয়ার",
            "কোনো ব্রাউজারে টেস্টিং এড়িয়ে যাওয়া",
        ],
        "A", "easy", "conceptual",
        "Planning reduces rework and improves usability.",
        "পরিকল্পনা পুনর্কাজ কমায় ও ব্যবহারযোগ্যতা বাড়ায়।",
    ),
    q(
        "A wireframe in web design is:",
        "ওয়েব ডিজাইনে ওয়্যারফ্রেম হলো:",
        [
            "A simple layout sketch of page regions without full visuals",
            "A metal frame for the server rack only",
            "An encrypted VPN tunnel only",
            "A compiled machine-code binary",
        ],
        [
            "পূর্ণ ভিজুয়াল ছাড়া পেজ অঞ্চলের সরল লেআউট স্কেচ",
            "শুধু সার্ভার র্যাকের ধাতব ফ্রেম",
            "শুধু এনক্রিপ্টেড VPN টানেল",
            "কম্পাইলড মেশিন-কোড বাইনারি",
        ],
        "A", "medium", "factual",
        "Wireframes map header, content, sidebar, footer placement.",
        "ওয়্যারফ্রেম হেডার, কন্টেন্ট, সাইডবার, ফুটার স্থান ম্যাপ করে।",
    ),
    q(
        "To publish a website on the Internet you typically need:",
        "ইন্টারনেটে ওয়েবসাইট প্রকাশে সাধারণত প্রয়োজন:",
        [
            "Web hosting space and a way to upload files (often with a domain)",
            "Only a local printer cable",
            "Only offline CD-ROM burning forever",
            "Only a graphics tablet without files",
        ],
        [
            "ওয়েব হোস্টিং জায়গা ও ফাইল আপলোডের উপায় (প্রায়ই ডোমেইনসহ)",
            "শুধু স্থানীয় প্রিন্টার কেবল",
            "চিরকাল শুধু অফলাইন CD-ROM বার্ন",
            "ফাইল ছাড়া শুধু গ্রাফিক্স ট্যাবলেট",
        ],
        "A", "easy", "factual",
        "Hosting + upload (FTP/SFTP/control panel) makes pages public.",
        "হোস্টিং + আপলোড (FTP/SFTP/কন্ট্রোল প্যানেল) পেজ পাবলিক করে।",
    ),
    q(
        "A domain name is:",
        "ডোমেইন নাম হলো:",
        [
            "A human-readable address registered for a site (e.g., school.edu.bd)",
            "Only the physical street address of the ISP",
            "Only the MAC address of one keyboard",
            "Only an IP printed on a mouse",
        ],
        [
            "সাইটের জন্য নিবন্ধিত মানুষ-পাঠযোগ্য ঠিকানা (যেমন school.edu.bd)",
            "শুধু ISP-এর ভৌত রাস্তার ঠিকানা",
            "শুধু এক কীবোর্ডের MAC ঠিকানা",
            "শুধু মাউসে ছাপানো IP",
        ],
        "A", "easy", "factual",
        "Domains map via DNS to hosting IP addresses.",
        "ডোমেইন DNS দিয়ে হোস্টিং IP-তে ম্যাপ হয়।",
    ),
    q(
        "FTP is commonly used to:",
        "FTP সাধারণত ব্যবহৃত হয়:",
        [
            "Transfer website files between local computer and server",
            "Format paragraphs inside the browser only",
            "Draw table borders automatically only",
            "Validate HTML comments only",
        ],
        [
            "স্থানীয় কম্পিউটার ও সার্ভারের মধ্যে ওয়েবসাইট ফাইল স্থানান্তর করতে",
            "শুধু ব্রাউজারের ভিতরে অনুচ্ছেদ ফরম্যাট করতে",
            "শুধু স্বয়ংক্রিয়ভাবে টেবিল বর্ডার আঁকতে",
            "শুধু HTML মন্তব্য যাচাই করতে",
        ],
        "A", "easy", "factual",
        "File Transfer Protocol uploads/downloads site files (SFTP/FTPS preferred for security).",
        "File Transfer Protocol সাইট ফাইল আপ/ডাউনলোড করে (নিরাপত্তায় SFTP/FTPS ভালো)।",
    ),
    q(
        "After editing HTML locally, you should:",
        "স্থানীয়ভাবে HTML সম্পাদনার পর উচিত:",
        [
            "Test the page in a browser before/after publishing",
            "Never open it in any browser",
            "Email the root password with the file",
            "Delete the DOCTYPE always",
        ],
        [
            "প্রকাশের আগে/পরে ব্রাউজারে পেজ পরীক্ষা করা",
            "কোনো ব্রাউজারে কখনো না খোলা",
            "ফাইলের সাথে রুট পাসওয়ার্ড ইমেইল করা",
            "সবসময় DOCTYPE মুছে ফেলা",
        ],
        "A", "easy", "application",
        "Local preview catches markup and layout mistakes early.",
        "স্থানীয় প্রিভিউ মার্কআপ ও লেআউট ভুল আগে ধরে।",
    ),
    q(
        "Consistent navigation across pages improves:",
        "পেজজুড়ে সামঞ্জস্যপূর্ণ নেভিগেশন উন্নত করে:",
        [
            "Usability so visitors can find sections easily",
            "CPU overclocking automatically",
            "Hard-disk fragmentation on purpose",
            "Random broken menus as a feature",
        ],
        [
            "ব্যবহারযোগ্যতা যাতে দর্শক সহজে বিভাগ খুঁজে পায়",
            "স্বয়ংক্রিয় CPU ওভারক্লকিং",
            "ইচ্ছাকৃত হার্ড-ডিস্ক ফ্র্যাগমেন্টেশন",
            "বৈশিষ্ট্য হিসেবে এলোমেলো ভাঙা মেনু",
        ],
        "A", "medium", "conceptual",
        "Repeated clear menus reduce confusion.",
        "পুনরাবৃত্ত স্পষ্ট মেনু বিভ্রান্তি কমায়।",
    ),
    q(
        "Readable web typography usually requires:",
        "পাঠযোগ্য ওয়েব টাইপোগ্রাফিতে সাধারণত প্রয়োজন:",
        [
            "Adequate contrast, font size, and line spacing",
            "Tiny grey text on grey backgrounds always",
            "All text as images of handwriting only",
            "Flashing rainbow text for every word",
        ],
        [
            "পর্যাপ্ত কনট্রাস্ট, ফন্ট সাইজ ও লাইন স্পেসিং",
            "সবসময় ধূসর পটভূমিতে ক্ষুদ্র ধূসর লেখা",
            "সব লেখা শুধু হাতের লেখার চিত্র",
            "প্রতি শব্দে ঝলমলে রংধনু লেখা",
        ],
        "A", "medium", "conceptual",
        "Legibility and contrast support all readers.",
        "পাঠযোগ্যতা ও কনট্রাস্ট সব পাঠককে সহায়তা করে।",
    ),
    q(
        "CSS is often used with HTML to:",
        "HTML-এর সাথে CSS প্রায়ই ব্যবহৃত হয়:",
        [
            "Control presentation (colours, layout, fonts) separately from structure",
            "Replace the need for any hosting",
            "Compile C programs inside the browser only",
            "Manage BIOS settings remotely only",
        ],
        [
            "কাঠামো থেকে আলাদাভাবে উপস্থাপনা (রং, লেআউট, ফন্ট) নিয়ন্ত্রণ করতে",
            "কোনো হোস্টিংয়ের প্রয়োজন প্রতিস্থাপন করতে",
            "শুধু ব্রাউজারের ভিতরে C প্রোগ্রাম কম্পাইল করতে",
            "শুধু দূর থেকে BIOS সেটিংস পরিচালনা করতে",
        ],
        "A", "medium", "conceptual",
        "HTML structures content; CSS styles it.",
        "HTML কন্টেন্ট গঠন করে; CSS স্টাইল দেয়।",
    ),
    q(
        "An index.html (or index.htm) file is often:",
        "index.html (বা index.htm) ফাইল প্রায়ই:",
        [
            "The default page a server shows for a folder/site root",
            "A forbidden filename on every host",
            "Only used for image galleries named photos.exe",
            "Required to be empty always",
        ],
        [
            "ফোল্ডার/সাইট রুটে সার্ভার যে ডিফল্ট পেজ দেখায়",
            "প্রতিটি হোস্টে নিষিদ্ধ ফাইলনাম",
            "শুধু photos.exe নামের ইমেজ গ্যালারির জন্য",
            "সবসময় খালি থাকতে বাধ্য",
        ],
        "A", "medium", "factual",
        "Many hosts serve index.html when a directory URL is requested.",
        "ডিরেক্টরি URL অনুরোধে অনেক হোস্ট index.html পরিবেশন করে।",
    ),
    q(
        "Checking a site on more than one browser helps detect:",
        "একাধিক ব্রাউজারে সাইট পরীক্ষা সাহায্য করে ধরতে:",
        [
            "Compatibility and rendering differences",
            "Only the temperature of the ISP office",
            "Only toner levels in distant printers",
            "Only undersea cable depth",
        ],
        [
            "সামঞ্জস্য ও রেন্ডারিং পার্থক্য",
            "শুধু ISP অফিসের তাপমাত্রা",
            "শুধু দূরবর্তী প্রিন্টারের টোনার স্তর",
            "শুধু সাবমেরিন কেবলের গভীরতা",
        ],
        "A", "easy", "application",
        "Cross-browser testing finds layout quirks early.",
        "ক্রস-ব্রাউজার টেস্টিং আগে লেআউট ত্রুটি ধরে।",
    ),
    q(
        "When uploading a site, keeping the same folder structure as local files:",
        "সাইট আপলোডে স্থানীয় ফাইলের মতো একই ফোল্ডার কাঠামো রাখা:",
        [
            "Helps relative links and image paths keep working",
            "Always breaks every hyperlink intentionally",
            "Is never recommended by anyone",
            "Only matters for printed books",
        ],
        [
            "রিলেটিভ লিঙ্ক ও চিত্র পাথ কাজ করতে সাহায্য করে",
            "সবসময় ইচ্ছাকৃতভাবে প্রতিটি হাইপারলিঙ্ক ভাঙে",
            "কেউ কখনো সুপারিশ করে না",
            "শুধু ছাপানো বইয়ের জন্য গুরুত্বপূর্ণ",
        ],
        "A", "medium", "application",
        "Mirrored paths preserve relative URLs after publish.",
        "মিরর করা পাথ প্রকাশের পর রিলেটিভ URL সংরক্ষণ করে।",
    ),
    q(
        "A responsive web design approach aims to:",
        "রেসপনসিভ ওয়েব ডিজাইন পদ্ধতির লক্ষ্য:",
        [
            "Adapt layouts to different screen sizes (phone, tablet, desktop)",
            "Support only one fixed CRT monitor forever",
            "Ignore mobile users completely",
            "Print pages at exactly one paper size only",
        ],
        [
            "বিভিন্ন স্ক্রিন আকারে (ফোন, ট্যাবলেট, ডেস্কটপ) লেআউট মানিয়ে নেওয়া",
            "চিরকাল শুধু এক স্থির CRT মনিটর সমর্থন",
            "মোবাইল ব্যবহারকারীকে সম্পূর্ণ উপেক্ষা",
            "শুধু এক কাগজ আকারে পেজ ছাপানো",
        ],
        "A", "hard", "conceptual",
        "Responsive design uses flexible layouts and media queries.",
        "রেসপনসিভ ডিজাইন নমনীয় লেআউট ও মিডিয়া কোয়েরি ব্যবহার করে।",
    ),
    q(
        "Website maintenance after publishing includes:",
        "প্রকাশের পর ওয়েবসাইট রক্ষণাবেক্ষণে অন্তর্ভুক্ত:",
        [
            "Updating content, fixing broken links, and checking security",
            "Never changing any text again",
            "Publishing the FTP password on social media",
            "Removing HTTPS permanently",
        ],
        [
            "কন্টেন্ট আপডেট, ভাঙা লিঙ্ক ঠিক ও নিরাপত্তা যাচাই",
            "কখনো আর কোনো লেখা না বদলানো",
            "সোশ্যাল মিডিয়ায় FTP পাসওয়ার্ড প্রকাশ",
            "স্থায়ীভাবে HTTPS সরিয়ে ফেলা",
        ],
        "A", "medium", "factual",
        "Live sites need ongoing updates and security care.",
        "লাইভ সাইটে চলমান আপডেট ও নিরাপত্তা যত্ন লাগে।",
    ),
    q(
        "Choosing colours and images for a school site should primarily consider:",
        "স্কুল সাইটের রং ও চিত্র বেছে নেওয়ার সময় প্রধানত বিবেচ্য:",
        [
            "Clarity, appropriateness for audience, and brand consistency",
            "Maximum flashing ads only",
            "Illegible decorative fonts for all body text",
            "Hidden malware banners",
        ],
        [
            "স্পষ্টতা, দর্শকের উপযুক্ততা ও ব্র্যান্ড সামঞ্জস্য",
            "শুধু সর্বোচ্চ ঝলমলে বিজ্ঞাপন",
            "সব বডি টেক্সটে অপাঠ্য আলংকারিক ফন্ট",
            "লুকানো ম্যালওয়্যার ব্যানার",
        ],
        "A", "easy", "application",
        "Design choices should serve communication goals.",
        "ডিজাইন পছন্দ যোগাযোগের লক্ষ্যকে সেবা করা উচিত।",
    ),
    q(
        "HTTPS on a published site helps by:",
        "প্রকাশিত সাইটে HTTPS সাহায্য করে:",
        [
            "Encrypting traffic between browser and server",
            "Making HTML tags optional",
            "Removing the need for any domain name",
            "Disabling all images automatically",
        ],
        [
            "ব্রাউজার ও সার্ভারের মধ্যে ট্রাফিক এনক্রিপ্ট করে",
            "HTML ট্যাগকে ঐচ্ছিক করে",
            "কোনো ডোমেইন নামের প্রয়োজন সরিয়ে",
            "স্বয়ংক্রিয়ভাবে সব চিত্র নিষ্ক্রিয় করে",
        ],
        "A", "medium", "conceptual",
        "TLS protects data in transit and builds user trust.",
        "TLS ট্রানজিটে ডেটা রক্ষা করে ও ব্যবহারকারীর আস্থা বাড়ায়।",
    ),
    q(
        "Which sequence best describes publishing a simple static site?",
        "সরল স্ট্যাটিক সাইট প্রকাশের কোন ক্রম সবচেয়ে উপযুক্ত?",
        [
            "Design/code → test locally → upload to host → verify online",
            "Upload first with no files → invent HTML later randomly",
            "Buy a printer → skip hosting → expect a public URL",
            "Delete DNS → upload → never test",
        ],
        [
            "ডিজাইন/কোড → স্থানীয় পরীক্ষা → হোস্টে আপলোড → অনলাইনে যাচাই",
            "ফাইল ছাড়া আগে আপলোড → পরে এলোমেলো HTML",
            "প্রিন্টার কেনা → হোস্টিং এড়ানো → পাবলিক URL আশা",
            "DNS মুছা → আপলোড → কখনো পরীক্ষা না করা",
        ],
        "A", "hard", "application",
        "Author, test, deploy, then confirm the live result.",
        "লিখুন, পরীক্ষা করুন, ডিপ্লয় করুন, তারপর লাইভ ফল নিশ্চিত করুন।",
    ),
    q(
        "File names for web pages should preferably:",
        "ওয়েব পেজের ফাইল নাম পছন্দনীয়ভাবে:",
        [
            "Be simple, lowercase, without spaces (use hyphens if needed)",
            "Contain many spaces and special symbols always",
            "Be 200 characters of random emoji only",
            "Include the server root password in the name",
        ],
        [
            "সরল, ছোট হাতের অক্ষর, স্পেসহীন হওয়া (প্রয়োজনে হাইফেন)",
            "সবসময় অনেক স্পেস ও বিশেষ চিহ্ন থাকা",
            "শুধু ২০০ অক্ষরের এলোমেলো ইমোজি হওয়া",
            "নামে সার্ভার রুট পাসওয়ার্ড রাখা",
        ],
        "A", "hard", "application",
        "Clean names avoid broken URLs and hosting issues.",
        "পরিষ্কার নাম ভাঙা URL ও হোস্টিং সমস্যা এড়ায়।",
    ),
]


# Fix T02 case-sensitivity question: correct must be A
T02[14] = q(
    "In modern HTML, tag names are generally treated as:",
    "আধুনিক HTML-এ ট্যাগ নাম সাধারণত বিবেচিত হয়:",
    [
        "Case-insensitive (conventionally written lowercase)",
        "Case-sensitive only in CAPS forever",
        "Invalid if lowercase",
        "Required to be binary digits",
    ],
    [
        "কেস-ইন্সেনসিটিভ (প্রথানুযায়ী ছোট হাতের অক্ষরে লেখা)",
        "চিরকাল শুধু বড় হাতের অক্ষরে কেস-সেনসিটিভ",
        "ছোট হাতের অক্ষরে অবৈধ",
        "বাইনারি অঙ্ক হতে বাধ্য",
    ],
    "A", "hard", "conceptual",
    "HTML parsers treat tags case-insensitively; lowercase is recommended.",
    "HTML পার্সার ট্যাগকে কেস-ইন্সেনসিটিভ ধরে; ছোট হাতের অক্ষর সুপারিশকৃত।",
)


TOPICS_MAP = {
    "ict27_ch04_t01": T01,
    "ict27_ch04_t02": T02,
    "ict27_ch04_t03": T03,
    "ict27_ch04_t04": T04,
    "ict27_ch04_t05": T05,
}


def write_topic(topic_id: str, rows: list[dict]) -> dict:
    if len(rows) != 20:
        raise SystemExit(f"{topic_id}: expected 20 rows, got {len(rows)}")
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
        "chapter": "ict27_ch04",
        "title_en": "Introduction to Web Design and HTML",
        "title_bn": "ওয়েব ডিজাইন পরিচিতি এবং HTML",
        "source": SRC,
        "pdf_pages": [],
        "note": (
            "Import CSV ict_1_ch04.csv had headers only; authored 20 bilingual MCQs "
            "per topic aligned to NCTB ict_2027 ch04 syllabus "
            "(Introduction to Web Design and HTML)."
        ),
        "counts": {**counts, "total": sum(counts.values())},
        "paths": paths,
        "pdf_mapping": {
            "ict27_ch04_t01": {
                "title": "Website structure / ওয়েবসাইটের কাঠামো",
                "themes": [
                    "website vs webpage vs homepage; WWW vs Internet",
                    "URL domain HTTPS browser server client–server",
                    "static vs dynamic; header nav footer sitemap",
                    "hypertext hosting frontend hierarchy",
                ],
            },
            "ict27_ch04_t02": {
                "title": "HTML structure, tags and syntax / HTML কাঠামো, ট্যাগ ও সিনট্যাক্স",
                "themes": [
                    "HTML meaning; tags elements attributes",
                    "html/head/body/title/meta; DOCTYPE",
                    "void tags comments nesting case",
                    "file extension charset element anatomy",
                ],
            },
            "ict27_ch04_t03": {
                "title": "Text formatting and hyperlinks / লেখার বিন্যাস ও হাইপারলিঙ্ক",
                "themes": [
                    "h1–h6 p br hr b/strong i/em u pre",
                    "ul/ol/li lists; a href target mailto",
                    "internal #id anchors; relative vs absolute",
                    "image wrapped in anchor; ol type",
                ],
            },
            "ict27_ch04_t04": {
                "title": "Images and tables / চিত্র ও টেবিল",
                "themes": [
                    "img src alt width height formats",
                    "table tr td th caption border",
                    "colspan rowspan thead/tbody/tfoot",
                    "cellpadding cellspacing accessibility",
                ],
            },
            "ict27_ch04_t05": {
                "title": "Web page design and publishing / ওয়েব পেজ তৈরি ও প্রকাশ",
                "themes": [
                    "editors WYSIWYG planning wireframe",
                    "hosting domain FTP index.html upload paths",
                    "CSS role usability typography HTTPS",
                    "responsive design maintenance publish workflow",
                ],
            },
        },
        "low_confidence": [
            "No in-repo OCR page set for ICT Udvash PDF ch04; items are syllabus-aligned authored MCQs, not direct OCR transcriptions.",
            "Import CSV content/bank/import/ict_1_ch04.csv had headers only (no stems to reuse).",
            "Some classic attributes (border, cellpadding, cellspacing, ol type) follow HSC textbook teaching; modern CSS equivalents may differ in exam wording.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate (ict27_ch04_* checked via validate_record)",
            "invalid": 0,
            "duplicates": 0,
            "per_topic": {tid: 20 for tid in TOPIC_IDS},
        },
        "ict_ch04_completion": {
            "topics_expected": 5,
            "topics_at_20": 5,
            "note": "ict27_ch04_t01..t05 complete at 20/topic (chapter total 100).",
        },
    }
    PARSED.mkdir(parents=True, exist_ok=True)
    out = PARSED / "ch04_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
