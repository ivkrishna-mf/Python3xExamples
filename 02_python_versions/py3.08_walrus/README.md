# Python 3.8 · Expressive Syntax
The walrus operator, positional-only parameters, `f"{x=}"`, structural typing with
`Protocol`, `TypedDict`/`Final`/`Literal`, and `functools.cached_property`.

| # | Feature | In one line |
|---|---|---|
| 01 | [Assignment expressions (walrus `:=`) — Python 3.8 (PEP 572)](01_walrus_operator/README.md) | assign and use a value inside an expression: `if (n := len(data)) > 10:`. |
| 02 | [Positional-only parameters `/` — Python 3.8 (PEP 570)](02_positional_only_parameters/README.md) | parameters before `/` can't be passed by keyword. |
| 03 | [f-string `=` specifier — Python 3.8](03_fstring_self_documenting/README.md) | `f"{x=}"` prints `x=42` — the expression text *and* its value. |
| 04 | [TypedDict, Final and Literal — Python 3.8 (PEP 589, 591, 586)](04_typeddict_final_literal/README.md) | precise types for dict shapes, constants and allowed literal values. |
| 05 | [Protocols (structural subtyping) — Python 3.8 (PEP 544)](05_protocols/README.md) | "if it has these methods, it fits" — static duck typing without inheritance. |
| 06 | [functools.cached_property — Python 3.8](06_cached_property/README.md) | a property computed once per instance, then stored as a normal attribute. |

Run every example in this folder:
```bash
python ../../run_examples.py 02_python_versions/py3.08_walrus
```
