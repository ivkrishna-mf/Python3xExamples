"""itertools.batched, Path.walk, math.sumprod, calendar enums — Python 3.12+."""
import calendar
import math
import sys
import tempfile
from itertools import batched
from pathlib import Path

MIN_VERSION = (3, 12)


def example_01_batched_basic():
    print(list(batched("ABCDEFG", 3)))


def example_02_bulk_insert_chunks():
    rows = [{"id": i} for i in range(1, 8)]
    for chunk in batched(rows, 3):
        print("INSERT", [r["id"] for r in chunk])


def example_03_batched_generator_input():
    squares = (n * n for n in range(10))
    print([sum(b) for b in batched(squares, 4)])


def example_04_batched_strict_313():
    if sys.version_info >= (3, 13):
        try:
            list(batched(range(5), 2, strict=True))
        except ValueError as exc:
            print("ValueError:", exc)
    else:
        print("strict= needs 3.13+")


def example_05_path_walk():
    root = Path(tempfile.mkdtemp())
    (root / "a" / "b").mkdir(parents=True)
    (root / "a" / "x.txt").touch()
    (root / "a" / "b" / "y.txt").touch()
    for dirpath, dirnames, filenames in root.walk():
        print(dirpath.relative_to(root), sorted(dirnames), sorted(filenames))


def example_06_math_sumprod():
    prices, qty = [9.99, 4.50, 1.25], [2, 3, 10]
    print(round(math.sumprod(prices, qty), 2))


def example_07_calendar_enums():
    print(calendar.Month.NOVEMBER, calendar.Month(11).name, calendar.Day.MONDAY.value)


def example_08_batched_for_rate_limited_api():
    ids = list(range(1, 11))
    for batch in batched(ids, 4):
        print(f"GET /users?ids={','.join(map(str, batch))}")


def example_09_matrix_from_flat_list():
    flat = [1, 2, 3, 4, 5, 6]
    print([list(r) for r in batched(flat, 3)])


def example_10_path_with_segments_subclass():
    class ProjectPath(type(Path())):
        pass
    p = ProjectPath("src") / "main.py"
    print(type(p).__name__, p)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
