# functools.singledispatch — Python 3.4 (PEP 443)

**In one line:** one function name, different implementations chosen by the type of the first argument.

## What it is
Decorate a base function with `@singledispatch`, then `@func.register` per type.
Since 3.7 you can register using type annotations; `singledispatchmethod` (3.8) works on methods.
Union types in `register` work since 3.11.

## When to use
- Serialising / formatting values of many types (to JSON, to HTML…).
- Replacing long `if isinstance(...) elif isinstance(...)` chains.
- Letting other modules extend your function for their own types.

## When NOT to use
- Dispatch on more than one argument (not supported).
- When regular polymorphism (a method on the class) is natural and you own the classes.

## Run
```bash
python examples.py
```
