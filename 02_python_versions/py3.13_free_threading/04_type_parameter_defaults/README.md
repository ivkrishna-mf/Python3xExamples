# Type parameter defaults — Python 3.13 (PEP 696)

**In one line:** `class Box[T = int]:` — a generic parameter falls back to a default when not specified.

## What it is
TypeVar, ParamSpec and TypeVarTuple can have defaults, both in the 3.12 bracket syntax and
via `TypeVar("T", default=int)`. Unparameterised uses (`Box`) mean `Box[int]` to checkers.

## When to use
- Generic classes where one type is overwhelmingly common (`Response[T = dict]`).
- Evolving a class to generic without breaking existing un-parameterised annotations.
- Generators/coroutines style multi-param generics where later params are often unused.

## When NOT to use
- When there is no obvious default — forcing users to choose is clearer.

## Run
```bash
python examples.py
```
