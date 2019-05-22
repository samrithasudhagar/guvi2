n=int(input())
l=list(map(int,input().split()))
k=list(set(l))
k.sort(reverse=True)
c=[]
a=[]
j=0
for i in k:
    c.append(l.count(i))
while j<len(c)+1:
    for i in range(len(c)):
        if max(c)==c[i] and max(c)!=0:
            a.append(k[i])
            c[i]=0
        j=j+1

print(*a)
