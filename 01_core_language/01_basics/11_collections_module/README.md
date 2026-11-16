# collections: Counter, defaultdict, deque, namedtuple, ChainMap, OrderedDict

**Introduced:** deque 2.4 · defaultdict 2.5 · namedtuple 2.6 · Counter/OrderedDict 2.7/3.1 · ChainMap 3.3

**In one line:** specialised containers that replace common hand-written dict/list patterns.

## What it is
- `Counter` — count hashable items, `most_common()`.
- `defaultdict(list)` — auto-create missing values (grouping).
- `deque` — fast appends/pops at both ends, bounded with `maxlen`.
- `ChainMap` — layered lookups (CLI > env > defaults) without copying.

## When to use
- Counting → Counter; grouping → defaultdict; queues/sliding windows → deque.

## When NOT to use
- Simple dicts/lists are enough — don't reach for these by default.

## Run
```bash
python examples.py
```
