# Variable annotations — Python 3.6 (PEP 526)

**In one line:** `count: int = 0` — annotate variables and class attributes, not just functions.

## What it is
Annotations on variables are stored in `__annotations__` (for modules/classes) and are used by
type checkers, `dataclasses`, `typing.NamedTuple`, `TypedDict`, pydantic, etc.

## When to use
- Declaring fields of dataclasses / NamedTuples / TypedDicts / ORM models.
- Clarifying the type of an empty container: `cache: dict[str, int] = {}`.
- Declaring instance attributes in the class body for readers and checkers.
- `ClassVar` to mark class-level constants.

## When NOT to use
- Annotating every obvious local (`x: int = 5`) adds noise.

## Run
```bash
python examples.py
```
