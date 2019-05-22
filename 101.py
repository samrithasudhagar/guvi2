n=int(input())
l=list(map(int,input().split()))
m=0
a=[]
for i in range(n-1):
    if l[i]>l[i+1]:
        a.append(l[i])
    else:
        a.append(l[i+1])
print(sum(a))
        
