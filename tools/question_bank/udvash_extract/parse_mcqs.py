#!/usr/bin/env python3
"""Parse OCR text into structured MCQs + answer keys.

Heuristic parser for Udvash two-column MCQ pages. Tolerates noisy OCR.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

Q_START = re.compile(
    r"(?m)^\s*(?:0?(\d{1,3})|০?([০-৯]{1,3}))[\.|\)]\s*(.+)$"
)
OPT = re.compile(
    r"(?m)^\s*[\(\[]?\s*([abcdabcdABCDকখগঘ]|[০-৩0-3])\s*[\)\].:-]\s*(.+)$"
)
# Inline: (a) foo (b) bar (c) baz (d) qux  — also tolerates OCR (by / (0) / (০)
INLINE_OPTS = re.compile(
    r"[\(\[]\s*([abcdABCDকখগঘ])\s*[\)\]]\s*([^(\[]+?)(?=[\(\[]\s*[abcdABCDকখগঘ]\s*[\)\]]|$)"
)
ANSWER_GRID = re.compile(
    r"(?i)(?:0?(\d{1,3})|০?([০-৯]{1,3}))\s*[\.:\-]?\s*([abcdABCDকখগঘ])\b"
)
BN_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")

OPT_MAP = {
    "a": "A", "b": "B", "c": "C", "d": "D",
    "A": "A", "B": "B", "C": "C", "D": "D",
    "ক": "A", "খ": "B", "গ": "C", "ঘ": "D",
    "0": "A", "1": "B", "2": "C", "3": "D",
    "০": "A", "১": "B", "২": "C", "৩": "D",
}


def bn_int(s: str) -> int:
    return int(s.translate(BN_DIGITS))


def normalize_opt(raw: str) -> str | None:
    raw = raw.strip()
    if raw in OPT_MAP:
        return OPT_MAP[raw]
    low = raw.lower()
    return OPT_MAP.get(low)


def parse_text(text: str) -> tuple[list[dict], dict[int, str]]:
    """Return (questions, answers_by_num). Questions may lack correct until merged."""
    # Drop answer/explanation sections from question parsing by splitting.
    parts = re.split(r"MCQ\s*উত্তরমালা|উত্তরমালা\s*ও\s*ব্যাখ্যা|ব্যাখ্যামূলক\s*সমাধান", text, flags=re.I)
    body = parts[0]
    answer_blob = "\n".join(parts[1:]) if len(parts) > 1 else text

    answers: dict[int, str] = {}
    for m in ANSWER_GRID.finditer(answer_blob):
        num = bn_int(m.group(1) or m.group(2))
        key = normalize_opt(m.group(3))
        if key and num not in answers:
            answers[num] = key

    lines = [ln.rstrip() for ln in body.splitlines()]
    questions: list[dict] = []
    cur: dict | None = None

    def flush():
        nonlocal cur
        if not cur:
            return
        opts = cur.get("options") or {}
        if cur.get("stem") and len(opts) >= 2:
            # pad missing options
            for letter in "ABCD":
                opts.setdefault(letter, "")
            cur["options"] = {k: opts[k] for k in "ABCD"}
            questions.append(cur)
        cur = None

    for ln in lines:
        if not ln.strip() or ln.startswith("====="):
            continue
        qm = Q_START.match(ln)
        if qm:
            flush()
            num = bn_int(qm.group(1) or qm.group(2))
            cur = {"number": num, "stem": qm.group(3).strip(), "options": {}}
            continue
        # Prefer extracting all inline (a)(b)(c)(d) from the line first.
        inline = list(INLINE_OPTS.finditer(ln))
        if cur is not None and len(inline) >= 2:
            for im in inline:
                letter = normalize_opt(im.group(1))
                if letter and letter not in cur["options"]:
                    cur["options"][letter] = im.group(2).strip(" .;|")
            continue
        om = OPT.match(ln)
        if om and cur is not None:
            letter = normalize_opt(om.group(1))
            if letter and letter not in cur["options"]:
                # remainder may still contain further inline options
                rest = om.group(2)
                more = list(INLINE_OPTS.finditer("(" + om.group(1) + ") " + rest))
                if len(more) >= 2:
                    for im in more:
                        letter2 = normalize_opt(im.group(1))
                        if letter2 and letter2 not in cur["options"]:
                            cur["options"][letter2] = im.group(2).strip(" .;|")
                else:
                    cur["options"][letter] = rest.strip()
            continue
        if cur is not None and len(cur["options"]) < 4:
            # continuation of stem or last option
            if not cur["options"]:
                cur["stem"] = (cur["stem"] + " " + ln.strip()).strip()
            else:
                last = list(cur["options"])[-1]
                cur["options"][last] = (cur["options"][last] + " " + ln.strip()).strip()
    flush()

    for q in questions:
        q["correct"] = answers.get(q["number"])
    return questions, answers


def load_manual_keys(path: Path | None) -> dict[int, str]:
    if not path or not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    keys = data.get("keys") or data
    out: dict[int, str] = {}
    for k, v in keys.items():
        letter = str(v).strip().upper()
        if letter in {"A", "B", "C", "D"}:
            out[int(k)] = letter
    return out


def parse_chapter_dir(ch_dir: Path, manual_keys: Path | None = None) -> list[dict]:
    by_num: dict[int, dict] = {}
    all_answers: dict[int, str] = {}
    all_answers.update(load_manual_keys(manual_keys))
    for txt in sorted(ch_dir.glob("*.txt")):
        if txt.parent.name == "cols" or "_L" in txt.name or "_R" in txt.name:
            continue
        text = txt.read_text(encoding="utf-8", errors="replace")
        qs, ans = parse_text(text)
        # Manual keys win over OCR grid guesses.
        for num, letter in ans.items():
            all_answers.setdefault(num, letter)
        for q in qs:
            # Prefer longer stem if duplicate number appears across pages
            prev = by_num.get(q["number"])
            if not prev or len(q["stem"]) > len(prev["stem"]):
                by_num[q["number"]] = q
    out = []
    for num in sorted(by_num):
        q = by_num[num]
        if num in all_answers:
            q["correct"] = all_answers[num]
        out.append(q)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ocr-dir", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--keys", type=Path, default=None, help="optional manual answer-key JSON")
    args = ap.parse_args()
    questions = parse_chapter_dir(args.ocr_dir, manual_keys=args.keys)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(questions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    keyed = sum(1 for q in questions if q.get("correct"))
    complete = sum(1 for q in questions if q.get("correct") and all(q["options"].values()))
    print(f"parsed={len(questions)} with_key={keyed} complete_abcd={complete} -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
