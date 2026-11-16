# asyncio.TaskGroup and asyncio.timeout — Python 3.11

**In one line:** structured concurrency — start tasks in a block; if one fails, the rest are cancelled.

## What it is
`async with asyncio.TaskGroup() as tg: tg.create_task(...)` waits for all tasks on exit and
raises an `ExceptionGroup` if any failed (cancelling the others). `async with
asyncio.timeout(s):` cancels the block after `s` seconds and raises `TimeoutError`.
3.15 adds `TaskGroup.cancel()` for stopping a group early.

## When to use
- Fan-out work where all results are needed (prefer over bare `gather`).
- Ensuring no "orphan" tasks leak after an error.
- Deadlines around a group of awaits (`timeout`), including rescheduling deadlines.

## When NOT to use
- When you want independent tasks that shouldn't cancel each other → `gather(...,
  return_exceptions=True)` or separate handling.

## Run
```bash
python examples.py
```
