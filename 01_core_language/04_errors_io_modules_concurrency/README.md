# Core Language · Errors, Resources, Modules, I/O and Concurrency
Exceptions, context managers, modules and packages, files and serialisation, and
concurrency with threads, processes and asyncio, all in today's idioms.

| # | Feature | In one line |
|---|---|---|
| 01 | [Exceptions: try / except / else / finally, raise, custom errors](01_exceptions/README.md) | signal and handle errors explicitly; catch specific exceptions, clean up in `finally`. |
| 02 | [Context managers: the `with` statement and contextlib](02_context_managers/README.md) | guarantee setup and cleanup (close files, release locks, roll back transactions) even when errors happen. |
| 03 | [Modules, packages and imports](03_modules_and_packages/README.md) | organise code into files (modules) and folders (packages) and import what you need. |
| 04 | [File I/O and serialisation (pathlib, open, json, csv, pickle)](04_file_io_and_serialization/README.md) | read and write text, binary, JSON, CSV and Python objects safely and portably. |
| 05 | [Concurrency: threads, processes and asyncio](05_concurrency_threads_processes_async/README.md) | run work concurrently — threads for I/O, processes (or free-threaded builds) for CPU, asyncio for massive I/O concurrency. |

Run every example in this folder:
```bash
python ../../run_examples.py 01_core_language/04_errors_io_modules_concurrency
```
