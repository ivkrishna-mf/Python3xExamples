"""Dict | and |= — Python 3.9+ (PEP 584)."""
from collections import ChainMap, Counter, defaultdict

MIN_VERSION = (3, 9)
defaults = {"host": "localhost", "port": 5432, "debug": False}


def example_01_merge_new_dict():
    print(defaults | {"port": 6543})


def example_02_right_side_wins():
    print({"a": 1, "b": 2} | {"b": 20, "c": 30})


def example_03_in_place_update():
    cfg = dict(defaults)
    cfg |= {"debug": True}
    print(cfg)


def example_04_layered_config():
    file_cfg = {"port": 7000}
    env_cfg = {"debug": True}
    cli_cfg = {"host": "0.0.0.0"}
    print(defaults | file_cfg | env_cfg | cli_cfg)


def example_05_inplace_accepts_pairs():
    d = {"a": 1}
    d |= [("b", 2), ("c", 3)]
    print(d)


def example_06_plain_or_rejects_pairs():
    try:
        {"a": 1} | [("b", 2)]
    except TypeError as exc:
        print("TypeError:", exc)


def example_07_shallow_not_deep():
    a = {"db": {"host": "x", "port": 1}}
    b = {"db": {"port": 2}}
    print(a | b, "<- nested dict replaced, not merged")


def example_08_deep_merge_helper():
    def deep_merge(a, b):
        out = dict(a)
        for k, v in b.items():
            out[k] = deep_merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
        return out
    print(deep_merge({"db": {"host": "x", "port": 1}}, {"db": {"port": 2}}))


def example_09_works_with_other_mappings():
    dd = defaultdict(int, {"x": 1})
    print(dd | {"y": 2}, Counter(a=1) | Counter(a=3, b=1))


def example_10_headers():
    base_headers = {"Accept": "application/json", "User-Agent": "demo/1.0"}
    def request_headers(token):
        return base_headers | {"Authorization": f"Bearer {token}"}
    print(request_headers("abc123"))
    print(dict(ChainMap({"k": "override"}, {"k": "base"})), "(ChainMap: a lazy alternative)")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
