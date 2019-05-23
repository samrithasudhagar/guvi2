s=input()
c=1
f=1
m=0
for i in range(0,len(s)-1):
    if f==0 and (int(s[i])%2==0 and int(s[i+1])%2==1 or int(s[i])%2==1 and int(s[i+1])%2==0):
        
        c=c+1
        if c>m:
            m=c
    elif (int(s[i])%2==0 and int(s[i+1])%2==0 or int(s[i])%2==1 and int(s[i+1])%2==1) and f==0:
      
    
      
        c=1
        f=1
    elif f==1 and (int(s[i])%2==0 and int(s[i+1])%2==1 or int(s[i])%2==1 and int(s[i+1])%2==0):
       
        c=c+1
        if c>m:
            m=c
        f=0
    else:
        c=1
        f=1
print(m)
