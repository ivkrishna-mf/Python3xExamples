"""Decorators — modern style (3.12 type-parameter syntax)."""
import functools
import time
from collections.abc import Callable

MIN_VERSION = (3, 12)


def timer[**P, R](fn: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            print(f"  {fn.__name__} took {time.perf_counter() - start:.4f}s")
    return wrapper


def example_01_basic_decorator():
    @timer
    def compute(n: int) -> int:
        return sum(range(n))
    print(compute(500_000))


def example_02_wraps_preserves_metadata():
    @timer
    def documented():
        """I have docs."""
    print(documented.__name__, documented.__doc__)


def example_03_decorator_with_arguments():
    def repeat(times: int):
        def deco[**P, R](fn: Callable[P, R]) -> Callable[P, list[R]]:
            @functools.wraps(fn)
            def wrapper(*args: P.args, **kwargs: P.kwargs) -> list[R]:
                return [fn(*args, **kwargs) for _ in range(times)]
            return wrapper
        return deco
    @repeat(3)
    def roll() -> str: return "🎲"
    print(roll())


def example_04_retry():
    def retry(attempts: int, exceptions: tuple[type[Exception], ...] = (Exception,)):
        def deco(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kwargs):
                for i in range(1, attempts + 1):
                    try:
                        return fn(*args, **kwargs)
                    except exceptions as exc:
                        print(f"  attempt {i} failed: {exc}")
                raise RuntimeError(f"{fn.__name__} failed after {attempts} attempts")
            return wrapper
        return deco
    outcomes = iter([ConnectionError("down"), "ok"])
    @retry(3, (ConnectionError,))
    def call():
        r = next(outcomes)
        if isinstance(r, Exception): raise r
        return r
    print(call())


def example_05_registration():
    handlers: dict[str, Callable] = {}
    def route(path: str):
        def deco(fn):
            handlers[path] = fn
            return fn
        return deco
    @route("/")
    def home(): return "home page"
    @route("/about")
    def about(): return "about page"
    print({p: f() for p, f in handlers.items()})


def example_06_stacking_order():
    def bold(fn): return lambda: f"<b>{fn()}</b>"
    def italic(fn): return lambda: f"<i>{fn()}</i>"
    @bold
    @italic
    def text(): return "hi"
    print(text())          # bold(italic(text))


def example_07_class_decorator():
    def add_repr(cls):
        cls.__repr__ = lambda self: f"{cls.__name__}({vars(self)})"
        return cls
    @add_repr
    class User:
        def __init__(self, name): self.name = name
    print(User("ann"))


def example_08_validation():
    def positive_args(fn):
        @functools.wraps(fn)
        def wrapper(*args):
            if any(a <= 0 for a in args):
                raise ValueError(f"{fn.__name__}: all args must be > 0")
            return fn(*args)
        return wrapper
    @positive_args
    def volume(l, w, h): return l * w * h
    print(volume(2, 3, 4))
    try:
        volume(2, -1, 3)
    except ValueError as exc:
        print("ValueError:", exc)


def example_09_memoize_builtin():
    @functools.cache
    def fib(n: int) -> int:
        return n if n < 2 else fib(n - 1) + fib(n - 2)
    print(fib(100))


def example_10_stateful_decorator_class():
    class CountCalls:
        def __init__(self, fn):
            functools.update_wrapper(self, fn)
            self.fn, self.calls = fn, 0
        def __call__(self, *args, **kwargs):
            self.calls += 1
            return self.fn(*args, **kwargs)
    @CountCalls
    def ping(): return "pong"
    ping(); ping()
    print(ping.__name__, "called", ping.calls, "times")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
