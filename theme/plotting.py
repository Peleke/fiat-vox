"""Matplotlib / seaborn house style for Equivalences, matched to theme/equivalences.scss.

Usage, first cell of a notebook (run from the repo root, or put theme/ on sys.path):

    from theme.plotting import use, PALETTE, CYCLE
    use()                      # light theme, default context
    use(context="talk")        # bigger text for slides / talks
    use(overrides={"figure.dpi": 200})

Every colour and font lives in the TOKENS / FONTS dicts below, so restyling the whole book
is an edit here plus re-running the notebooks. Nothing else should hard-code colours:
use PALETTE["accent"], CYCLE, or the registered colormaps instead.

Fonts: matplotlib needs the font files installed or registered. Drop static .ttf/.otf files
into theme/fonts/ (Cormorant Garamond, Inter, JetBrains Mono from Google Fonts; static
weights, not the variable font) and use() registers them. Missing fonts fall back to the
next name in each list.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap

# Palette tokens, same hex values as theme/equivalences.scss (from grymoire).
TOKENS = {
    "falun-100": "#fce8e5", "falun-200": "#f9d2cc", "falun-300": "#f3b0a6",
    "falun-500": "#d4564a", "falun-700": "#9a2520", "falun-900": "#6e2019",
    "ink-500": "#807d74", "ink-600": "#6b685e", "ink-800": "#4a4843", "ink-950": "#0f0f0e",
    "parchment-50": "#fdfcfa", "parchment-100": "#f8f5ef",
    "parchment-200": "#f0e9dd", "parchment-300": "#e5d9c5",
}

# Semantic roles. Change these, not the call sites.
PALETTE = {
    "background": TOKENS["parchment-50"],
    "panel": TOKENS["parchment-50"],
    "text": TOKENS["ink-800"],
    "heading": TOKENS["ink-950"],
    "muted": TOKENS["ink-500"],
    "grid": TOKENS["parchment-300"],
    "accent": TOKENS["falun-700"],
    "accent-light": TOKENS["falun-300"],
}

# Categorical cycle: accent first, then dark neutrals and muted earth tones that separate
# from Falun red on parchment. Order matters: first series = most important.
CYCLE = ["#9a2520", "#4a4843", "#b69a71", "#d4564a", "#807d74", "#6e2019", "#c4ad88"]

FONTS = {
    "serif": ["Cormorant Garamond", "Georgia", "DejaVu Serif"],    # titles
    "sans": ["Inter", "Avenir Next", "Helvetica Neue", "DejaVu Sans"],  # labels, ticks
    "mono": ["JetBrains Mono", "JetBrainsMono Nerd Font Mono", "DejaVu Sans Mono"],
}

FONT_DIR = Path(__file__).resolve().parent / "fonts"


def register_fonts(font_dir=FONT_DIR):
    """Register any .ttf/.otf files in font_dir with matplotlib. Returns the family names."""
    names = set()
    if font_dir.is_dir():
        for f in sorted(font_dir.glob("*.[ot]tf")):
            font_manager.fontManager.addfont(str(f))
            names.add(font_manager.FontProperties(fname=str(f)).get_name())
    return sorted(names)


def colormaps():
    """Sequential (parchment → Falun → ink) for spectrograms; diverging around parchment."""
    seq = LinearSegmentedColormap.from_list(
        "eq_seq", [TOKENS["parchment-50"], TOKENS["falun-300"], TOKENS["falun-700"], TOKENS["ink-950"]])
    div = LinearSegmentedColormap.from_list(
        "eq_div", [TOKENS["ink-800"], TOKENS["parchment-100"], TOKENS["falun-700"]])
    for cmap in (seq, div):
        if cmap.name not in mpl.colormaps:
            mpl.colormaps.register(cmap)
    return seq, div


def rc(context="notebook"):
    """The rcParams dict, without applying it (useful for plt.rc_context)."""
    scale = {"paper": 0.9, "notebook": 1.0, "talk": 1.3, "poster": 1.7}[context]
    p = PALETTE
    return {
        "figure.facecolor": p["background"], "axes.facecolor": p["panel"],
        "savefig.facecolor": p["background"], "savefig.transparent": False,
        "figure.dpi": 150, "savefig.dpi": 200, "savefig.bbox": "tight",
        "figure.figsize": (7.0, 4.0), "figure.constrained_layout.use": True,

        "font.family": "sans-serif",
        "font.sans-serif": FONTS["sans"], "font.serif": FONTS["serif"],
        "font.monospace": FONTS["mono"],
        "font.size": 10 * scale,
        "axes.titlesize": 15 * scale, "axes.titleweight": "semibold",
        "axes.titlelocation": "left", "axes.titlepad": 10,
        "axes.labelsize": 10 * scale, "xtick.labelsize": 9 * scale, "ytick.labelsize": 9 * scale,
        "legend.fontsize": 9 * scale,

        "text.color": p["text"], "axes.labelcolor": p["text"], "axes.titlecolor": p["heading"],
        "xtick.color": p["muted"], "ytick.color": p["muted"],
        "axes.edgecolor": p["grid"], "axes.linewidth": 0.8,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.color": p["grid"], "grid.linewidth": 0.6, "grid.alpha": 0.8,
        "axes.axisbelow": True,
        "axes.prop_cycle": mpl.cycler(color=CYCLE),

        "lines.linewidth": 1.6, "lines.markersize": 5,
        "patch.edgecolor": p["background"],
        "legend.frameon": False,
        "image.cmap": "eq_seq",
    }


def use(context="notebook", overrides=None):
    """Apply the house style globally (matplotlib and, if installed, seaborn)."""
    register_fonts()
    colormaps()
    params = rc(context)
    if overrides:
        params.update(overrides)
    try:
        import seaborn as sns
        sns.set_theme(context=context, style="whitegrid", palette=CYCLE, rc=params)
    except ImportError:
        pass
    mpl.rcParams.update(params)
    return params


def title(ax, text, **kw):
    """Serif chart title in the book's heading face (axes text stays sans)."""
    return ax.set_title(text, fontfamily=FONTS["serif"], fontsize=mpl.rcParams["axes.titlesize"] * 1.2, **kw)


def swatch():
    """Quick visual check of the palette, cycle, and colormaps."""
    use()
    fig, axes = plt.subplots(3, 1, figsize=(7, 4))
    for i, c in enumerate(CYCLE):
        axes[0].bar(i, 1, color=c)
    axes[0].set_axis_off()
    import numpy as np
    grad = np.linspace(0, 1, 256)[None, :]
    axes[1].imshow(grad, aspect="auto", cmap="eq_seq"); axes[1].set_axis_off()
    axes[2].imshow(grad, aspect="auto", cmap="eq_div"); axes[2].set_axis_off()
    title(axes[0], "Equivalences palette")
    return fig
