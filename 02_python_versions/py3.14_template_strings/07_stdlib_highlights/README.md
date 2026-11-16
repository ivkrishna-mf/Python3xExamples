# 3.14 stdlib highlights — pathlib copy/move, uuid7, heapq max-heap & more

**In one line:** small additions that remove boilerplate in everyday scripts.

## What it is
- `Path.copy()`, `copy_into()`, `move()`, `move_into()` and `Path.info` (cached stat info).
- `uuid.uuid7()` (time-ordered, great for DB keys), `uuid6()`, `uuid8()`.
- `heapq.heapify_max`, `heappush_max`, `heappop_max` — real max-heaps.
- `operator.is_none` / `is_not_none`, `map(strict=True)`, `int`/`float` `from_number`.
- `python -m pdb -p PID` remote attach; `asyncio ps/pstree PID` introspection.

## When to use
- File management scripts (no more `shutil` for simple copies/moves).
- Sortable unique IDs (`uuid7`) for primary keys and event logs.
- Priority queues that need largest-first.

## When NOT to use
- Code supporting < 3.14.

## Run
```bash
python examples.py
```
