# Equivalences

Quarto book. New chapters are `.qmd`; chapters carried over from the original notebook are `.ipynb`
and render from their stored outputs.

## Build

```sh
quarto preview   # live local preview
quarto render    # writes _book/
```

`.qmd` chapters execute locally and are frozen (`execute: freeze: auto`): run `quarto render` on your
machine and commit `_freeze/`, so CI never needs Python. `.ipynb` chapters are not executed.

CI (`.github/workflows/publish.yml`) renders and deploys to GitHub Pages on every push to `main`, nightly
at 07:00 UTC, and on manual dispatch.

## Layout

| Path | What |
|---|---|
| `01`–`08`, `references.qmd` | chapters (order in `_quarto.yml`) |
| `source/signals-archive.ipynb` | the original monolithic notebook, frozen 2026-10-21 |
| `scripts/restructure.py` | builds chapters 04–06 from the archive by cell index (one-off; re-running overwrites them) |
| `_archive-preview/` | single-page render of the archive: `cd _archive-preview && quarto preview signals.ipynb` |
| `_notes/` | local working notes, not rendered: `ERRATA.md`, `ensembles-tube-model.md`, `BOOK-TODO.md`, `dumps/` (formatted brain dumps included by chapters) |
| `live/_setup.qmd` | Strudel/Hydra include for live-coding blocks (Chrome only for Hydra) |
| `theme/equivalences.scss` | site theme (grymoire palette and fonts) |
| `theme/plotting.py` | matplotlib/seaborn house style matched to the site theme |

## Plot style

```python
from theme.plotting import use, title, PALETTE, CYCLE
use()                                  # or use(context="talk"), use(overrides={...})
fig, ax = plt.subplots()
ax.plot(t, x)                          # colours come from CYCLE automatically
title(ax, "Serif chart title")
```

Spectrograms pick up the `eq_seq` colormap by default (`image.cmap`); `eq_div` is the diverging map.
To restyle every figure, edit `TOKENS`/`PALETTE`/`CYCLE`/`FONTS` in `theme/plotting.py` and re-run the
notebooks. For the exact site fonts, put static Cormorant Garamond, Inter and JetBrains Mono `.ttf` files
in `theme/fonts/`; otherwise matplotlib falls back to Georgia / Avenir Next / JetBrains Mono Nerd Font.

## Data

Chapters read the Hillenbrand et al. (1995) vowel data from `data/hillenbrand/`. It is not committed;
locally `data` is a symlink to `../ling/data`.
