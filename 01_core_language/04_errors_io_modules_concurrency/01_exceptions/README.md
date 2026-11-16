# Exceptions: try / except / else / finally, raise, custom errors

**Introduced:** exceptions 1.0 · `try/except/finally` combined 2.5 · `as` syntax 2.6/3.0 · chaining 3.0 · groups & notes 3.11

**In one line:** signal and handle errors explicitly; catch specific exceptions, clean up in `finally`.

## What it is
`raise` signals an error; `try/except` handles it; `else` runs if nothing was raised;
`finally` always runs. Build a small hierarchy of custom exceptions for your domain, and chain
with `raise ... from ...` to keep the root cause.

## When to use
- Exceptional situations (missing file, invalid input, network failure).
- EAFP style: try the operation, handle failure (`try: d[k] except KeyError`).
- Custom exceptions for library/domain errors callers may want to catch.

## When NOT to use
- Bare `except:` or `except Exception: pass` (hides bugs).
- Exceptions for normal control flow in hot loops.

## Run
```bash
python examples.py
```
