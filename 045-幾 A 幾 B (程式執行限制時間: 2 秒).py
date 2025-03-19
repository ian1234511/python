n = int(input().strip())
for _ in range(n):
    j, k = input().strip().split(", ")
    A = sum(1 for x, y in zip(j, k) if x == y)
    B = 0
    for d in set(j):
        B += min(j.count(d), k.count(d))
    B -= A
    print(f"{A}A{B}B")
