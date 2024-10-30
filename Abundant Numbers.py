def is_abundant(n):
    proper_factors_sum = sum(i for i in range(1, n // 2 + 1) if n % i == 0)
    return proper_factors_sum > n

n = int(input().strip())
print(is_abundant(n))
