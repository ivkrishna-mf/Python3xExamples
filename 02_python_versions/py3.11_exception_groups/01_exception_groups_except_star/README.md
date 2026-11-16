# ExceptionGroup and `except*` — Python 3.11 (PEP 654)

**In one line:** raise and handle *several* unrelated exceptions at once.

## What it is
`ExceptionGroup("msg", [e1, e2])` bundles exceptions. `except* TypeError:` handles only the
matching members; the rest keep propagating. `asyncio.TaskGroup` raises groups when several
tasks fail.

## When to use
- Concurrent work (TaskGroup, thread pools) where multiple tasks can fail.
- Validation that reports *all* problems instead of the first.
- Cleanup steps where several independent failures can happen.

## When NOT to use
- Ordinary single-error code paths — plain `try/except` is simpler.
- You can't mix `except` and `except*` in the same `try`.

## Run
```bash
python examples.py
```
