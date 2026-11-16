"""frozendict — Python 3.15+ (PEP 814)."""
import copy
import json
import pickle
from collections.abc import Mapping
from functools import cache

MIN_VERSION = (3, 15)
DEFAULTS = frozendict(host="localhost", port=5432, ssl=False)


def example_01_create_and_read():
    print(DEFAULTS, DEFAULTS["port"], DEFAULTS.get("user", "postgres"))


def example_02_cannot_modify():
    try:
        DEFAULTS["port"] = 1
    except TypeError as exc:
        print("TypeError:", exc)


def example_03_merge_returns_new_frozendict():
    prod = DEFAULTS | {"host": "db.prod", "ssl": True}
    print(prod, type(prod).__name__)


def example_04_hashable_as_key():
    cache_by_cfg = {DEFAULTS: "connection-1"}
    print(cache_by_cfg[frozendict(ssl=False, port=5432, host="localhost")])


def example_05_order_insensitive_equality():
    print(frozendict(a=1, b=2) == frozendict(b=2, a=1), frozendict(a=1) == {"a": 1})


def example_06_works_with_functools_cache():
    @cache
    def connect(cfg: frozendict) -> str:
        print("  opening new connection...")
        return f"conn to {cfg['host']}"
    connect(DEFAULTS); print(connect(DEFAULTS))


def example_07_not_a_dict_subclass():
    print(isinstance(DEFAULTS, dict), isinstance(DEFAULTS, Mapping))


def example_08_json_and_pickle():
    print(json.dumps(DEFAULTS), pickle.loads(pickle.dumps(DEFAULTS)) == DEFAULTS)


def example_09_fully_immutable_json():
    data = json.loads('{"users": [{"id": 1}, {"id": 2}]}', object_hook=frozendict, array_hook=tuple)
    print(data, hash(data) is not None)


def example_10_copy_and_thaw():
    print(copy.copy(DEFAULTS) is DEFAULTS, "| mutable copy:", dict(DEFAULTS))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
