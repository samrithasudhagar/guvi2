s=input()
a=["a","e","i","o","u"]
k=""
for i in s:
    if i in a:
        k=k+i
for i in s:
    if i not in a:
        k=k+i
print(k)
