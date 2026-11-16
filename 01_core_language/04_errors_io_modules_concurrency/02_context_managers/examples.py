"""Context managers — modern style (3.11+ for contextlib.chdir)."""
import contextlib
import io
import os
import sqlite3
import tempfile
import threading
import time
from pathlib import Path

MIN_VERSION = (3, 11)
TMP = Path(tempfile.mkdtemp())


def example_01_file_closes_automatically():
    path = TMP / "a.txt"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("hello")
    print(fh.closed, path.read_text(encoding="utf-8"))


def example_02_class_based_manager():
    class Timer:
        def __enter__(self):
            self.start = time.perf_counter()
            return self
        def __exit__(self, exc_type, exc, tb):
            self.elapsed = time.perf_counter() - self.start
            return False             # don't swallow exceptions
    with Timer() as t:
        sum(range(200_000))
    print(f"took {t.elapsed:.4f}s")


def example_03_generator_based_manager():
    @contextlib.contextmanager
    def tag(name: str):
        print(f"<{name}>")
        try:
            yield
        finally:
            print(f"</{name}>")
    with tag("div"):
        print("  content")


def example_04_suppress():
    with contextlib.suppress(FileNotFoundError):
        os.remove(TMP / "does-not-exist")
    print("no error raised")


def example_05_lock():
    lock = threading.Lock()
    with lock:
        print("locked:", lock.locked())
    print("locked:", lock.locked())


def example_06_db_transaction():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE t (x INTEGER)")
    try:
        with conn:                        # commits on success, rolls back on error
            conn.execute("INSERT INTO t VALUES (1)")
            raise RuntimeError("abort!")
    except RuntimeError:
        pass
    print("rows after rollback:", conn.execute("SELECT COUNT(*) FROM t").fetchone()[0])


def example_07_multiple_managers_parenthesised():
    (TMP / "src.txt").write_text("data", encoding="utf-8")
    with (
        open(TMP / "src.txt", encoding="utf-8") as src,
        open(TMP / "dst.txt", "w", encoding="utf-8") as dst,
    ):
        dst.write(src.read().upper())
    print((TMP / "dst.txt").read_text(encoding="utf-8"))


def example_08_exitstack_dynamic():
    names = ["x.log", "y.log"]
    with contextlib.ExitStack() as stack:
        files = [stack.enter_context(open(TMP / n, "w", encoding="utf-8")) for n in names]
        stack.callback(print, "  all files closed")
        for f in files:
            f.write("ok")


def example_09_redirect_stdout_and_chdir():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        print("captured")
    with contextlib.chdir(TMP):
        here = Path.cwd().name
    print(repr(buf.getvalue()), here == TMP.name)


def example_10_temporary_setting():
    @contextlib.contextmanager
    def env(**vars: str):
        old = {k: os.environ.get(k) for k in vars}
        os.environ.update(vars)
        try:
            yield
        finally:
            for k, v in old.items():
                if v is None:
                    os.environ.pop(k, None)
                else:
                    os.environ[k] = v
    with env(APP_MODE="test"):
        print("inside:", os.environ["APP_MODE"])
    print("after:", os.environ.get("APP_MODE"))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
