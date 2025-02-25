a=int(input())
for i in range(1,a+1):
    for s in range(1,i+1):
        print(s,end=" ")
    print()
print()
for i in range(a,0,-1):
    for s in range(1,i+1):
        print(s,end=" ")
    print()
print()
for i in range(a+1):
    for s in range(a,i,-1):
        print(s,end=" ")
    print()
print()
for i in range(a,0,-1):
    print("  "*(i-1),end="")
    for s in range(1, a - i + 2, 1):
        print(s, end=" ")
    print()
print()
