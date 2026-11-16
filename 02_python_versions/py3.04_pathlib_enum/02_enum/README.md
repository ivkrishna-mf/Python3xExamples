# enum — Python 3.4 (PEP 435) · plus Flag/auto (3.6) and StrEnum (3.11)

**In one line:** a fixed set of named constants with identity, iteration and type safety.

## What it is
`class Color(Enum): RED = 1` creates singleton members. `IntEnum`/`StrEnum` also behave like
ints/strings; `Flag` supports bitwise combinations; `auto()` assigns values for you.

## When to use
- Replacing "magic" strings/ints: statuses, roles, modes, HTTP methods.
- Function parameters that accept one of a known set of options.
- Bit flags/permissions with `Flag`.
- Pattern matching on states (works great with `match`).

## When NOT to use
- Open-ended sets of values that change at runtime (use a dict / DB table).
- When plain `Literal["a", "b"]` type hints are enough and you don't need runtime objects.

## Run
```bash
python examples.py
```
