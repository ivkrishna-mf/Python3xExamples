"""Tuples & NamedTuple — modern style."""
from collections import namedtuple
from typing import NamedTuple

MIN_VERSION = (3, 8)


class Point(NamedTuple):
    x: float
    y: float = 0.0

    def distance(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


def example_01_create():
    t = (1, "a", 2.5)
    single = (42,)            # trailing comma makes a 1-tuple
    print(t, single, type(single).__name__, ())


def example_02_packing_unpacking():
    point = 3, 4
    x, y = point
    print(x, y)


def example_03_multiple_return_values():
    def min_max(nums: list[int]) -> tuple[int, int]:
        return min(nums), max(nums)
    lo, hi = min_max([4, 1, 9])
    print(lo, hi)


def example_04_as_dict_keys():
    distances = {("NYC", "LA"): 3936, ("NYC", "SF"): 4130}
    print(distances[("NYC", "LA")])


def example_05_immutability():
    t = (1, [2, 3])
    t[1].append(4)            # the list inside is still mutable
    print(t)


def example_06_namedtuple_class():
    p = Point(3, 4)
    print(p, p.x, p.distance(), p[0])


def example_07_namedtuple_helpers():
    p = Point(1, 2)
    print(p._asdict(), p._replace(y=10), Point._fields)


def example_08_functional_namedtuple():
    Color = namedtuple("Color", "r g b")
    print(Color(255, 128, 0))


def example_09_tuple_methods_and_comparison():
    t = (1, 2, 2, 3)
    print(t.count(2), t.index(3), (1, 2) < (1, 3), sorted([(2, "b"), (1, "z"), (1, "a")]))


def example_10_star_unpacking():
    record = ("2026-11-16", "INFO", "service", "started", "ok")
    date, level, *msg = record
    print(date, level, msg)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
