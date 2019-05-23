n=int(input())
l=[]
for i in range(n):
    l.append(input())
if all(l[i]!=l[i+1] for i in range(len(l)-1)):
    print("no")
else:
    print("yes")
