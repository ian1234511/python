d = int(input())
for _ in range(d):
    k = input().strip()
    j = 0
    l = 0
    for char in k:
        if char == 'O':
            l += 1
            j += l
        else:
            l = 0
    print(j)
