n=int(input())
l=list(map(int,input().split()))
m=0
for i in range(n):
    k=l[:i]+l[i+1:]
    if sum(k)>m:
        m=sum(k)
print(m) 
