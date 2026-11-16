"""ABCs & Protocols — modern style."""
from abc import ABC, abstractmethod
from collections.abc import Iterator, Mapping, MutableSequence
from typing import Protocol, runtime_checkable

MIN_VERSION = (3, 10)


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    def describe(self) -> str:                        # shared concrete method
        return f"{type(self).__name__} with area {self.area():.2f}"


class Square(Shape):
    def __init__(self, side: float): self.side = side
    def area(self) -> float: return self.side ** 2


def example_01_abc_concrete_subclass():
    print(Square(3).describe())


def example_02_cannot_instantiate_abstract():
    try:
        Shape()
    except TypeError as exc:
        print("TypeError:", exc)


def example_03_missing_method_detected():
    class Bad(Shape): ...
    try:
        Bad()
    except TypeError as exc:
        print("TypeError:", exc)


def example_04_abstract_property():
    class Storage(ABC):
        @property
        @abstractmethod
        def name(self) -> str: ...
    class S3(Storage):
        @property
        def name(self) -> str: return "s3"
    print(S3().name)


def example_05_collections_abc_mixins():
    class FrozenConfig(Mapping):
        def __init__(self, **kw): self._d = dict(kw)
        def __getitem__(self, k): return self._d[k]
        def __iter__(self) -> Iterator: return iter(self._d)
        def __len__(self): return len(self._d)
    c = FrozenConfig(host="db", port=1)
    print(dict(c), c.get("x", "default"), "host" in c, list(c.items()))   # get/items/__contains__ free


def example_06_mutable_sequence():
    class TypedList(MutableSequence):
        def __init__(self, kind): self.kind, self._items = kind, []
        def __getitem__(self, i): return self._items[i]
        def __setitem__(self, i, v): self._check(v); self._items[i] = v
        def __delitem__(self, i): del self._items[i]
        def __len__(self): return len(self._items)
        def insert(self, i, v): self._check(v); self._items.insert(i, v)
        def _check(self, v):
            if not isinstance(v, self.kind): raise TypeError(f"expected {self.kind.__name__}")
    tl = TypedList(int); tl.append(1); tl.extend([2, 3])       # append/extend come free
    print(list(tl))


def example_07_protocol_structural():
    class Notifier(Protocol):
        def send(self, msg: str) -> None: ...
    class Email:
        def send(self, msg: str) -> None: print("  email:", msg)
    class Sms:
        def send(self, msg: str) -> None: print("  sms:", msg)
    def alert(n: Notifier) -> None: n.send("disk full")
    for n in (Email(), Sms()):
        alert(n)


def example_08_runtime_checkable_protocol():
    @runtime_checkable
    class Closable(Protocol):
        def close(self) -> None: ...
    import io
    print(isinstance(io.StringIO(), Closable), isinstance("x", Closable))


def example_09_register_virtual_subclass():
    class Drawable(ABC):
        @abstractmethod
        def draw(self): ...
    class LegacyWidget:
        def draw(self): return "legacy"
    Drawable.register(LegacyWidget)
    print(isinstance(LegacyWidget(), Drawable))


def example_10_isinstance_with_abc_types():
    from collections.abc import Iterable, Callable, Hashable
    print(isinstance([1], Iterable), isinstance(len, Callable), isinstance([], Hashable))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
