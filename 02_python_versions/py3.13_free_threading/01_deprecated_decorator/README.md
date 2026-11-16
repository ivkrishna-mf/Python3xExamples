# @warnings.deprecated — Python 3.13 (PEP 702)

**In one line:** mark functions/classes/overloads as deprecated — warns at runtime *and* in type checkers/IDEs.

## What it is
`@deprecated("use new_func() instead")` emits `DeprecationWarning` when called/instantiated
and sets `__deprecated__`. Type checkers and editors show strike-through and warnings.

## When to use
- Phasing out library APIs with a clear migration message.
- Renaming functions while keeping old names temporarily.

## When NOT to use
- Internal code you can just change in one commit.
- Code supporting < 3.13 → `typing_extensions.deprecated`.

## Run
```bash
python examples.py
```
