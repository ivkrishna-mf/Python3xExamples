"""zip(strict) / pairwise / bit_count / bisect key / aiter-anext — Python 3.10+."""
import asyncio
import bisect
from itertools import pairwise

MIN_VERSION = (3, 10)


def example_01_strict_zip_ok():
    print(list(zip("abc", [1, 2, 3], strict=True)))


def example_02_strict_zip_mismatch():
    try:
        list(zip(["id", "name"], [1, "ann", "extra"], strict=True))
    except ValueError as exc:
        print("ValueError:", exc)


def example_03_csv_row_to_dict_safely():
    header = ["id", "name", "email"]
    row = ["1", "ann", "ann@x.io"]
    print(dict(zip(header, row, strict=True)))


def example_04_pairwise_deltas():
    prices = [100, 104, 101, 110]
    print([b - a for a, b in pairwise(prices)])


def example_05_pairwise_transitions():
    states = ["new", "paid", "shipped", "delivered"]
    print([f"{a}->{b}" for a, b in pairwise(states)])


def example_06_pairwise_is_sorted():
    def is_sorted(xs): return all(a <= b for a, b in pairwise(xs))
    print(is_sorted([1, 2, 2, 5]), is_sorted([3, 1]))


def example_07_route_distances():
    stops = [0, 12.5, 30.0, 41.2]
    print([round(b - a, 1) for a, b in pairwise(stops)])


def example_08_int_bit_count():
    print([n.bit_count() for n in (0, 7, 255, 1024)])


def example_09_bisect_with_key():
    events = [(1, "boot"), (5, "login"), (9, "logout")]   # sorted by time
    i = bisect.bisect_right(events, 6, key=lambda e: e[0])
    print("last event before t=6:", events[i - 1])


def example_10_aiter_anext_builtins():
    async def agen():
        for i in range(3):
            yield i
    async def main():
        it = aiter(agen())
        print(await anext(it), await anext(it), await anext(it), await anext(it, "done"))
    asyncio.run(main())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
