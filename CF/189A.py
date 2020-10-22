c=0
def func(n,l):
    l = sorted(l[1:])
    l1=[]
    for i in l:
        for j in l:
            if i+j not in l1:
                l1.append(i+j)
    f = 1
    while f:
        if n in l1:
            pass


l=list(map(int,input().split()))
n=l[0]
print(func(n,l))