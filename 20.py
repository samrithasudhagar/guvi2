s=input()
a=""
k=""
for i in s:
    if i=="x":
        k="a"
        a=a+k
    elif i=="y":
        k="b"
        a=a+k
    elif i=="z":
        k="c"
        a=a+k
    elif i=="Y":
        k="B"
        a=a+k
    elif i=="Z":
        k="C"
        a=a+k
    elif i=="X":
        k=="A"
    else:
        k=ord(i)+3
        a=a+str(chr(k))
	
print(a)
		

	

