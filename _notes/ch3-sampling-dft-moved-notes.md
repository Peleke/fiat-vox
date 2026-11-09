# Ch. 3 (Sampling & the DFT) — notes moved out of the chapter, 2026-11-09

Moved verbatim from cells 1–3 of `04-sampling-dft.ipynb`.

## Former cell 1

- Recording: Analog vs Digital
    - Sampling 
    - Waves as displacements over time 
    - Derivation of sine/cosine representation by sampling tuning fork

## Former cell 2

TODO

- Intuitive interpretation of matrix multiplication as change of basis: "New x is z times old, new y is ... etc.". This is what the matrix multiplication is saying. Because I can figure out _each new axis with only its corresponding partner in the input_, i can deal with _everything separately_, in turn. _You can't do this with non-orthogonal matrices_.
  - Like if I give you straght line directions to a hotel in NYC. I pull out a map, label the landmarks, and draw straight lines between them; in my $xy$-coordinates, it's straight lines between checkpoints. But you walk; you need to think in Manhattan distances on the grid. It would have been better to just give you a path in terms of the streets, so you don't have to translate.
- If I give you directions in _my_ coordinates, they break once the grid changes. Now, if you keep going in the direction we called "straight", you have to stop, at every block, and figure out _how far in both directions you went_. This becomes expensive and error prone; it would be much easier if you could just shift the directions to the new grid.
- You can:
  - Move the aove here; scenario is: We give you directions to get someplace, but wher we are standing, there is a road that extends left/right (like x-axis); and one that extends to the "northeast", 30 degrees off the road we're on. We use these two roads are our basis vectors; interlocutor needs to walk up the 30 degree street anyway. But then after a mile, it becomes a standard grid. Now, when we follow the new grid path, we have to _stop and check_ how far we've moved on our original line, and map our position back to our original coordinates. It would be easier if we cold just switch them over once and for all.
  - This happens because, in this new grid system, the "basis" we chose _is not orthogonal_; it can generate a path to the destination, but since it "mixes" the directions in which we're constrained to move, actually measuring movement is complicated, because it's an "unnatural" _representation_ of where we actually are.
- You'd do this by taking your line and _projecting_ it onto the grid: Everywhere it casts a shadow is a step.
  - This is, specifically, the transformation from $L_{2}$ to $L_{1}$, the "taxicab transformation", that projects lines in "free" Euclidean space into grid-constrained paths.
- The intersections of the grid are at 90 degree angles. That means that we have options to get to our destination: We can move all x units right, then all y units up; or "mix and match" to get around road blocks. The point is, if I move some distance horizontally, it has _no effect_ on how far I have to move vertically; I can deal with both separately.
  - If they _weren't_, every step I take would _also_ affect how far I have left to go vertically; imagine walking a diagonal road through Manhattan. You have to adjust _both_ how far up/down _and_ left/right you go. Annoying.

This is the advantage to orthogonal matrices. I can take "directions" you've provided, that are valid where _you_ are, and convert them, _piece by piece_, into a series of directions that make sense to me. The translation doesn't destroy information, so I can always translate _back_ to your terms if I need to.

## Former cell 3

TODO

- DFT is literally a vibe check.
- The "check" happens to be the dot product: if i take every piece of me, with every piece of you, add em up, and it's _not nothing_, it's a match.
- We collect the matches, order them, and ghost what we don't like (LPF).

