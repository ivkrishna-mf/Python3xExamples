"""Variable annotations — Python 3.6+ (PEP 526)."""
from typing import ClassVar, Dict, List, NamedTuple, Optional

MIN_VERSION = (3, 6)


def example_01_annotated_assignment():
    retries: int = 3
    print(retries)


def example_02_annotation_without_value():
    class Config:
        host: str
        port: int = 8080
    print(Config.__annotations__, hasattr(Config, "host"))


def example_03_empty_container_types():
    cache: Dict[str, int] = {}
    cache["hits"] = 1
    print(cache)


def example_04_classvar():
    class Counter:
        instances: ClassVar[int] = 0
        value: int
        def __init__(self):
            Counter.instances += 1
            self.value = 0
    Counter(); Counter()
    print(Counter.instances)


def example_05_namedtuple_class_syntax():
    class Point(NamedTuple):
        x: float
        y: float = 0.0
    print(Point(1.5), Point._fields)


def example_06_optional_attribute():
    class Node:
        next: Optional["Node"] = None
        def __init__(self, val: int):
            self.val = val
    n = Node(1); n.next = Node(2)
    print(n.val, n.next.val)


def example_07_module_annotations():
    import types
    mod = types.ModuleType("demo")
    exec("timeout: float = 2.5\nname: str", mod.__dict__)
    print(mod.__annotations__)


def example_08_inheritance_of_annotations():
    class Base:
        id: int
    class User(Base):
        name: str
    print(User.__annotations__, "(only its own)")
    import typing
    print(typing.get_type_hints(User), "(merged)")


def example_09_used_by_dataclasses():
    from dataclasses import dataclass, fields
    @dataclass
    class Item:
        sku: str
        qty: int = 1
    print([f.name for f in fields(Item)], Item("A1"))


def example_10_tuple_unpacking_needs_separate_lines():
    # Annotations don't work on tuple targets: `a, b: int = 1, 2` is a SyntaxError
    a: int
    b: List[int]
    a, b = 1, [2, 3]
    print(a, b)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
