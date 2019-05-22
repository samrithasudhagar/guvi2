l=list(map(int,input().split("-")))
k=["January","February","March","April","May","June","July","August","September","October","November","December"]
for i in range(len(k)+1):
    if l[1]==i:
       print(k[i-1])
    
