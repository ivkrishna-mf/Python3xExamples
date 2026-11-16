"""typing.TypeIs — Python 3.13+ (PEP 742)."""
from dataclasses import dataclass
from typing import Any, TypedDict, TypeIs

MIN_VERSION = (3, 13)


def is_str(x: object) -> TypeIs[str]:
    return isinstance(x, str)


def example_01_both_branches_narrow():
    def describe(v: int | str) -> str:
        if is_str(v):
            return v.upper()          # v: str
        return f"{v + 1}"             # v: int (TypeGuard couldn't do this)
    print(describe("ok"), describe(41))


def example_02_list_of_ints():
    def is_int_list(v: list[Any]) -> TypeIs[list[int]]:
        return all(isinstance(x, int) for x in v)
    data: list[Any] = [1, 2, 3]
    if is_int_list(data):
        print(sum(data))


def example_03_typed_dict_payload():
    class Click(TypedDict):
        x: int
        y: int
    def is_click(e: dict[str, Any]) -> TypeIs[Click]:
        return isinstance(e.get("x"), int) and isinstance(e.get("y"), int)
    evt = {"x": 3, "y": 4}
    print(is_click(evt), is_click({"x": "3"}))


def example_04_class_union():
    @dataclass
    class Cat:
        def meow(self) -> str: return "meow"
    @dataclass
    class Dog:
        def bark(self) -> str: return "woof"
    def is_cat(a: Cat | Dog) -> TypeIs[Cat]:
        return isinstance(a, Cat)
    for a in (Cat(), Dog()):
        print(a.meow() if is_cat(a) else a.bark())


def example_05_none_filter():
    def is_present[T](v: T | None) -> TypeIs[T]:
        return v is not None
    values = [1, None, 3]
    print([v * 10 for v in values if is_present(v)])


def example_06_validated_email():
    def is_nonempty(s: str | None) -> TypeIs[str]:
        return bool(s)
    email: str | None = "a@x.io"
    if is_nonempty(email):
        print(email.split("@")[1])


def example_07_numeric():
    def is_number(x: object) -> TypeIs[int | float]:
        return isinstance(x, (int, float)) and not isinstance(x, bool)
    print([x for x in [1, "2", 3.5, True] if is_number(x)])


def example_08_tuple_shape():
    def is_pair(t: tuple[int, ...]) -> TypeIs[tuple[int, int]]:
        return len(t) == 2
    t = (3, 4)
    if is_pair(t):
        a, b = t
        print(a * b)


def example_09_runtime_is_just_bool():
    print(is_str("x"), is_str(1), is_str.__annotations__["return"])


def example_10_compare_with_typeguard():
    from typing import TypeGuard
    def guard(x: int | str) -> TypeGuard[str]: return isinstance(x, str)
    def is_(x: int | str) -> TypeIs[str]: return isinstance(x, str)
    print("TypeGuard narrows only the True branch; TypeIs narrows True and False",
          guard("a"), is_(1))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
