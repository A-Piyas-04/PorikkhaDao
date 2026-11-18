"""Extract *candidate* chapter headings from NCTB curriculum PDFs.

The PDFs contain legacy Bijoy text. Conversion and heading detection are
fallible; this CSV is a review aid, never a publishable syllabus.
"""

from __future__ import annotations

import csv
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import fitz
import requests
from bijoy_unicode import to_unicode


ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "content/sources/nctb_higher_secondary_curricula.json"
OUT = ROOT / "content/sources/nctb_chapter_candidates.csv"
ORDINALS = "প্রথম|দ্বিতীয়|তৃতীয়|চতুর্থ|পঞ্চম|ষষ্ঠ|সপ্তম|অষ্টম|নবম|দশম|একাদশ|দ্বাদশ|ত্রয়োদশ|চতুর্দশ|পঞ্চদশ"
HEADING = re.compile(rf"(?:{ORDINALS})\s*অধ্যা[য়য়]\s*[:ঃ]?\s*.+")


def extract_one(item: dict[str, str]) -> list[dict[str, str | int]]:
    url = item["pdf_url"]
    if not url.startswith("https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/"):
        raise ValueError(f"Unexpected source domain: {url}")
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    document = fitz.open(stream=response.content, filetype="pdf")
    records = []
    for page_number, page in enumerate(document, 1):
        converted = to_unicode(page.get_text(), keep_english=True)
        for line in converted.splitlines():
            line = " ".join(line.split())
            if len(line) <= 180 and HEADING.search(line):
                records.append({
                    "subject_bn": item["name_bn"],
                    "page": page_number,
                    "candidate_heading": line,
                    "source_url": url,
                })
    return records


def main() -> None:
    items = json.loads(INDEX.read_text(encoding="utf-8"))["curricula"]
    all_records = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(extract_one, item): item for item in items}
        for future in as_completed(futures):
            item = futures[future]
            result = future.result()
            print(f"{item['name_bn']}: {len(result)} chapter heading candidates")
            all_records.extend(result)
    order = {item["name_bn"]: i for i, item in enumerate(items)}
    all_records.sort(key=lambda row: (order[row["subject_bn"]], row["page"], row["candidate_heading"]))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["subject_bn", "page", "candidate_heading", "source_url"])
        writer.writeheader()
        writer.writerows(all_records)
    print(f"Wrote {len(all_records)} candidates to {OUT}")


if __name__ == "__main__":
    main()
