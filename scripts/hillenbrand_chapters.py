#!/usr/bin/env python3
"""Split the working Hillenbrand notebook into three book chapters.

generated (Claude), 2026-11-09. Source of truth stays ../ling/hillenbrand.ipynb;
re-run this after editing it. Cells are copied with their stored outputs (Quarto
renders .ipynb chapters from stored outputs; it does not execute them).

Same conventions as restructure.py:
  - raw front-matter cell with the chapter title;
  - the section heading the title replaces is dropped;
  - headings shifted so each chapter's shallowest heading is '##'.
Each chapter also gets a copy of the notebook's reference list, since the
numbered citations in every part point into it.

Boundaries are found by heading text, not index, so inserting cells upstream
doesn't break the split; a missing or duplicated anchor stops the script.

Usage: python3 scripts/hillenbrand_chapters.py
"""
import json
import sys
from pathlib import Path

from restructure import front_matter, shallowest, shift_headings, src

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT.parent / "ling" / "hillenbrand.ipynb"

# (output file, working title, first-cell heading, heading of the next part or None)
CHAPTERS = [
    ("06-hillenbrand-1.ipynb", "Hillenbrand I: Formants & Normalization",
     "# Hillenbrand Classifier", "## Classical ML: Logistic Regression"),
    ("06-hillenbrand-2-logreg.ipynb", "Hillenbrand II: Logistic Regression",
     "## Classical ML: Logistic Regression", "## PyTorch: Fully Connected Layers"),
    ("06-hillenbrand-3-torch.ipynb", "Hillenbrand III: PyTorch, CNNs & ResNet34",
     "## PyTorch: Fully Connected Layers", "## References"),
]
REFERENCES = "## References"


def locate(cells, prefix):
    hits = [i for i, c in enumerate(cells)
            if c["cell_type"] == "markdown" and src(c).lstrip().startswith(prefix)]
    if len(hits) != 1:
        sys.exit(f"anchor {prefix!r}: {len(hits)} matches, expected 1")
    return hits[0]


def clean_reference_cell(cell):
    """Publication cleanup of the copied reference list (source notebook untouched):
    drop 'CITATION NEEDED:' prefixes and the trailing 'Unused (?)' scratch list,
    and restore Hillenbrand's first initial."""
    if cell["cell_type"] != "markdown":
        return cell
    text = src(cell).split("\nUnused (?)")[0].rstrip() + "\n"
    text = text.replace("CITATION NEEDED: ", "")
    text = text.replace("1. Hillenbrand, L. A. Getty", "1. J. Hillenbrand, L. A. Getty")
    return {**cell, "source": text}


def drop_local_paths(cell):
    """Remove stderr stream outputs (library warnings) that print local filesystem paths."""
    if cell["cell_type"] != "code":
        return cell
    outs = [o for o in cell.get("outputs", [])
            if not (o.get("output_type") == "stream" and o.get("name") == "stderr")]
    return {**cell, "outputs": outs}


def main():
    nb = json.loads(SOURCE.read_text())
    cells = nb["cells"]
    ref_start = locate(cells, REFERENCES)
    references = cells[ref_start:]
    for fname, title, start, stop in CHAPTERS:
        lo = locate(cells, start)
        hi = locate(cells, stop) if stop else len(cells)
        picked = cells[lo + 1:hi]  # drop the heading the title replaces
        delta = 2 - shallowest(picked)
        body = [drop_local_paths(shift_headings(c, delta)) for c in picked]
        refs = [clean_reference_cell(shift_headings(c, 2 - shallowest(references))) for c in references]
        out = {**nb, "cells": [front_matter(title)] + body + refs}
        (ROOT / fname).write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
        print(f"{fname}: source cells {lo + 1}-{hi - 1}, {len(body)} cells + "
              f"{len(refs)} reference cells, headings shifted {delta:+d}")


if __name__ == "__main__":
    main()
