n,l,r=map(int,input().split())
k=list(map(int,input().split()))
k.sort()
for i in k:
    if i>=l and i<=r:
        print(i)
        break
        
