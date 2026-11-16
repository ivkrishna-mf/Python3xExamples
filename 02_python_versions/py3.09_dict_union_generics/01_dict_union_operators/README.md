# Dict merge `|` and update `|=` — Python 3.9 (PEP 584)

**In one line:** `merged = defaults | overrides`; `config |= extra` updates in place.

## What it is
`d1 | d2` returns a new dict (right side wins on conflicts). `d1 |= d2` updates `d1`
(and accepts any mapping or iterable of pairs, like `dict.update`).

## When to use
- Layering configs: defaults | file | env | CLI flags.
- Building request headers/params from a base set.
- Any time you'd write `{**a, **b}` — `|` reads more clearly.

## When NOT to use
- Deep/nested merges — `|` is shallow; write a recursive merge for nested dicts.
- Code that must run on Python < 3.9.

## Run
```bash
python examples.py
```
