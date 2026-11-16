# Functions and arguments

**Introduced:** def 1.0 · default/keyword args 1.0 · `*args/**kwargs` 1.x · keyword-only 3.0 · annotations 3.0 · positional-only `/` 3.8

**In one line:** reusable blocks of code with positional, keyword, default, variadic, keyword-only and positional-only parameters.

## What it is
`def name(pos, /, normal, *args, kw_only, **kwargs) -> ReturnType:`. Functions are objects:
they can be stored, passed and returned. Docstrings document them; `return` without a value
returns `None`.

## When to use
- Any logic used more than once, or that deserves a name.
- Keyword-only arguments for options/flags; `/` for API-stable positional params.
- Type hints and docstrings on public functions.

## When NOT to use
- Mutable defaults (`def f(x=[])`) → use `None` and create inside.
- Functions with 6+ parameters → group into a dataclass/config object.

## Run
```bash
python examples.py
```
