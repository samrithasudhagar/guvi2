n=int(input())
a=[]
for i in range(n):
    a.append(input())
if all("a" in i or "o" in i or "i" in i or "e" in i or "u" in i for i in a):
    print("yes")
else:
    print("no")
