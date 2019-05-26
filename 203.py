n=int(input())
p=[]
for i in range(n):
    p.append(input())
l=[]
q=["a","e","i","o","u","A","E","I","O","U"]

for i in range(n):
    c=0
    for j in p[i]:
        if j in q:
            c+=1
    l.append(c)
v=sorted(l)
ans=[]
for i in v:
    pp=l.index(i)
    ans.append(p[pp])
for i in range(len(ans)-1,-1,-1):
    print(ans[i])
