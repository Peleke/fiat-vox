"""Split the source notebook into Quarto chapter notebooks per toc.json.

Each chapter starts at the markdown cell whose stripped source equals its
`start` string and runs up to the next chapter's start. The anchor cell is
replaced by a raw front-matter cell carrying the chapter title. Cells before
the first anchor are reported and not written (index.qmd holds the preface).
Cell contents and outputs are copied unchanged.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    toc = json.loads((ROOT / "toc.json").read_text())
    nb = json.loads((ROOT / toc["source"]).read_text())
    cells = nb["cells"]

    starts = []
    for ch in toc["chapters"]:
        hits = [i for i, c in enumerate(cells)
                if c["cell_type"] == "markdown" and "".join(c["source"]).strip() == ch["start"]]
        if len(hits) != 1:
            print(f"error: anchor {ch['start']!r} matched {len(hits)} cells", file=sys.stderr)
            return 1
        starts.append(hits[0])
    if starts != sorted(starts):
        print("error: toc.json chapters are out of notebook order", file=sys.stderr)
        return 1

    if starts[0] > 0:
        print(f"note: cells 0-{starts[0] - 1} precede the first chapter and are not written")

    bounds = starts + [len(cells)]
    for ch, lo, hi in zip(toc["chapters"], bounds, bounds[1:]):
        front = {"cell_type": "raw", "metadata": {},
                 "source": ["---\n", f"title: {json.dumps(ch['title'])}\n", "---"]}
        out = dict(nb, cells=[front] + cells[lo + 1:hi])
        (ROOT / ch["file"]).write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
        print(f"{ch['file']}: cells {lo}-{hi - 1}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
