"""ExceptionGroup & except* — Python 3.11+ (PEP 654)."""
import asyncio

MIN_VERSION = (3, 11)


def example_01_raise_and_catch_group():
    try:
        raise ExceptionGroup("batch failed", [ValueError("bad id"), TypeError("bad type")])
    except ExceptionGroup as eg:
        print(eg, "->", [repr(e) for e in eg.exceptions])


def example_02_except_star_splits_by_type():
    try:
        raise ExceptionGroup("errors", [ValueError("v1"), TypeError("t1"), ValueError("v2")])
    except* ValueError as eg:
        print("ValueErrors:", [str(e) for e in eg.exceptions])
    except* TypeError as eg:
        print("TypeErrors:", [str(e) for e in eg.exceptions])


def example_03_unhandled_members_propagate():
    try:
        try:
            raise ExceptionGroup("mixed", [KeyError("k"), OSError("disk")])
        except* KeyError:
            print("handled KeyError")
    except ExceptionGroup as rest:
        print("still propagating:", [type(e).__name__ for e in rest.exceptions])


def example_04_validate_all_fields():
    def validate(user):
        errors = []
        if not user.get("name"):
            errors.append(ValueError("name is required"))
        if "@" not in user.get("email", ""):
            errors.append(ValueError("email is invalid"))
        if not isinstance(user.get("age"), int):
            errors.append(TypeError("age must be int"))
        if errors:
            raise ExceptionGroup("invalid user", errors)
    try:
        validate({"name": "", "email": "nope", "age": "x"})
    except* ValueError as eg:
        for e in eg.exceptions:
            print("value problem:", e)
    except* TypeError as eg:
        for e in eg.exceptions:
            print("type problem:", e)


def example_05_taskgroup_failures():
    async def job(n):
        await asyncio.sleep(0.01 * n)
        if n % 2:
            raise RuntimeError(f"job {n} failed")
        return n
    async def main():
        try:
            async with asyncio.TaskGroup() as tg:
                for n in range(1, 4):
                    tg.create_task(job(n))
        except* RuntimeError as eg:
            print("failed jobs:", sorted(str(e) for e in eg.exceptions))
    asyncio.run(main())


def example_06_subgroup_and_split():
    eg = ExceptionGroup("all", [ValueError(1), TypeError(2), ValueError(3)])
    match, rest = eg.split(ValueError)
    print(match.exceptions, rest.exceptions)
    print(eg.subgroup(lambda e: isinstance(e, TypeError)).exceptions)


def example_07_nested_groups():
    inner = ExceptionGroup("inner", [KeyError("a")])
    outer = ExceptionGroup("outer", [inner, ValueError("b")])
    try:
        raise outer
    except* KeyError as eg:
        print("found KeyError even when nested:", eg.exceptions)
    except* ValueError:
        print("and the ValueError")


def example_08_base_exception_group():
    try:
        raise BaseExceptionGroup("base", [KeyboardInterrupt(), ValueError()])
    except* KeyboardInterrupt:
        print("KeyboardInterrupt handled")
    except* ValueError:
        print("ValueError handled")


def example_09_cleanup_collects_errors():
    def close_all(resources):
        errors = []
        for r in resources:
            try:
                r()
            except Exception as exc:
                errors.append(exc)
        if errors:
            raise ExceptionGroup("cleanup errors", errors)
    def ok(): pass
    def bad_socket(): raise ConnectionError("socket already closed")
    def bad_file(): raise OSError("flush failed")
    try:
        close_all([ok, bad_socket, bad_file])
    except* OSError as eg:    # ConnectionError is a subclass of OSError
        print([str(e) for e in eg.exceptions])


def example_10_naked_exception_is_wrapped():
    try:
        raise ValueError("single")
    except* ValueError as eg:
        print(type(eg).__name__, eg.exceptions)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
