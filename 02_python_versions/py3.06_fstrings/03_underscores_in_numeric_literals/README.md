# Underscores in numeric literals — Python 3.6 (PEP 515)

**In one line:** write `1_000_000` instead of `1000000` for readability.

## What it is
Single underscores are allowed between digits in int, float, complex, hex, octal and binary
literals, and as a thousands separator in format specs (`f"{n:_}"`).

## When to use
- Large constants: sizes, timeouts, money in cents, limits.
- Bit masks in binary/hex grouped by nibble/byte.

## When NOT to use
- In user-facing output where locale formatting is expected (use `f"{n:,}"` / `locale`).

## Run
```bash
python examples.py
```
