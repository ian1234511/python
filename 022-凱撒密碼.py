x=int(input())
for i in range(x):
    a,b=input().split()
    for d in a:
        c=(ord(d)-ord('A')+int(b))%26+ord('A')
        print(chr(c),end="")
    print()
