import math

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

d = int(input())
for _ in range(d):
    d = int(input())
    print("Y" if is_prime(d) else "N")
