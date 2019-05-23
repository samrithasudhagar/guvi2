n,k=map(int,input().split())
a=[]
c=0
for i in range(n):
    a.append(input())
p=["a","e","i","o","u"]
for i in a:
    if any(j in i for j in p):
        c=c+1
if c>=k:
    print("yes")
else:
    print("no")
