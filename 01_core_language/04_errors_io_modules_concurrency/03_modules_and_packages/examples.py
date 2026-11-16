"""Modules & packages — builds a tiny package in a temp dir and imports it."""
import importlib
import importlib.util
import sys
import tempfile
import textwrap
from pathlib import Path

MIN_VERSION = (3, 9)
ROOT = Path(tempfile.mkdtemp())
PKG = ROOT / "shop"
(PKG / "payments").mkdir(parents=True)
(PKG / "__init__.py").write_text(textwrap.dedent('''\
    """Shop package."""
    from .cart import Cart
    __all__ = ["Cart"]
    __version__ = "1.0.0"
    '''), encoding="utf-8")
(PKG / "cart.py").write_text(textwrap.dedent('''\
    from .payments.card import charge
    class Cart:
        def __init__(self): self.items = []
        def add(self, item, price): self.items.append((item, price)); return self
        def checkout(self): return charge(sum(p for _, p in self.items))
    def _private_helper(): ...
    '''), encoding="utf-8")
(PKG / "payments" / "__init__.py").write_text("", encoding="utf-8")
(PKG / "payments" / "card.py").write_text(
    "def charge(amount):\n    return f'charged ${amount:.2f}'\n", encoding="utf-8")
(ROOT / "tool.py").write_text(
    "def main():\n    return 'tool ran'\nif __name__ == '__main__':\n    print(main())\n", encoding="utf-8")
sys.path.insert(0, str(ROOT))


def example_01_import_package():
    import shop
    print(shop.__doc__, shop.__version__)


def example_02_from_import():
    from shop import Cart
    print(Cart().add("pen", 1.5).add("ink", 3).checkout())


def example_03_import_submodule_with_alias():
    import shop.payments.card as card
    print(card.charge(9.99))


def example_04_all_controls_star_import():
    ns = {}
    exec("from shop import *", ns)
    print([k for k in ns if not k.startswith("__")])


def example_05_module_attributes():
    import shop.cart
    print(shop.cart.__name__, Path(shop.cart.__file__).name, shop.cart.__package__)


def example_06_name_main_guard():
    import tool
    print("imported, not executed as script ->", tool.main())


def example_07_dynamic_import():
    mod = importlib.import_module("shop.payments.card")
    print(mod.charge(1))


def example_08_load_from_file_path():
    spec = importlib.util.spec_from_file_location("tool_copy", ROOT / "tool.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    print(mod.main())


def example_09_sys_modules_cache():
    import shop
    print("shop" in sys.modules, sys.modules["shop"] is shop)


def example_10_reload():
    import tool
    (ROOT / "tool.py").write_text("def main():\n    return 'tool v2'\n", encoding="utf-8")
    importlib.invalidate_caches()
    print(importlib.reload(tool).main())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
