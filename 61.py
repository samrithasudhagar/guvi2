n,x=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)-1):
	for j in range(i+1,len(l)):
		if l[i]+l[j]==x:
			c=c+1
if c>0:
	print("yes")
else:
	print("no")
