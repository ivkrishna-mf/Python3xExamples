"""Numbers & math — modern style."""
import math
from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction

MIN_VERSION = (3, 8)


def example_01_arithmetic_operators():
    print(7 / 2, 7 // 2, 7 % 2, 2 ** 10, -7 // 2, divmod(17, 5))


def example_02_big_integers():
    print(2 ** 200)
    print(f"{math.factorial(25):,}")


def example_03_float_precision():
    print(0.1 + 0.2, 0.1 + 0.2 == 0.3, math.isclose(0.1 + 0.2, 0.3))


def example_04_decimal_for_money():
    price = Decimal("19.99")
    total = (price * 3 * Decimal("1.18")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(total)


def example_05_fractions():
    print(Fraction(1, 3) + Fraction(1, 6), Fraction("0.75"), Fraction(0.5))


def example_06_bases_and_literals():
    print(0b1010, 0o17, 0xFF, 1_000_000, bin(10), hex(255), int("ff", 16))


def example_07_math_module():
    print(math.sqrt(16), math.pi, math.ceil(2.1), math.floor(-2.1), math.gcd(48, 18), math.hypot(3, 4))


def example_08_rounding():
    print(round(2.675, 2), round(1234.5678, -2), round(0.5), round(1.5), f"{2.675:.2f}")


def example_09_complex_numbers():
    z = 3 + 4j
    print(abs(z), z.real, z.imag, z.conjugate())


def example_10_special_floats():
    inf, nan = float("inf"), float("nan")
    print(inf > 10**308, nan == nan, math.isnan(nan), math.isinf(-inf))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
