"""Python 3.14 stdlib highlights."""
import heapq
import operator
import tempfile
import time
import uuid
from pathlib import Path

MIN_VERSION = (3, 14)
TMP = Path(tempfile.mkdtemp())


def example_01_path_copy():
    src = TMP / "report.txt"; src.write_text("Q4 numbers", encoding="utf-8")
    (TMP / "backup").mkdir(exist_ok=True)
    dst = src.copy(TMP / "backup" / "report-copy.txt")
    print(dst.relative_to(TMP), dst.read_text(encoding="utf-8"))


def example_02_copy_directory_tree():
    (TMP / "proj" / "src").mkdir(parents=True)
    (TMP / "proj" / "src" / "main.py").write_text("print(1)", encoding="utf-8")
    (TMP / "proj").copy(TMP / "proj_v2")
    print(sorted(str(p.relative_to(TMP)) for p in (TMP / "proj_v2").rglob("*")))


def example_03_copy_into_and_move_into():
    f = TMP / "data.csv"; f.write_text("a,b", encoding="utf-8")
    inbox = TMP / "inbox"; inbox.mkdir()
    archive = TMP / "archive"; archive.mkdir()
    copied = f.copy_into(inbox)
    moved = copied.move_into(archive)
    print(copied.exists(), moved.relative_to(TMP))


def example_04_path_move_rename():
    f = TMP / "old.log"; f.touch()
    print(f.move(TMP / "new.log").name, f.exists())


def example_05_path_info():
    p = TMP / "report.txt"
    print(p.info.exists(), p.info.is_file(), p.info.is_dir())


def example_06_uuid7_is_time_ordered():
    ids = []
    for _ in range(3):
        ids.append(uuid.uuid7()); time.sleep(0.002)
    print(ids[0].version, ids == sorted(ids))


def example_07_heapq_max_heap():
    jobs = [3, 9, 1, 7]
    heapq.heapify_max(jobs)
    heapq.heappush_max(jobs, 8)
    print([heapq.heappop_max(jobs) for _ in range(3)])


def example_08_operator_is_none():
    values = [1, None, 3, None]
    print(list(filter(operator.is_not_none, values)), sum(map(operator.is_none, values)))


def example_09_map_strict():
    try:
        list(map(operator.add, [1, 2], [10], strict=True))
    except ValueError as exc:
        print("ValueError:", exc)


def example_10_from_number():
    from fractions import Fraction
    print(float.from_number(Fraction(1, 4)), int.from_number(7.0) if hasattr(int, "from_number") else "n/a")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
