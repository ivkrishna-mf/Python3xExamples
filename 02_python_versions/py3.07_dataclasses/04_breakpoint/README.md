# breakpoint() — Python 3.7 (PEP 553)

**In one line:** drop into the debugger with one built-in call, configurable via `PYTHONBREAKPOINT`.

## What it is
`breakpoint()` calls `sys.breakpointhook()`, which by default starts `pdb`. Set
`PYTHONBREAKPOINT=0` to disable all breakpoints, or point it at another debugger
(`ipdb.set_trace`, `pudb.set_trace`, a custom function). 3.13 added `pdb` commands entered
directly at `breakpoint()`, 3.14 added remote attach (`python -m pdb -p PID`).

## When to use
- Interactive debugging during development.
- Conditional debugging: `if bad: breakpoint()`.

## When NOT to use
- Never leave it in committed/production code (lint rule T100).
- Non-interactive environments (CI, services) — use logging.

## Run
These examples replace the hook so they run without stopping. To really debug:
```bash
python -c "x = 41; breakpoint(); print(x + 1)"
PYTHONBREAKPOINT=0 python examples.py   # disables any breakpoint()
```
