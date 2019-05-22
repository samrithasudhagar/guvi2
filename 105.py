n=int(input())
l=list(map(int,input().split()))
k=sorted(l)
a=[]
for i in k:
    a.append(l.index(i)+1)
print(*a)
    
