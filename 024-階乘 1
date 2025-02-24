n = int(input())
for _ in range(n):
    x = int(input())
    sum_factorial = 0
    factorial = 1
    for i in range(1, x + 1):
        factorial = (factorial * i) % 1000000
        sum_factorial = (sum_factorial + factorial) % 1000000
    print(f"{sum_factorial:06d}")
