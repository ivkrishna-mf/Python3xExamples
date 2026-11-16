"""X | Y union types — Python 3.10+ (PEP 604)."""
import types
from typing import Optional, Union, get_args

MIN_VERSION = (3, 10)


def example_01_optional_value():
    def find(uid: int) -> str | None:
        return {1: "ann"}.get(uid)
    print(find(1), find(2))


def example_02_multiple_types():
    def to_int(v: int | str | float) -> int:
        return int(v)
    print(to_int("7") + to_int(2.9))


def example_03_isinstance_with_union():
    print([isinstance(v, int | float) for v in (1, 2.5, "3")])


def example_04_runtime_type():
    u = int | str
    print(type(u), isinstance(u, types.UnionType))


def example_05_equivalent_to_typing_union():
    print((int | None) == Optional[int], (int | str) == Union[int, str])


def example_06_get_args():
    print(get_args(int | str | None))


def example_07_order_and_duplicates():
    print(int | str == str | int, int | int)


def example_08_with_generics():
    def first(xs: list[int] | tuple[int, ...]) -> int | None:
        return xs[0] if xs else None
    print(first([5, 6]), first(()))


def example_09_issubclass():
    print(issubclass(bool, int | str))


def example_10_in_dataclass_fields():
    from dataclasses import dataclass
    @dataclass
    class Config:
        path: str
        timeout: float | None = None
        retries: int | None = None
    print(Config("/etc/app.toml", timeout=2.5))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
