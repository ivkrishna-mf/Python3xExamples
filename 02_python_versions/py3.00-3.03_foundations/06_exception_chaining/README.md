# Exception chaining — Python 3.0 / 3.3 (PEP 3134, PEP 409, PEP 415)

**In one line:** `raise NewError(...) from original` keeps the root cause; `from None` hides it.

## What it is
Exceptions carry `__cause__` (explicit, via `from`) and `__context__` (implicit — raised while
handling another). Tracebacks show both, so you never lose the original failure.

## When to use
- Translating low-level errors into domain errors: `raise ConfigError(...) from exc`.
- `from None` when the inner error is an implementation detail that would confuse users.
- Inspecting `__cause__` in tests or error reporting.

## When NOT to use
- Don't wrap just to wrap — if the original exception is already meaningful, let it propagate.

## Run
```bash
python examples.py
```
