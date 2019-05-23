n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    if sum(l[:i+1])%2==0:
        a.append(sum(l[:i+1]))
    else:
        a.append(l[i])
print(*a)
