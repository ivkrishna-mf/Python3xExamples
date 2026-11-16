# Async generators & async comprehensions — Python 3.6 (PEP 525, PEP 530)

**In one line:** `yield` inside `async def`, and `[x async for x in aiter()]` / `await` in comprehensions.

## What it is
An `async def` containing `yield` is an async generator, consumed with `async for`.
Comprehensions can use `async for` and `await` inside coroutines.

## When to use
- Streaming results from async sources: paginated APIs, websockets, DB cursors, file tails.
- Building async data pipelines (filter/map stages).
- Collecting async streams concisely.

## When NOT to use
- Outside an event loop / in sync code.
- When you need all data concurrently → `asyncio.gather` instead of sequential `async for`.

## Run
```bash
python examples.py
```
