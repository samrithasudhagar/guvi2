n=int(input())
p=[]
for i in range(n):
    p.append(list(map(int,input().split())))
s=0
k=0
j=n-1
for i in range(n):
    s=s+p[i][i]
    k=k+p[i][j]
    j=j-1
print(s*k)
        
