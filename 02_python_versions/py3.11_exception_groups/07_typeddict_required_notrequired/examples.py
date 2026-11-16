"""Required / NotRequired in TypedDict — Python 3.11+ (PEP 655)."""
import json
from typing import Generic, NotRequired, Required, TypedDict, TypeVar

MIN_VERSION = (3, 11)


class User(TypedDict):
    id: int
    name: str
    nickname: NotRequired[str]


class Options(TypedDict, total=False):
    url: Required[str]
    timeout: float
    retries: int


def example_01_optional_key_may_be_missing():
    u: User = {"id": 1, "name": "ann"}
    print(u, u.get("nickname", "(none)"))


def example_02_with_the_optional_key():
    u: User = {"id": 2, "name": "bob", "nickname": "bobby"}
    print(u["nickname"])


def example_03_runtime_key_sets():
    print(sorted(User.__required_keys__), sorted(User.__optional_keys__))


def example_04_required_in_total_false():
    o: Options = {"url": "https://x"}
    print(o, sorted(Options.__required_keys__))


def example_05_simple_runtime_validator():
    def missing_keys(td, data):
        return sorted(td.__required_keys__ - data.keys())
    print(missing_keys(User, {"id": 1}), missing_keys(Options, {"timeout": 2}))


def example_06_parse_api_response():
    raw = '[{"id": 1, "name": "ann"}, {"id": 2, "name": "bob", "nickname": "b"}]'
    users: list[User] = json.loads(raw)
    print([u.get("nickname", u["name"]) for u in users])


def example_07_function_kwargs_style():
    def connect(opts: Options) -> str:
        return f"{opts['url']} t={opts.get('timeout', 5)} r={opts.get('retries', 0)}"
    print(connect({"url": "db://", "retries": 3}))


def example_08_generic_typeddict_311():
    T = TypeVar("T")
    class Page(TypedDict, Generic[T]):
        items: list[T]
        next: NotRequired[str]
    p: Page[int] = {"items": [1, 2, 3]}
    print(p)


def example_09_inheritance():
    class Base(TypedDict):
        id: int
    class Event(Base):
        kind: str
        meta: NotRequired[dict]
    print(sorted(Event.__required_keys__), sorted(Event.__optional_keys__))


def example_10_functional_syntax():
    Item = TypedDict("Item", {"sku": str, "note": NotRequired[str]})
    print(Item.__optional_keys__)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
