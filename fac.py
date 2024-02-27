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
    # print(f"Call to fac({n})")
    if n < 1:
        raise ValueError(f"n={n} must be greater than or equal to 1")

    if n == 1:
        return 1

    return n * fac(n - 1)


def fac_depth(n: int, depth: int = 0) -> int:
    # sp = '  ' * depth
    # print(f"{sp}Call to fac_depth({n=}, {depth=})")
    if n < 1:
        raise ValueError(f"n={n} must be greater than or equal to 1")

    if n == 1:
        # print(f"{sp}return 1")
        return 1

    # r = n * fac_depth(n - 1, depth + 1)
    # print(f"{sp}return {r}")
    return n * fac_depth(n - 1, depth + 1)


def fac_tr(n, akku=1, depth=0):
    # sp = '  ' * depth
    # print(f"{sp}Call to fac_tr({n=}, {akku=}, {depth=})")
    if n < 1:
        raise ValueError(f"n={n} must be greater than or equal")

    if n == 1:
        # print(f"{sp}return 1")
        return akku
    else:
        # r = fac_tr(n - 1, n * akku, depth + 1)
        # print(f"{sp}return {r} = fac_tr({n=}, {akku=}, {depth=}")
        return fac_tr(n - 1, n * akku, depth + 1)


def fac_i(n):
    akku = 1
    for i in range(1, n + 1):
        akku *= i
    return akku


if __name__ == "__main__":
    print(fac(5))
    print(fac_depth(5))
    print(fac_tr(5))
    print(fac_i(5))
