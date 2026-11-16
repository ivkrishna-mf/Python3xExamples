"""Template strings (t-strings) — Python 3.14+ (PEP 750)."""
import html
import json
import shlex
import sqlite3
from string.templatelib import Interpolation, Template

MIN_VERSION = (3, 14)


def render(template: Template, transform=str) -> str:
    out = []
    for part in template:
        if isinstance(part, Interpolation):
            value = format(part.value, part.format_spec) if part.format_spec else part.value
            out.append(transform(value))
        else:
            out.append(part)
    return "".join(out)


def example_01_it_is_not_a_string():
    name = "ann"
    t = t"Hello {name}!"
    print(type(t).__name__, t.strings, t.values)


def example_02_inspect_interpolations():
    price, qty = 9.5, 3
    t = t"{qty} x {price:.2f} = {qty * price!r}"
    for i in t.interpolations:
        print(i.expression, i.value, i.conversion, i.format_spec)


def example_03_plain_render_like_fstring():
    item, cost = "coffee", 3.456
    print(render(t"{item} costs {cost:.2f}"))


def example_04_html_escaping():
    user_input = "<script>alert('x')</script>"
    print(render(t"<p>Hello {user_input}</p>", transform=lambda v: html.escape(str(v))))


def example_05_sql_parameterisation():
    def sql(t: Template) -> tuple[str, list]:
        query, params = [], []
        for part in t:
            if isinstance(part, Interpolation):
                query.append("?"); params.append(part.value)
            else:
                query.append(part)
        return "".join(query), params
    name = "bob'; DROP TABLE users;--"
    q, p = sql(t"SELECT * FROM users WHERE name = {name}")
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users(name TEXT)")
    print(q, p, conn.execute(q, p).fetchall())


def example_06_shell_quoting():
    filename = "my file; rm -rf ~"
    print(render(t"ls -l {filename}", transform=lambda v: shlex.quote(str(v))))


def example_07_structured_logging():
    def log(t: Template) -> str:
        message = render(t)
        fields = {i.expression: i.value for i in t.interpolations}
        return json.dumps({"msg": message, **fields})
    user_id, action = 42, "login"
    print(log(t"user {user_id} did {action}"))


def example_08_concatenate_templates():
    a, b = 1, 2
    combined = t"a={a} " + t"b={b}"
    print(combined.values, render(combined))


def example_09_build_programmatically():
    t = Template("Total: ", Interpolation(99.5, "amount", None, ".1f"), " USD")
    print(render(t))


def example_10_conversions_are_left_to_you():
    def render_with_conv(t: Template) -> str:
        conv = {"r": repr, "s": str, "a": ascii, None: str}
        return "".join(p if isinstance(p, str) else conv[p.conversion](p.value) for p in t)
    word = "café"
    print(render_with_conv(t"{word!r} {word!a} {word}"))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
