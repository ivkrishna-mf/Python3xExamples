"""Built-in generics — Python 3.9+ (PEP 585)."""
import re
from collections import defaultdict, deque
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence

MIN_VERSION = (3, 9)


def example_01_list_and_dict():
    def word_lengths(words: list[str]) -> dict[str, int]:
        return {w: len(w) for w in words}
    print(word_lengths(["hi", "there"]))


def example_02_tuples_fixed_and_variadic():
    def bounds(nums: tuple[int, ...]) -> tuple[int, int]:
        return min(nums), max(nums)
    print(bounds((4, 1, 9)))


def example_03_set_and_frozenset():
    def unique(items: list[int]) -> set[int]:
        return set(items)
    tags: frozenset[str] = frozenset({"a", "b"})
    print(unique([1, 1, 2]), tags)


def example_04_abc_iterables():
    def total(xs: Iterable[float]) -> float:
        return sum(xs)
    print(total([1.5, 2.5]), total(x for x in range(4)))


def example_05_callable_from_abc():
    def apply_all(fns: Sequence[Callable[[int], int]], x: int) -> list[int]:
        return [f(x) for f in fns]
    print(apply_all([abs, lambda v: v * 2], -3))


def example_06_mapping_param():
    def render(ctx: Mapping[str, object]) -> str:
        return ", ".join(f"{k}={v}" for k, v in ctx.items())
    print(render({"a": 1, "b": "x"}))


def example_07_collections_classes():
    q: deque[int] = deque([1, 2])
    groups: defaultdict[str, list[str]] = defaultdict(list)
    groups["a"].append("apple")
    print(q, dict(groups))


def example_08_re_pattern():
    def compile_all(patterns: list[str]) -> list[re.Pattern[str]]:
        return [re.compile(p) for p in patterns]
    print(compile_all([r"\d+"])[0].findall("a1b22"))


def example_09_type_objects_at_runtime():
    alias = dict[str, list[int]]
    print(alias, alias.__origin__, alias.__args__)


def example_10_generator_type():
    def countdown(n: int) -> Iterator[int]:
        while n:
            yield n
            n -= 1
    print(list(countdown(3)))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
