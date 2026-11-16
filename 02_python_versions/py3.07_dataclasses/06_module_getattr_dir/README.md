# Module __getattr__ and __dir__ — Python 3.7 (PEP 562)

**In one line:** define `__getattr__(name)` at module level to compute or lazily load attributes.

## What it is
When normal lookup on a module fails, Python calls the module's `__getattr__`. `__dir__`
customises `dir(module)`.

## When to use
- Deprecating module attributes with a warning.
- Lazy-loading heavy submodules on first access (pre-3.15; 3.15 adds `lazy import`).
- Aliases / computed constants.

## When NOT to use
- To hide typos — it makes bugs harder to find if you return defaults for anything.

## Run
```bash
python examples.py
```
