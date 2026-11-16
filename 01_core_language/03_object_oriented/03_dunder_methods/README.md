# Special ("dunder") methods and operator overloading

**Introduced:** 1.0 onward · rich comparisons 2.1 · `__format__` 2.6 · `__matmul__` 3.5 · `__class_getitem__` 3.7

**In one line:** implement `__len__`, `__eq__`, `__add__`, `__iter__`, `__getitem__`, `__call__`… so your objects work with Python syntax and built-ins.

## What it is
Python calls special methods behind operators and built-ins: `len(x)` → `x.__len__()`,
`a + b` → `a.__add__(b)`, `x[i]` → `__getitem__`, `with` → `__enter__/__exit__`,
`for` → `__iter__`, `str()`/`repr()` → `__str__/__repr__`.

## When to use
- Value types (Money, Vector, Matrix) that should support operators.
- Container-like classes (support `len`, indexing, iteration, `in`).
- Always implement a helpful `__repr__`.

## When NOT to use
- Operators with surprising meanings — keep semantics intuitive.

## Run
```bash
python examples.py
```
