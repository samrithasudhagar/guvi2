n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
	if i<n:
		p.append(i)
p.sort()
print(*p)
