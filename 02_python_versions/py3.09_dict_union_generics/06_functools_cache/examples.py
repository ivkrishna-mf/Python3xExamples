"""functools.cache — Python 3.9+."""
from functools import cache

MIN_VERSION = (3, 9)


def example_01_factorial():
    @cache
    def fact(n): return 1 if n < 2 else n * fact(n - 1)
    print(fact(30))


def example_02_cache_info():
    @cache
    def sq(x): return x * x
    [sq(i % 3) for i in range(10)]
    print(sq.cache_info())


def example_03_coin_change_dp():
    coins = (1, 5, 10, 25)
    @cache
    def ways(amount, i=0):
        if amount == 0: return 1
        if amount < 0 or i == len(coins): return 0
        return ways(amount - coins[i], i) + ways(amount, i + 1)
    print(ways(100))


def example_04_edit_distance():
    def distance(a, b):
        @cache
        def d(i, j):
            if i == 0: return j
            if j == 0: return i
            return min(d(i - 1, j) + 1, d(i, j - 1) + 1, d(i - 1, j - 1) + (a[i - 1] != b[j - 1]))
        return d(len(a), len(b))
    print(distance("kitten", "sitting"))


def example_05_staircase():
    @cache
    def climb(n): return 1 if n <= 1 else climb(n - 1) + climb(n - 2)
    print(climb(50))


def example_06_cache_clear():
    @cache
    def f(x): return x
    f(1); f.cache_clear()
    print(f.cache_info().currsize)


def example_07_keyword_args_are_distinct_keys():
    @cache
    def f(a, b=0): return a + b
    f(1, 2); f(1, b=2)
    print(f.cache_info().currsize, "entries (positional vs keyword call)")


def example_08_lookup_table():
    @cache
    def country_name(code):
        print(f"  looking up {code}")
        return {"IN": "India", "US": "United States"}.get(code, "?")
    country_name("IN"); country_name("IN")
    print(country_name("US"))


def example_09_with_staticmethod():
    class MathUtil:
        @staticmethod
        @cache
        def primes_upto(n):
            return [p for p in range(2, n + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]
    print(MathUtil.primes_upto(30))


def example_10_longest_increasing_subsequence():
    nums = (10, 9, 2, 5, 3, 7, 101, 18)
    @cache
    def lis_from(i):
        return 1 + max((lis_from(j) for j in range(i + 1, len(nums)) if nums[j] > nums[i]), default=0)
    print(max(lis_from(i) for i in range(len(nums))))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
