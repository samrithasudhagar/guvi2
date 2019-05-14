n=int(input())
l=list(map(int,input().split()))
m=0
for i in range(n-1):
	c=1
	for j in range(i+1,i+2):
		if l[i]==l[j]:
			c=c+1
		else:
			c=1
		if c>m:
			m=c
print(m)
