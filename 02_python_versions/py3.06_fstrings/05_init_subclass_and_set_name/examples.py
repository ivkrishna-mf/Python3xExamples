"""__init_subclass__ & __set_name__ — Python 3.6+ (PEP 487)."""
MIN_VERSION = (3, 6)


def example_01_plugin_registry():
    class Plugin:
        registry = {}
        def __init_subclass__(cls, **kw):
            super().__init_subclass__(**kw)
            Plugin.registry[cls.__name__.lower()] = cls
    class Csv(Plugin): ...
    class Json(Plugin): ...
    print(list(Plugin.registry))


def example_02_class_keyword_arguments():
    class Exporter:
        def __init_subclass__(cls, ext="txt", **kw):
            super().__init_subclass__(**kw)
            cls.ext = ext
    class CsvExporter(Exporter, ext="csv"): ...
    print(CsvExporter.ext)


def example_03_enforce_required_attribute():
    class Command:
        def __init_subclass__(cls, **kw):
            super().__init_subclass__(**kw)
            if not hasattr(cls, "name"):
                raise TypeError(f"{cls.__name__} must define 'name'")
    try:
        class Broken(Command): ...
    except TypeError as exc:
        print("TypeError:", exc)


def example_04_set_name_descriptor():
    class Field:
        def __set_name__(self, owner, name):
            self.name = name
        def __get__(self, obj, objtype=None):
            if obj is None:          # accessed on the class
                return self
            return obj.__dict__.get(self.name, "<unset>")
        def __set__(self, obj, value):
            obj.__dict__[self.name] = value
    class User:
        email = Field()
    u = User()
    print(u.email); u.email = "a@b.c"; print(u.email, User.email.name)


def example_05_validating_descriptor():
    class Positive:
        def __set_name__(self, owner, name):
            self.private = "_" + name
        def __get__(self, obj, objtype=None):
            return getattr(obj, self.private)
        def __set__(self, obj, value):
            if value <= 0:
                raise ValueError(f"{self.private[1:]} must be > 0")
            setattr(obj, self.private, value)
    class Order:
        qty = Positive()
        def __init__(self, qty): self.qty = qty
    print(Order(3).qty)
    try:
        Order(0)
    except ValueError as exc:
        print("ValueError:", exc)


def example_06_count_subclasses():
    class Shape:
        count = 0
        def __init_subclass__(cls, **kw):
            Shape.count += 1
    class Circle(Shape): ...
    class Square(Shape): ...
    print(Shape.count)


def example_07_typed_field_descriptor():
    class Typed:
        def __init__(self, kind): self.kind = kind
        def __set_name__(self, owner, name): self.name = name
        def __get__(self, obj, objtype=None): return obj.__dict__[self.name]
        def __set__(self, obj, v):
            if not isinstance(v, self.kind):
                raise TypeError(f"{self.name} must be {self.kind.__name__}")
            obj.__dict__[self.name] = v
    class Product:
        price = Typed(float)
    p = Product(); p.price = 9.99
    try:
        p.price = "free"
    except TypeError as exc:
        print(p.price, "| TypeError:", exc)


def example_08_auto_table_names():
    class Model:
        def __init_subclass__(cls, table=None, **kw):
            super().__init_subclass__(**kw)
            cls.__table__ = table or cls.__name__.lower() + "s"
    class User(Model): ...
    class Person(Model, table="people"): ...
    print(User.__table__, Person.__table__)


def example_09_set_name_collects_fields():
    class Col:
        def __set_name__(self, owner, name):
            owner._columns = getattr(owner, "_columns", []) + [name]
    class Table:
        id = Col()
        name = Col()
    print(Table._columns)


def example_10_chain_with_super():
    class A:
        def __init_subclass__(cls, **kw):
            print("A hook for", cls.__name__)
            super().__init_subclass__(**kw)
    class B(A):
        def __init_subclass__(cls, **kw):
            print("B hook for", cls.__name__)
            super().__init_subclass__(**kw)
    class C(B): ...


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
