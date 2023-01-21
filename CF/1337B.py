def func(x,n,m):
    while x>20 and n>0:
        x=x//2+10
        n-=1
    if x-10*m>0:
        return 'NO'
    return 'YES'
for _ in range(int(input())):
    x,n,m=map(int,input().split())
    print(func(x,n,m))