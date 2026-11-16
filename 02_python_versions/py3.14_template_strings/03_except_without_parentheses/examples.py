"""except A, B: without parentheses — Python 3.14+ (PEP 758)."""
import json

MIN_VERSION = (3, 14)


def example_01_basic():
    try:
        int("x")
    except ValueError, TypeError:
        print("caught ValueError or TypeError")


def example_02_three_types():
    for bad in ("x", None, [1]):
        try:
            int(bad)
        except ValueError, TypeError, OverflowError:
            print(f"cannot convert {bad!r}")


def example_03_with_as_still_needs_parentheses():
    try:
        {}["missing"]
    except (KeyError, IndexError) as exc:
        print("with 'as' you still write a tuple:", repr(exc))


def example_04_json_parsing():
    for raw in ['{"a": 1}', "not json", None]:
        try:
            print(json.loads(raw))
        except json.JSONDecodeError, TypeError:
            print("skipping invalid payload:", repr(raw))


def example_05_lookup_errors():
    data = {"items": [1, 2]}
    for path in (("items", 5), ("nope", 0)):
        try:
            data[path[0]][path[1]]
        except KeyError, IndexError:
            print("missing path", path)


def example_06_except_star_form():
    try:
        raise ExceptionGroup("g", [ValueError(), TypeError()])
    except* ValueError, TypeError:
        print("except* also accepts the unparenthesised list")


def example_07_file_errors():
    try:
        open("/no/such/file")
    except FileNotFoundError, PermissionError:
        print("could not open file")


def example_08_numeric_errors():
    for a, b in ((1, 0), (1e308, 1e-308)):
        try:
            print(a / b)
        except ZeroDivisionError, OverflowError:
            print("bad division", a, b)


def example_09_cleanup_ignore():
    import os
    try:
        os.remove("/tmp/__does_not_exist__")
    except FileNotFoundError, IsADirectoryError:
        pass
    print("ignored expected cleanup errors")


def example_10_equivalent_tuple_form():
    errors_seen = []
    for exc_type in (ValueError, TypeError):
        try:
            raise exc_type
        except ValueError, TypeError:
            errors_seen.append(exc_type.__name__)
    print(errors_seen, "== same as except (ValueError, TypeError):")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
