a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d =  b ** 2 - 4 * a * c
if d== 0:
    print(f"DR={-b / (2 * a)}")
elif d< 0:
    print("NoSolution")
else:
    s = d ** 0.5
    e1 = (-b - s) / (2 * a)
    e2 = (-b + s) / (2 * a)
    if e2 < e1:
        e1, e2 = e2, e1
    print(f"{e1} {e2}")

