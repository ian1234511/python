c = int(input())

for X in range(c):
    a = list(map(int, input().split()))
    
    F = a[0]   
    C = a[0]   
    
    for i in range(1, len(a)):
        C = max(a[i], C + a[i])
        F = max(F, C)
    
    print(F)
