#!/usr/bin/env python3


def fib(n: int):
    """returns the Nth fibonacci sequence number

    Usage:

        >>> fib(8)
        21

        >>> fib(123)
        22698374052006863956975682
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    p_prev = 0
    prev = 1
    cur = 1
    for _ in range(n - 1):
        cur = p_prev + prev
        p_prev = prev
        prev = cur
    return cur


if __name__ == "__main__":
    import doctest

    doctest.testmod()
