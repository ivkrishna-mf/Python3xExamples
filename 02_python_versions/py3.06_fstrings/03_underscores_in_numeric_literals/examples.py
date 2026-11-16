"""Underscores in numeric literals — Python 3.6+ (PEP 515)."""
MIN_VERSION = (3, 6)


def example_01_big_integers():
    population = 8_100_000_000
    print(population)


def example_02_floats():
    avogadro = 6.022_140_76e23
    print(avogadro)


def example_03_binary_masks():
    flags = 0b_1111_0000
    print(flags, bin(flags))


def example_04_hex_bytes():
    color = 0xFF_88_00
    print(hex(color))


def example_05_byte_sizes():
    MB = 1_048_576
    print(f"{5 * MB:_} bytes")


def example_06_format_with_underscore():
    print(f"{123456789:_}", f"{0xDEADBEEF:_x}")


def example_07_int_parses_underscores():
    print(int("1_000"), float("1_0.5"))


def example_08_money_in_cents():
    price_cents = 1_999_00
    print(f"${price_cents / 100:,.2f}")


def example_09_invalid_positions():
    for src in ("1__0", "1_", "_1"):
        try:
            eval(src)
            print(src, "-> valid name/number")
        except (SyntaxError, NameError) as exc:
            print(f"{src!r}: {type(exc).__name__}")


def example_10_timeouts_in_ms():
    TIMEOUT_MS = 30_000
    print(TIMEOUT_MS / 1_000, "seconds")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
