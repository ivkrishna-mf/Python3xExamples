"""functools.cached_property — Python 3.8+."""
import statistics
import time
from functools import cached_property

MIN_VERSION = (3, 8)


class Dataset:
    def __init__(self, values):
        self.values = values
        self.computations = 0

    @cached_property
    def stats(self):
        self.computations += 1
        time.sleep(0.05)
        return {"mean": statistics.mean(self.values), "max": max(self.values)}


def example_01_computed_once():
    d = Dataset([1, 2, 3])
    d.stats; d.stats; d.stats
    print(d.stats, "computed", d.computations, "time(s)")


def example_02_stored_in_instance_dict():
    d = Dataset([4, 5])
    print("stats" in d.__dict__); d.stats; print("stats" in d.__dict__)


def example_03_invalidate_with_del():
    d = Dataset([1, 2])
    d.stats
    d.values.append(100)
    del d.stats
    print(d.stats, "computations:", d.computations)


def example_04_per_instance():
    a, b = Dataset([1]), Dataset([2])
    print(a.stats["mean"], b.stats["mean"])


def example_05_lazy_heavy_resource():
    class Report:
        @cached_property
        def template(self):
            print("  loading template from disk...")
            return "<h1>{title}</h1>"
    r = Report()
    print(r.template.format(title="A"), r.template.format(title="B"))


def example_06_compiled_regex():
    import re
    class Validator:
        def __init__(self, pattern): self.pattern = pattern
        @cached_property
        def regex(self): return re.compile(self.pattern)
    v = Validator(r"^\d{3}-\d{4}$")
    print(bool(v.regex.match("555-1234")), bool(v.regex.match("nope")))


def example_07_can_be_overwritten():
    d = Dataset([1])
    d.stats = {"mean": "manual"}
    print(d.stats)


def example_08_vs_property():
    class Circle:
        def __init__(self, r): self.r = r
        @property
        def area_live(self): return 3.14159 * self.r ** 2
        @cached_property
        def area_cached(self): return 3.14159 * self.r ** 2
    c = Circle(1); c.area_cached; c.r = 2
    print(f"live={c.area_live:.2f} cached(stale)={c.area_cached:.2f}")


def example_09_timing():
    d = Dataset(list(range(1000)))
    t = time.perf_counter(); d.stats; first = time.perf_counter() - t
    t = time.perf_counter(); d.stats; again = time.perf_counter() - t
    print(f"first {first:.3f}s, again {again:.6f}s")


def example_10_slots_incompatible():
    class Slotted:
        __slots__ = ("x",)
        @cached_property
        def y(self): return 1
    try:
        Slotted().y
    except TypeError as exc:
        print("TypeError:", str(exc)[:70], "...")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
