Adapts the below, starting from "but wait there's more":

Good catch; yes I'm actually ignoring leakage at the moment and assuming a perfectly periodic/ideal input; the coverage route is DFT -> notice that once it works it drops time dynamics -> STFT -> naive window chopping introduces strange artifacts -> "universality" of the impulse, leakage, windows, etc.

Mainly, looking for validation on the "tuning fork" machine analogy. The analogy I want to lead with is: We generate the test frequency set (go grab our tuning forks, different set for each sound depending on how "long" it is/size of N, deal with relationship to bins and assumption of unit time later). We then play your sound once for each fork. Actually, maybe the right way to say it is: If _our fork_ rings _while your song is playing_, we've _detected_ that your song _contains that frequency_. We measure _how much/loudly_ the fork moves.

Now: Build a "keyboard". We can make it bigger or smaller depending on the sound, to accommodate however many forks we need. When someone hands you a sound, we grab the right forks, slot them in—maybe a better way to tink of it is as a gigantic machine with _enough_ forks for most uses, and then we just only use a subset (assuming nyquist at 22.1kHz and integer test frequencies this is conceivable, if contrived and unrealistic; it's not an uncountable set of frequencies or anything). Then, we play. that sound _through the machine_, and write down which tuning forks rang, and how much. It's a sound prism.

Each tuning fork represents a different basis vector in N-dimensional frequency space, where, again, N is determined by the "complexity" of the input sound. So the output measurements are coefficients for a linear combination of...Stuff.

_But_, since each tuning fork, despite being a physical device, responds to a _specific pure tone_, its _response_ to a resonance can be inverted into a _generator_ by simply..._Ringing_ the tuning fork.

So taking our output and "playing" the keyboard should produce the same sound as the input. We'll assume sufficient sampling for perfect reconstruction here.

Now—the idea for which I'm trying to evince an intuition is that each tuning fork is completely distinguishable from the others. If a signal contains 500 Hz and 501 Hz, well, it doesn't "maybe contain 501.5" (barring, of course, Gabor, etc., consider an ideal scenario here), if our forks are perfectly sensitive. That means we _can_ ring each one the right amount after and expect to get the same thing we started with; it's not like some of our forks actually ring as chords (if they did, we'd have a problem; this thought experiment is one of the ways I'm going to discuss the issue of resolution a bit later + augment the discussion of the importance of orthogonality, which as thus far been discussed in terms of directions shifting "meaning" when we end up following instructions from a road that moves 30 degrees of "normal" xy northeast, and then suddenly merges into a Manhattan-style grid, so our directions now don't make sense (following the new grid, which we have to do, means we have to check where we are relative to our initial instructions every corner, and might overshoot) unless we transform them; and the fact the grid is orthogonal makes this easy, cause we can take simple shadows and break our paths up into _arbitrary sequences_; if we used "chord forks", we'd have a similar problem–I could tell you the input has something that harmonizes with CMaj6, but wheter CAGE :shrug:; basically your note on ringing two, we touch on this when we revisit Gabor and uncertainty in general).

That means our "sound comb" basically just correlates the input with each tuning fork. ...And not just basically: That's rigorous. The inner product between the input and the complex exponential representing each tuning fork's oscillation _is a literal correlation_. The set of correlation strengths plus activated tuning forks yields the original sound, _because the forks are separate_.

At that point, it's motivated to ask: Well, let's maybe make sure our tuning forks _are_ uncorrelated...Otherwise we're testing with chords.

Then, we proceed to show pairwise orthogonal of complex exponentials, which really only makes a ton of sense to me if we take the above route to get there, otherwise it's just a math trick.

At that point, though, we have the _definition_ of a unitary matrix: A complex orthonormal (well, close enough) matrix acting as a basis for frequency space, which fell out of a matrix representation of the system of equations representing simply creating a chord out of four sine waves.

_Then_, we implement the quadratic DFT using the finally justified matrix definition.

BUT WAIT THERE'S MORE.

After that we touch on some obligations: STFT, windows, Mel spectrogram, etc., the idea is to explain everything needed to understand using CNNs to classify Hillenbrand vowels with PyTorch via CNN.

But not because that's interesting. Because it's a playground for explaining all of the above in terms of formants and DFT, in-depth; show a relevant technique; and then take the excuse to discuss some heavy-hitters

- Prereq to CNNs: Convolution
- Convolution in terms of circulant matrices
- Convolution theorem: The DFT appears, again...Somewhat out of nowhere.
- Not just that: If the DFT diagonalizes all circulant matrices, then its columns are the eigenvectors of all circulant matrices—and those eigenvectors are precisely the complex roots of unity.
- Circulants share eigenvectors "because" all circulant matrices can be generated by stacking shifts; or, better, circulants are generated via polynomials of the shift operator.
    - And, w...ait. If they're generated by the shift operator, then..._Only_ the eigenvectors of the shift matter. We also know that any circulant commits with a shift, because a circulant is just a product of powers of shifts, and matrices commute with themselves and their own powers. This implies that shifting + convolve is the same as convolve + shift, thanks to commutativity. So...Shift invariance of CNNs drops out from the algebra.
- That also means that multiplying the shift matrix by an eigenvector is equivalent to scaling the eigenvector...But what kind of function is _identical under shift_, up to scale? ...Sinusoids. What "makes" up for a shift, or encodes one? A phase delay...Corresponding to a root of unity.
    - So complex exponentials are FORCED.
    - Even better: This has nothing to do with "frequency". Or time. Or sound. Or signals. This is purely a consequence of algebra. Sinusoids are forced by structure. And if C commutes with S, this Fourier basis underlies _all circulant matrices_, regardless of how we might intuitively categorize them.
    - But, wait. Again. The adjacency representation of a circulant matrix generates a graph whose vertices can be mapped to a regular polygon of N sides within the unit circle on the complex plane; that graph is symmetrical, which...Is never an accident.
- Look closer: It's the Cayley graph of a cyclic group.

So...Wait. The DFT isn't about signals; it's not even "about" circulants...Or, really, even the roots of unity. It's a change of basis that simultaneously characterizes _all_ circular convolutions. Wowzers.

And...Thing is. Shift invariance with regard to sinusoids makes sense; it's equivalent to shift invariant action on vectors of the finite cyclic group (as we see from the matrix and vector representations)...The Cayley graph isn't just beautiful.

But, that then suggests...Shifting a vector under the group action of Zn and applying a circulant operator is the same as the commutative action. That should make you wonder: Can you parameterize Zn, replacing it with _any_ group whose action commutes with circulant matrices?...We then proceed to set the stage for a discussion of recovery of the Fourier Transform and z-Transform by extension to infinite mutually commuting matrices; then explain what happens when they do _not_ commute, starting with the symmetric group as the simplest example; here we get block diagonalization and representations mapping to subspace, and an introduction to group representation.

Payoff: This is the start of GDL.
