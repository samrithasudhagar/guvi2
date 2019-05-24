s=input()
a=[]
for i in range(0,len(s)-1,2):
    a.append(int(s[i+1])*s[i])
for i in a:
    print(i,end="")
    
