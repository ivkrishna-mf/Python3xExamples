"""Exception notes — Python 3.11+ (PEP 678)."""
import traceback

MIN_VERSION = (3, 11)


def example_01_add_a_note():
    try:
        e = ValueError("invalid literal")
        e.add_note("hint: check the 'age' column")
        raise e
    except ValueError as exc:
        print(exc, exc.__notes__)


def example_02_notes_appear_in_traceback():
    try:
        try:
            int("x")
        except ValueError as exc:
            exc.add_note("while parsing config key 'port'")
            raise
    except ValueError:
        print(traceback.format_exc().strip().splitlines()[-2:])


def example_03_row_context_while_importing():
    rows = ["1", "2", "three", "4"]
    try:
        for i, r in enumerate(rows, start=1):
            try:
                int(r)
            except ValueError as exc:
                exc.add_note(f"row {i}: {r!r}")
                raise
    except ValueError as exc:
        print(exc.__notes__)


def example_04_multiple_notes_as_it_bubbles():
    def parse(v):
        try:
            return int(v)
        except ValueError as e:
            e.add_note("in parse()")
            raise
    def load(v):
        try:
            return parse(v)
        except ValueError as e:
            e.add_note("in load()")
            raise
    try:
        load("NaN!")
    except ValueError as e:
        print(e.__notes__)


def example_05_retry_attempt_context():
    last = None
    for attempt in range(1, 4):
        try:
            raise TimeoutError("upstream slow")
        except TimeoutError as exc:
            exc.add_note(f"attempt {attempt}")
            last = exc
    print(last, last.__notes__)


def example_06_note_must_be_str():
    try:
        ValueError().add_note(123)
    except TypeError as exc:
        print("TypeError:", exc)


def example_07_with_exception_groups():
    errs = []
    for name in ["a.csv", "b.csv"]:
        e = FileNotFoundError(name)
        e.add_note(f"expected in ./data/{name}")
        errs.append(e)
    try:
        raise ExceptionGroup("missing inputs", errs)
    except* FileNotFoundError as eg:
        print([e.__notes__[0] for e in eg.exceptions])


def example_08_request_id_note():
    request_id = "req-9f2"
    try:
        try:
            {}["user"]
        except KeyError as exc:
            exc.add_note(f"request_id={request_id}")
            raise
    except KeyError as exc:
        print(repr(exc), exc.__notes__)


def example_09_no_notes_attribute_by_default():
    print(hasattr(ValueError(), "__notes__"))


def example_10_helper_context_manager():
    from contextlib import contextmanager
    @contextmanager
    def note(msg):
        try:
            yield
        except Exception as exc:
            exc.add_note(msg)
            raise
    try:
        with note("step: transform"), note("pipeline: nightly"):
            1 / 0
    except ZeroDivisionError as e:
        print(e.__notes__)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
