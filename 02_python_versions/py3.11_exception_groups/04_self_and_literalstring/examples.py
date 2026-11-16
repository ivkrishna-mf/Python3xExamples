"""typing.Self / LiteralString / assert_never — Python 3.11+ (PEP 673, 675)."""
import sqlite3
from dataclasses import dataclass, replace
from enum import Enum
from typing import LiteralString, Self, assert_never

MIN_VERSION = (3, 11)


class QueryBuilder:
    def __init__(self) -> None:
        self.parts: list[str] = []

    def select(self, cols: LiteralString) -> Self:
        self.parts.append(f"SELECT {cols}")
        return self

    def from_(self, table: LiteralString) -> Self:
        self.parts.append(f"FROM {table}")
        return self

    def build(self) -> str:
        return " ".join(self.parts)


class LimitedQuery(QueryBuilder):
    def limit(self, n: int) -> Self:
        self.parts.append(f"LIMIT {int(n)}")
        return self


def example_01_fluent_builder():
    print(QueryBuilder().select("id, name").from_("users").build())


def example_02_subclass_keeps_its_type():
    # Because select() returns Self, .limit() is available on the subclass chain
    print(LimitedQuery().select("*").from_("orders").limit(5).build())


def example_03_classmethod_constructor():
    @dataclass
    class Temperature:
        celsius: float
        @classmethod
        def from_f(cls, f: float) -> Self:
            return cls((f - 32) * 5 / 9)
    class Reading(Temperature): ...
    r = Reading.from_f(98.6)
    print(type(r).__name__, round(r.celsius, 1))


def example_04_with_method_returns_copy():
    @dataclass(frozen=True)
    class Req:
        url: str
        timeout: float = 5
        def with_timeout(self, t: float) -> Self:
            return replace(self, timeout=t)
    print(Req("/api").with_timeout(1))


def example_05_self_in_comparison():
    @dataclass
    class Money:
        cents: int
        def __add__(self, other: Self) -> Self:
            return type(self)(self.cents + other.cents)
    print(Money(150) + Money(250))


def example_06_literalstring_safe_sql():
    def run_query(conn: sqlite3.Connection, sql: LiteralString, params: tuple = ()) -> list:
        return conn.execute(sql, params).fetchall()
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    conn.execute("INSERT INTO users VALUES (1, 'ann'), (2, 'bob')")
    user_input = "bob"
    print(run_query(conn, "SELECT id FROM users WHERE name = ?", (user_input,)))
    # run_query(conn, f"SELECT id FROM users WHERE name = '{user_input}'")  <- checker error


def example_07_literalstring_composition_allowed():
    def table_sql(name: LiteralString) -> LiteralString:
        return "SELECT * FROM " + name     # literal + literal is still LiteralString
    print(table_sql("events"))


def example_08_assert_never_exhaustive():
    class Shape(Enum):
        CIRCLE = 1
        SQUARE = 2
    def sides(s: Shape) -> int:
        match s:
            case Shape.CIRCLE:
                return 0
            case Shape.SQUARE:
                return 4
            case _:
                assert_never(s)   # checker errors if a new member isn't handled
    print(sides(Shape.SQUARE))


def example_09_assert_never_at_runtime():
    try:
        assert_never("unexpected")   # type: ignore[arg-type]
    except AssertionError as exc:
        print("AssertionError:", str(exc)[:50])


def example_10_reveal_and_assert_type():
    from typing import assert_type, reveal_type
    x = [1, 2]
    assert_type(x, list[int])       # no-op at runtime, checked statically
    reveal_type(x)                  # prints the runtime type to stderr


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
