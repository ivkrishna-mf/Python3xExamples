# Lambdas and higher-order functions (map, filter, sorted, reduce, partial)

**Introduced:** lambda/map/filter/reduce 1.0 · `functools.reduce` 3.0 · `partial` 2.5 · `operator` module 1.x

**In one line:** pass functions as arguments; use small anonymous `lambda`s for one-off keys and callbacks.

## What it is
A higher-order function takes or returns functions. `lambda args: expr` creates a small
function. `sorted(key=)`, `min/max(key=)`, `map`, `filter`, `functools.reduce`, `partial` and
`operator.itemgetter/attrgetter` are the main tools.

## When to use
- `key=` functions for sorting/grouping.
- Callbacks and strategies.
- `partial` to pre-fill arguments.

## When NOT to use
- `map/filter` with lambdas → a comprehension is usually more readable.
- Multi-line logic → use `def` (lambdas can't hold statements).
- Assigning a lambda to a name (`f = lambda x: ...`) → use `def`.

## Run
```bash
python examples.py
```
