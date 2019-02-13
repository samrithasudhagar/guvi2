n=int(input())
s=""
for i in range(1,n+1):
    if n%i==0 and i%2==1:
        s=s+str(i)+" "
print(s.strip())
