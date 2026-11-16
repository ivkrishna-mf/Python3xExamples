# Comprehensions and generator expressions

**Introduced:** list comprehensions 2.0 (PEP 202) · generator expressions 2.4 (PEP 289) · dict/set comprehensions 2.7/3.0 · inlined 3.12 · `*` unpacking 3.15

**In one line:** build lists, dicts, sets or lazy generators from iterables in one readable expression.

## What it is
`[expr for x in it if cond]`, `{k: v for ...}`, `{x for ...}`, `(expr for ...)`.
Generator expressions are lazy — ideal with `sum()`, `any()`, `max()`.

## When to use
- Transform + filter a collection into a new one.
- Feeding aggregations without building a list: `sum(x*x for x in nums)`.

## When NOT to use
- Side effects (printing, appending elsewhere) → use a normal loop.
- More than two `for`s or complex conditions → readability suffers; use a loop/function.

## Run
```bash
python examples.py
```
