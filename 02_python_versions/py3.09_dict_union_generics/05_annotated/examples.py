"""typing.Annotated — Python 3.9+ (PEP 593)."""
from dataclasses import dataclass, fields
from typing import Annotated, get_args, get_origin, get_type_hints

MIN_VERSION = (3, 9)


@dataclass(frozen=True)
class Gt:
    value: float


@dataclass(frozen=True)
class MaxLen:
    value: int


@dataclass
class Product:
    name: Annotated[str, MaxLen(10)]
    price: Annotated[float, Gt(0)]
    qty: Annotated[int, Gt(-1)] = 0


def validate(obj):
    hints = get_type_hints(type(obj), include_extras=True)
    errors = []
    for f in fields(obj):
        value = getattr(obj, f.name)
        for meta in get_args(hints[f.name])[1:]:
            if isinstance(meta, Gt) and not value > meta.value:
                errors.append(f"{f.name} must be > {meta.value}")
            if isinstance(meta, MaxLen) and len(value) > meta.value:
                errors.append(f"{f.name} longer than {meta.value}")
    return errors or ["ok"]


def example_01_still_the_base_type():
    print(get_type_hints(Product)["price"])


def example_02_read_metadata():
    hints = get_type_hints(Product, include_extras=True)
    print(get_args(hints["price"]))


def example_03_origin_is_annotated():
    print(get_origin(Annotated[int, "meta"]) is Annotated)


def example_04_validate_ok():
    print(validate(Product("pen", 1.5, 3)))


def example_05_validate_errors():
    print(validate(Product("a-very-long-name", 0)))


def example_06_reusable_aliases():
    PositiveInt = Annotated[int, Gt(0)]
    def set_workers(n: PositiveInt) -> None: ...
    print(get_type_hints(set_workers, include_extras=True)["n"])


def example_07_units_as_metadata():
    Meters = Annotated[float, "unit:m"]
    Seconds = Annotated[float, "unit:s"]
    def speed(d: Meters, t: Seconds) -> Annotated[float, "unit:m/s"]:
        return d / t
    hints = get_type_hints(speed, include_extras=True)
    print({k: get_args(v)[1] for k, v in hints.items()}, speed(100, 9.58))


def example_08_cli_option_style():
    def cli(name: Annotated[str, "--name", "Who to greet"] = "world"):
        return f"hello {name}"
    meta = get_args(get_type_hints(cli, include_extras=True)["name"])[1:]
    print(meta, cli())


def example_09_nested_annotated_flattens():
    print(Annotated[Annotated[int, "a"], "b"])


def example_10_dependency_injection_marker():
    class Depends:
        def __init__(self, factory): self.factory = factory
    def get_db(): return "db-connection"
    def handler(db: Annotated[str, Depends(get_db)]):
        return f"using {db}"
    hints = get_type_hints(handler, include_extras=True)
    kwargs = {n: get_args(h)[1].factory() for n, h in hints.items()
              if get_origin(h) is Annotated and isinstance(get_args(h)[1], Depends)}
    print(handler(**kwargs))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
