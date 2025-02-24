def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1
n = int(input())
for _ in range(n):
    s0 = int(input())
    if is_happy_number(s0):
        print("T")
    else:
        print("F")
