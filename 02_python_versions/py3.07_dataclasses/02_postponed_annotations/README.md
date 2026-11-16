# Postponed evaluation of annotations — Python 3.7 (PEP 563)

**In one line:** `from __future__ import annotations` stores annotations as strings, so forward references just work.

## What it is
With the future import, annotations are not evaluated at definition time. That allows
referencing classes defined later (or the class itself) without quotes and makes imports
cheaper. Python 3.14 replaced this with *lazy* annotations by default (PEP 649/749 — see the
3.14 folder); the future import still works.

## When to use
- Code supporting Python 3.7–3.13 with many forward references / self-references.
- Using new syntax in annotations (`list[int]`, `X | None`) on older interpreters (3.7+).
- Avoiding import cycles caused by type-only imports (combine with `TYPE_CHECKING`).

## When NOT to use
- Code that reads `__annotations__` at runtime expecting real objects (use
  `typing.get_type_hints()` instead).
- New 3.14+-only code — deferred evaluation is already the default.

## Run
```bash
python examples.py
```
