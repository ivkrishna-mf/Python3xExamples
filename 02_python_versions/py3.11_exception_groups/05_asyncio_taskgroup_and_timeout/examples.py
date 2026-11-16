"""asyncio.TaskGroup & asyncio.timeout — Python 3.11+."""
import asyncio
import time

MIN_VERSION = (3, 11)


async def fetch(name, delay, fail=False):
    await asyncio.sleep(delay)
    if fail:
        raise ConnectionError(f"{name} failed")
    return f"{name}:ok"


def example_01_basic_taskgroup():
    async def main():
        async with asyncio.TaskGroup() as tg:
            t1 = tg.create_task(fetch("users", 0.05))
            t2 = tg.create_task(fetch("orders", 0.05))
        print(t1.result(), t2.result())
    asyncio.run(main())


def example_02_failure_cancels_siblings():
    async def slow():
        try:
            await asyncio.sleep(5)
        except asyncio.CancelledError:
            print("  slow task was cancelled")
            raise
    async def main():
        try:
            async with asyncio.TaskGroup() as tg:
                tg.create_task(slow())
                tg.create_task(fetch("api", 0.05, fail=True))
        except* ConnectionError as eg:
            print("error:", eg.exceptions[0])
    asyncio.run(main())


def example_03_collect_results_list():
    async def main():
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fetch(f"page{i}", 0.02)) for i in range(4)]
        print([t.result() for t in tasks])
    asyncio.run(main())


def example_04_timeout_context():
    async def main():
        try:
            async with asyncio.timeout(0.1):
                await fetch("slow", 1)
        except TimeoutError:
            print("operation timed out")
    asyncio.run(main())


def example_05_timeout_around_taskgroup():
    async def main():
        t = time.perf_counter()
        try:
            async with asyncio.timeout(0.2):
                async with asyncio.TaskGroup() as tg:
                    tg.create_task(fetch("a", 0.1))
                    tg.create_task(fetch("b", 2))
        except TimeoutError:
            print(f"group cancelled after {time.perf_counter() - t:.2f}s")
    asyncio.run(main())


def example_06_timeout_at_and_reschedule():
    async def main():
        loop = asyncio.get_running_loop()
        async with asyncio.timeout(None) as cm:      # no deadline yet
            cm.reschedule(loop.time() + 0.5)         # decide later
            print(await fetch("x", 0.1), "| deadline set:", cm.when() is not None)
    asyncio.run(main())


def example_07_nested_task_groups():
    async def section(name):
        async with asyncio.TaskGroup() as tg:
            ts = [tg.create_task(fetch(f"{name}{i}", 0.01)) for i in range(2)]
        return [t.result() for t in ts]
    async def main():
        async with asyncio.TaskGroup() as tg:
            a = tg.create_task(section("A"))
            b = tg.create_task(section("B"))
        print(a.result() + b.result())
    asyncio.run(main())


def example_08_task_names():
    async def main():
        async with asyncio.TaskGroup() as tg:
            t = tg.create_task(fetch("n", 0.01), name="loader")
        print(t.get_name(), t.result())
    asyncio.run(main())


def example_09_compare_with_gather_return_exceptions():
    async def main():
        results = await asyncio.gather(fetch("a", 0.01), fetch("b", 0.01, fail=True),
                                       return_exceptions=True)
        print([r if isinstance(r, str) else repr(r) for r in results])
    asyncio.run(main())


def example_10_bounded_concurrency_inside_group():
    async def main():
        sem = asyncio.Semaphore(2)
        async def limited(i):
            async with sem:
                return await fetch(f"job{i}", 0.02)
        async with asyncio.TaskGroup() as tg:
            ts = [tg.create_task(limited(i)) for i in range(5)]
        print(len([t.result() for t in ts]), "jobs done, max 2 at a time")
    asyncio.run(main())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
