# Union types with `X | Y` — Python 3.10 (PEP 604)

**In one line:** write `int | None` instead of `Optional[int]`, `int | str` instead of `Union[int, str]`.

## What it is
The `|` operator on types creates a `types.UnionType`. It works in annotations *and* at
runtime with `isinstance(x, int | str)`.

## When to use
- All new type hints on 3.10+ (or 3.7+ with `from __future__ import annotations`).
- `isinstance`/`issubclass` checks against several types.

## When NOT to use
- Runtime expressions on Python < 3.10 (string annotations are fine with the future import).

## Run
```bash
python examples.py
```
