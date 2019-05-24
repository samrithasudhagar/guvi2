l=list(map(str,input().split()))
for i in range(1,len(l)-1):
    if l[i]=="and":
        l[i-1],l[i+1]=l[i+1],l[i-1]
print(*l)
