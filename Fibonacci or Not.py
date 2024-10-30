import math

def is_fibonacci(n):
    return any(math.isqrt(5 * n * n + k) ** 2 == 5 * n * n + k for k in [4, -4])

n = int(input().strip())
print(is_fibonacci(n))
