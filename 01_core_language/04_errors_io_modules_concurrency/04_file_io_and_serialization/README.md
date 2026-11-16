# File I/O and serialisation (pathlib, open, json, csv, pickle)

**Introduced:** `open` 1.0 · `with` for files 2.5 · `io` 2.6/3.0 · `json` 2.6 · `csv` 2.3 · `pathlib` 3.4 · UTF-8 default 3.15

**In one line:** read and write text, binary, JSON, CSV and Python objects safely and portably.

## What it is
`pathlib.Path` for paths and quick reads/writes; `open()` in a `with` block for streaming;
`json` for interchange, `csv` for tabular data, `pickle` for Python-only object storage.

## When to use
- `Path.read_text()/write_text()` for small files; iterate a file object for big ones.
- JSON for configs/APIs; CSV for spreadsheets; pickle only for trusted, internal caches.
- Always specify `encoding="utf-8"` (until you can rely on 3.15+).

## When NOT to use
- `pickle.load` on untrusted data (can execute code).
- Manual string splitting for CSV (quotes/commas) → use the `csv` module.

## Run
```bash
python examples.py
```
