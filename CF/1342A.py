def func(a,b,x,y):
    m1,m2=min(x,y),max(x,y)
    return( min(m1*b+(m2-m1)*a,a*(m1+m2)))
for _ in range(int(input())):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    print(func(a,b,x,y))
