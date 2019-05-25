a,b,c=map(int,input().split())
if a==max(a,b,c):
    k=b
    l=c
elif b==max(a,b,c):
    k=a
    l=c
else:
    k=a
    l=b
if max(a,b,c)**2==(k**2)+(l**2):
    print("yes")
else:
    print("no")
