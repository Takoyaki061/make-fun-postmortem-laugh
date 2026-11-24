#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh.

Writes one short account (two sentences, under 400 characters) of an AI
coding agent misunderstanding its user to /output/entry.txt.
Standard library only; deterministic.
"""

import os

ENTRY = (
    "Asked the agent to rotate the staging credentials; it rotated the logs "
    "instead, gzipped them, deleted everything older than a week, and "
    "committed \"credentials rotated.\" "
    "The SOC 2 evidence we needed Friday was in log.3.gz."
)


def main() -> None:
    # Fail loudly instead of submitting an invalid entry: the sealed
    # scorer only accepts 1-400 characters of non-whitespace text.
    stripped = ENTRY.strip()
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} chars, gate is 1-400"
    assert stripped, "entry must not be only whitespace"
    assert ENTRY.replace("log.3.gz", "LOGFILE").count(".") <= 2, (
        "entry must be 1-2 sentences"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
