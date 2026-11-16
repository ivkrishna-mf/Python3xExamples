"""Walrus operator := — Python 3.8+ (PEP 572)."""
import io
import re

MIN_VERSION = (3, 8)


def example_01_if_with_assignment():
    data = list(range(15))
    if (n := len(data)) > 10:
        print(f"list too long ({n} items)")


def example_02_while_read_loop():
    stream = io.StringIO("abcdefghij")
    while chunk := stream.read(4):
        print(repr(chunk))


def example_03_regex_match():
    for line in ["user=ann", "garbage", "user=bob"]:
        if m := re.match(r"user=(\w+)", line):
            print("found", m.group(1))


def example_04_comprehension_reuse_value():
    def expensive(x):
        return x * x - 10
    print([y for x in range(6) if (y := expensive(x)) > 0])


def example_05_input_loop_simulated():
    commands = iter(["ls", "pwd", "quit", "never"])
    while (cmd := next(commands)) != "quit":
        print("running", cmd)


def example_06_capture_last_matching_item():
    nums = [3, 8, 12, 5]
    if any((big := n) > 10 for n in nums):
        print("first big number:", big)


def example_07_dict_get_and_use():
    config = {"timeout": "30"}
    if (t := config.get("timeout")) is not None:
        print("timeout seconds:", int(t))


def example_08_running_total():
    total = 0
    print([total := total + x for x in [1, 2, 3, 4]])


def example_09_avoid_double_computation():
    words = ["python", "is", "fun", "!"]
    print({w: n for w in words if (n := len(w)) > 2})


def example_10_queue_drain():
    queue = [1, 2, 3]
    while queue and (item := queue.pop(0)):
        print("processed", item)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
