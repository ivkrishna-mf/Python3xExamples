# print() as a function — Python 3.0 (PEP 3105)

**In one line:** `print` is a normal function with `sep`, `end`, `file` and `flush` keywords.

## What it is
In Python 2 `print` was a statement. In Python 3 it is a built-in function, so it can be
passed around, wrapped, redirected and configured with keyword arguments.

## When to use
- Quick output in scripts, CLIs and teaching code.
- Writing to `sys.stderr` or any file-like object with `file=`.
- Building simple separators/progress output with `sep=` / `end=` / `flush=True`.

## When NOT to use
- Libraries and long-running services → use `logging` instead.
- Building strings for later use → use f-strings / `str.join`.

## Run
```bash
python examples.py
```
