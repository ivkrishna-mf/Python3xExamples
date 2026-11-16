# Properties, descriptors and __slots__

**Introduced:** `property`, descriptors, `__slots__` 2.2 · `@prop.setter` syntax 2.6 · `__set_name__` 3.6 · `cached_property` 3.8

**In one line:** control attribute access — computed attributes, validation and memory-lean objects.

## What it is
- `@property` turns a method into a read-only attribute; add `@x.setter`/`@x.deleter`.
- Descriptors (`__get__/__set__/__set_name__`) are reusable property-like objects;
  `property`, `classmethod` and `staticmethod` are built on them.
- `__slots__` declares fixed attributes, saving memory and preventing typos.

## When to use
- Validation on assignment; computed/derived values; backwards-compatible API changes
  (turn an attribute into a property without changing callers).
- Reusable field validators (descriptors).
- Millions of small objects (`__slots__`, or `@dataclass(slots=True)`).

## When NOT to use
- Plain attributes are fine — don't write getters/setters "just in case".
- Expensive work in a property (callers expect attribute access to be cheap).

## Run
```bash
python examples.py
```
