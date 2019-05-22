s1,s2=map(str,input().split())
if len(s1)==len(s2):
    a=s1
    b=s2
else:
    if len(s1)>len(s2):
        a=s1[:len(s2)]
        b=s2
    else:
        a=s2[:len(s1)]
        b=s1
print(a+b)
