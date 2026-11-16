"""Properties, descriptors & __slots__ — modern style."""
import sys
from dataclasses import dataclass
from functools import cached_property

MIN_VERSION = (3, 10)


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius                 # goes through the setter

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value < 0:
            raise ValueError("radius must be >= 0")
        self._radius = value

    @property
    def area(self) -> float:                 # computed, read-only
        return 3.14159 * self._radius ** 2


def example_01_getter_and_setter():
    c = Circle(2)
    c.radius = 3
    print(c.radius, round(c.area, 2))


def example_02_validation():
    try:
        Circle(-1)
    except ValueError as exc:
        print("ValueError:", exc)


def example_03_read_only_property():
    try:
        Circle(1).area = 10
    except AttributeError as exc:
        print("AttributeError:", exc)


def example_04_reusable_descriptor():
    class Positive:
        def __set_name__(self, owner, name): self.name = "_" + name
        def __get__(self, obj, objtype=None):
            return self if obj is None else getattr(obj, self.name)
        def __set__(self, obj, value):
            if value <= 0:
                raise ValueError(f"{self.name[1:]} must be > 0, got {value}")
            setattr(obj, self.name, value)
    class Product:
        price = Positive()
        qty = Positive()
        def __init__(self, price, qty): self.price, self.qty = price, qty
    p = Product(9.99, 3)
    print(p.price, p.qty)
    try:
        p.qty = 0
    except ValueError as exc:
        print("ValueError:", exc)


def example_05_cached_property():
    class Report:
        @cached_property
        def data(self):
            print("  computing once...")
            return [1, 2, 3]
    r = Report(); r.data; print(r.data)


def example_06_slots_save_memory():
    class P1:
        def __init__(self): self.x = self.y = 0
    class P2:
        __slots__ = ("x", "y")
        def __init__(self): self.x = self.y = 0
    print(sys.getsizeof(P1().__dict__) + sys.getsizeof(P1()), ">", sys.getsizeof(P2()))


def example_07_slots_prevent_typos():
    class P:
        __slots__ = ("x",)
    p = P()
    try:
        p.xx = 1
    except AttributeError as exc:
        print("AttributeError:", exc)


def example_08_dataclass_slots():
    @dataclass(slots=True)
    class Pixel:
        x: int
        y: int
    print(Pixel(1, 2), hasattr(Pixel(1, 2), "__dict__"))


def example_09_deleter():
    class Session:
        def __init__(self): self._token = "abc"
        @property
        def token(self): return self._token
        @token.deleter
        def token(self):
            print("  revoking token"); self._token = None
    s = Session(); del s.token
    print(s.token)


def example_10_how_methods_are_descriptors():
    class A:
        def f(self): return "bound"
    a = A()
    print(A.__dict__["f"].__get__(a, A)(), type(A.f).__name__, type(a.f).__name__)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
