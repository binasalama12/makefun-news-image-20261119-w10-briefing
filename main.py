"""Global Briefing — Thursday, 19 November 2026, distilled.

A desk-brief format entry: the day's world news sorted into
Lead, Money, World, Science & Culture and Politics sections,
set in a clean corporate style. The briefing page is entry.png
in this repository; this program checks and issues it.
"""

import json
import shutil
from pathlib import Path

MANIFEST = {
    "edition": "Global Briefing",
    "date": "Thursday, 19 November 2026",
    "sections": {
        "LEAD": [
            "GTA VI launches worldwide after a 13-year wait",
            "Trump, Xi and Putin meet at APEC in Shenzhen",
        ],
        "MONEY": [
            "EU proposes a 45bn euro Ukraine loan",
            "Fed minutes: most officials expect further hikes",
            "Anthropic eyes a $1.4tn market debut",
        ],
        "WORLD": [
            "US and Iran exchange fire again in the Gulf",
            "Crimean Bridge attacked again, officials say",
            "Cyclone Akvan nears India's east coast",
        ],
        "SCIENCE & CULTURE": [
            "Voyager 1 reaches one light-day from Earth",
            "Van Gogh sells for a record $190.4m",
            "Ebola in DR Congo passes 11,000 cases",
        ],
        "POLITICS": [
            "Jeffries nominated: first African-American Speaker",
            "Canada recalibrates its China ties",
        ],
    },
}


def briefing_page() -> Path:
    return Path(__file__).resolve().parent / "entry.png"


def issue(page: Path) -> Path:
    blob = page.read_bytes()
    if blob[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("briefing page is not a PNG")
    if len(blob) > 1_048_576:
        raise SystemExit("briefing page exceeds 1 MiB")
    out = Path("/output/entry.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(page, out)
    return out


def main() -> None:
    out = issue(briefing_page())
    print(json.dumps({"edition": MANIFEST["edition"], "date": MANIFEST["date"]}))
    total = sum(len(v) for v in MANIFEST["sections"].values())
    print(f"{total} items across {len(MANIFEST['sections'])} sections")
    for section, items in MANIFEST["sections"].items():
        print(f"[{section}]")
        for item in items:
            print(f"  - {item}")
    print(f"briefing issued at {out}")


if __name__ == "__main__":
    main()
