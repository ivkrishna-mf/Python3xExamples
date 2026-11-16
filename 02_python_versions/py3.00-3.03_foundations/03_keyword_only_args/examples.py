"""Keyword-only arguments — Python 3.0+ (PEP 3102)."""
MIN_VERSION = (3, 0)


def example_01_bare_star():
    def connect(host, *, timeout=5):
        return f"{host} (timeout={timeout})"
    print(connect("db", timeout=10))
    try:
        connect("db", 10)
    except TypeError as exc:
        print("TypeError:", exc)


def example_02_after_varargs():
    def total(*nums, round_to=2):
        return round(sum(nums), round_to)
    print(total(1.111, 2.222, round_to=1))


def example_03_required_keyword_only():
    def transfer(*, source, target, amount):
        return f"{amount} from {source} to {target}"
    print(transfer(source="A", target="B", amount=100))


def example_04_boolean_flags_read_clearly():
    def export(rows, *, include_header=True, compress=False):
        return f"{len(rows)} rows, header={include_header}, gz={compress}"
    print(export([1, 2, 3], compress=True))


def example_05_with_kwargs():
    def make_tag(name, *, cls=None, **attrs):
        parts = [name] + ([f'class="{cls}"'] if cls else [])
        parts += [f'{k}="{v}"' for k, v in attrs.items()]
        return "<" + " ".join(parts) + ">"
    print(make_tag("a", cls="btn", href="/home"))


def example_06_methods():
    class Report:
        def render(self, *, fmt="text"):
            return f"report as {fmt}"
    print(Report().render(fmt="html"))


def example_07_inspect_signature():
    import inspect
    def f(a, *, b, c=1): ...
    for p in inspect.signature(f).parameters.values():
        print(p.name, p.kind.name)


def example_08_defaults_dict():
    def f(*, retries=3, backoff=0.5): ...
    print(f.__kwdefaults__)


def example_09_safe_api_evolution():
    # v2 adds 'encoding' without breaking anyone who called read(path)
    def read(path, *, encoding="utf-8", strict=True):
        return path, encoding, strict
    print(read("a.txt"), read("a.txt", strict=False))


def example_10_unpacking_a_config():
    def build(*, name, debug=False, workers=1):
        return name, debug, workers
    cfg = {"name": "api", "workers": 4}
    print(build(**cfg))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
