s=input()
p=""
for i in s:
    if s.count(i)>1:
        p=p+i.upper()
    else:
        p=p+i
print(p)
