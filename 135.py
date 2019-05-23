n=int(input())
l=list(map(int,input().split()))
if n%2==0:
    u=n//2
else:
    u=(n-1)//2
if len(l)==1:
    print(*l)
else:
    k=l[:u]
    i=l[u:]
    k.sort()
    i.sort(reverse=True)
    print(*k,end=" ")
    print(*i)
