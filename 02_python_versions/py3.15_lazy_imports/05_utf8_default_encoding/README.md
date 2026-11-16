# UTF-8 is the default encoding — Python 3.15 (PEP 686)

**In one line:** `open("file.txt")` now uses UTF-8 everywhere (including Windows), not the locale encoding.

## What it is
UTF-8 Mode is on by default: text files, `sys.stdin/stdout`, `subprocess` text pipes and
`os` filename handling default to UTF-8. Opt out with `PYTHONUTF8=0` or `-X utf8=0`;
`encoding="locale"` explicitly requests the old behaviour.

## When to use (this knowledge)
- Expect identical behaviour on Windows, macOS and Linux.
- Still pass `encoding="utf-8"` explicitly if your code supports older Pythons.
- Use `-X warn_default_encoding` on older versions to find calls that relied on the locale.

## When NOT to use
- Legacy files in cp1252/Shift-JIS etc. → pass that encoding (or `"locale"`) explicitly.

## Run
```bash
python3.15 examples.py
python3.15 -X utf8=0 examples.py     # compare with UTF-8 mode off
```
