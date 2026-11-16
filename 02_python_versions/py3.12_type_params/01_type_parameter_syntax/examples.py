"""Type parameter syntax — Python 3.12+ (PEP 695)."""
import functools
from collections.abc import Callable, Iterable

MIN_VERSION = (3, 12)


def first[T](items: list[T]) -> T:
    return items[0]


class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)


def example_01_generic_function():
    print(first([3, 2, 1]), first(["a", "b"]))


def example_02_generic_class():
    s = Stack[int]()
    s.push(1); s.push(2)
    print(s.pop(), len(s))


def example_03_bound():
    def longest[S: str](a: S, b: S) -> S:
        return a if len(a) >= len(b) else b
    print(longest("python", "go"))


def example_04_constraints():
    def add[N: (int, float)](a: N, b: N) -> N:
        return a + b
    print(add(1, 2), add(1.5, 2.5))


def example_05_multiple_params():
    def to_dict[K, V](pairs: Iterable[tuple[K, V]]) -> dict[K, V]:
        return dict(pairs)
    print(to_dict([("a", 1), ("b", 2)]))


def example_06_paramspec_decorator():
    def logged[**P, R](fn: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(fn)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            print(f"  calling {fn.__name__}")
            return fn(*args, **kwargs)
        return wrapper
    @logged
    def greet(name: str, *, loud: bool = False) -> str:
        return name.upper() if loud else name
    print(greet("ann", loud=True))


def example_07_typevartuple():
    def as_tuple[*Ts](*args: *Ts) -> tuple[*Ts]:
        return args
    print(as_tuple(1, "x", None))


def example_08_generic_dataclass():
    from dataclasses import dataclass
    @dataclass
    class Pair[A, B]:
        left: A
        right: B
        def swap(self) -> "Pair[B, A]":
            return Pair(self.right, self.left)
    print(Pair(1, "one").swap())


def example_09_introspection():
    print(first.__type_params__, Stack.__type_params__)
    (T,) = Stack.__type_params__
    print(type(T).__name__, T.__name__)


def example_10_generic_protocol():
    from typing import Protocol
    class Repository[T](Protocol):
        def get(self, key: str) -> T: ...
    class MemoryRepo[T]:
        def __init__(self, data: dict[str, T]) -> None:
            self.data = data
        def get(self, key: str) -> T:
            return self.data[key]
    def load[T](repo: Repository[T], key: str) -> T:
        return repo.get(key)
    print(load(MemoryRepo({"x": 42}), "x"))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
