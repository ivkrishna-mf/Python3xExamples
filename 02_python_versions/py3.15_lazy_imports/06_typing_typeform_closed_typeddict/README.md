# TypeForm, closed TypedDicts & disjoint bases — Python 3.15 (PEP 747, 728, 800)

**In one line:** type "a type expression" as a value, and declare TypedDicts that forbid (or type) extra keys.

## What it is
- `TypeForm[T]` annotates a parameter that receives a *type expression* (`int | None`,
  `list[str]`), letting checkers infer the result type of `trycast(int | None, v)`.
- `class Movie(TypedDict, closed=True)` — no keys other than those declared.
  `extra_items=int` — any extra key must have an `int` value.
- `@typing.disjoint_base` marks classes that can't share a subclass with other such bases.

## When to use
- Runtime validators/converters (`cast`-like helpers, pydantic-style APIs) → `TypeForm`.
- Strict JSON shapes (closed) or "known keys + typed extras" (extra_items).
- Library authors describing C-level layout conflicts → `disjoint_base`.

## When NOT to use
- Regular application code rarely needs `TypeForm` or `disjoint_base`.
- These are static-typing features; runtime behaviour is unchanged.

## Run
```bash
python3.15 examples.py
```
