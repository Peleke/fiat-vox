# Known errata — running list

Local only (the `_` prefix keeps Quarto from rendering it). Logged 2026-10-21 from the
restructure pass and two sweeps of hljod. The principal's own errata list (other machine) merges
here. Status: `open` until the rigor sweep. Each entry: where · what it says · correction.

Caveat on sources: entries marked *(sweep)* came from read-only agent sweeps of hljod and were
not independently re-checked; entries marked *(recall)* are from memory, not a source read this
session.

## Book: brain-dump cells (archive cells 6, 8, 15, 449)

| # | Where | Says | Correction | Status |
|---|---|---|---|---|
| E1 | Waves dump (archive 6) | Starts polar ("distance, angle"), then writes points as Cartesian `(1,0)→(0,1)`, then `(0,1) := (0,i)` | Mixed representations. Partly a deliberate fiction for a non-math reader (intuition → fuzzy → formal); the outline keeps the arc and adds a formal note. Clean form: a point is `x + iy` (Cartesian) or `r e^{iθ}` (polar); `i·(1,0) = (0,1)` is rotation by 90°. | open (by design, see outline) |
| E2 | Waves dump | "negative square roots do make sense" | "square roots of negative numbers" | open |
| E3 | Waves dump | Axioms listed: closure, inverses, identity, commutativity | Associativity is missing; it is what makes "turn 90°, three times" unambiguous. Zero is excluded from the multiplicative group (as the dump says). | open |
| E4 | Waves dump | "multiplication … means repeated addition … of angles" | For unit-modulus numbers, multiplying adds angles (and multiplies lengths in general). "Repeated addition" is the integer special case of multiplication, not its definition. | open |
| E5 | What's in a Wave dump (archive 15) | "its columns are the eigenvectors … and those eigenvectors are precisely the complex roots of unity" | The roots of unity are the shift's **eigenvalues**; the eigenvectors are the Fourier modes `(1, ω^k, ω^{2k}, …)`, vectors of powers of a root of unity. | open |
| E6 | What's in a Wave dump; archive 449 | "what kind of function is identical under shift, up to scale? … Sinusoids" | **Complex exponentials.** A real sine shifted is not a scalar multiple of itself (it is a combination of sin and cos). | open |
| E7 | What's in a Wave dump; archive 449 | "Shift invariance of CNNs drops out from the algebra" | Convolution is shift-**equivariant** (`C S = S C`). Invariance needs pooling/aggregation on top. | open |
| E8 | What's in a Wave dump | "A complex orthonormal (well, close enough) matrix" | The DFT matrix `F` has orthogonal columns of norm √N; `F/√N` is unitary. | open |
| E9 | What's in a Wave dump | "Can you parameterize Z_n, replacing it with any group whose action commutes with circulant matrices?" | Replace Z_n by a group G; the linear maps commuting with G's (regular) action are exactly the G-convolutions (Kondor–Trivedi 2018). The circulants are what commutes with Z_n, not the group. | open |
| E10 | What's in a Wave dump; archive 449 | "infinite mutually commuting matrices … recovers the Fourier transform and z-Transform" | Z gives the DTFT/Fourier series; R gives the Fourier transform. The z-transform extends the DTFT off the unit circle; it is not a separate group case. | open |
| E11 | Archive 449 | "Complex exponentials are the only functions that satisfy this constraint (proof?)" | True for eigenfunctions of all shifts simultaneously (characters of the group); state as such. Proof: `f(t+s) = λ(s) f(t)` ⇒ `λ` multiplicative ⇒ exponential (continuity). | open |
| E12 | Archive 449 | "Swap Z for the symmetry group" | "symmetric group" (S_n). Its smallest non-abelian case is S_3. | open |
| E13 | Archive 449 | "The roots of the polynomial defining C correspond to the roots of unity" | The **eigenvalues** of C are the polynomial `p(z) = Σ a_i z^i` **evaluated at** the roots of unity, not its roots. | open |
| E14 | Ensembles dump (archive 8) | "A4 sung and A4 struck on the violin" | Violin is bowed (or plucked), not struck. | open |
| E15 | Archive 451 | Formant values printed under "# in hz"; `f0_ss: 174` listed among formants | f0 is the fundamental, not a formant; label separately. | open |

## hljod material (fix before reuse)

| # | Where | Says | Correction | Status |
|---|---|---|---|---|
| H1 | EDM.2 reese *(sweep)* | Detune is "a quarter-tone flat" | Code is +0.15 semitone **sharp**; a quarter-tone is 0.5 semitone. | open |
| H2 | EDM.2 *(sweep)* | Text says `.lpf(120)` | Code uses `.lpf(200)`. | open |
| H3 | EDM.2 *(sweep)* | "Beating happens at every harmonic" | Harmonic k beats at k·Δf, so higher harmonics beat faster. | open |
| H4 | EDM.3 *(sweep)* | Ears can't tell direction of low frequencies | Interaural time difference is the main low-frequency cue; the real point is very low bass and mono-summing. | open |
| H5 | EDM.4c *(sweep)* | 808 kick "same math, not an approximation" as a decaying sine | The 808 kick has a pitch envelope at onset; decaying sine is an approximation. | open |
| H6 | EDM.4 atmosphere *(sweep)* | Listening table credits BotW Temple of Time to Kondo | Manaka Kataoka (body text is correct). | open |
| H7 | EDM.5 *(sweep)* | Lost Woods "Mixolydian" | F–A–B (raised 4th) suggests Lydian; not checked against the score. | open |
| H8 | EDM.5 *(sweep)* | `.every` with different periods "is" Reich phasing | Phasing is continuous tempo drift; `.every` is discrete periodic realignment. | open |
| H9 | EDM.1 / EDM.7 (read; sweep) | Amen break "6-second" vs "7-second"; GoFundMe described two ways; "never sued" vs "tried to claim royalties" | Internally inconsistent; verify against a source before any reuse. | open |
| H10 | EDM.1 / EDM.7 *(sweep)* | "NES 5 synthesis channels" | 4 tone/noise generators + 1 DPCM sample channel; the EDM.1 table lists DPCM correctly. | open |
| H11 | EDM.7 *(sweep)* | slice/splice explanation | Possibly reversed (splice changes speed to fit the slot); check Strudel docs. | open |
| H12 | EDM.8d *(sweep)* | Beethoven 5 as a "minor 3rd" | G–E♭ is a major 3rd. | open |
| H13 | EDM.9a, 9b *(sweep)* | ii–V–I is "three steps" on the circle of fifths | D→G→C is two steps. | open |
| H14 | EDM.9b *(sweep)* | "The dominant contains the tonic in its overtone series" | Reversed: the tonic's series contains the dominant (3rd harmonic). | open |
| H15 | EDM.9d *(sweep)* | Period consequent Fm→Cm called authentic; Autumn Leaves listed as AABA | Fm→Cm is plagal; Autumn Leaves is not AABA. | open |
| H16 | EDM.8e *(sweep)* | Several non-chord-tone labels (anticipation, appoggiatura, leap) | Mislabelled per sweep; re-check each example. | open |
| H17 | EDM.8c *(sweep)* | `.superimpose(x => x.add(note(-7)))` called contrary motion | Parallel motion. | open |
| H18 | EDM.9e *(sweep)* | 3+3+2 in 8 pulses called son clave | That is the tresillo; the history string isn't the son clave (code is correct). | open |
| H19 | EDM.9f *(sweep)* | `.jux` labelled "inversion"; Art of Fugue subject opens down a 4th | `.jux` is stereo split; melodic inversion is missing. The real subject rises a 5th *(recall)*. | open |
| H20 | EDM.9c *(sweep)* | Eno's coprime loops "never repeat" | Integer lengths realign at the LCM (17·23·29 = 11,339 s if those lengths are right; lengths unverified). | open |
| H21 | EDM.9a *(sweep)* | Code plays triads, comments say sevenths; G major in C minor | B♮ comes from harmonic minor; unstated. | open |
| H22 | hljod listening tables *(sweep)* | Genre tags (Zhu Zaiyu "hip-hop", *So What* "liquid DnB", Schaeffer "hip-hop") | Wrong; do not reuse tables. | open |
| H23 | hljod L0–L7 game "approximations" (AUDIT.md) | Named game-music transcriptions | AUDIT rates 0/15 correct, 9 wrong. Do not reuse as named pieces. | open |
| H25 | hljod euclidean-circle / EDM.0 (read) | "The tresillo and the son clave are the same necklace, worn differently"; (3,8,2) presented as the clave | Son clave is a 5-onset, 16-pulse pattern; rotations of E(3,8) are tresillo rotations. | open |
| H24 | hljod Syllabus | "Prose and most capstone samples are AI-generated" | Reuse structure, demos, code and facts only; never prose. | standing rule |
