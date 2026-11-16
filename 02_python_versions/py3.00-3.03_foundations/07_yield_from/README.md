# yield from — Python 3.3 (PEP 380)

**In one line:** delegate part of a generator's work to another iterable or sub-generator.

## What it is
`yield from sub` yields every value of `sub`, forwards `send()`/`throw()` to it, and evaluates
to the sub-generator's `return` value.

## When to use
- Flattening / chaining iterables inside a generator.
- Recursive generators (tree walks, nested structures).
- Splitting a big generator into smaller composable pieces.
- Capturing a sub-generator's return value.

## When NOT to use
- For async code — use `async`/`await` (3.5+) instead of generator-based coroutines.
- When `itertools.chain` is simpler.

## Run
```bash
python examples.py
```
