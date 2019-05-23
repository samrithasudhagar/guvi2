n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(1,len(l)):
    if l[i]%l[i-1]==0:
        a.append(l[i])
print(*a)        
        
