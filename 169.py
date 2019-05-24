s=input()
c=0
a=""
k=s[0]
for i in range(0,len(s)):
    if s[i]==k:
        c=c+1
        if i==len(s)-1:
            a=a+s[i]+str(c)
        
    else:
        a=a+s[i-1]+str(c)
        k=s[i]
        c=1
        if i==len(s)-1:
            a=a+s[i]+str(c)
        

print(a)
