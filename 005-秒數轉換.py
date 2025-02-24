a=int(input())
s=a%60
m=a%(60*60)//60
h=a%(24*60*60)//3600
d=a//(24*60*60)
print(f"{d}D{h}H{m}M{s}s")
