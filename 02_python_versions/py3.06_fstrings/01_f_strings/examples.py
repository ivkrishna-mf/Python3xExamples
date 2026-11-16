"""f-strings — Python 3.6+ (PEP 498)."""
from datetime import datetime

MIN_VERSION = (3, 6)
name, score, total = "Ann", 42, 50


def example_01_basic_interpolation():
    print(f"{name} scored {score}")


def example_02_expressions():
    print(f"{name.upper()} has {total - score} points to go")


def example_03_number_formatting():
    print(f"{3.14159:.2f} | {1234567:,} | {0.256:.1%} | {255:#x} | {5:03d}")


def example_04_alignment_and_width():
    for item, price in [("apple", 0.5), ("watermelon", 3.25)]:
        print(f"{item:<12}|{price:>8.2f}")


def example_05_dates():
    dt = datetime(2026, 11, 16, 9, 30)
    print(f"{dt:%Y-%m-%d %H:%M} ({dt:%A})")


def example_06_conversion_flags():
    s = "café"
    print(f"{s!r} {s!a} {s!s}")


def example_07_nested_format_spec():
    width, precision = 10, 3
    print(f"[{3.14159265:{width}.{precision}f}]")


def example_08_dict_access_and_calls():
    user = {"name": "bob", "roles": ["admin", "dev"]}
    print(f"{user['name']} -> {', '.join(user['roles'])}")


def example_09_multiline_report():
    rows = [("cpu", 73.2), ("mem", 41.0)]
    report = "\n".join(f"{k:>4}: {v:5.1f}% {'#' * int(v // 10)}" for k, v in rows)
    print(report)


def example_10_custom___format__():
    class Temperature:
        def __init__(self, c): self.c = c
        def __format__(self, spec):
            return f"{self.c * 9 / 5 + 32:.1f}°F" if spec == "F" else f"{self.c:.1f}°C"
    t = Temperature(21.5)
    print(f"{t} = {t:F}")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
