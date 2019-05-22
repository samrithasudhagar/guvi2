n=int(input())
l=list(map(int,input().split()))
p=max(l)
for i in range(1,100):
    if all((p*i)%l[j]==0 for j in range(len(l))):
        print((p*i))
        break
