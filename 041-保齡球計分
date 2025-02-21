def calculate_score(m):
    a = 0
    s = 0
    for d in range(10):
        if m[s] == 'X':
            a += 10 + get_next_two_rolls(m, s)
            s += 1
        elif m[s + 1] == '/':
            a += 10 + get_next_roll(m, s)
            s += 2
        else:
            a += int(m[s]) + int(m[s + 1])
            s += 2
    return a

def get_next_two_rolls(m, z):
    if m[z + 1] == 'X':
        return 10 + g(m, z + 2)
    elif m[z + 1] == '/':
        return 10
    else:
        return g(m, z + 1) + g(m, z + 2)

def get_next_roll(m, z):
    return g(m, z + 2)

def g(m, z):
    if m[z] == 'X':
        return 10
    elif m[z] == '/':
        return 10 - int(m[z - 1])
    else:
        return int(m[z])

n = int(input())
for r in range(n):
    m = input().split()
    x = calculate_score(m)
    print(x)
