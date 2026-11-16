"""breakpoint() — Python 3.7+ (PEP 553). Examples swap the hook so nothing blocks."""
import os
import sys

MIN_VERSION = (3, 7)


def fake_hook(*args, **kwargs):
    frame = sys._getframe(1)
    print(f"  [breakpoint hit in {frame.f_code.co_name}() line {frame.f_lineno}] locals={list(frame.f_locals)}")


def with_hook(fn):
    old = sys.breakpointhook
    sys.breakpointhook = fake_hook
    try:
        fn()
    finally:
        sys.breakpointhook = old


def example_01_basic_call():
    def work():
        total = 10
        breakpoint()
    with_hook(work)


def example_02_conditional_breakpoint():
    def process(items):
        for i, x in enumerate(items):
            if x < 0:
                breakpoint()     # only stop on bad data
    with_hook(lambda: process([1, -2, 3]))


def example_03_default_hook_is_pdb():
    print(sys.__breakpointhook__, "-> uses PYTHONBREAKPOINT or pdb.set_trace")


def example_04_env_var_disables():
    print("current PYTHONBREAKPOINT =", os.environ.get("PYTHONBREAKPOINT", "(unset → pdb)"))


def example_05_custom_hook_for_logging():
    def log_hook(*a, **k):
        print("  breakpoint reached — logged instead of stopping")
    old = sys.breakpointhook
    sys.breakpointhook = log_hook
    breakpoint()
    sys.breakpointhook = old


def example_06_hook_receives_arguments():
    def hook(*args, **kwargs):
        print("  hook got", args, kwargs)
    old, sys.breakpointhook = sys.breakpointhook, hook
    breakpoint("why", reason="investigating")
    sys.breakpointhook = old


def example_07_breakpoint_in_exception_handler():
    def risky():
        try:
            1 / 0
        except ZeroDivisionError:
            breakpoint()   # inspect state right where it failed
    with_hook(risky)


def example_08_post_mortem_alternative():
    import pdb
    print("pdb.post_mortem(tb) inspects a finished traceback:", pdb.post_mortem.__name__)


def example_09_common_pdb_commands():
    cmds = {"n": "next line", "s": "step into", "c": "continue", "p x": "print x",
            "l": "list source", "w": "where (stack)", "q": "quit"}
    for k, v in cmds.items():
        print(f"  {k:4} {v}")


def example_10_guard_for_ci():
    def maybe_debug():
        if os.environ.get("CI"):
            return
        breakpoint()
    with_hook(maybe_debug)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
