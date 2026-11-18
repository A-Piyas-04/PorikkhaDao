#!/usr/bin/env python3
"""Check a syllabus JSON and chapter CSV without trusting the local pilot DB."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

HEADERS = [
    "stem", "option_a", "option_b", "option_c", "option_d", "correct",
    "topic_ids", "difficulty", "type", "source", "verified", "explanation",
]


def audit(syllabus_path: Path, csv_paths: list[Path]) -> list[str]:
    errors: list[str] = []
    data = json.loads(syllabus_path.read_text(encoding="utf-8"))
    for field in ("curriculum_version", "subject", "paper", "chapters"):
        if not data.get(field):
            errors.append(f"{syllabus_path}: missing {field}")
    topics: dict[str, int] = {}
    chapter_ids: set[str] = set()
    chapter_numbers: set[int] = set()
    for chapter in data.get("chapters", []):
        cid = chapter.get("id", "")
        number = chapter.get("number")
        if not isinstance(number, int) or number in chapter_numbers:
            errors.append(f"{syllabus_path}: duplicate or invalid chapter number {number!r}")
        chapter_numbers.add(number)
        if cid in chapter_ids or not re.fullmatch(r"[a-z0-9_]+", cid):
            errors.append(f"{syllabus_path}: duplicate or invalid chapter id {cid!r}")
        chapter_ids.add(cid)
        if not chapter.get("title_en") or not chapter.get("title_bn"):
            errors.append(f"{syllabus_path}: missing chapter title at {cid}")
        topic_orders: set[int] = set()
        if not chapter.get("topics"):
            errors.append(f"{syllabus_path}: chapter {cid} has no topics")
        for topic in chapter.get("topics", []):
            tid = topic.get("id", "")
            order = topic.get("order")
            if not isinstance(order, int) or order in topic_orders:
                errors.append(f"{syllabus_path}: duplicate or invalid topic order {order!r} at {cid}")
            topic_orders.add(order)
            if tid in topics or not re.fullmatch(r"[a-z0-9_]+", tid):
                errors.append(f"{syllabus_path}: duplicate or invalid topic id {tid!r}")
            topics[tid] = chapter.get("number")
            if not topic.get("title_en") or not topic.get("title_bn"):
                errors.append(f"{syllabus_path}: missing topic title at {tid}")
        if topic_orders != set(range(1, len(topic_orders) + 1)):
            errors.append(f"{syllabus_path}: non-consecutive topic orders at {cid}")
    if chapter_numbers != set(range(1, len(chapter_numbers) + 1)):
        errors.append(f"{syllabus_path}: non-consecutive chapter numbers")

    seen_stems: set[str] = set()
    for path in csv_paths:
        match = re.search(r"_ch(\d+)\.csv$", path.name)
        expected_chapter = int(match.group(1)) if match else None
        with path.open(encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            if reader.fieldnames != HEADERS:
                errors.append(f"{path}: headers do not match the import template")
                continue
            for line, row in enumerate(reader, 2):
                where = f"{path}:{line}"
                for field in ("stem", "option_a", "option_b", "option_c", "option_d", "source"):
                    if not (row.get(field) or "").strip():
                        errors.append(f"{where}: empty {field}")
                stem = re.sub(r"\s+", " ", (row.get("stem") or "").strip().casefold())
                if stem in seen_stems:
                    errors.append(f"{where}: duplicate stem")
                seen_stems.add(stem)
                options = [(row.get(f"option_{letter}") or "").strip().casefold() for letter in "abcd"]
                if len(set(options)) != 4:
                    errors.append(f"{where}: options are not distinct")
                if row.get("correct") not in {"A", "B", "C", "D"}:
                    errors.append(f"{where}: invalid correct option")
                if row.get("verified") not in ("true", "false"):
                    errors.append(f"{where}: invalid verified value")
                if row.get("difficulty") not in ("", "easy", "medium", "hard"):
                    errors.append(f"{where}: invalid difficulty")
                if row.get("type") not in ("", "factual", "conceptual", "numerical", "application"):
                    errors.append(f"{where}: invalid type")
                ids = [item.strip() for item in (row.get("topic_ids") or "").split(";")]
                if not ids or any(not item for item in ids):
                    errors.append(f"{where}: empty topic id")
                for tid in ids:
                    if tid not in topics:
                        errors.append(f"{where}: unknown topic {tid}")
                    elif expected_chapter is not None and topics[tid] != expected_chapter:
                        errors.append(f"{where}: topic {tid} belongs to another chapter")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("syllabus", type=Path)
    parser.add_argument("csv", nargs="*", type=Path)
    args = parser.parse_args()
    problems = audit(args.syllabus, args.csv)
    for problem in problems:
        print(problem)
    print(f"{'FAIL' if problems else 'OK'}: {len(args.csv)} CSV file(s), {len(problems)} issue(s)")
    raise SystemExit(bool(problems))
