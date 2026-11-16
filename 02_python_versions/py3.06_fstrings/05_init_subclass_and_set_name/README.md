# __init_subclass__ and __set_name__ — Python 3.6 (PEP 487)

**In one line:** customise subclass creation and descriptors without writing a metaclass.

## What it is
- `__init_subclass__(cls, **kw)` runs on the parent whenever a subclass is defined.
- `__set_name__(self, owner, name)` tells a descriptor the attribute name it was assigned to.

## When to use
- Plugin registries (auto-register every subclass).
- Enforcing that subclasses define required attributes.
- Class keyword options: `class Csv(Exporter, ext="csv")`.
- Validating descriptors / ORM-style fields that need to know their own name.

## When NOT to use
- When a simple decorator or explicit registration is clearer.

## Run
```bash
python examples.py
```
