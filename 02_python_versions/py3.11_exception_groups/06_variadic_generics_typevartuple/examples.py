"""TypeVarTuple / Unpack — Python 3.11+ (PEP 646)."""
from typing import Callable, Generic, NewType, TypeVar, TypeVarTuple

MIN_VERSION = (3, 11)
T = TypeVar("T")
Ts = TypeVarTuple("Ts")


def example_01_typed_tuple_passthrough():
    def identity(*args: *Ts) -> tuple[*Ts]:
        return args
    print(identity(1, "a", 2.5))


def example_02_prepend_element():
    def with_id(id_: int, row: tuple[*Ts]) -> tuple[int, *Ts]:
        return (id_, *row)
    print(with_id(7, ("ann", True)))


def example_03_first_and_rest():
    def split(t: tuple[T, *Ts]) -> tuple[T, tuple[*Ts]]:
        return t[0], t[1:]
    print(split((1, "x", 3.0)))


def example_04_shape_typed_array():
    Batch = NewType("Batch", int)
    Height = NewType("Height", int)
    Width = NewType("Width", int)
    class Array(Generic[*Ts]):
        def __init__(self, *shape: *Ts):
            self.shape = shape
        def __repr__(self):
            return f"Array{self.shape}"
    img: Array[Batch, Height, Width] = Array(Batch(32), Height(224), Width(224))
    print(img)


def example_05_call_with_args():
    def call_later(fn: Callable[[*Ts], T], *args: *Ts) -> T:
        return fn(*args)
    print(call_later(lambda a, b: f"{a}-{b}", "x", 3))


def example_06_generic_record():
    class Row(Generic[*Ts]):
        def __init__(self, *values: *Ts):
            self.values = values
        def as_tuple(self) -> tuple[*Ts]:
            return self.values
    print(Row(1, "ann", 3.5).as_tuple())


def example_07_mixed_with_typevar():
    class Pipeline(Generic[T, *Ts]):
        def __init__(self, first: T, *rest: *Ts):
            self.first, self.rest = first, rest
    p = Pipeline("load", "clean", "save")
    print(p.first, p.rest)


def example_08_runtime_introspection():
    print(Ts, Ts.__name__, tuple[int, *Ts])


def example_09_unpack_spelling_for_older_style():
    from typing import Unpack
    def f(*args: Unpack[Ts]) -> tuple[Unpack[Ts]]:
        return args
    print(f("same", "as", "*Ts"))


def example_10_zip_like_function():
    def pairs(a: tuple[*Ts], b: tuple[*Ts]) -> list[tuple[object, object]]:
        return list(zip(a, b, strict=True))
    print(pairs((1, "a"), (2, "b")))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
