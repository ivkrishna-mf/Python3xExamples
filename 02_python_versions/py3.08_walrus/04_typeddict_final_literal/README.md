# TypedDict, Final and Literal — Python 3.8 (PEP 589, 591, 586)

**In one line:** precise types for dict shapes, constants and allowed literal values.

## What it is
- `TypedDict` describes a dict with known keys and value types (great for JSON).
- `Final` marks a name/attribute that must not be reassigned; `@final` forbids
  overriding/subclassing.
- `Literal["a", "b"]` restricts a value to specific literals.
All are checked by type checkers; at runtime they're ordinary dicts/values.

## When to use
- Typing JSON payloads / API responses / config files (TypedDict).
- Module constants and "sealed" classes (Final / @final).
- Mode/flag parameters with a fixed set of strings (Literal).

## When NOT to use
- You need runtime validation → pydantic / dataclasses with checks.
- A full object with behaviour → a dataclass is usually nicer than TypedDict.

## Run
```bash
python examples.py
```
