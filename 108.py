n=int(input())
s=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append(sum(s[:i+1]))
print(*a)
