a = {
    'A': (1, 0), 'B': (1, 1), 'C': (1, 2), 'D': (1, 3), 'E': (1, 4), 'F': (1, 5), 'G': (1, 6), 'H': (1, 7), 'I': (3, 4), 
    'J': (1, 8), 'K': (1, 9), 'L': (2, 0), 'M': (2, 1), 'N': (2, 2), 'O': (3, 5), 'P': (2, 3), 'Q': (2, 4), 'R': (2, 5), 
    'S': (2, 6), 'T': (2, 7), 'U': (2, 8), 'V': (2, 9), 'W': (3, 2), 'X': (3, 0), 'Y': (3, 1), 'Z': (3, 3)
}
l = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
s = int(input())
for _ in range(s):
    f = input().strip()
    if len(f) != 10 or f[0] not in a or not f[1:].isdigit():
        print("F")
        continue
    g, h = a[f[0]]  
    k = [g, h] + [int(x) for x in f[1:]]
    if k[2] not in (1, 2):
        print("F")
        continue
    z = sum(j * w for j, w in zip(k, l))
    print("T" if z % 10 == 0 else "F")
