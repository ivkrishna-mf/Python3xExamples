"""Extended iterable unpacking — Python 3.0+ (PEP 3132)."""
MIN_VERSION = (3, 0)


def example_01_head_and_tail():
    first, *rest = [1, 2, 3, 4]
    print(first, rest)


def example_02_init_and_last():
    *init, last = "abcde"
    print(init, last)


def example_03_first_and_last_ignore_middle():
    first, *_, last = range(10)
    print(first, last)


def example_04_command_parsing():
    cmd, *args = "git commit -m msg".split()
    print(cmd, args)


def example_05_empty_star_is_empty_list():
    a, *b = [1]
    print(a, b)


def example_06_in_for_loops():
    rows = [("ann", 90, 85, 77), ("bob", 60, 70)]
    for name, *scores in rows:
        print(name, sum(scores) / len(scores))


def example_07_nested_unpacking():
    (a, *b), c = [1, 2, 3], 4
    print(a, b, c)


def example_08_swap_and_rotate():
    x, y = 1, 2
    x, y = y, x
    head, *tail = [1, 2, 3, 4]
    print(x, y, tail + [head])


def example_09_csv_like_record():
    line = "2026-11-16,ERROR,db,timeout,retrying"
    date, level, *message = line.split(",")
    print(date, level, " ".join(message))


def example_10_too_few_values_error():
    try:
        a, b, *c = [1]
    except ValueError as exc:
        print("ValueError:", exc)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
