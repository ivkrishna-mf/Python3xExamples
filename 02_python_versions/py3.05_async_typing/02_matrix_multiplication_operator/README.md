# The @ matrix multiplication operator — Python 3.5 (PEP 465)

**In one line:** `a @ b` calls `a.__matmul__(b)`; NumPy uses it for matrix products.

## What it is
A dedicated infix operator for matrix multiplication. Python's built-in types don't implement
it, but any class can, via `__matmul__`, `__rmatmul__` and `__imatmul__` (`@=`).

## When to use
- Linear algebra with NumPy / PyTorch / JAX (`X @ W + b`).
- Your own Matrix/Vector/Transform classes where `*` is element-wise.
- Composing transformations (rotation @ scale @ translate).

## When NOT to use
- For unrelated meanings — readers expect "matrix product".

## Run
```bash
python examples.py
```
