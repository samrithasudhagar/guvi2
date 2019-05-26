a=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    p.append(l.count(i))
for i in range(len(p)):
    if p[i]==min(p):
        print(l[i])
