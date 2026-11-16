# Abstract base classes (abc) and Protocols

**Introduced:** `abc` module 2.6/3.0 (PEP 3119) · `collections.abc` 3.3 · `typing.Protocol` 3.8 (PEP 544)

**In one line:** define interfaces — nominal (ABC: must inherit) or structural (Protocol: just match the methods).

## What it is
- `ABC` + `@abstractmethod`: subclasses must implement the methods or they can't be instantiated.
- `collections.abc` (`Iterable`, `Mapping`, `Sequence`…) give mixin methods for free.
- `Protocol`: any object with matching methods satisfies the type — no inheritance.

## When to use
- ABC: framework base classes with shared code and enforced hooks.
- Protocol: decoupled interfaces, third-party objects, test fakes.
- `collections.abc`: custom containers that should behave like built-ins.

## When NOT to use
- One implementation only → you don't need an interface yet.

## Run
```bash
python examples.py
```
