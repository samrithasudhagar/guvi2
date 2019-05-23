a=input()
c=[]
for i in a:
    if i!="a" and i!="b":
        c.append(i)
if all(i=="a" or i=="b" for i in a):
    print("yes")
elif all(i=="a" for i in a):
    print("yes")
elif all(i=="b" for i in a):
    print("yes")
elif len(c)==1:
    print("yes")
else:
    print("no")
