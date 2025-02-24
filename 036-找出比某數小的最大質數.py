def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

for _ in range(n):
    x = int(input())
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            print(i)
            break
