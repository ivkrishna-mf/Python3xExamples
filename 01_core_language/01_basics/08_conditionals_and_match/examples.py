"""Conditionals & match — modern style (3.10+)."""
MIN_VERSION = (3, 10)


def example_01_if_elif_else():
    for t in (-5, 12, 30):
        if t < 0:
            label = "freezing"
        elif t < 25:
            label = "mild"
        else:
            label = "hot"
        print(t, label)


def example_02_chained_comparisons():
    x = 7
    print(0 < x < 10, 1 <= x <= 5)


def example_03_conditional_expression():
    n = 3
    print(f"{n} {'item' if n == 1 else 'items'}")


def example_04_and_or_return_operands():
    name = "" or "anonymous"
    port = None or 8080
    print(name, port, 0 and "never", "a" and "b")


def example_05_guard_clauses():
    def withdraw(balance: float, amount: float) -> float:
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > balance:
            raise ValueError("insufficient funds")
        return balance - amount
    print(withdraw(100, 30))


def example_06_membership_conditions():
    ext = "png"
    if ext in {"png", "jpg", "gif"}:
        print("image")


def example_07_any_all():
    nums = [2, 4, 6]
    print(all(n % 2 == 0 for n in nums), any(n > 5 for n in nums))


def example_08_match_literals():
    def http(code: int) -> str:
        match code:
            case 200 | 201 | 204:
                return "ok"
            case 301 | 302:
                return "redirect"
            case c if 400 <= c < 500:
                return "client error"
            case _:
                return "server error"
    print([http(c) for c in (201, 302, 404, 503)])


def example_09_match_shapes():
    def describe(event: dict) -> str:
        match event:
            case {"type": "order", "items": [first, *rest]}:
                return f"order: {first} + {len(rest)} more"
            case {"type": "refund", "amount": float(a) | int(a)}:
                return f"refund {a}"
            case _:
                return "unknown"
    print(describe({"type": "order", "items": ["pen", "ink", "pad"]}), describe({"type": "refund", "amount": 9.5}))


def example_10_dispatch_table_instead_of_if_chain():
    ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b}
    print(ops["*"](6, 7), ops.get("^", lambda a, b: "unsupported")(1, 2))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
