s=input()
s1=input()
c=0
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if s[i:j]==s1:
            c=c+1
print(c)
