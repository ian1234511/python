c=int(input())
for i in range(c):
    a,b=input().split(",")
    if a=='O' and b=='Y':
        print(1)
    elif a=='O' and b=='O':
        print(0)
    elif a=='O' and b=='P':
        print(2)
    elif a=='Y' and b=='Y':
        print(0)
    elif a=='Y' and b=='O':
        print(2)
    elif a=='Y' and b=='P':
        print(1)
    elif a=='P' and b=='P':
        print(0)
    elif a == 'P' and b == 'O':
        print(1)
    elif a=='P' and b=='Y':
        print(2)
