n=int(input())
li=[]
while n>0:
	r=n%10
	li.append(r)
	n=n//10
sum=li[0]+li[-1]
print(sum)
