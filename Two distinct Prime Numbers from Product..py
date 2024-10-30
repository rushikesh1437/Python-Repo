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

def find_prime_pair(n):
    for i in range(2, n):
        if is_prime(i) and n % i == 0:
            other = n // i
            if is_prime(other) and i != other:
                return i, other
    return -1

n = int(input().strip())
result = find_prime_pair(n)
print(result if result == -1 else f"{result[0]} {result[1]}")
