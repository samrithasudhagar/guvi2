s=input()
k=0
for i in s:
    if i!=" ":
        k=k+1
    
for i in range(2,k):
    if k%i==0:
        c=0
        break
    else:
        c=1
if c==1:
    print("yes")
else:
    print("no")
