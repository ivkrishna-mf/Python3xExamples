"""Type parameter defaults — Python 3.13+ (PEP 696)."""
from collections.abc import Callable
from dataclasses import dataclass
from typing import Generic, TypeVar

MIN_VERSION = (3, 13)


@dataclass
class Response[T = dict]:
    status: int
    body: T


def example_01_default_used():
    r: Response = Response(200, {"ok": True})    # means Response[dict]
    print(r)


def example_02_explicit_override():
    r: Response[str] = Response(200, "plain text")
    print(r)


def example_03_inspect_default():
    (T,) = Response.__type_params__
    print(T, T.__default__, T.has_default())


def example_04_classic_typevar_default():
    K = TypeVar("K", default=str)
    class Registry(Generic[K]):
        def __init__(self): self.items: dict[K, object] = {}
    print(Registry.__parameters__[0].__default__)


def example_05_default_refers_to_earlier_param():
    @dataclass
    class Pair[A, B = A]:
        a: A
        b: B
    print(Pair(1, 2), Pair.__type_params__[1].__default__)


def example_06_multiple_defaults():
    class Gen[Y, S = None, R = None]:
        """Like Generator[Y, S, R] where send/return types are usually None."""
    print([p.__default__ for p in Gen.__type_params__])


def example_07_paramspec_default():
    class Handler[**P = [str, int]]:
        def __init__(self, fn: Callable[P, None]): self.fn = fn
    (P,) = Handler.__type_params__
    print(P.__default__)


def example_08_typevartuple_default():
    class Shape[*Ts = *tuple[int, int]]:
        pass
    print(Shape.__type_params__[0].__default__)


def example_09_function_with_default_param():
    def parse[T = int](raw: str, conv: Callable[[str], T] = int) -> T:
        return conv(raw)
    print(parse("42"), parse("3.5", float))


def example_10_no_default_sentinel():
    from typing import NoDefault
    @dataclass
    class Box[T]:
        item: T
    print(Box.__type_params__[0].__default__ is NoDefault)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
