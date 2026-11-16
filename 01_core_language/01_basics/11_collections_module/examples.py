"""collections — modern style."""
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque

MIN_VERSION = (3, 8)
TEXT = "the quick brown fox jumps over the lazy dog the end"


def example_01_counter_words():
    print(Counter(TEXT.split()).most_common(2))


def example_02_counter_arithmetic():
    a, b = Counter(apples=3, pears=1), Counter(apples=1, kiwis=2)
    print(a + b, a - b, a & b)


def example_03_defaultdict_grouping():
    groups = defaultdict(list)
    for word in TEXT.split():
        groups[len(word)].append(word)
    print(dict(groups))


def example_04_defaultdict_nested_counts():
    sales = defaultdict(lambda: defaultdict(int))
    for region, product, qty in [("EU", "pen", 3), ("EU", "ink", 1), ("US", "pen", 2), ("EU", "pen", 1)]:
        sales[region][product] += qty
    print({r: dict(p) for r, p in sales.items()})


def example_05_deque_queue():
    q = deque(["a", "b"])
    q.append("c"); q.appendleft("start")
    print(q.popleft(), q.pop(), q)


def example_06_deque_sliding_window():
    window = deque(maxlen=3)
    for value in [1, 5, 2, 8, 3]:
        window.append(value)
        print(list(window), "avg", round(sum(window) / len(window), 2))


def example_07_deque_rotate():
    d = deque(range(5))
    d.rotate(2)
    print(d)


def example_08_chainmap_layered_config():
    defaults = {"color": "red", "user": "guest"}
    env = {"user": "admin"}
    cli = {"color": "blue"}
    cfg = ChainMap(cli, env, defaults)
    print(cfg["color"], cfg["user"], dict(cfg))


def example_09_ordereddict_lru():
    cache = OrderedDict()
    for key in ["a", "b", "a", "c", "d"]:
        cache[key] = True
        cache.move_to_end(key)
        if len(cache) > 3:
            cache.popitem(last=False)
    print(list(cache))


def example_10_counter_from_letters_total():
    c = Counter("mississippi")
    print(c, c.total() if hasattr(c, "total") else sum(c.values()))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
