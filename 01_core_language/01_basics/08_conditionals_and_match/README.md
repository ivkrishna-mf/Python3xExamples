# Conditionals: if / elif / else, conditional expressions, match

**Introduced:** if/elif 1.0 · `x if c else y` 2.5 · `match` 3.10 · walrus 3.8

**In one line:** branch on conditions; use `match` when you branch on the *shape* of data.

## What it is
`if/elif/else`, chained comparisons (`0 < x < 10`), boolean operators `and/or/not`
(short-circuit, return operands), conditional expressions, and structural `match/case`.

## When to use
- `if` for boolean conditions and ranges.
- Conditional expression for short value choices.
- `match` for commands, tagged data, JSON shapes, enums.
- A dict lookup instead of long equality chains mapping values to values.

## When NOT to use
- Deeply nested ifs → use early returns / guard clauses.

## Run
```bash
python examples.py
```
