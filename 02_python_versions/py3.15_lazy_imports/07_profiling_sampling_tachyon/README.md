# profiling package & Tachyon sampling profiler — Python 3.15 (PEP 799)

**In one line:** `python -m profiling.sampling run app.py` profiles with near-zero overhead — even attach to a running PID.

## What it is
A new `profiling` package groups the profilers: `profiling.tracing` (the deterministic
cProfile) and `profiling.sampling` ("Tachyon"), which samples stacks of a target process at
high frequency. Subcommands: `run`, `attach PID`, `dump PID`, `replay`. Output formats include
`--pstats`, `--collapsed`, `--flamegraph` (HTML), `--gecko` (Firefox Profiler), `--heatmap`,
`--live` (top-like TUI). Modes: `--mode wall|cpu|gil|exception`, `--async-aware`, `-a` all threads.

## When to use
- Finding hot spots in production-like runs without instrumenting code.
- Attaching to a stuck or slow running service to see what it's doing.
- Asyncio apps (`--async-aware`) and GIL-contention analysis (`--mode gil`).

## When NOT to use
- Exact call counts → deterministic `profiling.tracing` / cProfile.
- Attaching may need elevated permissions (ptrace on Linux, admin on Windows/macOS).

## Run
```bash
python3.15 examples.py                                    # self-contained demos
python3.15 -m profiling.sampling run --pstats examples.py # profile the demos themselves
```
