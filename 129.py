n=int(input())
l=list(map(int,input().split()))
if all(i>0 for i in l):
    print("0")
else:
    m=10000
    for i in range(0,n):
        for j in range(i+1,n+1):
            if sum(l[i:j+1])<m:
                m=sum(l[i:j+1])
    print(m)
            
