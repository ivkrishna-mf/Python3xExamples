"""f-string grammar (PEP 701) — Python 3.12+."""
MIN_VERSION = (3, 12)
user = {"name": "ann", "roles": ["admin", "dev"]}
lines = ["alpha", "beta", "gamma"]


def example_01_reuse_same_quotes():
    print(f"user: {user["name"]}")


def example_02_backslash_in_expression():
    print(f"{'\n'.join(lines)}")


def example_03_join_with_tab():
    print(f"{"\t".join(lines)}")


def example_04_multiline_with_comments():
    total = 1234.5
    print(f"Total: {
        total        # the amount
        * 1.18       # plus 18% tax
        :,.2f}")


def example_05_nested_same_quotes():
    print(f"{f"{f"{1 + 1}"}"}")


def example_06_dict_comprehension_inside():
    print(f"{ {k: len(v) for k, v in user.items() if k != "name"} }")


def example_07_unicode_escape_names():
    print(f"{"\N{SNAKE}"} python {"\N{SPARKLES}"}")


def example_08_conditional_with_quotes():
    n = 3
    print(f"{n} {"item" if n == 1 else "items"}")


def example_09_lambda_needs_parentheses():
    print(f"{(lambda x: x * 2)(21)}")


def example_10_debug_specifier_still_works():
    print(f"{user["roles"][0]=}")


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
