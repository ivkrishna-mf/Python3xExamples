# zoneinfo — Python 3.9 (PEP 615)

**In one line:** real IANA time zones (`ZoneInfo("Asia/Kolkata")`) in the standard library.

## What it is
`zoneinfo.ZoneInfo` provides `tzinfo` objects backed by the system tz database (or the
`tzdata` PyPI package on Windows). Handles daylight-saving transitions correctly.

## When to use
- Converting timestamps between time zones; displaying local times to users.
- Scheduling across DST changes.
- Replacing `pytz` in new code.

## When NOT to use
- Fixed offsets only → `datetime.timezone(timedelta(hours=5, minutes=30))`.
- Store and compute in UTC; convert to local zones only for display.

**Windows note:** run `pip install tzdata` if `ZoneInfo(...)` raises `ZoneInfoNotFoundError`.

## Run
```bash
python examples.py
```
