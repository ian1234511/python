def get_type(s):
    if all(c == '0' for c in s):
        return 'B'
    elif all(c == '1' for c in s):
        return 'I'
    else:
        return 'F'

def build_fbi_tree(s):
    if len(s) == 1:
        return get_type(s)
    mid = len(s) // 2
    left = build_fbi_tree(s[:mid])
    right = build_fbi_tree(s[mid:])
    root = get_type(s)
    return left + right + root

# 讀取輸入
n = int(input())
s = input()

# 輸出後序遍歷
print(build_fbi_tree(s))
