n=input()
for i in range(len(n)-1):
    for j in range(i+1,len(n)+1):
        if n[i:j]!=n:
            p=n[i:j]
            if int(p,2)%64==0 and p!="0":
                c=0
                break
            else:
                c=1
    if c==0:
        break
if c==0:
    print("yes")
else:
    print("no")
