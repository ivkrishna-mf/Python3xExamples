"""Ordered dicts — guaranteed since Python 3.7 (reversed(dict) needs 3.8)."""
import json
from collections import OrderedDict

MIN_VERSION = (3, 8)


def example_01_iteration_order():
    d = {}
    for k in ["zebra", "apple", "mango"]:
        d[k] = len(k)
    print(list(d))


def example_02_dedupe_preserving_order():
    print(list(dict.fromkeys([3, 1, 3, 2, 1])))


def example_03_first_and_last_key():
    d = {"a": 1, "b": 2, "c": 3}
    print(next(iter(d)), next(reversed(d)))       # reversed(dict) 3.8+


def example_04_update_keeps_position():
    d = {"a": 1, "b": 2}
    d["a"] = 100
    print(d)


def example_05_delete_and_reinsert_moves_to_end():
    d = {"a": 1, "b": 2, "c": 3}
    d["a"] = d.pop("a")
    print(d)


def example_06_kwargs_order_preserved():
    def show(**kw): return list(kw)
    print(show(z=1, y=2, x=3))


def example_07_json_round_trip_order():
    s = json.dumps({"id": 1, "name": "ann", "tags": []})
    print(s, list(json.loads(s)))


def example_08_equality_ignores_order():
    print({"a": 1, "b": 2} == {"b": 2, "a": 1},
          OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1))


def example_09_ordereddict_extras():
    od = OrderedDict.fromkeys("abc")
    od.move_to_end("a")
    od.popitem(last=False)
    print(list(od))


def example_10_tiny_lru_with_plain_dict():
    cache, cap = {}, 2
    def get(k):
        if k in cache:
            cache[k] = cache.pop(k)      # mark as most recent
        else:
            if len(cache) >= cap:
                del cache[next(iter(cache))]   # evict oldest
            cache[k] = k.upper()
        return cache[k]
    for k in "abac":
        get(k)
    print(cache)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
