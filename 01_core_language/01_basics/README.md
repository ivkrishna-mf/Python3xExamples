# Core Language · Basics
The building blocks Python has had since the beginning (1991 → today), written in modern
Python style: f-strings, type hints with built-in generics and `X | None`, `match`, and
comprehensions. Each README shows when the feature first appeared.

| # | Feature | In one line |
|---|---|---|
| 01 | [Variables, names and built-in types](01_variables_and_types/README.md) | names point to objects; every object has a type, an identity and a value. |
| 02 | [Numbers: int, float, complex, Decimal, Fraction](02_numbers_and_math/README.md) | arbitrary-precision ints, IEEE floats, exact decimals and fractions, plus the `math` module. |
| 03 | [Strings](03_strings/README.md) | immutable Unicode text with rich methods, slicing and f-string formatting. |
| 04 | [Lists](04_lists/README.md) | ordered, mutable, growable sequences — Python's workhorse collection. |
| 05 | [Tuples and named tuples](05_tuples/README.md) | immutable, hashable sequences — ideal for fixed records and multiple return values. |
| 06 | [Dictionaries](06_dictionaries/README.md) | fast key → value mappings, insertion-ordered, with comprehensions and merge operators. |
| 07 | [Sets and frozensets](07_sets/README.md) | unordered collections of unique, hashable items with fast membership and set algebra. |
| 08 | [Conditionals: if / elif / else, conditional expressions, match](08_conditionals_and_match/README.md) | branch on conditions; use `match` when you branch on the *shape* of data. |
| 09 | [Loops: for, while, break/continue, else, enumerate, zip](09_loops/README.md) | `for` iterates over any iterable; `while` repeats while a condition holds. |
| 10 | [Comprehensions and generator expressions](10_comprehensions/README.md) | build lists, dicts, sets or lazy generators from iterables in one readable expression. |
| 11 | [collections: Counter, defaultdict, deque, namedtuple, ChainMap, OrderedDict](11_collections_module/README.md) | specialised containers that replace common hand-written dict/list patterns. |

Run every example in this folder:
```bash
python ../../run_examples.py 01_core_language/01_basics
```
