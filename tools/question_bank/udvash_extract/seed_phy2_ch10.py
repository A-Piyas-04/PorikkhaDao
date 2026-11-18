#!/usr/bin/env python3
"""Seed Physics 2nd Paper Ch10 (Semiconductors and Electronics).

Curated from Udvash HSC Question Bank 2026 pages p330–p338 (PDF 336–344).
Writes exactly 20 bilingual JSONL rows per topic under content/bank/topics/.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools" / "question_bank" / "pipeline"))
from core import validate_record  # noqa: E402

TOPICS = ROOT / "content" / "bank" / "topics"
PARSED = ROOT / "content" / "bank" / "udvash_raw" / "physics_2" / "parsed"
SOURCE = (
    "Udvash HSC Question Bank 2026; licensed redistribution; "
    "physics p2 ch10; curated bilingual"
)


def _norm_pair(en: str, bn: str) -> tuple[str, str]:
    en, bn = en.strip(), bn.strip()
    if not re.search(r"[A-Za-z]", en):
        en = f"value {en}"
    if not re.search(r"[ঀ-৿]", bn):
        raw = bn
        bn = f"মান {raw}"
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
        "source": SOURCE,
        "verified": False,
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
        row["source"] = SOURCE
        err = validate_record(row)
        if err:
            raise SystemExit(f"{topic_id}: {err}\n{row['stem_en'][:100]}")
        lines.append(json.dumps(row, ensure_ascii=False))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return mapping


# ---------------------------------------------------------------------------
# t01 — Band theory and materials
# ---------------------------------------------------------------------------
T01 = [
    q(
        "For silicon, the energy gap between the valence band and the conduction band is—",
        "সিলিকনের জন্য যৌজন ব্যান্ড ও পরিবহণ ব্যান্ডের মধ্যে শক্তি ব্যবধানের মান কোনটি?",
        ["1.6 eV", "1.1 eV", "0.7 eV", "0.3 eV"],
        ["1.6 eV", "1.1 eV", "0.7 eV", "0.3 eV"],
        "B", "easy", "factual",
        "Printed key: Si band gap ≈ 1.1 eV.",
        "মুদ্রিত চাবি: সিলিকনের শক্তি ব্যবধান প্রায় ১.১ eV।",
        bank_n=7,
    ),
    q(
        "In which of the following do the valence and conduction bands overlap (no energy gap)?",
        "যোজন ব্যান্ড এবং পরিবহন ব্যান্ডের মধ্যে কোনো ফাঁকা থাকে না নিচের কোনটিতে?",
        ["Silicon", "Germanium", "Ceramic", "Copper"],
        ["সিলিকন", "জার্মেনিয়াম", "সিরামিক", "তামা"],
        "D", "easy", "factual",
        "Printed key: copper is a conductor with overlapping bands.",
        "মুদ্রিত চাবি: তামার যোজন ও পরিবহন ব্যান্ড অধিকৃত/ওভারল্যাপড।",
        bank_n=107,
    ),
    q(
        "The energy gap between the conduction band and valence band of a conductor is—",
        "পরিবাহী পদার্থের পরিবহন ব্যান্ড ও যোজন ব্যান্ডের মধ্যে শক্তি ব্যবধান—",
        ["0 eV", "0.7 eV", "1.1 eV", "7 eV"],
        ["0 eV", "0.7 eV", "1.1 eV", "7 eV"],
        "A", "easy", "factual",
        "Printed key: conductors have effectively zero forbidden gap.",
        "মুদ্রিত চাবি: পরিবাহীতে শক্তি ব্যবধান কার্যত শূন্য।",
        bank_n=48,
    ),
    q(
        "According to band theory, if there is no energy gap between valence and conduction bands, the material is a—",
        "ব্যান্ড তত্ত্বের আলোকে যোজন ব্যান্ড ও পরিবহন ব্যান্ডের মধ্যে শক্তি ব্যবধান না থাকলে পদার্থটি হবে—",
        ["Superconductor", "Conductor", "Semiconductor", "Insulator"],
        ["অতিপরিবাহী", "পরিবাহী", "অর্ধপরিবাহী", "অন্তরক"],
        "B", "easy", "conceptual",
        "Printed key: zero gap → conductor.",
        "মুদ্রিত চাবি: শূন্য ব্যবধান মানে পরিবাহী।",
        bank_n=49,
    ),
    q(
        "Forbidden energy bands exist in—\n(i) conductors\n(ii) semiconductors\n(iii) insulators\nWhich is correct?",
        "নিষিদ্ধ শক্তি ব্যান্ড থাকে—\n(i) পরিবাহীতে\n(ii) অর্ধপরিবাহীতে\n(iii) অন্তরকে\nনিচের কোনটি সঠিক?",
        ["i and ii", "i and iii", "ii and iii", "i, ii and iii"],
        ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        "C", "medium", "conceptual",
        "Printed key: forbidden gap exists in semiconductors and insulators, not conductors.",
        "মুদ্রিত চাবি: নিষিদ্ধ ব্যান্ড অর্ধপরিবাহী ও অন্তরকে থাকে, পরিবাহীতে নয়।",
        bank_n=52,
    ),
    q(
        "For germanium, the energy gap between valence and conduction bands is—",
        "Ge এর ক্ষেত্রে যোজন ব্যান্ড ও পরিবহন ব্যান্ডের মধ্যে শক্তির ব্যবধান কত?",
        ["0.7 eV", "1.1 eV", "6 eV", "7 eV"],
        ["0.7 eV", "1.1 eV", "6 eV", "7 eV"],
        "A", "easy", "factual",
        "Printed key: Ge band gap ≈ 0.7 eV.",
        "মুদ্রিত চাবি: জার্মেনিয়ামের শক্তি ব্যবধান প্রায় ০.৭ eV।",
        bank_n=86,
    ),
    q(
        "What is the approximate resistivity of a semiconductor?",
        "অর্ধপরিবাহীর আপেক্ষিক রোধের মান কত?",
        ["10^16 Ω m", "10^12 Ω m", "10^-8 Ω m", "10^-4 Ω m"],
        ["10^16 Ω m", "10^12 Ω m", "10^-8 Ω m", "10^-4 Ω m"],
        "D", "medium", "factual",
        "Printed key: semiconductor resistivity is of order ~10^-4 Ω m (between metal and insulator).",
        "মুদ্রিত চাবি: অর্ধপরিবাহীর আপেক্ষিক রোধ ~10^-4 Ω m ক্রমে।",
        bank_n=34,
    ),
    q(
        "The temperature coefficient of resistance of a semiconductor is—",
        "অর্ধপরিবাহীর রোধের উষ্ণতার সহগ—",
        ["Negative", "Zero", "Positive", "Infinite"],
        ["ঋণাত্মক", "শূন্য", "ধনাত্মক", "অসীম"],
        "A", "easy", "factual",
        "Printed key: semiconductor resistance falls with temperature → negative coefficient.",
        "মুদ্রিত চাবি: তাপমাত্রা বাড়লে রোধ কমে → ঋণাত্মক সহগ।",
        bank_n=33,
    ),
    q(
        "If temperature increases, the resistance of a semiconductor—",
        "তাপমাত্রা বৃদ্ধি পেলে অর্ধপরিবাহীর রোধ কীভাবে পরিবর্তিত হয়?",
        ["Increases", "First decreases then increases", "Remains the same", "Decreases"],
        ["বৃদ্ধি পায়", "প্রথমে হ্রাস পায় পরে বৃদ্ধি পায়", "একই থাকে", "হ্রাস পায়"],
        "D", "easy", "factual",
        "Printed key: more carriers are generated → resistance decreases.",
        "মুদ্রিত চাবি: বাহক সংখ্যা বাড়ে বলে রোধ হ্রাস পায়।",
        bank_n=45,
    ),
    q(
        "In which material do valence-band and conduction-band electron energies overlap?",
        "যোজন ব্যান্ড ও পরিবহণ ব্যান্ডে ইলেকট্রনের শক্তি অধিকৃত থাকে কোনটিতে?",
        ["Conductor", "Semiconductor", "Insulator", "Poor conductor"],
        ["পরিবাহী", "অর্ধপরিবাহী", "অন্তরক", "কু-পরিবাহী"],
        "A", "easy", "conceptual",
        "Printed key: conductors have overlapping valence and conduction bands.",
        "মুদ্রিত চাবি: পরিবাহীতে যোজন ও পরিবহণ ব্যান্ড অধিকৃত থাকে।",
        bank_n=18,
    ),
    q(
        "A typical insulator energy gap is of order—",
        "সাধারণ অন্তরকের শক্তি ব্যবধান প্রায় কোন ক্রমের?",
        ["0.01 eV", "0.7 eV", "1 eV", "5–15 eV"],
        ["0.01 eV", "0.7 eV", "1 eV", "5–15 eV"],
        "D", "medium", "factual",
        "Syllabus filler: insulators have large forbidden gaps (~several eV).",
        "সিলেবাস ফিলার: অন্তরকের নিষিদ্ধ ব্যবধান বড় (~কয়েক eV)।",
        filler=True,
    ),
    q(
        "At absolute zero, a pure semiconductor behaves like—",
        "পরম শূন্য তাপমাত্রায় বিশুদ্ধ অর্ধপরিবাহী আচরণ করে—",
        ["A perfect conductor", "An insulator", "A superconductor", "A metal"],
        ["নিখুঁত পরিবাহী", "অন্তরক", "অতিপরিবাহী", "ধাতু"],
        "B", "easy", "conceptual",
        "Syllabus filler: at 0 K the valence band is full and conduction band empty.",
        "সিলেবাস ফিলার: ০ K-এ যোজন ব্যান্ড পূর্ণ ও পরিবহণ ব্যান্ড শূন্য → অন্তরকসদৃশ।",
        filler=True,
    ),
    q(
        "Which statement about conductors is correct?",
        "পরিবাহী সম্পর্কে কোনটি সঠিক?",
        ["Large forbidden gap", "Valence and conduction bands overlap", "Only holes carry current", "Resistivity is ~10^12 Ω m"],
        ["বড় নিষিদ্ধ ব্যবধান", "যোজন ও পরিবহণ ব্যান্ড অধিকৃত", "শুধু হোল প্রবাহ বহন করে", "আপেক্ষিক রোধ ~10^12 Ω m"],
        "B", "easy", "conceptual",
        "Syllabus filler: overlapping bands define metallic conduction.",
        "সিলেবাস ফিলার: অধিকৃত ব্যান্ডই ধাতব পরিবাহিতার বৈশিষ্ট্য।",
        filler=True,
    ),
    q(
        "Compared with metals, semiconductors have—",
        "ধাতুর তুলনায় অর্ধপরিবাহীর—",
        ["Much lower resistivity always", "Resistivity between metals and insulators", "Zero band gap", "Positive temperature coefficient always"],
        ["সর্বদা অনেক কম রোধকতা", "ধাতু ও অন্তরকের মধ্যবর্তী রোধকতা", "শূন্য ব্যান্ড গ্যাপ", "সর্বদা ধনাত্মক উষ্ণতা সহগ"],
        "B", "easy", "conceptual",
        "Syllabus filler: semiconductor resistivity lies between metals and insulators.",
        "সিলেবাস ফিলার: অর্ধপরিবাহীর রোধকতা ধাতু ও অন্তরকের মাঝামাঝি।",
        filler=True,
    ),
    q(
        "In band theory, the forbidden energy region is called the—",
        "ব্যান্ড তত্ত্বে নিষিদ্ধ শক্তি অঞ্চলকে বলা হয়—",
        ["Valence band", "Conduction band", "Energy gap / forbidden band", "Fermi sea"],
        ["যোজন ব্যান্ড", "পরিবহণ ব্যান্ড", "শক্তি ফাঁক / নিষিদ্ধ ব্যান্ড", "ফার্মি সাগর"],
        "C", "easy", "factual",
        "Syllabus filler: the gap between valence and conduction bands is the forbidden band.",
        "সিলেবাস ফিলার: যোজন ও পরিবহণ ব্যান্ডের মধ্যবর্তী ফাঁকই নিষিদ্ধ ব্যান্ড।",
        filler=True,
    ),
    q(
        "Which material typically has the largest band gap among the following?",
        "নিচের কোন পদার্থের ব্যান্ড গ্যাপ সাধারণত সবচেয়ে বড়?",
        ["Copper", "Germanium", "Silicon", "Diamond / ceramic insulator"],
        ["তামা", "জার্মেনিয়াম", "সিলিকন", "হীরা / সিরামিক অন্তরক"],
        "D", "medium", "conceptual",
        "Syllabus filler: insulators such as diamond/ceramics have large gaps.",
        "সিলেবাস ফিলার: হীরা/সিরামিকের মতো অন্তরকের গ্যাপ অনেক বড়।",
        filler=True,
    ),
    q(
        "Electrical conductivity of an intrinsic semiconductor increases with temperature mainly because—",
        "বিশুদ্ধ অর্ধপরিবাহীর পরিবাহিতা তাপমাত্রায় বাড়ে প্রধানত কারণ—",
        ["Mobility always increases strongly", "More electron–hole pairs are generated", "Band gap becomes infinite", "Ions carry all current"],
        ["সচলতা সবসময় তীব্র বাড়ে", "অধিক ইলেকট্রন–হোল জোড়া সৃষ্টি হয়", "ব্যান্ড গ্যাপ অসীম হয়", "আয়নই সব প্রবাহ বহন করে"],
        "B", "medium", "conceptual",
        "Syllabus filler: thermal generation of carriers dominates the T dependence.",
        "সিলেবাস ফিলার: তাপীয় বাহক সৃষ্টিই তাপমাত্রা নির্ভরতার প্রধান কারণ।",
        filler=True,
    ),
    q(
        "Metals are good conductors primarily because—",
        "ধাতু ভালো পরিবাহী প্রধানত কারণ—",
        ["They have a huge forbidden gap", "Free electrons are available in overlapping/partially filled bands", "Only holes move", "They are always doped"],
        ["এদের নিষিদ্ধ ব্যবধান বিশাল", "অধিকৃত/আংশিক পূর্ণ ব্যান্ডে মুক্ত ইলেকট্রন থাকে", "শুধু হোল চলে", "এরা সবসময় ডোপড"],
        "B", "easy", "conceptual",
        "Syllabus filler: free electrons in overlapping bands enable conduction.",
        "সিলেবাস ফিলার: অধিকৃত ব্যান্ডের মুক্ত ইলেকট্রন পরিবহন সম্ভব করে।",
        filler=True,
    ),
    q(
        "Which ordering of band gaps is correct?",
        "ব্যান্ড গ্যাপের কোন ক্রমটি সঠিক?",
        ["Conductor > semiconductor > insulator", "Insulator > semiconductor > conductor", "Semiconductor > insulator > conductor", "All equal"],
        ["পরিবাহী > অর্ধপরিবাহী > অন্তরক", "অন্তরক > অর্ধপরিবাহী > পরিবাহী", "অর্ধপরিবাহী > অন্তরক > পরিবাহী", "সব সমান"],
        "B", "easy", "conceptual",
        "Syllabus filler: Eg(insulator) > Eg(semiconductor) > Eg(conductor≈0).",
        "সিলেবাস ফিলার: Eg(অন্তরক) > Eg(অর্ধপরিবাহী) > Eg(পরিবাহী≈0)।",
        filler=True,
    ),
    q(
        "In an insulator at room temperature, the conduction band is—",
        "কক্ষ তাপমাত্রায় অন্তরকের পরিবহণ ব্যান্ড—",
        ["Heavily populated by free electrons", "Essentially empty", "Completely overlapping the valence band", "Filled with holes only"],
        ["মুক্ত ইলেকট্রনে ভর্তি", "কার্যত শূন্য", "যোজন ব্যান্ডের সাথে পুরোপুরি অধিকৃত", "শুধু হোলে ভর্তি"],
        "B", "medium", "conceptual",
        "Syllabus filler: large gap keeps the conduction band nearly empty.",
        "সিলেবাস ফিলার: বড় গ্যাপের কারণে পরিবহণ ব্যান্ড প্রায় খালি থাকে।",
        filler=True,
    ),
]


from _ch10_part_a import build as build_a  # noqa: E402
from _ch10_part_b import build as build_b  # noqa: E402
from _ch10_part_c import build as build_c  # noqa: E402

T02, T03 = build_a(q)
T04, T05 = build_b(q)
T06, T07 = build_c(q)


def _mapping_stats(mapping: list) -> dict:
    main = [m for m in mapping if m != "filler" and m is not None]
    return {
        "main_bank": main,
        "cq_or_reconstructed_fillers": sum(1 for m in mapping if m == "filler"),
    }


def main() -> None:
    topics = {
        "phy2_27_ch10_t01": ("Band theory and materials / ব্যান্ড তত্ত্ব ও পদার্থের শ্রেণি", T01),
        "phy2_27_ch10_t02": ("Intrinsic and extrinsic semiconductors / বিশুদ্ধ ও অপদ্রব্যযুক্ত অর্ধপরিবাহী", T02),
        "phy2_27_ch10_t03": ("Electrons, holes and p/n types / ইলেকট্রন, হোল ও পি/এন টাইপ", T03),
        "phy2_27_ch10_t04": ("Junction diodes and rectification / জাংশন ডায়োড ও একমুখীকরণ", T04),
        "phy2_27_ch10_t05": ("Transistors and applications / ট্রানজিস্টর ও প্রয়োগ", T05),
        "phy2_27_ch10_t06": ("Number systems and binary operations / সংখ্যা পদ্ধতি ও বাইনারি অপারেশন", T06),
        "phy2_27_ch10_t07": ("Logic gates / লজিক গেট", T07),
    }

    pdf_mapping = {}
    counts = {}
    for tid, (title, items) in topics.items():
        mapping = write_topic(tid, items)
        counts[tid] = 20
        pdf_mapping[tid] = {"title": title, **_mapping_stats(mapping)}
    counts["total"] = 140

    # validate via bank pipeline
    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "question_bank" / "pipeline" / "bank.py"), "validate"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    stdout = (proc.stdout or "") + (proc.stderr or "")
    inv = 0
    dup = 0
    for line in stdout.splitlines():
        if "invalid" in line.lower() and "duplicate" in line.lower():
            # e.g. "invalid: 0   duplicates: 0"
            m = re.search(r"invalid:\s*(\d+).*duplicates:\s*(\d+)", line, re.I)
            if m:
                inv, dup = int(m.group(1)), int(m.group(2))

    summary = {
        "chapter": "phy2_27_ch10",
        "title_en": "Semiconductors and Electronics",
        "title_bn": "সেমিকন্ডাক্টর ও ইলেকট্রনিক্স",
        "source": "Udvash HSC Question Bank 2026; licensed redistribution",
        "pdf_pages": [
            "p330_pdf336.png",
            "p331_pdf337.png",
            "p332_pdf338.png",
            "p333_pdf339.png",
            "p334_pdf340.png",
            "p335_pdf341.png",
            "p336_pdf342.png",
            "p337_pdf343.png",
            "p338_pdf344.png",
        ],
        "skipped_faulty": {
            "Q21": "Printed voltage-gain options omit correct 4900 (dash in key) — skipped",
            "Q08_symbols_alt": "Non-basic gate symbol panels kept only as NOT basic-gate item",
            "Q39_print_dup": "Printed options listed XOR twice; curated as XNOR with fixed distractors",
            "Q44": "Four I–V graph panels; figure-only — skipped",
            "Q50": "Four NOR switch/LED circuit panels; figure-only — skipped",
            "Q14_panels": "Kept as reverse-bias wording from key without embedding all four circuit drawings",
            "Q02_graph": "Breakdown point P kept in text; full I–V figure not embedded",
        },
        "counts": counts,
        "pdf_mapping": pdf_mapping,
        "low_confidence": [
            "Q113 printed key c (electrons and holes in depletion) kept despite common 'ions only' wording.",
            "Q35 board frames α≈0.94 as switch rather than amplifier — printed key b kept.",
            "Q31 NOR-network boolean kept to printed key A; verify against upright figure if re-auditing.",
            "Some thin syllabus cells filled with reconstructed bilingual items marked filler.",
        ],
        "validate": {
            "command": "python tools/question_bank/pipeline/bank.py validate",
            "exit_code": proc.returncode,
            "invalid": inv,
            "duplicates": dup,
            "stdout_tail": "\n".join(stdout.strip().splitlines()[-8:]),
        },
    }
    out = PARSED / "ch10_curated_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(counts, indent=2))
    print("validate exit", proc.returncode, "invalid", inv, "duplicates", dup)
    print("summary", out)


if __name__ == "__main__":
    main()
