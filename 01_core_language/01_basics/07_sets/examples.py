"""Sets — modern style."""
MIN_VERSION = (3, 8)


def example_01_create_and_dedupe():
    print({1, 2, 2, 3}, set("hello"), set(), len({1, 1, 1}))


def example_02_membership_is_fast():
    allowed = {"admin", "editor"}
    print("admin" in allowed, "guest" not in allowed)


def example_03_algebra():
    a, b = {1, 2, 3}, {3, 4}
    print(a | b, a & b, a - b, a ^ b)


def example_04_subset_superset():
    print({1, 2} <= {1, 2, 3}, {1, 2, 3} >= {2}, {1}.isdisjoint({2}))


def example_05_add_remove():
    s = {1}
    s.add(2); s.update([3, 4]); s.discard(99); s.remove(1)
    print(s, s.pop() in {2, 3, 4})


def example_06_comprehension():
    print({w.lower() for w in ["Apple", "apple", "APPLE", "Pear"]})


def example_07_frozenset_as_key():
    teams = {frozenset({"ann", "bob"}): "blue"}
    print(teams[frozenset({"bob", "ann"})])


def example_08_find_missing():
    required = {"name", "email", "age"}
    payload = {"name": "x", "age": 3}
    print("missing:", required - payload.keys())


def example_09_unique_preserving_order():
    items = ["b", "a", "b", "c", "a"]
    print(list(dict.fromkeys(items)), "(sets don't keep order)")


def example_10_common_elements_across_lists():
    lists = [[1, 2, 3, 4], [2, 3, 5], [3, 2, 9]]
    print(set.intersection(*map(set, lists)))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
