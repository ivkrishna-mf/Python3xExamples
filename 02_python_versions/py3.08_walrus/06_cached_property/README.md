# functools.cached_property — Python 3.8

**In one line:** a property computed once per instance, then stored as a normal attribute.

## What it is
The first access runs the method and saves the result in the instance `__dict__`; later
accesses are plain attribute lookups. Delete the attribute (`del obj.prop`) to recompute.

## When to use
- Expensive derived values on objects that don't change: parsed config, compiled regex,
  computed statistics, loaded resources.
- Lazy initialisation of heavy attributes.

## When NOT to use
- Values that must update when other attributes change (use `@property`).
- Classes with `__slots__` and no `__dict__`.
- Shared/class-level caching (use `functools.cache` on a function).

## Run
```bash
python examples.py
```
