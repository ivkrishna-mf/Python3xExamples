"""yield from — Python 3.3+ (PEP 380)."""
MIN_VERSION = (3, 3)


def example_01_delegate_to_iterable():
    def gen():
        yield from [1, 2]
        yield from "ab"
    print(list(gen()))


def example_02_flatten_nested():
    def flatten(items):
        for x in items:
            if isinstance(x, list):
                yield from flatten(x)
            else:
                yield x
    print(list(flatten([1, [2, [3, [4]]], 5])))


def example_03_tree_walk():
    tree = {"name": "root", "kids": [{"name": "a", "kids": []},
                                     {"name": "b", "kids": [{"name": "c", "kids": []}]}]}
    def walk(node, depth=0):
        yield "  " * depth + node["name"]
        for k in node["kids"]:
            yield from walk(k, depth + 1)
    print("\n".join(walk(tree)))


def example_04_capture_return_value():
    def sub():
        yield 1
        yield 2
        return "sub done"
    def main():
        result = yield from sub()
        yield result
    print(list(main()))


def example_05_send_is_forwarded():
    def accumulator():
        total = 0
        while True:
            x = yield total
            if x is None:
                return total
            total += x
    def wrapper():
        final = yield from accumulator()
        print("final total:", final)
    g = wrapper()
    next(g)
    for n in (5, 10):
        print("running:", g.send(n))
    try:
        g.send(None)
    except StopIteration:
        pass


def example_06_chain_pipelines():
    def numbers(): yield from range(3)
    def letters(): yield from "xy"
    def both():
        yield from numbers()
        yield from letters()
    print(list(both()))


def example_07_read_many_sources():
    sources = {"a.txt": ["l1", "l2"], "b.txt": ["l3"]}
    def lines():
        for name, content in sources.items():
            yield from (f"{name}: {line}" for line in content)
    print(list(lines()))


def example_08_permutations_recursive():
    def perms(seq):
        if len(seq) <= 1:
            yield seq
            return
        for i, x in enumerate(seq):
            for p in perms(seq[:i] + seq[i + 1:]):
                yield [x] + p
    print(list(perms([1, 2, 3])))


def example_09_throw_is_forwarded():
    def inner():
        try:
            yield 1
        except ValueError:
            yield "inner handled ValueError"
    def outer():
        yield from inner()
    g = outer()
    next(g)
    print(g.throw(ValueError))


def example_10_compare_with_manual_loop():
    def manual(it):
        for x in it:
            yield x
    def delegated(it):
        yield from it
    print(list(manual("abc")) == list(delegated("abc")))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
