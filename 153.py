s,k=map(str,input().split())
k=int(k)
a=[]
for i in range(k-1,len(s),k):
    a.append(s[i])
print(*a)
