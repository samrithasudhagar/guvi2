s1,s2=map(str,input().split())
for i in s1:
    for j in s2:
        if i==j:
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
