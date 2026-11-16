# Assignment expressions (walrus `:=`) — Python 3.8 (PEP 572)

**In one line:** assign and use a value inside an expression: `if (n := len(data)) > 10:`.

## What it is
`name := expr` evaluates `expr`, binds it to `name` and returns it. Works in `if`, `while`,
comprehensions and function arguments (parenthesise when needed).

## When to use
- `while (chunk := f.read(1024)):` read loops.
- Avoiding a repeated expensive call in a condition + body.
- Comprehensions that filter on a computed value and keep it.
- Regex matching: `if (m := pattern.match(s)):`.

## When NOT to use
- Plain statements — `x = 5` is clearer than `(x := 5)`.
- Deeply nested expressions that hide where a variable came from.

## Run
```bash
python examples.py
```
