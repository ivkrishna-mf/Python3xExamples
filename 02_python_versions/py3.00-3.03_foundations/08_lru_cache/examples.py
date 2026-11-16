"""functools.lru_cache — Python 3.2+ (bare @lru_cache without parentheses needs 3.8)."""
import time
from functools import lru_cache

MIN_VERSION = (3, 8)


def example_01_fibonacci():
    @lru_cache(maxsize=None)
    def fib(n):
        return n if n < 2 else fib(n - 1) + fib(n - 2)
    print(fib(80))


def example_02_cache_info():
    @lru_cache(maxsize=32)
    def square(x): return x * x
    for x in [1, 2, 1, 1, 3]:
        square(x)
    print(square.cache_info())


def example_03_cache_clear():
    @lru_cache
    def f(x): return x
    f(1); f(1)
    f.cache_clear()
    print(f.cache_info())


def example_04_slow_lookup():
    @lru_cache(maxsize=128)
    def get_rate(currency):
        time.sleep(0.1)          # pretend network call
        return {"USD": 1.0, "EUR": 0.92}[currency]
    t = time.perf_counter(); get_rate("EUR"); first = time.perf_counter() - t
    t = time.perf_counter(); get_rate("EUR"); second = time.perf_counter() - t
    print(f"first {first:.3f}s, cached {second:.6f}s")


def example_05_eviction_with_small_maxsize():
    @lru_cache(maxsize=2)
    def f(x): return x
    for x in [1, 2, 3, 1]:   # 1 is evicted when 3 arrives
        f(x)
    print(f.cache_info())


def example_06_typed_flag():
    @lru_cache(typed=True)
    def describe(x): return f"{x!r} ({type(x).__name__})"
    print(describe(1), describe(1.0), describe.cache_info().currsize)


def example_07_unhashable_args_fail():
    @lru_cache
    def total(items): return sum(items)
    try:
        total([1, 2])
    except TypeError as exc:
        print("TypeError:", exc, "-> pass a tuple instead:", total((1, 2)))


def example_08_dynamic_programming_grid_paths():
    @lru_cache(maxsize=None)
    def paths(r, c):
        if r == 0 or c == 0:
            return 1
        return paths(r - 1, c) + paths(r, c - 1)
    print(paths(16, 16))


def example_09_parse_once():
    @lru_cache(maxsize=None)
    def load_settings(env):
        print(f"  parsing settings for {env}...")
        return {"env": env, "debug": env == "dev"}
    load_settings("dev"); load_settings("dev")
    print(load_settings("dev"))


def example_10_wrapped_original():
    @lru_cache
    def f(x): return x * 2
    print(f.__wrapped__(21), "(bypasses cache)")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
