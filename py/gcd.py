#!/usr/bin/env python3


def gcd(a: int, b: int):
    """greatest common denominator

    Usage:

        >>> gcd(12, 8)
        4

        >>> gcd(12345, 9876)
        2469
    """
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
