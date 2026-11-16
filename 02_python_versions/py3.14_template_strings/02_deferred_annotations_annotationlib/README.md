# Deferred evaluation of annotations & annotationlib — Python 3.14 (PEP 649, 749)

**In one line:** annotations are evaluated only when you ask for them — forward references just work, no quotes or `__future__` import needed.

## What it is
Annotations are compiled into an `__annotate__` function and computed lazily. The new
`annotationlib` module retrieves them in different formats:
- `Format.VALUE` — real objects (raises if a name is undefined)
- `Format.FORWARDREF` — real objects where possible, `ForwardRef` placeholders otherwise
- `Format.STRING` — source-like strings.

## When to use
- Self-referencing / mutually-referencing classes without string quotes.
- Libraries that introspect annotations (serialisers, DI, validators) → use
  `annotationlib.get_annotations()` and choose a format.
- Type-only imports guarded by `TYPE_CHECKING` without breaking runtime introspection.

## When NOT to use
- Code that must support < 3.14 still needs quotes or `from __future__ import annotations`.

## Run
```bash
python examples.py
```
