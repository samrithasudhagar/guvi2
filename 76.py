n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
	s=s+i
for i in l:
	if s%2==0:
		if i%2==0:
			print(i)
	else:
		if i%2==1:
			print(i)
