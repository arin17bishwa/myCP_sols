from math import sqrt
n,x=map(int,input().split())
ans=0
for i in range(1,n+1):
    if x%i==0 and x//i<=n:
        #print(i,x//i)
        ans+=1
print(ans)