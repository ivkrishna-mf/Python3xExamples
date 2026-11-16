"""Concurrency — threads, processes, asyncio (modern style, 3.11+ for TaskGroup)."""
import asyncio
import queue
import threading
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

MIN_VERSION = (3, 11)


def fake_io(n: int) -> str:
    time.sleep(0.1)
    return f"result {n}"


def cpu_heavy(n: int) -> int:
    return sum(i * i for i in range(n))


def example_01_thread_pool_map():
    t = time.perf_counter()
    with ThreadPoolExecutor(max_workers=5) as pool:
        results = list(pool.map(fake_io, range(5)))
    print(results, f"{time.perf_counter() - t:.2f}s (not 0.5s)")


def example_02_as_completed():
    with ThreadPoolExecutor() as pool:
        futures = {pool.submit(fake_io, n): n for n in range(3)}
        for fut in as_completed(futures):
            print("done:", futures[fut], fut.result())


def example_03_process_pool_for_cpu():
    with ProcessPoolExecutor(max_workers=2) as pool:
        print(list(pool.map(cpu_heavy, [100_000, 200_000])))


def example_04_raw_threads_and_join():
    results: list[str] = []
    def worker(n: int) -> None:
        results.append(fake_io(n))
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
    for th in threads: th.start()
    for th in threads: th.join()
    print(sorted(results))


def example_05_lock_for_shared_state():
    counter = 0
    lock = threading.Lock()
    def add():
        nonlocal counter
        for _ in range(10_000):
            with lock:
                counter += 1
    ts = [threading.Thread(target=add) for _ in range(4)]
    [t.start() for t in ts]; [t.join() for t in ts]
    print("counter:", counter)


def example_06_producer_consumer_queue():
    q: queue.Queue[int | None] = queue.Queue()
    def producer():
        for i in range(3):
            q.put(i)
        q.put(None)
    def consumer():
        while (item := q.get()) is not None:
            print("  consumed", item)
    threading.Thread(target=producer).start()
    consumer()


def example_07_event_signal():
    ready = threading.Event()
    def waiter():
        ready.wait()
        print("  got the signal")
    t = threading.Thread(target=waiter); t.start()
    time.sleep(0.05); ready.set(); t.join()


def example_08_asyncio_taskgroup():
    async def fetch(n: int) -> str:
        await asyncio.sleep(0.1)
        return f"page {n}"
    async def main():
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fetch(n)) for n in range(5)]
        print([t.result() for t in tasks])
    asyncio.run(main())


def example_09_asyncio_timeout_and_to_thread():
    async def main():
        result = await asyncio.to_thread(fake_io, 99)      # run blocking code without blocking the loop
        try:
            async with asyncio.timeout(0.05):
                await asyncio.sleep(1)
        except TimeoutError:
            print(result, "| slow call timed out")
    asyncio.run(main())


def example_10_asyncio_semaphore_rate_limit():
    async def call_api(i: int, sem: asyncio.Semaphore) -> int:
        async with sem:
            await asyncio.sleep(0.05)
            return i
    async def main():
        sem = asyncio.Semaphore(3)
        t = time.perf_counter()
        results = await asyncio.gather(*(call_api(i, sem) for i in range(9)))
        print(len(results), f"calls, max 3 at a time, {time.perf_counter() - t:.2f}s")
    asyncio.run(main())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
