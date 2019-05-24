from itertools import permutations
n=input()
k=permutations(n)
for i in max(k):
    print(i,end="")
