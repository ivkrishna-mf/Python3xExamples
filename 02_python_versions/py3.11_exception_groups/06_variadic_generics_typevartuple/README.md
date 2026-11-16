# Variadic generics — TypeVarTuple & Unpack — Python 3.11 (PEP 646)

**In one line:** generics over an *arbitrary number* of types — e.g. array shapes or tuple-like records.

## What it is
`Ts = TypeVarTuple("Ts")` stands for zero or more types. Use `*Ts` (or `Unpack[Ts]`) inside
`tuple[...]`, `Generic[...]` or `*args: *Ts`. 3.12 lets you write `class Array[*Shape]:`.

## When to use
- Tensor/array libraries typing shapes (`Array[Batch, Height, Width]`).
- Functions that forward or transform heterogeneous tuples.
- Typed `*args` where each position has its own type.

## When NOT to use
- Simple homogeneous sequences → `tuple[int, ...]` / `list[T]`.

## Run
```bash
python examples.py
```
