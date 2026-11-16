"""str vs bytes — Python 3.0+ (PEP 3137)."""
import hashlib

MIN_VERSION = (3, 0)


def example_01_encode_text():
    text = "café"
    data = text.encode("utf-8")
    print(text, len(text), "chars ->", data, len(data), "bytes")


def example_02_decode_bytes():
    data = b"caf\xc3\xa9"
    print(data.decode("utf-8"))


def example_03_mixing_raises():
    try:
        "abc" + b"def"
    except TypeError as exc:
        print("TypeError:", exc)


def example_04_error_handlers():
    bad = b"hello \xff world"
    print(bad.decode("utf-8", errors="replace"))
    print(bad.decode("utf-8", errors="ignore"))


def example_05_bytes_index_gives_int():
    data = b"ABC"
    print(data[0], data[0:1])          # 65  b'A'


def example_06_bytearray_is_mutable():
    buf = bytearray(b"hello")
    buf[0] = ord("H")
    buf.extend(b"!")
    print(buf, bytes(buf))


def example_07_hashing_needs_bytes():
    digest = hashlib.sha256("password".encode()).hexdigest()
    print(digest[:16], "...")


def example_08_hex_round_trip():
    data = bytes([0, 15, 255])
    print(data.hex(), bytes.fromhex("000fff"))


def example_09_unicode_normalisation():
    import unicodedata
    a = "é"                       # one code point
    b = "é"                 # e + combining accent
    print(a == b, unicodedata.normalize("NFC", b) == a)


def example_10_binary_file_round_trip():
    import tempfile, os
    path = os.path.join(tempfile.gettempdir(), "demo.bin")
    with open(path, "wb") as fh:
        fh.write(bytes(range(5)))
    with open(path, "rb") as fh:
        print(list(fh.read()))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
