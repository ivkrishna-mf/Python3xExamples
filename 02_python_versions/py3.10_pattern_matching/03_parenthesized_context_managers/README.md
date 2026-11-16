# Parenthesised context managers — Python 3.10

**In one line:** spread several `with` items over multiple lines inside parentheses.

## What it is
```python
with (
    open("in.txt") as src,
    open("out.txt", "w") as dst,
):
    ...
```
Officially supported in 3.10 thanks to the new PEG parser; trailing commas allowed.

## When to use
- Opening several files/locks/connections together.
- Tests that patch multiple objects with `unittest.mock.patch`.
- Any `with` statement too long for one line.

## When NOT to use
- A dynamic/unknown number of managers → `contextlib.ExitStack`.

## Run
```bash
python examples.py
```
