l=list(map(str,input().split()))
m=""
for i in l:
    if len(i)>len(m):
        m=i
for i in l:
    if m==i:
        print(i)
        break
    
