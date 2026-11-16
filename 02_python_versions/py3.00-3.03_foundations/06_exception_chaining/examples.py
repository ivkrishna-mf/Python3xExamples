"""Exception chaining — Python 3.0+ / 3.3+ (PEP 3134, 409, 415)."""
import traceback

MIN_VERSION = (3, 3)


class ConfigError(Exception):
    pass


def example_01_explicit_cause():
    try:
        try:
            int("abc")
        except ValueError as exc:
            raise ConfigError("PORT must be a number") from exc
    except ConfigError as err:
        print(err, "| cause:", repr(err.__cause__))


def example_02_implicit_context():
    try:
        try:
            1 / 0
        except ZeroDivisionError:
            undefined_name  # noqa: F821 - NameError while handling
    except NameError as err:
        print("context:", repr(err.__context__))


def example_03_suppress_with_from_none():
    try:
        try:
            {}["key"]
        except KeyError:
            raise ConfigError("missing setting 'key'") from None
    except ConfigError as err:
        print(err, "| cause:", err.__cause__, "| suppressed:", err.__suppress_context__)


def example_04_print_full_chain():
    try:
        try:
            open("/definitely/not/here")
        except OSError as exc:
            raise ConfigError("cannot load config") from exc
    except ConfigError:
        print(traceback.format_exc().splitlines()[-1])
        print("(full traceback shows both errors)")


def example_05_walk_the_chain():
    def chain(exc):
        while exc:
            yield exc
            exc = exc.__cause__ or exc.__context__
    try:
        try:
            try:
                raise KeyError("a")
            except KeyError as e:
                raise ValueError("b") from e
        except ValueError as e:
            raise RuntimeError("c") from e
    except RuntimeError as top:
        print([type(e).__name__ for e in chain(top)])


def example_06_domain_error_layer():
    class RepoError(Exception): ...
    def load_user(uid):
        try:
            return {"1": "ann"}[uid]
        except KeyError as exc:
            raise RepoError(f"user {uid} not found") from exc
    try:
        load_user("9")
    except RepoError as e:
        print(e, "<-", type(e.__cause__).__name__)


def example_07_reraise_keeps_traceback():
    try:
        try:
            [][1]
        except IndexError:
            print("logging and re-raising")
            raise
    except IndexError as e:
        print("caught again:", e)


def example_08_cause_can_be_any_exception():
    err = ConfigError("bad")
    err.__cause__ = TimeoutError("slow disk")
    print(repr(err.__cause__))


def example_09_raise_from_in_retry():
    last = None
    for attempt in range(3):
        try:
            raise ConnectionError(f"attempt {attempt}")
        except ConnectionError as exc:
            last = exc
    try:
        raise RuntimeError("all retries failed") from last
    except RuntimeError as e:
        print(e, "| last:", e.__cause__)


def example_10_testing_the_cause():
    try:
        try:
            int("x")
        except ValueError as exc:
            raise ConfigError("bad int") from exc
    except ConfigError as e:
        assert isinstance(e.__cause__, ValueError)
        print("assertion passed: cause is ValueError")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
