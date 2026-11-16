"""Postponed annotations — Python 3.7+ (PEP 563). get_type_hints() on X | Y needs 3.10 to evaluate."""
from __future__ import annotations

import typing
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:            # only imported by type checkers, never at runtime
    from decimal import Decimal

MIN_VERSION = (3, 10)


def example_01_forward_reference_without_quotes():
    class Node:
        def __init__(self, val: int, next: Node | None = None):
            self.val, self.next = val, next
    print(Node(1, Node(2)).next.val)


def example_02_annotations_are_strings():
    def f(x: int) -> list[int]: ...
    print(f.__annotations__)


def example_03_get_type_hints_resolves():
    print(typing.get_type_hints(Tree))


def example_04_method_returning_own_class():
    print(Tree(1).add(Tree(2)).children[0].value)


def example_05_new_syntax_on_old_python():
    def parse(items: list[str] | None) -> dict[str, int]:
        return {s: len(s) for s in items or []}
    print(parse(["ab", "cde"]))


def example_06_type_checking_only_import():
    def total(prices: list[Decimal]) -> Decimal:   # Decimal not imported at runtime
        return sum(prices)
    from decimal import Decimal as D
    print(total([D("1.10"), D("2.20")]))


def example_07_dataclass_still_works():
    @dataclass
    class Order:
        id: int
        parent: Order | None = None
    print(Order(2, Order(1)))


def example_08_mutual_references():
    print(Author("ann").books, Book("py", Author("bob")).author.name)


def example_09_cheap_definitions():
    # Expensive expressions in annotations are never executed:
    def f(x: print("this would run without the future import")) -> None: ...
    print("annotation was NOT evaluated:", f.__annotations__["x"])


def example_10_check_the_flag():
    import __future__
    print(__future__.annotations)


@dataclass
class Tree:
    value: int
    children: list[Tree] | None = None

    def add(self, child: Tree) -> Tree:
        self.children = (self.children or []) + [child]
        return self


@dataclass
class Author:
    name: str
    books: list[Book] | None = None


@dataclass
class Book:
    title: str
    author: Author


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
