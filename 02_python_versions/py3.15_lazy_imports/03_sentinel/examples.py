"""sentinel — Python 3.15+ (PEP 661)."""
import copy
import pickle

MIN_VERSION = (3, 15)
MISSING = sentinel("MISSING")
NOT_FOUND = sentinel("NOT_FOUND")


def example_01_readable_repr():
    print(MISSING, repr(MISSING), "vs old style:", object())


def example_02_none_is_a_valid_value():
    def update(record: dict, *, email: str | None | MISSING = MISSING) -> dict:
        if email is not MISSING:          # None means "clear the email"
            record["email"] = email
        return record
    print(update({"email": "a@x.io"}), update({"email": "a@x.io"}, email=None))


def example_03_cache_lookup_miss():
    cache = {"a": None}
    def lookup(key):
        return cache.get(key, NOT_FOUND)
    print(lookup("a"), lookup("b"), lookup("b") is NOT_FOUND)


def example_04_identity_survives_copy():
    print(copy.copy(MISSING) is MISSING, copy.deepcopy([MISSING])[0] is MISSING)


def example_05_identity_survives_pickle():
    print(pickle.loads(pickle.dumps(MISSING)) is MISSING)


def example_06_custom_repr():
    UNSET = sentinel("UNSET", repr="<unset>")
    print(UNSET)


def example_07_in_type_hints():
    def get(key: str, default: int | MISSING = MISSING) -> int:
        if key == "x":
            return 1
        if default is MISSING:
            raise KeyError(key)
        return default
    print(get("x"), get("y", 0), get.__annotations__["default"])


def example_08_distinct_sentinels():
    A, B = sentinel("A"), sentinel("A")
    print(A is B, "-> each call creates a unique object")


def example_09_end_of_stream_marker():
    import queue
    DONE = sentinel("DONE")
    q = queue.Queue()
    for item in [1, None, 2, DONE]:
        q.put(item)
    while (item := q.get()) is not DONE:
        print("got", item)


def example_10_use_is_not_equality():
    print(MISSING is MISSING, isinstance(MISSING, sentinel), bool(MISSING))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
