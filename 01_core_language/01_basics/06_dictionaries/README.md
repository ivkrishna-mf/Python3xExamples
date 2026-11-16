# Dictionaries

**Introduced:** dict 1.0 · dict comprehensions 2.7/3.0 · ordered 3.7 · `|` merge 3.9

**In one line:** fast key → value mappings, insertion-ordered, with comprehensions and merge operators.

## What it is
Keys must be hashable. Lookup, insert and delete are O(1) on average. Important methods:
`get`, `setdefault`, `pop`, `items`, `keys`, `values`, `update`, plus `|`/`|=`.

## When to use
- Lookups by key, counting, grouping, caching, JSON-like data.
- Configuration and keyword-argument forwarding.

## When NOT to use
- Fixed, known fields → dataclass / TypedDict for clarity.
- Counting/grouping → `Counter` / `defaultdict` are clearer (see `11_collections_module`).

## Run
```bash
python examples.py
```
