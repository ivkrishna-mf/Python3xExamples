"""Type hints & typing — Python 3.5+ (PEP 484). Classic spellings shown; see 3.9/3.10/3.12 for newer syntax."""
from typing import (Any, Callable, Dict, Generic, Iterator, List, NewType,
                    Optional, Tuple, TypeVar, Union, get_type_hints, overload)

MIN_VERSION = (3, 5)
T = TypeVar("T")


def example_01_basic_annotations():
    def greet(name: str, times: int = 1) -> str:
        return ", ".join([f"hi {name}"] * times)
    print(greet("ann", 2), greet.__annotations__)


def example_02_optional():
    def find(users: Dict[int, str], uid: int) -> Optional[str]:
        return users.get(uid)
    print(find({1: "ann"}, 2))


def example_03_union():
    def to_float(x: Union[int, str]) -> float:
        return float(x)
    print(to_float("3.5") + to_float(1))


def example_04_callable():
    def apply(fn: Callable[[int], int], value: int) -> int:
        return fn(value)
    print(apply(lambda x: x * 10, 4))


def example_05_typevar_generic_function():
    def first(items: List[T]) -> T:
        return items[0]
    print(first(["a", "b"]), first([1, 2]))


def example_06_generic_class():
    class Stack(Generic[T]):
        def __init__(self) -> None:
            self._items: List[T] = []
        def push(self, item: T) -> None:
            self._items.append(item)
        def pop(self) -> T:
            return self._items.pop()
    s: Stack[int] = Stack()
    s.push(1); s.push(2)
    print(s.pop())


def example_07_newtype_for_ids():
    UserId = NewType("UserId", int)
    OrderId = NewType("OrderId", int)
    def get_user(uid: UserId) -> str:
        return f"user {uid}"
    print(get_user(UserId(5)))   # a checker rejects get_user(OrderId(5))


def example_08_overload():
    @overload
    def double(x: int) -> int: ...
    @overload
    def double(x: str) -> str: ...
    def double(x: Any) -> Any:
        return x * 2
    print(double(4), double("ab"))


def example_09_iterator_and_tuple():
    def pairs(n: int) -> Iterator[Tuple[int, int]]:
        for i in range(n):
            yield i, i * i
    print(list(pairs(3)))


def example_10_not_enforced_at_runtime():
    def add(a: int, b: int) -> int:
        return a + b
    print(add("no ", "error!"), "<- hints are not runtime checks")
    print(get_type_hints(add))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
