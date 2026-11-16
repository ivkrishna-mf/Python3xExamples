"""Comprehensions — modern style."""
MIN_VERSION = (3, 8)


def example_01_list_comprehension():
    print([n * n for n in range(6)])


def example_02_with_filter():
    print([n for n in range(20) if n % 3 == 0])


def example_03_conditional_expression_inside():
    print(["even" if n % 2 == 0 else "odd" for n in range(4)])


def example_04_dict_comprehension():
    prices = {"pen": 1.5, "book": 12.0, "bag": 30.0}
    print({k: round(v * 0.9, 2) for k, v in prices.items() if v > 5})


def example_05_set_comprehension():
    print({w[0].upper() for w in ["apple", "avocado", "banana"]})


def example_06_nested_flatten():
    matrix = [[1, 2], [3, 4], [5]]
    print([x for row in matrix for x in row])


def example_07_matrix_transpose():
    m = [[1, 2, 3], [4, 5, 6]]
    print([[row[i] for row in m] for i in range(3)])


def example_08_generator_expression_is_lazy():
    total = sum(n * n for n in range(1_000_000))
    gen = (n for n in range(3))
    print(total, type(gen).__name__, next(gen))


def example_09_walrus_in_comprehension():
    import math
    print([r for x in range(1, 30) if (r := math.isqrt(x)) ** 2 == x])


def example_10_parse_records():
    lines = ["ann,31", "bob,25", "bad", "cy,40"]
    print({name: int(age) for line in lines if line.count(",") == 1 for name, age in [line.split(",")]})


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
