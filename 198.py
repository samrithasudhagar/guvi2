n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if l[i]==max(l):
        p=i
        break
for i in range(len(l)):
    if l[i]==min(l):
        q=i
        break
print(abs(p-q))
