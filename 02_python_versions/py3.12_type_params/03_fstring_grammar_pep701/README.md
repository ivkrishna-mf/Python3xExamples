# f-string grammar formalised — Python 3.12 (PEP 701)

**In one line:** f-strings can now reuse the same quotes, contain backslashes, comments and span lines.

## What it is
f-strings are parsed by the real Python grammar. Restrictions removed:
- reuse the outer quote: `f"{d["key"]}"`
- backslashes inside expressions: `f"{'\n'.join(lines)}"`
- multi-line expressions with `#` comments
- arbitrary nesting depth.

## When to use
- Cleaner dict access and joins inside f-strings.
- Long formatted expressions split over multiple lines.

## When NOT to use
- Code that must also run on Python ≤ 3.11 (these forms are SyntaxErrors there).
- Don't cram heavy logic into an f-string — compute it first.

## Run
```bash
python examples.py
```
