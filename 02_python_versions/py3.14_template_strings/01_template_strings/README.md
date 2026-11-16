# Template strings (t-strings) — Python 3.14 (PEP 750)

**In one line:** `t"Hello {name}"` gives you a `Template` object (strings + interpolations) instead of a finished `str`.

## What it is
Like an f-string, but *not* joined. You get `string.templatelib.Template` with `.strings` and
`.interpolations` (each with `.value`, `.expression`, `.conversion`, `.format_spec`). Your code
decides how to combine them — escape HTML, parameterise SQL, build structured logs, etc.

## When to use
- Safe HTML/SQL/shell building where user values must be escaped or parameterised.
- Structured logging (keep values separate from the message).
- DSLs and i18n where you need the parts, not the final string.

## When NOT to use
- Ordinary formatting → f-strings are simpler (a Template has no `__str__` join).
- Code supporting < 3.14.

## Run
```bash
python examples.py
```
