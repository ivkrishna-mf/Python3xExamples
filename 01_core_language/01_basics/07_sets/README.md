# Sets and frozensets

**Introduced:** `sets` module 2.3 · built-in `set`/`frozenset` 2.4 · set literals & comprehensions 2.7/3.0

**In one line:** unordered collections of unique, hashable items with fast membership and set algebra.

## What it is
`set` is mutable, `frozenset` immutable (and hashable). Operators: `|` union, `&`
intersection, `-` difference, `^` symmetric difference, `<=` subset.

## When to use
- De-duplicating, fast `in` checks on many items.
- Comparing groups: who is in both lists, who's missing.

## When NOT to use
- You need order or duplicates → list (or `dict.fromkeys` for ordered unique).
- Items are unhashable (lists, dicts).

## Run
```bash
python examples.py
```
