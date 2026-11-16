# Python 3.12 · New Generics Syntax
`def f[T](x: T)` and `class Box[T]`, the `type` alias statement, a formal f-string grammar
(quotes/backslashes/comments inside), `@override`, typed `**kwargs` with `Unpack`, and
`itertools.batched`. Comprehensions are inlined (faster) and error messages improved again.

| # | Feature | In one line |
|---|---|---|
| 01 | [Type parameter syntax — Python 3.12 (PEP 695)](01_type_parameter_syntax/README.md) | declare generics inline: `def first[T](xs: list[T]) -> T` and `class Stack[T]:`. |
| 02 | [The `type` statement — Python 3.12 (PEP 695)](02_type_statement_aliases/README.md) | `type Vector = list[float]` creates a lazily evaluated, possibly generic type alias. |
| 03 | [f-string grammar formalised — Python 3.12 (PEP 701)](03_fstring_grammar_pep701/README.md) | f-strings can now reuse the same quotes, contain backslashes, comments and span lines. |
| 04 | [@typing.override — Python 3.12 (PEP 698)](04_override_decorator/README.md) | mark a method as overriding a parent method so checkers catch typos and renames. |
| 05 | [Typed **kwargs with Unpack[TypedDict] — Python 3.12 (PEP 692)](05_unpack_typeddict_kwargs/README.md) | `def f(**kw: Unpack[Options])` gives each keyword argument its own type. |
| 06 | [itertools.batched & other 3.12 stdlib additions](06_itertools_batched_and_more/README.md) | `batched("ABCDEFG", 3)` → `('A','B','C') ('D','E','F') ('G',)`. |

Run every example in this folder:
```bash
python ../../run_examples.py 02_python_versions/py3.12_type_params
```
