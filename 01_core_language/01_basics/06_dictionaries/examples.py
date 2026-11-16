"""Dictionaries — modern style."""
MIN_VERSION = (3, 9)


def example_01_create_and_access():
    user = {"name": "ann", "age": 31}
    user["email"] = "ann@x.io"
    print(user["name"], user.get("phone", "n/a"), len(user))


def example_02_iterate():
    prices = {"apple": 0.5, "pear": 0.75}
    for item, price in prices.items():
        print(f"{item}: ${price:.2f}")


def example_03_comprehension():
    words = ["python", "is", "great"]
    print({w: len(w) for w in words})


def example_04_invert_mapping():
    codes = {"IN": "India", "US": "USA"}
    print({v: k for k, v in codes.items()})


def example_05_merge():
    defaults, overrides = {"debug": False, "port": 80}, {"port": 8080}
    print(defaults | overrides)


def example_06_setdefault_grouping():
    groups: dict[str, list[str]] = {}
    for name in ["ann", "bob", "amy", "ben"]:
        groups.setdefault(name[0], []).append(name)
    print(groups)


def example_07_pop_and_del():
    d = {"a": 1, "b": 2, "c": 3}
    print(d.pop("a"), d.pop("zzz", "default"))
    del d["b"]
    print(d)


def example_08_nested_dicts():
    config = {"db": {"host": "localhost", "port": 5432}}
    print(config["db"]["port"], config.get("cache", {}).get("ttl", 60))


def example_09_keys_views_are_set_like():
    a, b = {"x": 1, "y": 2}, {"y": 3, "z": 4}
    print(a.keys() & b.keys(), a.keys() | b.keys())


def example_10_dict_from_pairs_and_zip():
    keys, values = ["id", "name"], [7, "bob"]
    print(dict(zip(keys, values)), dict.fromkeys(["a", "b"], 0))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
