# Variables, names and built-in types

**Introduced:** Python 0.9/1.0 (1991–94) · `bool` 2.3 · type hints 3.5 · `X | None` 3.10

**In one line:** names point to objects; every object has a type, an identity and a value.

## What it is
Python is dynamically and strongly typed: a variable is a name bound to an object, and the
object carries the type. Core types: `int`, `float`, `complex`, `bool`, `str`, `bytes`,
`list`, `tuple`, `dict`, `set`, `frozenset`, `NoneType`. Mutable vs immutable matters for
copying, defaults and dict keys.

## When to use
- Annotate public functions and non-obvious variables (`users: list[User] = []`).
- Use `is` only for `None`/sentinels; `==` for value equality.
- Use `isinstance()` (not `type(x) ==`) for type checks.

## When NOT to use
- Don't rely on type hints for runtime validation.
- Don't use mutable objects as default argument values.

## Run
```bash
python examples.py
```
