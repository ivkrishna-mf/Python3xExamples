# f-strings (formatted string literals) — Python 3.6 (PEP 498)

**In one line:** `f"Hello {name}!"` — embed expressions directly in string literals.

## What it is
Expressions inside `{}` are evaluated at runtime and formatted with the format-spec
mini-language (`{x:>10}`, `{n:,}`, `{pct:.1%}`, `{dt:%Y-%m-%d}`). 3.8 added `{x=}` and 3.12
lifted most grammar limits (see those folders).

## When to use
- Almost all string formatting in modern Python: messages, reports, file names.
- Number/date formatting with format specs.

## When NOT to use
- Logging calls: prefer `log.info("x=%s", x)` so formatting is lazy.
- Building SQL/shell/HTML from user input — use parameters/escaping (or t-strings, 3.14).
- Translatable UI strings (need templates, not code).

## Run
```bash
python examples.py
```
