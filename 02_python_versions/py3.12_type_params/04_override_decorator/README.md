# @typing.override — Python 3.12 (PEP 698)

**In one line:** mark a method as overriding a parent method so checkers catch typos and renames.

## What it is
`@override` sets `__override__ = True` at runtime and tells type checkers "this must exist in a
base class". If the base method is renamed/removed, the checker reports an error.

## When to use
- Every overriding method in class hierarchies you maintain (frameworks, plugins, tests).
- Especially when base classes come from another package that might change.

## When NOT to use
- New methods that don't override anything (checker error).
- Code supporting < 3.12 → `typing_extensions.override`.

## Run
```bash
python examples.py
```
