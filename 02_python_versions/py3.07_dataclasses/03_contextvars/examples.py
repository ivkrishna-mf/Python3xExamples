"""contextvars — Python 3.7+ (PEP 567)."""
import asyncio
import contextvars
import logging

MIN_VERSION = (3, 7)
request_id = contextvars.ContextVar("request_id", default="-")


def example_01_get_set_default():
    print(request_id.get())
    request_id.set("abc")
    print(request_id.get())


def example_02_token_reset():
    token = request_id.set("temp")
    print(request_id.get())
    request_id.reset(token)
    print(request_id.get())


def example_03_isolated_per_task():
    async def handle(rid):
        request_id.set(rid)
        await asyncio.sleep(0.01)
        return f"task sees {request_id.get()}"
    async def main():
        print(await asyncio.gather(handle("r1"), handle("r2"), handle("r3")))
    asyncio.run(main())


def example_04_copy_context_and_run():
    ctx = contextvars.copy_context()
    def inside():
        request_id.set("only-in-copy")
        return request_id.get()
    print(ctx.run(inside), "| outside:", request_id.get())


def example_05_logging_filter():
    class RequestIdFilter(logging.Filter):
        def filter(self, record):
            record.rid = request_id.get()
            return True
    log = logging.getLogger("ctxdemo")
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("[%(rid)s] %(message)s"))
    handler.addFilter(RequestIdFilter())
    log.addHandler(handler); log.setLevel(logging.INFO); log.propagate = False
    async def handle(rid):
        request_id.set(rid)
        log.info("handling request")
    async def main():
        await asyncio.gather(handle("req-1"), handle("req-2"))
    asyncio.run(main())


def example_06_context_manager_helper():
    from contextlib import contextmanager
    user = contextvars.ContextVar("user", default="anonymous")
    @contextmanager
    def as_user(name):
        token = user.set(name)
        try:
            yield
        finally:
            user.reset(token)
    with as_user("admin"):
        print("inside:", user.get())
    print("after:", user.get())


def example_07_context_is_a_mapping():
    ctx = contextvars.copy_context()
    print(request_id in ctx, len(list(ctx.items())) >= 1)


def example_08_child_task_inherits_parent_value():
    async def child():
        return request_id.get()
    async def main():
        request_id.set("parent-value")
        print(await asyncio.create_task(child()))
    asyncio.run(main())


def example_09_threads_with_context():
    from concurrent.futures import ThreadPoolExecutor
    request_id.set("main-thread")
    ctx = contextvars.copy_context()
    with ThreadPoolExecutor() as ex:
        print(ex.submit(ctx.run, request_id.get).result())


def example_10_lookup_error_without_default():
    tenant = contextvars.ContextVar("tenant")
    try:
        tenant.get()
    except LookupError:
        print("LookupError -> no default; use tenant.get('fallback')", tenant.get("fallback"))


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
