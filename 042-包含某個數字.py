n = int(input())
for _ in range(n):
    A, B, N = map(int, input().split())
    count = 0
    for i in range(A, B + 1):
        if str(N) in str(i):
            count += 1
    print(count)
