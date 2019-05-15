n=int(input())
s=[]
c=0
while n>0:
	r=n%10
	if r not in s:
		s.append(r)
		
	else:
		c=c+1
	n=n//10
if c!=0:
	print("yes")
else:
	print("no")
