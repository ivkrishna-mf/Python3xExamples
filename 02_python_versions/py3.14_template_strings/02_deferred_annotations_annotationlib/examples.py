"""Deferred annotations & annotationlib — Python 3.14+ (PEP 649, 749)."""
import annotationlib
from annotationlib import Format, get_annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from decimal import Decimal

MIN_VERSION = (3, 14)


@dataclass
class Node:
    value: int
    next: Node | None = None          # no quotes, no __future__ import


def example_01_forward_reference_without_quotes():
    print(Node(1, Node(2)).next)


def example_02_annotations_are_real_objects():
    print(Node.__annotations__)


def example_03_annotate_function():
    print(callable(Node.__annotate__), Node.__annotate__(Format.VALUE)["value"])


def example_04_undefined_name_value_format_raises():
    def f(x: NotDefinedYet) -> None: ...      # noqa: F821 – fine at definition time
    try:
        get_annotations(f, format=Format.VALUE)
    except NameError as exc:
        print("VALUE format -> NameError:", exc)


def example_05_forwardref_format():
    def f(x: NotDefinedYet, y: int) -> None: ...  # noqa: F821
    print(get_annotations(f, format=Format.FORWARDREF))


def example_06_string_format():
    def f(x: list[int] | None, y: NotDefinedYet = 1) -> dict[str, int]: ...  # noqa: F821
    print(get_annotations(f, format=Format.STRING))


def example_07_type_checking_imports():
    def total(prices: list[Decimal]) -> Decimal: ...
    print(get_annotations(total, format=Format.STRING))


def example_08_definition_is_cheap():
    def expensive():
        print("  (annotation expression evaluated now)")
        return int
    def f(x: expensive()) -> None: ...
    print("function defined; nothing evaluated yet")
    print(f.__annotations__)


def example_09_mutually_recursive_classes():
    @dataclass
    class Author:
        name: str
        books: list[Book]
    @dataclass
    class Book:
        title: str
        author: Author | None = None
    print(get_annotations(Author, format=Format.FORWARDREF))


def example_10_annotations_to_source():
    print(annotationlib.type_repr(list[int] | None), annotationlib.type_repr(Node))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
