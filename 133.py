n,k=map(int,input().split())
l=[]
c=0
for i in range(n):
    o=list(map(int,input().split()))
    l.append(o)
p=len(o)
for i in range(n):
    for j in range(p-1):
        pp=l[i][j]
        if pp<=k and l[i][j+1]>=k:
            c=c+1
            break
        else:
            c=0
if c==0:
    print("no")
else:
    print("yes")
