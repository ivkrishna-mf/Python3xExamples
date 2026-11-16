# functools.cache — Python 3.9

**In one line:** `@cache` = `@lru_cache(maxsize=None)` — simple unbounded memoisation.

## What it is
A thin, slightly faster wrapper for an unbounded LRU cache. Same API (`cache_info`,
`cache_clear`).

## When to use
- Pure functions with a small/bounded set of possible inputs.
- Recursive algorithms (DP), parsing helpers, one-time lookups.

## When NOT to use
- Unbounded input domains (memory grows forever) → `lru_cache(maxsize=N)`.
- Methods on many short-lived instances (cache keeps them alive).
- Side-effecting or time-dependent functions.

## Run
```bash
python examples.py
```
