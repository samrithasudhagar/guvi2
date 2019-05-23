n=input()
k=""
k=bin(int(n))[2:]
a=k[::-1]
print(a.index("1")+1)
