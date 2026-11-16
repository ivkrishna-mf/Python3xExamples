# Unpacking in comprehensions — Python 3.15 (PEP 798)

**In one line:** `[*xs for xs in lists]` flattens one level; `{**d for d in dicts}` merges dicts.

## What it is
`*` and `**` are allowed as the element of list/set/dict comprehensions and generator
expressions. `[*L for L in lists]` == `[x for L in lists for x in L]`. Works with async
comprehensions too.

## When to use
- Flattening a list of lists/tuples/sets one level.
- Merging many dicts (later wins) in one expression.
- Building a set from many iterables.

## When NOT to use
- Deep (recursive) flattening — write a generator.
- Code supporting < 3.15 → nested `for` comprehension or `itertools.chain.from_iterable`.

## Run
```bash
python3.15 examples.py
```
