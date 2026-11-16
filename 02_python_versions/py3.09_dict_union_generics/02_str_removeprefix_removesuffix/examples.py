"""str.removeprefix / removesuffix — Python 3.9+ (PEP 616)."""
MIN_VERSION = (3, 9)


def example_01_basic_prefix():
    print("test_login".removeprefix("test_"))


def example_02_basic_suffix():
    print("report.csv".removesuffix(".csv"))


def example_03_no_match_returns_original():
    print("hello".removeprefix("xyz"))


def example_04_vs_lstrip_gotcha():
    s = "pypython"
    print("lstrip:", s.lstrip("py"), "| removeprefix:", s.removeprefix("py"))


def example_05_url_scheme():
    for url in ["https://python.org", "http://example.com", "ftp.host"]:
        print(url.removeprefix("https://").removeprefix("http://"))


def example_06_version_tag():
    print([t.removeprefix("v") for t in ["v3.12", "v3.13", "3.14"]])


def example_07_redis_style_keys():
    keys = ["user:1", "user:42", "session:9"]
    print([k.removeprefix("user:") for k in keys if k.startswith("user:")])


def example_08_bytes_support():
    print(b"\xef\xbb\xbfhello".removeprefix(b"\xef\xbb\xbf"))   # drop UTF-8 BOM


def example_09_only_once():
    print("aaab".removeprefix("a"), "ababab".removesuffix("ab"))


def example_10_clean_test_names():
    names = ["test_api.py", "test_db.py", "helpers.py"]
    print([n.removeprefix("test_").removesuffix(".py") for n in names])


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
