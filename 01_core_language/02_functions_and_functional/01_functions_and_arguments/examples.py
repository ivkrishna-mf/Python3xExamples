"""Functions & arguments — modern style."""
import inspect

MIN_VERSION = (3, 10)


def example_01_basic_function_with_hints():
    def area(width: float, height: float) -> float:
        """Return the area of a rectangle."""
        return width * height
    print(area(3, 4), area.__doc__)


def example_02_defaults_and_keywords():
    def greet(name: str, greeting: str = "Hello") -> str:
        return f"{greeting}, {name}!"
    print(greet("Ada"), greet("Ada", greeting="Hi"), greet(greeting="Hey", name="Bob"))


def example_03_args_and_kwargs():
    def log(level: str, *messages: str, **context: object) -> str:
        return f"[{level}] {' '.join(messages)} {context}"
    print(log("INFO", "user", "logged in", user_id=7, ip="10.0.0.1"))


def example_04_keyword_only_and_positional_only():
    def fetch(url: str, /, *, timeout: float = 5, retries: int = 0) -> str:
        return f"GET {url} t={timeout} r={retries}"
    print(fetch("/api", retries=2))


def example_05_mutable_default_pitfall():
    def bad(item, bucket=[]):
        bucket.append(item); return bucket
    def good(item, bucket: list | None = None):
        bucket = [] if bucket is None else bucket
        bucket.append(item); return bucket
    print(bad(1), bad(2), "|", good(1), good(2))


def example_06_unpacking_arguments():
    def point(x: int, y: int, z: int = 0) -> tuple[int, int, int]:
        return x, y, z
    coords, opts = [1, 2], {"z": 3}
    print(point(*coords, **opts))


def example_07_multiple_return_values():
    def stats(nums: list[float]) -> tuple[float, float, float]:
        return min(nums), max(nums), sum(nums) / len(nums)
    lo, hi, avg = stats([3, 9, 6])
    print(lo, hi, avg)


def example_08_functions_are_objects():
    def shout(s: str) -> str: return s.upper()
    def whisper(s: str) -> str: return s.lower()
    for fn in (shout, whisper):
        print(fn.__name__, fn("Hello"))


def example_09_recursion():
    def flatten(data: list) -> list:
        return [y for x in data for y in (flatten(x) if isinstance(x, list) else [x])]
    print(flatten([1, [2, [3, [4]]], 5]))


def example_10_introspection():
    def f(a: int, /, b: str = "x", *args, c: bool, **kw) -> None: ...
    sig = inspect.signature(f)
    print(sig, [p.kind.name for p in sig.parameters.values()])


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
