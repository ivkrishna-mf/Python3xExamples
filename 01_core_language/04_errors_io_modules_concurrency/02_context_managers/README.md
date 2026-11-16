# Context managers: the `with` statement and contextlib

**Introduced:** `with` 2.5 (PEP 343) · multiple managers 2.7/3.1 · `contextlib.suppress` 3.4 · `ExitStack` 3.3 · `asynccontextmanager` 3.7 · parenthesised 3.10 · `chdir` 3.11

**In one line:** guarantee setup and cleanup (close files, release locks, roll back transactions) even when errors happen.

## What it is
`with expr as x:` calls `__enter__` before the block and `__exit__` after (even on exceptions).
`contextlib.contextmanager` turns a generator into a context manager. Helpers: `suppress`,
`redirect_stdout`, `ExitStack`, `nullcontext`, `closing`, `chdir`.

## When to use
- Files, sockets, locks, DB connections/transactions, temporary state changes.
- Timing/profiling blocks; temporarily patching settings.

## When NOT to use
- Resources whose lifetime spans many functions/objects → manage explicitly (or ExitStack).

## Run
```bash
python examples.py
```
