# Concurrency: threads, processes and asyncio

**Introduced:** `threading` 1.5 · `multiprocessing` 2.6 · `concurrent.futures` 3.2 · `asyncio` 3.4 · `async/await` 3.5 · free-threading 3.13/3.14 · subinterpreters 3.14

**In one line:** run work concurrently — threads for I/O, processes (or free-threaded builds) for CPU, asyncio for massive I/O concurrency.

## What it is
- `ThreadPoolExecutor` — simple parallel I/O (HTTP calls, file reads).
- `ProcessPoolExecutor` — CPU-bound work across cores (bypasses the GIL).
- `asyncio` — thousands of concurrent I/O tasks on one thread (`async def`, `await`,
  `TaskGroup`).
- Synchronisation: `Lock`, `Queue`, `Event`, `Semaphore`.

## When to use
| Workload | Use |
|---|---|
| Many blocking I/O calls | `ThreadPoolExecutor` |
| Huge numbers of sockets/requests | `asyncio` |
| CPU-heavy pure Python | `ProcessPoolExecutor` / free-threaded `3.14t` / `InterpreterPoolExecutor` |

## When NOT to use
- Small, fast scripts — concurrency adds complexity.
- Shared mutable state without locks.

## Run
```bash
python examples.py
```
