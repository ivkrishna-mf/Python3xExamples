# Strings

**Introduced:** str 1.0 · string methods 1.6/2.0 · Unicode-by-default 3.0 · `str.format` 2.6 · f-strings 3.6 · `removeprefix` 3.9

**In one line:** immutable Unicode text with rich methods, slicing and f-string formatting.

## What it is
Strings are sequences of Unicode code points. Use f-strings for formatting, `join` for
building from parts, slicing for substrings and methods like `split`, `strip`, `replace`,
`startswith`, `casefold`.

## When to use
- f-strings for formatting; `"sep".join(parts)` for concatenating many pieces.
- `casefold()` for case-insensitive comparisons.
- Triple-quoted strings for multi-line text; raw strings `r"..."` for regex/Windows paths.

## When NOT to use
- `+=` in a loop for large strings (quadratic) → collect in a list and `join`.
- `%`-formatting / `.format()` in new code (except logging & templates).

## Run
```bash
python examples.py
```
