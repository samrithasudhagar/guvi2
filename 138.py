n=int(input())
for i in range(100):
    if (2**i)==n:
        c=0
        break
    else:
        c=1
if c==0:
    print("yes")
else:
    print("no")
