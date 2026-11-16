# Built-in generic types `list[int]` — Python 3.9 (PEP 585)

**In one line:** use `list[str]`, `dict[str, int]`, `tuple[int, ...]` directly — no `typing.List`.

## What it is
Standard collections (and many stdlib classes such as `collections.deque`,
`collections.abc.Callable`, `re.Pattern`) became subscriptable for type hints.
The `typing.List/Dict/...` aliases are deprecated.

## When to use
- All new type hints on Python 3.9+.
- Abstract types from `collections.abc` (`Iterable[int]`, `Mapping[str, Any]`, `Callable[...]`).

## When NOT to use
- Code supporting 3.8 or older (unless you add `from __future__ import annotations`).

## Run
```bash
python examples.py
```
