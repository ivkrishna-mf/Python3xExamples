# Python 3.11 · Faster CPython and Better Errors
10–60% faster interpreter, fine-grained error locations in tracebacks, exception groups and
`except*`, exception notes, `tomllib`, `asyncio.TaskGroup`/`timeout`, and new typing features
(`Self`, `LiteralString`, `TypeVarTuple`, `Required`/`NotRequired`).

| # | Feature | In one line |
|---|---|---|
| 01 | [ExceptionGroup and `except*` — Python 3.11 (PEP 654)](01_exception_groups_except_star/README.md) | raise and handle *several* unrelated exceptions at once. |
| 02 | [Exception notes `add_note()` — Python 3.11 (PEP 678)](02_exception_notes/README.md) | attach extra context to an exception without changing its type or message. |
| 03 | [tomllib — Python 3.11 (PEP 680)](03_tomllib/README.md) | read TOML files (like `pyproject.toml`) with the standard library. |
| 04 | [typing.Self and LiteralString — Python 3.11 (PEP 673, 675)](04_self_and_literalstring/README.md) | `-> Self` for methods returning their own class; `LiteralString` to guard against injection. |
| 05 | [asyncio.TaskGroup and asyncio.timeout — Python 3.11](05_asyncio_taskgroup_and_timeout/README.md) | structured concurrency — start tasks in a block; if one fails, the rest are cancelled. |
| 06 | [Variadic generics — TypeVarTuple & Unpack — Python 3.11 (PEP 646)](06_variadic_generics_typevartuple/README.md) | generics over an *arbitrary number* of types — e.g. array shapes or tuple-like records. |
| 07 | [TypedDict Required / NotRequired — Python 3.11 (PEP 655)](07_typeddict_required_notrequired/README.md) | mark individual TypedDict keys as optional (or required) without splitting classes. |

Run every example in this folder:
```bash
python ../../run_examples.py 02_python_versions/py3.11_exception_groups
```
