"""Inheritance & MRO — modern style (3.12+ for @override)."""
import json
from typing import override

MIN_VERSION = (3, 12)


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "..."

    def describe(self) -> str:
        return f"{self.name} says {self.speak()}"


class Dog(Animal):
    @override
    def speak(self) -> str:
        return "woof"


class Puppy(Dog):
    def __init__(self, name: str, age_weeks: int) -> None:
        super().__init__(name)
        self.age_weeks = age_weeks

    @override
    def speak(self) -> str:
        return super().speak() + " (squeaky)"


def example_01_override():
    print(Animal("thing").describe(), "|", Dog("rex").describe())


def example_02_super_extends_parent():
    p = Puppy("bit", 8)
    print(p.describe(), p.age_weeks)


def example_03_isinstance_issubclass():
    p = Puppy("x", 1)
    print(isinstance(p, Animal), issubclass(Puppy, Dog), issubclass(Dog, Puppy))


def example_04_mro():
    print([c.__name__ for c in Puppy.__mro__])


def example_05_diamond_cooperative_super():
    class Base:
        def setup(self): return ["Base"]
    class A(Base):
        def setup(self): return ["A"] + super().setup()
    class B(Base):
        def setup(self): return ["B"] + super().setup()
    class C(A, B):
        def setup(self): return ["C"] + super().setup()
    print(C().setup(), [k.__name__ for k in C.__mro__])


def example_06_mixins():
    class JsonMixin:
        def to_json(self) -> str:
            return json.dumps(vars(self))
    class ReprMixin:
        def __repr__(self) -> str:
            return f"{type(self).__name__}({vars(self)})"
    class User(JsonMixin, ReprMixin):
        def __init__(self, name: str): self.name = name
    u = User("ann")
    print(u, u.to_json())


def example_07_composition_over_inheritance():
    class Engine:
        def start(self) -> str: return "engine started"
    class Car:
        def __init__(self): self.engine = Engine()       # has-a
        def start(self) -> str: return f"car: {self.engine.start()}"
    print(Car().start())


def example_08_extending_builtins():
    class UpperDict(dict):
        def __setitem__(self, key: str, value) -> None:
            super().__setitem__(key.upper(), value)
    d = UpperDict(); d["name"] = "ann"
    print(d)


def example_09_calling_specific_parent():
    class A:
        def hello(self): return "A"
    class B(A):
        def hello(self): return "B+" + A.hello(self)
    print(B().hello())


def example_10_init_subclass_hook():
    class Plugin:
        registry: list[str] = []
        def __init_subclass__(cls, **kw):
            super().__init_subclass__(**kw)
            Plugin.registry.append(cls.__name__)
    class CsvExport(Plugin): ...
    class PdfExport(Plugin): ...
    print(Plugin.registry)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
