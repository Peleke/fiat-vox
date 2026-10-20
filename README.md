# Equivalences

Quarto book. Chapters are Jupyter notebooks at the repo root and render from their stored outputs; nothing executes at build time.

## Build

```sh
quarto preview   # live local preview
quarto render    # writes _book/
```

CI (`.github/workflows/publish.yml`) renders and deploys to GitHub Pages on every push to `main`, nightly at 07:00 UTC, and on manual dispatch.

## Splitting the source notebook

`source/signals.ipynb` is split into chapter notebooks by `scripts/split.py`, driven by `toc.json`. Each chapter entry names its output file, title, and the exact markdown heading cell where it starts.

```sh
python3 scripts/split.py
```

Re-running overwrites the chapter notebooks. Once chapters are edited directly, stop re-splitting.

## Data

Chapters read the Hillenbrand et al. (1995) vowel data from `data/hillenbrand/`. It is not committed; locally `data` is a symlink to `../ling/data`.
