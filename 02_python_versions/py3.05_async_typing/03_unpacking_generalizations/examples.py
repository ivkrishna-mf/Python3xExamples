"""Unpacking generalisations — Python 3.5+ (PEP 448)."""
MIN_VERSION = (3, 5)


def example_01_concat_lists():
    a, b = [1, 2], [3, 4]
    print([*a, *b, 5])


def example_02_merge_dicts_with_precedence():
    defaults = {"host": "localhost", "port": 5432}
    overrides = {"port": 6543}
    print({**defaults, **overrides})


def example_03_multiple_star_args_in_call():
    print(*[1, 2], *"ab", sep="-")


def example_04_multiple_kwargs_in_call():
    def connect(**kw): return kw
    print(connect(**{"user": "ann"}, **{"db": "prod"}, timeout=5))


def example_05_set_union_display():
    print({*{1, 2}, *[2, 3], 4})


def example_06_tuple_from_iterables():
    print((*range(3), *"xy"))


def example_07_unpack_any_iterable():
    print([*"hi", *range(2), *{"k": 1}])   # dicts unpack their keys


def example_08_copy_and_extend():
    base = {"a": 1}
    new = {**base, "b": 2}
    print(base, new)


def example_09_duplicate_kwargs_error():
    def f(**kw): return kw
    try:
        f(**{"x": 1}, **{"x": 2})
    except TypeError as exc:
        print("TypeError:", exc)


def example_10_flatten_one_level():
    nested = [[1, 2], [3], [4, 5]]
    flat = [*nested[0], *nested[1], *nested[2]]
    print(flat, "(3.15+: [*x for x in nested])")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
