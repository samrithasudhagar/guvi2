n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
a=[]
for i in range(len(l)-1,-1,-1):
    a.append(l[i])
if a==k:
    print("yes")
else:
    print("no")
