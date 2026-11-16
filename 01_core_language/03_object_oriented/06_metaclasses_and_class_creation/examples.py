"""Metaclasses & class creation — modern style."""
MIN_VERSION = (3, 10)


def example_01_classes_are_objects():
    class A: ...
    print(type(A), type(type), isinstance(A, type))


def example_02_create_class_with_type():
    def greet(self): return f"hi, I am {self.name}"
    Person = type("Person", (), {"name": "ann", "greet": greet})
    print(Person().greet(), Person.__name__)


def example_03_simple_metaclass():
    class Meta(type):
        def __new__(mcs, name, bases, ns):
            ns["created_by"] = "Meta"
            return super().__new__(mcs, name, bases, ns)
    class Model(metaclass=Meta): ...
    print(Model.created_by)


def example_04_registry_metaclass():
    class RegistryMeta(type):
        registry: dict[str, type] = {}
        def __init__(cls, name, bases, ns):
            super().__init__(name, bases, ns)
            if bases:
                RegistryMeta.registry[name.lower()] = cls
    class Handler(metaclass=RegistryMeta): ...
    class JsonHandler(Handler): ...
    class XmlHandler(Handler): ...
    print(list(RegistryMeta.registry))


def example_05_enforce_rules():
    class RequireDocs(type):
        def __new__(mcs, name, bases, ns):
            for attr, val in ns.items():
                if callable(val) and not attr.startswith("_") and not val.__doc__:
                    raise TypeError(f"{name}.{attr} needs a docstring")
            return super().__new__(mcs, name, bases, ns)
    try:
        class Api(metaclass=RequireDocs):
            def get(self): pass
    except TypeError as exc:
        print("TypeError:", exc)


def example_06_singleton():
    class Singleton(type):
        _instances: dict[type, object] = {}
        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]
    class Settings(metaclass=Singleton):
        def __init__(self): print("  Settings created")
    print(Settings() is Settings())


def example_07_prepare_custom_namespace():
    class OrderedFields(type):
        @classmethod
        def __prepare__(mcs, name, bases):
            return {"_field_order": []}
        def __new__(mcs, name, bases, ns):
            ns["_field_order"] = [k for k in ns if not k.startswith("_")]
            return super().__new__(mcs, name, bases, ns)
    class Row(metaclass=OrderedFields):
        id = 1
        name = "x"
        email = "y"
    print(Row._field_order)


def example_08_init_subclass_is_often_enough():
    class Base:
        subclasses: list[str] = []
        def __init_subclass__(cls, **kw):
            super().__init_subclass__(**kw)
            Base.subclasses.append(cls.__name__)
    class A(Base): ...
    class B(Base): ...
    print(Base.subclasses, "(no metaclass needed)")


def example_09_class_decorator_alternative():
    def auto_str(cls):
        cls.__str__ = lambda self: f"{cls.__name__}{vars(self)}"
        return cls
    @auto_str
    class Point:
        def __init__(self, x, y): self.x, self.y = x, y
    print(str(Point(1, 2)))


def example_10_enum_uses_a_metaclass():
    from enum import Enum
    class Color(Enum):
        RED = 1
    print(type(Color).__name__, list(Color), len(Color))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
