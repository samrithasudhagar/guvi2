l=list(map(str,input().split()))
for i in range(1,len(l)):
    if i!=len(l)-1:
               l[i]=l[i][::-1]
print(*l)
