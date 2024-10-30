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

def is_mega_prime(n):
    if not is_prime(n):
        return False
    prime_digits = {'2', '3', '5', '7'}
    return all(digit in prime_digits for digit in str(n))

n = int(input().strip())
print("Mega Prime" if is_mega_prime(n) else "Not Mega Prime")
