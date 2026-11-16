"""Classes & objects — modern style (3.11+ for Self)."""
from dataclasses import dataclass, field
from typing import ClassVar, Self

MIN_VERSION = (3, 11)


class BankAccount:
    bank_name: ClassVar[str] = "PyBank"           # class attribute (shared)

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner                         # instance attributes
        self.balance = balance

    def deposit(self, amount: float) -> Self:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount
        return self

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self.balance:.2f})"


def example_01_create_instances():
    a = BankAccount("ann", 100)
    b = BankAccount("bob")
    print(a, b)


def example_02_methods_and_chaining():
    print(BankAccount("ann").deposit(50).deposit(25))


def example_03_class_vs_instance_attributes():
    a, b = BankAccount("a"), BankAccount("b")
    a.bank_name = "Shadowed"
    print(a.bank_name, b.bank_name, BankAccount.bank_name)


def example_04_classmethod_alternative_constructor():
    @dataclass
    class Color:
        r: int
        g: int
        b: int
        @classmethod
        def from_hex(cls, code: str) -> Self:
            code = code.lstrip("#")
            return cls(*(int(code[i:i + 2], 16) for i in (0, 2, 4)))
    print(Color.from_hex("#ff8800"))


def example_05_staticmethod_utility():
    class Temperature:
        @staticmethod
        def c_to_f(c: float) -> float:
            return c * 9 / 5 + 32
    print(Temperature.c_to_f(37))


def example_06_dataclass_modern_default():
    @dataclass
    class Order:
        id: int
        items: list[str] = field(default_factory=list)
        def total_items(self) -> int:
            return len(self.items)
    o = Order(1, ["pen", "ink"])
    print(o, o.total_items())


def example_07_vars_and_dynamic_attributes():
    acc = BankAccount("cy", 5)
    acc.nickname = "c"                      # instances are open by default
    print(vars(acc), getattr(acc, "missing", "default"), hasattr(acc, "owner"))


def example_08_encapsulation_conventions():
    class Service:
        def __init__(self):
            self.public = 1
            self._internal = 2              # "please don't touch"
            self.__mangled = 3              # name-mangled to _Service__mangled
    s = Service()
    print(s.public, s._internal, s._Service__mangled)


def example_09_object_equality():
    @dataclass(frozen=True)
    class Point:
        x: int
        y: int
    print(Point(1, 2) == Point(1, 2), len({Point(1, 2), Point(1, 2)}))


def example_10_type_and_isinstance():
    acc = BankAccount("d")
    print(type(acc).__name__, isinstance(acc, BankAccount), BankAccount.__mro__)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
