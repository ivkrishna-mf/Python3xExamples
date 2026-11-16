# statistics — Python 3.4 (PEP 450) · grown through 3.8 / 3.10 / 3.13

**In one line:** mean, median, mode, stdev, quantiles, correlation… without NumPy.

## What it is
A pure-Python module for basic descriptive statistics with correct numerics
(works with `Fraction` and `Decimal`). Later versions added `fmean`, `quantiles`,
`NormalDist` (3.8), `correlation`/`linear_regression` (3.10) and `kde` (3.13).

## When to use
- Small/medium datasets in scripts, reports, tests, CLI tools.
- When you don't want a heavy dependency like NumPy/pandas.

## When NOT to use
- Large arrays or vectorised math → NumPy / pandas / polars are much faster.

## Run
```bash
python examples.py
```
