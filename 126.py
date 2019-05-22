n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[]
for i in l:
    if l.count(i)<k:
        if i not in a:
            a.append(i)
a.sort()
print(*a)
        
