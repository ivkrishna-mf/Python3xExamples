"""pathlib — Python 3.4+ (PEP 428)."""
import tempfile
from pathlib import Path

MIN_VERSION = (3, 4)
BASE = Path(tempfile.mkdtemp(prefix="pathlib_demo_"))


def example_01_join_with_slash():
    p = BASE / "reports" / "2026" / "nov.csv"
    print(p.relative_to(BASE))


def example_02_parts_of_a_path():
    p = Path("/srv/app/logs/server.log.gz")
    print(p.name, p.stem, p.suffix, p.suffixes, p.parent)


def example_03_mkdir_and_write_text():
    d = BASE / "notes"
    d.mkdir(parents=True, exist_ok=True)
    (d / "todo.txt").write_text("buy milk\n", encoding="utf-8")
    print((d / "todo.txt").read_text(encoding="utf-8").strip())


def example_04_exists_is_file_is_dir():
    print(BASE.exists(), BASE.is_dir(), (BASE / "nope").is_file())


def example_05_glob_and_rglob():
    for name in ("a.py", "b.py", "sub/c.py", "readme.md"):
        f = BASE / "proj" / name
        f.parent.mkdir(parents=True, exist_ok=True)
        f.touch()
    proj = BASE / "proj"
    print(sorted(p.name for p in proj.glob("*.py")))
    print(sorted(str(p.relative_to(proj)) for p in proj.rglob("*.py")))


def example_06_change_suffix_and_name():
    p = Path("photos/beach.jpeg")
    print(p.with_suffix(".png"), p.with_name("sunset.jpeg"))


def example_07_iterdir():
    (BASE / "list").mkdir(exist_ok=True)
    for n in "xyz":
        (BASE / "list" / f"{n}.txt").touch()
    print(sorted(p.name for p in (BASE / "list").iterdir()))


def example_08_stat_and_size():
    f = BASE / "size.bin"
    f.write_bytes(b"\0" * 1024)
    print(f.stat().st_size, "bytes")


def example_09_home_cwd_resolve():
    print("home:", Path.home().name != "", "| cwd absolute:", Path.cwd().is_absolute())
    print(Path("a/b/../c").resolve().name)


def example_10_open_like_builtin():
    f = BASE / "data.csv"
    with f.open("w", encoding="utf-8") as fh:
        fh.write("id,name\n1,ann\n")
    with f.open(encoding="utf-8") as fh:
        print([line.strip() for line in fh])


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
