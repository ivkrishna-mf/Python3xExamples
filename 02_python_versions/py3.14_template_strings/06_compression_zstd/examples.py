"""compression.zstd — Python 3.14+ (PEP 784)."""
import json
import tempfile
import time
from pathlib import Path

from compression import gzip, zstd

MIN_VERSION = (3, 14)
DATA = json.dumps([{"id": i, "name": f"user{i}", "active": i % 3 == 0} for i in range(5000)]).encode()
TMP = Path(tempfile.mkdtemp())


def example_01_one_shot():
    c = zstd.compress(DATA)
    print(f"{len(DATA):,} -> {len(c):,} bytes")


def example_02_round_trip():
    print(zstd.decompress(zstd.compress(DATA)) == DATA)


def example_03_levels():
    for level in (1, 3, 10, 19):
        t = time.perf_counter()
        size = len(zstd.compress(DATA, level=level))
        print(f"level {level:2}: {size:,} bytes in {time.perf_counter() - t:.3f}s")


def example_04_compare_with_gzip():
    print("gzip:", len(gzip.compress(DATA)), "| zstd:", len(zstd.compress(DATA)))


def example_05_write_and_read_file():
    path = TMP / "users.json.zst"
    with zstd.open(path, "wb") as fh:
        fh.write(DATA)
    with zstd.open(path, "rb") as fh:
        print(path.name, path.stat().st_size, "bytes on disk |", len(fh.read()), "decompressed")


def example_06_text_mode():
    path = TMP / "log.txt.zst"
    with zstd.open(path, "wt", encoding="utf-8") as fh:
        fh.write("INFO start\nERROR boom\n")
    with zstd.open(path, "rt", encoding="utf-8") as fh:
        print([line.strip() for line in fh])


def example_07_streaming_compressor():
    comp = zstd.ZstdCompressor()
    chunks = [comp.compress(DATA[i:i + 4096]) for i in range(0, len(DATA), 4096)]
    chunks.append(comp.flush())
    print(zstd.decompress(b"".join(chunks)) == DATA)


def example_08_options_checksum():
    c = zstd.compress(DATA, options={zstd.CompressionParameter.checksum_flag: 1})
    print("with checksum:", len(c), "bytes")


def example_09_frame_info():
    info = zstd.get_frame_info(zstd.compress(DATA))
    print(info)


def example_10_tarfile_support():
    import tarfile
    src = TMP / "a.txt"; src.write_text("hello", encoding="utf-8")
    archive = TMP / "bundle.tar.zst"
    with tarfile.open(archive, "w:zst") as tar:
        tar.add(src, arcname="a.txt")
    with tarfile.open(archive, "r:zst") as tar:
        print(tar.getnames())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
