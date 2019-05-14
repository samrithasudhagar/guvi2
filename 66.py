n,k=map(int,input().split())
l=list(map(int,input().split()))
p=[]
for i in range(0,n-1):
	c=1
	for j in range(i+1,n):
		if l[i]==l[j]:
			c+=1
			t=l[j]
	if c==k:
		p.append(t)
print(*p)
