"""profiling.sampling (Tachyon) & profiling.tracing — Python 3.15+ (PEP 799)."""
import io
import os
import pstats
import subprocess
import sys
import tempfile
from pathlib import Path

MIN_VERSION = (3, 15)
TMP = Path(tempfile.mkdtemp())
WORKLOAD = TMP / "workload.py"
WORKLOAD.write_text(
    "def slow():\n    return sum(i*i for i in range(3_000_000))\n"
    "def fast():\n    return sum(range(1000))\n"
    "for _ in range(3):\n    slow(); fast()\n", encoding="utf-8")


def sampling(*args, timeout=60):
    return subprocess.run([sys.executable, "-m", "profiling.sampling", *args],
                          capture_output=True, text=True, timeout=timeout)


def example_01_package_layout():
    import profiling
    print([m for m in ("sampling", "tracing") if (Path(profiling.__file__).parent / m).exists()])


def example_02_tracing_is_cprofile():
    from profiling import tracing
    prof = tracing.Profile()
    prof.enable(); sum(i * i for i in range(200_000)); prof.disable()
    out = io.StringIO()
    pstats.Stats(prof, stream=out).sort_stats("cumulative").print_stats(3)
    print(out.getvalue().strip().splitlines()[0])


def example_03_cli_help():
    print("\n".join(sampling("--help").stdout.splitlines()[:3]))


def example_04_run_with_pstats_output():
    r = sampling("run", "--pstats", str(WORKLOAD))
    lines = [l for l in r.stdout.splitlines() if "slow" in l or "fast" in l]
    print("\n".join(lines[:4]) or r.stderr.strip()[-300:])


def example_05_flamegraph_html():
    out = TMP / "flame.html"
    r = sampling("run", "--flamegraph", "-o", str(out), str(WORKLOAD))
    print("flamegraph written:", out.exists(), out.stat().st_size if out.exists() else r.stderr[-200:])


def example_06_collapsed_stacks():
    out = TMP / "stacks.txt"
    sampling("run", "--collapsed", "-o", str(out), str(WORKLOAD))
    print(out.read_text().splitlines()[:2] if out.exists() else "not produced")


def example_07_attach_to_running_process():
    print("python -m profiling.sampling attach <PID> --live      # top-like live view")
    print("python -m profiling.sampling attach <PID> --mode cpu --flamegraph -o cpu.html")


def example_08_dump_current_stacks():
    print("python -m profiling.sampling dump <PID>               # one-shot stack of all threads")
    print("python -m profiling.sampling dump <PID> --async-aware # asyncio task tree")


def example_09_modes():
    for mode, why in {"wall": "where time goes (default)", "cpu": "only on-CPU time",
                      "gil": "who holds the GIL", "exception": "code raising exceptions"}.items():
        print(f"--mode {mode:9} {why}")


def example_10_profile_a_module():
    print("python -m profiling.sampling run -m mypackage.cli --gecko -o profile.json")
    print("then open profile.json at https://profiler.firefox.com")
    print("this process pid:", os.getpid())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
