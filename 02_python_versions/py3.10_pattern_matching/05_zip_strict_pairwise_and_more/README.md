# zip(strict=True), itertools.pairwise & friends — Python 3.10 (PEP 618)

**In one line:** catch length mismatches in `zip`, iterate over consecutive pairs, plus small 3.10 helpers.

## What it is
- `zip(a, b, strict=True)` raises `ValueError` if the iterables differ in length.
- `itertools.pairwise(s)` → `(s0,s1), (s1,s2), ...`.
- Also new: `int.bit_count()`, `bisect` with `key=`, `aiter()`/`anext()` built-ins,
  `dataclass(slots=True, kw_only=True)` (see the 3.7 folder).

## When to use
- `strict=True` whenever the inputs *must* align (columns/headers, parallel lists).
- `pairwise` for deltas, transitions, sliding comparisons, route segments.
- `bisect(key=...)` for searching sorted records.

## When NOT to use
- `strict=True` when shorter-wins truncation is intended (or use `itertools.zip_longest`).

## Run
```bash
python examples.py
```
