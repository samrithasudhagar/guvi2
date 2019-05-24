s=list(map(str,input().split()))
o=sorted(s[0])
i=sorted(s[1])
k=set(o)
p=set(i)
if k==p:
    print("true")
else:
    print("false")
