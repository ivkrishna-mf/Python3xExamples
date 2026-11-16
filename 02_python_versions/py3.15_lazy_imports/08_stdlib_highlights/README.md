# 3.15 stdlib highlights — math.integer, re.prefixmatch, Counter ^, TaskGroup.cancel & more

**In one line:** many small, practical additions.

## What it is
- `math.integer` module (PEP 791): `gcd`, `lcm`, `isqrt`, `comb`, `perm`, `factorial`.
- `math.isnormal`, `issubnormal`, `fmax`, `fmin`, `signbit`.
- `re.prefixmatch()` — clearer name for `re.match()` (which is now soft-deprecated).
- `collections.Counter` supports `^` (symmetric difference).
- `bytearray.take_bytes(n)` — take bytes out of a buffer without copying.
- `asyncio.TaskGroup.cancel()` — stop a whole task group early.
- `json.loads(..., array_hook=...)`, `os.makedirs(parent_mode=...)`, `base64`/`binascii`
  additions, colourful REPL tab completion.

## When to use
- Integer maths in a dedicated namespace; IEEE float classification.
- Self-documenting regex calls (`prefixmatch` vs `search` vs `fullmatch`).
- Network/protocol buffers (`take_bytes`), early-exit concurrent searches (`TaskGroup.cancel`).

## Run
```bash
python3.15 examples.py
```
