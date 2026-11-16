"""Loops — modern style."""
import itertools

MIN_VERSION = (3, 10)


def example_01_for_over_iterables():
    for ch in "abc":
        print(ch, end=" ")
    for key in {"x": 1, "y": 2}:
        print(key, end=" ")
    print()


def example_02_range():
    print(list(range(5)), list(range(2, 10, 3)), list(range(5, 0, -1)))


def example_03_enumerate():
    for i, fruit in enumerate(["apple", "kiwi"], start=1):
        print(f"{i}. {fruit}")


def example_04_zip_parallel():
    for name, score in zip(["ann", "bob"], [91, 78], strict=True):
        print(name, score)


def example_05_while_loop():
    n, steps = 27, 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    print("collatz steps:", steps)


def example_06_break_continue():
    for n in range(10):
        if n % 2:
            continue
        if n > 6:
            break
        print(n, end=" ")
    print()


def example_07_for_else_search():
    for user in ["ann", "bob"]:
        if user == "zed":
            print("found")
            break
    else:
        print("zed not found")


def example_08_dict_items_loop():
    stock = {"pen": 3, "ink": 0}
    for item, qty in stock.items():
        print(f"{item}: {'out of stock' if not qty else qty}")


def example_09_nested_loops_and_product():
    for size, color in itertools.product(["S", "M"], ["red", "blue"]):
        print(size, color, end=" | ")
    print()


def example_10_retry_with_while():
    attempts, max_attempts = 0, 3
    results = iter([False, False, True])
    while attempts < max_attempts:
        attempts += 1
        if next(results):
            print(f"succeeded on attempt {attempts}")
            break
    else:
        print("all attempts failed")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
