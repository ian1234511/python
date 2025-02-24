def is_palindrome(n):
    return str(n) == str(n)[::-1]

n = int(input())
for _ in range(n):
    num = int(input())
    while not is_palindrome(num):
        num += int(str(num)[::-1])
    print(num)
