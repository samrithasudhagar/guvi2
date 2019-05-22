n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    for j in range(n,n+k):
        if l[i]==l[j]:
            if l[i] not in a:
                a.append(l[i])
a.sort()
print(*a)
         
