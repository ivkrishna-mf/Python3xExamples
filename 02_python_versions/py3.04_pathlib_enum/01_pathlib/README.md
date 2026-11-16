# pathlib — Python 3.4 (PEP 428)

**In one line:** filesystem paths as objects: `Path("data") / "file.csv"`.

## What it is
`pathlib.Path` replaces most of `os.path`, `glob` and many `open()` calls with methods on a
path object that works on Windows and POSIX.

## When to use
- Any new code that builds, inspects or walks file paths.
- Reading/writing small files quickly: `read_text()`, `write_text()`.
- Globbing: `Path(".").rglob("*.py")`.
- Cross-platform scripts (Windows `\` vs POSIX `/` handled for you).

## When NOT to use
- Hot loops over millions of path strings where `os.scandir` is faster.
- Code that must interoperate with very old APIs that only accept `str` (wrap with `str(p)`).

## Run
```bash
python examples.py
```
