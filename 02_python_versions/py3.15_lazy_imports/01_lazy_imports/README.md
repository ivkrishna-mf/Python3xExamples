# Explicit lazy imports — Python 3.15 (PEP 810)

**In one line:** `lazy import json` keeps the import at the top of the file but loads the module only on first use.

## What it is
`lazy` is a soft keyword for `import` and `from ... import`. The name is bound to a lazy proxy
(`types.LazyImportType`); the real import happens the first time the name is used. Errors
(e.g. missing module) surface at first use.
Rules: module scope only (not inside functions/classes/`try`), no `lazy from x import *`,
no lazy `__future__` imports. Global control: `-X lazy_imports=all|normal|none`,
`PYTHON_LAZY_IMPORTS`, `sys.set_lazy_imports()`, `sys.set_lazy_imports_filter()`.
For code that must also run on older versions, set `__lazy_modules__ = ["json", ...]`.

## When to use
- CLIs and apps where startup time matters (many subcommands, heavy optional deps).
- Imports needed only on rare code paths (plotting, export formats, admin commands).
- Replacing "import inside function" hacks while keeping imports visible at the top.

## When NOT to use
- Modules whose import has side effects you rely on (registering plugins, monkey-patching).
- When you want import errors to fail fast at startup.

## Run
```bash
python3.15 examples.py
python3.15 -X importtime examples.py 2>&1 | tail    # see what actually loads
```
