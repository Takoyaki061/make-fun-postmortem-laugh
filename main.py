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
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
