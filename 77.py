n=int(input())
l=list(map(int,input().split()))
f=0
c=1
m=0
for i in range(n-1):
	if l[i]<l[i+1] and f==0 :
		f=1
		c+=1 
		if c>m:
			m=c
	elif l[i]<l[i+1] and f==1:
		c+=1
		if c>m:
			m=c
	elif l[i]>l[i+1] and f==1:
		f=0
		c=1
	else:
		f=0
print(m)
