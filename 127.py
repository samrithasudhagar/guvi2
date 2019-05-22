s=list(map(str,input().split()))
x=input()
if x in s:
    s.remove(x)
print(*s)
