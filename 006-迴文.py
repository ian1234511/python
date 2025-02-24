S = input()

if S == S[::-1]:
    print(S)
else:
    print(S[::-1] + S)
