# Typed **kwargs with Unpack[TypedDict] — Python 3.12 (PEP 692)

**In one line:** `def f(**kw: Unpack[Options])` gives each keyword argument its own type.

## What it is
Previously `**kwargs: int` meant *all* values are ints. With `Unpack[SomeTypedDict]` each
key has its own type, and `NotRequired` keys are optional.

## When to use
- Wrapper functions that forward many options (HTTP clients, plotting, DB helpers).
- APIs with many optional keyword-only settings shared between functions.

## When NOT to use
- A handful of explicit keyword-only parameters is simpler and clearer.

## Run
```bash
python examples.py
```
