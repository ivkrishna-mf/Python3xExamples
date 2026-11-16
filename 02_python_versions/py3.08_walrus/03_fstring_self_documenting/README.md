# f-string `=` specifier — Python 3.8

**In one line:** `f"{x=}"` prints `x=42` — the expression text *and* its value.

## What it is
Adding `=` after an expression in an f-string emits the source text, `=`, and the repr of the
value. Format specs and conversions still work (`{x=:.2f}`, `{name=!s}`), and whitespace is
preserved (`{x = }`).

## When to use
- Quick debugging prints.
- Logging/tracing variable values during development.
- Readable assertion / error messages.

## When NOT to use
- User-facing output (shows code text).
- Production logging — prefer structured logging.

## Run
```bash
python examples.py
```
