"""Capture official NCTB higher-secondary curriculum PDF links.

This is a source inventory, not a 2027 syllabus parser. The NCTB site has an
incomplete certificate chain on some clients, so the TLS bypass is restricted
to this known public index and the returned links are kept for human review.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning


INDEX = "https://nctb.gov.bd/pages/files/6922dbc6933eb65569e0c702"
OUT = Path(__file__).resolve().parents[2] / "content/sources/nctb_higher_secondary_curricula.json"
SCIENCE_SUBJECTS_BN = {
    "বাংলা", "ইংরেজ", "তথ্য ও যোগাযোগ প্রযুক্তি", "পদার্থবিদ্যা",
    "রসায়ন", "জীববিজ্ঞান", "উচ্চতর গণিত",
}


def main() -> None:
    disable_warnings(InsecureRequestWarning)
    response = requests.get(INDEX, timeout=30, verify=False)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    records = []
    for chip in soup.select(".chip[title]"):
        anchor = chip.find("a", href=True)
        if anchor is None or not anchor["href"].startswith("https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/"):
            continue
        name = chip["title"].strip()
        if name in SCIENCE_SUBJECTS_BN:
            records.append({"name_bn": name, "pdf_url": anchor["href"]})
    if {record["name_bn"] for record in records} != SCIENCE_SUBJECTS_BN:
        raise RuntimeError("NCTB science-group source index is incomplete or changed")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    retrieved_date = datetime.now(ZoneInfo("Asia/Dhaka")).date().isoformat()
    OUT.write_text(json.dumps({"scope": "hsc_science_group_and_common_subjects", "index_url": INDEX, "retrieved_date": retrieved_date, "curricula": records}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {len(records)} science-group curriculum links to {OUT}")


if __name__ == "__main__":
    main()
