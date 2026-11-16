# Lists

**Introduced:** Python 1.0 · `sorted()` + `key=` 2.4 · list comprehensions 2.0

**In one line:** ordered, mutable, growable sequences — Python's workhorse collection.

## What it is
`list` supports indexing, slicing, `append`, `extend`, `insert`, `pop`, `remove`, `sort`,
`reverse`, membership tests and unpacking. `sorted()` returns a new list; `.sort()` sorts in place.

## When to use
- Ordered collections you add to or modify.
- Stacks (`append`/`pop`).
- Sorting with `key=` (e.g. `key=lambda u: u.age`).

## When NOT to use
- Queues popping from the front → `collections.deque`.
- Frequent membership tests on large data → `set`.
- Fixed records → `tuple` / dataclass.

## Run
```bash
python examples.py
```
