# typing.Annotated — Python 3.9 (PEP 593)

**In one line:** attach extra metadata to a type: `Annotated[int, Gt(0)]`.

## What it is
`Annotated[T, meta1, meta2]` is treated as plain `T` by type checkers, but frameworks can read
the metadata at runtime with `get_type_hints(..., include_extras=True)`.
FastAPI, pydantic, typer, SQLAlchemy and msgspec all use it.

## When to use
- Validation constraints, units, docs, DB column options, CLI options alongside the type.
- Writing your own lightweight validators or dependency injection.

## When NOT to use
- If no tool reads the metadata, it is just noise.

## Run
```bash
python examples.py
```
