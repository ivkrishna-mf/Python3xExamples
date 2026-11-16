# str.removeprefix() / removesuffix() — Python 3.9 (PEP 616)

**In one line:** strip an exact leading/trailing substring — once, and only if it's there.

## What it is
`"test_login".removeprefix("test_")` → `"login"`. Unlike `lstrip`/`rstrip`, which strip a
*set of characters*, these remove one exact substring. Also on `bytes`/`bytearray`.

## When to use
- Removing URL schemes, file extensions, key prefixes, version tags (`v1.2` → `1.2`).
- Cleaning IDs like `"user:123"` → `"123"`.

## When NOT to use
- Stripping whitespace or arbitrary characters → `strip()`.
- Changing file suffixes → `pathlib.Path.with_suffix`.

## Run
```bash
python examples.py
```
