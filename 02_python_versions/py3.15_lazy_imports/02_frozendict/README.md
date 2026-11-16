# frozendict built-in — Python 3.15 (PEP 814)

**In one line:** an immutable, hashable dict: `frozendict(host="db", port=5432)`.

## What it is
A mapping that can't be modified after creation. It keeps insertion order, compares equal
regardless of order, and is hashable if all keys and values are hashable. It is *not* a
subclass of `dict` (check with `isinstance(x, (dict, frozendict))` or `collections.abc.Mapping`).
Works with `copy`, `pickle`, `json`, `pprint`; `|` returns a new frozendict.

## When to use
- Constants and default configuration that must never be mutated.
- Dict values as keys in other dicts/sets, or as `functools.cache` arguments.
- Thread-safe shared read-only data (especially with free-threading).
- Fully immutable JSON with `json.loads(..., object_hook=frozendict, array_hook=tuple)`.

## When NOT to use
- Data you need to update frequently — rebuilding copies is costly.
- Code supporting < 3.15 → `types.MappingProxyType` (read-only view, not hashable).

## Run
```bash
python3.15 examples.py
```
