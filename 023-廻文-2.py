def is_palindrome(s):
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]

n = int(input())
for _ in range(n):
    s = input().strip()
    if is_palindrome(s):
        print("Y")
    else:
        print("N")
