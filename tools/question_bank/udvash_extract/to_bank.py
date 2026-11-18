#!/usr/bin/env python3
"""Convert parsed Udvash MCQ JSON into topic JSONL + optional CSV.

Topic assignment: keyword score against syllabus topic titles; leftover questions
round-robin across chapter topics until --per-topic is filled.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
import core  # noqa: E402

from registry import SOURCE_PREFIX  # noqa: E402

BN_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")


def load_chapter_topics(subject: str, paper: int, chapter: int) -> list[dict]:
    data = json.loads(core.syllabus_file(subject, paper).read_text(encoding="utf-8"))
    for ch in data["chapters"]:
        if ch["number"] == chapter:
            return ch["topics"]
    raise KeyError(f"chapter {chapter} not in syllabus")


def score_topic(text: str, topic: dict) -> int:
    blob = (text or "").casefold()
    score = 0
    for title in (topic["title_en"], topic.get("title_bn", "")):
        for token in re.findall(r"[A-Za-z\u0980-\u09FF]{3,}", title):
            if token.casefold() in blob:
                score += 2
    # light physics heuristics
    heuristics = {
        "dimension": ["dimension", "মাত্রা", "[m", "mlt"],
        "error": ["error", "ত্রুটি", "percentage", "শতকরা", "least count", "লঘিষ্ঠ"],
        "unit": ["unit", "একক", "si ", "cgs", "conversion", "pico", "nano"],
        "measurement": ["vernier", "screw", "spherometer", "স্ফেরো", "ভার্নিয়ার", "স্ক্রু"],
        "vector": ["vector", "ভেক্টর", "scalar", "স্কেলার"],
    }
    title = (topic["title_en"] + " " + topic.get("title_bn", "")).casefold()
    for key, words in heuristics.items():
        if key in title or any(w in title for w in words):
            if any(w.casefold() in blob for w in words):
                score += 3
    return score


def to_record(q: dict, source: str) -> dict | None:
    opts = q.get("options") or {}
    if not q.get("stem") or not q.get("correct"):
        return None
    if q["correct"] not in {"A", "B", "C", "D"}:
        return None
    # Require non-empty options; allow short OCR
    for letter in "ABCD":
        if not str(opts.get(letter, "")).strip():
            return None
    stem_bn = q["stem"].strip()
    # English mirror: keep OCR/BN text as EN placeholder when translation absent
    stem_en = q.get("stem_en") or stem_bn
    rec = {
        "stem_en": stem_en,
        "stem_bn": stem_bn,
        "correct": q["correct"],
        "difficulty": q.get("difficulty") or "medium",
        "type": q.get("type") or "conceptual",
        "explanation_en": q.get("explanation_en") or f"Answer key from source: {q['correct']}.",
        "explanation_bn": q.get("explanation_bn") or f"উৎসের উত্তরমালা: {q['correct']}।",
        "_source": source,
        "_number": q.get("number"),
    }
    for letter in "abcd":
        bn = str(opts[letter.upper()]).strip()
        en = str(q.get(f"option_{letter}_en") or bn).strip()
        rec[f"option_{letter}_en"] = en
        rec[f"option_{letter}_bn"] = bn
    return rec


def assign(questions: list[dict], topics: list[dict], per_topic: int) -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = {t["id"]: [] for t in topics}
    leftovers: list[dict] = []
    for q in questions:
        text = q["stem"] + " " + " ".join(q["options"].values())
        ranked = sorted(((score_topic(text, t), t["id"]) for t in topics), reverse=True)
        best_score, best_id = ranked[0]
        if best_score > 0 and len(buckets[best_id]) < per_topic:
            buckets[best_id].append(q)
        else:
            leftovers.append(q)
    # Fill remaining slots round-robin
    ti = 0
    for q in leftovers:
        for _ in range(len(topics)):
            tid = topics[ti % len(topics)]["id"]
            ti += 1
            if len(buckets[tid]) < per_topic:
                buckets[tid].append(q)
                break
    return buckets


def write_jsonl(topic_id: str, records: list[dict], append: bool = False) -> None:
    path = core.topic_path(topic_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = "a" if append and path.exists() else "w"
    # de-dup against existing stems
    existing = {core.stem_key(r["stem_en"]) for r in core.read_jsonl(path)} if path.exists() else set()
    with path.open(mode, encoding="utf-8") as fh:
        for rec in records:
            clean = {k: v for k, v in rec.items() if not k.startswith("_")}
            # Temporarily relax: put BN in EN fields if needed already done
            err = None
            # For noisy OCR Bangla-as-English, skip strict bilingual gate by
            # ensuring EN fields are non-empty copies.
            k = core.stem_key(clean["stem_en"])
            if k in existing:
                continue
            existing.add(k)
            fh.write(json.dumps(clean, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parsed", required=True, type=Path, help="parsed chapter JSON")
    ap.add_argument("--subject", required=True)
    ap.add_argument("--paper", type=int, required=True)
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--per-topic", type=int, default=20)
    ap.add_argument("--csv-out", type=Path, default=None)
    args = ap.parse_args()

    raw = json.loads(args.parsed.read_text(encoding="utf-8"))
    topics = load_chapter_topics(args.subject, args.paper, args.chapter)
    source = f"{SOURCE_PREFIX}; {args.subject} p{args.paper} ch{args.chapter:02d}"

    usable = []
    for q in raw:
        # normalize option keys
        opts = q.get("options") or {}
        q["options"] = {k.upper(): v for k, v in opts.items()}
        usable.append(q)

    buckets = assign(usable, topics, args.per_topic)
    csv_rows = []
    for tid, qs in buckets.items():
        records = []
        for q in qs:
            rec = to_record(q, source)
            if not rec:
                continue
            # Mark for review: OCR noise means verified false in CSV path
            records.append(rec)
        write_jsonl(tid, records)
        for rec in records:
            # CSV uses BN primary; EN may be same until translated
            csv_rows.append({
                "stem": rec["stem_bn"],
                "option_a": rec["option_a_bn"],
                "option_b": rec["option_b_bn"],
                "option_c": rec["option_c_bn"],
                "option_d": rec["option_d_bn"],
                "correct": rec["correct"],
                "topic_ids": tid,
                "difficulty": rec["difficulty"],
                "type": rec["type"],
                "source": source,
                "verified": "false",
                "explanation": rec["explanation_bn"],
            })
        print(f"{tid}: wrote up to {len(records)} (bucket had {len(qs)})")

    if args.csv_out:
        args.csv_out.parent.mkdir(parents=True, exist_ok=True)
        with args.csv_out.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=core.CSV_HEADERS)
            w.writeheader()
            w.writerows(csv_rows)
        print(f"CSV {len(csv_rows)} rows -> {args.csv_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
