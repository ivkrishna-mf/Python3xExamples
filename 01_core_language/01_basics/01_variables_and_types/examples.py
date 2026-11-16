"""Variables & built-in types — modern style (Python 3.10+)."""
import copy
import sys

MIN_VERSION = (3, 10)


def example_01_dynamic_binding():
    x = 42
    print(type(x).__name__, end=" -> ")
    x = "now a string"
    print(type(x).__name__)


def example_02_annotated_variables():
    name: str = "Ada"
    scores: list[int] = [90, 85]
    nickname: str | None = None
    print(name, scores, nickname)


def example_03_multiple_assignment_and_swap():
    a, b, c = 1, 2, 3
    a, b = b, a
    x = y = 0
    print(a, b, c, x, y)


def example_04_identity_vs_equality():
    a = [1, 2]
    b = [1, 2]
    print(a == b, a is b, id(a) != id(b))


def example_05_mutable_vs_immutable():
    t = (1, 2)
    lst = [1, 2]
    lst.append(3)                      # list changes in place
    try:
        t[0] = 9
    except TypeError as exc:
        print(lst, "| tuple:", exc)


def example_06_aliasing_and_copying():
    original = {"tags": ["a"]}
    alias = original
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)
    original["tags"].append("b")
    print(alias["tags"], shallow["tags"], deep["tags"])


def example_07_isinstance_checks():
    for v in (1, 2.5, True, "x", None):
        print(repr(v), isinstance(v, int | float), type(v).__name__)


def example_08_truthiness():
    values = [0, 0.0, "", [], {}, set(), None, "0", [0], 1]
    print([bool(v) for v in values])


def example_09_type_conversion():
    print(int("42"), float("3.5"), str(10), list("abc"), bool(""), int(3.99), round(3.5), round(2.5))


def example_10_object_size_and_none():
    print(sys.getsizeof(0), sys.getsizeof(10**100), "bytes | None is a singleton:", None is type(None)())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
