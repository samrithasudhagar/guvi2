n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(i+1,n+1):
        if len(l[i:j])>=1:
            c=c+1
print(c)
