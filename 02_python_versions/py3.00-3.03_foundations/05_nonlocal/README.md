# nonlocal — Python 3.0 (PEP 3104)

**In one line:** lets a nested function *rebind* a variable from its enclosing function.

## What it is
Without `nonlocal`, assigning to a name inside a nested function creates a new local.
`nonlocal x` says "x lives in the enclosing function scope — update that one".

## When to use
- Closures that keep small private state: counters, accumulators, memo tables.
- Decorators that count calls or track timing.
- Callbacks that need to update a result held by the outer function.

## When NOT to use
- When state grows → use a small class or `dataclass` instead.
- For module-level names → that's `global` (and usually a design smell).

## Run
```bash
python examples.py
```
