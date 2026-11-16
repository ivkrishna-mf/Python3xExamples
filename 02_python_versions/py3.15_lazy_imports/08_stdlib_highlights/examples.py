"""Python 3.15 stdlib highlights."""
import asyncio
import json
import math
import math.integer as mi
import re
from collections import Counter

MIN_VERSION = (3, 15)


def example_01_math_integer():
    print(mi.gcd(84, 36), mi.lcm(4, 6), mi.isqrt(99), mi.comb(10, 3), mi.perm(5, 2))


def example_02_float_classification():
    tiny = 5e-324
    print(math.isnormal(1.0), math.issubnormal(tiny), math.signbit(-0.0))


def example_03_fmax_fmin():
    print(math.fmax(1.5, float("nan")), math.fmin(-2, 3))


def example_04_re_prefixmatch():
    print(re.prefixmatch(r"\d+", "123abc").group(), re.prefixmatch(r"\d+", "abc123"))


def example_05_compiled_pattern_prefixmatch():
    version = re.compile(r"v(\d+)\.(\d+)")
    print(version.prefixmatch("v3.15 released").groups())


def example_06_counter_symmetric_difference():
    a, b = Counter(apples=3, pears=1), Counter(apples=1, kiwis=2)
    print(a ^ b)


def example_07_bytearray_take_bytes():
    buf = bytearray(b"HEADERpayload-data")
    header = buf.take_bytes(6)
    print(header, buf)


def example_08_taskgroup_cancel_early_exit():
    async def search(shard, found):
        await asyncio.sleep(0.05 * shard)
        if shard == 2:
            found.append(f"hit in shard {shard}")
    async def main():
        found = []
        async with asyncio.TaskGroup() as tg:
            for s in range(1, 6):
                tg.create_task(search(s, found))
            while not found:
                await asyncio.sleep(0.01)
            tg.cancel()                # stop the remaining shards
        print(found)
    asyncio.run(main())


def example_09_json_array_hook():
    print(json.loads("[1, [2, 3]]", array_hook=tuple))


def example_10_frozendict_and_tuple_json():
    data = json.loads('{"tags": ["a", "b"]}', object_hook=frozendict, array_hook=tuple)
    print(data, {data: "usable as a key"}[data])


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
