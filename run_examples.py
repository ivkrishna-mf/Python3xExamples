"""Run every examples.py under this folder (or a sub-path) with the current interpreter.

Each examples.py declares MIN_VERSION = (3, X). Files that need a newer Python are skipped,
so you can run the whole tree on any version and see what your interpreter supports.

Usage:
    python run_examples.py                         # everything
    python run_examples.py 01_core_language        # one section
    python run_examples.py 02_python_versions/py3.12_type_params
    python run_examples.py -v 02_python_versions/py3.10_pattern_matching   # show output
"""
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def min_version(path: Path) -> tuple[int, int]:
    m = re.search(r"^MIN_VERSION\s*=\s*\((\d+),\s*(\d+)\)", path.read_text(encoding="utf-8"), re.M)
    return (int(m.group(1)), int(m.group(2))) if m else (3, 0)


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    verbose = "-v" in sys.argv
    base = ROOT / args[0] if args else ROOT
    files = sorted(base.rglob("examples.py"))
    here = sys.version_info[:2]
    passed = failed = skipped = 0
    print(f"Python {sys.version.split()[0]} — {len(files)} example files under {base.relative_to(ROOT.parent)}\n")
    for f in files:
        rel = f.parent.relative_to(ROOT)
        need = min_version(f)
        if here < need:
            skipped += 1
            print(f"SKIP  {rel}  (needs {need[0]}.{need[1]}+)")
            continue
        t = time.perf_counter()
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        r = subprocess.run([sys.executable, str(f)], cwd=f.parent, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=300, env=env)
        dt = time.perf_counter() - t
        if r.returncode == 0:
            passed += 1
            print(f"PASS  {rel}  ({dt:.1f}s)")
            if verbose:
                print(r.stdout)
        else:
            failed += 1
            print(f"FAIL  {rel}\n{r.stderr[-1500:]}")
    print(f"\n{passed} passed, {failed} failed, {skipped} skipped (need newer Python)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
