"""zoneinfo — Python 3.9+ (PEP 615). On Windows: pip install tzdata."""
from datetime import datetime, timedelta, timezone

MIN_VERSION = (3, 9)
try:
    from zoneinfo import ZoneInfo, available_timezones
    ZoneInfo("UTC")
    HAVE_TZ = True
except Exception:
    HAVE_TZ = False


def needs_tz(fn):
    def wrapper():
        if not HAVE_TZ:
            print("tz database not found — pip install tzdata")
            return
        fn()
    wrapper.__name__ = fn.__name__
    return wrapper


@needs_tz
def example_01_aware_datetime():
    dt = datetime(2026, 11, 16, 9, 0, tzinfo=ZoneInfo("Asia/Kolkata"))
    print(dt, dt.tzname())


@needs_tz
def example_02_convert_between_zones():
    meeting = datetime(2026, 11, 16, 15, 0, tzinfo=ZoneInfo("America/New_York"))
    for tz in ("Europe/London", "Asia/Kolkata", "Asia/Tokyo"):
        print(f"{tz:16} {meeting.astimezone(ZoneInfo(tz)):%Y-%m-%d %H:%M}")


@needs_tz
def example_03_now_in_a_zone():
    print(datetime.now(ZoneInfo("Europe/Berlin")).strftime("%H:%M %Z"))


@needs_tz
def example_04_dst_transition():
    tz = ZoneInfo("America/New_York")
    before = datetime(2026, 3, 8, 1, 30, tzinfo=tz)
    after = (before.astimezone(timezone.utc) + timedelta(hours=1)).astimezone(tz)
    print(before, "->", after, "(clocks jumped)")


@needs_tz
def example_05_utc_offset():
    for tz in ("UTC", "Asia/Kolkata", "Australia/Adelaide"):
        print(tz, datetime(2026, 1, 1, tzinfo=ZoneInfo(tz)).utcoffset())


@needs_tz
def example_06_store_utc_display_local():
    stored = datetime(2026, 11, 16, 3, 30, tzinfo=timezone.utc)
    print("stored:", stored.isoformat(), "| shown:", stored.astimezone(ZoneInfo("Asia/Kolkata")).isoformat())


@needs_tz
def example_07_parse_iso_and_attach_zone():
    naive = datetime.fromisoformat("2026-11-16T18:00")
    print(naive.replace(tzinfo=ZoneInfo("Europe/Paris")).isoformat())


@needs_tz
def example_08_list_some_zones():
    zones = sorted(z for z in available_timezones() if z.startswith("Asia/K"))
    print(zones[:6])


@needs_tz
def example_09_ambiguous_time_fold():
    tz = ZoneInfo("America/New_York")
    first = datetime(2026, 11, 1, 1, 30, tzinfo=tz)
    second = first.replace(fold=1)
    print(first.tzname(), second.tzname())


@needs_tz
def example_10_comparing_aware_datetimes():
    a = datetime(2026, 1, 1, 12, tzinfo=ZoneInfo("Europe/London"))
    b = datetime(2026, 1, 1, 17, 30, tzinfo=ZoneInfo("Asia/Kolkata"))
    print("same instant:", a == b)


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
