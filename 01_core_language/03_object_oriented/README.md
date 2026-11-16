# Core Language · Object-Oriented Programming
Classes, inheritance and MRO, special ("dunder") methods, properties and descriptors,
abstract base classes and protocols, and metaclasses. Modern style throughout:
dataclasses, `Self`, `@override` and 3.12 generics.

| # | Feature | In one line |
|---|---|---|
| 01 | [Classes and objects](01_classes_and_objects/README.md) | bundle data (attributes) and behaviour (methods) into your own types. |
| 02 | [Inheritance, super() and the MRO](02_inheritance_and_mro/README.md) | reuse and specialise behaviour from parent classes; `super()` follows the method resolution order. |
| 03 | [Special ("dunder") methods and operator overloading](03_dunder_methods/README.md) | implement `__len__`, `__eq__`, `__add__`, `__iter__`, `__getitem__`, `__call__`… so your objects work with Python syntax and built-ins. |
| 04 | [Properties, descriptors and __slots__](04_properties_and_descriptors/README.md) | control attribute access — computed attributes, validation and memory-lean objects. |
| 05 | [Abstract base classes (abc) and Protocols](05_abstract_classes_and_protocols/README.md) | define interfaces — nominal (ABC: must inherit) or structural (Protocol: just match the methods). |
| 06 | [Metaclasses and dynamic class creation](06_metaclasses_and_class_creation/README.md) | classes are objects created by a metaclass (`type` by default) — you can customise how classes are built. |

Run every example in this folder:
```bash
python ../../run_examples.py 01_core_language/03_object_oriented
```
