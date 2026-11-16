# Iterators and generators

**Introduced:** iterator protocol 2.2 (PEP 234) · generators 2.2 (PEP 255) · `send()` 2.5 (PEP 342) · `yield from` 3.3

**In one line:** produce values lazily, one at a time, with `yield` — constant memory for any size of data.

## What it is
An iterable has `__iter__`; an iterator has `__next__` and raises `StopIteration` when done.
A generator function (contains `yield`) creates an iterator automatically and pauses between
values. Generator expressions are the inline form.

## When to use
- Processing large files/streams/DB results without loading everything.
- Infinite sequences (IDs, polling, simulations).
- Pipelines: read → filter → transform, each a generator.

## When NOT to use
- You need random access, `len()`, or to iterate multiple times → list.
- Tiny data where a list is simpler.

## Run
```bash
python examples.py
```
