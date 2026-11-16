# Type parameter syntax — Python 3.12 (PEP 695)

**In one line:** declare generics inline: `def first[T](xs: list[T]) -> T` and `class Stack[T]:`.

## What it is
No more `T = TypeVar("T")` boilerplate. Type parameters are scoped to the function/class.
Bounds: `[T: str]`; constraints: `[T: (int, float)]`; ParamSpec: `[**P]`; TypeVarTuple:
`[*Ts]`. 3.13 adds defaults: `[T = int]`.

## When to use
- All new generic functions and classes on 3.12+.
- Decorators with `[**P, R]`.

## When NOT to use
- Libraries that must support Python < 3.12 — keep `TypeVar`.

## Run
```bash
python examples.py
```
