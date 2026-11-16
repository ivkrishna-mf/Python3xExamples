# Structural pattern matching `match`/`case` — Python 3.10 (PEP 634, 635, 636)

**In one line:** match the *shape* of data (sequences, mappings, classes) and destructure it in one go.

## What it is
`match subject:` tries each `case pattern:` in order. Patterns can be literals, captures,
wildcards (`_`), sequences (`[x, *rest]`), mappings (`{"type": "click", **rest}`), class
patterns (`Point(x=0)`), alternatives (`|`), captures with `as`, and guards (`if cond`).

## When to use
- Parsing commands, tokens, AST nodes, protocol messages.
- Handling JSON/event payloads with different shapes.
- State machines and interpreters.
- Replacing long `if/elif` chains that inspect structure (not just equality).

## When NOT to use
- Simple value lookups → a dict is faster and clearer.
- A plain `if x == 1 / elif x == 2` with no destructuring.
- Note: `case NAME:` *captures* — to compare against a constant use a dotted name
  (`Color.RED`) or a literal.

## Run
```bash
python examples.py
```
