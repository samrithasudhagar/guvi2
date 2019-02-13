n=int(input())
l=list(map(int,input().split()))

min1=min(l)
for i in range(len(l)):
    if min1!=l[i]:
        min2=l[i]
        break
for i in range(1,len(l)):
    if l[i]<min2 and l[i]>min1:
        min2=l[i]
print(min2)
