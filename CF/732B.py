st=''

def func():
    if p[0]<c[0]:
        return 'NO'
    for i in range(1,n):
        dp=p[i]-p[i-1]
        dc=c[i]-c[i-1]
        if dp<0 or dc<0 or dc>dp or c[i]>p[i]:
            return 'NO'
    return 'YES'

for _ in range(int(input())):
    n=int(input())
    p,c=[],[]
    for i in range(n):
        a,b=map(int,input().split())
        p.append(a)
        c.append(b)
    st+=str(func())+'\n'
print(st)