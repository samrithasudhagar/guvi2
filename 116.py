n=int(input())
l=list(map(int,input().split()))
k=list(set(l))
k.sort(reverse=True)
c=[]
a=[]
j=0
for i in k:
    c.append(l.count(i))
while j<len(c):
    f=c.index(max(c))
    a.append(k[f])
    c[f]=0
    j=j+1

print(*a)
    
