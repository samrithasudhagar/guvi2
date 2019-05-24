n=int(input())
for i in range(100):
    for j in range(100):
        if (3*i)+(7*j)==n:
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
    
