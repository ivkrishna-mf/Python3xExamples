# Keyword-only arguments — Python 3.0 (PEP 3102)

**In one line:** parameters after `*` (or `*args`) can only be passed by name.

## What it is
`def f(a, *, flag=False)` means `flag` must be written as `flag=True`. This makes call
sites self-documenting and lets you add/reorder options without breaking callers.

## When to use
- Boolean flags and options: `sort(items, *, reverse=False)`.
- Functions with many optional settings.
- Public APIs you expect to evolve.

## When NOT to use
- For the one or two "obvious" main inputs — keep those positional.

## Run
```bash
python examples.py
```
