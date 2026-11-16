# typing.TypeIs — Python 3.13 (PEP 742)

**In one line:** a user-defined type guard that narrows in *both* the `if` and the `else` branch.

## What it is
`def is_str(x: object) -> TypeIs[str]` — when it returns True the checker treats `x` as `str`;
when False, as "not str". Unlike `TypeGuard` (3.10), the narrowed type must be consistent with
the input type, which makes it safer and more intuitive.

## When to use
- `isinstance`-like helpers: `is_int_list`, `is_user_dict`, `is_valid_event`.
- Distinguishing union members with custom logic.

## When NOT to use
- When the guard narrows to a type *unrelated* to the input → `TypeGuard`.
- Pre-3.13 → `typing_extensions.TypeIs`.

## Run
```bash
python examples.py
```
