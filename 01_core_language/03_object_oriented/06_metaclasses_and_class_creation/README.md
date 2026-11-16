# Metaclasses and dynamic class creation

**Introduced:** metaclasses 2.2 · `metaclass=` keyword 3.0 (PEP 3115) · `__prepare__` 3.0 · `__init_subclass__` 3.6 (often replaces metaclasses)

**In one line:** classes are objects created by a metaclass (`type` by default) — you can customise how classes are built.

## What it is
`type(name, bases, namespace)` creates classes dynamically. A custom metaclass (subclass of
`type`) can modify the class at creation: register it, validate it, add methods, enforce rules.

## When to use
- Frameworks/ORMs (Django models, SQLAlchemy, Enum) needing deep class customisation.
- Singletons / registries where `__init_subclass__` or class decorators aren't enough.

## When NOT to use
- Almost always prefer simpler tools first: class decorators, `__init_subclass__`,
  `__set_name__`, dataclasses.

## Run
```bash
python examples.py
```
