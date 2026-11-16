"""Explicit lazy imports — Python 3.15+ (PEP 810). `lazy` must be used at module scope."""
import sys
import tempfile
import types
from pathlib import Path

lazy import decimal
lazy import fractions
lazy from statistics import median
lazy import xml.dom.minidom
lazy import this_module_does_not_exist_xyz

MIN_VERSION = (3, 15)


def is_lazy(name):
    return isinstance(globals()[name], types.LazyImportType)


def example_01_not_loaded_until_used():
    print("decimal loaded?", "decimal" in sys.modules)
    print(decimal.Decimal("0.1") + decimal.Decimal("0.2"))
    print("decimal loaded?", "decimal" in sys.modules)


def example_02_proxy_type_before_use():
    print("fractions is a lazy proxy:", is_lazy("fractions"))
    fractions.Fraction(1, 3)
    print("after use:", is_lazy("fractions"), type(fractions).__name__)


def example_03_lazy_from_import():
    print(median([5, 1, 9]))


def example_04_dotted_module():
    doc = xml.dom.minidom.parseString("<a><b>hi</b></a>")
    print(doc.getElementsByTagName("b")[0].firstChild.data)


def example_05_errors_happen_at_first_use():
    try:
        this_module_does_not_exist_xyz.something
    except ImportError as exc:
        print(type(exc).__name__, "raised only now:", exc.name)


def example_06_global_mode():
    print("current mode:", sys.get_lazy_imports(), "| options: normal, all, none")


def example_07_filter_function():
    def only_my_app(importing, imported, fromlist):
        return imported.startswith("myapp.")
    print("sys.set_lazy_imports_filter(only_my_app) would make only myapp.* lazy:",
          only_my_app(None, "myapp.reports", None), only_my_app(None, "json", None))


def example_08_lazy_modules_compat_list():
    d = Path(tempfile.mkdtemp())
    (d / "compat_mod.py").write_text(
        '__lazy_modules__ = ["wave"]\n'
        "import wave            # lazy on 3.15+, eager on older Pythons\n"
        "import sys\n"
        "loaded_at_import = 'wave' in sys.modules\n", encoding="utf-8")
    sys.path.insert(0, str(d))
    import compat_mod
    print("wave loaded during import?", compat_mod.loaded_at_import)


def example_09_restrictions_are_syntax_errors():
    for src in ("def f():\n    lazy import json", "lazy from json import *",
                "try:\n    lazy import json\nexcept ImportError:\n    pass"):
        try:
            compile(src, "<demo>", "exec")
        except SyntaxError as exc:
            print("SyntaxError:", exc.msg)


def example_10_cli_startup_pattern():
    print("""Typical CLI layout:
    lazy import pandas          # only for 'export'
    lazy import matplotlib.pyplot as plt   # only for 'plot'
    def main(cmd):
        match cmd:
            case "export": pandas.DataFrame(...)
            case "plot":   plt.plot(...)
    -> `tool --help` starts instantly because nothing heavy is loaded.""")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
