"""secrets — Python 3.6+ (PEP 506)."""
import secrets
import string

MIN_VERSION = (3, 6)


def example_01_hex_token():
    print(secrets.token_hex(16))


def example_02_url_safe_token():
    print(secrets.token_urlsafe(24))


def example_03_raw_bytes():
    print(secrets.token_bytes(8))


def example_04_random_password():
    alphabet = string.ascii_letters + string.digits + "!@#$%"
    print("".join(secrets.choice(alphabet) for _ in range(16)))


def example_05_password_with_rules():
    alphabet = string.ascii_letters + string.digits
    while True:
        pw = "".join(secrets.choice(alphabet) for _ in range(12))
        if any(c.islower() for c in pw) and any(c.isupper() for c in pw) \
                and sum(c.isdigit() for c in pw) >= 3:
            break
    print(pw)


def example_06_otp_code():
    print(f"{secrets.randbelow(1_000_000):06d}")


def example_07_constant_time_compare():
    expected = "a1b2c3"
    print(secrets.compare_digest(expected, "a1b2c3"), secrets.compare_digest(expected, "zzz"))


def example_08_random_bits():
    print(secrets.randbits(32))


def example_09_reset_link():
    token = secrets.token_urlsafe(32)
    print(f"https://example.com/reset?token={token}")


def example_10_xkcd_style_passphrase():
    words = ["correct", "horse", "battery", "staple", "orbit", "lemon", "river", "piano"]
    print("-".join(secrets.choice(words) for _ in range(4)))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
