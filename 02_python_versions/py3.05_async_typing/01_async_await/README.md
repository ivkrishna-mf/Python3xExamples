# async / await — Python 3.5 (PEP 492) · asyncio.run 3.7

**In one line:** write concurrent I/O code that reads like sequential code.

## What it is
`async def` defines a coroutine; `await` pauses it until another awaitable finishes, letting the
event loop run other tasks meanwhile. `asyncio.gather`, `create_task`, `Queue`, `Semaphore`
coordinate many coroutines on a single thread.

## When to use
- Many concurrent I/O operations: HTTP calls, DB queries, websockets, chat servers.
- High-concurrency network services (thousands of connections).
- When a library you use is async-first (FastAPI, aiohttp, asyncpg…).

## When NOT to use
- CPU-bound work → use `multiprocessing`, `concurrent.futures`, or free-threaded builds.
- Small scripts doing a handful of sequential calls — plain sync code is simpler.
- Calling blocking functions inside coroutines (wrap with `asyncio.to_thread`).

## Run
```bash
python examples.py
```
