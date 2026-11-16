"""@warnings.deprecated — Python 3.13+ (PEP 702)."""
import warnings
from typing import overload
from warnings import deprecated

MIN_VERSION = (3, 13)
warnings.simplefilter("always", DeprecationWarning)


def capture(fn):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = fn()
    return result, [str(x.message) for x in w]


@deprecated("use fetch_user() instead")
def get_user(uid: int) -> str:
    return fetch_user(uid)


def fetch_user(uid: int) -> str:
    return f"user-{uid}"


def example_01_function_warning():
    print(capture(lambda: get_user(1)))


def example_02_marker_attribute():
    print(get_user.__deprecated__)


def example_03_deprecated_class():
    @deprecated("LegacyClient is replaced by Client")
    class LegacyClient:
        pass
    print(capture(LegacyClient)[1])


def example_04_custom_category():
    @deprecated("will be removed in v3", category=FutureWarning)
    def old(): return 1
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        old()
    print(w[0].category.__name__, w[0].message)


def example_05_static_only_no_runtime_warning():
    @deprecated("only flagged by type checkers", category=None)
    def quiet(): return "no runtime warning"
    print(capture(quiet))


def example_06_deprecated_overload():
    @overload
    @deprecated("passing str is deprecated; pass int")
    def parse(x: str) -> int: ...
    @overload
    def parse(x: int) -> int: ...
    def parse(x):
        return int(x)
    print(parse(5), parse("6"))


def example_07_deprecated_method():
    class Api:
        @deprecated("use .send() instead")
        def post(self, msg): return self.send(msg)
        def send(self, msg): return f"sent {msg}"
    print(capture(lambda: Api().post("hi")))


def example_08_turn_warnings_into_errors_in_tests():
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        try:
            get_user(2)
        except DeprecationWarning as exc:
            print("raised in strict mode:", exc)


def example_09_rename_shim():
    def new_name(x): return x * 2
    old_name = deprecated("old_name was renamed to new_name")(new_name)
    print(capture(lambda: old_name(21)))


def example_10_stacklevel_points_at_caller():
    @deprecated("use v2", stacklevel=1)
    def v1(): return "v1"
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        v1()
    print("warning reported at line", w[0].lineno)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
