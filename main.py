#!/usr/bin/env python3
"""Make the Judge Smile — entry program.

Writes one original line (a single sentence, at most 200 characters)
about a small good thing that happened today, to /output/entry.txt.
"""

import os
from pathlib import Path

ENTRY = (
    "This morning the ojek driver who dropped me off refused my tip, "
    "then pressed a warm pisang goreng into my hand and said the rain "
    "had already paid him."
)


def main() -> None:
    # Gate check, same bar as the sealed scorer: UTF-8 text, 1 to 200
    # characters, not only white space, and a single line.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
