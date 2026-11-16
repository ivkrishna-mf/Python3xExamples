# Python 3.10 · Pattern Matching
`match`/`case`, `int | None` union syntax, parenthesised context managers, `ParamSpec`,
`TypeAlias`, `TypeGuard`, `zip(strict=True)` and `itertools.pairwise`. Error messages also got
much more precise ("Did you mean…?").

| # | Feature | In one line |
|---|---|---|
| 01 | [Structural pattern matching `match`/`case` — Python 3.10 (PEP 634, 635, 636)](01_structural_pattern_matching/README.md) | match the *shape* of data (sequences, mappings, classes) and destructure it in one go. |
| 02 | [Union types with `X \| Y` — Python 3.10 (PEP 604)](02_union_type_operator/README.md) | write `int \| None` instead of `Optional[int]`, `int \| str` instead of `Union[int, str]`. |
| 03 | [Parenthesised context managers — Python 3.10](03_parenthesized_context_managers/README.md) | spread several `with` items over multiple lines inside parentheses. |
| 04 | [ParamSpec, Concatenate, TypeAlias, TypeGuard — Python 3.10 (PEP 612, 613, 647)](04_paramspec_typealias_typeguard/README.md) | type decorators precisely, name complex types, and write type-narrowing helpers. |
| 05 | [zip(strict=True), itertools.pairwise & friends — Python 3.10 (PEP 618)](05_zip_strict_pairwise_and_more/README.md) | catch length mismatches in `zip`, iterate over consecutive pairs, plus small 3.10 helpers. |

Run every example in this folder:
```bash
python ../../run_examples.py 02_python_versions/py3.10_pattern_matching
```
