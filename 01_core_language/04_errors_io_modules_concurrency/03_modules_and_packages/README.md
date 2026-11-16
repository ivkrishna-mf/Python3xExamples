# Modules, packages and imports

**Introduced:** modules 1.0 · packages 1.5 · absolute imports default 3.0 · relative `from . import` 2.5 · namespace packages 3.3 · `importlib` 3.1 · `lazy import` 3.15

**In one line:** organise code into files (modules) and folders (packages) and import what you need.

## What it is
Every `.py` file is a module; a folder with `__init__.py` is a package. `import x`,
`from x import y`, `import x as alias`, relative imports inside packages, `__all__` to define
the public API, and `if __name__ == "__main__":` for script entry points.

## When to use
- Split code by responsibility; keep modules focused.
- `__init__.py` to expose a clean package API.
- `python -m package.module` to run modules inside packages.
- `importlib` for plugins/dynamic loading.

## When NOT to use
- `from module import *` (pollutes namespaces) — except in interactive sessions.
- Circular imports — restructure, or import inside functions / use `lazy import` (3.15).

## Run
```bash
python examples.py
```
