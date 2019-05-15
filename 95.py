n,p,k=map(int,input().split())
li=[]
s=[]
while n>0:
	r=n%10
	li.append(r)
	n=n//10
for i in range(len(li)-1,-1,-1):
	s.append(li[i])

t=s[p+k-1]
print(t)
