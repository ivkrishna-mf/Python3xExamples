# Python 3.15 · Lazy Imports, frozendict and sentinel
Released October 2026. Explicit `lazy import`, built-in `frozendict` and `sentinel`, unpacking
inside comprehensions (`[*xs for xs in lists]`), UTF-8 as the default encoding, `TypeForm` and
closed TypedDicts, the Tachyon sampling profiler, and many stdlib additions.

| # | Feature | In one line |
|---|---|---|
| 01 | [Explicit lazy imports — Python 3.15 (PEP 810)](01_lazy_imports/README.md) | `lazy import json` keeps the import at the top of the file but loads the module only on first use. |
| 02 | [frozendict built-in — Python 3.15 (PEP 814)](02_frozendict/README.md) | an immutable, hashable dict: `frozendict(host="db", port=5432)`. |
| 03 | [sentinel built-in — Python 3.15 (PEP 661)](03_sentinel/README.md) | `MISSING = sentinel("MISSING")` — a unique marker with a clean repr that works in type hints. |
| 04 | [Unpacking in comprehensions — Python 3.15 (PEP 798)](04_unpacking_in_comprehensions/README.md) | `[*xs for xs in lists]` flattens one level; `{**d for d in dicts}` merges dicts. |
| 05 | [UTF-8 is the default encoding — Python 3.15 (PEP 686)](05_utf8_default_encoding/README.md) | `open("file.txt")` now uses UTF-8 everywhere (including Windows), not the locale encoding. |
| 06 | [TypeForm, closed TypedDicts & disjoint bases — Python 3.15 (PEP 747, 728, 800)](06_typing_typeform_closed_typeddict/README.md) | type "a type expression" as a value, and declare TypedDicts that forbid (or type) extra keys. |
| 07 | [profiling package & Tachyon sampling profiler — Python 3.15 (PEP 799)](07_profiling_sampling_tachyon/README.md) | `python -m profiling.sampling run app.py` profiles with near-zero overhead — even attach to a running PID. |
| 08 | [3.15 stdlib highlights — math.integer, re.prefixmatch, Counter ^, TaskGroup.cancel & more](08_stdlib_highlights/README.md) | many small, practical additions. |

Run every example in this folder:
```bash
python ../../run_examples.py 02_python_versions/py3.15_lazy_imports
```
