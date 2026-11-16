# tomllib — Python 3.11 (PEP 680)

**In one line:** read TOML files (like `pyproject.toml`) with the standard library.

## What it is
`tomllib.load(binary_file)` / `tomllib.loads(text)` return plain dicts. Read-only: use
`tomli-w` or similar to *write* TOML.

## When to use
- Reading `pyproject.toml` and application config files.
- Replacing INI (`configparser`) when you want typed values: ints, bools, dates, arrays, tables.

## When NOT to use
- Writing TOML (not supported).
- Untrusted huge files from the network without size limits.

## Run
```bash
python examples.py
```
