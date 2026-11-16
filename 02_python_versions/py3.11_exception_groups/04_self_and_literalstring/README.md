# typing.Self and LiteralString — Python 3.11 (PEP 673, 675)

**In one line:** `-> Self` for methods returning their own class; `LiteralString` to guard against injection.

## What it is
- `Self` means "the type of the current instance", so subclasses get correct return types for
  fluent/builder methods and alternative constructors.
- `LiteralString` accepts only strings written literally in source (or built from literals),
  so type checkers flag user input flowing into SQL/shell APIs.
- Also new in 3.11: `assert_never`, `reveal_type`, `assert_type`, `Never`.

## When to use
- Builders, `copy()`/`with_x()` methods, `@classmethod` constructors (`Self`).
- Database/shell/query APIs where injection is a risk (`LiteralString`).
- Exhaustiveness checks on enums/unions (`assert_never`).

## When NOT to use
- Return types that are always the base class.
- `LiteralString` isn't enforced at runtime — keep using parameterised queries.

## Run
```bash
python examples.py
```
