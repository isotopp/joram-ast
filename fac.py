#! /usr/bin/env python

# Fakultät berechnen
#
# n! = fac(n) = 1 * 2 * 3 * ... * n
#
# fac(5) =
#   1 * 2 * 3 * 4 * 5 =
#   1 * 2 * 3 * (20) =
#   1 * 2 * (60) =
#   1 * (120) = 120

def fac(n: int) -> int:
    print(f"Call to fac({n})")
    if n < 1:
        raise ValueError(f"n={n} must be greater than or equal to 1")

    if n == 1:
        return 1

    return n * fac(n - 1)


if __name__ == "__main__":
    print(fac(5))
