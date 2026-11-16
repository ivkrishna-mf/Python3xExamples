"""TypedDict / Final / Literal — Python 3.8+ (PEP 589, 591, 586)."""
import json
from typing import Final, List, Literal, TypedDict, final, get_args

MIN_VERSION = (3, 8)


class Movie(TypedDict):
    title: str
    year: int


class MovieWithRating(Movie, total=False):   # 'rating' is optional
    rating: float


def example_01_typeddict_is_a_dict():
    m: Movie = {"title": "Arrival", "year": 2016}
    print(m, type(m).__name__)


def example_02_from_json():
    payload: Movie = json.loads('{"title": "Dune", "year": 2021}')
    print(payload["title"].upper())


def example_03_optional_keys_total_false():
    m: MovieWithRating = {"title": "Her", "year": 2013}
    print(m.get("rating", "unrated"), MovieWithRating.__optional_keys__)


def example_04_functional_syntax():
    Point = TypedDict("Point", {"x": int, "y": int, "class": str})  # allows keyword keys
    p: Point = {"x": 1, "y": 2, "class": "A"}
    print(p, Point.__annotations__)


def example_05_final_constant():
    MAX_RETRIES: Final = 3
    # MAX_RETRIES = 4   <- a type checker reports this
    print(MAX_RETRIES)


def example_06_final_decorator():
    @final
    class Token:
        pass
    # class Sub(Token): ...   <- type checker error: cannot subclass a @final class
    print(Token.__name__, getattr(Token, "__final__", "n/a"))


def example_07_literal_parameter():
    Mode = Literal["r", "w", "a"]
    def open_file(path: str, mode: Mode) -> str:
        return f"opening {path} in {mode!r} mode"
    print(open_file("log.txt", "a"), get_args(Mode))


def example_08_runtime_check_against_literal():
    Color = Literal["red", "green"]
    def set_color(c: str) -> None:
        if c not in get_args(Color):
            raise ValueError(f"{c!r} not in {get_args(Color)}")
        print("color set to", c)
    set_color("red")
    try:
        set_color("blue")
    except ValueError as exc:
        print("ValueError:", exc)


def example_09_nested_typeddict():
    class Address(TypedDict):
        city: str
    class User(TypedDict):
        name: str
        address: Address
        tags: List[str]
    u: User = {"name": "ann", "address": {"city": "Pune"}, "tags": ["admin"]}
    print(u["address"]["city"])


def example_10_literal_return_type():
    def health() -> Literal["ok", "degraded", "down"]:
        return "ok"
    print(health())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
