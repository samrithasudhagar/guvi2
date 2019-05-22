n=int(input())
l=list(map(int,input().split()))
p=max(l)
for i in range(len(l)-1):
    if all(l[j]%l[i]==0 for j in range(i+1,len(l))):
           print(l[i])
           break
