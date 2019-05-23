s,k=map(str,input().split())
k=int(k)
s=list(s)
a=[]
for i in range(k-1,len(s),k):
    s[i]=s[i].upper()
for i in s:
    print(i,end="")
