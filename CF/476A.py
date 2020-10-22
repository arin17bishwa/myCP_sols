n,m=map(int,input().split())
q=n//2+n%2
if q%m!=0:
    q=q+(m-(q%m))
if q>n or m>n:
    print(-1)
else:
    print(q)