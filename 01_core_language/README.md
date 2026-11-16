# Core Language

Features Python has had since its first releases (1991 →), taught with **current syntax** (type hints, f-strings, `match`, dataclasses, pathlib). Start here if you are learning Python.

## [Core Language · Basics](01_basics/README.md)

| Feature | In one line |
|---|---|
| [Variables, names and built-in types](01_basics/01_variables_and_types/README.md) | names point to objects; every object has a type, an identity and a value. |
| [Numbers: int, float, complex, Decimal, Fraction](01_basics/02_numbers_and_math/README.md) | arbitrary-precision ints, IEEE floats, exact decimals and fractions, plus the `math` module. |
| [Strings](01_basics/03_strings/README.md) | immutable Unicode text with rich methods, slicing and f-string formatting. |
| [Lists](01_basics/04_lists/README.md) | ordered, mutable, growable sequences — Python's workhorse collection. |
| [Tuples and named tuples](01_basics/05_tuples/README.md) | immutable, hashable sequences — ideal for fixed records and multiple return values. |
| [Dictionaries](01_basics/06_dictionaries/README.md) | fast key → value mappings, insertion-ordered, with comprehensions and merge operators. |
| [Sets and frozensets](01_basics/07_sets/README.md) | unordered collections of unique, hashable items with fast membership and set algebra. |
| [Conditionals: if / elif / else, conditional expressions, match](01_basics/08_conditionals_and_match/README.md) | branch on conditions; use `match` when you branch on the *shape* of data. |
| [Loops: for, while, break/continue, else, enumerate, zip](01_basics/09_loops/README.md) | `for` iterates over any iterable; `while` repeats while a condition holds. |
| [Comprehensions and generator expressions](01_basics/10_comprehensions/README.md) | build lists, dicts, sets or lazy generators from iterables in one readable expression. |
| [collections: Counter, defaultdict, deque, namedtuple, ChainMap, OrderedDict](01_basics/11_collections_module/README.md) | specialised containers that replace common hand-written dict/list patterns. |

## [Core Language · Functions and Functional Programming](02_functions_and_functional/README.md)

| Feature | In one line |
|---|---|
| [Functions and arguments](02_functions_and_functional/01_functions_and_arguments/README.md) | reusable blocks of code with positional, keyword, default, variadic, keyword-only and positional-only parameters. |
| [Scope (LEGB), global, nonlocal and closures](02_functions_and_functional/02_scope_and_closures/README.md) | names resolve Local → Enclosing → Global → Built-in; inner functions can capture outer variables. |
| [Lambdas and higher-order functions (map, filter, sorted, reduce, partial)](02_functions_and_functional/03_lambda_and_higher_order/README.md) | pass functions as arguments; use small anonymous `lambda`s for one-off keys and callbacks. |
| [Decorators](02_functions_and_functional/04_decorators/README.md) | `@deco` wraps a function or class to add behaviour without changing its code. |
| [Iterators and generators](02_functions_and_functional/05_iterators_and_generators/README.md) | produce values lazily, one at a time, with `yield` — constant memory for any size of data. |
| [itertools and functools toolkits](02_functions_and_functional/06_itertools_and_functools/README.md) | fast, composable building blocks for iteration and function manipulation. |

## [Core Language · Object-Oriented Programming](03_object_oriented/README.md)

| Feature | In one line |
|---|---|
| [Classes and objects](03_object_oriented/01_classes_and_objects/README.md) | bundle data (attributes) and behaviour (methods) into your own types. |
| [Inheritance, super() and the MRO](03_object_oriented/02_inheritance_and_mro/README.md) | reuse and specialise behaviour from parent classes; `super()` follows the method resolution order. |
| [Special ("dunder") methods and operator overloading](03_object_oriented/03_dunder_methods/README.md) | implement `__len__`, `__eq__`, `__add__`, `__iter__`, `__getitem__`, `__call__`… so your objects work with Python syntax and built-ins. |
| [Properties, descriptors and __slots__](03_object_oriented/04_properties_and_descriptors/README.md) | control attribute access — computed attributes, validation and memory-lean objects. |
| [Abstract base classes (abc) and Protocols](03_object_oriented/05_abstract_classes_and_protocols/README.md) | define interfaces — nominal (ABC: must inherit) or structural (Protocol: just match the methods). |
| [Metaclasses and dynamic class creation](03_object_oriented/06_metaclasses_and_class_creation/README.md) | classes are objects created by a metaclass (`type` by default) — you can customise how classes are built. |

## [Core Language · Errors, Resources, Modules, I/O and Concurrency](04_errors_io_modules_concurrency/README.md)

| Feature | In one line |
|---|---|
| [Exceptions: try / except / else / finally, raise, custom errors](04_errors_io_modules_concurrency/01_exceptions/README.md) | signal and handle errors explicitly; catch specific exceptions, clean up in `finally`. |
| [Context managers: the `with` statement and contextlib](04_errors_io_modules_concurrency/02_context_managers/README.md) | guarantee setup and cleanup (close files, release locks, roll back transactions) even when errors happen. |
| [Modules, packages and imports](04_errors_io_modules_concurrency/03_modules_and_packages/README.md) | organise code into files (modules) and folders (packages) and import what you need. |
| [File I/O and serialisation (pathlib, open, json, csv, pickle)](04_errors_io_modules_concurrency/04_file_io_and_serialization/README.md) | read and write text, binary, JSON, CSV and Python objects safely and portably. |
| [Concurrency: threads, processes and asyncio](04_errors_io_modules_concurrency/05_concurrency_threads_processes_async/README.md) | run work concurrently — threads for I/O, processes (or free-threaded builds) for CPU, asyncio for massive I/O concurrency. |

