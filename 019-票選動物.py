a = [input().strip() for _ in range(9)]
t = a.count("Tiger")
l = a.count("Lion")
print("Tiger" if t > l else "Lion")
