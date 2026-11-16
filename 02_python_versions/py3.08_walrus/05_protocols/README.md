# Protocols (structural subtyping) — Python 3.8 (PEP 544)

**In one line:** "if it has these methods, it fits" — static duck typing without inheritance.

## What it is
`class SupportsClose(Protocol): def close(self) -> None: ...` describes an interface. Any class
with a matching `close()` is accepted by type checkers — no subclassing needed.
`@runtime_checkable` enables `isinstance()` checks (method presence only).

## When to use
- Accepting third-party objects you can't modify (file-likes, clients, loggers).
- Decoupling modules: depend on a tiny interface, not a concrete class.
- Test doubles: fakes automatically satisfy the protocol.

## When NOT to use
- When you want shared implementation → use an ABC / base class.
- Runtime validation of signatures — `isinstance` only checks attribute names exist.

## Run
```bash
python examples.py
```
