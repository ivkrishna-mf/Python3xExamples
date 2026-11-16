"""functools.singledispatch — Python 3.4+ (PEP 443)."""
import sys
from datetime import date
from decimal import Decimal
from functools import singledispatch, singledispatchmethod

MIN_VERSION = (3, 8)


@singledispatch
def to_json(obj):
    raise TypeError(f"can't serialise {type(obj).__name__}")


@to_json.register
def _(obj: int):
    return str(obj)


@to_json.register
def _(obj: str):
    return f'"{obj}"'


@to_json.register
def _(obj: list):
    return "[" + ",".join(to_json(x) for x in obj) + "]"


@to_json.register
def _(obj: dict):
    return "{" + ",".join(f"{to_json(k)}:{to_json(v)}" for k, v in obj.items()) + "}"


def example_01_basic_dispatch():
    print(to_json(42), to_json("hi"))


def example_02_recursive_containers():
    print(to_json({"ids": [1, 2], "name": "ann"}))


def example_03_unregistered_type():
    try:
        to_json(3.5j)
    except TypeError as exc:
        print("TypeError:", exc)


def example_04_register_without_annotation():
    @to_json.register(date)
    def _(obj):
        return f'"{obj.isoformat()}"'
    print(to_json([date(2026, 11, 16)]))


def example_05_subclasses_inherit_dispatch():
    class UserId(int): ...
    print(to_json(UserId(7)))


def example_06_inspect_registry():
    print([t.__name__ for t in to_json.registry if t is not object][:5])


def example_07_dispatch_lookup():
    print(to_json.dispatch(bool).__name__, "handles bool (bool is an int)")


def example_08_singledispatchmethod():
    class Formatter:
        @singledispatchmethod
        def fmt(self, x):
            return str(x)
        @fmt.register
        def _(self, x: float):
            return f"{x:.2f}"
        @fmt.register
        def _(self, x: Decimal):
            return f"${x}"
    f = Formatter()
    print(f.fmt(1), f.fmt(3.14159), f.fmt(Decimal("9.99")))


def example_09_union_registration_311():
    if sys.version_info >= (3, 11):
        @singledispatch
        def kind(x): return "other"
        @kind.register
        def _(x: int | float): return "number"
        print(kind(1), kind(2.5), kind("s"))
    else:
        print("needs 3.11+")


def example_10_plugin_style_extension():
    class Money:
        def __init__(self, cents): self.cents = cents
    # a different module could add this without touching to_json's source:
    to_json.register(Money, lambda m: f'{{"cents":{m.cents}}}')
    print(to_json(Money(1999)))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
