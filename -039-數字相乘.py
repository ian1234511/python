n = int(input())

for _ in range(n):
    N = int(input())
    if N == 1:
        print(1)
        continue

    factors = []
    for digit in range(9, 1, -1):
        while N % digit == 0:
            factors.append(digit)
            N //= digit

    if N > 1:
        print(-1)
    else:
        factors.sort()
        print("".join(map(str, factors)))
