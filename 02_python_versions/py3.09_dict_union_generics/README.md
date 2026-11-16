# Python 3.9 · Everyday Conveniences
Dict merge operators, `removeprefix`/`removesuffix`, `list[int]` generics without imports,
the `zoneinfo` time-zone database, `Annotated` metadata and `functools.cache`.

| # | Feature | In one line |
|---|---|---|
| 01 | [Dict merge `\|` and update `\|=` — Python 3.9 (PEP 584)](01_dict_union_operators/README.md) | `merged = defaults \| overrides`; `config \|= extra` updates in place. |
| 02 | [str.removeprefix() / removesuffix() — Python 3.9 (PEP 616)](02_str_removeprefix_removesuffix/README.md) | strip an exact leading/trailing substring — once, and only if it's there. |
| 03 | [Built-in generic types `list[int]` — Python 3.9 (PEP 585)](03_builtin_generic_types/README.md) | use `list[str]`, `dict[str, int]`, `tuple[int, ...]` directly — no `typing.List`. |
| 04 | [zoneinfo — Python 3.9 (PEP 615)](04_zoneinfo/README.md) | real IANA time zones (`ZoneInfo("Asia/Kolkata")`) in the standard library. |
| 05 | [typing.Annotated — Python 3.9 (PEP 593)](05_annotated/README.md) | attach extra metadata to a type: `Annotated[int, Gt(0)]`. |
| 06 | [functools.cache — Python 3.9](06_functools_cache/README.md) | `@cache` = `@lru_cache(maxsize=None)` — simple unbounded memoisation. |

Run every example in this folder:
```bash
python ../../run_examples.py 02_python_versions/py3.09_dict_union_generics
```
