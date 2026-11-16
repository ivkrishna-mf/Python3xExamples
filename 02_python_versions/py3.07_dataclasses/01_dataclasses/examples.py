"""dataclasses — Python 3.7+ (PEP 557); slots/kw_only need 3.10+."""
import sys
from dataclasses import asdict, astuple, dataclass, field, replace

MIN_VERSION = (3, 7)


@dataclass
class Point:
    x: float
    y: float = 0.0


def example_01_generated_init_repr_eq():
    print(Point(1, 2), Point(1, 2) == Point(1, 2))


def example_02_default_factory_for_mutables():
    @dataclass
    class Cart:
        items: list = field(default_factory=list)
    a, b = Cart(), Cart()
    a.items.append("apple")
    print(a, b)


def example_03_frozen_and_hashable():
    @dataclass(frozen=True)
    class Coord:
        lat: float
        lon: float
    c = Coord(51.5, -0.1)
    print({c: "London"})
    try:
        c.lat = 0
    except Exception as exc:
        print(type(exc).__name__, exc)


def example_04_ordering():
    @dataclass(order=True)
    class Version:
        major: int
        minor: int
        patch: int = 0
    print(sorted([Version(1, 10), Version(1, 2), Version(0, 9, 9)]))


def example_05_post_init_validation():
    @dataclass
    class Account:
        owner: str
        balance: float = 0.0
        def __post_init__(self):
            if self.balance < 0:
                raise ValueError("balance cannot be negative")
    try:
        Account("ann", -5)
    except ValueError as exc:
        print("ValueError:", exc)


def example_06_asdict_astuple():
    p = Point(3, 4)
    print(asdict(p), astuple(p))


def example_07_replace_creates_modified_copy():
    p = Point(1, 1)
    print(replace(p, y=99), p)


def example_08_field_options():
    @dataclass
    class User:
        name: str
        password: str = field(repr=False)
        login_count: int = field(default=0, compare=False)
    print(User("ann", "s3cret"))


def example_09_inheritance():
    @dataclass
    class Animal:
        name: str
    @dataclass
    class Dog(Animal):
        breed: str = "mixed"
    print(Dog("rex", "collie"))


def example_10_slots_and_kw_only_310():
    if sys.version_info >= (3, 10):
        @dataclass(slots=True, kw_only=True)
        class Settings:
            debug: bool = False
            workers: int = 4
        s = Settings(workers=8)
        print(s, hasattr(s, "__dict__"))
    else:
        print("slots/kw_only need 3.10+")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
