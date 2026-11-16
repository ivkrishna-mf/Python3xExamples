"""tomllib — Python 3.11+ (PEP 680)."""
import tempfile
import tomllib
from pathlib import Path

MIN_VERSION = (3, 11)

CONFIG = """
title = "Orders service"
debug = false
started = 2026-11-16T09:00:00Z

[server]
host = "0.0.0.0"
port = 8080
workers = 4

[database]
url = "postgresql://localhost/orders"
pool = { min = 2, max = 10 }

[[jobs]]
name = "cleanup"
cron = "0 3 * * *"

[[jobs]]
name = "report"
cron = "0 8 * * 1"
"""


def example_01_loads_string():
    cfg = tomllib.loads(CONFIG)
    print(cfg["title"], cfg["debug"])


def example_02_typed_values():
    cfg = tomllib.loads(CONFIG)
    print(type(cfg["server"]["port"]).__name__, type(cfg["started"]).__name__)


def example_03_nested_tables():
    print(tomllib.loads(CONFIG)["database"]["pool"])


def example_04_array_of_tables():
    print([j["name"] for j in tomllib.loads(CONFIG)["jobs"]])


def example_05_load_from_binary_file():
    path = Path(tempfile.mkdtemp()) / "app.toml"
    path.write_text(CONFIG, encoding="utf-8")
    with path.open("rb") as fh:          # must be binary mode
        print(tomllib.load(fh)["server"]["host"])


def example_06_read_pyproject():
    pyproject = 'project = { name = "demo", version = "0.1.0", dependencies = ["requests>=2"] }'
    meta = tomllib.loads(pyproject)["project"]
    print(meta["name"], meta["version"], meta["dependencies"])


def example_07_decode_error():
    try:
        tomllib.loads("port = = 1")
    except tomllib.TOMLDecodeError as exc:
        print("TOMLDecodeError:", exc)


def example_08_defaults_merge():
    defaults = {"host": "127.0.0.1", "port": 8000, "workers": 1}
    print(defaults | tomllib.loads(CONFIG)["server"])


def example_09_decimal_floats():
    from decimal import Decimal
    print(tomllib.loads("price = 0.1", parse_float=Decimal))


def example_10_dotted_keys_and_multiline_strings():
    doc = 'app.name = "x"\napp.owner.email = "ops@x.io"\nmotd = """\nHello\nWorld"""'
    print(tomllib.loads(doc))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
