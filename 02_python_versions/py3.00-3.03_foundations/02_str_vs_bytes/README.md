# Text (str) vs binary (bytes) — Python 3.0 (PEP 3137)

**In one line:** `str` is Unicode text, `bytes` is raw binary; you convert explicitly with `encode()`/`decode()`.

## What it is
Python 3 separates text from binary data. Mixing them raises `TypeError`, which forces you
to decide on an encoding at the boundary (files, sockets, subprocesses).

## When to use
- `str` for anything humans read: names, messages, JSON text, templates.
- `bytes` for network payloads, binary files, hashing, crypto, images.
- `bytearray` when you need a *mutable* byte buffer.
- Decode as early as possible when data comes in, encode as late as possible when it goes out
  (the "Unicode sandwich").

## When NOT to use
- Don't store text as bytes inside your program logic.
- Don't rely on the platform default encoding — pass `encoding="utf-8"` explicitly.

## Run
```bash
python examples.py
```
