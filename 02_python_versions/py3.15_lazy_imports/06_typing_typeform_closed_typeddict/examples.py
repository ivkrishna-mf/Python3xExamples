"""TypeForm (PEP 747), closed/extra_items TypedDict (PEP 728), disjoint_base (PEP 800) — Python 3.15+."""
import typing
from typing import Any, NotRequired, TypedDict, TypeForm, get_args, get_origin

MIN_VERSION = (3, 15)


def trycast[T](form: TypeForm[T], value: object) -> T | None:
    """Tiny runtime checker for simple forms: classes, unions, list[X]."""
    origin, args = get_origin(form), get_args(form)
    if origin in (typing.Union, getattr(__import__("types"), "UnionType")):
        return value if any(trycast(a, value) is not None or (a is type(None) and value is None)
                            for a in args) else None
    if origin is list:
        return value if isinstance(value, list) and all(trycast(args[0], v) is not None for v in value) else None
    return value if isinstance(value, form) else None


class Movie(TypedDict, closed=True):
    title: str
    year: NotRequired[int]


class Scores(TypedDict, extra_items=int):
    student: str


def example_01_typeform_simple_class():
    print(trycast(int, 5), trycast(int, "5"))


def example_02_typeform_union():
    print(trycast(int | str, "ok"), trycast(int | str, 2.5))


def example_03_typeform_generic():
    print(trycast(list[int], [1, 2]), trycast(list[int], [1, "x"]))


def example_04_typeform_as_annotation():
    print(trycast.__annotations__["form"])


def example_05_closed_typeddict():
    m: Movie = {"title": "Arrival", "year": 2016}
    # m2: Movie = {"title": "X", "rating": 9}   <- checker error: extra key on closed TypedDict
    print(m, "closed:", Movie.__closed__)


def example_06_extra_items_typeddict():
    s: Scores = {"student": "ann", "math": 91, "physics": 84}
    # {"student": "bob", "art": "A+"}  <- checker error: extras must be int
    print(s, "extra items type:", Scores.__extra_items__)


def example_07_runtime_validation_of_closed_shape():
    def check_closed(td, data: dict[str, Any]) -> list[str]:
        allowed = td.__required_keys__ | td.__optional_keys__
        return sorted(data.keys() - allowed)
    print("unexpected keys:", check_closed(Movie, {"title": "x", "rating": 9}))


def example_08_default_is_open():
    class Open(TypedDict):
        a: int
    print("closed:", getattr(Open, "__closed__", None), "| extra_items:", Open.__extra_items__)


def example_09_disjoint_base():
    @typing.disjoint_base
    class Packet:
        __slots__ = ("payload",)
    print(Packet.__name__, "marked disjoint:", getattr(Packet, "__disjoint_base__", True))


def example_10_typeform_function_signature_idea():
    def parse_env[T](name: str, form: TypeForm[T], raw: dict[str, str]) -> T | None:
        conv = {int: int, float: float, str: str, bool: lambda s: s.lower() in ("1", "true")}
        return conv[form](raw[name]) if name in raw else None
    env = {"WORKERS": "4", "DEBUG": "true"}
    print(parse_env("WORKERS", int, env), parse_env("DEBUG", bool, env))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
