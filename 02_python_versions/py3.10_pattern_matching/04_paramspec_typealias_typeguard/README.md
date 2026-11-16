# ParamSpec, Concatenate, TypeAlias, TypeGuard — Python 3.10 (PEP 612, 613, 647)

**In one line:** type decorators precisely, name complex types, and write type-narrowing helpers.

## What it is
- `ParamSpec("P")` captures a function's full parameter list so a decorator keeps it.
- `Concatenate[X, P]` describes "adds/removes a leading parameter".
- `TypeAlias` marks an explicit alias (3.12 replaced it with the `type` statement).
- `TypeGuard[T]` lets a boolean function narrow its argument's type (3.13 adds `TypeIs`).

## When to use
- Decorators: logging, retry, timing, auth, caching — preserve signatures for IDEs.
- Long/complex types used in many places.
- Validation helpers (`is_str_list(x)`) that should narrow types.

## When NOT to use
- 3.12+: prefer `def deco[**P, R](...)` and `type Alias = ...`.
- 3.13+: prefer `TypeIs` over `TypeGuard` in most cases.

## Run
```bash
python examples.py
```
