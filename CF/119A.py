from math import gcd
a,b,n=map(int,input().split())
f=1
while n>0:
    if f==1:
        n-=gcd(n,a)
        ans=0
    else:
        n-=gcd(n,b)
        ans=1
    f*=-1
print(ans)