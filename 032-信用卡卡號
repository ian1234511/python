n = int(input())
for i in range(n):
    a = input().strip()
    s = 0
    for i in range(len(a)):
        d = int(a[-(i+1)])
        if i % 2 == 1:
            d *= 2
            if d >= 10:
                d -= 9
        s += d
    if s % 10 == 0:
        print("T")
    else:
        print("F")
