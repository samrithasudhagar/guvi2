s=input()
k=""
l=[]
for i in s:
	l.append(s.count(i))
min1=min(l)
for i in range(0,len(l)):
	if l[i]==min1:
		k=k+s[i]
print(k)
