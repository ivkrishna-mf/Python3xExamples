# Python Versions 3.0 → 3.15

What each Python 3 release added, in release order. Use this to learn what's new, or to check the minimum version a feature needs.

## [Python 3.0 – 3.3 · The Foundations](py3.00-3.03_foundations/README.md)

| Feature | In one line |
|---|---|
| [print() as a function — Python 3.0 (PEP 3105)](py3.00-3.03_foundations/01_print_function/README.md) | `print` is a normal function with `sep`, `end`, `file` and `flush` keywords. |
| [Text (str) vs binary (bytes) — Python 3.0 (PEP 3137)](py3.00-3.03_foundations/02_str_vs_bytes/README.md) | `str` is Unicode text, `bytes` is raw binary; you convert explicitly with `encode()`/`decode()`. |
| [Keyword-only arguments — Python 3.0 (PEP 3102)](py3.00-3.03_foundations/03_keyword_only_args/README.md) | parameters after `*` (or `*args`) can only be passed by name. |
| [Extended iterable unpacking — Python 3.0 (PEP 3132)](py3.00-3.03_foundations/04_extended_unpacking/README.md) | `first, *rest = items` collects "everything else" into a list. |
| [nonlocal — Python 3.0 (PEP 3104)](py3.00-3.03_foundations/05_nonlocal/README.md) | lets a nested function *rebind* a variable from its enclosing function. |
| [Exception chaining — Python 3.0 / 3.3 (PEP 3134, PEP 409, PEP 415)](py3.00-3.03_foundations/06_exception_chaining/README.md) | `raise NewError(...) from original` keeps the root cause; `from None` hides it. |
| [yield from — Python 3.3 (PEP 380)](py3.00-3.03_foundations/07_yield_from/README.md) | delegate part of a generator's work to another iterable or sub-generator. |
| [functools.lru_cache — Python 3.2](py3.00-3.03_foundations/08_lru_cache/README.md) | memoise a pure function's results with a bounded, least-recently-used cache. |

## [Python 3.4 · Batteries Upgrade](py3.04_pathlib_enum/README.md)

| Feature | In one line |
|---|---|
| [pathlib — Python 3.4 (PEP 428)](py3.04_pathlib_enum/01_pathlib/README.md) | filesystem paths as objects: `Path("data") / "file.csv"`. |
| [enum — Python 3.4 (PEP 435) · plus Flag/auto (3.6) and StrEnum (3.11)](py3.04_pathlib_enum/02_enum/README.md) | a fixed set of named constants with identity, iteration and type safety. |
| [statistics — Python 3.4 (PEP 450) · grown through 3.8 / 3.10 / 3.13](py3.04_pathlib_enum/03_statistics/README.md) | mean, median, mode, stdev, quantiles, correlation… without NumPy. |
| [functools.singledispatch — Python 3.4 (PEP 443)](py3.04_pathlib_enum/04_singledispatch/README.md) | one function name, different implementations chosen by the type of the first argument. |

## [Python 3.5 · Async and Typing Arrive](py3.05_async_typing/README.md)

| Feature | In one line |
|---|---|
| [async / await — Python 3.5 (PEP 492) · asyncio.run 3.7](py3.05_async_typing/01_async_await/README.md) | write concurrent I/O code that reads like sequential code. |
| [The @ matrix multiplication operator — Python 3.5 (PEP 465)](py3.05_async_typing/02_matrix_multiplication_operator/README.md) | `a @ b` calls `a.__matmul__(b)`; NumPy uses it for matrix products. |
| [Additional unpacking generalisations — Python 3.5 (PEP 448)](py3.05_async_typing/03_unpacking_generalizations/README.md) | use `*` and `**` multiple times in calls and inside list/tuple/set/dict displays. |
| [Type hints and the typing module — Python 3.5 (PEP 484)](py3.05_async_typing/04_type_hints_typing/README.md) | annotate parameters and return values so tools (mypy, pyright, IDEs) can check your code. |

## [Python 3.6 · Readability Wins](py3.06_fstrings/README.md)

| Feature | In one line |
|---|---|
| [f-strings (formatted string literals) — Python 3.6 (PEP 498)](py3.06_fstrings/01_f_strings/README.md) | `f"Hello {name}!"` — embed expressions directly in string literals. |
| [Variable annotations — Python 3.6 (PEP 526)](py3.06_fstrings/02_variable_annotations/README.md) | `count: int = 0` — annotate variables and class attributes, not just functions. |
| [Underscores in numeric literals — Python 3.6 (PEP 515)](py3.06_fstrings/03_underscores_in_numeric_literals/README.md) | write `1_000_000` instead of `1000000` for readability. |
| [Async generators & async comprehensions — Python 3.6 (PEP 525, PEP 530)](py3.06_fstrings/04_async_generators_and_comprehensions/README.md) | `yield` inside `async def`, and `[x async for x in aiter()]` / `await` in comprehensions. |
| [__init_subclass__ and __set_name__ — Python 3.6 (PEP 487)](py3.06_fstrings/05_init_subclass_and_set_name/README.md) | customise subclass creation and descriptors without writing a metaclass. |
| [secrets — Python 3.6 (PEP 506)](py3.06_fstrings/06_secrets/README.md) | cryptographically strong random tokens, passwords and choices. |

## [Python 3.7 · Data Classes and Friends](py3.07_dataclasses/README.md)

| Feature | In one line |
|---|---|
| [dataclasses — Python 3.7 (PEP 557) · kw_only/slots/match_args 3.10](py3.07_dataclasses/01_dataclasses/README.md) | `@dataclass` writes `__init__`, `__repr__`, `__eq__` (and more) from annotated fields. |
| [Postponed evaluation of annotations — Python 3.7 (PEP 563)](py3.07_dataclasses/02_postponed_annotations/README.md) | `from __future__ import annotations` stores annotations as strings, so forward references just work. |
| [contextvars — Python 3.7 (PEP 567)](py3.07_dataclasses/03_contextvars/README.md) | "thread-local" state that also works correctly across asyncio tasks. |
| [breakpoint() — Python 3.7 (PEP 553)](py3.07_dataclasses/04_breakpoint/README.md) | drop into the debugger with one built-in call, configurable via `PYTHONBREAKPOINT`. |
| [Guaranteed dict insertion order — Python 3.7 (language guarantee)](py3.07_dataclasses/05_dict_insertion_order/README.md) | `dict` iterates in insertion order — officially, you can rely on it. |
| [Module __getattr__ and __dir__ — Python 3.7 (PEP 562)](py3.07_dataclasses/06_module_getattr_dir/README.md) | define `__getattr__(name)` at module level to compute or lazily load attributes. |

## [Python 3.8 · Expressive Syntax](py3.08_walrus/README.md)

| Feature | In one line |
|---|---|
| [Assignment expressions (walrus `:=`) — Python 3.8 (PEP 572)](py3.08_walrus/01_walrus_operator/README.md) | assign and use a value inside an expression: `if (n := len(data)) > 10:`. |
| [Positional-only parameters `/` — Python 3.8 (PEP 570)](py3.08_walrus/02_positional_only_parameters/README.md) | parameters before `/` can't be passed by keyword. |
| [f-string `=` specifier — Python 3.8](py3.08_walrus/03_fstring_self_documenting/README.md) | `f"{x=}"` prints `x=42` — the expression text *and* its value. |
| [TypedDict, Final and Literal — Python 3.8 (PEP 589, 591, 586)](py3.08_walrus/04_typeddict_final_literal/README.md) | precise types for dict shapes, constants and allowed literal values. |
| [Protocols (structural subtyping) — Python 3.8 (PEP 544)](py3.08_walrus/05_protocols/README.md) | "if it has these methods, it fits" — static duck typing without inheritance. |
| [functools.cached_property — Python 3.8](py3.08_walrus/06_cached_property/README.md) | a property computed once per instance, then stored as a normal attribute. |

## [Python 3.9 · Everyday Conveniences](py3.09_dict_union_generics/README.md)

| Feature | In one line |
|---|---|
| [Dict merge `\|` and update `\|=` — Python 3.9 (PEP 584)](py3.09_dict_union_generics/01_dict_union_operators/README.md) | `merged = defaults \| overrides`; `config \|= extra` updates in place. |
| [str.removeprefix() / removesuffix() — Python 3.9 (PEP 616)](py3.09_dict_union_generics/02_str_removeprefix_removesuffix/README.md) | strip an exact leading/trailing substring — once, and only if it's there. |
| [Built-in generic types `list[int]` — Python 3.9 (PEP 585)](py3.09_dict_union_generics/03_builtin_generic_types/README.md) | use `list[str]`, `dict[str, int]`, `tuple[int, ...]` directly — no `typing.List`. |
| [zoneinfo — Python 3.9 (PEP 615)](py3.09_dict_union_generics/04_zoneinfo/README.md) | real IANA time zones (`ZoneInfo("Asia/Kolkata")`) in the standard library. |
| [typing.Annotated — Python 3.9 (PEP 593)](py3.09_dict_union_generics/05_annotated/README.md) | attach extra metadata to a type: `Annotated[int, Gt(0)]`. |
| [functools.cache — Python 3.9](py3.09_dict_union_generics/06_functools_cache/README.md) | `@cache` = `@lru_cache(maxsize=None)` — simple unbounded memoisation. |

## [Python 3.10 · Pattern Matching](py3.10_pattern_matching/README.md)

| Feature | In one line |
|---|---|
| [Structural pattern matching `match`/`case` — Python 3.10 (PEP 634, 635, 636)](py3.10_pattern_matching/01_structural_pattern_matching/README.md) | match the *shape* of data (sequences, mappings, classes) and destructure it in one go. |
| [Union types with `X \| Y` — Python 3.10 (PEP 604)](py3.10_pattern_matching/02_union_type_operator/README.md) | write `int \| None` instead of `Optional[int]`, `int \| str` instead of `Union[int, str]`. |
| [Parenthesised context managers — Python 3.10](py3.10_pattern_matching/03_parenthesized_context_managers/README.md) | spread several `with` items over multiple lines inside parentheses. |
| [ParamSpec, Concatenate, TypeAlias, TypeGuard — Python 3.10 (PEP 612, 613, 647)](py3.10_pattern_matching/04_paramspec_typealias_typeguard/README.md) | type decorators precisely, name complex types, and write type-narrowing helpers. |
| [zip(strict=True), itertools.pairwise & friends — Python 3.10 (PEP 618)](py3.10_pattern_matching/05_zip_strict_pairwise_and_more/README.md) | catch length mismatches in `zip`, iterate over consecutive pairs, plus small 3.10 helpers. |

## [Python 3.11 · Faster CPython and Better Errors](py3.11_exception_groups/README.md)

| Feature | In one line |
|---|---|
| [ExceptionGroup and `except*` — Python 3.11 (PEP 654)](py3.11_exception_groups/01_exception_groups_except_star/README.md) | raise and handle *several* unrelated exceptions at once. |
| [Exception notes `add_note()` — Python 3.11 (PEP 678)](py3.11_exception_groups/02_exception_notes/README.md) | attach extra context to an exception without changing its type or message. |
| [tomllib — Python 3.11 (PEP 680)](py3.11_exception_groups/03_tomllib/README.md) | read TOML files (like `pyproject.toml`) with the standard library. |
| [typing.Self and LiteralString — Python 3.11 (PEP 673, 675)](py3.11_exception_groups/04_self_and_literalstring/README.md) | `-> Self` for methods returning their own class; `LiteralString` to guard against injection. |
| [asyncio.TaskGroup and asyncio.timeout — Python 3.11](py3.11_exception_groups/05_asyncio_taskgroup_and_timeout/README.md) | structured concurrency — start tasks in a block; if one fails, the rest are cancelled. |
| [Variadic generics — TypeVarTuple & Unpack — Python 3.11 (PEP 646)](py3.11_exception_groups/06_variadic_generics_typevartuple/README.md) | generics over an *arbitrary number* of types — e.g. array shapes or tuple-like records. |
| [TypedDict Required / NotRequired — Python 3.11 (PEP 655)](py3.11_exception_groups/07_typeddict_required_notrequired/README.md) | mark individual TypedDict keys as optional (or required) without splitting classes. |

## [Python 3.12 · New Generics Syntax](py3.12_type_params/README.md)

| Feature | In one line |
|---|---|
| [Type parameter syntax — Python 3.12 (PEP 695)](py3.12_type_params/01_type_parameter_syntax/README.md) | declare generics inline: `def first[T](xs: list[T]) -> T` and `class Stack[T]:`. |
| [The `type` statement — Python 3.12 (PEP 695)](py3.12_type_params/02_type_statement_aliases/README.md) | `type Vector = list[float]` creates a lazily evaluated, possibly generic type alias. |
| [f-string grammar formalised — Python 3.12 (PEP 701)](py3.12_type_params/03_fstring_grammar_pep701/README.md) | f-strings can now reuse the same quotes, contain backslashes, comments and span lines. |
| [@typing.override — Python 3.12 (PEP 698)](py3.12_type_params/04_override_decorator/README.md) | mark a method as overriding a parent method so checkers catch typos and renames. |
| [Typed **kwargs with Unpack[TypedDict] — Python 3.12 (PEP 692)](py3.12_type_params/05_unpack_typeddict_kwargs/README.md) | `def f(**kw: Unpack[Options])` gives each keyword argument its own type. |
| [itertools.batched & other 3.12 stdlib additions](py3.12_type_params/06_itertools_batched_and_more/README.md) | `batched("ABCDEFG", 3)` → `('A','B','C') ('D','E','F') ('G',)`. |

## [Python 3.13 · Free-threading Preview and a New REPL](py3.13_free_threading/README.md)

| Feature | In one line |
|---|---|
| [@warnings.deprecated — Python 3.13 (PEP 702)](py3.13_free_threading/01_deprecated_decorator/README.md) | mark functions/classes/overloads as deprecated — warns at runtime *and* in type checkers/IDEs. |
| [typing.TypeIs — Python 3.13 (PEP 742)](py3.13_free_threading/02_typeis_narrowing/README.md) | a user-defined type guard that narrows in *both* the `if` and the `else` branch. |
| [ReadOnly TypedDict keys — Python 3.13 (PEP 705)](py3.13_free_threading/03_readonly_typeddict/README.md) | `ReadOnly[str]` marks a TypedDict key that type checkers won't let you modify. |
| [Type parameter defaults — Python 3.13 (PEP 696)](py3.13_free_threading/04_type_parameter_defaults/README.md) | `class Box[T = int]:` — a generic parameter falls back to a default when not specified. |
| [copy.replace() — Python 3.13](py3.13_free_threading/05_copy_replace/README.md) | one function to make a modified copy of dataclasses, namedtuples, datetimes and more. |
| [Free-threaded CPython (no GIL) & JIT — Python 3.13 (PEP 703, 744) · supported in 3.14 (PEP 779)](py3.13_free_threading/06_free_threading_and_jit/README.md) | an optional `python3.13t` / `python3.14t` build lets threads run Python code truly in parallel. |

## [Python 3.14 · Template Strings and Lazy Annotations](py3.14_template_strings/README.md)

| Feature | In one line |
|---|---|
| [Template strings (t-strings) — Python 3.14 (PEP 750)](py3.14_template_strings/01_template_strings/README.md) | `t"Hello {name}"` gives you a `Template` object (strings + interpolations) instead of a finished `str`. |
| [Deferred evaluation of annotations & annotationlib — Python 3.14 (PEP 649, 749)](py3.14_template_strings/02_deferred_annotations_annotationlib/README.md) | annotations are evaluated only when you ask for them — forward references just work, no quotes or `__future__` import needed. |
| [`except A, B:` without parentheses — Python 3.14 (PEP 758)](py3.14_template_strings/03_except_without_parentheses/README.md) | catch several exception types without wrapping them in a tuple — when you don't use `as`. |
| [Warnings for return/break/continue in `finally` — Python 3.14 (PEP 765)](py3.14_template_strings/04_finally_control_flow_warning/README.md) | the compiler now emits `SyntaxWarning` when `return`/`break`/`continue` would exit a `finally` block. |
| [Multiple interpreters in the stdlib — Python 3.14 (PEP 734)](py3.14_template_strings/05_concurrent_interpreters/README.md) | `concurrent.interpreters` runs isolated Python interpreters in one process — each with its own GIL. |
| [compression.zstd — Python 3.14 (PEP 784)](py3.14_template_strings/06_compression_zstd/README.md) | Zstandard compression in the stdlib — fast, high ratio, tunable levels. |
| [3.14 stdlib highlights — pathlib copy/move, uuid7, heapq max-heap & more](py3.14_template_strings/07_stdlib_highlights/README.md) | small additions that remove boilerplate in everyday scripts. |

## [Python 3.15 · Lazy Imports, frozendict and sentinel](py3.15_lazy_imports/README.md)

| Feature | In one line |
|---|---|
| [Explicit lazy imports — Python 3.15 (PEP 810)](py3.15_lazy_imports/01_lazy_imports/README.md) | `lazy import json` keeps the import at the top of the file but loads the module only on first use. |
| [frozendict built-in — Python 3.15 (PEP 814)](py3.15_lazy_imports/02_frozendict/README.md) | an immutable, hashable dict: `frozendict(host="db", port=5432)`. |
| [sentinel built-in — Python 3.15 (PEP 661)](py3.15_lazy_imports/03_sentinel/README.md) | `MISSING = sentinel("MISSING")` — a unique marker with a clean repr that works in type hints. |
| [Unpacking in comprehensions — Python 3.15 (PEP 798)](py3.15_lazy_imports/04_unpacking_in_comprehensions/README.md) | `[*xs for xs in lists]` flattens one level; `{**d for d in dicts}` merges dicts. |
| [UTF-8 is the default encoding — Python 3.15 (PEP 686)](py3.15_lazy_imports/05_utf8_default_encoding/README.md) | `open("file.txt")` now uses UTF-8 everywhere (including Windows), not the locale encoding. |
| [TypeForm, closed TypedDicts & disjoint bases — Python 3.15 (PEP 747, 728, 800)](py3.15_lazy_imports/06_typing_typeform_closed_typeddict/README.md) | type "a type expression" as a value, and declare TypedDicts that forbid (or type) extra keys. |
| [profiling package & Tachyon sampling profiler — Python 3.15 (PEP 799)](py3.15_lazy_imports/07_profiling_sampling_tachyon/README.md) | `python -m profiling.sampling run app.py` profiles with near-zero overhead — even attach to a running PID. |
| [3.15 stdlib highlights — math.integer, re.prefixmatch, Counter ^, TaskGroup.cancel & more](py3.15_lazy_imports/08_stdlib_highlights/README.md) | many small, practical additions. |

