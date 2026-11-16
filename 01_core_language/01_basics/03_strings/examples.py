"""Strings — modern style."""
import textwrap

MIN_VERSION = (3, 9)


def example_01_literals():
    single, double = 'it\'s', "say \"hi\""
    raw = r"C:\new\table"
    multi = """line 1
line 2"""
    print(single, double, raw, multi, sep=" | ")


def example_02_indexing_and_slicing():
    s = "Python"
    print(s[0], s[-1], s[1:4], s[::-1], s[::2])


def example_03_fstring_formatting():
    name, balance = "Ada", 1234.5
    print(f"{name:<6}|{balance:>12,.2f}|{0.0725:.1%}")


def example_04_split_and_join():
    csv = "a, b ,c"
    parts = [p.strip() for p in csv.split(",")]
    print(parts, "-".join(parts))


def example_05_common_methods():
    s = "  Hello, World  "
    print(s.strip().lower(), s.count("l"), s.replace("World", "Python").strip(), s.find("W"))


def example_06_checks():
    print("abc123".isalnum(), "123".isdigit(), "Title Case".istitle(), "report.csv".endswith((".csv", ".tsv")))


def example_07_case_insensitive_compare():
    print("Straße".casefold() == "STRASSE".casefold(), "Hi".lower() == "hI".lower())


def example_08_build_efficiently():
    words = [f"w{i}" for i in range(5)]
    print(" ".join(words))


def example_09_unicode():
    s = "naïve café 😀"
    print(len(s), s.encode("utf-8"), [ord(c) for c in "é😀"], chr(9731))


def example_10_dedent_wrap_and_prefixes():
    doc = textwrap.dedent("""\
        Python strings are immutable sequences of Unicode code points.
        """)
    print(textwrap.fill(doc, width=30))
    print("v3.15".removeprefix("v"), "data.json".removesuffix(".json"))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
