s,n=map(str,input().split())
n=int(n)
s=list(s)
a=""
for i in range(n):
    s.append(s[0])
    s.remove(s[0])
for i in s:
    a=a+i
    
print(a)
    
