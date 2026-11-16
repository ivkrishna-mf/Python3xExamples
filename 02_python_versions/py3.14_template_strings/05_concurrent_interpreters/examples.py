"""concurrent.interpreters & InterpreterPoolExecutor — Python 3.14+ (PEP 734)."""
from concurrent import interpreters
from concurrent.futures import InterpreterPoolExecutor

MIN_VERSION = (3, 14)


def cpu_task(n):
    return sum(i * i for i in range(n))


def example_01_create_and_exec():
    interp = interpreters.create()
    interp.exec("print('  hello from interpreter', __import__('sys').implementation.name)")
    interp.close()


def example_02_call_a_function():
    interp = interpreters.create()
    print(interp.call(cpu_task, 1000))
    interp.close()


def example_03_isolated_state():
    interp = interpreters.create()
    interp.exec("x = 'only in sub-interpreter'")
    print("main has x:", "x" in globals())
    interp.exec("print('  sub has x:', x)")
    interp.close()


def example_04_list_interpreters():
    a, b = interpreters.create(), interpreters.create()
    print("ids:", [i.id for i in interpreters.list_all()])
    a.close(); b.close()


def example_05_main_and_current():
    print(interpreters.get_main().id, interpreters.get_current().id)


def example_06_queue_communication():
    q = interpreters.create_queue()
    interp = interpreters.create()
    interp.prepare_main(q=q)
    interp.exec("q.put('message from sub')")
    print(q.get())
    interp.close()


def example_07_pool_executor():
    with InterpreterPoolExecutor(max_workers=2) as ex:
        print(list(ex.map(cpu_task, [10, 100, 1000])))


def example_08_errors_propagate():
    interp = interpreters.create()
    try:
        interp.exec("raise ValueError('inside')")
    except interpreters.ExecutionFailed as exc:
        print("ExecutionFailed:", exc.excinfo.type.__name__, exc.excinfo.msg)
    interp.close()


def example_09_run_in_thread():
    interp = interpreters.create()
    t = interp.call_in_thread(cpu_task, 10_000)
    t.join()
    print("thread finished:", not t.is_alive())
    interp.close()


def example_10_context_manager_cleanup():
    interp = interpreters.create()
    try:
        interp.prepare_main(greeting="hi")
        interp.exec("print('  ', greeting, 'from', __name__)")
    finally:
        interp.close()
    print("closed; remaining interpreters:", [i.id for i in interpreters.list_all()])


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("example_"):
            print(f"\n--- {_name} ---")
            _fn()
