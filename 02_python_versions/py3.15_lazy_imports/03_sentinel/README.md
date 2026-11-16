# sentinel built-in — Python 3.15 (PEP 661)

**In one line:** `MISSING = sentinel("MISSING")` — a unique marker with a clean repr that works in type hints.

## What it is
`sentinel(name, /, *, repr=None)` creates a unique object. It prints as its name, keeps its
identity through `copy`/`deepcopy` and pickling (when importable by module + name), and can be
used directly in annotations: `def f(x: int | MISSING = MISSING)`.
Compare with `is`, never `==`.

## When to use
- "No value given" defaults when `None` is a valid value.
- Marking "not found", "end of stream", "use default" in APIs and caches.
- Replacing `_MISSING = object()` (ugly repr, not typeable, breaks on pickle).

## When NOT to use
- When `None` already means "absent" unambiguously.
- A closed set of several states → `enum.Enum`.

## Run
```bash
python3.15 examples.py
```
