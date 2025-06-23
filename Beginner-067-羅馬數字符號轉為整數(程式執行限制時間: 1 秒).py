a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
q = int(input())
for h in range(q):
    w = input()
    e = 0
    i = 0
    while i < len(w):
        if i + 1 < len(w) and a[w[i]] < a[w[i+1]]:
            e += a[w[i+1]] - a[w[i]]
            i += 2
        else:
            e += a[w[i]]
            i += 1
    print(e)
