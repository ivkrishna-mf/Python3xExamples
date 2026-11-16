# Exception notes `add_note()` — Python 3.11 (PEP 678)

**In one line:** attach extra context to an exception without changing its type or message.

## What it is
`exc.add_note("while processing row 42")` appends a string to `exc.__notes__`; tracebacks
print the notes under the error message.

## When to use
- Adding context as an error bubbles up (which file, row, request, retry attempt).
- Test frameworks / validators adding hints.
- Enriching errors before re-raising, while keeping the original exception type.

## When NOT to use
- When a different exception type better describes the failure → `raise New(...) from exc`.

## Run
```bash
python examples.py
```
