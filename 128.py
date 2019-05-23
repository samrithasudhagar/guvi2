n=int(input())
l=list(map(int,input().split()))
c=1
for i in range(n):
    c=c*l[i]
if c%2==0:
    print("even")
else:
    print("odd")
