s = input()
h = {'a', 'e', 'i', 'o', 'u'}
g = False
for t in s:
    if t in h:
        g = True
        break
print(g)
