def catalan(n):
    if n<=1:
        return(1)
    else:
        s=0
        for i in range(n):
            s=s+catalan(i)*catalan(n-i-1)
        return(s)
n=int(input())
a=[]
for i in range(n+1):
    a.append(catalan(i))
print(*a)
