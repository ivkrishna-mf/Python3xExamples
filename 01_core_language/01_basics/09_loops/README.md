# Loops: for, while, break/continue, else, enumerate, zip

**Introduced:** for/while 1.0 · `enumerate` 2.3 · `zip` 2.0 · `zip(strict=)` 3.10

**In one line:** `for` iterates over any iterable; `while` repeats while a condition holds.

## What it is
`for x in iterable` works on lists, strings, dicts, files, generators… `range()` for counting,
`enumerate()` for index + value, `zip()` for parallel iteration, `reversed()`/`sorted()`.
`break` exits, `continue` skips, and `for/while ... else` runs `else` only if no `break`.

## When to use
- `for` whenever you have something iterable (most of the time).
- `while` for "until condition" loops: retries, polling, reading chunks.
- `for ... else` for "search, and handle not-found".

## When NOT to use
- `for i in range(len(xs))` → use `enumerate`.
- Building a list with append in a loop → often a comprehension is clearer.

## Run
```bash
python examples.py
```
