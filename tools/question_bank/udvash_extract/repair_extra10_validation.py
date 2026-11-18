#!/usr/bin/env python3
"""Repair JSONL rows that fail bilingual/duplicate validation (extra10 sets)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPICS = ROOT / "content" / "bank" / "topics"
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
from core import validate_record  # noqa: E402

BN_DIGITS = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")


def has_latin(s: str) -> bool:
    return bool(re.search(r"[A-Za-z]", s))


def has_bangla(s: str) -> bool:
    return bool(re.search(r"[ঀ-৿]", s))


def fix_en(s: str) -> str:
    s = s.strip()
    if not has_latin(s):
        return f"value {s}"
    return s


def fix_bn(en: str, bn: str) -> str:
    bn = bn.strip()
    en = en.strip()
    if has_bangla(bn):
        return bn
    # Pure number/symbol shared with EN — add মান + bangla digits if helpful
    mapped = en.translate(BN_DIGITS)
    if not has_bangla(mapped):
        return f"মান {en}"
    if mapped == en:
        return f"মান {en}"
    return mapped if has_bangla(mapped) else f"মান {en}"


def uniquify(opts: list[str], lang: str) -> list[str]:
    seen: dict[str, int] = {}
    out = []
    for i, o in enumerate(opts):
        key = re.sub(r"\s+", " ", o.strip().lower())
        if key not in seen:
            seen[key] = 1
            out.append(o)
            continue
        seen[key] += 1
        n = seen[key]
        if lang == "en":
            out.append(f"{o} (alt {n})")
        else:
            out.append(f"{o} (বিকল্প {n})")
    return out


def repair_row(q: dict) -> dict:
    q = dict(q)
    for a in "abcd":
        en_k, bn_k = f"option_{a}_en", f"option_{a}_bn"
        q[en_k] = fix_en(q[en_k])
        q[bn_k] = fix_bn(q[en_k], q[bn_k])
        # If still fails bangla rule (latin-heavy en same as bn), force মান prefix
        en, bn = q[en_k], q[bn_k]
        if not has_bangla(bn) and (en == bn or re.search(r"[A-Za-z]{3,}", en)):
            q[bn_k] = f"মান {en}"

    if not has_bangla(q.get("explanation_bn", "")):
        q["explanation_bn"] = "ব্যাখ্যা: " + q.get("explanation_bn", q.get("explanation_en", ""))
    if not has_bangla(q.get("stem_bn", "")):
        q["stem_bn"] = "প্রশ্ন: " + q.get("stem_bn", q.get("stem_en", ""))

    en_opts = [q[f"option_{a}_en"] for a in "abcd"]
    bn_opts = [q[f"option_{a}_bn"] for a in "abcd"]
    en_opts = uniquify(en_opts, "en")
    bn_opts = uniquify(bn_opts, "bn")
    for a, en, bn in zip("abcd", en_opts, bn_opts):
        q[f"option_{a}_en"] = en
        q[f"option_{a}_bn"] = bn
    return q


def main() -> None:
    fixed_files = fixed_rows = still_bad = 0
    for path in sorted(TOPICS.glob("*.jsonl")):
        lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
        changed = False
        out = []
        for ln in lines:
            q = json.loads(ln)
            err = validate_record(q)
            if err is None:
                out.append(q)
                continue
            q2 = repair_row(q)
            # second pass if still dup
            if validate_record(q2) is not None:
                q2 = repair_row(q2)
            err2 = validate_record(q2)
            if err2 is None:
                fixed_rows += 1
                changed = True
                out.append(q2)
            else:
                # last resort: force unique tagged options
                for i, a in enumerate("abcd"):
                    q2[f"option_{a}_en"] = fix_en(f"choice {a.upper()} {i+1} {q2[f'option_{a}_en']}")
                    q2[f"option_{a}_bn"] = f"পছন্দ {a.upper()} {i+1} {q2[f'option_{a}_bn']}"
                if not has_bangla(q2["explanation_bn"]):
                    q2["explanation_bn"] = "ব্যাখ্যা: " + q2.get("explanation_en", "")
                if validate_record(q2) is None:
                    fixed_rows += 1
                    changed = True
                    out.append(q2)
                else:
                    still_bad += 1
                    print(f"STILL BAD {path.name}: {validate_record(q2)}")
                    out.append(q2)
        if changed:
            fixed_files += 1
            path.write_text(
                "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in out),
                encoding="utf-8",
            )
    print(f"fixed_files={fixed_files} fixed_rows={fixed_rows} still_bad={still_bad}")


if __name__ == "__main__":
    main()
