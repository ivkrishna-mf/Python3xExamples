# ReadOnly TypedDict keys — Python 3.13 (PEP 705)

**In one line:** `ReadOnly[str]` marks a TypedDict key that type checkers won't let you modify.

## What it is
Readers can rely on the key not being reassigned or deleted through that type. It also makes
read-only TypedDicts compatible with more specific ones (useful for function parameters).

## When to use
- IDs, timestamps and other fields that must not change after creation.
- Function parameters that only read a dict (accept wider inputs safely).

## When NOT to use
- You need runtime immutability → use `MappingProxyType` or `frozendict` (3.15).

## Run
```bash
python examples.py
```
