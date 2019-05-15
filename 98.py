n,k=map(str,input().split())
k=int(k)
c=0
if all(str(i) in n for i in range(k+1)):
		c=c+1
if c>0:
	print("yes")
else:
	print("no")
