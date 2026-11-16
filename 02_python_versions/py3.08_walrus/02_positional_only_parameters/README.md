# Positional-only parameters `/` — Python 3.8 (PEP 570)

**In one line:** parameters before `/` can't be passed by keyword.

## What it is
`def f(a, b, /, c, *, d)` → `a`,`b` positional-only, `c` either, `d` keyword-only.
Mirrors how many built-ins behave (`len(obj)`, `pow(x, y)`).

## When to use
- Library APIs where parameter *names* are an implementation detail you may rename later.
- Functions where a keyword name would read badly (`distance(p1, p2)`).
- Allowing `**kwargs` to accept any key, even one that clashes with a parameter name.

## When NOT to use
- Functions with many parameters or optional flags — keywords improve readability there.

## Run
```bash
python examples.py
```
