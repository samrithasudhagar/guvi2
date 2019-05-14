n,k=map(int,input().split())
l=list(map(int,input().split()))
p=[]
for i in l:
	if i<k:
		p.append(i)
p.sort()
print(*p)
