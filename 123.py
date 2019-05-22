def prime(n):
    
    c=0
    if n==2:
        return(1)
    else:
        for i in range(2,n):
            if n%i==0:
                c=1
                break
            else:
                c=0
        if c==0:
            return(1)
        else:
            return(0)
        
n=int(input())
a=[]
for i in range(2,n):
    if n%i==0:
        w=prime(i)
        if w==1:
            a.append(i)
a.sort()
print(*a)
           
