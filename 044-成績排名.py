q = int(input())
w = []
for k in range(q):
    e = list(map(int, input().split()))
    w.append(e)
for a in range(q - 1):
    for s in range(q - 1 - a):
        t, y = w[s], w[s + 1]
        if (t[1] < y[1]) or (t[1] == y[1] and t[2] < y[2]) or (t[1] == y[1] and t[2] == y[2] and t[0] > y[0]):
            w[s], w[s + 1] = w[s + 1], w[s]
for u in w:
    print(u[0], u[1], u[2])
