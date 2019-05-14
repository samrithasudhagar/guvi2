n,k=map(int,input().split())
l=list(map(int,input().split()))
s=""
for i in range(0,n-k):
	s=s+str(l[i])+" "
print(s.strip())
