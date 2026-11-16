# Core Language · Functions and Functional Programming
Defining and calling functions, scopes and closures, lambdas and higher-order functions,
decorators, iterators and generators, and the `itertools`/`functools` toolkits. Examples
use modern syntax, including 3.12 type parameters where they help.

| # | Feature | In one line |
|---|---|---|
| 01 | [Functions and arguments](01_functions_and_arguments/README.md) | reusable blocks of code with positional, keyword, default, variadic, keyword-only and positional-only parameters. |
| 02 | [Scope (LEGB), global, nonlocal and closures](02_scope_and_closures/README.md) | names resolve Local → Enclosing → Global → Built-in; inner functions can capture outer variables. |
| 03 | [Lambdas and higher-order functions (map, filter, sorted, reduce, partial)](03_lambda_and_higher_order/README.md) | pass functions as arguments; use small anonymous `lambda`s for one-off keys and callbacks. |
| 04 | [Decorators](04_decorators/README.md) | `@deco` wraps a function or class to add behaviour without changing its code. |
| 05 | [Iterators and generators](05_iterators_and_generators/README.md) | produce values lazily, one at a time, with `yield` — constant memory for any size of data. |
| 06 | [itertools and functools toolkits](06_itertools_and_functools/README.md) | fast, composable building blocks for iteration and function manipulation. |

Run every example in this folder:
```bash
python ../../run_examples.py 01_core_language/02_functions_and_functional
```
