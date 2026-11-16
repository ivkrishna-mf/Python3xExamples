"""itertools & functools — modern style (3.12+ for batched)."""
import itertools as it
from functools import total_ordering

MIN_VERSION = (3, 12)


def example_01_chain():
    print(list(it.chain([1, 2], "ab", range(2))))


def example_02_groupby_sorted_data():
    sales = sorted([("EU", 5), ("US", 3), ("EU", 2), ("US", 7)])
    print({region: sum(q for _, q in rows) for region, rows in it.groupby(sales, key=lambda r: r[0])})


def example_03_accumulate_running_total():
    print(list(it.accumulate([3, 1, 4, 1, 5])), list(it.accumulate([3, 1, 4], max)))


def example_04_combinatorics():
    print(list(it.combinations("ABC", 2)), len(list(it.permutations(range(4)))), list(it.product([0, 1], repeat=2)))


def example_05_count_cycle_islice():
    print(list(it.islice(it.count(10, 5), 4)), list(it.islice(it.cycle("RGB"), 7)))


def example_06_zip_longest():
    print(list(it.zip_longest("abc", [1], fillvalue="-")))


def example_07_takewhile_dropwhile():
    nums = [1, 3, 5, 6, 7]
    print(list(it.takewhile(lambda n: n % 2, nums)), list(it.dropwhile(lambda n: n % 2, nums)))


def example_08_pairwise_and_batched():
    print(list(it.pairwise([1, 4, 9])), list(it.batched(range(7), 3)))


def example_09_starmap_and_compress():
    print(list(it.starmap(pow, [(2, 3), (3, 2)])), list(it.compress("ABCD", [1, 0, 1, 0])))


def example_10_total_ordering():
    @total_ordering
    class Version:
        def __init__(self, s: str): self.parts = tuple(map(int, s.split(".")))
        def __eq__(self, o): return self.parts == o.parts
        def __lt__(self, o): return self.parts < o.parts
        def __repr__(self): return ".".join(map(str, self.parts))
    vs = [Version("3.12"), Version("3.9"), Version("3.15")]
    print(sorted(vs), Version("3.10") >= Version("3.9"))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
