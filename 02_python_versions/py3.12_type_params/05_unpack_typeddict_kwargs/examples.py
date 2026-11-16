"""Unpack[TypedDict] for **kwargs — Python 3.12+ (PEP 692)."""
from typing import NotRequired, Required, TypedDict, Unpack

MIN_VERSION = (3, 12)


class RequestOptions(TypedDict, total=False):
    timeout: float
    retries: int
    headers: dict[str, str]
    verify: bool


def request(url: str, **opts: Unpack[RequestOptions]) -> str:
    timeout = opts.get("timeout", 5.0)
    retries = opts.get("retries", 0)
    return f"GET {url} timeout={timeout} retries={retries} headers={opts.get('headers', {})}"


def example_01_basic_call():
    print(request("/users", timeout=2.5, retries=3))


def example_02_no_options():
    print(request("/health"))


def example_03_forwarding_wrapper():
    def get_json(url: str, **opts: Unpack[RequestOptions]) -> str:
        opts.setdefault("headers", {"Accept": "application/json"})
        return request(url, **opts)
    print(get_json("/orders", retries=1))


def example_04_pass_a_dict():
    opts: RequestOptions = {"timeout": 1.0, "verify": False}
    print(request("/x", **opts))


def example_05_required_keys():
    class PlotKw(TypedDict):
        title: Required[str]
        color: NotRequired[str]
    def plot(data: list[float], **kw: Unpack[PlotKw]) -> str:
        return f"{kw['title']} ({kw.get('color', 'blue')}): {data}"
    print(plot([1, 2, 3], title="Sales"))


def example_06_kwargs_is_a_dict():
    def show(**kw: Unpack[RequestOptions]) -> None:
        print(type(kw).__name__, kw)
    show(timeout=3)


def example_07_annotation_introspection():
    print(request.__annotations__["opts"])


def example_08_shared_options_across_functions():
    class DbOpts(TypedDict, total=False):
        pool_size: int
        echo: bool
    def connect(dsn: str, **o: Unpack[DbOpts]) -> str:
        return f"{dsn} pool={o.get('pool_size', 5)}"
    def migrate(dsn: str, **o: Unpack[DbOpts]) -> str:
        return "migrating via " + connect(dsn, **o)
    print(migrate("postgres://", pool_size=2))


def example_09_combined_with_positional():
    class FmtOpts(TypedDict, total=False):
        sep: str
        upper: bool
    def fmt(*words: str, **o: Unpack[FmtOpts]) -> str:
        s = o.get("sep", " ").join(words)
        return s.upper() if o.get("upper") else s
    print(fmt("a", "b", "c", sep="-", upper=True))


def example_10_unknown_keys_still_work_at_runtime():
    # A type checker rejects request("/x", tiemout=1); Python itself does not.
    print(request("/x", **{"tiemout": 1}))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
