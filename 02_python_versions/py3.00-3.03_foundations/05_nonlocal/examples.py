"""nonlocal — Python 3.0+ (PEP 3104)."""
MIN_VERSION = (3, 0)


def example_01_counter_closure():
    def make_counter():
        count = 0
        def inc():
            nonlocal count
            count += 1
            return count
        return inc
    c = make_counter()
    print(c(), c(), c())


def example_02_without_nonlocal_fails():
    def outer():
        n = 0
        def inner():
            n += 1           # UnboundLocalError
        inner()
    try:
        outer()
    except UnboundLocalError as exc:
        print("UnboundLocalError:", exc)


def example_03_running_average():
    def averager():
        total = count = 0
        def add(x):
            nonlocal total, count
            total += x; count += 1
            return total / count
        return add
    avg = averager()
    print(avg(10), avg(20), avg(30))


def example_04_call_counting_decorator():
    def counted(fn):
        calls = 0
        def wrapper(*a, **k):
            nonlocal calls
            calls += 1
            print(f"{fn.__name__} call #{calls}")
            return fn(*a, **k)
        return wrapper
    @counted
    def ping(): return "pong"
    ping(); ping()


def example_05_callback_collects_result():
    def find_first_even(nums):
        found = None
        def check(n):
            nonlocal found
            if found is None and n % 2 == 0:
                found = n
        for n in nums:
            check(n)
        return found
    print(find_first_even([3, 5, 8, 10]))


def example_06_toggle():
    def make_toggle():
        state = False
        def toggle():
            nonlocal state
            state = not state
            return state
        return toggle
    t = make_toggle()
    print(t(), t(), t())


def example_07_multiple_levels():
    def a():
        x = "a"
        def b():
            def c():
                nonlocal x
                x = "changed by c"
            c()
        b()
        return x
    print(a())


def example_08_id_generator():
    def id_gen(prefix):
        n = 0
        def next_id():
            nonlocal n
            n += 1
            return f"{prefix}-{n:04d}"
        return next_id
    gen = id_gen("ORD")
    print(gen(), gen())


def example_09_rate_limiter():
    import time
    def limiter(min_gap):
        last = 0.0
        def allowed():
            nonlocal last
            now = time.monotonic()
            if now - last >= min_gap:
                last = now
                return True
            return False
        return allowed
    ok = limiter(1.0)
    print(ok(), ok())


def example_10_mutating_needs_no_nonlocal():
    # Mutating an object is fine without nonlocal; only *rebinding* needs it.
    def collector():
        items = []
        def add(x):
            items.append(x)
            return items
        return add
    add = collector()
    add(1); print(add(2))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
