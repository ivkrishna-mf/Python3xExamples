# Classes and objects

**Introduced:** classes 1.0 · new-style classes 2.2 (unified in 3.0) · `@classmethod/@staticmethod` 2.2/2.4 · dataclasses 3.7

**In one line:** bundle data (attributes) and behaviour (methods) into your own types.

## What it is
`class` defines a type; `__init__` initialises instances; `self` is the instance.
Class attributes are shared, instance attributes are per object. `@classmethod` receives the
class (alternative constructors), `@staticmethod` receives nothing special.

## When to use
- Modelling entities with state + behaviour (Account, Order, Connection).
- Grouping related functions around shared data.
- `@dataclass` for data-centric classes (less boilerplate).

## When NOT to use
- A class with one method and no state → just a function.
- Pure data with no behaviour → dataclass/NamedTuple/TypedDict.

## Run
```bash
python examples.py
```
