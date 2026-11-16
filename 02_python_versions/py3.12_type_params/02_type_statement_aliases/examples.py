"""type statement — Python 3.12+ (PEP 695)."""
from collections.abc import Callable

MIN_VERSION = (3, 12)

type Vector = list[float]
type Json = dict[str, Json] | list[Json] | str | int | float | bool | None
type Pair[T] = tuple[T, T]
type Handler = Callable[[str], None]
type Matrix[T] = list[list[T]]


def example_01_simple_alias():
    def norm(v: Vector) -> float:
        return sum(x * x for x in v) ** 0.5
    print(norm([3.0, 4.0]))


def example_02_alias_object():
    print(type(Vector).__name__, Vector.__name__, Vector.__value__)


def example_03_recursive_json():
    def count_leaves(j: Json) -> int:
        if isinstance(j, dict):
            return sum(count_leaves(v) for v in j.values())
        if isinstance(j, list):
            return sum(count_leaves(v) for v in j)
        return 1
    print(count_leaves({"a": [1, 2, {"b": None}], "c": "x"}))


def example_04_generic_alias():
    def swap[T](p: Pair[T]) -> Pair[T]:
        return p[1], p[0]
    print(swap((1, 2)), Pair[int])


def example_05_callable_alias():
    handlers: dict[str, Handler] = {"print": print}
    handlers["print"]("handled!")


def example_06_lazy_evaluation():
    type Later = UndefinedYet          # not evaluated until accessed  # noqa: F821
    try:
        Later.__value__
    except NameError as exc:
        print("evaluated lazily -> NameError:", exc)


def example_07_generic_matrix():
    def transpose[T](m: Matrix[T]) -> Matrix[T]:
        return [list(r) for r in zip(*m)]
    print(transpose([[1, 2, 3], [4, 5, 6]]))


def example_08_type_params_introspection():
    print(Pair.__type_params__, Matrix.__type_params__)


def example_09_not_usable_with_isinstance():
    try:
        isinstance([1.0], Vector)
    except TypeError as exc:
        print("TypeError:", exc)
    print("use the value instead:", isinstance([1.0], Vector.__value__.__origin__))


def example_10_alias_in_class_scope():
    class Graph:
        type Node = str
        type Edges = dict[Node, list[Node]]
        def __init__(self, edges: "Graph.Edges") -> None:
            self.edges = edges
    print(Graph({"a": ["b"], "b": []}).edges, Graph.Edges.__value__)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
