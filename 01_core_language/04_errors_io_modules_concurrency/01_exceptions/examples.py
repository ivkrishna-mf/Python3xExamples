"""Exceptions — modern style (3.11+ for notes & groups)."""
import logging

MIN_VERSION = (3, 11)


class AppError(Exception):
    """Base class for this application's errors."""


class ValidationError(AppError):
    def __init__(self, field: str, message: str) -> None:
        super().__init__(f"{field}: {message}")
        self.field = field


class NotFoundError(AppError):
    pass


def example_01_try_except():
    try:
        result = 10 / 0
    except ZeroDivisionError as exc:
        print("caught:", exc)


def example_02_multiple_except_and_else_finally():
    for raw in ["42", "x", None]:
        try:
            n = int(raw)
        except ValueError:
            print(f"{raw!r}: not a number")
        except TypeError:
            print(f"{raw!r}: wrong type")
        else:
            print("parsed", n)
        finally:
            pass   # always runs (cleanup)


def example_03_raise_custom():
    def set_age(age: int) -> int:
        if not 0 <= age <= 150:
            raise ValidationError("age", f"{age} is out of range")
        return age
    try:
        set_age(200)
    except ValidationError as exc:
        print(type(exc).__name__, exc, "| field:", exc.field)


def example_04_catch_base_class():
    for exc in (ValidationError("x", "bad"), NotFoundError("user 9")):
        try:
            raise exc
        except AppError as err:
            print("AppError caught:", type(err).__name__, err)


def example_05_chaining_with_from():
    def load(path: str) -> str:
        try:
            with open(path) as fh:
                return fh.read()
        except FileNotFoundError as exc:
            raise NotFoundError(f"config {path} missing") from exc
    try:
        load("/no/such.toml")
    except NotFoundError as exc:
        print(exc, "<- cause:", type(exc.__cause__).__name__)


def example_06_eafp_vs_lbyl():
    data = {"a": 1}
    try:                                    # EAFP: easier to ask forgiveness
        value = data["b"]
    except KeyError:
        value = 0
    value2 = data["b"] if "b" in data else 0   # LBYL: look before you leap
    print(value, value2, data.get("b", 0))


def example_07_reraise_after_logging():
    log = logging.getLogger("demo")
    try:
        try:
            [][3]
        except IndexError:
            log.debug("logging then re-raising")
            raise
    except IndexError as exc:
        print("re-raised:", exc)


def example_08_exception_notes():
    try:
        try:
            int("abc")
        except ValueError as exc:
            exc.add_note("while reading row 12 of users.csv")
            raise
    except ValueError as exc:
        print(exc, exc.__notes__)


def example_09_exception_groups():
    try:
        raise ExceptionGroup("validation", [ValueError("bad email"), TypeError("age not int")])
    except* ValueError as eg:
        print("value errors:", eg.exceptions)
    except* TypeError as eg:
        print("type errors:", eg.exceptions)


def example_10_assert_for_invariants():
    def mean(xs: list[float]) -> float:
        assert xs, "mean() of empty list"      # disabled with python -O; not for input validation
        return sum(xs) / len(xs)
    try:
        mean([])
    except AssertionError as exc:
        print("AssertionError:", exc)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
