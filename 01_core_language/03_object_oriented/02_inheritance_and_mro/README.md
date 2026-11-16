# Inheritance, super() and the MRO

**Introduced:** inheritance 1.0 · `super()` 2.2 · C3 MRO 2.3 · zero-argument `super()` 3.0 · `@override` 3.12

**In one line:** reuse and specialise behaviour from parent classes; `super()` follows the method resolution order.

## What it is
A subclass inherits attributes/methods and can override them. Multiple inheritance is
resolved with the C3 linearisation (`Class.__mro__`). `super()` calls the next class in the MRO,
which makes cooperative mixins work.

## When to use
- True "is-a" relationships (Dog is an Animal).
- Mixins adding small orthogonal capabilities (JsonMixin, LoggingMixin).
- Framework extension points (subclass a base view/handler).

## When NOT to use
- "has-a" relationships → composition (store an object as an attribute).
- Deep hierarchies → prefer composition and protocols.

## Run
```bash
python examples.py
```
