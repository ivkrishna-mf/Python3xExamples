# Python 3.13 · Free-threading Preview and a New REPL
A colourful multi-line REPL, an experimental free-threaded (no-GIL) build and JIT, plus
`@warnings.deprecated`, `TypeIs`, `ReadOnly` TypedDict keys, type-parameter defaults and
`copy.replace()`. `locals()` semantics were defined precisely (PEP 667).

| # | Feature | In one line |
|---|---|---|
| 01 | [@warnings.deprecated — Python 3.13 (PEP 702)](01_deprecated_decorator/README.md) | mark functions/classes/overloads as deprecated — warns at runtime *and* in type checkers/IDEs. |
| 02 | [typing.TypeIs — Python 3.13 (PEP 742)](02_typeis_narrowing/README.md) | a user-defined type guard that narrows in *both* the `if` and the `else` branch. |
| 03 | [ReadOnly TypedDict keys — Python 3.13 (PEP 705)](03_readonly_typeddict/README.md) | `ReadOnly[str]` marks a TypedDict key that type checkers won't let you modify. |
| 04 | [Type parameter defaults — Python 3.13 (PEP 696)](04_type_parameter_defaults/README.md) | `class Box[T = int]:` — a generic parameter falls back to a default when not specified. |
| 05 | [copy.replace() — Python 3.13](05_copy_replace/README.md) | one function to make a modified copy of dataclasses, namedtuples, datetimes and more. |
| 06 | [Free-threaded CPython (no GIL) & JIT — Python 3.13 (PEP 703, 744) · supported in 3.14 (PEP 779)](06_free_threading_and_jit/README.md) | an optional `python3.13t` / `python3.14t` build lets threads run Python code truly in parallel. |

Run every example in this folder:
```bash
python ../../run_examples.py 02_python_versions/py3.13_free_threading
```
