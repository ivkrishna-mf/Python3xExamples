"""SyntaxWarning for control flow in finally — Python 3.14+ (PEP 765). Code compiled from strings."""
import warnings

MIN_VERSION = (3, 14)


def compile_and_warn(src):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        code = compile(src, "<demo>", "exec")
    return code, [f"{x.category.__name__}: {x.message}" for x in w]


def example_01_return_in_finally_warns():
    _, w = compile_and_warn("def f():\n    try:\n        1/0\n    finally:\n        return 'swallowed'")
    print(w)


def example_02_the_exception_is_lost():
    code, _ = compile_and_warn("def f():\n    try:\n        1/0\n    finally:\n        return 'swallowed'")
    ns = {}; exec(code, ns)
    print("f() returned", ns["f"](), "-> ZeroDivisionError vanished!")


def example_03_break_in_finally_warns():
    src = "for i in range(3):\n    try:\n        raise ValueError\n    finally:\n        break"
    print(compile_and_warn(src)[1])


def example_04_continue_in_finally_warns():
    src = "for i in range(3):\n    try:\n        pass\n    finally:\n        continue"
    print(compile_and_warn(src)[1])


def example_05_correct_pattern_return_after_try():
    def f():
        try:
            result = "computed"
        finally:
            print("  cleanup runs")
        return result
    print(f())


def example_06_loop_inside_finally_is_fine():
    src = "try:\n    pass\nfinally:\n    for i in range(2):\n        break"
    print("warnings:", compile_and_warn(src)[1], "(break targets the inner loop)")


def example_07_nested_function_in_finally_is_fine():
    src = "try:\n    pass\nfinally:\n    def g():\n        return 1"
    print("warnings:", compile_and_warn(src)[1])


def example_08_turn_into_error():
    with warnings.catch_warnings():
        warnings.simplefilter("error", SyntaxWarning)
        try:
            compile("def f():\n    try: pass\n    finally: return 1", "<demo>", "exec")
        except SyntaxError as exc:
            print("as error:", type(exc).__name__, exc.msg)


def example_09_cleanup_that_should_not_mask():
    def f():
        try:
            raise RuntimeError("real problem")
        finally:
            print("  closing resources (no return here)")
    try:
        f()
    except RuntimeError as exc:
        print("exception preserved:", exc)


def example_10_lint_your_project():
    print("Find offenders:  python -W error::SyntaxWarning -m compileall -q your_package/")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
