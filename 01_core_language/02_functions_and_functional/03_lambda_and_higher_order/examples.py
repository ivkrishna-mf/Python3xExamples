"""Lambdas & higher-order functions — modern style."""
from collections.abc import Callable
from functools import partial, reduce
from operator import attrgetter, itemgetter, mul

MIN_VERSION = (3, 9)
users = [{"name": "ann", "age": 31}, {"name": "bob", "age": 25}, {"name": "cy", "age": 40}]


def example_01_lambda_as_sort_key():
    print([u["name"] for u in sorted(users, key=lambda u: u["age"], reverse=True)])


def example_02_itemgetter_instead_of_lambda():
    print(max(users, key=itemgetter("age"))["name"])


def example_03_map_and_filter_vs_comprehension():
    nums = [1, 2, 3, 4]
    print(list(map(lambda n: n * 10, filter(lambda n: n % 2 == 0, nums))))
    print([n * 10 for n in nums if n % 2 == 0])


def example_04_reduce():
    print(reduce(mul, [1, 2, 3, 4, 5]), reduce(lambda acc, s: acc + len(s), ["ab", "cde"], 0))


def example_05_partial():
    def power(base: float, exp: float) -> float:
        return base ** exp
    square = partial(power, exp=2)
    print(square(9), int("ff", base=16), partial(int, base=2)("1011"))


def example_06_function_returning_function():
    def make_discount(pct: float) -> Callable[[float], float]:
        return lambda price: round(price * (1 - pct / 100), 2)
    print(make_discount(15)(200))


def example_07_compose():
    def compose(*fns: Callable) -> Callable:
        return lambda x: reduce(lambda acc, f: f(acc), fns, x)
    pipeline = compose(str.strip, str.lower, lambda s: s.replace(" ", "-"))
    print(pipeline("  Hello Big World "))


def example_08_strategy_dict():
    strategies: dict[str, Callable[[list[int]], float]] = {
        "mean": lambda xs: sum(xs) / len(xs), "max": max, "min": min}
    print({name: fn([4, 8, 6]) for name, fn in strategies.items()})


def example_09_attrgetter_multi_key():
    from dataclasses import dataclass
    @dataclass
    class Emp:
        dept: str
        name: str
    staff = [Emp("ops", "zed"), Emp("dev", "bob"), Emp("dev", "amy")]
    print([e.name for e in sorted(staff, key=attrgetter("dept", "name"))])


def example_10_callbacks():
    def download(url: str, on_done: Callable[[str], None]) -> None:
        on_done(f"{url} downloaded")
    download("https://x.io/file", lambda msg: print("callback:", msg))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
