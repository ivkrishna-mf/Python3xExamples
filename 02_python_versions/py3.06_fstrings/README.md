# Python 3.6 · Readability Wins
f-strings, variable annotations, `1_000_000` literals, async generators/comprehensions,
simpler class customisation hooks and the `secrets` module. Dicts became insertion-ordered
as an implementation detail (guaranteed in 3.7).

| # | Feature | In one line |
|---|---|---|
| 01 | [f-strings (formatted string literals) — Python 3.6 (PEP 498)](01_f_strings/README.md) | `f"Hello {name}!"` — embed expressions directly in string literals. |
| 02 | [Variable annotations — Python 3.6 (PEP 526)](02_variable_annotations/README.md) | `count: int = 0` — annotate variables and class attributes, not just functions. |
| 03 | [Underscores in numeric literals — Python 3.6 (PEP 515)](03_underscores_in_numeric_literals/README.md) | write `1_000_000` instead of `1000000` for readability. |
| 04 | [Async generators & async comprehensions — Python 3.6 (PEP 525, PEP 530)](04_async_generators_and_comprehensions/README.md) | `yield` inside `async def`, and `[x async for x in aiter()]` / `await` in comprehensions. |
| 05 | [__init_subclass__ and __set_name__ — Python 3.6 (PEP 487)](05_init_subclass_and_set_name/README.md) | customise subclass creation and descriptors without writing a metaclass. |
| 06 | [secrets — Python 3.6 (PEP 506)](06_secrets/README.md) | cryptographically strong random tokens, passwords and choices. |

Run every example in this folder:
```bash
python ../../run_examples.py 02_python_versions/py3.06_fstrings
```
