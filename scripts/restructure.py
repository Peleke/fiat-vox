#!/usr/bin/env python3
"""Build the .ipynb chapters carried over from the frozen archive notebook.

One-off restructure (2026-10-21): source/signals-archive.ipynb is the frozen
monolith; the chapters below take its cells by index, unchanged except for:
  - a raw front-matter cell (title) at the top of each chapter;
  - the old section heading cell dropped where the chapter title replaces it;
  - heading levels shifted so each chapter's shallowest heading becomes '##'.
New chapters (Space & Time, Waves, Ensembles, What's in a Wave, What Odin Knew)
are hand-written .qmd files and are not produced here.

Re-running overwrites the chapter notebooks. Once you edit them directly, stop
re-running this script.

Usage: python3 scripts/restructure.py
"""
import copy
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "source" / "signals-archive.ipynb"

# (file, title, [cell index ranges, inclusive], cells to drop)
# Leading ranges of note cells (10, 454-455, 13) are the author's planning notes for the chapter.
CHAPTERS = [
    ("04-sampling-dft.ipynb", "Interlude: Sampling & the DFT",
     [(10, 10), (454, 455), (125, 323)], {125}),
    ("05-stft-spectrograms.ipynb", "The STFT & Spectrograms",
     [(324, 427)], {324}),
    ("06-isoclines.ipynb", "Isoclines: Hillenbrand Vowel Classification",
     [(13, 13), (31, 124), (428, 445), (450, 451)], set()),
]

# Anchors: the archive cell each range boundary is expected to start with.
# Guards against the archive changing underneath the indices.
ANCHORS = {
    31: "## Vowels, Formants",
    125: "### Interlude: Spectral Analysis & the DFT",
    324: "### The STFT and Spectrograms",
    428: "#### Formant Normalization",
    443: "### Model Training",
    446: "### Shift Invariance of Convolution",
}

HEADING = re.compile(r"^(#{1,6})(\s)", re.M)


def src(cell):
    return "".join(cell["source"])


def check_anchors(cells):
    for i, prefix in ANCHORS.items():
        if not src(cells[i]).lstrip().startswith(prefix):
            sys.exit(f"anchor mismatch at cell {i}: expected {prefix!r}, "
                     f"found {src(cells[i])[:60]!r}")


def prose_lines(text):
    """Yield (is_prose, line) pairs; lines inside ``` fences are not prose."""
    fenced = False
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            yield False, line
        else:
            yield not fenced, line


def shallowest(cells):
    levels = [len(m.group(1)) for c in cells if c["cell_type"] == "markdown"
              for prose, line in prose_lines(src(c)) if prose
              for m in [HEADING.match(line)] if m]
    return min(levels) if levels else 2


def shift_headings(cell, delta):
    if cell["cell_type"] != "markdown" or delta == 0:
        return cell
    shift = lambda m: "#" * max(2, len(m.group(1)) + delta) + m.group(2)
    lines = [HEADING.sub(shift, line) if prose else line
             for prose, line in prose_lines(src(cell))]
    cell = copy.deepcopy(cell)
    cell["source"] = lines
    return cell


def front_matter(title):
    return {"cell_type": "raw", "metadata": {},
            "source": ["---\n", f'title: "{title}"\n', "---\n"]}


def main():
    nb = json.loads(ARCHIVE.read_text())
    cells = nb["cells"]
    check_anchors(cells)
    for fname, title, ranges, drop in CHAPTERS:
        picked = [cells[i] for lo, hi in ranges for i in range(lo, hi + 1) if i not in drop]
        delta = 2 - shallowest(picked)
        body = [shift_headings(c, delta) for c in picked]
        out = {**nb, "cells": [front_matter(title)] + body}
        (ROOT / fname).write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
        idx = ", ".join(f"{lo}-{hi}" for lo, hi in ranges)
        print(f"{fname}: cells {idx} (dropped {sorted(drop) or 'none'}), "
              f"{len(body)} cells, headings shifted {delta:+d}")


if __name__ == "__main__":
    main()
