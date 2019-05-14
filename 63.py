n=int(input())
p=[]

l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in l:
	if i in m:
		p.append(i)
k=set(p)
k=list(k)
k=sorted(k)
print(*k)
