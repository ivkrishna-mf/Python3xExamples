"""File I/O & serialisation — modern style."""
import csv
import json
import pickle
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path

MIN_VERSION = (3, 8)
TMP = Path(tempfile.mkdtemp())


@dataclass
class User:
    id: int
    name: str
    email: str


USERS = [User(1, "ann", "ann@x.io"), User(2, "bob", "bob@x.io")]


def example_01_write_and_read_text():
    p = TMP / "notes.txt"
    p.write_text("line 1\nline 2\n", encoding="utf-8")
    print(p.read_text(encoding="utf-8").splitlines())


def example_02_stream_large_file_line_by_line():
    p = TMP / "big.log"
    p.write_text("".join(f"row {i}\n" for i in range(1000)), encoding="utf-8")
    with p.open(encoding="utf-8") as fh:
        count = sum(1 for line in fh if line.strip().endswith("7"))
    print("lines ending in 7:", count)


def example_03_append_mode():
    p = TMP / "audit.log"
    for event in ("login", "logout"):
        with p.open("a", encoding="utf-8") as fh:
            print(event, file=fh)
    print(p.read_text(encoding="utf-8").split())


def example_04_binary_files():
    p = TMP / "data.bin"
    p.write_bytes(bytes(range(8)))
    print(list(p.read_bytes()))


def example_05_json_dump_and_load():
    p = TMP / "users.json"
    p.write_text(json.dumps([asdict(u) for u in USERS], indent=2), encoding="utf-8")
    loaded = [User(**d) for d in json.loads(p.read_text(encoding="utf-8"))]
    print(loaded[0])


def example_06_json_custom_types():
    from datetime import datetime
    def default(o):
        if isinstance(o, datetime):
            return o.isoformat()
        raise TypeError(f"not serialisable: {type(o).__name__}")
    print(json.dumps({"at": datetime(2026, 11, 16, 9, 0)}, default=default))


def example_07_csv_dictwriter_dictreader():
    p = TMP / "users.csv"
    with p.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "name", "email"])
        w.writeheader()
        w.writerows(asdict(u) for u in USERS)
    with p.open(newline="", encoding="utf-8") as fh:
        print([row["name"] for row in csv.DictReader(fh)])


def example_08_csv_with_quotes():
    p = TMP / "tricky.csv"
    with p.open("w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerow(["Smith, John", 'He said "hi"', 3])
    print(p.read_text(encoding="utf-8").strip())


def example_09_pickle_python_objects():
    p = TMP / "cache.pkl"
    p.write_bytes(pickle.dumps({"users": USERS}))
    print(pickle.loads(p.read_bytes())["users"][1], "(only unpickle trusted data!)")


def example_10_list_and_filter_files():
    for name in ("a.json", "b.csv", "c.json"):
        (TMP / "dir" / name).parent.mkdir(exist_ok=True)
        (TMP / "dir" / name).touch()
    print(sorted(p.name for p in (TMP / "dir").glob("*.json")))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
