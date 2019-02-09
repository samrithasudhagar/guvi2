n=int(input())
k=""
for i in range(1,n+1):
	for j in range(1,n+1):
		if i*j==n:
			if i%2==0:
				k=k+str(i)+" "
print(k.strip())
