n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
for i in l:
    if i>k:
        print(i)
        break
