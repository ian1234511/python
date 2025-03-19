n = int(input())
for _ in range(n):
    s = input()
    q = s.find(",")
    j = s[:q]
    k = s[q + 2:]
    A = 0
    for i in range(len(j)):
        if j[i] == k[i]:
            A += 1
    B = 0
    for d in set(j):
        B += min(j.count(d), k.count(d))
    B -= A
    print(f"{A}A{B}B")
