n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    print(nums[0], nums[1])
