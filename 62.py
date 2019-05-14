n=int(input())
for i in range(1,n+1):
	k=n//i
	if k%2==1 and n%i==0:
		print(i)
		break
	
