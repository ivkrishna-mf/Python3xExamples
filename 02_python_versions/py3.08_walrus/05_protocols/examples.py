"""Protocols — Python 3.8+ (PEP 544)."""
import io
from typing import Iterable, Protocol, TypeVar, runtime_checkable

MIN_VERSION = (3, 8)


class Greeter(Protocol):
    def greet(self, name: str) -> str: ...


class English:
    def greet(self, name: str) -> str:
        return f"Hello {name}"


class Hindi:
    def greet(self, name: str) -> str:
        return f"Namaste {name}"


def welcome(g: Greeter, name: str) -> None:
    print(g.greet(name))


def example_01_no_inheritance_needed():
    welcome(English(), "ann")
    welcome(Hindi(), "bob")


def example_02_runtime_checkable():
    @runtime_checkable
    class Closeable(Protocol):
        def close(self) -> None: ...
    print(isinstance(io.StringIO(), Closeable), isinstance(42, Closeable))


def example_03_protocol_with_attribute():
    class Named(Protocol):
        name: str
    class User:
        def __init__(self): self.name = "ann"
    def show(x: Named) -> str: return x.name
    print(show(User()))


def example_04_repository_interface():
    class UserRepo(Protocol):
        def get(self, uid: int) -> str: ...
    class InMemoryRepo:
        def __init__(self): self.data = {1: "ann"}
        def get(self, uid: int) -> str: return self.data[uid]
    def service(repo: UserRepo) -> str:
        return repo.get(1).title()
    print(service(InMemoryRepo()))


def example_05_test_fake():
    class Clock(Protocol):
        def now(self) -> float: ...
    class FakeClock:
        def now(self) -> float: return 1_700_000_000.0
    def timestamp_msg(clock: Clock) -> str:
        return f"at {clock.now():.0f}"
    print(timestamp_msg(FakeClock()))


def example_06_generic_protocol():
    T = TypeVar("T", covariant=True)
    class Source(Protocol[T]):
        def read(self) -> T: ...
    class IntSource:
        def read(self) -> int: return 7
    def consume(s: "Source[int]") -> int: return s.read() * 2
    print(consume(IntSource()))


def example_07_protocol_for_operators():
    class SupportsLessThan(Protocol):
        def __lt__(self, other) -> bool: ...
    def smallest(items: Iterable[SupportsLessThan]):
        return min(items)
    print(smallest([3, 1, 2]), smallest(["b", "a"]))


def example_08_callback_protocol():
    class OnEvent(Protocol):
        def __call__(self, name: str, *, payload: dict) -> None: ...
    def emit(cb: OnEvent) -> None:
        cb("saved", payload={"id": 1})
    def handler(name: str, *, payload: dict) -> None:
        print("event", name, payload)
    emit(handler)


def example_09_explicit_subclass_gives_defaults():
    class Shape(Protocol):
        def area(self) -> float: ...
        def describe(self) -> str:
            return f"shape with area {self.area():.1f}"
    class Square(Shape):           # explicit opt-in inherits describe()
        def __init__(self, s): self.s = s
        def area(self) -> float: return self.s ** 2
    print(Square(3).describe())


def example_10_isinstance_only_checks_names():
    @runtime_checkable
    class HasLen(Protocol):
        def __len__(self) -> int: ...
    print([isinstance(x, HasLen) for x in ([], "abc", 5, {})])


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
