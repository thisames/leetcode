x = int(input())

from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(x):
    n = int(input())
    print(f"Fib({n}) = {fibonacci(n)}")

# 0 1 1 2 3 5 8 13
