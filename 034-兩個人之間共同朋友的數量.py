for i in range(int(input())):
    a = set((list(map(int, input().split())))[1::])
    b = set((list(map(int, input().split())))[1::])
    print(len(a & b))
