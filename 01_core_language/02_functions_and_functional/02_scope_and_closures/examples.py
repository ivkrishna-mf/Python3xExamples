"""Scope & closures — modern style."""
MIN_VERSION = (3, 8)
counter = 0


def example_01_legb_lookup():
    x = "local"
    def inner():
        return x            # found in Enclosing scope
    print(inner(), len("builtin len"))


def example_02_local_shadows_global():
    counter = 99            # new local, global untouched
    print(counter, globals()["counter"])


def example_03_global_keyword():
    def bump():
        global counter
        counter += 1
    bump(); bump()
    print("global counter:", counter)


def example_04_function_factory():
    def make_multiplier(n: int):
        def multiply(x: int) -> int:
            return x * n
        return multiply
    double, triple = make_multiplier(2), make_multiplier(3)
    print(double(5), triple(5))


def example_05_closure_cells():
    def outer():
        secret = "s3"
        return lambda: secret
    f = outer()
    print(f.__closure__[0].cell_contents)


def example_06_nonlocal_counter():
    def make_counter():
        count = 0
        def inc() -> int:
            nonlocal count
            count += 1
            return count
        return inc
    c = make_counter()
    print(c(), c(), c())


def example_07_late_binding_gotcha():
    funcs_bad = [lambda: i for i in range(3)]
    funcs_ok = [lambda i=i: i for i in range(3)]
    print([f() for f in funcs_bad], [f() for f in funcs_ok])


def example_08_configured_validator():
    def length_between(lo: int, hi: int):
        def check(s: str) -> bool:
            return lo <= len(s) <= hi
        return check
    username_ok = length_between(3, 12)
    print(username_ok("ab"), username_ok("ada_l"))


def example_09_unboundlocal_error():
    total = 10
    def broken():
        try:
            total += 1      # assignment makes 'total' local
        except UnboundLocalError as exc:
            return str(exc)
    print(broken())


def example_10_class_scope_is_not_enclosing():
    class C:
        x = 10
        def method(self):
            return C.x          # must qualify; class body isn't an enclosing scope for methods
    print(C().method())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
