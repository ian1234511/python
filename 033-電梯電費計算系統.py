n = int(input())
for _ in range(n):
    _ = input()
    floors = list(map(int, input().split(",")))
    total_cost = 0
    for i in range(len(floors) - 1):
        if floors[i + 1] > floors[i]:  
            total_cost += (floors[i + 1] - floors[i]) * 20
        else:
            total_cost += (floors[i] - floors[i + 1]) * 10

    print(total_cost)
