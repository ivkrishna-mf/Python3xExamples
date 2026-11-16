"""Iterators & generators — modern style."""
from collections.abc import Generator, Iterable, Iterator
from itertools import islice

MIN_VERSION = (3, 9)


def example_01_iter_and_next():
    it = iter([10, 20])
    print(next(it), next(it), next(it, "exhausted"))


def example_02_simple_generator():
    def countdown(n: int) -> Iterator[int]:
        while n > 0:
            yield n
            n -= 1
    print(list(countdown(5)))


def example_03_infinite_generator():
    def ids(prefix: str) -> Iterator[str]:
        n = 0
        while True:
            n += 1
            yield f"{prefix}{n:03d}"
    print(list(islice(ids("ORD-"), 3)))


def example_04_pipeline():
    lines = ["INFO ok", "ERROR db down", "INFO ok", "ERROR timeout"]
    def errors(ls: Iterable[str]) -> Iterator[str]:
        return (l for l in ls if l.startswith("ERROR"))
    def messages(ls: Iterable[str]) -> Iterator[str]:
        return (l.split(" ", 1)[1] for l in ls)
    print(list(messages(errors(lines))))


def example_05_custom_iterator_class():
    class Range2:
        def __init__(self, stop: int): self.i, self.stop = 0, stop
        def __iter__(self): return self
        def __next__(self) -> int:
            if self.i >= self.stop:
                raise StopIteration
            self.i += 1
            return self.i * 2
    print(list(Range2(4)))


def example_06_iterable_class_with_generator():
    class Deck:
        def __init__(self): self.cards = [f"{r}{s}" for s in "♠♥" for r in "AK"]
        def __iter__(self): yield from self.cards
    print(list(Deck()))


def example_07_send_values_into_generator():
    def running_avg() -> Generator[float, float, None]:
        total = count = 0
        avg = 0.0
        while True:
            value = yield avg
            total += value; count += 1
            avg = total / count
    g = running_avg(); next(g)
    print([g.send(v) for v in (10, 20, 60)])


def example_08_generators_exhaust():
    gen = (x for x in range(3))
    print(list(gen), list(gen), "<- second pass is empty")


def example_09_memory_efficiency():
    import sys
    lst = [n for n in range(100_000)]
    gen = (n for n in range(100_000))
    print(sys.getsizeof(lst), "bytes vs", sys.getsizeof(gen), "bytes")


def example_10_chunked_reader():
    def chunks(data: str, size: int) -> Iterator[str]:
        for i in range(0, len(data), size):
            yield data[i:i + size]
    print(list(chunks("abcdefghij", 4)))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
