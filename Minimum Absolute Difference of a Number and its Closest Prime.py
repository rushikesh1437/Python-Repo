def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def closest_prime_difference(n):
    if is_prime(n):
        return 0
    lower, upper = n - 1, n + 1
    while True:
        if is_prime(lower):
            return n - lower
        if is_prime(upper):
            return upper - n
        lower -= 1
        upper += 1

n = int(input().strip())
print(closest_prime_difference(n))
