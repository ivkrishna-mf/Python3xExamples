# Python 3.4 · Batteries Upgrade
Object-oriented paths, real enumerations, a statistics module and single-dispatch
generic functions. (asyncio also arrived here; see 3.5 for async/await.)

| # | Feature | In one line |
|---|---|---|
| 01 | [pathlib — Python 3.4 (PEP 428)](01_pathlib/README.md) | filesystem paths as objects: `Path("data") / "file.csv"`. |
| 02 | [enum — Python 3.4 (PEP 435) · plus Flag/auto (3.6) and StrEnum (3.11)](02_enum/README.md) | a fixed set of named constants with identity, iteration and type safety. |
| 03 | [statistics — Python 3.4 (PEP 450) · grown through 3.8 / 3.10 / 3.13](03_statistics/README.md) | mean, median, mode, stdev, quantiles, correlation… without NumPy. |
| 04 | [functools.singledispatch — Python 3.4 (PEP 443)](04_singledispatch/README.md) | one function name, different implementations chosen by the type of the first argument. |

Run every example in this folder:
```bash
python ../../run_examples.py 02_python_versions/py3.04_pathlib_enum
```
