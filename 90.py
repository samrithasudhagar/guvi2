def fact(n):
	c=1
	for i in range(1,n+1):
		c=c*i
	return(c)
n,k=map(int,input().split())
print(fact(n)//(fact(n-k)*fact(k)))
