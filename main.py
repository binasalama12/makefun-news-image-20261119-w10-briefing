#!/usr/bin/env python3
"""Global Briefing -- wallet w10 entry, news-image-20261119.

Design: a clean desk brief in five sections, covering the world
news of Thursday 19 November 2026 in a single image.

Behaviour: find entry.png in this repository, confirm it is a PNG
no larger than 1 MiB, copy it to /output/entry.png, and print the
briefing summary to stdout.
"""

import hashlib
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENTRY = HERE / "entry.png"
OUTPUT = Path("/output/entry.png")
MAGIC = b"\x89PNG\r\n\x1a\n"
CAP = 1024 * 1024


@dataclass
class Section:
    title: str
    items: list[str] = field(default_factory=list)


SECTIONS = [
    Section("Diplomacy", [
        "Trump, Xi and Putin meet at APEC in Shenzhen",
        "EU proposes a EUR 45 billion loan for Ukraine",
    ]),
    Section("Conflict", [
        "US and Iran exchange fire in the Gulf",
        "Crimean Bridge attacked again",
    ]),
    Section("Markets & Tech", [
        "Fed minutes lean toward another rate hike",
        "Anthropic heads for a $1.4 trillion market debut",
        "Van Gogh sells for a record $190.4 million",
    ]),
    Section("World", [
        "Cyclone Akvan nears the Andhra and Odisha coasts",
        "Ebola cases in DR Congo pass 11,000",
        "Democrats nominate Hakeem Jeffries for Speaker",
    ]),
    Section("Culture & Space", [
        "GTA VI launches globally after 13 years",
        "Voyager 1 reaches one light-day from Earth",
    ]),
]


def inspect_entry(path: Path) -> tuple[int, str]:
    if not path.is_file():
        sys.exit(f"briefing halted: {path} is missing")
    data = path.read_bytes()
    if not data:
        sys.exit("briefing halted: entry.png is empty")
    if len(data) > CAP:
        sys.exit(f"briefing halted: entry.png is {len(data)} bytes, over {CAP}")
    if not data.startswith(MAGIC):
        sys.exit("briefing halted: entry.png lacks the PNG signature")
    return len(data), hashlib.sha256(data).hexdigest()[:12]


def main() -> None:
    size, digest = inspect_entry(ENTRY)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ENTRY, OUTPUT)

    print("GLOBAL BRIEFING -- Thursday, 19 November 2026")
    print(f"entry.png: {size} bytes, sha256 {digest}..., copied to {OUTPUT}")
    for section in SECTIONS:
        print(f"\n{section.title.upper()}")
        for item in section.items:
            print(f" - {item}")
    print("\nEnd of briefing.")


if __name__ == "__main__":
    main()
