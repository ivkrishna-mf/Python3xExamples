# Decorators

**Introduced:** `@decorator` syntax 2.4 (PEP 318) · class decorators 2.6/3.0 (PEP 3129) · relaxed grammar 3.9 (PEP 614)

**In one line:** `@deco` wraps a function or class to add behaviour without changing its code.

## What it is
`@deco def f(): ...` is shorthand for `f = deco(f)`. Use `functools.wraps` to keep the name,
docstring and signature. Decorators can take arguments (a factory returning a decorator) and
can decorate classes too.

## When to use
- Cross-cutting concerns: logging, timing, caching, retries, auth, validation, registration.
- Framework hooks (`@app.route`, `@pytest.fixture`, `@dataclass`).

## When NOT to use
- When the behaviour is core logic that readers need to see inline.
- Stacking many decorators that change signatures in surprising ways.

## Run
```bash
python examples.py
```
