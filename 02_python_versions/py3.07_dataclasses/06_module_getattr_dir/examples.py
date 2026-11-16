"""Module-level __getattr__ / __dir__ — Python 3.7+ (PEP 562). Uses throwaway modules."""
import sys
import types
import warnings

MIN_VERSION = (3, 7)


def make_module(name, source):
    mod = types.ModuleType(name)
    exec(source, mod.__dict__)
    sys.modules[name] = mod
    return mod


def example_01_fallback_attribute():
    m = make_module("m1", "def __getattr__(name):\n    return f'<computed {name}>'")
    print(m.anything)


def example_02_deprecation_warning():
    m = make_module("m2", """
import warnings
new_name = 42
def __getattr__(name):
    if name == "old_name":
        warnings.warn("old_name is deprecated, use new_name", DeprecationWarning, stacklevel=2)
        return new_name
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
""")
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        print(m.old_name, "|", w[0].message)


def example_03_attribute_error_for_unknown():
    m = make_module("m3", "def __getattr__(name):\n    raise AttributeError(name)")
    print(hasattr(m, "missing"))


def example_04_lazy_submodule_loading():
    m = make_module("m4", """
import importlib
_lazy = {"json": "json", "decimal": "decimal"}
def __getattr__(name):
    if name in _lazy:
        mod = importlib.import_module(_lazy[name])
        globals()[name] = mod       # cache for next time
        return mod
    raise AttributeError(name)
""")
    print("json" in m.__dict__, m.json.dumps([1]), "json" in m.__dict__)


def example_05_custom_dir():
    m = make_module("m5", "a = 1\n_private = 2\ndef __dir__():\n    return ['a', 'virtual']")
    print(dir(m))


def example_06_computed_constant():
    m = make_module("m6", """
import os
def __getattr__(name):
    if name == "CPU_COUNT":
        return os.cpu_count()
    raise AttributeError(name)
""")
    print("CPU_COUNT =", m.CPU_COUNT)


def example_07_aliases():
    m = make_module("m7", """
def compute(): return "computed"
_aliases = {"calc": "compute", "run": "compute"}
def __getattr__(name):
    if name in _aliases:
        return globals()[_aliases[name]]
    raise AttributeError(name)
""")
    print(m.calc(), m.run())


def example_08_from_import_uses_getattr():
    make_module("m8", "def __getattr__(name):\n    return name.upper()")
    from m8 import hello  # noqa
    print(hello)


def example_09_normal_attributes_win():
    m = make_module("m9", "x = 'real'\ndef __getattr__(name):\n    return 'fallback'")
    print(m.x, m.y)


def example_10_count_accesses():
    m = make_module("m10", """
hits = {}
def __getattr__(name):
    hits[name] = hits.get(name, 0) + 1
    return None
""")
    m.a; m.a; m.b
    print(m.hits)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
