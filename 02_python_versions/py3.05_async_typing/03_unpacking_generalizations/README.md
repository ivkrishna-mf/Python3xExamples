# Additional unpacking generalisations — Python 3.5 (PEP 448)

**In one line:** use `*` and `**` multiple times in calls and inside list/tuple/set/dict displays.

## What it is
`f(*a, *b, **c, **d)` and literals like `[*a, *b]`, `{**defaults, **overrides}` now work,
making merging and concatenation one-liners.

## When to use
- Merging dicts with precedence (3.9+ also has `|`).
- Building lists/sets/tuples from several iterables.
- Forwarding several argument sources to a call.

## When NOT to use
- On very large iterables in hot paths — consider `itertools.chain` to avoid copies.

## Run
```bash
python examples.py
```
