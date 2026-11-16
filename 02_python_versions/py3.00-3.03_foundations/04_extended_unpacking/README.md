# Extended iterable unpacking — Python 3.0 (PEP 3132)

**In one line:** `first, *rest = items` collects "everything else" into a list.

## What it is
A starred target in an assignment grabs all remaining items. Only one starred name is allowed
per assignment, and it always becomes a `list`.

## When to use
- Splitting head/tail: `cmd, *args = line.split()`.
- Ignoring the middle: `first, *_, last = rows`.
- Swapping / rotating values, parsing records of variable length.

## When NOT to use
- On huge or infinite iterators — the starred part is fully materialised.
- When fixed indexing (`x[0]`) is clearer.

## Run
```bash
python examples.py
```
