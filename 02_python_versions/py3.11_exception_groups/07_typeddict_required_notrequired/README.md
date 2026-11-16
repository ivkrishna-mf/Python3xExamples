# TypedDict Required / NotRequired — Python 3.11 (PEP 655)

**In one line:** mark individual TypedDict keys as optional (or required) without splitting classes.

## What it is
`NotRequired[int]` makes one key optional in a total TypedDict; `Required[str]` makes one key
mandatory in a `total=False` TypedDict. Generic TypedDicts also became possible in 3.11.

## When to use
- JSON/API payloads with a few optional fields.
- Config dicts where most keys have defaults.

## When NOT to use
- When the dict is really an object with behaviour → dataclass.

## Run
```bash
python examples.py
```
