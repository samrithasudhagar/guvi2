s=input()
a=input()
p=[]
if s.isdigit()==False and a.isdigit()==False:
    s=s.split()
    a=a.split()
for i in s:
    if i not in a:
        p.append(i)
    elif s.count(i)!=a.count(i):
        p.append(i)
for i in a:
    if i not in s:
        p.append(i)
    elif a.count(i)!=s.count(i):
        p.append(i)
p=set(p)
print(*p)
