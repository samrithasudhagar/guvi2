n,k=map(int,input().split())
l=[]
for i in range(n):
    l.append(input())
for i in l:
    if l.count(i)==k:
        c=0
        break
    else:
        c=1
if c==0:
    print("yes")
else:
    print("no")
