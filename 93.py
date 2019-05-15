n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(0,(n-1),2):
	l[i],l[i+1]=l[i+1],l[i]
	k.append(l[i])
	k.append(l[i+1])
if len(l)%2==1:
	k.append(l[-1])
print(*k)
