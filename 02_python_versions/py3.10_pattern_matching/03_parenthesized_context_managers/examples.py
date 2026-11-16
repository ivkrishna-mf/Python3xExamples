"""Parenthesised context managers — Python 3.10+."""
import contextlib
import io
import tempfile
import threading
from pathlib import Path
from unittest import mock

MIN_VERSION = (3, 10)
TMP = Path(tempfile.mkdtemp())


@contextlib.contextmanager
def tag(name):
    print(f"<{name}>")
    yield name
    print(f"</{name}>")


def example_01_two_files():
    (TMP / "in.txt").write_text("hello\nworld\n", encoding="utf-8")
    with (
        open(TMP / "in.txt", encoding="utf-8") as src,
        open(TMP / "out.txt", "w", encoding="utf-8") as dst,
    ):
        dst.write(src.read().upper())
    print((TMP / "out.txt").read_text(encoding="utf-8").split())


def example_02_nesting_order():
    with (tag("html"), tag("body"), tag("p")):
        print("   content")


def example_03_without_as_names():
    lock_a, lock_b = threading.Lock(), threading.Lock()
    with (lock_a, lock_b):
        print(lock_a.locked(), lock_b.locked())


def example_04_mock_patching():
    import os
    with (
        mock.patch("os.getcwd", return_value="/fake"),
        mock.patch("os.cpu_count", return_value=64),
    ):
        print(os.getcwd(), os.cpu_count())


def example_05_redirect_output():
    out, err = io.StringIO(), io.StringIO()
    with (
        contextlib.redirect_stdout(out),
        contextlib.redirect_stderr(err),
    ):
        print("captured!")
    print("stdout had:", out.getvalue().strip())


def example_06_suppress_and_file():
    with (
        contextlib.suppress(FileNotFoundError),
        open(TMP / "missing.txt", encoding="utf-8") as fh,
    ):
        print(fh.read())
    print("missing file silently suppressed")


def example_07_exitstack_for_dynamic_count():
    names = ["a.txt", "b.txt", "c.txt"]
    with contextlib.ExitStack() as stack:
        files = [stack.enter_context(open(TMP / n, "w", encoding="utf-8")) for n in names]
        for f in files:
            f.write(f.name)
    print(sorted(p.name for p in TMP.glob("?.txt")))


def example_08_exceptions_unwind_all():
    try:
        with (tag("outer"), tag("inner")):
            raise RuntimeError("boom")
    except RuntimeError:
        print("all managers exited before the handler ran")


def example_09_tempdir_and_file():
    with (
        tempfile.TemporaryDirectory() as d,
        open(Path(d) / "x.log", "w", encoding="utf-8") as log,
    ):
        log.write("ok")
        print("writing inside", Path(d).name)


def example_10_nullcontext_optional_manager():
    def process(lock=None):
        with (lock or contextlib.nullcontext(), tag("work")):
            print("   processing")
    process()
    process(threading.Lock())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
