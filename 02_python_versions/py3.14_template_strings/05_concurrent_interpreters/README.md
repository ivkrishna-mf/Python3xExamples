# Multiple interpreters in the stdlib — Python 3.14 (PEP 734)

**In one line:** `concurrent.interpreters` runs isolated Python interpreters in one process — each with its own GIL.

## What it is
Each sub-interpreter has separate modules and state, so CPU-bound work can run in parallel
(like processes) with lower overhead. Communicate via `interpreters.create_queue()`, or use
`concurrent.futures.InterpreterPoolExecutor` for a pool API.

## When to use
- CPU-bound parallelism with strong isolation, on a regular (GIL) build.
- Running untrusted-ish or plugin code in a separate interpreter state.
- Actor-style designs with message passing.

## When NOT to use
- Many C extensions don't support sub-interpreters yet.
- Sharing lots of objects — data is copied/pickled between interpreters.
- Simple I/O concurrency → asyncio/threads.

## Run
```bash
python examples.py
```
