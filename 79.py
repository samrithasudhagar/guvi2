n=int(input())
l=list(map(int,input().split()))
m=0
for i in range(0,n-1):
	for j in range(i+1,n):
		k=l[j]-l[i]
		if k<0:
			k=k*-1
		if k>m:
			m=k
print(m)
		
