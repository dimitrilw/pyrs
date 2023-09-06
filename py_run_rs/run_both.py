# cSpell:ignore pyfib, pygcd, rustimport, rustfib, rustgcd

from timeit import timeit

import pyfib
import pygcd

# ==================================================================================================
# rust import stuff
import rustimport.import_hook

# these next two lines set rustimport to compile release binaries;
# i.e., the compile time is longer, but the runtime is faster
import rustimport.settings

rustimport.settings.compile_release_binaries = True

import rustfib
import rustgcd

# ==================================================================================================


def run_py():
    a = pyfib.fib(111)
    b = pygcd.gcd(a, 123456789)

    x = pyfib.fib(123)
    y = pygcd.gcd(x, 987654321)


def run_rs():
    a = rustfib.fib(111)
    b = rustgcd.gcd(a, 123456789)

    x = rustfib.fib(123)
    y = rustgcd.gcd(x, 987654321)


if __name__ == "__main__":
    py_res = timeit(lambda: run_py())
    print(f"{py_res=}")

    rs_res = timeit(lambda: run_rs())
    print(f"{rs_res=}")
