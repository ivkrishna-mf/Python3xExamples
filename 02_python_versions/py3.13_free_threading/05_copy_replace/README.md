# copy.replace() — Python 3.13

**In one line:** one function to make a modified copy of dataclasses, namedtuples, datetimes and more.

## What it is
`copy.replace(obj, **changes)` calls `obj.__replace__(**changes)`. Supported by dataclasses,
`namedtuple`, `datetime`/`date`/`time`, `inspect.Signature`/`Parameter`, `SimpleNamespace`,
code objects — and your own classes if they define `__replace__`.

## When to use
- Immutable / frozen objects: create an updated copy.
- Generic code that "updates" objects without knowing their concrete type.

## When NOT to use
- Deep modification of nested structures (it's a shallow copy).
- Code supporting < 3.13 → `dataclasses.replace` / `nt._replace` / `dt.replace`.

## Run
```bash
python examples.py
```
