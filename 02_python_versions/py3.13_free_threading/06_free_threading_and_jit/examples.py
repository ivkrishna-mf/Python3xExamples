"""Free-threading & JIT helpers — Python 3.13+ (PEP 703, 744, 779). Runs on any 3.13+ build."""
import os
import sys
import sysconfig
import threading
import time
from concurrent.futures import ThreadPoolExecutor

MIN_VERSION = (3, 13)


def gil_enabled() -> bool:
    return getattr(sys, "_is_gil_enabled", lambda: True)()


def cpu_work(n=2_000_000):
    total = 0
    for i in range(n):
        total += i * i
    return total


def example_01_is_this_a_free_threaded_build():
    print("Py_GIL_DISABLED build:", bool(sysconfig.get_config_var("Py_GIL_DISABLED")))


def example_02_is_the_gil_active_now():
    print("GIL enabled at runtime:", gil_enabled())


def example_03_cpu_count():
    print("cores available:", os.process_cpu_count() if hasattr(os, "process_cpu_count") else os.cpu_count())


def example_04_parallel_cpu_threads_timing():
    workers = 4
    t = time.perf_counter()
    for _ in range(workers):
        cpu_work(400_000)
    serial = time.perf_counter() - t
    t = time.perf_counter()
    with ThreadPoolExecutor(workers) as ex:
        list(ex.map(cpu_work, [400_000] * workers))
    threaded = time.perf_counter() - t
    print(f"serial {serial:.2f}s | {workers} threads {threaded:.2f}s | speed-up x{serial / threaded:.1f}"
          f" ({'no GIL' if not gil_enabled() else 'GIL limits CPU threads'})")


def example_05_lock_protects_shared_state():
    counter = 0
    lock = threading.Lock()
    def inc():
        nonlocal counter
        for _ in range(50_000):
            with lock:
                counter += 1
    threads = [threading.Thread(target=inc) for _ in range(4)]
    [t.start() for t in threads]; [t.join() for t in threads]
    print("counter =", counter, "(always 200000 with the lock)")


def example_06_thread_local_storage():
    local = threading.local()
    results = []
    def worker(n):
        local.value = n * 10
        time.sleep(0.01)
        results.append(local.value)
    ts = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
    [t.start() for t in ts]; [t.join() for t in ts]
    print(sorted(results))


def example_07_queue_pipeline():
    import queue
    q: queue.Queue[int | None] = queue.Queue()
    out = []
    def consumer():
        while (item := q.get()) is not None:
            out.append(item * item)
    t = threading.Thread(target=consumer); t.start()
    for i in range(5):
        q.put(i)
    q.put(None); t.join()
    print(out)


def example_08_jit_status():
    jit = getattr(sys, "_jit", None)
    if jit is not None:            # 3.14+
        print("JIT available:", jit.is_available(), "| enabled:", jit.is_enabled())
    else:
        print("sys._jit not present; PYTHON_JIT env var =", os.environ.get("PYTHON_JIT", "(unset)"))


def example_09_env_switches():
    for var in ("PYTHON_GIL", "PYTHON_JIT"):
        print(var, "=", os.environ.get(var, "(unset)"))


def example_10_interpreter_info():
    print(sys.version.split()[0], sys.implementation.name, sysconfig.get_config_var("SOABI"))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
