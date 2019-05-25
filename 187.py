l=list(map(str,input().split()))
k=len(l[0])
p=len(l[1])
a=[]
for i in range(2,min(k,p)+1):
    if k%i==0 and p%i==0:
        c=0
        break
    else:
        c=1
if c==0:
    print("no")
else:
    print("yes")
