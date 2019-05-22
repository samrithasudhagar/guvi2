n=int(input())
l=list(map(int,input().split()))
m=0
for i in range(len(l)-1):
    s=l[i]+l[i+1]
    m=m+s
print(m)
