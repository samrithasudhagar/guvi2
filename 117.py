s=input()
for i in range(len(s)-1,-1,-1):
    if i!=0:
        print(s[i],end="-")
    else:
        print(s[i])
