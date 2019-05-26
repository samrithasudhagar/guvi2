n=int(input())
l=list(map(int,input().split()))
if all(l[i]>l[i-1] and l[i]>l[i+1] for i in range(1,len(l)-1,2)) or all(l[i]<l[i-1] and l[i]<l[i+1] for i in range(1,len(l)-1,2)):
    print("yes")
else:
    print("no")
