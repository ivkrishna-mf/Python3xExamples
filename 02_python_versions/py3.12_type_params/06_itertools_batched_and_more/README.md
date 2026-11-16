# itertools.batched & other 3.12 stdlib additions

**In one line:** `batched("ABCDEFG", 3)` → `('A','B','C') ('D','E','F') ('G',)`.

## What it is
- `itertools.batched(iterable, n)` splits into tuples of length `n` (3.13 adds `strict=True`).
- `pathlib.Path.walk()` (like `os.walk`), `Path.with_segments`.
- `math.sumprod`, `statistics` improvements, `calendar.Month`/`Day` enums,
  `sqlite3` CLI (`python -m sqlite3`), `uuid` CLI (`python -m uuid`).

## When to use
- Bulk inserts, API pagination/batching, chunked file processing (`batched`).
- Directory traversal with `Path` objects (`Path.walk`).
- Dot products / weighted sums without NumPy (`sumprod`).

## When NOT to use
- `batched` on data you need as overlapping windows → use `collections.deque` / `pairwise`.

## Run
```bash
python examples.py
```
