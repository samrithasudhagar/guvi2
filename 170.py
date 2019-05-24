s=input()
p=[]
for i in s:
    p.append(s.count(i))
k=max(p)
out=[]
for i in range(len(p)):
    if p[i]==k:
        o=i
        out.append(s[o])

out=set(out)
print(k,end=" ")
for i in out:
    print(i,end="")
