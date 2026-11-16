"""@override — Python 3.12+ (PEP 698)."""
import json
import unittest
from abc import ABC, abstractmethod
from typing import override

MIN_VERSION = (3, 12)


class Exporter:
    def export(self, data: dict) -> str:
        return str(data)

    def file_extension(self) -> str:
        return "txt"


class JsonExporter(Exporter):
    @override
    def export(self, data: dict) -> str:
        return json.dumps(data)

    @override
    def file_extension(self) -> str:
        return "json"


def example_01_basic_override():
    print(JsonExporter().export({"a": 1}), JsonExporter().file_extension())


def example_02_runtime_marker():
    print(JsonExporter.export.__override__)


def example_03_catches_typos_statically():
    class Broken(Exporter):
        @override
        def exprot(self, data: dict) -> str:   # typo! mypy/pyright: no base method 'exprot'
            return ""
    print("runtime is fine, checker flags Broken.exprot")


def example_04_with_abstract_base():
    class Shape(ABC):
        @abstractmethod
        def area(self) -> float: ...
    class Square(Shape):
        def __init__(self, s: float): self.s = s
        @override
        def area(self) -> float: return self.s ** 2
    print(Square(3).area())


def example_05_dunder_methods():
    class Money:
        def __init__(self, cents: int): self.cents = cents
        @override
        def __repr__(self) -> str: return f"Money({self.cents / 100:.2f})"
        @override
        def __eq__(self, other: object) -> bool:
            return isinstance(other, Money) and other.cents == self.cents
        @override
        def __hash__(self) -> int: return hash(self.cents)
    print(Money(199), Money(1) == Money(1))


def example_06_test_case_setup():
    class MyTest(unittest.TestCase):
        @override
        def setUp(self) -> None:
            self.value = 42
        def test_value(self) -> None:
            self.assertEqual(self.value, 42)
    result = unittest.TextTestRunner(verbosity=0).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(MyTest))
    print("tests ok:", result.wasSuccessful())


def example_07_property_override():
    class Animal:
        @property
        def sound(self) -> str: return "..."
    class Dog(Animal):
        @property
        @override
        def sound(self) -> str: return "woof"
    print(Dog().sound)


def example_08_classmethod_override():
    class Model:
        @classmethod
        def table(cls) -> str: return cls.__name__.lower()
    class Person(Model):
        @classmethod
        @override
        def table(cls) -> str: return "people"
    print(Model.table(), Person.table())


def example_09_multi_level():
    class A:
        def run(self) -> str: return "A"
    class B(A):
        @override
        def run(self) -> str: return "B>" + super().run()
    class C(B):
        @override
        def run(self) -> str: return "C>" + super().run()
    print(C().run())


def example_10_exception_subclass():
    class AppError(Exception):
        def __init__(self, code: int, msg: str):
            super().__init__(msg); self.code = code
        @override
        def __str__(self) -> str: return f"[{self.code}] {self.args[0]}"
    print(AppError(404, "not found"))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
