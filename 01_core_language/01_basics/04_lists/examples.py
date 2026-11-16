"""Lists — modern style."""
from operator import itemgetter

MIN_VERSION = (3, 8)


def example_01_create_and_access():
    nums = [10, 20, 30, 40]
    print(nums[0], nums[-1], nums[1:3], len(nums))


def example_02_add_items():
    items = ["a"]
    items.append("b")
    items.extend(["c", "d"])
    items.insert(0, "start")
    items += ["e"]
    print(items)


def example_03_remove_items():
    items = ["a", "b", "c", "b", "d"]
    items.remove("b")
    last = items.pop()
    first = items.pop(0)
    del items[0]
    print(items, last, first)


def example_04_sort_and_sorted():
    nums = [5, 2, 9, 1]
    print(sorted(nums), sorted(nums, reverse=True), nums)
    nums.sort()
    print(nums)


def example_05_sort_by_key():
    users = [{"name": "bob", "age": 25}, {"name": "ann", "age": 31}, {"name": "cy", "age": 19}]
    print([u["name"] for u in sorted(users, key=itemgetter("age"))])
    print(sorted(["banana", "Apple", "cherry"], key=str.lower))


def example_06_slicing_assignment():
    nums = list(range(10))
    nums[2:5] = ["x"]
    print(nums, nums[::3])


def example_07_search():
    nums = [3, 7, 7, 1]
    print(7 in nums, nums.index(7), nums.count(7), max(nums), min(nums), sum(nums))


def example_08_stack():
    stack: list[str] = []
    for page in ("home", "about", "contact"):
        stack.append(page)
    print("back to:", stack.pop(), "->", stack[-1])


def example_09_copy_pitfalls():
    grid_bad = [[0] * 3] * 2
    grid_bad[0][0] = 1
    grid_ok = [[0] * 3 for _ in range(2)]
    grid_ok[0][0] = 1
    print(grid_bad, grid_ok)


def example_10_enumerate_and_zip():
    names, scores = ["ann", "bob"], [90, 82]
    for i, (n, s) in enumerate(zip(names, scores, strict=True), start=1):
        print(i, n, s)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
