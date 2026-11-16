# Tuples and named tuples

**Introduced:** tuple 1.0 · `collections.namedtuple` 2.6 · `typing.NamedTuple` class syntax 3.6

**In one line:** immutable, hashable sequences — ideal for fixed records and multiple return values.

## What it is
A tuple groups values: `(lat, lon)`. Being immutable, tuples of hashables can be dict keys
and set members. `NamedTuple` adds field names while staying a tuple.

## When to use
- Returning several values from a function.
- Fixed-size records, coordinates, composite dict keys.
- Lightweight read-only data with `NamedTuple`.

## When NOT to use
- Collections you need to change → list.
- Records with defaults/validation/methods → `@dataclass` is often nicer.

## Run
```bash
python examples.py
```
