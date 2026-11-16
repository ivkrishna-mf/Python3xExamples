# Scope (LEGB), global, nonlocal and closures

**Introduced:** nested scopes 2.1/2.2 (PEP 227) · `nonlocal` 3.0 (PEP 3104)

**In one line:** names resolve Local → Enclosing → Global → Built-in; inner functions can capture outer variables.

## What it is
A closure is a function that remembers variables from the scope where it was created.
`nonlocal` rebinds an enclosing variable; `global` rebinds a module variable.

## When to use
- Function factories (make_multiplier, configured validators).
- Small private state (counters) and decorators.

## When NOT to use
- `global` for shared state → pass arguments or use a class.
- Complex state in closures → a class is clearer.

## Run
```bash
python examples.py
```
