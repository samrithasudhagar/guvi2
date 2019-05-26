n=input()
if all(i<="9" or i<="F" for i in n):
    print("yes")
else:
    print("no")
