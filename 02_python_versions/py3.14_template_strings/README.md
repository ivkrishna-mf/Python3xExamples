# Python 3.14 · Template Strings and Lazy Annotations
`t"..."` template strings, deferred evaluation of annotations by default, `except A, B:` without
parentheses, warnings for control flow escaping `finally`, multiple interpreters in the stdlib,
Zstandard compression, an officially supported free-threaded build, and many stdlib upgrades
(`Path.copy/move`, `uuid7`, `heapq` max-heaps, remote `pdb` attach).

| # | Feature | In one line |
|---|---|---|
| 01 | [Template strings (t-strings) — Python 3.14 (PEP 750)](01_template_strings/README.md) | `t"Hello {name}"` gives you a `Template` object (strings + interpolations) instead of a finished `str`. |
| 02 | [Deferred evaluation of annotations & annotationlib — Python 3.14 (PEP 649, 749)](02_deferred_annotations_annotationlib/README.md) | annotations are evaluated only when you ask for them — forward references just work, no quotes or `__future__` import needed. |
| 03 | [`except A, B:` without parentheses — Python 3.14 (PEP 758)](03_except_without_parentheses/README.md) | catch several exception types without wrapping them in a tuple — when you don't use `as`. |
| 04 | [Warnings for return/break/continue in `finally` — Python 3.14 (PEP 765)](04_finally_control_flow_warning/README.md) | the compiler now emits `SyntaxWarning` when `return`/`break`/`continue` would exit a `finally` block. |
| 05 | [Multiple interpreters in the stdlib — Python 3.14 (PEP 734)](05_concurrent_interpreters/README.md) | `concurrent.interpreters` runs isolated Python interpreters in one process — each with its own GIL. |
| 06 | [compression.zstd — Python 3.14 (PEP 784)](06_compression_zstd/README.md) | Zstandard compression in the stdlib — fast, high ratio, tunable levels. |
| 07 | [3.14 stdlib highlights — pathlib copy/move, uuid7, heapq max-heap & more](07_stdlib_highlights/README.md) | small additions that remove boilerplate in everyday scripts. |

Run every example in this folder:
```bash
python ../../run_examples.py 02_python_versions/py3.14_template_strings
```
