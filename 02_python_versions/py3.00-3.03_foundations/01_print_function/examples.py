"""print() as a function — Python 3.0+ (PEP 3105)."""
import io
import sys
from functools import partial

MIN_VERSION = (3, 0)


def example_01_basic():
    print("Hello", "World")                 # args separated by a space


def example_02_custom_separator():
    print("2026", "11", "16", sep="-")      # 2026-11-16


def example_03_custom_end():
    for i in range(3):
        print(i, end=" | ")
    print()                                 # finish the line


def example_04_print_to_stderr():
    print("warning: disk almost full", file=sys.stderr)


def example_05_print_to_a_buffer():
    buf = io.StringIO()
    print("captured", 42, file=buf)
    print("buffer holds:", repr(buf.getvalue()))


def example_06_unpack_an_iterable():
    names = ["ann", "bob", "cy"]
    print(*names, sep=", ")


def example_07_flush_for_progress():
    import time
    for pct in (0, 50, 100):
        print(f"\rprogress {pct:3d}%", end="", flush=True)
        time.sleep(0.05)
    print()


def example_08_print_is_a_first_class_object():
    log = partial(print, "[app]", sep=" :: ")
    log("started")
    log("ready")


def example_09_write_to_a_file():
    import tempfile, os
    path = os.path.join(tempfile.gettempdir(), "print_demo.txt")
    with open(path, "w", encoding="utf-8") as fh:
        print("line one", file=fh)
        print("line two", file=fh)
    with open(path, encoding="utf-8") as fh:
        print(fh.read().splitlines())


def example_10_map_print_over_values():
    # print returns None, so wrap in list() only to force evaluation
    list(map(print, ["a", "b", "c"]))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
