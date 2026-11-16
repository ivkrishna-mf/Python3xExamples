# Type hints and the typing module — Python 3.5 (PEP 484)

**In one line:** annotate parameters and return values so tools (mypy, pyright, IDEs) can check your code.

## What it is
Function annotations (3.0) got standard meaning in 3.5 with `typing`: `Optional`, `Union`,
`Callable`, `TypeVar`, `Generic`, `NewType`, `overload`… Python itself does **not** enforce
them at runtime — they are for tools and readers. Later versions simplified the syntax
(`list[int]` in 3.9, `X | Y` in 3.10, `class Box[T]` in 3.12).

## When to use
- Libraries and any code shared by a team.
- Larger codebases where refactoring safety matters.
- Public functions and data models (they double as documentation).

## When NOT to use
- Don't expect runtime validation — use pydantic/attrs/`isinstance` for that.
- Don't over-engineer types for throwaway scripts.

## Run
```bash
python examples.py
mypy examples.py   # optional: see a type checker in action
```
