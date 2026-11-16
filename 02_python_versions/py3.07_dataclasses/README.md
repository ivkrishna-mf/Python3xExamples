# Python 3.7 · Data Classes and Friends
`@dataclass`, postponed evaluation of annotations, context variables, `breakpoint()`,
guaranteed dict ordering and module-level `__getattr__`. `asyncio.run()` also landed here.

| # | Feature | In one line |
|---|---|---|
| 01 | [dataclasses — Python 3.7 (PEP 557) · kw_only/slots/match_args 3.10](01_dataclasses/README.md) | `@dataclass` writes `__init__`, `__repr__`, `__eq__` (and more) from annotated fields. |
| 02 | [Postponed evaluation of annotations — Python 3.7 (PEP 563)](02_postponed_annotations/README.md) | `from __future__ import annotations` stores annotations as strings, so forward references just work. |
| 03 | [contextvars — Python 3.7 (PEP 567)](03_contextvars/README.md) | "thread-local" state that also works correctly across asyncio tasks. |
| 04 | [breakpoint() — Python 3.7 (PEP 553)](04_breakpoint/README.md) | drop into the debugger with one built-in call, configurable via `PYTHONBREAKPOINT`. |
| 05 | [Guaranteed dict insertion order — Python 3.7 (language guarantee)](05_dict_insertion_order/README.md) | `dict` iterates in insertion order — officially, you can rely on it. |
| 06 | [Module __getattr__ and __dir__ — Python 3.7 (PEP 562)](06_module_getattr_dir/README.md) | define `__getattr__(name)` at module level to compute or lazily load attributes. |

Run every example in this folder:
```bash
python ../../run_examples.py 02_python_versions/py3.07_dataclasses
```
