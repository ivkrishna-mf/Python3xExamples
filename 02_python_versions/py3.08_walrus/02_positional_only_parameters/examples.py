"""Positional-only parameters — Python 3.8+ (PEP 570)."""
import inspect

MIN_VERSION = (3, 8)


def example_01_basic():
    def area(w, h, /):
        return w * h
    print(area(3, 4))
    try:
        area(w=3, h=4)
    except TypeError as exc:
        print("TypeError:", exc)


def example_02_all_three_kinds():
    def f(pos, /, either, *, kw):
        return pos, either, kw
    print(f(1, 2, kw=3), f(1, either=2, kw=3))


def example_03_safe_renaming():
    # Callers can never depend on the names 'a'/'b', so renaming them later is safe.
    def clamp(a, b, c, /):
        return max(b, min(a, c))
    print(clamp(15, 0, 10))


def example_04_kwargs_can_reuse_name():
    def format_record(name, /, **fields):
        return name, fields
    print(format_record("user", name="ann", age=30))   # 'name' goes into **fields


def example_05_mirrors_builtins():
    print(inspect.signature(len), inspect.signature(divmod))


def example_06_with_defaults():
    def greet(name, greeting="hello", /):
        return f"{greeting}, {name}"
    print(greet("ann"), greet("bob", "hey"))


def example_07_inspect_kinds():
    def f(a, /, b, *, c): ...
    print({n: p.kind.name for n, p in inspect.signature(f).parameters.items()})


def example_08_dunder_like_signature():
    class Vec:
        def __init__(self, x, y, /):
            self.x, self.y = x, y
        def dot(self, other, /):
            return self.x * other.x + self.y * other.y
    print(Vec(1, 2).dot(Vec(3, 4)))


def example_09_wrapper_passes_everything():
    def logged(fn):
        def wrapper(*args, **kwargs):
            print("calling", fn.__name__, args, kwargs)
            return fn(*args, **kwargs)
        return wrapper
    @logged
    def power(base, exp, /): return base ** exp
    print(power(2, 10))


def example_10_dict_like_get():
    def get(mapping, key, default=None, /):
        return mapping.get(key, default)
    print(get({"a": 1}, "b", "fallback"))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
