# Warnings for return/break/continue in `finally` — Python 3.14 (PEP 765)

**In one line:** the compiler now emits `SyntaxWarning` when `return`/`break`/`continue` would exit a `finally` block.

## What it is
Leaving a `finally` with `return`/`break`/`continue` silently *swallows* any in-flight exception
(including `KeyboardInterrupt`). 3.14 warns about it at compile time.

## When to use (this knowledge)
- Code review & linting: move the `return` after the `try` statement.
- Understanding why legacy code "loses" exceptions.

## When NOT to use
- Never write control flow out of `finally` in new code.

## Run
```bash
python examples.py
```
