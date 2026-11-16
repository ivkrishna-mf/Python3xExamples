"""async / await — Python 3.5+ (PEP 492). Examples also use asyncio.run (3.7), := (3.8), to_thread (3.9)."""
import asyncio
import time

MIN_VERSION = (3, 9)


async def fetch(name, delay):
    await asyncio.sleep(delay)          # simulates network I/O
    return f"{name} done in {delay}s"


def example_01_hello_coroutine():
    async def main():
        print(await fetch("hello", 0.05))
    asyncio.run(main())


def example_02_gather_runs_concurrently():
    async def main():
        t = time.perf_counter()
        results = await asyncio.gather(fetch("a", 0.2), fetch("b", 0.2), fetch("c", 0.2))
        print(results, f"total {time.perf_counter() - t:.2f}s (not 0.6s)")
    asyncio.run(main())


def example_03_create_task_background():
    async def main():
        task = asyncio.create_task(fetch("bg", 0.1))
        print("doing other work while task runs...")
        print(await task)
    asyncio.run(main())


def example_04_timeout_with_wait_for():
    async def main():
        try:
            await asyncio.wait_for(fetch("slow", 1), timeout=0.1)
        except asyncio.TimeoutError:
            print("timed out")
    asyncio.run(main())


def example_05_as_completed_order():
    async def main():
        coros = [fetch("slow", 0.3), fetch("fast", 0.1), fetch("mid", 0.2)]
        for fut in asyncio.as_completed(coros):
            print(await fut)
    asyncio.run(main())


def example_06_semaphore_limits_concurrency():
    async def main():
        sem = asyncio.Semaphore(2)
        async def limited(i):
            async with sem:
                await asyncio.sleep(0.05)
                return i
        print(await asyncio.gather(*(limited(i) for i in range(6))))
    asyncio.run(main())


def example_07_producer_consumer_queue():
    async def main():
        q = asyncio.Queue()
        async def producer():
            for i in range(3):
                await q.put(i)
            await q.put(None)
        async def consumer():
            while (item := await q.get()) is not None:
                print("consumed", item)
        await asyncio.gather(producer(), consumer())
    asyncio.run(main())


def example_08_async_context_manager():
    class Connection:
        async def __aenter__(self):
            print("open"); return self
        async def __aexit__(self, *exc):
            print("close")
        async def query(self):
            await asyncio.sleep(0.01); return [1, 2]
    async def main():
        async with Connection() as conn:
            print(await conn.query())
    asyncio.run(main())


def example_09_async_iterator():
    class Ticker:
        def __init__(self, n): self.n = n
        def __aiter__(self): return self
        async def __anext__(self):
            if self.n == 0:
                raise StopAsyncIteration
            self.n -= 1
            await asyncio.sleep(0.01)
            return self.n
    async def main():
        async for tick in Ticker(3):
            print("tick", tick)
    asyncio.run(main())


def example_10_blocking_code_in_thread():
    def blocking_io():
        time.sleep(0.1)
        return "blocking result"
    async def main():
        result = await asyncio.to_thread(blocking_io)   # 3.9+
        print(result)
    asyncio.run(main())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
