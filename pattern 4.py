n=int(input())
k=0
for i in range(n,0,-1):
     k=k+1
     for j in range(1,i+1):
         print(k,end="")
print()