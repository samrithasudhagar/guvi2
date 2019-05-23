n,k=map(int,input().split())
p=n|k
o=bin(p)[2:]
print(o.count("1"))
