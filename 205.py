n=input()
p=""
for i in n:
    if i.isupper():
        p=p+i.lower()
    else:
        p=p+i.upper()
print(p)
    
