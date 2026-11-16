"""enum — Python 3.4+ (PEP 435); Flag/auto 3.6+, StrEnum 3.11+."""
import sys
from enum import Enum, IntEnum, Flag, auto, unique

MIN_VERSION = (3, 6)


class Status(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    CLOSED = "closed"


def example_01_access_members():
    print(Status.ACTIVE, Status.ACTIVE.name, Status.ACTIVE.value)


def example_02_lookup_by_value_and_name():
    print(Status("closed"), Status["PENDING"])


def example_03_iterate():
    print([s.value for s in Status])


def example_04_identity_comparison():
    s = Status("active")
    print(s is Status.ACTIVE, s == "active")   # True False – not a string!


def example_05_auto_values():
    class Priority(Enum):
        LOW = auto()
        MEDIUM = auto()
        HIGH = auto()
    print([(p.name, p.value) for p in Priority])


def example_06_intenum_compares_with_int():
    class Level(IntEnum):
        DEBUG = 10
        ERROR = 40
    print(Level.ERROR > 20, sorted([Level.ERROR, Level.DEBUG]))


def example_07_flags():
    class Perm(Flag):
        READ = auto()
        WRITE = auto()
        EXEC = auto()
    rw = Perm.READ | Perm.WRITE
    print(rw, Perm.WRITE in rw, Perm.EXEC in rw)


def example_08_methods_on_enum():
    class Planet(Enum):
        EARTH = (5.97e24, 6.37e6)
        MARS = (6.42e23, 3.39e6)
        def __init__(self, mass, radius):
            self.mass, self.radius = mass, radius
        @property
        def gravity(self):
            return 6.674e-11 * self.mass / self.radius ** 2
    print(f"{Planet.MARS.gravity:.2f} m/s²")


def example_09_unique_guard():
    try:
        @unique
        class Dup(Enum):
            A = 1
            B = 1
    except ValueError as exc:
        print("ValueError:", exc)


def example_10_strenum_311():
    if sys.version_info >= (3, 11):
        from enum import StrEnum
        class Method(StrEnum):
            GET = auto()
            POST = auto()
        print(Method.GET, Method.GET == "get", f"{Method.POST}")
    else:
        print("StrEnum needs Python 3.11+")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
