n,k=map(int,input().split())
s=list(map(int,input().split()))
k=int(k)
a=s[:k]
b=s[k:]
a.sort()
b.sort(reverse=True)
print(*a,*b)
