n = int(input())

for _ in range(n):
    N = input()
    A, B = "", ""

    for digit in N:
        if digit == "4":
            A += "3"
            B += "1"
        else:
            A += digit
            B += "0"

    print(int(A), int(B))
