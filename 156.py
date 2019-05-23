n,k=map(int,input().split())
p=n*k
o=bin(p)[2:]
o=o[::-1]
i=o.index("1")
print(i+1)
