# functools.lru_cache — Python 3.2

**In one line:** memoise a pure function's results with a bounded, least-recently-used cache.

## What it is
`@lru_cache(maxsize=128)` stores results keyed by the arguments. Repeated calls with the same
(hashable) arguments return instantly. `cache_info()` and `cache_clear()` help you inspect it.

## When to use
- Expensive, deterministic functions called repeatedly with the same inputs.
- Recursive algorithms with overlapping sub-problems (dynamic programming).
- Caching config/parsing lookups.

## When NOT to use
- Functions with side effects or results that change over time.
- Unhashable arguments (lists, dicts).
- On instance methods without care — the cache keeps `self` alive (memory leak risk).
- For unbounded caching prefer `functools.cache` (3.9).

## Run
```bash
python examples.py
```
