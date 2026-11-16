# contextvars — Python 3.7 (PEP 567)

**In one line:** "thread-local" state that also works correctly across asyncio tasks.

## What it is
A `ContextVar` holds a value per execution context. Each asyncio task gets a copy of the
context, so a request ID set in one task does not leak into another. `token = var.set(x)` /
`var.reset(token)` restores previous values.

## When to use
- Request IDs / correlation IDs / current user in async web servers and logs.
- Per-request DB sessions, locale, tenant, feature flags.
- Any implicit "current X" state in async code (replacement for `threading.local`).

## When NOT to use
- Passing data explicitly as arguments is clearer — prefer that when practical.
- Global configuration that never changes per request.

## Run
```bash
python examples.py
```
