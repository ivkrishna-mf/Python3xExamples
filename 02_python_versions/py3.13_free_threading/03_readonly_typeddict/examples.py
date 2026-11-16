"""ReadOnly in TypedDict — Python 3.13+ (PEP 705)."""
from types import MappingProxyType
from typing import NotRequired, ReadOnly, TypedDict

MIN_VERSION = (3, 13)


class Order(TypedDict):
    id: ReadOnly[int]
    created: ReadOnly[str]
    status: str


def example_01_normal_key_can_change():
    o: Order = {"id": 1, "created": "2026-11-16", "status": "new"}
    o["status"] = "paid"
    print(o)


def example_02_readonly_flagged_by_checker():
    o: Order = {"id": 1, "created": "2026-11-16", "status": "new"}
    # o["id"] = 2   <- mypy/pyright: "id" is a read-only key
    print("id stays", o["id"])


def example_03_introspect_readonly_keys():
    print(sorted(Order.__readonly_keys__), sorted(Order.__mutable_keys__))


def example_04_readonly_parameter_accepts_subtypes():
    class HasName(TypedDict):
        name: ReadOnly[str | None]
    class Person(TypedDict):
        name: str
    def greet(x: HasName) -> str:
        return f"hi {x['name']}"
    p: Person = {"name": "ann"}
    print(greet(p))       # OK only because 'name' is ReadOnly in HasName


def example_05_combined_with_notrequired():
    class Profile(TypedDict):
        user_id: ReadOnly[int]
        bio: NotRequired[ReadOnly[str]]
    p: Profile = {"user_id": 9}
    print(p, Profile.__readonly_keys__)


def example_06_runtime_is_still_mutable():
    o: Order = {"id": 1, "created": "x", "status": "new"}
    o["id"] = 99            # type: ignore  (Python itself doesn't stop this)
    print(o["id"], "-> ReadOnly is a static guarantee only")


def example_07_true_runtime_readonly_view():
    o = {"id": 1, "status": "new"}
    view = MappingProxyType(o)
    try:
        view["id"] = 2
    except TypeError as exc:
        print("MappingProxyType:", exc)


def example_08_audit_event():
    class AuditEvent(TypedDict):
        event_id: ReadOnly[str]
        actor: ReadOnly[str]
        at: ReadOnly[str]
        notes: list[str]
    e: AuditEvent = {"event_id": "e1", "actor": "ann", "at": "09:00", "notes": []}
    e["notes"].append("reviewed")
    print(e)


def example_09_functional_syntax():
    Cfg = TypedDict("Cfg", {"env": ReadOnly[str], "debug": bool})
    print(Cfg.__readonly_keys__)


def example_10_inheritance_keeps_readonly():
    class Base(TypedDict):
        id: ReadOnly[int]
    class Child(Base):
        label: str
    print(Child.__readonly_keys__, Child.__mutable_keys__)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
