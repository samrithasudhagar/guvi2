n=int(input())
l=list(map(int,input().split()))
w=list(map(int,input().split()))
p=sorted(w)
a=[]
for i in p:
    oo=w.index(i)
    a.append(l[oo])
print(*a)
    
