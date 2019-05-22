n=int(input())
s=list(map(int,input().split()))
a=[]
for i in range(n):
    b=sum(s[i:])
    k=sum(s[:i+1])
    a.append(b+k)
print(*a)
