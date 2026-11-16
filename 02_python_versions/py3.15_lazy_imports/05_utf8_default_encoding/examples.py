"""UTF-8 default encoding — Python 3.15+ (PEP 686)."""
import io
import locale
import subprocess
import sys
import tempfile
from pathlib import Path

MIN_VERSION = (3, 15)
TMP = Path(tempfile.mkdtemp())


def example_01_utf8_mode_flag():
    print("sys.flags.utf8_mode =", sys.flags.utf8_mode)


def example_02_default_open_encoding():
    with open(TMP / "a.txt", "w") as fh:
        print("open() default encoding:", fh.encoding)


def example_03_round_trip_non_ascii():
    p = TMP / "names.txt"
    p.write_text("José, Zoë, 東京, नमस्ते")      # no encoding= needed on 3.15
    print(p.read_text(), "|", len(p.read_bytes()), "bytes")


def example_04_locale_encoding_still_available():
    print("locale encoding:", locale.getencoding())
    with open(TMP / "legacy.txt", "w", encoding="locale") as fh:
        print("encoding='locale' ->", fh.encoding)


def example_05_stdout_encoding():
    print("stdout:", sys.stdout.encoding)


def example_06_text_io_wrapper_default():
    print(io.TextIOWrapper(io.BytesIO()).encoding)


def example_07_subprocess_text_mode():
    out = subprocess.run([sys.executable, "-c", "print('ñandú')"], capture_output=True, text=True)
    print(out.stdout.strip())


def example_08_portable_code_is_explicit():
    p = TMP / "portable.txt"
    p.write_text("café", encoding="utf-8")        # same result on every Python version
    print(p.read_text(encoding="utf-8"))


def example_09_legacy_file_explicit_encoding():
    p = TMP / "cp1252.txt"
    p.write_bytes("café".encode("cp1252"))
    print(p.read_text(encoding="cp1252"), "| as utf-8 w/ replace:", p.read_text(errors="replace"))


def example_10_opt_out_child_process():
    out = subprocess.run([sys.executable, "-X", "utf8=0", "-c", "import sys; print(sys.flags.utf8_mode)"],
                         capture_output=True, text=True)
    print("child with -X utf8=0 -> utf8_mode =", out.stdout.strip())


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
