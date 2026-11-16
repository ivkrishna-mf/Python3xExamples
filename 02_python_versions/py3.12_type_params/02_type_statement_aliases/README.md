# The `type` statement — Python 3.12 (PEP 695)

**In one line:** `type Vector = list[float]` creates a lazily evaluated, possibly generic type alias.

## What it is
`type Name = expr` creates a `typing.TypeAliasType`. The value is evaluated lazily, so aliases
can be recursive (`type Json = dict[str, Json] | ...`) and generic (`type Pair[T] = tuple[T, T]`).

## When to use
- Naming complex unions/callables/dict shapes used throughout a codebase.
- Recursive types (JSON, trees).
- Generic aliases.

## When NOT to use
- When you need a *distinct* type for the checker → `NewType`.
- Runtime `isinstance` with the alias (use `Alias.__value__` if you must).
- Code supporting Python < 3.12.

## Run
```bash
python examples.py
```
