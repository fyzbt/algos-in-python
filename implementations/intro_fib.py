from functools import lru_cache


def memo(f):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner


@memo
def fib(n):
    assert n >= 0
    return n if n <= 1 else fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=None)  # maxsize=None for caching all the values
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


print(fib(80), fib1(80))

# iteration instead of recursion


def fib2(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


print(fib2(500))
