"""Dunder methods — modern style."""
from __future__ import annotations

import math
from functools import total_ordering

MIN_VERSION = (3, 10)


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x, self.y = x, y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, k: float) -> Vector:
        return Vector(self.x * k, self.y * k)

    __rmul__ = __mul__

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __bool__(self) -> bool:
        return bool(self.x or self.y)

    def __iter__(self):
        yield self.x
        yield self.y


def example_01_repr_and_str():
    v = Vector(1, 2)
    print(repr(v), str(v), f"{v!r}")


def example_02_arithmetic_operators():
    print(Vector(1, 2) + Vector(3, 4), Vector(1, 2) * 3, 2 * Vector(1, 1))


def example_03_abs_bool_eq_hash():
    print(abs(Vector(3, 4)), bool(Vector(0, 0)), Vector(1, 1) == Vector(1, 1), len({Vector(1, 1), Vector(1, 1)}))


def example_04_iteration_and_unpacking():
    x, y = Vector(5, 6)
    print(x, y, list(Vector(7, 8)))


def example_05_container_protocol():
    class Playlist:
        def __init__(self, *songs: str): self._songs = list(songs)
        def __len__(self): return len(self._songs)
        def __getitem__(self, i): return self._songs[i]
        def __contains__(self, s): return s in self._songs
    p = Playlist("a", "b", "c")
    print(len(p), p[0], p[-1], p[1:], "b" in p, list(p))


def example_06_ordering_with_total_ordering():
    @total_ordering
    class Money:
        def __init__(self, cents: int): self.cents = cents
        def __eq__(self, o): return self.cents == o.cents
        def __lt__(self, o): return self.cents < o.cents
        def __repr__(self): return f"${self.cents / 100:.2f}"
    print(sorted([Money(500), Money(199), Money(1000)]), Money(5) >= Money(3))


def example_07_callable_objects():
    class Multiplier:
        def __init__(self, k: int): self.k = k
        def __call__(self, x: int) -> int: return x * self.k
    triple = Multiplier(3)
    print(triple(7), callable(triple))


def example_08_context_manager_protocol():
    class Timer:
        def __enter__(self):
            import time; self.t = time.perf_counter(); return self
        def __exit__(self, *exc):
            import time; print(f"  elapsed {time.perf_counter() - self.t:.4f}s"); return False
    with Timer():
        sum(range(100_000))


def example_09_format_protocol():
    class Celsius:
        def __init__(self, v: float): self.v = v
        def __format__(self, spec: str) -> str:
            return f"{self.v * 9 / 5 + 32:.1f}°F" if spec == "F" else f"{self.v:{spec or '.1f'}}°C"
    t = Celsius(21.456)
    print(f"{t} | {t:.2f} | {t:F}")


def example_10_attribute_access_hooks():
    class Config:
        def __init__(self, data: dict): self._data = data
        def __getattr__(self, name):            # only called when normal lookup fails
            try:
                return self._data[name]
            except KeyError:
                raise AttributeError(name) from None
    cfg = Config({"host": "db", "port": 5432})
    print(cfg.host, cfg.port, hasattr(cfg, "user"))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
