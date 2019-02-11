n=int(input())
l=list(map(int,input().split()))
k=sorted(l)
if k==l:
	print("yes")
else:
	print("no")
