s=input()
c=1
f=1
m=0
xx=["a","e","i","o","u","A","E","I","O","U"]
for i in range(0,len(s)-1):
    if f==0 and (s[i] in xx and s[i+1] not in xx or s[i] not in xx and s[i+1] in xx):
        
        c=c+1
        if c>m:
            m=c
    elif (s[i] in xx and s[i+1] in xx or s[i] not in xx  and s[i+1] not in xx)and f==0:
      
    
      
        c=1
        f=1
    elif f==1 and (s[i] in xx and s[i+1] not in xx or s[i] not in xx and s[i+1] in xx):
       
        c=c+1
        if c>m:
            m=c
        f=0
    else:
        c=1
        f=1
print(m)
