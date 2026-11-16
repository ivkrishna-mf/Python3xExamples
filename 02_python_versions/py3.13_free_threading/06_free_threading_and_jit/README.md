# Free-threaded CPython (no GIL) & JIT — Python 3.13 (PEP 703, 744) · supported in 3.14 (PEP 779)

**In one line:** an optional `python3.13t` / `python3.14t` build lets threads run Python code truly in parallel.

## What it is
- The free-threaded build disables the Global Interpreter Lock, so CPU-bound threads can use
  all cores. Experimental in 3.13, officially supported (phase II) in 3.14.
  Check with `sys._is_gil_enabled()`; control with `PYTHON_GIL=0/1` or `-X gil=0/1`.
- An experimental copy-and-patch JIT (`PYTHON_JIT=1` on builds compiled with it).

## When to use
- CPU-bound parallel work in pure Python threads (data processing, simulations) on the `t` build.
- Libraries testing thread-safety for the free-threaded future.

## When NOT to use
- I/O-bound code → threads/asyncio already work fine with the GIL.
- If your C-extension dependencies don't yet support free-threading (they may re-enable the GIL).
- Shared mutable state without locks — free-threading makes races *more* likely.

## Run
```bash
python examples.py          # normal build: threads share the GIL
python3.14t examples.py     # free-threaded build: example_04 shows real speed-up
```
