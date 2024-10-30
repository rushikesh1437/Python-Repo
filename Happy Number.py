def is_happy(n):
    def sum_of_squares(num):
        return sum(int(digit) ** 2 for digit in str(num))
    
    seen = set()
    while n != 1 and n != 7:
        if n in seen:
            return False
        seen.add(n)
        n = sum_of_squares(n)
    return True

n = int(input().strip())
print(is_happy(n))
