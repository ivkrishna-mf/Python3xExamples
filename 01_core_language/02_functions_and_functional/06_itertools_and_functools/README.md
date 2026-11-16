# itertools and functools toolkits

**Introduced:** itertools 2.3 · functools 2.5 · `accumulate` 3.2 · `pairwise` 3.10 · `batched` 3.12 · `cache` 3.9

**In one line:** fast, composable building blocks for iteration and function manipulation.

## What it is
- itertools: `chain`, `islice`, `groupby`, `accumulate`, `product`, `permutations`,
  `combinations`, `count`, `cycle`, `zip_longest`, `takewhile`, `pairwise`, `batched`.
- functools: `cache`, `lru_cache`, `partial`, `reduce`, `wraps`, `total_ordering`,
  `singledispatch`, `cached_property`.

## When to use
- Combinatorics, grouping sorted data, running totals, chunking, lazy slicing.
- Reducing boilerplate in classes (`total_ordering`) and functions (`partial`, `cache`).

## When NOT to use
- When a plain loop is clearer for your team.

## Run
```bash
python examples.py
```
