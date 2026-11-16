"""Structural pattern matching — Python 3.10+ (PEP 634)."""
from dataclasses import dataclass
from enum import Enum

MIN_VERSION = (3, 10)


@dataclass
class Point:
    x: int
    y: int


class Color(Enum):
    RED = "red"
    GREEN = "green"


def example_01_literals_and_wildcard():
    def http_status(code):
        match code:
            case 200 | 201:
                return "success"
            case 404:
                return "not found"
            case _:
                return "other"
    print([http_status(c) for c in (200, 404, 500)])


def example_02_sequence_patterns():
    def run(cmd):
        match cmd.split():
            case ["go", direction]:
                return f"moving {direction}"
            case ["take", *items]:
                return f"taking {', '.join(items)}"
            case ["quit" | "exit"]:
                return "bye"
            case []:
                return "empty"
            case _:
                return f"unknown: {cmd}"
    for c in ["go north", "take key lamp", "exit", "", "dance"]:
        print(run(c))


def example_03_mapping_patterns_json_events():
    def handle(event):
        match event:
            case {"type": "click", "x": x, "y": y}:
                return f"click at ({x},{y})"
            case {"type": "key", "key": str(k)}:
                return f"key {k!r}"
            case {"type": t, **rest}:
                return f"unhandled {t} with {rest}"
    print(handle({"type": "click", "x": 3, "y": 4}))
    print(handle({"type": "key", "key": "q"}))
    print(handle({"type": "scroll", "dy": -1}))


def example_04_class_patterns():
    def where(p):
        match p:
            case Point(x=0, y=0):
                return "origin"
            case Point(x=0, y=y):
                return f"on y-axis at {y}"
            case Point(x, y) if x == y:
                return "on the diagonal"
            case Point():
                return "somewhere else"
    print([where(p) for p in (Point(0, 0), Point(0, 5), Point(2, 2), Point(1, 9))])


def example_05_guards():
    def classify(n):
        match n:
            case int() if n < 0:
                return "negative"
            case int() if n % 2 == 0:
                return "even"
            case int():
                return "odd"
            case _:
                return "not an int"
    print([classify(v) for v in (-3, 4, 7, "x")])


def example_06_enum_constants_with_dotted_names():
    def describe(c):
        match c:
            case Color.RED:
                return "stop"
            case Color.GREEN:
                return "go"
    print(describe(Color.GREEN))


def example_07_as_capture_and_or_patterns():
    def shape(value):
        match value:
            case [int() | float() as a, int() | float() as b]:
                return f"pair of numbers {a}, {b}"
            case (str() as s) | [str() as s]:
                return f"text {s!r}"
    print(shape([1, 2.5]), "|", shape("hi"), "|", shape(["yo"]))


def example_08_nested_patterns_ast_like():
    def evaluate(expr):
        match expr:
            case ("num", n):
                return n
            case ("add", left, right):
                return evaluate(left) + evaluate(right)
            case ("mul", left, right):
                return evaluate(left) * evaluate(right)
            case ("neg", inner):
                return -evaluate(inner)
    tree = ("add", ("num", 2), ("mul", ("num", 3), ("neg", ("num", 4))))
    print(evaluate(tree))


def example_09_type_dispatch():
    def to_text(v):
        match v:
            case bool():
                return "yes" if v else "no"
            case int() | float():
                return f"{v:,}"
            case str():
                return v
            case list() | tuple():
                return ", ".join(to_text(x) for x in v)
            case dict():
                return "; ".join(f"{k}={to_text(x)}" for k, x in v.items())
            case None:
                return "-"
    print(to_text({"ok": True, "count": 12000, "tags": ["a", "b"], "note": None}))


def example_10_state_machine():
    def step(state, event):
        match (state, event):
            case ("idle", "start"):
                return "running"
            case ("running", "pause"):
                return "paused"
            case ("paused", "resume"):
                return "running"
            case (_, "stop"):
                return "idle"
            case _:
                return state
    s = "idle"
    for e in ["start", "pause", "resume", "jump", "stop"]:
        s = step(s, e)
        print(f"{e:>6} -> {s}")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
