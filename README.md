# Python 3.x Feature Examples (through Python 3.15)

**107 features × 10 runnable examples = 1070 examples.** Every feature folder has a `README.md` (what it is · when to use · when **not** to use) and an `examples.py` with ten self-contained, numbered examples.

## How it's organised
```
Python3xExamples/
├── README.md                  ← you are here (master index)
├── run_examples.py            ← runs everything your Python supports
├── 01_core_language/          ← timeless features in modern syntax
│   ├── 01_basics/
│   │   ├── README.md          ← group index
│   │   └── 03_strings/
│   │       ├── README.md      ← what / when to use / when not
│   │       └── examples.py    ← 10 examples
│   └── ...
└── 02_python_versions/        ← what each release added
    ├── py3.00-3.03_foundations/
    ├── ...
    └── py3.15_lazy_imports/
```

## Quick start
```bash
python run_examples.py                                   # run all (newer-version folders are skipped)
python run_examples.py 01_core_language                  # one section
python run_examples.py -v 02_python_versions/py3.10_pattern_matching   # with output
cd 01_core_language/01_basics/03_strings && python examples.py         # a single feature
```
Each `examples.py` declares `MIN_VERSION`. To try the newest folders, install more interpreters, e.g. `uv python install 3.14 3.15` then `uv run --python 3.15 python run_examples.py`.

## Python 3 releases at a glance
| Version | Year | Headline features |
|---|---|---|
| 3.0–3.3 | 2008–2012 | print(), str/bytes split, keyword-only args, nonlocal, yield from |
| 3.4 | 2014 | pathlib, enum, asyncio, statistics |
| 3.5 | 2015 | async/await, typing, @ operator, unpacking generalisations |
| 3.6 | 2016 | f-strings, variable annotations, 1_000 literals, secrets |
| 3.7 | 2018 | dataclasses, contextvars, breakpoint(), ordered dicts guaranteed |
| 3.8 | 2019 | walrus :=, positional-only /, f'{x=}', Protocol, TypedDict |
| 3.9 | 2020 | dict \|, list[int] generics, zoneinfo, removeprefix |
| 3.10 | 2021 | match/case, X \| Y unions, ParamSpec, zip(strict=) |
| 3.11 | 2022 | 10–60% faster, ExceptionGroup/except*, tomllib, TaskGroup, Self |
| 3.12 | 2023 | def f[T](), type X = ..., f-string grammar, @override |
| 3.13 | 2024 | new REPL, free-threading (experimental), JIT, @deprecated, TypeIs |
| 3.14 | 2025 | t-strings, lazy annotations, except A, B:, subinterpreters, zstd |
| 3.15 | 2026 | lazy import, frozendict, sentinel, [*x for x in xs], UTF-8 default |

## [Core Language](01_core_language/README.md)

Features Python has had since its first releases (1991 →), taught with **current syntax** (type hints, f-strings, `match`, dataclasses, pathlib). Start here if you are learning Python.

### [Core Language · Basics](01_core_language/01_basics/README.md)
- [Variables, names and built-in types](01_core_language/01_basics/01_variables_and_types/README.md)
- [Numbers: int, float, complex, Decimal, Fraction](01_core_language/01_basics/02_numbers_and_math/README.md)
- [Strings](01_core_language/01_basics/03_strings/README.md)
- [Lists](01_core_language/01_basics/04_lists/README.md)
- [Tuples and named tuples](01_core_language/01_basics/05_tuples/README.md)
- [Dictionaries](01_core_language/01_basics/06_dictionaries/README.md)
- [Sets and frozensets](01_core_language/01_basics/07_sets/README.md)
- [Conditionals: if / elif / else, conditional expressions, match](01_core_language/01_basics/08_conditionals_and_match/README.md)
- [Loops: for, while, break/continue, else, enumerate, zip](01_core_language/01_basics/09_loops/README.md)
- [Comprehensions and generator expressions](01_core_language/01_basics/10_comprehensions/README.md)
- [collections: Counter, defaultdict, deque, namedtuple, ChainMap, OrderedDict](01_core_language/01_basics/11_collections_module/README.md)

### [Core Language · Functions and Functional Programming](01_core_language/02_functions_and_functional/README.md)
- [Functions and arguments](01_core_language/02_functions_and_functional/01_functions_and_arguments/README.md)
- [Scope (LEGB), global, nonlocal and closures](01_core_language/02_functions_and_functional/02_scope_and_closures/README.md)
- [Lambdas and higher-order functions (map, filter, sorted, reduce, partial)](01_core_language/02_functions_and_functional/03_lambda_and_higher_order/README.md)
- [Decorators](01_core_language/02_functions_and_functional/04_decorators/README.md)
- [Iterators and generators](01_core_language/02_functions_and_functional/05_iterators_and_generators/README.md)
- [itertools and functools toolkits](01_core_language/02_functions_and_functional/06_itertools_and_functools/README.md)

### [Core Language · Object-Oriented Programming](01_core_language/03_object_oriented/README.md)
- [Classes and objects](01_core_language/03_object_oriented/01_classes_and_objects/README.md)
- [Inheritance, super() and the MRO](01_core_language/03_object_oriented/02_inheritance_and_mro/README.md)
- [Special ("dunder") methods and operator overloading](01_core_language/03_object_oriented/03_dunder_methods/README.md)
- [Properties, descriptors and __slots__](01_core_language/03_object_oriented/04_properties_and_descriptors/README.md)
- [Abstract base classes (abc) and Protocols](01_core_language/03_object_oriented/05_abstract_classes_and_protocols/README.md)
- [Metaclasses and dynamic class creation](01_core_language/03_object_oriented/06_metaclasses_and_class_creation/README.md)

### [Core Language · Errors, Resources, Modules, I/O and Concurrency](01_core_language/04_errors_io_modules_concurrency/README.md)
- [Exceptions: try / except / else / finally, raise, custom errors](01_core_language/04_errors_io_modules_concurrency/01_exceptions/README.md)
- [Context managers: the `with` statement and contextlib](01_core_language/04_errors_io_modules_concurrency/02_context_managers/README.md)
- [Modules, packages and imports](01_core_language/04_errors_io_modules_concurrency/03_modules_and_packages/README.md)
- [File I/O and serialisation (pathlib, open, json, csv, pickle)](01_core_language/04_errors_io_modules_concurrency/04_file_io_and_serialization/README.md)
- [Concurrency: threads, processes and asyncio](01_core_language/04_errors_io_modules_concurrency/05_concurrency_threads_processes_async/README.md)


## [Python Versions 3.0 → 3.15](02_python_versions/README.md)

What each Python 3 release added, in release order. Use this to learn what's new, or to check the minimum version a feature needs.

### [Python 3.0 – 3.3 · The Foundations](02_python_versions/py3.00-3.03_foundations/README.md)
- [print() as a function — Python 3.0 (PEP 3105)](02_python_versions/py3.00-3.03_foundations/01_print_function/README.md)
- [Text (str) vs binary (bytes) — Python 3.0 (PEP 3137)](02_python_versions/py3.00-3.03_foundations/02_str_vs_bytes/README.md)
- [Keyword-only arguments — Python 3.0 (PEP 3102)](02_python_versions/py3.00-3.03_foundations/03_keyword_only_args/README.md)
- [Extended iterable unpacking — Python 3.0 (PEP 3132)](02_python_versions/py3.00-3.03_foundations/04_extended_unpacking/README.md)
- [nonlocal — Python 3.0 (PEP 3104)](02_python_versions/py3.00-3.03_foundations/05_nonlocal/README.md)
- [Exception chaining — Python 3.0 / 3.3 (PEP 3134, PEP 409, PEP 415)](02_python_versions/py3.00-3.03_foundations/06_exception_chaining/README.md)
- [yield from — Python 3.3 (PEP 380)](02_python_versions/py3.00-3.03_foundations/07_yield_from/README.md)
- [functools.lru_cache — Python 3.2](02_python_versions/py3.00-3.03_foundations/08_lru_cache/README.md)

### [Python 3.4 · Batteries Upgrade](02_python_versions/py3.04_pathlib_enum/README.md)
- [pathlib — Python 3.4 (PEP 428)](02_python_versions/py3.04_pathlib_enum/01_pathlib/README.md)
- [enum — Python 3.4 (PEP 435) · plus Flag/auto (3.6) and StrEnum (3.11)](02_python_versions/py3.04_pathlib_enum/02_enum/README.md)
- [statistics — Python 3.4 (PEP 450) · grown through 3.8 / 3.10 / 3.13](02_python_versions/py3.04_pathlib_enum/03_statistics/README.md)
- [functools.singledispatch — Python 3.4 (PEP 443)](02_python_versions/py3.04_pathlib_enum/04_singledispatch/README.md)

### [Python 3.5 · Async and Typing Arrive](02_python_versions/py3.05_async_typing/README.md)
- [async / await — Python 3.5 (PEP 492) · asyncio.run 3.7](02_python_versions/py3.05_async_typing/01_async_await/README.md)
- [The @ matrix multiplication operator — Python 3.5 (PEP 465)](02_python_versions/py3.05_async_typing/02_matrix_multiplication_operator/README.md)
- [Additional unpacking generalisations — Python 3.5 (PEP 448)](02_python_versions/py3.05_async_typing/03_unpacking_generalizations/README.md)
- [Type hints and the typing module — Python 3.5 (PEP 484)](02_python_versions/py3.05_async_typing/04_type_hints_typing/README.md)

### [Python 3.6 · Readability Wins](02_python_versions/py3.06_fstrings/README.md)
- [f-strings (formatted string literals) — Python 3.6 (PEP 498)](02_python_versions/py3.06_fstrings/01_f_strings/README.md)
- [Variable annotations — Python 3.6 (PEP 526)](02_python_versions/py3.06_fstrings/02_variable_annotations/README.md)
- [Underscores in numeric literals — Python 3.6 (PEP 515)](02_python_versions/py3.06_fstrings/03_underscores_in_numeric_literals/README.md)
- [Async generators & async comprehensions — Python 3.6 (PEP 525, PEP 530)](02_python_versions/py3.06_fstrings/04_async_generators_and_comprehensions/README.md)
- [__init_subclass__ and __set_name__ — Python 3.6 (PEP 487)](02_python_versions/py3.06_fstrings/05_init_subclass_and_set_name/README.md)
- [secrets — Python 3.6 (PEP 506)](02_python_versions/py3.06_fstrings/06_secrets/README.md)

### [Python 3.7 · Data Classes and Friends](02_python_versions/py3.07_dataclasses/README.md)
- [dataclasses — Python 3.7 (PEP 557) · kw_only/slots/match_args 3.10](02_python_versions/py3.07_dataclasses/01_dataclasses/README.md)
- [Postponed evaluation of annotations — Python 3.7 (PEP 563)](02_python_versions/py3.07_dataclasses/02_postponed_annotations/README.md)
- [contextvars — Python 3.7 (PEP 567)](02_python_versions/py3.07_dataclasses/03_contextvars/README.md)
- [breakpoint() — Python 3.7 (PEP 553)](02_python_versions/py3.07_dataclasses/04_breakpoint/README.md)
- [Guaranteed dict insertion order — Python 3.7 (language guarantee)](02_python_versions/py3.07_dataclasses/05_dict_insertion_order/README.md)
- [Module __getattr__ and __dir__ — Python 3.7 (PEP 562)](02_python_versions/py3.07_dataclasses/06_module_getattr_dir/README.md)

### [Python 3.8 · Expressive Syntax](02_python_versions/py3.08_walrus/README.md)
- [Assignment expressions (walrus `:=`) — Python 3.8 (PEP 572)](02_python_versions/py3.08_walrus/01_walrus_operator/README.md)
- [Positional-only parameters `/` — Python 3.8 (PEP 570)](02_python_versions/py3.08_walrus/02_positional_only_parameters/README.md)
- [f-string `=` specifier — Python 3.8](02_python_versions/py3.08_walrus/03_fstring_self_documenting/README.md)
- [TypedDict, Final and Literal — Python 3.8 (PEP 589, 591, 586)](02_python_versions/py3.08_walrus/04_typeddict_final_literal/README.md)
- [Protocols (structural subtyping) — Python 3.8 (PEP 544)](02_python_versions/py3.08_walrus/05_protocols/README.md)
- [functools.cached_property — Python 3.8](02_python_versions/py3.08_walrus/06_cached_property/README.md)

### [Python 3.9 · Everyday Conveniences](02_python_versions/py3.09_dict_union_generics/README.md)
- [Dict merge `|` and update `|=` — Python 3.9 (PEP 584)](02_python_versions/py3.09_dict_union_generics/01_dict_union_operators/README.md)
- [str.removeprefix() / removesuffix() — Python 3.9 (PEP 616)](02_python_versions/py3.09_dict_union_generics/02_str_removeprefix_removesuffix/README.md)
- [Built-in generic types `list[int]` — Python 3.9 (PEP 585)](02_python_versions/py3.09_dict_union_generics/03_builtin_generic_types/README.md)
- [zoneinfo — Python 3.9 (PEP 615)](02_python_versions/py3.09_dict_union_generics/04_zoneinfo/README.md)
- [typing.Annotated — Python 3.9 (PEP 593)](02_python_versions/py3.09_dict_union_generics/05_annotated/README.md)
- [functools.cache — Python 3.9](02_python_versions/py3.09_dict_union_generics/06_functools_cache/README.md)

### [Python 3.10 · Pattern Matching](02_python_versions/py3.10_pattern_matching/README.md)
- [Structural pattern matching `match`/`case` — Python 3.10 (PEP 634, 635, 636)](02_python_versions/py3.10_pattern_matching/01_structural_pattern_matching/README.md)
- [Union types with `X | Y` — Python 3.10 (PEP 604)](02_python_versions/py3.10_pattern_matching/02_union_type_operator/README.md)
- [Parenthesised context managers — Python 3.10](02_python_versions/py3.10_pattern_matching/03_parenthesized_context_managers/README.md)
- [ParamSpec, Concatenate, TypeAlias, TypeGuard — Python 3.10 (PEP 612, 613, 647)](02_python_versions/py3.10_pattern_matching/04_paramspec_typealias_typeguard/README.md)
- [zip(strict=True), itertools.pairwise & friends — Python 3.10 (PEP 618)](02_python_versions/py3.10_pattern_matching/05_zip_strict_pairwise_and_more/README.md)

### [Python 3.11 · Faster CPython and Better Errors](02_python_versions/py3.11_exception_groups/README.md)
- [ExceptionGroup and `except*` — Python 3.11 (PEP 654)](02_python_versions/py3.11_exception_groups/01_exception_groups_except_star/README.md)
- [Exception notes `add_note()` — Python 3.11 (PEP 678)](02_python_versions/py3.11_exception_groups/02_exception_notes/README.md)
- [tomllib — Python 3.11 (PEP 680)](02_python_versions/py3.11_exception_groups/03_tomllib/README.md)
- [typing.Self and LiteralString — Python 3.11 (PEP 673, 675)](02_python_versions/py3.11_exception_groups/04_self_and_literalstring/README.md)
- [asyncio.TaskGroup and asyncio.timeout — Python 3.11](02_python_versions/py3.11_exception_groups/05_asyncio_taskgroup_and_timeout/README.md)
- [Variadic generics — TypeVarTuple & Unpack — Python 3.11 (PEP 646)](02_python_versions/py3.11_exception_groups/06_variadic_generics_typevartuple/README.md)
- [TypedDict Required / NotRequired — Python 3.11 (PEP 655)](02_python_versions/py3.11_exception_groups/07_typeddict_required_notrequired/README.md)

### [Python 3.12 · New Generics Syntax](02_python_versions/py3.12_type_params/README.md)
- [Type parameter syntax — Python 3.12 (PEP 695)](02_python_versions/py3.12_type_params/01_type_parameter_syntax/README.md)
- [The `type` statement — Python 3.12 (PEP 695)](02_python_versions/py3.12_type_params/02_type_statement_aliases/README.md)
- [f-string grammar formalised — Python 3.12 (PEP 701)](02_python_versions/py3.12_type_params/03_fstring_grammar_pep701/README.md)
- [@typing.override — Python 3.12 (PEP 698)](02_python_versions/py3.12_type_params/04_override_decorator/README.md)
- [Typed **kwargs with Unpack[TypedDict] — Python 3.12 (PEP 692)](02_python_versions/py3.12_type_params/05_unpack_typeddict_kwargs/README.md)
- [itertools.batched & other 3.12 stdlib additions](02_python_versions/py3.12_type_params/06_itertools_batched_and_more/README.md)

### [Python 3.13 · Free-threading Preview and a New REPL](02_python_versions/py3.13_free_threading/README.md)
- [@warnings.deprecated — Python 3.13 (PEP 702)](02_python_versions/py3.13_free_threading/01_deprecated_decorator/README.md)
- [typing.TypeIs — Python 3.13 (PEP 742)](02_python_versions/py3.13_free_threading/02_typeis_narrowing/README.md)
- [ReadOnly TypedDict keys — Python 3.13 (PEP 705)](02_python_versions/py3.13_free_threading/03_readonly_typeddict/README.md)
- [Type parameter defaults — Python 3.13 (PEP 696)](02_python_versions/py3.13_free_threading/04_type_parameter_defaults/README.md)
- [copy.replace() — Python 3.13](02_python_versions/py3.13_free_threading/05_copy_replace/README.md)
- [Free-threaded CPython (no GIL) & JIT — Python 3.13 (PEP 703, 744) · supported in 3.14 (PEP 779)](02_python_versions/py3.13_free_threading/06_free_threading_and_jit/README.md)

### [Python 3.14 · Template Strings and Lazy Annotations](02_python_versions/py3.14_template_strings/README.md)
- [Template strings (t-strings) — Python 3.14 (PEP 750)](02_python_versions/py3.14_template_strings/01_template_strings/README.md)
- [Deferred evaluation of annotations & annotationlib — Python 3.14 (PEP 649, 749)](02_python_versions/py3.14_template_strings/02_deferred_annotations_annotationlib/README.md)
- [`except A, B:` without parentheses — Python 3.14 (PEP 758)](02_python_versions/py3.14_template_strings/03_except_without_parentheses/README.md)
- [Warnings for return/break/continue in `finally` — Python 3.14 (PEP 765)](02_python_versions/py3.14_template_strings/04_finally_control_flow_warning/README.md)
- [Multiple interpreters in the stdlib — Python 3.14 (PEP 734)](02_python_versions/py3.14_template_strings/05_concurrent_interpreters/README.md)
- [compression.zstd — Python 3.14 (PEP 784)](02_python_versions/py3.14_template_strings/06_compression_zstd/README.md)
- [3.14 stdlib highlights — pathlib copy/move, uuid7, heapq max-heap & more](02_python_versions/py3.14_template_strings/07_stdlib_highlights/README.md)

### [Python 3.15 · Lazy Imports, frozendict and sentinel](02_python_versions/py3.15_lazy_imports/README.md)
- [Explicit lazy imports — Python 3.15 (PEP 810)](02_python_versions/py3.15_lazy_imports/01_lazy_imports/README.md)
- [frozendict built-in — Python 3.15 (PEP 814)](02_python_versions/py3.15_lazy_imports/02_frozendict/README.md)
- [sentinel built-in — Python 3.15 (PEP 661)](02_python_versions/py3.15_lazy_imports/03_sentinel/README.md)
- [Unpacking in comprehensions — Python 3.15 (PEP 798)](02_python_versions/py3.15_lazy_imports/04_unpacking_in_comprehensions/README.md)
- [UTF-8 is the default encoding — Python 3.15 (PEP 686)](02_python_versions/py3.15_lazy_imports/05_utf8_default_encoding/README.md)
- [TypeForm, closed TypedDicts & disjoint bases — Python 3.15 (PEP 747, 728, 800)](02_python_versions/py3.15_lazy_imports/06_typing_typeform_closed_typeddict/README.md)
- [profiling package & Tachyon sampling profiler — Python 3.15 (PEP 799)](02_python_versions/py3.15_lazy_imports/07_profiling_sampling_tachyon/README.md)
- [3.15 stdlib highlights — math.integer, re.prefixmatch, Counter ^, TaskGroup.cancel & more](02_python_versions/py3.15_lazy_imports/08_stdlib_highlights/README.md)

## Conventions
- Examples use current idioms: `list[int]`, `X | None`, f-strings, `pathlib`, `match`, dataclasses.
- Every example function is named `example_NN_description` and prints its result.
- Temporary files go to the system temp folder, so running examples never litters this repo.
- Windows: `04_zoneinfo` needs `pip install tzdata`.

