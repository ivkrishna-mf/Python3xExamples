# compression.zstd — Python 3.14 (PEP 784)

**In one line:** Zstandard compression in the stdlib — fast, high ratio, tunable levels.

## What it is
The new `compression` package hosts `compression.zstd` plus re-exports `gzip`, `bz2`, `lzma`,
`zlib`. zstd supports one-shot `compress`/`decompress`, file objects (`zstd.open`), streaming
compressors, trained dictionaries, and `tarfile`/`zipfile`/`shutil` integration.

## When to use
- Compressing logs, datasets, caches, network payloads — better speed/ratio than gzip.
- Interop with tools already using `.zst` files.

## When NOT to use
- Consumers that only understand gzip/zip without zstd.
- Python < 3.14 (use the `zstandard` PyPI package).

## Run
```bash
python examples.py
```
