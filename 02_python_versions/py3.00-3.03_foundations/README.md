# Python 3.0 – 3.3 · The Foundations
The big break from Python 2: text vs bytes, print as a function, keyword-only
arguments, `nonlocal`, extended unpacking, exception chaining and `yield from`.
Everything here works on every modern Python 3.

| # | Feature | In one line |
|---|---|---|
| 01 | [print() as a function — Python 3.0 (PEP 3105)](01_print_function/README.md) | `print` is a normal function with `sep`, `end`, `file` and `flush` keywords. |
| 02 | [Text (str) vs binary (bytes) — Python 3.0 (PEP 3137)](02_str_vs_bytes/README.md) | `str` is Unicode text, `bytes` is raw binary; you convert explicitly with `encode()`/`decode()`. |
| 03 | [Keyword-only arguments — Python 3.0 (PEP 3102)](03_keyword_only_args/README.md) | parameters after `*` (or `*args`) can only be passed by name. |
| 04 | [Extended iterable unpacking — Python 3.0 (PEP 3132)](04_extended_unpacking/README.md) | `first, *rest = items` collects "everything else" into a list. |
| 05 | [nonlocal — Python 3.0 (PEP 3104)](05_nonlocal/README.md) | lets a nested function *rebind* a variable from its enclosing function. |
| 06 | [Exception chaining — Python 3.0 / 3.3 (PEP 3134, PEP 409, PEP 415)](06_exception_chaining/README.md) | `raise NewError(...) from original` keeps the root cause; `from None` hides it. |
| 07 | [yield from — Python 3.3 (PEP 380)](07_yield_from/README.md) | delegate part of a generator's work to another iterable or sub-generator. |
| 08 | [functools.lru_cache — Python 3.2](08_lru_cache/README.md) | memoise a pure function's results with a bounded, least-recently-used cache. |

Run every example in this folder:
```bash
python ../../run_examples.py 02_python_versions/py3.00-3.03_foundations
```
