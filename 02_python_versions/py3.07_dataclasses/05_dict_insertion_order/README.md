# Guaranteed dict insertion order — Python 3.7 (language guarantee)

**In one line:** `dict` iterates in insertion order — officially, you can rely on it.

## What it is
CPython 3.6 implemented compact, ordered dicts; 3.7 made insertion order part of the language
spec. `**kwargs`, class namespaces and JSON round-trips preserve order too.

## When to use
- Ordered config, JSON output with stable key order, CSV column order.
- De-duplicating while preserving order: `list(dict.fromkeys(items))`.
- Simple LRU tricks (pop/reinsert), "first key" lookups.

## When NOT to use
- `OrderedDict` is still better when you need `move_to_end`, `popitem(last=False)` or
  order-sensitive equality.
- Don't treat dicts as sequences (no indexing).

## Run
```bash
python examples.py
```
