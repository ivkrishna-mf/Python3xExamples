"""copy.replace — Python 3.13+."""
import copy
from collections import namedtuple
from dataclasses import dataclass
from datetime import date, datetime
from types import SimpleNamespace

MIN_VERSION = (3, 13)


@dataclass(frozen=True)
class Settings:
    env: str
    debug: bool = False
    workers: int = 4


def example_01_frozen_dataclass():
    prod = Settings("prod")
    print(copy.replace(prod, workers=16), prod)


def example_02_namedtuple():
    Point = namedtuple("Point", "x y")
    print(copy.replace(Point(1, 2), y=99))


def example_03_datetime():
    print(copy.replace(datetime(2026, 11, 16, 9, 30), hour=18, minute=0))


def example_04_date_first_of_month():
    print(copy.replace(date(2026, 11, 16), day=1))


def example_05_simplenamespace():
    ns = SimpleNamespace(a=1, b=2)
    print(copy.replace(ns, b=20))


def example_06_custom_class():
    class Money:
        def __init__(self, amount, currency):
            self.amount, self.currency = amount, currency
        def __replace__(self, **changes):
            return Money(changes.get("amount", self.amount), changes.get("currency", self.currency))
        def __repr__(self): return f"Money({self.amount} {self.currency})"
    print(copy.replace(Money(10, "USD"), currency="EUR"))


def example_07_generic_update_function():
    def bump(obj, field, by=1):
        return copy.replace(obj, **{field: getattr(obj, field) + by})
    print(bump(Settings("dev"), "workers"), bump(date(2026, 1, 1), "day", 9))


def example_08_unknown_field_error():
    try:
        copy.replace(Settings("dev"), colour="red")
    except TypeError as exc:
        print("TypeError:", exc)


def example_09_shallow_copy_semantics():
    @dataclass
    class Team:
        name: str
        members: list
    a = Team("core", ["ann"])
    b = copy.replace(a, name="core-2")
    b.members.append("bob")
    print(a.members, "<- shared list (shallow)")


def example_10_unsupported_type():
    try:
        copy.replace([1, 2], x=1)
    except TypeError as exc:
        print("TypeError:", exc)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
