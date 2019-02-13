n,m=map(int,input().split())
for i in range(n+1):
    for j in range(n+1):
        if 2*(i+j)==n and i*j==m:
            flag=0
            break
        else:
            flag=1
    if flag==0:
        break
if flag==0:
    print("yes")
else:
    print("no")
