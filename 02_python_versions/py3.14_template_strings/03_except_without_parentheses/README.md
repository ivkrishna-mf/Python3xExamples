# `except A, B:` without parentheses — Python 3.14 (PEP 758)

**In one line:** catch several exception types without wrapping them in a tuple — when you don't use `as`.

## What it is
`except ValueError, TypeError:` is now valid (also for `except*`). With `as name` you must still
write parentheses: `except (ValueError, TypeError) as exc:`.

## When to use
- Short handlers that don't need the exception object.

## When NOT to use
- Code that must run on Python < 3.14 (SyntaxError there — in Python 2 this syntax meant
  something totally different!).
- When you need the exception → parentheses + `as` are required.

## Run
```bash
python examples.py
```
