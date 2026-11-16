"""f-string '=' — Python 3.8+."""
import math

MIN_VERSION = (3, 8)
user, retries, ratio = "ann", 3, 0.123456


def example_01_basic():
    print(f"{user=}")


def example_02_multiple():
    print(f"{user=}, {retries=}")


def example_03_expression():
    print(f"{retries * 2 + 1=}")


def example_04_with_format_spec():
    print(f"{ratio=:.2%}")


def example_05_str_conversion():
    print(f"{user=!s}")


def example_06_whitespace_preserved():
    print(f"{retries = }")


def example_07_function_call():
    print(f"{math.sqrt(2)=:.4f}")


def example_08_attribute_and_index():
    data = {"items": [10, 20]}
    print(f"{data['items'][1]=}")


def example_09_in_assert_message():
    balance = -5
    try:
        assert balance >= 0, f"invalid state: {balance=}"
    except AssertionError as exc:
        print("AssertionError:", exc)


def example_10_debug_loop():
    for i, ch in enumerate("ab"):
        print(f"{i=} {ch=} {ord(ch)=}")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
