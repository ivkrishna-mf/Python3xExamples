# Python 3.5 · Async and Typing Arrive
Native coroutines with `async`/`await`, the `@` matrix operator, generalised `*`/`**`
unpacking and the `typing` module.

| # | Feature | In one line |
|---|---|---|
| 01 | [async / await — Python 3.5 (PEP 492) · asyncio.run 3.7](01_async_await/README.md) | write concurrent I/O code that reads like sequential code. |
| 02 | [The @ matrix multiplication operator — Python 3.5 (PEP 465)](02_matrix_multiplication_operator/README.md) | `a @ b` calls `a.__matmul__(b)`; NumPy uses it for matrix products. |
| 03 | [Additional unpacking generalisations — Python 3.5 (PEP 448)](03_unpacking_generalizations/README.md) | use `*` and `**` multiple times in calls and inside list/tuple/set/dict displays. |
| 04 | [Type hints and the typing module — Python 3.5 (PEP 484)](04_type_hints_typing/README.md) | annotate parameters and return values so tools (mypy, pyright, IDEs) can check your code. |

Run every example in this folder:
```bash
python ../../run_examples.py 02_python_versions/py3.05_async_typing
```
