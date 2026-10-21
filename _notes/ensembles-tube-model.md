# Ensembles — tube-model working outline (LOCAL, not rendered)

Free-form working notes for the Ensembles chapter, to be replaced wholesale by the author's own
content. Drafted by Claude (Opus 5.5), 2026-10-21, at the author's request ("consider that outline free
for you to contribute to however you'd like … those outline notes stay local/out of quarto").
Contribution: arc steps 1–7 are the author's; the physics, numbers, demos, and ties are Claude's
(~75% of this file). Numbers below marked [G] are from a fetched *summary* of Guldimann's posts,
not re-derived; verify before use.

## Scope

- **In:** swept bandpass → "sounds like a vowel" → why. Source (buzz) + tube (filter). Wave equation in a
  tube, standing waves, quarter-wave resonances, constrictions, nomogram, one/two-tube estimates,
  digital waveguide / Kelly–Lochbaum.
- **Out (reference only):** losses and bandwidths, lip radiation, all-pole/LPC, Levinson–Durbin, cepstrum,
  inverse filtering — Guldimann Part 1 §8–9 and Part 2. Ties to keep (below) because they land elsewhere
  in the book.

## The author's arc, with technical content per step

1. **Formants raise the question: how?**
   - Entry demo already exists: a sawtooth through a swept `.bpf()` sounds vowel-like (`hljod:edm-2`).
     One band ≈ one formant; two bands moving independently ≈ a vowel space.
   - Setup from earlier chapters: the source is a harmonic comb (Waves: many turning points at whole-
     number multiples of a base rate); the filter shapes the comb's envelope.
2. **Here's a throat.**
   - Diagram: lungs → larynx/vocal folds (source) → pharynx → oral cavity (+ nasal branch) → lips.
   - The vocal folds as a click train with a shape: glottal pulses at f₀ (~100–250 Hz), harmonic comb,
     envelope falling ~12 dB/octave [G]. Direct callback to Space & Time's click train.
   - Pink Trombone (Neil Thapen) as the playable model; check its license before embedding — linking is
     safe.
3. **Look, it's a tube** (spherical-horse moment).
   - Plane waves only: valid while wavelength ≫ tract width (~2 cm), i.e. below roughly 4 kHz [G].
4. **Physics.**
   - 1-D wave equation from mass + momentum conservation for a thin slice of air; d'Alembert solution =
     forward + backward travelling waves (two delay lines — callback to Strudel's delay).
   - Boundary conditions: closed at the glottis (velocity node), open at the lips (pressure node) →
     quarter-wave resonator: Fₙ = (2n − 1)·c / 4L.
   - Numbers: c ≈ 350 m/s, L ≈ 17.5 cm → F1, F2, F3 ≈ 500, 1500, 2500 Hz (schwa). L = 12–13 cm (child)
     → all formants scale up by L_adult/L_child.
   - **Uniform scaling with 1/L is the assumption behind formant normalization** (Isoclines chapter) — the
     strongest forward tie in this chapter.
   - Non-uniform tubes: a narrow neck into a wide cavity behaves like a Helmholtz resonator,
     f = (c/2π)·√(A_neck / (V·L_neck)) — a low resonance not predicted by the uniform tube. This is the
     low-area-ratio limit of the two-tube model.
   - Perturbation rule (where constrictions go matters): narrowing the tube where formant *n* has a
     velocity maximum lowers Fₙ; narrowing where it has a pressure maximum raises it. This is why
     constriction *location* is the control variable. (Chiba–Kajiyama / Schroeder; cite before stating.)
5. **Nomogram.**
   - Fant's method: fix a short constriction (~3 cm), slide it from glottis to lips, plot F1–F3; degree
     of constriction stretches the curves [G]. Pharyngeal → high F1/low F2 (open/back vowels); palatal →
     low F1/high F2 (/i/).
   - Interactive version (OJS): sliders for constriction place and degree, live F1–F3 readout plus a
     position in the F1–F2 plane over the Hillenbrand vowel clouds (data already in the book).
6. **One- and two-tube simplifications.**
   - Two tubes (back l₁, A₁; front l₂, A₂): resonances where tan(k l₁)·tan(k l₂) = A₂/A₁, k = 2πf/c [G].
     Limits: large ratio → cavities decouple (each a quarter-wave tube); small ratio → half-wave
     behaviour [G].
   - Worked /ɑ/: l₁ = l₂ ≈ 8.7 cm, A₁ = 1 cm², A₂ = 7 cm² → ~770, ~1230 Hz vs measured ~720, ~1090 [G].
     Reversing the areas heads toward /i/ (F1 ↓, F2 ↑) [G].
   - Solve numerically in a code cell (root-finding on the tan equation); compare to Hillenbrand means.
7. **Digital waveguide and Kelly–Lochbaum.**
   - Chain of N short cylinders; at each junction, continuity of pressure and volume velocity gives
     reflection coefficient rₖ = (Aₖ − Aₖ₊₁)/(Aₖ + Aₖ₊₁); closed end → +1, open end → −1 [G].
   - Section length tied to sample rate: one sample of travel each way, Δx = c / (2·fs) ≈ 0.4 cm at
     44.1 kHz; ~44 sections ≈ 17.5 cm [G].
   - Implementation as two delay lines + scattering junctions — the same shift operator as Strudel's
     `.delay()`, and a preview of What's in a Wave's shift matrix.
   - Demo targets: numpy KL simulation rendering vowel audio; later RNBO/`gen~` version (M4L plan).

## Ties into the rest of the book (keep even though the material is out of scope)

- **All-pole = spirals.** A lossless tube is an all-pole filter; poles are the Waves chapter's spirals
  (distance < 1 decays). One sentence here, full treatment never.
- **Cepstrum = logs turn products into sums.** Source × filter becomes source + filter after a log — the
  Waves chapter's success test, reused. Reference only.
- **Mel / log-frequency** — STFT & Spectrograms.
- **VTLN** (vocal-tract length normalization) = warping frequency by one scale factor α; the speaker
  scaling group from the symmetry notes; what Isoclines' normalization assumes.
- **Child vs adult tract length** (Peterson & Barney ratios ~1.34–1.38 [G]) — Hillenbrand has children's
  data; a direct check the book can run.

## Open decisions for the author

- Does the archive's **Bandpass Synthesis** section (now in `04-sampling-dft.ipynb`) move here? It is a
  source–filter demo by content.
- How far into Helmholtz: one formula and a picture, or a derivation?
- KL in numpy only, or numpy + Web Audio/OJS?

## Guldimann reference notes (for coverage/visual ideas only; no text taken)

- Part 1 "How a tube becomes a vowel": §1 source (pitch, open-quotient sliders) · §2 factorisation
  (linearity, ~25 ms stationarity, source–filter independence as weakest assumption) · §3 sound in a pipe
  (plane waves, impedance ρc/A) · §4 one tube (length slider, standing waves + transfer function) ·
  §5 two tubes (junction + area sliders) · §6 nomogram (static) · §7 N-tube lattice (44 draggable
  sections, vowel presets, F1–F2 vs Peterson & Barney) · §8 losses + radiation (out) · §9 all-pole/LPC
  (out) · §10 limits: nasals/laterals add zeros, fricatives are turbulence, source–tract interaction,
  >4 kHz breakdown.
- Part 2 "Running the tube backwards" (out of scope; personal reference): framing/window trade-off,
  cepstrum + liftering, mel filterbank, DCT/MFCC history, HMM/Viterbi alignment, CTC, modern encoders,
  VTLN with an α slider (min misfit α ≈ 1.33).
- Visual ideas worth matching or beating: standing-wave plot under a length slider; area-function editor
  with live transfer function; vowel-space dot over reference clouds.
- Cited sources worth reading directly: Fant (1960) *Acoustic Theory of Speech Production*; Kelly &
  Lochbaum (1962); Peterson & Barney (1952); Stevens *Acoustic Phonetics*; Rabiner & Schafer.
