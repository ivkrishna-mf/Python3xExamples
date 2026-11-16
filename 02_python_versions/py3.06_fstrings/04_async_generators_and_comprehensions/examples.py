"""Async generators & comprehensions — Python 3.6+ (PEP 525, 530). Some examples use := (3.8)."""
import asyncio
import contextlib

MIN_VERSION = (3, 8)


async def countdown(n, delay=0.01):
    while n > 0:
        await asyncio.sleep(delay)
        yield n
        n -= 1


def run(coro):
    return asyncio.run(coro)


def example_01_async_for():
    async def main():
        async for n in countdown(3):
            print(n)
    run(main())


def example_02_async_list_comprehension():
    async def main():
        print([n async for n in countdown(4)])
    run(main())


def example_03_async_comprehension_with_filter():
    async def main():
        print([n * 10 async for n in countdown(6) if n % 2 == 0])
    run(main())


def example_04_await_inside_comprehension():
    async def double(x):
        await asyncio.sleep(0)
        return x * 2
    async def main():
        print([await double(x) for x in range(4)])
    run(main())


def example_05_paginated_api():
    async def fetch_page(page):
        await asyncio.sleep(0.01)
        return [f"item{page}-{i}" for i in range(2)] if page < 3 else []
    async def all_items():
        page = 0
        while items := await fetch_page(page):
            for item in items:
                yield item
            page += 1
    async def main():
        print([x async for x in all_items()])
    run(main())


def example_06_pipeline_stages():
    async def source():
        for i in range(5):
            yield i
    async def squared(agen):
        async for x in agen:
            yield x * x
    async def evens(agen):
        async for x in agen:
            if x % 2 == 0:
                yield x
    async def main():
        print([x async for x in evens(squared(source()))])
    run(main())


def example_07_async_set_and_dict_comprehension():
    async def main():
        print({n % 3 async for n in countdown(6)})
        print({n: n * n async for n in countdown(3)})
    run(main())


def example_08_cleanup_with_aclose():
    async def stream():
        try:
            for i in range(100):
                yield i
        finally:
            print("stream closed, resources released")
    async def main():
        gen = stream()
        async for x in gen:
            if x == 2:
                break
        await gen.aclose()
    run(main())


def example_09_asynccontextmanager():
    @contextlib.asynccontextmanager
    async def session():
        print("connect")
        yield "session"
        print("disconnect")
    async def main():
        async with session() as s:
            print("using", s)
    run(main())


def example_10_async_generator_expression():
    async def main():
        gen = (n async for n in countdown(3))
        print(type(gen).__name__, [x async for x in gen])
    run(main())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
