st=''
from bisect import bisect_left
def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    return i

def func():
    l.sort()
    ind=find_ge(l,x)
    s=sum(l[ind:])
    i=ind-1
    c=n-ind
    while i>-1:
        if (s+l[i])/(c+1)<x:
            break
        else:
            s+=l[i]
            i-=1
            c+=1
    return c

for _ in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    st+=str(func())+'\n'
print(st)