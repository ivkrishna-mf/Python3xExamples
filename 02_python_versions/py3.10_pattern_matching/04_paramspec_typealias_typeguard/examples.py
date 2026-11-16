"""ParamSpec / Concatenate / TypeAlias / TypeGuard — Python 3.10+ (PEP 612, 613, 647)."""
import functools
import time
from typing import Callable, Concatenate, ParamSpec, TypeAlias, TypeGuard, TypeVar

MIN_VERSION = (3, 10)
P = ParamSpec("P")
R = TypeVar("R")


def logged(fn: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"  -> {fn.__name__}{args}{kwargs}")
        return fn(*args, **kwargs)
    return wrapper


def example_01_signature_preserving_decorator():
    @logged
    def add(a: int, b: int = 0) -> int:
        return a + b
    print(add(2, b=3))


def example_02_retry_decorator_factory():
    def retry(times: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
        def deco(fn: Callable[P, R]) -> Callable[P, R]:
            @functools.wraps(fn)
            def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
                for attempt in range(1, times + 1):
                    try:
                        return fn(*args, **kwargs)
                    except ValueError as exc:
                        print(f"  attempt {attempt} failed: {exc}")
                raise RuntimeError("gave up")
            return wrapper
        return deco
    calls = iter([ValueError("flaky"), ValueError("flaky"), "ok"])
    @retry(3)
    def fetch(url: str) -> str:
        v = next(calls)
        if isinstance(v, Exception):
            raise v
        return f"{url}: {v}"
    print(fetch("https://api"))


def example_03_timing_decorator():
    def timed(fn: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            t = time.perf_counter()
            try:
                return fn(*args, **kwargs)
            finally:
                print(f"  {fn.__name__} took {time.perf_counter() - t:.4f}s")
        return wrapper
    @timed
    def work(n: int) -> int: return sum(range(n))
    print(work(100_000))


def example_04_concatenate_injects_argument():
    class Db:
        def query(self, sql: str) -> str: return f"rows for {sql!r}"
    def with_db(fn: Callable[Concatenate[Db, P], R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            return fn(Db(), *args, **kwargs)
        return wrapper
    @with_db
    def get_user(db: Db, uid: int) -> str:
        return db.query(f"SELECT * FROM users WHERE id={uid}")
    print(get_user(7))           # caller doesn't pass db


def example_05_type_alias():
    JsonValue: TypeAlias = "dict[str, JsonValue] | list[JsonValue] | str | int | float | bool | None"
    Headers: TypeAlias = dict[str, str]
    def send(h: Headers) -> int: return len(h)
    print(send({"Accept": "*/*"}), JsonValue[:20] + "...")


def example_06_typeguard_list_check():
    def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
        return all(isinstance(x, str) for x in val)
    data: list[object] = ["a", "b"]
    if is_str_list(data):
        print(" ".join(data).upper())       # checker knows data is list[str]


def example_07_typeguard_for_dict_payload():
    def is_user(obj: object) -> TypeGuard[dict[str, str]]:
        return isinstance(obj, dict) and {"name", "email"} <= obj.keys()
    payload: object = {"name": "ann", "email": "a@x.io"}
    print(is_user(payload), is_user({"name": "x"}))


def example_08_paramspec_args_inspection():
    print(P.args, P.kwargs, P.__name__)


def example_09_callback_registry():
    handlers: dict[str, Callable[..., None]] = {}
    def on(event: str) -> Callable[[Callable[P, None]], Callable[P, None]]:
        def deco(fn: Callable[P, None]) -> Callable[P, None]:
            handlers[event] = fn
            return fn
        return deco
    @on("signup")
    def welcome(user: str, *, vip: bool = False) -> None:
        print("  welcome", user, "(VIP)" if vip else "")
    handlers["signup"]("ann", vip=True)


def example_10_wraps_keeps_metadata():
    @logged
    def documented(x: int) -> int:
        """Doubles x."""
        return x * 2
    print(documented.__name__, "|", documented.__doc__, "|", documented.__wrapped__(4))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
