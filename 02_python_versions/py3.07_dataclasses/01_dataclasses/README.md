# dataclasses — Python 3.7 (PEP 557) · kw_only/slots/match_args 3.10

**In one line:** `@dataclass` writes `__init__`, `__repr__`, `__eq__` (and more) from annotated fields.

## What it is
Annotate fields in a class body; the decorator generates the boilerplate. Options:
`frozen=True` (immutable), `order=True` (comparisons), `slots=True` (3.10, less memory),
`kw_only=True` (3.10), `field(default_factory=...)`, `__post_init__` for validation.

## When to use
- Plain data containers: DTOs, config objects, records, value objects, events.
- Anything you'd otherwise write `__init__`/`__repr__`/`__eq__` for by hand.
- Immutable, hashable keys with `frozen=True`.

## When NOT to use
- You need heavy validation/parsing from untrusted input → pydantic / attrs.
- Behaviour-rich objects where the data is incidental.
- Simple fixed tuples → `NamedTuple`.

## Run
```bash
python examples.py
```
