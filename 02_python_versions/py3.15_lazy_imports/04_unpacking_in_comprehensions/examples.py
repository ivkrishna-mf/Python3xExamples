"""Unpacking in comprehensions — Python 3.15+ (PEP 798)."""
import asyncio
from itertools import chain

MIN_VERSION = (3, 15)
lists = [[1, 2], [3, 4], [5]]


def example_01_flatten_list():
    print([*L for L in lists])


def example_02_equivalent_old_spellings():
    print([*L for L in lists] == [x for L in lists for x in L] == list(chain.from_iterable(lists)))


def example_03_set_union():
    print({*s for s in [{1, 2}, {2, 3}, {3, 4}]})


def example_04_merge_dicts_later_wins():
    print({**d for d in [{"a": 1}, {"b": 2}, {"a": 3}]})


def example_05_generator_expression():
    gen = (*L for L in lists)
    print(type(gen).__name__, list(gen))


def example_06_with_filter():
    groups = {"admins": ["ann"], "guests": ["x", "y"], "devs": ["bob", "cy"]}
    print([*members for name, members in groups.items() if name != "guests"])


def example_07_layered_config():
    layers = [{"debug": False, "port": 80}, {"port": 8080}, {"debug": True}]
    print({**layer for layer in layers})


def example_08_flatten_rows_of_csv():
    rows = ["a,b", "c", "d,e,f"]
    print([*r.split(",") for r in rows])


def example_09_dict_from_list_of_mappings():
    users = [{"id": 1, "name": "ann"}, {"id": 2, "name": "bob"}]
    print({**{u["id"]: u["name"]} for u in users})


def example_10_async_comprehension():
    async def pages():
        for p in ([1, 2], [3], [4, 5]):
            await asyncio.sleep(0)
            yield p
    async def main():
        print([*p async for p in pages()])
    asyncio.run(main())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
