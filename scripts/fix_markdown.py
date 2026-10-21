#!/usr/bin/env python3
"""Normalize notebook markdown that Jupyter tolerates but Pandoc (Quarto) does not.

Whitespace-only fixes, outside code fences:
  - inline math: `$ N $` -> `$N$` (Pandoc requires no space inside single-dollar math);
  - a list that directly follows a paragraph line gets a blank line before it;
  - blank lines inside a $$ display block are removed (they end the block in Pandoc).

Idempotent. Prints per-file counts. Usage: python3 scripts/fix_markdown.py FILE.ipynb [...]
"""
import json
import re
import sys

INLINE = re.compile(r"(?<![\$\\])\$(?!\$)([^\$\n]+?)(?<![\\])\$(?!\$)")
LIST_ITEM = re.compile(r"^\s*([-*+]|\d+[.)])\s")


def fix_text(text):
    counts = {"math": 0, "list": 0, "display": 0}
    out, prev, fenced, display = [], "", False, False
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("```"):
            fenced = not fenced
        elif not fenced:
            if stripped == "$$" or (stripped.startswith("$$") and stripped.count("$$") == 1):
                display = not display
            elif display and not stripped:
                counts["display"] += 1
                continue
            if not display:
                def tighten(m):
                    inner = m.group(1).strip()
                    if inner != m.group(1):
                        counts["math"] += 1
                    return f"${inner}$"
                line = INLINE.sub(tighten, line)
                if (LIST_ITEM.match(line) and prev.strip() and not LIST_ITEM.match(prev)
                        and not prev.lstrip().startswith(("#", ">", "|"))
                        and not prev.startswith((" ", "\t"))):
                    out.append("")
                    counts["list"] += 1
        out.append(line)
        prev = line
    return "\n".join(out), counts


def main(paths):
    for path in paths:
        nb = json.load(open(path))
        total = {"math": 0, "list": 0, "display": 0}
        for cell in nb["cells"]:
            if cell["cell_type"] != "markdown":
                continue
            new, counts = fix_text("".join(cell["source"]))
            for k in total:
                total[k] += counts[k]
            cell["source"] = new.splitlines(keepends=True)
        with open(path, "w") as f:
            f.write(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")
        print(f"{path}: inline math {total['math']}, lists {total['list']}, display blanks {total['display']}")


if __name__ == "__main__":
    main(sys.argv[1:])
