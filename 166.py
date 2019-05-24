a,b=map(int,input().split())
k=min(a,b)
v=1
for i in range(1,k+1):
    v=v*i
print(v)
