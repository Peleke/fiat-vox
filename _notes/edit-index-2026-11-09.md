# Edit index — 2026-11-09

Edits made by the DA (Claude) at the principal's direction. Cell ids are stable; indices shift.
"Generated" = AI-generated code or figure, disclosed here and in a code comment in the cell.

## Ch. 3 — `04-sampling-dft.ipynb` (Interlude: Sampling & the DFT)

Edited live through the Jupyter server (:8899), kernel `ling-env`. Backup of the pre-edit
file: session scratchpad `04-backup-pre-edit.ipynb`.

### Structure
- Moved former cells 1–3 (planning notes) verbatim to `_notes/ch3-sampling-dft-moved-notes.md`; deleted from chapter.
- Added hidden setup cell at the top (`#| include: false`): numpy, matplotlib, IPython.display, theme `use()`. Generated.
- Deleted: "To make sounds with the formant frequencies…" cell; "TODO: Make this the tube model…" cell;
  "This is sort of a big deal…" cell; "A couple of technical observations / TODO" cell; "Here is his solution:" cell;
  the master-method section (recurrence `T(n) = aT(n/b) + f(n)` + "TODO: Complete…"); the commented-out
  matplotlib Slider cell (replaced by the Plotly cell below).

### Text edits (as specified)
- Footnote on tube-in-mouth cut (and its `<sup>1</sup>` marker).
- "…Let's take a step back." cut. "Because it is: We'll…Come back to that." → "It is: we'll come back to it."
- "Like we discussed," cut. F4 clause → "but it's often omitted, so we won't include it when training our models."
- "The trick is this…" paragraph cut.
- "Now, we _do_ have to make some decisions." → "We make the following decisions:"
- "I'd be doing you dirty…" → "Why 44,100 Hz?"; "Let's step back." cut.
- "Here's how that works (…briefly):" → "Briefly:"; "Again—there's no magic." cut; preceding italics removed.
- "Observe:" removed. "This is exactly the same concept." → "This is analogous."
  "It turns out there's something deeper than this, though." → "It's even deeper than this:"
- "On the right, _we don't have enough_." italics removed.
- TODO cell (folding / Nyquist / 44,100) replaced: Nyquist–Shannon statement + link to JOS
  *Mathematics of the DFT* "Sampling Theorem" (statement checked against that page: X(jω)=0 for |ω| ≥ π/T).
  Aliasing note left for the principal.
- "…Odd." cut. "do have _something_ to do with" → "are clearly related to". "What?" cut.
- "I lied about infinity, earlier." → "Small correction."; "Or rather," cut.
- "Your larynx plucks the string. Your mouth shapes and amplifies the sound." → "Your larynx generates a pulse
  train. Your mouth filters resonant frequencies, amplifying some frequencies and suppressing others."
  "…to hear _you_." → "…for it to sound like you."
- "we're out of luck as far as adding more formant frequencies: We've only" → "we've only"; "Let's back up." cut;
  "infinitely more" un-italicized. "- ...But, it's clear" → "- It's clear".
- "(discussed in deep dive on complex exponentials…)" cut.
- "…, in other words." and "In other words:" (tuning-fork cell) cut. "This is the key insight." cut.
  "That's a bit abstract…" cut. "This turns out to help make things clearer." cut. "Remember:" cut. "however" cut.
- "It's actually _not_ relevant…" → "If our case were continuous, a straightforward evaluation of the integrals
  over a period would prove this is the case."
- Proof TODO → geometric-series sentence + invitation to JOS "Orthogonality of the DFT Sinusoids".
- "directly" removed; "alas…You" → "you".
- "but now that we're here…We'll need" → "but we'll need".
- "…we'll implement it next." → "…next time. To do so, we'll need the Fast Fourier Transform, first."
- "…BUt first: …CNN." paragraph cut. "is…Impractical, at best." → "is impractical."
  "; that would actually be practical" cut. "the [Cooley-Tukey algorithm]" → "called the [Cooley-Tukey algorithm]".
- Emphasis italics removed in running sentences across the chapter (62 instances in 33 cells).
  Kept: _voilà_ (foreign word), wave _length_ (wordplay on wavelength), _alternating current_ (term defined
  as **AC**), and two italicized questions quoted as questions.

### Normalization factor (approved)
- 1/N added throughout: M⁻¹ = (1/N)Mᴴ; M has orthogonal columns of length √N; (1/√N)M is unitary.
  Cells rewritten: "Look again…", "that last expression is curious…", the orthogonal/unitary definition,
  "Again: MᴴM = NI…", "Because we know the columns of M are orthogonal…".
- `SimpleAnalyzer` already divided by N (principal's edit); B♭6 plot now plots `np.abs(amps)` and was re-run.

### LaTeX / math fixes
- Filled the four `TODO: LaTeX` slots: single correlation A_k = (1/N)⟨S, e_k⟩; matrix form (1/N)MᴴS = a;
  reconstruction S[n] = Σ A_k e^{2πikn/N}; matrix form S = Ma.
- Row breaks: single `\` → `\\` in six display-math cells (cause of "matrices inline" in 3.2/3.3).
- Typo: second line of the unit-vector check used ‖î‖ for ĵ; fixed.

### Generated cells (code + outputs)
- Sampling 2-up (5 Hz at 100 vs 6 samples/s, alias curve at 1 Hz).
- Listening demo: 6 kHz tone at 44,100 vs 8,000 samples/s (aliases to 2 kHz).
- Plotly aliasing slider (4–30 samples/s; sinc reconstruction; title reports the folded frequency).
  Output is plain HTML (`include_mathjax=False`): `fig.show()` with `notebook_connected` injected MathJax 3.2.2,
  which blocked the book's MathJax 4 on the whole page. Fixed and browser-verified.
- Orthogonality 2-up: cos3t·cos5t (area 0) vs cos²3t (area π).
- SymPy + NumPy check: continuous integrals; MᴴM = NI for N = 64.
- DFT of 0.1 s of a bandpass-noise vowel (F1–F3 of `df.iloc[0]`), via `SimpleAnalyzer`.
- Radix-2 FFT (explicit halves, no `np.tile`) + check on a Hillenbrand WAV: matches `np.fft.fft`
  (max abs diff 1.4e-5, float32 input); timing vs `SimpleAnalyzer` on 4096 samples.

### Kernel state note
The chapter has no data-loading cells (they live in `source/signals-archive.ipynb`), so re-running cells
required bootstrapping the kernel from archive cells 39–117 (imports, `df`, `df_timedata`). Only the cells
listed above were re-executed; all others keep their stored outputs.

### Flagged, not changed
- The B♭6 DFT peaks read ~0.52/0.17/0.10/0.03 against amplitudes 0.6/0.25/0.10/0.05: leakage, because the
  chord frequencies fall between 10 Hz bins. The text after it says "A perfect analysis".
- The chapter's `vowel_filter` zips 5 formants (f0–f4) with 3 bandwidths, so it filters f0, f1, f2 — f0 is the
  fundamental, not a formant, and F3 is dropped. The new vowel-DFT demo uses F1–F3.
- "The larynx produces a sound that, on its own, sounds like a hiss" conflicts with the new "pulse train" line.
- Remaining TODOs not in scope: "TODO: Replace with glottal pulse train later"; the "**Note**: Need to
  introduce basics of sound…" cell.

## Hillenbrand II — `06-hillenbrand-2-logreg.ipynb`
- `### Bootstrapping` heading: NOT DONE. The chapter is generated from `../ling/hillenbrand.ipynb`; attaching
  to that notebook through the Jupyter MCP returned an empty document (0 cells) while the file on disk has 300.
  Detached without writing. File on disk unchanged (mtime 04:05).

## Ch. 4 — `05-stft-spectrograms.ipynb` (The STFT & Spectrograms)

Edited live through the Jupyter server (:8899), same `ling-env` kernel. Backup: session scratchpad
`05-backup-pre-edit.ipynb`. All code cells re-executed top to bottom after the edits.

### Text edits (as specified)
- Deleted: top TODO list (Windows / Gabor / Mel…), "I'm waving my hands…" list (Max 4 Live etc.),
  "That's…Less encouraging…", "TODO: Expound analysis…", "…So we have a choice to make: Wideband/Narrowband…",
  the "# TODO: show" cell, "Refer to Downey and his code."
- "So…The impulse signal, the humble value 1, contains every frequency. …Yeah. That's not a mistake."
  → "The impulse signal contains every frequency."
- "Now we can see the problem." → "The problem:"; leakage sentence reordered as specified.
- "The takeaway for now: …diluting…" → stated directly as spectral leakage.
- "This implies not using a naive rectangle…" cut. Window Functions opens with "One solution is to force
  values at the window's boundary to zero. We have options."
- Italics removed: tapers, decay differently, rise, half; the italics in the impulse paragraph.
- Δf formula: was f_s/N = 1000/2048 ≈ 1.95 (arithmetic wrong: 1000/2048 = 0.49). Now f_s/M = 1000/512 ≈ 1.95,
  with a sentence that zero-padding doesn't change bin width.

### Added
- Hidden setup cell (imports, theme). Generated.
- After "To show the DFT is periodic…": Downey, *Think DSP* §7.8, quoted with link (text checked against the
  live page), plus one sentence: the same argument on n shows the inverse DFT repeats every N samples.
- After the formant printout: quote from Hillenbrand I (narrowband L > 2T₀ / wideband L < T₀), linked, with a
  note that the chapter uses it extensively.

### Generated cells (code + outputs)
- Test sound: ten 0.1 s clips at 4 kHz, two tones each, none a multiple of 10 Hz; waveform plot.
- Chop into 10 × 400-sample frames; DFT; frame-1 spectrum with leakage skirts.
- Four frames side by side; frame 1 tiled to show the seam (last sample +0.247, first 0.000);
  100 + 300 Hz control that tiles seamlessly and has exactly two DFT spikes.
- Impulse and its DFT (all bins = 1, checked).
- Window head-to-head table (pandas Styler): null-to-null, −3/−6 dB widths, peak sidelobe, rolloff,
  ENBW, scalloping loss, coherent gain, Hz columns at fs = 1000, M = 512. Widths match the Harris 1978 values
  quoted in Hillenbrand I (rect 0.88/1.20, Hann 1.44/2.00, Hamming 1.30/1.81).
- `spectrogram()` (window, FFT per frame, frame-centre timestamps, dB) + `plot_spectrogram()`.
- Test-sound spectrogram (50 ms Hamming); vowel m01ae spectrogram (5 ms Hamming) with F1–F3 from the dataset.
- Mel spectrogram via librosa (64 bands, 5 ms Hamming window).

### Rolloff fix
`compute_rolloff_rate(spectrum, freqs, M, lo_bins=8, hi_bins=M//16)`: fits sidelobe peaks in dB against
log2(bin) over bins 8–32 only. Results: boxcar −5.99, Hamming −5.69, Hann −18.09, triangular −12.05 dB/octave
(theory −6, −6, −18, −12). The old version fit every peak out to Nyquist, where the finite-window response
stops decaying as 1/fᵖ, and converted log10 slope with a stray factor; that produced −5.37 for the boxcar.
Call sites now pass M.

### Restyle
Hard-coded colors → theme `CYCLE`/`PALETTE`; `plt.tight_layout()` removed (theme uses constrained layout);
`plt.suptitle(..., y=0.98)` → `fig.suptitle(...)` (it overlapped the two-line subplot titles).

### Flagged, not changed (prose)
- "computed at -5.37 dB" in the boxcar summary and the "we're off due to discrete sampling" paragraph are now
  stale: computed value is −5.99.
- Hamming "chalk this up to estimation error": measured −5.69 over bins 8–32; Hamming's near sidelobes don't
  follow the −6 dB/oct asymptote until further out.
- "Anything quieter than -17.9 dB…" conflicts with the −13.46 dB first sidelobe just computed.
- "boxcar has very high 2-bin mainlobe width" — 2 bins is the narrowest of the four.
- Cell "DFT(x + N) = DFT(x)" — the index belongs inside: DFT(y)[k+N] = DFT(y)[k].
- "This wasn't the case with the test sound we used before": the control I added is a new 100+300 Hz sound,
  not one from Ch. 3.
- Frequency-response 4-up uses n_fft = 2048 (4× padding), so the curves are visibly piecewise-linear.
